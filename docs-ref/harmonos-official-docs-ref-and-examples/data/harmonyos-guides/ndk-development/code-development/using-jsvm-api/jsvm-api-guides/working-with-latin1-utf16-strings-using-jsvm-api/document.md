# Working with Latin1/UTF16 Strings Using JSVM-API

#### Introduction

This topic walks you through on how to create and use external strings using JSVM-API.

#### Basic Concepts

By using JSVM-API, you can create JavaScript strings directly in the memory allocated for Latin1/UTF16 strings. This allows you to manipulate these strings like normal JavaScript strings.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateExternalStringLatin1 | Creates an external JS string from a C string encoded in ISO-8859-1 format. |
| OH\_JSVM\_CreateExternalStringUtf16 | Creates an external JS string from a C string encoded in UTF16-LE format. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in manipulating external strings.

## Determining a Number Object

CPP code:

#include <cstring>
#include <string>
static char stringLatin1\[\] = "hello";
static char16\_t stringUTF16\[\] = u"world";

static JSVM\_Value testExternalString(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_VM vm;
    OH\_JSVM\_GetVM(env, &vm);

    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);
    JSVM\_Value jsStrLatin1 = nullptr;
    bool copied = true;
    char buf\[10\];
    OH\_JSVM\_CreateExternalStringLatin1(env, stringLatin1, strlen(stringLatin1), nullptr, nullptr,
                                       &jsStrLatin1, &copied);
    OH\_JSVM\_GetValueStringUtf8(env, jsStrLatin1, buf, 10, nullptr);
    OH\_LOG\_INFO(LOG\_APP, "created latin1 string is : %{public}s\\n", buf);
    // If the value of copied is true, the external string fails to be created. Otherwise, the external string is created successfully.
    OH\_LOG\_INFO(LOG\_APP, "create external string failed : %{public}d\\n", copied);
    copied = true;
    JSVM\_Value jsStrUTF16 = nullptr;
    OH\_JSVM\_CreateExternalStringUtf16(env, stringUTF16, std::char\_traits<char16\_t>::length(stringUTF16),
                                      nullptr, nullptr, &jsStrUTF16, &copied);
    OH\_JSVM\_GetValueStringUtf8(env, jsStrUTF16, buf, 10, nullptr);
    OH\_LOG\_INFO(LOG\_APP, "created utf16 string is : %{public}s\\n", buf);
    // If the value of copied is true, the external string fails to be created. Otherwise, the external string is created successfully.
    OH\_LOG\_INFO(LOG\_APP, "create external string failed : %{public}d\\n", copied);
    OH\_JSVM\_CloseHandleScope(env, handleScope);

    return nullptr;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = testExternalString},
};

static JSVM\_CallbackStruct \*method = param;

// Alias for the wrapperObject method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"testExternalString", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(testExternalString();)JS";

#### Expected Result

created latin1 string is : hello
create external string failed: 0
created utf16 string is : world
create external string failed: 0
