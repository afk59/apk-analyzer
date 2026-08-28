# native\_huks\_param.h

#### Overview

Provides APIs for constructing, using, and destroying a parameter set.

**File to include**: <huks/native\_huks\_param.h>

**Library**: libhuks\_ndk.z.so

**System capability**: SystemCapability.Security.Huks.Core

The preceding system capability is available since API version 20. From API versions 9 to 19, the system capability is **SystemCapability.Security.Huks**.

**Since**: 9

**Related module**: [HuksParamSetApi](../../modules/huksparamsetapi/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result OH\_Huks\_InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)](#oh_huks_initparamset) | Initializes a parameter set. No parameter information is required, and the default available memory space is allocated to the parameter set. The initialized parameter set needs to be freed by calling\*\* OH\_Huks\_FreeParamSet\*\*. To add parameters to a parameter set, you need to call **OH\_Huks\_AddParams** to add parameters and call **OH\_Huks\_BuildParamSet** to build the parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_AddParams(struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Param \*params, uint32\_t paramCnt)](#oh_huks_addparams) | Adds parameters to a parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_BuildParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)](#oh_huks_buildparamset) | Builds a parameter set. After the parameter set is initialized and parameters are added, the parameter set is serialized and the data of the BLOB type is copied to the adjacent memory area at the end of the **paramSet** struct. |
| [void OH\_Huks\_FreeParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)](#oh_huks_freeparamset) | Frees a parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_CopyParamSet(const struct OH\_Huks\_ParamSet \*fromParamSet, uint32\_t fromParamSetSize, struct OH\_Huks\_ParamSet \*\*paramSet)](#oh_huks_copyparamset) | Copies a parameter set (deep copy). |
| [struct OH\_Huks\_Result OH\_Huks\_GetParam(const struct OH\_Huks\_ParamSet \*paramSet, uint32\_t tag, struct OH\_Huks\_Param \*\*param)](#oh_huks_getparam) | Obtains a parameter from a parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_FreshParamSet(struct OH\_Huks\_ParamSet \*paramSet, bool isCopy)](#oh_huks_freshparamset) | Refreshes the [OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) data in the parameter set. |
| [struct OH\_Huks\_Result OH\_Huks\_IsParamSetTagValid(const struct OH\_Huks\_ParamSet \*paramSet)](#oh_huks_isparamsettagvalid) | Checks whether the parameters in a parameter set are valid. |
| [struct OH\_Huks\_Result OH\_Huks\_IsParamSetValid(const struct OH\_Huks\_ParamSet \*paramSet, uint32\_t size)](#oh_huks_isparamsetvalid) | Checks whether a parameter set is of the valid size. |
| [struct OH\_Huks\_Result OH\_Huks\_CheckParamMatch(const struct OH\_Huks\_Param \*baseParam, const struct OH\_Huks\_Param \*param)](#oh_huks_checkparammatch) | Checks whether two parameters are the same. |
| [void OH\_Huks\_FreeKeyAliasSet(struct OH\_Huks\_KeyAliasSet \*keyAliasSet)](#oh_huks_freekeyaliasset) | Destroys the parameter set of a key alias. |

#### Function Description

#### \[h2\]OH\_Huks\_InitParamSet()

struct OH\_Huks\_Result OH\_Huks\_InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)

**Description**

Initializes a parameter set. No parameter information is required, and the default available memory space is allocated to the parameter set. The initialized parameter set needs to be freed by calling\*\* OH\_Huks\_FreeParamSet\*\*. To add parameters to a parameter set, you need to call **OH\_Huks\_AddParams** to add parameters and call **OH\_Huks\_BuildParamSet** to build the parameter set.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*\*paramSet | Pointer to the parameter set to initialize. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: Initialization successful.

OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014: Insufficient memory.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **paramSet** is invalid.

 |

#### \[h2\]OH\_Huks\_AddParams()

struct OH\_Huks\_Result OH\_Huks\_AddParams(struct OH\_Huks\_ParamSet \*paramSet, const struct OH\_Huks\_Param \*params, uint32\_t paramCnt)

**Description**

Adds parameters to a parameter set.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameter set to which parameters are to be added. |
| [const struct OH\_Huks\_Param](../../structs/oh-huks-param/document.md) \*params | Pointer to an array of parameters to add. |
| uint32\_t paramCnt | Number of parameters to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: Operation successful.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **params** is a null pointer or **paramSet** is invalid.

 |

#### \[h2\]OH\_Huks\_BuildParamSet()

struct OH\_Huks\_Result OH\_Huks\_BuildParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)

**Description**

Builds a parameter set. After the parameter set is initialized and parameters are added, the parameter set is serialized and the data of the BLOB type is copied to the adjacent memory area at the end of the **paramSet** struct.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*\*paramSet | Double pointer to the parameter set to build. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: Operation successful.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **paramSet** is invalid.

OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_FreeParamSet()

void OH\_Huks\_FreeParamSet(struct OH\_Huks\_ParamSet \*\*paramSet)

**Description**

Frees a parameter set.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*\*paramSet | Pointer to the parameter set to free. |

#### \[h2\]OH\_Huks\_CopyParamSet()

struct OH\_Huks\_Result OH\_Huks\_CopyParamSet(const struct OH\_Huks\_ParamSet \*fromParamSet, uint32\_t fromParamSetSize, struct OH\_Huks\_ParamSet \*\*paramSet)

**Description**

Copies a parameter set (deep copy).

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*fromParamSet | Pointer to the parameter set to copy. |
| uint32\_t fromParamSetSize | Size of the memory occupied by the copied parameter set. |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*\*paramSet | Double pointer to the new parameter set generated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: Operation successful.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **fromParamSet**, **fromParamSetSize**, or **paramSet** is invalid.

OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_GetParam()

struct OH\_Huks\_Result OH\_Huks\_GetParam(const struct OH\_Huks\_ParamSet \*paramSet, uint32\_t tag, struct OH\_Huks\_Param \*\*param)

**Description**

Obtains a parameter from a parameter set.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameter set to check. |
| uint32\_t tag | Name of the parameter to obtain. |
| [struct OH\_Huks\_Param](../../structs/oh-huks-param/document.md) \*\*param | Double pointer to the obtained parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: Operation successful.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **paramSet** or **param** is invalid, or **param** is not in **paramSet**.

 |

#### \[h2\]OH\_Huks\_FreshParamSet()

struct OH\_Huks\_Result OH\_Huks\_FreshParamSet(struct OH\_Huks\_ParamSet \*paramSet, bool isCopy)

**Description**

Refreshes the [OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) data in the parameter set.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameter set to check. |
| bool isCopy | If the value is **true**, the address of the [OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) data is refreshed and copied to the parameter set. If the value is **false**, only the address of the [OH\_Huks\_Blob](../../structs/oh-huks-blob/document.md) data is refreshed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: Operation successful.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **paramSet** is invalid.

OH\_HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY = 12000014: Insufficient memory.

 |

#### \[h2\]OH\_Huks\_IsParamSetTagValid()

struct OH\_Huks\_Result OH\_Huks\_IsParamSetTagValid(const struct OH\_Huks\_ParamSet \*paramSet)

**Description**

Checks whether the parameters in a parameter set are valid.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameter set to check. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: All parameters in **paramSet** are valid.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **paramSet** is invalid, or the parameter set contains invalid, duplicate, or incorrect tags.

 |

#### \[h2\]OH\_Huks\_IsParamSetValid()

struct OH\_Huks\_Result OH\_Huks\_IsParamSetValid(const struct OH\_Huks\_ParamSet \*paramSet, uint32\_t size)

**Description**

Checks whether a parameter set is of the valid size.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_ParamSet](../../structs/oh-huks-paramset/document.md) \*paramSet | Pointer to the parameter set to check. |
| uint32\_t size | Memory size occupied by the parameter set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: The size of the parameter set is valid.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: **paramSet** is invalid.

 |

#### \[h2\]OH\_Huks\_CheckParamMatch()

struct OH\_Huks\_Result OH\_Huks\_CheckParamMatch(const struct OH\_Huks\_Param \*baseParam, const struct OH\_Huks\_Param \*param)

**Description**

Checks whether two parameters are the same.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct OH\_Huks\_Param](../../structs/oh-huks-param/document.md) \*baseParam | Pointer to the first parameter to compare. |
| [const struct OH\_Huks\_Param](../../structs/oh-huks-param/document.md) \*param | Pointer to the second parameter to compare. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_Huks\_Result](../../structs/oh-huks-result/document.md) | 
Possible error codes (**errorCode**):

OH\_HUKS\_SUCCESS = 0: The two parameters to be compared are the same.

OH\_HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT = 401: One of the parameter sets is invalid, the parameters do not match,

or there is an invalid tag internally.

 |

#### \[h2\]OH\_Huks\_FreeKeyAliasSet()

void OH\_Huks\_FreeKeyAliasSet(struct OH\_Huks\_KeyAliasSet \*keyAliasSet)

**Description**

Destroys the parameter set of a key alias.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_Huks\_KeyAliasSet](../../structs/oh-huks-keyaliasset/document.md) \*keyAliasSet | Pointer to the parameter set of the key alias to destroy. |
