# asset\_type.h

#### Overview

Defines the enums, structs, and error codes used in the asset store service.

**File to include**: <asset/asset\_type.h>

**Library**: libasset\_ndk.z.so

**System capability**: SystemCapability.Security.Asset

**Since**: 11

**Related module**: [AssetType](../../modules/assettype/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Asset\_Blob](../../structs/asset-blob/document.md) | Asset\_Blob | Defines a binary array, that is, an array of bytes with variable length. |
| [Asset\_Value](../../structs/asset-value/document.md) | Asset\_Value | Defines the value of the asset attribute. |
| [Asset\_Attr](../../structs/asset-attr/document.md) | Asset\_Attr | Represents an asset attribute in the form of a key-value (KV) pair. |
| [Asset\_Result](../../structs/asset-result/document.md) | Asset\_Result | Represents the query result of an asset. |
| [Asset\_ResultSet](../../structs/asset-resultset/document.md) | Asset\_ResultSet | Represents the query result of multiple assets. |
| [Asset\_SyncResult](../../structs/asset-syncresult/document.md) | Asset\_SyncResult | Represents the sync result of an asset. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Asset\_TagType](#asset_tagtype) | Asset\_TagType | Enumerates the types of the keys of asset attributes. |
| [Asset\_Tag](#asset_tag) | Asset\_Tag | Enumerates the keys of asset attributes. |
| [Asset\_ResultCode](#asset_resultcode) | Asset\_ResultCode | Enumerates the result codes used in the ASSET APIs. |
| [Asset\_Accessibility](#asset_accessibility) | Asset\_Accessibility | Enumerates the types of the access control based on the lock screen status. |
| [Asset\_AuthType](#asset_authtype) | Asset\_AuthType | Enumerates the user authentication types supported by assets. |
| [Asset\_SyncType](#asset_synctype) | Asset\_SyncType | Enumerates the asset sync types. |
| [Asset\_WrapType](#asset_wraptype) | Asset\_WrapType | Encrypted import/export type supported by the asset. |
| [Asset\_ConflictResolution](#asset_conflictresolution) | Asset\_ConflictResolution | Enumerates the policies for resolving the conflict (for example, a duplicate alias). |
| [Asset\_ReturnType](#asset_returntype) | Asset\_ReturnType | Enumerates the types of the asset query result to return. |
| [Asset\_OperationType](#asset_operationtype) | Asset\_OperationType | Enumerates the additional asset operation types. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| ASSET\_TAG\_TYPE\_MASK (0xF << 28) | 
Defines the mask used to obtain the key type of an asset attribute.

**Since**: 11

 |

#### Enum Description

#### \[h2\]Asset\_TagType

enum Asset\_TagType

**Description**

Enumerates the types of the keys of asset attributes.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_TYPE\_BOOL = 0x1 << 28 | Boolean. |
| ASSET\_TYPE\_NUMBER = 0x2 << 28 | uint32\_t. |
| ASSET\_TYPE\_BYTES = 0x3 << 28 | Bytes. |

#### \[h2\]Asset\_Tag

enum Asset\_Tag

**Description**

Enumerates the keys of asset attributes.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_TAG\_SECRET = ASSET\_TYPE\_BYTES | 0x01 | Sensitive user data in the form of bytes, such as passwords and tokens. |
| ASSET\_TAG\_ALIAS = ASSET\_TYPE\_BYTES | 0x02 | Asset alias (identifier) in the form of bytes. |
| ASSET\_TAG\_ACCESSIBILITY = ASSET\_TYPE\_NUMBER | 0x03 | Access control based on the lock screen status. The value is of the uint32\_t type. |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET = ASSET\_TYPE\_BOOL | 0x04 | A Boolean value indicating whether the asset is available only with a lock screen password. |
| ASSET\_TAG\_AUTH\_TYPE = ASSET\_TYPE\_NUMBER | 0x05 | User authentication type for the asset. The value is of the uint32\_t type. |
| ASSET\_TAG\_AUTH\_VALIDITY\_PERIOD = ASSET\_TYPE\_NUMBER | 0x06 | Validity period of the user authentication, in seconds. The value is of the uint32\_t type, in seconds. |
| ASSET\_TAG\_AUTH\_CHALLENGE = ASSET\_TYPE\_BYTES | 0x07 | Challenge value, in the form of bytes, used for anti-replay during the authentication. |
| ASSET\_TAG\_AUTH\_TOKEN = ASSET\_TYPE\_BYTES | 0x08 | Authentication token, in the form of bytes, obtained after a successful user authentication. |
| ASSET\_TAG\_SYNC\_TYPE = ASSET\_TYPE\_NUMBER | 0x10 | Asset sync type. The value is of the uint32\_t type. |
| ASSET\_TAG\_IS\_PERSISTENT = ASSET\_TYPE\_BOOL | 0x11 | 
Whether the asset needs to be stored persistently.

Verification of **ohos.permission.STORE\_PERSISTENT\_DATA** is required if **OH\_Asset\_Add** is called with this tag passed in.

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_1 = ASSET\_TYPE\_BYTES | 0x20 | Custom data, which is of the bytes type and cannot be changed. |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 = ASSET\_TYPE\_BYTES | 0x21 | Custom data, which is of the bytes type and cannot be changed. |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 = ASSET\_TYPE\_BYTES | 0x22 | Custom data, which is of the bytes type and cannot be changed. |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 = ASSET\_TYPE\_BYTES | 0x23 | Custom data, which is of the bytes type and cannot be changed. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 = ASSET\_TYPE\_BYTES | 0x30 | Custom data, which is of the bytes type and can be changed. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 = ASSET\_TYPE\_BYTES | 0x31 | Custom data, which is of the bytes type and can be changed. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 = ASSET\_TYPE\_BYTES | 0x32 | Custom data, which is of the bytes type and can be changed. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 = ASSET\_TYPE\_BYTES | 0x33 | Custom data, which is of the bytes type and can be changed. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_1 = ASSET\_TYPE\_BYTES | 0x34 | 

Custom data, which is of the bytes type, can be changed, but cannot be synced.

**Since**: 12

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_2 = ASSET\_TYPE\_BYTES | 0x35 | 

Custom data, which is of the bytes type, can be changed, but cannot be synced.

**Since**: 12

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_3 = ASSET\_TYPE\_BYTES | 0x36 | 

Custom data, which is of the bytes type, can be changed, but cannot be synced.

**Since**: 12

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_4 = ASSET\_TYPE\_BYTES | 0x37 | 

Custom data, which is of the bytes type, can be changed, but cannot be synced.

**Since**: 12

 |
| ASSET\_TAG\_RETURN\_TYPE = ASSET\_TYPE\_NUMBER | 0x40 | Type of asset information to return. The value is of the uint32\_t type. |
| ASSET\_TAG\_RETURN\_LIMIT = ASSET\_TYPE\_NUMBER | 0x41 | Maximum number of assets that can be returned in a query operation. The value is of the uint32\_t type. |
| ASSET\_TAG\_RETURN\_OFFSET = ASSET\_TYPE\_NUMBER | 0x42 | Offset of the returned assets in a batch query. The value is of the uint32\_t type. |
| ASSET\_TAG\_RETURN\_ORDERED\_BY = ASSET\_TYPE\_NUMBER | 0x43 | Sorting order of the assets in the query result. The value is of the uint32\_t type. |
| ASSET\_TAG\_CONFLICT\_RESOLUTION = ASSET\_TYPE\_NUMBER | 0x44 | Policy for resolving the conflict when an asset is added. The value is of the uint32\_t type. |
| ASSET\_TAG\_UPDATE\_TIME = ASSET\_TYPE\_BYTES | 0x45 | 

Asset update time, in timestamp format. The value is of the bytes type.

**Since**: 12

 |
| ASSET\_TAG\_OPERATION\_TYPE = ASSET\_TYPE\_NUMBER | 0x46 | 

Additional operation type. The value is of the uint32\_t type.

**Since**: 12

 |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED = ASSET\_TYPE\_BOOL | 0x47 | 

Whether to encrypt the additional information customized by the service. The value is of the Boolean type.

**Since**: 14

 |
| ASSET\_TAG\_GROUP\_ID = ASSET\_TYPE\_BYTES | 0x48 | 

Group to which the asset belongs. The value is of the bytes type.

**Since**: 18

 |
| ASSET\_TAG\_WRAP\_TYPE = ASSET\_TYPE\_NUMBER | 0x49 | 

Encrypted import/export type supported by the asset. The value is of the uint32\_t type.

**Since**: 18

 |

#### \[h2\]Asset\_ResultCode

enum Asset\_ResultCode

**Description**

Enumerates the result codes used in the ASSET APIs.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_SUCCESS = 0 | The operation is successful. |
| ASSET\_PERMISSION\_DENIED = 201 | The caller does not have the required permission. |
| ASSET\_INVALID\_ARGUMENT = 401 | The parameter is invalid. |
| ASSET\_SERVICE\_UNAVAILABLE = 24000001 | The asset store service is unavailable. |
| ASSET\_NOT\_FOUND = 24000002 | The asset is not found. |
| ASSET\_DUPLICATED = 24000003 | The asset already exists. |
| ASSET\_ACCESS\_DENIED = 24000004 | The access is denied. |
| ASSET\_STATUS\_MISMATCH = 24000005 | The lock screen status does not match. |
| ASSET\_OUT\_OF\_MEMORY = 24000006 | The system memory is insufficient. |
| ASSET\_DATA\_CORRUPTED = 24000007 | The asset is corrupted. |
| ASSET\_DATABASE\_ERROR = 24000008 | The database operation failed. |
| ASSET\_CRYPTO\_ERROR = 24000009 | The cryptographic operation failed. |
| ASSET\_IPC\_ERROR = 24000010 | The IPC failed. |
| ASSET\_BMS\_ERROR = 24000011 | The Bundle Manager service is abnormal. |
| ASSET\_ACCOUNT\_ERROR = 24000012 | The account system service is abnormal. |
| ASSET\_ACCESS\_TOKEN\_ERROR = 24000013 | The Access Token service is abnormal. |
| ASSET\_FILE\_OPERATION\_ERROR = 24000014 | The file operation failed. |
| ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015 | Failed to obtain the system time. |
| ASSET\_LIMIT\_EXCEEDED = 24000016 | The number of cached assets exceeds the limit. |
| ASSET\_UNSUPPORTED = 24000017 | The function is not supported. |
| ASSET\_PARAM\_VERIFICATION\_FAILED = 24000018 | 
The parameter verification fails.

**Since**: 20

 |

#### \[h2\]Asset\_Accessibility

enum Asset\_Accessibility

**Description**

Enumerates the types of the access control based on the lock screen status.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_ACCESSIBILITY\_DEVICE\_POWERED\_ON = 0 | The asset can be accessed after the device is powered on. |
| ASSET\_ACCESSIBILITY\_DEVICE\_FIRST\_UNLOCKED = 1 | The asset can be accessed only after the device is unlocked for the first time. |
| ASSET\_ACCESSIBILITY\_DEVICE\_UNLOCKED = 2 | The asset can be accessed only after the device is unlocked. |

#### \[h2\]Asset\_AuthType

enum Asset\_AuthType

**Description**

Enumerates the user authentication types supported by assets.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_AUTH\_TYPE\_NONE = 0x00 | No user authentication is required before the asset is accessed. |
| ASSET\_AUTH\_TYPE\_ANY = 0xFF | The asset can be accessed if any user authentication (such as PIN, facial, or fingerprint authentication) is successful. |

#### \[h2\]Asset\_SyncType

enum Asset\_SyncType

**Description**

Asset sync type.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_SYNC\_TYPE\_NEVER = 0 | Asset sync is not allowed. |
| ASSET\_SYNC\_TYPE\_THIS\_DEVICE = 1 << 0 | Asset sync is allowed only on the local device, for example, in data restore on the local device. |
| ASSET\_SYNC\_TYPE\_TRUSTED\_DEVICE = 1 << 1 | Asset sync is allowed only between trusted devices, for example, in the case of cloning. |
| ASSET\_SYNC\_TYPE\_TRUSTED\_ACCOUNT = 1 << 2 | 
Asset sync is allowed only between the devices that are logged in with trusted accounts, for example, in cloud sync scenarios.

**Since**: 12

 |

#### \[h2\]Asset\_WrapType

enum Asset\_WrapType

**Description**

Encrypted import/export type supported by the asset.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| ASSET\_WRAP\_TYPE\_NEVER = 0 | Encrypted import/export is not allowed for the asset. |
| ASSET\_WRAP\_TYPE\_TRUSTED\_ACCOUNT = 1 | Encrypted import/export is allowed for the asset only on devices where a trusted account is logged in. |

#### \[h2\]Asset\_ConflictResolution

enum Asset\_ConflictResolution

**Description**

Policy for resolving the conflict (for example, a duplicate alias).

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_CONFLICT\_OVERWRITE = 0 | Overwrite the original asset. |
| ASSET\_CONFLICT\_THROW\_ERROR = 1 | Throw an exception for the service to perform subsequent processing. |

#### \[h2\]Asset\_ReturnType

enum Asset\_ReturnType

**Description**

Type of the asset query result to return.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| ASSET\_RETURN\_ALL = 0 | The query result contains the asset plaintext and its attributes. |
| ASSET\_RETURN\_ATTRIBUTES = 1 | The query result contains only the asset attributes. |

#### \[h2\]Asset\_OperationType

enum Asset\_OperationType

**Description**

Enumerates the additional asset operation types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| ASSET\_NEED\_SYNC = 0 | Sync. |
| ASSET\_NEED\_LOGOUT = 1 | Logout. |
