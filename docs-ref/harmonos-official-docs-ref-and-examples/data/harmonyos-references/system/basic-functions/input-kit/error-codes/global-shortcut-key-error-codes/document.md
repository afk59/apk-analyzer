# Global Shortcut Key Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ZQMgDdrLQGqw-1LrezjLUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062405Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBBFF6E30339D6EE86CF26DC0B2B386B8FF31BF19CD0D5DA101C1CEC9ECEF2BF)

-   This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 4200002 Shortcut Key Already Registered by a System Application

**Error Message**

The hotkey has been used by the system.

**Description**

This error code is reported if the shortcut key has been registered by a system application.

**Possible Cause**

1.  The shortcut key has been registered by a system application.

**Solution**

1.  You can call [getAllSystemHotkeys](../../arkts-apis/ohos-multimodalinput-inputconsumer-global-shortcut-keys/document.md#inputconsumergetallsystemhotkeys) to query all system shortcut keys.

#### 4200003 Shortcut Key Already Registered by a Third-party Application

**Error Message**

The hotkey has been subscribed to by another.

**Description**

This error code is generated when the shortcut key is registered by a third-party application.

**Possible Cause**

1.  The shortcut key has been registered by a third-party application.

**Solution**

1.  In the cmd window, run **hidumper -s 3101 -a -s** to query all registered shortcut keys and use any available shortcut keys.

#### 3800001 Multimodal input internal error

**Error Message**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**Description**

Internal error of the multimodal input service.

**Possible Cause**

Unexpected errors, such as memory allocation failure, busy thread, and abnormal service exit, occur.

**Solution**

Try again later.
