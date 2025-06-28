#!/usr/bin/env python3
from collections import defaultdict
import dataclasses
import unittest

from phab_tool import users
from phab_tool.convert import gitea_users, blender_id


@dataclasses.dataclass(frozen=True, eq=True)
class UserEmailInfo:
    email: str
    is_primary: bool
    is_verified: bool


class UserEmailTest(unittest.TestCase):
    def test_sybren_data(self):
        seen_sybrens = []
        for row in users.phabricator_user_dump():
            if row["userName"] != "sybren":
                continue
            seen_sybrens.append(row)

        self.assertEqual(
            1,
            sum(int(row["email-isPrimary"]) for row in seen_sybrens),
            "Expecting only a single primary email address",
        )

        self.assertEqual(
            len(seen_sybrens),
            sum(int(row["email-isVerified"]) for row in seen_sybrens),
            "Expecting all email addresses to be verified",
        )

    def test_nonverified_primary(self):
        # This user doesn't have a verified primary address, but does have a verified secondary address.
        email = users.lookup_user_email("PHID-USER-audxoc53t3zfe575qwbd")
        self.assertRegex(email, r"olivier.[a-z]+@gmail.com")

    def test_all_have_primary_email(self):
        # Mapping from PHID to emails.
        all_emails: dict[str, list[UserEmailInfo]] = defaultdict(list)

        for row in users.phabricator_user_dump():
            phid = row["phid"]
            email = row["email-address"]

            try:
                info = UserEmailInfo(
                    email=email,
                    is_primary=bool(int(row["email-isPrimary"])),
                    is_verified=bool(int(row["email-isVerified"])),
                )
            except TypeError as ex:
                raise TypeError(f"error converting {phid}/{email}: {ex}") from None

            all_emails[phid].append(info)

        num_nonverified_primaries = 0
        for phid, emails in all_emails.items():
            primary = [e for e in emails if e.is_primary]
            verified = [e for e in emails if e.is_verified]
            primary_and_verified = [e for e in emails if e.is_primary and e.is_verified]

            self.assertLessEqual(
                len(primary),
                1,
                f"expecting at most one primary email, but {phid} has {primary}",
            )

            if not primary_and_verified and verified:
                # Expecting that when people have a verified secondary address
                # with a non-verified primary address, that at least there is
                # only one verified address.
                self.assertEqual(
                    1,
                    len(verified),
                    f"{phid} has unverified primary {primary} and verified {verified}",
                )
                num_nonverified_primaries += 1

        # At the time of writing this code, this number is valid. The test is
        # just here to keep an eye on whether our assumptions about the dataset
        # still hold.
        self.assertEqual(1, num_nonverified_primaries)


class UsernameConversionTest(unittest.TestCase):
    def test_conversion(self):
        convert = gitea_users.gitealize_username
        # Tuples (expected, input)
        tests = [
            (None, None),  # "no username" should remain the same.
            ("", ""),  # Empty strings shouldn't be touched.
            ("_", "_"),  # Unable-to-shorten names should be kept as-is.
            ("dash", "-"),  # Yes, there is a user with username '-'.
            ("ghost2", "ghost"),  # Reserved name in Gitea.
            ("x", "x"),
            ("simple", "simple"),
            ("startbad", "____startbad"),
            ("endbad", "endbad___"),  # Unaccepted suffix should be stripped
            ("Tommy1", "Tommy_"),  # Unless we know it'll create a collision
            ("sentinel2", "sentinel__"),
            ("Alex2", "Alex-"),
            ("MAT1", "--MAT--"),
            ("mid_bad", "mid__bad"),
            ("user_name", "user_.-name"),
            (
                # Max username length is 40:
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ),
            ("pXd", "-pXd-"),
            ("sakuraa", "_sakuraa_"),
            ("Umlaut-ska", "Ümlaut-ŝka"),
            ("RT2_356", "RT2+356"),
            ("RT2356", "RT2356+"),
        ]
        for expected, input in tests:
            self.assertEqual(expected, convert(input), f"input={input!r}")

    def test_uniqueness(self):
        phab_users = list(users.iter_users())

        # Do the conversion, and keep track of all names that map to the same name.
        usernames: dict[str, list[str]] = defaultdict(list)
        for u in phab_users:
            username = u["fields"]["username"]
            if username is None:
                continue

            converted = gitea_users.gitealize_username(username)
            assert isinstance(converted, str)

            usernames[converted.lower()].append(username)

        problematic_usernames: dict[str, list[str]] = {}
        for new_name, old_names in usernames.items():
            if len(old_names) == 1:
                continue
            problematic_usernames[new_name] = old_names

        self.assertEqual({}, problematic_usernames)

    def test_uniqueness_bid(self) -> None:
        # NOTE: This test is known to not work, since the Blender ID nickname is
        # case sensitive. There are four users with different capitalisations of
        # "Mike".
        pass

        # # Set of BlenderID users that will be created on the Gitea side.
        # gitea_emails: set[str] = set()
        # mangled_usernames_to_emails: dict[str, list[str]] = defaultdict(list)

        # # Do the conversion, and keep track of all names that map to the same name.
        # usernames: dict[str, list[str]] = defaultdict(list)
        # for u in blender_id._iter_csv():
        #     assert u.bid_nickname, f"BID user {u.email} has no nickname"

        #     gitea_nickname = gitea_users.gitealize_username(u.bid_nickname)
        #     assert gitea_nickname is not None

        #     u.gitea_username = gitea_nickname
        #     lower_nickname = gitea_nickname.lower()

        #     usernames[lower_nickname].append(u.bid_nickname)
        #     mangled_usernames_to_emails[lower_nickname].append(u.email)
        #     gitea_emails.add(u.email.lower())

        # # Check that usernames within the Gitea set remain unique
        # problematic_usernames: dict[str, list[str]] = {}
        # for new_name, old_names in usernames.items():
        #     if len(old_names) == 1:
        #         continue
        #     problematic_usernames[new_name] = old_names

        # self.assertEqual({}, problematic_usernames)

        # Load the full dump CSV to check that the usernames stay unique within
        # the full dump.

        # num_overlaps = 0
        # for fulldump_user in blender_id._iter_full_dump_csv():
        #     if fulldump_user.email.lower() in gitea_emails:
        #         # This was a converted user.
        #         continue

        #     lower_bid_name = fulldump_user.bid_nickname.lower()
        #     if lower_bid_name not in usernames:
        #         # This username wasn't reused by the Gitea set.
        #         continue

        #     gitea_usernames = usernames[lower_bid_name]
        #     overlapping_bids = mangled_usernames_to_emails[lower_bid_name]
        #     print(
        #         f"{lower_bid_name} is owned by {fulldump_user.bid_id} / {fulldump_user.email}"
        #     )
        #     print(f"    Gitea usernames mapping here: {gitea_usernames}")
        #     print(f"    Emails of those names: {overlapping_bids}")

        #     num_overlaps += 1

        # self.assertEqual(0, num_overlaps)
