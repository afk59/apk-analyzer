# Working with Buffer Using Node-API

#### Introduction

In ArkTS, **Buffer** is a data type used to represent binary data.

#### Basic Concepts

Node-API provides APIs for handling binary data with ArkTS via the **Buffer** object. You can use these APIs to create and operate **Buffer** objects, processing binary data in I/O and network transmission.

-   **Buffer** object: an object used to represent binary data.
-   External buffer: a buffer created in the Node-API module to associate with existing data without copying the data.

#### Available APIs

The following table lists the APIs for processing the binary data in the ArkTS layer, such as file I/O and network transmission.

| API | Description |
| :-- | :-- |
| napi\_create\_buffer | Creates an ArkTS **Buffer** instance of the specified size. |
| napi\_create\_buffer\_copy | Creates and obtains an ArkTS **Buffer** instance of the specified size and initializes the **Buffer** instance with the given parameters. |
| napi\_create\_external\_buffer | Creates an ArkTS **Buffer** instance of the specified size, and initializes it with the given data. You can use this API to add extra data to the buffer. |
| napi\_get\_buffer\_info | Obtains the underlying data buffer and its length of an ArkTS **Buffer** instance. |
| napi\_is\_buffer | Checks whether the given ArkTS value is a **Buffer** object. |
| napi\_create\_external\_arraybuffer | Creates an ArkTS external **ArrayBuffer**. An external **ArrayBuffer** is a special type of **ArrayBuffer** that holds the reference to external data without actually owning the data. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to **Buffer** management.

## napi\_create\_buffer

Call **napi\_create\_buffer** to create a **Buffer** instance. A **Buffer** object is used to manipulate binary data in C/C++.

CPP code:

#include <string>
#include "hilog/log.h"
#include "napi/native\_api.h"

static napi\_value CreateBuffer(napi\_env env, napi\_callback\_info info)
{
    std::string str("CreateBuffer");
    void \*bufferPtr = nullptr;
    size\_t bufferSize = str.size();
    napi\_value buffer = nullptr;
    // Call napi\_create\_buffer to create an ArkTS Buffer instance with the specified size.
    napi\_status status = napi\_create\_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_create\_buffer failed");
        return nullptr;
    }
    // Copy the value of str to the Buffer memory.
    strcpy((char \*)bufferPtr, str.data());
    return buffer;
}

API declaration:

// index.d.ts
export const createBuffer: () => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_buffer: %{public}s', testNapi.createBuffer().toString());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_create\_buffer error');
}

## napi\_create\_buffer\_copy

Call **napi\_create\_buffer\_copy** to create a **Buffer** instance of the specified size and initialize it with data copied from the passed-in buffer. This API allows the specified data to be copied to a **Buffer** instance created.

CPP code:

#include <string>
#include "hilog/log.h"
#include "napi/native\_api.h"

static napi\_value CreateBufferCopy(napi\_env env, napi\_callback\_info info)
{
    // Data to copy.
    char str\[\] = "CreateBufferCopy";
    napi\_value buffer = nullptr;
    // Call napi\_create\_buffer\_copy to create a Buffer instance and copy the content of str to the Buffer.
    void\* resultData = nullptr;
    napi\_status status = napi\_create\_buffer\_copy(env, sizeof(str), str, &resultData, &buffer);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_create\_buffer\_copy failed");
        return nullptr;
    }
    if (resultData != nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "Node-API resultData is : %{public}s.", reinterpret\_cast <const char\*>(resultData));
    } else {
        OH\_LOG\_INFO(LOG\_APP, "Node-API resultData is nullptr.");
    }
    return buffer;
}

API declaration:

// index.d.ts
export const createBufferCopy: () => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_buffer\_copy: %{public}s', testNapi.createBufferCopy().toString());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_create\_buffer\_copy error');
}

## napi\_create\_external\_buffer

Call **napi\_create\_external\_buffer** to create an ArkTS **Buffer** instance that holds a pointer to existing data. This allows the ArkTS layer to directly access and operate the memory, avoiding additional memory allocation and copy operations.

CPP code:

#include <cstdlib>
#include <string>
#include <hilog/log.h>
#include "napi/native\_api.h"

// Callback used to release memory.
void FinalizeCallback(napi\_env env, void \*data, void \*hint)
{
    if (data == nullptr) {
        return;
    }
    free(data);
    data = nullptr;
}

static napi\_value CreateExternalBuffer(napi\_env env, napi\_callback\_info info)
{
    // Create a string.
    std::string str("CreateExternalBuffer");
    // Allocate memory of the string length on the heap.
    void\* data = malloc(str.size() + 1);
    if (data == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "malloc failed");
        return nullptr;
    }
    memset(data, 0, str.size() + 1);
    // Copy the string to the allocated memory.
    strcpy((char \*)(data), (char\*)(str.data()));
    // Use napi\_create\_external\_buffer to create a Buffer instance of the specified size.
    napi\_value buffer = nullptr;
    napi\_status status = napi\_create\_external\_buffer(env, str.size(), data, FinalizeCallback, nullptr, &buffer);
    if (status != napi\_ok) {
        free(data);
        OH\_LOG\_ERROR(LOG\_APP, "napi\_create\_external\_buffer failed");
        return nullptr;
    }
    return buffer;
}

