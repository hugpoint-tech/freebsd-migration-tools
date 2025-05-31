#!/usr/bin/env python3

import unittest
from typing import Any

from phab_tool.convert import projects
from phab_tool import common


# Some task numbers with multiple project tags:
#   90433: 4
#   94080: 4
#   95965: 4
#  102251: 4
#  102879: 4
#  103187: 4
#  103387: 4
#  103789: 4
#  103176: 5
#  103410: 5


class ProjectSlugTest(unittest.TestCase):
    @staticmethod
    def _task(task_id: int) -> dict[str, Any]:
        return common.readJsonFile(
            common.orig_dirs["task"] / common.subpath(task_id, ".json")
        )

    def test_task_projects(self):
        task = self._task(103825)
        proj_slugs = projects.project_slugs(task)
        self.assertEqual({"bf_blender"}, proj_slugs)

    def test_multiple_modules_and_labels(self):
        task = self._task(103410)
        proj_slugs = projects.project_slugs(task)
        self.assertEqual(
            {
                "animation_rigging",
                "bf_blender",
                "good_first_issue",
                "modeling",
                "nodes_physics",
            },
            proj_slugs,
        )

    def test_label_for_module(self):
        def f(*args):
            modules = frozenset(args)
            return projects.label_for_module(modules)

        self.assertEqual("", f())
        self.assertEqual("Module::Animation & Rigging", f("animation_rigging"))
        self.assertEqual("Module::Animation & Rigging", f("animation_rigging", "core"))
        self.assertEqual(
            "Module::Animation & Rigging",
            f("animation_rigging", "core", "random-module-name"),
        )
        self.assertEqual(
            "Module::Animation & Rigging",
            f("animation_rigging", "user_interface", "core"),
        )
        self.assertEqual("Module::User Interface", f("user_interface", "core"))
        self.assertEqual("Module::Core", f("core", "random-weird-one"))
