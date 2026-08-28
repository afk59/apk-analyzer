# JSVM-API Data Types and APIs

#### Data Types

## JSVM\_Status

Defines an enum for the execution statuses of a JSVM-API call.

Each time a JSVM-API function is called, a value of **JSVM\_Status** is returned to indicate the execution result.

    typedef enum {
        JSVM\_OK,                              /\* Successful. \*/
        JSVM\_INVALID\_ARG,                     /\* Invalid parameters. \*/
        JSVM\_OBJECT\_EXPECTED,                 /\* An object is expected. \*/
        JSVM\_STRING\_EXPECTED,                 /\* A string is expected. \*/
        JSVM\_NAME\_EXPECTED,                   /\* A name is expected. \*/
        JSVM\_FUNCTION\_EXPECTED,               /\* A function is expected. \*/
        JSVM\_NUMBER\_EXPECTED,                 /\* A number is expected. \*/
        JSVM\_BOOL\_EXPECTED,                   /\* A Boolean value is expected. \*/
        JSVM\_ARRAY\_EXPECTED,                  /\* An array is expected. \*/
        JSVM\_GENERIC\_FAILURE,                 /\* Generic failure. \*/
        JSVM\_PENDING\_EXCEPTION,               /\* Pending exception. \*/
        JSVM\_CANCELLED,                       /\* Canceled \*/
        JSVM\_ESCAPE\_CALLED\_TWICE,             /\* Escape is called twice. \*/
        JSVM\_HANDLE\_SCOPE\_MISMATCH,           /\* Handle scope does not match. \*/
        JSVM\_CALLBACK\_SCOPE\_MISMATCH,         /\* Callback scope does not match. \*/
        JSVM\_QUEUE\_FULL,                      /\* The queue is full. \*/
        JSVM\_CLOSING,                         /\* Closing. \*/
        JSVM\_BIGINT\_EXPECTED,                 /\* A Bigint value is expected. \*/
        JSVM\_DATE\_EXPECTED,                   /\* A date is expected. \*/
        JSVM\_ARRAYBUFFER\_EXPECTED,            /\* An ArrayBuffer is expected. \*/
        JSVM\_DETACHABLE\_ARRAYBUFFER\_EXPECTED, /\* A detachable ArrayBuffer is expected. \*/
        JSVM\_WOULD\_DEADLOCK,                  /\* About to deadlock. \*/
        JSVM\_NO\_EXTERNAL\_BUFFERS\_ALLOWED,     /\* External buffers are not allowed. \*/
        JSVM\_CANNOT\_RUN\_JS,                   /\* JS cannot be executed. \*/
        JSVM\_INVALID\_TYPE,                    /\* Invalid type. \*/
        JSVM\_JIT\_MODE\_EXPECTED,                /\* JIT mode is expected. \*/
    } JSVM\_Status;

## JSVM\_ExtendedErrorInfo

Defines a struct that represents detailed error information when a JSVM-API call fails.

typedef struct {
    const char\* errorMessage;
    void\* engineReserved;
    uint32\_t engineErrorCode;
    JSVM\_Status errorCode;
} JSVM\_ExtendedErrorInfo;

## JSVM\_Value

Defines a JavaScript (JS) value in C++.

## JSVM\_Env

-   Defines the context for the underlying JSVM-API implementation. It is passed to the JSVM-API in a native function as an input parameter.
    
-   When the native addon exits, **JSVM\_Env** becomes invalid and this event is passed to **OH\_JSVM\_SetInstanceData** via a callback.
    
-   Avoid caching **JSVM\_Env** or passing **JSVM\_Env** between different worker threads.
    
-   If **JSVM\_Env** is shared between different threads, the **threadlocal** variable must be isolated across threads. For this purpose, close the env scope of the current thread before switching to another thread and open a new env scope in each thread switched to.
    

## JSVM\_ValueType

Defines an enum for the **JSVM\_Value** types. **JSVM\_Value** includes the types defined in ECMAScript. **JSVM\_EXTERNAL** indicates an external data type.

typedef enum {
    JSVM\_UNDEFINED,
    JSVM\_NULL,
    JSVM\_BOOLEAN,
    JSVM\_NUMBER,
    JSVM\_STRING,
    JSVM\_SYMBOL,
    JSVM\_OBJECT,
    JSVM\_FUNCTION,
    JSVM\_EXTERNAL,
    JSVM\_BIGINT,
} JSVM\_ValueType;

## JSVM\_TypedarrayType

Defines an enum for data types of the **TypedArray** object.

typedef enum {
    JSVM\_INT8\_ARRAY,
    JSVM\_UINT8\_ARRAY,
    JSVM\_UINT8\_CLAMPED\_ARRAY,
    JSVM\_INT16\_ARRAY,
    JSVM\_UINT16\_ARRAY,
    JSVM\_INT32\_ARRAY,
    JSVM\_UINT32\_ARRAY,
    JSVM\_FLOAT32\_ARRAY,
    JSVM\_FLOAT64\_ARRAY,
    JSVM\_BIGINT64\_ARRAY,
    JSVM\_BIGUINT64\_ARRAY,
} JSVM\_TypedarrayType;

## JSVM\_RegExpFlags

Defines an enum for regular expression flags.

typedef enum {
    JSVM\_REGEXP\_NONE = 0,
    JSVM\_REGEXP\_GLOBAL = 1 << 0,
    JSVM\_REGEXP\_IGNORE\_CASE = 1 << 1,
    JSVM\_REGEXP\_MULTILINE = 1 << 2,
    JSVM\_REGEXP\_STICKY = 1 << 3,
    JSVM\_REGEXP\_UNICODE = 1 << 4,
    JSVM\_REGEXP\_DOT\_ALL = 1 << 5,
    JSVM\_REGEXP\_LINEAR = 1 << 6,
    JSVM\_REGEXP\_HAS\_INDICES = 1 << 7,
    JSVM\_REGEXP\_UNICODE\_SETS = 1 << 8,
} JSVM\_RegExpFlags;

## Compilation Option Types

**JSVM\_CompileOptions**

Defines a struct that represents the type of the elements in **options** of **OH\_JSVM\_CompileScriptWithOptions**.

The struct consists of the following parameters:

-   **id**: identifies a compilation option.
-   **content**: specifies a compilation option.

**id** and **content** together define a compilation option.

typedef struct {
    /\*\* Compilation option type. \*/
    JSVM\_CompileOptionId id;
    /\*\* Compilation option content. \*/
    union {
      /\*\* ptr type. \*/
      void \*ptr;
      /\*\* int type. \*/
      int num;
      /\*\* bool type. \*/
      \_Bool boolean;
    } content;
} JSVM\_CompileOptions;

**JSVM\_CompileOptionId**

Defines an enum for **id** in **JSVM\_CompileOptions**. Each **id** corresponds to a **content** value. The value **JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP** corresponds to bool and is valid only when **sourceMapUrl** in **JSVM\_ScriptOrigin** is not empty.

typedef enum {
    /\*\* Compilation mode. \*/
    JSVM\_COMPILE\_MODE,
    /\*\* Code cache. \*/
    JSVM\_COMPILE\_CODE\_CACHE,
    /\*\* Script origin. \*/
    JSVM\_COMPILE\_SCRIPT\_ORIGIN,
    /\*\* Compilation profile. \*/
    JSVM\_COMPILE\_COMPILE\_PROFILE,
    /\*\* Switch for source map support. \*/
    JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP,
} JSVM\_CompileOptionId;

**JSVM\_CompileMode**

Defines an enum for the compilation modes when **id** is **JSVM\_COMPILE\_MODE**.

-   **JSVM\_COMPILE\_MODE\_DEFAULT**: indicates the default compilation mode.
-   **JSVM\_COMPILE\_MODE\_CONSUME\_CODE\_CACHE**: indicates the compilation with the code cache.
-   **JSVM\_COMPILE\_MODE\_EAGER\_COMPILE**: indicates full compilation.
-   **JSVM\_COMPILE\_MODE\_PRODUCE\_COMPILE\_PROFILE**/**JSVM\_COMPILE\_MODE\_CONSUME\_COMPILE\_PROFILE**: reserved at present.

typedef enum {
    /\*\* Default mode. \*/
    JSVM\_COMPILE\_MODE\_DEFAULT,
    /\*\* Compilation by leveraging the code cache. \*/
    JSVM\_COMPILE\_MODE\_CONSUME\_CODE\_CACHE,
    /\*\* Full compilation. \*/
    JSVM\_COMPILE\_MODE\_EAGER\_COMPILE,
    /\*\* Compilation with a preset compilation profile. \*/
    JSVM\_COMPILE\_MODE\_PRODUCE\_COMPILE\_PROFILE,
    /\*\* Compilation by using a compile profile. \*/
    JSVM\_COMPILE\_MODE\_CONSUME\_COMPILE\_PROFILE,
} JSVM\_CompileMode;

**JSVM\_CodeCache**

Defines a struct that represents the code cache when **id** is **JSVM\_COMPILE\_CODE\_CACHE**. The struct consists of the following:

-   **cache**: pointer to the code cache to use.
-   **length**: size of the code cache.

typedef struct {
    /\*\* cache pointer. \*/
    uint8\_t \*cache;
    /\*\* length. \*/
    size\_t length;
} JSVM\_CodeCache;

**JSVM\_ScriptOrigin**

Defines a struct that represents the source code of the script to compile when **id** is **JSVM\_COMPILE\_SCRIPT\_ORIGIN**. The struct consists of the following:

-   **sourceMapUrl**: path of the source map. Currently, only the local paths of the device are supported. This parameter can be left empty.
-   **resourceName**: name of the JS script to be compiled.

typedef struct {
    /\*\* Source map URL. \*/
    const char\* sourceMapUrl;
    /\*\* Script to compile. \*/
    const char\* resourceName;
    /\*\* Line offset in the script. \*/
    size\_t resourceLineOffset;
    /\*\* Column offset in the script. \*/
    size\_t resourceColumnOffset;
} JSVM\_ScriptOrigin;

## JSVM

## Memory Management Types

JSVM-API provides the following memory management types:

**JSVM\_HandleScope**

Data used to manage the lifecycle of JS objects. It ensures that all JS objects created in a specified range remain active until the end. This can prevent released objects from being used, which improves code reliability and performance.

**JSVM\_EscapableHandleScope**

-   It is created by **OH\_JSVM\_OpenEscapableHandleScope** and closed by **OH\_JSVM\_CloseEscapableHandleScope**.
    
-   It is a special type of handle range used to return values created within the scope of **JSVM\_EscapableHandleScope** to a parent scope.
    
-   You can use **OH\_JSVM\_EscapeHandle** to promote values in **JSVM\_EscapableHandleScope** to JavaScript objects for the lifetime of the outer scope.
    

**JSVM\_Ref**

Reference to **JSVM\_Value**, which allows you to manage the lifecycle of JS values.

**JSVM\_TypeTag**

Struct containing two unsigned 64-bit integers to identify the type of a JSVM-API value.

typedef struct {
    uint64\_t lower;
    uint64\_t upper;
} JSVM\_TypeTag;

-   It is a 128-bit value stored as two unsigned 64-bit integers. It is used to tag JS objects to ensure that they are of a certain type.
    
-   This is a stronger check than **OH\_JSVM\_Instanceof** because **OH\_JSVM\_Instanceof** may report a false positive if the object's prototype is manipulated.
    
-   The combination of **JSVM\_TypeTag** and **OH\_JSVM\_Wrap** is useful because it ensures that the pointer retrieved from a wrapped object can be safely converted to the native type corresponding to the type tag that had been previously applied to the JS object.
    

## Callback Types

JSVM-API provides the following callback types:

**JSVM\_CallbackStruct**

Callback function pointer and data for user-provided native callbacks, which are to be exposed to JS via JSVM-API. For example, you can use **OH\_JSVM\_CreateFunction** to create a JS function bound to a native callback defined by **JSVM\_CallbackStruct**. Unless otherwise required in object lifecycle management, do not create a handle or callback scope in this callback.

typedef struct {
  JSVM\_Value(\*callback)(JSVM\_Env env, JSVM\_CallbackInfo info);
  void\* data;
} JSVM\_CallbackStruct;

**JSVM\_Callback**

Alias of the **JSVM\_CallbackStruct** pointer type.

It is defined as follows:

typedef JSVM\_CallbackStruct\* JSVM\_Callback;

**JSVM\_CallbackInfo**

User-defined native callback. The type of the first parameter is **JSVM\_Env**, and that of the second parameter is **JSVM\_CallbackInfo**. **JSVM\_CallbackInfo** can be used to obtain additional information about the context in which the callback was invoked, for example, the parameter list. When a native callback is implemented, **OH\_JSVM\_GetCbInfo** is used to obtain the invoking information from **JSVM\_CallbackInfo**.

**JSVM\_Finalize**

Function pointer, which is passed in APIs such as **OH\_JSVM\_SetInstanceData**, **OH\_JSVM\_CreateExternal**, and **OH\_JSVM\_Wrap**. **JSVM\_Finalize** is called to release the native object after a JS object is garbage collected. JSVM does not guarantee whether to execute the callback or the timing of executing the callback. You should not depend on the execution timing of the callback.

The format is as follows:

typedef void (\*JSVM\_Finalize)(JSVM\_Env env, void\* finalizeData, void\* finalizeHint);

**JSVM\_PropertyHandlerConfigurationStruct**

Callback to be invoked when the **getter()**, **setter()**, **deleter()**, or **enumerator()** of an object is executed.

typedef struct {
    JSVM\_Value(JSVM\_CDECL\* genericNamedPropertyGetterCallback)(JSVM\_Env env,
                                                               JSVM\_Value name,
                                                               JSVM\_Value thisArg,
                                                               JSVM\_Value namedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericNamedPropertySetterCallback)(JSVM\_Env env,
                                                               JSVM\_Value name,
                                                               JSVM\_Value property,
                                                               JSVM\_Value thisArg,
                                                               JSVM\_Value namedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericNamedPropertyDeleterCallback)(JSVM\_Env env,
                                                                JSVM\_Value name,
                                                                JSVM\_Value thisArg,
                                                                JSVM\_Value namedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericNamedPropertyEnumeratorCallback)(JSVM\_Env env,
                                                                   JSVM\_Value thisArg,
                                                                   JSVM\_Value namedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericIndexedPropertyGetterCallback)(JSVM\_Env env,
                                                                JSVM\_Value index,
                                                                JSVM\_Value thisArg,
                                                                JSVM\_Value indexedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericIndexedPropertySetterCallback)(JSVM\_Env env,
                                                                 JSVM\_Value index,
                                                                 JSVM\_Value property,
                                                                 JSVM\_Value thisArg,
                                                                 JSVM\_Value indexedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericIndexedPropertyDeleterCallback)(JSVM\_Env env,
                                                                  JSVM\_Value index,
                                                                  JSVM\_Value thisArg,
                                                                  JSVM\_Value indexedPropertyData);
    JSVM\_Value(JSVM\_CDECL\* genericIndexedPropertyEnumeratorCallback)(JSVM\_Env env,
                                                                     JSVM\_Value thisArg,
                                                                     JSVM\_Value indexedPropertyData);
    JSVM\_Value namedPropertyData;
    JSVM\_Value indexedPropertyData;
} JSVM\_PropertyHandlerConfigurationStruct;

**JSVM\_PropertyHandlerCfg**

Pointer type of the struct that contains the property listening callback.

The usage is as follows:

typedef JSVM\_PropertyHandlerConfigurationStruct\* JSVM\_PropertyHandlerCfg;

#### APIs

JSVM-API provides capabilities of the standard JS engine. JSVM-API can be dynamically linked to JS engine libraries of different versions to shield the differences between engine interfaces. JSVM-API provides capabilities, such as VM lifecycle management, JS context management, JS code execution, JS/C++ interaction, context snapshot management, and code caching. Read on the following for details.

## Creating a VM Instance and JS Context

**Scenarios**

Before executing JS code, you need to create a JavaScript virtual machine (JSVM) and JS context.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_Init | Initializes a JS engine instance. |
| OH\_JSVM\_CreateVM | Creates a JSVM instance. |
| OH\_JSVM\_DestroyVM | Destroys a JSVM instance. |
| OH\_JSVM\_OpenVMScope | Opens a VM scope. The VM instance can be used only within the scope and will not be garbage-collected until the scope is closed. |
| OH\_JSVM\_CloseVMScope | Closes a VM scope. |
| OH\_JSVM\_CreateEnv | Creates a JS context and registers the specified native function. |
| OH\_JSVM\_DestroyEnv | Destroys a JS context. |
| OH\_JSVM\_OpenEnvScope | Opens a JS context scope. The context can be used only within the scope. |
| OH\_JSVM\_CloseEnvScope | Closes a JS context scope. |
| OH\_JSVM\_OpenHandleScope | Opens a handle scope. **JSVM\_Value** within the scope will not be garbage-collected. |
| OH\_JSVM\_CloseHandleScope | Closes a handle scope. |

Using **JSVM\_InitOptions**

JSVM provides multiple configuration options, allowing you to flexibly configure the behavior of **OH\_JSVM\_Init**. You can use the **OH\_JSVM\_GetVMInfo** API to obtain the V8 engine version corresponding to the current JSVM version. The options supported by the JSVM are the same as those supported by the corresponding V8 engine version. For details about how to use the **OH\_JSVM\_GetVMInfo** API, see [Obtaining the JSVM-API Version Using JSVM-API](../jsvm-api-guides/obtaining-the-jsvm-api-version-using-jsvm-api/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/65jX5ayKSv2HCzX584EzEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E5501B9F66333BA37A5A261653068E007438A26B19BE899D724FBFA2652E907)

-   You are advised to use only the default configuration options of the JSVM unless otherwise required.

Example:

Initialize a JSVM in normal mode.

static void NormalInit(bool &vmInit) {
    if (!vmInit) {
        // The JSVM only needs to be initialized once.
        JSVM\_InitOptions initOptions;
        memset(&initOptions, 0, sizeof(initOptions));
        JSVM\_Status cond = OH\_JSVM\_Init(&initOptions);
        if(cond == JSVM\_OK) {
            vmInit = true;
        } else {
            vmInit = false;
        }
    }
}

Example:

Initialize a JSVM with low memory usage.

static void LowMemoryInit(bool &vmInit) {
    if (!vmInit) {
        // The JSVM only needs to be initialized once.
        JSVM\_InitOptions initOptions;
        int argc = 4;
        initOptions.argc = &argc;
        const char\* argv\[4\];
        argv\[1\] = "--incremental-marking-hard-trigger=40";
        argv\[2\] = "--min-semi-space-size=1";
        argv\[3\] = "--max-semi-space-size=4";
        initOptions.argv = const\_cast<char\*\*>(argv);
        OH\_JSVM\_Init(&initOptions);
        vmInit = true;
    }
}

Example:

Initialize a JSVM with a low GC triggering frequency.

static void LowGCFrequencyInit(bool &vmInit) {
    if (!vmInit) {
        // The JSVM only needs to be initialized once.
        JSVM\_InitOptions initOptions;
        int argc = 4;
        initOptions.argc = &argc;
        const char\* argv\[4\];
        argv\[1\] = "--incremental-marking-hard-trigger=80";
        argv\[2\] = "--min-semi-space-size=16";
        argv\[3\] = "--max-semi-space-size=16";
        initOptions.argv = const\_cast<char\*\*>(argv);
        OH\_JSVM\_Init(&initOptions);
        vmInit = true;
    }
}

Execution result:

The preceding three interfaces can be used to initialize JSVMs with different features. After initialization, a JSVM instance can be created to run JS scripts.

Compared with **NormalInit()**, **LowGCFrequencyInit()** initializes JSVMs with a lower GC triggering frequency, and **LowMemoryInit()** initializes JSVMs with lower memory usage.

**Creating a JSVM instance**

Example:

Create and destroy a JSVM instance (including the execution context).

bool VM\_INIT = false;

static JSVM\_Value ConsoleInfo(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\];
    char log\[256\] = "";
    size\_t logLength = 0;
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL);

    OH\_JSVM\_GetValueStringUtf8(env, args\[0\], log, 255, &logLength);
    log\[255\] = 0;
    OH\_LOG\_INFO(LOG\_APP, "JSVM API TEST: %{public}s", log);
    return nullptr;
}

static JSVM\_Value Add(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 2;
    JSVM\_Value args\[2\];
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL);
    double num1 = 0;
    double num2 = 0;
    OH\_JSVM\_GetValueDouble(env, args\[0\], &num1);
    OH\_JSVM\_GetValueDouble(env, args\[1\], &num2);
    JSVM\_Value sum = nullptr;
    OH\_JSVM\_CreateDouble(env, num1 + num2, &sum);
    return sum;
}

static napi\_value MyJSVMDemo(\[\[maybe\_unused\]\] napi\_env \_env, \[\[maybe\_unused\]\] napi\_callback\_info \_info) {
    std::thread t(\[\]() {
        // Initialized a JSVM with the required capability based on service requirements.
        // 1. Call NormalInit to initialize the default JSVM.
        // 2. Call LowMemoryInit to initialize a JSVM with low memory usage.
        // 3. Call LowGCFrequencyInit to initialize a JSVM with a low GC triggering frequency.
        NormalInit(VM\_INIT);
        // Create a VM instance and open the VM scope.
        JSVM\_VM vm;
        JSVM\_CreateVMOptions options;
        memset(&options, 0, sizeof(options));
        OH\_JSVM\_CreateVM(&options, &vm);

        JSVM\_VMScope vmScope;
        OH\_JSVM\_OpenVMScope(vm, &vmScope);

        JSVM\_CallbackStruct param\[\] = {
            {.data = nullptr, .callback = ConsoleInfo},
            {.data = nullptr, .callback = Add},
        };
        JSVM\_PropertyDescriptor descriptor\[\] = {
            {"consoleinfo", NULL, &param\[0\], NULL, NULL, NULL, JSVM\_DEFAULT},
            {"add", NULL, &param\[1\], NULL, NULL, NULL, JSVM\_DEFAULT},
        };
        // Create env, register a native method, and open an env scope.
        JSVM\_Env env;
        OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env);

        JSVM\_EnvScope envScope;
        OH\_JSVM\_OpenEnvScope(env, &envScope);

        // Open a handle scope.
        JSVM\_HandleScope handleScope;
        OH\_JSVM\_OpenHandleScope(env, &handleScope);

        std::string sourceCodeStr = "\\
        {\\
            let value = add(4.96, 5.28);\\
            consoleinfo('Result is:' + value);\\
        }";
        // Compile the JS script.
        JSVM\_Value sourceCodeValue;
        OH\_JSVM\_CreateStringUtf8(env, sourceCodeStr.c\_str(), sourceCodeStr.size(), &sourceCodeValue);
        JSVM\_Script script;
        OH\_JSVM\_CompileScript(env, sourceCodeValue, nullptr, 0, true, nullptr, &script);
        JSVM\_Value result;
        // Run the JS script.
        OH\_JSVM\_RunScript(env, script, &result);
        JSVM\_ValueType type;
        OH\_JSVM\_Typeof(env, result, &type);
        OH\_LOG\_INFO(LOG\_APP, "JSVM API TEST type: %{public}d", type);

        // Exit the VM and release the memory.
        OH\_JSVM\_CloseHandleScope(env, handleScope);

        OH\_JSVM\_CloseEnvScope(env, envScope);
        OH\_JSVM\_DestroyEnv(env);

        OH\_JSVM\_CloseVMScope(vm, vmScope);
        OH\_JSVM\_DestroyVM(vm);
    });

    t.detach();

    return nullptr;
}

## Compiling and Running JS Code

**Scenarios**

Compile and run JS code.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CompileScript | Compiles JS code and returns the compiled script bound to the current environment. |
| OH\_JSVM\_CompileScriptWithOrigin | Compiles JS code and returns the compiled script bound to the current environment, with source code information including **sourceMapUrl** and source file name to process source map information. |
| OH\_JSVM\_CompileScriptWithOptions | Compiles a script with the specified options. You can pass the compilation options via the **option** array, which supports option extensions. |
| OH\_JSVM\_CreateCodeCache | Creates a code cache for the compiled script. |
| OH\_JSVM\_RunScript | Executes the compiled script. If the JIT permission is not supported, the script containing WebAssembly will fail to be executed. The performance varies in specific scenarios, and a log is printed for notification. |

Example:

Compile and execute JavaScript code. Specifically, create VM instances, register functions, execute JavaScript code, and destroy VM instances.

CPP code:

#include <cstring>
#include <fstream>
#include <string>
#include <vector>

// Add the dependency libjsvm.so.
#include "ark\_runtime/jsvm.h"

using namespace std;

static JSVM\_Value Hello(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_Value output;
    void\* data = nullptr;
    OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, nullptr, &data);
    OH\_JSVM\_CreateStringUtf8(env, (char\*)data, strlen((char\*)data), &output);
    return output;
}

static JSVM\_CallbackStruct hello\_cb = { Hello, (void\*)"Hello" };

static string srcGlobal = R"JS(
const concat = (...args) => args.reduce((a, b) => a + b);
)JS";

