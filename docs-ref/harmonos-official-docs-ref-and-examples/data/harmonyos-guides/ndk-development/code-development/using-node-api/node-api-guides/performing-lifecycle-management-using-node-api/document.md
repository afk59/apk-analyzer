# Performing Lifecycle Management Using Node-API

#### Introduction

In Node-API, **napi\_value** is an abstract data type that represents an ArkTS value of any type, which includes the basic type (such as number, string, or Boolean) and the composite type (such as array, function, or object).

The **napi\_value** lifecycle is closely related to the lifecycle of the ArkTS value. When an ArkTS value is garbage-collected, the **napi\_value** associated with it is no longer valid. Avoid using the **napi\_value** when the ArkTS value no longer exists.

Scope is used to manage the **napi\_value** lifecycle in the framework layer. You can use **napi\_open\_handle\_scope** to open a scope and use **napi\_close\_handle\_scope** to close it. By creating a **napi\_value** in a scope, you can ensure that the **napi\_value** is automatically released when the scope ends. This helps prevent memory leaks.

**napi\_ref** is a Node-API type used to manage the **napi\_value** lifecycle. It allows reference to a **napi\_value** during its lifecycle, even if the value is beyond its original context. The reference allows a **napi\_value** to be shared in different contexts and released in a timely manner.

#### Basic Concepts

Node-API provides APIs for creating and manipulating ArkTS objects, managing references to and lifecycle of the ArkTS objects, and registering garbage collection (GC) callbacks in C/C++. Before you get started, you need to understand the following concepts:

-   **Scope**: Used to manage the lifecycle of ArkTS objects. Object handles created in a scope can be used only within the scope by default. After the scope is closed, the objects created in the scope cannot be accessed unless they are explicitly escaped from the current scope.
-   Reference management: Node-API provides APIs for creating, deleting, and managing object references to extend the lifecycle of objects and prevent the use-after-free issues. In addition, reference management also helps prevent memory leaks.
-   Escapable scope: used to return the values created within the **escapable\_handle\_scope** to a parent scope. It is created by **napi\_open\_escapable\_handle\_scope** and closed by **napi\_close\_escapable\_handle\_scope**.
-   GC callback: You can register GC callbacks to perform specific cleanup operations when ArkTS objects are garbage-collected.

Understanding these concepts helps you securely and effectively manipulate ArkTS objects in C/C++ and perform object lifecycle management.

#### Available APIs

The following table lists the APIs for ArkTS object lifecycle management.

| API | Description |
| :-- | :-- |
| 
napi\_open\_handle\_scope

napi\_close\_handle\_scope

 | Opens a scope and closes a scope respectively. When processing ArkTS objects with Node-API, you need to create a temporary scope to store object references so that the objects can be correctly accessed during the execution and closed after the execution. |
| 

napi\_open\_escapable\_handle\_scope

napi\_close\_escapable\_handle\_scope

 | Creates an escapable scope so that the ArkTS object created in the native function can be correctly returned to the external ArkTS environment that calls the function. |
| napi\_escape\_handle | Promotes the handle to an ArkTS object so that it is valid for the lifetime of its parent scope. |
| 

napi\_create\_reference

napi\_delete\_reference

 | Creates a reference to a value to extend the ArkTS object's lifespan and deletes a reference respectively. |
| 

napi\_reference\_ref

napi\_reference\_unref

 | Increments the reference count and decrements the reference count respectively. |
| napi\_get\_reference\_value | Obtains the ArkTS object associated with the reference. |
| napi\_add\_finalizer | Adds a **napi\_finalize** callback, which will be called to clean up or release resources before the ArkTS object is garbage-collected. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to lifecycle management.

The following header files are required for the C++ code:

#include "napi/native\_api.h"
// log.h is used to print logs in C++.
#include "hilog/log.h"

The following modules are required for the ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

## napi\_open\_handle\_scopemarkdownBrRepalcenapi\_close\_handle\_scope

