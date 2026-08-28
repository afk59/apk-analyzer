# Using Node-API Extension APIs

#### Introduction

The Node-API [extension APIs](../../node-api-data-types-and-apis/document.md#extended-capabilities) extend Node-API functionalities and allow you to create custom ArkTS objects, which enable more flexible interaction between ArkTS and C/C++.

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the Node-API extension APIs.

The following header files are required for the C++ code:

#include "napi/native\_api.h"
#include <bits/alltypes.h>
#include <mutex>
#include <unordered\_set>
#include <uv.h>
#include "hilog/log.h"

The following modules are required for the ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
import { taskpool } from '@kit.ArkTS';

#### Module Loading

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_load\_module | Loads an .abc file as a module. This API returns the namespace of the module. You can use it for the applications that need to dynamically load modules or resources in runtime. |
| napi\_load\_module\_with\_info | Loads a module. After the module is loaded, you can use **napi\_get\_property** to obtain the variables exported by the module or use **napi\_get\_named\_property** to obtain the functions exported by the module. The **napi\_load\_module\_with\_info** API can be used in a [newly created ArkTS runtime environment](../../typical-node-api-use-cases/creating-an-arkts-runtime-environment-using-node-api/document.md). |
| napi\_module\_register | Registers a native module. Sometimes, you may need to implement certain functionalities using Node-API for better performance. You can use **napi\_module\_register** to customize the functionalities implemented using Node-API as a module and register it with ArkTS. This can improve the overall performance. |

## Example

**napi\_load\_module**

Call **napi\_load\_module** to [load a module in the main thread](../../typical-node-api-use-cases/loading-a-module-in-the-main-thread-using-node-api/document.md).

**napi\_load\_module\_with\_info**

Call **napi\_load\_module\_with\_info** to [load a module](../../typical-node-api-use-cases/loading-a-module-using-node-api/document.md).

**napi\_module\_register**

Call **napi\_module\_register** to register a custom module, which is implemented by using Node-API, with the ArkTS environment.

CPP code:

#include "napi/native\_api.h"

// This module is a Node-API callback function.
static napi\_value Add(napi\_env env, napi\_callback\_info info)
{
    // Obtain the two parameters passed in.
    size\_t requireArgc = 2;
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);

    // Convert the parameter of the napi\_value type to the double type.
    double valueLeft;
    double valueRight;
    napi\_get\_value\_double(env, args\[0\], &valueLeft);
    napi\_get\_value\_double(env, args\[1\], &valueRight);

    // Add up the converted double values, convert the sum into napi\_value, and return the result to ArkTS.
    napi\_value sum;
    napi\_create\_double(env, valueLeft + valueRight, &sum);

    return sum;
}

