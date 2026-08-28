# JSVM-API Development Specifications

#### Lifecycle Management

**\[Rule\]** Properly use **OH\_JSVM\_OpenHandleScope** and **OH\_JSVM\_CloseHandleScope** to minimize the lifecycle of **JSVM\_Value** and prevent memory leaks.

Each **JSVM\_Value** belongs to a specific **HandleScope** instance, which is created by **OH\_JSVM\_OpenHandleScope** and closed by **OH\_JSVM\_CloseHandleScope**. After a **HandleScope** instance is closed, the corresponding **JSVM\_Value** will be automatically released.

**NOTE**

1.  **JSVM\_Value** can be created only after **HandleScope** is opened; otherwise, the application may crash. Node-API does not have this restriction.
2.  **JSVM\_Value** cannot be used after the corresponding **HandleScope** is closed. To hold **JSVM\_Value** persistently, call **OH\_JSVM\_CreateReference** to convert **JSVM\_Value** to **JSVM\_Ref**.
3.  The scopes (including **JSVM\_VMScope**, **JSVM\_EnvScope**, and **JSVM\_HandleScope**) must be closed in reverse order. The scope opened first must be closed last. Otherwise, the application may crash.

**Example (scope closing error)**

// If JSVM\_VMScope is not closed in reverse order, the application may crash.
JSVM\_VM vm;
JSVM\_CreateVMOptions options;
OH\_JSVM\_CreateVM(&options, &vm);

JSVM\_VMScope vmScope1, vmScope2;
OH\_JSVM\_OpenVMScope(vm, &vmScope1);
OH\_JSVM\_OpenVMScope(vm, &vmScope2);

// You need to close vmScope2 and then vmScope1.
OH\_JSVM\_CloseVMScope(vm, vmScope1);
OH\_JSVM\_CloseVMScope(vm, vmScope2);
OH\_JSVM\_DestroyVM(vm);

**Encapsulation in C++**

class HandleScopeWrapper {
 public:
  HandleScopeWrapper(JSVM\_Env env) : env(env) {
    OH\_JSVM\_OpenHandleScope(env, &handleScope);
  }

  ~HandleScopeWrapper() {
    OH\_JSVM\_CloseHandleScope(env, handleScope);
  }

  HandleScopeWrapper(const HandleScopeWrapper&) = delete;
  HandleScopeWrapper& operator=(const HandleScopeWrapper&) = delete;
  HandleScopeWrapper(HandleScopeWrapper&&) = delete;
  void\* operator new(size\_t) = delete;
  void\* operator new\[\](size\_t) = delete;

 protected:
  JSVM\_Env env;
  JSVM\_HandleScope handleScope;
};

**Example**

// When JSVM-API is frequently called to create JS objects in the for loop, use handle\_scope to release resources in a timely manner when they are no longer used.
// In the following example, the lifecycle of the local variable res ends at the end of each loop. To prevent memory leaks, scope is used to release the JS object in a timely manner.
// After each for loop ends, trigger the destructor function of HandleScopeWrapper to release the JS object held by scope.
for (int i = 0; i < 100000; i++)
{
    HandleScopeWrapper scope(env);
    JSVM\_Value res;
    OH\_JSVM\_CreateObject(env, &res);
    if (i == 1000) {
        // After the loop exits, the HandleScopeWrapper destructor is automatically called to release resources.
        break;
    }
}

#### Context Sensitive in Multiple JSVM Instances

**\[Rule\]** Do not use JSVM-API to access JS objects across JSVM instances.

A JSVM instance is an independent running environment. Operations such as creating and accessing a JS object must be performed in the same JSVM instance. If an object is operated in different JSVM instances, the application may crash. A JSVM instance is represented as a **JSVM\_Env** in APIs.

**Example (incorrect)**

// Create a string object with value of "value1" in env1.
OH\_JSVM\_CreateStringUtf8(env1, "value1", JSVM\_AUTO\_LENGTH , &string);
// Create an object in env2 and set the string object to this object.
JSVM\_Status status = OH\_JSVM\_CreateObject(env2, &object);
if (status != JSVM\_OK)
{
    return;
}

