# CreateUserOption

CreateUserOption create user options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**username** | **str** |  | 
**created_at** | **datetime** | For back-dating user creation. Useful when users are migrated from other systems. If omitted, the user&#39;s creation timestamp will be set to \&quot;now\&quot;. | [optional] 
**full_name** | **str** |  | [optional] 
**login_name** | **str** |  | [optional] 
**must_change_password** | **bool** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**send_notify** | **bool** |  | [optional] 
**source_id** | **int** |  | [optional] 
**visibility** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


