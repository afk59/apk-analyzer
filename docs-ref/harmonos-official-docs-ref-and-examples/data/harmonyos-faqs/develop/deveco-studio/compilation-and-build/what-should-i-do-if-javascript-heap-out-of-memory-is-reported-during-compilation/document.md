# What should I do if "JavaScript heap out of memory" is reported during compilation in a Linux environment?

**Symptom**

In a Linux environment, the system memory is 64 GB, and **\--max-old-space-size=40960** is configured in the hvigorw script. However, during the compilation and build process, "JavaScript heap out of memory" is reported even though the actual memory usage has not reached the configured limit (for example, only around 20 GB is used).

FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
Writing Node.js report to file: report.20200512.172528.47517.24.011.json
Node.js report completed
1: 0xa295e0 node::Abort() \[node\]
2: 0x9782df node::FatalError(char const\*, char const\*) \[node\]
3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate\*, char const\*, bool) \[node\]
4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate\*, char const\*, bool) \[node\]
5: 0xd3a3b5 \[node\]
6: 0xd74f27 \[node\]
7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() \[node\]
8: 0xd481b9 v8::internal::Heap::MarkCompact() \[node\]
9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::GCCallbackFlags) \[node\]
10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) \[node\]
11: 0xd4aebf v8::internal::Heap::HandleGCRequest() \[node\]
12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() \[node\]
13: 0x104b803 v8::internal::Runtime\_StackGuard(int, unsigned long\*, v8::internal::Isolate\*) \[node\]
14: 0x13a5a99 \[node\]
Aborted (core dumped)

**Possible Causes**

As a parameter related to the kernel's virtual memory subsystem, **vm.max\_map\_count** controls the maximum number of memory mapping areas that a process can have. It is commonly used to limit the number of files a process can open, especially in cases where a large number of memory-mapped files are used.

In Linux, the default value of **vm.max\_map\_count** is usually a relatively small number, such as **65530**. For applications or specific scenarios that require a large number of memory mappings, you are advised to increase the value of this parameter.

V8 engine cannot establish sufficient memory mapping areas even if the physical memory is sufficient when vm.max\_map\_count is insufficient, resulting in premature OOM.

**Solution**

Change the value of **vm.max\_map\_count**.

-   Temporary modification: Set it to 262144 (four times of the default value) or a larger value based on application requirements.
    
    sysctl -w vm.max\_map\_count=new\_value
    
-   Permanent modification: In the **/etc/sysctl.conf** file, add or modify the following line:
    
    \# The root permission is required.
    # The modification takes effect only after the service is restarted or sysctl -p is executed.
    vm.max\_map\_count=new\_value
    
    Save the file and run the following command to apply the changes:
    
    sysctl -p
