#!/usr/bin/env python3

import inspect
import os
import unittest

from typing import Type

from phab_tool import users
from phab_tool.convert import markup_processor
from phab_tool.convert.markup_processor import process_markup_to_markdown

FAKE_PASTES_JSON = {
    123: {
        "id": 123,
        "fields": {
            "title": "Title",
            "language": "cpp",
        },
        "attachments": {
            "content": {
                "content": "Content",
            }
        },
    },
}

FAKE_FILES_JSON = {
    123: {
        "id": 123,
        "name": "My File.txt",
    },
    14081760: {
        "id": 14081760,
        "name": "system.jpg",
        "mimeType": "image/jpeg",
    },
}

FAKE_REVISIONS_JSON = {
    123: {
        "id": 123,
        "fields": {
            "title": "My Revision",
        },
    },
}


FAKE_TASKS_JSON = {
    123: {
        "id": 123,
        "phid": "PHID-TASK-123",
        "fields": {
            "name": "My Task",
        },
        "attachments": {
            "projects": {
                "projectPHIDs": ["PHID-PROJ-hclk7tvd6pmpjmqastjl"],  # BF Blender
            }
        },
    },
    456: {
        "id": 456,
        "phid": "PHID-TASK-456",
        "fields": {
            "name": "My Task in Addons",
        },
        "attachments": {
            "projects": {
                "projectPHIDs": ["PHID-PROJ-jb6eqxvwwhbo2xs3ev3m"],  # BF Add-Ons
            }
        },
    },
}

FAKE_USER_MAP = {
    "sergey": "hackerman",
}


class ContextLoadingFakeData(markup_processor.Context):
    def load_resource(
        self, resource_class: Type[markup_processor.Resource], id: int
    ) -> markup_processor.Resource:

        assert markup_processor.Paste.orig_dir
        assert markup_processor.File.orig_dir
        assert markup_processor.Revision.orig_dir
        assert markup_processor.Task.orig_dir

        if resource_class == markup_processor.Paste:
            return markup_processor.Paste.create_from_json(FAKE_PASTES_JSON[id])

        if resource_class == markup_processor.File:
            return markup_processor.File.create_from_json(FAKE_FILES_JSON[id])

        if resource_class == markup_processor.Revision:
            return markup_processor.Revision.create_from_json(FAKE_REVISIONS_JSON[id])

        if resource_class == markup_processor.Task:
            return markup_processor.Task.create_from_json(FAKE_TASKS_JSON[id])

    def get_new_user_name(self, phabricator_user_name: str) -> str:
        return FAKE_USER_MAP.get(phabricator_user_name, None)


class BaseMarkupToMarkdownTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["ARCHIVE_URL"] = "https://archive.org/"

    @classmethod
    def create_context(cls) -> markup_processor.Context:
        return ContextLoadingFakeData(repository_name="blender")


class MarkupToMarkdownTest(BaseMarkupToMarkdownTest):
    def test_empty(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, ""), "")


class MarkupToMarkdownPasteTest(BaseMarkupToMarkdownTest):
    def test_referencing_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "P123"),
            "[P123](https://archive.org/P123.txt)",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head\nP123\ntail"),
            "head\n[P123](https://archive.org/P123.txt)\ntail",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head P123 tail"),
            "head [P123](https://archive.org/P123.txt) tail",
        )

    def test_referencing_partial_braces(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{P123"),
            "{[P123](https://archive.org/P123.txt)",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "P123}"),
            "[P123](https://archive.org/P123.txt)}",
        )

    def test_referencing_text_around(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "fooP123"), "fooP123")
        self.assertEqual(process_markup_to_markdown(context, "P123bar"), "P123bar")

    def test_embedded_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{P123}"),
            """[P123: Title](https://archive.org/P123.txt)
```cpp
Content
```
""",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo {P123} bar"),
            """foo [P123: Title](https://archive.org/P123.txt)
```cpp
Content
```
 bar""",
        )

    def test_embedded_text_around(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "foo{P123}"),
            "foo{[P123](https://archive.org/P123.txt)}",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "{P123}bar"),
            "{[P123](https://archive.org/P123.txt)}bar",
        )


