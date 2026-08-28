# Working with Primitives Using JSVM-API

#### Introduction

JSVM-API provides APIs for converting data between C/C++ and JavaScript (JS) data types and obtaining the JS object of the specified type.

#### Basic Concepts

Before using JSVM to operate JS objects, you need to understand the following basic concepts:

-   Conversion between JS and C/C primitives: You can use JSVM-API to convert JS values to C/C++ data types, for example, convert a JS value into a C/C++ integer and convert a JS string into a C/C++ string array. You can also convert C/C++ data into a JS value and return the JS value to JS.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CoerceToBool | Converts a JS value to an object of the Boolean type. |
| OH\_JSVM\_CoerceToNumber | Converts a JS value to an object of the number type. |
| OH\_JSVM\_CoerceToObject | Converts a JS value to an object of the object type. |
| OH\_JSVM\_CoerceToString | Converts a JS value to an object of the string type. |
| OH\_JSVM\_GetBoolean | Obtains a JS singleton object that is used to represent the given Boolean value. |
| OH\_JSVM\_GetValueBool | Obtains the C Boolean primitive equivalent of the given JS Boolean. |
| OH\_JSVM\_GetGlobal | Obtains the **global** object of the current environment. |
| OH\_JSVM\_GetNull | Obtains the JS **null** object. |
| OH\_JSVM\_GetUndefined | Obtains the JS **undefined** object. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

## OH\_JSVM\_CoerceToBool

Call **OH\_JSVM\_CoerceToBool** to forcibly convert a JS value to a JS Boolean value.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CoerceToBool.
static JSVM\_Value CoerceToBool(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value boolean = nullptr;
    JSVM\_Status status = OH\_JSVM\_CoerceToBool(env, args\[0\], &boolean);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CoerceToBool failed");
    } else {
        bool result = false;
        OH\_JSVM\_GetValueBool(env, boolean, &result);
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CoerceToBool success:%{public}d", result);
    }
    return boolean;
}
// Register the CoerceToBool callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CoerceToBool},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CoerceToBool method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"coerceToBool", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(coerceToBool("123"))JS";

Expected result:

JSVM OH\_JSVM\_CoerceToBool success:1

## OH\_JSVM\_CoerceToNumber

Call **OH\_JSVM\_CoerceToNumber** to forcibly convert a JS value to a JS number.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CoerceToNumber.
static JSVM\_Value CoerceToNumber(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value number = nullptr;
    JSVM\_Status status = OH\_JSVM\_CoerceToNumber(env, args\[0\], &number);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CoerceToNumber failed");
    } else {
        int32\_t result = 0;
        OH\_JSVM\_GetValueInt32(env, number, &result);
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CoerceToNumber success:%{public}d", result);
    }
    return number;
}
// Register the CoerceToNumber callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CoerceToNumber},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CoerceToNumber method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"coerceToNumber", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(coerceToNumber(true))JS";

Expected result:

JSVM OH\_JSVM\_CoerceToNumber success:1

## OH\_JSVM\_CoerceToObject

Call **OH\_JSVM\_CoerceToObject** to forcibly convert a JS value to a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CoerceToObject.
static JSVM\_Value CoerceToObject(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value obj = nullptr;
    JSVM\_Status status = OH\_JSVM\_CoerceToObject(env, args\[0\], &obj);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_CoerceToObject failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CoerceToObject success");
    }
    return obj;
}
// Register the CoerceToObject callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CoerceToObject},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CoerceToObject method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"coerceToObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(coerceToObject(123))JS";

Expected result:

JSVM OH\_JSVM\_CoerceToObject success

## OH\_JSVM\_CoerceToString

Call **OH\_JSVM\_CoerceToString** to forcibly convert a JS value to a JS string.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CoerceToString.
static JSVM\_Value CoerceToString(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value str = nullptr;
    JSVM\_Status status = OH\_JSVM\_CoerceToString(env, args\[0\], &str);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_CoerceToString fail");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CoerceToString success");
    }
    return str;
}
// Register the CoerceToString callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CoerceToString},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CoerceToString method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"coerceToString", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(coerceToString(22222))JS";

Expected result:

JSVM OH\_JSVM\_CoerceToString success

## OH\_JSVM\_GetBoolean

