# Comparing JS Values Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to check whether two JavaScript (JS) values are strictly equal (equal in both value and type). The API provided is equivalent to the JS strict equality operator (**\===**). This API avoids type conversion and loose equality comparison, ensuring equal values and types.

#### Basic Concepts

Strictly equal: If two values are strictly equal, they are equal in both value and type. When type conversion is considered, if the values being compared are of different types, **false** will be returned even if the values are the same.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_StrictEquals | Checks whether two **JSVM\_Value** objects are strictly equal. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in comparing JS values.

## OH\_JSVM\_StrictEquals

Use **OH\_JSVM\_StrictEquals** to check whether two JS values are strictly equal.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_StrictEquals.
static JSVM\_Value IsStrictEquals(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the input parameters.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Call OH\_JSVM\_StrictEquals to check whether two given JS values are strictly equal.
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_StrictEquals(env, args\[0\], args\[1\], &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_StrictEquals: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_StrictEquals: success: %{public}d", result);
    }
    JSVM\_Value isStrictEqual = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &isStrictEqual);
    return isStrictEqual;
}
// Register the IsStrictEquals callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsStrictEquals},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named isStrictEquals and associate it with a callback. This allows the isStrictEquals callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isStrictEquals", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(data = '123';value = '123';isStrictEquals(data,value);)JS";

Expected result:

JSVM OH\_JSVM\_StrictEquals: success: 1
