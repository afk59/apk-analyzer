# Using the Input Method in a Custom Edit Box (C/C++)

#### When to Use

IME Kit allows you to use input method in the custom edit box to interact with input method applications, including displaying and hiding input methods and receiving text editing notifications from input method applications. This document describes how to use C/C++ to develop this function.

#### APIs

For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-inputmethod).

#### Adding Dynamic Link Libraries

Add the following library to **CMakeLists.txt**.

libohinputmethod.so

#### Including Header Files

#include <inputmethod/inputmethod\_controller\_capi.h>

#### Binding an Input Method

When the text box is focused, you can call the [OH\_InputMethodController\_Attach](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-inputmethod-controller-capi-h#oh_inputmethodcontroller_attach) API to bind the input method. After the binding is successful, you can use the input method to enter text.

1.  Create an **InputMethod\_TextEditorProxy** instance. The sample code is as follows:
    
    // Create an InputMethod\_TextEditorProxy instance.
    textEditorProxy = OH\_TextEditorProxy\_Create();
    
2.  Create an **InputMethod\_AttachOptions** instance and set the options for binding the input method. The sample code is as follows:
    
    // Create an InputMethod\_AttachOptions instance. showKeyboard specifies whether to display the keyboard after the binding is successful. The following uses displaying the target keyboard as an example.
    bool showKeyboard = true;
    attachOptions = OH\_AttachOptions\_Create(showKeyboard);
    
3.  Call **OH\_InputMethodController\_Attach** to bind the input method service. After the call is successful, you can obtain **InputMethod\_InputMethodProxy** used to interact with the input method. The sample code is as follows:
    
    // Send a binding request.
    auto ret = OH\_InputMethodController\_Attach(textEditorProxy, attachOptions, &inputMethodProxy);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Attach failed, ret=%{public}d.", ret);
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        OH\_AttachOptions\_Destroy(attachOptions);
        return;
    }
    

#### Displaying or Hiding the Panel

After the binding is successful, you can use the obtained [InputMethod\_InputMethodProxy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-inputmethod-inputmethod-inputmethodproxy) object to send a message to the input method. The sample code is as follows:

// Display the keyboard.
if (OH\_InputMethodProxy\_ShowKeyboard(inputMethodProxy) != InputMethod\_ErrorCode::IME\_ERR\_OK) {
    OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "ShowKeyboard failed!");
}
// Hide the keyboard.
if (OH\_InputMethodProxy\_HideKeyboard(inputMethodProxy) != InputMethod\_ErrorCode::IME\_ERR\_OK) {
    OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "HideKeyboard failed!");
}
// Notify the change of the input box configuration.
if (OH\_InputMethodProxy\_NotifyConfigurationChange(inputMethodProxy, InputMethod\_EnterKeyType::IME\_ENTER\_KEY\_GO, InputMethod\_TextInputType::IME\_TEXT\_INPUT\_TYPE\_TEXT) != InputMethod\_ErrorCode::IME\_ERR\_OK) {
    OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "NotifyConfigurationChange failed!");
}

#### Listening to Requests/Notifications from the Input Method Application

1.  Implement the response processing function for the request or notification sent by the input method application. The sample code is as follows:
    
    // Implement the input method application event response function in InputMethod\_TextEditorProxy.
    void GetTextConfig(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_TextConfig \*config)
    {
        // Process the request sent by the input method for obtaining the input box configuration.
    }
    void InsertText(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t \*text, size\_t length)
    {
        // Process the text insertion request sent by the input method.
    }
    void DeleteForward(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)
    {
        // Process the text deletion request sent by the input method.
    }
    // ......
    
2.  Set the implemented response function to [InputMethod\_TextEditorProxy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-inputmethod-inputmethod-texteditorproxy), and then set the response function to the input method framework using [OH\_InputMethodController\_Attach](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-inputmethod-controller-capi-h#oh_inputmethodcontroller_attach) called when the input method is bound to complete listener registration. The sample code is as follows:
    
    OH\_TextEditorProxy\_SetGetTextConfigFunc(textEditorProxy, GetTextConfigFunc);
    OH\_TextEditorProxy\_SetInsertTextFunc(textEditorProxy, InsertTextFunc);
    OH\_TextEditorProxy\_SetDeleteForwardFunc(textEditorProxy, DeleteForwardFunc);
    OH\_TextEditorProxy\_SetDeleteBackwardFunc(textEditorProxy, DeleteBackwardFunc);
    OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(textEditorProxy, SendKeyboardStatusFunc);
    OH\_TextEditorProxy\_SetSendEnterKeyFunc(textEditorProxy, SendEnterKeyFunc);
    OH\_TextEditorProxy\_SetMoveCursorFunc(textEditorProxy, MoveCursorFunc);
    OH\_TextEditorProxy\_SetHandleSetSelectionFunc(textEditorProxy, HandleSetSelectionFunc);
    OH\_TextEditorProxy\_SetHandleExtendActionFunc(textEditorProxy, HandleExtendActionFunc);
    OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(textEditorProxy, GetLeftTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(textEditorProxy, GetRightTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(textEditorProxy, GetTextIndexAtCursorFunc);
    OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(textEditorProxy, ReceivePrivateCommandFunc);
    OH\_TextEditorProxy\_SetSetPreviewTextFunc(textEditorProxy, SetPreviewTextFunc);
    OH\_TextEditorProxy\_SetFinishTextPreviewFunc(textEditorProxy, FinishTextPreviewFunc);
    

#### Unbinding an Input Method

When the edit box is out of focus, you need to stop using the input method and unbind the input method framework by calling [OH\_InputMethodController\_Detach](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-inputmethod-controller-capi-h#oh_inputmethodcontroller_detach).

// Send an unbinding request.
OH\_InputMethodController\_Detach(inputMethodProxy);
OH\_TextEditorProxy\_Destroy(textEditorProxy);
OH\_AttachOptions\_Destroy(attachOptions);

#### Sample Code

The sample code shows how to bind, hide, and unbind an input method.

The entry is the **InputMethodNdkDemo** function.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/du-VVLITTRebLS3W4SmCKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BE257143E97835D1028B4C550BB6B5F54A70CC2866575C07A529B0F27DB7F25)

Dependencies of **libohinputmethod.so** and **libhilog\_ndk.z.so** should be added to the **CMakeList.txt** file.

#include "napi/native\_api.h"
#include <codecvt>
#include <locale>
#include <thread>

#include "hilog/log.h"
#include "inputmethod/inputmethod\_controller\_capi.h"

 constexpr int32\_t TEXTSIZE = 1024;

static std::string g\_strText;
char g\_strTextChar\[TEXTSIZE\];
int32\_t g\_strTextCharLen = 0;
bool g\_flagShow = false;
std::mutex g\_textMutex;
InputMethod\_TextEditorProxy \*textEditorProxy = nullptr;
InputMethod\_AttachOptions \*attachOptions = nullptr;
InputMethod\_InputMethodProxy \*inputMethodProxy = nullptr;

void InputMethodDestroy();

void InitText()
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    if (g\_flagShow) {
        memset(g\_strTextChar, 0x00, sizeof(g\_strTextChar));
        g\_strTextCharLen = 0;
        g\_flagShow = false;
    }
}

void SetText(const char\* input)
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    g\_strTextCharLen = strlen(input);
    if (g\_strTextCharLen > TEXTSIZE) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Length greater than 1024 , ret=%{public}d", g\_strTextCharLen);
    }
    strncpy(g\_strTextChar, input, g\_strTextCharLen);
}

void GetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_TextConfig \*config)
{ // Process the request sent by the input method for obtaining the text box configuration.
    auto ret = OH\_TextConfig\_SetEnterKeyType(config, InputMethod\_EnterKeyType::IME\_ENTER\_KEY\_SEND);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "SetEnterKeyType failed, ret=%{public}d", ret);
        return;
    }

    ret = OH\_TextConfig\_SetInputType(config, InputMethod\_TextInputType::IME\_TEXT\_INPUT\_TYPE\_PHONE);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "SetInputType failed, ret=%{public}d", ret);
        return;
    }
}

void InsertTextFunc(InputMethod\_TextEditorProxy \*proxy, const char16\_t \*text, size\_t length)
{
    InitText();

    // Process the text insertion request.
    // Convert the string of the char16\_t type to u16string.
    std::u16string u16Str(text, length + 1);

    // Convert the string to the UTF-8 encoding format.
    std::wstring\_convert<std::codecvt\_utf8\_utf16<char16\_t>, char16\_t> converter;
    std::string utf8Str = converter.to\_bytes(u16Str);
    for (size\_t i = 0; i < utf8Str.size(); ++i) {
        unsigned char c = static\_cast<unsigned char>(utf8Str\[i\]);
        if (c != 0x00) {
            std::lock\_guard<std::mutex> lock(g\_textMutex);
            g\_strTextChar\[g\_strTextCharLen\] = c;
            g\_strTextCharLen += 1;
        }
    }
}

void DeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t length)
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    if (g\_strTextCharLen > 0) {
        strncpy(g\_strTextChar, g\_strTextChar + 1, g\_strTextCharLen - 1);
        g\_strTextCharLen = (g\_strTextCharLen > 0) ? g\_strTextCharLen - 1 : g\_strTextCharLen;
    }
}

void DeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t length)
{
    std::lock\_guard<std::mutex> lock(g\_textMutex);
    g\_strTextCharLen = (g\_strTextCharLen > 0) ? g\_strTextCharLen - 1 : g\_strTextCharLen;
    g\_strTextChar\[g\_strTextCharLen\] = '\\0';
}

void SendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_KeyboardStatus status)
{
    if (status == InputMethod\_KeyboardStatus::IME\_KEYBOARD\_STATUS\_HIDE) {
        g\_flagShow = false;
        SetText("The keyboard is hidden.");
    } else if (status == InputMethod\_KeyboardStatus::IME\_KEYBOARD\_STATUS\_SHOW && g\_flagShow != true) {
        g\_flagShow = true;
        SetText("The keyboard is displayed.");
    }
}

void SendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_EnterKeyType type)
{
    SetText("Process the Enter key request.");
    g\_flagShow = true;
}

void MoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_Direction direction)
{
    if (direction == InputMethod\_Direction::IME\_DIRECTION\_UP) {
        SetText("The cursor is moving upward.");
    } else if (direction == InputMethod\_Direction::IME\_DIRECTION\_DOWN) {
        SetText("The cursor is moving downward.");
    } else if (direction == InputMethod\_Direction::IME\_DIRECTION\_LEFT) {
        SetText("The cursor is moving left.");
    } else if (direction == InputMethod\_Direction::IME\_DIRECTION\_RIGHT) {
        SetText("The cursor is moving right.");
    } else {
        SetText("An error occurred while moving the cursor.");
    }
}

void HandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t start, int32\_t end)
{
    SetText("Process the selected text request.");
}

void HandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_ExtendAction action)
{
    SetText("Process the extended edit request.");
}

void GetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t number, char16\_t text\[\], size\_t \*length)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "Process the request for obtaining the text on the left of the cursor.");
}

void GetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, int32\_t number, char16\_t text\[\], size\_t \*length)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "Process the request for obtaining the text on the right of the cursor.");
}

int32\_t GetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "Process the request for obtaining the text index of the text box where the cursor is located.");
    return 0;
}
int32\_t ReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, InputMethod\_PrivateCommand \*privateCommand\[\],
    size\_t size)
{
    SetText("Process the extended edit request.");
    return 0;
}

int32\_t SetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, const char16\_t \*text, size\_t length, int32\_t start,
    int32\_t end)
{
    SetText("Process the request for setting the preview text.");
    return 0;
}

void FinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy)
{
    SetText("Process the request for ending the preview.");
}

