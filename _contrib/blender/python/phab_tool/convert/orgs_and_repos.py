from collections import defaultdict
from functools import partial, lru_cache
from typing import Iterable
import logging

from phab_tool import gitea
from phab_tool.gitea_api.api import organization_api
from phab_tool.gitea_api.models import Organization, CreateOrgOption

from .. import common
from . import paths, gitea_types, gitea_projects, projects

# These will be replaced with the actual on-the-server organisations of the same
# name, by ensure_orgs(). Not super important, as they are referred to by name
# anyway (and not some database ID that may change).
ORGS = [
    Organization(
        name="blender",
        username="blender",
        full_name="Blender",
        description="Blender Foundation",
        repo_admin_change_team_access=True,
        visibility="public",
    ),
    Organization(
        name="studio",
        username="studio",
        full_name="Blender Studio",
        description="Projects created, managed, or used by Blender Studio",
        repo_admin_change_team_access=True,
        visibility="public",
    ),
    Organization(
        name="archive",
        username="archive",
        full_name="Archived projects",
        description="Archived projects.",
        repo_admin_change_team_access=True,
        visibility="public",
    ),
    Organization(
        name="infrastructure",
        username="infrastructure",
        full_name="Infrastructural projects",
        description="www, devfund, buildbot, gitea, etc.",
        repo_admin_change_team_access=True,
        visibility="public",
    ),
]

# Mapping from organization name to its repositories.
# These repositories are NOT created here, as they may not already exist when we
# run `gitea restore_repo` on them. The info here is used to create the
# `repo.yml` for them (and maybe other things too).

bRepo = partial(gitea_types.Repository, owner="blender")
sRepo = partial(gitea_types.Repository, owner="studio")
aRepo = partial(gitea_types.Repository, owner="archive")
iRepo = partial(gitea_types.Repository, owner="infrastructure")
REPOS = {
    "blender": [
        bRepo(name="blender-app-templates", description="Blender app templates"),
        bRepo(name="blender-asset-tracer", description="Blender Asset Tracer"),
        bRepo(name="blender-translations", description="Blender translations"),
        bRepo(name="blender-dev-tools", description="Blender developer tools"),
        bRepo(name="blender-file", description="Blender-File"),
        bRepo(
            name="blender-package-manager-addon",
            description="Blender package manager add-on",
        ),
        bRepo(name="blender-staging", description="Staging fork of Blender"),
        bRepo(name="cycles", description="Cycles"),
        bRepo(name="libmv", description="Libmv"),
        bRepo(name="oss-attribution-builder", description="Oss-Attribution-Builder"),
        bRepo(name="documentation", description="Documentation of Blender"),
        bRepo(
            name="scons",
            description="Mirror of SCons which is used as submodule for Blender repository",
        ),
        bRepo(name="blender-addons-contrib", description="Unofficial Blender add-ons"),
        bRepo(name="blender-addons", description="Blender add-ons"),
        bRepo(name="blender", description="Blender"),
    ],
    "infrastructure": [
        iRepo(name="blender-benchmark-bundle", description="Blender Benchmark Bundle"),
        iRepo(name="blender-buildbot-www", description="Blender Buildbot Www"),
        iRepo(name="blender-buildbot", description="Blender Buildbot"),
        iRepo(name="blender-conference", description="Blender Conference"),
        iRepo(name="blender-dev-fund", description="Blender development fund"),
        iRepo(
            name="blender-extensions-platform",
            description="Blender Extensions platform",
        ),
        iRepo(name="blender-id-addon", description="Blender ID add-on"),
        iRepo(name="blender-id", description="Blender ID"),
        iRepo(name="blender-open-data", description="Open Data"),
        iRepo(name="blender-org", description="Blender-org"),
        iRepo(name="blender-store", description="Blender-store"),
        iRepo(name="blender-web-assets", description="Blender-web-assets"),
        iRepo(name="looper", description="Looper"),
        iRepo(name="phabricator", description="Phabricator"),
    ],
    "studio": [
        sRepo(name="blender-studio-tools", description="Blender-studio-tools"),
        sRepo(name="blender-studio", description="Blender-studio"),
        sRepo(name="flamenco", description="Flamenco", defaultbranch="main"),
    ],
    "archive": [
        aRepo(name="attract", description="Attract"),
        aRepo(name="blender-cloud-addon", description="Blender Cloud add-on"),
        aRepo(name="blender-asset-manager", description="Blender Asset Manager"),
        aRepo(name="blender-cloud", description="Blender Cloud"),
        aRepo(name="blender-institute", description="Blender-institute"),
        aRepo(name="flamenco-manager", description="Flamenco-manager"),
        aRepo(name="flamenco-worker", description="Flamenco-worker"),
        aRepo(name="pillar-python-sdk", description="Pillar-python-sdk"),
        aRepo(name="pillar-svnman", description="Pillar-svnman"),
        aRepo(name="pillar", description="Pillar"),
        aRepo(name="blender-bfct", description="Blender-BFCT"),
        aRepo(name="blender-my-data", description="My Data"),
    ],
}

