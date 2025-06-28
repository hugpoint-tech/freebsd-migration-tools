import functools
import logging
import random
from collections import defaultdict
from typing import Any

from .. import common

_log = logging.getLogger(__name__)

"""Project information.

Projects are identified by their slug, for human readability. The dumper makes
sure these slugs are unique.
"""

# Projects that are Blender modules:
module_projects = {
    "animation_rigging": {
        "pose-library-basics",
    },
    "core": {
        "audio",
        "datablocks_and_libraries",
        "dependency_graph",
        "images_movies",
        "liboverrides-usability-and-ux",
        "overrides",
        "undo",
    },
    "development_management": {},
    "eevee_viewport": {
        "eevee",
        "gpu_viewport",
        "virtual_reality",
    },
    "grease_pencil": {},
    "modeling": {
        "modifiers",
        "uv_editing",
    },
    "nodes_physics": {
        "geometry_nodes",
        "nodes",
        "physics",
        "retrospective",  # sub-project of Geometry Nodes
    },
    "pipeline_assets_i_o": {
        "alembic",
        "asset_browser",
        "asset_browser_archived",
        "asset_browser_project_overview",
        "collada",
        "import_export",
        "usd",
    },
    "platforms_builds_tests_devices": {
        "automated_testing",
        "platform:_freebsd",
        "platform:_linux",
        "platform:_windows",
        "platform_macos",
        "wintab_high_frequency",
    },
    "python_api": {
        "text_editor",
    },
    "render_cycles": {
        "cycles",
        "render_pipeline",
    },
    "sculpt_paint_texture": {},
    "triaging": {},
    "user_interface": {},
    "vfx_video": {
        "compositing",
        "freestyle",
        "line_art",
        "masking",
        "motion_tracking",
        "video_sequencer",
    },
}

# Project slugs that are actually indicative of versions of Blender. They map to
# the Blender version.
blender_milestones: dict[str, str] = {
    "1-0-0-beta-2": "1.0.0-beta2",
    "2-81": "2.81",
    "2-82": "2.82",
    "2-83": "2.83",
    "2-90": "2.90",
    "2-91": "2.91",
    "2-92": "2.92",
    "2-93": "2.93",
    "3-0": "3.0",
    "3-1": "3.1",
    "3-2": "3.2",
    "3-3": "3.3",
    "3-4": "3.4",
    "3-5": "3.5",
    "3-6": "3.6",
    "4-0": "4.0",
    "bf_blender_2.8": "2.8",
    "blender_2.70": "2.70",
}

# Project slugs that indicate the thing belongs to the Blender repo, but don't
# imply a specific module.
blender_slugs: set[str] = {
    "bf_blender:_after_release",
    "bf_blender:_next",
    "bf_blender:_regressions",
    "bf_blender:_unconfirmed",
    "bf_blender",
    "code_quest",
    "game_animation",
    "game_audio",
    "game_data_conversion",
    "game_engine",
    "game_logic",
    "game_physics",
    "game_python",
    "game_rendering",
    "game_ui",
    "milestone-1-basic-local-asset-browser",
    "tracker_curfew",
    "translations",
}

# Mapping from project slug to repository name for non-Blender projects (i.e.
# projects that are not supposed to go into the blender repository).
#
# Repository names can be found in orgs_and_repos.py. There also the relation
# between repositories and organisations is defined.
repositories: dict[str, str] = {
    "add-ons_bf-blender": "blender-addons",
    "add-ons_community": "blender-addons",
    "application_templates": "blender-app-templates",
    "attract_server": "attract",
    "attract": "attract",
    "bf_blender:_staging": "blender-staging",
    "blender_asset_tracer": "blender-asset-tracer",
    "blender_benchmark": "blender-benchmark-bundle",
    "blender_cloud": "blender-cloud",
    "blender_conference": "blender-conference",
    "blender_development_fund": "blender-dev-fund",
    "blender_file": "blender-file",
    "blender_id": "blender-id",
    "blender_open_data": "blender-open-data",
    "blender_studio": "blender-studio",
    "documentation": "documentation",
    "flamenco": "flamenco",
    "infrastructure_blender.org": "blender-org",
    "infrastructure:_blender_buildbot": "blender-buildbot",
    "infrastructure:_blender_foundation_certified_trainers": "blender-bfct",
    "infrastructure:_blender_store": "blender-store",
    "infrastructure:_blender_web_assets": "blender-web-assets",
    "libmv": "libmv",
    "looper": "looper",
    "oss-attribution-builder": "oss-attribution-builder",
    "phabricator": "phabricator",
    "pillar_python_sdk": "pillar-python-sdk",
    "pillar_web": "pillar",
    "pillar_website": "pillar",
    "pillar": "pillar",
    "pillar_framework": "pillar",
}

