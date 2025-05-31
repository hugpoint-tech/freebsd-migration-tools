from pathlib import Path
from typing import Type, List, Optional
import re
import os


from . import heuristics, orgs_and_repos, gitea_types, user_mapping
from .callsign_map import callsign_to_repo_name
from .. import common


class Resource:
    """Base class of a resource like paste or a file"""

    id: int
    orig_dir: str

    @classmethod
    def load(cls, id: int) -> Optional["Resource"]:
        """
        Load resource information from its JSON file

        If the json file does not exist None is returned.
        """

        json_subpath = common.subpath(id, ".json")
        json_path = cls.orig_dir / json_subpath

        if not json_path.exists():
            return None

        return cls.load_from_json_file(json_path)

    @classmethod
    def load_from_json_file(cls, json_filename: Path) -> "Resource":
        """
        Load the resource from the JSON file

        If the json file does not exist None is returned.
        """

        json = common.readJsonFile(json_filename)

        return cls.create_from_json(json)

    @classmethod
    def create_from_json(cls, json: dict) -> "Resource":
        """Create resource from its serialized JSON dictionary"""
        raise Exception("Needs implementation")


class Paste(Resource):
    """Paste resource"""

    orig_dir = common.orig_dirs["paste"]

    title: str
    content: str
    language: str

    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.content = ""
        self.language = ""

    def get_uri(self) -> str:
        return os.environ["ARCHIVE_URL"] + f"P{self.id}.txt"

    def get_render_title(self) -> str:
        """
        Get paste title suitable for embedding

        It follows the Phabricator rules and replaces the empty title with
        "(An Untitled Masterwork)".
        """
        if self.title:
            return self.title

        return "(An Untitled Masterwork)"

    def get_render_language(self) -> str:
        """
        Get paste language suitable for embedding
        """

        if not self.language:
            return ""

        return self.language

    @classmethod
    def create_from_json(cls, json: dict) -> "Paste":
        paste = Paste()
        paste.id = json["id"]
        paste.title = json["fields"]["title"]
        paste.content = json["attachments"]["content"]["content"]
        paste.language = json["fields"].get("language", "")

        return paste


class File(Resource):
    """File resource"""

    orig_dir = common.orig_dirs["file"]

    id: int
    name: str
    mime_type: str

    def __init__(self) -> None:
        self.id = 0
        self.name = ""
        self.mime_type = ""

    def get_uri(self) -> str:
        """Get URI to this file"""
        safe_file_name = common.make_file_name_safe(self.name)
        return os.environ["ARCHIVE_URL"] + f"F{self.id}/{safe_file_name}"

    @classmethod
    def create_from_json(cls, json: dict) -> "File":
        file = File()
        file.id = json["id"]
        file.name = json["name"]
        file.mime_type = json.get("mimeType", "")

        return file

    def is_image(self) -> bool:
        if not self.mime_type:
            return False
        return self.mime_type.split("/")[0] == "image"


class Revision(Resource):
    """Differential revision resource"""

    orig_dir = common.orig_dirs["bake"] / "differential"

    id: int
    title: str

    def __init__(self) -> None:
        self.id = 0
        self.title = ""

    def get_uri(self) -> str:
        """Get URI to this revision"""
        return os.environ["ARCHIVE_URL"] + f"D{self.id}"

    @classmethod
    def load(cls, id: int) -> "Revision":
        json_subpath = common.subpath(id, "") / "info.json"
        json_path = cls.orig_dir / json_subpath

        if not json_path.exists():
            json_subpath = common.subpath(id, ".json")
            json_path = common.orig_dirs["drev"] / json_subpath

        if not json_path.exists():
            return None

        json = common.readJsonFile(json_path)
        json["id"] = id

        return cls.create_from_json(json)

    @classmethod
    def load_from_json_file(cls, json: dict) -> "Revision":
        raise Exception("Not supported")

    @classmethod
    def create_from_json(cls, json: dict) -> "Revision":
        revision = Revision()

        revision.id = json["id"]

        if "fields" in json:
            revision.title = json["fields"]["title"]
        else:
            revision.title = json["title"]

        return revision


