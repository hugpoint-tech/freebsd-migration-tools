import dataclasses
import logging
from pathlib import Path

from . import gitea_types as gt
from . import projects
from .. import common

_log = logging.getLogger(__name__)

# A Gitea project for each Blender module. Almost.
project_names = [
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
    # Splitting up the VFX & Video module:
    "Compositing",
    "Motion Tracking",
    "Video Sequencer",
]


blender_projects: list[gt.Project] = [
    gt.Project(title=module) for module in sorted(project_names)
]


def write_to_yaml(yamlpath: Path) -> None:
    _log.debug("Writing Gitea projects to %s", yamlpath)

    data = [dataclasses.asdict(p) for p in blender_projects]
    common.saveYamlFile(data, yamlpath)
