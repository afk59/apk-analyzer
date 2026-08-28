# inputmethod\_private\_command\_capi.h

#### Overview

Provides methods for creating, destroying, reading, and writing private data objects.

**Header file**: <inputmethod/inputmethod\_private\_command\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) | InputMethod\_PrivateCommand | Private data exchanged between the text box and the input method application. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand \*OH\_PrivateCommand\_Create(char key\[\], size\_t keyLength)](#oh_privatecommand_create) | Creates an [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance. |
| [void OH\_PrivateCommand\_Destroy(InputMethod\_PrivateCommand \*command)](#oh_privatecommand_destroy) | Destroys an [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance. |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetKey(InputMethod\_PrivateCommand \*command, char key\[\], size\_t keyLength)](#oh_privatecommand_setkey) | Sets the key value for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetBoolValue(InputMethod\_PrivateCommand \*command, bool value)](#oh_privatecommand_setboolvalue) | Sets the value of the Boolean type for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetIntValue(InputMethod\_PrivateCommand \*command, int32\_t value)](#oh_privatecommand_setintvalue) | Sets the value of the integer type for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_SetStrValue(InputMethod\_PrivateCommand \*command, char value\[\], size\_t valueLength)](#oh_privatecommand_setstrvalue) | Sets the value of the string type for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetKey(InputMethod\_PrivateCommand \*command, const char \*\*key, size\_t \*keyLength)](#oh_privatecommand_getkey) | Obtains the key value from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetValueType(InputMethod\_PrivateCommand \*command, InputMethod\_CommandValueType \*type)](#oh_privatecommand_getvaluetype) | Obtains the data type of value from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetBoolValue(InputMethod\_PrivateCommand \*command, bool \*value)](#oh_privatecommand_getboolvalue) | Obtains the value of the Boolean type from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetIntValue(InputMethod\_PrivateCommand \*command, int32\_t \*value)](#oh_privatecommand_getintvalue) | Obtains the value of the integer type from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |
| [InputMethod\_ErrorCode OH\_PrivateCommand\_GetStrValue(InputMethod\_PrivateCommand \*command, const char \*\*value, size\_t \*valueLength)](#oh_privatecommand_getstrvalue) | Obtains the value of the string type from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). |

#### Function Description

#### \[h2\]OH\_PrivateCommand\_Create()

InputMethod\_PrivateCommand \*OH\_PrivateCommand\_Create(char key\[\], size\_t keyLength)

**Description**

Creates an [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char key\[\] | Key value of the private data. |
| size\_t keyLength | Key length. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance is returned.

If the operation failed, **NULL** is returned, which may be caused by insufficient application address space.

 |

#### \[h2\]OH\_PrivateCommand\_Destroy()

void OH\_PrivateCommand\_Destroy(InputMethod\_PrivateCommand \*command)

**Description**

Destroys an [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance to be destroyed. |

#### \[h2\]OH\_PrivateCommand\_SetKey()

InputMethod\_ErrorCode OH\_PrivateCommand\_SetKey(InputMethod\_PrivateCommand \*command, char key\[\], size\_t keyLength)

**Description**

Sets the key value for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance to be set. |
| char key\[\] | Key value. |
| size\_t keyLength | Key length. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_SetBoolValue()

InputMethod\_ErrorCode OH\_PrivateCommand\_SetBoolValue(InputMethod\_PrivateCommand \*command, bool value)

**Description**

Sets the value of the Boolean type for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance to be set. |
| bool value | Boolean value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_SetIntValue()

InputMethod\_ErrorCode OH\_PrivateCommand\_SetIntValue(InputMethod\_PrivateCommand \*command, int32\_t value)

**Description**

Sets the value of the integer type for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance to be set. |
| int32\_t value | Value of the integer type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_SetStrValue()

InputMethod\_ErrorCode OH\_PrivateCommand\_SetStrValue(InputMethod\_PrivateCommand \*command, char value\[\], size\_t valueLength)

**Description**

Sets the value of the string type for [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance to be set. |
| char value\[\] | Value of the string type. |
| size\_t valueLength | Value length. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_GetKey()

InputMethod\_ErrorCode OH\_PrivateCommand\_GetKey(InputMethod\_PrivateCommand \*command, const char \*\*key, size\_t \*keyLength)

**Description**

Obtains the key value from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance from which the key value is to be obtained. |
| const char \*\*key | The lifespan of **key** is consistent with that of **command**. You are advised to copy instead of directly saving the key address or writing **key**. |
| size\_t \*keyLength | Key length. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_GetValueType()

InputMethod\_ErrorCode OH\_PrivateCommand\_GetValueType(InputMethod\_PrivateCommand \*command, InputMethod\_CommandValueType \*type)

**Description**

Obtains the data type of value from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance from which the value is to be obtained. |
| [InputMethod\_CommandValueType](../inputmethod-types-capi-h/document.md#inputmethod_commandvaluetype) \*type | Pointer to the [InputMethod\_CommandValueType](../inputmethod-types-capi-h/document.md#inputmethod_commandvaluetype) instance, used to indicate the data type of the value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_GetBoolValue()

InputMethod\_ErrorCode OH\_PrivateCommand\_GetBoolValue(InputMethod\_PrivateCommand \*command, bool \*value)

**Description**

Obtains the value of the Boolean type from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance from which the value is to be obtained. |
| bool \*value | Boolean value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

[IME\_ERR\_QUERY\_FAILED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Query failed as the command contains no Boolean value.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_GetIntValue()

InputMethod\_ErrorCode OH\_PrivateCommand\_GetIntValue(InputMethod\_PrivateCommand \*command, int32\_t \*value)

**Description**

Obtains the value of the integer type from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance from which the value is to be obtained. |
| int32\_t \*value | Value of the integer type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

[IME\_ERR\_QUERY\_FAILED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Query failed because the command does not contain an integer value.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_PrivateCommand\_GetStrValue()

InputMethod\_ErrorCode OH\_PrivateCommand\_GetStrValue(InputMethod\_PrivateCommand \*command, const char \*\*value, size\_t \*valueLength)

**Description**

Obtains the value of the string type from [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*command | Pointer to the [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) instance from which the value is to be obtained. |
| const char \*\*value | Value of the string type. |
| size\_t \*valueLength | The lifespan of **value** is consistent with that of **command**. You are advised to copy instead of directly saving the value address or writing **value**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

[IME\_ERR\_QUERY\_FAILED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Query failed because the command does not contain a string value.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |
