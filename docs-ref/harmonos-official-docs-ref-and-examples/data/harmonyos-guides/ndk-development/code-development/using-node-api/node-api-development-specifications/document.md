# Node-API Development Specifications

#### Obtaining Arguments Passed by JS

**\[Rule\]** When **argv** in **napi\_get\_cb\_info** is not **nullptr**, the length of **argv** must be greater than or equal to **argc**.

If **argv** is not **nullptr**, the arguments actually passed by JS will be copied to **argv** in **napi\_get\_cb\_info** based on the value of **argc**. If there are more arguments than the provided count, only the requested number of arguments are copied. If there are fewer arguments provided than the claimed, the rest of **argv** is filled with values that represent **undefined**.

**Example (incorrect)**

static napi\_value IncorrectDemo1(napi\_env env, napi\_callback\_info info) {
    // argc is not correctly initialized and is set to a random value. If the length of argv is less than the number of arguments specified by argc, data overwriting occurs.
    size\_t argc;
    napi\_value argv\[10\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    return nullptr;
}

static napi\_value IncorrectDemo2(napi\_env env, napi\_callback\_info info) {
    // The number of arguments specified by argc is greater than the length of argv. As a result, data overwriting occurs when napi\_get\_cb\_info writes argv.
    size\_t argc = 5;
    napi\_value argv\[3\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    return nullptr;
}

**Example (correct)**

static napi\_value GetArgvDemo1(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 0;
    // Pass in nullptr to argv to obtain the actual number of arguments passed by JS.
    napi\_get\_cb\_info(env, info, &argc, nullptr, nullptr, nullptr);
    // If 0 is passed by JS, the subsequent logic is not executed.
    if (argc == 0) {
        return nullptr;
    }
    // Create an array to obtain the arguments passed by JS.
    napi\_value\* argv = new napi\_value\[argc\];
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Service code.
    // ... ...
    // argv is an object created by new and must be manually released when it is not required.
    delete\[\] argv;
    return nullptr;
}

static napi\_value GetArgvDemo2(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value argv\[2\] = {nullptr};
    // napi\_get\_cb\_info writes the arguments (of the quantity specified by argc) passed by JS or undefined to argv.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Service code.
    // ... ...
    return nullptr;
}

#### Lifecycle Management

**\[Rule\]** Properly use **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** to minimize the lifecycle of **napi\_value** and avoid memory leaks.

Each **napi\_value** belongs to a specific **HandleScope**, which is opened and closed by **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope**, respectively. After a **HandleScope** is closed, its **napi\_value** is automatically released.

**Example (correct)**

// When Node-API is frequently called to create JS objects in the for loop, use handle\_scope to release resources in a timely manner when they are no longer used.
// In the following example, the lifecycle of the local variable res ends at the end of each loop. To prevent memory leaks, scope is used to release the JS object in a timely manner.
for (int i = 0; i < 100000; i++) {
    napi\_handle\_scope scope = nullptr;
    napi\_open\_handle\_scope(env, &scope);
    if (scope == nullptr) {
        return;
    }
    napi\_value res;
    napi\_create\_object(env, &res);
    napi\_close\_handle\_scope(env, scope);
}

#### Context Sensitive

**\[Rule\]** Do not use Node-API to access JS objects across engine instances.

An engine instance is an independent running environment. Operations such as creating and accessing a JS object must be performed in the same engine instance. If an object is operated in different engine instances, the application may crash. An engine instance is represented as a value of **napi\_env** in APIs.

**Example (incorrect)**

// Create a string object with value of "bar" in env1.
napi\_create\_string\_utf8(env1, "bar", NAPI\_AUTO\_LENGTH, &string);
// Create an object in env2 and set the string object to this object.
napi\_status status = napi\_create\_object(env2, &object);
if (status != napi\_ok) {
    napi\_throw\_error(env, ...);
    return;
}

status = napi\_set\_named\_property(env2, object, "foo", string);
if (status != napi\_ok) {
    napi\_throw\_error(env, ...);
    return;
}

JS objects belong to a specific **napi\_env**. Therefore, you cannot set an object of env1 to an object of env2. If the object of env1 is accessed in env2, the application may crash.

#### Exception Handling

**\[Suggestion\]** Any exception occurred in a Node-API call should be handled in a timely manner. Otherwise, unexpected behavior may occur.

**Example (correct)**

// 1. Create an object.
napi\_status status = napi\_create\_object(env, &object);
if (status != napi\_ok) {
    napi\_throw\_error(env, ...);
    return;
}
// 2. Create a property.
status = napi\_create\_string\_utf8(env, "bar", NAPI\_AUTO\_LENGTH, &string);
if (status != napi\_ok) {
    napi\_throw\_error(env, ...);
    return;
}
// 3. Set the result of step 2 to the value of the object property foo.
status = napi\_set\_named\_property(env, object, "foo", string);
if (status != napi\_ok) {
    napi\_throw\_error(env, ...);
    return;
}

In this example, if an exception occurs in step 1 or step 2, step 3 will not be performed. Step 3 will be performed only when napi\_ok is returned in steps 1 and 2.

#### Asynchronous Tasks

**\[Rule\]** When the **uv\_queue\_work** method is called to throw a work to a JS thread for execution, use **napi\_handle\_scope** to manage the lifecycle of **napi\_value** created by the JS callback.

The Node-API framework will not be used when the **uv\_queue\_work** method is called. In this case, you must use **napi\_handle\_scope** to manage the lifecycle of **napi\_value**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/hSyVa312Q8SmSf98ilSPZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EC9BCEA22510F913CBC78026E0F8D48B23D3463FF1F1055D69399000701207F)

This rule focuses on the **napi\_value** lifecycle. If you only want to throw tasks to the JS thread, you are advised not to use **uv\_queue\_work**. To throw tasks, use [napi\_threadsafe\_function](../typical-node-api-use-cases/thread-safety-development-using-node-api/document.md) APIs.

**Example (correct)**

void CallbackTest(CallbackContext\* context)
{
    uv\_loop\_s\* loop = nullptr;
    napi\_get\_uv\_event\_loop(context->env, &loop);
    uv\_work\_t\* work = new uv\_work\_t;
    context->retData = 1;
    work->data = (void\*)context;
    uv\_queue\_work(
        loop, work,
        // Note that uv\_queue\_work creates a thread and executes the callback. If you only want to throw tasks to the JS thread, you are advised not to use uv\_queue\_work to avoid creation of redundant threads.
        \[\](uv\_work\_t\* work) {
            // Execute service logic.
        },
        // The callback is executed on the JS thread where the loop is located.
        \[\](uv\_work\_t\* work, int status) {
            CallbackContext\* context = (CallbackContext\*)work->data;
            napi\_handle\_scope scope = nullptr;
            napi\_open\_handle\_scope(context->env, &scope);
            if (scope == nullptr) {
                if (work != nullptr) {
                    delete work;
                }
                return;
            }
            napi\_value callback = nullptr;
            napi\_get\_reference\_value(context->env, context->callbackRef, &callback);
            napi\_value retArg;
            napi\_create\_int32(context->env, context->retData, &retArg);
            napi\_value ret;
            napi\_call\_function(context->env, nullptr, callback, 1, &retArg, &ret);
            napi\_delete\_reference(context->env, context->callbackRef);
            napi\_close\_handle\_scope(context->env, scope);
            if (work != nullptr) {
                delete work;
            }
            delete context;
        }
    );
}

#### Object Wrapping

**\[Rule\]** If the value of the last parameter **result** is not **nullptr** in **napi\_wrap()**, use **napi\_remove\_wrap()** at a proper time to delete the created **napi\_ref**.

The **napi\_wrap** interface is defined as follows:

napi\_wrap(napi\_env env, napi\_value js\_object, void\* native\_object, napi\_finalize finalize\_cb, void\* finalize\_hint, napi\_ref\* result)

When the last parameter **result** is not null, the Node-API framework creates an **napi\_ref** object pointing to **js\_object**. You need to manage the lifecycle of **js\_object**. Specifically, use **napi\_remove\_wrap** to delete **napi\_ref** at a proper time so that the garbage collector (GC) can release **js\_object** and trigger the destructor **finalize\_cb** bound to the C++ object **native\_object**.

Generally, you can directly pass in **nullptr** for the last parameter **result**.

**Example (correct)**

// Case 1: Pass in nullptr via the last parameter in napi\_wrap. In this case, the created napi\_ref is a weak reference, which is managed by the system and does not need manual release.
napi\_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

// Case 2: The last parameter in napi\_wrap is not nullptr. In this case, the returned napi\_ref is a strong reference and needs to be manually released. Otherwise, memory leaks may occur.
napi\_ref result;
napi\_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
// When js\_object and result are no longer used, call napi\_remove\_wrap to release result.
void\* nativeObjectResult = nullptr;
napi\_remove\_wrap(env, jsobject, &nativeObjectResult);

#### Arrays for High Performance

**\[Suggestion\]** Use ArrayBuffer instead of JSArray to store value-type data for higher performance.

JSArray is used as a container to store data and supports almost all JS data types.

When **napi\_set\_element** is used to store value-type data (such as int32) in JSArray, interaction with the runtime is involved, which causes unnecessary overhead.

The operations on ArrayBuffer are performed in the buffer, which delivers higher performance than using **napi\_set\_element** to operate JSArray.

Therefore, you are advised to use the **ArrayBuffer** object created by **napi\_create\_arraybuffer** in this scenario.

**Example:**

// In the following code, JSArray is used to store only int32 data.
// Since JSArray is a JS object, only Node-API methods can be used to operate it, which compromises the performance.
static napi\_value ArrayDemo(napi\_env env, napi\_callback\_info info)
{
    constexpr size\_t arrSize = 1000;
    napi\_value jsArr = nullptr;
    napi\_create\_array(env, &jsArr);
    for (int i = 0; i < arrSize; i++) {
        napi\_value arrValue = nullptr;
        napi\_create\_int32(env, i, &arrValue);
        // Using Node-API methods to read and write JSArray affects the performance.
        napi\_set\_element(env, jsArr, i, arrValue);
    }
    return jsArr;
}

// To improve the performance, modify the code as follows:
// Use ArrayBuffer to hold int32 data.
// In this case, C/C++ methods can be used to directly add or modify data in the buffer.
static napi\_value ArrayBufferDemo(napi\_env env, napi\_callback\_info info)
{
    constexpr size\_t arrSize = 1000;
    napi\_value arrBuffer = nullptr;
    void\* data = nullptr;

    napi\_create\_arraybuffer(env, arrSize \* sizeof(int32\_t), &data, &arrBuffer);
    // data is a null pointer. Cancel the write of data.
    if (data == nullptr) {
        return arrBuffer;
    }
    int32\_t\* i32Buffer = reinterpret\_cast<int32\_t\*>(data);
    for (int i = 0; i < arrSize; i++) {
        // Using arrayBuffer allows data to be directly modified in the buffer, which eliminates the interaction with the runtime.
        // The performance is equivalent to that of operating native C/C++ objects.
        i32Buffer\[i\] = i;
    }

    return arrBuffer;
}

**napi\_create\_arraybuffer** is equivalent to **new ArrayBuffer(size)** in JS. The object generated cannot be directly read in TS/JS. It can be read or written only after being encapsulated into a TypedArray or DataView object.

**Benchmark performance test result**:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Eb6f8cSrTaeG61PNAJ3YBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C24B688467ED963F96A904B7DFE1F47935ADAFDECC1EB1085AE5377AEB2865DF)

