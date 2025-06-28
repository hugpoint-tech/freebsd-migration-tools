"""Utility functions to get a Gitea client."""

import os
import logging
import functools

from phab_tool import gitea_api as api

_log = logging.getLogger(__name__)


@functools.lru_cache()
def api_client() -> api.ApiClient:
    """Returns an API client for communicating with a Gitea instance."""
    return new_api_client()


def new_api_client() -> api.ApiClient:
    """Constructs a new API client for communicating with a Gitea instance."""
    gitea_api_url = os.environ.get("GITEA_API_URL", "") or os.environ["GITEA_URL"]
    configuration = api.Configuration(
        host=gitea_api_url.rstrip("/") + "/api/v1",
        username=os.environ["GITEA_USERNAME"],
        password=os.environ["GITEA_PASSWORD"],
    )

    _gitea_client = api.ApiClient(configuration)
    _log.info("created API client for Gitea at %s", gitea_api_url)

    return _gitea_client
