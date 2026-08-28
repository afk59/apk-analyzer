# How Do I Determine Whether Scanning is Canceled on the Default Scanning UI?

**Problem**

How do I implement the logic to determine whether scanning has been canceled on the default scanning UI?

**Solution**

If the default scanning UI is opened but scanning is directly canceled, you can determine whether scanning is canceled based on the [1000500002](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-error-code#section158201210912) error returned in the callback and then implement relevant logic.
