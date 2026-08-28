# Using HiLog (C/C++)

During application development, you can log from your application's key code. Through logs, you can find out how the application is running. For example, the logs can tell you whether the application is running properly, and whether the code execution sequence and logic branch are correct.

HiLog is a subsystem that provides logging for the system framework, services, and applications to record information on user operations and system running status.

#### Available APIs

HiLog defines five log levels (DEBUG, INFO, WARN, ERROR, and FATAL) and provides APIs to output logs of different levels. For details about the APIs, see [log.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-log-h).

| API/Macro | Description |
| :-- | :-- |
| bool OH\_LOG\_IsLoggable(unsigned int domain, const char \*tag, LogLevel level) | 
Checks whether logs of the specified service domain, tag, and level can be printed.

This API returns **true** if the specified logs can be printed and returns **false** otherwise.

 |
| int OH\_LOG\_Print(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, ...) | 

Outputs logs of the specified domain, tag, and log level, with the variable parameters in the **printf** format.

If the return value is greater than or equal to 0, the operation is successful. Otherwise, the operation fails.

 |
| int OH\_LOG\_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*message) | 

Outputs log strings of the specified domain, tag, and log level.

If the return value is greater than or equal to 0, the operation is successful. Otherwise, the operation fails.

Note: This API is supported since API version 18.

 |
| int OH\_LOG\_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char \*tag, size\_t tagLen, const char \*message, size\_t messageLen) | 

Outputs the log string of the specified domain, tag, and log level, with the tag and string length specified.

If the return value is greater than or equal to 0, the operation is successful. Otherwise, the operation fails.

Note: This API is supported since API version 18.

 |
| int OH\_LOG\_VPrint(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, va\_list ap) | 

Used in the same way as **OH\_LOG\_Print**, but the parameter list is **va\_list**.

Note: This API is supported since API version 18.

 |
| #define OH\_LOG\_DEBUG(type, ...) ((void)OH\_LOG\_Print((type), LOG\_DEBUG, LOG\_DOMAIN, LOG\_TAG, **VA\_ARGS**)) | Outputs DEBUG logs. This is a function-like macro. |
| #define OH\_LOG\_INFO(type, ...) ((void)OH\_LOG\_Print((type), LOG\_INFO, LOG\_DOMAIN, LOG\_TAG, **VA\_ARGS**)) | Outputs INFO logs. This is a function-like macro. |
| #define OH\_LOG\_WARN(type, ...) ((void)OH\_LOG\_Print((type), LOG\_WARN, LOG\_DOMAIN, LOG\_TAG, **VA\_ARGS**)) | Outputs WARN logs. This is a function-like macro. |
| #define OH\_LOG\_ERROR(type, ...) ((void)OH\_LOG\_Print((type), LOG\_ERROR, LOG\_DOMAIN, LOG\_TAG, **VA\_ARGS**)) | Outputs ERROR logs. This is a function-like macro. |
| #define OH\_LOG\_FATAL(type, ...) ((void)OH\_LOG\_Print((type), LOG\_FATAL, LOG\_DOMAIN, LOG\_TAG, **VA\_ARGS**)) | Outputs FATAL logs. This is a function-like macro. |
| void OH\_LOG\_SetCallback(LogCallback callback) | Registers a callback to return the HiLog logs for the process. When the **OH\_LOG\_IsLoggable** API returns true, the callback can obtain the log. |
| void OH\_LOG\_SetMinLogLevel(LogLevel level) | 

Sets the minimum log level.

Note: This API is supported since API version 15.

 |
| void OH\_LOG\_SetLogLevel(LogLevel level, PreferStrategy prefer) | 

Sets the minimum log level of the current application process. You can configure different preference strategies.

Note: This API is supported since API version 21.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_X_bFLdwQaC1Vf7kTER6-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC56164D1553E4C8485FE9779A8512FACDFF9B5329197BBD92A6716950BA837F)

The HiLog APIs are not signal-safe functions. Do not call the HiLog APIs in signal processing functions.

If the set log level is lower than the [global log level](../../command-line-tools/hilog/document.md#displaying-and-setting-log-levels), the **OH\_LOG\_SetMinLogLevel()** setting does not take effect.

In the debug applications, the **OH\_LOG\_SetMinLogLevel()** and **OH\_LOG\_SetLogLevel()** functions do not take effect.

## Parameters

-   **domain**: service domain of logs. The value range is 0x0000 to 0xFFFF. You can define the value as required.
    
-   **tag**: log identifier. It can be any string. You are advised to use this parameter to identify the class or service behavior of a method call. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur.
    
-   **level**: log level. For details, see [LogLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-log-h#loglevel).
    
-   **prefer**: preference strategy. For details, see [PreferStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-log-h#preferstrategy).
    
-   **fmt**: format of the log to output. The value is a string in the "%{private flag}specifier" format.
    
    | Private Flag | Description |
    | :-- | :-- |
    | private | The output is **<private>**, which indicates that the log information is invisible. |
    | public | The log information is displayed. |
    | Not specified | The default value **<private>** is used. |
    
    | Specifier | Description | Example |
    | :-- | :-- | :-- |
    | d/i | The decimal integer type can be printed. | 123 |
    | s | The char\* type can be printed. | "this is a hilog" |
    
    Multiple parameters can be set in the format string. For example, if the format string is **"%s World"**, **"%s"** is a variable parameter identifier indicating that the parameter type is string. The specific value is defined in **args**. For the usage of format specifiers, see [printf](https://man7.org/linux/man-pages/man3/printf.3.html).
    
    The debug application does not have a privacy control mechanism. Parameters can be displayed in plaintext when any of the preceding private flags is used to print logs.
    
-   **args**: parameters of the types specified by **specifier** in **format**. This parameter can be left blank. The number and type of parameters must match **specifier**.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ddH2da5lRiiEi3RqMitpPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36961CB434BD6814E1381368F83AF043DEE4B8A8DE9E51E09E42DF261344D4C4)

-   The domains, tags, and levels specified in **OH\_LOG\_IsLoggable()** and **OH\_LOG\_Print()** must be the same.
    
-   **OH\_LOG\_IsLoggable()** returns **true** if the specified logs can be printed; returns **false** otherwise.
    
    For debug applications, all log levels can be printed.
    
    For release applications, logs are printed only if the log level is not lower than the global log level.
    
    During debugging, you can change the log level. For details, see [Displaying and Setting Log Levels](../../command-line-tools/hilog/document.md#displaying-and-setting-log-levels).
    

#### Constraints

The maximum size of a log file is 4096 bytes. Excess content will be discarded.

#### How to Develop

1.  Add the link of **libhilog\_ndk.z.so** to **CMakeLists.txt**.
    
    target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
    
2.  Include the **hilog** header file in the source file, and define the **domain** and **tag** macros.
    
    #include "hilog/log.h"
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x3200 // Global domain, which identifies the service domain.
    #define LOG\_TAG "MY\_TAG"   // Global tag macro, which identifies the module log tag.
    
3.  Print logs.
    
    OH\_LOG\_INFO(LOG\_APP, "Failed to visit path.");
    // Set the minimum log level to Warn.
    OH\_LOG\_SetMinLogLevel(LOG\_WARN);
    OH\_LOG\_INFO(LOG\_APP, "this is an info level log");
    OH\_LOG\_ERROR(LOG\_APP, "this is an error level log");
    // Set the minimum log level to the PREFER\_OPEN\_LOG strategy so that logs whose levels are not lower than INFO can be printed.
    OH\_LOG\_SetLogLevel(LOG\_WARN, PREFER\_OPEN\_LOG);
    OH\_LOG\_INFO(LOG\_APP, "this is an another info level log");
    OH\_LOG\_ERROR(LOG\_APP, "this is an another error level log");
    
4.  The output is as follows:
    

   01-02 08:39:38.915   9012-9012     A03200/com.example.hilogDemo/MY\_TAG  com.example.hilogDemo  I     Failed to visit path.
   01-02 08:39:38.915   9012-9012     A03200/com.example.hilogDemo/MY\_TAG  com.example.hilogDemo  E     this is an error level log
   01-02 08:39:38.915   9012-9012     A03200/com.example.hilogDemo/MY\_TAG  com.example.hilogDemo  I     this is an another info level log
   01-02 08:39:38.915   9012-9012     A03200/com.example.hilogDemo/MY\_TAG  com.example.hilogDemo  E     this is an another error level log

## Registering a Log Callback

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/29juYEH9S5SbJ9d6YWAW2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56A86D1BE26FA7671D16029B285172DDF0624D9E456BA9683C2D348A8A46B035)

1.  Do not call the HiLog API recursively in the callback. Otherwise, a cyclic call issue occurs.
    
2.  Register the callback only once for a process. If the callback is registered multiple times, the last registered one takes effect.
    

#include "hilog/log.h"

// Customize a callback for processing logs.
void MyHiLog(const LogType type, const LogLevel level, const unsigned int domain, const char \*tag, const char \*msg)
{
    // Define how to handle your logs, such as redirect/filter.
    // Note: Do not call the HiLog API recursively in the callback function. Otherwise, a cyclic call issue occurs.
}

static void Test(void)
{
   // 1. Register a callback.
   OH\_LOG\_SetCallback(MyHiLog);
    
   // 2. Call the HiLog API to print logs. Logs are output to HiLog and returned to MyHiLog() through the registered callback. Then, MyHiLog() is called to process the logs.
   OH\_LOG\_INFO(LOG\_APP, "hello world");
}
