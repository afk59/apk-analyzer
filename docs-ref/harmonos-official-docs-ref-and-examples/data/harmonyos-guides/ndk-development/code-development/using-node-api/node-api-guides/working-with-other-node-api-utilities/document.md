# Working with Other Node-API Utilities

#### Introduction

Node-API also provides some useful APIs to improve development experience.

#### Basic Concepts

-   Module loading: A module is an ArkTS file that contains specific functionalities. You can import a module to the shared library. Understanding the loading mechanism and dependencies between Node-API modules is helpful for using **node\_api\_get\_module\_file\_name** correctly.
-   File path and URL: The return value of **node\_api\_get\_module\_file\_name** is the absolute path of the module to be loaded.
-   Strict equality check: The strict equality check is used to check whether two ArkTS values are equal in type and value. When type conversion is considered, if the values being compared are of different types, **false** will be returned even if the values are the same.
-   Asynchronous operation processing: libuv can be used to implement asynchronous operations to avoid blocking the main thread.
-   Event loop: The Node-API module leverages libuv to implement the event-driven programming model. libuv provides an event loop mechanism to process events, trigger callbacks, and manage event queues.

#### Available APIs

| API | Description |
| :-- | :-- |
| node\_api\_get\_module\_file\_name | Obtains the absolute path of the module to be loaded. |
| napi\_strict\_equals | Checks whether two values are strictly equal, that is, equal in both the value and type. For example, you can use **napi\_strict\_equals** to ensure data consistency when working on data structs or algorithms of the specific type. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the APIs mentioned in this topic.

## node\_api\_get\_module\_file\_name

Use **node\_api\_get\_module\_file\_name** to obtain the absolute path of the module to be loaded.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetModuleFileName(napi\_env env, napi\_callback\_info info)
{
    // Declare file, a pointer variable of the const char type, to store the absolute path of the module.
    const char \*file = nullptr;
    napi\_value value = nullptr;
    // Obtain the absolute path of the module and store it in the file variable.
    napi\_status status = node\_api\_get\_module\_file\_name(env, &file);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to get module file name");
        return nullptr;
    }
    // Create a string of the napi\_value type that contains the absolute path.
    napi\_create\_string\_utf8(env, file, NAPI\_AUTO\_LENGTH, &value);
    return value;
}

API declaration:

// index.d.ts
export const getModuleFileName: () => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
    let filename = testNapi.getModuleFileName();
    hilog.info(0x0000, 'testTag', 'Test Node-API node\_api\_get\_module\_file\_name:%{public}s', filename);
} catch (error) {
    hilog.error(0x0000, 'testTag', 'Test Node-API node\_api\_get\_module\_file\_name error: %{public}s', error.message);
}

## napi\_strict\_equals

Use **napi\_strict\_equals** to check whether two ArkTS values are strictly equal.

CPP code:

#include "napi/native\_api.h"

static napi\_value StrictEquals(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_strict\_equals to check whether two ArkTS values are strictly equal.
    bool result = true;
    napi\_status status = napi\_strict\_equals(env, args\[0\], args\[1\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_strict\_equals fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return napi\_value.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);
    return returnValue;
}

API declaration:

// index.d.ts
export const strictEquals: (lhs: string, rhs: string | number) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  let lhs = "123";
  let rhs = "123";
  let str = "456";
  let num = 123;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_strict\_equals: %{public}s', testNapi.strictEquals(lhs, rhs));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_strict\_equals: %{public}s', testNapi.strictEquals(lhs, str));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_strict\_equals: %{public}s', testNapi.strictEquals(lhs, num));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_strict\_equals error: %{public}s', error.message);
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
