# Overview of ArkTS Inter-Thread Communication

Inter-thread communication involves the exchange of data between concurrent threads. Given that ArkTS is compatible with TS/JS, its runtime is implemented using the actor model with memory isolation, similar to other JS engines.

The behavior of inter-thread communication in ArkTS varies depending on the type of data object involved. For instance, regular JS objects, ArrayBuffer objects, and SharedArrayBuffer objects each exhibit different behaviors, including serialization and deserialization, data transfer, and data sharing.

Taking JS objects as an example, inter-thread communication uses the standard Structured Clone algorithm for serialization and deserialization. This process involves converting JS objects into engine-independent data (such as strings or memory blocks) and then restoring them into new objects with the same content in another concurrent task. This typically requires deep copying, which can be less efficient. In addition to standard JS serialization and deserialization, ArkTS supports the transfer of native JS object and the sharing of [Sendable objects](../inter-thread-communication-objects/sendable-object/overview-of-sendable-objects/document.md).

Currently, ArkTS provides two concurrency capabilities for inter-thread communication: TaskPool and Worker.

-   Worker is the standard API for cross-thread communication in the actor model. Its usage patterns are similar to those of Web Worker or Node.js Worker.
    
-   TaskPool provides a more powerful and user-friendly API for concurrent programming. The behavior of object passing across concurrent tasks in TaskPool is consistent with that of Worker, utilizing the standard Structured Clone algorithm. The time required for concurrent communication increases with the size of the objects involved.
    

Leveraging the TaskPool and Worker concurrency APIs, ArkTS supports a variety of inter-thread communication capabilities to satisfy different development needs in inter-thread communication scenarios. For example, [independent time-consuming tasks](../communication-between-threads/using-taskpool-for-independent-time-consuming-tasks/document.md), [multiple time-consuming tasks](../communication-between-threads/using-taskpool-for-multiple-time-consuming-tasks/document.md), [communication between the TaskPool task and host thread](../communication-between-threads/communication-between-the-taskpool-task-and-host-thread/document.md), [real-time communication between the Worker thread and host thread](../communication-between-threads/real-time-communication-between-the-worker-thread-and-host-thread/document.md), and [synchronous calls to host thread interfaces from Worker](../communication-between-threads/synchronous-calls-to-host-thread-interfaces-from-worker/document.md). In addition, ArkTS supports cross-thread calls to ArkTS APIs from C++ threads, based on the mechanisms provided by [Node-API](../../../../../ndk-development/code-development/using-node-api/node-api-overview/document.md).

Figure 1 Serialization and deserialization principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/BEQLkN1xSW2zikpDcNzw1A/en-us_image_0000002537924318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061923Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=201BFE2503E7F5C91FB61BBFEC4BB0787D0D4B9966A255F1B8437326E5605535)