Use **napi\_open\_handle\_scope** to create a context and use **napi\_close\_handle\_scope** to close the context. You can use these two APIs to manage the **napi\_value** lifecycle of an ArkTS object, which prevents the object from being incorrectly garbage-collected.

Note that the API supports only the single-layer nested scope structure. There is only one active scope at any time, and all newly created handles will be associated with that scope. Scopes must be closed in the reverse order of opening. In addition, all scopes created in the native method must be closed before the method returns.

For details about the code of lifecycle management, see:

[Lifecycle Management](../../node-api-development-specifications/document.md#lifecycle-management)

For details about the code of typical incorrect usage, see:

[Typical Error Scenarios](../../node-api-faqs/faqs-about-stability/document.md#what-are-the-typical-error-scenarios-of-lifecycle-related-development-between-napi_open_handle_scope-and-napi_close_handle_scope)

CPP code:

// napi\_open\_handle\_scope, napi\_close\_handle\_scope
static napi\_value HandleScopeTest(napi\_env env, napi\_callback\_info info)
{
    // Call napi\_open\_handle\_scope to open a scope.
    napi\_handle\_scope scope;
    napi\_open\_handle\_scope(env, &scope);
    // Create an object within the scope.
    napi\_value obj = nullptr;
    napi\_create\_object(env, &obj);
    // Add a property to the object.
    napi\_value value = nullptr;
    napi\_create\_string\_utf8(env, "handleScope", NAPI\_AUTO\_LENGTH, &value);
    napi\_set\_named\_property(env, obj, "key", value);
    // Obtain the object property in the scope and return it.
    napi\_value result = nullptr;
    napi\_get\_named\_property(env, obj, "key", &result);
    // Close the scope. Then, the object handle created within the scope is automatically released.
    napi\_close\_handle\_scope(env, scope);
    // result has left the scope. If it is used, stability problems may occur. To use objects outside the scope, you are advised to use the napi\_open\_escapable\_handle\_scope APIs.
    return nullptr;
}

static napi\_value HandleScope(napi\_env env, napi\_callback\_info info)
{
    // Call napi\_open\_handle\_scope to open a scope.
    napi\_handle\_scope scope;
    napi\_open\_handle\_scope(env, &scope);
    // Create an object within the scope.
    napi\_value obj = nullptr;
    napi\_create\_object(env, &obj);
    // Add a property to the object.
    napi\_value value = nullptr;
    napi\_create\_string\_utf8(env, "handleScope", NAPI\_AUTO\_LENGTH, &value);
    napi\_set\_named\_property(env, obj, "key", value);
    // Close the scope. Then, the object handle created within the scope is automatically released.
    napi\_close\_handle\_scope(env, scope);
    // Obtain and return the object property outside the scope. In this example, "undefined" is obtained.
    napi\_value result = nullptr;
    napi\_get\_named\_property(env, obj, "key", &result);
    return result;
}

API declaration:

index.d.ts

export const handleScopeTest: () => string; // napi\_open\_handle\_scope, napi\_close\_handle\_scope

export const handleScope: () => string;

ArkTS code:

// napi\_open\_handle\_scope  napi\_close\_handle\_scope
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API handleScopeTest: %{public}s',
    testNapi.handleScopeTest());
  hilog.info(0x0000, 'testTag', 'Test Node-API handleScope: %{public}s', testNapi.handleScope());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag',
    'Test Node-API handleScopeTest errorCode: %{public}s, errorMessage: %{public}s', error.code,
    error.message);
  // ...
}

The framework layer defines the API mapping table between the ArkTS and native sides in the core initialization function **Init**. When the ArkTS side accesses the native function through the API in the mapping table, the framework layer automatically adds the scope. You do not need to add the **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** APIs to manage the lifecycle of ArkTS objects. That is, the scope is automatically opened when the native function is called and automatically closed when the native function ends. The lifecycle of the ArkTS object created in the native function ends when the native function returns, and no memory leak occurs. The following example defines the **NewObject** function. (You do not need to add **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** to define the function in the API mapping table to manage the lifecycle of the ArkTS object.)

