# How do I manage the JSVM\_CallbackStruct lifecycle?

**Question**

1.  The application crashes when the JavaScript function created using **OH\_JSVM\_CreateFunction** is called.
    
    You need to specify the time to release the memory allocated for **JSVM\_CallbackStruct** using **new()**.
    

**Possible Causes**

The lifecycle of **JSVM\_CallbackStruct** is not correctly managed. An example of the error code is as follows:

JSVM\_Value CreateFunction(JSVM\_Env env) {
    JSVM\_CallbackStruct callbackStruct;
    callbackStruct.data = nullptr;
    callbackStruct.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        return nullptr;
    };

    JSVM\_Value result = nullptr;
    OH\_JSVM\_CreateFunction(env, "foo", JSVM\_AUTO\_LENGTH, &callbackStruct, &result);
    return result;
}
void SomeFunction() {
    char stack\[\] = "hello world";
}

The application crashes when the following code is executed:

// ...

auto func = CreateFunction(env);
SomeFunction();

JSVM\_Value undef = nullptr;
OH\_JSVM\_GetUndefined(env, &undef);

JSVM\_Value result;
OH\_JSVM\_CallFunction(env, undef, func, 0, nullptr, &result);

// ...

When **OH\_JSVM\_CallFunction** is called, **callbackStruct** is a variable on the stack, and **OH\_JSVM\_CreateFunction** receives the stack memory address (**&callbackStruct**). After **SomeFunction** is called, the stack memory is modified. When **OH\_JSVM\_CallFunction** is called, the callback function in **JSVM\_CallbackStruct** is executed. Because the memory of **JSVM\_CallbackStruct** has been modified, invalid memory access causes the application to crash.

**Answer**

If the JavaScript function created using **OH\_JSVM\_CreateFunction** needs to be used across functions, the memory for **JSVM\_CallbackStruct** must be applied for from the heap and cannot be released before the JavaScript function becomes invalid. The memory of **JSVM\_CallbackStruct** can be released by the garbage collection mechanism of the VM. You can call **OH\_JSVM\_AddFinalizer** to set the **Finalize** method for the JavaScript function. When the JavaScript function is garbage collected, the **Finalize** method is called and **JSVM\_CallbackStruct** is released. Refer to the code snippet below:

JSVM\_Value CreateFunction(JSVM\_Env env) {
    JSVM\_Callback cb = new JSVM\_CallbackStruct;
    cb->data = nullptr;
    cb->callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value { return nullptr; };

    JSVM\_Value result = nullptr;
    OH\_JSVM\_CreateFunction(env, "foo", JSVM\_AUTO\_LENGTH, cb, &result);
    OH\_JSVM\_AddFinalizer(
        env, result, reinterpret\_cast<void \*>(cb),
        \[\](JSVM\_Env env, void \*data, void \*hint) -> void { 
            delete static\_cast<JSVM\_Callback>(data);
        }, nullptr, nullptr);

    return result;
}
