# Creating and Obtaining Values Using JSVM-API

#### Introduction

In JavaScript (JS), the integer type represents a number without a decimal point, and the double type represents a number with a fractional part. Due to the limitation of the value storage mode of JS, very large or very small numbers cannot be accurately represented. In this case, you can use JSVM-API to represent large numbers in BigInt format.

#### Basic Concepts

Before using JSVM-API to create and obtain numbers, you need to understand the following concepts:

-   Number type
    
    When using JSVM-API, you may need to convert values of number types between C and JS. When converting the data, pay attention to the data range, signedness (signed or unsigned), and precision (single or double precision).
    
-   Error handling
    
    You also need to use JSVM-API to capture and handle errors that may occur during the conversion. For example, when an integer is created, you may need to capture and handle memory allocation failures or other runtime errors.
    
-   Interaction between JS and JSVM-API
    
    During the development, you need to consider the interaction between JS and JSVM-API, including how to pass the data of the number type and return the correct value.
    

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetValueUint32 | Obtains the C Uint32 primitive equivalent of the given JS number. |
| OH\_JSVM\_GetValueInt32 | Obtains the C Int32 primitive equivalent of the given JS number. |
| OH\_JSVM\_GetValueInt64 | Obtains the C Int64 primitive equivalent of the given JS number. |
| OH\_JSVM\_GetValueDouble | Obtains the C Double primitive equivalent of the given JS number. |
| OH\_JSVM\_CreateInt32 | Creates a JS number object from a C Int32\_t object. |
| OH\_JSVM\_CreateUint32 | Creates a JS number object from a C Uint32\_t object. |
| OH\_JSVM\_CreateInt64 | Creates a JS number object from a C Int64\_t object. |
| OH\_JSVM\_CreateDouble | Creates a JS number object from a C double object. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in manipulating basic data types.

## OH\_JSVM\_GetValueUint32

Use **OH\_JSVM\_GetValueInt32** to obtain a C uint32 value from a JS value.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_GetValueUint32.
static JSVM\_Value GetValueUint32(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the parameter of the Number type.
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    // Parse the input parameters.
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    uint32\_t number = 0;
    // Obtain a 32-bit unsigned integer.
    JSVM\_Status status = OH\_JSVM\_GetValueUint32(env, argv\[0\], &number);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueUint32 fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueUint32 success: %{public}u", number);
    }
    return argv\[0\];
}

// Register the GetValueUint32 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueUint32},
};
static JSVM\_CallbackStruct \*method = param;

// Set a property descriptor named getValueUint and associate it with a callback. This allows the GetValueUint callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueUint32", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getValueUint32(123))JS";

Expected result:

JSVM GetValueUint32 success: 123

## OH\_JSVM\_GetValueInt32

Use **OH\_JSVM\_GetValueInt32** to obtain a C Int32 value from a JS value.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_GetValueInt32.
static JSVM\_Value GetValueInt32(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    int32\_t result32 = 0;
    // Parse the input parameters.
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Convert the parameter into a C int32 value.
    JSVM\_Status status = OH\_JSVM\_GetValueInt32(env, args\[0\], &result32);
    if (status != JSVM\_OK) {
        return nullptr;
    }
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueInt32 fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueInt32 success: %{public}d", result32);
    }
    return args\[0\];
}

// Register the GetValueInt32 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueInt32},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getValueInt32 and associate it with a callback. This allows the GetValueInt32 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueInt32", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getValueInt32(-123))JS";

Expected result:

JSVM GetValueInt32 success: -123

## OH\_JSVM\_GetValueInt64

Use **OH\_JSVM\_GetValueInt64** to obtain a C Int64 value from a JS value.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_GetValueInt64.
static JSVM\_Value GetValueInt64(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    int64\_t result64 = 0;
    // Parse the input parameters.
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Convert the input parameters into C int64 values.
    JSVM\_Status status = OH\_JSVM\_GetValueInt64(env, args\[0\], &result64);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueInt64 fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueInt64 success: %{public}ld", result64);
    }
    return args\[0\];
}

