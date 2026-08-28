# Triggering GC Using JSVM-API

#### Introduction

JSVM-API provides the capability of registering callbacks to monitor memory GC of the JSVM. You can customize logic to perform optimization, debugging, or performance monitoring before or after GC.

#### Basic Concepts

In JS, GC is automatically performed, and users are not aware of the GC behavior of the JSVM. The JS engine enters the prologue phase before each GC, and enters the epilogue phase after each GC. The prologue is the setup phase before the actual GC begins. In this phase, the system prepares for GC. The epilogue is the final cleanup phase after GC, ensuring that the memory is restored to a normal state and ready for the next allocation. In these two phases, the JS engine calls the callbacks registered. You can suspend some tasks, record the memory usage, and optimize performance in the callbacks registered in the prologue phase, and record the memory status after GC and start subsequent tasks in the callbacks registered in the epilogue phase.

JSVM-API provides the **OH\_JSVM\_AddHandlerForGC** API for registering a callback with a JSVM. You can pass in **JSVM\_CB\_TRIGGER\_BEFORE\_GC** to specify the callback in the prologue phase, and pass in **JSVM\_CB\_TRIGGER\_AFTER\_GC** to specify the callback in the epilogue phase. You can use **OH\_JSVM\_RemoveHandlerForGC** to remove a registered callback from a JSVM.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_AddHandlerForGC | Registers a callback with a JSVM. |
| OH\_JSVM\_RemoveHandlerForGC | Removes a registered callback from a JSVM. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in GC management.

## OH\_JSVM\_AddHandlerForGC & OH\_JSVM\_RemoveHandlerForGC

You can call **OH\_JSVM\_AddHandlerForGC** multiple times to register callbacks with a JSVM, and all registered callbacks will take effect. During registration, the callback pointer and **native-data** are used as the key. If multiple registration behaviors have the same key, the registration will be considered invalid and the **JSVM\_INVALID\_ARG** error code will be returned. The order in which callbacks are invoked under the same triggering condition does not strictly follow the registration order.

You can use **OH\_JSVM\_RemoveHandlerForGC** to remove a registered callback from a JSVM. Removing callbacks with the same key will be considered an invalid removal, and the **JSVM\_INVALID\_ARG** error will be returned.

**CPP Code**

// hello.cpp
#include <iostream>

static bool before\_flag1 = false;
static bool before\_flag2 = false;
static bool after\_flag1 = false;
static bool after\_flag2 = false;

void OnBeforeGC(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void \*data)
{
    OH\_LOG\_INFO(LOG\_APP, "== before GC ==");
    OH\_LOG\_INFO(LOG\_APP, "gc type: %{public}d", gcType);
    OH\_LOG\_INFO(LOG\_APP, "gc flag: %{public}d", flags);
    before\_flag1 = true;
}

void OnBeforeGC2(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void \*data)
{
    OH\_LOG\_INFO(LOG\_APP, "== before GC2 ==");
    OH\_LOG\_INFO(LOG\_APP, "gc type: %{public}d", gcType);
    OH\_LOG\_INFO(LOG\_APP, "gc flag: %{public}d", flags);
    OH\_LOG\_INFO(LOG\_APP, "data: %{public}d", \*(int\*)data);
    if (\*(int\*)data == 2024) {
        before\_flag2 = true;
    }
}

void OnAfterGC(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void \*data)
{
    after\_flag1 = true;
}

void OnAfterGC2(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void \*data)
{
    after\_flag2 = true;
}

void OnAfterGC3(JSVM\_VM vm, JSVM\_GCType gcType, JSVM\_GCCallbackFlags flags, void \*data)
{
    after\_flag2 = true;
}

static JSVM\_Value TriggerGC(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    bool remove\_repeated = false;
    bool remove\_notAdded = false;
    bool add\_repeated = false;
    before\_flag1 = false;
    before\_flag2 = false;
    after\_flag1 = false;
    after\_flag2 = false;
    JSVM\_VM vm;
    OH\_JSVM\_GetVM(env, &vm);
    // Register two callbacks to be called before GC.
    int data = 2024;
    JSVM\_CALL(OH\_JSVM\_AddHandlerForGC(vm, JSVM\_CB\_TRIGGER\_BEFORE\_GC, OnBeforeGC, JSVM\_GC\_TYPE\_ALL, NULL));
    JSVM\_CALL(OH\_JSVM\_AddHandlerForGC(vm, JSVM\_CB\_TRIGGER\_BEFORE\_GC, OnBeforeGC2, JSVM\_GC\_TYPE\_ALL, (void\*)(&data)));
    // Register two callbacks to be called after GC.
    JSVM\_CALL(OH\_JSVM\_AddHandlerForGC(vm, JSVM\_CB\_TRIGGER\_AFTER\_GC, OnAfterGC, JSVM\_GC\_TYPE\_ALL, NULL));
    JSVM\_CALL(OH\_JSVM\_AddHandlerForGC(vm, JSVM\_CB\_TRIGGER\_AFTER\_GC, OnAfterGC2, JSVM\_GC\_TYPE\_ALL, NULL));
    // The registration is invalid because (OnAfterGC2, NULL) has been registered.
    if (OH\_JSVM\_AddHandlerForGC(vm, JSVM\_CB\_TRIGGER\_AFTER\_GC, OnAfterGC2, JSVM\_GC\_TYPE\_ALL, NULL) == JSVM\_INVALID\_ARG) {
        add\_repeated = true;
    }
    // Remove the OnAfter2 callback.
    JSVM\_CALL(OH\_JSVM\_RemoveHandlerForGC(vm, JSVM\_CB\_TRIGGER\_AFTER\_GC, OnAfterGC2, NULL));
    // Repeated removal of OnAfter2 is invalid.
    if (OH\_JSVM\_RemoveHandlerForGC(vm, JSVM\_CB\_TRIGGER\_AFTER\_GC, OnAfterGC2, NULL) == JSVM\_INVALID\_ARG) {
        remove\_repeated = true;
    }
    // Removing a callback that has never been registered is invalid.
    if (OH\_JSVM\_RemoveHandlerForGC(vm, JSVM\_CB\_TRIGGER\_AFTER\_GC, OnAfterGC3, NULL) == JSVM\_INVALID\_ARG) {
        remove\_notAdded = true;
    }
    // Notify the system when the JSVM is under high memory pressure, which is likely to trigger GC of the JSVM.
    JSVM\_CALL(OH\_JSVM\_MemoryPressureNotification(env, JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL));
    if ((before\_flag1) &&
        (before\_flag2) &&
        (after\_flag1) &&
        (!after\_flag2) &&
        (remove\_repeated) &&
        (remove\_notAdded) &&
        (add\_repeated)) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM Trigger GC: success");
    } else {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM Trigger GC: failed");
    }
    JSVM\_Value checked;
    OH\_JSVM\_GetBoolean(env, true, &checked);
    return checked;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = TriggerGC},
};
static JSVM\_CallbackStruct \*method = param;

static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"triggerGC", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

**JS Example**

const char \*srcCallNative = R"JS(triggerGC();)JS";

**Execution Result**

The following information is displayed in the log:

\== before GC ==
gc type: 4
gc flag: 4
== before GC2 ==
gc type: 4
gc flag: 4
data: 2024
JSVM Trigger GC: success