static void RunScriptWithOption(JSVM\_Env env, string& src,
                                uint8\_t\*\* dataPtr = nullptr,
                                size\_t\* lengthPtr = nullptr) {
    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);

    JSVM\_Value jsSrc;
    OH\_JSVM\_CreateStringUtf8(env, src.c\_str(), src.size(), &jsSrc);

    uint8\_t\* data = dataPtr ? \*dataPtr : nullptr;
    auto compilMode = data ? JSVM\_COMPILE\_MODE\_CONSUME\_CODE\_CACHE :  JSVM\_COMPILE\_MODE\_DEFAULT;
    size\_t length = lengthPtr ? \*lengthPtr : 0;
    JSVM\_Script script;
    // Compile the JS code.
    JSVM\_ScriptOrigin origin {
        // In this example, the bundle name is helloworld, and the path of the sourcemap is /data/app/el2/100/base/com.example.helloworld/files/index.js.map.
        .sourceMapUrl = "/data/app/el2/100/base/com.example.helloworld/files/index.js.map",
        // Name of the source file.
        .resourceName = "index.js",
        // Start row and column number of script in the source file
        .resourceLineOffset = 0,
        .resourceColumnOffset = 0,
    };
    JSVM\_CompileOptions option\[3\];
    option\[0\] = {
        .id = JSVM\_COMPILE\_MODE,
        .content = { .num = compilMode }
    };
    JSVM\_CodeCache codeCache = {
        .cache = data,
        .length = length
    };
    option\[1\] = {
        .id = JSVM\_COMPILE\_CODE\_CACHE,
        .content = { .ptr = &codeCache }
    };
    // The default value of JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP is false. If the value is true, sourceMapUrl cannot be empty.
    option\[2\] = {
        .id = JSVM\_COMPILE\_ENABLE\_SOURCE\_MAP,
        .content = { .boolean = true }
    };
    OH\_JSVM\_CompileScriptWithOptions(env, jsSrc, 3, option, &script);

    JSVM\_Value result;
    // Run the JS code.
    OH\_JSVM\_RunScript(env, script, &result);

    char resultStr\[128\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, result, resultStr, 128, &size);

    OH\_JSVM\_CloseHandleScope(env, handleScope);
}

static void RunScript(JSVM\_Env env, string& src,
                       bool withOrigin = false,
                       uint8\_t\*\* dataPtr = nullptr,
                       size\_t\* lengthPtr = nullptr) {
    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);

    JSVM\_Value jsSrc;
    OH\_JSVM\_CreateStringUtf8(env, src.c\_str(), src.size(), &jsSrc);

    uint8\_t\* data = dataPtr ? \*dataPtr : nullptr;
    size\_t length = lengthPtr ? \*lengthPtr : 0;
    bool cacheRejected = true;
    JSVM\_Script script;
    // Compile the JS code.
    if (withOrigin) {
        JSVM\_ScriptOrigin origin {
            // In this example, the bundle name is helloworld, and the path of the sourcemap is /data/app/el2/100/base/com.example.helloworld/files/index.js.map.
            .sourceMapUrl = "/data/app/el2/100/base/com.example.helloworld/files/index.js.map",
            // Name of the source file.
            .resourceName = "index.js",
            // Start row and column number of script in the source file
            .resourceLineOffset = 0,
            .resourceColumnOffset = 0,
        };
        OH\_JSVM\_CompileScriptWithOrigin(env, jsSrc, data, length, true, &cacheRejected, &origin, &script);
    } else {
        OH\_JSVM\_CompileScript(env, jsSrc, data, length, true, &cacheRejected, &script);
    }
    printf("Code cache is %s\\n", cacheRejected ? "rejected" : "used");

    JSVM\_Value result;
    // Run the JS code.
    OH\_JSVM\_RunScript(env, script, &result);

    char resultStr\[128\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, result, resultStr, 128, &size);

    OH\_JSVM\_CloseHandleScope(env, handleScope);
}

void RunWithOption(uint8\_t\*\* dataPtr, size\_t\* lengthPtr) {
    // Create a VM instance.
    JSVM\_VM vm;
    OH\_JSVM\_CreateVM(nullptr, &vm);
    JSVM\_VMScope vmScope;
    OH\_JSVM\_OpenVMScope(vm, &vmScope);

    JSVM\_Env env;
    // Register the native function as a method that can be called by a JS API. hello\_cb holds the pointer and parameters of the native function.
    JSVM\_PropertyDescriptor descriptors\[\] = {
        { "hello", NULL, &hello\_cb, NULL, NULL, NULL, JSVM\_DEFAULT }
    };
    OH\_JSVM\_CreateEnv(vm, 1, descriptors, &env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    // Execute the JS source code src, which can contain any JS syntax. The registered native function can also be invoked.
    auto src = srcGlobal + "concat(hello(), ', ', 'World', ' from RunWithOption!')";
    // Use RunScriptWithOption, which covers all the functionalities of the \*\*Compile\*\* APIs and provides extensions.
    RunScriptWithOption(env, src, dataPtr, lengthPtr);

    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vmScope);
    OH\_JSVM\_DestroyVM(vm);

    bool result = true;
    OH\_LOG\_INFO(LOG\_APP, "RunWithOption: success: %{public}d", result);
}

void RunWithOrigin(uint8\_t \*\*dataPtr, size\_t \*lengthPtr) {
    // Create a VM instance.
    JSVM\_VM vm;
    JSVM\_CreateVMOptions options;
    memset(&options, 0, sizeof(options));
    options.isForSnapshotting = true;
    OH\_JSVM\_CreateVM(&options, &vm);
    JSVM\_VMScope vmScope;
    OH\_JSVM\_OpenVMScope(vm, &vmScope);

    // Create env from a snapshot.
    JSVM\_Env env;
    // Register the native function as a method that can be called by a JS API. hello\_cb holds the pointer and parameters of the native function.
    JSVM\_PropertyDescriptor descriptors\[\] = {
        { "hello", NULL, &hello\_cb, NULL, NULL, NULL, JSVM\_DEFAULT }
    };
    OH\_JSVM\_CreateEnv(vm, 1, descriptors, &env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    // Run the JS script. Because the snapshot contains hello() defined in env, you do not need to redefine hello(). If dataPtr contains the compiled JS script, the JS script can be directly executed, which avoids repeated compilation from the source code.
    string src = "concat(hello(), ', ', 'World', ' from RunWithOrigin!')";
    RunScript(env, src, true, dataPtr, lengthPtr);

    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vmScope);
    OH\_JSVM\_DestroyVM(vm);

    bool result = true;
    OH\_LOG\_INFO(LOG\_APP, "RunWithOrigin: success: %{public}d", result);
}

static JSVM\_Value RunDemo(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);

    char\* str = "WithOrigin";
    size\_t len = strlen(str);
    JSVM\_Value result = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, str, len, &result);

    uint8\_t\* data = nullptr;
    size\_t length = 0;
    bool equal = false;
    OH\_JSVM\_StrictEquals(env, args\[0\], result, &equal);
    const auto run = equal ? RunWithOrigin : RunWithOption;
    run(&data, &length);
    delete\[\] data;

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
const char \*srcCallNative = R"JS(RunDemo("WithOrigin"); RunDemo("WithOption"))JS";

Expected result:

RunWithOption: success: 1
RunWithOrigin: success: 1

For details about how to use the **OH\_JSVM\_CreateCodeCache** API, see [Accelerating Compilation Using a Code Cache](../typical-jsvm-api-use-cases/jsvm-api-tuning-and-performant-coding-cases/accelerating-compilation-using-a-code-cache/document.md).

## Compiling the Wasm Module

**Scenarios**

JSVM-API provides APIs for compiling the WebAssembly (Wasm) bytecode, optimizing Wasm functions, and serializing and deserializing Wasm caches.

For details, see [Working with Wasm Using JSVM-API](../jsvm-api-guides/working-with-wasm-using-jsvm-api/document.md).

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CompileWasmModule | Compiles the Wasm bytecode into a Wasm module. If the **cache** parameter is passed in, the cache will be deserialized into a Wasm module first. The compilation is performed when the deserialization fails. If the JIT permission is not supported, a log is printed for notification. |
| OH\_JSVM\_CompileWasmFunction | Compiles the function with the specified ID in a Wasm module into the optimized machine code. Currently, only the highest optimization level is enabled. The validity of the function ID is ensured by the caller. If the JIT permission is not supported, a log is printed for notification. |
| OH\_JSVM\_IsWasmModuleObject | Checks whether the input value is a Wasm module. |
| OH\_JSVM\_CreateWasmCache | Serializes the machine code in a Wasm module into a Wasm cache. If the Wasm module does not contain machine code, the serialization will fail. If the JIT permission is not supported, a log is printed for notification. |
| OH\_JSVM\_ReleaseCache | Releases a Wasm cache instance created by JSVM-API. The **cacheType** and **cacheData** passed in must match. Otherwise, undefined behavior may occur. |

**Scenario Example**

For details, see [Working with Wasm Using JSVM-API](../jsvm-api-guides/working-with-wasm-using-jsvm-api/document.md).

## Exception Handling

**Scenarios**

Capture, throw, and clear JS exceptions as required.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_Throw | Throws a JS value. |
| OH\_JSVM\_ThrowTypeError | Throws a JS type error. |
| OH\_JSVM\_ThrowRangeError | Throws a JS range error. |
| OH\_JSVM\_IsError | Checks whether a JS value indicates an error. |
| OH\_JSVM\_CreateError | Creates a JS error. |
| OH\_JSVM\_CreateTypeError | Creates a JS type error and returns it. |
| OH\_JSVM\_CreateRangeError | Creates a JS range error and returns it. |
| OH\_JSVM\_ThrowError | Throws a JS exception. |
| OH\_JSVM\_GetAndClearLastException | Obtains and clears the last JS exception. |
| OH\_JSVM\_IsExceptionPending | Checks whether an exception occurs. |
| OH\_JSVM\_GetLastErrorInfo | Obtains information about the last exception. |
| OH\_JSVM\_ThrowSyntaxError | Throws a JS syntax error. |
| OH\_JSVM\_CreateSyntaxError | Creates a JS syntax error and returns it. |

Example:

The following walks you through on how to create, judge, and throw a JS type error.

JSVM\_Value code = nullptr;
JSVM\_Value message = nullptr;
OH\_JSVM\_CreateStringUtf8(env, "500", JSVM\_AUTO\_LENGTH, &code);
OH\_JSVM\_CreateStringUtf8(env, "type error 500", JSVM\_AUTO\_LENGTH, &message);
JSVM\_Value error = nullptr;
OH\_JSVM\_CreateTypeError(env, code, message, &error);
bool isError = false;
OH\_JSVM\_IsError(env, error, &isError);
OH\_JSVM\_ThrowTypeError(env, nullptr, "type error1");

Call **OH\_JSVM\_GetAndClearLastException** to log the exception information as a string to the console.

if (status != JSVM\_OK) // An exception occurs when the execution fails.
{
    bool isPending = false;
    if (JSVM\_OK == OH\_JSVM\_IsExceptionPending((env), &isPending) && isPending)
    {
        JSVM\_Value error;
        if (JSVM\_OK == OH\_JSVM\_GetAndClearLastException((env), &error))
        {
            // Obtain the exception stack.
            JSVM\_Value stack;
            OH\_JSVM\_GetNamedProperty((env), error, "stack", &stack);

            JSVM\_Value message;
            OH\_JSVM\_GetNamedProperty((env), error, "message", &message);

            char stackstr\[256\];
            OH\_JSVM\_GetValueStringUtf8(env, stack, stackstr, 256, nullptr);
            OH\_LOG\_INFO(LOG\_APP, "JSVM error stack: %{public}s", stackstr);

            char messagestr\[256\];
            OH\_JSVM\_GetValueStringUtf8(env, message, messagestr, 256, nullptr);
            OH\_LOG\_INFO(LOG\_APP, "JSVM error message: %{public}s", messagestr);
        }
    }
}

## Object Lifetime Management

When JSVM-API calls are made, handles to objects in the heap for the underlying VM may be returned as **JSVM\_Value**s. These handles must hold the objects live until they are no longer required by the native code. Otherwise, the objects will be collected.

When an object handle is returned, it is associated with a scope. The lifecycle of the default scope is tied to the lifecycle of the native method call. By default, a handle remains valid and the object associated with it will be held live for the lifecycle of the native method call.

However, in many cases, you may need to adjust the lifecycle to be shorter or longer than that of the native method. The following describes the JSVM-API methods that can be used to change the lifecycle of a handle.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_OpenHandleScope | Opens a handle scope. The object within the scope will not be garbage-collected until the handle scope is closed. |
| OH\_JSVM\_CloseHandleScope | Closes a handle scope. The object within the scope will be garbage-collected after the handle scope is closed. |
| OH\_JSVM\_OpenEscapableHandleScope | Opens an escapable handle scope. Before this scope is closed, the object created within the scope has the same lifecycle as its parent scope. |
| OH\_JSVM\_CloseEscapableHandleScope | Closes an escapable handle scope. |
| OH\_JSVM\_EscapeHandle | Promotes a handle to a JS object so that it is valid for the lifetime of the outer scope. |
| OH\_JSVM\_CreateReference | Creates a new reference with the specified reference count to the value passed in. The reference allows objects to be used and shared in different contexts and effectively monitors the lifecycle of the object. |
| OH\_JSVM\_DeleteReference | Releases the reference created by **OH\_JSVM\_CreateReference**. This allows objects to be correctly released and reclaimed when they are no longer required, avoiding memory leaks. |
| OH\_JSVM\_ReferenceRef | Increments the reference count of the reference created by **OH\_JSVM\_CreateReference** so that the object referenced will not be released. |
| OH\_JSVM\_ReferenceUnref | Decrements the reference count of the reference created by **OH\_JSVM\_CreateReference** so that the object can be correctly released and reclaimed when it is not referenced. |
| OH\_JSVM\_GetReferenceValue | Obtains the object referenced by **OH\_JSVM\_CreateReference**. |
| OH\_JSVM\_RetainScript | Retains a **JSVM\_Script** persistently so that it can be used out of the current scope. |
| OH\_JSVM\_ReleaseScript | Releases a **JSVM\_Script** that is persistently retained. The released **JSVM\_Script** will no longer be used and must be left empty. |

Example:

Use a handle scope to protect an object created within the scope from being reclaimed.

JSVM\_HandleScope scope;
OH\_JSVM\_OpenHandleScope(env, &scope);
JSVM\_Value obj = nullptr;
OH\_JSVM\_CreateObject(env, &obj);
OH\_JSVM\_CloseHandleScope(env, scope);

Use an escapable handle scope to protect an object from being reclaimed within its parent scope.

JSVM\_EscapableHandleScope scope;
JSVM\_CALL(OH\_JSVM\_OpenEscapableHandleScope(env, &scope));
JSVM\_Value output = NULL;
JSVM\_Value escapee = NULL;
JSVM\_CALL(OH\_JSVM\_CreateObject(env, &output));
JSVM\_CALL(OH\_JSVM\_EscapeHandle(env, scope, output, &escapee));
JSVM\_CALL(OH\_JSVM\_CloseEscapableHandleScope(env, scope));
return escapee;

Reference a JS object and release the reference.

JSVM\_Value obj = nullptr;
OH\_JSVM\_CreateObject(env, &obj);
// Create a reference.
JSVM\_Ref reference;
OH\_JSVM\_CreateReference(env, obj, 1, &reference);

// Create a reference with a JS object.
JSVM\_Value result;
OH\_JSVM\_GetReferenceValue(env, reference, &result);

// Release the reference.
OH\_JSVM\_DeleteReference(env, reference);

Use **RetainScript()** to persistently hold **JSVM\_Script** and use it.

JSVM\_HandleScope scope;
JSVM\_CALL(OH\_JSVM\_OpenHandleScope(env, &scope));
JSVM\_Script script;
JSVM\_Value jsSrc;
std::string src(R"JS(
let a = 37;
a = a \* 9;
)JS");
JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, src.c\_str(), src.size(), &jsSrc));
JSVM\_CALL(OH\_JSVM\_CompileScriptWithOptions(env, jsSrc, 0, nullptr, &script));
JSVM\_CALL(OH\_JSVM\_RetainScript(env, script));
JSVM\_CALL(OH\_JSVM\_CloseHandleScope(env, scope));

// Run a JSVM script.
JSVM\_CALL(OH\_JSVM\_OpenHandleScope(env, &scope));
JSVM\_Value result;
JSVM\_CALL(OH\_JSVM\_RunScript(env, script, &result));

// Release a JSVM script and set it to null.
JSVM\_CALL(OH\_JSVM\_ReleaseScript(env, script));
script = nullptr;
JSVM\_CALL(OH\_JSVM\_CloseHandleScope(env, scope));

## Creating JS Object Types and Basic Types

**Scenarios**

Create JS object types and basic types.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateArray | Creates a JS array object. |
| OH\_JSVM\_CreateArrayWithLength | Creates a JS array object of the specified length. |
| OH\_JSVM\_CreateArraybuffer | Creates an **ArrayBuffer** object of the specified size. |
| OH\_JSVM\_CreateDate | Creates a date object representing the given number of milliseconds. |
| OH\_JSVM\_CreateExternal | Creates a JS object that wraps an external pointer. |
| OH\_JSVM\_CreateObject | Creates a default JS object. |
| OH\_JSVM\_CreateSymbol | Creates a symbol object based on the given descriptor. |
| OH\_JSVM\_SymbolFor | Searches for a symbol with the given key in a global (runtime-wide) symbol registry. If a match is found, the symbol will be returned. Otherwise, a symbol will be created in the registry. |
| OH\_JSVM\_CreateTypedarray | Creates a JS **TypedArray** object for an **ArrayBuffer**. The **TypedArray** object provides an array-like view over an underlying data buffer, where each element has the same underlying binary scalar data type. |
| OH\_JSVM\_CreateDataview | Creates a JS **DataView** object for an **ArrayBuffer**. The **DataView** object provides an array-like view over an underlying data buffer. |
| OH\_JSVM\_CreateInt32 | Creates a JS number object from a C Int32\_t object. |
| OH\_JSVM\_CreateUint32 | Creates a JS number object from a C Uint32\_t object. |
| OH\_JSVM\_CreateInt64 | Creates a JS number object from a C Int64\_t object. |
| OH\_JSVM\_CreateDouble | Creates a JS number object from a C Double object. |
| OH\_JSVM\_CreateBigintInt64 | Creates a JS BigInt object from a C Int64 object. |
| OH\_JSVM\_CreateBigintUint64 | Creates a JS BigInt object from a C Uint64 object. |
| OH\_JSVM\_CreateBigintWords | Creates a JS BigInt object from a C Uint64\_t array. |
| OH\_JSVM\_CreateStringLatin1 | Creates a JS string object from an ISO-8859-1-encoded C string. ISO-8859-1 is also referred to as Latin-1. |
| OH\_JSVM\_CreateStringUtf16 | Creates a JS string object from a UTF16-encoded C string. |
| OH\_JSVM\_CreateStringUtf8 | Creates a JS string object from a UTF8-encoded C string. |
| OH\_JSVM\_CreateMap | Creates a JS **Map** object. |
| OH\_JSVM\_CreateRegExp | Creates a JS regular expression object based on the given string. |
| OH\_JSVM\_CreateSet | Creates a JS **Set** object. |

Example:

Create a JS array of the specified length.

size\_t arrayLength = 2;
JSVM\_Value arr;

OH\_JSVM\_CreateArrayWithLength(env, arrayLength, &arr);
for (uint32\_t i = 0; i < arrayLength; i++)
{
    JSVM\_Value element;
    OH\_JSVM\_CreateUint32(env, i \* 2, &element);
    OH\_JSVM\_SetElement(env, arr, i, element);
}

Create a JS Int32Array.

JSVM\_Value arrayBuffer = nullptr;
void \*arrayBufferPtr = nullptr;
size\_t arrayBufferSize = 16;
size\_t typedArrayLength = 4;
OH\_JSVM\_CreateArraybuffer(env, arrayBufferSize, &arrayBufferPtr, &arrayBuffer);

void \*tmpArrayBufferPtr = nullptr;
size\_t arrayBufferLength = 0;
OH\_JSVM\_GetArraybufferInfo(env, arrayBuffer, &tmpArrayBufferPtr, &arrayBufferLength);

JSVM\_Value result;
OH\_JSVM\_CreateTypedarray(env, JSVM\_TypedarrayType::JSVM\_INT32\_ARRAY, typedArrayLength, arrayBuffer, 0, &result);
return result;

Create JS numbers and strings.

const char \*testStringStr = "test";
JSVM\_Value testString = nullptr;
OH\_JSVM\_CreateStringUtf8(env, testStringStr, strlen(testStringStr), &testString);

JSVM\_Value testNumber1 = nullptr;
JSVM\_Value testNumber2 = nullptr;
OH\_JSVM\_CreateDouble(env, 10.1, &testNumber1);
OH\_JSVM\_CreateInt32(env, 10, &testNumber2);

Create a map.

JSVM\_Value value = nullptr;
OH\_JSVM\_CreateMap(env, &value);

Create a regular expression.

JSVM\_Value value = nullptr;
const char testStr\[\] = "ab+c";
OH\_JSVM\_CreateStringUtf8(env, testStr, strlen(testStr), &value);
JSVM\_Value result = nullptr;
OH\_JSVM\_CreateRegExp(env, value, JSVM\_RegExpFlags::JSVM\_REGEXP\_GLOBAL, &result);

Create a **set()** instance.

JSVM\_Value value = nullptr;
OH\_JSVM\_CreateSet(env, &value);

## Obtaining C Type and JS Type Information from JS Types

**Scenarios**

Obtain C type and JS type information from JS types.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetArrayLength | Obtains the length of an array. |
| OH\_JSVM\_GetArraybufferInfo | Obtains the underlying data buffer of an **ArrayBuffer** and its length. |
| OH\_JSVM\_GetPrototype | Obtains the prototype of a JS object. |
| OH\_JSVM\_GetTypedarrayInfo | Obtains information about a **TypedArray** object. |
| OH\_JSVM\_GetDataviewInfo | Obtains information about a **DataView** object. |
| OH\_JSVM\_GetDateValue | Obtains the C double primitive of the time value for the given JS **Date** object. |
| OH\_JSVM\_GetValueBool | Obtains the C Boolean primitive equivalent of the given JS Boolean. |
| OH\_JSVM\_GetValueDouble | Obtains the C Double primitive equivalent of the given JS number. |
| OH\_JSVM\_GetValueBigintInt64 | Obtains the C Int64\_t primitive equivalent of the given JS BigInt. |
| OH\_JSVM\_GetValueBigintUint64 | Obtains the C Uint64\_t primitive equivalent of the given JS BigInt. |
| OH\_JSVM\_GetValueBigintWords | Obtains the underlying data of a given JS BigInt object, that is, the word representation of BigInt data. |
| OH\_JSVM\_GetValueExternal | Obtains the external data pointer previously passed to **OH\_JSVM\_CreateExternal**. |
| OH\_JSVM\_GetValueInt32 | Obtains the C Int32 primitive equivalent of the given JS number. |
| OH\_JSVM\_GetValueInt64 | Obtains the C Int64 primitive equivalent of the given JS number. |
| OH\_JSVM\_GetValueStringLatin1 | Obtains the ISO-8859-1-encoded string from the given JS string. |
| OH\_JSVM\_GetValueStringUtf8 | Obtains the UTF8-encoded string from the given JS string. |
| OH\_JSVM\_GetValueStringUtf16 | Obtains the UTF16-encoded string from the given JS string. |
| OH\_JSVM\_GetValueUint32 | Obtains the C primitive equivalent (a Uint32) of the given JS number. |
| OH\_JSVM\_GetBoolean | Obtains a JS singleton object that is used to represent the given Boolean value. |
| OH\_JSVM\_GetGlobal | Obtains the **global** object of the current environment. |
| OH\_JSVM\_GetNull | Obtains the JS **null** object. |
| OH\_JSVM\_GetUndefined | Obtains the JS **Undefined** object. |

Example:

Create a JS BigInt object from a C Int64 object and obtain the C Int64\_t primitive equivalent.

int64\_t testValue = INT64\_MAX;
JSVM\_Value result = nullptr;
OH\_JSVM\_CreateBigintInt64(env, testValue, &result);
int64\_t resultValue = 0;
bool flag = false;
OH\_JSVM\_GetValueBigintInt64(env, result, &resultValue, &flag);

Create an Int32Array and obtain its information such as the length and byte offset.

JSVM\_Value arrayBuffer = nullptr;
void \*arrayBufferPtr = nullptr;
size\_t arrayBufferSize = 16;
size\_t typedArrayLength = 4;
OH\_JSVM\_CreateArraybuffer(env, arrayBufferSize, &arrayBufferPtr, &arrayBuffer);

bool isArrayBuffer = false;
OH\_JSVM\_IsArraybuffer(env, arrayBuffer, &isArrayBuffer);

JSVM\_Value result;
OH\_JSVM\_CreateTypedarray(env, JSVM\_TypedarrayType::JSVM\_INT32\_ARRAY, typedArrayLength, arrayBuffer, 0, &result);

bool isTypedArray = false;
OH\_JSVM\_IsTypedarray(env, result, &isTypedArray);

JSVM\_TypedarrayType type;
size\_t length = 0;
void \*data = nullptr;
JSVM\_Value retArrayBuffer;
size\_t byteOffset = -1;
OH\_JSVM\_GetTypedarrayInfo(env, result, &type, &length, &data, &retArrayBuffer, &byteOffset);

bool retIsArrayBuffer = false;
OH\_JSVM\_IsArraybuffer(env, retArrayBuffer, &retIsArrayBuffer);
void \*tmpArrayBufferPtr = nullptr;
size\_t arrayBufferLength = 0;
OH\_JSVM\_GetArraybufferInfo(env, retArrayBuffer, &tmpArrayBufferPtr, &arrayBufferLength);

Create a JavaScript string from a UTF-8-encoded C string, and obtain the UTF-8-encoded C string for the specified JavaScript string.

const char \*testStringStr = "testString";
JSVM\_Value testString = nullptr;
JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, testStringStr, strlen(testStringStr), &testString));

char buffer\[128\];
size\_t bufferSize = 128;
size\_t copied = 0;

JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, testString, buffer, bufferSize, &copied));

## Working with JS Values and Abstract Operations

**Scenarios**

Perform abstract operations on JS values.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CoerceToBool | Converts a JS value to an object of the Boolean type. |
| OH\_JSVM\_CoerceToNumber | Converts a JS value to an object of the number type. |
| OH\_JSVM\_CoerceToObject | Converts a JS value to an object of the object type. |
| OH\_JSVM\_CoerceToString | Converts a JS value to an object of the string type. |
| OH\_JSVM\_CoerceToBigInt | Converts a JS value to an object of the BigInt type. |
| OH\_JSVM\_Typeof | Returns the type of a JS object. |
| OH\_JSVM\_Instanceof | Checks whether an object is an instance of a constructor. |
| OH\_JSVM\_IsArray | Checks whether a JS object is an array. |
| OH\_JSVM\_IsArraybuffer | Checks whether a JS object is an **ArrayBuffer** object. |
| OH\_JSVM\_IsDate | Checks whether a JS object is a **Date** object. |
| OH\_JSVM\_IsTypedarray | Checks whether a JS object is a **TypedArray** object. |
| OH\_JSVM\_IsDataview | Checks whether a JS object is a **DataView** object. |
| OH\_JSVM\_IsUndefined | Checks whether the value passed in is **Undefined**. This API is equivalent to executing JS code **value === undefined**. |
| OH\_JSVM\_IsNull | Checks whether the value passed in is a **Null** object. This API is equivalent to executing JS code **value === null**. |
| OH\_JSVM\_IsNullOrUndefined | Checks whether the value passed in is **Null** or **Undefined**. This API is equivalent to executing JS code **value == null**. |
| OH\_JSVM\_IsBoolean | Checks whether the value passed in is a Boolean value. This API is equivalent to executing JS code **typeof value ==='boolean'**. |
| OH\_JSVM\_IsNumber | Checks whether the value passed in is a number. This API is equivalent to executing JS code **typeof value === 'number'**. |
| OH\_JSVM\_IsString | Checks whether the value passed in is a string. This API is equivalent to executing JS code **typeof value === 'string'**. |
| OH\_JSVM\_IsSymbol | Checks whether the value passed in is a symbol. This API is equivalent to executing JS code **typeof value === 'symbol'**. |
| OH\_JSVM\_IsFunction | Checks whether the value passed in is a function. This API is equivalent to executing JS code **typeof value === 'function'**. |
| OH\_JSVM\_IsObject | Checks whether the value passed in is an object . |
| OH\_JSVM\_IsBigInt | Checks whether the value passed in is a BigInt. This API is equivalent to executing JS code **typeof value === 'bigint'**. |
| OH\_JSVM\_IsConstructor | Checks whether the value passed in is a constructor. |
| OH\_JSVM\_IsMap | Checks whether the value passed in is a map. |
| OH\_JSVM\_IsSet | Checks whether the value passed in is a **set()** instance. |
| OH\_JSVM\_IsRegExp | Checks whether the value passed in is a regular expression. |
| OH\_JSVM\_StrictEquals | Checks whether two **JSVM\_Value** objects are strictly equal. |
| OH\_JSVM\_Equals | Checks whether two **JSVM\_Value** objects are roughly equal. |
| OH\_JSVM\_DetachArraybuffer | Calls the **Detach()** operation of an **ArrayBuffer** object. |
| OH\_JSVM\_IsDetachedArraybuffer | Checks whether an **ArrayBuffer** object has been detached. |

Example:

Check whether the JS value is an array.

JSVM\_Value array = nullptr;
OH\_JSVM\_CreateArray(env, &array);
bool isArray = false;
OH\_JSVM\_IsArray(env, array, &isArray);

Convert a JS int32 value to a string.

int32\_t num = 123;
JSVM\_Value intValue;
OH\_JSVM\_CreateInt32(env, num, &intValue);
JSVM\_Value stringValue;
OH\_JSVM\_CoerceToString(env, intValue, &stringValue);

char buffer\[128\];
size\_t bufferSize = 128;
size\_t copied = 0;

OH\_JSVM\_GetValueStringUtf8(env, stringValue, buffer, bufferSize, &copied);
// buffer:"123";

Convert a JS boolean value to a bigint.

JSVM\_Value boolValue;
OH\_JSVM\_GetBoolean(env, false, &boolValue);
JSVM\_Value bigIntValue;
OH\_JSVM\_CoerceToBigInt(env, boolValue, &bigIntValue);

Check whether two **JSVM\_Value** objects are strictly equal as follows: Compare the operand types first. If the operand types are different, the values are different. If the operand types are the same, compare the two values. If the values are the same, **true** is returned.

JSVM\_Value value = nullptr;
JSVM\_Value value1 = nullptr;
OH\_JSVM\_CreateArray(env, &value);

OH\_JSVM\_CreateInt32(env, 10, &value1);
bool isArray = true;
OH\_JSVM\_StrictEquals(env, value, value, &isArray);

Check whether two **JSVM\_Value** objects are roughly equal as follows: Compare the operand types first. If the operand types are different but can be converted to the same type, convert the operand types to the same type and check whether the values are strictly equal. If the values are the same, **true** is returned. **false** is returned in other cases.

JSVM\_HandleScope handleScope;
OH\_JSVM\_OpenHandleScope(env, &handleScope);
const char testStr\[\] = "1";
JSVM\_Value lhs = nullptr;
OH\_JSVM\_CreateStringUtf8(env, testStr, strlen(testStr), &lhs);
JSVM\_Value rhs;
OH\_JSVM\_CreateInt32(env, 1, &rhs);
bool isEquals = false;
OH\_JSVM\_Equals(env, lhs, rhs, &isEquals); // The value of isEquals is true.
OH\_JSVM\_CloseHandleScope(env, handleScope);

Check whether the input JS value is a constructor.

JSVM\_Value SayHello(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    return nullptr;
}
JSVM\_Value value = nullptr;
JSVM\_CallbackStruct param;
param.data = nullptr;
param.callback = SayHello;
OH\_JSVM\_CreateFunction(env, "func", JSVM\_AUTO\_LENGTH, &param, &value);
bool isConstructor = false;
OH\_JSVM\_IsConstructor(env, value, &isConstructor); // The value of isConstructor is true.

Check whether the JS value is of the map type.

JSVM\_Value value = nullptr;
OH\_JSVM\_CreateMap(env, &value);
bool isMap = false;
OH\_JSVM\_IsMap(env, value, &isMap); // The value of isMap is true.

Check whether the JS value is of the set type.

JSVM\_Value value;
OH\_JSVM\_CreateSet(env, &value);
bool isSet = false;
OH\_JSVM\_IsSet(env, value, &isSet); // The value of isSet is true.

Check whether the JS value is a regular expression.

JSVM\_Value value = nullptr;
const char testStr\[\] = "ab+c";
OH\_JSVM\_CreateStringUtf8(env, testStr, strlen(testStr), &value);
JSVM\_Value result = nullptr;
OH\_JSVM\_CreateRegExp(env, value, JSVM\_RegExpFlags::JSVM\_REGEXP\_GLOBAL, &result);
bool isRegExp = false;
OH\_JSVM\_IsRegExp(env, result, &isRegExp);

## Working with JS Properties

**Scenarios**

Set, get, delete, and check properties of a JS object.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetPropertyNames | Obtains the names of all enumerable properties of a JS object as a JS array. |
| OH\_JSVM\_GetAllPropertyNames | Obtains the names of all available properties of a JS object as a JS array. |
| OH\_JSVM\_SetProperty | Sets a property for a JS object. |
| OH\_JSVM\_GetProperty | Obtains the requested property from a JS object. |
| OH\_JSVM\_HasProperty | Checks whether a JS object has the specified property. |
| OH\_JSVM\_DeleteProperty | Deletes a property from a JS object. |
| OH\_JSVM\_HasOwnProperty | Checks whether a JS object has the specified own property. |
| OH\_JSVM\_SetNamedProperty | Sets a property with the given property name for a JS object. This API is equivalent to calling **OH\_JSVM\_SetProperty** with a **JSVM\_Value** created from the string passed in as **utf8Name**. |
| OH\_JSVM\_GetNamedProperty | Obtains the property from a JS object with the given property name. This API is equivalent to calling **OH\_JSVM\_GetProperty** with a **JSVM\_Value** created from the string passed in as **utf8Name**. |
| OH\_JSVM\_HasNamedProperty | Checks whether a JS object has the specified property. This API is equivalent to calling **OH\_JSVM\_HasProperty** using a **JSVM\_Value** created from the string passed in as **utf8Name**. |
| OH\_JSVM\_SetElement | Sets an element at the specified index for a JS object. |
| OH\_JSVM\_GetElement | Obtains the element at the specified index of a JS object. |
| OH\_JSVM\_HasElement | Checks whether a JS object has an element at the specified index. |
| OH\_JSVM\_DeleteElement | Deletes the element at the specified index from a JS object. |
| OH\_JSVM\_DefineProperties | Defines multiple properties for a JS object. |
| OH\_JSVM\_ObjectFreeze | Freezes a JS object. Once a JS object is frozen, new properties cannot be added to it, existing properties cannot be removed, the enumerability, configurability, or writability of existing properties cannot be changed, and the values of existing properties cannot be changed. |
| OH\_JSVM\_ObjectSeal | Seals a JS object. Once a JS object is sealed, new properties cannot be added to it and all existing properties are marked as unconfigurable. |
| OH\_JSVM\_ObjectSetPrototypeOf | Sets a prototype for a given object. |
| OH\_JSVM\_ObjectGetPrototypeOf | Obtains the prototype of a JS object. |

Example:

Set, get, delete, and check properties of a JS object.

// Create an empty object.
JSVM\_Value myObject = nullptr;
OH\_JSVM\_CreateObject(env, &myObject);

// Set properties.
const char \*testNameStr = "John Doe";
JSVM\_Value propValue = nullptr;
JSVM\_Value key = nullptr;
OH\_JSVM\_CreateStringUtf8(env, "name", JSVM\_AUTO\_LENGTH, &key);
OH\_JSVM\_CreateStringUtf8(env, testNameStr, strlen(testNameStr), &propValue);
OH\_JSVM\_SetProperty(env, myObject, key, propValue);

// Obtain properties.
JSVM\_Value propResult = nullptr;
OH\_JSVM\_GetProperty(env, myObject, key, &propResult);

// Check whether a property exists.
bool hasProperty = false;
OH\_JSVM\_HasNamedProperty(env, myObject, "name", &hasProperty);
    // The property exists. Perform subsequent processing accordingly.
    if (hasProperty)
    {
        // Obtain all property names of the object.
        JSVM\_Value propNames = nullptr;
        OH\_JSVM\_GetPropertyNames(env, myObject, &propNames);

        bool isArray = false;
        OH\_JSVM\_IsArray(env, propNames, &isArray);

        uint32\_t arrayLength = 0;
        OH\_JSVM\_GetArrayLength(env, propNames, &arrayLength);
        // Traverse property elements.
        for (uint32\_t i = 0; i < arrayLength; i++)
        {
            bool hasElement = false;
            OH\_JSVM\_HasElement(env, propNames, i, &hasElement);

            JSVM\_Value propName = nullptr;
            OH\_JSVM\_GetElement(env, propNames, i, &propName);

            bool hasProp = false;
            OH\_JSVM\_HasProperty(env, myObject, propName, &hasProp);

            JSVM\_Value propValue = nullptr;
            OH\_JSVM\_GetProperty(env, myObject, propName, &propValue);
        }
    }

// Delete a property.
OH\_JSVM\_DeleteProperty(env, myObject, key, &hasProperty);

// Set the object prototype.
JSVM\_Value value;
OH\_JSVM\_CreateSet(env, &value);
OH\_JSVM\_ObjectSetPrototypeOf(env, myObject, value);

// Obtain the object prototype.
JSVM\_Value proto;
OH\_JSVM\_ObjectGetPrototypeOf(env, myObject, &proto);

## Working with JS Functions

**Scenarios**

Call back JS code into native code and call JS functions from native code.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CallFunction | Calls a JS function from a C/C++ addon. |
| OH\_JSVM\_CreateFunction | Creates a JS function object in native code, which allows calling into the native code from JS. |
| OH\_JSVM\_GetCbInfo | Obtains detailed information about the call, such as the parameters and **this** pointer, from the given callback information. |
| OH\_JSVM\_GetNewTarget | Obtains the **new.target** of the constructor call. |
| OH\_JSVM\_NewInstance | Creates an instance based on the given constructor. |
| OH\_JSVM\_CreateFunctionWithScript | Creates a JS function object based on the given function body and parameter list. |

Example:

Create a JS function.

JSVM\_Value SayHello(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    printf("Hello\\n");
    JSVM\_Value ret;
    OH\_JSVM\_CreateInt32(env, 2, &ret);
    return ret;
}

static JSVM\_Value JsvmCreateFunction(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_CallbackStruct param;
    param.data = nullptr;
    param.callback = SayHello;

    JSVM\_Value funcValue = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateFunction(env, "func", JSVM\_AUTO\_LENGTH, &param, &funcValue);
    return funcValue;
}

Call a JS function from a C/C++ addon.

static JSVM\_Value CallFunction(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\];
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL));
    if (argc < 1) {
        OH\_LOG\_ERROR(LOG\_APP, "Wrong number of arguments");
        return nullptr;
    }

    JSVM\_ValueType valuetype;
    JSVM\_CALL(OH\_JSVM\_Typeof(env, args\[0\], &valuetype));
    if (valuetype != JSVM\_ValueType::JSVM\_FUNCTION) {
        OH\_LOG\_ERROR(LOG\_APP, "Wrong type of argument. Expects a function.");
        return nullptr;
    }

    JSVM\_Value global;
    JSVM\_CALL(OH\_JSVM\_GetGlobal(env, &global));

    JSVM\_Value ret;
    JSVM\_CALL(OH\_JSVM\_CallFunction(env, global, args\[0\], 0, nullptr, &ret));
    return ret;
}

Create a JS function.

JSVM\_Value script;
OH\_JSVM\_CreateStringUtf8(env, "return a + b;", JSVM\_AUTO\_LENGTH, &script);
JSVM\_Value param1;
JSVM\_Value param2;
OH\_JSVM\_CreateStringUtf8(env, "a", JSVM\_AUTO\_LENGTH, &param1);
OH\_JSVM\_CreateStringUtf8(env, "b", JSVM\_AUTO\_LENGTH, &param2);
JSVM\_Value argus\[\] = {param1, param2};
JSVM\_Value func;
OH\_JSVM\_CreateFunctionWithScript(env, "add", JSVM\_AUTO\_LENGTH, 2, argus, script, &func);

## Wrapping Objects

**Scenarios**

Wrap native classes and instances so that the class constructor and methods can be called from JS.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_DefineClass | Defines a JS class and associated functions within a C/C++ addon. It allows you to define a constructor, methods, and properties that can be accessed from JS. |
| OH\_JSVM\_Wrap | Wraps a native instance in a JS object. You can use **OH\_JSVM\_Unwrap()** to retrieve the native instance later. |
| OH\_JSVM\_Unwrap | Retrieves a native instance from a JS object. |
| OH\_JSVM\_RemoveWrap | Retrieves a native instance previously wrapped in a JS object and removes the wrapping. |
| OH\_JSVM\_TypeTagObject | Associates the value of the **type\_tag** pointer with a JS object or an external object. |
| OH\_JSVM\_CheckObjectTypeTag | Checks whether a tag matches the tag type of an object. |
| OH\_JSVM\_AddFinalizer | Adds a **JSVM\_Finalize** callback to a JS object. The callback will be invoked to release the native object when the JS object is garbage-collected. |
| OH\_JSVM\_DefineClassWithPropertyHandler | Defines a JS class with the given class name, constructor, property, and callback handler, and calls it as a function callback. The property operations include getter, setter, deleter, and enumerator. |
| OH\_JSVM\_DefineClassWithOptions | Defines a JS class with the given class name, constructor, properties, callback handler, and parent class. The **DefineClassOptions** parameter specifies whether to set a property proxy for the defined class, reserve the internal-field slot, and set a callback when the class is called as a function. |

Example:

Wrap a native object in a JS object.

static int aa = 0;

static JSVM\_Value AssertEqual(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 2;
    JSVM\_Value args\[2\];
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL));

    bool isStrictEquals = false;
    OH\_JSVM\_StrictEquals(env, args\[0\], args\[1\], &isStrictEquals);
    return nullptr;
}

static napi\_value TestWrap(napi\_env env1, napi\_callback\_info info)
{
    OH\_LOG\_ERROR(LOG\_APP, "testWrap start");
    JSVM\_InitOptions init\_options;
    memset(&init\_options, 0, sizeof(init\_options));
    if (aa == 0) {
        OH\_JSVM\_Init(&init\_options);
        aa++;
    }
    JSVM\_VM vm;
    JSVM\_CreateVMOptions options;
    memset(&options, 0, sizeof(options));
    OH\_JSVM\_CreateVM(&options, &vm);
    JSVM\_VMScope vm\_scope;
    OH\_JSVM\_OpenVMScope(vm, &vm\_scope);
    JSVM\_Env env;
    JSVM\_CallbackStruct param\[1\];
    param\[0\].data = nullptr;
    param\[0\].callback = AssertEqual;
    JSVM\_PropertyDescriptor descriptor\[\] = {
        {"assertEqual", NULL, &param\[0\], NULL, NULL, NULL, JSVM\_DEFAULT},
    };
    OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    JSVM\_HandleScope handlescope;
    OH\_JSVM\_OpenHandleScope(env, &handlescope);
    JSVM\_Value testClass = nullptr;
    JSVM\_CallbackStruct param1;
    param1.data = nullptr;
    param1.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        JSVM\_Value thisVar = nullptr;
        OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);

        return thisVar;
    };
    OH\_JSVM\_DefineClass(env, "TestClass", JSVM\_AUTO\_LENGTH, &param1, 0, nullptr, &testClass);

    JSVM\_Value instanceValue = nullptr;
    OH\_JSVM\_NewInstance(env, testClass, 0, nullptr, &instanceValue);

    const char \*testStr = "test";
    OH\_JSVM\_Wrap(
        env, instanceValue, (void \*)testStr, \[\](JSVM\_Env env, void \*data, void \*hint) {}, nullptr, nullptr);
    const char \*tmpTestStr = nullptr;
    OH\_JSVM\_Unwrap(env, instanceValue, (void \*\*)&tmpTestStr);
    const char \*tmpTestStr1 = nullptr;
    OH\_JSVM\_RemoveWrap(env, instanceValue, (void \*\*)&tmpTestStr1);
    OH\_JSVM\_Unwrap(env, instanceValue, (void \*\*)&tmpTestStr1);
    OH\_JSVM\_CloseHandleScope(env, handlescope);
    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vm\_scope);
    OH\_JSVM\_DestroyVM(vm);
    OH\_LOG\_ERROR(LOG\_APP, "testWrap pass");
    return nullptr;
}

Example:

Wrap a native object and register a listener for property access operations.

static int aa = 0;
static JSVM\_Value hello(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_Value output;
    void \*data = nullptr;
    OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, nullptr, &data);
    OH\_JSVM\_CreateStringUtf8(env, (char \*)data, strlen((char \*)data), &output);
    return output;
}

static JSVM\_CallbackStruct hello\_cb = {hello, (void \*)"Hello"};
static intptr\_t externals\[\] = {
    (intptr\_t)&hello\_cb,
    0,
};

static void test1() { OH\_LOG\_INFO(LOG\_APP, "test1 called"); }

struct Test {
    void \*ptr1;
    void \*ptr2;
};

static JSVM\_Value assertEqual(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 2;
    JSVM\_Value args\[2\];
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL));

    bool isStrictEquals = false;
    OH\_JSVM\_StrictEquals(env, args\[0\], args\[1\], &isStrictEquals);
    return nullptr;
}

static JSVM\_Value GetPropertyCbInfo(JSVM\_Env env, JSVM\_Value name, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the getter of the object.
    char strValue\[100\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, name, strValue, 300, &size);
    JSVM\_Value newResult = nullptr;
    char newStr\[\] = "new return value hahaha from name listening";
    OH\_JSVM\_CreateStringUtf8(env, newStr, strlen(newStr), &newResult);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "GetPropertyCbInfo wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value SetPropertyCbInfo(JSVM\_Env env, JSVM\_Value name, JSVM\_Value property, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the setter of the object.
    char strValue\[100\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, name, strValue, 300, &size);
    JSVM\_Value newResult = nullptr;
    char newStr\[\] = "new return value hahaha from name listening";
    OH\_JSVM\_CreateStringUtf8(env, newStr, strlen(newStr), &newResult);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "SetPropertyCbInfo wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value DeleterPropertyCbInfo(JSVM\_Env env, JSVM\_Value name, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the deleter of the object.
    char strValue\[100\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, name, strValue, 300, &size);
    JSVM\_Value newResult = nullptr;
    bool returnValue = false;
    OH\_JSVM\_GetBoolean(env, returnValue, &newResult);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "DeleterPropertyCbInfo wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value EnumeratorPropertyCbInfo(JSVM\_Env env, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the enumerator of an object.
    JSVM\_Value testArray = nullptr;
    OH\_JSVM\_CreateArrayWithLength(env, 2, &testArray);
    JSVM\_Value name1 = nullptr;
    char newStr1\[\] = "hahaha";
    OH\_JSVM\_CreateStringUtf8(env, newStr1, strlen(newStr1), &name1);
    JSVM\_Value name2 = nullptr;
    char newStr2\[\] = "heheheh";
    OH\_JSVM\_CreateStringUtf8(env, newStr2, strlen(newStr2), &name2);

    OH\_JSVM\_SetElement(env, testArray, 0, name1);
    OH\_JSVM\_SetElement(env, testArray, 1, name2);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "EnumeratorPropertyCbInfo wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value IndexedPropertyGet(JSVM\_Env env, JSVM\_Value index, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the indexed getter.
    uint32\_t value = 0;
    OH\_JSVM\_GetValueUint32(env, index, &value);

    JSVM\_Value newResult = nullptr;
    char newStr\[\] = "new return value hahaha from index listening";
    OH\_JSVM\_CreateStringUtf8(env, newStr, strlen(newStr), &newResult);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "IndexedPropertyGet wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value IndexedPropertySet(JSVM\_Env env, JSVM\_Value index, JSVM\_Value property, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the indexed setter.
    uint32\_t value = 0;
    OH\_JSVM\_GetValueUint32(env, index, &value);
    char str\[100\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, property, str, 100, &size);
    JSVM\_Value newResult = nullptr;
    char newStr\[\] = "new return value hahaha from name listening";
    OH\_JSVM\_CreateStringUtf8(env, newStr, strlen(newStr), &newResult);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "IndexedPropertySet wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value IndexedPropertyDeleter(JSVM\_Env env, JSVM\_Value index, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the indexed deleter.
    uint32\_t value = 0;
    OH\_JSVM\_GetValueUint32(env, index, &value);
    JSVM\_Value newResult = nullptr;
    bool returnValue = false;
    OH\_JSVM\_GetBoolean(env, returnValue, &newResult);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "IndexedPropertyDeleter wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static JSVM\_Value IndexedPropertyEnumerator(JSVM\_Env env, JSVM\_Value thisArg, JSVM\_Value data) {
    // This callback is triggered by the indexed enumerator.
    JSVM\_Value testArray = nullptr;
    OH\_JSVM\_CreateArrayWithLength(env, 2, &testArray);
    JSVM\_Value index1 = nullptr;
    OH\_JSVM\_CreateUint32(env, 1, &index1);
    JSVM\_Value index2 = nullptr;
    OH\_JSVM\_CreateUint32(env, 2, &index2);
    OH\_JSVM\_SetElement(env, testArray, 0, index1);
    OH\_JSVM\_SetElement(env, testArray, 1, index2);
    int signBit = 0;
    size\_t wordCount = 2;
    uint64\_t wordsOut\[2\] = {0ULL, 0ULL};
    JSVM\_Status status = OH\_JSVM\_GetValueBigintWords(env, data, &signBit, &wordCount, wordsOut);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "IndexedPropertyDeleter wordCount is %{public}zu", wordCount);
        auto test = reinterpret\_cast<Test \*>(wordsOut);
        typedef void (\*callTest1)();
        callTest1 callTe = reinterpret\_cast<callTest1>(test->ptr1);
        callTe();
    }
    return nullptr;
}

static napi\_value TestDefineClassWithProperty(napi\_env env1, napi\_callback\_info info) {
    OH\_LOG\_ERROR(LOG\_APP, "TestDefineClassWithProperty start");
    JSVM\_InitOptions init\_options;
    memset(&init\_options, 0, sizeof(init\_options));
    init\_options.externalReferences = externals;
    if (aa == 0) {
        OH\_JSVM\_Init(&init\_options);
        aa++;
    }
    JSVM\_VM vm;
    JSVM\_CreateVMOptions options;
    memset(&options, 0, sizeof(options));
    OH\_JSVM\_CreateVM(&options, &vm);
    JSVM\_VMScope vm\_scope;
    OH\_JSVM\_OpenVMScope(vm, &vm\_scope);
    JSVM\_Env env;
    JSVM\_CallbackStruct param\[1\];
    param\[0\].data = nullptr;
    param\[0\].callback = assertEqual;
    JSVM\_PropertyDescriptor descriptor\[\] = {
        {"assertEqual", NULL, &param\[0\], NULL, NULL, NULL, JSVM\_DEFAULT},
    };
    OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    JSVM\_HandleScope handlescope;
    OH\_JSVM\_OpenHandleScope(env, &handlescope);

    JSVM\_CallbackStruct param1;
    param1.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        JSVM\_Value thisVar = nullptr;
        OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
        return thisVar;
    };
    param1.data = nullptr;

    JSVM\_Value res = nullptr;
    Test \*test = new Test();
    test->ptr1 = (void \*)test1;
    test->ptr2 = (void \*)test1;
    OH\_LOG\_INFO(LOG\_APP, "OH\_JSVM\_CreateBigintWords 111 word count %{public}d",
                sizeof(\*test) / sizeof(uint64\_t));
    JSVM\_Status status = OH\_JSVM\_CreateBigintWords(env, 1, 2, reinterpret\_cast<const uint64\_t \*>(test), &res);

    // Initialize propertyCfg.
    JSVM\_PropertyHandlerConfigurationStruct propertyCfg;
    propertyCfg.genericNamedPropertyGetterCallback = GetPropertyCbInfo;
    propertyCfg.genericNamedPropertySetterCallback = SetPropertyCbInfo;
    propertyCfg.genericNamedPropertyDeleterCallback = DeleterPropertyCbInfo;
    propertyCfg.genericNamedPropertyEnumeratorCallback = EnumeratorPropertyCbInfo;
    propertyCfg.genericIndexedPropertyGetterCallback = IndexedPropertyGet;
    propertyCfg.genericIndexedPropertySetterCallback = IndexedPropertySet;
    propertyCfg.genericIndexedPropertyDeleterCallback = IndexedPropertyDeleter;
    propertyCfg.genericIndexedPropertyEnumeratorCallback = IndexedPropertyEnumerator;
    propertyCfg.namedPropertyData = res;
    propertyCfg.indexedPropertyData = res;

    JSVM\_CallbackStruct callbackStruct;
    callbackStruct.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        OH\_LOG\_INFO(LOG\_APP, "call as a function called");
        JSVM\_Value thisVar = nullptr;
        void \*innerData;
        size\_t argc = 1;
        JSVM\_Value args\[1\];
        OH\_JSVM\_GetCbInfo(env, info, &argc, args, &thisVar, &innerData);
        OH\_LOG\_INFO(LOG\_APP, "function call as function result is %{public}s", reinterpret\_cast<char \*>(innerData));
        uint32\_t ret = 0;
        OH\_JSVM\_GetValueUint32(env, args\[0\], &ret);
        const char testStr\[\] = "hello world 111111";
        JSVM\_Value setvalueName = nullptr;
        JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, testStr, strlen(testStr), &setvalueName));
        return setvalueName;
    };
    char data\[100\] = "1111 hello world";
    callbackStruct.data = data;
    JSVM\_Value testWrapClass = nullptr;

    // Register a property access listener in propertyCfg.
    OH\_JSVM\_DefineClassWithPropertyHandler(env, "TestWrapClass", NAPI\_AUTO\_LENGTH, &param1, 0, nullptr, &propertyCfg,
                                           &callbackStruct, &testWrapClass);
    JSVM\_Value instanceValue = nullptr;
    OH\_JSVM\_NewInstance(env, testWrapClass, 0, nullptr, &instanceValue);
    const char testStr\[\] = "hello world";
    JSVM\_Value setvalueName = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, testStr, strlen(testStr), &setvalueName);

    // 1. Callbacks for properties.
    // Set properties.
    OH\_JSVM\_SetNamedProperty(env, instanceValue, "str11", setvalueName);
    OH\_JSVM\_SetNamedProperty(env, instanceValue, "str123", setvalueName);

    // Obtain properties.
    JSVM\_Value valueName = nullptr;
    OH\_JSVM\_GetNamedProperty(env, instanceValue, "str11", &valueName);
    char str\[100\];
    size\_t size = 0;
    OH\_JSVM\_GetValueStringUtf8(env, valueName, str, 100, &size);

    // Obtain all property names.
    JSVM\_Value allPropertyNames = nullptr;
    OH\_JSVM\_GetAllPropertyNames(env, instanceValue, JSVM\_KEY\_OWN\_ONLY,
                                static\_cast<JSVM\_KeyFilter>(JSVM\_KEY\_ENUMERABLE | JSVM\_KEY\_SKIP\_SYMBOLS),
                                JSVM\_KEY\_NUMBERS\_TO\_STRINGS, &allPropertyNames);
    uint32\_t nameSize = 0;
    OH\_JSVM\_GetArrayLength(env, allPropertyNames, &nameSize);
    JSVM\_Value propertyName = nullptr;
    for (uint32\_t i = 0; i < nameSize; ++i) {
        OH\_JSVM\_GetElement(env, allPropertyNames, i, &propertyName);
        char str\[100\];
        size\_t size = 0;
        OH\_JSVM\_GetValueStringUtf8(env, propertyName, str, 100, &size);
    }

    // Delete a property.
    bool result = false;
    propertyName = nullptr;
    char propertyChar\[\] = "str11";
    OH\_JSVM\_CreateStringUtf8(env, propertyChar, strlen(propertyChar), &propertyName);
    OH\_JSVM\_DeleteProperty(env, instanceValue, propertyName, &result);

    // 2. Callbacks for index properties.
    // Set properties.
    JSVM\_Value jsIndex = nullptr;
    uint32\_t index = 0;
    OH\_JSVM\_CreateUint32(env, index, &jsIndex);
    OH\_JSVM\_SetProperty(env, instanceValue, jsIndex, setvalueName);
    JSVM\_Value jsIndex1 = nullptr;
    index = 1;
    OH\_JSVM\_CreateUint32(env, index, &jsIndex1);
    OH\_JSVM\_SetProperty(env, instanceValue, jsIndex1, setvalueName);

    // Obtain properties.
    JSVM\_Value valueName1 = nullptr;
    OH\_JSVM\_GetProperty(env, instanceValue, jsIndex, &valueName1);
    char str1\[100\];
    size\_t size1 = 0;
    OH\_JSVM\_GetValueStringUtf8(env, valueName1, str1, 100, &size1);

    // Obtain all property names.
    JSVM\_Value allPropertyNames1 = nullptr;
    OH\_JSVM\_GetAllPropertyNames(env, instanceValue, JSVM\_KEY\_OWN\_ONLY,
                                static\_cast<JSVM\_KeyFilter>(JSVM\_KEY\_ENUMERABLE | JSVM\_KEY\_SKIP\_SYMBOLS),
                                JSVM\_KEY\_NUMBERS\_TO\_STRINGS, &allPropertyNames1);
    uint32\_t nameSize1 = 0;
    OH\_JSVM\_GetArrayLength(env, allPropertyNames1, &nameSize1);
    JSVM\_Value propertyName1 = nullptr;
    for (uint32\_t i = 0; i < nameSize1; ++i) {
        OH\_JSVM\_GetElement(env, allPropertyNames1, i, &propertyName1);
        char str\[100\];
        size\_t size = 0;
        OH\_JSVM\_GetValueStringUtf8(env, propertyName1, str, 100, &size);
    }

    // Delete a property.
    bool result1 = false;
    OH\_JSVM\_DeleteProperty(env, instanceValue, jsIndex, &result1);

    // 3. Callback of a function.
    JSVM\_Value globalObj = nullptr;
    OH\_JSVM\_GetGlobal(env, &globalObj);
    OH\_JSVM\_SetNamedProperty(env, globalObj, "myTestInstance", instanceValue);
    OH\_LOG\_INFO(LOG\_APP, "set property on global object");
    std::string innerSourcecodestr = R"(
    {
        let res = myTestInstance(12);
    })";
    JSVM\_Value innerSourcecodevalue;
    OH\_JSVM\_CreateStringUtf8(env, innerSourcecodestr.c\_str(), innerSourcecodestr.size(), &innerSourcecodevalue);
    JSVM\_Script innerscript;
    OH\_JSVM\_CompileScript(env, innerSourcecodevalue, nullptr, 0, true, nullptr, &innerscript);
    JSVM\_Value innerResult;
    OH\_JSVM\_RunScript(env, innerscript, &innerResult);

    OH\_JSVM\_CloseHandleScope(env, handlescope);
    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vm\_scope);
    OH\_JSVM\_DestroyVM(vm);
    OH\_LOG\_ERROR(LOG\_APP, "TestDefineClassWithProperty pass");
    return nullptr;
}

Scenario: Set a parent class and register a listener for property access operations.

For details, see [Working with Classes Using JSVM-API](../jsvm-api-guides/working-with-classes-using-jsvm-api/document.md).

## Version Management

**Scenarios**

Obtain version information.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetVersion | Obtains the latest JSVM API version supported by the JSVM runtime. |
| OH\_JSVM\_GetVMInfo | Obtains the VM information. |

Example:

Obtain version information.

JSVM\_VMInfo result;
OH\_JSVM\_GetVMInfo(&result);
uint32\_t versionId = 0;
OH\_JSVM\_GetVersion(env, &versionId);

## Memory Management

**Scenarios**

Perform memory management.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_AdjustExternalMemory | Adjusts the amount of registered external memory used to give the JSVM an indication of the amount of externally allocated memory that is kept alive by JS objects. The JSVM then determines whether to perform global GC. Increasing the externally allocated memory will increase the probability of triggering global. |
| OH\_JSVM\_MemoryPressureNotification | Notifies the VM of the memory pressure level and selectively triggers GC. |
| OH\_JSVM\_AllocateArrayBufferBackingStoreData | Allocates memory for a backing store. |
| OH\_JSVM\_FreeArrayBufferBackingStoreData | Releases the backing store memory. |
| OH\_JSVM\_CreateArrayBufferFromBackingStoreData | Creates an array buffer based on the backing store memory allocated. |

Using a backing store is a critical operation. You must ensure correct use of memory and exercise caution when using it. For details, see the following example.

Example:

Perform memory management.

// Before and after calling OH\_JSVM\_AdjustExternalMemory, check the memory allocated externally from the perspective of the underlying VM.
int64\_t result = 0;
OH\_JSVM\_AdjustExternalMemory(env, 0, &result); // The externally allocated memory remains unchanged.
OH\_LOG\_INFO(LOG\_APP, "Before AdjustExternalMemory: %{public}lld\\n", result); // Obtain the memory value before the adjustment.
// Increase the memory usage and notify the VM of the change.
int64\_t memoryIncrease = 1024 \* 1024; // Increase the memory by 1 MB.
OH\_JSVM\_AdjustExternalMemory(env, memoryIncrease, &result);
OH\_LOG\_INFO(LOG\_APP, "After AdjustExternalMemory: %{public}lld\\n", result); // Obtain the memory value after the adjustment.

// Open a handle scope and apply for a large amount of memory within the scope to test the function.
// Check the memory status after the memory is allocated, after the scope is closed, and after OH\_JSVM\_MemoryPressureNotification is called.
JSVM\_HandleScope tmpscope = nullptr;
OH\_JSVM\_OpenHandleScope(env, &tmpscope);
for (int i = 0; i < 1000000; ++i) {
    JSVM\_Value obj;
    OH\_JSVM\_CreateObject(env, &obj);
}
JSVM\_HeapStatistics mem;
OH\_JSVM\_GetHeapStatistics(vm, &mem); // Obtain the heap statistics of the VM.
OH\_LOG\_INFO(LOG\_APP, "%{public}zu\\n", mem.usedHeapSize); // After the requested memory is allocated, the memory is of the maximum size.
OH\_JSVM\_CloseHandleScope (env, tmpscope); // Close the handle scope.

OH\_JSVM\_GetHeapStatistics(vm, &mem);
OH\_LOG\_INFO(LOG\_APP, "%{public}zu\\n", mem.usedHeapSize); // After the scope is closed, GC is not performed immediately.

// Notify the VM of the memory pressure level and selectively trigger GC.
OH\_JSVM\_MemoryPressureNotification(env, JSVM\_MEMORY\_PRESSURE\_LEVEL\_CRITICAL); // The memory pressure is in the critical state.

OH\_JSVM\_GetHeapStatistics(vm, &mem);
OH\_LOG\_INFO(LOG\_APP, "%{public}zu\\n", mem.usedHeapSize); // After GC is triggered.

Example

void \*backingStore;
JSVM\_Value arrayBuffer;

// Allocate memory of 100 bytes for a backing store.
OH\_JSVM\_AllocateArrayBufferBackingStoreData(100, JSVM\_ZERO\_INITIALIZED, &backingStore);

// In the allocated memory, create an ArrayBuffer of 20 bytes at 30 bytes away from the start address of the backing store.
OH\_JSVM\_CreateArrayBufferFromBackingStoreData(env, backingStore, 100, 30, 20, &arrayBuffer);

// Use the created ArrayBuffer in JS.
JSVM\_Value js\_global;
JSVM\_Value name;
OH\_JSVM\_GetGlobal(env, &js\_global);
OH\_JSVM\_CreateStringUtf8(env, "buffer", JSVM\_AUTO\_LENGTH, &name);
OH\_JSVM\_SetProperty(env, js\_global, name, arrayBuffer);

JSVM\_Script script;
JSVM\_Value scriptString;
JSVM\_Value result;
const char \*src = R"JS(
function writeBuffer(data) {
  let view = new Uint8Array(data);
  // Write some values to the ArrayBuffer
  for (let i = 0; i < view.length; i++) {
    view\[i\] = i % 256;
  }
}
writeBuffer(buffer)
)JS";
OH\_JSVM\_CreateStringUtf8(env, src, JSVM\_AUTO\_LENGTH, &scriptString);
OH\_JSVM\_CompileScriptWithOptions(env, scriptString, 0, nullptr, &script);
OH\_JSVM\_RunScript(env, script, &result);

// Check the ArrayBuffer content.
uint8\_t \*array = static\_cast<uint8\_t\*>(backingStore);
for (auto i = 0; i < 100; ++i) {
  if (array\[i\] != i % 256) {
    return false;
  }
}

// Release the ArrayBuffer. Before releasing the backing store, you must
// call OH\_JSVM\_DetachArraybuffer to release all ArrayBuffers created in the backing store.
// Otherwise, unpredictable memory problems may occur.
OH\_JSVM\_DetachArraybuffer(env, arrayBuffer);

// Release the memory allocated for the backing store.
OH\_JSVM\_FreeArrayBufferBackingStoreData(backingStore);

## Promises

**Scenarios**

Perform operations related to promises.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreatePromise | Creates a **deferred** object and a JS promise. |
| OH\_JSVM\_ResolveDeferred | Resolves a JS promise by using the **deferred** object associated with it. |
| OH\_JSVM\_RejectDeferred | Rejects a JS promise by using the **deferred** object associated with it. |
| OH\_JSVM\_IsPromise | Checks whether a promise object is a native promise object. |

Example:

Perform operations related to promises.

JSVM\_Deferred deferred;
JSVM\_Value promise;
OH\_JSVM\_CreatePromise(env, &deferred, &promise);

// Perform an asynchronous operation.
int result = 42;
bool success = true;
if (success)
{
    // Resolve the promise and pass the result.
    JSVM\_Value value;
    OH\_JSVM\_CreateInt32(env, result, &value);
    OH\_JSVM\_ResolveDeferred(env, deferred, value);
} else {
    // Reject the promise and pass the error information.
    JSVM\_Value code = nullptr;
    JSVM\_Value message = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "600", JSVM\_AUTO\_LENGTH, &code);
    OH\_JSVM\_CreateStringUtf8(env, "Async operation failed", JSVM\_AUTO\_LENGTH, &message);
    JSVM\_Value error = nullptr;
    OH\_JSVM\_CreateError(env, code, message, &error);
    OH\_JSVM\_RejectDeferred(env, deferred, error);
}

## JSON Operations

**Scenarios**

Perform JSON operations.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_JsonParse | Parses a JSON string and returns the parsed value. |
| OH\_JSVM\_JsonStringify | Converts a JS object into a JSON string and returns the converted string. |

Example:

Parse JSON strings.

std::string sourcecodestr = "{\\"name\\": \\"John\\", \\"age\\": 30, \\"city\\": \\"New York\\"}" ;
JSVM\_Value jsonString;
OH\_JSVM\_CreateStringUtf8(env, sourcecodestr.c\_str(), sourcecodestr.size(), &jsonString);
JSVM\_Value result;
OH\_JSVM\_JsonParse(env, jsonString, &result);

## Creating and Using a VM Startup Snapshot

**Scenarios**

Create and use a VM startup snapshot.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateSnapshot | Creates a VM startup snapshot. |
| OH\_JSVM\_CreateEnvFromSnapshot | Creates a JSVM environment from a startup snapshot. |

Example:

See \[Working with VM Snapshots Using JSVM-API\] (use-jsvm-create-snapshot.md).

## Checking Input Parameters

**Scenarios**

Check whether the input parameters are callable.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_IsCallable | Checks whether the input parameters are callable. |

Example:

Check whether the input parameters are callable.

static JSVM\_Value NapiIsCallable(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_Value value, rst;
    size\_t argc = 1;
    bool isCallable = false;
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, &value, NULL, NULL));
    JSVM\_CALL(OH\_JSVM\_IsCallable(env, value, &isCallable));
    OH\_JSVM\_GetBoolean(env, isCallable, &rst);
    return rst;
}

static napi\_value MyJSVMDemo(\[\[maybe\_unused\]\] napi\_env \_env, \[\[maybe\_unused\]\] napi\_callback\_info \_info) {
    std::thread t(\[\]() {
        // Create a VM instance and open the VM scope.
        JSVM\_VM vm;
        JSVM\_CreateVMOptions options;
        memset(&options, 0, sizeof(options));
        OH\_JSVM\_CreateVM(&options, &vm);
        JSVM\_VMScope vmScope;
        OH\_JSVM\_OpenVMScope(vm, &vmScope);
        JSVM\_CallbackStruct param\[\] = {
            {.data = nullptr, .callback = NapiIsCallable},
        };
        JSVM\_PropertyDescriptor descriptor\[\] = {
            {"napiIsCallable", NULL, &param\[0\], NULL, NULL, NULL, JSVM\_DEFAULT},
        };
        // Create env, register a native method, and open an env scope.
        JSVM\_Env env;
        OH\_JSVM\_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor, &env);
        JSVM\_EnvScope envScope;
        OH\_JSVM\_OpenEnvScope(env, &envScope);
        // Open a handle scope.
        JSVM\_HandleScope handleScope;
        OH\_JSVM\_OpenHandleScope(env, &handleScope);
        std::string sourceCodeStr = R"JS(
        function addNumbers(num1, num2)
        {
            var rst= num1 + num2;
            return rst;
        }
        let rst = napiIsCallable(addNumbers);
        )JS";
        // Compile the JS script.
        JSVM\_Value sourceCodeValue;
        OH\_JSVM\_CreateStringUtf8(env, sourceCodeStr.c\_str(), sourceCodeStr.size(), &sourceCodeValue);
        JSVM\_Script script;
        OH\_JSVM\_CompileScript(env, sourceCodeValue, nullptr, 0, true, nullptr, &script);
        JSVM\_Value result;
        // Run the JS script.
        OH\_JSVM\_RunScript(env, script, &result);
        JSVM\_ValueType type;
        OH\_JSVM\_Typeof(env, result, &type);
        OH\_LOG\_INFO(LOG\_APP, "JSVM API TEST type: %{public}d", type);
        // Exit the VM and release the memory.
        OH\_JSVM\_CloseHandleScope(env, handleScope);
        OH\_JSVM\_CloseEnvScope(env, envScope);
        OH\_JSVM\_DestroyEnv(env);
        OH\_JSVM\_CloseVMScope(vm, vmScope);
        OH\_JSVM\_DestroyVM(vm);
    });
    t.detach();
    return nullptr;
}

## Lock Operations

**Scenarios**

Perform lock operations.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_IsLocked | Checks whether the current thread holds a lock of the specified environment. |
| OH\_JSVM\_AcquireLock | Obtains a lock. |
| OH\_JSVM\_ReleaseLock | Releases a lock. |

Example:

Obtain and release a lock.

class LockWrapper {
 public:
  LockWrapper(JSVM\_Env env) : env(env) {
    OH\_JSVM\_IsLocked(env, &isLocked);
    if (!isLocked) {
      OH\_JSVM\_AcquireLock(env);
      OH\_JSVM\_GetVM(env, &vm);
      OH\_JSVM\_OpenVMScope(vm, &vmScope);
      OH\_JSVM\_OpenEnvScope(env, &envScope);
    }
  }

  ~LockWrapper() {
    if (!isLocked) {
      OH\_JSVM\_CloseEnvScope(env, envScope);
      OH\_JSVM\_CloseVMScope(vm, vmScope);
      OH\_JSVM\_ReleaseLock(env);
    }
  }

  LockWrapper(const LockWrapper&) = delete;
  LockWrapper& operator=(const LockWrapper&) = delete;
  LockWrapper(LockWrapper&&) = delete;
  void\* operator new(size\_t) = delete;
  void\* operator new\[\](size\_t) = delete;

 private:
  JSVM\_Env env;
  JSVM\_EnvScope envScope;
  JSVM\_VMScope vmScope;
  JSVM\_VM vm;
  bool isLocked;
};

static int aa = 0;

static napi\_value Add(\[\[maybe\_unused\]\] napi\_env \_env, \[\[maybe\_unused\]\] napi\_callback\_info \_info) {
    static JSVM\_VM vm;
    static JSVM\_Env env;
    if (aa == 0) {
        OH\_JSVM\_Init(nullptr);
        aa++;
        // create vm
        JSVM\_CreateVMOptions options;
        memset(&options, 0, sizeof(options));
        OH\_JSVM\_CreateVM(&options, &vm);
        // create env
        OH\_JSVM\_CreateEnv(vm, 0, nullptr, &env);
    }

    std::thread t1(\[\]() {
        LockWrapper lock(env);
        JSVM\_HandleScope handleScope;
        OH\_JSVM\_OpenHandleScope(env, &handleScope);
        JSVM\_Value value;
        JSVM\_Status rst = OH\_JSVM\_CreateInt32(env, 32, &value); // 32: numerical value
        if (rst == JSVM\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "JSVM:t1 OH\_JSVM\_CreateInt32 suc");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "JSVM:t1 OH\_JSVM\_CreateInt32 fail");
        }
        int32\_t num1 = 0;
        OH\_JSVM\_GetValueInt32(env, value, &num1);
        OH\_LOG\_INFO(LOG\_APP, "JSVM:t1 num1 = %{public}d", num1);
        OH\_JSVM\_CloseHandleScope(env, handleScope);
    });
    std::thread t2(\[\]() {
        LockWrapper lock(env);
        JSVM\_HandleScope handleScope;
        OH\_JSVM\_OpenHandleScope(env, &handleScope);
        JSVM\_Value value;
        JSVM\_Status rst = OH\_JSVM\_CreateInt32(env, 32, &value); // 32: numerical value
        if (rst == JSVM\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "JSVM:t2 OH\_JSVM\_CreateInt32 suc");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "JSVM:t2 OH\_JSVM\_CreateInt32 fail");
        }
        int32\_t num1 = 0;
        OH\_JSVM\_GetValueInt32(env, value, &num1);
        OH\_LOG\_INFO(LOG\_APP, "JSVM:t2 num1 = %{public}d", num1);
        OH\_JSVM\_CloseHandleScope(env, handleScope);
    });
    t1.detach();
    t2.detach();
    return nullptr;
}

## Setting and Obtaining Data Associated with a JSVM Instance

**Scenarios**

Call **OH\_JSVM\_SetInstanceData** to set the data associated with a JSVM instance.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_SetInstanceData | Sets data to be associated with a JSVM instance. |
| OH\_JSVM\_GetInstanceData | Obtains the data associated with a JSVM instance. |

Example:

Set and obtain the data associated with a JSVM instance.

JSVM\_VM vm;
JSVM\_CreateVMOptions options;
JSVM\_VMScope vm\_scope;
JSVM\_Env env;
JSVM\_EnvScope envScope;
JSVM\_HandleScope handlescope;

static int aa = 0;
struct InstanceData {
    int32\_t value;
};

// Initialize the VM and create a JSVM instance.
void init\_JSVM\_environment(){
    JSVM\_InitOptions init\_options;
    memset(&init\_options, 0, sizeof(init\_options));
    if (aa == 0) {
        OH\_JSVM\_Init(&init\_options);
        aa++;
    }
    memset(&options, 0, sizeof(options));
    OH\_JSVM\_CreateVM(&options, &vm);
    OH\_JSVM\_OpenVMScope(vm, &vm\_scope);
    OH\_JSVM\_CreateEnv(vm, 0, nullptr, &env);
    OH\_JSVM\_OpenEnvScope(env, &envScope);
    OH\_JSVM\_OpenHandleScope(env, &handlescope);
}

// Exit the VM and release the running environment.
napi\_value close\_JSVM\_environment(napi\_env env1, napi\_callback\_info info)
{
    OH\_JSVM\_CloseHandleScope(env, handlescope);
    OH\_JSVM\_CloseEnvScope(env, envScope);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vm\_scope);
    OH\_JSVM\_DestroyVM(vm);
    napi\_value result;
    char\* s = "ok";
    napi\_create\_string\_latin1(env1, s, strlen(s), &result);
    return result;
}

// Clear and release the memory used by the instance.
void InstanceFinalizeCallback(JSVM\_Env env, void \*finalizeData, void \*finalizeHint)
{
    if (finalizeData) {
        InstanceData \*data = reinterpret\_cast<InstanceData \*>(finalizeData);
        free(data);
        \*(InstanceData \*\*)finalizeData = nullptr;
    }
}

static napi\_value GetInstanceData(napi\_env env1, napi\_callback\_info info)
{
    InstanceData \*instanceData = reinterpret\_cast<InstanceData \*>(malloc(sizeof(InstanceData)));
    if (instanceData == nullptr) {
        printf("Memory allocation failed!\\n");
        return nullptr;
    }
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    // Obtain the callback function parameters.
    napi\_get\_cb\_info(env1, info, &argc, args , nullptr, nullptr);
    napi\_valuetype valuetype0;
    napi\_typeof(env1, args\[0\], &valuetype0);
    int32\_t tmp = 0;
    napi\_get\_value\_int32(env1, args\[0\], &tmp);
    instanceData->value = tmp;
    // Associate the obtained parameters with the current JSVM environment.
    OH\_JSVM\_SetInstanceData(env, instanceData, InstanceFinalizeCallback, nullptr);
    InstanceData \*resData = nullptr;
    // Obtain the data associated with the JSVM instance.
    OH\_JSVM\_GetInstanceData(env, (void \*\*)&resData);
    napi\_value result;
    napi\_create\_uint32(env1, resData->value, &result);
    return result;
}

## Task Queue

**Scenarios**

Start the running of a task queue in a JSVM and check whether there are micro tasks waiting in the queue. The task queue can be executed cyclically by external events.

**Available APIs**

| API | Description |
| :-- | :-- |
| OH\_JSVM\_PumpMessageLoop | Starts running a task queue. |
| OH\_JSVM\_PerformMicrotaskCheckpoint | Executes micro tasks in a task queue. |

Example:

[Working with Tasks Using JSVM-API](../jsvm-api-guides/working-with-tasks-using-jsvm-api/document.md)