// Open the scope before calling NewObject.
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
    // After the result leaves the scope, the object handle is released, and the object returned to ArkTS is managed by ArkTS.
    return object;
}
// The framework layer closes the scope after the NewObject function call ends.

// Core initialization function.
static napi\_value Init(napi\_env env, napi\_value exports)
{
    // Define the API mapping table.
    napi\_property\_descriptor desc\[\] = {
        { "newObject", nullptr, NewObject, nullptr, nullptr, nullptr, napi\_default, nullptr }
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}

## napi\_open\_escapable\_handle\_scope, napi\_close\_escapable\_handle\_scope, and napi\_escape\_handle

Use **napi\_open\_escapable\_handle\_scope** to open an escapable scope, which allows the declared values in the scope to be returned to the parent scope. The scope must be closed using **napi\_close\_escapable\_handle\_scope**. Use **napi\_escape\_handle** to promote the lifecycle of an ArkTS object so that it is valid for the lifetime of the parent scope.

These APIs are helpful for managing ArkTS objects more flexibly in C/C++, especially when passing cross-scope values.

CPP code:

// napi\_open\_escapable\_handle\_scope, napi\_close\_escapable\_handle\_scope, and napi\_escape\_handle
static napi\_value EscapableHandleScopeTest(napi\_env env, napi\_callback\_info info)
{
    // Create an escapable scope.
    napi\_escapable\_handle\_scope scope;
    napi\_open\_escapable\_handle\_scope(env, &scope);
    // Create an object within the escapable scope.
    napi\_value obj = nullptr;
    napi\_create\_object(env, &obj);
    // Add a property to the object.
    napi\_value value = nullptr;
    napi\_create\_string\_utf8(env, "Test napi\_escapable\_handle\_scope", NAPI\_AUTO\_LENGTH, &value);
    napi\_set\_named\_property(env, obj, "key", value);
    napi\_value prop = nullptr;
    napi\_get\_named\_property(env, obj, "key", &prop);
    // Call napi\_escape\_handle to escape the property value to a scope outside.
    napi\_value result = nullptr;
    napi\_escape\_handle(env, scope, prop, &result);
    // Close the escapable scope to clear resources.
    napi\_close\_escapable\_handle\_scope(env, scope);
    // The escaped result can be used outside the scope.
    return result;
}

API declaration:

index.d.ts

export const escapableHandleScopeTest: () => string; // napi\_open\_escapable\_handle\_scope, napi\_close\_escapable\_handle\_scope, and napi\_escape\_handle

ArkTS code:

// napi\_open\_escapable\_handle\_scope, napi\_close\_escapable\_handle\_scope, and napi\_escape\_handle
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API EscapableHandleScopeTest: %{public}s',
    testNapi.escapableHandleScopeTest());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag',
    'Test Node-API EscapableHandleScopeTest errorCode: %{public}s, errorMessage: %{public}s',
    error.code,
    error.message);
  // ...
}

## napi\_ref

Use **napi\_ref** to manage the lifecycle of ArkTS objects. **napi\_ref** is a reference type, which can be strong reference or weak reference. It is a weak reference when the **ref** count is 0, and a strong reference when the **ref** count is greater than 0. A strong reference prevents the garbage collector from reclaiming the referenced object. It is suitable for scenarios where the object needs to be kept alive for a long time. However, the reference count and release must be managed manually; otherwise, memory leaks will occur. A weak reference, by contrast, does not prevent garbage collection and allows the object to be reclaimed normally when it is no longer held by any other strong references. It is applicable to temporary reference scenarios such as caching, as it can become invalid automatically, but it is necessary to check whether the object is still alive when obtaining it. You need to use strong and weak reference types correctly to balance memory management and performance.

