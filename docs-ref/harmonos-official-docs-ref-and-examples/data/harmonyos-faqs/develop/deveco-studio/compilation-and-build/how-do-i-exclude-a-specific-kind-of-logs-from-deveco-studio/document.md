# How do I exclude a specific kind of logs from DevEco Studio?

Use **^(?!.\*xxx).\*$** regular expression to search logs. This regular expression can be applied to full logs, including **domain** and **tag**.

**Reference**

[Filtering Logs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-setup-hilog#section1022292292216)
