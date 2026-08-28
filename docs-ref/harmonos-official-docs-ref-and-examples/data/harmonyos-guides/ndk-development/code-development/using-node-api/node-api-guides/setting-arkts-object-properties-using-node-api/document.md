# Setting ArkTS Object Properties Using Node-API

#### Introduction

Node-API provides APIs for obtaining and setting properties of ArkTS objects in C/C++ to implement more complex functionalities and logic.

#### Basic Concepts

Before working with ArkTS objects using Node-API, you need to understand the following concepts:

-   Object: a composite data type that allows values of different types in an independent entity in ArkTS. An object is a collection of properties and methods. A property is a value associated with the object, and a method is an operation that the object can perform.
-   Property: a feature, in the key-value format, of an object in ArkTS. Each property has a name (key or identifier) and a value. The property value can be of any data type, including the basic type, object, and function.
-   Enumerable property: a property in ArkTS with **enumerable** set to **true**. An enumerable property can be traversed by **for...in**.
-   Own property: a property defined for an object rather than inherited from the prototype chain.

#### Available APIs

The following table lists the APIs for manipulating ArkTS object properties.

| API | Description |
| :-- | :-- |
| napi\_get\_property\_names | Obtains the names of the enumerable properties of an object in an array of strings. |
| napi\_set\_property | Adds a property to an object or modifies a property value of an object. |
| napi\_get\_property | Obtains the requested property of an object and passes it to another function for processing. |
| napi\_has\_property | Checks whether an object has the specified property. This can prevent the exception or error caused by access to a property that does not exist. |
| napi\_delete\_property | Deletes a property from an ArkTS object. |
| napi\_has\_own\_property | Checks whether an object has the specified own property. |
| napi\_set\_named\_property | Sets a property with the specified name for an ArkTS object. |
| napi\_get\_named\_property | Obtains the value of a property in an ArkTS object. |
| napi\_has\_named\_property | Checks whether an ArkTS object has the property with the specified name. |
| napi\_define\_properties | Defines multiple properties for an ArkTS object. |
| napi\_get\_all\_property\_names | Obtains the names of all properties of an ArkTS object. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in related APIs.

## napi\_get\_property\_names

Call **napi\_get\_property\_names** to obtain the names of the enumerable properties of an object in an array of strings.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetPropertyNames(napi\_env env, napi\_callback\_info info)
{
    // Parse the ArkTS input parameters.
    size\_t argc = 1;
    napi\_value args\[1\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the names of all the enumerable properties of the object in the form of a string array and output the string array in result.
    napi\_value result;
    napi\_status status = napi\_get\_property\_names(env, args\[0\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_get\_property\_names fail");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const getPropertyNames: (obj: Object) => Array<string> | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = { data: 0, message: "hello world" };
  let propertyNames = testNapi.getPropertyNames(obj);
  if (Array.isArray(propertyNames) && propertyNames.length > 0) {
    hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_property\_names: %{public}s', propertyNames\[0\]);
    hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_property\_names: %{public}s', propertyNames\[1\]);
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_get\_property\_names error: %{public}s', error.message);
}

## napi\_set\_property

Call **napi\_set\_property** to set a property for an object.

CPP code:

#include "napi/native\_api.h"

static constexpr int INT\_ARG\_2 = 2; // Input parameter index.

static napi\_value SetProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS. The first parameter specifies the object, the second parameter specifies the property name, and the third parameter specifies the property value to set.
    size\_t argc = 3;
    napi\_value args\[3\] = { nullptr };
    napi\_status status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_get\_cb\_info fail");
        return nullptr;
    }
    // Call napi\_set\_property to set the property name and value to the object. If the operation fails, throw an error.
    status = napi\_set\_property(env, args\[0\], args\[1\], args\[INT\_ARG\_2\]);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_set\_property fail");
        return nullptr;
    }
    // Return the object that is successfully set.
    return args\[0\];
}

API declaration:

// index.d.ts
export const setProperty: (obj: Object, key: String, value: string) => Object | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = { data: 0, message: "hello world" };
  let result = testNapi.setProperty(obj, "code", "hi");
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_set\_property: %{public}s', JSON.stringify(result));
} catch (error) {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_set\_property error: %{public}s', error.message);
}

## napi\_get\_property

Call **napi\_get\_property** to obtain the value of the specified property in an object.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // The first parameter specifies the target object, and the second specifies the property name. Call napi\_get\_property to obtain the value of the property.
    napi\_value result;
    napi\_status status = napi\_get\_property(env, args\[0\], args\[1\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_get\_property fail");
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const getProperty: (obj: Object, key: string) => string | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = { data: 0, message: "hello world" };
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_property: %{public}s', testNapi.getProperty(obj, "message"));
} catch (error) {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_property error: %{public}s', error.message);
}

## napi\_has\_property

Call **napi\_has\_property** to check whether an object has the specified property. This can prevent the exception or error caused by access to a property that does not exist.

CPP code:

#include "napi/native\_api.h"

static napi\_value HasProperty(napi\_env env, napi\_callback\_info info)
{
    // Pass in two parameters from ArkTS. The first parameter specifies the target object, and the second parameter specifies the property to check.
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Pass the parameters to napi\_has\_property. If the API is successfully called, convert the result to napi\_value and return napi\_value. Otherwise, throw an error.
    bool result;
    napi\_status status = napi\_has\_property(env, args\[0\], args\[1\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_has\_property fail");
        return nullptr;
    }

    // If the property exists in the object, output true, convert the result to napi\_value, and return napi\_value.
    napi\_value returnResult;
    napi\_get\_boolean(env, result, &returnResult);
    return returnResult;
}

API declaration:

// index.d.ts
export const hasProperty: (obj: Object, key: number | string) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = { data: 0, message: "hello world" };
  let resultFalse = testNapi.hasProperty(obj, 0);
  let resultTrue = testNapi.hasProperty(obj, "data");
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_property: %{public}s', JSON.stringify(resultFalse));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_property: %{public}s', JSON.stringify(resultTrue));
} catch (error) {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_property error: %{public}s', error.message);
}

## napi\_delete\_property

Call **napi\_delete\_property** to delete the property specified by **key** from an object.

If the object is non-extensible or the property is not configurable, the property cannot be deleted.

CPP code:

#include "napi/native\_api.h"

// Delete the specified property from the object and return a bool value indicating whether the deletion is successful.
static napi\_value DeleteProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    napi\_valuetype valueType;
    napi\_typeof(env, args\[0\], &valueType);
    if (valueType != napi\_object) {
        napi\_throw\_error(env, nullptr, "Expects an object as argument.");
        return nullptr;
    }
    // Delete the specified property and store the operation result in result.
    bool result = false;
    napi\_status status = napi\_delete\_property(env, args\[0\], args\[1\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_delete\_property failed");
        return nullptr;
    }
    // Convert the bool value to napi\_value and return it.
    napi\_value ret;
    napi\_get\_boolean(env, result, &ret);
    return ret;
}

API declaration:

// index.d.ts
export const deleteProperty: (obj: Object, key:string) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

class Obj {
  first: number = 0;
}
let obj: Obj = { first: 1 };
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_delete\_property first: %{public}s', testNapi.deleteProperty(obj, 'first'));
// Set the new property to unconfigurable.
// The Object.defineProperty method is not supported in DevEco Studio 4.1.0.400 or later. It must be used in TS.
Object.defineProperty(obj, 'config', {
  configurable: false,
  value: "value"
})
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_delete\_property config: %{public}s', testNapi.deleteProperty(obj, 'config'));

## napi\_has\_own\_property

Call **napi\_has\_own\_property** to check whether an ArkTS object has its own property.

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiHasOwnProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Check whether the first parameter is an object.
    napi\_valuetype valueTypeObj;
    napi\_typeof(env, args\[0\], &valueTypeObj);
    if (valueTypeObj != napi\_object) {
        napi\_throw\_error(env, nullptr, "First argument must be an object.");
        return nullptr;
    }
    // Check whether the second parameter is a string.
    napi\_valuetype valuetypeStr;
    napi\_typeof(env, args\[1\], &valuetypeStr);
    if (valuetypeStr != napi\_string) {
        napi\_throw\_error(env, nullptr, "Second argument must be a string.");
        return nullptr;
    }
    // Check whether the object has the specified property and returns the result in hasProperty.
    bool hasProperty;
    napi\_status status = napi\_has\_own\_property(env, args\[0\], args\[1\], &hasProperty);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_has\_own\_property failed");
        return nullptr;
    }
    // Convert the bool value to napi\_value and return it.
    napi\_value result;
    napi\_get\_boolean(env, hasProperty, &result);
    return result;
}

API declaration:

// index.d.ts
export const napiHasOwnProperty: (obj: Object, key:string) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let myObj = { 'myProperty': 1 };
let inheritedObj = { 'inheritedProperty': 2 };
// The Object.setPrototypeOf method is not supported in DevEco Studio 4.1.0.400 or later. It must be used in TS.
Object.setPrototypeOf(myObj, inheritedObj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_own\_property my: %{public}s', testNapi.napiHasOwnProperty(myObj, 'myProperty'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_own\_property inherited: %{public}s', testNapi.napiHasOwnProperty(myObj, 'inheritedProperty'));

## napi\_set\_named\_property

Call **napi\_set\_named\_property** to set a property for an ArkTS object.

CPP code:

#include "napi/native\_api.h"
#include "hilog/log.h"

static napi\_value NapiSetNamedProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameter passed from ArkTS.
    size\_t argc = 1;
    napi\_value str;
    const int32\_t strLength = 32;
    char strKey\[strLength\] = "";
    napi\_get\_cb\_info(env, info, &argc, &str, nullptr, nullptr);
    // Obtain the string passed in and store it in strKey.
    size\_t keyLength;
    napi\_status status = napi\_get\_value\_string\_utf8(env, str, strKey, strLength, &keyLength);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_value\_string\_utf8 failed");
        return nullptr;
    }
    // Create an object.
    napi\_value newObj;
    napi\_create\_object(env, &newObj);
    // Set the property value to 1234.
    int32\_t value = 1234;
    napi\_value numValue;
    napi\_create\_int32(env, value, &numValue);
    // Associate the integer value with the property name.
    status = napi\_set\_named\_property(env, newObj, strKey, numValue);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_set\_named\_property failed");
        return nullptr;
    }
    // Return the newObj object with the specified property set.
    return newObj;
}

API declaration:

// index.d.ts
export const napiSetNamedProperty: (key: string) => Object | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

let obj = testNapi.napiSetNamedProperty('myProperty');
let objAsString = JSON.stringify(obj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_set\_named\_property: %{public}s', objAsString);

## napi\_get\_named\_property

Call **napi\_get\_named\_property** to obtain the value of the specified property from an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiGetNamedProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr };
    const int32\_t strLength = 32;
    char strKey\[strLength\] = "";
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the name of the property to obtain.
    size\_t keyLength;
    napi\_get\_value\_string\_utf8(env, args\[1\], strKey, strLength, &keyLength);
    // Obtain the value of the property and store it in result.
    napi\_value result;
    napi\_status status = napi\_get\_named\_property(env, args\[0\], strKey, &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_get\_named\_property failed");
        return nullptr;
    }
    // Return result.
    return result;
}

API declaration:

// index.d.ts
export const napiGetNamedProperty: (obj: Object, key: string) => boolean | number | string | Object | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

interface NestedObj {
  nestedStr: string;
  nestedNum: number;
}
class Obj {
  str: string = "";
  num: number = 0;
  bol: boolean = false;
  nestedObj: NestedObj = { nestedStr: "", nestedNum: 0 };
}
let obj: Obj = {str: "bar", num: 42, bol: true,
  nestedObj: { nestedStr: "nestedValue", nestedNum: 123 }};
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_named\_property : %{public}s', testNapi.napiGetNamedProperty(obj, 'str'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_named\_property : %{public}d', testNapi.napiGetNamedProperty(obj, 'num'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_named\_property : %{public}s', testNapi.napiGetNamedProperty(obj, 'bol'));
let nestedObj = testNapi.napiGetNamedProperty(obj, 'nestedObj');
let objAsString = JSON.stringify(nestedObj);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_named\_property : %{public}s', objAsString);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_named\_property : %{public}s', testNapi.napiGetNamedProperty(obj, 'null'));

## napi\_has\_named\_property

Call **napi\_has\_named\_property** to check whether an ArkTS object contains the specified property.

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiHasNamedProperty(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = { nullptr };
    const int32\_t strLength = 32;
    char strKey\[strLength\] = "";
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the property name.
    size\_t keyLength;
    napi\_get\_value\_string\_utf8(env, args\[1\], strKey, strLength, &keyLength);
    // Check whether the object has the specified property and stores the result in hasProperty.
    bool hasProperty = false;
    napi\_status status = napi\_has\_named\_property(env, args\[0\], strKey, &hasProperty);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_has\_named\_property failed");
        return nullptr;
    }
    // Convert the bool value to napi\_value and return it.
    napi\_value result;
    napi\_get\_boolean(env, hasProperty, &result);
    return result;
}

API declaration:

// index.d.ts
export const napiHasNamedProperty: (obj: Object, key:string) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

interface NestedObj {
  nestedStr: string;
  nestedNum: number;
}
class Obj {
  str: string = "";
  num: number = 0;
  bol: boolean = false;
  nestedObj: NestedObj = { nestedStr: "", nestedNum: 0 };
}
let obj: Obj = {str: "bar", num: 42, bol: true,
  nestedObj: { nestedStr: "nestedValue", nestedNum: 123 }};
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_named\_property : %{public}s', testNapi.napiHasNamedProperty(obj, 'str'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_named\_property : %{public}s', testNapi.napiHasNamedProperty(obj, 'nestedStr'));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_named\_property : %{public}s', testNapi.napiHasNamedProperty(obj, 'bol'));

## napi\_define\_properties

Call **napi\_define\_properties** to set object properties.

CPP code:

#include <string>
#include "napi/native\_api.h"

static napi\_value DefineMethodPropertiesExample(napi\_env env, napi\_callback\_info info)
{
    // Create a property value of the int32 type.
    int32\_t propValue = 26;
    napi\_value returnValue = nullptr;
    napi\_create\_int32(env, propValue, &returnValue);
    return returnValue;
}
// Define a getter callback.
static napi\_value GetterCallback(napi\_env env, napi\_callback\_info info)
{
    napi\_value result;
    const char \*str = u8"World!";
    size\_t length = strlen(str);
    // Create property values.
    napi\_create\_string\_utf8(env, str, length, &result);
    return result;
}

