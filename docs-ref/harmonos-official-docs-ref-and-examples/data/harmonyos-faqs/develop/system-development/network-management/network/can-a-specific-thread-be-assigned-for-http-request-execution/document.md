# Can a specific thread be assigned for HTTP request execution?

**Question**

Can a specific thread be assigned to execute the HTTP request initiated by a third-party application?

**Answer**

Each time an application sends a request, the underlying system obtains a thread from the thread pool to execute the request. The thread execution process is controlled by the underlying system. Third-party applications can obtain data throughout the execution process through event listening. They can control the creation and destruction of HTTP requests, but not the execution process.

**Reference**

[@ohos.net.http (Data Request)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-http)
