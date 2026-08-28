# FAQs About Basic Functionalities

#### What should I do if the module fails to be loaded and the error message "Error message: is not callable" is displayed?

-   Question:

When the **libxxx.so** file provided by the following module registration code is used to call the API of the dynamic library in some projects, **Error message: is not callable** is displayed.

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "xxx",
    .nm\_priv = nullptr,
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule()
{
    napi\_module\_register(&demoModule);
}

-   Answer:

1.  You can locate and resolve the issue based on the following topics:
    
    [What should I do if an error message "undefined" is displayed on the ArkTS side](#what-should-i-do-if-an-error-message-undefined-is-displayed-on-the-arkts-side)
    
    [Module Registration and Naming](../../node-api-development-specifications/document.md#module-registration-and-naming)
    
2.  You can also check whether the dynamic loading capability is sufficient for this scenario.
    
    [Scenarios Supported by napi\_load\_module\_with\_info](../../typical-node-api-use-cases/loading-a-module-using-node-api/document.md#scenarios-supported-by-napi_load_module_with_info)
    
    [Scenarios Supported by napi\_load\_module](../../typical-node-api-use-cases/loading-a-module-in-the-main-thread-using-node-api/document.md#scenarios-supported-by-napi_load_module)
    

#### How to ensure the order of asynchronous tasks in scenarios where a large number of ArkTS methods need to be called for communication

-   Question: In a scenario where a large number of ArkTS methods need to be called through C++ for communication, how to ensure the order of asynchronous tasks?
-   Answer:

You can use **napi\_call\_threadsafe\_function** to ensure the execution sequence of asynchronous tasks. Ensure that the asynchronous tasks are delivered to the ArkTS thread for execution. If the asynchronous tasks are delivered to the main thread, the application may freeze and exit if they are executed for a long time. Therefore, you are not advised to deliver long-time tasks to the main thread through thread-safe functions.

[Thread Safety Development Using Node-API](../../typical-node-api-use-cases/thread-safety-development-using-node-api/document.md)

In addition, the differences between the common task throwing methods in Node-API are as follows:

1.  The **napi\_async\_work** APIs can ensure that **execute\_cb** is executed before **complete\_cb**, but cannot ensure the sequence of different **napi\_async\_work**.
    
    Based on the common **napi\_queue\_async\_work**, [napi\_queue\_async\_work\_with\_qos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/napi#napi_queue_async_work_with_qos) supports custom QoS priority. However, it only specifies the thread priority when libuv schedules tasks, not the task priority. Therefore, the task sequence cannot be ensured.
    
2.  The **napi\_threadsafe\_function** APIs maintain a queue to ensure the task execution sequence.
    
    **napi\_call\_threadsafe\_function** is executed in the first in first out (FIFO) sequence.
    
    **napi\_call\_threadsafe\_function\_with\_priority** is executed according to the specified queueing mode.
    

[Passing a Task with the Specified Priority to an ArkTS Thread from an Asynchronous Thread Using Node-API](../../typical-node-api-use-cases/passing-a-task-with-the-specified-priority-and-enqueuing-mode-to-an-arkts-thread/document.md)

#### Is there a convenient way to call back ArkTS

-   Question:

During multi-thread development, ArkTS functions can be executed only on the thread where they are created. C++ threads cannot call ArkTS callbacks in **napi\_call\_function** mode. Is there a convenient method?

References

[Implementing Communication Between Native Child Threads and the UI Main Thread](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-native-sub-main-comm)

[Asynchronous Task Development Using Node-API](../../typical-node-api-use-cases/asynchronous-task-development-using-node-api/document.md)

#### How do I call back the ArkTS method in C++ code?

-   References

[How do I invoke a function transferred from ArkTS in a C++ subthread?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-ndk-26)

#### How to ensure the correct mapping of data types and the security of memory management

-   Question: While complying with the single return value constraint of Node-API, how to securely and efficiently pass multiple return values (including structured data and pointer information) to the ArkTS runtime environment and ensure correct data type mapping and memory management security?
-   Answer:

Although the **napi\_value** API supports only a single return value, you can use the return value to encapsulate all required information.

For example, you can use **napi\_create\_object** to create an ArkTS object and use it to carry all returned information. **number** and **string** can be set to this object through the API set by properties such as **napi\_set\_property** or **napi\_set\_named\_property**. You can also use **napi\_wrap** to bind a native object to an ArkTS object, and then use **napi\_unwrap** to retrieve the native object.

In addition, you can use an ArkTS array to carry data, which is flexible.

-   References

[Working with Objects Using Node-API](../../node-api-guides/working-with-objects-using-node-api/document.md)

[Working with Arrays Using Node-API](../../node-api-guides/working-with-arrays-using-node-api/document.md)

#### What are the error codes of the napi\_get\_uv\_event\_loop API

Additional parameter verification is added to prevent use of invalid **napi\_env** in **napi\_get\_uv\_event\_loop**. The return value indicates the verification result. The return values of this API are as follows:

1.  If **env** and/or **loop** are **nullptr**, **napi\_invalid\_arg** is returned.
2.  If **env** is a valid **napi\_env** and **loop** is a valid pointer, **napi\_ok** is returned.
3.  If **env** is not a valid **napi\_env** (for example, a released **env**), **napi\_generic\_failure** is returned.

-   Example:

napi\_value NapiInvalidArg(napi\_env env, napi\_callback\_info)
{
    napi\_status status = napi\_ok;
    status = napi\_get\_uv\_event\_loop(env, nullptr); // loop is nullptr, and the status code is napi\_invalid\_arg.
    if (status == napi\_ok) {
        // do something
    }

    uv\_loop\_s\* loop = nullptr;
    status = napi\_get\_uv\_event\_loop(nullptr, &loop); // env is nullptr, and the status code is napi\_invalid\_arg.
    if (status == napi\_ok) {
        // do something
    }

    status = napi\_get\_uv\_event\_loop(nullptr, nullptr); // env and loop are nullptr, and the status code is napi\_invalid\_arg.
    if (status == napi\_ok) {
        // do something
    }

    return nullptr;
}

napi\_value NapiGenericFailure(napi\_env env, napi\_callback\_info)
{
    std::thread(\[\]() {
        napi\_env env = nullptr;
        napi\_create\_ark\_runtime(&env); // Generally, the return value needs to be checked.
        // napi\_destroy\_ark\_runtime sets the pointer to null. Copy the pointer to simulate the problem.
        napi\_env copiedEnv = env;
        napi\_destroy\_ark\_runtime(&env);
        uv\_loop\_s\* loop = nullptr;
        napi\_status status = napi\_get\_uv\_event\_loop(copiedEnv, &loop); // env is invalid, and the status code is napi\_generic\_failure.
        if (status == napi\_ok) {
            // do something
        }
    }).detach();
}

#### Must a function be passed to the native layer when the native layer calls the object method of the ArkTS layer

-   Question: When the native layer of Node-API calls an object method from the ArkTS layer, must a function be passed to the native layer?
-   Answer:

To call an object method of the ArkTS layer at the native layer, the native layer needs to obtain the ArkTS function object.

You can obtain the ArkTS function object in any of the following ways:

1.  Pass the function from the ArkTS layer to the native layer.
2.  Bind the ArkTS function to an object that can be accessed by the native layer by setting attributes. In this way, the native layer can obtain and call the function through the object.
3.  Node-API provides **napi\_create\_function** to create an ArkTS function object in the native layer. In this way, the native layer can obtain the ArkTS function object.

#### Can I call an ArkTS method and obtain the result

-   Question: Can the thread created by using **pthread** or **std::thread** in C++ call an ArkTS method and obtain the result?

Possible causes:

If the thread is created directly in C++, it does not have the ArkTS running environment, specifically the corresponding **napi\_env**. Calling ArkTS methods on the thread directly causes multi-thread security issues, which is an undefined behavior.

-   Answer:

1.  Use the Node-API of **napi\_threadsafe\_function** to throw tasks from the C++ thread to the ArkTS thread for executing the ArkTS method.
    
    [Thread Safety Development Using Node-API](../../typical-node-api-use-cases/thread-safety-development-using-node-api/document.md)
    
2.  Create an ArkTS running environment in the C++ thread.
    
    [Creating an ArkTS Runtime Environment Using Node-API](../../typical-node-api-use-cases/creating-an-arkts-runtime-environment-using-node-api/document.md)
    

#### Whether there is a napi\_get\_value\_string\_utf8 API or capability that does not need the copy operation

-   Question: The **napi\_get\_value\_string\_utf8** API of Node-API needs a copy operation each time it is called. Is there a **napi\_get\_value\_string\_utf8** API or capability that does not need the copy operation?
-   Answer:

No, **napi\_get\_value\_string\_utf8** always needs a copy operation.

It is necessary because the string lifecycle is involved. When GC is triggered, the ArkTS object may be moved to another place or reclaimed in the VM. If an address of a char\* type is returned, the memory may change after the object is moved or reclaimed.

#### What are the precautions for using napi\_env in multi-thread mode

-   Question:

What are the precautions for using **napi\_env** in multi-thread mode? Is there any exception caused by **napi\_env** switchover? Must **napi\_env** be used in the main thread?

-   Answer:

1.  **napi\_env** is bound to the ArkTS thread, so that it cannot be used across threads. Otherwise, stability issues may occur. References:
    
    [Multithread Processing](../../node-api-development-process/document.md#multithread-processing)
    
2.  When using **env** to call Node-APIs, note that most Node-APIs can only be called on the ArkTS thread to which **env** belongs. Otherwise, thread-safety issues may arise.
    
3.  Do not cache napi\_env. Otherwise, thread-safety issues and **use-after-free** issues may occur.
    
4.  [Why cannot napi\_env be cached?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-ndk-73)
    

#### What should I do if the napi\_call\_threadsafe\_function execution sequence does not meet the expectation

-   Question:

The expected execution sequence of **napi\_call\_threadsafe\_function** is a -> b -> c.

posttask(a);

posttask(b);

posttask(c);

However, the actual execution sequence is b -> a -> c.

-   Answer:

1.  Check whether the same **napi\_threadsafe\_function** instance is used. If not, the execution sequence may be different.
    
    Note: For the same **napi\_threadsafe\_function**, the execution sequence of **napi\_call\_threadsafe\_function** is guaranteed. The first function called is executed first.
    
2.  Check whether the actual call sequence of **napi\_threadsafe\_function** is a -> b -> c.
    

#### What should I do if an error message "undefined" is displayed on the ArkTS side

Question:

What should I do when "undefined/not callable" or specific error message is reported for xxx after "import xxx from libxxx.so" is executed on ArkTS?

1.  Check whether the module name in the .cpp file used in module registration is the same as that in the .so file name.
    
    If the module name is **entry**, the .so file name must be **libentry.so**, and the **nm\_modname** field in **napi\_module** must be **entry**. The module names must be of the same case.
    
2.  Check whether the .so file is successfully loaded.
    
    Check the logs related to module loading during the application startup. Search for the keyword "dlopen" and check for error information. Generally, a loading failure is caused when the file to be loaded does not exist or is in a blocklist or the application does not have the required permission. In multi-thread scenarios (such as worker threads and taskpool), check whether **nm\_modname** is the same as the module name. The module names must be of the same case.
    
3.  Check whether the dependency .so files are successfully loaded.
    
    Check that all the dependency .so files are packaged into the application and the application has the permission to open them.
    
    | **Error Log** | **Fault Analysis & Solution** |
    | :-- | :-- |
    | module $SO is not allowed to load in restricted runtime. | The module, identified by **$SO**, is not allowed for the worker thread running in a restricted environment and cannot be loaded. You are advised to delete the module. |
    | module $SO is in blocklist, loading prohibited. | The module, identified by **$SO**, is in the blocklist due to the control of the widget or Extension, and cannot be loaded. You are advised to delete the module. |
    | load module failed. $ERRMSG. | 
    The dynamic library fails to be loaded. **$ERRMSG** indicates the cause of the loading failure. Possible causes include the following:
    
    \- The .so file to be loaded does not exist.
    
    \- The dependency .so file does not exist.
    
    \- Undefined symbol is found.
    
    Locate the cause based on the error message.
    
     |
    | try to load abc file from $FILEPATH failed. | You can load either a dynamic library or an .abc file. If this log information is displayed when you attempt to load a dynamic library, ignore this message. If it is displayed when you attempt to load an .abc file, the .abc file does not exist. **$FILEPATH** indicates the module path. |
    
4.  If specific error message is reported, identify the fault based on the error message.
    
    | **Error message** | **Fault Analysis & Solution** |
    | :-- | :-- |
    | First attempt: $ERRMSG. | Loading the .so file with the module name of "xxx" fails. $ERRMSG indicates the error information. |
    | Second attempt: $ERRMSG. | Loading the .so file with the module name of "xxx\_napi" fails. $ERRMSG indicates the error information. |
    | try to load abc file from xxx failed. | Loading the .abc file fails. xxx indicates the name of the .abc file. |
    | module xxx is not allowed to load in restricted runtime. | This module cannot be used in restricted runtime. xxx indicates the module name. You are advised to delete the module. |
    | module xxx is in blocklist, loading prohibited. | The module cannot be used in the current extension. xxx indicates the module name. You are advised to delete the module. |
    

#### What should I do if the API execution result is unexpected

Question: What should I do when an unexpected value is returned by an API and "occur exception need return" is reported?

Before the call is complete, some Node-APIs are checked for ArkTS exceptions in the VM. If an exception is detected, "occur exception need return" will be reported, with the line number of the code and the Node-API name.

Answer:

-   If the exception does not matter, clear the exception.
    
    Call **napi\_get\_and\_clear\_last\_exception** before "occur exception need return" is printed to clear the exception.
    
-   Throw the exception to the ArkTS layer for capture.
    
    Throw the exception directly to the ArkTS layer without going through the native logic.
    

#### What are the differences between the lifecycle of napi\_value and napi\_ref

-   **napi\_value** is managed by **HandleScope**. Generally, you do not need to add **HandleScope** for **napi\_value** (except for complete callback of **uv\_queue\_work**).
    
-   **napi\_ref** must be deleted manually.
    

#### How do I locate the fault if the return value of a Node-API is not "napi\_ok"

When a Node-API is successfully executed, **napi\_ok** is returned. If the return value is not **napi\_ok**, see [Node-API Status Codes](../../node-api-status-codes/document.md).

Locate the fault as follows:

-   Check the result of the input parameter null check, which is performed first before a Node-API is executed. The code is as follows:
    
    CHECK\_ENV: null check for env.
    CHECK\_ARG: null check for other input parameters.
    
-   Check the result of the input parameter type check, which is performed for certain Node-APIs. For example, **napi\_get\_value\_double** is used to obtain a C double value from an ArkTS number, and the type of the ArkTS value passed in must be number. The parameter type check is as follows:
    
    RETURN\_STATUS\_IF\_FALSE(env, NativeValue->TypeOf() == Native\_NUMBER, napi\_number\_expected);
    
-   Check the return value, which contains the verification result of certain APIs. For example, **napi\_call\_function** is used to execute an ArkTS function. If an exception occurs in the ArkTS function, Node-API returns **napi\_pending\_exception**.
    
    // Internal implementation of the API. The status value is returned after verification.
    auto resultValue = engine->CallFunction(NativeRecv, NativeFunc, NativeArgv, argc);
    RETURN\_STATUS\_IF\_FALSE(env, resultValue != nullptr, napi\_pending\_exception)
    
-   Determine the status value returned, and analyze the situation in which the status value is returned.
    

#### How do I ensure that objects wrapped by napi\_wrap are destructed in the expected order

Question: When using **napi\_wrap** to bind two C++ objects to two JavaScript objects, I need to ensure that the first C++ object is destroyed before the second, since the first depends on the second. However, the JavaScript garbage collection (GC) time is uncertain. If the C++ objects are destroyed directly in the **finalize\_cb** callback of **napi\_wrap**, the destruction sequence cannot meet the requirements. How do I ensure the destruction sequence of two C++ objects?

Answer:

Mark both A and B as releasable and release the C++ object at the same time.

Principle: All the release logic of dependent objects is processed in the **finalize\_cb** of the last ArkTS object to be destroyed.

Procedure:

Mark **cppObjA** as to-be-destroyed (not released immediately) in **finalize\_cb** of **jsObjA**.

Mark **cppObjB** as to-be-destroyed (not released immediately) in **finalize\_cb** of **jsObjB**.

When **jsObjA** and **jsObjB** are to be destroyed, destroy **cppObjA** and **cppObjB** in sequence.

The sample code is as follows:

struct ObjectPair {
    CppObjA\* objA;
    CppObjB\* objB;
    bool objADestroyedA = false;
    bool objADestroyedB = false;
};

// finalize callback of jsObjA.
void FinalizeA(napi\_env env, void\* data, void\* hint) {
    ObjectPair\* pair = static\_cast<ObjectPair\*>(data);
    pair->objADestroyedA = true;
    if (pair->objADestroyedA && pair->objADestroyedB) {
        delete pair->objA; // Ensure that object A is destroyed first.
        delete pair->objB; // Destroy object B.
        delete pair;       // Release the wrapper structure.
    }
}

// finalize callback of jsObjB.
void FinalizeB(napi\_env env, void\* data, void\* hint) {
    ObjectPair\* pair = static\_cast<ObjectPair\*>(data);
    pair->objADestroyedB = true;
    if (pair->objADestroyedA && pair->objADestroyedB) {
        delete pair->objA; // Ensure that object A is destroyed first.
        delete pair->objB; // Destroy object B.
        delete pair;       // Release the wrapper structure.
    }
}

#### What should I do if the napi\_call\_threadsafe\_function callback task is not executed

Answer:

Cause 1: The return value of **napi\_call\_threadsafe\_function** is not **napi\_ok**. Check whether all the return values of the **napi\_call\_threadsafe\_function** calls are **napi\_ok**. If not, locate the cause by referring to [Node-API Status Codes](../../node-api-status-codes/document.md).

Cause 2: The ArkTS thread to which **env** belongs is blocked. The callback of **napi\_call\_threadsafe\_function** is executed on the ArkTS thread to which **env** belongs. If the ArkTS thread is blocked, the thread-safe function callback will not be executed.

Cause 3: The **uv\_async\_t** handle of the thread-safe function is re-initialized, and the task is not executed. All **uv\_async\_t** handles created during the first initialization and repeated initialization cannot be accessed by uv. Since the thread-safe function is implemented based on the **uv\_async\_t** mechanism, it is invalid in this scenario.

#### How to use development tools to quickly develop Node-APIs using C/C++ code?

HarmonyOS provides various Node-API examples. You can quickly learn the Node-API module development process by referring to the guides and sample projects.

With development tools such as [AKI](https://gitcode.com/openharmony-sig/aki) and [napi-generator](https://gitcode.com/openharmony/napi_generator), you can develop Node-APIs more easily and efficiently.