class Task(Resource):
    """Maniphest task resource"""

    orig_dir = common.orig_dirs["task"]

    id: int
    name: str

    repository: gitea_types.Repository

    def __init__(self) -> None:
        self.id = 0
        self.name = ""
        self.repository = None

    @classmethod
    def create_from_json(cls, json: dict) -> "Task":
        task = Task()
        task.id = json["id"]
        task.name = json["fields"]["name"]

        ctx = heuristics.task_context(json)
        if not ctx.reject:
            task.repository = orgs_and_repos.repo_by_name(ctx.repository)

        return task


class Context:
    repository_name: str = ""

    def __init__(self, repository_name: str) -> None:
        self.repository_name = repository_name

    def load_resource(self, resource_class: Type[Resource], id: int) -> Resource:
        """Load resource information for the given ID"""

        return resource_class.load(id)

    def get_new_user_name(self, maybe_phabricator_user_name: str) -> str:
        """
        Get the new GItea user name for the old Phabricator user name

        Return "" if the user mapping is unknown (which can happen for invalid @ mention or
        # mentions of a deleted user).
        """
        try:
            u = user_mapping.gitea_username(maybe_phabricator_user_name)
        except user_mapping.UnkownUserError:
            # This may not be a username after all.
            return maybe_phabricator_user_name
        return u


class BaseProcessor:
    """
    Base class for processing function

    Each of the processors are processing a single aspect of markup conversion to markdown: such
    as expansion of file links.
    """

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        """
        Process the input text are turn the output

        The input text is the current state of conversion of markup to markdown, and the output is
        a text which is closer to the final ideal markdown.
        """
        raise Exception("Needs implementation")


class SpecialCharacterProcessor(BaseProcessor):
    """
    Processor which replaces special characters

    For example, replaces non-breaking spaced with spaces.

    This is needed because the special characters might interfere with the parser of Gitea.
    """

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        return text.replace("\u00a0", " ")


class RegexProcessor(BaseProcessor):
    regex: re.Pattern

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        # Current state of the processed text.
        processed_text = ""

        # Position in the input string up to which the input has been appended to the result.
        prev_input_pos = 0

        for match in cls.regex.finditer(text):
            span = match.span()

            # Append the input text from previously handled position up to the position prior to
            # # the match.
            processed_text += text[prev_input_pos : span[0]]

            # Handle the substitution.
            processed_text += cls.process_match(context, match)

            # Move the handled position forward: the input text up to the end of the current match
            # has been handled.
            prev_input_pos = span[1]

        processed_text += text[prev_input_pos:]

        return processed_text

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        """Process match of the input text and return the text which is to replace it"""
        raise Exception("Needs implementation")

    @classmethod
    def get_match_text(cls, match: re.Match) -> str:
        """Get string which is matched"""
        span = match.span()
        return match.string[span[0] : span[1]]


class LinkProcessor(RegexProcessor):
    """
    Processor which replaces Markup/Wiki links syntax with markdown

    Example:
        [[ link | text ]] -> [text](link)
    """

    regex = re.compile(r"\[\[\s*(?P<link>.*?)\s*\|\s*(?P<text>.*)\s*\]\]")

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        text = match.group("text")
        link = match.group("link")
        return f"[{text}]({link})"


class BoldProcessor(RegexProcessor):
    """
    Processor which ensures spacing around bold marker `**` is compatible with markdown

    The Phabricator has less strict rules about those.
    """

    regex = re.compile(r"(?!(\s+\*)|(\A\*\*\s))\*\*\s*(?P<text>\w.*?)\s*\*\*")

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        text = match.group("text")
        return f"**{text}**"


class ItalicProcessor(RegexProcessor):
    """
    Processor which converts markup italics // .. // to markdown * .. *
    """

    regex = re.compile(r"//\s*(?P<text>.*?)\s*//")

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        text = match.group("text")
        return f"*{text}*"


class CheckboxProcessor(RegexProcessor):
    """
    Processor which ensures checkboxes are prefixed with `-`.
    """

    regex = re.compile(r"(?=\s*\[)(?P<checkbox>\[.?\])(?=.*\w)")

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        checkbox = match.group("checkbox")

        if checkbox == "[]":
            checkbox = "[ ]"

        if checkbox != "[ ]":
            checkbox = "[x]"

        return f"- {checkbox}"


