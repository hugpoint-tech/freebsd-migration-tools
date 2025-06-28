
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.activitypub_api import ActivitypubApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from phab_tool.gitea_api.api.activitypub_api import ActivitypubApi
from phab_tool.gitea_api.api.admin_api import AdminApi
from phab_tool.gitea_api.api.issue_api import IssueApi
from phab_tool.gitea_api.api.miscellaneous_api import MiscellaneousApi
from phab_tool.gitea_api.api.notification_api import NotificationApi
from phab_tool.gitea_api.api.organization_api import OrganizationApi
from phab_tool.gitea_api.api.package_api import PackageApi
from phab_tool.gitea_api.api.repository_api import RepositoryApi
from phab_tool.gitea_api.api.settings_api import SettingsApi
from phab_tool.gitea_api.api.user_api import UserApi