Call **OH\_JSVM\_GetBoolean** to obtain a JS singleton object that is used to represent the given Boolean value.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetBoolean.
static JSVM\_Value GetBoolean(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Pass in two parameters and parse them.
    size\_t argc = 2;
    JSVM\_Value argv\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    int32\_t paramData = 0;
    OH\_JSVM\_GetValueInt32(env, argv\[0\], &paramData);
    int32\_t paramValue = 0;
    OH\_JSVM\_GetValueInt32(env, argv\[1\], &paramValue);
    JSVM\_Value returnValue = nullptr;
    bool type = false;
    if (paramData == paramValue) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM resultType equal");
        type = true;
    }
    JSVM\_Status status = OH\_JSVM\_GetBoolean(env, type, &returnValue);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_GetBoolean fail");
    } else {
        bool result = false;
        OH\_JSVM\_GetValueBool(env, returnValue, &result);
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetBoolean success:%{public}d", result);
    }
    // Return the result.
    return returnValue;
}
// Register the GetBoolean callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetBoolean},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetBoolean method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getBoolean", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(getBoolean(1, 2);
                                 getBoolean(1, 1))JS";

Expected result:

JSVM OH\_JSVM\_GetBoolean success:0
JSVM resultType equal
JSVM OH\_JSVM\_GetBoolean success:1

## OH\_JSVM\_GetValueBool

Call **OH\_JSVM\_GetValueBool** to obtain the C Boolean primitive equivalent of the given JS Boolean.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetValueBool.
static JSVM\_Value GetValueBool(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_GetValueBool(env, args\[0\], &result);
    if (status != JSVM\_OK) {
        // If OH\_JSVM\_GetValueBool is successful, JSVM\_OK is returned. If a non-Boolean value is passed in, JSVM\_BOOLEAN\_EXPECTED is returned.
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_GetValueBool fail:%{public}d", status);
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetValueBool success:%{public}d", result);
    }
    JSVM\_Value boolJv = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &boolJv);
    return boolJv;
}
// Register the GetValueBool callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueBool},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetValueBool method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueBool", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(getValueBool("abc");
                                getValueBool(true);
                                getValueBool(false);)JS";

Expected result:

JSVM OH\_JSVM\_GetValueBool fail:7
JSVM OH\_JSVM\_GetValueBool success:1
JSVM OH\_JSVM\_GetValueBool success:0

## OH\_JSVM\_GetGlobal

Call **OH\_JSVM\_GetGlobal** to obtain a JS **global** object. You can use this API to obtain the **JSVM\_Value** that represents a JS global object, so that the JSVM module can interact with the global variables and functions defined in the JS context.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetGlobal.
static JSVM\_Value GetGlobal(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the global object.
    JSVM\_Value value = nullptr;
    JSVM\_Value global = nullptr;
    OH\_JSVM\_CreateInt32(env, 1, &value);
    JSVM\_Status status = OH\_JSVM\_GetGlobal(env, &global);
    OH\_JSVM\_SetNamedProperty(env, global, "Row", value);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_GetGlobal fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetGlobal success");
    }
    return global;
}
// Register the GetGlobal callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetGlobal},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetGlobal method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getGlobal", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(getGlobal())JS";

Expected result:

JSVM OH\_JSVM\_GetGlobal success

## OH\_JSVM\_GetNull

Call **OH\_JSVM\_GetNull** to obtain a JavaScript null object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetNull.
static JSVM\_Value GetNull(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_Value nullValue = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetNull(env, &nullValue);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_GetNull fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetNull success");
    }
    return nullValue;
}
// Register the GetNull callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetNull},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetNull method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getNull", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(getNull())JS";

Expected result:

JSVM OH\_JSVM\_GetNull success

## OH\_JSVM\_GetUndefined

Call **OH\_JSVM\_GetUndefined** to obtain a JavaScript undefined object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetUndefined.
static JSVM\_Value GetUndefined(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain and parse the parameters passed in.
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Create the value 'undefined'.
    JSVM\_Value value = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetUndefined(env, &value);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_GetUndefined failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetUndefined success");
    }
    return value;
}
// Register the GetUndefined callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetUndefined},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetUndefined method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getUndefined", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call C++ code from JS.
const char \*srcCallNative = R"JS(getUndefined())JS";

Expected result:

JSVM OH\_JSVM\_GetUndefined success