class MonogramProcessor(RegexProcessor):
    """
    Processor which handles monogram references
    """

    resource_cls: Type[Resource]

    @classmethod
    def compile_regex(cls, monogram_char: str, attributes=[]) -> re.Pattern:
        """
        Compile regex pattern which matches references to a resource via its monogram and id

        For example, it matches P123 and {P123}
        """

        attributes_part = r"(\s*,\s*(" + ("".join(attributes)) + r")\s*=\s*\w*)?"

        return re.compile(
            r"((?P<open>((?<=\W)|(?<=\A)){(?="
            + monogram_char
            + r"[0-9]+"
            + attributes_part
            + r"}(?=(\Z|[\s\|\,\.:;)]))))|(\b))"
            r"(?(open)|((?<=(\A))|(?<=([^/]))))"
            r"(" + monogram_char + r"(?P<id>[0-9]+))"
            r"(?(open)" + attributes_part + r"}|(\b))",
            re.MULTILINE,
        )

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        id = int(match.group("id"))
        resource = context.load_resource(cls.resource_cls, id)

        if not resource:
            # If the resource reference is invalid return the input text as-is.
            return cls.get_match_text(match)

        if match.group("open"):
            return cls.render_embedded(context, match, resource)

        return cls.render_reference(context, match, resource)

    @classmethod
    def render_embedded(
        cls, context: Context, match: re.Match, resource: Resource
    ) -> str:
        """
        Render embedded resource

        The match consists of a string `{<monogram><id>}`. For example, `{P123}`.
        """
        raise Exception("Needs implementation")

    @classmethod
    def render_reference(
        cls, context: Context, match: re.Match, resource: Resource
    ) -> str:
        """
        Render reference to a resource

        The match consists of a string {<monogram><id>`. For example, `P123`.
        """
        raise Exception("Needs implementation")


class PasteProcessor(MonogramProcessor):
    """
    Processor of references to pastes

    Handles both embedded and externally referencing pastes.

    The embedded paste is defined by the markup `{P<id>}`. In Phabricator it is rendered as a
    monogram with an id and title, followed by an actual content of the paste (with limited
    number of visible lines, and scrolling when needed).

    The externally referencing paste is defined by the markup `P<id>`. In Phabricator it is
    rendered as a link with title of P<id> pointing to a page where the full paste is visible.

    An example of the processed embedded paste reference:

      P123: Paste Title
      ```cpp
      // Paste content
      ```

    An example of the processed externally referencing paste reference:

      [P123](https://archive.blender.org/P123.txt)

    """

    regex = MonogramProcessor.compile_regex("P")
    resource_cls = Paste

    @classmethod
    def render_embedded(cls, context: Context, match: re.Match, paste: Paste) -> str:
        # TODO(sergey): Investigate whether there is a way to limit the number of visible lines.

        return (
            f"[P{paste.id}: {paste.get_render_title()}]({paste.get_uri()})\n"
            f"```{paste.get_render_language()}\n"
            f"{paste.content}\n"
            "```\n"
        )

    @classmethod
    def render_reference(cls, context: Context, match: re.Match, paste: Paste) -> str:
        return f"[P{paste.id}]({paste.get_uri()})"


class FileProcessor(MonogramProcessor):
    """
    Processor of references to files

    Handles both embedded and externally referencing files.

    The embedded file is defined by the markup `{F<id>}`. In Phabricator it is rendered in a few
    possible ways;

    * Images are rendered with their preview, clicking on which opens the full resolution image
    * Videos ar rendered as a `<video>` HTML5 tag, allowing viewing directly in the browser.
    * The rest of the file types are rendered as a download box with the file name and size
      displayed.

    The externally referencing file is defined by the markup `F<id>`. In Phabricator it is
    rendered as a link with title of F<id> pointing to a page where the full file is visible.

    An example of the processed embedded file reference:

      [F123: File name](https://archive.blender.org/F123.bin)

    An example of the processed externally referencing file reference:

      [F123](https://archive.blender.org/F123.bin)

    """

    regex = MonogramProcessor.compile_regex("F", ("width",))
    resource_cls = File

    @classmethod
    def render_embedded(cls, context: Context, match: re.Match, file: File) -> str:
        prefix = ""

        if file.is_image():
            prefix = "!"

        return f"{prefix}[{file.name}]({file.get_uri()})"

    @classmethod
    def render_reference(cls, context: Context, match: re.Match, file: File) -> str:
        return f"[F{file.id}]({file.get_uri()})"


