# What should I do if OOM (v8::FatalProcessOutOfMemory) occurs?

**Symptom**

When the memory requested by an application reaches the upper limit of the V8 JavaScript engine, OOM (v8::FatalProcessOutOfMemory) occurs. The crash stack information is as follows:

#00 pc 0000000001d28a24 /system/lib64/ndk/libjsvm.so(v8::base::OS::Abort()+28)#01 pc 00000000014102c0 /system/lib64/ndk/libjsvm.so(v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate\*, char const\*, v8::OOMDetails const&)+756)#02 pc 0000000001629960 /system/lib64/ndk/libjsvm.so(v8::internal::Heap::FatalProcessOutOfMemory(char const\*)+28)#03 pc 00000000016284a4 /system/lib64/ndk/libjsvm.so(v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags)+2100)#04 pc 000000000161df8c /system/lib64/ndk/libjsvm.so(v8::internal::HeapAllocator::AllocateRawWithLightRetrySlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment)+1952)#05 pc 000000000161e810 /system/lib64/ndk/libjsvm.so(v8::internal::HeapAllocator::AllocateRawWithRetryOrFailSlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment)+68)#06 pc 0000000001602744 /system/lib64/ndk/libjsvm.so(v8::internal::Factory::AllocateRaw(int, v8::internal::AllocationType, v8::internal::AllocationAlignment)+724)#07 pc 00000000015f41dc /system/lib64/ndk/libjsvm.so(v8::internal::FactoryBase<v8::internal::Factory>::NewFixedArray(int, v8::internal::AllocationType)+96)#08 pc 00000000017e8698 /system/lib64/ndk/libjsvm.so#09 pc 00000000018d86a4 /system/lib64/ndk/libjsvm.so(v8::internal::Object::CreateListFromArrayLike(v8::internal::Isolate\*, v8::internal::Handle<v8::internal::Object>, v8::internal::ElementTypes)+1168)#10 pc 0000000001a0dd9c /system/lib64/ndk/libjsvm.so(v8::internal::Runtime\_CreateListFromArrayLike(int, unsigned long\*, v8::internal::Isolate\*)+48)#11 pc 0000000000f6d0b4 /system/lib64/ndk/libjsvm.so(Builtins\_CEntry\_Return1\_ArgvOnStack\_NoBuiltinExit+84)#12 pc 0000000000eddbac /system/lib64/ndk/libjsvm.so(Builtins\_CallWithArrayLike+812)

**Solution**

Pass in the **max-semi-space-size** and **max-old-space-size** parameters (in MB) to **OH\_JSVM\_Init** to increase the memory upper limit of the V8. Check whether the app still crashes after the V8 memory upper limit is increased. If the app still crashes, use a memory leak detection tool to check whether the app has memory leakage.

// ...
JSVM\_InitOptions init\_options;
init\_options.argc = (int\*)malloc(sizeof(int));
\*init\_options.argc = 3;
init\_options.argv = (char\*\*)malloc(3 \* sizeof(char\*));
init\_options.argv\[1\] = "--max-semi-space-size=1024";
init\_options.argv\[2\] = "--max-old-space-size=1024";
init\_options.removeFlags = true;
init\_options.externalReferences = nullptr;
      
JSVM\_Status status = OH\_JSVM\_Init(&init\_options);

if (status != JSVM\_OK)  {
  // If the status is not JSVM-OK, it indicates that OH\_JSVM\_Init execution failed and init\_options was not successfully set.
}
// ...

The default values of the memory in the JSVM are as follows:

-   max\_semi\_space\_size: 16MB
-   max\_old\_space\_size: 1400MB
-   initial\_semispace\_size: 1MB
-   initial\_old\_space\_size: 512MB
