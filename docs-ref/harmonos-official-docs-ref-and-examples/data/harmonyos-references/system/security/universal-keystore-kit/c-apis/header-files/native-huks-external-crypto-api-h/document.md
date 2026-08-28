# native\_huks\_external\_crypto\_api.h

#### Overview

Defines the HarmonyOS Universal KeyStore (HUKS) APIs for external key management extensions.

**File to include**: <huks/native\_huks\_external\_crypto\_api.h>

**Library**: libhuks\_external\_crypto.z.so

**System capability**: SystemCapability.Security.Huks.CryptoExtension

**Since**: 22

**Related module**: [HuksExternalCryptoApi](../../modules/huksexternalcryptoapi/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result OH\_Huks\_RegisterProvider(const struct OH\_Huks\_Blob \*providerName, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)](#oh_huks_registerprovider) | Registers an external key management extension provider. |
| [struct OH\_Huks\_Result OH\_Huks\_UnregisterProvider(const struct OH\_Huks\_Blob \*providerName, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)](#oh_huks_unregisterprovider) | Unregisters an external key management extension provider. |
| [struct OH\_Huks\_Result OH\_Huks\_OpenResource(const struct OH\_Huks\_Blob \*resourceId, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)](#oh_huks_openresource) | 
Opens a resource based on the specified resource ID.

Note: The opened resource must be closed using [OH\_Huks\_CloseResource](#oh_huks_closeresource).

 |
| [struct OH\_Huks\_Result OH\_Huks\_CloseResource(const struct OH\_Huks\_Blob \*resourceId, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)](#oh_huks_closeresource) | Closes a resource based on the specified resource ID. |
| [struct OH\_Huks\_Result OH\_Huks\_GetUkeyPinAuthState(const struct OH\_Huks\_Blob \*resourceId, const OH\_Huks\_ExternalCryptoParamSet \*paramSet, OH\_Huks\_ExternalPinAuthState \*authState)](#oh_huks_getukeypinauthstate) | Obtains the PIN authorization state of the specified Ukey resource ID. |
| [struct OH\_Huks\_Result OH\_Huks\_GetProperty(const struct OH\_Huks\_Blob \*resourceId, const struct OH\_Huks\_Blob \*propertyId, const OH\_Huks\_ExternalCryptoParamSet \*paramSetIn, OH\_Huks\_ExternalCryptoParamSet \*\*paramSetOut)](#oh_huks_getproperty) | Obtains the property information of the external key management extension provider. |
| [struct OH\_Huks\_Result OH\_Huks\_InitExternalCryptoParamSet(OH\_Huks\_ExternalCryptoParamSet \*\*paramSet)](#oh_huks_initexternalcryptoparamset) | Initializes a parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_AddExternalCryptoParams(OH\_Huks\_ExternalCryptoParamSet \*paramSet, const OH\_Huks\_ExternalCryptoParam \*params, uint32\_t paramCnt)](#oh_huks_addexternalcryptoparams) | Adds parameters to a parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_BuildExternalCryptoParamSet(OH\_Huks\_ExternalCryptoParamSet \*\*paramSet)](#oh_huks_buildexternalcryptoparamset) | Builds a parameter set. |
| [void OH\_Huks\_FreeExternalCryptoParamSet(OH\_Huks\_ExternalCryptoParamSet \*\*paramSet)](#oh_huks_freeexternalcryptoparamset) | Destroys a parameter set and releases related memory. |
| [struct OH\_Huks\_Result OH\_Huks\_GetExternalCryptoParam(OH\_Huks\_ExternalCryptoParamSet \*paramSet, const uint32\_t tag, OH\_Huks\_ExternalCryptoParam \*\*param)](#oh_huks_getexternalcryptoparam) | Obtains a specified parameter from a parameter set. |

#### Function Description

#### \[h2\]OH\_Huks\_RegisterProvider()

struct OH\_Huks\_Result OH\_Huks\_RegisterProvider(const struct OH\_Huks\_Blob \*providerName, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)

**Description**

Registers an external key management extension provider.

**Required permissions**: ohos.permission.CRYPTO\_EXTENSION\_REGISTER

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*providerName | Name of the provider. |
| [const OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the registration parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL 201**: Permission verification fails. Apply for the required permission first.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API 801**: Unsupported API.

**OH\_HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT 12000002**: Failed to obtain the provider parameters.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT 12000018**: Invalid **providerName** or **paramSet**.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST 12000019**: The provider has been registered.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_ERROR 12000020**: An error occurs in the dependent module.

**OH\_HUKS\_ERR\_CODE\_EXCEED\_LIMIT 12000025**: The number of providers exceeds the upper limit.

 |

#### \[h2\]OH\_Huks\_UnregisterProvider()

struct OH\_Huks\_Result OH\_Huks\_UnregisterProvider(const struct OH\_Huks\_Blob \*providerName, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)

**Description**

Unregisters an external key management extension provider.

**Required permissions**: ohos.permission.CRYPTO\_EXTENSION\_REGISTER

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*providerName | Name of the provider. |
| [const OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the registration parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_PERMISSION\_FAIL 201**: Permission verification fails. Apply for the required permission first.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API 801**: Unsupported API.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST 12000011**: The specified provider is not found.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR = 12000012**: An internal system error occurs. The key management extension module is not loaded.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT 12000018**: Invalid **providerName**.

 |

#### \[h2\]OH\_Huks\_OpenResource()

struct OH\_Huks\_Result OH\_Huks\_OpenResource(const struct OH\_Huks\_Blob \*resourceId, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)

**Description**

Opens a resource based on the specified resource ID.

Note: The opened resource must be closed using [OH\_Huks\_CloseResource](#oh_huks_closeresource).

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*resourceId | Resource ID of the specified provider. |
| [const OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the handle operation parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API 801**: Unsupported API.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL 12000006**: Ukey driver error.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST 12000011**: The cached resource handle is not found. Open the resource based on the resource ID first.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR 12000012**: An internal system error occurs. The processing function is not found.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST 12000017**: The resource is already open.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT 12000018**: Invalid **resourceId** or **paramSet**.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_ERROR 12000020**: Provider execution fails.

**OH\_HUKS\_ERR\_CODE\_BUSY 12000024**: The provider or Ukey is busy.

**OH\_HUKS\_ERR\_CODE\_EXCEED\_LIMIT 12000025**: The number of opened resources exceeds the limit.

 |

#### \[h2\]OH\_Huks\_CloseResource()

struct OH\_Huks\_Result OH\_Huks\_CloseResource(const struct OH\_Huks\_Blob \*resourceId, const OH\_Huks\_ExternalCryptoParamSet \*paramSet)

**Description**

Closes a resource based on the specified resource ID.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*resourceId | Resource ID of the specified provider. |
| [const OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the handle operation parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API 801**: Unsupported API.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL 12000006**: Ukey driver error.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR 12000012**: An internal system error occurs. The processing function is not found.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT 12000018**: Invalid **resourceId** or **paramSet**.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_ERROR 12000020**: Provider execution fails.

**OH\_HUKS\_ERR\_CODE\_BUSY 12000024**: The provider or Ukey is busy.

 |

#### \[h2\]OH\_Huks\_GetUkeyPinAuthState()

struct OH\_Huks\_Result OH\_Huks\_GetUkeyPinAuthState(const struct OH\_Huks\_Blob \*resourceId, const OH\_Huks\_ExternalCryptoParamSet \*paramSet, OH\_Huks\_ExternalPinAuthState \*authState)

**Description**

Obtains the PIN authorization state of the specified Ukey resource ID.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*resourceId | Resource ID of the specified provider. |
| [const OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the PIN authorization parameters. |
| bool \*authState | Whether a specified index is authorized. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API 801**: Unsupported API.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL 12000006**: Ukey driver error.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST 12000011**: The specified resource ID is invalid.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR 12000012**: An internal system error occurs. The processing function is not found.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT 12000018**: Invalid **resourceId** or **paramSet**.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_ERROR 12000020**: Provider execution fails.

**OH\_HUKS\_ERR\_CODE\_BUSY 12000024**: The provider or Ukey is busy.

 |

#### \[h2\]OH\_Huks\_GetProperty()

struct OH\_Huks\_Result OH\_Huks\_GetProperty(const struct OH\_Huks\_Blob \*resourceId, const struct OH\_Huks\_Blob \*propertyId, const OH\_Huks\_ExternalCryptoParamSet \*paramSetIn, OH\_Huks\_ExternalCryptoParamSet \*\*paramSetOut)

**Description**

Obtains the property information of the external key management extension provider.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*resourceId | Resource ID of the specified provider. |
| [const struct OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) \*propertyId | Name of the property function defined by GMT 0016-2023. |
| [const OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSetIn | Pointer to the input operation parameters. |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*\*paramSetOut | Pointer to the output parameters, which must contain the **OH\_HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA** parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API 801**: Unsupported API.

**OH\_HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL 12000005**: IPC communication failed.

**OH\_HUKS\_ERR\_CODE\_CRYPTO\_FAIL 12000006**: Driver error.

**OH\_HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST 12000011**: The specified handle in the cache is not found.

**OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR 12000012**: An internal system error occurs. The processing function is not found.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT 12000018**: Invalid **resourceId**, **propertyId**, **paramSet**, or callback.

**OH\_HUKS\_ERR\_CODE\_EXTERNAL\_ERROR 12000020**: The provider or Ukey internal execution fails.

**OH\_HUKS\_ERR\_CODE\_PIN\_LOCKED 12000021**: The PIN is locked.

**OH\_HUKS\_ERR\_CODE\_PIN\_NO\_AUTH 12000023**: PIN authentication fails.

**OH\_HUKS\_ERR\_CODE\_BUSY 12000024**: The resources in the provider or Ukey are being used.

 |

#### \[h2\]OH\_Huks\_InitExternalCryptoParamSet()

struct OH\_Huks\_Result OH\_Huks\_InitExternalCryptoParamSet(OH\_Huks\_ExternalCryptoParamSet \*\*paramSet)

**Description**

Initializes a parameter set.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*\*paramSet | Level-2 pointer to the parameter set to initialize. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

**OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT 12000018**: **params** is NULL or **paramSet** is invalid.

 |

#### \[h2\]OH\_Huks\_AddExternalCryptoParams()

struct OH\_Huks\_Result OH\_Huks\_AddExternalCryptoParams(OH\_Huks\_ExternalCryptoParamSet \*paramSet, const OH\_Huks\_ExternalCryptoParam \*params, uint32\_t paramCnt)

**Description**

Adds parameters to a parameter set.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the parameter set to which parameters are to be added. |
| [const OH\_Huks\_ExternalCryptoParam](../../structs/oh-huks-externalcryptoparam/document.md) \*params | Pointer to the parameter array to be added. |
| uint32\_t paramCnt | Number of parameters to be added. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT 12000018**: **params** is NULL or **paramSet** is invalid.

 |

#### \[h2\]OH\_Huks\_BuildExternalCryptoParamSet()

struct OH\_Huks\_Result OH\_Huks\_BuildExternalCryptoParamSet(OH\_Huks\_ExternalCryptoParamSet \*\*paramSet)

**Description**

Builds a parameter set.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*\*paramSet | Level-2 pointer to the parameter set to build. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT 12000018** - Invalid **paramSet**.

**OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY 12000014**: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_FreeExternalCryptoParamSet()

void OH\_Huks\_FreeExternalCryptoParamSet(OH\_Huks\_ExternalCryptoParamSet \*\*paramSet)

**Description**

Destroys a parameter set and releases related memory.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*\*paramSet | Level-2 pointer to the parameter set to destroy. |

#### \[h2\]OH\_Huks\_GetExternalCryptoParam()

struct OH\_Huks\_Result OH\_Huks\_GetExternalCryptoParam(OH\_Huks\_ExternalCryptoParamSet \*paramSet, const uint32\_t tag, OH\_Huks\_ExternalCryptoParam \*\*param)

**Description**

Obtains a specified parameter from a parameter set.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Huks\_ExternalCryptoParamSet](../../structs/oh-huks-externalcryptoparamset/document.md) \*paramSet | Pointer to the target parameter set. |
| const uint32\_t tag | Tag value of the parameter to obtain. |
| [OH\_Huks\_ExternalCryptoParam](../../structs/oh-huks-externalcryptoparam/document.md) \*\*param | Level-2 pointer used to return the obtained parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

**OH\_HUKS\_SUCCESS 0**: Operation successful.

**OH\_HUKS\_ERR\_CODE\_INVALID\_ARGUMENT 12000018** - **paramSet** or **param** is invalid, or the parameter does not exist in the set.

 |
