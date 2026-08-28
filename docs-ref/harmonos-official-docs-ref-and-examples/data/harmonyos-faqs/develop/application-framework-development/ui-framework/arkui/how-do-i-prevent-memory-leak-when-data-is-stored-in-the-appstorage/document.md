# How do I prevent memory leak when data is stored in the AppStorage?

**Question**

When storing data in **AppStorage** within **EntryAbility**, will there be a memory leak if data is read when it needs to be accessed?

**Solution**

**AppStorage** is a singleton created when the application is launching. It provides central storage for application state data that is accessible at the application level. AppStorage maintains all properties throughout the application lifecycle. You can manage the lifecycle of variables in AppStorage. If variables are not in use, you can delete them using the [delete](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-state-management#delete10) API.
