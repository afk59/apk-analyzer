# Performing Memory Management Using JSVM-API

#### Introduction

JSVM-API provides APIs for managing JavaScript virtual machine (JSVM) memory. With these APIs, you can better control the memory used by JS code and optimize memory management and garbage collection (GC) mechanisms.

#### Basic Concepts

In JS, memory management and GC are performed automatically. The JSVM is responsible for tracking the allocation and release of objects and reclaiming the memory that is no longer required. However, if a JSVM consumes a large amount of memory, an out-of-memory error may occur. To prevent this type of errors, JSVM-API provides APIs to better control memory management and GC mechanisms.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_AdjustExternalMemory | Manages the external allocated memory held by a JS object. |
| OH\_JSVM\_MemoryPressureNotification | Notifies the underlying JSVM that the VM system memory is insufficient and selectively trigger GC. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code and ArkTS code involved in related APIs.

## OH\_JSVM\_AdjustExternalMemory

Call **OH\_JSVM\_AdjustExternalMemory** to adjust the amount of externally allocated memory that is kept alive for a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_AdjustExternalMemory.
static JSVM\_Value AdjustExternalMemory(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Allocate 1 MB of memory.
    int64\_t change = 1024 \* 1024;
    int64\_t adjustedValue = 0;
    JSVM\_Status status = OH\_JSVM\_AdjustExternalMemory(env, change, &adjustedValue);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_AdjustExternalMemory: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_AdjustExternalMemory: success");
        OH\_LOG\_INFO(LOG\_APP, "JSVM Allocate memory size: %{public}d", adjustedValue);
    }
    JSVM\_Value checked;
    OH\_JSVM\_GetBoolean(env, true, &checked);
    return checked;
}
// Register the AdjustExternalMemory callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = AdjustExternalMemory},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the AdjustExternalMemory method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"adjustExternalMemory", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(adjustExternalMemory())JS";

Expected result:

JSVM OH\_JSVM\_AdjustExternalMemory: success
JSVM Allocate memory size: 1048576

## OH\_JSVM\_MemoryPressureNotification

Call **OH\_JSVM\_MemoryPressureNotification** to notify the VM of insufficient system memory and selectively triggers garbage collection.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_MemoryPressureNotification.
static JSVM\_Value MemoryPressureNotification(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Set the memory pressure level of the current JSVM.
    JSVM\_Status status = OH\_JSVM\_MemoryPressureNotification(env, JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_MemoryPressureNotification: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_MemoryPressureNotification: success");
        OH\_LOG\_INFO(LOG\_APP, "JSVM Current JSVM memory pressure level: %{public}d", JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL);
    }
    return nullptr;
}
// Register the MemoryPressureNotification callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = MemoryPressureNotification},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the MemoryPressureNotification method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"memoryPressureNotification", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(memoryPressureNotification())JS";

Expected result:

JSVM OH\_JSVM\_MemoryPressureNotification: success
JSVM Current JSVM memory pressure level: 2