# Just update the clone_url for all at once.
svn_repos = {"documentation", "blender-asset-manager"}
for org_name, org_repos in REPOS.items():
    for repo in org_repos:
        repo.construct_original_url()
        if repo.name in svn_repos:
            continue
        if repo.clone_url:
            continue
        repo.clone_url = f"git://git.blender.org/{repo.name}.git"


# Mapping from PHID-REPO to Gitea repository.
# Used for mapping a PHID-COMMIT to commit in a specific Gitea repository.
repo_phid_to_gitea: dict[str, str] = {
    "PHID-REPO-rkl3q4432o3i7qtslwjh": "archive/attract",
    "PHID-REPO-gsfnlui5uaftm66dfr3p": "archive/blender-asset-manager",
    "PHID-REPO-e4iqbh6brod7umxjwlty": "archive/blender-bfct",
    "PHID-REPO-cawf6esn2c6ouwtzdhzk": "archive/blender-cloud",
    "PHID-REPO-vtlagl6uaaf5ipiaka7w": "archive/blender-cloud-addon",
    "PHID-REPO-rwtj7f3pguceoikhcy6t": "archive/blender-institute",
    "PHID-REPO-skb7pebkckam6bc6y55r": "archive/blender-my-data",
    "PHID-REPO-dgky7weio5jagcgq7ty7": "archive/flamenco-manager",
    "PHID-REPO-3o6ostg72cqmlt4c6tkp": "archive/flamenco-worker",
    "PHID-REPO-ikmpd4wivrv34tpb37ko": "archive/pillar",
    "PHID-REPO-k6v2snvisa3celichwwu": "archive/pillar-python-sdk",
    "PHID-REPO-unto55chjwp54sqkmn3d": "archive/pillar-svnman",
    "PHID-REPO-sqcyoemwnp7xafywvps3": "archive/scons",
    "PHID-REPO-jecxaju7eq2vibswb3st": "blender/blender",
    "PHID-REPO-pfxtx23pyhjzjmzwhz7n": "blender/blender-addons",
    "PHID-REPO-rnno3dbsjto7jmtgk43l": "blender/blender-addons-contrib",
    "PHID-REPO-oszum6evzepj4slw3emy": "blender/blender-app-templates",
    "PHID-REPO-3ihrkoffr77rcwjn46am": "blender/blender-asset-tracer",
    "PHID-REPO-sm6n64fxlcgkssuulkeg": "blender/blender-dev-tools",
    "PHID-REPO-vl4qdbdtbpnfontjd4av": "blender/blender-file",
    "PHID-REPO-hwmeghje5sa3yhhgkhhh": "blender/blender-package-manager-addon",
    "PHID-REPO-anv5w6hl5fmcgcodtacv": "blender/blender-staging",
    "PHID-REPO-ku2q7bqxws7sycseo3ik": "blender/blender-translations",
    "PHID-REPO-oefx3zq3mibmv3pwymsm": "blender/blender-translations",
    "PHID-REPO-ay2qj4ol2flttkouzze5": "blender/cycles",
    "PHID-REPO-exbkht6xac5mkdim4rjw": "blender/documentation",
    "PHID-REPO-m6omyio7zcyrjveafajk": "blender/documentation",
    "PHID-REPO-6dju2kzbr5vhyyyhvxff": "blender/libmv",
    "PHID-REPO-6twkopl4idbz5omisiwm": "blender/oss-attribition-builder",
    "PHID-REPO-vbwpl34sdkfkkanrw4wg": "blender/oss-attribution-builder",
    "PHID-REPO-5wuxdw7dbe4ttpedvjt3": "infrastructure/blender-benchmark-bundle",
    "PHID-REPO-cwtgg4oih5winkm2iv2b": "infrastructure/blender-buildbot",
    "PHID-REPO-ow3b3yycmmmyeyim3zop": "infrastructure/blender-buildbot-www",
    "PHID-REPO-pxhcqpgk6sjticcacybr": "infrastructure/blender-conference",
    "PHID-REPO-f3xyd2cbme5ep2jkwrvk": "infrastructure/blender-dev-fund",
    "PHID-REPO-k4qq3ah43vvd4vollkks": "infrastructure/blender-extensions-platform",
    "PHID-REPO-7roro4f6dy2kmlb4ugy7": "infrastructure/blender-id",
    "PHID-REPO-jqpus5x3izqmz3ksxgrx": "infrastructure/blender-id-addon",
    "PHID-REPO-jadv67emnd42ikdptuyc": "infrastructure/blender-open-data",
    "PHID-REPO-ufcixsddv3swparvonw3": "infrastructure/blender-org",
    "PHID-REPO-5yizzsaknpb7kypngrwn": "infrastructure/blender-store",
    "PHID-REPO-xhkghtjqykbf6kkiybl5": "infrastructure/blender-web-assets",
    "PHID-REPO-r3pzqmivduvjc223tehc": "infrastructure/looper",
    "PHID-REPO-c4uxxh4hmqaw2vjhrgnt": "infrastructure/phabricator",
    "PHID-REPO-q32i5qqyv2yokynxja7u": "studio/blender-studio",
    "PHID-REPO-ct4vwyem7zqvaezoq4dc": "studio/blender-studio-tools",
    "PHID-REPO-5lwg6xpzomfafewstv3c": "studio/flamenco",
}