# List of Blender module names. Used to generate other lists.
blender_modules = [
    "Animation & Rigging",
    "Core",
    "Development Management",
    "EEVEE & Viewport",
    "Grease Pencil",
    "Modeling",
    "Nodes & Physics",
    "Pipeline, Assets & IO",
    "Platforms, Builds Tests & Devices",
    "Python API",
    "Rendering & Cycles",
    "Sculpt, Paint & Texture",
    "Triaging",
    "User Interface",
    "VFX & Video",
]

# Mapping from project slug to a label.
# TODO: These should map to Label objects, like labels_for_task_subtype.
# TODO: visit these to see if we actually want those labels, or want to merge some.
module_label_prefix = "legacy module/"
module_label_scoped_prefix = "Module::"
project_label_prefix = "legacy project/"

labels: dict[str, str] = {
    "good_first_issue": "good first issue",
    "papercut": "papercut",
    "straightforward_issue": "straightforward issue",
    "todo": "todo",
    "performance": "performance",
    "animation_rigging": f"{module_label_prefix}Animation & Rigging",
    "core": f"{module_label_prefix}Core",
    "development_management": f"{module_label_prefix}Development Management",
    "eevee_viewport": f"{module_label_prefix}Eevee & Viewport",
    "grease_pencil": f"{module_label_prefix}Grease Pencil",
    "modeling": f"{module_label_prefix}Modeling",
    "nodes_physics": f"{module_label_prefix}Nodes & Physics",
    "pipeline_assets_i_o": f"{module_label_prefix}Pipeline, Assets & IO",
    "platforms_builds_tests_devices": f"{module_label_prefix}Platforms, Builds, Tests & Devices",
    "python_api": f"{module_label_prefix}Python API",
    "render_cycles": f"{module_label_prefix}Rendering & Cycles",
    "sculpt_paint_texture": f"{module_label_prefix}Sculpt, Paint & Texture",
    "triaging": f"{module_label_prefix}Triaging",
    "user_interface": f"{module_label_prefix}User Interface",
    "vfx_video": f"{module_label_prefix}VFX & Video",
}

# Anything tagged with this will be discarded and not migrated to Gitea.
reject_slugs: set[str] = {
    "blender_asset_manager",  # the Git repo has already been removed, no need to port tasks.
    "moduleexamplepage",
    "spam",
    "spam1",
    "studio_sprite_fright_build",
    "sub-subproject_c_child_of_b",
    "subproject_a_-_renamed_once_again",
    "subproject_b",
    "technical_documentation",  # New project, will be set up from scratch after migration.
    "test_members",
    "test-milestone",
    "test",
}

# Mapping from slug to repository. These are used only when there are no other
# indicators of the repository. For example "flamenco, good_first_issue" will be
# Flamenco, but "good_first_issue" by itself will be Blender.
weak_slugs: dict[str, str] = {
    "good_first_issue": "blender",
    "infrastructure:_websites": "blender-org",
    "opengl_error": "blender",
    "performance": "blender",
}

# Project slugs that should not be converted into a "legacy project" label.
# These typically are the project slugs that get an issue assigned to a
# repository and after that are redundant.
slugs_without_label = {
    "attract",
    "bf_blender:_staging",
    "bf_blender",
    "blender_conference",
    "blender_development_fund",
    "blender_file",
    "blender_id",
    "blender_open_data",
    "blender_studio",
    "flamenco",
    "looper",
}


