# Can a specific network be specified for sending HTTP requests?

**Question**

How do I specify whether to use Wi-Fi or cellular data for sending network requests?

**Answer**

You can use [connection.setAppNet()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectionsetappnet9-1) to bind an application to a specific network. In this case, all HTTP requests initiated by the application will be sent over the specified network. If you want to use another network, call [connection.setAppNet()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectionsetappnet9-1) to bind the application to that network.

**Reference**

[@ohos.net.connection (Network Connection Management)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection)