class RevisionProcessor(MonogramProcessor):
    """
    Processor of references to differential revisions

    The embedded revision is defined by the markup `{D<id>}`. In Phabricator it is rendered as
    a link with text `D<id>: <Title>`.

    The externally referencing revision is defined by the markup `D<id>`. In Phabricator it is
    rendered as a link with title of D<id> pointing to a code review page.

    An example of the processed embedded revision reference:

      [D123: Awesome feature](https://archive.blender.org/differential/D123.html)

    An example of the processed externally referencing revision reference:

      [D123](https://archive.blender.org/differential/D123.html)

    """

    regex = MonogramProcessor.compile_regex("D")
    resource_cls = Revision

    @classmethod
    def render_embedded(
        cls, context: Context, match: re.Match, revision: Revision
    ) -> str:
        return f"[D{revision.id}: {revision.title}]({revision.get_uri()})"

    @classmethod
    def render_reference(
        cls, context: Context, match: re.Match, revision: Revision
    ) -> str:
        return f"[D{revision.id}]({revision.get_uri()})"


class TaskProcessor(MonogramProcessor):
    """
    Processor of references to tasks

    The embedded task is defined by the markup `{T<id>}`. In Phabricator it is rendered as
    a link with text `T<id>: <name>`.

    The externally referencing task is defined by the markup `T<id>`. In Phabricator it is
    rendered as a link with title of T<id> pointing to the task page.

    An example of the processed embedded task reference:

      #123: Bug report

    An example of the processed externally referencing task reference:

      #123

    If the task is from different repository then a full(er) syntax is used: <org>/<repo>#<issue>
    """

    regex = MonogramProcessor.compile_regex("T")
    resource_cls = Task

    @classmethod
    def render_embedded(cls, context: Context, match: re.Match, task: Task) -> str:
        reference = cls._get_task_reference(context, task)
        return f"{reference} ({task.name})"

    @classmethod
    def render_reference(cls, context: Context, match: re.Match, task: Task) -> str:
        reference = cls._get_task_reference(context, task)
        return f"{reference}"

    @classmethod
    def _get_task_reference(cls, context: Context, task: Task) -> str:
        """
        Get shortest possible Gitea-style reference to the task

        If the task is from the same repo as the currently processing one then the reference is
        the simple #<id>.
        Otherwise, it is <org>/<repo>#<id>
        """

        if not task.repository:
            return f"#{task.id}"

        if task.repository.name == context.repository_name:
            return f"#{task.id}"

        return f"{task.repository.owner}/{task.repository.name}#{task.id}"


class CommitProcessor(RegexProcessor):
    """
    Processor of references to commits

    The embedded commit reference is defined by the markup `{r<callsign><id>}`. In Phabricator it
    is rendered as a link with text `r<callsign><<id>: <title>`.

    The externally referencing commit is defined by the markup `r<callsign><id>`. In Phabricator it
    is rendered as a link with title of r<callsign><id> pointing to a commit page.

    The commit information is not known during the migration, so both cases are rendered as a
    reference to a commit using default Gitea syntax.
    """

    regex = re.compile(
        r"((?P<open>((?<=\W)|(?<=\A)){(?=r[A-Z]+[A-Fa-f0-9]+}(?=(\Z|[\s\|\,\.:;)]))))|(\b))"
        r"(?(open)|((?<=(\A))|(?<=([^/]))))"
        r"(r(?P<callsign>[A-Z]+)(?P<hash>[A-Fa-f0-9]+))"
        r"(?(open)}|(\b))",
        re.MULTILINE,
    )

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        callsign = match.group("callsign")

        callsign_repo_name = callsign_to_repo_name.get(callsign, None)
        if not callsign_repo_name:
            return cls.get_match_text(match)

        referenced_repo = orgs_and_repos.repo_by_name(callsign_repo_name)
        if not referenced_repo:
            return cls.get_match_text(match)

        # Shorten to 10 characters: this is what Gitea expects to be. Full length of hash is not
        # converted to a link.
        hash = match.group("hash")[0:10]

        if referenced_repo.name == context.repository_name:
            return hash

        return f"{referenced_repo.owner}/{referenced_repo.name}@{hash}"


class TableProcessor:
    """
    Processor which converts table from markup to markdown

    In the markdown it is required to have the header row followed by |--|.
    This processor ensures that the tables from Phabricator follows this rule.
    """

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        new_text = ""

        is_inside_table = False
        table_lines = []

        for line in text.splitlines(keepends=True):
            if not cls.is_table_row(line):
                new_text += cls.assemble_table(table_lines)
                new_text += line

                is_inside_table = False
                table_lines = []
                continue

            is_inside_table = True
            table_lines.append(line)

        if is_inside_table:
            new_text += cls.assemble_table(table_lines)

        return new_text

    @classmethod
    def is_table_row(cls, line: str) -> bool:
        return line.startswith("|") or line.startswith(" |")

    @classmethod
    def is_table_separator_row(cls, line: str) -> bool:
        clean_line = line.strip()
        return clean_line.startswith("| --") or clean_line.startswith("|--")

    @classmethod
    def assemble_table(cls, lines: List[str]) -> str:
        num_lines = len(lines)

        if num_lines == 0:
            return ""

        if num_lines == 1:
            return lines[0] + cls.generate_separator_row(lines[0])

        if cls.is_table_separator_row(lines[1]):
            return "".join(lines)

        return lines[0] + cls.generate_separator_row(lines[0]) + "".join(lines[1:])

    @classmethod
    def generate_separator_row(cls, header_line: str) -> bool:
        clean_header_line = header_line.strip()

        num_column_separators = clean_header_line.count("|")
        if not clean_header_line.endswith("|"):
            num_column_separators += 1

        prefix = ""

        if not header_line.endswith("\n"):
            prefix += "\n"

        # Indent to the same level as the header.
        prefix += header_line[: header_line.find("|")]

        return prefix + ("| -- " * (num_column_separators - 1)) + "|\n"


class HeaderLineProcessor(BaseProcessor):
    """
    Processor which replaces header lines syntax from a sequence of = to a sequence of #

    NOTE: Must be called on a per-line basis.
    """

    @classmethod
    def process(cls, context: Context, line: str) -> str:
        if not line:
            return line

        ch = line[0]

        if ch not in ("=", "#"):
            return line

        requested_header_level = len(line) - len(line.lstrip(ch))

        header_text = line.strip().strip(ch).strip()

        if requested_header_level > 3:
            return f"**{header_text}**\n"

        return ("#" * requested_header_level) + " " + header_text + "\n"


class NumberListProcessor(BaseProcessor):
    """
    Processor which converts numbered lists syntax

    It implements heuristics to tell numbered lists from headers apart
    """

    regex = re.compile(r"\A(?P<prefix>\s*)(?P<list>#+)\s*(?P<text>.*)")

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        new_text = ""

        prev_match = None
        is_inside_list = False

        for line in text.splitlines(keepends=True):
            match = cls.regex.match(line)

            if match and prev_match is None:
                prev_match = match
                continue

            if match and prev_match:
                is_inside_list = True

            if match and is_inside_list:
                if prev_match:
                    new_text += cls._process_match(prev_match)
                    prev_match = None
                new_text += cls._process_match(match)
                continue

            if not match:
                if prev_match:
                    new_text += prev_match.string
                is_inside_list = False

            new_text += line
            prev_match = match

        if prev_match:
            new_text += cls._process_match(prev_match)

        return new_text

    @classmethod
    def _process_match(cls, match: re.Match) -> str:
        span = match.span()

        new_line = match.string[: span[0]]
        new_line += cls._create_list_line_from_match(match)
        new_line += match.string[span[1] :]

        return new_line

    @classmethod
    def _create_list_line_from_match(cls, match: re.Match) -> str:
        prefix = match.group("prefix")
        list = match.group("list")
        text = match.group("text")

        if not text:
            return RegexProcessor.get_match_text(match)

        level = len(list)
        indent = "  " * (level - 1)

        return f"{prefix}{indent}- {text}"


