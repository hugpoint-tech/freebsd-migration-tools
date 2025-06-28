import logging
import os
import shutil
from pathlib import Path

from phab_tool import common
from phabricator import Phabricator


_log = logging.getLogger(__name__)

RESOURCE_MAP = {
    "/res/phabricator/351fd46a/rsrc/externals/font/fontawesome/fontawesome-webfont.woff2?v=4.7.0": "static/fontawesome-webfont.woff2",
    "/res/phabricator/8f846797/rsrc/externals/font/lato/lato-regular.woff2": "static/lato-regular.woff2",
    "/res/phabricator/fffc0d8c/rsrc/externals/font/lato/lato-italic.woff2": "static/lato-italic.woff2",
    "/res/phabricator/389fcdb1/rsrc/externals/font/lato/lato-bold.woff2": "static/lato-bold.woff2",
    "/res/phabricator/bc7d1274/rsrc/externals/font/lato/lato-bolditalic.woff2": "static/lato-bolditalic.woff2",
    "/res/phabricator/bfbd0616/rsrc/externals/font/lato/lato-bolditalic.woff": "static/lato-bolditalic.woff",
    "/res/phabricator/9c3aec21/rsrc/externals/font/lato/lato-bolditalic.ttf": "static/lato-bolditalic.ttf",
    "/rsrc/image/avatar.png": "static/avatar.png",
}


def _ensure_and_get_webroot_dir() -> Path:
    """
    Make sure the destination website directory exists and return path to it
    """
    webroot_dir = Path(os.environ["ARCHIVE_WEBSITE_ROOT"])

    webroot_dir.mkdir(parents=True, exist_ok=True)

    return webroot_dir


def _copy_static(webroot_dir: Path):
    webroot_static_dir = webroot_dir / "static"
    template_static_dir = common.orig_dirs["bake"] / "template" / "static"

    if webroot_static_dir.exists():
        shutil.rmtree(webroot_static_dir)

    shutil.copytree(template_static_dir, webroot_static_dir)


def _make_paste(webroot_dir: Path) -> None:
    """
    Make the paste data structure of the website
    """

    _log.info("Making website directory structure for pastes")

    orig_paste_dir = common.orig_dirs["paste"]
    website_paste_dir = webroot_dir / "paste"

    for paste_json_path in orig_paste_dir.glob("**/*.json"):
        paste = common.readJsonFile(paste_json_path)
        paste_id = int(paste["id"])

        website_paste_subpath = common.subpath(paste_id, "")

        website_paste_filename = (
            website_paste_dir / website_paste_subpath / ("P" + str(paste_id) + ".txt")
        )
        website_paste_filename.parent.mkdir(parents=True, exist_ok=True)

        content = paste["attachments"]["content"]["content"]

        # TODO(sergey): Consider some read-back check, so that we do not keep overwriting the
        # same file over and over again, to be more friendly to re-iteration on the production
        # environment with backing up set up.

        website_paste_filename.write_text(content)


def _make_file(webroot_dir: Path) -> None:
    """
    Make the file data structure of the website
    """

    _log.info("Making website directory structure for files")

    orig_file_dir = common.orig_dirs["file"]
    website_file_dir = webroot_dir / "file"

    file_data_dir = common.orig_dirs["file_data"]

    for file_json_path in orig_file_dir.glob("**/*.json"):
        file = common.readJsonFile(file_json_path)
        file_id = int(file["id"])

        file_data_subpath = common.subpath(file_id, "")

        file_data_filename = file_data_dir / file_data_subpath
        if not file_data_filename.exists():
            continue

        website_file_data_dir = website_file_dir / file_data_subpath
        website_file_data_dir.mkdir(parents=True, exist_ok=True)

        website_file_data_filename = website_file_data_dir / common.make_file_name_safe(
            file["name"]
        )

        if website_file_data_filename.exists():
            if (
                website_file_data_filename.stat().st_size
                == file_data_filename.stat().st_size
            ):
                continue

        shutil.copy2(file_data_filename, website_file_data_filename)


