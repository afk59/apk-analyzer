# Working with BigInt Using JSVM-API

#### Introduction

BigInt is a data type used to represent integers of any precision in JavaScript (JS), with values greater than the value range of the Number type. You can use JSVM-API to create, obtain, and operate JS BigInt values.

#### Basic Concepts

Before using JSVM-API to operate BigInt values, you need to understand the following basic concepts:

-   BigInt: a data type used to represent integers of any precision in JS. Unlike the Number type, BigInt can accurately represent very large integers without losing precision or causing overflows.
-   BigInt creation: You can use JSVM-API to create a JS BigInt object from a C **Int64** or **Uint64** value. This makes it easy to create BigInt values using C/C++.
-   BigInt operation: JSVM-API provides APIs for operating BigInt values. You can use these APIs to obtain and convert BigInt values and perform arithmetic and bitwise operations.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateBigintInt64 | Creates a JS BigInt object from a C int64\_t object. |
| OH\_JSVM\_CreateBigintUint64 | Creates a JS BigInt object from a C uint64\_t object. |
| OH\_JSVM\_CreateBigintWords | Creates a JS BigInt object from a C uint64\_t array. |
| OH\_JSVM\_GetValueBigintInt64 | Obtains the C int64\_t primitive equivalent of the given JS BigInt. If necessary, it truncates the value and sets **lossless** to **false**. |
| OH\_JSVM\_GetValueBigintUint64 | Obtains the C uint64\_t primitive equivalent of the given JS BigInt. If necessary, it truncates the value and sets **lossless** to **false**. |
| OH\_JSVM\_GetValueBigintWords | Obtains the underlying data (word representation) of a given JS BigInt object. The word representation includes a sign bit, a 64-bit little-endian array, and the length of the array. If **signBit** and **words** are set to **NULL**, only **wordCount** is obtained. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code and ArkTS code involved in related APIs.

## OH\_JSVM\_GetValueBigintWords

Use **OH\_JSVM\_GetValueBigintWords** to obtain the underlying data of a given JS BigInt object, that is, the word representation of BigInt data.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <fstream>

// Define OH\_JSVM\_GetValueBigintWords.
static JSVM\_Value GetValueBigintWords(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    int signBit = 0;
    size\_t wordCount = 0;
    uint64\_t\* words{nullptr};
    // Call OH\_JSVM\_GetValueBigintWords to obtain wordCount.
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, args\[0\], nullptr, &wordCount, nullptr);
    OH\_LOG\_INFO(LOG\_APP, "OH\_JSVM\_GetValueBigintWords wordCount:%{public}d.", wordCount);
    words = (uint64\_t\*)malloc(wordCount\*sizeof(uint64\_t));
    if (words == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_JSVM\_GetValueBigintWords malloc failed.");
        return nullptr;
    }
    // Call OH\_JSVM\_GetValueBigintWords to obtain BigInt information, such as whether the value passed by signBit is a positive or negative number.
    status = OH\_JSVM\_GetValueBigintWords(env, args\[0\], &signBit, &wordCount, words);
    free(words);
    words = nullptr;
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_JSVM\_GetValueBigintWords fail, status:%{public}d.", status);
    } else {
        OH\_LOG\_INFO(LOG\_APP, "OH\_JSVM\_GetValueBigintWords signBit: %{public}d.", signBit);
    }
    // Convert the sign bit into a value of Int type and pass it.
    JSVM\_Value returnValue = nullptr;
    OH\_JSVM\_CreateInt32(env, signBit, &returnValue);
    return returnValue;
}
// Register the GetValueBigintWords callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueBigintWords},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getValueBigintWords and associate it with a callback. This allows the GetValueBigintWords callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueBigintWords", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getValueBigintWords(BigInt(5555555555555555)))JS";

Expected result:

OH\_JSVM\_GetValueBigintWords wordCount:1.
OH\_JSVM\_GetValueBigintWords signBit: 0.

## OH\_JSVM\_CreateBigintWords

Use **OH\_JSVM\_GetValueBigintWords** to create a JS BigInt object from a C uint64\_t array.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CreateBigintWords.
static int DIFF\_VALUE\_THREE = 3;
static JSVM\_Value CreateBigintWords(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Call OH\_JSVM\_CreateBigintWords to create a BigInt object.
    int signBit = 0;
    size\_t wordCount = DIFF\_VALUE\_THREE;
    uint64\_t words\[\] = {12ULL, 34ULL, 56ULL};
    JSVM\_Value returnValue = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateBigintWords(env, signBit, wordCount, words, &returnValue);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CreateBigintWords fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CreateBigintWords success");
    }
    return returnValue;
}
// Register the CreateBigintWords callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateBigintWords},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createBigintWords and associate it with a callback. This allows the CreateBigintWords callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createBigintWords", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createBigintWords())JS";

