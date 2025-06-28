#!/usr/bin/env python3

"""
Phabricator Tool (PT) for pulling and converting Phabricator data, and preparing
for feeding into other systems (like Gitea).
"""

import sys
import logging
import time
from pathlib import Path

from dotenv import load_dotenv
from phabricator import Phabricator

# Set some things up before even importing from phab_tool:
load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)7s %(name)s %(message)s"
)


from phab_tool import convert, dump, debug, common
from phab_tool.convert import gitea_users, blender_id
from website import website


def main():
    FUNCS = {
        "pt.dump": dump.pt_dump,
        "pt.dump.maniphest": dump.pt_dump_maniphest,
        "pt.dump.maniphest.all": dump.pt_dump_maniphest_all,
        "pt.dump.maniphest.edges": dump.pt_dump_maniphest_edges,
        "pt.dump.maniphest.transactions": dump.pt_dump_maniphest_transactions,
        "pt.dump.maniphest.update": dump.pt_dump_maniphest_update,
        "pt.dump.invalid_subscribers_to_tasks_json": dump.invalid_subscribers_to_tasks_json,
        "pt.dump.differential": dump.pt_dump_differential,
        "pt.dump.differential.transactions": dump.pt_dump_differential_transactions,
        "pt.dump.differential.diffs": dump.pt_dump_differential_diffs,
        "pt.dump.files": dump.pt_dump_files,
        "pt.dump.projects": dump.pt_dump_projects,
        "pt.dump.pastes": dump.pt_dump_pastes,
        "pt.dump.repositories": dump.pt_dump_repositories,
        "pt.debug.differential.diffs.stats": debug.pt_debug_differential_diffs_stats,
        "pt.debug.users_prune": debug.pt_debug_users_prune,
        "pt.convert": convert.pt_convert,
        "pt.convert.maniphest": convert.pt_convert_maniphest,
        "pt.convert.differential": convert.pt_convert_differential,
        "pt.convert.differential.transactions": convert.pt_convert_differential_transactions,
        "pt.create.bid_import": blender_id.pt_create_bid_import,
        "pt.create.users": gitea_users.create_at_gitea,
        "pt.website": website.pt_website,
    }
    time_startup = time.monotonic()

    applet = Path(sys.argv[0]).name
    try:
        func = FUNCS[applet]
    except KeyError:
        raise SystemExit("Command %s not known" % applet)

    log = logging.getLogger(__name__)

    # Load settings from the .env file into os.environ.
    load_dotenv()

    # initialize Phabricator connection (uses ~/.arcrc to know where to connect)
    phab = Phabricator()
    # update available lookups by asking Phabricator what it can do
    phab.update_interfaces()

    restoreState()

    try:
        func(phab)
    except KeyboardInterrupt:
        print()
        print("CTRL-C caught, saving state!")
        saveState()
        raise SystemExit("stopping by user request")
    except Exception:
        log.exception("exception while running script, saving state before quitting")
        saveState()
        raise SystemExit("stopping due to exception")

    saveState()

    duration = time.monotonic() - time_startup
    log.info("Done in %s", common.humanize_duration(duration))


def saveState():
    """Save state of any updated caches, save cursor, etc. after succesful run or when catching sig-int"""
    dump.saveState()


def restoreState():
    """Load the state of important variables from disk at startup, making sure to not skip any handled by saveState"""
    dump.restoreState()


if __name__ == "__main__":
    main()
