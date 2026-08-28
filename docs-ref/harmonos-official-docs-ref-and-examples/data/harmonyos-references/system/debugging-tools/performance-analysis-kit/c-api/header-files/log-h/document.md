# log.h

#### Overview

Defines the logging functions of the HiLog module. Before outputting logs, you must define the service domain, and log tag, use the API with the specified log type and level, and specify the privacy identifier.

**Service domain**: service domain of logs. You can define the value as required. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed.

**Log tag**: a string used to identify the class, file, or service behavior.

**Log level**: DEBUG, INFO, WARN, ERROR, or FATAL.

**Parameter format**: printf format string, which starts with a % character, including a parameter type identifier and a variable parameter.

**Privacy identifier**: **{public}** or **{private}** added between the % character and the parameter type identifier in each parameter. **Note**: If no privacy identifier is added, the parameter is considered to be **private**.

**File to include**: <hilog/log.h>

**Library**: libhilog\_ndk.z.so

**System capability**: SystemCapability.HiviewDFX.HiLog

**Since**: 8

**Related module**: [HiLog](../../modules/hilog/document.md)

#### Summary

#### \[h2\]Enum

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [LogType](#logtype) | LogType | 
Enumerates the log types. You can use this function to specify the type of output logs. Currently, only **LOG\_APP** is available.

 |
| [LogLevel](#loglevel) | LogLevel | 

Enumerates the log levels. You are advised to select log levels based on their respective use cases. Log levels:

**DEBUG**: provides more detailed process information than INFO logs to help developers analyze service processes and locate faults. DEBUG logs are not recorded in official versions by default. They are available in debug versions or in official versions with the debug function enabled.

**INFO**: indicates the key service process nodes and exceptions (for example, no network signal or login failure) that occur during service running. These logs should be recorded by the dominant module in the service to avoid repeated logging conducted by multiple invoked modules or low-level functions.

**WARN**: indicates a severe, unexpected fault that has little impact on users and can be rectified by the programs themselves or through simple operations.

**ERROR**: indicates a program or functional error that affects the normal running or use of the functionality and can be fixed at a high cost, for example, by resetting data.

**FATAL**: indicates that a program or functionality is about to crash and the fault cannot be rectified.

 |
| [PreferStrategy](#preferstrategy) | PreferStrategy | Enumerates the preference strategies. This enum is used in [OH\_LOG\_SetLogLevel](#oh_log_setloglevel). The minimum log level that takes effect varies according to the strategy. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| OH\_LOG\_DEBUG(type, ...) ((void)OH\_LOG\_Print((type), LOG\_DEBUG, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | 
Indicates DEBUG logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

 |
| OH\_LOG\_INFO(type, ...) ((void)OH\_LOG\_Print((type), LOG\_INFO, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | 

Indicates INFO logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

 |
| OH\_LOG\_WARN(type, ...) ((void)OH\_LOG\_Print((type), LOG\_WARN, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | 

Indicates WARN logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

 |
| OH\_LOG\_ERROR(type, ...) ((void)OH\_LOG\_Print((type), LOG\_ERROR, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | 

Indicates ERROR logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

 |
| OH\_LOG\_FATAL(type, ...) ((void)OH\_LOG\_Print((type), LOG\_FATAL, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | 

Indicates FATAL logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

 |
| LOG\_DOMAIN | 

Specifies the service domain of the output log. The default value is **0**. The value range is 0x0 to 0xFFFF. If the value of **domainID** exceeds the range, the log cannot be printed.

**Since**: 8

 |
| LOG\_TAG | 

Identifies the class or service behavior where the log is called. The value is a string constant, which is **NULL** by default. The maximum length is 31 bytes. If the length exceeds 31 bytes, the log will be truncated. The value must be a non-null string. Otherwise, the log cannot be printed. Chinese characters are not recommended, because they may cause garbled characters or alignment issues.

**Since**: 8

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [int OH\_LOG\_Print(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, ...)](#oh_log_print) | \- | Outputs logs of the specified **type**, **level**, **domain**, **tag**, and variables determined by the format specifier and privacy identifier in the printf format. |
| [int OH\_LOG\_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*message)](#oh_log_printmsg) | \- | Outputs constant log strings of the specified **type**, **level**, **domain**, and **tag**. |
| [int OH\_LOG\_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char \*tag, size\_t tagLen, const char \*message, size\_t messageLen)](#oh_log_printmsgbylen) | \- | Outputs log constant strings of the specified **domain**, **tag**, and **level**. The tag and string length must be specified. Unlike **OH\_LOG\_PrintMsg**, this API allows strings without terminators. |
| [int OH\_LOG\_VPrint(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, va\_list ap)](#oh_log_vprint) | \- | Outputs logs of the specified **type**, **level**, **domain**, **tag**, and variables determined by the format specifier and privacy identifier in the printf format. The variables are of the **va\_list** type. |
| [bool OH\_LOG\_IsLoggable(unsigned int domain, const char \*tag, LogLevel level)](#oh_log_isloggable) | \- | Checks whether logs of the specified service domain, tag, and level can be printed. |
| [typedef void (\*LogCallback)(const LogType type, const LogLevel level, const unsigned int domain, const char \*tag, const char \*msg)](#logcallback) | LogCallback | Customizes the processing of HiLog logs in the callback. |
| [void OH\_LOG\_SetCallback(LogCallback callback)](#oh_log_setcallback) | \- | 
Registers a callback function. After this function is called, the custom callback can receive all HiLog logs of the current process.

Note that whether this API is called or not, it does not change the default log processing of the current process.

 |
| [void OH\_LOG\_SetMinLogLevel(LogLevel level)](#oh_log_setminloglevel) | \- | Sets the minimum log level. |
| [void OH\_LOG\_SetLogLevel(LogLevel level, PreferStrategy prefer)](#oh_log_setloglevel) | \- | Sets the minimum log level of the current application process. You can configure different preference strategies. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/psxtwjMsQGKz1aPe2ZLrKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062415Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFA47BA740F804A73BBF7906C265C5968CEA3D4393880A032DC59224EAF301C4)

If the set log level is lower than the [global log level](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hilog#displaying-and-setting-log-levels), the **OH\_LOG\_SetMinLogLevel()** setting does not take effect.

In the debug applications, the **OH\_LOG\_SetMinLogLevel()** and **OH\_LOG\_SetLogLevel()** functions do not take effect.

#### Enum Description

#### \[h2\]LogType

enum LogType

**Description**

Enumerates the log types. You can use this function to specify the type of output logs. Currently, only **LOG\_APP** is available.

**Since**: 8

| Enum Item | Description |
| :-- | :-- |
| LOG\_APP = 0 | Application log. |

#### \[h2\]LogLevel

enum LogLevel

**Description**

Enumerates the log levels. You are advised to select log levels based on their respective use cases. Log levels:

**DEBUG**: provides more detailed process information than INFO logs to help developers analyze service processes and locate faults. DEBUG logs are not recorded in official versions by default. They are available in debug versions or in official versions with the debug function enabled.

**INFO**: indicates the key service process nodes and exceptions (for example, no network signal or login failure) that occur during service running. These logs should be recorded by the dominant module in the service to avoid repeated logging conducted by multiple invoked modules or low-level functions.

**WARN**: indicates a severe, unexpected fault that has little impact on users and can be rectified by the programs themselves or through simple operations.

**ERROR**: indicates a program or functional error that affects the normal running or use of the functionality and can be fixed at a high cost, for example, by resetting data.

**FATAL**: indicates that a program or functionality is about to crash and the fault cannot be rectified.

**Since**: 8

| Enum Item | Description |
| :-- | :-- |
| LOG\_DEBUG = 3 | DEBUG level to be used by **OH\_LOG\_DEBUG**. |
| LOG\_INFO = 4 | INFO level to be used by **OH\_LOG\_INFO**. |
| LOG\_WARN = 5 | WARN level to be used by **OH\_LOG\_WARN**. |
| LOG\_ERROR = 6 | ERROR level to be used by **OH\_LOG\_ERROR**. |
| LOG\_FATAL = 7 | FATAL level to be used by **OH\_LOG\_FATAL**. |

#### \[h2\]PreferStrategy

enum PreferStrategy

**Description**

Enumerates the preference strategies. This enum is used in [OH\_LOG\_SetLogLevel](#oh_log_setloglevel). The minimum log level that takes effect varies according to the strategy.

**Since**: 21

| Enum Item | Description |
| :-- | :-- |
| UNSET\_LOGLEVEL = 0 | The setting is cleared. The minimum log level that actually takes effect is the system-controlled minimum log level. |
| PREFER\_CLOSE\_LOG = 1 | The minimum log level that actually takes effect is the larger value of the new log level and the system-controlled minimum log level. |
| PREFER\_OPEN\_LOG = 2 | The minimum log level that actually takes effect is the smaller value of the new log level and the system-controlled minimum log level. |

#### Function Description

#### \[h2\]OH\_LOG\_Print()

int OH\_LOG\_Print(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, ...)

**Description**

Outputs logs of the specified **type**, **level**, **domain**, **tag**, and variables determined by the format specifier and privacy identifier in the printf format.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogType](#logtype) type | Log type. The type for third-party applications is defined by **LOG\_APP**. |
| [LogLevel](#loglevel) level | Log level. The value can be **LOG\_DEBUG**, **LOG\_INFO**, **LOG\_WARN**, **LOG\_ERROR**, and **LOG\_FATAL**. |
| unsigned int domain | Service domain. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed. |
| const char \*tag | Log tag, which is a string used to identify the class, file, or service. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur. |
| const char \*fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| ... | Parameter list corresponding to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
**0** or a larger value if the operation is successful; a value smaller than **0** otherwise.

Possible failure causes: The **LogLevel** passed in is lower than the allowed log level; the **domain** is out of range; the **tag** is a null pointer; the CPU is overloaded; the memory is insufficient; the number of logs on the device is too large.

 |

#### \[h2\]OH\_LOG\_PrintMsg()

int OH\_LOG\_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*message)

**Description**

Outputs constant log strings of the specified **type**, **level**, **domain**, and **tag**.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogType](#logtype) type | Log type. The type for third-party applications is defined by **LOG\_APP**. |
| [LogLevel](#loglevel) level | Log level. The value can be **LOG\_DEBUG**, **LOG\_INFO**, **LOG\_WARN**, **LOG\_ERROR**, and **LOG\_FATAL**. |
| unsigned int domain | Service domain. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed. |
| const char \*tag | Log tag, which is a string used to identify the class, file, or service. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur. |
| const char \*message | Constant log string. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
**0** or a larger value if the operation is successful; a value smaller than **0** otherwise.

Possible failure causes: The **LogLevel** passed in is lower than the allowed log level; the **domain** is out of range; the **tag** is a null pointer; the CPU is overloaded; the memory is insufficient; the number of logs on the device is too large.

 |

#### \[h2\]OH\_LOG\_PrintMsgByLen()

int OH\_LOG\_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char \*tag, size\_t tagLen, const char \*message, size\_t messageLen)

**Description**

Outputs log constant strings of the specified **domain**, **tag**, and **level**. The tag and string length must be specified. Unlike **OH\_LOG\_PrintMsg**, this API allows strings without terminators.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogType](#logtype) type | Log type. The type for third-party applications is defined by **LOG\_APP**. |
| [LogLevel](#loglevel) level | Log level. The value can be **LOG\_DEBUG**, **LOG\_INFO**, **LOG\_WARN**, **LOG\_ERROR**, and **LOG\_FATAL**. |
| unsigned int domain | Service domain. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed. |
| const char \*tag | Log tag, which is a string used to identify the class, file, or service. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur. |
| size\_t tagLen | Length of the tag. |
| const char \*message | Constant log string. |
| size\_t messageLen | Length of the constant string, which is less than 3500 characters. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
**0** or a larger value if the operation is successful; a value smaller than **0** otherwise.

Possible failure causes: The **LogLevel** passed in is lower than the allowed log level; the **domain** is out of range; the **tag** is a null pointer; the CPU is overloaded; the memory is insufficient; the number of logs on the device is too large.

 |

#### \[h2\]OH\_LOG\_VPrint()

int OH\_LOG\_VPrint(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, va\_list ap)

**Description**

Outputs logs of the specified **type**, **level**, **domain**, **tag**, and variables determined by the format specifier and privacy identifier in the printf format. The variables are of the **va\_list** type.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogType](#logtype) type | Log type. The type for third-party applications is defined by **LOG\_APP**. |
| [LogLevel](#loglevel) level | Log level. The value can be **LOG\_DEBUG**, **LOG\_INFO**, **LOG\_WARN**, **LOG\_ERROR**, and **LOG\_FATAL**. |
| unsigned int domain | Service domain. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed. |
| const char \*tag | Log tag, which is a string used to identify the class, file, or service. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur. |
| const char \*fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| va\_list ap | Parameter list of the **va\_list** type that corresponds to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
**0** or a larger value if the operation is successful; a value smaller than **0** otherwise.

Possible failure causes: The **LogLevel** passed in is lower than the allowed log level; the **domain** is out of range; the **tag** is a null pointer; the CPU is overloaded; the memory is insufficient; the number of logs on the device is too large.

 |

#### \[h2\]OH\_LOG\_IsLoggable()

bool OH\_LOG\_IsLoggable(unsigned int domain, const char \*tag, LogLevel level)

**Description**

Checks whether logs of the specified service domain, tag, and level can be printed.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| unsigned int domain | Service domain. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed. |
| const char \*tag | Log tag, which is a string used to identify the class, file, or service. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur. |
| [LogLevel](#loglevel) level | Log level. The value can be **LOG\_DEBUG**, **LOG\_INFO**, **LOG\_WARN**, **LOG\_ERROR**, and **LOG\_FATAL**. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the specified logs can be output; **false** otherwise. |

#### \[h2\]OH\_LOG\_DEBUG()

OH\_LOG\_DEBUG(type, ...)((void)OH\_LOG\_Print((type), LOG\_DEBUG, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_))

**Description**

Indicates DEBUG logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| type | Log type. The third-party application log type is [LOG\_APP](#logtype). |
| fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| ... | Parameter list corresponding to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**See also**

[OH\_LOG\_Print](#oh_log_print)

#### \[h2\]OH\_LOG\_INFO()

OH\_LOG\_INFO(type, ...)((void)OH\_LOG\_Print((type), LOG\_INFO, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_))

**Description**

Indicates INFO logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| type | Log type. The type for third-party applications is defined by **LOG\_APP**. |
| fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| ... | Parameter list corresponding to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**See also**

[OH\_LOG\_Print](#oh_log_print)

#### \[h2\]OH\_LOG\_WARN()

OH\_LOG\_WARN(type, ...)((void)OH\_LOG\_Print((type), LOG\_WARN, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_))

**Description**

Indicates WARN logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| type | Log type. The third-party application log type is [LOG\_APP](#logtype). |
| fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| ... | Parameter list corresponding to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**See also**

[OH\_LOG\_Print](#oh_log_print)

#### \[h2\]OH\_LOG\_ERROR()

OH\_LOG\_ERROR(type, ...)((void)OH\_LOG\_Print((type), LOG\_ERROR, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_))

**Description**

Indicates ERROR logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| type | Log type. The third-party application log type is [LOG\_APP](#logtype). |
| fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| ... | Parameter list corresponding to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**See also**

[OH\_LOG\_Print](#oh_log_print)

#### \[h2\]OH\_LOG\_FATAL()

OH\_LOG\_FATAL(type, ...)((void)OH\_LOG\_Print((type), LOG\_FATAL, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_))

**Description**

Indicates FATAL logs. This is a function-like macro. Before using this macro, define **LOG\_DOMAIN** and **LOG\_TAG** at the beginning of the source file.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| type | Log type. The third-party application log type is [LOG\_APP](#logtype). |
| fmt | Format string, which is an enhancement of a printf format string and supports the privacy identifier. Specifically, **{public}** or **{private}** is added between the % character and the format specifier in each parameter. |
| ... | Parameter list corresponding to the parameter type in the format string. The number and type of parameters must be mapped onto the identifier in the format string. |

**See also**

[OH\_LOG\_Print](#oh_log_print)

#### \[h2\]LogCallback()

typedef void (\*LogCallback)(const LogType type, const LogLevel level, const unsigned int domain, const char \*tag, const char \*msg)

**Description**

Customizes the processing of HiLog logs in the callback.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const LogType](#logtype) type | Log type. The third-party application log type is [LOG\_APP](#logtype). |
| [const LogLevel](#loglevel) level | Log level. The value can be **LOG\_DEBUG**, **LOG\_INFO**, **LOG\_WARN**, **LOG\_ERROR**, and **LOG\_FATAL**. |
| const unsigned int domain | Service domain. Its value is a hexadecimal integer ranging from 0x0 to 0xFFFF. If the value exceeds the range, logs cannot be printed. |
| const char \*tag | Log tag, which is a string used to identify the class, file, or service. A tag can contain a maximum of 31 bytes. If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled characters or alignment problems may occur. |
| const char \*msg | Log content, which is made up of formatted log strings. |

#### \[h2\]OH\_LOG\_SetCallback()

void OH\_LOG\_SetCallback(LogCallback callback)

**Description**

Registers a callback function. After this function is called, the custom callback can receive all HiLog logs of the current process.

Note that whether this API is called or not, it does not change the default log processing of the current process.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogCallback](#logcallback) callback | Custom callback function. If processing of logs is not needed, a null pointer can be transferred. |

#### \[h2\]OH\_LOG\_SetMinLogLevel()

void OH\_LOG\_SetMinLogLevel(LogLevel level)

**Description**

Sets the minimum log level.

**NOTE**

1.  If the set log level is lower than the [global log level](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hilog#displaying-and-setting-log-levels), the setting does not take effect.
    
2.  This function does not take effect for debug applications.
    

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogLevel](#loglevel) level | Log level. |

#### \[h2\]OH\_LOG\_SetLogLevel()

void OH\_LOG\_SetLogLevel(LogLevel level, PreferStrategy prefer)

**Description**

Sets the minimum log level of the current application process.

You can configure different preference strategies using the **prefer** parameter. The **PREFER\_CLOSE\_LOG** strategy has the same effect as the **OH\_LOG\_SetMinLogLevel()** function.

Note: This function does not take effect for debug applications.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [LogLevel](#loglevel) level | Log level. |
| [PreferStrategy](#preferstrategy) prefer | Preference strategy. |
