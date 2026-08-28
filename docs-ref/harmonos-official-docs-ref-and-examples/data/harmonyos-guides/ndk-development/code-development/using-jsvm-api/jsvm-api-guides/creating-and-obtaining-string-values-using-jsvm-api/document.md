# Creating and Obtaining String Values Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to convert data between native strings and JavaScript (JS) strings.

#### Basic Concepts

Strings are a common data type in programming. They are used to store and manipulate text data, build user interface (UI) elements such as tags, buttons, and text boxes, process user input, and validate and format data. Different encodings support different character sets and languages. Major encoding schemes include the following:

-   ASCII
    
    ASCII is one of the earliest character encoding schemes. It uses 7 bits to represent English letters, digits, and some basic symbols. It serves as the foundation for encoding schemes.
    
-   UTF-8
    
    UTF-8 is a variable-length encoding scheme that can represent any Unicode character. It uses 8 bits per character and uses byte sequences of different lengths depending on the range of the character. UTF-8 is widely used for web content.
    
-   UTF-16
    
    UTF-16 is a fixed-length or variable-length encoding scheme that uses 16 bits per character. It can represent all Unicode characters and is suitable for larger character sets.
    
-   ISO-8859-1 (Latin-1)
    
    ISO-8859-1 is a single-byte coding scheme that uses 8 bits per character. It is mainly used to represent Latin alphabet characters and commonly used in European languages.
    

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetValueStringUtf8 | Obtains the UTF8-encoded string from a JS string. |
| OH\_JSVM\_CreateStringUtf8 | Creates a JS string object from a UTF8-encoded C string. |
| OH\_JSVM\_GetValueStringUtf16 | Obtains the UTF16-encoded string from a JS string. |
| OH\_JSVM\_CreateStringUtf16 | Creates a JS string object based on a UTF16-encoded string. |
| OH\_JSVM\_GetValueStringLatin1 | Obtains the ISO-8859-1-encoded string from a JS string. |
| OH\_JSVM\_CreateStringLatin1 | Creates a JS string object from an ISO-8859-1-encoded C string. ISO-8859-1 is also referred to as Latin-1. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

## OH\_JSVM\_GetValueStringUtf8

Call **OH\_JSVM\_GetValueStringUtf8** to convert a JS string into a UTF-8-encoded string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <cstdlib>
// Define OH\_JSVM\_GetValueStringUtf8.
static JSVM\_Value GetValueStringUtf8(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    size\_t length = 0;
    JSVM\_Status status = OH\_JSVM\_GetValueStringUtf8(env, args\[0\], nullptr, 0, &length);
    char \*buf = (char \*)malloc(length + 1);
    if (buf == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "malloc failed");
        return nullptr;
    }
    memset(buf, 0, length + 1);
    status = OH\_JSVM\_GetValueStringUtf8(env, args\[0\], buf, length + 1, &length);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueStringUtf8 fail");
        free(buf);
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueStringUtf8 success: %{public}s", buf);
    }
    JSVM\_Value result = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, buf, length, &result);
    free(buf);
    return result;
}
// Register the GetValueStringUtf8 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueStringUtf8},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetValueStringUtf8 method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueStringUtf8", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let data = "aaBC+-$%^Hello 123";
    let script = getValueStringUtf8(data);
)JS";

Expected result:

JSVM GetValueStringUtf8 success: aaBC+-$%^Hello 123

**NOTE**

The call fails if the input parameter **arg** of **getValueStringUtf8()** is not of the string type.

## OH\_JSVM\_CreateStringUtf8

Call **OH\_JSVM\_CreateStringUtf8** to create a JS string from a UTF8-encoded C string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <string>
// Define OH\_JSVM\_CreateStringUtf8.
static JSVM\_Value CreateStringUtf8(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    const char \*str = u8"Hello, World!, succeed in creating UTF-8 string!";
    size\_t length = strlen(str);
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateStringUtf8(env, str, length, &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "Failed to create UTF-8 string");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateStringUtf8 success: %{public}s", str);
    }
    return result;
}
// Register the CreateStringUtf8 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateStringUtf8},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CreateStringUtf8 method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createStringUtf8", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let script = createStringUtf8();
)JS";

Expected result:

JSVM CreateStringUtf8 success: Hello, World!, succeed in creating UTF-8 string!

## OH\_JSVM\_GetValueStringUtf16

Call **OH\_JSVM\_GetValueStringUtf16** to convert a JS string into a UTF-16-encoded string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <codecvt>
#include <locale>
#include <cstdlib>

// Define OH\_JSVM\_GetValueStringUtf16.
// Set the maximum length of the string buffer.
static const int MAX\_BUFFER\_SIZE = 128;
static JSVM\_Value GetValueStringUtf16(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value result = nullptr;
    size\_t length = 0;
    char16\_t buffer\[MAX\_BUFFER\_SIZE\] = {0};
    // Size of the buffer for storing the string.
    size\_t bufferSize = MAX\_BUFFER\_SIZE;
    JSVM\_Status status = OH\_JSVM\_GetValueStringUtf16(env, args\[0\], buffer, bufferSize, &length);
    // Convert char16\_t to std::u16string.
    std::u16string u16str = {buffer};
    // Convert std::u16string to std::string.
    std::wstring\_convert<std::codecvt\_utf8\_utf16<char16\_t>, char16\_t> converter;
    std::string str = converter.to\_bytes(u16str);
    // Obtain the string.
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueStringUtf16 fail");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueStringUtf16 success: %{public}s", str.c\_str());
    }
    return result;
}
// Register the GetValueStringUtf16 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueStringUtf16},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetValueStringUtf16 method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueStringUtf16", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let data = "ahello.";
    let script = getValueStringUtf16(data);
)JS";

Expected result:

JSVM GetValueStringUtf16 success: ahello.

**Note**: The **arg** parameter of **getValueStringUtf16(arg)** must be a string. Otherwise, the API call fails.

## OH\_JSVM\_CreateStringUtf16

Call **OH\_JSVM\_GetValueStringUtf16** to create a JS string from a UTF16-encoded C string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <codecvt>
#include <locale>
#include <cstring>

// Define OH\_JSVM\_CreateStringUtf16.
static JSVM\_Value CreateStringUtf16(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    const char16\_t \*str = u"Hello, World!, succeed in creating UTF-16 string!";
    std::u16string ustr(str);
    size\_t length = ustr.length();
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateStringUtf16(env, str, length, &result);
    std::u16string u16str = {str};
    // Convert std::u16string to std::string.
    std::wstring\_convert<std::codecvt\_utf8\_utf16<char16\_t>, char16\_t> converter;
    std::string strResult = converter.to\_bytes(u16str);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateStringUtf16 fail");
    }else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateStringUtf16 success: %{public}s", strResult.c\_str());
    }
    return result;
}
// Register the CreateStringUtf16 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateStringUtf16},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CreateStringUtf16 method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createStringUtf16", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let script = createStringUtf16();
)JS";

Expected result:

JSVM CreateStringUtf16 success: Hello, World!, succeed in creating UTF-16 string!

## OH\_JSVM\_GetValueStringLatin1

Call **OH\_JSVM\_GetValueStringLatin1** to convert a JS string into an ISO-8859-1-encoded string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <cstdlib>
// Define OH\_JSVM\_GetValueStringLatin1.
// Set the maximum length of the string buffer.
static const int MAX\_BUFFER\_SIZE = 128;
static JSVM\_Value GetValueStringLatin1(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    char buf\[MAX\_BUFFER\_SIZE\];
    size\_t length = 0;
    JSVM\_Value jsvmRes = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetValueStringLatin1(env, args\[0\], buf, MAX\_BUFFER\_SIZE, &length);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueStringLatin1 fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueStringLatin1 success: %{public}s", buf);
    }
    OH\_JSVM\_CreateStringLatin1(env, buf, length, &jsvmRes);
    return jsvmRes;
}
// Register the GetValueStringLatin1 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueStringLatin1},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetValueStringLatin1 method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueStringLatin1", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let data = "Chinese";
    let script = getValueStringLatin1(data);
)JS";

Expected output (The ISO-8859-1 encoding does not support Chinese characters. If Chinese characters are passed in, garbled characters will be displayed.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/cZ2VC-YCTwW0TY4S2wrw4Q/en-us_image_0000002568685013.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062133Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=205A7001440E3BE57956FC25A965EF1E93CAA8254729EC973B218CCDC10265C8)

**Note**: The input parameter **arg** of **getValueStringLatin1(arg)** must be a string. Otherwise, the API fails to be called.

## OH\_JSVM\_CreateStringLatin1

Call **OH\_JSVM\_CreateStringLatin1** to create a JS string from an ISO-8859-1-encoded C string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <cstring>
// Register the CreateStringLatin1 callback.
// Set the maximum length of the string buffer.
static const int MAX\_BUFFER\_SIZE = 128;
// Define OH\_JSVM\_CreateStringLatin1.
static JSVM\_Value CreateStringLatin1(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    const char \*str = "Hello, World! éçñ, succeed in creating Latin1 string!";
    size\_t length = JSVM\_AUTO\_LENGTH;
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateStringLatin1(env, str, length, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateStringLatin1 fail");
    } else {
        char buf\[MAX\_BUFFER\_SIZE\];
        size\_t length = 0;
        OH\_JSVM\_GetValueStringLatin1(env, result, buf, MAX\_BUFFER\_SIZE, &length);
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateStringLatin1 success: %{public}s", buf);
    }
    return result;
}
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateStringLatin1},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CreateStringLatin1 method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createStringLatin1", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let script = createStringLatin1();
)JS";

Expected result:

JSVM CreateStringLatin1 success: Hello, World! éçñ, succeed in creating Latin1 string!