Expected result:

JSVM OH\_JSVM\_CreateBigintWords success

## OH\_JSVM\_CreateBigintUint64

Use **OH\_JSVM\_CreateBigintUint64** to create a JavaScript BigInt object from a Uint64 object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Declare the variable value of uint64\_t.
static uint64\_t TEST\_VALUE = 5555555555555555555;
// Define OH\_JSVM\_CreateBigintUint64.
static JSVM\_Value CreateBigintUint64(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Convert value to the JSVM\_Value type and return the value.
    JSVM\_Value returnValue = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateBigintUint64(env, TEST\_VALUE, &returnValue);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CreateBigintUint64 fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CreateBigintUint64 success");
    }
    return returnValue;
}
// Define CreateBigintUint64.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateBigintUint64},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createBigintUint64 and associate it with a callback. This allows the CreateBigintUint64 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createBigintUint64", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createBigintUint64())JS";

Expected result:

JSVM OH\_JSVM\_CreateBigintUint64 success

## OH\_JSVM\_GetValueBigintUint64

Use **OH\_JSVM\_GetValueBigintUint64** to obtain the C uint64\_t primitive equivalent of the given JS BigInt object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetValueBigintUint64.
static JSVM\_Value GetValueBigintUint64(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the BigInt value.
    uint64\_t value = 0;
    bool lossLess = false;
    OH\_JSVM\_GetValueBigintUint64(env, args\[0\], &value, &lossLess);
    // Check whether the BigInt value obtained is a product of lossless conversion. If no, an exception is thrown.
    if (!lossLess) {
        OH\_JSVM\_ThrowError(env, nullptr, "BigInt values have no lossless converted");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueBigintUint64 success");
    }
    JSVM\_Value returnValue = nullptr;
    OH\_JSVM\_CreateBigintUint64(env, value, &returnValue);
    return returnValue;
}
// Register the GetValueBigintUint64 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueBigintUint64},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getValueBigintUint64 and associate it with a callback. This allows the GetValueBigintUint64 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueBigintUint64", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getValueBigintUint64(BigInt(5555555555555555)))JS";

Expected result:

JSVM GetValueBigintUint64 success

## OH\_JSVM\_CreateBigintInt64

Use **OH\_JSVM\_CreateBigintInt64** to create a JavaScript BigInt object from an int64\_t object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Declare the variable value of int64\_t.
static int64\_t TEST\_VALUE\_DEMO = -5555555555555555555;
// Define OH\_JSVM\_CreateBigintInt64.
static JSVM\_Value CreateBigintInt64(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Value returnValue = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateBigintInt64(env, TEST\_VALUE\_DEMO, &returnValue);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CreateBigintInt64 fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CreateBigintInt64 success");
    }
    return returnValue;
}
// Register the CreateBigintInt64 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateBigintInt64},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createBigintInt64 and associate it with a callback. This allows the CreateBigintInt64 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createBigintInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createBigintInt64())JS";

Expected result:

JSVM OH\_JSVM\_CreateBigintInt64 success

## OH\_JSVM\_GetValueBigintInt64

Use OH\_JSVM\_GetValueBigintInt64 to obtain the C int64\_t primitive equivalent of the given JS BigInt object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetValueBigintInt64.
static JSVM\_Value GetBigintInt64(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the 64-bit big integer from the input parameter.
    int64\_t value = 0;
    bool lossLess = false;
    OH\_JSVM\_GetValueBigintInt64(env, args\[0\], &value, &lossLess);
    // Check whether the BigInt value obtained is a product of lossless conversion. If no, an exception is thrown.
    if (!lossLess) {
        OH\_JSVM\_ThrowError(env, nullptr, "BigInt values have no lossless converted");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetBigintInt64 success");
    }
    JSVM\_Value returnValue = nullptr;
    OH\_JSVM\_CreateBigintInt64(env, value, &returnValue);
    return returnValue;
}
// Register the GetBigintInt64 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetBigintInt64},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getBigintInt64 and associate it with a callback. This allows the GetBigintInt64 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getBigintInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getBigintInt64(BigInt(-5555555555555555)))JS";

Expected result:

JSVM GetValueBigintUint64 success
