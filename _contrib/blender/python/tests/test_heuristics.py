#!/usr/bin/env python3

import unittest
from typing import Any

from phab_tool.convert import heuristics
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


class TaskContextTest(unittest.TestCase):
    @staticmethod
    def _task(task_id: int) -> dict[str, Any]:
        return common.readJsonFile(
            common.orig_dirs["task"] / common.subpath(task_id, ".json")
        )

    def test_empty_task(self):
        ctx = heuristics.task_context(
            {
                "id": 161,
                "phid": "PHID-TASK-opjehoofd",
                "fields": {},
            }
        )
        expect = heuristics.TaskGiteaContext(number=161, reject=True)
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_blender_task(self):
        # This task is tagged with "bf_blender".
        task = self._task(103825)
        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(number=103825, repository="blender")
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_multiple_modules_and_labels(self):
        # This task is tagged with "animation_rigging", "bf_blender", "good_first_issue", "modeling", "nodes_physics".
        task = self._task(103410)
        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(
            number=103410,
            repository="blender",  # It's clear this is Blender.
            project="",  # the tags are ambiguous, so no project should be chosen.
            labels={
                "good first issue",
                "legacy module/Animation & Rigging",
                "legacy module/Modeling",
                "legacy module/Nodes & Physics",
                "legacy project/Animation & Rigging",
                "legacy project/Nodes & Physics",
                "legacy project/Modeling",
                "legacy project/Good First Issue",
            },
        )
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_flamenco_task(self):
        # This task is tagged with "flamenco", "good_first_issue".
        task = self._task(102429)
        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(
            number=102429,
            repository="flamenco",  # It's clear this is Flamenco.
            project="",  # No projects for the Flamenco repo.
            labels={
                "good first issue",
                "legacy project/Good First Issue",
            },
        )
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_untagged_bugreport(self):
        # This task doesn't have any tags, and is a Blender bug report.
        task = self._task(101416)
        self.assertEqual([], task["attachments"]["projects"]["projectPHIDs"])

        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(number=101416, repository="blender")
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_empty_spam_task(self):
        # This task was spam, and was cleared off all its contents.
        task = self._task(101483)
        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(number=101483, reject=True)
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_spam_task(self):
        # This task was spam, and its contents replaced with the word "Spam".
        task = self._task(100960)
        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(number=100960, reject=True)
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)

    def test_unrecognisable_task(self):
        # This task was unrecognisable, but shouldn't be rejected either.
        task = self._task(103644)
        ctx = heuristics.task_context(task)
        expect = heuristics.TaskGiteaContext(
            number=103644,
            repository="blender",
            labels={"migration/requires-manual-verification"},
        )
        self.assertEqual(expect.repository, ctx.repository)
        self.assertEqual(expect.project, ctx.project)
        self.assertEqual(expect.labels, ctx.labels)
        self.assertEqual(expect.reject, ctx.reject)