class MarkupToMarkdownFileTest(BaseMarkupToMarkdownTest):
    def test_referencing_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "F123"),
            "[F123](https://archive.org/F123/My_File.txt)",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head\nF123\ntail"),
            "head\n[F123](https://archive.org/F123/My_File.txt)\ntail",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head F123 tail"),
            "head [F123](https://archive.org/F123/My_File.txt) tail",
        )

    def test_referencing_partial_braces(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{F123"),
            "{[F123](https://archive.org/F123/My_File.txt)",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "F123}"),
            "[F123](https://archive.org/F123/My_File.txt)}",
        )

    def test_referencing_text_around(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "fooF123"), "fooF123")
        self.assertEqual(process_markup_to_markdown(context, "F123bar"), "F123bar")

    def test_embedded_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{F123}"),
            "[My File.txt](https://archive.org/F123/My_File.txt)",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo {F123} bar"),
            "foo [My File.txt](https://archive.org/F123/My_File.txt) bar",
        )

    def test_embedded_image(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{F14081760}"),
            "![system.jpg](https://archive.org/F14081760/system.jpg)",
        )

    def test_embedded_text_around(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "foo{F123}"),
            "foo{[F123](https://archive.org/F123/My_File.txt)}",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "{F123}bar"),
            "{[F123](https://archive.org/F123/My_File.txt)}bar",
        )

    def test_embedded_attributes(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{F14081760, width = 800}"),
            "![system.jpg](https://archive.org/F14081760/system.jpg)",
        )

    def test_corner_cases(self):
        context = self.create_context()

        # From T104088: File reference in the parenthesis.
        self.assertEqual(
            process_markup_to_markdown(context, "(Open {F123})"),
            "(Open [My File.txt](https://archive.org/F123/My_File.txt))",
        )

        # From T104025: T96261 used in the URL
        self.assertEqual(
            process_markup_to_markdown(context, "https://developer.blender.org/T123"),
            "https://developer.blender.org/T123",
        )


class MarkupToMarkdownRevisionTest(BaseMarkupToMarkdownTest):
    def test_referencing_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "D123"),
            "[D123](https://archive.org/D123)",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head\nD123\ntail"),
            "head\n[D123](https://archive.org/D123)\ntail",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head D123 tail"),
            "head [D123](https://archive.org/D123) tail",
        )

    def test_referencing_partial_braces(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{D123"),
            "{[D123](https://archive.org/D123)",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "D123}"),
            "[D123](https://archive.org/D123)}",
        )

    def test_referencing_text_around(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "fooD123"), "fooD123")
        self.assertEqual(process_markup_to_markdown(context, "D123bar"), "D123bar")

    def test_embedded_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{D123}"),
            "[D123: My Revision](https://archive.org/D123)",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo {D123} bar"),
            "foo [D123: My Revision](https://archive.org/D123) bar",
        )

    def test_embedded_text_around(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "foo{D123}"),
            "foo{[D123](https://archive.org/D123)}",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "{D123}bar"),
            "{[D123](https://archive.org/D123)}bar",
        )


class MarkupToMarkdownTaskTest(BaseMarkupToMarkdownTest):
    def test_referencing_simple(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "T123"), "#123")

        self.assertEqual(
            process_markup_to_markdown(context, "head\nT123\ntail"),
            "head\n#123\ntail",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head T123 tail"), "head #123 tail"
        )

    def test_referencing_partial_braces(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "{T123"), "{#123")
        self.assertEqual(
            process_markup_to_markdown(context, "T123}"),
            "#123}",
        )

    def test_referencing_text_around(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "fooT123"), "fooT123")
        self.assertEqual(process_markup_to_markdown(context, "T123bar"), "T123bar")

    def test_embedded_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{T123}"), "#123 (My Task)"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo {T123} bar"),
            "foo #123 (My Task) bar",
        )

    def test_embedded_text_around(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "foo{T123}"),
            "foo{#123}",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "{T123}bar"),
            "{#123}bar",
        )

    def test_task_from_other_repo(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "T456"), "blender/blender-addons#456"
        )


class MarkupToMarkdownCommitTest(BaseMarkupToMarkdownTest):
    def test_referencing_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context, "rB7df5d7c7a70963f72a71e2f19507218b51d0f188"
            ),
            "7df5d7c7a7",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head\nrB7df5d7c7a7\ntail"),
            "head\n7df5d7c7a7\ntail",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "head rB7df5d7c7a7 tail"),
            "head 7df5d7c7a7 tail",
        )

    def test_referencing_other_repo(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context, "rBA7df5d7c7a70963f72a71e2f19507218b51d0f188"
            ),
            "blender/blender-addons@7df5d7c7a7",
        )

    def test_referencing_partial_braces(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{rB7df5d7c7a7"), "{7df5d7c7a7"
        )
        self.assertEqual(
            process_markup_to_markdown(context, "rB7df5d7c7a7}"), "7df5d7c7a7}"
        )

    def test_referencing_text_around(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "foorB7df5d7c7a7"),
            "foorB7df5d7c7a7",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "rB7df5d7c7a7bar"),
            "rB7df5d7c7a7bar",
        )

    def test_embedded_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "{rB7df5d7c7a7}"), "7df5d7c7a7"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo {rB7df5d7c7a7} bar"),
            "foo 7df5d7c7a7 bar",
        )

    def test_embedded_text_around(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "foo{rB7df5d7c7a7}"),
            "foo{7df5d7c7a7}",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "{rB7df5d7c7a7}bar"),
            "{7df5d7c7a7}bar",
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo |{rB7df5d7c7a7}"),
            "foo |7df5d7c7a7",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "foo {rB7df5d7c7a7}|"),
            "foo 7df5d7c7a7|",
        )

    def test_url(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context, "https://developer.blender.org/rB7df5d7c7a7"
            ),
            "https://developer.blender.org/rB7df5d7c7a7",
        )

    def test_corner_cases(self):
        context = self.create_context()

        # T100749 has a non-breaking space: \u00a0{rB07ba515b21...}
        self.assertEqual(
            process_markup_to_markdown(context, "\u00a0rB07ba515b21"),
            " 07ba515b21",
        )

        # Git commit reference in T88438.
        self.assertEqual(
            process_markup_to_markdown(context, "({rB12d93e44d0})"),
            "(12d93e44d0)",
        )

        # SVN commit references in T88438.
        self.assertEqual(
            process_markup_to_markdown(context, "({rBL62657})"),
            "({rBL62657})",
        )
        self.assertEqual(
            process_markup_to_markdown(context, "{rBL62657},"),
            "{rBL62657},",
        )


class MarkupToMarkdownTableTest(BaseMarkupToMarkdownTest):
    def test_existing_sepaartor(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context, "| Header 1 | Header 2 |\n| -- | -- |\n| Data 1 | Data 2 |\n"
            ),
            "| Header 1 | Header 2 |\n| -- | -- |\n| Data 1 | Data 2 |\n",
        )

    def test_single_row(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "| Header 1 | Header 2 |"),
            "| Header 1 | Header 2 |\n| -- | -- |\n",
        )

        self.assertEqual(
            process_markup_to_markdown(context, " | Header 1 | Header 2 |"),
            " | Header 1 | Header 2 |\n | -- | -- |\n",
        )

    def test_multiple_rows(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context, "| Header 1 | Header 2 |\n| Data 1 | Data 2 |\n"
            ),
            "| Header 1 | Header 2 |\n| -- | -- |\n| Data 1 | Data 2 |\n",
        )


class MarkupToMarkdownLinkTest(BaseMarkupToMarkdownTest):
    def test_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "[[https://example.com/ | Test Link]]"),
            "[Test Link](https://example.com/)",
        )


