import csv
import dataclasses
import functools
import logging
import threading
from typing import Iterable, Optional

from .. import common
from .. import users as pt_users
from . import paths, gitea_users, user_mapping


@dataclasses.dataclass
class User:
    """Blender ID user.

    Note that only users who have an active account and have confirmed their
    email address are loaded. The rest is treated as "without Blender ID".
    """

    # See `data/orig/blender_id-users/blender-id.csv`
    # username,full_name,email,phid,bid_email,bid_nickname,bid_id,created
    bid_id: int
    email: str
    full_name: str
    bid_nickname: str
    bid_is_active: bool
    phab_username: str


# Mutex to protect the globals
_mutex = threading.RLock()

# Mapping from lower-cased email to Blender ID user.
_users: dict[str, User] = {}
_full_dump_path = common.orig_dirs["blender-id"] / "blender-id.csv"
_fed_through_bid_path = common.orig_dirs["blender-id"] / "blender-id-imported.csv"
_fed_through_bid_warned_missing = False

# Mapping of Phabricator to Blender ID usernames.
_username_mapping: dict[str, str] = {}

_log = logging.getLogger(__name__)


@functools.cache
def find_user(email: str) -> Optional[User]:
    """Find the Blender ID account with this email address.

    :return: None if not found, or if the email was not verified on
        Blender ID.
    """
    _ensure_users_loaded()
    return _users.get(email.lower())


def _ensure_users_loaded() -> None:
    with _mutex:
        if _users:
            return

        for user in _iter_csv():
            _users[user.email.lower()] = user
            _username_mapping[user.phab_username] = user.bid_nickname


def _iter_csv() -> Iterable[User]:
    """Generator, yields Blender ID users.

    Only yields users that were exported to Blender ID with
    `pt_create_bid_import()`.
    """
    global _fed_through_bid_warned_missing

    if not _fed_through_bid_path.exists():
        if not _fed_through_bid_warned_missing:
            _log.warning(
                "Blender ID user file %s does not exist, going to assume gitealized Phabricator usernames are good enough",
                _fed_through_bid_path,
            )
            _fed_through_bid_warned_missing = True
        return []

    _log.info("Loading Blender ID users from %s", _fed_through_bid_path)

    expected_columns = {
        "username",
        "full_name",
        "email",
        "phid",
        "bid_email",
        "bid_nickname",
        "bid_id",
        "bid_is_active",
        "created",
    }

    with _fed_through_bid_path.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert (
                set(row.keys()) == expected_columns
            ), f"found unexpected columns in {set(row.keys())}"

            if not row["username"]:  # Skip empty lines.
                continue

            user = User(
                bid_id=int(row["bid_id"]),
                email=row["bid_email"],
                full_name=row["full_name"],
                bid_nickname=row["bid_nickname"],
                bid_is_active=row["bid_is_active"] == "True",
                phab_username=row["username"],
            )

            yield user


def _iter_full_dump_csv() -> Iterable[User]:
    """Generator, yields Blender ID users.

    Only yields partial users, from `data/orig/blender_id-users/blender-id.csv`
    """

    _log.info("Loading Blender ID users from %s", _full_dump_path)

    expected_columns = {
        "id",
        "email",
        "full_name",
        "confirmed_email_at",
        "is_staff",
        "is_superuser",
        "is_active",
        "nickname",
    }

    with _full_dump_path.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert (
                set(row.keys()) == expected_columns
            ), f"found unexpected columns in {set(row.keys())}"

            if not row["id"]:  # Skip empty lines.
                continue

            user = User(
                bid_id=int(row["id"]),
                email=row["email"],
                full_name=row["full_name"],
                bid_nickname=row["nickname"],
                bid_is_active=row["is_active"] == "t",
                phab_username="",
            )

            yield user


def pt_create_bid_import(_phab: object) -> None:
    """Export users to BlenderID-importable CSV file."""

    num_users_without_email = 0
    num_users_exported = 0

    phab_users = list(pt_users.iter_users())
    phab_users.sort(key=lambda u: u["fields"]["dateCreated"])
    gitea_users.phab_users_sanity_checks(phab_users)

    csvpath = paths.for_blender_id_user_csv()
    with csvpath.open("w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(
            outfile, fieldnames=["username", "full_name", "email", "phid"]
        )
        writer.writeheader()

        for phab_user in common.timed_iter(_log, phab_users):
            email = phab_user["_email"]

            # No email, no user.
            if not email:
                num_users_without_email += 1
                continue

            # Export to CSV
            row = {
                "username": phab_user["fields"]["username"],
                "full_name": phab_user["fields"]["realName"],
                "email": email,
                "phid": phab_user["phid"],
            }
            writer.writerow(row)
            num_users_exported += 1

    _log.info("Skipped %d users without email", num_users_without_email)
    _log.info("Exported %d users", num_users_exported)
    _log.info("Wrote to %s", csvpath.absolute())
