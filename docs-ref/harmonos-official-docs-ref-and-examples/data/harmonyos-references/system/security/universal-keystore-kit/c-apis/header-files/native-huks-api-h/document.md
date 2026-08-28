# native\_huks\_api.h

#### Overview

Declares the APIs used to access the HUKS.

**File to include**: <huks/native\_huks\_api.h>

**Library**: libhuks\_ndk.z.so

**System capability**: SystemCapability.Security.Huks.Core

The preceding system capability is available since API version 20. From API versions 9 to 19, the system capability is **SystemCapability.Security.Huks.Core**.

**Since**: 9

**Related module**: [HuksKeyApi](../../modules/hukskeyapi/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result OH\_Huks\_GetSdkVersion(struct OH\_Huks\_Blob \*sdkVersion)](#oh_huks_getsdkversion) | Obtains the current HUKS SDK version. |
| [struct OH\_Huks\_Result OH\_Huks\_GenerateKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSetIn, struct OH\_Huks\_ParamSet \*paramSetOut)](#oh_huks_generatekeyitem) | Generates a key. |
| [struct OH\_Huks\_Result OH\_Huks\_ImportKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*key)](#oh_huks_importkeyitem) | Imports a key in plaintext. |
| [struct OH\_Huks\_Result OH\_Huks\_ImportWrappedKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*wrappingKeyAlias, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*wrappedKeyData)](#oh_huks_importwrappedkeyitem) | Imports a key in ciphertext. |
| [struct OH\_Huks\_Result OH\_Huks\_ExportPublicKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*key)](#oh_huks_exportpublickeyitem) | Exports the public key. |
| [struct OH\_Huks\_Result OH\_Huks\_DeleteKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet)](#oh_huks_deletekeyitem) | Deletes a key. |
| [struct OH\_Huks\_Result OH\_Huks\_GetKeyItemParamSet(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSetIn, struct OH\_Huks\_ParamSet \*paramSetOut)](#oh_huks_getkeyitemparamset) | Obtains the properties of a key. |
| [struct OH\_Huks\_Result OH\_Huks\_IsKeyItemExist(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet)](#oh_huks_iskeyitemexist) | Checks whether a key exists. |
| [struct OH\_Huks\_Result OH\_Huks\_AttestKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_CertChain \*certChain)](#oh_huks_attestkeyitem) | Obtains the certificate chain of a key. This API is open only to system applications. |
| [struct OH\_Huks\_Result OH\_Huks\_AnonAttestKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_CertChain \*certChain)](#oh_huks_anonattestkeyitem) | 
Obtains the certificate chain of a key.

This function involves time-consuming network operation. The caller can obtain the certificate chain through an asynchronous thread.

 |
| [struct OH\_Huks\_Result OH\_Huks\_InitSession(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*handle, struct OH\_Huks\_Blob \*token)](#oh_huks_initsession) | Initializes a key session. This function returns a session handle (mandatory) and a challenge value (optional). |
| [struct OH\_Huks\_Result OH\_Huks\_UpdateSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)](#oh_huks_updatesession) | Adds data by segment for the key operation, performs the related key operation, and outputs the processed data. |
| [struct OH\_Huks\_Result OH\_Huks\_FinishSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)](#oh_huks_finishsession) | Finishes a key session. |
| [struct OH\_Huks\_Result OH\_Huks\_AbortSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet)](#oh_huks_abortsession) | Aborts a key session. |
| [struct OH\_Huks\_Result OH\_Huks\_ListAliases(const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_KeyAliasSet \*\*outData)](#oh_huks_listaliases) | Obtains the key alias set. |
| [struct OH\_Huks\_Result OH\_Huks\_WrapKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*wrappedKey)](#oh_huks_wrapkey) | Exports a wrapped key. |
| [struct OH\_Huks\_Result OH\_Huks\_UnwrapKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*wrappedKey)](#oh_huks_unwrapkey) | Imports a wrapped key. |

#### Function Description

#### \[h2\]OH\_Huks\_GetSdkVersion()

struct OH\_Huks\_Result OH\_Huks\_GetSdkVersion(struct OH\_Huks\_Blob \*sdkVersion)

**Description**

Obtains the current HUKS SDK version.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*sdkVersion | Pointer to the SDK version (string) obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: The value of **sdkVersion** or **sdkVersion->data** is **null**, or the value of **sdkVersion->size** is too small.

 |

#### \[h2\]OH\_Huks\_GenerateKeyItem()

struct OH\_Huks\_Result OH\_Huks\_GenerateKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSetIn, struct OH\_Huks\_ParamSet \*paramSetOut)

**Description**

Generates a key.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to generate. The alias must be unique in the process of the service. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSetIn | Pointer to the parameters for generating the key. |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSetOut | Pointer to a temporary key generated. If the generated key is not a temporary key, this parameter is a null pointer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSetIn**, or **paramSetOut** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004**: Failed to delete or write the file.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015**: Failed to connect to the user IAM.

**OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016**: No device password is set.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 (new in API version 20): A key with the same name already exists.

 |

#### \[h2\]OH\_Huks\_ImportKeyItem()

struct OH\_Huks\_Result OH\_Huks\_ImportKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*key)

**Description**

Imports a key in plaintext.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to import. The alias must be unique in the process of the service. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the properties of the key to import. |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*key | Pointer to the data of the key to import, complying with the format requirements of HUKS. For details, see [native\_huks\_type.h](../native-huks-type-h/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSet**, or **key** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004**: Failed to delete or write the file.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015**: Failed to connect to the user IAM.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 (new in API version 20): A key with the same name already exists.

 |

#### \[h2\]OH\_Huks\_ImportWrappedKeyItem()

struct OH\_Huks\_Result OH\_Huks\_ImportWrappedKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*wrappingKeyAlias, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*wrappedKeyData)

**Description**

Imports a key in ciphertext.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to import. The alias must be unique in the process of the service. |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*wrappingKeyAlias | Pointer to the alias of the key used for key agreement, which generates a shared secret to decrypt the key to import. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for importing the key in ciphertext. |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*wrappedKeyData | Pointer to the data of the key to import, complying with the format requirements of HUKS. For details, see [OH\_Huks\_AlgSuite](../native-huks-type-h/document.md#oh_huks_algsuite). |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **wrappingKeyAlias**, **paramSet**, or **wrappedKeyData** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004**: Failed to delete or write the file.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015**: Failed to connect to the user IAM.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 (new in API version 20): A key with the same name already exists.

 |

#### \[h2\]OH\_Huks\_ExportPublicKeyItem()

struct OH\_Huks\_Result OH\_Huks\_ExportPublicKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*key)

**Description**

Exports the public key.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the public key to export. It must be the same as the alias used for generating the key. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for exporting the public key. |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*key | Pointer to the public key exported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSet**, or **key** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

 |

#### \[h2\]OH\_Huks\_DeleteKeyItem()

struct OH\_Huks\_Result OH\_Huks\_DeleteKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet)

**Description**

Deletes a key.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to delete. It must be the same as the alias used for generating the key. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for deleting the key. By default, this parameter is a null pointer. The default key storage level is [OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_CE](../native-huks-type-h/document.md#oh_huks_authstoragelevel). |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias** or **paramSet** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_GetKeyItemParamSet()

struct OH\_Huks\_Result OH\_Huks\_GetKeyItemParamSet(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSetIn, struct OH\_Huks\_ParamSet \*paramSetOut)

**Description**

Obtains the properties of a key.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the target key. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSetIn | Pointer to the tag required for obtaining the properties. By default, this parameter is a null pointer. |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSetOut | Pointer to the key properties obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSetIn**, or **paramSetOut** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

 |

#### \[h2\]OH\_Huks\_IsKeyItemExist()

struct OH\_Huks\_Result OH\_Huks\_IsKeyItemExist(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet)

**Description**

Checks whether a key exists.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to check. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for checking the key. By default, this parameter is a null pointer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias** or **paramSet** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_AttestKeyItem()

struct OH\_Huks\_Result OH\_Huks\_AttestKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_CertChain \*certChain)

**Description**

Obtains the certificate chain of a key. This API is open only to system applications.

**Required permissions**: ohos.permission.ATTEST\_KEY (available only for system applications)

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the target key. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for obtaining the certificate chain. |
| [struct OH\_Huks\_CertChain](../../structs/oh-huks-certchain/document.md) \*certChain | Pointer to the certificate chain obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSet**, or **certChain** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

**OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL = 201**: Permission check failed. Request the permission first.

 |

#### \[h2\]OH\_Huks\_AnonAttestKeyItem()

struct OH\_Huks\_Result OH\_Huks\_AnonAttestKeyItem(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_CertChain \*certChain)

**Description**

Obtains the certificate chain of a key.

This function involves time-consuming network operation. The caller can obtain the certificate chain through an asynchronous thread.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the target key. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for obtaining the certificate chain. |
| [struct OH\_Huks\_CertChain](../../structs/oh-huks-certchain/document.md) \*certChain | Pointer to the certificate chain obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSet**, or **certChain** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

**OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL = 201**: Permission check failed. Request the permission first.

 |

#### \[h2\]OH\_Huks\_InitSession()

struct OH\_Huks\_Result OH\_Huks\_InitSession(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*handle, struct OH\_Huks\_Blob \*token)

**Description**

Initializes a key session. This function returns a session handle (mandatory) and a challenge value (optional).

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to be operated. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for the initialization operation. |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*handle | Pointer to the handle of the key session. This handle is required for subsequent operations of the same key, including [OH\_Huks\_UpdateSession](#oh_huks_updatesession), [OH\_Huks\_FinishSession](#oh_huks_finishsession), and [OH\_Huks\_AbortSession](#oh_huks_abortsession). |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*token | Pointer to the token used for key access control. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **keyAlias**, **paramSet**, **handle**, or **token** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_SESSION\_LIMIT = 12000010**: Hit the session limit.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018: (Added in API version 22) The parameter set is invalid.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020**: The provider or Ukey internal execution fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021**: The PIN is locked. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023**: The PIN authentication fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_BUSY = 12000024**: The resource in the provider or Ukey is being used. (This error code is added in API version 22.)

 |

**Reference**

[OH\_Huks\_UpdateSession](#oh_huks_updatesession)

[OH\_Huks\_FinishSession](#oh_huks_finishsession)

[OH\_Huks\_AbortSession](#oh_huks_abortsession)

#### \[h2\]OH\_Huks\_UpdateSession()

struct OH\_Huks\_Result OH\_Huks\_UpdateSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)

**Description**

Adds data by segment for the key operation, performs the related key operation, and outputs the processed data.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*handle | Pointer to the key session handle, which is returned by [OH\_Huks\_InitSession](#oh_huks_initsession). |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters required for the key operation. |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*inData | Pointer to the data to be processed. If there is a large amount of data to be processed, you can call this function multiple times to process data by segment. |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*outData | Pointer to the output data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **handle**, **paramSet**, **inData**, or **outData** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file or the handle does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013**: The certificate does not exist.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED = 12000008**: Failed to verify the access token.

**OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED = 12000007**: Failed to verify the access token information.

**OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT = 12000009**: The verification of the access token times out.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016**: No device password is set.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020**: The provider or Ukey internal execution fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021**: The PIN is locked. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023**: The PIN authentication fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_BUSY = 12000024**: The resource in the provider or Ukey is being used. (This error code is added in API version 22.)

 |

**Reference**

[OH\_Huks\_InitSession](#oh_huks_initsession)

[OH\_Huks\_FinishSession](#oh_huks_finishsession)

[OH\_Huks\_AbortSession](#oh_huks_abortsession)

#### \[h2\]OH\_Huks\_FinishSession()

struct OH\_Huks\_Result OH\_Huks\_FinishSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)

**Description**

Finishes a key session.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*handle | Pointer to the key session handle, which is returned by [OH\_Huks\_InitSession](#oh_huks_initsession). |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters required for the key operation. |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*inData | Pointer to the data to be passed in. |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*outData | Pointer to the output data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **handle**, **paramSet**, **inData**, or **outData** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file or the handle does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013**: The certificate does not exist.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000006**: The encryption engine failed.

**OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED = 12000008**: Failed to verify the access token.

**OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED = 12000007**: Failed to verify the access token information.

**OH\_HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT = 12000009**: The verification of the access token times out.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET = 12000016**: No device password is set.

**OH\_HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED = 12000001**: This feature is not supported currently.

OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST = 12000017 (new in API version 20): A key with the same name already exists.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020**: The provider or Ukey internal execution fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED = 12000021**: The PIN is locked. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH = 12000023**: The PIN authentication fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_BUSY = 12000024**: The resource in the provider or Ukey is being used. (This error code is added in API version 22.)

 |

**Reference**

[OH\_Huks\_InitSession](#oh_huks_initsession)

[OH\_Huks\_UpdateSession](#oh_huks_updatesession)

[OH\_Huks\_AbortSession](#oh_huks_abortsession)

#### \[h2\]OH\_Huks\_AbortSession()

struct OH\_Huks\_Result OH\_Huks\_AbortSession(const struct OH\_Huks\_Blob \*handle, const struct OH\_Huks\_ParamSet \*paramSet)

**Description**

Aborts a key session.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*handle | Pointer to the key session handle, which is returned by [OH\_Huks\_InitSession](#oh_huks_initsession). |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for aborting the key session. By default, this parameter is a null pointer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **handle**, **paramSet**, **inData**, or **outData** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT = 12000003**: Invalid key parameter.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST = 12000011**: The key file or the handle does not exist.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT = 12000002**: Failed to obtain key arguments.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST = 12000013**: The certificate does not exist.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_MODULE = 12000020**: The provider or Ukey internal execution fails. (This error code is added in API version 22.)

**OH\_HUKS\_ERR\_CODE\_BUSY = 12000024**: The resource in the provider or Ukey is being used. (This error code is added in API version 22.)

 |

**Reference**

[OH\_Huks\_InitSession](#oh_huks_initsession)

[OH\_Huks\_UpdateSession](#oh_huks_updatesession)

[OH\_Huks\_FinishSession](#oh_huks_finishsession)

#### \[h2\]OH\_Huks\_ListAliases()

struct OH\_Huks\_Result OH\_Huks\_ListAliases(const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_KeyAliasSet \*\*outData)

**Description**

Obtains the key alias set.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for obtaining the key alias set. By default, this parameter is a null pointer. |
| [struct OH\_Huks\_KeyAliasSet](../../structs/oh-huks-keyaliasset/document.md) \*\*outData | Pointer to the output data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401**: **paramSet** or **outData** is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_WrapKey()

struct OH\_Huks\_Result OH\_Huks\_WrapKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*wrappedKey)

**Description**

Exports a wrapped key.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to export. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for encrypting the exported key. |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*wrappedKey | Pointer to the wrapped key to export. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API = 801**: The API is not supported.

**OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004**: Failed to delete or write the file.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL = 12000011**: The key file does not exist.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018**: The key alias, parameter set, or wrapped key is invalid.

 |

#### \[h2\]OH\_Huks\_UnwrapKey()

struct OH\_Huks\_Result OH\_Huks\_UnwrapKey(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*paramSet, struct OH\_Huks\_Blob \*wrappedKey)

**Description**

Imports a wrapped key.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*keyAlias | Pointer to the alias of the key to import. The alias must be unique in the service process. Otherwise, the key will be overwritten. |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameters for encrypting the imported key. |
| [struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*wrappedKey | Pointer to the wrapped key to import. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS = 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API = 801**: The API is not supported.

**OH\_HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL = 12000004**: Failed to delete or write the file.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL = 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: A system error occurs.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED = 12000015**: Failed to connect to the user IAM.

**OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT = 12000018**: The key alias, parameter set, or wrapped key is invalid.

 |