// Define a setter callback.
static napi\_value SetterCallback(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed to setter.
    size\_t argc = 1;
    napi\_value argv\[1\] = { nullptr };
    napi\_value result;
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    size\_t length = 0;
    napi\_get\_value\_string\_utf8(env, argv\[0\], nullptr, 0, &length);
    char\* buf = new char\[length + 1\];
    std::memset(buf, 0, length + 1);
    napi\_get\_value\_string\_utf8(env, argv\[0\], buf, length + 1, &length);
    napi\_create\_string\_utf8(env, buf, length, &result);
    delete\[\] buf;
    return result;
}
static napi\_value DefineMethodProperties(napi\_env env, napi\_callback\_info info)
{
    napi\_value obj;
    napi\_create\_object(env, &obj);
    // Define the defineMethodPropertiesExample function for the obj object, define a variable in the defineMethodPropertiesExample function, and return the variable. When the obj object is called, the defineMethodPropertiesExample will be called.
    napi\_property\_descriptor descriptor\[\] = {
        {"defineMethodPropertiesExample", nullptr, DefineMethodPropertiesExample, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, obj, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor);
    return obj;
}
static napi\_value DefineStringProperties(napi\_env env, napi\_callback\_info info)
{
    napi\_value obj;
    napi\_create\_object(env, &obj);
    // Create a property value of the string type.
    napi\_value string\_value;
    napi\_create\_string\_utf8(env, "Hello!", NAPI\_AUTO\_LENGTH, &string\_value);
    napi\_property\_descriptor descriptor\[\] = {
        {"defineStringPropertiesExample", nullptr, nullptr, nullptr, nullptr, string\_value, napi\_default, nullptr}};
    napi\_define\_properties(env, obj, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor);
    return obj;
}

static napi\_value CreateStringWithGetterSetter(napi\_env env, napi\_callback\_info info)
{
    napi\_value obj;
    napi\_create\_object(env, &obj);
    // Define the getter function.
    napi\_value getterFn;
    napi\_create\_function(env, nullptr, 0, GetterCallback, nullptr, &getterFn);
    napi\_set\_named\_property(env, obj, "getterCallback", getterFn);
    // Define the setter function.
    napi\_value setterFn;
    napi\_create\_function(env, nullptr, 0, SetterCallback, nullptr, &setterFn);
    napi\_set\_named\_property(env, obj, "setterCallback", setterFn);
    // Define properties with getter and setter.
    napi\_property\_descriptor desc = {"defineGetterSetter", nullptr, nullptr, GetterCallback, SetterCallback, nullptr, napi\_enumerable, nullptr};
    napi\_define\_properties(env, obj, 1, &desc);
    return obj;
}

API declaration:

// index.d.ts
export class DefineMethodObj {
  defineMethodPropertiesExample: Function;
}
export class DefineStringObj {
  defineStringPropertiesExample: string;
}
export class DefineGetterSetterObj {
  getterCallback: Function;
  setterCallback: Function;
}
export const defineMethodProperties: () => DefineMethodObj;
export const defineStringProperties: () => DefineStringObj;
export const createStringWithGetterSetter: () => DefineGetterSetterObj;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

// Define a property of the method type.
hilog.info(0x0000, 'testTag', 'Test Node-API define\_method\_properties:%{public}d', testNapi.defineMethodProperties()
  .defineMethodPropertiesExample());
// Define a property of the string type.
hilog.info(0x0000, 'testTag', 'Test Node-API define\_string\_properties::%{public}s ', testNapi.defineStringProperties()
  .defineStringPropertiesExample);
// getter and setter.
hilog.info(0x0000, 'testTag', 'Test Node-API get::%{public}s ', testNapi.createStringWithGetterSetter()
  .getterCallback());
hilog.info(0x0000, 'testTag', 'Test Node-API setter::%{public}s ', testNapi.createStringWithGetterSetter()
  .setterCallback('set data'));

## napi\_get\_all\_property\_names

Call **napi\_get\_all\_property\_names** to obtain all property names in an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetAllPropertyNames(napi\_env env, napi\_callback\_info info)
{
    // obtain the parameter.
    size\_t argc = 1;
    napi\_value args\[1\] = { nullptr };
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Obtain all property names of the given object.
    napi\_value result;
    napi\_status status = napi\_get\_all\_property\_names(env, args\[0\], napi\_key\_own\_only, napi\_key\_writable,
                                                     napi\_key\_numbers\_to\_strings, &result);
    // If the operation fails, throw an error.
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_get\_all\_property\_names fail");
        return nullptr;
    }

    return result;
}

API declaration:

// index.d.ts
export const getAllPropertyNames : (obj: Object) => Array<string> | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  class Obj {
    data: number = 0
    message: string = ""
  }
  let obj: Obj = { data: 0, message: "hello world" };
  let propertyNames = testNapi.getAllPropertyNames(obj);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_all\_property\_names: %{public}s', JSON.stringify(propertyNames));
} catch (error) {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_all\_property\_names error: %{public}s', error.message);
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
