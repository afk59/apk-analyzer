# @ohos.faultLogger (FaultLogger)

The **faultLogger** APIs can be used to query fault logs of an application cached on the system. The APIs use the application bundle name and the UID allocated by the system as the unique key value.

The number of application fault logs stored in the system is limited by the system log pressure. You are advised to use [@ohos.hiviewdfx.hiAppEvent](../../ohos-hiviewdfx-hiappevent-application-event-logging/document.md) to subscribe to fault events such as **APP\_CRASH** and **APP\_FREEZE**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/CnKBuBdUQXutpnS9wR_wmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE36B5643E1521DDDAD57BD6168D4478A5973A3F2CE50AB7B40E4C943F9AD36A)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module are no longer maintained since API version 18. You are advised to use [@ohos.hiviewdfx.hiAppEvent](../../ohos-hiviewdfx-hiappevent-application-event-logging/document.md) to subscribe to the **APP\_CRASH** and **APP\_FREEZE** events in later versions.

For details about how to use HiAppEvent to subscribe to the **APP\_CRASH** event, see [Migrating Crash Events from the FaultLogger API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-crash-events-arkts#migrating-crash-events-from-the-faultlogger-api).

For details about how to use HiAppEvent to subscribe to the **APP\_FREEZE** event, see [Migrating Application Freeze Events from the Faultlogger API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hiappevent-watcher-freeze-events-arkts#migrating-application-freeze-events-from-the-faultlogger-api).

#### Modules to Import

import { FaultLogger } from '@kit.PerformanceAnalysisKit';

#### FaultType

Enumerates the fault types.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_SPECIFIC | 0 | No specific fault type. |
| CPP\_CRASH | 2 | C++ program crash. |
| JS\_CRASH | 3 | JS program crash. |
| APP\_FREEZE | 4 | Application freezing. |

#### FaultLogInfo

Defines the data structure of the fault log information.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | No | No | Process ID of the faulty process. |
| uid | number | No | No | User ID of the faulty process. |
| type | [FaultType](#faulttype) | No | No | Fault type. |
| timestamp | number | No | No | Millisecond-level timestamp when the log was generated. |
| reason | string | No | No | Reason for the fault. |
| module | string | No | No | Module on which the fault occurred. |
| summary | string | No | No | Summary of the fault. |
| fullLog | string | No | No | Full log text. |

#### FaultLogger.query9+

query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>) : void

Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| faultType | [FaultType](#faulttype) | Yes | Fault type. |
| callback | AsyncCallback<Array<[FaultLogInfo](#faultloginfo)\>> | Yes | 
Callback used to return the fault information array.

**value** is the fault information array obtained. If **value** is **undefined**, an exception occurs during the information retrieval. In this case, an error string will be returned.

 |

**Error codes**

For details about the error codes, see [FaultLogger Error Codes](../../../error-codes/faultlogger-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed, Parameter type error. |
| 801 | The specified SystemCapability name was not found. |
| 10600001 | The service is not started or is faulty. |

**Example**

import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
    if (error) {
        console.error(\`error code:${error.code}, error msg:${error.message}\`);
    } else {
        console.info("value length is " + value.length);
        let len: number = value.length;
        for (let i = 0; i < len; i++) {
            console.info(\`log: ${i}\`);
            console.info(\`Log pid: ${value\[i\].pid}\`);
            console.info(\`Log uid: ${value\[i\].uid}\`);
            console.info(\`Log type: ${value\[i\].type}\`);
            console.info(\`Log timestamp: ${value\[i\].timestamp}\`);
            console.info(\`Log reason: ${value\[i\].reason}\`);
            console.info(\`Log module: ${value\[i\].module}\`);
            console.info(\`Log summary: ${value\[i\].summary}\`);
            console.info(\`Log text: ${value\[i\].fullLog}\`);
        }
    }
}
try {
    FaultLogger.query(FaultLogger.FaultType.JS\_CRASH, queryFaultLogCallback);
} catch (err) {
    console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
}

#### FaultLogger.query9+

query(faultType: FaultType) : Promise<Array<FaultLogInfo>>

Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| faultType | [FaultType](#faulttype) | Yes | Fault type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[FaultLogInfo](#faultloginfo)\>> | 
Promise used to return the fault information array. You can obtain the fault information instance in its **then()** method or use **await**.

**value** is the fault information array obtained. If **value** is **undefined**, an exception occurs during the information retrieval.

 |

**Error codes**

For details about the error codes, see [FaultLogger Error Codes](../../../error-codes/faultlogger-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed, Parameter type error. |
| 801 | The specified SystemCapability name was not found. |
| 10600001 | The service is not started or is faulty. |

**Example**

import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getLog() {
  try {
    let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS\_CRASH);
    if (value) {
      console.info(\`value length: ${value.length}\`);
      let len: number = value.length;
      for (let i = 0; i < len; i++) {
        console.info(\`log: ${i}\`);
        console.info(\`Log pid: ${value\[i\].pid}\`);
        console.info(\`Log uid: ${value\[i\].uid}\`);
        console.info(\`Log type: ${value\[i\].type}\`);
        console.info(\`Log timestamp: ${value\[i\].timestamp}\`);
        console.info(\`Log reason: ${value\[i\].reason}\`);
        console.info(\`Log module: ${value\[i\].module}\`);
        console.info(\`Log summary: ${value\[i\].summary}\`);
        console.info(\`Log text: ${value\[i\].fullLog}\`);
      }
    }
  } catch (err) {
    console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
  }
}

#### FaultLogger.querySelfFaultLog(deprecated)

querySelfFaultLog(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>) : void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/NFpsLx_hSQGWuwN0gVjyeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0DA147EE910F281F56FEB6FB2B25D0AE08DAB22BA645F52A50CB078A4768D9A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [FaultLogger.query](#faultloggerquery9) instead.

Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| faultType | [FaultType](#faulttype) | Yes | Fault type. |
| callback | AsyncCallback<Array<[FaultLogInfo](#faultloginfo)\>> | Yes | 
Callback used to return the fault information array.

**value** is the fault information array obtained. If **value** is **undefined**, an exception occurs during the information retrieval. In this case, an error string will be returned.

 |

**Example**

import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
  if (error) {
    console.error(\`error code:${error.code}, error msg:${error.message}\`);
  } else {
    console.info(\`value length: ${value.length}\`);
    let len: number = value.length;
    for (let i = 0; i < len; i++) {
      console.info(\`log: ${i}\`);
      console.info(\`Log pid: ${value\[i\].pid}\`);
      console.info(\`Log uid: ${value\[i\].uid}\`);
      console.info(\`Log type: ${value\[i\].type}\`);
      console.info(\`Log timestamp: ${value\[i\].timestamp}\`);
      console.info(\`Log reason: ${value\[i\].reason}\`);
      console.info(\`Log module: ${value\[i\].module}\`);
      console.info(\`Log summary: ${value\[i\].summary}\`);
      console.info(\`Log text: ${value\[i\].fullLog}\`);
    }
  }
}
FaultLogger.querySelfFaultLog(FaultLogger.FaultType.JS\_CRASH, queryFaultLogCallback);

#### FaultLogger.querySelfFaultLog(deprecated)

querySelfFaultLog(faultType: FaultType) : Promise<Array<FaultLogInfo>>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/swiQVRRaSnqUrB2XjiCwoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4D0D92E2726DEFA883080BE0160C66175AA932257F3216473D895FF0EC4595B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [FaultLogger.query](#faultloggerquery9-1) instead.

Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| faultType | [FaultType](#faulttype) | Yes | Fault type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[FaultLogInfo](#faultloginfo)\>> | 
Promise used to return the fault information array. You can obtain the fault information instance in its **then()** method or use **await**.

**value** is the fault information array obtained. If **value** is **undefined**, an exception occurs during the information retrieval.

 |

**Example**

import { FaultLogger } from '@kit.PerformanceAnalysisKit';

async function getLog() {
  let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.querySelfFaultLog(FaultLogger.FaultType.JS\_CRASH);
  if (value) {
    console.info(\`value length: ${value.length}\`);
    let len: number = value.length;
    for (let i = 0; i < len; i++) {
      console.info(\`log: ${i}\`);
      console.info(\`Log pid: ${value\[i\].pid}\`);
      console.info(\`Log uid: ${value\[i\].uid}\`);
      console.info(\`Log type: ${value\[i\].type}\`);
      console.info(\`Log timestamp: ${value\[i\].timestamp}\`);
      console.info(\`Log reason: ${value\[i\].reason}\`);
      console.info(\`Log module: ${value\[i\].module}\`);
      console.info(\`Log summary: ${value\[i\].summary}\`);
      console.info(\`Log text: ${value\[i\].fullLog}\`);
    }
  }
}