status = OH\_JSVM\_SetNamedProperty(env2, object, "string1", string);
if (status != JSVM\_OK)
{
    return;
}

A JS object belongs to a specific **JSVM\_Env**. Therefore, you cannot set an object of env1 to an object of env2. If the object of env1 is accessed in env2, the application may crash.

#### JSVM Instance Shared by Multiple Threads

\[**Rule**\] When multiple threads use the same JSVM instance, use a lock to ensure that the JSVM instance can be executed in only one thread at a time. If multiple threads use the JSVM instance at the same time, the application may crash.

**NOTE**

1.  You can use **OH\_JSVM\_IsLocked** to check whether the calling thread holds the lock of the JSVM instance instead of setting a loop to wait for other threads to release the lock.
2.  Nested use of **OH\_JSVM\_AcquireLock** in the same thread will not cause deadlock.
3.  When using **OH\_JSVM\_ReleaseLock**, you need to check whether it is at the outermost layer to prevent the inner layer from releasing the lock of the entire thread when **OH\_JSVM\_AcquireLock** is nested in the same thread.
4.  After **OH\_JSVM\_AcquireLock** is called, use **OH\_JSVM\_OpenHandleScope** to enable the JSVM instance to enter the thread. Before **OH\_JSVM\_ReleaseLock** is called, use **OH\_JSVM\_CloseHandleScope** to enable the JSVM instance to exit the thread.
5.  A JSVM instance cannot be nested across threads. If you need to temporarily change the thread that uses the JSVM instance, ensure that **JSVM\_Value** is saved as **JSVM\_Ref**. After the lock is released, **JSVM\_Value** cannot be accessed.
6.  The sequence of obtaining resources is as follows: Lock -> VMScope -> EnvScope -> HandleScope. The sequence of releasing resources is the opposite. An incorrect sequence may cause the application to crash.

**Encapsulation in C++**

class LockWrapper {
 public:
  // Constructor, lock acquisition, VMScope, and EnvScope.
  LockWrapper(JSVM\_Env env) : env(env) {
    OH\_JSVM\_IsLocked(env, &isLocked);
    if (!isLocked) {
      OH\_JSVM\_AcquireLock(env);
      OH\_JSVM\_GetVM(env, &vm);
      OH\_JSVM\_OpenVMScope(vm, &vmScope);
      OH\_JSVM\_OpenEnvScope(env, &envScope);
    }
  }

