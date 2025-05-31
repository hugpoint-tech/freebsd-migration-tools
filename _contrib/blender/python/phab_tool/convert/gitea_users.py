import concurrent.futures
import datetime
import functools
import logging
import pprint
import os
import re
import time
import threading
from dataclasses import dataclass
from typing import Any, Optional

import unidecode

from . import tracability, blender_id, user_mapping
from .. import users as pt_users
from .. import common, gitea

from phab_tool.gitea_api.api import admin_api
from phab_tool.gitea_api import ApiClient
from phab_tool.gitea_api import models as api_models
import phab_tool.gitea_api.exceptions as api_exceptions

_log = logging.getLogger(__name__)

user_lookup = tracability.UserIDTracer.load()
"""Tool to convert PHID-USER to Gitea UserID"""


class InvalidUsernameError(BaseException):
    pass


class InvalidEmailError(BaseException):
    pass


class UsernameAlreadyUsedError(BaseException):
    def __init__(self, username: str) -> None:
        super().__init__()
        self.username = username


@dataclass
class CreateUserOption:
    # Fields from api_models.CreateUserOption that we actually use:
    email: str
    password: str
    username: str
    created_at: datetime.datetime
    full_name: str
    login_name: str
    source_id: int
    visibility: str

    # Our extensions for migration use:
    phid: str
    """Phabricator UserID PHID-USER-xxx"""
    phab_is_admin: bool
    """Whether this user is an admin on Phabricator."""
    phab_is_disabled: bool
    """Whether this user is disabled on Phabricator."""

    # Fields from api_models.CreateUserOption that are never changed:
    must_change_password: bool = False
    restricted: bool = False
    send_notify: bool = False

    def api_create_option(self) -> api_models.CreateUserOption:
        opt: api_models.CreateUserOption = api_models.CreateUserOption(
            email=self.email,
            password=self.password,
            username=self.username,
            created_at=self.created_at,
            full_name=self.full_name,
            login_name=self.login_name,
            source_id=self.source_id,
            visibility=self.visibility,
            must_change_password=self.must_change_password,
            restricted=self.restricted,
            send_notify=self.send_notify,
        )
        return opt

    def api_edit_option(self) -> api_models.EditUserOption:
        opt: api_models.EditUserOption = api_models.EditUserOption(
            login_name=self.login_name,
            source_id=self.source_id,
            prohibit_login=self.phab_is_disabled,
            admin=self.phab_is_admin,
        )
        return opt


