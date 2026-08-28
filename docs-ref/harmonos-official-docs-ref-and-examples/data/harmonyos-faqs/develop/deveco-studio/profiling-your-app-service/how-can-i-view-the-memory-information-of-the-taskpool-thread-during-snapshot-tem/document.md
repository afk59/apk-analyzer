# How can I view the memory information of the taskpool thread during Snapshot template recording?

**Symptom**

When the Snapshot template is recorded, the memory information of the taskpool thread cannot be viewed.

**Possible Causes**

The Snapshot template supports only the dump of the VM heap memory of the main thread.

**Solution**

You can run the **hidumper --mem-jsheap ${pid} -T ${tid}** command to obtain the VM heap memory of the specified JS thread in the specified process. After the file is generated, import the file to Profiler for viewing. For details, see [Querying VM Heap Memory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hidumper#querying-vm-heap-memory).
