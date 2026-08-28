# @ohos.process (Obtaining Process Information)

The **process** module provides process management APIs, for example, APIs for obtaining process information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Azkbo6GGS8uf_BVchiW5fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FFAC1CAF14CF34040178CA8C563618B69E2A10E02CD54D88EE5546F0542868D)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { process } from '@kit.ArkTS';

#### Properties

**System capability**: SystemCapability.Utils.Lang

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uid | number | Yes | No | User identifier (UID) of the process. |
| pid | number | Yes | No | Process ID (PID) of the process. |
| tid8+ | number | Yes | No | Thread ID (TID) of the thread. |

#### EventListener

type EventListener = (evt: Object) => void

Event to store.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| evt | Object | Yes | Event. |

#### process.isIsolatedProcess8+

isIsolatedProcess(): boolean

Checks whether this process is isolated.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the process is isolated; otherwise, **false** is returned. |

**Example**

let result = process.isIsolatedProcess();

#### process.is64Bit8+

is64Bit(): boolean

Checks whether this process is running in a 64-bit environment.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the process is running in a 64-bit environment; otherwise, **false** is returned. |

**Example**

let result = process.is64Bit();

#### process.getStartRealtime8+

getStartRealtime(): number

Obtains the duration (excluding the system sleep time), in milliseconds, from the time the system starts to the time the process starts.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Duration obtained, in milliseconds. |

**Example**

let realtime = process.getStartRealtime();

#### process.getPastCpuTime8+

getPastCpuTime(): number

Obtains the CPU time (in milliseconds) from the time the process starts to the current time.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | CPU time obtained, in milliseconds. |

**Example**

let result = process.getPastCpuTime();

#### process.abort

abort(): void

Aborts a process and generates a core file. This method will cause a process to exit immediately. Exercise caution when using this method.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Example**

process.abort();

#### process.uptime

uptime(): number

Obtains the running time of the current system, in seconds.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Running time of the system, in seconds. |

**Example**

let time = process.uptime();

#### process.kill(deprecated)

kill(signal: number, pid: number): boolean