log = logging.getLogger(__name__)


class LabelGatherer:
    """Collect labels per repository, and write to its label.yml."""

    # Mapping from label name (case-insensitive) to label color.
    # NOTE: the name in the `_colors` dict MUST be lower-case!
    # Colors must be 6-digit RRGGBB HTML codes (without leading #);
    _default_color = "474747"
    _colors: dict[str, str] = {
        "type::bug": "505862",
        "type::design": "505862",
        "type::known issue": "505862",
        "type::patch": "505862",
        "type::todo": "505862",
        "status::archived": "474747",
        "status::confirmed": "437045",
        "status::duplicate": "474747",
        "status::needs information from developers": "2d5086",
        "status::needs information from user": "2d5086",
        "status::needs triage": "5e4785",
        "status::resolved": "474747",
        "priority::high": "813131",
        "priority::medium": "474747",
        "priority::low": "474747",
        "migration/requires-manual-verification": "57a57a",
    }

    def __init__(self) -> None:
        self._labels: dict[str, set[str]] = defaultdict(set)
        """Mapping from repository name to its label names."""
        self._add_blender_module_labels()

    def remember(self, repository_name: str, labels: set[str]) -> None:
        """Remember that this set of labels was used in this repository."""
        self._labels[repository_name].update(labels)

    def items(self) -> Iterable[tuple[str, list[gitea_types.Label]]]:
        """Generator, yields (repo name, labels used) tuples."""

        for repo_name, label_names in self._labels.items():
            labels = []
            for name in sorted(label_names):
                color = self._colors.get(name.lower(), self._default_color)
                labels.append(gitea_types.Label(name, color, ""))
            yield repo_name, labels

    def _add_blender_module_labels(self):
        """Add scoped labels for Blender modules.

        These always need to be there, regardless of whether they're referenced or not.
        """
        labels = projects.scoped_module_labels()
        self.remember("blender", labels)


def ensure_orgs_on_gitea():
    """Ensure the configured organisations exist.

    Doesn't touch already-existing ones, doesn't delete unknown ones.
    """

    log.info("Ensuring all %d organisations exist", len(ORGS))

    client = gitea.api_client()
    orgAPI = organization_api.OrganizationApi(client)

    existing_orgs: list[Organization] = orgAPI.org_get_all()
    existing_by_name = {org.name: org for org in existing_orgs}

    for org_idx, org in enumerate(ORGS):
        try:
            ORGS[org_idx] = existing_by_name[org.name]
        except KeyError:
            pass  # This is fine, we'll create it.
        else:
            log.debug("Organisation %s already exists", org.name)
            continue

        log.info("Creating organisation %s", org.name)
        to_create = CreateOrgOption(**org.to_dict())
        created: Organization = orgAPI.org_create(to_create)
        ORGS[org_idx] = created
        log.debug("Created %s", created.name)


def create_repo_dirs_for_conversion():
    """Create org/repo directories, and write some repo-wide YAML files there for Gitea."""

    log.info("Creating conversion dirs for orgs & repos")
    for org_name, org_repos in REPOS.items():
        org_path = paths.for_org(org_name)
        org_path.mkdir(parents=True, exist_ok=True)

        for repo in org_repos:
            repo_path = paths.for_repo(org_name, repo.name)
            repo_path.mkdir(parents=True, exist_ok=True)

            yaml_path = repo_path / "repo.yml"
            log.debug("Writing %s", yaml_path)
            common.saveYamlFile(repo, yaml_path)

            if repo.name == "blender":
                gitea_projects.write_to_yaml(repo_path / "project.yml")


@lru_cache()
def repo_by_name(name: str) -> gitea_types.Repository:
    for org_repos in REPOS.values():
        for repo in org_repos:
            if repo.name == name:
                return repo

    raise ValueError(f"no such repository '{name}'")