  // Destructor used to release EnvScope, VMScope, and lock.
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

**Example (correct)**

// This example demonstrates how to use a JSVM across threads.
// Thread t1 obtains the lock and call JSVM-API.
// Thread t2 is blocked when thread t1 obtained the lock, continues to call JSVM-API when t1 releases the lock.
static napi\_value Add(\[\[maybe\_unused\]\] napi\_env \_env, \[\[maybe\_unused\]\] napi\_callback\_info \_info) {
    static JSVM\_VM vm;
    static JSVM\_Env env;
    static int aa = 0;
    if (aa == 0) {
        OH\_JSVM\_Init(nullptr);
        aa++;
        // create vm
        JSVM\_CreateVMOptions options;
        memset(&options, 0, sizeof(options));
        OH\_JSVM\_CreateVM(&options, &vm);
        // Create env.
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

#### Obtaining Arguments Passed from JS

**\[Rule\]** When **argv** in **OH\_JSVM\_GetCbInfo** is not **nullptr**, the length of **argv** must be greater than or equal to **argc**.

If **argv** is not **nullptr**, the arguments actually passed from JS will be written to **argv** in **OH\_JSVM\_GetCbInfo** based on the value of **argc**. If there are more arguments than the provided count, only the requested number of arguments are copied. If there are fewer arguments provided than the claimed, the rest of **argv** is filled with values that represent **undefined**.

**Example (incorrect)**

static JSVM\_Value IncorrectDemo1(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // argc is not correctly initialized and is set to a random value. If the length of argv is less than the number of arguments specified by argc, data overwriting occurs.
    size\_t argc;
    JSVM\_Value argv\[10\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    return nullptr;
}

static JSVM\_Value IncorrectDemo2(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // If the number of arguments specified by argc is greater than the length of argv, out-of-bounds write will occur when data is written to argv in napi\_get\_cb\_info.
    size\_t argc = 5;
    JSVM\_Value argv\[3\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    return nullptr;
}

**Example (correct)**

static JSVM\_Value GetArgvDemo1(napi\_env env, JSVM\_CallbackInfo info) {
    size\_t argc = 0;
    // Pass in nullptr to argv to obtain the actual number of arguments passed by JS.
    OH\_JSVM\_GetCbInfo(env, info, &argc, nullptr, nullptr, nullptr);
    // If 0 is passed by JS, the subsequent logic is not executed.
    if (argc == 0) {
        return nullptr;
    }
    // Create an array to obtain the arguments passed by JS.
    JSVM\_Value\* argv = new JSVM\_Value\[argc\];
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // Service code.
    // ... ...
    // argv is an object created by new and must be manually released when it is not required.
    delete\[\] argv;
    return nullptr;
}

static JSVM\_Value GetArgvDemo2(napi\_env env, JSVM\_CallbackInfo info) {
    size\_t argc = 2;
    JSVM\_Value\* argv\[2\] = {nullptr};
    // The arguments (of the quantity specified by argc) passed from JS or undefined will be written to argv of OH\_JSVM\_GetCbInfo.
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // Service code.
    // ... ...
    return nullptr;
}

#### Exception Handling

**\[Suggestion\]** Any exception occurred in a JSVM-API call should be handled in a timely manner. Otherwise, unexpected behavior may occur.

Exception handling can be classified into the following types based on the primary/secondary relationship:

1.  If a C++ exception occurs when the JSVM executes a C++ callback function (JS is primary and native is secondary), the exception needs to be thrown to the JSVM. The following example demonstrates the implementation of the C++ callback function in three difference scenarios. **NOTE**
    
    If the JSVM-API call in a C++ callback fails, you can either throw an exception to the JSVM or not. To throw an exception, ensure that there is no pending exception in the JSVM. If you choose not to throw an exception, JS **try-catch** can capture such JS exceptions. For details, see **NativeFunctionExceptionDemo3**.
    
    // JSVM is primary, and native is secondary.
    void DoSomething() {
        throw("Do something failed");
    }
    
    // Demo 1: Throw the exception captured in C++ to the JSVM.
    JSVM\_Value NativeFunctionExceptionDemo1(JSVM\_Env env, JSVM\_CallbackInfo info) {
        try {
            DoSomething();
        } catch (const char \*ex) {
            OH\_JSVM\_ThrowError(env, nullptr, ex);
            return nullptr;
        }
        return nullptr;
    }
    
    // Demo 2: Throw an exception to the JSVM when a JSVM-API call fails.
    JSVM\_Value NativeFunctionExceptionDemo2(JSVM\_Env env, JSVM\_CallbackInfo info) {
        JSVM\_Value JSBool = nullptr;
        bool value = false;
        auto status = OH\_JSVM\_GetValueBool(env, JSBool, &value);
        if (status != JSVM\_OK) {
            OH\_JSVM\_ThrowError(env, nullptr, "Get bool value failed");
            return nullptr;
        }
        return nullptr;
    }
    
    // Demo 3: Add an exception to the JSVM for handling when the JSVM-API call fails. In this case, you do not need to throw exceptions to the JSVM.
    JSVM\_Value NativeFunctionExceptionDemo3(JSVM\_Env env, JSVM\_CallbackInfo info) {
        std::string sourcecodestr = R"JS(
            throw Error('Error throw from js');
        )JS";
        JSVM\_Value sourcecodevalue = nullptr;
        JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, sourcecodestr.c\_str(), sourcecodestr.size(), &sourcecodevalue));
        JSVM\_Script script;
        auto status = OH\_JSVM\_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script);
        if (status != JSVM\_OK) {
            OH\_JSVM\_ThrowError(env, nullptr, "compile script failed");
            return nullptr;
        }
        JSVM\_Value result;
        // Execute the JS script and throw a JS exception during the execution.
        status = OH\_JSVM\_RunScript(env, script, &result);
        if (status != JSVM\_OK) {
            bool isPending = false;
            // If an exception already exists, do not throw the exception to the JSVM.
            // If a new exception needs to be thrown, handle the pending exception in the JSVM first.
            if (JSVM\_OK == OH\_JSVM\_IsExceptionPending((env), &isPending) && isPending) {
                return nullptr;
            }
            OH\_JSVM\_ThrowError(env, nullptr, "Runscript failed");
            return nullptr;
        }
        return nullptr;
    }
    
    // Bind NativeFunction to the JSVM. The process is omitted here.
    std::string sourcecodestr = R"JS(
        // The console log needs to be implemented.
        try {
            // Call the native function.
            NativeFunction()
        } catch (e) {
            // Handle the exception in C/C++.
            consolelog(e.message)
        }
    )JS";
    JSVM\_Value sourcecodevalue = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, sourcecodestr.c\_str(), sourcecodestr.size(), &sourcecodevalue));
    JSVM\_Script script;
    JSVM\_CALL(OH\_JSVM\_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script));
    JSVM\_Value result;
    // Execute the JS script to call native methods from JS.
    JSVM\_CALL(OH\_JSVM\_RunScript(env, script, &result));
    
2.  If JSVM-API (native is primary and JS is secondary) fails to be called from C++, clear the pending exceptions in JSVM to prevent the impact on subsequent JSVM-API execution and set a branch to handling C++ exception (or throw a C++ exception).
    
    std::string sourcecodestr = R"JS(
        throw Error('Error throw from js');
    )JS";
    JSVM\_Value sourcecodevalue = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, sourcecodestr.c\_str(), sourcecodestr.size(), &sourcecodevalue);
    JSVM\_Script script;
    auto status = OH\_JSVM\_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script);
    // Exception handling.
    if (status != JSVM\_OK) {
        JSVM\_Value error = nullptr;
        // Obtain and clear the exception.
        JSVM\_CALL(OH\_JSVM\_GetAndClearLastException((env), &error));
        // Handle the exception, for example, printing information. The code is omitted here.
        // Throw a C++ exception or stop function execution.
        throw "JS Compile Error";
    }
    JSVM\_Value result;
    // Execute the JS script and throw a JS exception during the execution.
    status = OH\_JSVM\_RunScript(env, script, &result);
    
    // Exception handling.
    if (status != JSVM\_OK) {
        JSVM\_Value error = nullptr;
        // Obtain and clear the exception.
        JSVM\_CALL(OH\_JSVM\_GetAndClearLastException((env), &error));
        // Handle the exception, for example, printing information. The code is omitted here.
        // Throw a C++ exception or stop function execution.
        throw "JS RunScript Error";
    }
    

#### Binding Object Context

**\[Rule\]**: The JS function and object generated by JSVM-API can be accessed from JS only after they are bound to the context. The const char \* parameter in **OH\_JSVM\_CreateFunction** is the property **name** of the created function, without pointing to the function name in the context. This rule also applies to the class and object generated by JSVM-API.

**Example**

JSVM\_Value JSFunc = nullptr;
const char \*name = "NativeFunction";
JSVM\_CallbackStruct cb = {NativeFunction, nullptr};
// Create a JS function, whose property "name" is set to "NativeFunction".
OH\_JSVM\_CreateFunction(env, name, strlen(name), &cb, &JSFunc);
// Bind the function to the context.
// Obtain the global object of the context.
JSVM\_Value global = nullptr;
OH\_JSVM\_GetGlobal(env, &global);
// Create the JS string "FunctionNameInJSContext."
JSVM\_Value key = nullptr;
OH\_JSVM\_CreateStringLatin1(env, "FunctionNameInJSContext", JSVM\_AUTO\_LENGTH, &key);
// Set the global property "FunctionNameInJSContext" to "JSFunc". This binds the function to the context.
OH\_JSVM\_SetProperty(env, global, key, JSFunc);
// Call the function from JS.
std::string sourcecodestr = R"JS(
    // The console log needs to be implemented.
    FunctionNameInJSContext() // The call is successful.
    consolelog(FunctionNameInJSContext.name) // Print "NativeFunction."
    try {
        NativeFunction() // If the function cannot be found, throw an exception.
    } catch (e) {
        consolelog(e.message)
    }
)JS";