// Call the C++ Init() function to initialize the addon, which associates the functions or properties in ArkTS with those in C++.
EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    // Use the napi\_property\_descriptor struct to define the properties to be exported and used in the Node-API module. napi\_define\_properties associates ArkTS properties with C++ functions so that they can be accessed and called from ArkTS.
    napi\_property\_descriptor desc\[\] = {
        { "add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr }
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

// The addon initialization is defined in a struct named demoModule, which contains the basic module information, such as the version number and registered functions.
static napi\_module demoModule = {
    .nm\_version =1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

// In the RegisterEntryModule function, the napi\_module\_register function is used to register and export the addon.
extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

API declaration:

export const add: (a: number, b: number) => number; // Module loading.

ArkTS code:

hilog.info(0x0000, 'testTag', 'Test Node-API 2 + 3 = %{public}d', testNapi.add(2, 3));

#### ArkTS Object Operations

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_create\_object\_with\_properties | Creates an ArkTS object with the given **napi\_property\_descriptor** in a native module. The key in **napi\_property\_descriptor** must be a string and cannot be converted into a number. |
| napi\_create\_object\_with\_named\_properties | Creates an ArkTS object with the given **napi\_value** and key in a native module. The key must be a string and cannot be converted into a number. |

## Example

**napi\_create\_object\_with\_properties**

Call **napi\_create\_object\_with\_properties** to create an ArkTS object with the given **napi\_property\_descriptor**. The key of **napi\_property\_descriptor** must be a string and cannot be converted into a number.

CPP code:

// napi\_create\_object\_with\_properties related to the ArkTS object.
static napi\_value CreateObjectWithProperties(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    // Obtain the parameters of the call.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Declare a napi\_property\_descriptor array desc. It contains a property named "name", whose value is the first input parameter argv\[0\].
    napi\_property\_descriptor desc\[\] = {
        {"name", nullptr, nullptr, nullptr, nullptr, argv\[0\], napi\_default\_jsproperty, nullptr}};
    napi\_value object = nullptr;
    // Call napi\_create\_object\_with\_properties to create an ArkTS object with the specified properties.
    napi\_create\_object\_with\_properties(env, &object, sizeof(desc) / sizeof(desc\[0\]), desc);
    napi\_valuetype valueType;
    napi\_typeof(env, object, &valueType);
    if (valueType == napi\_object) {
        return object;
    }
}

API declaration:

export const createObjectWithProperties: (data: string) => {name:string}; // napi\_create\_object\_with\_properties related to the ArkTS object.

ArkTS code:

// napi\_create\_object\_with\_properties related to the ArkTS object.
let value1 = testNapi.createObjectWithProperties('createObject');
hilog.info(0x0000, 'testTag', 'Node-API napi\_create\_object\_with\_properties:%{public}s',
  JSON.stringify(value1));

**napi\_create\_object\_with\_named\_properties**

Call **napi\_create\_object\_with\_named\_properties** to create an ArkTS object with the specified **napi\_value** and key. The key must be a string and cannot be converted into a number.

CPP code:

// napi\_create\_object\_with\_named\_properties related to the ArkTS object.
static napi\_value CreateObjectWithNameProperties(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    // Obtain the parameters of the call.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    napi\_value obj = nullptr;
    const char \*key\[\] = {
        "name",
    };
    const napi\_value values\[\] = {
        argv\[0\],
    };
    napi\_property\_descriptor desc\[\] = {{"name", nullptr, nullptr,
                                        nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_status status = napi\_create\_object\_with\_named\_properties(
        env, &obj, sizeof(desc) / sizeof(desc\[0\]), key, values
    );
    if (status != napi\_ok) {
        return nullptr;
    }
    return obj;
}

API declaration:

export const createObjectWithNameProperties: (data: string) => undefined | { name: string }; //  napi\_create\_object\_with\_named\_properties related to the ArkTS object.

ArkTS code:

// napi\_create\_object\_with\_named\_properties related to the ArkTS object.
let value2 = testNapi.createObjectWithNameProperties('ls');
try {
  hilog.info(0x0000, 'testTag', 'Node-API napi\_create\_object\_with\_named\_properties:%{public}s', JSON.stringify(value2));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Node-API napi\_create\_object\_with\_named\_properties: %{public}s', error.message);
}

#### Running an .abc File

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_run\_script\_path | Runs the specified .abc file. |

## Example

**napi\_run\_script\_path**

Call **napi\_run\_script\_path** to run an .abc file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/QwSARL_-Rw-dWw4uwiaNpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6E66F74546C0187C12C7431D3F8D796239F279629500C1427C7136A9FEEA103)

Calling this API in the signal function is insecure. Direct calling may cause stack overflow.

CPP code:

// Call napi\_run\_script\_path to run the specified .abc file.
static napi\_value RunScriptPath(napi\_env env, napi\_callback\_info info)
{
    napi\_value value = nullptr;
    // The .abc file in the rawfile directory of the application.
    const char \*scriptPath = "/entry/resources/rawfile/test.abc";
    // Call napi\_run\_script\_path to execute the file of the specified path.
    napi\_status status = napi\_run\_script\_path(env, scriptPath, &value);
    // Check whether the script execution is successful. If the execution fails, return false.
    napi\_value returnValue = nullptr;
    if (value == nullptr || status != napi\_ok) {
        napi\_get\_boolean(env, false, &returnValue);
    } else {
        napi\_get\_boolean(env, true, &returnValue);
    }
    return returnValue;
}

API declaration:

export const runScriptPath: () => boolean; // Call napi\_run\_script\_path to run the specified .abc file.

ArkTS code:

// Call napi\_run\_script\_path to run the specified .abc file.
try { // If the execution fails, false is returned. Otherwise, true is returned.
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_run\_script\_path: %{public}s',
    testNapi.runScriptPath());
  // ···
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_run\_script\_path errorMessage: %{public}s',
    error.message);
  // ···
}

To compile JS code, **test.js** for example, into an .abc file, perform the following steps:

1.  Place the **test.js** file in the **ets/build-tools/ets-loader/bin/ark/build-win/bin** directory of the SDK.
2.  Run the **es2abc.exe test.js --output test.abc** command. The **test.abc** file is generated.

Save the file to the **/entry/resources/rawfile** directory.

function add(a, b) {
  return a + b;
}
add(1, 2);

#### Adding an Async Work with the Specified Priority to a Queue

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_queue\_async\_work\_with\_qos | Adds an async work object to the queue so that it can be scheduled for execution based on the QoS priority passed in. |

## Example

**napi\_queue\_async\_work\_with\_qos**

Call **napi\_queue\_async\_work\_with\_qos** to add an async work to the queue. Then, the async work will be scheduled for execution based on the specified QoS priority.

#### Binding an ArkTS Object and a Native Callback with Parameters

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_coerce\_to\_native\_binding\_object | Forcibly binds an ArkTS object and a native callback with necessary data. This API allows the ArkTS object to carry native information. |

## Example

**napi\_coerce\_to\_native\_binding\_object**

Call **napi\_coerce\_to\_native\_binding\_object** to bind an ArkTS object and a native callback with necessary data. This API allows the ArkTS object to carry native information.

CPP code:

#include <hilog/log.h>
#include <mutex>
#include <unordered\_set>
#include "napi/native\_api.h"

class Object {
public:
    Object() = default;
    ~Object() = default;

    static Object\* GetInstance()
    {
        Object\* instance = new Object();
        return instance;
    }

    static napi\_value GetAddress(napi\_env env, napi\_callback\_info info)
    {
        napi\_value thisVar = nullptr;
        napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisVar, nullptr);
        if (thisVar == nullptr) {
            return nullptr;
        }
        void\* object = nullptr;
        napi\_unwrap(env, thisVar, &object);
        if (object == nullptr) {
            return nullptr;
        }
        uint64\_t addressVal = reinterpret\_cast<uint64\_t>(object);
        napi\_value address = nullptr;
        napi\_create\_bigint\_uint64(env, addressVal, &address);
        return address;
    }

    // Obtain the array size.
    static napi\_value GetSetSize(napi\_env env, napi\_callback\_info info)
    {
        napi\_value thisVar = nullptr;
        napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisVar, nullptr);
        if (thisVar == nullptr) {
            return nullptr;
        }
        void\* object = nullptr;
        napi\_unwrap(env, thisVar, &object);
        if (object == nullptr) {
            return nullptr;
        }
        std::lock\_guard<std::mutex> lock(reinterpret\_cast<Object\*>(object)->numberSetMutex\_);
        uint32\_t setSize = reinterpret\_cast<Object\*>(object)->numberSet\_.size();
        napi\_value napiSize = nullptr;
        napi\_create\_uint32(env, setSize, &napiSize);
        return napiSize;
    }

    // Insert an element into the array.
    static napi\_value Store(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_value thisVar = nullptr;
        napi\_get\_cb\_info(env, info, &argc, args, &thisVar, nullptr);
        if (argc != 1) {
            napi\_throw\_error(env, nullptr, "Store args number must be one.");
            return nullptr;
        }
        napi\_valuetype type = napi\_undefined;
        napi\_typeof(env, args\[0\], &type);
        if (type != napi\_number) {
            napi\_throw\_error(env, nullptr, "Store args is not number.");
            return nullptr;
        }
        if (thisVar == nullptr) {
            return nullptr;
        }
        uint32\_t value = 0;
        napi\_get\_value\_uint32(env, args\[0\], &value);
        void\* object = nullptr;
        napi\_unwrap(env, thisVar, &object);
        if (object == nullptr) {
            return nullptr;
        }
        std::lock\_guard<std::mutex> lock(reinterpret\_cast<Object\*>(object)->numberSetMutex\_);
        reinterpret\_cast<Object \*>(object)-> numberSet\_.insert(value);
        return nullptr;
    }

    // Delete an element from the array.
    static napi\_value Erase(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_value thisVar = nullptr;
        napi\_get\_cb\_info(env, info, &argc, args, &thisVar, nullptr);
        if (argc != 1) {
            napi\_throw\_error(env, nullptr, "Erase args number must be one.");
            return nullptr;
        }
        napi\_valuetype type = napi\_undefined;
        napi\_typeof(env, args\[0\], &type);
        if (type != napi\_number) {
            napi\_throw\_error(env, nullptr, "Erase args is not number.");
            return nullptr;
        }
        if (thisVar == nullptr) {
            return nullptr;
        }
        uint32\_t value = 0;
        napi\_get\_value\_uint32(env, args\[0\], &value);
        void\* object = nullptr;
        napi\_unwrap(env, thisVar, &object);
        if (object == nullptr) {
            return nullptr;
        }
        std::lock\_guard<std::mutex> lock(reinterpret\_cast<Object\*>(object)->numberSetMutex\_);
        reinterpret\_cast<Object \*>(object)->numberSet\_.erase(value);
        return nullptr;
    }

    // Clear the array.
    static napi\_value Clear(napi\_env env, napi\_callback\_info info)
    {
        napi\_value thisVar = nullptr;
        napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisVar, nullptr);
        if (thisVar == nullptr) {
            return nullptr;
        }
        void\* object = nullptr;
        napi\_unwrap(env, thisVar, &object);
        if (object == nullptr) {
            return nullptr;
        }
        std::lock\_guard<std::mutex> lock(reinterpret\_cast<Object\*>(object)->numberSetMutex\_);
        reinterpret\_cast<Object \*>(object)->numberSet\_.clear();
        return nullptr;
    }

private:
    Object(const Object &) = delete;
    Object &operator=(const Object &) = delete;

    std::unordered\_set<uint32\_t> numberSet\_{};
    std::mutex numberSetMutex\_{};
};

void FinalizerCallback(napi\_env env, void \*data, void \*hint)
{
    return;
}

// Detach a callback. Generally, it is called in serialization to perform cleanup operations when the object is detached.
void\* DetachCallback(napi\_env env, void \*value, void \*hint)
{
    return value;
}

// Attach the callback, which is called during deserialization.
napi\_value AttachCallback(napi\_env env, void\* value, void\* hint)
{
    napi\_value object = nullptr;
    napi\_create\_object(env, &object);
    napi\_property\_descriptor desc\[\] = {
        {"getAddress", nullptr, Object::GetAddress, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"getSetSize", nullptr, Object::GetSetSize, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"store", nullptr, Object::Store, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"erase", nullptr, Object::Erase, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"clear", nullptr, Object::Clear, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, object, sizeof(desc) / sizeof(desc\[0\]), desc);
    // Bind the ArkTS object named object to the lifecycle of the native object named value.
    napi\_status status = napi\_wrap(env, object, value, FinalizerCallback, nullptr, nullptr);
    if (status != napi\_ok) {
        OH\_LOG\_INFO(LOG\_APP, "Node-API attachCallback is failed.");
    }
    // Enable the ArkTS object to carry native information.
    napi\_coerce\_to\_native\_binding\_object(env, object, DetachCallback, AttachCallback, value, hint);
    return object;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"getAddress", nullptr, Object::GetAddress, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"getSetSize", nullptr, Object::GetSetSize, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"store", nullptr, Object::Store, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"erase", nullptr, Object::Erase, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"clear", nullptr, Object::Clear, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    auto object = Object::GetInstance();
    napi\_status status = napi\_wrap(env, exports, reinterpret\_cast<void\*>(object), FinalizerCallback, nullptr, nullptr);
    if (status != napi\_ok) {
        OH\_LOG\_INFO(LOG\_APP, "Node-API napi\_wrap is failed.");
    }
    napi\_coerce\_to\_native\_binding\_object(env, exports, DetachCallback, AttachCallback, reinterpret\_cast<void\*>(object),
                                         nullptr);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

API declaration:

// Call napi\_coerce\_to\_native\_binding\_object to bind an ArkTS object to the callback and the callback's parameters.
export const getAddress: () => number;

export const getSetSize: () => number;

export const store: (a: number) => void;

export const erase: (a: number) => void;

export const clear: () => void;

ArkTS code:

// index.ets
import testNapi from 'libentry.so';
import { taskpool } from '@kit.ArkTS';

@Concurrent
function getAddress() {
  let address: number = testNapi.getAddress();
  console.info("taskpool:: address is " + address);
}

@Concurrent
function store(a:number, b:number, c:number) {
  let size:number = testNapi.getSetSize();
  console.info("set size is " + size + " before store");
  testNapi.store(a);
  testNapi.store(b);
  testNapi.store(c);
  size = testNapi.getSetSize();
  console.info("set size is " + size + " after store");
}

@Concurrent
function erase(a:number) {
  let size:number = testNapi.getSetSize();
  console.info("set size is " + size + " before erase");
  testNapi.erase(a);
  size = testNapi.getSetSize();
  console.info("set size is " + size + " after erase");
}

@Concurrent
function clear() {
  let size:number = testNapi.getSetSize();
  console.info("set size is " + size + " before clear");
  testNapi.clear();
  size = testNapi.getSetSize();
  console.info("set size is " + size + " after clear");
}

async function test01(): Promise<void> {
    let address:number = testNapi.getAddress();
    console.info("host thread address is " + address);

    let task1 = new taskpool.Task(getAddress);
    await taskpool.execute(task1);

    let task2 = new taskpool.Task(store, 1, 2, 3);
    await taskpool.execute(task2);

    let task3 = new taskpool.Task(store, 4, 5, 6);
    await taskpool.execute(task3);

    let task4 = new taskpool.Task(erase, 3);
    await taskpool.execute(task4);

    let task5 = new taskpool.Task(erase, 5);
    await taskpool.execute(task5);

    let task6 = new taskpool.Task(clear);
    await taskpool.execute(task6);
}

test01();

**NOTE**

Call **napi\_coerce\_to\_native\_binding\_object** to add the **detach()** and **attach()** callbacks and native object information to ArkTs object A, and then pass object A across threads. To pass object A across threads, you need to serialize and deserialize it by calling the **napi\_serialize** and **napi\_deserialize** APIs. As shown in the following figure, in thread 1, "data" is obtained after object A is serialized, and the **detach()** callback is invoked in the serialization process. Then, "data" is passed to thread 2 and deserialized in thread 2. The **attach()** callback is invoked to obtain the ArkTS object A. The **detach()** and **attach()** callback are used to notify that serialization and deserialization are complete.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/NNwMJvwOR0ioM0_Sxk5SWQ/en-us_image_0000002568685009.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1350B327E60268A1F24036F1A34ED4E3ECFBCBEEF6E38C6F67D41C90580FB2A)

#### Event Loop

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_run\_event\_loop | Runs an underlying event loop. |
| napi\_stop\_event\_loop | Stops an underlying event loop. |

## Example

**napi\_run\_event\_loop** and **napi\_stop\_event\_loop**

See [Running or Stopping an Event Loop in an Asynchronous Thread Using Node-API Extensions](../../typical-node-api-use-cases/running-or-stopping-an-event-loop-in-an-asynchronous-thread-using-node-api-exten/document.md)

#### ArkTS Runtime Environment

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_create\_ark\_runtime | Creates an ArkTS runtime environment. |
| napi\_destroy\_ark\_runtime | Destroys the ArkTS runtime environment. |

## Example

**napi\_create\_ark\_runtime** and **napi\_destroy\_ark\_runtime**

See [Creating an ArkTs Runtime Environment Using Node-API](../../typical-node-api-use-cases/creating-an-arkts-runtime-environment-using-node-api/document.md).

#### Serialization and Deserialization

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_serialize | 
Converts an ArkTS object into native data.

The first parameter **env** indicates the ArkTS environment where the API is executed. The second parameter **object** indicates the ArkTS object to be serialized. The third parameter **transfer\_list** indicates an array that holds the **arrayBuffer** to be passed. This parameter can be set to **undefined** if there is no data to be passed. The fourth parameter **clone\_list** indicates an array that holds the sendable object to be cloned. This parameter can be set to **undefined** if there is no data to be cloned. The fifth parameter **result** indicates the serialized data obtained.

 |
| napi\_deserialize | Converts native data into an ArkTS object. The first parameter **env** indicates the ArkTS environment where the API is executed. The second parameter **buffer** indicates the data to be deserialized. The third parameter **object** indicates the deserialized data obtained. |
| napi\_delete\_serialization\_data | Deletes serialized data. |

## Example

**napi\_serialize**, **napi\_deserialize**, and **napi\_delete\_serialization\_data**

Call **napi\_serialize** to convert an ArkTS object into native data; call **napi\_deserialize** to convert native data into an ArkTS object; call **napi\_delete\_serialization\_data** to delete serialized data.

CPP code:

// Serialization and deserialization.
static napi\_value AboutSerialize(napi\_env env, napi\_callback\_info info)
{
    // Obtain an ArkTS object as a parameter.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_value undefined = nullptr;
    // Construct the parameters required by the napi\_serialize method.
    napi\_get\_undefined(env, &undefined);
    void \*data = nullptr;
    // Call napi\_serialize to convert the ArkTS object into native data.
    napi\_status status = napi\_serialize(env, args\[0\], undefined, undefined, &data);
    if (status != napi\_ok || data == nullptr) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_serialize fail");
        return nullptr;
    }
    // Construct data of the napi\_value type to hold the ArkTS object converted from the native data.
    napi\_value result = nullptr;
    napi\_deserialize(env, data, &result);
    napi\_value number = nullptr;
    // Obtain the value of the numKey property in the ArkTS object converted from native data.
    napi\_get\_named\_property(env, result, "numKey", &number);
    // Check whether the obtained property value is of the number type.
    napi\_valuetype valuetype;
    napi\_typeof(env, number, &valuetype);
    if (valuetype != napi\_number) {
        napi\_throw\_error(env, nullptr, "Node-API Wrong type of argument. Expects a number.");
        return nullptr;
    }
    // Call napi\_delete\_serialization\_data to delete the serialized data.
    napi\_delete\_serialization\_data(env, data);
    // Return the obtained property value.
    return number;
}

API declaration:

export const aboutSerialize: (obj: {numKey:number}) => number | undefined; // Serialization and deserialization.

ArkTS code:

class Obj {
  numKey: number = 0;
}

// Serialization and deserialization.
let obj: Obj = { numKey: 500 };
hilog.info(0x0000, 'testTag', ' Node-API aboutSerialize: %{public}d', testNapi.aboutSerialize(obj));

#### Passing a Task from an Asynchronous Thread to an ArkTS Thread

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_call\_threadsafe\_function\_with\_priority | Calls a task with the specified priority and enqueuing mode into the ArkTS main thread. |

## Example

**napi\_call\_threadsafe\_function\_with\_priority**

See [Passing a Task with the Specified Priority to an ArkTS Thread from an Asynchronous Thread Using Node-API](../../typical-node-api-use-cases/passing-a-task-with-the-specified-priority-and-enqueuing-mode-to-an-arkts-thread/document.md).

#### Sendable-related Operations

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_is\_sendable | Checks whether an ArkTS value is sendable. |
| napi\_define\_sendable\_class | Creates a sendable class. |
| napi\_create\_sendable\_object\_with\_properties | Creates a sendable object with the given **napi\_property\_descriptor**. |
| napi\_create\_sendable\_array | Creates a sendable array. |
| napi\_create\_sendable\_array\_with\_length | Creates a sendable array of the specified length. |
| napi\_create\_sendable\_arraybuffer | Creates a sendable **ArrayBuffer**. |
| napi\_create\_sendable\_typedarray | Creates a sendable **TypedArray**. |
| napi\_wrap\_sendable | Wraps a native instance into an ArkTS object. |
| napi\_wrap\_sendable\_with\_size | Wraps a native instance of the specified size into an ArkTS object. |
| napi\_unwrap\_sendable | Unwraps the native instance from an ArkTS object. |
| napi\_remove\_wrap\_sendable | Removes and obtains the native instance wrapped by an ArkTS object. After removal, the callback will no longer be triggered and must be manually deleted to free memory. |

