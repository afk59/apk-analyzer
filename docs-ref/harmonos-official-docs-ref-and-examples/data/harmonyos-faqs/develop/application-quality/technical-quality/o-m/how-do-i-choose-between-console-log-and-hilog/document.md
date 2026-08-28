# How do I choose between console.log and HiLog?

-   The console.log encapsulates the HiLog system with the default parameter configuration, in which the service domain is **A0c0d0**, the log tag is **JSApp**, and the log level is **info**.
-   HiLog contains four parts: service domain, log tag, log level, and log content, which you can customize.
-   The console is mainly used in the application development and debugging phase.
-   You are advised to use HiLog, which classifies and processes logs in a unified manner. If you use console.log to print logs, it is inconvenient to locate logs.

**Reference**

[Hilog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-hilog)
