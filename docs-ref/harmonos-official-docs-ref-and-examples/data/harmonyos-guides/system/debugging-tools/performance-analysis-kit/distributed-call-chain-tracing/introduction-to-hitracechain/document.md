# Introduction to HiTraceChain

#### Overview

HiTraceChain is a lightweight implementation of the distributed call chain tracing. It allows applications to trace cross-thread, cross-process, and cross-device service calls. With HiTraceChain, a unique ID is generated for a service process, passed throughout the service process, and associated with various output information (including HiTraceMeter logging, application events, and HiLog logs). During debugging and fault locating, you can use the unique **chainId** to quickly correlate various information related to the service process. HiTraceChain provides APIs to implement call chain tracing throughout a service process. This can help you quickly obtain the run log for the call chain of a service process and locate faults across devices, processes, and threads.

#### Basic Concepts

**HiTraceId**: tracing ID provided by HiTraceChain, which uniquely identifies the call chain of a service process.

**chainId**: tracing chain ID, which is a part of **HiTraceId** and uniquely identifies the service process that is being traced.

**spanId**: span ID, which is a part of **HiTraceId** and uniquely identifies a specific task of the service process in a service. Different span IDs can be created for distinguishing tasks. The default value is **0**. When an API is called to create a **spanId**, or **HiTraceId** is automatically passed, a new **spanId** is generated.

**parentSpanId**: parent span ID, which is a part of **HiTraceId** and identifies the parent task of the current task. Different parent span IDs can be used to display the hierarchical relationship between tasks. The default value is **0**. A new **spanId** is created by assigning the current **spanId** to **parentSpanId**.

#### Implementation Principles

1.  **Generate a HiTraceId**: After HiTraceChain tracing is enabled, a globally unique trace ID **HiTraceId** is generated in the Thread Local Storage (TLS) of the calling thread.
    
2.  **Obtain the HiTraceId**: The native layer directly obtains **HiTraceId** from the TLS, and the ArkTS layer obtains **HiTraceId** from the TLS of the native layer through the Node-API.
    
3.  **Pass the HiTraceId**: During the service process, you can obtain the **HiTraceId** from the TLS of the current thread, pass it between different threads (such as **thread1** and **thread2**), processes (such as **APP1** and **APP2**), and devices (such as **Device1** and **Device2**), and set the **HiTraceId** in the TLS of other threads to ensure that all related threads can access the unique **HiTraceId** in the same service process.
    
4.  **Record information**: For service processes that enable HiTraceChain, the **HiTraceId** is included in the output information (such as HiTraceMeter logs, application events, and HiLog logs). You can correlate the information with **HiTraceId** to enable cross-device call-chain tracing.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/qr7VYTvoSWajDDgHjAsXQA/en-us_image_0000002568764845.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062029Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C1AC035F63FD3468226837A35BF444DE10F53894B78CFD17473F7388CDD9A08)
    

#### Constraints

You can set [HiTraceFlag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hitracechain#hitraceflag) to enable asynchronous call tracing. **HiTraceId** can be automatically transferred in the automatic transfer mechanism of **HiTraceChain**.

The following table lists some common mechanisms that support and do not support HiTraceChain automatic transfer. If it is not supported, **HiTraceId** cannot be passed to the created asynchronous tasks, threads, or processes. As a result, the HiTraceChain tracing is interrupted. In this case, you need to manually pass and set **HiTraceId** to implement complete tracing.

| Scenario | Asynchronous Task | Cross-thread | Cross-process | Cross-device |
| :-- | :-- | :-- | :-- | :-- |
| Mechanism supporting HiTraceChain automatic transfer | 
[async/await](../../../../../application-framework/arkts/arkts-concurrency/asynchronous-concurrency-promise-and-async-await/document.md#asyncawait)

[Promise](../../../../../application-framework/arkts/arkts-concurrency/asynchronous-concurrency-promise-and-async-await/document.md#promise)

 | 

[HiAppEvent](../../event-subscription/introduction-to-hiappevent/document.md)

[napi\_async\_work](../../../../../ndk-development/code-development/using-node-api/typical-node-api-use-cases/asynchronous-task-development-using-node-api/document.md)

[FFRT](../../../../basic-functions/function-flow-runtime-kit/about-this-kit/document.md)

 | [IPC](../../../../../application-framework/ipc-kit/about-this-kit/document.md) | [RPC](../../../../../application-framework/ipc-kit/about-this-kit/document.md) |
| Mechanism not supporting HiTraceChain automatic transfer | Macro tasks and their asynchronous tasks (such as [setTimeout](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-timer#settimeout) and [setInterval](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-timer#setinterval)) | 

[TaskPool](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/taskpool/document.md)

[Worker](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md)

Threads created using **std::thread**, **pthread\_create**, and **std::async** of the C++ standard library.

 | 

[Socket](../../../../network/network-kit/network-access/using-socket-for-network-access/document.md)

[Ashmem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#ashmem8)

 | \- |
