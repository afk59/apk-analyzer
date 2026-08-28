# Working with VM Snapshots Using JSVM-API

#### Introduction

A JavaScript virtual machine (JSVM) snapshot records the state of a JSVM at a particular time point. The snapshot file contains information, such as the current heap memory, execution context, and function closure.

#### Basic Concepts

-   VM startup snapshot: a snapshot of the VM status at a specific time, including all internal status and data of the VM. The snapshot can be used to quickly restore the VM to the state it was when the snapshot was created.

It helps simplify complex programming tasks and shorten the creation time of a JS context, making the application more efficient and stable.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateSnapshot | Creates a VM startup snapshot. |
| OH\_JSVM\_CreateEnvFromSnapshot | Creates an environment based on the start snapshot of a VM. |

#### Example

## OH\_JSVM\_CreateSnapshot & OH\_JSVM\_CreateEnvFromSnapshot

Use **OH\_JSVM\_CreateSnapshot** to create a VM startup snapshot.

CPP code:

**NOTE**

Register the external dependencies of the JSVM with **initOptions.externalReferences** in **OH\_JSVM\_Init**.

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
#include <fstream>

#define LOG\_DOMAIN 0x0202
#define LOG\_TAG "TEST\_TAG"

static int g\_aa = 0;

#define CHECK\_RET(theCall)                                                                           \\
    do {                                                                                             \\
        JSVM\_Status cond = theCall;                                                                  \\
        if ((cond) != JSVM\_OK) {                                                                     \\
            const JSVM\_ExtendedErrorInfo \*info;                                                      \\
            OH\_JSVM\_GetLastErrorInfo(env, &info);                                                    \\
            OH\_LOG\_ERROR(LOG\_APP,                                                                    \\
                "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \\
                \_\_FILE\_\_,                                                                            \\
                \_\_LINE\_\_,                                                                            \\
                cond,                                                                                \\
                info != nullptr ? info->errorMessage : "");                                          \\
            return -1;                                                                               \\
        }                                                                                            \\
    } while (0)

#define CHECK(theCall)                                                                                              \\
    do {                                                                                                            \\
        JSVM\_Status cond = theCall;                                                                                 \\
        if ((cond) != JSVM\_OK) {                                                                                    \\
            OH\_LOG\_ERROR(                                                                                           \\
                LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", \_\_FILE\_\_, \_\_LINE\_\_, cond); \\
            return -1;                                                                                              \\
        }                                                                                                           \\
    } while (0)

// Call theCall and check whether the return value is JSVM\_OK.
// If no, call GET\_AND\_THROW\_LAST\_ERROR to process the error and return retVal.
#define JSVM\_CALL\_BASE(env, theCall, retVal)                                                         \\
    do {                                                                                             \\
        JSVM\_Status cond = theCall;                                                                  \\
        if (cond != JSVM\_OK) {                                                                       \\
            const JSVM\_ExtendedErrorInfo \*info;                                                      \\
            OH\_JSVM\_GetLastErrorInfo(env, &info);                                                    \\
            OH\_LOG\_ERROR(LOG\_APP,                                                                    \\
                "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \\
                \_\_FILE\_\_,                                                                            \\
                \_\_LINE\_\_,                                                                            \\
                cond,                                                                                \\
                info != nullptr ? info->errorMessage : "");                                          \\
            return retVal;                                                                           \\
        }                                                                                            \\
    } while (0)

// Simplified version of JSVM\_CALL\_BASE, which returns nullptr.
#define JSVM\_CALL(theCall) JSVM\_CALL\_BASE(env, theCall, nullptr)

static const int MAX\_BUFFER\_SIZE = 128;
// Allow the JSVM to call the CreateHelloString() function when needs, using the callback struct and external references.
static JSVM\_Value CreateHelloString(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Value outPut;
    OH\_JSVM\_CreateStringUtf8(env, "Hello world!", JSVM\_AUTO\_LENGTH, &outPut);
    return outPut;
}
// Enable the JSVM to call the bound function through external references.
static JSVM\_CallbackStruct helloCb = {CreateHelloString, nullptr};

static intptr\_t externals\[\] = {
    (intptr\_t)&helloCb,
    0,
};

static JSVM\_Value RunVMScript(JSVM\_Env env, std::string &src)
{
    // Open the handle scope.
    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);
    JSVM\_Value jsStr = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, src.c\_str(), src.size(), &jsStr);
    // Compile the JS code.
    JSVM\_Script script;
    OH\_JSVM\_CompileScript(env, jsStr, nullptr, 0, true, nullptr, &script);
    // Execute the JS code.
    JSVM\_Value result = nullptr;
    OH\_JSVM\_RunScript(env, script, &result);
    // Close the handle scope.
    OH\_JSVM\_CloseHandleScope(env, handleScope);
    return result;
}
// Define OH\_JSVM\_CreateSnapshot.
static void CreateVMSnapshot()
{
    // Create a JSVM instance and open the VM scope.
    JSVM\_VM vm;
    JSVM\_CreateVMOptions vmOptions;
    memset(&vmOptions, 0, sizeof(vmOptions));
    // Use isForSnapshotting to set whether the VM is used for creating snapshots.
    vmOptions.isForSnapshotting = true;
    OH\_JSVM\_CreateVM(&vmOptions, &vm);
    JSVM\_VMScope vmScope;
    OH\_JSVM\_OpenVMScope(vm, &vmScope);
    // Create a JS environment and open the environment scope.
    JSVM\_Env env;
    // Register the native function as a method that can be called from JS.
    JSVM\_PropertyDescriptor descriptor\[\] = {
        {"createHelloString", nullptr, &helloCb, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    };
    OH\_JSVM\_CreateEnv(vm, 1, descriptor, &env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    // Use OH\_JSVM\_CreateSnapshot to create a VM startup snapshot.
    const char \*blobData = nullptr;
    size\_t blobSize = 0;
    JSVM\_Env envs\[1\] = {env};
    OH\_JSVM\_CreateSnapshot(vm, 1, envs, &blobData, &blobSize);
    // Save the snapshot to a file.
    // Save the snapshot data to the /data/storage/el2/base/files/test\_blob.bin directory, which is a sandbox directory.
    // For example, the bundle name is com.example.jsvm. The snapshot file is saved in /data/app/el2/100/base/com.example.jsvm/files/test\_blob.bin.
    std::ofstream file(
        "/data/storage/el2/base/files/test\_blob.bin", std::ios::out | std::ios::binary | std::ios::trunc);
    file.write(blobData, blobSize);
    file.close();
    // Close and destroy the environment and the VM.
    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vmScope);
    OH\_JSVM\_DestroyVM(vm);
}

static void RunVMSnapshot()
{
    // The lifespan of blobData cannot be shorter than that of the VM.
    // Read the snapshot from the file.
    std::vector<char> blobData;
    std::ifstream file("/data/storage/el2/base/files/test\_blob.bin", std::ios::in | std::ios::binary | std::ios::ate);
    size\_t blobSize = file.tellg();
    blobData.resize(blobSize);
    file.seekg(0, std::ios::beg);
    file.read(blobData.data(), blobSize);
    file.close();
    OH\_LOG\_INFO(LOG\_APP, "Test JSVM RunVMSnapshot read file blobSize = : %{public}ld", blobSize);
    // Use the snapshot data to create a VM instance.
    JSVM\_VM vm;
    JSVM\_CreateVMOptions vmOptions;
    memset(&vmOptions, 0, sizeof(vmOptions));
    vmOptions.snapshotBlobData = blobData.data();
    vmOptions.snapshotBlobSize = blobSize;
    OH\_JSVM\_CreateVM(&vmOptions, &vm);
    JSVM\_VMScope vmScope;
    OH\_JSVM\_OpenVMScope(vm, &vmScope);
    // Create an environment from the snapshot.
    JSVM\_Env env;
    OH\_JSVM\_CreateEnvFromSnapshot(vm, 0, &env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    // Execute the JS script. createHelloString() is defined in env of the snapshot record.
    std::string src = "createHelloString()";
    JSVM\_Value result = RunVMScript(env, src);
    // Check the script execution result before closing the environment.
    char str\[MAX\_BUFFER\_SIZE\];
    OH\_JSVM\_GetValueStringUtf8(env, result, str, MAX\_BUFFER\_SIZE, nullptr);
    if (strcmp(str, "Hello world!") != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d", \_\_FILE\_\_, \_\_LINE\_\_);
    }
    // Close and destroy the environment and the VM.
    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vmScope);
    OH\_JSVM\_DestroyVM(vm);
    return;
}

static JSVM\_Value AdjustExternalMemory(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // If external dependencies exist when creating a VM snapshot, register the external dependencies with initOptions.externalReferences in OH\_JSVM\_Init.
    // Create a VM snapshot and save it to a file.
    CreateVMSnapshot();
    // The snapshot records the specific JS execution environment and can be used to quickly restore the JS execution context environment across processes.
    RunVMSnapshot();
    JSVM\_Value result = nullptr;
    OH\_JSVM\_CreateInt32(env, 0, &result);
    return result;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = AdjustExternalMemory},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named adjustExternalMemory and associate it with a callback. This allows the AdjustExternalMemory callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"adjustExternalMemory", nullptr, method, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(adjustExternalMemory();)JS";

static int32\_t TestJSVM()
{
    JSVM\_InitOptions initOptions = {0};
    JSVM\_VM vm;
    JSVM\_Env env = nullptr;
    JSVM\_VMScope vmScope;
    JSVM\_EnvScope envScope;
    JSVM\_HandleScope handleScope;
    JSVM\_Value result;
    // Initialize the JSVM instance.
    if (g\_aa == 0) {
        g\_aa++;
        initOptions.externalReferences = externals;
        int argc = 0;
        char \*\*argv = nullptr;
        initOptions.argc = &argc;
        initOptions.argv = argv;
        CHECK(OH\_JSVM\_Init(&initOptions));
    }
    // Create a JSVM environment.
    CHECK(OH\_JSVM\_CreateVM(nullptr, &vm));
    CHECK(OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env));
    CHECK(OH\_JSVM\_OpenVMScope(vm, &vmScope));
    CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));

    // Call the test function through the script.
    JSVM\_Script script;
    JSVM\_Value jsSrc;
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, srcCallNative, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));

    // Destroy the JSVM environment.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vmScope));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

static napi\_value RunTest(napi\_env env, napi\_callback\_info info)
{
    TestJSVM();
    return nullptr;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    OH\_LOG\_INFO(LOG\_APP, "JSVM Init");
    napi\_property\_descriptor desc\[\] = {
        {"runTest", nullptr, RunTest, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };

    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }

ArkTS code:

import napitest from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // runtest
            napitest.runTest();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Log output when the screen is clicked once:

Test JSVM RunVMSnapshot read file blobSize = : 300064

Log output when the screen is clicked multiple times:

Test JSVM RunVMSnapshot read file blobSize = : 300176
Test JSVM RunVMSnapshot read file blobSize = : 300064
Test JSVM RunVMSnapshot read file blobSize = : 300160
Test JSVM RunVMSnapshot read file blobSize = : 300032
Test JSVM RunVMSnapshot read file blobSize = : 300176
Test JSVM RunVMSnapshot read file blobSize = : 300048

**blobSize** is the snapshot file size obtained through **file.tellg()** when the file is read. Therefore, different values are displayed.