The following data is the accumulated data written in thousands of cycles. To better reflect the difference, the core frequency of the device has been limited.

| Container Type | Benchmark Data (us) |
| :-- | :-- |
| JSArray | 1566.174 |
| ArrayBuffer | 3.609 |

#### Data Conversion

**\[Suggestion\]** Minimize the number of data conversions and avoid unnecessary replication.

-   Frequent data conversion affects performance. You are advised to use batch data processing or optimize the data structs to improve performance.
-   During data conversion, use Node-API to access the original data instead of creating a copy.
-   For the data that may be used in multiple conversions, store it in a buffer to avoid repeated data conversions. In this way, unnecessary calculations can be reduced, leading to better performance.

#### Module Registration and Naming

**\[Rule\]**

Add "static" to the function corresponding to **nm\_register\_func** to prevent conflicts with symbols in other binary .so files.

The module registration entry, that is, the name of the function decorated by ****attribute**((constructor))** must be different from that of other modules.

The **.nm\_modname** field must completely match the name of the binary .so file and is case sensitive.

**Example (incorrect)**

The following is an incorrect example when the name of the binary .so file is **nativerender**.

EXTERN\_C\_START
napi\_value Init(napi\_env env, napi\_value exports)
{
    // ...
    return exports;
}
EXTERN\_C\_END

static napi\_module nativeModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    // static is not added to the function corresponding to nm\_register\_func.
    .nm\_register\_func = Init,
    // The .nm\_modname value does not match the module name. As a result, the module fails to be loaded in the multi-thread scenario.
    .nm\_modname = "entry",
    .nm\_priv = nullptr,
    .reserved = { 0 },
};

// The name of the module registration entry function is RegisterModule, which is easy to be duplicate with that of other modules.
extern "C" \_\_attribute\_\_((constructor)) void RegisterModule()
{
    napi\_module\_register(&nativeModule);
}

Figure 1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Q1bX7rp-RdmKsW6DRnhlIw/en-us_image_0000002537765292.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14393ACD2D86ED8291B61D944B8FA1071796AA774F4C1A89C32017AD5A505EE0)

Figure 2

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/yuPDGticTLuoL8YsTgPw0A/en-us_image_0000002537925232.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80F4211487A23F01D58EBBD3CAAB8B9B0F8EDD5518F1836A5F07BDCB11A65B8C)

**Example (correct)**

In the following example, the module name is **nativerender**.

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    // ...
    return exports;
}
EXTERN\_C\_END

static napi\_module nativeModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "nativerender",
    .nm\_priv = nullptr,
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterNativeRenderModule()
{
    napi\_module\_register(&nativeModule);
}

#### dlopen and Module Registration

**\[Rule\]**

If **dlopen** has been called, register the module as follows:

The module must export the function named **napi\_onLoad**, and call the registration function in the function. **napi\_onLoad** is only called by the import statement of ArkTS code, so that module registration is not triggered in advance when **dlopen** is called.

**Example**

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    // ...
    return exports;
}
EXTERN\_C\_END

static napi\_module nativeModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "nativerender",
    .nm\_priv = nullptr,
    .reserved = { 0 },
};

extern "C" void napi\_onLoad()
{
    napi\_module\_register(&nativeModule);
}

#### Using JS Objects Created by napi\_create\_external APIs

**\[Rule\]** The JS object created by **napi\_create\_external** APIs can be passed and used only in the calling thread. If it is passed across threads (for example, using **post\_message** of the **worker** interface), the application may crash. If a JS object bound with a native object needs to be passed across threads, use **napi\_coerce\_to\_native\_binding\_object** to bind the two objects. For details about the APIs, see [napi\_create\_external](../node-api-guides/working-with-objects-using-node-api/document.md#napi_create_external).

**Example (incorrect)**

static void MyFinalizeCB(napi\_env env, void \*finalize\_data, void \*finalize\_hint) { return; }

static napi\_value CreateMyExternal(napi\_env env, napi\_callback\_info info) {
    napi\_value result = nullptr;
    napi\_create\_external(env, nullptr, MyFinalizeCB, nullptr, &result);
    return result;
}

// The code for module registration is omitted here. You may need to register the CreateMyExternal method.

// index.d.ts
export const createMyExternal: () => Object;

// Application code.
import testNapi from 'libentry.so';
import { worker } from '@kit.ArkTS';

const mWorker = new worker.ThreadWorker('../workers/Worker');

{
    const mExternalObj = testNapi.createMyExternal();

    mWorker.postMessage(mExternalObj);

}

// Close the worker thread.
// The application may crash in this step or when the engine performs GC.
mWorker.terminate();
// The implementation of worker is the default template, which is omitted here.

#### Avoiding Releasing the Obtained Buffer Repeatedly

**\[Rule\]** The parameter **data** in certain APIs, such as **napi\_get\_arraybuffer\_info**, cannot be released manually. Its lifecycle is managed by the engine.

The following uses **napi\_get\_arraybuffer\_info** as an example to describe the interface definition:

napi\_get\_arraybuffer\_info(napi\_env env, napi\_value arraybuffer, void\*\* data, size\_t\* byte\_length)

The parameter **data** specifies the buffer header pointer to **ArrayBuffer**. This buffer can be read and written in the given range but cannot be released. The buffer memory is managed by the ArrayBuffer Allocator in the engine and is released with the lifecycle of the JS object **ArrayBuffer**.

**Example (incorrect)**

void\* arrayBufferPtr = nullptr;
napi\_value arrayBuffer = nullptr;
size\_t createBufferSize = ARRAY\_BUFFER\_SIZE;
napi\_status verification = napi\_create\_arraybuffer(env, createBufferSize, &arrayBufferPtr, &arrayBuffer);
size\_t arrayBufferSize;
napi\_status result = napi\_get\_arraybuffer\_info(env, arrayBuffer, &arrayBufferPtr, &arrayBufferSize);
delete arrayBufferPtr; // This operation is not allowed and may cause a double free of the buffer. The lifecycle of the created arrayBufferPtr is managed by the engine and cannot be manually deleted.

| Applicable APIs |
| :-- |
| napi\_create\_arraybuffer |
| napi\_create\_sendable\_arraybuffer |
| napi\_get\_arraybuffer\_info |
| napi\_create\_buffer |
| napi\_get\_buffer\_info |
| napi\_get\_typedarray\_info |
| napi\_get\_dataview\_info |

#### Others

**\[Suggestion\]** Properly use **napi\_object\_freeze** and **napi\_object\_seal**.

**napi\_object\_freeze** is equivalent to **Object.freeze**. After an object is frozen, all its properties are immutable. **napi\_object\_seal** is equivalent to **Object.seal**. After an object is sealed, no properties can be added or deleted, but the existing property values are mutable.

If the semantics are violated in strict mode (default), an error will be thrown.

#### Reference

[Communication Between Native Child Threads and the UI Main Thread](https://developer.huawei.com/consumer/en/doc/best-practices-V5/bpta-native-sub-main-comm-V5)

[How do I directly call ArkTS APIs in a C++ subthread on the native side without triggering callbacks on the ArkTS side?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs-V5/faqs-ndk-8-V5)

\[Are napi\_env and napi\_value instances shared across worker threads?\] ([https://developer.huawei.com/consumer/en/doc/harmonyos-faqs-V5/faqs-ndk-55-V5](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs-V5/faqs-ndk-55-V5))

[How do I create a subthread on the native side? What are the restrictions? How does the native subthread communicate with the main thread?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs-V5/faqs-ndk-68-V5)
