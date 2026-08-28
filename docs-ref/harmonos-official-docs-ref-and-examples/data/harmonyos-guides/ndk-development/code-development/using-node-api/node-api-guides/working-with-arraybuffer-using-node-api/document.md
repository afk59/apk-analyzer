# Working with ArrayBuffer Using Node-API

#### Introduction

**ArrayBuffer** in ArkTS is a type of object that represents a generic, fixed-length buffer of raw binary data. It provides a way to effectively represent and manipulate raw binary data in ArkTS.

#### Basic Concepts

-   **ArrayBuffer**: An **ArrayBuffer** object represents a generic, fixed-length buffer of raw binary data. The **ArrayBuffer** content cannot be directly operated. Instead, you need to use a **TypedArray** or **DataView** object to interpret the buffer data in specific formats. **ArrayBuffer** is used to process a large amount of binary data, such as files and network data packets.

#### Available APIs

The following table lists the APIs used to manipulate data of the **ArrayBuffer** type.

| API | Description |
| :-- | :-- |
| napi\_is\_arraybuffer | Checks whether a value is an **ArrayBuffer** object. Note that this API cannot be used to check whether a value is a **TypedArray** object. To check whether a value is a **TypedArray** object, use **napi\_is\_typedarray**. |
| napi\_get\_arraybuffer\_info | Obtains information of an **ArrayBuffer** object, including the pointer to the data and the data length. |
| napi\_detach\_arraybuffer | Detaches the underlying data from an **ArrayBuffer** object. After the data is detached, you can operate the data in C/C++. |
| napi\_is\_detached\_arraybuffer | Checks whether an **ArrayBuffer** object has been detached. |
| napi\_create\_arraybuffer | Creates an ArkTS **ArrayBuffer** object with the specified byte length. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to **ArrayBuffer** management.

The following header files are required for the C++ code:

#include "napi/native\_api.h"
#include <cstring>
#include "hilog/log.h"

The following modules are required for the ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

## napi\_is\_arraybuffer

Call **napi\_is\_arraybuffer** to check whether a JS value is an **ArrayBuffer** object.

CPP code:

// napi\_is\_arraybuffer
static napi\_value IsArrayBuffer(napi\_env env, napi\_callback\_info info)
{
    // Obtain a parameter.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_is\_arraybuffer to check whether the input parameter is an \*\*ArrayBuffer\*\* object.
    bool result = false;
    napi\_status status = napi\_is\_arraybuffer(env, args\[0\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_is\_arraybuffer fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return it.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);
    return returnValue;
}

API declaration:

index.d.ts

export const isArrayBuffer: <T>(arrayBuffer: T) => boolean | undefined; // napi\_is\_arraybuffer

ArkTS code:

// test interface napi\_is\_arraybuffer
try {
  let value = new ArrayBuffer(1);
  let data = "123";
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_arraybuffer: %{public}s',
    testNapi.isArrayBuffer(value));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_arraybuffer: %{public}s',
    testNapi.isArrayBuffer(data));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_arraybuffer error: %{public}s',
    error.message);
  // ...
}

Log output:

Test Node-API napi\_is\_arraybuffer: true

Test Node-API napi\_is\_arraybuffer: false

## napi\_get\_arraybuffer\_info

Call **napi\_get\_arraybuffer\_info** to obtain the underlying data buffer and length of an **ArrayBuffer** object. This API can process only **ArrayBuffer** objects. Do not pass other types to the API. To obtain an **ArrayBuffer** object from a **Uint8Array** object, you need to execute the **.buffer** operation on the ArkTS side.

CPP code:

// napi\_get\_arraybuffer\_info
static napi\_value GetArrayBufferInfo(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Check whether the parameter is an ArrayBuffer object.
    bool isArrayBuffer = false;
    napi\_is\_arraybuffer(env, args\[0\], &isArrayBuffer);
    if (!isArrayBuffer) {
        napi\_throw\_type\_error(env, nullptr, "Argument must be an ArrayBuffer");
        return nullptr;
    }

    void \*data = nullptr;
    size\_t byteLength = 0;
    // Obtain the underlying data buffer and length of the ArrayBuffer object.
    napi\_status status = napi\_get\_arraybuffer\_info(env, args\[0\], &data, &byteLength);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to get ArrayBuffer info");
        return nullptr;
    }
    // Create a result object.
    napi\_value result = nullptr;
    napi\_create\_object(env, &result);
    // Set the byte length property of the data buffer.
    napi\_value byteLengthValue = nullptr;
    napi\_create\_uint32(env, byteLength, &byteLengthValue);
    napi\_set\_named\_property(env, result, "byteLength", byteLengthValue);
    napi\_value bufferData = nullptr;
    void \*newData = nullptr;
    napi\_create\_arraybuffer(env, byteLength, &newData, &bufferData);
    memcpy(newData, data, byteLength);
    napi\_set\_named\_property(env, result, "buffer", bufferData);
    return result;
}

API declaration:

index.d.ts

export class ArrayBufferInfo {
  byteLength: number;
  buffer: ArrayBuffer;
}
export const getArrayBufferInfo: (data: ArrayBuffer) => ArrayBufferInfo | undefined; // napi\_get\_arraybuffer\_info

ArkTS code:

