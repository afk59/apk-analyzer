# How do I obtain the context in a utility class?

The context cannot be directly obtained from a utility class. You can obtain the context from an EntryAbility, save it to an AppStorage, and then use the AppStorage to obtain the context from the utility class.

**Reference**

[AppStorage: Storing Application-wide UI State](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-appstorage)
