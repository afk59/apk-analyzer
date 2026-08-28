# Working with ArrayBuffer Using JSVM-API

#### Introduction

**ArrayBuffer** in JavaScript (JS) is a type of object that represents a generic, fixed-length buffer of raw binary data. It provides a way to effectively represent and manipulate raw binary data in JS.

#### Basic Concepts

-   **ArrayBuffer**: An **ArrayBuffer** object represents a generic, fixed-length buffer of raw binary data. The **ArrayBuffer** content cannot be directly operated. Instead, you need to use a TypedArray or **DataView** object to interpret the buffer data in specific formats. **ArrayBuffer** is used to process original binary data of a fixed length, such as files and network data packets.
-   Lifecycle and memory management: When using **ArrayBuffer** with JSVM-API, pay special attention to lifecycle and memory management, ensuring timely memory release.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetArraybufferInfo | Obtains the underlying data buffer of an **ArrayBuffer** object and its length. |
| OH\_JSVM\_IsArraybuffer | Checks whether a JS object is an **ArrayBuffer** object. |
| OH\_JSVM\_DetachArraybuffer | Calls the **Detach()** operation of an **ArrayBuffer** object. |
| OH\_JSVM\_IsDetachedArraybuffer | Checks whether an **ArrayBuffer** object has been detached. |
| OH\_JSVM\_CreateArraybuffer | Creates an **ArrayBuffer** object of the specified size. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in **ArrayBuffer** development.

## OH\_JSVM\_GetArraybufferInfo

Use **OH\_JSVM\_GetArraybufferInfo** to obtain the underlying data buffer of an **ArrayBuffer** object and its length.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetArraybufferInfo.
static JSVM\_Value GetArraybufferInfo(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    // Parse the input parameters.
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Check whether the parameter is an ArrayBuffer object.
    bool isArrayBuffer = false;
    OH\_JSVM\_IsArraybuffer(env, args\[0\], &isArrayBuffer);
    if (!isArrayBuffer) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetArraybufferInfo isArrayBuffer:false");
        return nullptr;
    }
    void \*data;
    size\_t byteLength = 0;
    // Obtain the underlying data buffer and length of the ArrayBuffer object.
    JSVM\_Status status = OH\_JSVM\_GetArraybufferInfo(env, args\[0\], &data, &byteLength);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetArraybufferInfo: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetArraybufferInfo: success");
    }
    return args\[0\];
}
// Register the GetArraybufferInfo callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetArraybufferInfo},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getArraybufferInfo and associate it with a callback. This allows the GetArraybufferInfo callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getArraybufferInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Sample test JS code.
const char \*srcCallNative = R"JS(
getArraybufferInfo(new ArrayBuffer(10));
)JS";

Expected result:

JSVM GetArraybufferInfo: success

## OH\_JSVM\_IsArraybuffer

Use **OH\_JSVM\_IsArraybuffer** to check whether a JS object is an **ArrayBuffer** object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_IsArraybuffer.
static JSVM\_Value IsArrayBuffer(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Call OH\_JSVM\_IsArraybuffer to check whether the input parameter is an ArrayBuffer object.
    bool isArrayBuffer = false;
    JSVM\_Status status = OH\_JSVM\_IsArraybuffer(env, args\[0\], &isArrayBuffer);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM IsArrayBuffer: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsArrayBuffer: success");
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsArrayBuffer: %{public}d", isArrayBuffer);
    }
    JSVM\_Value boolean = nullptr;
    OH\_JSVM\_GetBoolean(env, isArrayBuffer, &boolean);
    return boolean;
}
// Register the IsArrayBuffer callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsArrayBuffer},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named isArrayBuffer and associate it with a callback. This allows the IsArrayBuffer callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isArrayBuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Sample test JS code.
const char \*srcCallNative = R"JS(
isArrayBuffer(new ArrayBuffer(8));
)JS";

Expected result:

JSVM IsArrayBuffer: success
JSVM IsArrayBuffer: 1

## OH\_JSVM\_DetachArraybuffer

Use **OH\_JSVM\_DetachArraybuffer** to call the **Detach()** operation of an **ArrayBuffer** object.

## OH\_JSVM\_IsDetachedArraybuffer

Use **OH\_JSVM\_IsDetachedArraybuffer** to check whether an **ArrayBuffer** object has been detached.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_DetachArraybuffer and OH\_JSVM\_IsDetachedArraybuffer.
static JSVM\_Value DetachArraybuffer(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value arraybuffer = args\[0\];
    JSVM\_Status status = OH\_JSVM\_DetachArraybuffer(env, arraybuffer);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM DetachArraybuffer: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM DetachArraybuffer: success");
    }
    return arraybuffer;
}
static JSVM\_Value IsDetachedArraybuffer(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_Value arraybuffer = args\[0\];
    OH\_JSVM\_DetachArraybuffer(env, arraybuffer);
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_IsDetachedArraybuffer(env, arraybuffer, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM IsDetachedArraybuffer: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsDetachedArraybuffer: success");
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsArrayBuffer: %{public}d", result);
    }
    JSVM\_Value isDetached = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &isDetached);
    return isDetached;
}
// Register the DetachArraybuffer and IsDetachedArraybuffer callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = DetachArraybuffer},
    {.data = nullptr, .callback = IsDetachedArraybuffer},
};
static JSVM\_CallbackStruct \*method = param;
// Set property descriptors named DetachArraybuffer and IsDetachedArraybuffer, and associate them with a callback each. This allows the DetachArraybuffer and IsDetachedArraybuffer callbacks to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"detachArraybuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"isDetachedArraybuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Sample test JS code.
const char \*srcCallNative = R"JS(
let arrayBuffer = new ArrayBuffer(10);
detachArraybuffer(arrayBuffer);
isDetachedArraybuffer(arrayBuffer);
)JS";

Expected result:

JSVM DetachArraybuffer: success
JSVM IsDetachedArraybuffer: success
JSVM IsArrayBuffer: 1

## OH\_JSVM\_CreateArraybuffer

Use **OH\_JSVM\_CreateArraybuffer** to create an **ArrayBuffer** object of the specified size.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CreateArraybuffer.
static JSVM\_Value CreateArraybuffer(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    JSVM\_Value result = nullptr;
    // Parse the input parameters.
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    int32\_t value = 0;
    size\_t length = 0;
    JSVM\_CALL(OH\_JSVM\_GetValueInt32(env, argv\[0\], &value));
    length = size\_t(value);
    void \*data;
    // Create an ArrayBuffer object.
    JSVM\_Status status = OH\_JSVM\_CreateArraybuffer(env, length, &data, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateArraybuffer: failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateArraybuffer: success");
        OH\_LOG\_INFO(LOG\_APP, "JSVM ArrayBuffer length: %{public}d", length);
    }
    // Return the created ArrayBuffer.
    return result;
}
// Register the CreateArraybuffer callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateArraybuffer},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createArraybuffer and associate it with a callback. This allows the CreateArraybuffer callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createArraybuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Sample test JS code.
const char \*srcCallNative = R"JS(
createArraybuffer(8);
)JS";

Expected result:

JSVM CreateArraybuffer: success
JSVM ArrayBuffer length: 8
