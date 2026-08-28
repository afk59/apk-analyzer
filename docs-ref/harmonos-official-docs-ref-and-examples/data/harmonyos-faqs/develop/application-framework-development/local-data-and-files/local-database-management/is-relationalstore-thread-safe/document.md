# Is relationalStore thread-safe?

**relationalStore** is thread-safe. However, worker threads run in an independent context and are isolated from the **relationalStore** instance of the main thread. Therefore, worker threads are not supported. ArkTS provides two multithreading solutions, TaskPool and Worker, both of which are implemented on the actor model. This model transfers data through events, which eliminates the need for handling complex issues such as lock contention, ensuring thread safety and a relatively high level of concurrency.

[@ohos.data.relationalStore (RDB Store)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-relationalstore)
