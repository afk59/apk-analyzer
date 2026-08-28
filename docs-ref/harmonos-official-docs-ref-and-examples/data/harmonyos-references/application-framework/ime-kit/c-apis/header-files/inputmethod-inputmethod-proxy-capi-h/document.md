# inputmethod\_inputmethod\_proxy\_capi.h

#### Overview

Provides methods for using the input method, allowing requests and notifications to be sent to the input method application.

**File to include**: <inputmethod/inputmethod\_inputmethod\_proxy\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) | InputMethod\_InputMethodProxy | Input method proxy object, which can be used to call the method for using the input method. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)](#oh_inputmethodproxy_showkeyboard) | Displays the keyboard. |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowTextInput(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_AttachOptions \*options)](#oh_inputmethodproxy_showtextinput) | Displays the text box. |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_HideKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)](#oh_inputmethodproxy_hidekeyboard) | Hides the keyboard. |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifySelectionChange(InputMethod\_InputMethodProxy \*inputMethodProxy, char16\_t text\[\], size\_t length, int start, int end)](#oh_inputmethodproxy_notifyselectionchange) | Notifies the input method application of the change in the selected text area, including the change of text content, cursor position, or the selected text. |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyConfigurationChange(InputMethod\_InputMethodProxy \*inputMethodProxy,InputMethod\_EnterKeyType enterKey, InputMethod\_TextInputType textType)](#oh_inputmethodproxy_notifyconfigurationchange) | Notifies the change of the text box configuration. |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyCursorUpdate(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_CursorInfo \*cursorInfo)](#oh_inputmethodproxy_notifycursorupdate) | Notifies the change of the cursor position. |
| [InputMethod\_ErrorCode OH\_InputMethodProxy\_SendPrivateCommand(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_PrivateCommand \*privateCommand\[\], size\_t size)](#oh_inputmethodproxy_sendprivatecommand) | Sends a private data command. |

#### Function Description

#### \[h2\]OH\_InputMethodProxy\_ShowKeyboard()

InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)

**Description**

Displays the keyboard.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodProxy\_ShowTextInput()

InputMethod\_ErrorCode OH\_InputMethodProxy\_ShowTextInput(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_AttachOptions \*options)

**Description**

Displays the text box.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \*options | 
Pointer to the [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance, which is used to obtain the configuration options.

In this API, you only need to pay attention to [InputMethod\_RequestKeyboardReason](../inputmethod-types-capi-h/document.md#inputmethod_requestkeyboardreason), which indicates the reason for requesting the keyboard.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodProxy\_HideKeyboard()

InputMethod\_ErrorCode OH\_InputMethodProxy\_HideKeyboard(InputMethod\_InputMethodProxy \*inputMethodProxy)

**Description**

Hides the keyboard.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodProxy\_NotifySelectionChange()

InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifySelectionChange(InputMethod\_InputMethodProxy \*inputMethodProxy, char16\_t text\[\], size\_t length, int start, int end)

**Description**

Notifies the input method application of the change in the selected text area, including the change of text content, cursor position, or the selected text.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| text | Entire input text. |
| size\_t length | Length of the **text** parameter. Maximum length: 8 KB. |
| int start | Start position of the selected text. |
| int end | End position of the selected text. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_PARAMCHECK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Parameter error.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodProxy\_NotifyConfigurationChange()

InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyConfigurationChange(InputMethod\_InputMethodProxy \*inputMethodProxy,InputMethod\_EnterKeyType enterKey, InputMethod\_TextInputType textType)

**Description**

Notifies the change of the text box configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [InputMethod\_EnterKeyType](../inputmethod-types-capi-h/document.md#inputmethod_enterkeytype) enterKey | Enter key type. |
| [InputMethod\_TextInputType](../inputmethod-types-capi-h/document.md#inputmethod_textinputtype) textType | Text box type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_PARAMCHECK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Parameter error.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodProxy\_NotifyCursorUpdate()

InputMethod\_ErrorCode OH\_InputMethodProxy\_NotifyCursorUpdate(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_CursorInfo \*cursorInfo)

**Description**

Notifies the cursor position change.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) \*cursorInfo | Pointer to the [InputMethod\_CursorInfo](../../structs/inputmethod-cursorinfo/document.md) instance, indicating the cursor information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_PARAMCHECK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Parameter error.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodProxy\_SendPrivateCommand()

InputMethod\_ErrorCode OH\_InputMethodProxy\_SendPrivateCommand(InputMethod\_InputMethodProxy \*inputMethodProxy, InputMethod\_PrivateCommand \*privateCommand\[\], size\_t size)

**Description**

Sends a private data command.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*privateCommand\[\] | Private command that is defined in [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md). The maximum size is 32 KB. |
| size\_t size | Size of the private command array. The maximum size is 5. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_PARAMCHECK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Parameter error.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_DETACHED](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method not bound.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |
