# How can I create a thread?

-   Use Worker to create threads in ArkTS. Independent from the main thread, the worker thread cannot directly operate the UI. A maximum of 64 worker threads can be created.
-   Use TaskPool to create thread tasks in ArkTS.
-   With the NAPI mechanism, create threads using the standard thread APIs in C code.
