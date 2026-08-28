# inputmethod\_attach\_options\_capi.h

#### Overview

Provides methods for creating, destroying, reading, and writing the option object bound to the input method.

**File to include**: <inputmethod/inputmethod\_attach\_options\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) | InputMethod\_AttachOptions | Options for binding the input method. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [InputMethod\_AttachOptions \*OH\_AttachOptions\_Create(bool showKeyboard)](#oh_attachoptions_create) | Creates an [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance. |
| [InputMethod\_AttachOptions \*OH\_AttachOptions\_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod\_RequestKeyboardReason requestKeyboardReason)](#oh_attachoptions_createwithrequestkeyboardreason) | Creates an [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance. |
| [void OH\_AttachOptions\_Destroy(InputMethod\_AttachOptions \*options)](#oh_attachoptions_destroy) | Destroys an [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance. |
| [InputMethod\_ErrorCode OH\_AttachOptions\_IsShowKeyboard(InputMethod\_AttachOptions \*options, bool \*showKeyboard)](#oh_attachoptions_isshowkeyboard) | Obtains the value that indicates whether to display the keyboard from [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md). |
| [InputMethod\_ErrorCode OH\_AttachOptions\_GetRequestKeyboardReason(InputMethod\_AttachOptions \*options, int \*requestKeyboardReason)](#oh_attachoptions_getrequestkeyboardreason) | Obtains the reason that triggers the input method from [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md). |

#### Function Description

#### \[h2\]OH\_AttachOptions\_Create()

InputMethod\_AttachOptions \*OH\_AttachOptions\_Create(bool showKeyboard)

**Description**

Creates an [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| bool showKeyboard | Pointer to whether to display the keyboard during binding. **true**: The keyboard is displayed after the binding is complete. **false**: The keyboard is hidden after the binding is complete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance is returned.

If the operation failed, **NULL** is returned, which may be caused by insufficient application address space.

 |

#### \[h2\]OH\_AttachOptions\_CreateWithRequestKeyboardReason()

InputMethod\_AttachOptions \*OH\_AttachOptions\_CreateWithRequestKeyboardReason(bool showKeyboard, InputMethod\_RequestKeyboardReason requestKeyboardReason)

**Description**

Creates an [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| bool showKeyboard | Pointer to whether to display the keyboard during binding. **true**: The keyboard is displayed after the binding is complete. **false**: The keyboard is hidden after the binding is complete. |
| [InputMethod\_RequestKeyboardReason](../inputmethod-types-capi-h/document.md#inputmethod_requestkeyboardreason) requestKeyboardReason | Reason for requesting the keyboard. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance is returned.

If the operation failed, **NULL** is returned, which may be caused by insufficient application address space.

 |

#### \[h2\]OH\_AttachOptions\_Destroy()

void OH\_AttachOptions\_Destroy(InputMethod\_AttachOptions \*options)

**Description**

Destroys an [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \*options | [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance to be destroyed. |

#### \[h2\]OH\_AttachOptions\_IsShowKeyboard()

InputMethod\_ErrorCode OH\_AttachOptions\_IsShowKeyboard(InputMethod\_AttachOptions \*options, bool \*showKeyboard)

**Description**

Obtains the value that indicates whether to display the keyboard from [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \*options | Pointer to the [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance whose value is to be read. |
| bool \*showKeyboard | Pointer to whether to display the keyboard during binding. **true**: The keyboard is displayed after the binding is complete. **false**: The keyboard is hidden after the binding is complete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_AttachOptions\_GetRequestKeyboardReason()

InputMethod\_ErrorCode OH\_AttachOptions\_GetRequestKeyboardReason(InputMethod\_AttachOptions \*options, int \*requestKeyboardReason)

**Description**

Obtains the reason for requesting the keyboard from [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md).

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \*options | Pointer to the [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance whose value is to be read. |
| int \*requestKeyboardReason | Pointer to the reason for requesting the keyboard. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |
