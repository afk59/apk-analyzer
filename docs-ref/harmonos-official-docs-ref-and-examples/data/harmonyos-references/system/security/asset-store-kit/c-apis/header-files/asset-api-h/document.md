# asset\_api.h

#### Overview

Defines the functions for accessing assets.

**File to include**: <asset/asset\_api.h>

**Library**: libasset\_ndk.z.so

**System capability**: SystemCapability.Security.Asset

**Since**: 11

**Related module**: [AssetApi](../../modules/assetapi/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_Asset\_Add(const Asset\_Attr \*attributes, uint32\_t attrCnt)](#oh_asset_add) | 
Adds an asset.

To set the [Asset\_Tag](../asset-type-h/document.md#asset_tag).**ASSET\_TAG\_IS\_PERSISTENT** attribute, request the **ohos.permission.STORE\_PERSISTENT\_DATA** permission.

 |
| [int32\_t OH\_Asset\_Remove(const Asset\_Attr \*query, uint32\_t queryCnt)](#oh_asset_remove) | Removes one or more assets. |
| [int32\_t OH\_Asset\_Update(const Asset\_Attr \*query, uint32\_t queryCnt, const Asset\_Attr \*attributesToUpdate, uint32\_t updateCnt)](#oh_asset_update) | Updates an asset. |
| [int32\_t OH\_Asset\_PreQuery(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_Blob \*challenge)](#oh_asset_prequery) | Performs preprocessing for the asset query. This function is used when user authentication is required for the access to the asset. |
| [int32\_t OH\_Asset\_Query(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_ResultSet \*resultSet)](#oh_asset_query) | Queries one or more assets. |
| [int32\_t OH\_Asset\_PostQuery(const Asset\_Attr \*handle, uint32\_t handleCnt)](#oh_asset_postquery) | Performs postprocessing for the asset query. This function is used when user authentication is required for the access to the asset. |
| [int32\_t OH\_Asset\_QuerySyncResult(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_SyncResult \*syncResult)](#oh_asset_querysyncresult) | Queries the sync result of an asset. |
| [Asset\_Attr \*OH\_Asset\_ParseAttr(const Asset\_Result \*result, Asset\_Tag tag)](#oh_asset_parseattr) | Parses the query result and obtains the specified attribute. |
| [void OH\_Asset\_FreeBlob(Asset\_Blob \*blob)](#oh_asset_freeblob) | Releases the memory occupied by the challenge value. |
| [void OH\_Asset\_FreeResultSet(Asset\_ResultSet \*resultSet)](#oh_asset_freeresultset) | Releases the memory occupied by the query result. |

#### Function Description

#### \[h2\]OH\_Asset\_Add()

int32\_t OH\_Asset\_Add(const Asset\_Attr \*attributes, uint32\_t attrCnt)

**Description**

Adds an asset.

To set the [Asset\_Tag](../asset-type-h/document.md#asset_tag).**ASSET\_TAG\_IS\_PERSISTENT** attribute, request the **ohos.permission.STORE\_PERSISTENT\_DATA** permission.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*attributes | Attributes of the asset to add. |
| uint32\_t attrCnt | Number of attributes of the asset to add. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_PERMISSION\_DENIED = 201: The caller is not a system application.

ASSET\_INVALID\_ARGUMENT = 401: invalid parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. The parameter type is incorrect.

3\. Parameter verification failed.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_DUPLICATED = 24000003: The asset already exists.

ASSET\_STATUS\_MISMATCH = 24000005: The screen lock status is incorrect.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_DATA\_CORRUPTED = 24000007: The asset is corrupted.

ASSET\_DATABASE\_ERROR = 24000008: The database operation failed.

ASSET\_CRYPTO\_ERROR = 24000009: The cryptographic operation failed.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

ASSET\_FILE\_OPERATION\_ERROR = 24000014: The file operation failed.

ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015: Failed to obtain the system time.

 |

#### \[h2\]OH\_Asset\_Remove()

int32\_t OH\_Asset\_Remove(const Asset\_Attr \*query, uint32\_t queryCnt)

**Description**

Removes one or more assets.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*query | Attributes of the asset to remove. |
| uint32\_t queryCnt | Number of attributes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_INVALID\_ARGUMENT = 401: invalid parameter. Possible causes:

1\. The parameter type is incorrect.

2\. Parameter verification failed.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_NOT\_FOUND = 24000002: The asset is not found.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_DATA\_CORRUPTED = 24000007: The asset is corrupted.

ASSET\_DATABASE\_ERROR = 24000008: The database operation failed.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015: Failed to obtain the system time.

 |

#### \[h2\]OH\_Asset\_Update()

int32\_t OH\_Asset\_Update(const Asset\_Attr \*query, uint32\_t queryCnt,const Asset\_Attr \*attributesToUpdate, uint32\_t updateCnt)

**Description**

Updates an asset.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*query | Attributes of the asset to update. |
| uint32\_t queryCnt | Number of attributes to update. |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*attributesToUpdate | New attributes of the asset. |
| uint32\_t updateCnt | Number of new attributes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_INVALID\_ARGUMENT = 401: invalid parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. The parameter type is incorrect.

3\. Parameter verification failed.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_NOT\_FOUND = 24000002: The asset is not found.

ASSET\_STATUS\_MISMATCH = 24000005: The screen lock status is incorrect.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_DATA\_CORRUPTED = 24000007: The asset is corrupted.

ASSET\_DATABASE\_ERROR = 24000008: The database operation failed.

ASSET\_CRYPTO\_ERROR = 24000009: The cryptographic operation failed.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015: Failed to obtain the system time.

 |

#### \[h2\]OH\_Asset\_PreQuery()

int32\_t OH\_Asset\_PreQuery(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_Blob \*challenge)

**Description**

Performs preprocessing for the asset query. This API is used when user authentication is required for the access to the asset.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*query | Attributes of the asset to query. |
| uint32\_t queryCnt | Number of attributes. |
| [Asset\_Blob](../../structs/asset-blob/document.md) \*challenge | Challenge value, which is used when [OH\_Asset\_Query](#oh_asset_query) is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_INVALID\_ARGUMENT = 401: invalid parameter. Possible causes:

1\. The parameter type is incorrect.

2\. Parameter verification failed.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_NOT\_FOUND = 24000002: The asset is not found.

ASSET\_STATUS\_MISMATCH = 24000005: The screen lock status is incorrect.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_DATA\_CORRUPTED = 24000007: The asset is corrupted.

ASSET\_DATABASE\_ERROR = 24000008: The database operation failed.

ASSET\_CRYPTO\_ERROR = 24000009: The cryptographic operation failed.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

ASSET\_LIMIT\_EXCEEDED = 24000016: The number of cached assets reaches the limit.

ASSET\_UNSUPPORTED = 24000017: This function is not supported.

 |

#### \[h2\]OH\_Asset\_Query()

int32\_t OH\_Asset\_Query(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_ResultSet \*resultSet)

**Description**

Queries one or more assets.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*query | Attributes of the asset to query. |
| uint32\_t queryCnt | Number of attributes. |
| [Asset\_ResultSet](../../structs/asset-resultset/document.md) \*resultSet | Array of query results. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_INVALID\_ARGUMENT = 401: invalid parameter. Possible causes:

1\. The parameter type is incorrect.

2\. Parameter verification failed.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_NOT\_FOUND = 24000002: The asset is not found.

ASSET\_ACCESS\_DENIED = 24000004: The access is denied.

ASSET\_STATUS\_MISMATCH = 24000005: The screen lock status is incorrect.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_DATA\_CORRUPTED = 24000007: The asset is corrupted.

ASSET\_DATABASE\_ERROR = 24000008: The database operation failed.

ASSET\_CRYPTO\_ERROR = 24000009: The cryptographic operation failed.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

ASSET\_UNSUPPORTED = 24000017: This function is not supported.

 |

#### \[h2\]OH\_Asset\_PostQuery()

int32\_t OH\_Asset\_PostQuery(const Asset\_Attr \*handle, uint32\_t handleCnt)

**Description**

Performs postprocessing for the asset query. This API is used when user authentication is required for the access to the asset.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*handle | Handle of the query operation, including the challenge value returned by [OH\_Asset\_PreQuery](#oh_asset_prequery). |
| uint32\_t handleCnt | Number of elements in the handle attribute set. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_INVALID\_ARGUMENT = 401: invalid parameter. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. The parameter type is incorrect.

3\. Parameter verification failed.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

 |

#### \[h2\]OH\_Asset\_QuerySyncResult()

int32\_t OH\_Asset\_QuerySyncResult(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_SyncResult \*syncResult)

**Description**

Queries the sync result of an asset.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Attr](../../structs/asset-attr/document.md) \*query | Attributes of the asset to query the sync result. |
| uint32\_t queryCnt | Number of attributes. |
| [Asset\_SyncResult](../../structs/asset-syncresult/document.md) \*syncResult | Sync result of the queried asset. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[Asset\_ResultCode](../asset-type-h/document.md#asset_resultcode):

ASSET\_SUCCESS = 0: Operation succeeded.

ASSET\_SERVICE\_UNAVAILABLE = 24000001: The asset service is unavailable.

ASSET\_OUT\_OF\_MEMORY = 24000006: The system memory is insufficient.

ASSET\_IPC\_ERROR = 24000010: The IPC failed.

ASSET\_BMS\_ERROR = 24000011: The bundle manager service is abnormal.

ASSET\_ACCOUNT\_ERROR = 24000012: The account system service is abnormal.

ASSET\_ACCESS\_TOKEN\_ERROR = 24000013: The access token service is abnormal.

ASSET\_FILE\_OPERATION\_ERROR = 24000014: The file operation failed.

ASSET\_PARAM\_VERIFICATION\_FAILED = 24000018: Parameter verification failed.

 |

#### \[h2\]OH\_Asset\_ParseAttr()

Asset\_Attr \*OH\_Asset\_ParseAttr(const Asset\_Result \*result, Asset\_Tag tag)

**Description**

Parses the query result and obtains the specified attribute.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [Asset\_Result](../../structs/asset-result/document.md) \*result | Query result returned by [OH\_Asset\_Query](#oh_asset_query). |
| [Asset\_Tag](../asset-type-h/document.md#asset_tag) tag | Key of the attribute to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Asset\_Attr](../../structs/asset-attr/document.md) | Returns **Asset\_Attr** obtained if the operation is successful; returns **NULL** otherwise. The attribute does not need to be released by the service. |

#### \[h2\]OH\_Asset\_FreeBlob()

void OH\_Asset\_FreeBlob(Asset\_Blob \*blob)

**Description**

Releases the memory occupied by the challenge value.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Asset\_Blob](../../structs/asset-blob/document.md) \*blob | Challenge value returned by [OH\_Asset\_PreQuery](#oh_asset_prequery). |

#### \[h2\]OH\_Asset\_FreeResultSet()

void OH\_Asset\_FreeResultSet(Asset\_ResultSet \*resultSet)

**Description**

Releases the memory occupied by the query result.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Asset\_ResultSet](../../structs/asset-resultset/document.md) \*resultSet | Query result returned by [OH\_Asset\_Query](#oh_asset_query). |
