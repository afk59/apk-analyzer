# Using Longque JS APIs

Provided by Longque JS Engine, Longque JS APIs are used to build stable and high-performance applications on HarmonyOS. They are under the ****Longque**** object. You can use ****Longque**.version** to obtain the API version for determining features.

Note: Longque JS APIs are in the experimental phase. Before using the APIs, read this topic to evaluate their stability and compatibility.

#### Available APIs

| Name | Description |
| :-- | :-- |
| createDelegate | Creates a delegate. |

#### Properties

| Name | Description |
| :-- | :-- |
| version | Version of the Longque JS API. |
| SKIP\_PROTOTYPE\_CHAIN | Property filter of **createDelegate**, which skips the prototype chain. |
| SKIP\_PREFIX\_UNDERSCORE | Property filter of **createDelegate**, which skips properties starting with an underscore (\_). |
| SKIP\_PREFIX\_DOLLAR | Property filter of **createDelegate**, which skips properties starting with a dollar sign ($). |
| SKIP\_CONSTRUCTOR | Property filter of **createDelegate**, which skips the **constructor** property. |

#### createDelegate

API introduction version: 1

## Description

| API | Usage | Description |
| :-- | :-- | :-- |
| createDelegate | Delegate creation. | Creates a delegate object for **underlyingObject**. The read and write operations on the delegate object are mapped to **underlyingObject**. You can specify the initial delegate object through **initObject** and the property filter through **propertyFilterFlags**. By default, all enumerable string key properties in **underlyingObject** and its prototype chain are mapped. |

## Parameters

(1) **underlyingObject**: This parameter is mandatory. Underlying object to delegate. Parameter requirements:

-   **underlyingObject** must be an object. Otherwise, the **TypeError** exception is thrown.
-   If **underlyingObject** is a delegate object, a **TypeError** exception is thrown.
-   If the **SKIP\_PROTOTYPE\_CHAIN** filter is not specified and a delegate object exists in the **underlyingObject** prototype chain, a **TypeError** exception is thrown.

(2) **initObject**: This parameter is optional. Initial delegate object. If **undefined** is passed, the initial object is not specified and is automatically created by the API. Parameter requirements:

-   **initObject** must be an object. Otherwise, a **TypeError** exception is thrown.
-   If **initObject** is a delegate object, a **TypeError** exception is thrown.
-   The delegate object cannot be used as **initObject**. Otherwise, a **TypeError** exception is thrown.
-   If **initObject** is not extensible, a **TypeError** exception is thrown.
-   If some properties of **initObject** cannot be defined, a **TypeError** exception is thrown. In this case, only some properties of **initObject** are successfully defined.

(3) **propertyFilterFlags**: This parameter is optional. Property filter. If **undefined** is passed, no filter is specified. Parameter requirements:

-   The following lists the supported property filters (which may be extended in the future).

\_\_Longque\_\_.SKIP\_PROTOTYPE\_CHAIN: Delegates only the underlyingObject properties and skips the prototype chain.
\_\_Longque\_\_.SKIP\_PREFIX\_UNDERSCORE: Skips properties whose names start with underscores (\_).
\_\_Longque\_\_.SKIP\_PREFIX\_DOLLAR: Skips properties whose names start with dollar signs ($).
\_\_Longque\_\_.SKIP\_CONSTRUCTOR: Skips the constructor property.

-   You must use any of the listed filters. Otherwise, the API behavior is not defined, which may cause code compatibility issues.
-   All filters are of the **number** type. You can use the | operator to specify multiple filters.
-   If **propertyFilterFlags** is not of the **number** type, a **TypeError** exception is thrown.

## Return Value

The API returns results correctly only if no exception is thrown.

-   If no initial delegate object is specified, the newly created delegate object is returned.
-   If the initial delegate object is specified, it is returned.

## Precautions

(1) The property sequence of the delegate object may be different from the result of the **for-in** or **Object.keys** method. Do not depend on the property sequence.

(2) The implementation of the delegate object is an internal mechanism of the engine. Do not depend on the return result of calling **Object.getOwnPropertyDescriptor**, **getOwnPropertyDescriptors** or **Reflect.getOwnPropertyDescriptor** on the delegate object.

## Sample Code

The following example shows how to use the Longque JS API in JSVM. If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../using-jsvm-api/jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in using the Longque JS API.

C++ code:

// JS code to be executed.
static const char \*STR\_TASK = R"JS(
  function createDelegateTest() {
    var myobj = {
      42: 0,
      x: 1,
      \_y: 2,
      $z:3
    };

    var proto = {
      foo: 'foo'
    };
    Object.setPrototypeOf(myobj, proto);

    var d1 = \_\_Longque\_\_.createDelegate(myobj, undefined);
    consoleinfo(JSON.stringify(d1)); // {"42":0,"x":1,"\_y":2,"$z":3,"foo":"foo"}

    const propertyFilterFlags = \_\_Longque\_\_.SKIP\_PREFIX\_UNDERSCORE | \_\_Longque\_\_.SKIP\_PREFIX\_DOLLAR;
    var d2 = \_\_Longque\_\_.createDelegate(myobj, undefined, propertyFilterFlags);
    consoleinfo(JSON.stringify(d2)); // {"42":0,"x":1,"foo":"foo"}

    d2\[42\] = 100;

    const newFilter = propertyFilterFlags | \_\_Longque\_\_.SKIP\_PROTOTYPE\_CHAIN;
    var d3 = \_\_Longque\_\_.createDelegate(myobj, undefined, newFilter);
    consoleinfo(JSON.stringify(d3)); // {"42":100,"x":1}
  }
  createDelegateTest();
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

    // Close and destroy the environment and the VM.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handlescope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vm\_scope));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

Expected output:

JSVM API TEST: {"42":0,"x":1,"\_y":2,"$z":3,"foo":"foo"}
JSVM API TEST: {"42":0,"x":1,"foo":"foo"}
JSVM API TEST: {"42":100,"x":1}

## Performance Testing Sample Code

This sample code demonstrates how to test the performance before and after using Longque JS APIs.

C++ code:

// JS code to be executed.
static const char \*STR\_TASK = R"JS(
  // Original JS code
  function base(underlying) {
    var obj = {};
    var tryDefineProperty = function (key) {
      if (key.indexOf('\_') === 0 || key.indexOf('$') === 0 || key === 'constructor') {
        return false;
      }
      Object.defineProperty(obj, key, {
        configurable: true,
        enumerable: true,
        get: function get() {
          return underlying\[key\];
        },
        set: function set(value) {
          return (underlying\[key\] = value);
        },
      });
      return true;
    };
    for (var key in underlying) {
      if (!tryDefineProperty(key)) {
        continue;
      }
    }
    return obj;
  }

  // Code after the Longque JSVM API is used
  function opt(underlying) {
    var delegate = \_\_Longque\_\_.createDelegate(
      underlying,
      undefined,
      \_\_Longque\_\_.SKIP\_PREFIX\_UNDERSCORE |
      \_\_Longque\_\_.SKIP\_PREFIX\_DOLLAR |
      \_\_Longque\_\_.SKIP\_CONSTRUCTOR,
    );
    return delegate;
  }

  // Performance test
  function doTest(tag, func, underlying, times) {
    const begin = Date.now();
    var obj = null;
    for (var i = 0; i < times; ++i) {
      obj = func(underlying);
    }
    const end = Date.now();
    consoleinfo(\`\[${tag}\] Time cost: ${(end - begin).toFixed(0)} ms\`);
    return obj;
  }

  function testEntry() {
    var underlying = {
      x: 1,
      y: 2,
      foo: 'foo',
      \_bar: '\_bar',
      \_hi: '\_hi',
      $test: '$test',
      constructor: 'ctor',
      pi: 3.14,
    };
    for (var i = 0; i < 100; ++i) {
      underlying\[\`key\_${i}\`\] = i;
    }
    const n = 10000;
    // Test the runtime of the original JS code.
    doTest('base', base, underlying, n);
    // Test the runtime after the Longque JSVM API is used.
    doTest('opt', opt, underlying, n);
  }

  testEntry();
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
  
    // Close and destroy the environment and the VM.
    CHECK\_RET(OH\_JSVM\_CloseHandleScope(env, handlescope));
    CHECK\_RET(OH\_JSVM\_CloseEnvScope(env, envScope));
    CHECK(OH\_JSVM\_DestroyEnv(env));
    CHECK(OH\_JSVM\_CloseVMScope(vm, vm\_scope));
    CHECK(OH\_JSVM\_DestroyVM(vm));
    return 0;
}

Output of a test:

JSVM API TEST: \[base\] Time cost: 414 ms
JSVM API TEST: \[opt\] Time cost: 148 ms
