# How do I query the allocated heap memory size and free heap memory size of an application?

You can query the current CPU usage using either of the following methods:

In the code:

Call **hidebug.getNativeHeapAllocatedSize** to query the allocated heap memory size; call **hidebug.getNativeHeapFreeSize** to query the free heap memory size.

The code snippet is as follows:

let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize(); // Get the allocated memory size of the heap memory in this application
let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize(); // Get the free memory size of the heap memory in this application

In the CLI:

Run the **\--mem pid** command to obtain the total memory usage. You can specify **pid** to obtain the corresponding memory usage.

hidumper --mem pid

**Reference**

[hidebug.getNativeHeapFreeSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hidebug#hidebuggetnativeheapfreesize)

[hidebug.getNativeHeapAllocatedSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hidebug#hidebuggetnativeheapallocatedsize)

[hidumper](<https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hidumper >)
