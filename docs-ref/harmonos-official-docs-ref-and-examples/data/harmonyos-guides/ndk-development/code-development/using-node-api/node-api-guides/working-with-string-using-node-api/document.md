# Working with String Using Node-API

#### Introduction

This topic walks you through on how to use Node-API to convert data between native strings and ArkTS strings.

#### Basic Concepts

Strings are a common data type in programming. They are used to store and manipulate text data, represent and process character sequences, build user interface (UI) elements such as tags, buttons, and text boxes, process user input, and validate and format data. Different encodings support different character sets and languages. Major encoding schemes include the following:

-   ASCII
    
    ASCII is one of the earliest character encoding schemes. It uses 7 bits to represent English letters, digits, and some basic symbols. It serves as the foundation for encoding schemes.
    
-   UTF-8
    
    UTF-8 is a variable-length encoding scheme that can represent any Unicode character. It uses 8 bits per character and uses byte sequences of different lengths depending on the range of the character. UTF-8 is widely used for web content.
    
-   UTF-16
    
    UTF-16 is a fixed-length or variable-length encoding scheme that uses 16 bits per character. It can represent all Unicode characters and is suitable for larger character sets.
    
-   ISO-8859-1 (Latin-1)
    
    ISO-8859-1 is a single-byte coding scheme that uses 8 bits per character. It is mainly used to represent Latin alphabet characters and commonly used in European languages.
    

#### Available APIs

The following table lists the APIs provided by the Node-API module for creating and obtaining strings.

| API | Description | Earliest Version |
| :-- | :-- | :-- |
| napi\_get\_value\_string\_utf8 | Obtains a UTF8-encoded string from an ArkTS value. | 10 |
| napi\_create\_string\_utf8 | Creates an ArkTS string from a UTF8-encoded C string. | 10 |
| napi\_get\_value\_string\_utf16 | Obtains a UTF16-encoded string from an ArkTS value. | 10 |
| napi\_create\_string\_utf16 | Creates an ArkTS string from a UTF16-encoded C string. | 10 |
| napi\_get\_value\_string\_latin1 | Obtains an ISO-8859-1-encoded string from an ArkTS value. | 10 |
| napi\_create\_string\_latin1 | Creates an ArkTS string from an ISO-8859-1-encoded string. | 10 |
| napi\_create\_external\_string\_utf16 | Creates an ArkTS string from an external UTF-16 encoded string buffer, without performing memory copy operations. | 22 |
| napi\_create\_external\_string\_ascii | Creates an ArkTS string from an external ASCII encoded string buffer, without performing memory copy operations. | 22 |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the string-related APIs.

## napi\_get\_value\_string\_utf8

Use **napi\_get\_value\_string\_utf8** to convert an ArkTS string to a UTF-8-encoded string.

CPP code:

#include "napi/native\_api.h"
#include "hilog/log.h"
#include <cstring>

static napi\_value GetValueStringUtf8(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the length of the string.
    size\_t length = 0;
    napi\_status status = napi\_get\_value\_string\_utf8(env, args\[0\], nullptr, 0, &length);
    // napi\_string\_expected will be returned for non-string inputs.
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_value\_string\_utf8 failed");
        return nullptr;
    }
    char\* buf = new char\[length + 1\];
    std::memset(buf, 0, length + 1);
    status = napi\_get\_value\_string\_utf8(env, args\[0\], buf, length + 1, &length);
    if (status != napi\_ok) {
        if (buf) {
            delete\[\] buf;
        }
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_value\_string\_utf8 failed");
        return nullptr;
    }
    napi\_value result = nullptr;
    status = napi\_create\_string\_utf8(env, buf, length, &result);
    if (buf) {
        delete\[\] buf;
    }
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_string\_utf8 failed");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const getValueStringUtf8: (param: string | number) => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

// Pass in a string and a number respectively. If the input is a string, the string will be returned. If the input is not a string, 'undefined' will be returned.
hilog.info(0x0000, 'testTag', 'Test Node-API get\_value\_string\_utf8\_string %{public}s', testNapi.getValueStringUtf8('aaBC+-$%^Hello 123'));
hilog.info(0x0000, 'testTag', 'Test Node-API get\_value\_string\_utf8\_not\_string %{public}s', testNapi.getValueStringUtf8(50));

## napi\_create\_string\_utf8

Use **napi\_create\_string\_utf8** to create an ArkTS string from a UTF8-encoded C string.

CPP code:

#include "napi/native\_api.h"
#include <string>

