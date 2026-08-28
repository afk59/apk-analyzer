# Working with Primitives Using Node-API

#### Introduction

Node-API provides APIs for converting data between C/C++ and ArkTS data types and obtaining the ArkTS objects in specified format.

#### Basic Concepts

Before using Node-API to operate ArkTS objects, you need to understand the following basic concepts:

-   Conversion between ArkTS and C/C primitives: You can use Node-API to convert ArkTS values to C/C++ data types, for example, convert an ArkTS value into a C/C++ integer and convert an ArkTS string into a C/C++ string array. You can also convert C/C++ data into an ArkTS value and return the ArkTS value to ArkTS.

#### Available APIs

The following table lists the APIs for converting data between ArkTS and C/C++ types.

| API | Description |
| :-- | :-- |
| napi\_coerce\_to\_bool | Forcibly converts an ArkTS value to an ArkTS Boolean value. |
| napi\_coerce\_to\_number | Forcibly converts an ArkTS value to an ArkTS number. |
| napi\_coerce\_to\_object | Forcibly converts an ArkTS value to an ArkTS object. |
| napi\_coerce\_to\_string | Forcibly converts an ArkTS value to an ArkTS string. |
| napi\_get\_boolean | Obtains the ArkTS Boolean value based on the given C Boolean value. |
| napi\_get\_value\_bool | Obtains the C/C++ equivalent of the given ArkTS Boolean value. |
| napi\_get\_global | Obtains an ArkTS global object so that it can be accessed and manipulated in C/C++. |
| napi\_get\_null | Obtains the ArkTS **null**. |
| napi\_get\_undefined | Obtains the ArkTS **undefined**. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in related APIs.

## napi\_coerce\_to\_bool

Call **napi\_coerce\_to\_bool** to forcibly convert an ArkTS value to an ArkTS Boolean value.

CPP code:

#include "napi/native\_api.h"

static napi\_value CoerceToBool(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse the parameters passed in.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the input value to a Boolean value.
    napi\_value result = nullptr;
    napi\_coerce\_to\_bool(env, args\[0\], &result);
    // Return the ArkTS boolean value.
    return result;
}

API declaration:

// index.d.ts
export const coerceToBool: <T>(data: T) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let value = testNapi.coerceToBool<number>(0);
let str = testNapi.coerceToBool<string>('111111111');
let obj = new Object();
let res = testNapi.coerceToBool<Object>(obj);
let result = testNapi.coerceToBool<null>(null);
// false
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_bool:%{public}s', value);
// true
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_bool:%{public}s', str);
// true
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_bool:%{public}s', res);
// false
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_bool:%{public}s', result);

## napi\_coerce\_to\_number

Call **napi\_coerce\_to\_number** to forcibly convert an ArkTS value to an ArkTS number.

CPP code:

#include "napi/native\_api.h"

static napi\_value CoerceToNumber(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse the parameters passed in.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the input value to a number.
    napi\_value result = nullptr;
    napi\_coerce\_to\_number(env, args\[0\], &result);
    return result;
}

API declaration:

// index.d.ts
export const coerceToNumber: <T>(data: T) => number;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let value = testNapi.coerceToNumber<string>('2556');
let str = testNapi.coerceToNumber<string>('sssss');
let bool = testNapi.coerceToNumber<boolean>(true);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_number:%{public}d', value);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_number:%{public}d', str);    // NAN is returned.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_number:%{public}d', bool);   // 1 is returned.

## napi\_coerce\_to\_object

Call **napi\_coerce\_to\_object** to forcibly convert an ArkTS value to an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value CoerceToObject(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse the parameters passed in.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_value obj = nullptr;
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the input value to an object.
    napi\_coerce\_to\_object(env, args\[0\], &obj);
    return obj;
}

API declaration:

// index.d.ts
export const coerceToObject: <T>(data: T) => Object;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let value = testNapi.coerceToObject<string>('222222');
let result = testNapi.coerceToObject<number>(111);
hilog.info(0x0000, 'testTag', 'Node-API coerceToObject:%{public}s.', typeof result);
if (typeof value === 'object') {
  hilog.info(0x0000, 'testTag', 'Node-API The value is an object.');
} else {
  hilog.info(0x0000, 'testTag', 'Node-API The value is not an object.');
}

## napi\_coerce\_to\_string

Call **napi\_coerce\_to\_string** to forcibly convert an ArkTS value to an ArkTS string.

CPP code:

#include "napi/native\_api.h"

static napi\_value CoerceToString(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse the parameters passed in.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the input value to a string.
    napi\_value str = nullptr;
    napi\_coerce\_to\_string(env, args\[0\], &str);
    return str;
}

API declaration:

// index.d.ts
export const coerceToString: <T>(data: T) => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let value = testNapi.coerceToString<number>(212);
let obj = new Object();
let res = testNapi.coerceToString<Object>(obj);
let bool = testNapi.coerceToString<boolean>(false);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_string:%{public}s', value);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_string:%{public}s', typeof res);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_coerce\_to\_string:%{public}s', bool);

## napi\_get\_boolean

Call **napi\_get\_boolean** to obtain the ArkTS Boolean value based on the given C Boolean value.

CPP code:

#include "napi/native\_api.h"
#include "hilog/log.h"

static napi\_value GetBoolean(napi\_env env, napi\_callback\_info info)
{
    // Pass in two parameters and parse them.
    size\_t argc = 2;
    napi\_value argv\[2\];
    napi\_valuetype data, value;
    napi\_status status = napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed");
        return nullptr;
    }
    // Check the types of the two parameters.
    napi\_typeof(env, argv\[0\], &data);
    napi\_typeof(env, argv\[1\], &value);

    napi\_value returnValue = nullptr;
    // Check whether the types of the two parameters are the same and return the result via a Boolean value.
    status = napi\_get\_boolean(env, data == value, &returnValue);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_boolean failed");
        return nullptr;
    }
    // Return the result.
    return returnValue;
}

API declaration:

// index.d.ts
export const getBoolean: <T>(data: T, value: string) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let value = testNapi.getBoolean<number>(1, '1');
let data = testNapi.getBoolean<string>('sss', '1');
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_boolean:%{public}s', value);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_boolean:%{public}s', data);

## napi\_get\_value\_bool

Call **napi\_get\_value\_bool** to obtain the C Boolean equivalent of an ArkTS Boolean value.

CPP code:

#include "napi/native\_api.h"
#include "hilog/log.h"

static napi\_value GetValueBool(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};

    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
    bool bool\_c = false;
    napi\_status status = napi\_get\_value\_bool(env, args\[0\], &bool\_c);
    if (status == napi\_boolean\_expected) {
        // If napi\_get\_value\_bool is successful, napi\_ok is returned. If a non-Boolean value is passed in, napi\_boolean\_expected is returned.
        return nullptr;
    }
    napi\_value boolNapi = nullptr;
    status = napi\_get\_boolean(env, bool\_c, &boolNapi);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_boolean failed");
        return nullptr;
    }
    return boolNapi;
}

API declaration:

// index.d.ts
export const getValueBool: (value: boolean | string) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

// Pass in a Boolean value and a non-Boolean value. After the Boolean value is passed in, the Boolean value is returned. After the non-Boolean value is passed in, undefined is returned.
hilog.info(0x0000, 'Node-API', 'get\_value\_bool\_not\_bool %{public}s', testNapi.getValueBool('Hello 123'));
hilog.info(0x0000, 'Node-API', 'get\_value\_bool\_true %{public}s', testNapi.getValueBool(true));
hilog.info(0x0000, 'Node-API', 'get\_value\_bool\_false %{public}s', testNapi.getValueBool(false));

## napi\_get\_global

Call **napi\_get\_global** to obtain an ArkTS global object. You can use this API to obtain the **napi\_value** that represents an ArkTS global object, so that the global object of the ArkTS runtime can be called by C/C++.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetGlobal(napi\_env env, napi\_callback\_info info)
{
    napi\_value global = nullptr;
    // Obtains a global object.
    napi\_get\_global(env, &global);
    return global;
}

API declaration:

// index.d.ts
export const getGlobal: () => Object;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let globalObj = testNapi.getGlobal();
// Check whether the obtained global object has its own properties.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_global:%{public}s', globalObj.hasOwnProperty!("undefined"));

## napi\_get\_null

Call **napi\_get\_null** to obtain **null** in ArkTS.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetNull(napi\_env env, napi\_callback\_info info)
{
    napi\_value nullValue = nullptr;
    napi\_get\_null(env, &nullValue);
    return nullValue;
}

API declaration:

// index.d.ts
export const getNull: () => null;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let value = testNapi.getNull();
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_null:%{public}s', value);

## napi\_get\_undefined

Call **napi\_get\_undefined** to obtain **undefined** in ArkTS.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetUndefined(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse the parameters passed in.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    napi\_value value = nullptr;
    napi\_get\_undefined(env, &value);
    // Check whether the input parameter is equal to the ArkTS 'undefined' in both the type and value.
    bool isEqual = false;
    napi\_strict\_equals(env, args\[0\], value, &isEqual);
    // Return a value based on the strict equality check.
    napi\_value result = nullptr;
    // Return true if the two parameters are equal, return false otherwise.
    napi\_get\_boolean(env, isEqual, &result);
    return result;
}

API declaration:

// index.d.ts
export const getUndefined: (value: undefined) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let data: undefined = undefined;
let value = testNapi.getUndefined(data);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_undefined:%{public}s', value);

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
