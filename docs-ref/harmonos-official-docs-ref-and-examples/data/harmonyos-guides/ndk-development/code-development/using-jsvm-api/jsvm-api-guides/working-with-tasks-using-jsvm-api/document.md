# Working with Tasks Using JSVM-API

#### Introduction

This topic describes how to start a task queue on a VM, check whether there are micro tasks waiting in the queue, and execute the task queue by external events.

#### Basic Concepts

-   Task queue: a mechanism used to manage the scheduling and execution of asynchronous tasks to ensure that tasks are processed in sequence.
-   Micro task: a small task that needs to be executed as soon as possible. Micro tasks usually have a higher priority.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_PumpMessageLoop | Starts running a task queue. |
| OH\_JSVM\_PerformMicrotaskCheckpoint | Executes micro tasks in a task queue. |
| OH\_JSVM\_SetMicrotaskPolicy | Sets the execution policy for micro tasks. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

**Permission requirements**: To run the Wasm bytecode, the application must have the JIT permission. For details about how to apply for the permission, see [Requesting the JIT Permission](../../typical-jsvm-api-use-cases/requesting-the-jit-profile-for-jsvm-api/document.md).

**Running restrictions**: In the current JSVM version, all functional modules of WebAssembly are disabled in Secure Shield mode. You need to evaluate application compatibility based on the restrictions. For details, see [JSVM-API Secure Shield Mode](../../typical-jsvm-api-use-cases/jsvm-api-secure-shield-mode/document.md).

## OH\_JSVM\_PumpMessageLoop & OH\_JSVM\_PerformMicrotaskCheckpoint

Call **OH\_JSVM\_PumpMessageLoop** to start running a task queue.

CPP code:

#include <chrono>
#include <string.h>

static int g\_aa = 0;

// JS code to be executed.
static const char \*STR\_TASK = R"JS(
    // Wasm bytecode (using the add module as an example)
    // The following is the text format of the Wasm bytecode corresponding to wasmBuffer, which contains only the add function.
    // (module
    //   (func $add (param $lhs i32) (param $rhs i32) (result i32)
    //     local.get $lhs
    //     local.get $rhs
    //     i32.add
    //   )
    //   (export "add" (func $add))
    // )
    var wasmBytes = new Uint8Array(\[0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00, 0x01, 0x07, 0x01,
                                       0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f, 0x03, 0x02, 0x01, 0x00, 0x07,
                                       0x07, 0x01, 0x03, 0x61, 0x64, 0x64, 0x00, 0x00, 0x0a, 0x09, 0x01,
                                       0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a, 0x0b\]);

    var p = WebAssembly.instantiate(wasmBytes, {});
    p.then((result) => {
        consoleinfo("Called with instance " + result);
    });
    p.finally(() => {
       consoleinfo("Called Finally");
    });
)JS";

// Ensure normal printing of the JS code information.
static JSVM\_Value ConsoleInfo(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\];
    char log\[256\] = "";
    size\_t logLength = 0;
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL));

    OH\_JSVM\_GetValueStringUtf8(env, args\[0\], log, 255, &logLength);
    log\[255\] = 0;
    OH\_LOG\_INFO(LOG\_APP, "JSVM API TEST: %{public}s", log);
    return nullptr;
}

// Register the consoleinfo callback.
JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = ConsoleInfo},
};
JSVM\_PropertyDescriptor descriptor\[\] = {
    {"consoleinfo", NULL, &param\[0\], NULL, NULL, NULL, JSVM\_DEFAULT},
};

static int32\_t TestJSVM() {
    JSVM\_InitOptions init\_options;
    memset(&init\_options, 0, sizeof(init\_options));
    if (g\_aa == 0) {
        OH\_JSVM\_Init(&init\_options);
        g\_aa++;
    }
    // Create a JSVM instance and open the VM scope.
    JSVM\_VM vm;
    JSVM\_CreateVMOptions options;
    memset(&options, 0, sizeof(options));
    CHECK(OH\_JSVM\_CreateVM(&options, &vm));
    JSVM\_VMScope vm\_scope;
    CHECK(OH\_JSVM\_OpenVMScope(vm, &vm\_scope));
    
    JSVM\_Env env;
    CHECK(OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env));
    JSVM\_EnvScope envScope;
    CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
    JSVM\_HandleScope handlescope;
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handlescope));
    JSVM\_Value sourcecodevalue;
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, STR\_TASK, strlen(STR\_TASK), &sourcecodevalue));
    JSVM\_Script script;
    CHECK\_RET(OH\_JSVM\_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script));
    JSVM\_Value result;
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));
    bool rst = false;
    auto start = std::chrono::system\_clock::now();
    while (true) {
        // If no task is started in the task queue, set rst to false.
        CHECK\_RET(OH\_JSVM\_PumpMessageLoop(vm, &rst));
        CHECK\_RET(OH\_JSVM\_PerformMicrotaskCheckpoint(vm));
        // Exit at the scheduled time.
        auto now = std::chrono::system\_clock::now();
        auto cost = std::chrono::duration\_cast<std::chrono::milliseconds>(now - start).count();
        if (cost > 100) {
            break;
        }
    }

    // Close and destroy the environment and the VM.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handlescope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vm\_scope));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

