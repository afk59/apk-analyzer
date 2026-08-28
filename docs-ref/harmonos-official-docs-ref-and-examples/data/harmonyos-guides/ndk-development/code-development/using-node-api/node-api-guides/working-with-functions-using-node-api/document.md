# Working with Functions Using Node-API

#### Introduction

Node-API provides APIs for calling ArkTS functions and passing parameters or creating ArkTS functions in C/C++.

#### Basic Concepts

Functions are blocks of reusable code that performs specific tasks or operations. You can define functions to implement different operations. Functions provide a way to modularize and structure code, helping make your code more organized, reusable, and maintainable.

#### Available APIs

| API | Description |
| :-- | :-- |
| napi\_get\_cb\_info | Obtains detailed information about the call, such as the parameters and **this** pointer, from the given callback information. |
| napi\_call\_function | Calls an ArkTS function from a C/C++ addon. |
| napi\_create\_function | Creates an ArkTS function based on a C/C++ function. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to function invocation.

#### napi\_get\_cb\_info

Use **napi\_get\_cb\_info** to obtain detailed information about function calls.

CPP code:

#include "napi/native\_api.h"
// Obtain information about the parameters passed from ArkTS.
static napi\_value GetCbArgs(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
    return args\[0\];
}
// Obtain the number of parameters passed from ArkTS.
static napi\_value GetCbArgQuantity(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 0;
    napi\_value result = nullptr;
    napi\_get\_cb\_info(env, info, &argc, nullptr, nullptr, nullptr);
    napi\_create\_int32(env, argc, &result);
    return result;
}
// Obtain thisArg passed from ArkTS.
static napi\_value GetCbContext(napi\_env env, napi\_callback\_info info)
{
    napi\_value thisArg = nullptr;
    napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisArg, nullptr);
    return thisArg;
}

API declaration:

// index.d.ts
export const getCbArgs: <T>(arg: T) => T;
// The input parameters of getCbArgQuantity are customized. In this example, two input parameters are used: string and number.
export const getCbArgQuantity: (str: string, num: number) => number;
export const getCbContext: () => Object;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

function summation(arr: Array<number>) {
  let sum: number = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr\[i\];
  }
  return sum;
}
const str = 'message';
const arr = \[0, 1, 2, 3, 4, 5\];
const num = 526;
class Student {
  name: string;
  age: number;
  score: number;
  constructor(name: string, age: number, score: number) {
    this.name = name;
    this.age = age;
    this.score = score;
  }
}
let student = new Student('Alice', 18, 100);
// Obtain parameters.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get string arg:%{public}s', testNapi.getCbArgs(str));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get array arg:%{public}s ', testNapi.getCbArgs(arr).toString());
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get num arg:%{public}d ', testNapi.getCbArgs(num));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get undefined arg:%{public}s ', testNapi.getCbArgs(undefined));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get object arg:%{public}s ', JSON.stringify(testNapi.getCbArgs(student)));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get function arg:%{public}d ', testNapi.getCbArgs(summation(arr)));
// Obtain the number of parameters.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get arg quantity:%{public}d ', testNapi.getCbArgQuantity(str, num));
// Obtain the context.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_cb\_info get thisArg:%{public}s ', testNapi.getCbContext().toString());

#### napi\_call\_function

Use **napi\_call\_function** to call an ArkTS function from a C/C++ addon.

Note: The length of **argv** passed to **napi\_call\_function** must be greater than or equal to the number of **argc** declarations, and each element must be initialized to **nullptr**.

CPP code:

#include "napi/native\_api.h"

static napi\_value CallFunction(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    // Obtain the parameters passed from ArkTS.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Obtain the global object. Here, global is used because the second parameter of napi\_call\_function is the this parameter of the ArkTS function.
    napi\_value global = nullptr;
    napi\_get\_global(env, &global);
    // Call the ArkTS method.
    napi\_value result = nullptr;
    // The length of argv passed by napi\_call\_function must be greater than or equal to the value of argc and must be initialized to nullptr.
    napi\_call\_function(env, global, argv\[0\], argc, argv, &result);
    return result;
}

static napi\_value ObjCallFunction(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value argv\[2\] = {nullptr};
    // Obtain the parameters passed from ArkTS.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Call the ArkTS method.
    napi\_value result = nullptr;
    // The length of argv passed by napi\_call\_function must be greater than or equal to the value of argc and must be initialized to nullptr.
    napi\_call\_function(env, argv\[0\], argv\[1\], argc, argv, &result);
    return result;
}

API declaration:

// index.d.ts
export const callFunction: (func: Function) => number;
export const objCallFunction: (obj: Object, func: Function) => number;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

function returnNumber() {
  return 10;
}
class Person {
  age(): number {
    return 11;
  }
}
const person = new Person();
hilog.info(0x0000, 'testTag', 'Test Node-API call\_function:%{public}d', testNapi.callFunction(returnNumber));
hilog.info(0x0000, 'testTag', 'Test Node-API call\_function:%{public}d', testNapi.objCallFunction(person,person.age));

#### napi\_create\_function

Use **napi\_create\_function** to create an ArkTS function object in native code, which allows calling into the native code from ArkTS. This API returns a **napi\_value** that represents the function created.

CPP code:

#include "napi/native\_api.h"

static napi\_value CalculateArea(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    double width = 0;
    napi\_get\_value\_double(env, args\[0\], &width);
    double height = 0;
    napi\_get\_value\_double(env, args\[1\], &height);
    napi\_value area = nullptr;
    napi\_create\_double(env, width \* height, &area);
    return area;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports) {
    napi\_value fn = nullptr;
    napi\_create\_function(env, nullptr, 0, CalculateArea, nullptr, &fn);
    napi\_set\_named\_property(env, exports, "calculateArea", fn);
    return exports;
}
EXTERN\_C\_END

API declaration:

// index.d.ts
export const calculateArea: (width: number, height: number) => number;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'testTag', 'Test Node-API create\_function:%{public}d ', testNapi.calculateArea(1.2, 4));

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
