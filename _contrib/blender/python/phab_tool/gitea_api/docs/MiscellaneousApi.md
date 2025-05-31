# phab_tool.gitea_api.MiscellaneousApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_info**](MiscellaneousApi.md#get_node_info) | **GET** /nodeinfo | Returns the nodeinfo of the Gitea application
[**get_signing_key**](MiscellaneousApi.md#get_signing_key) | **GET** /signing-key.gpg | Get default signing-key.gpg
[**get_version**](MiscellaneousApi.md#get_version) | **GET** /version | Returns the version of the Gitea application
[**render_markdown**](MiscellaneousApi.md#render_markdown) | **POST** /markdown | Render a markdown document as HTML
[**render_markdown_raw**](MiscellaneousApi.md#render_markdown_raw) | **POST** /markdown/raw | Render raw markdown as HTML


# **get_node_info**
> NodeInfo get_node_info()

Returns the nodeinfo of the Gitea application

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
from phab_tool.gitea_api.api import miscellaneous_api
from phab_tool.gitea_api.model.node_info import NodeInfo
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
    api_instance = miscellaneous_api.MiscellaneousApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the nodeinfo of the Gitea application
        api_response = api_instance.get_node_info()
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling MiscellaneousApi->get_node_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeInfo**](NodeInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NodeInfo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_key**
> str get_signing_key()

Get default signing-key.gpg

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
from phab_tool.gitea_api.api import miscellaneous_api
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
    api_instance = miscellaneous_api.MiscellaneousApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get default signing-key.gpg
        api_response = api_instance.get_signing_key()
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling MiscellaneousApi->get_signing_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GPG armored public key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> ServerVersion get_version()

Returns the version of the Gitea application

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
from phab_tool.gitea_api.api import miscellaneous_api
from phab_tool.gitea_api.model.server_version import ServerVersion
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
    api_instance = miscellaneous_api.MiscellaneousApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the version of the Gitea application
        api_response = api_instance.get_version()
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling MiscellaneousApi->get_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerVersion**](ServerVersion.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServerVersion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_markdown**
> str render_markdown()

Render a markdown document as HTML

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
from phab_tool.gitea_api.api import miscellaneous_api
from phab_tool.gitea_api.model.markdown_option import MarkdownOption
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
    api_instance = miscellaneous_api.MiscellaneousApi(api_client)
    body = MarkdownOption(
        context="context_example",
        mode="mode_example",
        text="text_example",
        wiki=True,
    ) # MarkdownOption |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Render a markdown document as HTML
        api_response = api_instance.render_markdown(body=body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling MiscellaneousApi->render_markdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkdownOption**](MarkdownOption.md)|  | [optional]

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarkdownRender is a rendered markdown document |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_markdown_raw**
> str render_markdown_raw(body)

Render raw markdown as HTML

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
from phab_tool.gitea_api.api import miscellaneous_api
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
    api_instance = miscellaneous_api.MiscellaneousApi(api_client)
    body = "body_example" # str | Request body to render

    # example passing only required values which don't have defaults set
    try:
        # Render raw markdown as HTML
        api_response = api_instance.render_markdown_raw(body)
        pprint(api_response)
    except phab_tool.gitea_api.ApiException as e:
        print("Exception when calling MiscellaneousApi->render_markdown_raw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Request body to render |

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarkdownRender is a rendered markdown document |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

