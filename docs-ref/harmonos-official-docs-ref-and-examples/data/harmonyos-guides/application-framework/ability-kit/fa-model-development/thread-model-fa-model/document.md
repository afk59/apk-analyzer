# Thread Model (FA Model)

There are three types of threads in the [FA model](../../ability-kit-terminology/document.md#fa-model):

-   Main thread:
    
    Manages other threads.
    
-   Ability thread:
    
    -   One ability thread for each ability.
    -   Distributes input events.
    -   Draws the UI.
    -   Invokes application code callbacks (event processing and lifecycle callbacks).
    -   Receives messages sent by the worker thread.
-   Worker thread:
    
    Performs time-consuming operations.
    

Based on the thread model, different services run on different threads. Service interaction requires inter-thread communication. Threads can communicate with each other in [Emitter](../../../../system/basic-functions/basic-services-kit/process-and-thread-communication/using-emitter-for-inter-thread-communication/document.md) or [Worker](../../../arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md) mode. Emitter is mainly used for event synchronization between threads, and Worker is mainly used to execute time-consuming tasks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/hEDR1TXiTwyeyZVmyrA5iQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061918Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51BEA0A25B9B9172CA5903FDA34363A1EB4D7B72C1C66BAF8CB7FD08AE079986)

The FA model provides an independent thread for each ability. Emitter is mainly used for event synchronization within the ability thread, between a pair of ability threads, or between the ability thread and worker thread.
