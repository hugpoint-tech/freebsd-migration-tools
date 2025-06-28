# phab_tool.gitea_api.IssueApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_add_label**](IssueApi.md#issue_add_label) | **POST** /repos/{owner}/{repo}/issues/{index}/labels | Add a label to an issue
[**issue_add_subscription**](IssueApi.md#issue_add_subscription) | **PUT** /repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | Subscribe user to issue
[**issue_add_time**](IssueApi.md#issue_add_time) | **POST** /repos/{owner}/{repo}/issues/{index}/times | Add tracked time to a issue
[**issue_check_subscription**](IssueApi.md#issue_check_subscription) | **GET** /repos/{owner}/{repo}/issues/{index}/subscriptions/check | Check if user is subscribed to an issue
[**issue_clear_labels**](IssueApi.md#issue_clear_labels) | **DELETE** /repos/{owner}/{repo}/issues/{index}/labels | Remove all labels from an issue
[**issue_create_comment**](IssueApi.md#issue_create_comment) | **POST** /repos/{owner}/{repo}/issues/{index}/comments | Add a comment to an issue
[**issue_create_issue**](IssueApi.md#issue_create_issue) | **POST** /repos/{owner}/{repo}/issues | Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_create_issue_attachment**](IssueApi.md#issue_create_issue_attachment) | **POST** /repos/{owner}/{repo}/issues/{index}/assets | Create an issue attachment
[**issue_create_issue_comment_attachment**](IssueApi.md#issue_create_issue_comment_attachment) | **POST** /repos/{owner}/{repo}/issues/comments/{id}/assets | Create a comment attachment
[**issue_create_label**](IssueApi.md#issue_create_label) | **POST** /repos/{owner}/{repo}/labels | Create a label
[**issue_create_milestone**](IssueApi.md#issue_create_milestone) | **POST** /repos/{owner}/{repo}/milestones | Create a milestone
[**issue_delete**](IssueApi.md#issue_delete) | **DELETE** /repos/{owner}/{repo}/issues/{index} | Delete an issue
[**issue_delete_comment**](IssueApi.md#issue_delete_comment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{id} | Delete a comment
[**issue_delete_comment_deprecated**](IssueApi.md#issue_delete_comment_deprecated) | **DELETE** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Delete a comment
[**issue_delete_comment_reaction**](IssueApi.md#issue_delete_comment_reaction) | **DELETE** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Remove a reaction from a comment of an issue
[**issue_delete_issue_attachment**](IssueApi.md#issue_delete_issue_attachment) | **DELETE** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Delete an issue attachment
[**issue_delete_issue_comment_attachment**](IssueApi.md#issue_delete_issue_comment_attachment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Delete a comment attachment
[**issue_delete_issue_reaction**](IssueApi.md#issue_delete_issue_reaction) | **DELETE** /repos/{owner}/{repo}/issues/{index}/reactions | Remove a reaction from an issue
[**issue_delete_label**](IssueApi.md#issue_delete_label) | **DELETE** /repos/{owner}/{repo}/labels/{id} | Delete a label
[**issue_delete_milestone**](IssueApi.md#issue_delete_milestone) | **DELETE** /repos/{owner}/{repo}/milestones/{id} | Delete a milestone
[**issue_delete_stop_watch**](IssueApi.md#issue_delete_stop_watch) | **DELETE** /repos/{owner}/{repo}/issues/{index}/stopwatch/delete | Delete an issue&#39;s existing stopwatch.
[**issue_delete_subscription**](IssueApi.md#issue_delete_subscription) | **DELETE** /repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | Unsubscribe user from issue
[**issue_delete_time**](IssueApi.md#issue_delete_time) | **DELETE** /repos/{owner}/{repo}/issues/{index}/times/{id} | Delete specific tracked time
[**issue_edit_comment**](IssueApi.md#issue_edit_comment) | **PATCH** /repos/{owner}/{repo}/issues/comments/{id} | Edit a comment
[**issue_edit_comment_deprecated**](IssueApi.md#issue_edit_comment_deprecated) | **PATCH** /repos/{owner}/{repo}/issues/{index}/comments/{id} | Edit a comment
[**issue_edit_issue**](IssueApi.md#issue_edit_issue) | **PATCH** /repos/{owner}/{repo}/issues/{index} | Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_edit_issue_attachment**](IssueApi.md#issue_edit_issue_attachment) | **PATCH** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Edit an issue attachment
[**issue_edit_issue_comment_attachment**](IssueApi.md#issue_edit_issue_comment_attachment) | **PATCH** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Edit a comment attachment
[**issue_edit_issue_deadline**](IssueApi.md#issue_edit_issue_deadline) | **POST** /repos/{owner}/{repo}/issues/{index}/deadline | Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
[**issue_edit_label**](IssueApi.md#issue_edit_label) | **PATCH** /repos/{owner}/{repo}/labels/{id} | Update a label
[**issue_edit_milestone**](IssueApi.md#issue_edit_milestone) | **PATCH** /repos/{owner}/{repo}/milestones/{id} | Update a milestone
[**issue_get_comment**](IssueApi.md#issue_get_comment) | **GET** /repos/{owner}/{repo}/issues/comments/{id} | Get a comment
[**issue_get_comment_reactions**](IssueApi.md#issue_get_comment_reactions) | **GET** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Get a list of reactions from a comment of an issue
[**issue_get_comments**](IssueApi.md#issue_get_comments) | **GET** /repos/{owner}/{repo}/issues/{index}/comments | List all comments on an issue
[**issue_get_comments_and_timeline**](IssueApi.md#issue_get_comments_and_timeline) | **GET** /repos/{owner}/{repo}/issues/{index}/timeline | List all comments and events on an issue
[**issue_get_issue**](IssueApi.md#issue_get_issue) | **GET** /repos/{owner}/{repo}/issues/{index} | Get an issue
[**issue_get_issue_attachment**](IssueApi.md#issue_get_issue_attachment) | **GET** /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | Get an issue attachment
[**issue_get_issue_comment_attachment**](IssueApi.md#issue_get_issue_comment_attachment) | **GET** /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id} | Get a comment attachment
[**issue_get_issue_reactions**](IssueApi.md#issue_get_issue_reactions) | **GET** /repos/{owner}/{repo}/issues/{index}/reactions | Get a list reactions of an issue
[**issue_get_label**](IssueApi.md#issue_get_label) | **GET** /repos/{owner}/{repo}/labels/{id} | Get a single label
[**issue_get_labels**](IssueApi.md#issue_get_labels) | **GET** /repos/{owner}/{repo}/issues/{index}/labels | Get an issue&#39;s labels
[**issue_get_milestone**](IssueApi.md#issue_get_milestone) | **GET** /repos/{owner}/{repo}/milestones/{id} | Get a milestone
[**issue_get_milestones_list**](IssueApi.md#issue_get_milestones_list) | **GET** /repos/{owner}/{repo}/milestones | Get all of a repository&#39;s opened milestones
[**issue_get_repo_comments**](IssueApi.md#issue_get_repo_comments) | **GET** /repos/{owner}/{repo}/issues/comments | List all comments in a repository
[**issue_list_issue_attachments**](IssueApi.md#issue_list_issue_attachments) | **GET** /repos/{owner}/{repo}/issues/{index}/assets | List issue&#39;s attachments
[**issue_list_issue_comment_attachments**](IssueApi.md#issue_list_issue_comment_attachments) | **GET** /repos/{owner}/{repo}/issues/comments/{id}/assets | List comment&#39;s attachments
[**issue_list_issues**](IssueApi.md#issue_list_issues) | **GET** /repos/{owner}/{repo}/issues | List a repository&#39;s issues
[**issue_list_labels**](IssueApi.md#issue_list_labels) | **GET** /repos/{owner}/{repo}/labels | Get all of a repository&#39;s labels
[**issue_post_comment_reaction**](IssueApi.md#issue_post_comment_reaction) | **POST** /repos/{owner}/{repo}/issues/comments/{id}/reactions | Add a reaction to a comment of an issue
[**issue_post_issue_reaction**](IssueApi.md#issue_post_issue_reaction) | **POST** /repos/{owner}/{repo}/issues/{index}/reactions | Add a reaction to an issue
[**issue_remove_label**](IssueApi.md#issue_remove_label) | **DELETE** /repos/{owner}/{repo}/issues/{index}/labels/{id} | Remove a label from an issue
[**issue_replace_labels**](IssueApi.md#issue_replace_labels) | **PUT** /repos/{owner}/{repo}/issues/{index}/labels | Replace an issue&#39;s labels
[**issue_reset_time**](IssueApi.md#issue_reset_time) | **DELETE** /repos/{owner}/{repo}/issues/{index}/times | Reset a tracked time of an issue
[**issue_search_issues**](IssueApi.md#issue_search_issues) | **GET** /repos/issues/search | Search for issues across the repositories that the user has access to
[**issue_start_stop_watch**](IssueApi.md#issue_start_stop_watch) | **POST** /repos/{owner}/{repo}/issues/{index}/stopwatch/start | Start stopwatch on an issue.
[**issue_stop_stop_watch**](IssueApi.md#issue_stop_stop_watch) | **POST** /repos/{owner}/{repo}/issues/{index}/stopwatch/stop | Stop an issue&#39;s existing stopwatch.
[**issue_subscriptions**](IssueApi.md#issue_subscriptions) | **GET** /repos/{owner}/{repo}/issues/{index}/subscriptions | Get users who subscribed on an issue.
[**issue_tracked_times**](IssueApi.md#issue_tracked_times) | **GET** /repos/{owner}/{repo}/issues/{index}/times | List an issue&#39;s tracked times


# **issue_add_label**
> [Label] issue_add_label(owner, repo, index)

Add a label to an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.label import Label
from phab_tool.gitea_api.model.issue_labels_option import IssueLabelsOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    body = IssueLabelsOption(
        labels=[
            1,
        ],
    ) # IssueLabelsOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a label to an issue
        api_response = api_instance.issue_add_label(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_add_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a label to an issue
        api_response = api_instance.issue_add_label(owner, repo, index, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_add_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**IssueLabelsOption**](IssueLabelsOption.md)|  | [optional]

### Return type

[**[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LabelList |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_add_subscription**
> issue_add_subscription(owner, repo, index, user)

Subscribe user to issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    user = "user_example" # str | user to subscribe

    # example passing only required values which don't have defaults set
    try:
        # Subscribe user to issue
        api_instance.issue_add_subscription(owner, repo, index, user)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_add_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **user** | **str**| user to subscribe |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Already subscribed |  -  |
**201** | Successfully Subscribed |  -  |
**304** | User can only subscribe itself if he is no admin |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_add_time**
> TrackedTime issue_add_time(owner, repo, index)

Add tracked time to a issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.tracked_time import TrackedTime
from phab_tool.gitea_api.model.add_time_option import AddTimeOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    body = AddTimeOption(
        created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        time=1,
        user_name="user_name_example",
    ) # AddTimeOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add tracked time to a issue
        api_response = api_instance.issue_add_time(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_add_time: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add tracked time to a issue
        api_response = api_instance.issue_add_time(owner, repo, index, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_add_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**AddTimeOption**](AddTimeOption.md)|  | [optional]

### Return type

[**TrackedTime**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackedTime |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_check_subscription**
> WatchInfo issue_check_subscription(owner, repo, index)

Check if user is subscribed to an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.watch_info import WatchInfo
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue

    # example passing only required values which don't have defaults set
    try:
        # Check if user is subscribed to an issue
        api_response = api_instance.issue_check_subscription(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_check_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WatchInfo |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_clear_labels**
> issue_clear_labels(owner, repo, index)

Remove all labels from an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue

    # example passing only required values which don't have defaults set
    try:
        # Remove all labels from an issue
        api_instance.issue_clear_labels(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_clear_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_comment**
> Comment issue_create_comment(owner, repo, index)

Add a comment to an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.comment import Comment
from phab_tool.gitea_api.model.create_issue_comment_option import CreateIssueCommentOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    body = CreateIssueCommentOption(
        body="body_example",
    ) # CreateIssueCommentOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a comment to an issue
        api_response = api_instance.issue_create_comment(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a comment to an issue
        api_response = api_instance.issue_create_comment(owner, repo, index, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**CreateIssueCommentOption**](CreateIssueCommentOption.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comment |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_issue**
> Issue issue_create_issue(owner, repo)

Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.issue import Issue
from phab_tool.gitea_api.model.create_issue_option import CreateIssueOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateIssueOption(
        assignee="assignee_example",
        assignees=[
            "assignees_example",
        ],
        body="body_example",
        closed=True,
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        labels=[
            1,
        ],
        milestone=1,
        ref="ref_example",
        title="title_example",
    ) # CreateIssueOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_create_issue(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_create_issue(owner, repo, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateIssueOption**](CreateIssueOption.md)|  | [optional]

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Issue |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**412** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_issue_attachment**
> Attachment issue_create_issue_attachment(owner, repo, index, attachment)

Create an issue attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    attachment = open('/path/to/file', 'rb') # file_type | attachment to upload
    name = "name_example" # str | name of the attachment (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an issue attachment
        api_response = api_instance.issue_create_issue_attachment(owner, repo, index, attachment)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an issue attachment
        api_response = api_instance.issue_create_issue_attachment(owner, repo, index, attachment, name=name)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **attachment** | **file_type**| attachment to upload |
 **name** | **str**| name of the attachment | [optional]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_issue_comment_attachment**
> Attachment issue_create_issue_comment_attachment(owner, repo, id, attachment)

Create a comment attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment
    attachment = open('/path/to/file', 'rb') # file_type | attachment to upload
    name = "name_example" # str | name of the attachment (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a comment attachment
        api_response = api_instance.issue_create_issue_comment_attachment(owner, repo, id, attachment)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_comment_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a comment attachment
        api_response = api_instance.issue_create_issue_comment_attachment(owner, repo, id, attachment, name=name)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_issue_comment_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment |
 **attachment** | **file_type**| attachment to upload |
 **name** | **str**| name of the attachment | [optional]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_label**
> Label issue_create_label(owner, repo)

Create a label

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.create_label_option import CreateLabelOption
from phab_tool.gitea_api.model.label import Label
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateLabelOption(
        color="#00aabb",
        description="description_example",
        name="name_example",
    ) # CreateLabelOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a label
        api_response = api_instance.issue_create_label(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a label
        api_response = api_instance.issue_create_label(owner, repo, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateLabelOption**](CreateLabelOption.md)|  | [optional]

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Label |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_create_milestone**
> Milestone issue_create_milestone(owner, repo)

Create a milestone

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.create_milestone_option import CreateMilestoneOption
from phab_tool.gitea_api.model.milestone import Milestone
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateMilestoneOption(
        description="description_example",
        due_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        state="open",
        title="title_example",
    ) # CreateMilestoneOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a milestone
        api_response = api_instance.issue_create_milestone(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_milestone: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a milestone
        api_response = api_instance.issue_create_milestone(owner, repo, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_create_milestone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateMilestoneOption**](CreateMilestoneOption.md)|  | [optional]

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Milestone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete**
> issue_delete(owner, repo, index)

Delete an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of issue to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete an issue
        api_instance.issue_delete(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of issue to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_comment**
> issue_delete_comment(owner, repo, id)

Delete a comment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of comment to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a comment
        api_instance.issue_delete_comment(owner, repo, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of comment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_comment_deprecated**
> issue_delete_comment_deprecated(owner, repo, index, id)

Delete a comment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | this parameter is ignored
    id = 1 # int | id of comment to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a comment
        api_instance.issue_delete_comment_deprecated(owner, repo, index, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| this parameter is ignored |
 **id** | **int**| id of comment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_comment_reaction**
> issue_delete_comment_reaction(owner, repo, id)

Remove a reaction from a comment of an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_reaction_option import EditReactionOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment to edit
    content = EditReactionOption(
        content="content_example",
    ) # EditReactionOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a reaction from a comment of an issue
        api_instance.issue_delete_comment_reaction(owner, repo, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment_reaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a reaction from a comment of an issue
        api_instance.issue_delete_comment_reaction(owner, repo, id, content=content)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_comment_reaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment to edit |
 **content** | [**EditReactionOption**](EditReactionOption.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_issue_attachment**
> issue_delete_issue_attachment(owner, repo, index, attachment_id)

Delete an issue attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    attachment_id = 1 # int | id of the attachment to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete an issue attachment
        api_instance.issue_delete_issue_attachment(owner, repo, index, attachment_id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **attachment_id** | **int**| id of the attachment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_issue_comment_attachment**
> issue_delete_issue_comment_attachment(owner, repo, id, attachment_id)

Delete a comment attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment
    attachment_id = 1 # int | id of the attachment to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a comment attachment
        api_instance.issue_delete_issue_comment_attachment(owner, repo, id, attachment_id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_comment_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment |
 **attachment_id** | **int**| id of the attachment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_issue_reaction**
> issue_delete_issue_reaction(owner, repo, index)

Remove a reaction from an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_reaction_option import EditReactionOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    content = EditReactionOption(
        content="content_example",
    ) # EditReactionOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a reaction from an issue
        api_instance.issue_delete_issue_reaction(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_reaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a reaction from an issue
        api_instance.issue_delete_issue_reaction(owner, repo, index, content=content)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_issue_reaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **content** | [**EditReactionOption**](EditReactionOption.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_label**
> issue_delete_label(owner, repo, id)

Delete a label

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the label to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a label
        api_instance.issue_delete_label(owner, repo, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the label to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_milestone**
> issue_delete_milestone(owner, repo, id)

Delete a milestone

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = "id_example" # str | the milestone to delete, identified by ID and if not available by name

    # example passing only required values which don't have defaults set
    try:
        # Delete a milestone
        api_instance.issue_delete_milestone(owner, repo, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_milestone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **str**| the milestone to delete, identified by ID and if not available by name |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_stop_watch**
> issue_delete_stop_watch(owner, repo, index)

Delete an issue's existing stopwatch.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to stop the stopwatch on

    # example passing only required values which don't have defaults set
    try:
        # Delete an issue's existing stopwatch.
        api_instance.issue_delete_stop_watch(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_stop_watch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to stop the stopwatch on |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | Not repo writer, user does not have rights to toggle stopwatch |  -  |
**404** | APINotFound is a not found empty response |  -  |
**409** | Cannot cancel a non existent stopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_subscription**
> issue_delete_subscription(owner, repo, index, user)

Unsubscribe user from issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    user = "user_example" # str | user witch unsubscribe

    # example passing only required values which don't have defaults set
    try:
        # Unsubscribe user from issue
        api_instance.issue_delete_subscription(owner, repo, index, user)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **user** | **str**| user witch unsubscribe |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Already unsubscribed |  -  |
**201** | Successfully Unsubscribed |  -  |
**304** | User can only subscribe itself if he is no admin |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_delete_time**
> issue_delete_time(owner, repo, index, id)

Delete specific tracked time

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    id = 1 # int | id of time to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete specific tracked time
        api_instance.issue_delete_time(owner, repo, index, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_delete_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **id** | **int**| id of time to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_comment**
> Comment issue_edit_comment(owner, repo, id)

Edit a comment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_issue_comment_option import EditIssueCommentOption
from phab_tool.gitea_api.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment to edit
    body = EditIssueCommentOption(
        body="body_example",
    ) # EditIssueCommentOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment(owner, repo, id, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment to edit |
 **body** | [**EditIssueCommentOption**](EditIssueCommentOption.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment |  -  |
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_comment_deprecated**
> Comment issue_edit_comment_deprecated(owner, repo, index, id)

Edit a comment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_issue_comment_option import EditIssueCommentOption
from phab_tool.gitea_api.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | this parameter is ignored
    id = 1 # int | id of the comment to edit
    body = EditIssueCommentOption(
        body="body_example",
    ) # EditIssueCommentOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment_deprecated(owner, repo, index, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a comment
        api_response = api_instance.issue_edit_comment_deprecated(owner, repo, index, id, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_comment_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| this parameter is ignored |
 **id** | **int**| id of the comment to edit |
 **body** | [**EditIssueCommentOption**](EditIssueCommentOption.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment |  -  |
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_issue**
> Issue issue_edit_issue(owner, repo, index)

Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_issue_option import EditIssueOption
from phab_tool.gitea_api.model.issue import Issue
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to edit
    body = EditIssueOption(
        assignee="assignee_example",
        assignees=[
            "assignees_example",
        ],
        body="body_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        milestone=1,
        ref="ref_example",
        state="state_example",
        title="title_example",
        unset_due_date=True,
    ) # EditIssueOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue(owner, repo, index, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to edit |
 **body** | [**EditIssueOption**](EditIssueOption.md)|  | [optional]

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Issue |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**412** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_issue_attachment**
> Attachment issue_edit_issue_attachment(owner, repo, index, attachment_id)

Edit an issue attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_attachment_options import EditAttachmentOptions
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    attachment_id = 1 # int | id of the attachment to edit
    body = EditAttachmentOptions(
        name="name_example",
    ) # EditAttachmentOptions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an issue attachment
        api_response = api_instance.issue_edit_issue_attachment(owner, repo, index, attachment_id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an issue attachment
        api_response = api_instance.issue_edit_issue_attachment(owner, repo, index, attachment_id, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **attachment_id** | **int**| id of the attachment to edit |
 **body** | [**EditAttachmentOptions**](EditAttachmentOptions.md)|  | [optional]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_issue_comment_attachment**
> Attachment issue_edit_issue_comment_attachment(owner, repo, id, attachment_id)

Edit a comment attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_attachment_options import EditAttachmentOptions
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment
    attachment_id = 1 # int | id of the attachment to edit
    body = EditAttachmentOptions(
        name="name_example",
    ) # EditAttachmentOptions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a comment attachment
        api_response = api_instance.issue_edit_issue_comment_attachment(owner, repo, id, attachment_id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_comment_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a comment attachment
        api_response = api_instance.issue_edit_issue_comment_attachment(owner, repo, id, attachment_id, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_comment_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment |
 **attachment_id** | **int**| id of the attachment to edit |
 **body** | [**EditAttachmentOptions**](EditAttachmentOptions.md)|  | [optional]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_issue_deadline**
> IssueDeadline issue_edit_issue_deadline(owner, repo, index)

Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.issue_deadline import IssueDeadline
from phab_tool.gitea_api.model.edit_deadline_option import EditDeadlineOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to create or update a deadline on
    body = EditDeadlineOption(
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # EditDeadlineOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue_deadline(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_deadline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.issue_edit_issue_deadline(owner, repo, index, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_issue_deadline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to create or update a deadline on |
 **body** | [**EditDeadlineOption**](EditDeadlineOption.md)|  | [optional]

### Return type

[**IssueDeadline**](IssueDeadline.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IssueDeadline |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_label**
> Label issue_edit_label(owner, repo, id)

Update a label

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_label_option import EditLabelOption
from phab_tool.gitea_api.model.label import Label
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the label to edit
    body = EditLabelOption(
        color="color_example",
        description="description_example",
        name="name_example",
    ) # EditLabelOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a label
        api_response = api_instance.issue_edit_label(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a label
        api_response = api_instance.issue_edit_label(owner, repo, id, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the label to edit |
 **body** | [**EditLabelOption**](EditLabelOption.md)|  | [optional]

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_edit_milestone**
> Milestone issue_edit_milestone(owner, repo, id)

Update a milestone

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.edit_milestone_option import EditMilestoneOption
from phab_tool.gitea_api.model.milestone import Milestone
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = "id_example" # str | the milestone to edit, identified by ID and if not available by name
    body = EditMilestoneOption(
        description="description_example",
        due_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        state="state_example",
        title="title_example",
    ) # EditMilestoneOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a milestone
        api_response = api_instance.issue_edit_milestone(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_milestone: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a milestone
        api_response = api_instance.issue_edit_milestone(owner, repo, id, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_edit_milestone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **str**| the milestone to edit, identified by ID and if not available by name |
 **body** | [**EditMilestoneOption**](EditMilestoneOption.md)|  | [optional]

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Milestone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_comment**
> Comment issue_get_comment(owner, repo, id)

Get a comment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment

    # example passing only required values which don't have defaults set
    try:
        # Get a comment
        api_response = api_instance.issue_get_comment(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment |

### Return type

[**Comment**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment |  -  |
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_comment_reactions**
> [Reaction] issue_get_comment_reactions(owner, repo, id)

Get a list of reactions from a comment of an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.reaction import Reaction
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment to edit

    # example passing only required values which don't have defaults set
    try:
        # Get a list of reactions from a comment of an issue
        api_response = api_instance.issue_get_comment_reactions(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comment_reactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment to edit |

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReactionList |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_comments**
> [Comment] issue_get_comments(owner, repo, index)

List all comments on an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | if provided, only comments updated since the specified time are returned. (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | if provided, only comments updated before the provided time are returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all comments on an issue
        api_response = api_instance.issue_get_comments(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all comments on an issue
        api_response = api_instance.issue_get_comments(owner, repo, index, since=since, before=before)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **since** | **datetime**| if provided, only comments updated since the specified time are returned. | [optional]
 **before** | **datetime**| if provided, only comments updated before the provided time are returned. | [optional]

### Return type

[**[Comment]**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommentList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_comments_and_timeline**
> [TimelineComment] issue_get_comments_and_timeline(owner, repo, index)

List all comments and events on an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.timeline_comment import TimelineComment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | if provided, only comments updated since the specified time are returned. (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | if provided, only comments updated before the provided time are returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all comments and events on an issue
        api_response = api_instance.issue_get_comments_and_timeline(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments_and_timeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all comments and events on an issue
        api_response = api_instance.issue_get_comments_and_timeline(owner, repo, index, since=since, page=page, limit=limit, before=before)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_comments_and_timeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **since** | **datetime**| if provided, only comments updated since the specified time are returned. | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]
 **before** | **datetime**| if provided, only comments updated before the provided time are returned. | [optional]

### Return type

[**[TimelineComment]**](TimelineComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimelineList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_issue**
> Issue issue_get_issue(owner, repo, index)

Get an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.issue import Issue
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to get

    # example passing only required values which don't have defaults set
    try:
        # Get an issue
        api_response = api_instance.issue_get_issue(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to get |

### Return type

[**Issue**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Issue |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_issue_attachment**
> Attachment issue_get_issue_attachment(owner, repo, index, attachment_id)

Get an issue attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    attachment_id = 1 # int | id of the attachment to get

    # example passing only required values which don't have defaults set
    try:
        # Get an issue attachment
        api_response = api_instance.issue_get_issue_attachment(owner, repo, index, attachment_id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **attachment_id** | **int**| id of the attachment to get |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_issue_comment_attachment**
> Attachment issue_get_issue_comment_attachment(owner, repo, id, attachment_id)

Get a comment attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment
    attachment_id = 1 # int | id of the attachment to get

    # example passing only required values which don't have defaults set
    try:
        # Get a comment attachment
        api_response = api_instance.issue_get_issue_comment_attachment(owner, repo, id, attachment_id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_comment_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment |
 **attachment_id** | **int**| id of the attachment to get |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_issue_reactions**
> [Reaction] issue_get_issue_reactions(owner, repo, index)

Get a list reactions of an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.reaction import Reaction
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list reactions of an issue
        api_response = api_instance.issue_get_issue_reactions(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_reactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list reactions of an issue
        api_response = api_instance.issue_get_issue_reactions(owner, repo, index, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_issue_reactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Reaction]**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReactionList |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_label**
> Label issue_get_label(owner, repo, id)

Get a single label

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.label import Label
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the label to get

    # example passing only required values which don't have defaults set
    try:
        # Get a single label
        api_response = api_instance.issue_get_label(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the label to get |

### Return type

[**Label**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_labels**
> [Label] issue_get_labels(owner, repo, index)

Get an issue's labels

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.label import Label
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue

    # example passing only required values which don't have defaults set
    try:
        # Get an issue's labels
        api_response = api_instance.issue_get_labels(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |

### Return type

[**[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LabelList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_milestone**
> Milestone issue_get_milestone(owner, repo, id)

Get a milestone

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.milestone import Milestone
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = "id_example" # str | the milestone to get, identified by ID and if not available by name

    # example passing only required values which don't have defaults set
    try:
        # Get a milestone
        api_response = api_instance.issue_get_milestone(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_milestone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **str**| the milestone to get, identified by ID and if not available by name |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Milestone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_milestones_list**
> [Milestone] issue_get_milestones_list(owner, repo)

Get all of a repository's opened milestones

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.milestone import Milestone
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    state = "state_example" # str | Milestone state, Recognized values are open, closed and all. Defaults to \"open\" (optional)
    name = "name_example" # str | filter by milestone name (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all of a repository's opened milestones
        api_response = api_instance.issue_get_milestones_list(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_milestones_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all of a repository's opened milestones
        api_response = api_instance.issue_get_milestones_list(owner, repo, state=state, name=name, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_milestones_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **state** | **str**| Milestone state, Recognized values are open, closed and all. Defaults to \&quot;open\&quot; | [optional]
 **name** | **str**| filter by milestone name | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Milestone]**](Milestone.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MilestoneList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_get_repo_comments**
> [Comment] issue_get_repo_comments(owner, repo)

List all comments in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | if provided, only comments updated since the provided time are returned. (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | if provided, only comments updated before the provided time are returned. (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all comments in a repository
        api_response = api_instance.issue_get_repo_comments(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_repo_comments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all comments in a repository
        api_response = api_instance.issue_get_repo_comments(owner, repo, since=since, before=before, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_get_repo_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **since** | **datetime**| if provided, only comments updated since the provided time are returned. | [optional]
 **before** | **datetime**| if provided, only comments updated before the provided time are returned. | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Comment]**](Comment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommentList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_list_issue_attachments**
> [Attachment] issue_list_issue_attachments(owner, repo, index)

List issue's attachments

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue

    # example passing only required values which don't have defaults set
    try:
        # List issue's attachments
        api_response = api_instance.issue_list_issue_attachments(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issue_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AttachmentList |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_list_issue_comment_attachments**
> [Attachment] issue_list_issue_comment_attachments(owner, repo, id)

List comment's attachments

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment

    # example passing only required values which don't have defaults set
    try:
        # List comment's attachments
        api_response = api_instance.issue_list_issue_comment_attachments(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issue_comment_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment |

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AttachmentList |  -  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_list_issues**
> [Issue] issue_list_issues(owner, repo)

List a repository's issues

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.issue import Issue
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    state = "closed" # str | whether issue is open or closed (optional)
    labels = "labels_example" # str | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded (optional)
    q = "q_example" # str | search string (optional)
    type = "issues" # str | filter by type (issues / pulls) if set (optional)
    milestones = "milestones_example" # str | comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show items updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show items updated before the given time. This is a timestamp in RFC 3339 format (optional)
    created_by = "created_by_example" # str | Only show items which were created by the the given user (optional)
    assigned_by = "assigned_by_example" # str | Only show items for which the given user is assigned (optional)
    mentioned_by = "mentioned_by_example" # str | Only show items in which the given user was mentioned (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repository's issues
        api_response = api_instance.issue_list_issues(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issues: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repository's issues
        api_response = api_instance.issue_list_issues(owner, repo, state=state, labels=labels, q=q, type=type, milestones=milestones, since=since, before=before, created_by=created_by, assigned_by=assigned_by, mentioned_by=mentioned_by, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_list_issues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **state** | **str**| whether issue is open or closed | [optional]
 **labels** | **str**| comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded | [optional]
 **q** | **str**| search string | [optional]
 **type** | **str**| filter by type (issues / pulls) if set | [optional]
 **milestones** | **str**| comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded | [optional]
 **since** | **datetime**| Only show items updated after the given time. This is a timestamp in RFC 3339 format | [optional]
 **before** | **datetime**| Only show items updated before the given time. This is a timestamp in RFC 3339 format | [optional]
 **created_by** | **str**| Only show items which were created by the the given user | [optional]
 **assigned_by** | **str**| Only show items for which the given user is assigned | [optional]
 **mentioned_by** | **str**| Only show items in which the given user was mentioned | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Issue]**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IssueList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_list_labels**
> [Label] issue_list_labels(owner, repo)

Get all of a repository's labels

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.label import Label
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all of a repository's labels
        api_response = api_instance.issue_list_labels(owner, repo)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_list_labels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all of a repository's labels
        api_response = api_instance.issue_list_labels(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_list_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LabelList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_post_comment_reaction**
> Reaction issue_post_comment_reaction(owner, repo, id)

Add a reaction to a comment of an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.reaction import Reaction
from phab_tool.gitea_api.model.edit_reaction_option import EditReactionOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the comment to edit
    content = EditReactionOption(
        content="content_example",
    ) # EditReactionOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a reaction to a comment of an issue
        api_response = api_instance.issue_post_comment_reaction(owner, repo, id)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_post_comment_reaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a reaction to a comment of an issue
        api_response = api_instance.issue_post_comment_reaction(owner, repo, id, content=content)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_post_comment_reaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the comment to edit |
 **content** | [**EditReactionOption**](EditReactionOption.md)|  | [optional]

### Return type

[**Reaction**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction |  -  |
**201** | Reaction |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_post_issue_reaction**
> Reaction issue_post_issue_reaction(owner, repo, index)

Add a reaction to an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.reaction import Reaction
from phab_tool.gitea_api.model.edit_reaction_option import EditReactionOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    content = EditReactionOption(
        content="content_example",
    ) # EditReactionOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a reaction to an issue
        api_response = api_instance.issue_post_issue_reaction(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_post_issue_reaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a reaction to an issue
        api_response = api_instance.issue_post_issue_reaction(owner, repo, index, content=content)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_post_issue_reaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **content** | [**EditReactionOption**](EditReactionOption.md)|  | [optional]

### Return type

[**Reaction**](Reaction.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction |  -  |
**201** | Reaction |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_remove_label**
> issue_remove_label(owner, repo, index, id)

Remove a label from an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    id = 1 # int | id of the label to remove

    # example passing only required values which don't have defaults set
    try:
        # Remove a label from an issue
        api_instance.issue_remove_label(owner, repo, index, id)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_remove_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **id** | **int**| id of the label to remove |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_replace_labels**
> [Label] issue_replace_labels(owner, repo, index)

Replace an issue's labels

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.label import Label
from phab_tool.gitea_api.model.issue_labels_option import IssueLabelsOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    body = IssueLabelsOption(
        labels=[
            1,
        ],
    ) # IssueLabelsOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace an issue's labels
        api_response = api_instance.issue_replace_labels(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_replace_labels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace an issue's labels
        api_response = api_instance.issue_replace_labels(owner, repo, index, body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_replace_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **body** | [**IssueLabelsOption**](IssueLabelsOption.md)|  | [optional]

### Return type

[**[Label]**](Label.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LabelList |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_reset_time**
> issue_reset_time(owner, repo, index)

Reset a tracked time of an issue

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to add tracked time to

    # example passing only required values which don't have defaults set
    try:
        # Reset a tracked time of an issue
        api_instance.issue_reset_time(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_reset_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to add tracked time to |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_search_issues**
> [Issue] issue_search_issues()

Search for issues across the repositories that the user has access to

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.issue import Issue
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    state = "state_example" # str | whether issue is open or closed (optional)
    labels = "labels_example" # str | comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded (optional)
    milestones = "milestones_example" # str | comma separated list of milestone names. Fetch only issues that have any of this milestones. Non existent are discarded (optional)
    q = "q_example" # str | search string (optional)
    priority_repo_id = 1 # int | repository to prioritize in the results (optional)
    type = "type_example" # str | filter by type (issues / pulls) if set (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format (optional)
    assigned = True # bool | filter (issues / pulls) assigned to you, default is false (optional)
    created = True # bool | filter (issues / pulls) created by you, default is false (optional)
    mentioned = True # bool | filter (issues / pulls) mentioning you, default is false (optional)
    review_requested = True # bool | filter pulls requesting your review, default is false (optional)
    owner = "owner_example" # str | filter by owner (optional)
    team = "team_example" # str | filter by team (requires organization owner parameter to be provided) (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for issues across the repositories that the user has access to
        api_response = api_instance.issue_search_issues(state=state, labels=labels, milestones=milestones, q=q, priority_repo_id=priority_repo_id, type=type, since=since, before=before, assigned=assigned, created=created, mentioned=mentioned, review_requested=review_requested, owner=owner, team=team, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_search_issues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| whether issue is open or closed | [optional]
 **labels** | **str**| comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded | [optional]
 **milestones** | **str**| comma separated list of milestone names. Fetch only issues that have any of this milestones. Non existent are discarded | [optional]
 **q** | **str**| search string | [optional]
 **priority_repo_id** | **int**| repository to prioritize in the results | [optional]
 **type** | **str**| filter by type (issues / pulls) if set | [optional]
 **since** | **datetime**| Only show notifications updated after the given time. This is a timestamp in RFC 3339 format | [optional]
 **before** | **datetime**| Only show notifications updated before the given time. This is a timestamp in RFC 3339 format | [optional]
 **assigned** | **bool**| filter (issues / pulls) assigned to you, default is false | [optional]
 **created** | **bool**| filter (issues / pulls) created by you, default is false | [optional]
 **mentioned** | **bool**| filter (issues / pulls) mentioning you, default is false | [optional]
 **review_requested** | **bool**| filter pulls requesting your review, default is false | [optional]
 **owner** | **str**| filter by owner | [optional]
 **team** | **str**| filter by team (requires organization owner parameter to be provided) | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Issue]**](Issue.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IssueList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_start_stop_watch**
> issue_start_stop_watch(owner, repo, index)

Start stopwatch on an issue.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to create the stopwatch on

    # example passing only required values which don't have defaults set
    try:
        # Start stopwatch on an issue.
        api_instance.issue_start_stop_watch(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_start_stop_watch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to create the stopwatch on |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | APIEmpty is an empty response |  -  |
**403** | Not repo writer, user does not have rights to toggle stopwatch |  -  |
**404** | APINotFound is a not found empty response |  -  |
**409** | Cannot start a stopwatch again if it already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_stop_stop_watch**
> issue_stop_stop_watch(owner, repo, index)

Stop an issue's existing stopwatch.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue to stop the stopwatch on

    # example passing only required values which don't have defaults set
    try:
        # Stop an issue's existing stopwatch.
        api_instance.issue_stop_stop_watch(owner, repo, index)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_stop_stop_watch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue to stop the stopwatch on |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | APIEmpty is an empty response |  -  |
**403** | Not repo writer, user does not have rights to toggle stopwatch |  -  |
**404** | APINotFound is a not found empty response |  -  |
**409** | Cannot stop a non existent stopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_subscriptions**
> [User] issue_subscriptions(owner, repo, index)

Get users who subscribed on an issue.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get users who subscribed on an issue.
        api_response = api_instance.issue_subscriptions(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_subscriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get users who subscribed on an issue.
        api_response = api_instance.issue_subscriptions(owner, repo, index, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_tracked_times**
> [TrackedTime] issue_tracked_times(owner, repo, index)

List an issue's tracked times

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import phab_tool.gitea_api
from phab_tool.gitea_api.api import issue_api
from phab_tool.gitea_api.model.tracked_time import TrackedTime
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = phab_tool.gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = phab_tool.gitea_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with phab_tool.gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issue_api.IssueApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the issue
    user = "user_example" # str | optional filter by user (available for issue managers) (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show times updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show times updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List an issue's tracked times
        api_response = api_instance.issue_tracked_times(owner, repo, index)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_tracked_times: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List an issue's tracked times
        api_response = api_instance.issue_tracked_times(owner, repo, index, user=user, since=since, before=before, page=page, limit=limit)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling IssueApi->issue_tracked_times: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the issue |
 **user** | **str**| optional filter by user (available for issue managers) | [optional]
 **since** | **datetime**| Only show times updated after the given time. This is a timestamp in RFC 3339 format | [optional]
 **before** | **datetime**| Only show times updated before the given time. This is a timestamp in RFC 3339 format | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[TrackedTime]**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackedTimeList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

