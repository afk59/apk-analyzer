# Implementing Asynchronous Operations Using Node-API

#### Introduction

Node-API provides APIs for implementing asynchronous operations for time-consuming tasks, such as downloading data from network or reading a large file. Unlike synchronous operations, asynchronous operations are executed in the background without blocking the main thread. When an asynchronous operation is complete, it will be added to the task queue and executed when the main thread is idle.

#### Basic Concepts

A promise is an object used to handle asynchronous operations in ArkTS. It has three states: **pending**, **fulfilled**, and **rejected**. The initial state of a promise is **pending**. The **resolve** function changes its state from **pending** to **fulfilled**, while the **reject** function changes its state from **pending** to **rejected**. Once the state becomes **fulfilled** or **rejected**, it cannot be changed. The basic concepts are as follows:

-   **Synchronous**: Code is executed line by line in sequence. Each line of code is executed after the previous line of code is executed. If an operation takes a long time, the entire application will be blocked.
-   **Asynchronous**: Tasks can be executed concurrently without waiting for the end of the previous task. Common asynchronous operations apply for timers, event listening, and network requests. Instead of blocking subsequent tasks, the asynchronous task uses a callback or promise to process its result.
-   **Promise**: an ArkTS object used to handle asynchronous operations. It is customized by using **then()**, **catch()**, and **finally()**.
-   **deferred**: an object used to control the promise state. It can be used to mark the promise state as **fulfilled** or **rejected** at a future time.
-   **resolve**: a function used to change the promise state from **pending** to **fulfilled**. The parameters passed to **resolve()** can be obtained from **then()** of the **Promise** object.
-   **reject**: a function used to change the promise state from **pending** to **rejected**. The parameters passed to **reject()** can be obtained from **catch()** of the **Promise** object.

**Promise** allows multiple callbacks to be called in a chain, providing better code readability and a better way to deal with asynchronous operations. The APIs provided by the Node-API module help you flexibly process ArkTS asynchronous operations in C/C++.

#### Available APIs

The following table lists the APIs for implementing asynchronous operations using ArkTS promises.

| API | Description |
| :-- | :-- |
| napi\_is\_promise | Checks whether a **napi\_value** is a **Promise** object. |
| napi\_create\_promise | Creates a **Promise** object. |
| napi\_resolve\_deferred | Resolves a promise by using the **deferred** object associated with it. |
| napi\_reject\_deferred | Rejects a promise by using the **deferred** object associated with it |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to promise development.

## napi\_is\_promise

Call **napi\_is\_promise** to check whether the given **napi\_value** is a **Promise** object.

CPP code:

// napi\_is\_promise
static napi\_value IsPromise(napi\_env env, napi\_callback\_info info)
{
    napi\_value argv\[1\] = {nullptr};
    size\_t argc = 1;
    napi\_status status;
    // Obtain the parameters passed in.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    bool isPromise = false;
    // Check whether the given parameter is a Promise object and save the result in the isPromise variable.
    status = napi\_is\_promise(env, argv\[0\], &isPromise);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_is\_promise failed");
        return nullptr;
    }
    napi\_value result = nullptr;
    // Convert the value of isPromise to the type specified by napi\_value, and return it.
    napi\_get\_boolean(env, isPromise, &result);
    return result;
}

API declaration:

export const isPromise: <T>(value: T) => boolean; // napi\_is\_promise

ArkTS code:

// napi\_is\_promise
let value = Promise.resolve();
// Return true if the object passed in is a promise; return false otherwise.
hilog.info(0x0000, 'Node-API', 'napi\_is\_promise %{public}s', testNapi.isPromise(value));
hilog.info(0x0000, 'Node-API', 'napi\_is\_promise string %{public}s', testNapi.isPromise(''));

## napi\_create\_promise

Call **napi\_create\_promise** to create a **Promise** object.

When using this API, observe to the following:

1.  If **napi\_create\_promise** is called when there is an exception not handled, **napi\_pending\_exception** will be returned.
2.  After calling **napi\_create\_promise**, always check whether the return value is **napi\_ok**. If **deferred** and **promise** are used, the application will crash.

napi\_value NapiPromiseDemo(napi\_env env, napi\_callback\_info info)
{
    napi\_deferred deferred = nullptr;
    napi\_value promise = nullptr;
    napi\_status status = napi\_ok;

    napi\_throw\_error(env, "500", "common error");

    status = napi\_create\_promise(env, &deferred, &promise); // If there is an error, return napi\_pending\_exception with deferred and promise set to nullptr.
    if (status == napi\_ok) {
        // do something
    }

    return nullptr;
}

## napi\_resolve\_deferred & napi\_reject\_deferred

Call **napi\_resolve\_deferred** to change the promise state from **pending** to **fulfilled**, and call **napi\_reject\_deferred** to change the promise state from **pending** to **rejected**.

To ensure execution of microtasks, the ArkTS runtime will trigger a microtask execution when fulfilling a promise using Node-API.

CPP code:

// napi\_resolve\_deferred & napi\_reject\_deferred
static napi\_value CreatePromise(napi\_env env, napi\_callback\_info info)
{
    // deferred is an object associated with the promise object and is used to control the promise state (resolve or reject).
    napi\_deferred deferred = nullptr;
    napi\_value promise = nullptr;
    // Create a Promise object.
    napi\_status status = napi\_create\_promise(env, &deferred, &promise);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Create promise failed");
        return nullptr;
    }
    //Call napi\_is\_promise to check whether the object created by napi\_create\_promise is a Promise object.
    bool isPromise = false;
    napi\_value returnIsPromise = nullptr;
    status = napi\_is\_promise(env, promise, &isPromise);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_is\_promise failed");
        return nullptr;
    }
    // Convert the Boolean value to napi\_value and return it.
    napi\_get\_boolean(env, isPromise, &returnIsPromise);
    return returnIsPromise;
}

static napi\_value ResolveRejectDeferred(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse parameters.
    size\_t argc = 3;
    napi\_value args\[3\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // The first parameter is the data to be passed to Resolve(), the second parameter is the data to be passed to reject(), and the third parameter is the Promise state.
    bool promiseStatus;
    napi\_status status = napi\_get\_value\_bool(env, args\[INT\_ARG\_2\], &promiseStatus);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_get\_value\_bool failed");
        return nullptr;
    }

    // Create a Promise object.
    napi\_deferred deferred = nullptr;
    napi\_value promise = nullptr;
    status = napi\_create\_promise(env, &deferred, &promise);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Create promise failed");
        return nullptr;
    }
    // Set the promise state based on the third parameter.
    if (promiseStatus) {
        napi\_resolve\_deferred(env, deferred, args\[INT\_ARG\_0\]);
    } else {
        napi\_reject\_deferred(env, deferred, args\[INT\_ARG\_1\]);
    }
    // Return the Promise object with the state set.
    return promise;
}

API declaration example:

export const createPromise: () => boolean | undefined; // napi\_resolve\_deferred & napi\_reject\_deferred

export const resolveRejectDeferred: (resolve: string, reject: string, status: boolean) => Promise<string> | undefined;

ArkTS code:

// napi\_resolve\_deferred & napi\_reject\_deferred
// Create a promise. Return true if the operation is successful, and return false otherwise.
hilog.info(0x0000, 'Node-API', 'napi\_create\_promise %{public}s', testNapi.createPromise());
// Call resolveRejectDeferred to resolve or reject the promise and set the promise state.
// Resolve the promise. The return value is passed to the then function.
let promiseSuccess: Promise<string> =
  testNapi.resolveRejectDeferred('success', 'fail', true) as Promise<string>;
promiseSuccess.then((res) => {
  hilog.info(0x0000, 'Node-API', 'get\_resolve\_deferred resolve %{public}s', res);
  // ...
}).catch((err: Error) => {
  hilog.info(0x0000, 'Node-API', 'get\_resolve\_deferred reject %{public}s', err);
  // ...
})
// Reject the promise. The return value is passed to the catch function.
let promiseFail: Promise<string> =
  testNapi.resolveRejectDeferred('success', 'fail', false) as Promise<string>;
promiseFail.then((res) => {
  hilog.info(0x0000, 'Node-API', 'get\_resolve\_deferred resolve %{public}s', res);
  // ...
}).catch((err: Error) => {
  hilog.info(0x0000, 'Node-API', 'get\_resolve\_deferred reject %{public}s', err);
  // ...
})

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