# These are the leftover slugs. Just here for reference, they're not used for anything.
_ignored_slugs: set[str] = {
    "blender_asset_bundle",
    "gsoc",
    "moderators",
}


def project_slugs(task: dict[str, Any]) -> set[str]:
    """Return the project slugs of this task."""
    task_projects: list[str]
    try:
        task_projects = task["attachments"]["projects"]["projectPHIDs"]
    except KeyError:
        task_projects = []

    phab_projs = phab_project_info()
    slugs = set()
    for proj_phid in task_projects:
        try:
            proj = phab_projs[proj_phid]
        except KeyError:
            _log.error(
                "%s %s has unknown project PHID %s", task["type"], task["id"], proj_phid
            )
            continue
        slugs.add(proj["fields"]["slug"])
    return slugs


def must_reject(project_slugs: set[str]) -> bool:
    return bool(reject_slugs & project_slugs)


@functools.lru_cache()
def phab_project_info() -> dict[str, dict[str, Any]]:
    """Get Phabricator project info.

    :return: mapping from project PHID to its JSON dict.

    Each project dict gets an extra computed field `_parent_phid`, which is the
    top-most parent project, i.e. the gandest grandparent.

    This also fills the `project_phids` dictionary.

    See `data/orig/projects.json`
    """

    _log.debug("Loading Phabricator projects")
    proj_list = common.readJsonFile(common.orig_dir / "projects.json")
    proj_dict = {p["phid"]: p for p in proj_list}

    # Annotate with the top-most project
    for proj in proj_dict.values():
        ancestors = proj["attachments"]["ancestors"]["ancestors"]
        if not ancestors:
            proj["_parent_phid"] = None
            continue
        # The first anchestor is the top-most one, i.e. the grandest grandparent.
        proj["_parent_phid"] = ancestors[0]["phid"]

    _log.info("Loaded info of %d Phabricator projects", len(proj_dict))
    return proj_dict


@functools.cache
def phab_project_name(project_slug: str) -> str:
    """Return the project name for this slug."""
    proj_dict = phab_project_info()
    for proj in proj_dict.values():
        if proj["fields"]["slug"] == project_slug:
            return proj["fields"]["name"]

    raise KeyError(f"No project with slug {project_slug!r} known")


@functools.cache
def label_for_project(project_slug: str) -> str:
    """Returns the label for the project, or the empty string if there should be none."""
    if project_slug in slugs_without_label:
        return ""
    project_name = phab_project_name(project_slug)
    return f"{project_label_prefix}{project_name}"


def scoped_module_labels() -> set[str]:
    return {f"{module_label_scoped_prefix}{name}" for name in blender_modules}


# Modules with a higher specificity will be more likely to be picked to assign a
# scoped "Module::XYZ" label to an issue.
_module_specificity: dict[str, int] = defaultdict(
    int,
    {
        "animation_rigging": 3,
        "eevee_viewport": 3,
        "grease_pencil": 3,
        "modeling": 3,
        "nodes_physics": 3,
        "pipeline_assets_i_o": 3,
        "render_cycles": 3,
        "sculpt_paint_texture": 3,
        "vfx_video": 3,
        "user_interface": 2,
        "core": 1,
        "development_management": 1,
        "platforms_builds_tests_devices": 1,
        "python_api": 1,
        "triaging": 1,
    },
)


@functools.cache
def label_for_module(module_slugs: frozenset[str]) -> str:
    """Determine the appropriate scoped module label, given the set of modules.

    :param modules: module project slugs, see _module_specificy.
    """
    if not module_slugs:
        return ""

    max_score: int = max(_module_specificity[m] for m in module_slugs)
    potential_slugs: list[str] = [
        m
        for (m, score) in _module_specificity.items()
        if score == max_score and m in module_slugs
    ]
    if not potential_slugs:
        return ""
    slug = random.choice(potential_slugs)

    label = labels[slug]
    return label.replace(module_label_prefix, module_label_scoped_prefix)


@functools.cache
def is_module_label(label: str) -> bool:
    return label.startswith(module_label_prefix)