def create_at_gitea(_phab: object) -> None:
    num_cpus = os.cpu_count()
    if num_cpus:
        # Leave about 33% CPU power to Gitea.
        num_workers = int(round(num_cpus * 2 / 3))
    else:
        raise SystemExit("how many CPUs do you have?")

    user_id_tracer = tracability.UserIDTracer.load()

    client = gitea.api_client()
    _log.info("Fetching complete user list from Gitea. This may take a while.")
    gitea_users = _gitea_user_list(client)
    _log.info("Found %d users on Gitea", len(gitea_users))

    gitea_users_by_email = {user.email.lower(): user for user in gitea_users}

    phab_phids_invalid_usernames: dict[str, str] = dict()
    phab_phids_invalid_emails: dict[str, str] = dict()

    num_users_without_email = 0
    num_users_created = 0
    num_users_already_existing = 0

    phab_users = list(pt_users.iter_users())
    phab_users.sort(key=lambda u: u["fields"]["dateCreated"])
    phab_users_sanity_checks(phab_users)

    mutex = threading.Lock()
    threadlocal = threading.local()
    threadlocal.client = None

    # Start with an empty mapping. The rest of the code isn't dealing with
    # midway-aborted user creation very well either.
    user_map = user_mapping.MappedUserTracer()

    def _creation_thread(phab_user: dict[str, Any]) -> None:
        nonlocal num_users_created

        if getattr(threadlocal, "client", None) is None:
            threadlocal.client = gitea.new_api_client()
        client = threadlocal.client

        create_option = _phab_to_create_option(phab_user)
        if not create_option:
            return

        user_phid = create_option.phid
        original_username = create_option.username

        # Create a user on Gitea.
        gitea_user: Optional[api_models.User] = None
        max_attempts = 10
        for attempt_num in range(max_attempts):
            _log.debug(
                "Creating user %s: %s / %s (attempt #%d)",
                user_phid,
                create_option.username,
                create_option.email,
                attempt_num + 1,
            )

            try:
                gitea_user = _create_gitea_user(client, create_option)
            except InvalidEmailError as ex:
                _log.warning("User %s has invalid email: %s", user_phid, ex)

                # Can't do anything with this, so remember this one and skip this user's creation.
                with mutex:
                    phab_phids_invalid_emails[user_phid] = create_option.email
                return
            except InvalidUsernameError as ex:
                _log.warning(
                    "User %s has invalid username %r: %s",
                    user_phid,
                    create_option.username,
                    ex,
                )

                if attempt_num < 2:
                    # These are gitealized usernames from Blender ID or Phabricator.
                    # Give it another attempt when we add a digit at the end, to see
                    # if that resolves things.
                    pass
                else:
                    # Changing digits likely won't help now.
                    # Remember this one and skip this user's creation.
                    with mutex:
                        phab_phids_invalid_usernames[user_phid] = create_option.username
                    return
            except UsernameAlreadyUsedError as ex:
                # This we can handle. Time to try another one in the next iteration.
                _log.info(
                    "User %s username %r has already been taken, going to try another one (this was attempt %d)",
                    user_phid,
                    create_option.username,
                    attempt_num + 1,
                )
            else:
                # User creation OK!
                break

            # Construct a new username to try for the next iteration.
            match attempt_num:
                case 0:
                    # First attempt, which used the gitealized Blender ID nickname.
                    # If that's already taken, try the Phabricator username next.
                    phab_username = phab_user["fields"]["username"]
                    new_username = gitealize_username(phab_username)
                    assert new_username is not None
                    create_option.username = new_username
                case _:
                    # Phabricator username was also not accepted, so go back to
                    # the Blender ID username and see if we can add digits.
                    create_option.username = f"{original_username}{attempt_num}"

        if not gitea_user:
            raise RuntimeError(
                f"Unable to create a Gitea user for {phab_user} after {max_attempts} attempts"
            )

        # Remember all the info about this user.
        blid_user: Optional[blender_id.User] = blender_id.find_user(create_option.email)
        userinfo = user_mapping.UserInfo(
            email=create_option.email,
            full_name=create_option.full_name,
            bid_id=blid_user.bid_id if blid_user else 0,
            bid_nickname=blid_user.bid_nickname if blid_user else "",
            phab_phid=phab_user["phid"],
            phab_username=phab_user["fields"]["username"],
            gitea_userid=gitea_user.id,
            gitea_username=create_option.username,
        )
        user_map.remember(userinfo)

        with mutex:
            user_id_tracer.add(user_phid, gitea_user.id)
            num_users_created += 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as pool:
        try:
            futures = []
            for phab_user in common.timed_iter(_log, phab_users):
                phid = phab_user["phid"]
                email = phab_user["_email"]

                # No email, no user.
                if not email:
                    num_users_without_email += 1
                    continue

                # Check for existing Gitea users.
                with mutex:
                    try:
                        gitea_user = gitea_users_by_email[email.lower()]
                    except KeyError:
                        pass
                    else:
                        _log.debug(
                            "User %s exists on Gitea as %s / %s",
                            phid,
                            gitea_user.email,
                            gitea_user.username,
                        )
                        try:
                            user_id_tracer.add(phid, gitea_user.id)
                        except ValueError as ex:
                            raise ValueError(f"{ex} with email {email}") from None
                        num_users_already_existing += 1
                        continue

                future = pool.submit(_creation_thread, phab_user)
                futures.append(future)

            _log.info("Threads have been scheduled, waiting for results")
            for fut in common.timed_iter(_log, futures):
                fut.result()
        except KeyboardInterrupt:
            _log.error("Aborting on Ctrl+C")
            pool.shutdown(cancel_futures=True)
        except Exception:
            _log.exception(f"Aborting on exception")
            pool.shutdown(cancel_futures=True)

    try:
        user_map.save()
    except Exception:
        _log.exception("Exception saving user mapping")

    try:
        user_id_tracer.save()
    except Exception:
        _log.exception("Exception saving user ID mapping")

    if phab_phids_invalid_usernames:
        _log.info(
            "Could not create %d users because of invalid usernames:\n%s",
            len(phab_phids_invalid_usernames),
            pprint.pformat(phab_phids_invalid_usernames),
        )
    if phab_phids_invalid_emails:
        _log.info(
            "Could not create %d users because of invalid email addresses:\n%s",
            len(phab_phids_invalid_emails),
            pprint.pformat(phab_phids_invalid_emails),
        )
    _log.info("Skipped %d users without email", num_users_without_email)
    _log.info("Skipped %d users already existing on Gitea", num_users_already_existing)
    _log.info("Created %d users", num_users_created)


def _gitea_user_list(client: ApiClient) -> list[api_models.User]:
    """Query Gitea for all its users."""
    adminAPI = admin_api.AdminApi(client)
    users: list[api_models.User] = adminAPI.admin_get_all_users()
    return users


def _phab_to_create_option(phab_user: dict[str, Any]) -> Optional[CreateUserOption]:
    """Create Gitea CreateUserOption for a Phabricator user."""

    # Phab roles are {'verified', 'activated', 'admin', 'approved', 'disabled'}
    phab_roles: set[str] = set(phab_user["fields"]["roles"])
    is_disabled = "disabled" in phab_roles
    is_active = "activated" in phab_roles and not is_disabled
    phab_username = phab_user["fields"]["username"]

    if is_disabled and "spam" in phab_user["fields"]["realName"].lower():
        # Don't bother porting spam users.
        _log.debug("Skipping spam user %s", phab_username)
        return None

    email = phab_user["_email"]
    if not email:
        # # There are users without email address. Let's give them one.
        # email = f"noreply+phabricator-migrated-{phab_user['id']}@blackhole.blender.org"
        return None

    gitea_username = _construct_plausible_gitea_username(email, phab_username)
    bid_login = _find_blenderid_userid(email, phab_username)

    create_option = CreateUserOption(
        email=email,
        password=pt_users.random_password(),
        username=gitea_username,
        login_name=bid_login,
        full_name=phab_user["fields"]["realName"],
        visibility="private" if is_disabled else "public",  # public,limited,private
        created_at=common.parse_timestamp(phab_user["fields"]["dateCreated"]),
        source_id=int(os.environ.get("GITEA_USER_AUTH_SOURCE_ID", "1")),
        phid=phab_user["phid"],
        phab_is_admin=is_active and "admin" in phab_user["fields"]["roles"],
        phab_is_disabled=is_disabled,
    )
    return create_option


def _construct_plausible_gitea_username(email: str, phab_username: str) -> str:
    blid_user: Optional[blender_id.User] = blender_id.find_user(email)
    if not blid_user:
        # This shouldn't happen at the final migration, but could happen while developing.
        gitea_username = gitealize_username(f"{phab_username}-{time.monotonic_ns()}")
        _log.debug(
            "No Blender ID for user email=%r, phab_username=%r", email, phab_username
        )
    else:
        gitea_username = gitealize_username(blid_user.bid_nickname)

    assert isinstance(gitea_username, str), f"expected str, got {gitea_username!r}"
    return gitea_username


def _find_blenderid_userid(email: str, phab_username: str) -> str:
    blid_user: Optional[blender_id.User] = blender_id.find_user(email)
    if not blid_user:
        # This shouldn't happen at the final migration, but could happen while developing.
        return f"no-blender-id-{phab_username}"
    return str(blid_user.bid_id)


def _create_gitea_user(
    client: ApiClient,
    create_option: CreateUserOption,
) -> api_models.User:

    adminAPI = admin_api.AdminApi(client)
    api_create_option = create_option.api_create_option()

    try:
        # This call returns the Gitea user, which SHOULD be the authoritative
        # source of the username from now on. HOWEVER, for some reason the
        # Python API code can transform usernames into other types. Yes, there
        # is someone with a 'dd-mm-yyyy' username, and yes that gets turned into
        # a `datetime.date` object. This is why below `create_option.username`
        # is used, instead of some property of the user returned by the
        # `admin_create_user()` call here.
        adminAPI.admin_create_user(body=api_create_option)
    except api_exceptions.ApiException as ex:
        if ex.status == 422:  # unprocessable entity
            body = str(ex.body)
            if "invalid username" in body:
                raise InvalidUsernameError(
                    f"{body} with username={create_option.username!r}"
                )
            if "[Username]: MaxSize" in body:
                raise InvalidUsernameError(
                    f"{body} with too long username={create_option.username!r}"
                )
            if "[Email]: Email" in body:
                raise InvalidEmailError(f"{body} with email={create_option.email!r}")
            if "user already exists" in body:
                raise UsernameAlreadyUsedError(create_option.username)
        raise

    try:
        # Some options can only be set by editing, and not when creating.
        edits = create_option.api_edit_option()
        edited_user: api_models.User = adminAPI.admin_edit_user(
            create_option.username, body=edits
        )
    except Exception as ex:
        _log.error(
            "%s exception while creating user, attempting deletion of username=%s",
            type(ex).__qualname__,
            create_option.username,
        )
        try:
            adminAPI.admin_delete_user(create_option.username)
        except api_exceptions.ApiException:
            _log.exception("Unable to delete user %r", create_option.username)
        raise  # Re-raise the original exception.

    return edited_user


def phab_users_sanity_checks(phab_users: list[dict[str, Any]]) -> None:
    # Check Phabricator usernames are unique.
    # TODO: create a "username fixer" that attempts to produce Gitea-compatible
    # usernames, and then check that these are unique.
    phab_usernames: set[str] = set()
    double_usernames: set[str] = set()
    for phab_user in phab_users:
        username = phab_user["fields"]["username"]
        if username in phab_usernames:
            double_usernames.add(username)
        else:
            phab_usernames.add(username)
    if double_usernames:
        raise SystemExit(f"Phabricator has non-unique usernames: {double_usernames}")

    # Check emails are unique:
    phab_emails: set[str] = set()
    double_emails: set[str] = set()
    for phab_user in phab_users:
        email = phab_user["_email"]
        if not email:
            continue
        if email in phab_emails:
            double_emails.add(email)
        else:
            phab_emails.add(email)
    if double_emails:
        raise SystemExit(f"Phabricator has non-unique emails: {double_emails}")


_validUsernamePattern = re.compile(r"^[\da-zA-Z][.\w-]*$")
# No consecutive or trailing non-alphanumeric chars:
_invalidUsernamePattern = re.compile(r"[._-]{2,}|[._-]$")

_invalidCharsPattern = re.compile(r"[^\da-zA-Z.\w-]+")

# Consecutive non-alphanumeric at start:
_cons_prefix = re.compile(r"^[._-]+")
_cons_suffix = re.compile(r"[._-]+$")
_cons_infix = re.compile(r"[._-]{2,}")

# Usernames for which the `gitealize_username()` function doesn't produce a unique result.
# Mapping from Phabricator username to Gitea username.
#
# NOTE: after changing this, be sure to run the unit tests to see that the rules
# still produce unique usernames.
hardcoded_changes = {
    # Exceptions to the automatic rules:
    "-": "dash",  # The cleanup rules would turn "-" into ""
    "Alex-": "Alex2",
    "--MAT--": "MAT1",
    "HAWk_": "HAWk1",
    "jason_": "jason1",
    "Jos__": "Jos2",
    "kira_": "kira1",
    "ME__": "ME2",
    "ndh_": "ndh1",
    "nichod_": "nichod1",
    "nils_": "nils1",
    "ravi_": "ravi1",
    "sentinel__": "sentinel2",
    "tejay_": "tejay1",
    "tizbac_": "tizbac1",
    "Tommy_": "Tommy1",
    "Vlad_": "Vlad1",
    "_Alex_": "Alex3",
    "-Dima": "Dima2",
    "-Erik-": "Erik2",
    "_luc": "luc2",
    "_nils": "nils2",
    ".rhavin": "rhavin2",
    "_Thomas_": "Thomas2",
}

# From models/user/user.go
gitea_reserved_names: set[str] = {
    ".",
    "..",
    ".well-known",
    "admin",
    "api",
    "assets",
    "attachments",
    "avatar",
    "avatars",
    "captcha",
    "commits",
    "debug",
    "error",
    "explore",
    "favicon.ico",
    "ghost",
    "issues",
    "login",
    "manifest.json",
    "metrics",
    "milestones",
    "new",
    "notifications",
    "org",
    "pulls",
    "raw",
    "repo",
    "repo-avatars",
    "robots.txt",
    "search",
    "serviceworker.js",
    "ssh_info",
    "swagger.v1.json",
    "user",
    "v2",
}

# Not yet used, but Gitea has this internally as well:
gitea_reserved_user_patterns = {"*.keys", "*.gpg", "*.rss", "*.atom"}


@functools.cache
def gitealize_username(username: Optional[str]) -> Optional[str]:
    """Convert the Phabricator username to something Gitea might accept.

    This is based on IsValidUsername() in modules/validation/helpers.go

    At the moment of writing this code, these transformations will still produce
    unique usernames. This is enforced ih the `UsernameConversionTest` unit
    test in `tests/test_users.py`.
    """

    # NOTE: after changing this function, be sure to run the unit tests to see
    # that the rules still produce unique usernames.

    if not username:
        return username
    assert isinstance(username, str)

    if username in hardcoded_changes:
        return hardcoded_changes[username]

    # Remove accents and other non-ASCIIness.
    ascii_username: str = unidecode.unidecode(username).strip().replace(" ", "_")

    # It is difficult to find a single pattern that is both readable and effective,
    # but it's easier to use positive and negative checks.
    validMatch = _validUsernamePattern.search(ascii_username)
    invalidMatch = _invalidUsernamePattern.search(ascii_username)
    if (
        validMatch
        and not invalidMatch
        and len(ascii_username) <= 40
        and ascii_username not in gitea_reserved_names
    ):
        return ascii_username

    def replace_prefix(match: re.Match[str]) -> str:
        # Earlier idea to convert an N-character prefix into "N" + the first
        # character of the prefix. Just stripping the invalid prefix turned out
        # to be enough and still produces unique usernames.
        #
        # prefix = match.group()
        # return f"{len(prefix)}{prefix[0]}"
        return ""

    def replace_suffix(match: re.Match[str]) -> str:
        return ""

    def replace_infix(match: re.Match[str]) -> str:
        # Replace repeated non-alphanumerics with the single first character of
        # that repeat, so "user_.-name" becomes "user_name"
        infix = match.group()
        return infix[0]

    def replace_illegals(match: re.Match[str]) -> str:
        return "_"

    new_username = ascii_username
    new_username = _invalidCharsPattern.sub(replace_illegals, new_username)
    new_username = _cons_prefix.sub(replace_prefix, new_username)
    new_username = _cons_suffix.sub(replace_suffix, new_username)
    new_username = _cons_infix.sub(replace_infix, new_username)

    if not new_username:
        # Everything was stripped and nothing was left. Better to keep as-is and
        # just let Gitea bork on it.
        return ascii_username

    if new_username in gitea_reserved_names:
        new_username += "2"

    return new_username[:40]
