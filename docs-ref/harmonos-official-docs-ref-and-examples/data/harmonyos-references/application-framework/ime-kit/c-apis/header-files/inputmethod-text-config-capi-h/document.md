# inputmethod\_text\_config\_capi.h

#### Overview

Provides methods for creating, destroying, reading, and writing the text box configuration information objects.

**File to include**: <inputmethod/inputmethod\_text\_config\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) | InputMethod\_TextConfig | Text box configuration. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig \*OH\_TextConfig\_Create(void)](#oh_textconfig_create) | Creates an [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance. |
| [void OH\_TextConfig\_Destroy(InputMethod\_TextConfig \*config)](#oh_textconfig_destroy) | Destroys an [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetInputType(InputMethod\_TextConfig \*config, InputMethod\_TextInputType inputType)](#oh_textconfig_setinputtype) | Sets the text box type. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetEnterKeyType(InputMethod\_TextConfig \*config, InputMethod\_EnterKeyType enterKeyType)](#oh_textconfig_setenterkeytype) | Sets the Enter key type. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetPreviewTextSupport(InputMethod\_TextConfig \*config, bool supported)](#oh_textconfig_setpreviewtextsupport) | Sets the text preview feature. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetSelection(InputMethod\_TextConfig \*config, int32\_t start, int32\_t end)](#oh_textconfig_setselection) | Sets the selected text area. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetWindowId(InputMethod\_TextConfig \*config, int32\_t windowId)](#oh_textconfig_setwindowid) | Sets the window ID. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetPlaceholder(InputMethod\_TextConfig \*config, const char16\_t \*placeholder,size\_t length)](#oh_textconfig_setplaceholder) | Sets the placeholder text. |
| [InputMethod\_ErrorCode OH\_TextConfig\_SetAbilityName(InputMethod\_TextConfig \*config, const char16\_t \*abilityName,size\_t length)](#oh_textconfig_setabilityname) | Sets the ability name. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetInputType(InputMethod\_TextConfig \*config, InputMethod\_TextInputType \*inputType)](#oh_textconfig_getinputtype) | Obtains the text box type. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetEnterKeyType(InputMethod\_TextConfig \*config, InputMethod\_EnterKeyType \*enterKeyType)](#oh_textconfig_getenterkeytype) | Obtains the Enter key type. |
| [InputMethod\_ErrorCode OH\_TextConfig\_IsPreviewTextSupported(InputMethod\_TextConfig \*config, bool \*supported)](#oh_textconfig_ispreviewtextsupported) | Obtains whether the text preview feature is supported. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetCursorInfo(InputMethod\_TextConfig \*config, InputMethod\_CursorInfo \*\*cursorInfo)](#oh_textconfig_getcursorinfo) | Obtains the cursor information. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetTextAvoidInfo(InputMethod\_TextConfig \*config, InputMethod\_TextAvoidInfo \*\*avoidInfo)](#oh_textconfig_gettextavoidinfo) | Obtains the avoidance information. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetSelection(InputMethod\_TextConfig \*config, int32\_t \*start, int32\_t \*end)](#oh_textconfig_getselection) | Obtains the selected text area. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetWindowId(InputMethod\_TextConfig \*config, int32\_t \*windowId)](#oh_textconfig_getwindowid) | Obtains the window ID. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetPlaceholder(InputMethod\_TextConfig \*config, char16\_t \*placeholder,size\_t \*length)](#oh_textconfig_getplaceholder) | Obtains the placeholder text. |
| [InputMethod\_ErrorCode OH\_TextConfig\_GetAbilityName(InputMethod\_TextConfig \*config, char16\_t \*abilityName,size\_t \*length)](#oh_textconfig_getabilityname) | Obtains the ability name. |

#### Function Description

#### \[h2\]OH\_TextConfig\_Create()

InputMethod\_TextConfig \*OH\_TextConfig\_Create(void)

**Description**

Creates an [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance is returned.

If the operation failed, **NULL** is returned, which may be caused by insufficient application address space.

 |

#### \[h2\]OH\_TextConfig\_Destroy()

void OH\_TextConfig\_Destroy(InputMethod\_TextConfig \*config)

**Description**

Destroys an [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance to be destroyed. |

#### \[h2\]OH\_TextConfig\_SetInputType()

InputMethod\_ErrorCode OH\_TextConfig\_SetInputType(InputMethod\_TextConfig \*config, InputMethod\_TextInputType inputType)

**Description**

Sets the text box type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| [InputMethod\_TextInputType](../inputmethod-types-capi-h/document.md#inputmethod_textinputtype) inputType | Input type of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_SetEnterKeyType()

InputMethod\_ErrorCode OH\_TextConfig\_SetEnterKeyType(InputMethod\_TextConfig \*config, InputMethod\_EnterKeyType enterKeyType)

**Description**

Sets the Enter key type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| [InputMethod\_EnterKeyType](../inputmethod-types-capi-h/document.md#inputmethod_enterkeytype) enterKeyType | Enter key type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_SetPreviewTextSupport()

InputMethod\_ErrorCode OH\_TextConfig\_SetPreviewTextSupport(InputMethod\_TextConfig \*config, bool supported)

**Description**

Sets the text preview feature.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| bool supported | Whether text preview is supported. **true**: Text preview is supported. **false**: Text preview is not supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_SetSelection()

InputMethod\_ErrorCode OH\_TextConfig\_SetSelection(InputMethod\_TextConfig \*config, int32\_t start, int32\_t end)

**Description**

Sets the selected text area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| int32\_t start | Start position of the selected text. |
| int32\_t end | End position of the selected text. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_SetWindowId()

InputMethod\_ErrorCode OH\_TextConfig\_SetWindowId(InputMethod\_TextConfig \*config, int32\_t windowId)

**Description**

Sets the window ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| int32\_t windowId | Window ID of the application bound to the input method. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_SetPlaceholder()

InputMethod\_ErrorCode OH\_TextConfig\_SetPlaceholder(InputMethod\_TextConfig \*config, const char16\_t \*placeholder,size\_t length)

**Description**

Sets the placeholder text.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| const char16\_t \*placeholder | Pointer to a UTF-16 encoded double-byte string. If a null pointer is passed, the placeholder text is an empty string. |
| size\_t length | Number of elements in the memory to which **placeholder** points, including the null character of the double-byte string.1. If **length** is **0**, the placeholder text is an empty string.2. The maximum length of UTF-16 encoding is 255 characters (the null character of the string is not included in the count). If the length exceeds 255 characters, the extra characters will be truncated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
[InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode):

**IME\_ERR\_OK** = **0**: indicates success.

**IME\_ERR\_NULL\_POINTER** = **12802000**: indicates an unexpected null pointer.

 |

#### \[h2\]OH\_TextConfig\_SetAbilityName()

InputMethod\_ErrorCode OH\_TextConfig\_SetAbilityName(InputMethod\_TextConfig \*config, const char16\_t \*abilityName,size\_t length)

**Description**

Sets the ability name.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be set. |
| const char16\_t \*abilityName | Pointer to a UTF-16 encoded double-byte string. If a null pointer is passed, the ability name is an empty string. |
| size\_t length | Number of elements in the memory to which **abilityName** points, including the null character of the double-byte string.1. If **length** is **0**, the ability name is set to an empty string.2. The maximum length of UTF-16 encoding is 127 characters (the null character of the string is not included in the count). If the length exceeds 127 characters, the extra characters will be truncated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
[InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode):

**IME\_ERR\_OK** = **0**: indicates success.

**IME\_ERR\_NULL\_POINTER** = **12802000**: indicates an unexpected null pointer.

 |

#### \[h2\]OH\_TextConfig\_GetInputType()

InputMethod\_ErrorCode OH\_TextConfig\_GetInputType(InputMethod\_TextConfig \*config, InputMethod\_TextInputType \*inputType)

**Description**

Obtains the text box type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| [InputMethod\_TextInputType](../inputmethod-types-capi-h/document.md#inputmethod_textinputtype) \*inputType | Pointer to the [InputMethod\_TextInputType](../inputmethod-types-capi-h/document.md#inputmethod_textinputtype) instance. Input type of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_GetEnterKeyType()

InputMethod\_ErrorCode OH\_TextConfig\_GetEnterKeyType(InputMethod\_TextConfig \*config, InputMethod\_EnterKeyType \*enterKeyType)

**Description**

Obtains the Enter key type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| [InputMethod\_EnterKeyType](../inputmethod-types-capi-h/document.md#inputmethod_enterkeytype) \*enterKeyType | Pointer to the [InputMethod\_EnterKeyType](../inputmethod-types-capi-h/document.md#inputmethod_enterkeytype) instance. Enter key type of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_IsPreviewTextSupported()

InputMethod\_ErrorCode OH\_TextConfig\_IsPreviewTextSupported(InputMethod\_TextConfig \*config, bool \*supported)

**Description**

Obtains whether the text preview feature is supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| bool \*supported | Whether text preview is supported. **true**: Text preview is supported. **false**: Text preview is not supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_GetCursorInfo()

InputMethod\_ErrorCode OH\_TextConfig\_GetCursorInfo(InputMethod\_TextConfig \*config, InputMethod\_CursorInfo \*\*cursorInfo)

**Description**

Obtains the cursor information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) \*\*cursorInfo | Cursor information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_GetTextAvoidInfo()

InputMethod\_ErrorCode OH\_TextConfig\_GetTextAvoidInfo(InputMethod\_TextConfig \*config, InputMethod\_TextAvoidInfo \*\*avoidInfo)

**Description**

Obtains the avoidance information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Text configuration information. |
| [InputMethod\_TextAvoidInfo](../../structs/inputmethod-textavoidinfo/document.md) \*\*avoidInfo | Text box avoidance information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_GetSelection()

InputMethod\_ErrorCode OH\_TextConfig\_GetSelection(InputMethod\_TextConfig \*config, int32\_t \*start, int32\_t \*end)

**Description**

Obtains the selected text area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| int32\_t \*start | Start position of the selected text. |
| int32\_t \*end | End position of the selected text. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_GetWindowId()

InputMethod\_ErrorCode OH\_TextConfig\_GetWindowId(InputMethod\_TextConfig \*config, int32\_t \*windowId)

**Description**

Obtains the window ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| int32\_t \*windowId | Window ID of the application bound to the input method. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextConfig\_GetPlaceholder()

InputMethod\_ErrorCode OH\_TextConfig\_GetPlaceholder(InputMethod\_TextConfig \*config, char16\_t \*placeholder,size\_t \*length)

**Description**

Obtains the placeholder text.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| char16\_t \*placeholder | Pointer to the placeholder text. The memory of this pointer is maintained by the caller. |
| size\_t \*length | Pointer to the length of the placeholder text, in double bytes. The length includes the null character of the string.1. As an input parameter, **length** indicates the available length of the memory to which **placeholder** points. As an output parameter, it indicates the actual length of the placeholder text.2. If **placeholder** is a null pointer and **length** points to valid memory, **length** will be set to the actual length of the placeholder text, and an error will be thrown.3. If both **placeholder** and **length** point to valid memory, but the value of **length** is less than the actual length of the placeholder text, **length** will be set to the actual length of the placeholder text, and an error will be thrown. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
[InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode):

**IME\_ERR\_OK** = **0**: indicates success.

**IME\_ERR\_PARAMCHECK** = **401**: indicates that parameter check failed.

**IME\_ERR\_NULL\_POINTER** = **12802000**: indicates an unexpected null pointer.

 |

#### \[h2\]OH\_TextConfig\_GetAbilityName()

InputMethod\_ErrorCode OH\_TextConfig\_GetAbilityName(InputMethod\_TextConfig \*config, char16\_t \*abilityName,size\_t \*length)

**Description**

Obtains the ability name.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance whose value is to be obtained. |
| char16\_t \*abilityName | Pointer to the ability name. The memory of this pointer is maintained by the caller. |
| size\_t \*length | Pointer to the length of the ability name, in double bytes. The length includes the null character of the string.1. As an input parameter, **length** indicates the available length of the memory to which **abilityName** points. As an output parameter, it indicates the actual length of the ability name.2. If **abilityName** is a null pointer and **length** points to valid memory, **length** will be set to the actual length of the ability name, and an error will be thrown.3. If both **abilityName** and **length** point to valid memory, but the value of **length** is less than the actual length of the ability name, **length** will be set to the actual length of the ability name, and an error will be thrown. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
[InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode):

**IME\_ERR\_OK** = **0**: indicates success.

**IME\_ERR\_PARAMCHECK** = **401**: indicates that parameter check failed.

**IME\_ERR\_NULL\_POINTER** = **12802000**: indicates an unexpected null pointer.

 |
