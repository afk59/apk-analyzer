# inputmethod\_controller\_capi.h

#### Overview

Provides methods for binding and unbinding input methods.

**File to include**: <inputmethod/inputmethod\_controller\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode OH\_InputMethodController\_Attach(InputMethod\_TextEditorProxy \*textEditorProxy,InputMethod\_AttachOptions \*options, InputMethod\_InputMethodProxy \*\*inputMethodProxy)](#oh_inputmethodcontroller_attach) | Binds an application to the input method service. |
| [InputMethod\_ErrorCode OH\_InputMethodController\_Detach(InputMethod\_InputMethodProxy \*inputMethodProxy)](#oh_inputmethodcontroller_detach) | Unbinds an application from the input method service. |

#### Function Description

#### \[h2\]OH\_InputMethodController\_Attach()

InputMethod\_ErrorCode OH\_InputMethodController\_Attach(InputMethod\_TextEditorProxy \*textEditorProxy,InputMethod\_AttachOptions \*options, InputMethod\_InputMethodProxy \*\*inputMethodProxy)

**Description**

Binds an application to the input method service.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance. The caller needs to manage the **textEditorProxy** lifecycle. If the calling is successful, the caller cannot release **textEditorProxy** before the next binding or unbinding call. |
| [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) \*options | Pointer to the [InputMethod\_AttachOptions](../../structs/inputmethod-attachoptions/document.md) instance. This parameter is used to specify the options of attaching an input method. |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*\*inputMethodProxy | Double pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance. The lifecycle lasts until the next binding or unbinding call. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_PARAMCHECK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Parameter error.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_InputMethodController\_Detach()

InputMethod\_ErrorCode OH\_InputMethodController\_Detach(InputMethod\_InputMethodProxy \*inputMethodProxy)

**Description**

Unbinds an application from the input method service.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) \*inputMethodProxy | Pointer to the [InputMethod\_InputMethodProxy](../../structs/inputmethod-inputmethodproxy/document.md) instance obtained by calling [OH\_InputMethodController\_Attach](#oh_inputmethodcontroller_attach). |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_IMCLIENT](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Client error in input method.

[IME\_ERR\_IMMS](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Input method service error.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |
