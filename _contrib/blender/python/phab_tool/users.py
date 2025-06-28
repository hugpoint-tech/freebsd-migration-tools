import csv
import dataclasses
import functools
import logging
import os
from collections import defaultdict
from typing import Optional, Iterator, Any

from phabricator import Phabricator

from . import common
from .convert import user_mapping

# Mapping from PHID to user info.
_users = {}

# Mapping from PHID to the user's email address.
_user_emails: dict[str, str] = {}

log = logging.getLogger(__name__)

# Emails of users without Blender ID account that we've already warned about. To
# avoid warning more than once per account.
_warned_about_users_without_bid: set[str] = set()

_warned_about_unknown_user_phids: set[str] = set()


@dataclasses.dataclass(frozen=True, eq=True)
class BestEffortUser:
    """Best-Effort User.

    Gitea information may not be available for users that haven't been created
    on Gitea yet. Somewhat reasonable fake info will be returned to allow the
    conversion process to continue.
    """

    id: int
    phid: Optional[str]
    username: str
    email: str

    @property
    def gitea_username(self) -> str:
        """Get the Gitea username, falling back to Phabricator username if unknown."""
        if not self.phid:
            return self.username
        try:
            userinfo = user_mapping.by_phid(self.phid)
        except user_mapping.UnkownUserError as ex:
            if (
                user_mapping.has_data()
                and self.phid not in _warned_about_unknown_user_phids
            ):
                log.warning(f"Not-yet-converted user: {ex}")
                _warned_about_unknown_user_phids.add(self.phid)
            return self.username
        return userinfo.gitea_username

    @property
    def gitea_userid(self) -> int:
        if not self.phid:
            return 0
        try:
            userinfo = user_mapping.by_phid(self.phid)
        except user_mapping.UnkownUserError as ex:
            if (
                user_mapping.has_data()
                and self.phid not in _warned_about_unknown_user_phids
            ):
                log.warning(f"Not-yet-converted user: {ex}")
                _warned_about_unknown_user_phids.add(self.phid)
            return 0
        return userinfo.gitea_userid


@dataclasses.dataclass(frozen=True, eq=True)
class UserEmailInfo:
    """Internal class, used to select one email address per user for Gitea."""

    email: str
    is_primary: bool
    is_verified: bool


@functools.lru_cache(maxsize=1000)
def getBestEffortUser(phab: Phabricator, userPhid: str) -> BestEffortUser:
    """Returns best-effort user info with this PHID.

    Gitea info may not be available when this user was not created on Gitea.
    However, calling this function can trigger a download of Phabricator user
    data when new users are referenced.
    """

    user = _lookupUserPhid(phab, userPhid)

    if user.get("id"):  # i.e. if user is not the "deleted" user.
        email = lookup_user_email(userPhid)
    else:
        email = ""

    return BestEffortUser(
        id=user["id"],
        phid=user["phid"],
        username=user["fields"]["username"],
        email=email,
    )


def _saveUserJSON(user_data: dict) -> None:
    phid = user_data["phid"]
    if not phid.startswith("PHID-"):
        raise ValueError(f"{phid!r} is not a valid PHID")

    user_path = common.orig_dirs["user"] / f"{phid}.json"
    common.saveJsonFile(user_data, user_path)


# Returns a Phabricator 'User' struct when given a 'PHID'.
# Uses a cache that gets saved on disk and loaded upon startup.
# Handles deleted users by populating entry with 'empty' data
def _lookupUserPhid(phab: Phabricator, phid: Optional[str]) -> dict:
    if not phid:
        return {
            "id": 0,
            "type": "USER",
            "phid": None,
            "fields": {
                "username": "None",
                "realName": "None",
                "dateCreated": 0,
                "dateModified": 0,
            },
        }

    if not _users:
        loadUserData()

    if not phid.startswith("PHID-"):
        raise ValueError(f"{phid!r} is not a valid PHID")

    if not phid.startswith("PHID-USER-"):
        raise ValueError(f"{phid!r} is not a valid USER PHID")

    try:
        return _users[phid]
    except KeyError:
        pass

    result = phab.user.search(constraints={"phids": [phid]})
    try:
        user_data = result.data[0]
    except IndexError:
        user_data = {
            "id": 0,
            "type": "USER",
            "phid": phid,
            "fields": {
                "username": "(Deleted)",
                "realName": "(Deleted User)",
                "dateCreated": 0,
                "dateMofidied": 0,
            },
        }

    _saveUserJSON(user_data)
    _users[phid] = user_data
    return user_data