## Example

**napi\_is\_sendable**

Call **napi\_is\_sendable** to check whether an ArkTS value is sendable.

CPP code:

// napi\_is\_sendable related to Sendable.
static napi\_value IsSendable(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    bool isSendable = false;
    napi\_is\_sendable(env, args\[0\], &isSendable);
    napi\_value result;
    napi\_get\_boolean(env, isSendable, &result);
    return result;
}

API declaration:

export const isSendable: <T>(a: T) => boolean; // napi\_is\_sendable related to Sendable.

ArkTS code:

// napi\_is\_sendable related to Sendable.
let value = testNapi.isSendable('createObject');
hilog.info(0x0000, 'testTag', 'Node-API napi\_is\_sendable: %{public}s', JSON.stringify(value));

**napi\_define\_sendable\_class**

Call **napi\_define\_sendable\_class** to create a sendable class.

CPP code:

#include "napi/native\_api.h"

static napi\_value func(napi\_env env, napi\_callback\_info info) {
    napi\_value val;
    napi\_create\_string\_utf8(env, "func result", NAPI\_AUTO\_LENGTH, &val);
    return val;
}

static napi\_value DefineSendableClass(napi\_env env) {
    napi\_value str;
    napi\_create\_string\_utf8(env, "str", NAPI\_AUTO\_LENGTH, &str);

    napi\_property\_descriptor props\[\] = {
        {"staticStr", nullptr, nullptr, nullptr, nullptr, str,
         static\_cast<napi\_property\_attributes>(napi\_static | napi\_writable), nullptr},
        {"staticFunc", nullptr, func, nullptr, nullptr, nullptr, napi\_static, nullptr},
        {"str", nullptr, nullptr, nullptr, nullptr, str, static\_cast<napi\_property\_attributes>(1 << 9 | napi\_writable),
         nullptr},
        {"func", nullptr, nullptr, nullptr, nullptr, nullptr,
         static\_cast<napi\_property\_attributes>(1 << 11 | napi\_writable), nullptr},
    };

    napi\_value sendableClass = nullptr;
    napi\_define\_sendable\_class(
        env, "SendableClass", NAPI\_AUTO\_LENGTH,
        \[\](napi\_env env, napi\_callback\_info info) -> napi\_value {
            napi\_value thisVar = nullptr;
            napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisVar, nullptr);
            napi\_value str;
            napi\_create\_string\_utf8(env, "instance str", NAPI\_AUTO\_LENGTH, &str);
            napi\_property\_descriptor props\[\] = {
                {"str", nullptr, nullptr, nullptr, nullptr, str, napi\_default, nullptr},
                {"func", nullptr, func, nullptr, nullptr, nullptr, napi\_default, nullptr},
            };
            napi\_define\_properties(env, thisVar, sizeof(props) / sizeof(props\[0\]), props);
            return thisVar;
        },
        nullptr, sizeof(props) / sizeof(props\[0\]), props, nullptr, &sendableClass);

    return sendableClass;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    napi\_value cons = DefineSendableClass(env);
    napi\_set\_named\_property(env, exports, "SendableClass", cons);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

API declaration:

@Sendable
export class SendableClass {
  static staticStr: string;
  static staticFunc(): string;
  str: string;
  func(): string;
} // napi\_define\_sendable\_class related to Sendable.

ArkTS code:

// napi\_define\_sendable\_class related to Sendable
let value = new testNapi.SendableClass();
hilog.info(0x0000, 'testTag', 'Node-API napi\_define\_sendable\_class: %{public}s', value.str);

**napi\_create\_sendable\_object\_with\_properties**

Call **napi\_create\_sendable\_object\_with\_properties** to create a sendable object with the given **napi\_property\_descriptor**.

CPP code:

// napi\_create\_sendable\_object\_with\_properties related to Sendable.
static napi\_value GetSendableObject(napi\_env env, napi\_callback\_info info)
{
    napi\_value val\_true;
    napi\_get\_boolean(env, true, &val\_true);
    napi\_property\_descriptor desc1\[\] = {
        {"x", nullptr, nullptr, nullptr, nullptr, val\_true, napi\_default\_jsproperty, nullptr},
    };
    napi\_value obj;
    napi\_create\_sendable\_object\_with\_properties(env, 1, desc1, &obj);
    return obj;
}

API declaration:

export const getSendableObject: () => { x: true }; // napi\_create\_sendable\_object\_with\_properties related to Sendable.

ArkTS code:

// napi\_create\_sendable\_object\_with\_properties related to Sendable.
let value = testNapi.getSendableObject();
hilog.info(0x0000, 'testTag', 'Node-API napi\_create\_sendable\_object\_with\_properties: %{public}s',
  JSON.stringify(value));

**napi\_create\_sendable\_array**

Call **napi\_create\_sendable\_array** to create a sendable array.

CPP code:

// napi\_create\_sendable\_array related to Sendable.
static napi\_value GetSendableArray(napi\_env env, napi\_callback\_info info)
{
    napi\_value result = nullptr;
    napi\_create\_sendable\_array(env, &result);
    return result;
}

API declaration:

export const getSendableArray: () => \[\]; // napi\_create\_sendable\_array related to Sendable.

ArkTS code:

// napi\_create\_sendable\_array related to Sendable.
let value = testNapi.getSendableArray();
hilog.info(0x0000, 'testTag', 'Node-API napi\_create\_sendable\_array: %{public}s',
  JSON.stringify(value));

**napi\_create\_sendable\_array\_with\_length**

Call **napi\_create\_sendable\_array\_with\_length** to create a sendable array of the specified length.

CPP code:

// napi\_create\_sendable\_array\_with\_length related to Sendable.
static napi\_value GetSendableArrayWithLength(napi\_env env, napi\_callback\_info info)
{
    napi\_value result = nullptr;
    napi\_create\_sendable\_array\_with\_length(env, 1, &result);
    return result;
}

API declaration:

// index.d.ts
export const getSendableArrayWithLength: () => \[\];

ArkTS code:

let value = testNapi.getSendableArrayWithLength();
hilog.info(0x0000, 'testTag', 'Node-API napi\_create\_sendable\_array\_with\_length: %{public}s', JSON.stringify(value.length));

**napi\_create\_sendable\_arraybuffer**

Call **napi\_create\_sendable\_arraybuffer** to create a sendable **ArrayBuffer**.

CPP code:

static napi\_value GetSendableArrayBuffer(napi\_env env, napi\_callback\_info info) {
    static size\_t LENGTH = 1024;
    void \*data;
    napi\_value result = nullptr;
    napi\_create\_sendable\_arraybuffer(env, LENGTH, &data, &result);
    bool isArrayBuffer = false;
    napi\_is\_arraybuffer(env, result, &isArrayBuffer);
    OH\_LOG\_INFO(LOG\_APP, "isArrayBuffer: %{public}d", isArrayBuffer);
    return result;
}

API declaration:

// index.d.ts
export const getSendableArrayBuffer: () => ArrayBuffer;

ArkTS code:

testNapi.getSendableArrayBuffer();

**napi\_create\_sendable\_typedarray**

Call **napi\_create\_sendable\_typedarray** to create a sendable **TypedArray**.

CPP code:

static napi\_value GetSendableTypedArray(napi\_env env, napi\_callback\_info info) {
    static size\_t LENGTH = 1024;
    static size\_t OFFSET = 0;
    void \*data;
    napi\_value arraybuffer = nullptr;
    napi\_create\_sendable\_arraybuffer(env, LENGTH, &data, &arraybuffer);

    napi\_value result = nullptr;
    napi\_create\_sendable\_typedarray(env, napi\_uint8\_array, LENGTH, arraybuffer, OFFSET, &result);
    bool isTypedArray = false;
    napi\_is\_typedarray(env, result, &isTypedArray);
    OH\_LOG\_INFO(LOG\_APP, "isTypedArray: %{public}d", isTypedArray);
    return result;
}

API declaration:

// index.d.ts
export const getSendableTypedArray: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

testNapi.getSendableTypedArray();

**napi\_wrap\_sendable**

Call **napi\_wrap\_sendable** to wrap a native instance into an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value WrapSendable(napi\_env env, napi\_callback\_info info) {
    napi\_value val\_true;
    napi\_get\_boolean(env, true, &val\_true);
    napi\_property\_descriptor desc1\[\] = {
        {"x", nullptr, nullptr, nullptr, nullptr, val\_true, napi\_default\_jsproperty, nullptr},
    };
    napi\_value obj;
    napi\_create\_sendable\_object\_with\_properties(env, 1, desc1, &obj);

    const char\* testStr = "test";
    napi\_wrap\_sendable(env, obj, (void\*)testStr, \[\](napi\_env env, void\* data, void\* hint) {}, nullptr);

    return nullptr;
}

API declaration:

// index.d.ts
export const wrapSendable: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

testNapi.wrapSendable();

**napi\_wrap\_sendable\_with\_size**

Call **napi\_wrap\_sendable\_with\_size** to wrap a native instance of the specified size into an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value WrapSendableWithSize(napi\_env env, napi\_callback\_info info) {
    napi\_value val\_true;
    napi\_get\_boolean(env, true, &val\_true);
    napi\_property\_descriptor desc1\[\] = {
        {"x", nullptr, nullptr, nullptr, nullptr, val\_true, napi\_default\_jsproperty, nullptr},
    };
    napi\_value obj;
    napi\_create\_sendable\_object\_with\_properties(env, 1, desc1, &obj);

    const char\* testStr = "test";
    napi\_wrap\_sendable\_with\_size(env, obj, (void\*)testStr, \[\](napi\_env env, void\* data, void\* hint) {}, nullptr, 100);

    return nullptr;
}

API declaration:

// index.d.ts
export const wrapSendableWithSize: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

testNapi.wrapSendableWithSize();

**napi\_unwrap\_sendable**

Call **napi\_unwrap\_sendable** to unwrap the native instance from an ArkTS object.

CPP code:

#include "napi/native\_api.h"

static napi\_value UnwrapSendable(napi\_env env, napi\_callback\_info info) {
    napi\_value val\_true;
    napi\_get\_boolean(env, true, &val\_true);
    napi\_property\_descriptor desc1\[\] = {
        {"x", nullptr, nullptr, nullptr, nullptr, val\_true, napi\_default\_jsproperty, nullptr},
    };
    napi\_value obj;
    napi\_create\_sendable\_object\_with\_properties(env, 1, desc1, &obj);

    const char\* testStr = "test";
    napi\_wrap\_sendable(env, obj, (void\*)testStr, \[\](napi\_env env, void\* data, void\* hint) {}, nullptr);

    char\* tmpTestStr = nullptr;
    napi\_unwrap\_sendable(env, obj, (void\*\*)&tmpTestStr);
    OH\_LOG\_INFO(LOG\_APP, "native value is %{public}s", tmpTestStr);

    return nullptr;
}

API declaration:

// index.d.ts
export const unwrapSendable: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

testNapi.unwrapSendable();

**napi\_remove\_wrap\_sendable**

Call **napi\_remove\_wrap\_sendable** to remove and obtain the native instance wrapped by an ArkTS object. After removal, the callback will no longer be triggered and must be manually deleted to free memory.

CPP code:

#include "napi/native\_api.h"

static napi\_value RemoveWrapSendable(napi\_env env, napi\_callback\_info info) {
    napi\_value val\_true;
    napi\_get\_boolean(env, true, &val\_true);
    napi\_property\_descriptor desc1\[\] = {
        {"x", nullptr, nullptr, nullptr, nullptr, val\_true, napi\_default\_jsproperty, nullptr},
    };
    napi\_value obj;
    napi\_create\_sendable\_object\_with\_properties(env, 1, desc1, &obj);

    const char\* testStr = "test";
    napi\_wrap\_sendable(env, obj, (void\*)testStr, \[\](napi\_env env, void\* data, void\* hint) {}, nullptr);

    char\* tmpTestStr = nullptr;
    napi\_remove\_wrap\_sendable(env, obj, (void\*\*)&tmpTestStr);
    OH\_LOG\_INFO(LOG\_APP, "native value is %{public}s", tmpTestStr);

    return nullptr;
}

API declaration:

// index.d.ts
export const removeWrapSendable: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

testNapi.removeWrapSendable();

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
target\_compile\_definitions(entry PRIVATE LOG\_DOMAIN=0xd0d0 LOG\_TAG="testTag")
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)

#### napi\_wrap Enhancement

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_wrap\_enhance | Wraps a native instance of the specified size into an ArkTS object. During runtime, the instance size is counted and accumulated. When the accumulated size reaches the GC triggering threshold, the garbage collection process is started. You can specify whether to execute the registered callback asynchronously (if asynchronous, it must be thread-safe). |

## Example

**napi\_wrap\_enhance**

Call **napi\_wrap\_enhance** to wrap a native instance of the specified size into an ArkTS object. During runtime, the instance size is counted and accumulated. When the accumulated size reaches the GC triggering threshold, the garbage collection process is started. You can specify whether to execute the registered callback asynchronously (if asynchronous, it must be thread-safe).

CPP code:

#include "napi/native\_api.h"

static napi\_value TestNapiWrapEnhance(napi\_env env, napi\_callback\_info info)
{
    napi\_value testClass = nullptr;
    napi\_define\_class(
        env, "TestClass", NAPI\_AUTO\_LENGTH,
        \[\](napi\_env env, napi\_callback\_info info) -> napi\_value {
            napi\_value thisVar = nullptr;
            napi\_get\_cb\_info(env, info, nullptr, nullptr, &thisVar, nullptr);
            return thisVar;
        },
        nullptr, 0, nullptr, &testClass);

    napi\_value obj = nullptr;
    napi\_new\_instance(env, testClass, 0, nullptr, &obj);
    const char\* testStr = "test";
    napi\_ref wrappedRef = nullptr;
    napi\_wrap\_enhance(env, obj, (void\*)testStr, \[\](napi\_env env, void\* data, void\* hint) {}, false, nullptr, sizeof(testStr), &wrappedRef);
    return nullptr;
}

API declaration:

// index.d.ts
export const testNapiWrapEnhance: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

testNapi.testNapiWrapEnhance();

#### Multi-context of Node-API

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_create\_ark\_context | Creates a basic runtime context. |
| napi\_switch\_ark\_context | Switches to the specified runtime context environment. |
| napi\_destroy\_ark\_context | Destroys the basic runtime context. |

## Example

**napi\_create\_ark\_context, napi\_switch\_ark\_context, and napi\_destroy\_ark\_context**

[Creating, Switching, and Destroying a Context in a Thread Using Node-API Extension APIs](../../typical-node-api-use-cases/creating-switching-and-destroying-a-context-in-a-thread-using-node-api-extension/document.md)

#### Accessing ArkTS String Memory Data Using the Pointer of Node-API

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | Obtains the memory data buffer of an ArkTS string encoded in UTF-16. |

## Example

**napi\_get\_buffer\_string\_utf16\_in\_critical\_scope**

[Creating and Destroying a Critical Scope and Accessing String Content Using Node-API Extension APIs](../../typical-node-api-use-cases/creating-and-destroying-a-critical-scope-and-accessing-string-content-using-node/document.md)

#### Implementing a Critical Scope Through Node-API

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_open\_critical\_scope | Opens a critical scope. |
| napi\_close\_critical\_scope | Closes a critical scope. |

## Example

**napi\_open\_critical\_scope, napi\_close\_critical\_scope**

[Creating and Destroying a Critical Scope and Accessing String Content Using Node-API Extension APIs](../../typical-node-api-use-cases/creating-and-destroying-a-critical-scope-and-accessing-string-content-using-node/document.md)

#### Creating Lightweight Strong Reference Objects Using Node-API

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_create\_strong\_reference | Creates a strong reference to an ArkTS object. |
| napi\_delete\_strong\_reference | Deletes a strong reference. |
| napi\_get\_strong\_reference\_value | Obtains the ArkTS object value associated with a strong reference object. |

## Example

**napi\_create\_strong\_reference, napi\_delete\_strong\_reference, napi\_get\_value\_strong\_reference**

[Creating a Strong Reference to an ArkTS Object Using Node-API Extension APIs](../../typical-node-api-use-cases/creating-a-strong-reference-to-an-arkts-object-using-node-api-extension-apis/document.md)

#### Creating Sendable Strong References Using Node-API

## Available APIs

| API | Description |
| :-- | :-- |
| napi\_create\_strong\_sendable\_reference | Creates a Sendable strong reference to a Sendable ArkTS object. |
| napi\_delete\_strong\_sendable\_reference | Deletes a Sendable strong reference. |
| napi\_get\_strong\_sendable\_reference\_value | Obtains the ArkTS object value associated with a Sendable strong reference. |

## Example

**napi\_create\_strong\_sendable\_reference, napi\_delete\_strong\_sendable\_reference, napi\_get\_strong\_sendable\_reference\_value**

[Creating a Sendable Strong Reference to an ArkTS Object Using Node-API Extension APIs](../../typical-node-api-use-cases/creating-a-sendable-strong-reference-to-an-arkts-object-using-node-api-extension/document.md)