// test interface napi\_get\_arraybuffer\_info
try {
  let typedArray = new Uint8Array(\[1, 2, 3, 4, 5\]);
  let buffer = typedArray.buffer;
  let result = testNapi.getArrayBufferInfo(buffer) as testNapi.ArrayBufferInfo;
  let resBuffer = new Uint8Array(result.buffer);
  hilog.info(0x0000, 'testTag', 'Test Node-API get\_arrayBuffer\_info byteLength: %{public}d buffer: %{public}s', result.byteLength, JSON.stringify(resBuffer));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API get\_arrayBuffer\_info error: %{public}s', error.message);
}

Log output:

Test Node-API napi\_get\_arraybuffer\_info byteLength: 5 buffer: {"0":1,"1":2,"2":3,"3":4,"4":5}

## napi\_detach\_arraybuffer

Call **napi\_detach\_arraybuffer** to detach the underlying data from an **ArrayBuffer** object.

## napi\_is\_detached\_arraybuffer

Call **napi\_is\_detached\_arraybuffer** to check whether an **ArrayBuffer** object has been detached.

CPP code:

// napi\_detach\_arraybuffer
static napi\_value DetachedArrayBuffer(napi\_env env, napi\_callback\_info info)
{
    // Call napi\_detach\_arraybuffer to detach the underlying data from an ArrayBuffer object.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_value arrayBuffer = args\[0\];
    napi\_detach\_arraybuffer(env, arrayBuffer);
    // Pass out the detached ArrayBuffer object.
    return arrayBuffer;
}

// napi\_is\_detach\_arraybuffer
static napi\_value IsDetachedArrayBuffer(napi\_env env, napi\_callback\_info info)
{
    // Call napi\_is\_detached\_arraybuffer to check whether the specified ArrayBuffer object has been detached.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_value arrayBuffer = args\[0\];
    bool result = false;
    napi\_is\_detached\_arraybuffer(env, arrayBuffer, &result);
    // Call napi\_get\_boolean to convert the return value to napi\_value, and pass out the napi\_value for printing.
    napi\_value returnValue;
    napi\_get\_boolean(env, result, &returnValue);
    return returnValue;
}

API declaration:

index.d.ts

export const detachedArrayBuffer: (buffer:ArrayBuffer) => ArrayBuffer; // napi\_detach\_arraybuffer
export const isDetachedArrayBuffer: (arrayBuffer: ArrayBuffer) => boolean; //napi\_is\_detached\_arraybuffer

ArkTS code:

// test interface napi\_detach\_arraybuffer and napi\_is\_detached\_arraybuffer
try {
  const bufferArray = new ArrayBuffer(8);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_detached\_arraybuffer one: %{public}s',
    testNapi.isDetachedArrayBuffer(bufferArray));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_detached\_arraybuffer two: %{public}s ',
    testNapi.isDetachedArrayBuffer(testNapi.detachedArrayBuffer(bufferArray)));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_detached\_arraybuffer error: %{public}s',
    error.message);
  // ...
}

Log output:

Test Node-API napi\_is\_detached\_arraybuffer one: false

Test Node-API napi\_is\_detached\_arraybuffer two: true

## napi\_create\_arraybuffer

Call **napi\_create\_arraybuffer** to create an ArkTS **ArrayBuffer** object with the specified byte length in C/C++. If the caller wants to directly operate the buffer, return the underlying buffer to the caller. To write data to this buffer from ArkTS, you need to create a **TypedArray** or **DataView** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/6MF9hXHUTeKszHIBh5tOmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1C379274E56FAA6D60AFA49FC4CB0CC20CA44C2A324374C453610EFE35B7B55)

If **byte\_length** of **napi\_create\_arraybuffer** is **0** or an excessively large value, nullptr will be returned in **data**. Therefore, it is necessary to check whether **data** is empty before using it.

CPP code:

// napi\_create\_arraybuffer
static napi\_value CreateArrayBuffer(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_value result = nullptr;
    // Parse the input parameters.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    int32\_t value;
    size\_t length;
    // Convert the parameter passed from ArkTS to the size\_t type and use it as the parameter of napi\_create\_arraybuffer.
    napi\_get\_value\_int32(env, argv\[0\], &value);
    length = size\_t(value);
    void \*data = nullptr;
    // Create an ArrayBuffer object.
    napi\_create\_arraybuffer(env, length, &data, &result);
    if (data != nullptr) {
        // Check data before using it for subsequent operations.
    } else {
        // Handle the memory allocation failure.
        OH\_LOG\_ERROR(LOG\_APP, "Failed to allocate memory for ArrayBuffer");
        return nullptr;
    }
    // Return the ArrayBuffer object.
    return result;
}

API declaration:

index.d.ts

export const createArrayBuffer: (size: number) => ArrayBuffer; // napi\_create\_arraybuffer

ArkTS code:

// test interface napi\_create\_arraybuffer
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_arraybuffer:%{public}s',
  testNapi.createArrayBuffer(10).toString());

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)

Log output:

Test Node-API napi\_create\_arraybuffer:\[object ArrayBuffer\]

#### NOTE

-   Lifecycle and memory management: When using Node-API to process **ArrayBuffer** objects, note that the lifecycle of the buffer data segment of the **void**\* type is managed by the engine and [cannot be deleted by users. Otherwise, a double free error may occur](../../node-api-development-specifications/document.md#avoiding-releasing-the-obtained-buffer-repeatedly).
-   Allocated buffer size: When the value of **byte\_length** is large, no exception is thrown when the allocation fails. The memory specified by **data** is **nullptr**. It is recommended that \***data == nullptr** be strictly checked and the upper limit of **byte\_length** be checked to avoid OOM.
