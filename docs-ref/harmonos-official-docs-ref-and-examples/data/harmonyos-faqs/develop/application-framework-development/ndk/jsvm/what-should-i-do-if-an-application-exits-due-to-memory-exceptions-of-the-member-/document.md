# What should I do if an application exits due to memory exceptions of the member variable (array\_buffer\_allocator\_) in the VM when OH\_JSVM\_CreateVM is called by multiple threads during application running?

**Symptom**

The crash call stack is as follows:

#00 pc 00000000017793f8 /system/lib64/ndk/libjsvm.so
#01 pc 000000000163cef4 /system/lib64/ndk/libjsvm.so(v8::internal::Heap::AllocateExternalBackingStore(std::\_\_h::function<void\* (unsigned long)> const&, unsigned long)+212)
#02 pc 0000000001777454 /system/lib64/ndk/libjsvm.so(v8::internal::BackingStore::Allocate(v8::internal::Isolate\*, unsigned long, v8::internal::SharedFlag, v8::internal::InitializedFlag)+220)
#03 pc 000000000149e420 /system/lib64/ndk/libjsvm.so
#04 pc 000000000149d99c /system/lib64/ndk/libjsvm.so(v8::internal::Builtin\_ArrayBufferConstructor(int, unsigned long\*, v8::internal::Isolate\*)+260)
#05 pc 0000000000f75984 /system/lib64/ndk/libjsvm.so(Builtins\_CEntry\_Return1\_ArgvOnStack\_BuiltinExit+100)
#06 pc 0000000000ee6e40 /system/lib64/ndk/libjsvm.so(Builtins\_JSBuiltinsConstructStub+320)
#07 pc 000000000102eae4 /system/lib64/ndk/libjsvm.so(Builtins\_ConstructHandler+644)
#08 pc 0000000000ee9b88 /system/lib64/ndk/libjsvm.so(Builtins\_InterpreterEntryTrampoline+264)
#09 pc 0000000000ee9b88 /system/lib64/ndk/libjsvm.so(Builtins\_InterpreterEntryTrampoline+264)

**Possible Causes**

According to the call stack, the error occurs in the **v8::internal::Heap::AllocateExternalBackingStore** function of the libjsvm.so library. When the function attempts to allocate external storage, it calls the **allocate** function, in which a null pointer exception occurs.

std::unique\_ptr<BackingStore> BackingStore::Allocate(
    Isolate\* isolate, size\_t byte\_length, SharedFlag shared,
    InitializedFlag initialized) {
  ...
  auto allocator = isolate->array\_buffer\_allocator();
  ...
  auto allocate\_buffer = \[allocator, initialized\](size\_t byte\_length) {
      if (initialized == InitializedFlag::kUninitialized) {
        return allocator->AllocateUninitialized(byte\_length);
      }
      void\* buffer\_start = allocator->Allocate(byte\_length);
      if (buffer\_start) {
        // TODO(wasm): node does not implement the zero-initialization API.
        // Reenable this debug check when node does implement it properly.
        constexpr bool
            kDebugCheckZeroDisabledDueToNodeNotImplementingZeroInitAPI = true;
        if ((!(kDebugCheckZeroDisabledDueToNodeNotImplementingZeroInitAPI)) &&
            !v8\_flags.mock\_arraybuffer\_allocator) {
          DebugCheckZero(buffer\_start, byte\_length);
        }
      }
      return buffer\_start;
  };
  buffer\_start = isolate->heap()->AllocateExternalBackingStore(
      allocate\_buffer, byte\_length);
  ...
}

The root cause of the error is that the allocator is empty. The allocator is returned by the **array\_buffer\_allocator()** method of **Isolate**, which is created by **v8::Isolate::New(create\_params)** in the **OH\_JSVM\_CreateVM** function. Therefore, the initialization process of **array\_buffer\_allocator** may be incorrect. Since **array\_buffer\_allocator** is created by **GetOrCreateDefaultArrayBufferAllocator()** in the **OH\_JSVM\_CreateVM** function, competitions may occur during the creation of **array\_buffer\_allocator** if multiple threads call the **OH\_JSVM\_CreateVM** function at the same time, resulting in memory exceptions.

To conclude, the allocator object is empty because the **OH\_JSVM\_CreateVM** function is called by multiple threads when **array\_buffer\_allocator** is created. As a result, a null pointer exception occurs in the **AllocateExternalBackingStore** function.

**Solution**

Add a lock on the application to ensure that **OH\_JSVM\_CreateVM** can only be called by one thread at a time. The sample code is as follows:

// Create an instance of JSVM.
const JSVM\_CreateVMOptions\* options = new JSVM\_CreateVMOptions();
JSVM\_Status res = USVM\_OK;
{
  std::Lock\_guard<std::mutex> Lock(create\_jsym\_mutex\_);
  res = OH\_JSVM\_CreateVM(options, &vm\_);
}
if (res != JSVM\_OK vm\_ == nullptr) {
  XLOG(ERROR) << "JSVM create vm failed";
}
// When we start, open vm scope.
