# How do I analyze the CPU usage of an application online?

When a freeze event or frame loss occurs in an application, or the running status of an application needs to be evaluated, you can use the **HiDebug** API to obtain resource data and check the running status of the current application.

[@ohos.hidebug](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hidebug) is a module that allows you to obtain the memory usage of an application, including the static heap memory (native heap) and proportional set size (PSS) occupied by the application process. It also allows you to export VM memory slices and collect VM CPU profiling data.
