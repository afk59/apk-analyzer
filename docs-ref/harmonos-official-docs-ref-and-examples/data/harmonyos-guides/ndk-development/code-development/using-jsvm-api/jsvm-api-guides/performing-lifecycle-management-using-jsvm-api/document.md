# Performing Lifecycle Management Using JSVM-API

#### Introduction

In JSVM-API, **JSVM\_Value** is an abstract data type that represents a JavaScript (JS) value of any type, which includes the basic type (such as number, string, or Boolean) and the composite type (such as array, function, or object).

The **JSVM\_Value** lifecycle is related to the lifecycle of the JS value. After the JS value is garbage collected, the **JSVM\_Value** is no longer valid. Do not use **JSVM\_Value** when the JS value does not exist.

Scope is used to manage the **JSVM\_Value** lifecycle in the framework layer. You can use **OH\_JSVM\_OpenHandleScope** to create a scope and use **OH\_JSVM\_CloseHandleScope** to destroy a scope. By creating a **JSVM\_Value** in a scope, you can ensure that the **JSVM\_Value** is automatically released when the scope ends. This helps prevent memory leaks.

**JSVM\_Ref** is a JSVM-API data type used to manage the **JSVM\_Value** lifecycle. It allows reference to a **JSVM\_Value** during its lifecycle, even if the value is beyond its original context. The reference allows a **JSVM\_Value** to be shared in different contexts and released in a timely manner.

You are advised to properly use **OH\_JSVM\_OpenHandleScope** and **OH\_JSVM\_CloseHandleScope** to manage the lifecycle of **JSVM\_Value** instances, avoiding memory leaks.

Each **JSVM\_Value** belongs to a specific **HandleScope** instance, which is created by **OH\_JSVM\_OpenHandleScope** and closed by **OH\_JSVM\_CloseHandleScope**. After a **HandleScope** instance is closed, the corresponding **JSVM\_Value** will be automatically released.

#### Basic Concepts

JSVM-API provides APIs for creating and manipulating JS objects, managing references to and lifecycle of the JS objects, and registering garbage collection (GC) callbacks in C/C++. Before you get started, you need to understand the following concepts:

-   Scope: used to ensure that the objects created within a certain scope remain active and are properly cleared when no longer required. JSVM-API provides APIs for creating and closing normal and escapable scopes.
-   Reference management: JSVM-API provides APIs for creating, deleting, and managing object references to extend the object lifecycle and prevent memory leaks when objects are used.
-   Escapable scope: used to return the values created within the **escapable\_handle\_scope** to a parent scope. It is created by **OH\_JSVM\_OpenEscapableHandleScope** and closed by **OH\_JSVM\_CloseEscapableHandleScope**.
-   GC callback: You can register GC callbacks to perform specific cleanup operations when JS objects are garbage-collected.

Understanding these concepts helps you securely and effectively manipulate JavaScript objects and manage object lifecycles.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_OpenHandleScope | Opens a handle scope. **JSVM\_Value** within the scope will not be garbage-collected. |
| OH\_JSVM\_CloseHandleScope | Closes a handle scope. |
| OH\_JSVM\_OpenEscapableHandleScope | Opens an escapable handle scope. Before this scope is closed, the object created within the scope has the same lifecycle as its parent scope. |
| OH\_JSVM\_CloseEscapableHandleScope | Closes an escapable handle scope. |
| OH\_JSVM\_EscapeHandle | Promotes a handle to a JS object so that it is valid for the lifetime of the outer scope. |
| OH\_JSVM\_CreateReference | Creates a reference with the specified reference count to the value passed in. The reference allows objects to be used and shared in different contexts and helps effective track of the object lifecycle. |
| OH\_JSVM\_DeleteReference | Deletes the reference created by **OH\_JSVM\_CreateReference**. This allows objects to be correctly released and reclaimed when they are no longer required, avoiding memory leaks. |
| OH\_JSVM\_ReferenceRef | Increments the reference count of the reference created by **OH\_JSVM\_CreateReference** so that the object referenced will not be released. |
| OH\_JSVM\_ReferenceUnref | Decrements the reference count of the reference created by **OH\_JSVM\_CreateReference** so that the object can be correctly released and reclaimed when it is not referenced. |
| OH\_JSVM\_GetReferenceValue | Obtains the object referenced by **OH\_JSVM\_CreateReference**. |
| OH\_JSVM\_AddFinalizer | Adds a **JSVM\_Finalize** callback to a JS object. The callback will be invoked to release the native object when the JS object is garbage-collected. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in the related APIs.

## OH\_JSVM\_OpenHandleScope and OH\_JSVM\_CloseHandleScope

Call **OH\_JSVM\_OpenHandleScope** to create a context and call **OH\_JSVM\_CloseHandleScope** to close the context. Properly managing JS handle scopes can prevent GC problems.

CPP code:

// Define OH\_JSVM\_OpenHandleScope and OH\_JSVM\_CloseHandleScope.
static JSVM\_Value HandleScopeFor(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // When JSVM-API is frequently called to create JS objects in the for loop, use handle\_scope to release resources in a timely manner when they are no longer required.
    // In the following example, the lifecycle of the local variable res ends at the end of each loop. To prevent memory leaks, scope is used to release the JS object in a timely manner.
    constexpr uint32\_t DIFF\_VALUE\_TEN\_THOUSAND = 10000;
    JSVM\_Value checked = nullptr;
    for (int i = 0; i < DIFF\_VALUE\_TEN\_THOUSAND; i++) {
        JSVM\_HandleScope scope = nullptr;
        JSVM\_Status status = OH\_JSVM\_OpenHandleScope(env, &scope);
        if (status != JSVM\_OK || scope == nullptr) {
            OH\_JSVM\_GetBoolean(env, false, &checked);
            OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_OpenHandleScope: failed");
            return checked;
        }
        JSVM\_Value res = nullptr;
        OH\_JSVM\_CreateObject(env, &res);
        status = OH\_JSVM\_CloseHandleScope(env, scope);
        if (status != JSVM\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CloseHandleScope: failed");
        }
    }
    OH\_JSVM\_GetBoolean(env, true, &checked);
    OH\_LOG\_INFO(LOG\_APP, "JSVM HandleScopeFor: success");
    return checked;
}

// Register the HandleScopeFor callback.
static JSVM\_CallbackStruct param\[\] = {
    {.callback = HandleScopeFor, .data = nullptr},
};

static JSVM\_CallbackStruct \*method = param;
// Alias for the HandleScopeFor method, which can be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"HandleScopeFor", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

const char \*srcCallNative = "HandleScopeFor()";

Expected result:

JSVM HandleScopeFor: success

## OH\_JSVM\_OpenEscapableHandleScope, OH\_JSVM\_CloseEscapableHandleScope, and OH\_JSVM\_EscapeHandle

Call **OH\_JSVM\_OpenEscapableHandleScope** to create an escapable handle scope, which allows the declared values in a scope to be returned to its parent scope.

Call **OH\_JSVM\_CloseEscapableHandleScope** to close the created scope. Call **OH\_JSVM\_EscapeHandle** to promote the lifecycle of the passed-in JS object to its parent scope.

These APIs are helpful for managing JS objects more flexibly in C/C++, especially when passing cross-scope values.

CPP code:

// Define OH\_JSVM\_OpenEscapableHandleScope, OH\_JSVM\_CloseEscapableHandleScope, and OH\_JSVM\_EscapeHandle.
static JSVM\_Value EscapableHandleScopeTest(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Create an escapable handle scope.
    JSVM\_EscapableHandleScope scope = nullptr;
    JSVM\_Status status = OH\_JSVM\_OpenEscapableHandleScope(env, &scope);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_OpenEscapableHandleScope: failed");
        return nullptr;
    }
    // Create an object within the scope of the escapable handle.
    JSVM\_Value obj = nullptr;
    OH\_JSVM\_CreateObject(env, &obj);
    // Add properties to the object.
    JSVM\_Value value = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "Test jsvm\_escapable\_handle\_scope", JSVM\_AUTO\_LENGTH, &value);
    OH\_JSVM\_SetNamedProperty(env, obj, "name", value);
    // Call OH\_JSVM\_EscapeHandle to promote the JS object handle to make it valid with the lifetime of the outer scope.
    JSVM\_Value escapedObj = nullptr;
    OH\_JSVM\_EscapeHandle(env, scope, obj, &escapedObj);
    // Close the escapable handle scope to clear resources.
    status = OH\_JSVM\_CloseEscapableHandleScope(env, scope);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CloseEscapableHandleScope: failed");
        return nullptr;
    }
    // Here, escapedObj can be used in the outer scope.
    bool result = false;
    OH\_JSVM\_CreateStringUtf8(env, "name", JSVM\_AUTO\_LENGTH, &value);
    OH\_JSVM\_HasProperty(env, escapedObj, value, &result);
    if (result) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM EscapableHandleScopeTest: success");
    }
    return escapedObj;
}

