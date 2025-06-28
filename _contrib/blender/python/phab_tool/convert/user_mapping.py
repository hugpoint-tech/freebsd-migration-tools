import csv
import dataclasses
import datetime
import logging
import threading
from typing import Optional

from . import paths

_log = logging.getLogger(__name__)

_global_map: Optional["MappedUserTracer"] = None
_mutex = threading.Lock()


@dataclasses.dataclass(frozen=True)
class UserInfo:
    """Info about a remapped user.

    This class contains info from Phabricator, Blender ID, and Gitea.
    """

    # Common:
    email: str
    full_name: str

    # Blender ID:
    bid_id: int
    bid_nickname: str

    # Phabricator:
    phab_phid: str
    phab_username: str

    # Gitea:
    gitea_userid: int
    gitea_username: str


class UnkownUserError(Exception):
    pass


class MappedUserTracer:
    """Source of truth when it comes to user info."""

    _by_email: dict[str, UserInfo]
    _by_phid: dict[str, UserInfo]
    _by_phab_username: dict[str, UserInfo]

    def __init__(self) -> None:
        self._by_email = {}
        self._by_phid = {}
        self._by_phab_username = {}
        self._mutex = threading.Lock()

    def remember(self, user: UserInfo) -> None:
        """Remember this user, thread-safe."""
        if not user.email:
            raise ValueError(f"user has empty email, cannot track: {user}")
        if not user.phab_phid:
            raise ValueError(f"user has empty phab_phid, cannot track: {user}")
        if not user.phab_username:
            raise ValueError(f"user has empty phab_username, cannot track: {user}")

        with self._mutex:
            self._remember(user)

    def _remember(self, user: UserInfo) -> None:
        """Thread-unsafe, remember this user."""
        # Convert case-insensitive names to lower case.
        email = user.email.lower()
        phab_username = user.phab_username.lower()

        if email in self._by_email:
            existing = self._by_email[email]
            raise ValueError(f"user email={user.email} already tracked: {existing}")
        if user.phab_phid in self._by_phid:
            existing = self._by_phid[user.phab_phid]
            raise ValueError(f"user phid={user.phab_phid} already tracked: {existing}")
        if phab_username in self._by_phab_username:
            existing = self._by_phab_username[phab_username]
            raise ValueError(
                f"user phab_username={user.phab_username} already tracked: {existing}"
            )

        self._by_email[email] = user
        self._by_phid[user.phab_phid] = user
        self._by_phab_username[phab_username] = user

    def by_email(self, email: str) -> UserInfo:
        with self._mutex:
            return self._by_email[email.lower()]

    def by_phid(self, phid: str) -> UserInfo:
        with self._mutex:
            return self._by_phid[phid]

    def by_phab_username(self, phab_username: str) -> UserInfo:
        with self._mutex:
            return self._by_phab_username[phab_username.lower()]

    def has_data(self) -> bool:
        with self._mutex:
            return bool(self._by_email)

    @classmethod
    def load(cls) -> "MappedUserTracer":
        csv_path = paths.for_user_mapping()

        if not csv_path.exists():
            _log.warning("No user mapping in %s, starting without", csv_path)
            return cls()

        self = cls()
        with csv_path.open("r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                user = UserInfo(
                    email=row["email"],
                    full_name=row["full_name"],
                    bid_id=int(row["bid_id"]),
                    bid_nickname=row["bid_nickname"],
                    phab_phid=row["phab_phid"],
                    phab_username=row["phab_username"],
                    gitea_userid=int(row["gitea_userid"]),
                    gitea_username=row["gitea_username"],
                )
                self._remember(user)
        return self

    def save(self) -> None:
        csv_path = paths.for_user_mapping()

        if not self.has_data():
            _log.error("Refusing to write empty user map to %s", csv_path)
            return

        _log.info(
            "Writing user map of %d users to %s",
            len(self._by_email),
            csv_path,
        )

        if csv_path.exists():
            timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S.%f")
            name = f"{csv_path.stem}-{timestamp}{csv_path.suffix}"
            backup_path = csv_path.with_name(name)
            csv_path.rename(backup_path)

        with self._mutex:
            to_save = [dataclasses.asdict(u) for u in self._by_email.values()]

        with csv_path.open("w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(
                outfile,
                [
                    "email",
                    "full_name",
                    "bid_id",
                    "bid_nickname",
                    "phab_phid",
                    "phab_username",
                    "gitea_userid",
                    "gitea_username",
                ],
            )
            writer.writeheader()
            writer.writerows(to_save)


def by_email(email: str) -> UserInfo:
    _ensure_global_map_loaded()
    assert _global_map is not None
    try:
        return _global_map.by_email(email)
    except KeyError:
        raise UnkownUserError(f"email={email!r}") from None


def by_phid(phid: str) -> UserInfo:
    _ensure_global_map_loaded()
    assert _global_map is not None
    try:
        return _global_map.by_phid(phid)
    except KeyError:
        raise UnkownUserError(f"phid={phid!r}") from None


def has_data() -> bool:
    _ensure_global_map_loaded()
    assert _global_map is not None
    return _global_map.has_data()


def gitea_username(phab_username: str) -> str:
    _ensure_global_map_loaded()
    assert _global_map is not None
    try:
        u = _global_map.by_phab_username(phab_username)
    except KeyError:
        raise UnkownUserError(f"phab_username={phab_username!r}") from None

    return u.gitea_username


def _ensure_global_map_loaded():
    global _global_map

    with _mutex:
        if _global_map is not None:
            return
        _global_map = MappedUserTracer.load()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    u = UserInfo(
        email="email",
        full_name="full_name",
        bid_id=47,
        bid_nickname="bid_nickname",
        phab_phid="phab_phid",
        phab_username="phab_username",
        gitea_userid=327,
        gitea_username="gitea_username",
    )

    t = MappedUserTracer.load()
    t.remember(u)
    t.save()
    t.load()

    print(t.by_email("email"))
    print(t.by_phid("PHID-USER-zl6qyaociyqtbsy7hoop"))
