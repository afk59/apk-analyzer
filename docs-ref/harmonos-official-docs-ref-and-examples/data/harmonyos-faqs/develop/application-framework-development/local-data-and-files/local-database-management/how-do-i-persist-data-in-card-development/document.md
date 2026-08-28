# How do I persist data in card development?

HarmonyOS provides three data persistence solutions: **Preferences** (for lightweight key-value storage), **KV-Store** (for distributed data synchronization), and **RelationalStore** (for SQLite relational data management).

-   **Preferences**: After data is stored in the **Preferences** instance, the **flush()** method is used to persist the data. You are advised to call this method at key points (such as **onBackground**) in the application lifecycle to ensure data security.
-   **KV-Store**: **put()** is called to insert data into the KV Store. The **put()** method of the **KV-Store** supports synchronous and asynchronous write modes, which are applicable to data synchronization between devices. The distributed feature requires the caller to handle exceptions such as **CONFLICT\_FOUND**.
-   **RelationalStore**: After an **RdbStore** instance is obtained, call **insert()** to insert data.

**Reference**

[Persisting User Preferences (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-preferences)

[Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store)

[Persisting RDB Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-rdb-store)