API declaration:

// index.d.ts
export const createExternalBuffer: () => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_external\_buffer: %{public}s', testNapi.createExternalBuffer()
    .toString());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_create\_external\_buffer error');
}

## napi\_get\_buffer\_info

Before performing an operation on the data in a **Buffer** instance in ArkTS, use **napi\_get\_buffer\_info** to obtain the pointer to the data and the data length. This allows the data to be operated without copying data.

CPP code:

#include <string>
#include "hilog/log.h"
#include "napi/native\_api.h"

static napi\_value GetBufferInfo(napi\_env env, napi\_callback\_info info)
{
    // Create a string.
    std::string str("GetBufferInfo");
    napi\_value buffer = nullptr;
    void \*bufferPtr = nullptr;
    size\_t bufferSize = str.size();
    napi\_status status = napi\_create\_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_create\_buffer failed");
        return nullptr;
    }
    strcpy((char \*)bufferPtr, str.data());

    // Obtain the Buffer information.
    void \*tmpBufferPtr = nullptr;
    size\_t bufferLength = 0;
    napi\_get\_buffer\_info(env, buffer, &tmpBufferPtr, &bufferLength);

    // Create an ArkTS string to save the Buffer content and return it.
    if (bufferLength == 0 || ((char\*)tmpBufferPtr)\[bufferLength - 1\] != '\\0') {
        OH\_LOG\_ERROR(LOG\_APP, "Buffer is not null-terminated");
        return nullptr;
    }
    napi\_value returnValue = nullptr;
    napi\_create\_string\_utf8(env, (char\*)tmpBufferPtr, bufferLength, &returnValue);
    return returnValue;
}

API declaration:

// index.d.ts
export const getBufferInfo: () => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_buffer\_info: %{public}s', testNapi.getBufferInfo().toString());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_get\_buffer\_info error');
}

## napi\_is\_buffer

Call **napi\_is\_buffer** to check whether an ArkTS value is a **Buffer** object.

CPP code:

#include <string>
#include "napi/native\_api.h"

static napi\_value IsBuffer(napi\_env env, napi\_callback\_info info)
{
    // Create a Buffer object.
    std::string str = "buffer";
    napi\_value buffer = nullptr;
    void \*bufferPtr = nullptr;
    napi\_create\_buffer(env, str.size(), &bufferPtr, &buffer);

    //Call napi\_is\_buffer to check whether the created object is a Buffer.
    bool result = false;
    napi\_is\_buffer(env, buffer, &result);
    // Return the result.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);
    return returnValue;
}

API declaration:

// index.d.ts
export const isBuffer: () => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_buffer: %{public}s', JSON.stringify(testNapi.isBuffer()));
} catch (error) {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_buffer error');
}

## napi\_create\_external\_arraybuffer

Call **napi\_create\_external\_arraybuffer** to create an ArkTS **ArrayBuffer** with external data.

CPP code:

#include "napi/native\_api.h"

typedef struct {
    uint8\_t \*data;
    size\_t length;
} BufferData;

void FinalizeCallback(napi\_env env, void \*finalize\_data, void \*finalize\_hint)
{
    // Obtain the finalized data.
    BufferData \*bufferData = static\_cast<BufferData \*>(finalize\_hint);

    // Perform the cleanup operation, for example, release memory.
    delete\[\] bufferData->data;
    delete bufferData;
}

napi\_value CreateExternalArraybuffer(napi\_env env, napi\_callback\_info info)
{
    // Create a C++ array with five elements.
    uint8\_t \*dataArray = new uint8\_t\[5\]{1, 2, 3, 4, 5};
    napi\_value externalBuffer = nullptr;
    BufferData \*bufferData = new BufferData{dataArray, 5};

    // Call napi\_create\_external\_arraybuffer to create an external ArrayBuffer instance and specify the callback to be invoked when the ArrayBuffer object is garbage-collected.
    napi\_status status =
        napi\_create\_external\_arraybuffer(env, dataArray, 5, FinalizeCallback, bufferData, &externalBuffer);
    if (status != napi\_ok) {
        // Error handling.
        delete\[\] dataArray;
        delete bufferData;
        napi\_throw\_error(env, nullptr, "Node-API napi\_create\_external\_arraybuffer fail");
        return nullptr;
    }
    napi\_value outputArray;
    // Use napi\_create\_typedarray to create a TypedArray object and pass the external buffer object as a parameter.
    status = napi\_create\_typedarray(env, napi\_int8\_array, 5, externalBuffer, 0, &outputArray);
    if (status != napi\_ok) {
        // Error handling.
        napi\_throw\_error(env, nullptr, "Node-API napi\_create\_typedarray fail");
        return nullptr;
    }
    return outputArray;
}

API declaration:

// index.d.ts
export const createExternalArraybuffer: () => ArrayBuffer | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'testTag', 'Node-API createExternalArraybuffer: %{public}s',
           JSON.stringify(testNapi.createExternalArraybuffer()));

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