class MarkupToMarkdownStyleTest(BaseMarkupToMarkdownTest):
    def test_bold(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "**Text**"), "**Text**")
        self.assertEqual(process_markup_to_markdown(context, "**Text **"), "**Text**")

        self.assertEqual(
            process_markup_to_markdown(context, "foo** Text**"), "foo**Text**"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo ** Text**"), "foo **Text**"
        )

        # TODO(sergey): This should become a level 2 nested item with text `Text **`.
        self.assertEqual(
            process_markup_to_markdown(context, "** Text **"), "** Text **"
        )

    def test_italic(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "// Text //"), "*Text*")

    def test_checkbox(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "[]"), "[]")
        self.assertEqual(process_markup_to_markdown(context, "[ ]"), "[ ]")
        self.assertEqual(process_markup_to_markdown(context, "[x]"), "[x]")

        self.assertEqual(process_markup_to_markdown(context, "[] Text"), "- [ ] Text")
        self.assertEqual(process_markup_to_markdown(context, "[x] Text"), "- [x] Text")

        self.assertEqual(process_markup_to_markdown(context, "[X] Text"), "- [x] Text")
        self.assertEqual(process_markup_to_markdown(context, "[-] Text"), "- [x] Text")
        self.assertEqual(process_markup_to_markdown(context, "[.] Text"), "- [x] Text")

        self.assertEqual(
            process_markup_to_markdown(context, "  [] Text"), "  - [ ] Text"
        )

    def test_header(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "=Header 1="), "# Header 1\n"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "== Header 2 =="), "## Header 2\n"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "=== Header 3==="), "### Header 3\n"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "==== Header 4 ===="), "**Header 4**\n"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "=====Description=====\n"),
            "**Description**\n",
        )

    def test_list(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "# Item 1"), "- Item 1")
        self.assertEqual(process_markup_to_markdown(context, "## Item 1"), "  - Item 1")

        self.assertEqual(process_markup_to_markdown(context, "- Item 1"), "- Item 1")
        self.assertEqual(process_markup_to_markdown(context, "-- Item 1"), "  - Item 1")

        self.assertEqual(
            process_markup_to_markdown(context, "# Item 1\n# Item 2"),
            "- Item 1\n- Item 2",
        )

    def test_tricky_cases(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(context, "# List item\n"), "- List item\n"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "# Header\nText"), "# Header\nText"
        )

    def test_complex(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context,
                inspect.cleandoc(
                    """
                    # Header

                    Text

                    # Item 1
                    ## Item 1.1

                    ### Tasks

                    Testing

                    ####File Type
                    Blurb

                    [x] Checkbox
                      * Item nested in checkbox

                    # Item
                    """
                ),
            ),
            inspect.cleandoc(
                """
                # Header

                Text

                - Item 1
                  - Item 1.1

                ### Tasks

                Testing

                **File Type**
                Blurb

                - [x] Checkbox
                  * Item nested in checkbox

                - Item
                """
            ),
        )

    def test_separator(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "---"), "---")

    def test_explicit_code(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context,
                inspect.cleandoc(
                    """
                    Text line
                    ```
                    Code line
                    ```
                    Another text line
                    """
                ),
            ),
            inspect.cleandoc(
                """
                Text line
                ```
                Code line
                ```
                Another text line
                """
            ),
        )

    def test_implicit_code(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context,
                inspect.cleandoc(
                    """
                    Text line
                      Code line 1
                      Code line 2
                    Another text line
                    """
                ),
            ),
            inspect.cleandoc(
                """
                Text line
                ```
                Code line 1
                Code line 2
                ```
                Another text line
                """
            ),
        )


class MarkupToMarkdownUserHandleTest(BaseMarkupToMarkdownTest):
    def test_simple(self):
        context = self.create_context()

        self.assertEqual(process_markup_to_markdown(context, "@sergey"), "@hackerman")

        self.assertEqual(process_markup_to_markdown(context, "@sergey@"), "@hackerman@")

        self.assertEqual(process_markup_to_markdown(context, "@@sergey"), "@@sergey")
        self.assertEqual(
            process_markup_to_markdown(context, "foo@sergey"), "foo@sergey"
        )

        self.assertEqual(
            process_markup_to_markdown(context, "foo @sergey bar"), "foo @hackerman bar"
        )


class UserHandleProcessorTest(unittest.TestCase):
    def test_all_usernames(self):
        phab_users = list(users.iter_users())

        regex = markup_processor.UserHandleProcessor.regex

        for u in phab_users:
            username = u["fields"]["username"]
            if username is None:
                continue

            match = regex.match(f"@{username}")
            if match:
                self.assertEqual(username, match.group("username"))
            else:
                self.fail(f"no match found for @{username}")


class MarkupToMarkdownQuoteTest(BaseMarkupToMarkdownTest):
    def test_simple(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context,
                inspect.cleandoc(
                    """
                    >> Quote level 2
                    >> Quote level 2 Line 2
                    > Quote level 1
                    > Quote level 1 Line 2
                    Comment
                    """
                ),
            ),
            inspect.cleandoc(
                """
                >> Quote level 2
                >> Quote level 2 Line 2

                > Quote level 1
                > Quote level 1 Line 2

                Comment
                """
            ),
        )

    def test_title(self):
        context = self.create_context()

        self.assertEqual(
            process_markup_to_markdown(
                context,
                inspect.cleandoc(
                    """
                    >>! Quote level 1 Title
                    > Quote level 1 Line
                    Comment
                    """
                ),
            ),
            inspect.cleandoc(
                """
                > Quote level 1 Title
                > Quote level 1 Line

                Comment
                """
            ),
        )
