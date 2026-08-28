# inputmethod\_text\_avoid\_info\_capi.h

#### Overview

Provides methods for creating, destroying, reading, and writing the text box avoidance information objects.

**File to include**: <inputmethod/inputmethod\_text\_avoid\_info\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) | InputMethod\_TextAvoidInfo | Represents the information used by the input box to avoid the keyboard. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo \*OH\_TextAvoidInfo\_Create(double positionY, double height)](#oh_textavoidinfo_create) | Creates an [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance. |
| [void OH\_TextAvoidInfo\_Destroy(InputMethod\_TextAvoidInfo \*info)](#oh_textavoidinfo_destroy) | Destroys an [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance. |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_SetPositionY(InputMethod\_TextAvoidInfo \*info, double positionY)](#oh_textavoidinfo_setpositiony) | Sets the Y coordinate in [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md). |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_SetHeight(InputMethod\_TextAvoidInfo \*info, double height)](#oh_textavoidinfo_setheight) | Sets the height in [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md). |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_GetPositionY(InputMethod\_TextAvoidInfo \*info, double \*positionY)](#oh_textavoidinfo_getpositiony) | Obtains the Y coordinate from [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md). |
| [InputMethod\_ErrorCode OH\_TextAvoidInfo\_GetHeight(InputMethod\_TextAvoidInfo \*info, double \*height)](#oh_textavoidinfo_getheight) | Obtains the height from [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md). |

#### Function Description

#### \[h2\]OH\_TextAvoidInfo\_Create()

InputMethod\_TextAvoidInfo \*OH\_TextAvoidInfo\_Create(double positionY, double height)

**Description**

Creates an [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| double positionY | Y coordinate of the text box, in px. |
| double height | Height of the text box, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance is returned.

If the operation failed, **NULL** is returned, which may be caused by insufficient application address space.

 |

#### \[h2\]OH\_TextAvoidInfo\_Destroy()

void OH\_TextAvoidInfo\_Destroy(InputMethod\_TextAvoidInfo \*info)

**Description**

Destroys an [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \*info | Pointer to the [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance to be destroyed. |

#### \[h2\]OH\_TextAvoidInfo\_SetPositionY()

InputMethod\_ErrorCode OH\_TextAvoidInfo\_SetPositionY(InputMethod\_TextAvoidInfo \*info, double positionY)

**Description**

Sets the Y coordinate in [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \*info | Pointer to the [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance whose value is to be set. |
| double positionY | Y coordinate, that is, the absolute value of the distance between the text box's top vertex and the top edge of the physical screen, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextAvoidInfo\_SetHeight()

InputMethod\_ErrorCode OH\_TextAvoidInfo\_SetHeight(InputMethod\_TextAvoidInfo \*info, double height)

**Description**

Sets the height in [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \*info | Pointer to the [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance whose value is to be set. |
| double height | Height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextAvoidInfo\_GetPositionY()

InputMethod\_ErrorCode OH\_TextAvoidInfo\_GetPositionY(InputMethod\_TextAvoidInfo \*info, double \*positionY)

**Description**

Obtains the Y coordinate from [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \*info | Pointer to the [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance whose value is to be obtained. |
| double \*positionY | Y coordinate, that is, the absolute value of the distance between the text box's top vertex and the top edge of the physical screen, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextAvoidInfo\_GetHeight()

InputMethod\_ErrorCode OH\_TextAvoidInfo\_GetHeight(InputMethod\_TextAvoidInfo \*info, double \*height)

**Description**

Obtains the height from [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \*info | Pointer to the [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) instance whose value is to be obtained. |
| double \*height | Height of the text box, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |
