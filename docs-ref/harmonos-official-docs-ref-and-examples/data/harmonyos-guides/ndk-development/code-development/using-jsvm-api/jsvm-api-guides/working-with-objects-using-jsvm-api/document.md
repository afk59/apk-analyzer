# Working with Objects Using JSVM-API

#### Overview

JSVM-API provides APIs for basic JavaScript (JS) object operations, including creating an object, obtaining the prototype of an object, freezing or sealing an object, and checking the object type. You can use these APIs to manage JS objects.

#### Basic Concepts

You may need to define and operate objects when using JSVM-API in development. For example, define an API with an object as an input parameter, perform operations on the object, and have a result object returned. In this process, you need to ensure that the API definition is clear and compatible with the properties and methods of the object.

-   API: defines the interaction protocol between components. An API includes input parameters, output result, and possible error handling. By calling APIs, components can interact and exchange data with each other without knowing the internal implementation details.
-   Object: a composite data type that allows values of different types in an independent entity in JS. An object is a collection of properties and methods. A property is a value associated with an object, and a method is an operation that the object can perform.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetPrototype | Obtains the prototype of a JS object. |
| OH\_JSVM\_CreateObject | Creates a default JS object. |
| OH\_JSVM\_ObjectFreeze | Freezes a JS object. Once a JS object is frozen, new properties cannot be added to it, existing properties cannot be removed, the enumerability, configurability, or writability of existing properties cannot be changed, and the values of existing properties cannot be changed. |
| OH\_JSVM\_ObjectSeal | Seals a JS object. Once a JS object is sealed, new properties cannot be added to it and all existing properties are marked as unconfigurable. |
| OH\_JSVM\_Typeof | Returns the type of a JS object. |
| OH\_JSVM\_Instanceof | Checks whether an object is an instance of a constructor. |
| OH\_JSVM\_TypeTagObject | Associates the value of the **type\_tag** pointer with a JS object or an external object. |
| OH\_JSVM\_CheckObjectTypeTag | Checks whether a tag matches the tag type of an object. |
| OH\_JSVM\_CreateSymbol | Creates a symbol object based on the given descriptor. |
| OH\_JSVM\_SymbolFor | Searches for a symbol with the given key in a global (runtime-wide) symbol registry. If a match is found, the symbol will be returned. Otherwise, a symbol will be created in the registry. |
| OH\_JSVM\_CreateExternal | Creates a JS object that wraps an external pointer. |
| OH\_JSVM\_GetValueExternal | Obtains the external data pointer previously passed to **OH\_JSVM\_CreateExternal**. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following only demonstrates the C++ and ArkTS code for object management APIs.

## OH\_JSVM\_GetPrototype

Call **OH\_JSVM\_GetPrototype** to obtain the prototype of a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <fstream>
#include <string>
// Register the GetPrototype callback.
// Define OH\_JSVM\_GetPrototype.
static JSVM\_Value GetPrototype(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    JSVM\_Value result{nullptr};
    JSVM\_Status status = OH\_JSVM\_GetPrototype(env, argv\[0\], &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetPrototype fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetPrototype success");
    }
    return result;
}
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetPrototype},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the getPrototype method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getPrototype", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(const myObject = {};
    const proto = getPrototype(myObject);
    console.info(proto === Object.prototype);)JS";

Expected result:

JSVM GetPrototype success

## OH\_JSVM\_CreateObject

Call **OH\_JSVM\_CreateObject** to create a default JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <fstream>
// Define OH\_JSVM\_CreateObject.
static JSVM\_Value CreateObject(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Value object = nullptr;
    // Create an empty object.
    JSVM\_Status status = OH\_JSVM\_CreateObject(env, &object);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateObject fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateObject success");
    }
    // Set the object property.
    JSVM\_Value name = nullptr;
    // Set the property name to "name".
    OH\_JSVM\_CreateStringUtf8(env, "name", JSVM\_AUTO\_LENGTH, &name);
    JSVM\_Value value = nullptr;
    // Set the property value to "Hello from N-API!"
    OH\_JSVM\_CreateStringUtf8(env, "Hello OH\_JSVM\_CreateObject!", JSVM\_AUTO\_LENGTH, &value);
    // Set the property on the object.
    OH\_JSVM\_SetProperty(env, object, name, value);
    return object;
}
// Register the CreateObject callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateObject},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the createObject method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createObject())JS";

Expected result:

JSVM CreateObject success

## OH\_JSVM\_ObjectFreeze

Call **OH\_JSVM\_ObjectFreeze** to freeze a JS object. Once a JS object is frozen, new properties cannot be added to it, existing properties cannot be removed, the enumerability, configurability, or writability of existing properties cannot be changed, and the values of existing properties cannot be changed.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_ObjectFreeze.
static JSVM\_Value ObjectFreeze(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Accept an object passed in from JS.
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // Call OH\_JSVM\_ObjectFreeze to freeze the object passed in.
    JSVM\_Status status = OH\_JSVM\_ObjectFreeze(env, argv\[0\]);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "Test JSVM OH\_JSVM\_ObjectFreeze success");
    }
    // Check whether the properties of the frozen object can be modified.
    JSVM\_Value value = nullptr;
    OH\_JSVM\_CreateInt32(env, 111111, &value);
    OH\_JSVM\_SetNamedProperty(env, argv\[0\], "data", value);
    // Return the properties modified after the freezing to JS.
    return argv\[0\];
}
// Register the ObjectFreeze callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = ObjectFreeze},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the ObjectFreeze method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"objectFreeze", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(let obj = { data: 55, message: "hello world"};
  objectFreeze(obj))JS";

Expected result:

Test JSVM OH\_JSVM\_ObjectFreeze success

## OH\_JSVM\_ObjectSeal

Call **OH\_JSVM\_ObjectSeal** to seal a JS object. Once a JS object is sealed, new properties cannot be added to it and all existing properties are marked as unconfigurable.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_ObjectSeal.
static JSVM\_Value ObjectSeal(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Accept an object passed in from JS.
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // Call OH\_JSVM\_ObjectSeal to seal the object passed in.
    JSVM\_Status status = OH\_JSVM\_ObjectSeal(env, argv\[0\]);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "Test JSVM OH\_JSVM\_ObjectSeal success");
    }
    // Check whether the properties of the sealed object can be modified, deleted, or added.
    // Modify a property of the sealed object.
    JSVM\_Value changeValue = nullptr;
    OH\_JSVM\_CreateInt32(env, 111111, &changeValue);
    OH\_JSVM\_SetNamedProperty(env, argv\[0\], "data", changeValue);
    // Delete a property from the sealed object.
    JSVM\_Value deleteProperty = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "message", JSVM\_AUTO\_LENGTH, &deleteProperty);
    bool result = false;
    OH\_JSVM\_DeleteProperty(env, argv\[0\], deleteProperty, &result);
    if (result) {
        OH\_LOG\_INFO(LOG\_APP, "Test JSVM OH\_JSVM\_ObjectSeal failed");
    }
    // Add a property to the sealed object.
    JSVM\_Value addValue = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "addValue", JSVM\_AUTO\_LENGTH, &addValue);
    OH\_JSVM\_SetNamedProperty(env, argv\[0\], "newProperty", addValue);
    // Return the modified object to JS.
    return argv\[0\];
}
// Register the ObjectSeal callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = ObjectSeal},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the ObjectSeal method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"objectSeal", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS( let obj = { data: 55, message: "hello world"};
  objectSeal(obj))JS";

Expected result:

Test JSVM OH\_JSVM\_ObjectSeal success

## OH\_JSVM\_Typeof

Call **OH\_JSVM\_Typeof** to return the type of a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_Typeof.
static JSVM\_Value GetTypeof(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_ValueType valueType;
    OH\_JSVM\_Typeof(env, args\[0\], &valueType);
    JSVM\_Value type = nullptr;
    switch (valueType) {
        case JSVM\_UNDEFINED:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is undefined");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is undefined", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_NULL:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is null");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is null", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_BOOLEAN:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is boolean");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is boolean", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_NUMBER:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is number");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is number", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_STRING:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is string");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is string", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_SYMBOL:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is symbol");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is symbol", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_OBJECT:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is object");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is object", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_FUNCTION:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is function");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is function", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_EXTERNAL:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is external");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is external", JSVM\_AUTO\_LENGTH, &type);
            break;
        case JSVM\_BIGINT:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type is bigint");
            OH\_JSVM\_CreateStringUtf8(env, "Input type is bigint", JSVM\_AUTO\_LENGTH, &type);
            break;
        default:
            OH\_LOG\_INFO(LOG\_APP, "JSVM Input type does not match any");
            OH\_JSVM\_CreateStringUtf8(env, " ", JSVM\_AUTO\_LENGTH, &type);
            break;
    }
    return type;
}
// Register the GetTypeof callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetTypeof},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetTypeof method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getTypeof", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getTypeof(true);)JS";

Expected result:

JSVM Input type is boolean

## OH\_JSVM\_Instanceof

Call **OH\_JSVM\_Instanceof** to check whether an object is an instance of a constructor.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_Instanceof.
static JSVM\_Value InstanceOf(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_Instanceof(env, args\[0\], args\[1\], &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM InstanceOf fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM InstanceOf: %{public}d", result);
    }
    JSVM\_Value returnValue = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &returnValue);
    return returnValue;
}
// Register the InstanceOf callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = InstanceOf},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the InstanceOf method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"instanceOf", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(class Person {
        name;
        age;
        constructor(name, age) {
          this.name = name;
          this.age = age;
        }
      }
     instanceOf(new Person('Alice', 30), Person);
     ;)JS";

Expected result:

JSVM InstanceOf: 1

## OH\_JSVM\_TypeTagObject

Call **OH\_JSVM\_TypeTagObject** to associate the value of the **type\_tag** pointer with a JS object so that the object can be identified more accurately.

## OH\_JSVM\_CheckObjectTypeTag

Call **OH\_JSVM\_CheckObjectTypeTag** to check whether a tag matches the tag type of an object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#define NUMBERINT\_FOUR 4
// Define a static constant JSVM\_TypeTag array to store type tags.
static const JSVM\_TypeTag TagsData\[NUMBERINT\_FOUR\] = {
    {0x9e4b2449547061b3, 0x33999f8a6516c499},
    {0x1d55a794c53a726d, 0x43633f509f9c944e},
    {0, 0}, // Indicates the default tag or no tag.
    {0x6a971439f5b2e5d7, 0x531dc28a7e5317c0},
};
// Define OH\_JSVM\_TypeTagObject.
static JSVM\_Value SetTypeTagToObject(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index number and convert it to JSVM\_Value.
    int32\_t index = 0;
    OH\_JSVM\_GetValueInt32(env, args\[1\], &index);
    // Set the type tag for the parameter (object).
    JSVM\_Status status = OH\_JSVM\_TypeTagObject(env, args\[0\], &TagsData\[index\]);
    // Convert the bool value to JSVM\_Value and return it.
    JSVM\_Value result = nullptr;
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM SetTypeTagToObject fail");
        OH\_JSVM\_GetBoolean(env, false, &result);
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM SetTypeTagToObject success");
        OH\_JSVM\_GetBoolean(env, true, &result);
    }
    return result;
}
// Define OH\_JSVM\_CheckObjectTypeTag.
static JSVM\_Value CheckObjectTypeTag(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index number and convert it to JSVM\_Value.
    int32\_t index = 0;
    OH\_JSVM\_GetValueInt32(env, args\[1\], &index);
    // Check the type tag of the object.
    bool checkResult = false;
    JSVM\_Status status = OH\_JSVM\_CheckObjectTypeTag(env, args\[0\], &TagsData\[index\], &checkResult);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CheckObjectTypeTag fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CheckObjectTypeTag:%{public}d", checkResult);
    }
    // Convert the bool value to JSVM\_Value and return it.
    JSVM\_Value checked = nullptr;
    OH\_JSVM\_GetBoolean(env, checkResult, &checked);
    return checked;
}
// Registers the SetTypeTagToObject and CheckObjectTypeTag callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = SetTypeTagToObject},
    {.data = nullptr, .callback = CheckObjectTypeTag},
};
static JSVM\_CallbackStruct \*method = param;
// Aliases for the SetTypeTagToObject and CheckObjectTypeTag methods to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"setTypeTagToObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"checkObjectTypeTag", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(
         class Obj {
           data;
           message;
         }
         let obj= { data: 0, message: "hello world"};
         setTypeTagToObject(obj, 0);
         checkObjectTypeTag(obj,0);)JS";

Expected result:

JSVM SetTypeTagToObject success
JSVM CheckObjectTypeTag:1

## OH\_JSVM\_CreateExternal

Call **OH\_JSVM\_CreateExternal** to create a JS object that wraps an external pointer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BvDG-YrZRh2__F-g_tG19g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062133Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26C243B938FC5E03394513DCCE5DAC47DA73A7692C48E9635F18B6C2CEEB2D7E)

When a JS object is garbage-collected, the content pointed to by the wrapped external pointer is not directly managed by GC. Only the function corresponding to the third input parameter (if it is not nullptr) is called.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <fstream>
// Define OH\_JSVM\_CreateExternal.
static JSVM\_Value CreateExternal(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t dataSize = 10;
    void \*data = malloc(dataSize);
    if (data == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM Failed to malloc.");
        return nullptr;
    }
    memset(data, 0, dataSize);
    const char\* testStr = "test";
    JSVM\_Value external = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateExternal(
        env, data, \[\](JSVM\_Env env, void \*data, void \*hint) {free(data);}, (void \*)testStr, &external);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM Failed to create external data, status:%{public}d.", status);
        free(data);
        data = nullptr;
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateExternal success");
    }
    return external;
}
// Register the CreateExternal callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateExternal},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CreateExternal method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createExternal", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createExternal())JS";

Expected result:

JSVM CreateExternal success

## OH\_JSVM\_GetValueExternal

Call **OH\_JSVM\_CreateExternal** to create a JS object that wraps a custom C/C++ object, and call **OH\_JSVM\_GetValueExternal** to obtain the pointer to the external object wrapped by **OH\_JSVM\_CreateExternal**.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetValueExternal.
static JSVM\_Value GetValueExternal(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    static int data = 0x12345;
    JSVM\_Value externalValue = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateExternal(env, (void\*)&data, nullptr, nullptr, &externalValue);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CreateExternal fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CreateExternal success");
    }
    void \*data\_value;
    status = OH\_JSVM\_GetValueExternal(env, externalValue, &data\_value);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetValueExternal fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetValueExternal success");
    }
    // Convert the sign bit into a value of int type and pass it.
    JSVM\_Value returnValue = nullptr;
    int retData = \*static\_cast<int \*>(data\_value);
    OH\_JSVM\_CreateInt32(env, retData, &returnValue);
    return returnValue;
}
// Register the GetValueExternal callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetValueExternal},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetValueExternal method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getValueExternal", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(getValueExternal())JS";

Expected result:

JSVM OH\_JSVM\_CreateExternal success
JSVM GetValueExternal success

## OH\_JSVM\_CreateSymbol

Call **OH\_JSVM\_CreateSymbol** to create a symbol. Symbol is a special data type used to indicate a unique identifier. Unlike strings or numbers, the value of a symbol is unique. Even if two symbols have the same description, they are not equal. Symbols are often used as keys for object properties to ensure property uniqueness.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CreateSymbol.
static JSVM\_Value CreateSymbol(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Value result = nullptr;
    const char \*des = "only";
    OH\_JSVM\_CreateStringUtf8(env, des, JSVM\_AUTO\_LENGTH, &result);
    JSVM\_Value returnSymbol = nullptr;
    OH\_JSVM\_CreateSymbol(env, result, &returnSymbol);
    JSVM\_ValueType valuetypeSymbol;
    OH\_JSVM\_Typeof(env, returnSymbol, &valuetypeSymbol);
    if (valuetypeSymbol == JSVM\_SYMBOL) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateSymbol Success");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateSymbol fail");
    }
    return returnSymbol;
}
// Register the CreateSymbol callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateSymbol},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the CreateSymbol method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createSymbol", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(createSymbol())JS";

Expected result:

JSVM CreateSymbol Success

## OH\_JSVM\_SymbolFor

Call **OH\_JSVM\_SymbolFor** to search for a symbol with the given key in a global (runtime-wide) symbol registry. If a match is found, the symbol will be returned. Otherwise, a symbol will be created in the Registry.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define a constant to store the maximum length of a string.
static const int MAX\_BUFFER\_SIZE = 128;
// Define OH\_JSVM\_SymbolFor.
static JSVM\_Value SymbolFor(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Value description = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "test\_demo", 9, &description);
    char buffer\[MAX\_BUFFER\_SIZE\];
    size\_t bufferSize = MAX\_BUFFER\_SIZE;
    size\_t copied = 0;
    OH\_JSVM\_GetValueStringUtf8(env, description, buffer, bufferSize, &copied);
    JSVM\_Value symbol = nullptr;
    OH\_JSVM\_CreateSymbol(env, description, &symbol);
    JSVM\_Value result\_symbol = nullptr;
    JSVM\_Status status = OH\_JSVM\_SymbolFor(env, buffer, copied, &result\_symbol);
    JSVM\_ValueType valuetypeSymbol;
    OH\_JSVM\_Typeof(env, result\_symbol, &valuetypeSymbol);
    if (valuetypeSymbol == JSVM\_SYMBOL && status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_SymbolFor success");
    }
    // Return the result.
    return result\_symbol;
}
// Register the SymbolFor callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = SymbolFor},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the SymbolFor method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"symbolFor", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char\* srcCallNative = R"JS(symbolFor())JS";

Expected result:

JSVM OH\_JSVM\_SymbolFor success
