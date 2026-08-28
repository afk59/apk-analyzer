# How do I obtain a wakelock to prevent system sleep?

Call the **runningLock.create** API to create a **RunningLock** object. Call the **hold** API to set the duration for locking and holding the **RunningLock** object. During this period, the system does not sleep. After the duration expires, if no other **RunningLock** object is set, the **RunningLock** object is automatically released, and the system sleeps.

**Reference**

[@ohos.runningLock (RunningLock)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-runninglock)
