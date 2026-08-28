# inputmethod\_cursor\_info\_capi.h

#### Overview

Provides methods for creating, destroying, reading, and writing cursor information objects.

**File to include**: <inputmethod/inputmethod\_cursor\_info\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) | InputMethod\_CursorInfo | Represents the cursor information, including the coordinates, width, and height of the cursor. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [InputMethod\_CursorInfo \*OH\_CursorInfo\_Create(double left, double top, double width, double height)](#oh_cursorinfo_create) | Creates an [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance. |
| [void OH\_CursorInfo\_Destroy(InputMethod\_CursorInfo \*cursorInfo)](#oh_cursorinfo_destroy) | Destroys an [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance. |
| [InputMethod\_ErrorCode OH\_CursorInfo\_SetRect(InputMethod\_CursorInfo \*cursorInfo, double left, double top, double width, double height)](#oh_cursorinfo_setrect) | Sets the cursor information. |
| [InputMethod\_ErrorCode OH\_CursorInfo\_GetRect(InputMethod\_CursorInfo \*cursorInfo, double \*left, double \*top, double \*width, double \*height)](#oh_cursorinfo_getrect) | Obtains the cursor information. |

#### Function Description

#### \[h2\]OH\_CursorInfo\_Create()

InputMethod\_CursorInfo \*OH\_CursorInfo\_Create(double left, double top, double width, double height)

**Description**

Creates an [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| double left | Absolute value of the distance between the cursor's leftmost point and the left edge of the physical screen, in px. |
| double top | Absolute value of the distance between the cursor's top point and the top edge of the physical screen, in px. |
| double width | Width, in px. |
| double height | Height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance is returned.

If the operation fails, **NULL** is returned. This may occur when the application's address space is exhausted.

 |

#### \[h2\]OH\_CursorInfo\_Destroy()

void OH\_CursorInfo\_Destroy(InputMethod\_CursorInfo \*cursorInfo)

**Description**

Destroys an [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) \*cursorInfo | Pointer to the [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance to be destroyed. |

#### \[h2\]OH\_CursorInfo\_SetRect()

InputMethod\_ErrorCode OH\_CursorInfo\_SetRect(InputMethod\_CursorInfo \*cursorInfo, double left, double top, double width, double height)

**Description**

Sets the cursor information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) \*cursorInfo | Pointer to the [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance. |
| double left | Absolute value of the distance between the cursor's leftmost point and the left edge of the physical screen, in px. |
| double top | Absolute value of the distance between the cursor's top point and the top edge of the physical screen, in px. |
| double width | Width, in px. |
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

#### \[h2\]OH\_CursorInfo\_GetRect()

InputMethod\_ErrorCode OH\_CursorInfo\_GetRect(InputMethod\_CursorInfo \*cursorInfo, double \*left, double \*top, double \*width, double \*height)

**Description**

Obtains the cursor information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) \*cursorInfo | Pointer to the [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance. |
| double \*left | Absolute value of the distance between the cursor's leftmost point and the left edge of the physical screen, in px. |
| double \*top | Absolute value of the distance between the cursor's top point and the top edge of the physical screen, in px. |
| double \*width | Width, in px. |
| double \*height | Height, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |
