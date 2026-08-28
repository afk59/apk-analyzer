# Logging

Logs provide insights into the build process and help you troubleshoot any problem that arises. Hvigor defines four log levels, as listed in the following table.

#### Log Levels

| 
Log Level

 | 

Description

 |
| :-- | :-- |
| 

ERROR

 | 

Error

 |
| 

WARN

 | 

Warning

 |
| 

INFO

 | 

Information

 |
| 

DEBUG

 | 

Debugging information

 |

#### Setting the Log Level

You can set the log level by using commands or setting **logging.level** in the [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md) file. You can also enable or disable stack trace logs by using commands or setting **debugging.stacktrace** in the [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md) file.

## Log Level Options in Commands

**Table 1** Log level options
| 
Log Option

 | 

Description

 |
| :-- | :-- |
| 

**\-e** or **\--error**

 | 

Prints logs of the error level.

 |
| 

**\-w** or **\--warn**

 | 

Prints logs of warning and higher levels.

 |
| 

**\-i** or **\--info**

 | 

Prints logs of information and higher levels.

 |
| 

**\-d** or **\--debug**

 | 

Prints logs of debugging and higher levels, that is, logs of all levels.

 |

## Stack Trace Options in Commands

\--stacktrace

Prints complete stack trace information on the console.

\--no-stacktrace

Do not print stack trace information on the console for build errors (such as compilation errors).