Sends a signal to a specified process to terminate it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/KqxQlxXDTgWC0abKouqqig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CED4180B6F6DF80CE2B9AE0DEBF08496F5AC1EE5400DC35694C8D2E45244C163)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [kill9+](#kill9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| signal | number | Yes | Signal to send. |
| pid | number | Yes | PID of the process, to which the signal will be sent. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | If the signal is sent successfully, **true** is returned. Other, **false** is returned. |

**Example**

let pres = process.pid;
let result = process.kill(28, pres);

#### process.exit(deprecated)

exit(code: number): void

Terminates this process.

Exercise caution when using this API. After this API is called, the application exits. If the input parameter is not 0, data loss or exceptions may occur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/SVya4oTUREmvm5ggwWDQkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F491B3FB0D9A48F4E1E7DDE5664FB13B4D96DBF6E0FFAFBB7070D1E05DA85E44)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [exit9+](#exit9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Exit code of the process. |

**Example**

process.exit(0);

#### process.getUidForName(deprecated)

getUidForName(v: string): number

Obtains the UID of a user from the user database of the system based on the specified user name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/pv-uY7RxT1Wa92FuzU56kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF5E2C2D97FE203BB4F74AC4FAE87D35752A451DF328C9E42BE65CD8C598C34D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getUidForName9+](#getuidforname9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| v | string | Yes | User name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | UID of the user. |

**Example**

let pres = process.getUidForName("tool");

#### process.getThreadPriority(deprecated)

getThreadPriority(v: number): number

Obtains the thread priority based on the specified TID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/PEWeaXjxRcqA9_gfY9xK0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3E86C45384193E9F9092CA71E2EC58BF34D3B6DA7AB974A8CF75CE10FFE5B20)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getThreadPriority9+](#getthreadpriority9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| v | number | Yes | TID. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Priority of the thread. The priority depends on the operating system. |

**Example**

let tid = process.tid;
let pres = process.getThreadPriority(tid);

#### process.isAppUid(deprecated)

isAppUid(v: number): boolean

Checks whether a UID belongs to this application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/MfyC1yrASIGNonOvk-tg2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79CDAD7510DFB053B7196C261416579B24D53BDCAD8E857526D121B9054CCA1C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isAppUid9+](#isappuid9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| v | number | Yes | UID. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the UID belongs to the application; otherwise, **false** is returned. |

**Example**

let result = process.isAppUid(688);

#### process.getSystemConfig(deprecated)

getSystemConfig(name: number): number

Obtains the system configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/dTK-jyM1QeCZrDCUBBoStA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7E79C24D87644061DD3BEA94BDFC41633D5828760E5062E5C7CCD5E5C070736)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getSystemConfig9+](#getsystemconfig9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | number | Yes | System configuration parameter name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | System configuration obtained. |

**Example**

let \_SC\_ARG\_MAX = 0;
let pres = process.getSystemConfig(\_SC\_ARG\_MAX);

#### process.getEnvironmentVar(deprecated)

getEnvironmentVar(name: string): string

Obtains the value of an environment variable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/NRLE-0MxTW-nwH97AjAKoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D9FA31FBE30FAA4D5F35666BD2FB9F946EE39E3D7B1669269846042AC5268A6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getEnvironmentVar9+](#getenvironmentvar9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Environment variable name. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the environment variable. |

**Example**

let pres = process.getEnvironmentVar("PATH");

#### ProcessManager9+

Provides APIs for throwing exceptions during the addition of a process.

Construct a **ProcessManager** object.

#### \[h2\]isAppUid9+

isAppUid(v: number): boolean

Checks whether a UID belongs to this application.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| v | number | Yes | UID. which can be obtained by running **process.uid**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the UID belongs to the application; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
// Use process.uid to obtain the UID.
let pres = process.uid;
let result = pro.isAppUid(pres);
console.info("result: " + result); // result: true

#### \[h2\]getUidForName9+

getUidForName(v: string): number

Obtains the UID of a user from the user database of the system based on the specified user name.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| v | string | Yes | User name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | UID of the user. If the user does not exist, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
let pres = pro.getUidForName("tool");

#### \[h2\]getThreadPriority9+

getThreadPriority(v: number): number

Obtains the thread priority based on the specified TID.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| v | number | Yes | TID. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Priority of the thread. The priority depends on the operating system. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
let tid = process.tid;
let pres = pro.getThreadPriority(tid);

#### \[h2\]getSystemConfig9+

getSystemConfig(name: number): number

Obtains the system configuration.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | number | Yes | System configuration parameter name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | System configuration obtained. If the configuration does not exist, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
let \_SC\_ARG\_MAX = 0;
let pres = pro.getSystemConfig(\_SC\_ARG\_MAX);

#### \[h2\]getEnvironmentVar9+

getEnvironmentVar(name: string): string

Obtains the value of an environment variable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/_aqdmJH_TTmbCsxFp-2GyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F043670B92C6663CBBA81D0812893486317BDEB47CAC87FF76A6E526142BCD9E)

Obtains the value of an environment variable. If the environment variable does not exist, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Environment variable name. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the environment variable. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
let pres = pro.getEnvironmentVar("PATH");

#### \[h2\]exit9+

exit(code: number): void

Terminates this process.

Exercise caution when using this API. After this API is called, the application exits. If the input parameter is not 0, data loss or exceptions may occur.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Exit code of the process. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
pro.exit(0);

#### \[h2\]kill9+

kill(signal: number, pid: number): boolean

Sends a signal to the specified process to terminate it. Only the current process can be terminated.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| signal | number | Yes | Signal to send. Value range: 1 <= signal <= 64. |
| pid | number | Yes | PID of the process, to which the signal will be sent. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Signal sending result. The value **true** is returned if the signal is sent successfully; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new process.ProcessManager();
let pres = process.pid;
let result = pro.kill(28, pres);