## napi\_create\_reference and napi\_delete\_reference

Use **napi\_create\_reference** to create a reference for an object to extend its lifespan. The caller needs to manage the reference lifespan. Use **napi\_delete\_reference** to delete a reference.

## napi\_reference\_ref and napi\_reference\_unref

Use **napi\_reference\_ref** to increment the reference count and use **napi\_reference\_unref** to decrement the reference count, and return the new count value.

## napi\_get\_reference\_value

Use **napi\_get\_reference\_value** to obtain the ArkTS object associated with the reference.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/id28idvzQW-oBEnQy3eOVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75315F82717E7AC3534D18865CF2B1F4FC3B33ACB47EF6CA54C1210CE7312127)

The release of a weak reference (**napi\_ref** whose reference count is 0) and GC of a JS object do not occur at the same time.

Consequently, the JS object may be garbage-collected before the weak reference is released.

As a result, calling this API may yield a null pointer even if **napi\_ref** is valid.

Sample code for using a weak reference:

When creating a weak reference, initialize the reference count to 0. The **ref** created in this way is a weak reference, which does not prevent the object from being garbage collected. Before obtaining the reference, initialize **weakValue** to **nullptr**. After obtaining the value, check whether **weakValue** is still **nullptr**. If yes, the object has been garbage collected. If no, the object can still be used.

CPP code:

#include "napi/native\_api.h"

napi\_ref g\_weakRef = nullptr;

static napi\_value CreateWeakReference(napi\_env env, napi\_callback\_info info)
{
    napi\_value value = nullptr;
    napi\_create\_string\_utf8(env, "This is a test property", NAPI\_AUTO\_LENGTH, &value);
    napi\_value jsObject = nullptr;
    napi\_create\_object(env, &jsObject);
    napi\_set\_named\_property(env, jsObject, "test", value);

    // Clear the previous reference (if any).
    if (g\_weakRef != nullptr) {
        napi\_delete\_reference(env, g\_weakRef);
        g\_weakRef = nullptr;
    }

    // Create a weak reference. The weak reference does not prevent garbage collection and will be reclaimed when no other strong reference exists.
    napi\_status status = napi\_create\_reference(env, jsObject, 0, &g\_weakRef);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to create weak reference");
        return nullptr;
    }

    return nullptr;
}

static napi\_value GetWeakReferenceValue(napi\_env env, napi\_callback\_info info)
{
    napi\_value weakValue;
    napi\_status status = napi\_get\_reference\_value(env, g\_weakRef, &weakValue);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to get reference value");
        return nullptr;
    }

    // Check whether the object has been reclaimed.
    if (weakValue == nullptr) {
        napi\_throw\_error(env, nullptr, "Object has been garbage collected");
        return nullptr;
    }

    // Obtain the properties of the object to check whether it is still valid.
    napi\_value result = nullptr;
    napi\_get\_named\_property(env, weakValue, "test", &result);

    return result;
}

API declaration:

// index.d.ts

export const createWeakReference: () => void;

export const getWeakReferenceValue: () => string;

ArkTS code:

try {
    testNapi.createWeakReference();
    hilog.info(0x0000, 'testTag', 'reference test: %{public}s', testNapi.getWeakReferenceValue());
} catch (error) {
    hilog.error(0x0000, 'testTag', \`Call error: ${error.message}\`);
}

Sample code for using a strong reference:

When creating a strong reference, initialize the reference count to **1**. The **ref** created in this way is a strong reference, which guarantees the object will not be garbage collected. When the reference is no longer used, call **napi\_delete\_reference** to destroy the reference, preventing memory leaks.

CPP code:

#include "napi/native\_api.h"

// Global strong reference.
napi\_ref g\_strongRef = nullptr;

// Create a strong reference.
static napi\_value CreateStrongReference(napi\_env env, napi\_callback\_info info)
{
    napi\_value value = nullptr;
    napi\_create\_string\_utf8(env, "This is a test property", NAPI\_AUTO\_LENGTH, &value);
    napi\_value jsObject = nullptr;
    napi\_create\_object(env, &jsObject);
    napi\_set\_named\_property(env, jsObject, "test", value);

    // Clear the previous strong reference (if any).
    if (g\_strongRef != nullptr) {
        napi\_delete\_reference(env, g\_strongRef);
        g\_strongRef = nullptr;
    }

    // Create a strong reference (by initializing the reference count to 1) to prevent the garbage collection.
    napi\_status status = napi\_create\_reference(env, jsObject, 1, &g\_strongRef);

    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to create strong reference");
        return nullptr;
    }

    return nullptr;
}

static napi\_value GetStrongReferenceValue(napi\_env env, napi\_callback\_info info)
{
    napi\_value jsValue;
    napi\_status status = napi\_get\_reference\_value(env, g\_strongRef, &jsValue);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to get reference value");
        return nullptr;
    }

    // Obtain the properties of the object to check whether it is still valid.
    napi\_value result = nullptr;
    napi\_get\_named\_property(env, jsValue, "test", &result);

    return result;
}

// Clear the strong reference.
static napi\_value CleanupStrongReference(napi\_env env, napi\_callback\_info info) {
    napi\_value ret = nullptr;
    if (g\_strongRef != nullptr) {
        // Forcibly delete the reference, even if the reference count is not 0.
        napi\_delete\_reference(env, g\_strongRef);
        g\_strongRef = nullptr;
        napi\_get\_boolean(env, true, &ret);
        return ret;
    }
    napi\_get\_boolean(env, false, &ret);
    return ret;
}

API declaration:

// index.d.ts

export const createStrongReference: () => void;

export const getStrongReferenceValue: () => string;

export const cleanupStrongReference: () => void;

ArkTS code:

try {
    testNapi.createStrongReference();
    hilog.info(0x0000, 'testTag', 'reference test: %{public}s', testNapi.getStrongReferenceValue());
    testNapi.cleanupStrongReference();
} catch (error) {
    hilog.error(0x0000, 'testTag', \`Call error: ${error.message}\`);
}

## napi\_add\_finalizer

Use **napi\_add\_finalizer** to add a **napi\_finalizer** callback, which will be called when the ArkTS object is garbage-collected.

CPP code:

// Create a pointer to napi\_ref to store the created reference. Before calling napi\_add\_finalizer, allocate a variable of the napi\_ref type and pass its address as the result parameter.
napi\_ref gRefFinalizer = nullptr;

// Create a pointer to napi\_ref to store the created reference. Before calling napi\_create\_reference, allocate a variable of the napi\_ref type and pass its address as the result parameter.
napi\_ref gRef = nullptr;

void Finalizer(napi\_env env, void \*data, void \*hint)
{
    // Clear resources.
    OH\_LOG\_INFO(LOG\_APP, "Test Node-API Use Finalizer to release resources.");
    // Release resources.
}

static napi\_value AddFinalizer(napi\_env env, napi\_callback\_info info)
{
    napi\_value obj = nullptr;
    napi\_status status = napi\_create\_object(env, &obj);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_object fail");
        return nullptr;
    }
    napi\_value value = nullptr;
    status = napi\_create\_string\_utf8(env, "AddFinalizer", NAPI\_AUTO\_LENGTH, &value);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_string\_utf8 fail");
        return nullptr;
    }
    // Add a property to the object.
    status = napi\_set\_named\_property(env, obj, "key", value);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_set\_named\_property fail");
        return nullptr;
    }

    // Register a Finalizer to release resources.
    void \*data = {};
    status = napi\_add\_finalizer(env, obj, data, Finalizer, nullptr, &gRefFinalizer);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_add\_finalizer fail");
        return nullptr;
    }

    return obj;
}

static napi\_value CreateReference(napi\_env env, napi\_callback\_info info)
{
    napi\_value obj = nullptr;
    napi\_status status = napi\_create\_object(env, &obj);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_object fail");
        return nullptr;
    }
    napi\_value value = nullptr;
    status = napi\_create\_string\_utf8(env, "CreateReference", NAPI\_AUTO\_LENGTH, &value);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_string\_utf8 fail");
        return nullptr;
    }
    // Add a property to the object.
    status = napi\_set\_named\_property(env, obj, "key", value);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_set\_named\_property fail");
        return nullptr;
    }
    // Create a reference to the ArkTS object.
    status = napi\_create\_reference(env, obj, 1, &gRef);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_reference fail");
        return nullptr;
    }
    // Increment the reference count and return the new reference count.
    uint32\_t result = 0;
    status = napi\_reference\_ref(env, gRef, &result);
    OH\_LOG\_INFO(LOG\_APP, "Test Node-API napi\_reference\_ref, count = %{public}d.", result);
    uint32\_t numCount = 2;
    if (status != napi\_ok || result != numCount) {
        // If the reference count passed in does not increase, throw an error.
        napi\_throw\_error(env, nullptr, "napi\_reference\_ref fail");
        return nullptr;
    }
    return obj;
}

static napi\_value UseReference(napi\_env env, napi\_callback\_info info)
{
    napi\_value obj = nullptr;
    // Call napi\_get\_reference\_value to obtain the referenced ArkTS object.
    napi\_status status = napi\_get\_reference\_value(env, gRef, &obj);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_get\_reference\_value fail");
        return nullptr;
    }
    // Return the obtained object.
    return obj;
}

static napi\_value DeleteReference(napi\_env env, napi\_callback\_info info)
{
    // Decrement the reference count and return the new reference count.
    uint32\_t result = 0;
    napi\_value count = nullptr;
    napi\_status status = napi\_reference\_unref(env, gRef, &result);
    OH\_LOG\_INFO(LOG\_APP, "Test Node-API napi\_reference\_unref, count = %{public}d.", result);
    uint32\_t numCount = 1;
    if (status != napi\_ok || result != numCount) {
        // If the reference count passed in does not decrease, throw an error.
        napi\_throw\_error(env, nullptr, "napi\_reference\_unref fail");
        return nullptr;
    }

    // Call napi\_delete\_reference to delete the reference to the ArkTS object.
    status = napi\_delete\_reference(env, gRef);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_delete\_reference fail");
        return nullptr;
    }

    status = napi\_delete\_reference(env, gRefFinalizer);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_delete\_reference fail");
        return nullptr;
    }
    napi\_value returnResult = nullptr;
    status = napi\_create\_string\_utf8(env, "napi\_delete\_reference success", NAPI\_AUTO\_LENGTH, &returnResult);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_string\_utf8 fail");
        return nullptr;
    }
    return returnResult;
}

API declaration:

// index.d.ts

export const addFinalizer: () => Object | undefined; // napi\_add\_finalizer

export const createReference: () => Object | undefined; // napi\_create\_reference and napi\_reference\_ref

export const useReference: () => Object | undefined; // napi\_get\_reference\_value

export const deleteReference: () => string | undefined; // napi\_delete\_reference and napi\_reference\_unref

ArkTS code:

// napi\_add\_finalizer
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API addFinalizer: %{public}s',
    JSON.stringify(testNapi.addFinalizer()));
  hilog.info(0x0000, 'testTag', 'Test Node-API createReference: %{public}s',
    JSON.stringify(testNapi.createReference()));
  hilog.info(0x0000, 'testTag', 'Test Node-API useReference: %{public}s',
    JSON.stringify(testNapi.useReference()));
  hilog.info(0x0000, 'testTag', 'Test Node-API deleteReference: %{public}s',
    testNapi.deleteReference());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag',
    'Test Node-API ReferenceTest errorCode: %{public}s, errorMessage: %{public}s', error.code,
    error.message);
  // ...
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
