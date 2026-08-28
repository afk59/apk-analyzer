# What do I do if the application crashes when JS code is executed in Finalizer()?

**Symptom**

The crash call stack is as follows:

#00 pc 0000000001d2cfa8 /system/lib64/ndk/libjsvm.so(v8::base::OS::Abort()+28)
#01 pc 0000000001d21bfc /system/lib64/ndk/libjsvm.so(V8\_Fatal(char const\*, ...)+384)
#02 pc 000000000159ba30 /system/lib64/ndk/libjsvm.so(v8::internal::(anonymous namespace)::Invoke(v8::internal::Isolate\*, v8::internal::(anonymous namespace)::InvokeParams const&)+2952)
#03 pc 000000000159ae24 /system/lib64/ndk/libjsvm.so(v8::internal::Execution::Call(v8::internal::Isolate\*, v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>\*)+96)
#04 pc 0000000001432154 /system/lib64/ndk/libjsvm.so(v8::Function::Call(v8::Local<v8::Context>, v8::Local<v8::Value>, int, v8::Local<v8::Value>\*)+384)
#05 pc 0000000000c6e3e0 /system/lib64/ndk/libjsvm.so(OH\_JSVM\_CallFunction+348)
........
#24 pc 0000000000c77df8 /system/lib64/ndk/libjsvm.so(JSVM\_Env\_\_::CallFinalizer(void (\*)(JSVM\_Env\_\_\*, void\*, void\*), void\*, void\*)+96)
#25 pc 0000000000c65f5c /system/lib64/ndk/libjsvm.so(non-virtual thunk to v8impl::Reference::Finalize()+108)
#26 pc 0000000000c65fdc /system/lib64/ndk/libjsvm.so(v8impl::Reference::WeakCallback(v8::WeakCallbackInfo<v8impl::Reference> const&)+76)

**Possible Causes**

Currently, the Finalizer() method registered by the JSVM does not allow JS code. In the preceding crash call stack, the **Finalizer()** method calls **OH\_JSVM\_CallFunction** to execute JS code.

**Solution**

In Finalizer, only objects bound to the lifecycle of the JS object are cleared, and the JSVM API is not called. To execute a piece of JS code after the lifecycle of the JS object ends, you can add the execution of the related code to the external event loop queue in the Finalizer method and call the code when the next event loop is executed. In this way, the time sequence is implemented.
