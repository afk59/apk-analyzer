# inputmethod\_text\_editor\_proxy\_capi.h

#### Overview

Provides a set of methods for the custom text box developed by the application to obtain notifications and requests from the input method application.

**File to include**: <inputmethod/inputmethod\_text\_editor\_proxy\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) | InputMethod\_TextEditorProxy | Represents the text box proxy. It provides methods for obtaining notifications and requests from the input method application. |

#### \[h2\]Function

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_TextEditorProxy\_GetTextConfigFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_TextConfig \*config)](#oh_texteditorproxy_gettextconfigfunc) | OH\_TextEditorProxy\_GetTextConfigFunc | Function called when the input method obtains the text box configuration. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetTextConfigFunc](#oh_texteditorproxy_setgettextconfigfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_InsertTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t \*text, size\_t length)](#oh_texteditorproxy_inserttextfunc) | OH\_TextEditorProxy\_InsertTextFunc | Function called when the input method application inserts text. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetInsertTextFunc](#oh_texteditorproxy_setinserttextfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_DeleteForwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)](#oh_texteditorproxy_deleteforwardfunc) | OH\_TextEditorProxy\_DeleteForwardFunc | Function called when the input method deletes the text on the right of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetDeleteForwardFunc](#oh_texteditorproxy_setdeleteforwardfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_DeleteBackwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)](#oh_texteditorproxy_deletebackwardfunc) | OH\_TextEditorProxy\_DeleteBackwardFunc | Function called when the input method deletes the text on the left of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetDeleteBackwardFunc](#oh_texteditorproxy_setdeletebackwardfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_SendKeyboardStatusFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_KeyboardStatus keyboardStatus)](#oh_texteditorproxy_sendkeyboardstatusfunc) | OH\_TextEditorProxy\_SendKeyboardStatusFunc | Function called when the input method notifies the keyboard status. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetSendKeyboardStatusFunc](#oh_texteditorproxy_setsendkeyboardstatusfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_SendEnterKeyFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_EnterKeyType enterKeyType)](#oh_texteditorproxy_sendenterkeyfunc) | OH\_TextEditorProxy\_SendEnterKeyFunc | Function called when the Enter key is pressed in the input method. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetSendEnterKeyFunc](#oh_texteditorproxy_setsendenterkeyfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_MoveCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_Direction direction)](#oh_texteditorproxy_movecursorfunc) | OH\_TextEditorProxy\_MoveCursorFunc | Function called when the cursor is moved in the input method. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetMoveCursorFunc](#oh_texteditorproxy_setmovecursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_HandleSetSelectionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t start, int32\_t end)](#oh_texteditorproxy_handlesetselectionfunc) | OH\_TextEditorProxy\_HandleSetSelectionFunc | Function called when the input method requests to select text. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetHandleSetSelectionFunc](#oh_texteditorproxy_sethandlesetselectionfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_HandleExtendActionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_ExtendAction action)](#oh_texteditorproxy_handleextendactionfunc) | OH\_TextEditorProxy\_HandleExtendActionFunc | Function called when the input method sends an extended editing operation. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetHandleExtendActionFunc](#oh_texteditorproxy_sethandleextendactionfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_GetLeftTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text\[\], size\_t \*length)](#oh_texteditorproxy_getlefttextofcursorfunc) | OH\_TextEditorProxy\_GetLeftTextOfCursorFunc | Function called when the input method obtains the text on the left of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc](#oh_texteditorproxy_setgetlefttextofcursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_GetRightTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text\[\], size\_t \*length)](#oh_texteditorproxy_getrighttextofcursorfunc) | OH\_TextEditorProxy\_GetRightTextOfCursorFunc | Function called when the input method obtains the text on the right of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc](#oh_texteditorproxy_setgetrighttextofcursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef int32\_t (\*OH\_TextEditorProxy\_GetTextIndexAtCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)](#oh_texteditorproxy_gettextindexatcursorfunc) | OH\_TextEditorProxy\_GetTextIndexAtCursorFunc | Function called when the input method obtains the index of the text where the cursor is located in the text box. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc](#oh_texteditorproxy_setgettextindexatcursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef int32\_t (\*OH\_TextEditorProxy\_ReceivePrivateCommandFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_PrivateCommand \*privateCommand\[\], size\_t size)](#oh_texteditorproxy_receiveprivatecommandfunc) | OH\_TextEditorProxy\_ReceivePrivateCommandFunc | Function called when the input method application sends a private data command. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetReceivePrivateCommandFunc](#oh_texteditorproxy_setreceiveprivatecommandfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef int32\_t (\*OH\_TextEditorProxy\_SetPreviewTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t text\[\], size\_t length, int32\_t start, int32\_t end)](#oh_texteditorproxy_setpreviewtextfunc) | OH\_TextEditorProxy\_SetPreviewTextFunc | Function called when the input method sets the text preview feature. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetSetPreviewTextFunc](#oh_texteditorproxy_setsetpreviewtextfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [typedef void (\*OH\_TextEditorProxy\_FinishTextPreviewFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)](#oh_texteditorproxy_finishtextpreviewfunc) | OH\_TextEditorProxy\_FinishTextPreviewFunc | Function called when the input method ends the text preview feature. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetFinishTextPreviewFunc](#oh_texteditorproxy_setfinishtextpreviewfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach). |
| [InputMethod\_TextEditorProxy \*OH\_TextEditorProxy\_Create(void)](#oh_texteditorproxy_create) | \- | Creates an [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance. |
| [void OH\_TextEditorProxy\_Destroy(InputMethod\_TextEditorProxy \*proxy)](#oh_texteditorproxy_destroy) | \- | Destroys an [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance. |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc getTextConfigFunc)](#oh_texteditorproxy_setgettextconfigfunc) | \- | Sets the [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc insertTextFunc)](#oh_texteditorproxy_setinserttextfunc) | \- | Sets the [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc deleteForwardFunc)](#oh_texteditorproxy_setdeleteforwardfunc) | \- | Sets the [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc deleteBackwardFunc)](#oh_texteditorproxy_setdeletebackwardfunc) | \- | Sets the [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc sendKeyboardStatusFunc)](#oh_texteditorproxy_setsendkeyboardstatusfunc) | \- | Sets the [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc sendEnterKeyFunc)](#oh_texteditorproxy_setsendenterkeyfunc) | \- | Sets the [OH\_TextEditorProxy\_SetSendEnterKeyFunc](#oh_texteditorproxy_setsendenterkeyfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc moveCursorFunc)](#oh_texteditorproxy_setmovecursorfunc) | \- | Sets the [OH\_TextEditorProxy\_SetMoveCursorFunc](#oh_texteditorproxy_setmovecursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc handleSetSelectionFunc)](#oh_texteditorproxy_sethandlesetselectionfunc) | \- | Sets the [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc handleExtendActionFunc)](#oh_texteditorproxy_sethandleextendactionfunc) | \- | Sets the [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)](#oh_texteditorproxy_setgetlefttextofcursorfunc) | \- | Sets the [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc getRightTextOfCursorFunc)](#oh_texteditorproxy_setgetrighttextofcursorfunc) | \- | Sets the [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)](#oh_texteditorproxy_setgettextindexatcursorfunc) | \- | Sets the [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc receivePrivateCommandFunc)](#oh_texteditorproxy_setreceiveprivatecommandfunc) | \- | Sets the [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc setPreviewTextFunc)](#oh_texteditorproxy_setsetpreviewtextfunc) | \- | Sets the [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc finishTextPreviewFunc)](#oh_texteditorproxy_setfinishtextpreviewfunc) | \- | Sets the [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc \*getTextConfigFunc)](#oh_texteditorproxy_getgettextconfigfunc) | \- | Obtains the [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc \*insertTextFunc)](#oh_texteditorproxy_getinserttextfunc) | \- | Obtains the [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc \*deleteForwardFunc)](#oh_texteditorproxy_getdeleteforwardfunc) | \- | Obtains the [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc \*deleteBackwardFunc)](#oh_texteditorproxy_getdeletebackwardfunc) | \- | Obtains the [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc \*sendKeyboardStatusFunc)](#oh_texteditorproxy_getsendkeyboardstatusfunc) | \- | Obtains the [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc \*sendEnterKeyFunc)](#oh_texteditorproxy_getsendenterkeyfunc) | \- | Obtains the [OH\_TextEditorProxy\_SendEnterKeyFunc](#oh_texteditorproxy_sendenterkeyfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc \*moveCursorFunc)](#oh_texteditorproxy_getmovecursorfunc) | \- | Obtains the [OH\_TextEditorProxy\_MoveCursorFunc](#oh_texteditorproxy_movecursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc \*handleSetSelectionFunc)](#oh_texteditorproxy_gethandlesetselectionfunc) | \- | Obtains the [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc \*handleExtendActionFunc)](#oh_texteditorproxy_gethandleextendactionfunc) | \- | Obtains the [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc \*getLeftTextOfCursorFunc)](#oh_texteditorproxy_getgetlefttextofcursorfunc) | \- | Obtains the [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc \*getRightTextOfCursorFunc)](#oh_texteditorproxy_getgetrighttextofcursorfunc) | \- | Obtains the [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc \*getTextIndexAtCursorFunc)](#oh_texteditorproxy_getgettextindexatcursorfunc) | \- | Obtains the [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc \*receivePrivateCommandFunc)](#oh_texteditorproxy_getreceiveprivatecommandfunc) | \- | Obtains the [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc \*setPreviewTextFunc)](#oh_texteditorproxy_getsetpreviewtextfunc) | \- | Obtains the [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc \*finishTextPreviewFunc)](#oh_texteditorproxy_getfinishtextpreviewfunc) | \- | Obtains the [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md). |

#### Function Description

#### \[h2\]OH\_TextEditorProxy\_GetTextConfigFunc()

typedef void (\*OH\_TextEditorProxy\_GetTextConfigFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_TextConfig \*config)

**Description**

Function called when the input method obtains the text box configuration. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetTextConfigFunc](#oh_texteditorproxy_setgettextconfigfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) \*config | Pointer to the [InputMethod\_TextConfig](../../structs/inputmethod-textconfig/document.md) instance. The memory to which this pointer points can be accessed only when this API is called. Once the callback returns, the memory will be released and must not be accessed thereafter. |

#### \[h2\]OH\_TextEditorProxy\_InsertTextFunc()

typedef void (\*OH\_TextEditorProxy\_InsertTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t \*text, size\_t length)

**Description**

Function called when the input method application inserts text. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetInsertTextFunc](#oh_texteditorproxy_setinserttextfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set.in. |
| const char16\_t \*text | Pointer to the characters to be inserted. The memory to which this pointer points can be accessed only when this API is called. Once the callback returns, the memory will be released and must not be accessed thereafter. |
| size\_t length | Length of the characters to be inserted. |

#### \[h2\]OH\_TextEditorProxy\_DeleteForwardFunc()

typedef void (\*OH\_TextEditorProxy\_DeleteForwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)

**Description**

Function called when the input method deletes the text on the right of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetDeleteForwardFunc](#oh_texteditorproxy_setdeleteforwardfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set.in. |
| int32\_t length | Length of the characters to be deleted. |

#### \[h2\]OH\_TextEditorProxy\_DeleteBackwardFunc()

typedef void (\*OH\_TextEditorProxy\_DeleteBackwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)

**Description**

Function called when the input method deletes the text on the left of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetDeleteBackwardFunc](#oh_texteditorproxy_setdeletebackwardfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set.in. |
| int32\_t length | Length of the characters to be deleted. |

#### \[h2\]OH\_TextEditorProxy\_SendKeyboardStatusFunc()

typedef void (\*OH\_TextEditorProxy\_SendKeyboardStatusFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_KeyboardStatus keyboardStatus)

**Description**

Function called when the input method notifies the keyboard status. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetSendKeyboardStatusFunc](#oh_texteditorproxy_setsendkeyboardstatusfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [InputMethod\_KeyboardStatus](../inputmethod-types-capi-h/document.md#inputmethod_keyboardstatus) keyboardStatus | Keyboard status. For details, see [InputMethod\_KeyboardStatus](../inputmethod-types-capi-h/document.md#inputmethod_keyboardstatus). |

#### \[h2\]OH\_TextEditorProxy\_SendEnterKeyFunc()

typedef void (\*OH\_TextEditorProxy\_SendEnterKeyFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_EnterKeyType enterKeyType)

**Description**

Function called when the Enter key is pressed in the input method. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetSendEnterKeyFunc](#oh_texteditorproxy_setsendenterkeyfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [InputMethod\_EnterKeyType](../inputmethod-types-capi-h/document.md#inputmethod_enterkeytype) enterKeyType | Enter key type. For details, see [InputMethod\_EnterKeyType](../inputmethod-types-capi-h/document.md#inputmethod_enterkeytype). |

#### \[h2\]OH\_TextEditorProxy\_MoveCursorFunc()

typedef void (\*OH\_TextEditorProxy\_MoveCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_Direction direction)

**Description**

Function called when the cursor is moved in the input method. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetMoveCursorFunc](#oh_texteditorproxy_setmovecursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [InputMethod\_Direction](../inputmethod-types-capi-h/document.md#inputmethod_direction) direction | Direction in which the cursor moves. For details, see [InputMethod\_Direction](../inputmethod-types-capi-h/document.md#inputmethod_direction). |

#### \[h2\]OH\_TextEditorProxy\_HandleSetSelectionFunc()

typedef void (\*OH\_TextEditorProxy\_HandleSetSelectionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t start, int32\_t end)

**Description**

Function called when the input method requests to select text. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetHandleSetSelectionFunc](#oh_texteditorproxy_sethandlesetselectionfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| int32\_t start | Start position of the selected text. |
| int32\_t end | End position of the selected text. |

#### \[h2\]OH\_TextEditorProxy\_HandleExtendActionFunc()

typedef void (\*OH\_TextEditorProxy\_HandleExtendActionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_ExtendAction action)

**Description**

Function called when the input method sends an extended editing operation. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetHandleExtendActionFunc](#oh_texteditorproxy_sethandleextendactionfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [InputMethod\_ExtendAction](../inputmethod-types-capi-h/document.md#inputmethod_extendaction) action | Extended editing operation. For details, see [InputMethod\_ExtendAction](../inputmethod-types-capi-h/document.md#inputmethod_extendaction). |

#### \[h2\]OH\_TextEditorProxy\_GetLeftTextOfCursorFunc()

typedef void (\*OH\_TextEditorProxy\_GetLeftTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text\[\], size\_t \*length)

**Description**

Function called when the input method obtains the text on the left of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc](#oh_texteditorproxy_setgetlefttextofcursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| int32\_t number | Length of the text to be obtained. |
| char16\_t text\[\] | Text content of a specified length on the left of the cursor. You need to assign a value to the text content in the function implementation. The memory to which this pointer points can be accessed only when this API is called. Once the callback returns, the memory will be released and must not be accessed thereafter. |
| size\_t \*length | Pointer to the length of the text on the left of the cursor. You need to transfer this parameter. |

#### \[h2\]OH\_TextEditorProxy\_GetRightTextOfCursorFunc()

typedef void (\*OH\_TextEditorProxy\_GetRightTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text\[\], size\_t \*length)

**Description**

Function called when the input method obtains the text on the right of the cursor. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc](#oh_texteditorproxy_setgetrighttextofcursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| int32\_t number | Length of the text to be obtained. |
| char16\_t text\[\] | Text content of a specified length on the right of the cursor. You need to assign a value to the text content in the function implementation. The memory to which this pointer points can be accessed only when this API is called. Once the callback returns, the memory will be released and must not be accessed thereafter. |
| size\_t \*length | Pointer to the length of the text on the right of the cursor. You need to transfer this parameter. |

#### \[h2\]OH\_TextEditorProxy\_GetTextIndexAtCursorFunc()

typedef int32\_t (\*OH\_TextEditorProxy\_GetTextIndexAtCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)

**Description**

Function called when the input method obtains the index of the text where the cursor is located in the text box. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc](#oh_texteditorproxy_setgettextindexatcursorfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Index of the text where the cursor is located. |

#### \[h2\]OH\_TextEditorProxy\_ReceivePrivateCommandFunc()

typedef int32\_t (\*OH\_TextEditorProxy\_ReceivePrivateCommandFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_PrivateCommand \*privateCommand\[\], size\_t size)

**Description**

Function called when the input method application sends a private data command. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetReceivePrivateCommandFunc](#oh_texteditorproxy_setreceiveprivatecommandfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [InputMethod\_PrivateCommand](../../structs/inputmethod-privatecommand/document.md) \*privateCommand\[\] | Private data command. The memory to which this pointer points can be accessed only when this API is called. Once the callback returns, the memory will be released and must not be accessed thereafter. |
| size\_t size | Size of the private data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Processing result of the private data command. |

#### \[h2\]OH\_TextEditorProxy\_SetPreviewTextFunc()

typedef int32\_t (\*OH\_TextEditorProxy\_SetPreviewTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t text\[\], size\_t length, int32\_t start, int32\_t end)

**Description**

Function called when the input method sets the text preview feature. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetSetPreviewTextFunc](#oh_texteditorproxy_setsetpreviewtextfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| const char16\_t text\[\] | Text requested to be previewed. The memory to which this pointer points can be accessed only when this API is called. Once the callback returns, the memory will be released and must not be accessed thereafter. |
| size\_t length | Length of the text to be previewed. |
| int32\_t start | Starting cursor position of the text to be previewed. |
| int32\_t end | Ending cursor position of the text to be previewed. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Result of setting text preview. |

#### \[h2\]OH\_TextEditorProxy\_FinishTextPreviewFunc()

typedef void (\*OH\_TextEditorProxy\_FinishTextPreviewFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)

**Description**

Function called when the input method ends the text preview feature. You need to implement this function, set it to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) via [OH\_TextEditorProxy\_SetFinishTextPreviewFunc](#oh_texteditorproxy_setfinishtextpreviewfunc), and register it through [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*textEditorProxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |

#### \[h2\]OH\_TextEditorProxy\_Create()

InputMethod\_TextEditorProxy \*OH\_TextEditorProxy\_Create(void)

**Description**

Creates an [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \* | 
If the operation is successful, a pointer to the created [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance is returned.

If the operation failed, **NULL** is returned, which may be caused by insufficient application address space.

 |

#### \[h2\]OH\_TextEditorProxy\_Destroy()

void OH\_TextEditorProxy\_Destroy(InputMethod\_TextEditorProxy \*proxy)

**Description**

Destroys an [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be destroyed. |

#### \[h2\]OH\_TextEditorProxy\_SetGetTextConfigFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc getTextConfigFunc)

**Description**

Sets the [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) getTextConfigFunc | [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetInsertTextFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc insertTextFunc)

**Description**

Sets the [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) insertTextFunc | [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetDeleteForwardFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc deleteForwardFunc)

**Description**

Sets the [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) deleteForwardFunc | [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetDeleteBackwardFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc deleteBackwardFunc)

**Description**

Sets the [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) deleteBackwardFunc | [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetSendKeyboardStatusFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc sendKeyboardStatusFunc)

**Description**

Sets the [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) sendKeyboardStatusFunc | [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetSendEnterKeyFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc sendEnterKeyFunc)

**Description**

Sets the [OH\_TextEditorProxy\_SetSendEnterKeyFunc](#oh_texteditorproxy_setsendenterkeyfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_SendEnterKeyFunc](#oh_texteditorproxy_sendenterkeyfunc) sendEnterKeyFunc | [OH\_TextEditorProxy\_SendEnterKeyFunc](#oh_texteditorproxy_sendenterkeyfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetMoveCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc moveCursorFunc)

**Description**

Sets the [OH\_TextEditorProxy\_SetMoveCursorFunc](#oh_texteditorproxy_setmovecursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_MoveCursorFunc](#oh_texteditorproxy_movecursorfunc) moveCursorFunc | [OH\_TextEditorProxy\_MoveCursorFunc](#oh_texteditorproxy_movecursorfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetHandleSetSelectionFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc handleSetSelectionFunc)

**Description**

Sets the [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) handleSetSelectionFunc | [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetHandleExtendActionFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc handleExtendActionFunc)

**Description**

Sets the [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) handleExtendActionFunc | [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)

**Description**

Sets the [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) getLeftTextOfCursorFunc | [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc getRightTextOfCursorFunc)

**Description**

Sets the [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) getRightTextOfCursorFunc | [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)

**Description**

Sets the [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) getTextIndexAtCursorFunc | [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetReceivePrivateCommandFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc receivePrivateCommandFunc)

**Description**

Sets the [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) receivePrivateCommandFunc | [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetSetPreviewTextFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc setPreviewTextFunc)

**Description**

Sets the [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) setPreviewTextFunc | [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetFinishTextPreviewFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc finishTextPreviewFunc)

**Description**

Sets the [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) function to [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be set. |
| [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) finishTextPreviewFunc | [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) to be set to the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetGetTextConfigFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc \*getTextConfigFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) \*getTextConfigFunc | Function [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetInsertTextFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc \*insertTextFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) \*insertTextFunc | Function [OH\_TextEditorProxy\_InsertTextFunc](#oh_texteditorproxy_inserttextfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetDeleteForwardFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc \*deleteForwardFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) \*deleteForwardFunc | Function [OH\_TextEditorProxy\_DeleteForwardFunc](#oh_texteditorproxy_deleteforwardfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetDeleteBackwardFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc \*deleteBackwardFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) \*deleteBackwardFunc | Function [OH\_TextEditorProxy\_DeleteBackwardFunc](#oh_texteditorproxy_deletebackwardfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetSendKeyboardStatusFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc \*sendKeyboardStatusFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) \*sendKeyboardStatusFunc | Function [OH\_TextEditorProxy\_SendKeyboardStatusFunc](#oh_texteditorproxy_sendkeyboardstatusfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetSendEnterKeyFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc \*sendEnterKeyFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_SendEnterKeyFunc](#oh_texteditorproxy_sendenterkeyfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_SendEnterKeyFunc](#oh_texteditorproxy_sendenterkeyfunc) \*sendEnterKeyFunc | Function [OH\_TextEditorProxy\_SendEnterKeyFunc](#oh_texteditorproxy_sendenterkeyfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetMoveCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc \*moveCursorFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_MoveCursorFunc](#oh_texteditorproxy_movecursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_MoveCursorFunc](#oh_texteditorproxy_movecursorfunc) \*moveCursorFunc | Function [OH\_TextEditorProxy\_MoveCursorFunc](#oh_texteditorproxy_movecursorfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetHandleSetSelectionFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc \*handleSetSelectionFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) \*handleSetSelectionFunc | Function [OH\_TextEditorProxy\_HandleSetSelectionFunc](#oh_texteditorproxy_handlesetselectionfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetHandleExtendActionFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc \*handleExtendActionFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) \*handleExtendActionFunc | Function [OH\_TextEditorProxy\_HandleExtendActionFunc](#oh_texteditorproxy_handleextendactionfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc \*getLeftTextOfCursorFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) \*getLeftTextOfCursorFunc | Function [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](#oh_texteditorproxy_getlefttextofcursorfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc \*getRightTextOfCursorFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) \*getRightTextOfCursorFunc | Function [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](#oh_texteditorproxy_getrighttextofcursorfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc \*getTextIndexAtCursorFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) \*getTextIndexAtCursorFunc | Function [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](#oh_texteditorproxy_gettextindexatcursorfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetReceivePrivateCommandFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc \*receivePrivateCommandFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) \*receivePrivateCommandFunc | Function [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](#oh_texteditorproxy_receiveprivatecommandfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetSetPreviewTextFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc \*setPreviewTextFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) \*setPreviewTextFunc | Function [OH\_TextEditorProxy\_SetPreviewTextFunc](#oh_texteditorproxy_setpreviewtextfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_GetFinishTextPreviewFunc()

InputMethod\_ErrorCode OH\_TextEditorProxy\_GetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc \*finishTextPreviewFunc)

**Description**

Obtains the [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) function from [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) instance to be read. |
| [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) \*finishTextPreviewFunc | Function [OH\_TextEditorProxy\_FinishTextPreviewFunc](#oh_texteditorproxy_finishtextpreviewfunc) obtained from the proxy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
An error code.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - An unexpected null pointer.

For details about the error codes, see [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode).

 |

#### \[h2\]OH\_TextEditorProxy\_SetCallbackInMainThread()

InputMethod\_ErrorCode OH\_TextEditorProxy\_SetCallbackInMainThread(InputMethod\_TextEditorProxy \*proxy, bool isCallbackInMainThread)

**Description**

Configures the execution thread (main thread/IPC thread) for the callback function of **InputMethod\_TextEditorProxy**. This API controls all callbacks of **InputMethod\_TextEditorProxy** except [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc). The execution thread of [OH\_TextEditorProxy\_GetTextConfigFunc](#oh_texteditorproxy_gettextconfigfunc) is determined by the thread that calls [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach), and is not affected by this API. If this callback needs to be executed on the main thread, ensure that [OH\_InputMethodController\_Attach](../inputmethod-controller-capi-h/document.md#oh_inputmethodcontroller_attach) is called on the main thread.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [InputMethod\_TextEditorProxy](../../structs/inputmethod-texteditorproxy/document.md) \*proxy | Pointer to the target **InputMethod\_TextEditorProxy** instance. |
| bool isCallbackInMainThread | Thread execution policy. - **true**: The callback executes on the main thread to avoid multithreaded concurrency. Do not perform time-consuming operations in the callback, as this may block the main thread. - **false**: The callback executes on an IPC thread (which may result in multithreaded concurrency). |

**Returns**

| Type | Description |
| :-- | :-- |
| [InputMethod\_ErrorCode](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) | 
Execution result.

[IME\_ERR\_OK](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - Success.

[IME\_ERR\_NULL\_POINTER](../inputmethod-types-capi-h/document.md#inputmethod_errorcode) - It is returned when **proxy** is **null**.

 |