Expected result:

JSVM API TEST: Called with instance \[object Object\]
JSVM API TEST: Called Finally

## OH\_JSVM\_SetMicrotaskPolicy

Call **OH\_JSVM\_SetMicrotaskPolicy** to set the execution policy for micro tasks.

The execution policy can be any of the following:

-   **JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_EXPLICIT**: executes micro tasks after **OH\_JSVM\_PerformMicrotaskCheckpoint** is called.
-   **JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_AUTO** (default): executes micro tasks automatically when the JS call stack is empty.

CPP code:

// Define OH\_JSVM\_SetMicrotaskPolicy.
static int SetMicrotaskPolicy(JSVM\_VM vm, JSVM\_Env env) {
    // Use the default policy or set the policy to JSVM\_MICROTASK\_AUTO.
    const char \*scriptEvalMicrotask = R"JS(
        evaluateMicrotask = false;
        Promise.resolve().then(()=>{
            evaluateMicrotask = true;
        });
    )JS";
    JSVM\_Script script;
    JSVM\_Value jsSrc;
    JSVM\_Value result;
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, scriptEvalMicrotask, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));
    JSVM\_Value global;
    CHECK\_RET(OH\_JSVM\_GetGlobal(env, &global));
    JSVM\_Value hasEvaluateMicrotask;
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "evaluateMicrotask", &hasEvaluateMicrotask));
    bool val = false;
    CHECK\_RET(OH\_JSVM\_GetValueBool(env, hasEvaluateMicrotask, &val));

    OH\_LOG\_INFO(LOG\_APP, "Policy :JSVM\_MICROTASK\_AUTO, evaluateMicrotask : %{public}d", val);

    // Set the policy to JSVM\_MICROTASK\_EXPLICIT.
    CHECK\_RET(OH\_JSVM\_SetMicrotaskPolicy(vm, JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_EXPLICIT));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "evaluateMicrotask", &hasEvaluateMicrotask));
    CHECK\_RET(OH\_JSVM\_GetValueBool(env, hasEvaluateMicrotask, &val));
    OH\_LOG\_INFO(
        LOG\_APP,
        "Policy :JSVM\_MICROTASK\_AUTO, evaluateMicrotask before calling OH\_JSVM\_PerformMicrotaskCheckpoint: %{public}d",
        val);

    CHECK\_RET(OH\_JSVM\_PerformMicrotaskCheckpoint(vm));
    CHECK\_RET(OH\_JSVM\_GetNamedProperty(env, global, "evaluateMicrotask", &hasEvaluateMicrotask));
    CHECK\_RET(OH\_JSVM\_GetValueBool(env, hasEvaluateMicrotask, &val));
    OH\_LOG\_INFO(
        LOG\_APP,
        "Policy :JSVM\_MICROTASK\_AUTO, evaluateMicrotask after calling OH\_JSVM\_PerformMicrotaskCheckpoint: %{public}d",
        val);

    return 0;
}

static void RunDemo(JSVM\_VM vm, JSVM\_Env env) {
    if (SetMicrotaskPolicy(vm, env) != 0) {
        OH\_LOG\_INFO(LOG\_APP, "Run Microtask Policy failed");
    }
}

static int32\_t TestJSVM() {
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
        CHECK(OH\_JSVM\_Init(&initOptions));
    }
    // Create a JSVM environment.
    CHECK(OH\_JSVM\_CreateVM(nullptr, &vm));
    CHECK(OH\_JSVM\_CreateEnv(vm, 0, nullptr, &env));
    CHECK(OH\_JSVM\_OpenVMScope(vm, &vmScope));
    CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));

    // Call the demo function using the script.
    RunDemo(vm, env);

    // Destroy the JSVM environment.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vmScope));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

Expected result:

Policy :JSVM\_MICROTASK\_AUTO, evaluateMicrotask : 1
Policy :JSVM\_MICROTASK\_AUTO, evaluateMicrotask before calling OH\_JSVM\_PerformMicrotaskCheckpoint: 0
Policy :JSVM\_MICROTASK\_AUTO, evaluateMicrotask after calling OH\_JSVM\_PerformMicrotaskCheckpoint: 1
