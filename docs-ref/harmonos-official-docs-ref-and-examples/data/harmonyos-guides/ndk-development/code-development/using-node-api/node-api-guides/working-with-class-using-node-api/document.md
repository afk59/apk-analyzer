# Working with Class Using Node-API

#### Introduction

Node-API provides APIs for managing ArkTS classes, for example, defining an ArkTS class and creating an ArkTS instance, in C/C++.

#### Basic Concepts

To begin with, it is important to understand the following basic concepts:

-   Class: a template used to create an object. It provides a way to define object properties and methods in a structured manner. Classes in ArkTS are based on prototypes and added with unique syntax and semantics.
-   Instance: an object created from a class. A class defines the structure and behavior of an object, and an instance is a specific representation of a class. Instantiating a class allows access to the properties and methods defined in the class. Each instance has its own property values.
-   Prototype: ArkTS also employs classes to implement inheritance across types. Defined in the early EcmaScript specifications, the prototype concept is used to achieve object inheritance via prototype chains. For details about the prototype concept, see [EcmaScript Language Specification](https://262.ecma-international.org/#sec-terms-and-definitions-prototype).

#### Available APIs

The following table lists the APIs for manipulating ArkTS classes.

| API | Description |
| :-- | :-- |
| napi\_new\_instance | Creates an instance based on the given constructor. |
| napi\_get\_new\_target | Obtains the **new.target** of the constructor call. |
| napi\_define\_class | Defines an ArkTS class corresponding to the C/C++ class. This API binds an ArkTS class and a C/C++ class. |
| napi\_wrap | Wraps a native object into an ArkTS object. This API allows the methods and properties of a native object to be called from ArkTS. |
| napi\_unwrap | Unwraps the native object from an ArkTS object. |
| napi\_remove\_wrap | Removes the wrapping after the native object is unwrapped from an ArkTS object. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the class-related APIs.

## napi\_new\_instance

Call **napi\_new\_instance** to create an ArkTS instance with the given constructor. This API returns an instance that can be called from ArkTS.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9IjOS6wRR6iXH5NqKirKhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=647271241D75DDE24D23212FE672BE14ED5F93690BF88B45CA93D0DB3CE90B25)

If **constructor** is not of the function type, **napi\_function\_expected** will be returned.

CPP code:

// napi\_new\_instance
static napi\_value NewInstance(napi\_env env, napi\_callback\_info info)
{
    // Pass in and parse parameters. The first parameter is the constructor, and the second parameter is the parameters of the constructor.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_new\_instance to create an instance and return the instance created.
    napi\_value result = nullptr;
    napi\_new\_instance(env, args\[0\], 1, &args\[1\], &result);
    return result;
}

API declaration:

export const newInstance: (obj: Object, param: string) => Object; // napi\_new\_instance

ArkTS code:

class Fruit {
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}

// napi\_new\_instance
// Call the function and use the variable obj to hold the instance created.
let obj = testNapi.newInstance(Fruit, 'test');
// Print the information about the object obj.
hilog.info(0x0000, 'Node-API', 'napi\_new\_instance %{public}s', JSON.stringify(obj));

## napi\_get\_new\_target

Call **napi\_get\_new\_target** to obtain **new.target** of a constructor. In ArkTS, **new.target** is a meta property used to determine whether a constructor was called using the **new** operator.

For more information, see:

[Wrapping a Native Object in an ArkTS Object](../../typical-node-api-use-cases/wrapping-a-native-object-in-an-arkts-object/document.md)

## napi\_define\_class

Call **napi\_define\_class** to define an ArkTS class. This API creates an ArkTS class and associates the methods and properties of the ArkTS class with those of a C/C++ class.

For more information, see:

[Wrapping a Native Object in an ArkTS Object](../../typical-node-api-use-cases/wrapping-a-native-object-in-an-arkts-object/document.md)

## napi\_wrap

Call **napi\_wrap** to wrap a native instance in an ArkTS object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/LMvi3vTjTAWzgcTUs5yuvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C75FC71B406054F7F2895E40E29E73A70D8FF15D9AB860CE27B2BA4728EC98C1)

If **js\_object** is not of the object or function type, **napi\_object\_expected** will be returned.

## napi\_unwrap

Call **napi\_unwrap** to obtain the data pointer wrapped in an object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/UvUiPXRfStir3Lvh4boBhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2DEC06C7EEFB052C433425B2B20BCFA9F6129600E2EC7707FD5D00CFC72FD8E)

If **js\_object** is not of the object or function type, **napi\_object\_expected** will be returned.

## napi\_remove\_wrap

Call **napi\_remove\_wrap** to remove the wrapping after a native instance is unwrapped from an ArkTS object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Zqpd4zXQTca0PgBk1MZSBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA8FAD180D835D41A52BCEF5BB0A1B28517B5B4EF292D9E041BB36C81716A532)

If **js\_object** is not of the object or function type, **napi\_object\_expected** will be returned.

CPP code:

struct Object {
    std::string name;
    int32\_t age;
};

static void DerefItem(napi\_env env, void \*data, void \*hint)
{
    // Optional native callback, which is used to release the native instance when the ArkTS object is garbage-collected.
    OH\_LOG\_INFO(LOG\_APP, "Node-API DerefItem");
    Object \*obj = reinterpret\_cast<Object \*>(data);
    if (obj != nullptr) {
        delete obj;
    }
}

// napi\_wrap
static napi\_value Wrap(napi\_env env, napi\_callback\_info info)
{
    OH\_LOG\_INFO(LOG\_APP, "Node-API wrap");
    // Initialize the native object.
    struct Object \*obj = new struct Object();
    obj->name = "liLei";
    obj->age = INT\_ARG\_18;
    size\_t argc = 1;
    napi\_value toWrap;
    // Call napi\_wrap to wrap the native object in an ArkTS object.
    napi\_status status\_cb = napi\_get\_cb\_info(env, info, &argc, &toWrap, NULL, NULL);
    if (status\_cb != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed");
        delete obj;
        return nullptr;
    }
    napi\_status status = napi\_wrap(env, toWrap, reinterpret\_cast<void \*>(obj), DerefItem, NULL, NULL);
    if (status != napi\_ok) {
        // Proactively release the memory.
        delete obj;
    }

    return toWrap;
}

// napi\_remove\_wrap
static napi\_value RemoveWrap(napi\_env env, napi\_callback\_info info)
{
    OH\_LOG\_INFO(LOG\_APP, "Node-API removeWrap");
    size\_t argc = 1;
    napi\_value wrapped = nullptr;
    void \*data = nullptr;
    // Call napi\_remove\_wrap to remove the wrapping.
    napi\_get\_cb\_info(env, info, &argc, &wrapped, nullptr, nullptr);
    napi\_status status = napi\_remove\_wrap(env, wrapped, &data);
    if (status != napi\_ok || data == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API napi\_remove\_wrap failed or data is nullptr");
        return nullptr;
    }

    return nullptr;
}

// napi\_unwrap
static napi\_value UnWrap(napi\_env env, napi\_callback\_info info)
{
    OH\_LOG\_INFO(LOG\_APP, "Node-API unWrap");
    size\_t argc = 1;
    napi\_value wrapped = nullptr;
    napi\_get\_cb\_info(env, info, &argc, &wrapped, nullptr, nullptr);
    // Call napi\_unwrap to retrieve the data from the ArkTS object and print the data.
    struct Object \*data = nullptr;
    napi\_status status = napi\_unwrap(env, wrapped, reinterpret\_cast<void \*\*>(&data));
    if (status != napi\_ok || data == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API napi\_unwrap failed or data is nullptr");
        return nullptr;
    }
    OH\_LOG\_INFO(LOG\_APP, "Node-API name: %{public}s", data->name.c\_str());
    OH\_LOG\_INFO(LOG\_APP, "Node-API age: %{public}d", data->age);
    return nullptr;
}

API declaration:

export const wrap: (obj: Object) => Object; // napi\_wrap

export const unWrap: (obj: Object) => void; // napi\_unwrap

export const removeWrap: (obj: Object) => void; // napi\_remove\_wrap

ArkTS code:

try {
  class Obj {
  }

  let obj: Obj = {};
  testNapi.wrap(obj); // napi\_wrap
  testNapi.unWrap(obj); // napi\_unwrap
  testNapi.removeWrap(obj); // napi\_remove\_wrap
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API error: %{public}s', error.message);
  // ...
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