def loadUserData() -> None:
    """Populate 'users' cache; used to lookup a user by PHID"""
    log.info("Loading users...")

    users_dir = common.orig_dirs["user"]
    for fpath in users_dir.glob("*.json"):
        try:
            user_data = common.readJsonFile(fpath)
        except Exception as ex:
            log.error(f"Error in {fpath.name}: {ex}")
            continue
        _users[user_data["phid"]] = user_data


def iter_users() -> Iterator[dict[str, Any]]:
    """Iterator, iterates over dumped users."""
    if not _users:
        loadUserData()
    for phid, user in _users.items():
        if not user.get("id"):  # i.e. if user is the "deleted" user.
            continue

        email = lookup_user_email(phid)
        user["_email"] = email
        yield user


def lookup_user_email(user_phid: str) -> str:
    if not user_phid:
        return ""

    if not _user_emails:
        # Mapping from PHID to all the emails.
        all_emails: dict[str, list[UserEmailInfo]] = defaultdict(list)

        for row in phabricator_user_dump():
            phid: str = row["phid"]
            email: str = row["email-address"]

            try:
                info = UserEmailInfo(
                    email=email,
                    is_primary=bool(int(row["email-isPrimary"])),
                    is_verified=bool(int(row["email-isVerified"])),
                )
            except TypeError as ex:
                raise TypeError(f"error converting {phid}/{email}: {ex}") from None

            all_emails[phid].append(info)

        # For each PHID, pick the best email address (primary + verified is
        # preferred, otherwise pick the verified one).
        for phid, emails in all_emails.items():
            verified = [e for e in emails if e.is_verified]
            primary_and_verified = [e for e in emails if e.is_primary and e.is_verified]

            if primary_and_verified:
                assert len(primary_and_verified) == 1
                _user_emails[phid] = primary_and_verified[0].email
                continue

            if verified:
                # Prefer verified addresses over primary addresses.
                _user_emails[phid] = verified[0].email
                continue

            # Don't bother porting over unverified email addresses.

    return _user_emails.get(user_phid) or ""


def phabricator_user_dump() -> Iterator[dict[str, Any]]:
    """Generator, yields rows of `phabricator-user-user_email.tsv`."""

    file_path = common.orig_dirs["user-email"] / "phabricator-user-user_email.tsv"
    log.info("Loading user emails from %s", file_path)

    # TODO: verify that this file is indeed written in Latin-1. It for sure contains invalid UTF-8 sequences.
    with file_path.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t", quotechar="\\")
        # We can't use a dictreader because there are repeating headers, so
        # later columns would overwrite earlier ones.
        for idx, row in enumerate(reader):
            if idx == 0:  # Skip the header.
                continue
            if not row[0]:  # Skip empty lines.
                continue

            assert len(row) >= 18, f"row {idx+1} has {len(row)} items: {row}"

            dict_row = {
                "id": row[0],
                "phid": row[1],
                "userName": row[2],
                "realName": row[3],
                "dateCreated": row[4],
                "dateModified": row[5],
                "isDisabled": row[6],
                "isAdmin": row[7],
                "isEmailVerified": row[8],
                "isApproved": row[9],
                "email-id": row[10],
                "email-userPHID": row[11],
                "email-address": row[12],
                "email-isVerified": row[13],
                "email-isPrimary": row[14],
                "email-dateCreated": row[15],
                "email-dateModified": row[16],
                "email-phid": row[17],
            }
            dict_row["phid"] = dict_row["phid"].strip()

            # Phabricator is wonderful. Some people have newlines in their email address.
            addr: str = dict_row["email-address"] or ""
            dict_row["email-address"] = addr.replace("\n", "").strip()

            yield dict_row


def random_password() -> str:
    """Generate a secure, random password."""
    return os.urandom(16).hex("-", 4)
