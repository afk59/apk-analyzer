# Implementing Asynchronous Operations Using JSVM-API

#### Introduction

JSVM-API provides APIs for implementing asynchronous operations. An asynchronous operation is used for a time-consuming task, for example, downloading data from network or reading a large file. Unlike a synchronous operation which blocks the main thread, the asynchronous operation is executed in the background. When an asynchronous operation is complete, it will be put into the task queue and executed when the main thread is idle.

#### Basic Concepts

**Promise** is an object used to handle asynchronous operations in JavaScript (JS). It has three states: **pending**, **fulfilled**, and **rejected**. The initial state is **pending**, which can be changed to **fulfilled** by **resolve()** and to **rejected** by **reject()**. Once the state is **fulfilled** or **rejected**, the promise state cannot be changed. Read on the following to learn basic concepts related to **Promise**:

-   Synchronous: Code is executed line by line in sequence. Each line of code is executed after the previous line of code is executed. During synchronous execution, if an operation takes a long time, the execution of the entire application will be blocked until the operation is complete.
-   Asynchronous: Tasks can be executed concurrently without waiting for the end of the previous task. In JS, common asynchronous operations apply for timers, event listening, and network requests. Instead of blocking subsequent tasks, the asynchronous task uses a callback or promise to process its result.
-   **Promise**: a JS object used to handle asynchronous operations. Generally, it is exposed externally by using **then()**, **catch()**, or **finally()** to custom logic.
-   **deferred**: a utility object associated with the **Promise** object to set **resolve()** and **reject()** of **Promise**. It is used internally to maintain the state of the asynchronous model and set the **resolve()** and **reject()** callbacks.
-   **resolve**: a function used to change the promise state from **pending** to **fulfilled**. The parameters passed to **resolve()** can be obtained from **then()** of the **Promise** object.
-   **reject**: a function used to change the promise state from **pending** to **rejected**. The parameters passed to **reject()** can be obtained from **catch()** of the **Promise** object.

**Promise** allows multiple callbacks to be called in a chain, providing better code readability and a better way to deal with asynchronous operations. JSVM-API provides APIs for implementing JS promises in C/C++.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_IsPromise | Checks whether the given **JSVM\_Value** is a **Promise** object. |
| OH\_JSVM\_CreatePromise | Creates a **deferred** object and a JS promise. |
| OH\_JSVM\_ResolveDeferred | Resolves a JS promise by using the **deferred** object associated with it. |
| OH\_JSVM\_RejectDeferred | Rejects a JS promise by using the **deferred** object associated with it. |
| OH\_JSVM\_PromiseRegisterHandler | Registers a callback to be invoked after a promise is fulfilled or rejected. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in promise development.

## OH\_JSVM\_IsPromise

Call **OH\_JSVM\_IsPromise** to check whether the given **JSVM\_Value** is a **Promise** object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_IsPromise.
static JSVM\_Value IsPromise(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    bool isPromise = false;
    JSVM\_Status status = OH\_JSVM\_IsPromise(env, args\[0\], &isPromise);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_IsPromise fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_IsPromise success:%{public}d", isPromise);
    }
    JSVM\_Value result = nullptr;
    OH\_JSVM\_GetBoolean(env, isPromise, &result);
    return result;
}
// Register the IsPromise callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsPromise},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the IsPromise method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isPromise", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(isPromise())JS";

Expected result:

JSVM OH\_JSVM\_IsPromise success:0

## OH\_JSVM\_CreatePromise

Call **OH\_JSVM\_CreatePromise** to create a **Promise** object.

## OH\_JSVM\_ResolveDeferred and OH\_JSVM\_RejectDeferred

Call **OH\_JSVM\_ResolveDeferred** to change the promise state from **pending** to **fulfilled**, and call **OH\_JSVM\_RejectDeferred** to change the promise state from **pending** to **rejected**.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CreatePromise, OH\_JSVM\_ResolveDeferred, and OH\_JSVM\_RejectDeferred.
static JSVM\_Value CreatePromise(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Deferred defer = nullptr;
    JSVM\_Value promise = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreatePromise(env, &defer, &promise);
    bool isPromise = false;
    JSVM\_Value returnIsPromise = nullptr;
    OH\_JSVM\_IsPromise(env, promise, &isPromise);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreatePromise fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreatePromise success:%{public}d", isPromise);
    }
    // Convert the Boolean value to JSVM\_Value and return it.
    OH\_JSVM\_GetBoolean(env, isPromise, &returnIsPromise);
    return returnIsPromise;
}

static JSVM\_Value ResolveRejectDeferred(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain and parse parameters.
    size\_t argc = 3;
    JSVM\_Value args\[3\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // The first parameter is the data to be passed to Resolve(), the second parameter is the data to be passed to reject(), and the third parameter is the Promise state.
    bool status = false;
    OH\_JSVM\_GetValueBool(env, args\[2\], &status);
    // Create a Promise object.
    JSVM\_Deferred deferred = nullptr;
    JSVM\_Value promise = nullptr;
    JSVM\_Status createStatus = OH\_JSVM\_CreatePromise(env, &deferred, &promise);
    if (createStatus != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "Create promise failed");
        return nullptr;
    }
    // Set the promise state based on the third parameter.
    if (status) {
        OH\_JSVM\_ResolveDeferred(env, deferred, args\[0\]);
        OH\_LOG\_INFO(LOG\_APP, "OH\_JSVM\_ResolveDeferred resolve");
    } else {
        OH\_JSVM\_RejectDeferred(env, deferred, args\[1\]);
        OH\_LOG\_INFO(LOG\_APP, "OH\_JSVM\_RejectDeferred reject");
    }
    JSVM\_Value result = nullptr;
    OH\_JSVM\_GetBoolean(env, true, &result);
    return result;
}
// Register the CreatePromise and ResolveRejectDeferred callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreatePromise},
    {.data = nullptr, .callback = ResolveRejectDeferred},
};
static JSVM\_CallbackStruct \*method = param;
// Aliases for the CreatePromise and ResolveRejectDeferred methods to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createPromise", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"resolveRejectDeferred", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(createPromise();
                                 resolveRejectDeferred('success', 'fail', true);
                                 resolveRejectDeferred('success', 'fail', false);)JS";

Expected result:

JSVM CreatePromise success:1
OH\_JSVM\_ResolveDeferred resolve
OH\_JSVM\_RejectDeferred reject

#### OH\_JSVM\_PromiseRegisterHandler

Call **OH\_JSVM\_PromiseRegisterHandler** to register a callback that is invoked after a promise is fulfilled rejected. It is equivalent to calling the native **Promise.then()** or **Promise.catch()**.

The following describes only part of the C++ code. For details about other framework code, such as the **TestJSVM** function, see the implementation of **OH\_JSVM\_SetMicrotaskPolicy** in [Working with Tasks Using JSVM-API](../working-with-tasks-using-jsvm-api/document.md).

static int PromiseRegisterHandler(JSVM\_VM vm, JSVM\_Env env) {
    const char \*defineFunction = R"JS(
        var x1 = 0;
        var x2 = 0;
        function f1(x) {
            x1 = x;
            return x + 1;
        }
        function f2(x) {
            x2 = x;
            return x + 1;
        }
    )JS";

    const char \*init = R"JS(
        x1 = 0;
        x2 = 0;
    )JS";

    JSVM\_Script script;
    JSVM\_Value jsSrc;
    JSVM\_Value result;

    // Define the JS functions f1 and f2.
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, defineFunction, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));

    // Initialize x1 and x2 to 0.
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, init, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));

    // Obtain functions f1 and f2.
    JSVM\_Value global;
    CHECK\_RET(OH\_JSVM\_GetGlobal(env, &global));
    JSVM\_Value f1;
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "f1", &f1));
    JSVM\_Value f2;
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "f2", &f2));

    // Create a promise.
    JSVM\_Value promise;
    JSVM\_Deferred deferred;
    CHECK\_RET(OH\_JSVM\_CreatePromise(env, &deferred, &promise));
    // Register a callback for the promise and assign the result (new promise) of then() to promise1.
    JSVM\_Value promise1;
    CHECK\_RET(OH\_JSVM\_PromiseRegisterHandler(env, promise, f1, nullptr, &promise1));
    // Register a callback for promise1.
    CHECK\_RET(OH\_JSVM\_PromiseRegisterHandler(env, promise1, f2, nullptr, nullptr));

    // Obtain the values of x1 and x2 before the promise is parsed.
    JSVM\_Value x1;
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "x1", &x1));
    int32\_t x1Int = 0;
    CHECK\_RET(OH\_JSVM\_GetValueInt32(env, x1, &x1Int));
    JSVM\_Value x2;
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "x2", &x2));
    int32\_t x2Int = 0;
    CHECK\_RET(OH\_JSVM\_GetValueInt32(env, x2, &x2Int));
    OH\_LOG\_INFO(LOG\_APP, "Before promise resolved, x1: %{public}d, x2: %{public}d", x1Int, x2Int);

    // Parse the promise.
    JSVM\_Value resolveValue;
    CHECK\_RET(OH\_JSVM\_CreateInt32(env, 2, &resolveValue));
    if (deferred != nullptr) {
        OH\_JSVM\_ResolveDeferred(env, deferred, resolveValue);
        deferred = nullptr;
    }

    // Obtain the values of x1 and x2 after the promise is parsed.
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "x1", &x1));
    CHECK\_RET(OH\_JSVM\_GetValueInt32(env, x1, &x1Int));
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "x2", &x2));
    CHECK\_RET(OH\_JSVM\_GetValueInt32(env, x2, &x2Int));
    OH\_LOG\_INFO(LOG\_APP, "After promise resolved, x1: %{public}d, x2: %{public}d", x1Int, x2Int);

    return 0;
}

static void RunDemo(JSVM\_VM vm, JSVM\_Env env) {
    if (PromiseRegisterHandler(vm, env) != 0) {
        OH\_LOG\_INFO(LOG\_APP, "Run PromiseRegisterHandler failed");
    }
}

Expected result:

Before promise resolved, x1: 0, x2: 0
After promise resolved, x1: 2, x2: 3
