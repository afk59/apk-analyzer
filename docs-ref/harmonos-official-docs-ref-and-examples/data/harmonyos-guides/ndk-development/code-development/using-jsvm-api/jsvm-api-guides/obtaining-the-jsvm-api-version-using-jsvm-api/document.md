# Obtaining the JSVM-API Version Using JSVM-API

#### Introduction

This topic walks you through how to use JSVM-API to obtain the JSVM-API version.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetVersion | Obtains the latest JSVM API version supported by the JSVM runtime. |
| OH\_JSVM\_GetVMInfo | Obtains the VM information. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in using version-related APIs.

## OH\_JSVM\_GetVersion && OH\_JSVM\_GetVMInfo

Use **OH\_JSVM\_GetVersion && OH\_JSVM\_GetVMInfo** to obtain the latest JSVM API version supported by the current environment and the VM information.

CPP code:

// hello.cpp
#include <string.h>

// Define OH\_JSVM\_GetVersion.
static JSVM\_Value GetVersion(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    uint32\_t jsVersion = 0;
    // Obtain the latest JSVM API version supported by the current JSVM runtime.
    JSVM\_CALL(OH\_JSVM\_GetVersion(env, &jsVersion));
    int value = static\_cast<int>(jsVersion);
    OH\_LOG\_INFO(LOG\_APP, "JSVM GetVersion success:%{public}d", value);
    return nullptr;
}

// Define OH\_JSVM\_GetVMInfo.
// Print the JSVM information.
void PrintVmInfo(JSVM\_VMInfo vmInfo) {
    OH\_LOG\_INFO(LOG\_APP, "JSVM API apiVersion: %{public}d", vmInfo.apiVersion);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API engine: %{public}s", vmInfo.engine);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API version: %{public}s", vmInfo.version);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API cachedDataVersionTag: 0x%{public}x", vmInfo.cachedDataVersionTag);
}

static JSVM\_Value GetVMInfo(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the VM information.
    JSVM\_VMInfo result;
    JSVM\_CALL(OH\_JSVM\_GetVMInfo(&result));
    // Output VM information.
    PrintVmInfo(result);
    return nullptr;
}

// JS code to be executed.
static const char \*srcCallNative = R"JS(getVersion();getVMInfo();)JS";

// Register the GetVersion and GetVMInfo callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetVersion},
    {.data = nullptr, .callback = GetVMInfo},
};
static JSVM\_CallbackStruct \*method = param;
// Aliases of the GetVersion and GetVMInfo methods, which can be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getVersion", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"getVMInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

Expected result:

JSVM GetVersion success:9
JSVM API apiVersion: 1
JSVM API engine: v8
JSVM API version: 13.2.152.41
JSVM API cachedDataVersionTag: 0x81ff9402
