# Thread Model (Stage Model)

A thread is the basic unit for the operating system to perform computing and scheduling. It is an execution flow within a [process](../process-model/document.md) and shares the resources of the process. A process can contain multiple threads.

#### Thread Type

There are three types of threads in the [stage model](../../ability-kit-terminology/document.md#stage-model):

-   Main thread
    -   Draws the UI.
    -   Manages the [ArkTS engine](../../../arkts/arkts-runtime/overview-of-arkts-runtime/document.md) instance of the main thread so that multiple UIAbility components can run on it.
    -   Manages [ArkTS engine](../../../arkts/arkts-runtime/overview-of-arkts-runtime/document.md) instances of other threads, for example, using **TaskPool** to create or cancel tasks, and starting and terminating **Worker** threads.
    -   Distributes interaction events.
    -   Processes application code callbacks (event processing and lifecycle management).
    -   Receives messages sent by the **TaskPool** and **Worker** threads.
-   [TaskPool Thread](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-taskpool)
    -   Used for time-consuming operations and provides APIs for setting the scheduling priority and load balancing. It is recommended.
-   [Worker Thread](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-worker)
    -   Used for time-consuming operations and supports inter-thread communication.
        
        For details about the operation mechanism, communication method, and usage of **TaskPool** and **Worker**, see [Comparison Between TaskPool and Worker](../../../arkts/arkts-concurrency/multithreaded-concurrency/comparison-between-taskpool-and-worker/document.md).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/SMIYdCanSzePM7XpBhKrAw/en-us_image_0000002568684081.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061917Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8613E5C54EEEE4C61D07D87F68A31B56F4E8E301AE985C39CC89AFA43AD25EFC)
        

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Xi4TDFNBSTixXoaE-AjpJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061917Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3646764CC1FE4474A702AE05348600827DE9F5905EE61D9437C295DD8799EC3)

-   **TaskPool** manages the number of threads that can be created and their lifecycle. However, you need to maintain the lifecycle of [Worker](../../../arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md) threads.
-   Multiple components can exist in the same thread. For example, both UIAbility and UI components exist in the main thread. In the stage model, [EventHub](#using-eventhub-for-intra-thread-communication) is used for data communication.
-   To view thread information about an application process, run the **hdc shell** command to enter the shell CLI of the device, and then run the **ps -p <pid> -T command**, where <pid> indicates the [process ID](../process-model/document.md) of the application.

#### Using EventHub for Intra-Thread Communication

[EventHub](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-eventhub) provides APIs for sending and processing events in threads, including subscribing to, unsubscribing from, and triggering events. [Using EventHub for Data Synchronization](../stage-model-application-components/uiability-component/data-synchronization-between-uiability-and-ui-page/document.md#using-eventhub-for-data-synchronization) describes the development procedure by using data synchronization between the UIAbility component and the UI as an example.