// Register the GetValueInt64 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueInt64},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getValueInt64 and associate it with a callback. This allows the GetValueInt64 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getValueInt64(-123))JS";

Expected result:

JSVM GetValueInt64 success: -123

## OH\_JSVM\_GetValueDouble

Use **OH\_JSVM\_GetValueDouble** to obtain a C double value from a JS value.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_GetValueDouble.
static JSVM\_Value GetDouble(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    double value = 0;
    JSVM\_Status status = OH\_JSVM\_GetValueDouble(env, args\[0\], &value);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetDouble fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetDouble success: %{public}f", value);
    }
    return args\[0\];
}

// Register the GetDouble callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetDouble},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getDouble and associate it with a callback. This allows the GetDouble callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getDouble", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getDouble(-110.0456))JS";

Expected result:

JSVM GetDouble success: -110.045600

## OH\_JSVM\_CreateInt32

Use **OH\_JSVM\_CreateInt32** to create a JS number object from an int32\_t object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_CreateInt32.
static JSVM\_Value CreateInt32(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    int32\_t value = -20;
    // Create a JS Int32 number.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateInt32(env, value, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateInt32 fail");
    } else {
        int32\_t number = 0;
        OH\_JSVM\_GetValueInt32(env, result, &number);
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateInt32 success: %{public}d", number);
    }
    return result;
}

// Register the CreateInt32 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateInt32},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createInt32 and associate it with a callback. This allows the CreateInt32 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createInt32", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createInt32())JS";

Expected result:

JSVM CreateInt32 success: -20

## OH\_JSVM\_CreateUint32

Use **OH\_JSVM\_CreateUint32** to create a JS number object from a uint32\_t object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_CreateUint32.
static JSVM\_Value CreateUInt32(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    //
    // If the uint32\_t type is used to represent -26, overflow occurs. Modulo operation is performed on the result to convert the binary complement of the negative number to a positive number. That is, 4294967270 will be returned.
    // uint32\_t represents a 32-bit unsigned integer, ranging from 0 to 2^32 - 1, that is, 0 to 4294967295.
    //
    uint32\_t value = 26;
    // Create a JS Uint32 number.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateUint32(env, value, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateUInt32 fail");
    } else {
        uint32\_t number = 0;
        OH\_JSVM\_GetValueUint32(env, result, &number);
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateUInt32 success: %{public}u", number);
    }
    return result;
}

// Register the CreateUInt32 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateUInt32},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createUInt32 and associate it with a callback. This allows the CreateUInt32 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createUInt32", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createUInt32())JS";

Expected result:

JSVM CreateUInt32 success: 26

## OH\_JSVM\_CreateInt64

Use **OH\_JSVM\_CreateInt64** to create a JS number object from an int64\_t object. You are advised to use the **BigInt** API to indicate the large JS number.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_CreateInt64.
static JSVM\_Value CreateInt64(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    int64\_t value = 2147483648;
    // Create a JS Int64 number.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateInt64(env, value, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateInt64 fail");
    } else {
        int64\_t number = 0;
        OH\_JSVM\_GetValueInt64(env, result, &number);
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateInt64 success: %{public}ld", number);
    }
    return result;
}

// Register the CreateInt64 callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateInt64},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createInt64 and associate it with a callback. This allows the CreateInt64 callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createInt64())JS";

Expected result:

JSVM CreateInt64 success: 2147483648

## OH\_JSVM\_CreateDouble

Use **OH\_JSVM\_CreateDouble** to create a JS number object from a double object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// register a CreateDouble callback.

// Define OH\_JSVM\_CreateDouble.
static JSVM\_Value CreateDouble(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    double value = 1.234;
    // Create a JS double number.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateDouble(env, value, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateDouble fail");
    } else {
        double number = 0;
        OH\_JSVM\_GetValueDouble(env, result, &number);
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateDouble success: %{public}f", number);
    }
    return result;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateDouble},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createDouble and associate it with a callback. This allows the CreateDouble callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createDouble", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createDouble())JS";

Expected result:

JSVM CreateDouble success: 1.234000
