# Is a synchronous Hash.hash API available?

**Answer**

[@ohos.file.hash](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-hash) provides the file hash processing capability.

Currently, only the asynchronous [Hash.hash](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-hash#hashhash) method is available. To implement the synchronous logic, call the **Hash.hash** method in a callback.
