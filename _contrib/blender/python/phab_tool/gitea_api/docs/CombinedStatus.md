# CombinedStatus

CombinedStatus holds the combined state of several statuses for a single commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_url** | **str** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**sha** | **str** |  | [optional] 
**state** | **str** | CommitStatusState holds the state of a CommitStatus It can be \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot;, \&quot;failure\&quot;, and \&quot;warning\&quot; | [optional] 
**statuses** | [**[CommitStatus]**](CommitStatus.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


