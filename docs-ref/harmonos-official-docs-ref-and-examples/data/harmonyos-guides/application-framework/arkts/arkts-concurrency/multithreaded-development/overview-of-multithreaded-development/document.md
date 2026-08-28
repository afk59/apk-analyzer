# Overview of Multithreaded Development

In ArkTS application development, different service scenarios require different concurrency capabilities and task types.

There are three types of concurrent tasks in common service scenarios:

[Time-consuming tasks](../concurrency-in-time-consuming-tasks/overview-of-concurrency-in-time-consuming-tasks/document.md): These involve significant computation or multiple I/O operations and take a long time to execute.

[Continuous tasks](../concurrency-in-continuous-tasks/overview-of-concurrency-in-continuous-tasks/document.md): These include tasks like listening or periodically collecting data that need to run continuously over extended periods.

[Resident tasks](../concurrency-in-resident-tasks/overview-of-concurrency-in-resident-tasks/document.md): These are bound to the lifecycle of the main thread or closely integrated with it.

Different task types can be further classified. For example, time-consuming tasks can be CPU intensive, I/O intensive, or synchronous, each corresponding to different service scenarios. TaskPool and Worker both support multithreaded concurrency. You can select the concurrency capability as required. For details, see [Use Case Comparison](../../multithreaded-concurrency/comparison-between-taskpool-and-worker/document.md#use-case-comparison).

The following sections will list common scenarios and examples in multithreaded development.