def _replace_resource_uris(code: str, uri_prefix: str) -> str:
    for orig, new in RESOURCE_MAP.items():
        code = code.replace(orig, uri_prefix + new)

    return code


def _process_styles(webroot_dir: Path) -> None:
    webroot_style_dir = webroot_dir / "style"
    template_style_dir = common.orig_dirs["bake"] / "template" / "style"

    webroot_style_dir.mkdir(parents=True, exist_ok=True)

    for style_file in template_style_dir.iterdir():
        style = style_file.read_text()
        resolved_style = _replace_resource_uris(style, "../")

        relative_file = style_file.relative_to(template_style_dir)
        target = webroot_style_dir / relative_file

        target.write_text(resolved_style)


def _process_baked_revision_html(revision_info, baked_html: str) -> None:
    template_dir = common.orig_dirs["bake"] / "template"

    template = (template_dir / "template.html").read_text()

    content = _replace_resource_uris(baked_html, "../../../")

    resolved_content = template
    resolved_content = resolved_content.replace("{$CONTENT}", content)
    resolved_content = resolved_content.replace("{$TITLE}", revision_info["page_title"])

    return resolved_content


def _make_differential(webroot_dir: Path) -> None:
    _log.info("Making website directory structure for differentials")

    orig_revision_dir = common.orig_dirs["bake"] / "differential"
    website_differential_dir = webroot_dir / "differential"

    for revision_info_path in orig_revision_dir.glob("**/info.json"):
        revision_id = int(revision_info_path.parent.name)
        revision_dir = revision_info_path.parent

        revision_info = common.readJsonFile(revision_info_path)

        revision_subpath = common.subpath(revision_id, "")

        website_revision_dir = website_differential_dir / revision_subpath
        website_raw_diff_dir = website_revision_dir / "raw_diff"

        website_raw_diff_dir.mkdir(parents=True, exist_ok=True)

        for raw_diff in (revision_dir / "raw_diff").iterdir():
            website_raw_diff = website_raw_diff_dir / raw_diff.name
            if not website_raw_diff.exists():
                shutil.copy2(raw_diff, website_raw_diff)

        for baked_revision_html_path in revision_dir.iterdir():
            if baked_revision_html_path.suffix != ".html":
                continue

            baked_revision_html = baked_revision_html_path.read_text()
            website_revision_html = _process_baked_revision_html(
                revision_info, baked_revision_html
            )

            website_revision_html_path = (
                website_revision_dir / baked_revision_html_path.name
            )
            website_revision_html_path.write_text(website_revision_html)

        last_diff_id = revision_info["last_diff_id"]
        last_html_path = website_revision_dir / f"D{revision_id}.id{last_diff_id}.html"
        index_path = website_revision_dir / "index.html"
        index_path.write_text(last_html_path.read_text())


def _make_maniphest(webroot_dir: Path) -> None:
    _log.info("Making website directory structure for maniphest")

    orig_task_dir = common.orig_dirs["bake"] / "maniphest"
    website_maniphest_dir = webroot_dir / "maniphest"

    for task_info_path in orig_task_dir.glob("**/info.json"):
        task_id = int(task_info_path.parent.name)
        task_dir = task_info_path.parent

        task_info = common.readJsonFile(task_info_path)

        task_subpath = common.subpath(task_id, "")

        website_task_dir = website_maniphest_dir / task_subpath

        website_task_dir.mkdir(parents=True, exist_ok=True)

        baked_task_html_path = task_dir / "index.html"
        baked_task_html = baked_task_html_path.read_text()

        website_task_html = _process_baked_revision_html(task_info, baked_task_html)

        website_task_html_path = website_task_dir / baked_task_html_path.name
        website_task_html_path.write_text(website_task_html)


def pt_website(phab: Phabricator) -> None:
    """
    Generate the final state of the archive website
    """

    webroot_dir = _ensure_and_get_webroot_dir()

    _copy_static(webroot_dir)

    _make_paste(webroot_dir)
    _make_file(webroot_dir)

    _process_styles(webroot_dir)
    _make_differential(webroot_dir)
    _make_maniphest(webroot_dir)
