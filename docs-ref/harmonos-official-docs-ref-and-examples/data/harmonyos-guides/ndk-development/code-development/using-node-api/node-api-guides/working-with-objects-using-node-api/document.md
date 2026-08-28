# Working with Objects Using Node-API

#### Overview

Node-API provides APIs for basic object operations, including creating an object, obtaining the prototype of an object, freezing or sealing an object, and checking the object type.

#### Basic Concepts

You may need to define and operate objects when using Node-API in development. For example, define an API with an object as an input parameter, perform operations on the object, and have a result object returned. In this process, you need to ensure that the API definition is clear and compatible with the properties and methods of the object.

-   API: defines the interaction protocol between components. An API includes input parameters, output result, and possible error handling. By calling APIs, components can interact and exchange data with each other without knowing the internal implementation details.
-   Object: a composite data type that allows values of different types in an independent entity in ArkTS. An object is a collection of properties and methods. A property is a value associated with an object, and a method is an operation that the object can perform.

#### Available APIs

The following table lists the APIs for operating and managing ArkTS objects.

| API | Description |
| :-- | :-- |
| napi\_get\_prototype | Obtains the prototype of an ArkTS object. You can use this API to obtain the prototype object in C/C++. |
| napi\_create\_object | Creates a default ArkTS object. |
| napi\_object\_freeze | Freezes an ArkTS object. Once an object is frozen, its properties are immutable. |
| napi\_object\_seal | Seals an ArkTS object. Once an object is sealed, its properties cannot be added or deleted, but property values can be modified. |
| napi\_typeof | Obtains the type of an ArkTS value. |
| napi\_instanceof | Checks whether an ArkTS object is an instance of the specified constructor. |
| napi\_type\_tag\_object | Associates the value of a tag pointer with an ArkTS object. |
| napi\_check\_object\_type\_tag | Checks whether a tag pointer is associated with a ArkTS object. |
| napi\_create\_symbol | Creates an ArkTS **Symbol** object. |
| napi\_create\_external | Creates an ArkTS external object, which can be used to pass custom data structs or objects in C/C++ to ArkTS so that it can be accessible from ArkTS. |
| napi\_get\_value\_external | Obtains the ArkTS data from the external object created by **napi\_create\_external**. This API can be used to pass data between ArkTS and C/C++. |

With these APIs, you can easily create and manipulate ArkTS objects in C/C++.

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to object management.

## napi\_get\_prototype

Call **napi\_get\_prototype** to obtain the prototype of an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetPrototype(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse input parameters.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
    napi\_value result = nullptr;
    // Obtain the prototype object of this object and return the prototype object obtained to the variable result of the napi\_value type.
    napi\_get\_prototype(env, args\[0\], &result);
    return result;
}

API declaration:

// index.d.ts
export const getPrototype: (object: Object) => Object;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

// Define a class.
class Person {
  // Property.
  name: string;
  age: number;
  // Constructor.
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}
// Create a class instance.
const person = new Person('Alice', 30);
// Pass in an instance object and obtain the prototype of the object.
let applePrototype = testNapi.getPrototype(person);
// Check whether the prototype obtained by testNapi.getPrototype() is an Apple prototype.
// Since DevEco Studio 4.1, ArkTS does not have the prototype concept.
// When you perform prototype-related operations,
// 'Prototype assignment is not supported (arkts-no-prototype-assignment)' will be displayed.
// Therefore, you need to run the following code in a TS file:
if (applePrototype === Person.prototype) {
  hilog.info(0x0000, 'Node-API', 'get\_prototype\_success');
} else {
  hilog.error(0x0000, 'Node-API', 'get\_prototype\_fail');
}

## napi\_create\_object

Call **napi\_create\_object** to create an empty ArkTS object.

CPP code:

#include "napi/native\_api.h"

napi\_value NewObject(napi\_env env, napi\_callback\_info info)
{
    napi\_value object = nullptr;
    // Create an empty object.
    napi\_create\_object(env, &object);
    // Set the object property.
    napi\_value name = nullptr;
    // Set the property name to "name".
    napi\_create\_string\_utf8(env, "name", NAPI\_AUTO\_LENGTH, &name);
    napi\_value value = nullptr;
    // Set the property value to "Hello from N-API!"
    napi\_create\_string\_utf8(env, "Hello from Node-API!", NAPI\_AUTO\_LENGTH, &value);
    // Set the property on the object.
    napi\_set\_property(env, object, name, value);
    return object;
}

API declaration:

// index.d.ts
export const createObject: () => { name: string };

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  const myObject = testNapi.createObject();
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_object: %{public}s', myObject.name);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_create\_object errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}

## napi\_object\_freeze

Call **napi\_object\_freeze** to freeze an ArkTS object. After an object is frozen, new properties or methods cannot be added to the object, and the values of existing properties or methods cannot be modified.

CPP code:

#include "hilog/log.h"
#include "napi/native\_api.h"

static napi\_value ObjectFreeze(napi\_env env, napi\_callback\_info info)
{
    // Obtain the object passed from ArkTS.
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);

    // Call napi\_object\_freeze to freeze the object passed in.
    napi\_value objFreeze = argv\[0\];
    napi\_status status = napi\_object\_freeze(env, objFreeze);
    if (status == napi\_ok) {
        OH\_LOG\_INFO(LOG\_APP, "Node-API napi\_object\_freeze success");
    }
    // Return the frozen object to ArkTS.
    return objFreeze;
}

API declaration:

// index.d.ts
export interface Obj {
  data: number
  message: string
}
export const objectFreeze: (objFreeze: Object) => Obj;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = {data: 0, message: "hello world"};
  let objFreeze = testNapi.objectFreeze(obj);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_object\_freeze: %{public}s', (objFreeze.data = 1));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_object\_freeze error: %{public}s', error.message);
}

## napi\_object\_seal

Call **napi\_object\_seal** to seal an ArkTS object. After an object is sealed, new properties cannot be added to the object, existing properties cannot be deleted, but the values of existing properties can be modified.

CPP code:

#include "hilog/log.h"
#include "napi/native\_api.h"

static napi\_value ObjectSeal(napi\_env env, napi\_callback\_info info)
{
    // Obtain the object passed from ArkTS.
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Call napi\_object\_seal to seal the object passed in.
    napi\_value objSeal = argv\[0\];
    napi\_status status = napi\_object\_seal(env, objSeal);
    if (status == napi\_ok) {
        OH\_LOG\_INFO(LOG\_APP, "Node-API napi\_object\_seal success");
    } else {
        napi\_throw\_error(env, nullptr, "Node-API napi\_object\_seal failed");
        return nullptr;
    }
    // Return the sealed object to ArkTS.
    return objSeal;
}

API declaration:

// index.d.ts
export interface Obj {
  data: number
  message: string
  id: number
}
export const objectSeal : (objSeal: Object) => Obj;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
    // Optional property.
    address?: number
  }
  let obj: Obj = { data: 0, message: "hello world"};
  let objSeal = testNapi.objectSeal(obj);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_object\_seal: %{public}s', objSeal.message);
  objSeal.data = 1;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_object\_seal: %{public}d', objSeal.data);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_object\_seal: %{public}d', (objSeal.id = 1));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_object\_seal error: %{public}s', error.message);
}

## napi\_typeof

Call **napi\_typeof** to obtain the ArkTS type of an ArkTS value.

**NOTE**

**napi\_typeof** can determine the following types.

| Type |
| :-- |
| undefined |
| null |
| boolean |
| number |
| string |
| object |
| function |
| bigint |

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiTypeOf(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameter.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Call napi\_typeof to check the type of the ArkTS parameter passed in.
    napi\_valuetype valueType;
    napi\_status status = napi\_typeof(env, args\[0\], &valueType);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_typeof fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return napi\_value.
    napi\_value returnValue = nullptr;
    switch(valueType) {
    case napi\_undefined:
        napi\_create\_string\_utf8(env, "Input type is napi\_undefined", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_null:
        napi\_create\_string\_utf8(env, "Input type is napi\_null", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_boolean:
        napi\_create\_string\_utf8(env, "Input type is napi\_boolean", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_number:
        napi\_create\_string\_utf8(env, "Input type is napi\_number", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_string:
        napi\_create\_string\_utf8(env, "Input type is napi\_string", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_object:
        napi\_create\_string\_utf8(env, "Input type is napi\_object", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_function:
        napi\_create\_string\_utf8(env, "Input type is napi\_function", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    case napi\_bigint:
        napi\_create\_string\_utf8(env, "Input type is napi\_bigint", NAPI\_AUTO\_LENGTH, &returnValue);
        break;
    default:
        napi\_create\_string\_utf8(env, "unknown", NAPI\_AUTO\_LENGTH, &returnValue);
    }

    return returnValue;
}

API declaration:

// index.d.ts
export const napiTypeOf : <T>(value: T) => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  let varUndefined: undefined;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varUndefined));
  let varNull: null = null;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varNull));
  let varTrue= true;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varTrue));
  let varNum = 1;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varNum));
  let varString = "str";
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varString));
  class Obj {
    id: number = 0
    name: string = ""
  }
  let varObject: Obj = {id: 1, name: "LiLei"};
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varObject));
  const mulNum = (a: number, b: number): number => a \* b;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(mulNum));
  let varBigint = BigInt("1234567890123456789012345678901234567890");
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_typeof: %{public}s', testNapi.napiTypeOf(varBigint));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_typeof error: %{public}s', error.message);
}

## napi\_instanceof

Call **napi\_instanceof** to check whether an ArkTS object is an instance of the specified constructor.

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiInstanceOf(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_instanceof to check whether the given object is an instance of the given constructor.
    bool result = true;
    napi\_status status = napi\_instanceof(env, args\[0\], args\[1\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_instanceof fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return napi\_value.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);

    return returnValue;
}

API declaration:

// index.d.ts
export const napiInstanceOf: (date: Object, construct: Object) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  }
  const person = new Person("Alice", 30);
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = { data: 0, message: "hello world"};
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_instanceof: %{public}s', testNapi.napiInstanceOf(person, Person));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_instanceof: %{public}s', testNapi.napiInstanceOf(obj, Person));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_instanceof error: %{public}s', error.message);
}

## napi\_type\_tag\_object

Call **napi\_type\_tag\_object** to associate the value of a **type\_tag** pointer with an ArkTS object so that the object can be identified more accurately.

In the ArkTS version, **napi\_type\_tag\_object** does not use private symbols. As a result, the type\_tag may be overwritten. You are advised not to use this API in key security scenarios.

## napi\_check\_object\_type\_tag

Call **napi\_check\_object\_type\_tag** to check whether an ArkTS object is associated with a tag pointer.

The type tags associate native types with ArkTS types, allowing ArkTS objects to be accurately identified and processed in C/C++.

CPP code:

#include "napi/native\_api.h"

#define NUMBERINT\_FOUR 4
// Define a static constant named napi\_type\_tag array to store type tags.
static const napi\_type\_tag TagsData\[NUMBERINT\_FOUR\] = {
    {0x9e4b2449547061b3, 0x33999f8a6516c499},
    {0x1d55a794c53a726d, 0x43633f509f9c944e},
    // Default tag or no tag.
    {0, 0},
    {0x6a971439f5b2e5d7, 0x531dc28a7e5317c0},
};

static napi\_value SetTypeTagToObject(napi\_env env, napi\_callback\_info info)
{
    // Obtain the call information and parameters.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index number and convert it to napi\_value.
    int32\_t index = 0;
    napi\_get\_value\_int32(env, args\[1\], &index);
    // Set the type tag for the parameter (object).
    napi\_status status = napi\_type\_tag\_object(env, args\[0\], &TagsData\[index\]);
    if (status != napi\_ok) {
        napi\_throw\_error(env, "Reconnect error", "napi\_type\_tag\_object failed");
        return nullptr;
    }
    // Convert the bool value to napi\_value and return it.
    napi\_value result = nullptr;
    napi\_get\_boolean(env, true, &result);
    return result;
}

static napi\_value CheckObjectTypeTag(napi\_env env, napi\_callback\_info info)
{
    // Obtain the call information and parameters.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index number and convert it to napi\_value.
    int32\_t index = 0;
    napi\_get\_value\_int32(env, args\[1\], &index);
    // Check the type tag of the object.
    bool checkResult = true;
    napi\_check\_object\_type\_tag(env, args\[0\], &TagsData\[index\], &checkResult);
    // Convert the bool value to napi\_value and return it.
    napi\_value checked = nullptr;
    napi\_get\_boolean(env, checkResult, &checked);

    return checked;
}

API declaration:

// index.d.ts
export const setTypeTagToObject: (obj: Object, index: number) => boolean | undefined;
export const checkObjectTypeTag: (obj: Object, index: number) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

class Obj {
  data: number = 0
  message: string = ""
}
let objA: Obj = { data: 0, message: "hello world"};
let objB: Obj = { data: 10, message: "typeTag"};
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_type\_tag\_object objA -> 0: %{public}s', testNapi.setTypeTagToObject(objA, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_type\_tag\_object objB -> 0: %{public}s', testNapi.setTypeTagToObject(objB, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_check\_object\_type\_tag objA -> 0: %{public}s', testNapi.checkObjectTypeTag(objA, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_check\_object\_type\_tag objB -> 1: %{public}s', testNapi.checkObjectTypeTag(objB, 1));

## napi\_create\_external

Call **napi\_create\_external** to create an ArkTS external object with a custom C/C++ object and expose it to ArkTS. With this API, you can create a Node-API value that contains a pointer to a custom C/C++ object so that the object can be accessed and managed by ArkTS.

CPP code:

#include <cstdlib>
#include <string>
#include "hilog/log.h"
#include "napi/native\_api.h"

// Callback used to release the external data.
void finalizeCallback(napi\_env env, void \*data, void \*hint) {
    // Release external data.
    free(data);
}

static napi\_value GetExternalType(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the data type of the parameter.
    napi\_valuetype valueType;
    napi\_typeof(env, args\[0\], &valueType);
    napi\_value returnValue = nullptr;
    if (valueType == napi\_external) {
        // If the data type is napi\_external, return true.
        napi\_get\_boolean(env, true, &returnValue);
    } else {
        napi\_get\_boolean(env, false, &returnValue);
    }
    return returnValue;
}

static napi\_value CreateExternal(napi\_env env, napi\_callback\_info info)
{
    // Set the external data size to 10.
    const size\_t dataSize = 10;
    // Allocate memory to the external data.
    void \*data = malloc(dataSize);
    if (data == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "malloc failed");
        return nullptr;
    }
    // Initialize the external data.
    memset(data, 0, dataSize);
    napi\_value result = nullptr;
    // Return an object with external data.
    napi\_status status = napi\_create\_external(env, data, finalizeCallback, nullptr, &result);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, " Node-API Failed to create external data");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const createExternal: () => Object;
export const getExternalType: (externalData: Object) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

const externalData = testNapi.createExternal();
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_external:%{public}s', testNapi.getExternalType(externalData));

## napi\_get\_value\_external

Call **napi\_get\_value\_external** to obtain the ArkTS data from the external object created by **napi\_create\_external**.

CPP code:

#include "napi/native\_api.h"

static int external = 5;
static napi\_value GetValueExternal(napi\_env env, napi\_callback\_info info)
{
    // Create external data.
    int\* data = &external;
    napi\_value setExternal = nullptr;
    napi\_create\_external(env, data, nullptr, nullptr, &setExternal);
    // Obtain the value of the external data.
    void \*getExternal;
    napi\_get\_value\_external(env, setExternal, &getExternal);
    // Return the obtained external data.
    napi\_value result = nullptr;
    napi\_create\_int32(env, \*(int \*)getExternal, &result);
    return result;
}

API declaration:

// index.d.ts
export const getValueExternal: () => number;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'Node-API', 'get\_value\_external:%{public}d', testNapi.getValueExternal());

## napi\_create\_symbol

Call **napi\_create\_symbol** to create a symbol. Symbol is a special data type used to indicate a unique identifier. Unlike strings or numbers, the value of a symbol is unique. Even if two symbols have the same description, they are not equal. Symbols are often used as keys for object properties to ensure property uniqueness.

CPP code:

#include "napi/native\_api.h"
#include "hilog/log.h"

static napi\_value CreateSymbol(napi\_env env, napi\_callback\_info info)
{
    napi\_value result = nullptr;
    const char \*des = "only";
    // Use napi\_create\_string\_utf8 to create a description string.
    napi\_status status = napi\_create\_string\_utf8(env, des, NAPI\_AUTO\_LENGTH, &result);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API napi\_create\_string\_utf8 failed");
        return nullptr;
    }
    napi\_value returnSymbol = nullptr;
    // Create a symbol and return it.
    status = napi\_create\_symbol(env, result, &returnSymbol);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API napi\_create\_symbol failed");
        return nullptr;
    }
    return returnSymbol;
}

API declaration:

// index.d.ts
export const createSymbol : () => symbol;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let varSymbol = testNapi.createSymbol();
hilog.info(0x0000, 'Node-API', 'createSymbol:%{public}s', typeof varSymbol);

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
