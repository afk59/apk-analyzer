# Performing Debug Operations Using JSVM-API

#### Overview

JSVM-API provides an API to enable or disable a specified debug option in a specific JSVM\_Env. Currently, **JSVM\_SCOPE\_CHECK** is supported.

#### Debug Options

All debug options are of the JSVM\_DebugOption type.

## JSVM\_SCOPE\_CHECK

-   During development, you may call **JSVM\_Value** variables in the previous **HandleScope** after it ends, causing application crash. **JSVM\_SCOPE\_CHECK** is a method for checking whether the called **JSVM\_Value** variable exceeds the scope of **HandleScope**. If yes, the error "Run in wrong HandleScope" is reported.
-   After this debug option is enabled, if JSVM-API creates a **JSVM\_Value**, **ADD\_VAL\_TO\_SCOPE\_CHECK in function: \[function name\]** is output in HiLog logs, for example, **ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_GetBoolean**. If JSVM-API uses **JSVM\_Value**, **CHECK\_SCOPE in function: \[function name\]** is output in HiLog logs, indicating that **HandleScope** verification is performed on the used **JSVM\_Value**, for example, **CHECK\_SCOPE in function: OH\_JSVM\_IsBoolean**.

#### Available APIs

| Name | Description |
| :-- | :-- |
| OH\_JSVM\_SetDebugOption | Enables or disables a specified debug option in a specific **JSVM\_Env**. The input **debugOption** must be of the **JSVM\_DebugOption** type. The Boolean parameter **isEnabled** is used to control whether to enable the debug option. This API is used only for debugging. Enabling this API may cause performance deterioration. |

#### Sample Code

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in using the API.

## JSVM\_DebugOption

Replace the **TestJSVM()** function in the sample code of [JSVM-API Development Process](../../jsvm-api-development-process/document.md).

-   Call the JSVM\_Value variable in the correct **HandleScope**.

static int32\_t TestJSVM()
{
    JSVM\_InitOptions initOptions = {0};
    JSVM\_VM vm;
    JSVM\_Env env = nullptr;
    JSVM\_VMScope vmScope;
    JSVM\_EnvScope envScope;
    JSVM\_HandleScope handleScope;

    // Initialize the JSVM instance.
    if (g\_aa == 0) {
        g\_aa++;
        CHECK(OH\_JSVM\_Init(&initOptions));
    }
    // Create a JSVM environment.
    CHECK(OH\_JSVM\_CreateVM(nullptr, &vm));
    CHECK(OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env));
    // Enable the JSVM\_SCOPE\_CHECK option.
    CHECK(OH\_JSVM\_SetDebugOption(env, JSVM\_SCOPE\_CHECK, true));
    CHECK(OH\_JSVM\_OpenVMScope(vm, &vmScope));
    CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
    // Open HandleScope.
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));

    // Call the demo function using the script.
    JSVM\_Script script;
    JSVM\_Value jsSrc, result;
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, srcCallNative, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));

    bool boolResult = true;
    // The OH\_JSVM\_IsBoolean API calls the JSVM\_Value variable result.
    JSVM\_Status status = OH\_JSVM\_IsBoolean(env, result, &boolResult);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_IsBoolean: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_IsBoolean: success: %{public}d", boolResult);
    }

    // Destroy the JSVM environment.
    // Close HandleScope.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vmScope));
    // Disable the JSVM\_SCOPE\_CHECK option.
    CHECK(OH\_JSVM\_SetDebugOption(env, JSVM\_SCOPE\_CHECK, false));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

**Execution result**

The following information is displayed in the HiLog:

ADD\_VAL\_TO\_SCOPE\_CHECK in function: NewString
CHECK\_SCOPE in function: OH\_JSVM\_CompileScript
ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_GetCbInfo
ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_GetCbInfo
ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_GetCbInfo
CHECK\_SCOPE in function: OH\_JSVM\_StrictEquals
CHECK\_SCOPE in function: OH\_JSVM\_StrictEquals
JSVM OH\_JSVM\_StrictEquals: success: 0
ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_GetBoolean
ADD\_VAL\_TO\_SCOPE\_CHECK in function: OH\_JSVM\_RunScript
CHECK\_SCOPE in function: OH\_JSVM\_IsBoolean
JSVM OH\_JSVM\_IsBoolean: success: 1

-   The **JSVM\_Value** variable is called in an incorrect HandleScope.

static int32\_t TestJSVM()
{
    JSVM\_InitOptions initOptions = {0};
    JSVM\_VM vm;
    JSVM\_Env env = nullptr;
    JSVM\_VMScope vmScope;
    JSVM\_EnvScope envScope;
    JSVM\_HandleScope handleScope;

    // Initialize the JSVM instance.
    if (g\_aa == 0) {
        g\_aa++;
        CHECK(OH\_JSVM\_Init(&initOptions));
    }
    // Create a JSVM environment.
    CHECK(OH\_JSVM\_CreateVM(nullptr, &vm));
    CHECK(OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env));
    // Enable the JSVM\_SCOPE\_CHECK option.
    CHECK(OH\_JSVM\_SetDebugOption(env, JSVM\_SCOPE\_CHECK, true));
    CHECK(OH\_JSVM\_OpenVMScope(vm, &vmScope));
    CHECK\_RET(OH\_JSVM\_OpenEnvScope(env, &envScope));
    // Open HandleScope.
    CHECK\_RET(OH\_JSVM\_OpenHandleScope(env, &handleScope));

    // Call the demo function using the script.
    JSVM\_Script script;
    JSVM\_Value jsSrc, result;
    CHECK\_RET(OH\_JSVM\_CreateStringUtf8(env, srcCallNative, JSVM\_AUTO\_LENGTH, &jsSrc));
    CHECK\_RET(OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
    CHECK\_RET(OH\_JSVM\_RunScript(env, script, &result));

    bool boolResult = true;

    // Destroy the JSVM environment.
    // Close HandleScope.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handleScope));
    // The OH\_JSVM\_IsBoolean API calls the JSVM\_Value variable result in the incorrect HandleScope.
    JSVM\_Status status = OH\_JSVM\_IsBoolean(env, result, &boolResult);
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vmScope));
    // Disable the JSVM\_SCOPE\_CHECK option.
    CHECK(OH\_JSVM\_SetDebugOption(env, JSVM\_SCOPE\_CHECK, false));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

**Execution result**

The application crashes, the cppcrash log is generated, and the following information is displayed in HiLog:

JSVM Fatal Error Position : "../../../../../../../arkcompiler/jsvm/src/js\_native\_api\_v8.cpp":4537
JSVM Fatal Error Message : "Run in wrong HandleScope"
