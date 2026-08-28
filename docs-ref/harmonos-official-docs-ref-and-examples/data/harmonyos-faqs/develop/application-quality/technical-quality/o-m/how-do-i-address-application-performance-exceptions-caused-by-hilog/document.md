# How do I address application performance exceptions caused by HiLog?

If HiLog is found to cause application performance exceptions, the possible causes are as follows:

**Cause 1**

Logs are printed cyclically, causing the process to detect that the time taken for log printing has increased.

**Solution**

Check whether logs are printed cyclically. If yes, delete the logs that are printed cyclically.

**Cause 2**

The initialization of log printing parameters takes a long time.

For example, the following code for API input parameters to call the function exists: **hilog.debug(0xd010, 'testTag', 'map info: %{public}s', mapToJson(this.paramsMap))**. In this code, **mapToJson(this.paramsMap)** is first called to obtain the log parameter string, which may involve time-consuming operations and increase the time taken by the **hilog.debug** API.

**Solution**

If the initialization function is confirmed to be time-consuming, you can use **hilog.isLoggable** to check whether the current printing meets the log level requirements before log printing. For example:

if (hilog.isLoggable(0xd010, 'testTag', hilog.LogLevel.DEBUG)) {
  hilog.debug(0xd010, 'testTag', 'map info: %{public}s', mapToJson(this.paramsMap))
}

**Cause 3**

The callback function passed by the **OH\_LOG\_SetCallback** API involves time-consuming operations, causing the log printing API to take a longer time.

**Solution**

Optimize the implementation of the callback function passed by the **OH\_LOG\_SetCallback** API to resolve the time-consuming issue.