void ConstructTextEditorProxy(InputMethod\_TextEditorProxy \*textEditorProxy)
{
    OH\_TextEditorProxy\_SetGetTextConfigFunc(textEditorProxy, GetTextConfigFunc);
    OH\_TextEditorProxy\_SetInsertTextFunc(textEditorProxy, InsertTextFunc);
    OH\_TextEditorProxy\_SetDeleteForwardFunc(textEditorProxy, DeleteForwardFunc);
    OH\_TextEditorProxy\_SetDeleteBackwardFunc(textEditorProxy, DeleteBackwardFunc);
    OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(textEditorProxy, SendKeyboardStatusFunc);
    OH\_TextEditorProxy\_SetSendEnterKeyFunc(textEditorProxy, SendEnterKeyFunc);
    OH\_TextEditorProxy\_SetMoveCursorFunc(textEditorProxy, MoveCursorFunc);
    OH\_TextEditorProxy\_SetHandleSetSelectionFunc(textEditorProxy, HandleSetSelectionFunc);
    OH\_TextEditorProxy\_SetHandleExtendActionFunc(textEditorProxy, HandleExtendActionFunc);
    OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(textEditorProxy, GetLeftTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(textEditorProxy, GetRightTextOfCursorFunc);
    OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(textEditorProxy, GetTextIndexAtCursorFunc);
    OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(textEditorProxy, ReceivePrivateCommandFunc);
    OH\_TextEditorProxy\_SetSetPreviewTextFunc(textEditorProxy, SetPreviewTextFunc);
    OH\_TextEditorProxy\_SetFinishTextPreviewFunc(textEditorProxy, FinishTextPreviewFunc);
}

void InputMethodNdkDemo()
{
    // Create an InputMethod\_TextEditorProxy instance.
    textEditorProxy = OH\_TextEditorProxy\_Create();
    if (textEditorProxy == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Create TextEditorProxy failed.");
        return;
    }

    // Set the implemented response processing function to InputMethod\_TextEditorProxy.
    ConstructTextEditorProxy(textEditorProxy);

    // Create an InputMethod\_AttachOptions instance. showKeyboard specifies whether to display the keyboard after the binding is successful. The following uses displaying the target keyboard as an example.
    bool showKeyboard = true;
    attachOptions = OH\_AttachOptions\_Create(showKeyboard);
    if (attachOptions == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Create AttachOptions failed.");
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        return;
    }

    // Send a binding request.
    auto ret = OH\_InputMethodController\_Attach(textEditorProxy, attachOptions, &inputMethodProxy);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "Attach failed, ret=%{public}d.", ret);
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        OH\_AttachOptions\_Destroy(attachOptions);
        return;
    }
}

static napi\_value InputMethodDestroy(napi\_env env, napi\_callback\_info info)
{
   // Hide the keyboard.
    int ret = OH\_InputMethodProxy\_HideKeyboard(inputMethodProxy);
    if (ret != IME\_ERR\_OK) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0, "testTag", "HideKeyboard failed, ret=%{public}d.", ret);
        OH\_TextEditorProxy\_Destroy(textEditorProxy);
        OH\_AttachOptions\_Destroy(attachOptions);
        return nullptr;
    }

    // Send an unbinding request.
    OH\_InputMethodController\_Detach(inputMethodProxy);
    OH\_TextEditorProxy\_Destroy(textEditorProxy);
    OH\_AttachOptions\_Destroy(attachOptions);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "testTag", "Finished.");
    return nullptr;
}

static napi\_value AttachInputMethod(napi\_env env, napi\_callback\_info info)
{
    InputMethodNdkDemo();

    napi\_value result;
    napi\_create\_string\_utf8(env,  g\_strText.c\_str(),  g\_strText.length(),  &result);
    return result;
}

static napi\_value GetText(napi\_env env, napi\_callback\_info info)
{
    napi\_value result;
    napi\_create\_string\_utf8(env, g\_strTextChar, g\_strTextCharLen,  &result);
    return result;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "attachInputMethod", nullptr, AttachInputMethod, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "getText", nullptr, GetText, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "inputMethodDestroy", nullptr, InputMethodDestroy, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}