// Define the EscapableHandleScopeTest callback.
static JSVM\_CallbackStruct param\[\] = {
    {.callback = EscapableHandleScopeTest, .data = nullptr},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the escapableHandleScopeTest method, which can be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"escapableHandleScopeTest", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

const char \*srcCallNative = "escapableHandleScopeTest()";

Expected result:

JSVM EscapableHandleScopeTest: success

## OH\_JSVM\_CreateReference, OH\_JSVM\_DeleteReference, and OH\_JSVM\_GetReferenceValue

1.  Call **OH\_JSVM\_CreateReference** to create a reference for a JS variable to extend its lifecycle.
2.  Call **OH\_JSVM\_GetReferenceValue** to obtain the JS variable associated with the reference.
3.  Call **OH\_JSVM\_DeleteReference** to delete the reference.

The caller must manage the reference lifecycle. During the reference validity period, the JS variable will not be garbage-collected.

## OH\_JSVM\_ReferenceRef and OH\_JSVM\_ReferenceUnref

Call **OH\_JSVM\_ReferenceRef** to increment the reference count of a reference and call **OH\_JSVM\_ReferenceUnref** to decrement the reference count of a reference, and return the new count value. When the reference count is **0**, the reference will be set as a weak reference for the JS types that can be set as weak references (objects, functions, and external variables). The associated variable will be garbage-collected when the GC mechanism deems it necessary. After the variable is garbage-collected, calling **OH\_JSVM\_GetReferenceValue** will return C **NULL**. For JS types that cannot be set as weak references, the reference will be cleared and calling **OH\_JSVM\_GetReferenceValue** will return C **NULL**.

CPP code:

static JSVM\_Value UseReference(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Create a JS object.
    JSVM\_Value obj = nullptr;
    OH\_JSVM\_CreateObject(env, &obj);
    JSVM\_Value value = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "UseReference", JSVM\_AUTO\_LENGTH, &value);
    OH\_JSVM\_SetNamedProperty(env, obj, "name", value);
    
    JSVM\_Ref g\_ref = nullptr;
    // Create a reference to the JS object.
    JSVM\_Status status = OH\_JSVM\_CreateReference(env, obj, 1, &g\_ref);
    if (status != JSVM\_OK) {
        return nullptr;
    }

    // Increment the reference count and return the new reference count.
    uint32\_t result = 0u;
    OH\_JSVM\_ReferenceRef(env, g\_ref, &result);
    OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_ReferenceRef, count = %{public}d.", result);
    if (result != 2) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_ReferenceRef: failed");
        return nullptr;
    }

    // Decrement the reference count and return the new reference count.
    uint32\_t num = 0u;
    OH\_JSVM\_ReferenceUnref(env, g\_ref, &num);
    OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_ReferenceUnref, count = %{public}d.", num);
    if (num != 1) {
        return nullptr;
    }

    JSVM\_Value object = nullptr;
    // Call OH\_JSVM\_GetReferenceValue to obtain the referenced JS object.
    status = OH\_JSVM\_GetReferenceValue(env, g\_ref, &object);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_GetReferenceValue: failed");
        return nullptr;
    }

    // When the reference is no longer required, call OH\_JSVM\_DeleteReference to delete it.
    status = OH\_JSVM\_DeleteReference(env, g\_ref);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_DeleteReference: failed");
        return nullptr;
    }

    // Return the obtained object.
    OH\_LOG\_INFO(LOG\_APP, "JSVM UseReference success");
    return object;
}

// Register the CreateReference, UseReference, and DeleteReference callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.callback = UseReference, .data = nullptr},
};
static JSVM\_CallbackStruct \*method = param;
// Aliases for the CreateReference, UseReference, and DeleteReference methods, which cal be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"useReference", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

const char \*srcCallNative = "useReference()";

Expected result:

JSVM OH\_JSVM\_ReferenceRef, count = 2.
JSVM OH\_JSVM\_ReferenceUnref, count = 1.
JSVM UseReference success

## OH\_JSVM\_AddFinalizer

Call **OH\_JSVM\_AddFinalizer** to add the **JSVM\_Finalize** callback to a JS object. The callback will be invoked when the JS object is garbage-collected. **OH\_JSVM\_AddFinalizer** is usually used to release the native object associated with a JS object. If the input parameter is not a JS object, the call will fail and return an error code.

The Finalizer method cannot be canceled after being registered. If it is not executed before **OH\_JSVM\_DestroyEnv** is called, it will be executed when **OH\_JSVM\_DestroyEnv** is called.

CPP code:

static int AddFinalizer(JSVM\_VM vm, JSVM\_Env env) {
    // Open the handle scope.
    JSVM\_HandleScope handleScope;
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));
    // Create an object and set a callback.
    JSVM\_Value obj = nullptr;
    CHECK\_RET(OH\_JSVM\_CreateObject(env, &obj));
    CHECK\_RET(OH\_JSVM\_AddFinalizer(
        env, obj, nullptr,
        \[\](JSVM\_Env env, void \*data, void \*hint) -> void {
            // Finalizer method, which can be used to clear the native object.
            OH\_LOG\_INFO(LOG\_APP, "JSVM: finalizer called.");
        },
        nullptr, nullptr));
    OH\_LOG\_INFO(LOG\_APP, "JSVM: finalizer added.");
    // Close the handle scope to trigger GC. The Finalizer callback will be called during GC.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
    OH\_LOG\_INFO(LOG\_APP, "JSVM: before call gc.");
    CHECK\_RET(OH\_JSVM\_MemoryPressureNotification(env, JSVM\_MemoryPressureLevel::JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL));
    OH\_LOG\_INFO(LOG\_APP, "JSVM: after call gc.");

    return 0;
}

static JSVM\_Value RunDemo(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_VM vm;
    OH\_JSVM\_GetVM(env, &vm);
    if (AddFinalizer(vm, env) != 0) {
        OH\_LOG\_INFO(LOG\_APP, "Run PromiseRegisterHandler failed");
    }

    return nullptr;
}

// Register the RunDemo callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = RunDemo},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the RunDemo method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"RunDemo", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call C++ code from JS.
const char \*srcCallNative = R"JS(RunDemo();)JS";

Expected result:

JSVM: finalizer added.
JSVM: before call gc.
JSVM: finalizer called.
JSVM: after call gc.
