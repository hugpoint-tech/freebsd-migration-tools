# GPGKey

GPGKey a user GPG key to sign commit and tag in repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_certify** | **bool** |  | [optional] 
**can_encrypt_comms** | **bool** |  | [optional] 
**can_encrypt_storage** | **bool** |  | [optional] 
**can_sign** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**emails** | [**[GPGKeyEmail]**](GPGKeyEmail.md) |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**key_id** | **str** |  | [optional] 
**primary_key_id** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**subkeys** | [**[GPGKey]**](GPGKey.md) |  | [optional] 
**verified** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