class QuoteProcessor(BaseProcessor):
    """
    Processor which ensures empty lines between different levels of quotes

    In the Phabricator the following text follows the corresponding text behavior.
    But to have same render result in Gitea new lines are to be added between lines.

        >> Quote level 2
        > Quote level 1
        Comment

    """

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        new_text = ""

        # Quote level of 0 corresponds to the actual comment text.
        prev_quote_level = 0

        for line in text.splitlines(keepends=True):
            current_quote_level = len(line) - len(line.lstrip(">"))

            if current_quote_level > 1:
                if line.startswith(">" * current_quote_level + "!"):
                    line = (
                        ">" * (current_quote_level - 1)
                        + line[current_quote_level + 1 :]
                    )
                    current_quote_level -= 1

            if current_quote_level < prev_quote_level:
                new_text += "\n"

            prev_quote_level = current_quote_level

            new_text += line

        return new_text


class BulletListProcessor(RegexProcessor):
    """
    Processor which replaces bullet lists syntax

    NOTE: Must be called on a per-line basis.
    """

    regex = re.compile(r"\A(?P<prefix>\s*)(?P<list>\-+)\s*(?P<text>.*)")

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        return NumberListProcessor._create_list_line_from_match(match)


class UserHandleProcessor(RegexProcessor):
    """
    Processor which replaces user handles
    """

    regex = re.compile(
        r"((?<=\A)|(?<=\s)|(?<=[^@\w]))(?P<handle>@(?P<username>[A-Za-z0-9_\-.]+))"
    )

    @classmethod
    def process_match(cls, context: Context, match: re.Match) -> str:
        username = match.group("username")

        new_username = context.get_new_user_name(username)
        if not new_username:
            raise ValueError(
                f"cannot replace @-mention of {username} with empty username"
            )

        return f"@{new_username}"


class PerLineProcessor(BaseProcessor):
    processors = (
        UserHandleProcessor,
        HeaderLineProcessor,
        BulletListProcessor,
        LinkProcessor,
        PasteProcessor,
        FileProcessor,
        RevisionProcessor,
        TaskProcessor,
        CommitProcessor,
        CheckboxProcessor,
    )

    code_marker_regex = re.compile(r"\A```(lines=[0-9]+)?\Z")

    # Regex is applied on a stripped line which starts with space.
    implicit_code_marker_ignore_regex = re.compile(r"\A([\-\*#0-9])|(\[.?\])")

    @classmethod
    def process(cls, context: Context, text: str) -> str:
        new_text = ""

        is_inside_code_block = False
        need_close_implicit = False

        for line in text.splitlines(keepends=True):
            if cls._is_explicit_code_marker(line):
                is_inside_code_block = not is_inside_code_block
                new_text += line
                continue

            if cls._is_implicit_code_marker(line):
                if not is_inside_code_block:
                    is_inside_code_block = True
                    need_close_implicit = True
                    new_text += "```\n"
            elif need_close_implicit:
                new_text += "```\n"
                need_close_implicit = False
                is_inside_code_block = False

            if is_inside_code_block:
                if need_close_implicit:
                    line = line[2:]
                new_text += line
                continue

            new_line = line

            for processor in cls.processors:
                new_line = processor.process(context, new_line)

            new_text += new_line

        return new_text

    @classmethod
    def _is_explicit_code_marker(cls, line: str) -> bool:
        clean_line = line.strip()

        if not clean_line.startswith("```"):
            return False

        if clean_line == "```":
            return True

        return cls.code_marker_regex.match(clean_line)

    @classmethod
    def _is_implicit_code_marker(cls, line: str) -> bool:
        if not line.startswith("  "):
            return False

        clean_line = line.strip()
        if not clean_line:
            return True

        return not cls.implicit_code_marker_ignore_regex.match(clean_line)


def process_markup_to_markdown(context: Context, markup: str) -> str:
    """
    Process ReMarkup text from Phabricator into markdown of Gitea

    This processing performs modification of the markup syntax, as well as expands monogram
    references (such as F123) to an actual embedded content or a link to an externally hosted
    file.
    """

    processors = (
        SpecialCharacterProcessor,
        BoldProcessor,
        ItalicProcessor,
        TableProcessor,
        NumberListProcessor,
        QuoteProcessor,
        PerLineProcessor,
    )

    markdown = markup

    for processor in processors:
        markdown = processor.process(context, markdown)

    return markdown