static napi\_value CreateStringUtf8(napi\_env env, napi\_callback\_info info)
{
    const char \*str = u8"Hello, World!, successes to create UTF-8 string! 111";
    size\_t length = strlen(str);
    napi\_value result = nullptr;
    napi\_status status = napi\_create\_string\_utf8(env, str, length, &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to create UTF-8 string");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const createStringUtf8: () => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_string\_utf8:%{public}s', testNapi.createStringUtf8());

## napi\_get\_value\_string\_utf16

Use **napi\_get\_value\_string\_utf16** to convert an ArkTS string to a UTF-16-encoded string.

CPP code:

#include "napi/native\_api.h"

// Set the maximum length of the string buffer.
static const int MAX\_BUFFER\_SIZE = 128;

static napi\_value GetValueStringUtf16(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\];
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_value result = nullptr;
    // Buffer of the string.
    char16\_t buffer\[MAX\_BUFFER\_SIZE\];
    // Size of the buffer for storing the string.
    size\_t bufferSize = MAX\_BUFFER\_SIZE;
    // Length of the string.
    size\_t stringLen;
    // Obtain the value and length of the string.
    napi\_get\_value\_string\_utf16(env, args\[0\], buffer, bufferSize, &stringLen);
    // Obtain the string.
    napi\_create\_string\_utf16(env, buffer, stringLen, &result);
    // Return the result.
    return result;
}

API declaration:

// index.d.ts
export const getValueStringUtf16: (data: string) => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let result = testNapi.getValueStringUtf16('hello,');
hilog.info(0x0000,'testTag','Node-API napi\_get\_value\_string\_utf16:%{public}s', result);

## napi\_create\_string\_utf16

Use **napi\_create\_string\_utf16** to create an ArkTS string from a UTF16-encoded C string.

CPP code:

#include "napi/native\_api.h"

static napi\_value CreateStringUtf16(napi\_env env, napi\_callback\_info info)
{
    const char16\_t  \*str = u"Hello, World!, successes to create UTF-16 string! 111";
    size\_t length = NAPI\_AUTO\_LENGTH;
    napi\_value result = nullptr;
    napi\_status status = napi\_create\_string\_utf16(env, str, length, &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to create UTF-16 string");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const createStringUtf16: () => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_string\_utf16:%{public}s ', testNapi.createStringUtf16());

## napi\_get\_value\_string\_latin1

Use **napi\_get\_value\_string\_latin1** to convert an ArkTS string into an ISO-8859-1-encoded string.

CPP code:

#include "napi/native\_api.h"

static const int MAX\_BUFFER\_SIZE = 128;

static napi\_value GetValueStringLatin1(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
    char buf\[MAX\_BUFFER\_SIZE\];
    size\_t length = 0;
    napi\_value napi\_Res = nullptr;
    napi\_status status = napi\_get\_value\_string\_latin1(env, args\[0\], buf, MAX\_BUFFER\_SIZE, &length);
    // If the value passed in is not a string, napi\_string\_expected will be returned.
    if (status != napi\_ok) {
        return nullptr;
    }
    napi\_create\_string\_latin1(env, buf, length, &napi\_Res);
    return napi\_Res;
}

API declaration:

// index.d.ts
export const getValueStringLatin1: (param: number | string) => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

// If non-character data is passed in, undefined will be returned.
hilog.info(0x0000, 'testTag', 'Test Node-API get\_value\_string\_latin1\_not\_string %{public}s', testNapi.getValueStringLatin1(10));
// The ISO-8859-1 encoding does not support Chinese characters. If Chinese characters are passed in, garbled characters will be displayed.
hilog.info(0x0000, 'testTag', 'Test Node-API get\_value\_string\_latin1\_string\_chinese %{public}s', testNapi.getValueStringLatin1('Chinese characters'));
// Passing in characters of other languages will not cause garbled characters.
hilog.info(0x0000, 'testTag', 'Test Node-API get\_value\_string\_latin1\_string %{public}s', testNapi.getValueStringLatin1('abo ABP=-&\*/'));

## napi\_create\_string\_latin1

Use **napi\_create\_string\_latin1** to create an ArkTS string from an ISO-8859-1-encoded C string.

CPP code:

#include "napi/native\_api.h"

static napi\_value CreateStringLatin1(napi\_env env, napi\_callback\_info info)
{
    const char \*str = "Hello, World! éçñ, successes to create Latin1 string! 111";
    size\_t length = NAPI\_AUTO\_LENGTH;
    napi\_value result = nullptr;
    napi\_status status = napi\_create\_string\_latin1(env, str, length, &result);
    if (status != napi\_ok) {
        // Error handling.
        napi\_throw\_error(env, nullptr, "Failed to create Latin1 string");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const createStringLatin1: () => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'testTag', 'Test Node-API  napi\_create\_string\_latin1:%{public}s', testNapi.createStringLatin1());

## napi\_create\_external\_string\_utf16

Use **napi\_create\_external\_string\_utf16** to create an ArkTS UTF-16 string that references external resources.

CPP code:

// Define the destruction callback function of the string to release external resources.
// The hint parameter can be used to pass some additional information, such as the reference count. You can also ignore this parameter and pass nullptr.
static void StringFinalizerUTF16(void\* data, void\* hint)
{
    // Release external resources.
    delete\[\] static\_cast<char16\_t\*>(data);
}

static napi\_value CreateExternalStringUtf16(napi\_env env, napi\_callback\_info info)
{
    const char16\_t source\[\] = u"Hello, World!, successes to create UTF-16 string! 111";
    napi\_value result = nullptr;
    int char16tLength = sizeof(source) / sizeof(char16\_t);
    // Allocate memory dynamically on the heap and copy the string content.
    char16\_t\* str = new char16\_t\[char16tLength\];
    std::copy(source, source + char16tLength, str);
    // When the created string is reclaimed by GC at the end of its lifecycle in ArkTS, the StringFinalizerUTF16(str, finalize\_hint) function is called.
    // If finalize\_callback is set to nullptr, no callback function is called. You need to manage the lifecycle of the external resource str.
    napi\_status status = napi\_create\_external\_string\_utf16(
        env,
        str,                    // External string buffer.
        NAPI\_AUTO\_LENGTH,       // String length. If NAPI\_AUTO\_LENGTH is passed in, the string ends with '\\0'.
        StringFinalizerUTF16,   // Destruction callback function of the string.
        nullptr,                // The hint parameter passed to the destruction callback function. This parameter is not required in this example.
        &result                 // Accept the created ArkTS string value.
    );
    if (status != napi\_ok) {
        // Error handling.
        delete\[\] str;
        napi\_throw\_error(env, nullptr, "Failed to create utf16 string");
        return nullptr;
    }
    return result;
}

API declaration:

export const CreateExternalStringUtf16: () => string | void;

ArkTS code:

hilog.info(0x0000, 'testTag', 'Test Node-API  napi\_create\_string\_latin1:%{public}s',
  testNapi.CreateExternalStringUtf16());

The ArkTS string object created by **napi\_create\_external\_string\_utf16** is managed by GC. When the lifecycle of the ArkTS string object ends, GC reclaims the object and triggers the **StringFinalizerUTF16** function to reclaim the native resources referenced by it.

## napi\_create\_external\_string\_ascii

Use **napi\_create\_external\_string\_ascii** to create an ASCII-encoded ArkTS string that references an external resource.

CPP code:

// Define the destruction callback function of the string to release external resources.
// The hint parameter can be used to pass some additional information, such as the reference count. You can also ignore this parameter and pass nullptr.
static void StringFinalizerASCII(void\* data, void\* hint)
{
    // Release external resources.
    delete\[\] static\_cast<char\*>(data);
}

static napi\_value CreateExternalStringAscii(napi\_env env, napi\_callback\_info info)
{
    const char source\[\] = "hello, World!, successes to create ASCII string! 111";
    napi\_value result = nullptr;
    int charLength = sizeof(source) / sizeof(char);
    // Allocate memory dynamically on the heap and copy the string content.
    char\* str = new char\[charLength\];
    std::copy(source, source + charLength, str);
    // When the created string is reclaimed by GC at the end of its lifecycle in ArkTS, the StringFinalizerASCII(str, finalize\_hint) function is called.
    // If finalize\_callback is set to nullptr, no callback function is called. You need to manage the lifecycle of the external resource str.
    // napi\_create\_external\_string\_ascii requires that the input string must not contain the null character '\\0' within the specified length range. Otherwise, unexpected behavior may occur.
    napi\_status status = napi\_create\_external\_string\_ascii(
        env,
        str,                    // External string buffer.
        NAPI\_AUTO\_LENGTH,       // String length. If NAPI\_AUTO\_LENGTH is passed in, the string ends with '\\0'.
        StringFinalizerASCII,   // Destruction callback function of the string.
        nullptr,                // The hint parameter passed to the destruction callback function. This parameter is not required in this example.
        &result                 // Accept the created ArkTS string value.
    );
    if (status != napi\_ok) {
        // Error handling.
        delete\[\] str;
        napi\_throw\_error(env, nullptr, "Failed to create ascii string");
        return nullptr;
    }
    return result;
}

API declaration:

export const CreateExternalStringAscii: () => string | void;

ArkTS code:

hilog.info(0x0000, 'testTag', 'Test Node-API  napi\_create\_string\_latin1:%{public}s',
  testNapi.CreateExternalStringAscii());

The ArkTS string object created by **napi\_create\_external\_string\_ascii** is managed by GC. When the lifecycle of the ArkTS string object ends, GC reclaims the object and triggers the **StringFinalizerASCII** function to reclaim the native resources referenced by it.

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
