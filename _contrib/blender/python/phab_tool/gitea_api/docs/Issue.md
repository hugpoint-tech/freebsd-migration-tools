# Issue

Issue represents an issue in a repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**[Attachment]**](Attachment.md) |  | [optional] 
**assignee** | [**User**](User.md) |  | [optional] 
**assignees** | [**[User]**](User.md) |  | [optional] 
**body** | **str** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 
**comments** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**labels** | [**[Label]**](Label.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**number** | **int** |  | [optional] 
**original_author** | **str** |  | [optional] 
**original_author_id** | **int** |  | [optional] 
**pull_request** | [**PullRequestMeta**](PullRequestMeta.md) |  | [optional] 
**ref** | **str** |  | [optional] 
**repository** | [**RepositoryMeta**](RepositoryMeta.md) |  | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


