# Does the RCP request have a data size limit?

By default, the maximum data volume in the [response](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section156381815599) of an RCP request is **50 MB**. If the data volume exceeds the limit, you are advised to receive the data in streaming mode using [onDataReceive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section9264115918536) of [HttpEventsHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section87603011401).

**Reference**

[response](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section156381815599)

[HttpEventsHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section87603011401)

[onDataReceive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section9264115918536)
