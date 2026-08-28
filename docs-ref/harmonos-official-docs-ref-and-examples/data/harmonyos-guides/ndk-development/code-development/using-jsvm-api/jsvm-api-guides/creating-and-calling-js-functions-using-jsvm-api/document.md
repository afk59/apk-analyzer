# Creating and Calling JS Functions Using JSVM-API

#### Introduction

JSVM-API provides APIs for calling JavaScript (JS) functions and passing parameters or creating JS methods in C/C++.

#### Basic Concepts

Functions are blocks of reusable code that performs specific tasks or operations.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetCbInfo | Obtains detailed information about the call, such as the parameters and **this** pointer, from the given callback information. |
| OH\_JSVM\_CallFunction | Calls a JS function from a C/C++ addon. |
| OH\_JSVM\_IsFunction | Checks whether an object is a function object. |
| OH\_JSVM\_CreateFunction | Creates a JS function to call a C/C++ function in JS environment. The function can be called only after it is set in a JS object. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in creating and calling functions.

## OH\_JSVM function Test

Full code for the CPP test. The entry is **TEST\_FUNC**.

#include "hilog/log.h"
#include "ark\_runtime/jsvm.h"

#define LOG\_DOMAIN 0x3200
#define LOG\_TAG "APP"

#define CHECK\_RET(cond) \\
  if ((cond)) { \\
    const JSVM\_ExtendedErrorInfo\* info; \\
    OH\_JSVM\_GetLastErrorInfo(env, &info); \\
    OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \_\_FILE\_\_, \_\_LINE\_\_, cond, info != nullptr ? info->errorMessage : ""); \\
    return -1;   \\
  }

#define CHECK(cond) \\
  if (!(cond)) { \\
     OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d", \_\_FILE\_\_, \_\_LINE\_\_, cond); \\
     return -1;   \\
  }

JSVM\_Value NativeCreateFunctionTest(JSVM\_Env env, JSVM\_CallbackInfo info) {
    void \*data = nullptr;
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    JSVM\_Value thisArg;
    // Obtain the callback parameters.
    JSVM\_Status ret = OH\_JSVM\_GetCbInfo(env, info, &argc, &argv\[0\], &thisArg, &data);
    if (ret != JSVM\_OK) {
      const JSVM\_ExtendedErrorInfo\* info;
      OH\_JSVM\_GetLastErrorInfo(env, &info);
      OH\_LOG\_ERROR(LOG\_APP, "jsvm fail file: %{public}s line: %{public}d ret = %{public}d message = %{public}s", \_\_FILE\_\_, \_\_LINE\_\_, ret, info != nullptr ? info->errorMessage : "");
      return nullptr;
    }
    char message\[256\];
    OH\_JSVM\_GetValueStringLatin1(env, argv\[0\], message, 256, nullptr);
    if (data == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "jsvm: %{public}s; callback data null", message);
    } else {
        OH\_LOG\_INFO(LOG\_APP, "jsvm: %{public}s; %{public}s", message, (char\*)data);
    }
    return nullptr;
}

static int32\_t TEST\_FUNC() {
    JSVM\_InitOptions initOptions{};
    JSVM\_VM vm;
    JSVM\_Env env = nullptr;
    JSVM\_VMScope vmScope;
    JSVM\_EnvScope envScope;
    JSVM\_HandleScope handleScope;
    JSVM\_Value result;
    static bool isVMInit = false;
    if (!isVMInit) {
        isVMInit = true;
        // A single process needs to be initialized only once.
        OH\_JSVM\_Init(&initOptions);
    }
    CHECK\_RET(OH\_JSVM\_CreateVM(nullptr, &vm));
    CHECK\_RET(OH\_JSVM\_CreateEnv(vm, 0, nullptr, &env));
    CHECK\_RET(OH\_JSVM\_OpenVMScope(vm, &vmScope));
    CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));

    // Create a function and check it.
    char hello\[\] = "Hello World!";
    JSVM\_CallbackStruct cb = {NativeCreateFunctionTest, (void\*)hello};
    JSVM\_Value func;
    CHECK\_RET(OH\_JSVM\_CreateFunction(env, "", JSVM\_AUTO\_LENGTH, &cb, &func));
    bool isFunction = false;
    CHECK\_RET(OH\_JSVM\_IsFunction(env, func, &isFunction));
    CHECK(isFunction);

    // Set the function to a global object.
    JSVM\_Value global;
    CHECK\_RET(OH\_JSVM\_GetGlobal(env, &global));
    JSVM\_Value key;
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, "NativeFunc", JSVM\_AUTO\_LENGTH, &key));
    CHECK\_RET(OH\_JSVM\_SetProperty(env, global, key, func));

    // Call the function through OH\_JSVM\_CallFunction.
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_CreateStringUtf8(env, "jsvm api call function", JSVM\_AUTO\_LENGTH, &argv\[0\]);
    CHECK\_RET(OH\_JSVM\_CallFunction(env, global, func, 1, argv, &result));

    // Call the function through the script.
    JSVM\_Script script;
    JSVM\_Value jsSrc;
    const char\* srcCallNative = R"JS(NativeFunc('js source call function');)JS";
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, srcCallNative, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));

    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK\_RET(OH\_JSVM\_CloseVMScope(vm, vmScope));
    CHECK\_RET(OH\_JSVM\_DestroyEnv(env));
    CHECK\_RET(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

Expected output:

jsvm: jsvm api call function; Hello World!
jsvm: js source call function; Hello World!
