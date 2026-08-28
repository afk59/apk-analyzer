# data\_asset.h

#### Overview

Defines data asset structs.

Asset is a data struct used in data management. You can use it to set and obtain file attributes, including the name, absolute path, relative path, creation time, modification time, status, and size of a file.

**File to include**: <database/data/data\_asset.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) | Data\_Asset | 
Defines a struct for a data asset,

which provides information about a data asset.

 |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Data\_AssetStatus](#data_assetstatus) | Data\_AssetStatus | Enumerates the data asset statuses. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int OH\_Data\_Asset\_SetName(Data\_Asset \*asset, const char \*name)](#oh_data_asset_setname) | Sets the name of an asset. |
| [int OH\_Data\_Asset\_SetUri(Data\_Asset \*asset, const char \*uri)](#oh_data_asset_seturi) | Sets the absolute path (URI) of an asset in the system. |
| [int OH\_Data\_Asset\_SetPath(Data\_Asset \*asset, const char \*path)](#oh_data_asset_setpath) | Sets the relative path of an asset in the application sandbox directory. |
| [int OH\_Data\_Asset\_SetCreateTime(Data\_Asset \*asset, int64\_t createTime)](#oh_data_asset_setcreatetime) | Sets the creation time for an asset. |
| [int OH\_Data\_Asset\_SetModifyTime(Data\_Asset \*asset, int64\_t modifyTime)](#oh_data_asset_setmodifytime) | Sets the last modification time for an asset. |
| [int OH\_Data\_Asset\_SetSize(Data\_Asset \*asset, size\_t size)](#oh_data_asset_setsize) | Sets the size of an asset. |
| [int OH\_Data\_Asset\_SetStatus(Data\_Asset \*asset, Data\_AssetStatus status)](#oh_data_asset_setstatus) | Sets the status of an asset. |
| [int OH\_Data\_Asset\_GetName(Data\_Asset \*asset, char \*name, size\_t \*length)](#oh_data_asset_getname) | Obtains the name of a data asset. |
| [int OH\_Data\_Asset\_GetUri(Data\_Asset \*asset, char \*uri, size\_t \*length)](#oh_data_asset_geturi) | Obtains the absolute path of a data asset. |
| [int OH\_Data\_Asset\_GetPath(Data\_Asset \*asset, char \*path, size\_t \*length)](#oh_data_asset_getpath) | Obtains the relative path of an asset. |
| [int OH\_Data\_Asset\_GetCreateTime(Data\_Asset \*asset, int64\_t \*createTime)](#oh_data_asset_getcreatetime) | Obtains the creation time of a data asset. |
| [int OH\_Data\_Asset\_GetModifyTime(Data\_Asset \*asset, int64\_t \*modifyTime)](#oh_data_asset_getmodifytime) | Obtains the last modification time of an asset. |
| [int OH\_Data\_Asset\_GetSize(Data\_Asset \*asset, size\_t \*size)](#oh_data_asset_getsize) | Obtains the space occupied by an asset. |
| [int OH\_Data\_Asset\_GetStatus(Data\_Asset \*asset, Data\_AssetStatus \*status)](#oh_data_asset_getstatus) | Obtains the status of a data asset. |
| [Data\_Asset \*OH\_Data\_Asset\_CreateOne(void)](#oh_data_asset_createone) | Creates a [Data\_Asset](../../structs/data-asset/document.md) instance. |
| [int OH\_Data\_Asset\_DestroyOne(Data\_Asset \*asset)](#oh_data_asset_destroyone) | Destroys a [Data\_Asset](../../structs/data-asset/document.md) object and reclaims the memory occupied by the object. |
| [Data\_Asset \*\*OH\_Data\_Asset\_CreateMultiple(uint32\_t count)](#oh_data_asset_createmultiple) | Creates a specified number of [Data\_Asset](../../structs/data-asset/document.md) instances. |
| [int OH\_Data\_Asset\_DestroyMultiple(Data\_Asset \*\*assets, uint32\_t count)](#oh_data_asset_destroymultiple) | Destroys multiple [Data\_Asset](../../structs/data-asset/document.md) objects and reclaims the memory occupied by the objects. |

#### Enum Description

#### \[h2\]Data\_AssetStatus

enum Data\_AssetStatus

**Description**

Enumerates the data asset statuses.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| ASSET\_NULL = 0 | The data asset is null. |
| ASSET\_NORMAL | The asset is in normal status. |
| ASSET\_INSERT | The asset is to be inserted to the cloud. |
| ASSET\_UPDATE | The asset is to be updated to the cloud. |
| ASSET\_DELETE | The asset is to be deleted from the cloud. |
| ASSET\_ABNORMAL | The asset is in abnormal status. |
| ASSET\_DOWNLOADING | The asset is being downloaded to a local device. |

#### Function Description

#### \[h2\]OH\_Data\_Asset\_SetName()

int OH\_Data\_Asset\_SetName(Data\_Asset \*asset, const char \*name)

**Description**

Sets the name of an asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| const char \*name | Pointer to the name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_SetUri()

int OH\_Data\_Asset\_SetUri(Data\_Asset \*asset, const char \*uri)

**Description**

Sets the absolute path (URI) of an asset in the system.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| const char \*uri | Pointer to the URI to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_SetPath()

int OH\_Data\_Asset\_SetPath(Data\_Asset \*asset, const char \*path)

**Description**

Sets the relative path of an asset in the application sandbox directory.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| const char \*path | Pointer to the relative path to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_SetCreateTime()

int OH\_Data\_Asset\_SetCreateTime(Data\_Asset \*asset, int64\_t createTime)

**Description**

Sets the creation time for an asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| int64\_t createTime | Creation time to set. No specific unit. You can specify it. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_SetModifyTime()

int OH\_Data\_Asset\_SetModifyTime(Data\_Asset \*asset, int64\_t modifyTime)

**Description**

Sets the last modification time for a data asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| int64\_t modifyTime | Last modification time to set. No specific unit. You can specify it. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_SetSize()

int OH\_Data\_Asset\_SetSize(Data\_Asset \*asset, size\_t size)

**Description**

Sets the size of an asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| size\_t size | Size of the data asset to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_SetStatus()

int OH\_Data\_Asset\_SetStatus(Data\_Asset \*asset, Data\_AssetStatus status)

**Description**

Sets the status of an asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| [Data\_AssetStatus](#data_assetstatus) status | Status to set. For details, see [Data\_AssetStatus](#data_assetstatus). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_GetName()

int OH\_Data\_Asset\_GetName(Data\_Asset \*asset, char \*name, size\_t \*length)

**Description**

Obtains the name of a data asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| char \*name | Pointer to the data asset name obtained, in the form of a string. |
| size\_t \*length | Pointer to the length of the name. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_ERR** indicates that the operation fails.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_GetUri()

int OH\_Data\_Asset\_GetUri(Data\_Asset \*asset, char \*uri, size\_t \*length)

**Description**

Obtains the absolute path (URI) of a data asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| char \*uri | Pointer to the absolute path of the data asset obtained, in the form of a string. |
| size\_t \*length | Pointer to the length of the URI. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_ERR** indicates that the operation fails.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_GetPath()

int OH\_Data\_Asset\_GetPath(Data\_Asset \*asset, char \*path, size\_t \*length)

**Description**

Obtains the relative path of a data asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| char \*path | Pointer to the relative path of the data asset obtained, in the form of a string. |
| size\_t \*length | Pointer to the length of the relative path. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_ERR** indicates that the operation fails.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_GetCreateTime()

int OH\_Data\_Asset\_GetCreateTime(Data\_Asset \*asset, int64\_t \*createTime)

**Description**

Obtains the creation time of a data asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| int64\_t \*createTime | Pointer to the creation time obtained, in int64\_t format. No specific unit. You can specify it. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_ERR** indicates that the operation fails.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

**See**

Data\_Asset

#### \[h2\]OH\_Data\_Asset\_GetModifyTime()

int OH\_Data\_Asset\_GetModifyTime(Data\_Asset \*asset, int64\_t \*modifyTime)

**Description**

Obtains the last modification time of an asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| int64\_t \*modifyTime | Pointer to the last modification time obtained, in int64\_t format. No specific unit. You can specify it. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_ERR** indicates that the operation fails.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_GetSize()

int OH\_Data\_Asset\_GetSize(Data\_Asset \*asset, size\_t \*size)

**Description**

Obtains the space occupied by an asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| size\_t \*size | Pointer to the data asset size obtained, in the format of size\_t. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_ERR** indicates that the operation fails.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_GetStatus()

int OH\_Data\_Asset\_GetStatus(Data\_Asset \*asset, Data\_AssetStatus \*status)

**Description**

Obtains the status of a data asset.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| [Data\_AssetStatus](#data_assetstatus) \*status | Pointer to the [Data\_AssetStatus](#data_assetstatus) obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Data\_Asset\_CreateOne()

Data\_Asset \*OH\_Data\_Asset\_CreateOne(void)

**Description**

Creates a [Data\_Asset](../../structs/data-asset/document.md) instance.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) | 
Returns the pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance created if the operation is successful; returns null otherwise.

After the instance is used, call the [OH\_Data\_Asset\_DestroyOne](#oh_data_asset_destroyone) API to release the memory.

 |

#### \[h2\]OH\_Data\_Asset\_DestroyOne()

int OH\_Data\_Asset\_DestroyOne(Data\_Asset \*asset)

**Description**

Destroys a [Data\_Asset](../../structs/data-asset/document.md) object and reclaims the memory occupied by the object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*asset | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode). |

#### \[h2\]OH\_Data\_Asset\_CreateMultiple()

Data\_Asset \*\*OH\_Data\_Asset\_CreateMultiple(uint32\_t count)

**Description**

Creates a specified number of [Data\_Asset](../../structs/data-asset/document.md) instances.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t count | Number of data assets to create. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) | 
Returns the pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance created if the operation is successful; returns null otherwise.

After the instance is used, call the [OH\_Data\_Asset\_DestroyMultiple](#oh_data_asset_destroymultiple) API to release the memory.

 |

#### \[h2\]OH\_Data\_Asset\_DestroyMultiple()

int OH\_Data\_Asset\_DestroyMultiple(Data\_Asset \*\*assets, uint32\_t count)

**Description**

Destroys multiple [Data\_Asset](../../structs/data-asset/document.md) objects and reclaims the memory occupied by the objects.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Data\_Asset](../../structs/data-asset/document.md) \*\*assets | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| uint32\_t count | Number of [Data\_Asset](../../structs/data-asset/document.md) objects to be destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. For details, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode). |
