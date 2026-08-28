# @ohos.resourceschedule.backgroundTaskManager (Background Task Management)

The **backgroundTaskManager** module provides APIs to request background tasks. You can use the APIs to request transient tasks, continuous tasks, or efficiency resources to prevent the application process from being terminated or suspended when your application is switched to the background. For details, see [Continuous Task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/continuous-task) and [Transient Task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/transient-task).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/uBVVtB6UTtylBVg7BqCLpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0960ADC24968C11C7C37D78FF61A1BEFC6999686962EDC88AE8C630D124B0162)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

#### backgroundTaskManager.requestSuspendDelay

requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo

Requests a transient task.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4FcgDm6XRSyj2R82rbbRNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062318Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B272C6E10D79E0985ECDE3000F45CE573F0964E063BD54D02741C7B5E7B4682)

For details about the constraints on requesting and using a transient task, see [Transient Task (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/transient-task#constraints).

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reason | string | Yes | Reason for requesting the transient task. |
| callback | Callback<void> | Yes | Callback used to notify the application that the transient task is about to time out. Generally, the callback is invoked 6 seconds before the timeout. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DelaySuspendInfo](#delaysuspendinfo) | Information about the transient task. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let myReason = 'test requestSuspendDelay';
try {
  let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
  // Callback function, which is triggered when the transient task is about to time out. The application can carry out data clear and annotation, and cancel the task in the callback.
  // The callback is independent of the service of the application. After the request for the transient task is successful, the application normally executes its own service logic.
    console.info("Request suspension delay will time out.");
  })
  let id = delayInfo.requestId;
  let time = delayInfo.actualDelayTime;
  console.info("The requestId is: " + id);
  console.info("The actualDelayTime is: " + time);
} catch (error) {
  console.error(\`requestSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
}

#### backgroundTaskManager.getRemainingDelayTime

getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void

Obtains the remaining time of a transient task. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| requestId | number | Yes | Request ID of the transient task. It is obtained by calling the [requestSuspendDelay](#backgroundtaskmanagerrequestsuspenddelay) API. |
| callback | AsyncCallback<number> | Yes | Callback used to return the remaining time of the transient task, in milliseconds. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
backgroundTaskManager.getRemainingDelayTime(id, (error: BusinessError, res: number) => {
  if(error) {
    console.error(\`callback => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}\`);
  } else {
    console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
  }
})

#### backgroundTaskManager.getRemainingDelayTime

getRemainingDelayTime(requestId: number): Promise<number>

Obtains the remaining time of a transient task. This API uses a promise to return the result.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| requestId | number | Yes | Request ID of the transient task. It is obtained by calling the [requestSuspendDelay](#backgroundtaskmanagerrequestsuspenddelay) API. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise that returns the remaining time of the transient task, in milliseconds. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
backgroundTaskManager.getRemainingDelayTime(id).then((res: number) => {
  console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
}).catch((error: BusinessError) => {
  console.error(\`promise => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}\`);
})

#### backgroundTaskManager.cancelSuspendDelay

cancelSuspendDelay(requestId: number): void

Cancels a transient task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| requestId | number | Yes | Request ID of the transient task. It is obtained by calling the [requestSuspendDelay](#backgroundtaskmanagerrequestsuspenddelay) API. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let id = 1;
try {
  backgroundTaskManager.cancelSuspendDelay(id);
} catch (error) {
  console.error(\`cancelSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
}

#### backgroundTaskManager.getTransientTaskInfo20+

getTransientTaskInfo(): Promise<TransientTaskInfo>

Obtains all transient task information, including the remaining quota of the current day. This API uses a promise to return the result.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[TransientTaskInfo](#transienttaskinfo20)\> | Promise that returns all transient task information. |

**Error codes**

For details about the error codes, see [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9900001 | Caller information verification failed for a transient task. |
| 9900003 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9900004 | System service operation failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  backgroundTaskManager.getTransientTaskInfo().then((res: backgroundTaskManager.TransientTaskInfo) => {
    console.info(\`Operation getTransientTaskInfo succeeded. data: \` + JSON.stringify(res));
  }).catch((error : BusinessError) => {
    console.error(\`Operation getTransientTaskInfo failed. code is ${error.code} message is ${error.message}\`);
  });
} catch (error) {
  console.error(\`Operation getTransientTaskInfo failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
}

#### backgroundTaskManager.startBackgroundRunning

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void

Requests a continuous task of a specific type. This API uses an asynchronous callback to return the result. After a continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request multiple continuous tasks by calling [startBackgroundRunning](#backgroundtaskmanagerstartbackgroundrunning21) added in API version 21.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| bgMode | [BackgroundMode](#backgroundmode) | Yes | Type of the continuous task. |
| wantAgent | [WantAgent](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | Notification parameters, which are used to specify the target page that is redirected to when a continuous task notification is clicked. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the continuous task is requested, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 202 | Not System App. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
// In atomic services, please remove the WantAgent import.

function callback(error: BusinessError, data: void) {
  if (error) {
    console.error(\`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
  } else {
    console.info("Operation startBackgroundRunning succeeded");
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // List of operations to be executed after the notification is clicked.
      wants: \[
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      \],
      // Type of the operation to perform after the notification is clicked.
      actionType: wantAgent.OperationType.START\_ABILITY,
      // Custom request code.
      requestCode: 0,
      // Execution attribute of the operation to perform after the notification is clicked.
      wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
    };

    try {
      // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
      // In atomic services, please replace the following line of code with wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {.
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          backgroundTaskManager.startBackgroundRunning(this.context,
            backgroundTaskManager.BackgroundMode.AUDIO\_PLAYBACK, wantAgentObj, callback)
        } catch (error) {
          console.error(\`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      });
    } catch (error) {
      console.error(\`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.startBackgroundRunning

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>

Requests a continuous task of a specific type. This API uses a promise to return the result. After a continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request multiple continuous tasks by calling [startBackgroundRunning](#backgroundtaskmanagerstartbackgroundrunning21) added in API version 21.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| bgMode | [BackgroundMode](#backgroundmode) | Yes | Type of the continuous task. |
| wantAgent | [WantAgent](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | Notification parameters, which are used to specify the target page that is redirected to when a continuous task notification is clicked. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 202 | Not System App. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
// In atomic services, please remove the WantAgent import.

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // List of operations to be executed after the notification is clicked.
      wants: \[
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      \],
      // Type of the operation to perform after the notification is clicked.
      actionType: wantAgent.OperationType.START\_ABILITY,
      // Custom request code.
      requestCode: 0,
      // Execution attribute of the operation to perform after the notification is clicked.
      wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
    };

    try {
      // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
      // In atomic services, please replace the following line of code with wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {.
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          backgroundTaskManager.startBackgroundRunning(this.context,
            backgroundTaskManager.BackgroundMode.AUDIO\_PLAYBACK, wantAgentObj).then(() => {
              console.info("Operation startBackgroundRunning succeeded");
            }).catch((error: BusinessError) => {
              console.error(\`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
            });
        } catch (error) {
          console.error(\`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      });
    } catch (error) {
      console.error(\`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.stopBackgroundRunning

stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void

Cancels all continuous tasks in the current UIAbility (ServiceAbility in the FA model). This API uses an asynchronous callback to return the result. You can also call the [stopBackgroundRunning](#backgroundtaskmanagerstopbackgroundrunning21) API to cancel a continuous task with the specified ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the continuous task is canceled, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(error: BusinessError, data: void) {
  if (error) {
    console.error(\`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
  } else {
    console.info("Operation stopBackgroundRunning succeeded");
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.stopBackgroundRunning(this.context, callback);
    } catch (error) {
      console.error(\`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.stopBackgroundRunning

stopBackgroundRunning(context: Context): Promise<void>

Cancels all continuous tasks in the current UIAbility (ServiceAbility in the FA model). This API uses a promise to return the result. You can also call the [stopBackgroundRunning](#backgroundtaskmanagerstopbackgroundrunning21) API to cancel a continuous task with the specified ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
        console.info("Operation stopBackgroundRunning succeeded");
      }).catch((error: BusinessError) => {
        console.error(\`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
      });
    } catch (error) {
      console.error(\`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.startBackgroundRunning12+

startBackgroundRunning(context: Context, bgModes: string\[\], wantAgent: WantAgent): Promise<ContinuousTaskNotification>

Requests continuous tasks of multiple types. This API uses a promise to return the result. After a continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request multiple continuous tasks by calling [startBackgroundRunning](#backgroundtaskmanagerstartbackgroundrunning21) added in API version 21.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| bgModes | string\[\] | Yes | 

Types of continuous tasks. For details about the available options, see [Item](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/continuous-task#use-cases).

Note: One or more types can be passed.

 |
| wantAgent | [WantAgent](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | Notification parameters, which are used to specify the target page that is redirected to when a continuous task notification is clicked. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ContinuousTaskNotification](#continuoustasknotification12)\> | Promise that returns an object of the [ContinuousTaskNotification](#continuoustasknotification12) type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { notificationManager } from '@kit.NotificationKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
// In atomic services, please remove the WantAgent import.

export default class EntryAbility extends UIAbility {
  id: number = 0; // Save the notification ID.

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // List of operations to be executed after the notification is clicked.
      wants: \[
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      \],
      // Type of the operation to perform after the notification is clicked.
      actionType: wantAgent.OperationType.START\_ABILITY,
      // Custom request code.
      requestCode: 0,
      // Execution attribute of the operation to perform after the notification is clicked.
      wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
    };

    try {
      // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
      // In atomic services, please replace the following line of code with wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {.
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          let list: Array<string> = \["dataTransfer"\];
          // In atomic services, let list: Array<string> = \["audioPlayback"\];
          backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
            console.info("Operation startBackgroundRunning succeeded");
            // For a continuous task of the upload and download type, the application can use the notification ID returned in res to update the notification, for example, sending a template notification with a progress bar.
            this.id = res.notificationId;
          }).catch((error: BusinessError) => {
            console.error(\`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
          });
        } catch (error) {
          console.error(\`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      });
    } catch (error) {
      console.error(\`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }

  // The application updates its progress.
  updateProcess(process: number) {
    // Define the notification type. The notification type of the progress update must be live view.
    let downLoadTemplate: notificationManager.NotificationTemplate = {
      name: 'downloadTemplate', // Currently, only downloadTemplate is supported. Retain the value.
      data: {
        title: 'File download: music.mp4', // Mandatory.
        fileName: 'senTemplate', // Mandatory.
        progressValue: process, // The application updates the progress, which is user-defined.
      }
    };
    let request: notificationManager.NotificationRequest = {
      content: {
        // System live view type, which remains unchanged.
        notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_SYSTEM\_LIVE\_VIEW,
        systemLiveView: {
          typeCode: 8, // Set this parameter to 8 for the upload and download type. Currently, only the upload and download type is supported. Retain the value.
          title: "test", // Customized by the application.
          text: "test", // Customized by the application.
        }
      },
      id: this.id, // The value must be the ID returned for a continuous-task request. Otherwise, the application fails to update the notification.
      notificationSlotType: notificationManager.SlotType.LIVE\_VIEW, // Live view type. Retain the value.
      template: downLoadTemplate // Name of the template to be set for the application.
    };

    try {
      notificationManager.publish(request).then(() => {
        console.info("publish success, id= " + this.id);
      }).catch((err: BusinessError) => {
        console.error(\`publish fail: ${JSON.stringify(err)}\`);
      });
    } catch (err) {
      console.error(\`publish fail: ${JSON.stringify(err)}\`);
    }
  }
};

#### backgroundTaskManager.updateBackgroundRunning12+

updateBackgroundRunning(context: Context, bgModes: string\[\]): Promise<ContinuousTaskNotification>

Updates continuous tasks of multiple types. This API uses a promise to return the result. After a continuous task is successfully updated, there will be a notification message without prompt tone.

Before updating a continuous task, you can call [getAllContinuousTasks](#backgroundtaskmanagergetallcontinuoustasks20) to retrieve information about all existing continuous tasks. If there are no continuous tasks, the update will fail.

This API can only be used to update continuous tasks that were requested via the following APIs:

[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void](#backgroundtaskmanagerstartbackgroundrunning)

[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>](#backgroundtaskmanagerstartbackgroundrunning-1)

[startBackgroundRunning(context: Context, bgModes: string\[\], wantAgent: WantAgent): Promise<ContinuousTaskNotification>](#backgroundtaskmanagerstartbackgroundrunning12)

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| bgModes | string\[\] | Yes | 

Types of continuous tasks after the update. For details about the available options, see [Item](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/continuous-task#use-cases).

Note: One or more types can be passed.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ContinuousTaskNotification](#continuoustasknotification12)\> | Promise that returns an object of the [ContinuousTaskNotification](#continuoustasknotification12) type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      // You must call startBackgroundRunning before updateBackgroundRunning. Here it is assumed that you have called startBackgroundRunning.
      let list: Array<string> = \["audioPlayback"\];
      backgroundTaskManager.updateBackgroundRunning(this.context, list).then(() => {
        console.info("Operation updateBackgroundRunning succeeded");
      }).catch((error: BusinessError) => {
        console.error(\`Operation updateBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
      });
    } catch (error) {
      console.error(\`Operation updateBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.getAllContinuousTasks20+

getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo\[\]>

Obtains all continuous task information, including the task ID and type. This API uses a promise to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ContinuousTaskInfo](#continuoustaskinfo20)\[\]> | Promise that returns all continuous task information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      // If no continuous task is requested, an empty array is obtained.
      backgroundTaskManager.getAllContinuousTasks(this.context).then((res: backgroundTaskManager.ContinuousTaskInfo\[\]) => {
        console.info(\`Operation getAllContinuousTasks succeeded. data: \` + JSON.stringify(res));
      }).catch((error: BusinessError) => {
        console.error(\`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}\`);
      });
    } catch (error) {
      console.error(\`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.getAllContinuousTasks20+

getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo\[\]>

Obtains all continuous task information, including the task ID and type. It supports specifying whether to include suspended tasks and uses a promise to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| includeSuspended | boolean | Yes | Whether to obtain the information about the suspended continuous task. The value **true** means to obtain the information, and the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ContinuousTaskInfo](#continuoustaskinfo20)\[\]> | Promise that returns all continuous task information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      // If no continuous task is requested, an empty array is obtained.
      backgroundTaskManager.getAllContinuousTasks(this.context, false).then((res: backgroundTaskManager.ContinuousTaskInfo\[\]) => {
        console.info(\`Operation getAllContinuousTasks succeeded. data: \` + JSON.stringify(res));
      }).catch((error: BusinessError) => {
        console.error(\`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}\`);
      });
    } catch (error) {
      console.error(\`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.on('continuousTaskCancel')15+

on(type: 'continuousTaskCancel', callback: Callback<ContinuousTaskCancelInfo>): void

Subscribes to continuous task cancellation events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'continuousTaskCancel'**, indicating that a continuous task is canceled. |
| callback | Callback<[ContinuousTaskCancelInfo](#continuoustaskcancelinfo15)\> | Yes | Callback used to return information such as the reason for canceling a continuous task. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Register a exist callback type; 3. Parameter verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
  console.info('continuousTaskCancel callback id ' + info.id);
  console.info('continuousTaskCancel callback reason ' + info.reason);
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.on("continuousTaskCancel", callback);
    } catch (error) {
      console.error(\`Operation onContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.off('continuousTaskCancel')15+

off(type: 'continuousTaskCancel', callback?: Callback<ContinuousTaskCancelInfo>): void

Unsubscribes from continuous task cancellation events. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cancels a continuous task. The value is fixed at **'continuousTaskCancel'**. |
| callback | Callback<[ContinuousTaskCancelInfo](#continuoustaskcancelinfo15)\> | No | Callback for which listening is cancelled. If this parameter is left unspecified, all registered callbacks are cancelled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Unregister type has not register; 3. Parameter verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
  console.info('continuousTaskCancel callback id ' + info.id);
  console.info('continuousTaskCancel callback reason ' + info.reason);
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.off("continuousTaskCancel", callback);
    } catch (error) {
      console.error(\`Operation onContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.on('continuousTaskSuspend')20+

on(type: 'continuousTaskSuspend', callback: Callback<ContinuousTaskSuspendInfo>): void

Registers a listener for continuous task suspension. This API uses an asynchronous callback to return the result. After the callback is registered, if the system detects for the first time that the application does not execute the corresponding service, the system does not directly cancel the continuous task. Instead, it will mark the task as suspended. If the detection failures persist, the system will cancel the continuous task.

When a continuous task is suspended, the application will be suspended when switched to the background and automatically activated when brought back to the foreground.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'continuousTaskSuspend'**, indicating that the continuous task is suspended. |
| callback | Callback<[ContinuousTaskSuspendInfo](#continuoustasksuspendinfo20)\> | Yes | Callback used to return information such as the reason for suspending a continuous task. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskSuspendInfo) {
  console.info('continuousTaskSuspend callback continuousTaskId: ' + info.continuousTaskId);
  console.info('continuousTaskSuspend callback suspendState: ' + info.suspendState);
  console.info('continuousTaskSuspend callback suspendReason: ' + info.suspendReason);
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.on("continuousTaskSuspend", callback);
    } catch (error) {
      console.error(\`Operation onContinuousTaskSuspend failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.off('continuousTaskSuspend')20+

off(type: 'continuousTaskSuspend', callback?: Callback<ContinuousTaskSuspendInfo>): void

Unregisters from the listener for continuous task suspension. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'continuousTaskSuspend'**, indicating that the continuous task is suspended. |
| callback | Callback<[ContinuousTaskSuspendInfo](#continuoustasksuspendinfo20)\> | No | Callback used to unregister from the listener for continuous task suspension. If this parameter is not passed, all listeners are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskSuspendInfo) {
  console.info('continuousTaskSuspend callback continuousTaskId: ' + info.continuousTaskId);
  console.info('continuousTaskSuspend callback suspendState: ' + info.suspendState);
  console.info('continuousTaskSuspend callback suspendReason: ' + info.suspendReason);
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.off("continuousTaskSuspend", callback);
    } catch (error) {
      console.error(\`Operation offContinuousTaskSuspend failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.on('continuousTaskActive')20+

on(type: 'continuousTaskActive', callback: Callback<ContinuousTaskActiveInfo>): void

Registers a listener for continuous task activation. This API uses an asynchronous callback to return the result. The application returns to the foreground to activate the suspended continuous task.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'continuousTaskActive'**, indicating that the continuous task is activated. |
| callback | Callback<[ContinuousTaskActiveInfo](#continuoustaskactiveinfo20)\> | Yes | Callback used to return the activation information about a continuous task. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskActiveInfo) {
  console.info('continuousTaskActive callback id: ' + info.id);
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.on("continuousTaskActive", callback);
    } catch (error) {
      console.error(\`Operation onContinuousTaskActive failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.off('continuousTaskActive')20+

off(type: 'continuousTaskActive', callback?: Callback<ContinuousTaskActiveInfo>): void

Unregisters from the listener for continuous task activation. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'continuousTaskActive'**, indicating that the continuous task is activated. |
| callback | Callback<[ContinuousTaskActiveInfo](#continuoustaskactiveinfo20)\> | No | Callback used to unregister from the listener for continuous task activation. If this parameter is not passed, all listeners are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

function callback(info: backgroundTaskManager.ContinuousTaskActiveInfo) {
  console.info('continuousTaskActive callback id: ' + info.id);
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.off("continuousTaskActive", callback);
    } catch (error) {
      console.error(\`Operation offContinuousTaskActive failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.startBackgroundRunning21+

startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>

Requests a continuous task. This API allows a UIAbility (ServiceAbility in the FA model) to request multiple continuous tasks and uses a promise to return the result. When using this API to request a continuous task, its notification can be combined with that of an existing continuous task. For details, see [ContinuousTaskRequest](#continuoustaskrequest21).

A maximum of 10 continuous tasks can be created simultaneously. Upon successful creation of a continuous task, a notification will be sent without a prompt tone.

If a continuous task requested via this API includes multiple task types (including data transmission tasks), two notifications will appear in the notification panel: one for the data transmission task and the other for the remaining tasks. Removing either notification will cancel the continuous task and remove the other notification. The continuous task notification ID returned by the API is the ID of the data transmission type, which is used to update the data transmission progress.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| request | [ContinuousTaskRequest](#continuoustaskrequest21) | Yes | Request information of a continuous task, including the main type and subtype. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ContinuousTaskNotification](#continuoustasknotification12)\> | Promise used to return the continuous task notification information, including the continuous task ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  notificationId: number = 0; // Save the notification ID.
  continuousTaskId: number | undefined = -1;
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // Replace the bundleName and abilityName of the application with the actual ones.
      wants: \[
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      \],
      // Set the operation type after the notification is tapped.
      actionType: wantAgent.OperationType.START\_ABILITY,
      // Custom request code, which is used to identify the operation to execute.
      requestCode: 0,
      // Set the operation properties after the notification is tapped.
      wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
    };

    try {
      // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          // If notifications need to be combined, the main type and subtype must be the same, combinedTaskNotification must be set to true, and continuousTaskId must exist and be valid.
          // Request a continuous task whose main type is MODE\_LOCATION.
          let modeList: Array<number> = \[backgroundTaskManager.BackgroundTaskMode.MODE\_LOCATION\];
          let subModeList: Array<number> = \[backgroundTaskManager.BackgroundTaskSubmode.SUBMODE\_NORMAL\_NOTIFICATION\];
          let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
          continuousTaskRequest.backgroundTaskModes =  modeList;
          continuousTaskRequest.backgroundTaskSubmodes = subModeList;
          continuousTaskRequest.wantAgent = wantAgentObj;
          continuousTaskRequest.combinedTaskNotification = false;
          continuousTaskRequest.continuousTaskId = this.continuousTaskId;
          backgroundTaskManager.startBackgroundRunning(this.context, continuousTaskRequest).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
            console.info(\`Operation startBackgroundRunning succeeded. notificationId is ${res.notificationId} continuousTaskId is ${res.continuousTaskId}\`);
            this.notificationId = res.notificationId;
            this.continuousTaskId = res.continuousTaskId;
          }).catch((error: BusinessError) => {
            console.error(\`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
          });
        } catch (error) {
          console.error(\`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      });
    } catch (error) {
      console.error(\`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.updateBackgroundRunning21+

updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>

Updates a continuous task. This API uses a promise to return the result. After a continuous task is successfully updated, there will be a notification message without prompt tone.

The following restrictions apply when updating a continuous task:

1.  This API can only update continuous tasks requested via [startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>](#backgroundtaskmanagerstartbackgroundrunning21).
2.  If the main type and subtype of the background tasks are the same, only the wants information (such as **abilityName**) in **ContinuousTaskRequest.wantAgent** can be updated. If the types are different, the update fails.
3.  If the continuous task to be updated or the specified update type contains the data transmission type, a failure message is returned.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| request | [ContinuousTaskRequest](#continuoustaskrequest21) | Yes | Continuous task request information, including the ID of the continuous task to be updated. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ContinuousTaskNotification](#continuoustasknotification12)\> | Promise used to return the updated continuous task notification information, including the continuous task ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  notificationId: number = 0; // Save the notification ID.
  continuousTaskId: number | undefined = -1; // Continuous task ID.
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // Add the bundleName and abilityName of the application to be started. Replace them with the actual ones.
      wants: \[
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      \],
      // Set the operation type after the notification is tapped.
      actionType: wantAgent.OperationType.START\_ABILITY,
      // Custom request code, which is used to identify the operation to execute.
      requestCode: 0,
      // Set the operation properties after the notification is tapped.
      wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
    };

    try {
      // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          // You must call startBackgroundRunning before updateBackgroundRunning. Apply for a continuous task in advance.
          let modeList: Array<number> = \[backgroundTaskManager.BackgroundTaskMode.MODE\_LOCATION\];
          let subModeList: Array<number> = \[backgroundTaskManager.BackgroundTaskSubmode.SUBMODE\_NORMAL\_NOTIFICATION\];
          let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
          continuousTaskRequest.backgroundTaskModes = modeList;
          continuousTaskRequest.backgroundTaskSubmodes = subModeList;
          continuousTaskRequest.wantAgent = wantAgentObj;
          continuousTaskRequest.combinedTaskNotification = false;
          continuousTaskRequest.continuousTaskId = this.continuousTaskId; // For the update API, the continuous task ID must be passed and the ID must exist. Otherwise, the update fails.
          backgroundTaskManager.updateBackgroundRunning(this.context, continuousTaskRequest).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
            console.info("Operation updateBackgroundRunning succeeded");
            this.notificationId = res.notificationId;
          }).catch((error: BusinessError) => {
            console.error(\`Operation updateBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
          });
        } catch (error) {
          console.error(\`Operation updateBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      });
    } catch (error) {
      console.error(\`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### backgroundTaskManager.stopBackgroundRunning21+

stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>

Cancels a continuous task with the specified ID. This API uses a promise to return the result. You can also call the [stopBackgroundRunning](#backgroundtaskmanagerstopbackgroundrunning) API to cancel all continuous tasks in the current UIAbility.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| continuousTaskId | number | Yes | 

Continuous task ID.

Note: You can obtain the ID of the current continuous task through the return value of the [startBackgroundRunning](#backgroundtaskmanagerstartbackgroundrunning21) API, or obtain information about all continuous tasks through the [getAllContinuousTasks](#backgroundtaskmanagergetallcontinuoustasks20-1) API.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  continuousTaskId: number = 0;
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      backgroundTaskManager.stopBackgroundRunning(this.context, this.continuousTaskId).then(() => {
        console.info("Operation stopBackgroundRunning succeeded");
      }).catch((error: BusinessError) => {
        console.error(\`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}\`);
      });
    } catch (error) {
      console.error(\`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### DelaySuspendInfo

Defines the information about the transient task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| requestId | number | No | No | Request ID of the transient task. |
| actualDelayTime | number | No | No | 
Actual duration of the transient task requested by the application, in milliseconds.

Note: The maximum duration of a transient task is 3 minutes in normal cases. In the case of a low battery ([BatteryCapacityLevel](../../../../system/basic-functions/basic-services-kit/arkts-apis/device-management/ohos-batteryinfo-battery-information/document.md#batterycapacitylevel9) set to **LEVEL\_LOW**), the maximum duration is decreased to 1 minute.

 |

#### TransientTaskInfo20+

Describes all transient task information.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| remainingQuota | number | No | No | Remaining quota of the application on the current day, in ms. |
| transientTasks | [DelaySuspendInfo](#delaysuspendinfo)\[\] | No | No | All information about the requested transient task. |

#### BackgroundMode

Defines the type of a continuous task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| DATA\_TRANSFER | 1 | 
Data transfer.

Use scenario: upload and download in non-hosting mode, for example, uploading or downloading data in the background of a browser.

Note: During data transfer, the application needs to update the progress. If the progress is not updated for more than 10 minutes, the continuous task of the **DATA\_TRANSFER** type will be canceled.

The notification type of the progress update must be live view. For details, see the example in [startBackgroundRunning()](#backgroundtaskmanagerstartbackgroundrunning12).

 |
| AUDIO\_PLAYBACK | 2 | 

Audio and video playback.

Use scenario: audio/video playback in the background and audio/video casting.

**Atomic service API**: This API can be used in atomic services since API version 12.

Note: Since API version 20, if an application requests or updates a continuous task of the **AUDIO\_PLAYBACK** type without connecting to AVSession, a notification will appear in the notification panel once the task is successfully requested or updated.

Once AVSession is connected, notifications will be sent by AVSession instead of the background task module.

For API version 19 and earlier versions, the background task module does not display notifications in the notification panel.

 |
| AUDIO\_RECORDING | 3 | 

Audio recording.

Use scenario: recording and screen capture in the background.

 |
| LOCATION | 4 | Positioning and navigation. |
| BLUETOOTH\_INTERACTION | 5 | 

Bluetooth-related services.

Use scenario: An application moves to the background while transferring files via Bluetooth.

 |
| MULTI\_DEVICE\_CONNECTION | 6 | 

Multi-device connection.

Use scenario: distributed service connection and casting.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| VOIP13+ | 8 | 

Audio and video calls.

Use scenario: Chat applications (with audio and video services) transition into the background during audio and video calls.

 |
| TASK\_KEEPING | 9 | 

Computing tasks.

Use scenario: antivirus software.

Note: Starting from API version 21, this capability is available for PCs/2-in-1 devices, and non-PCs/2-in-1 devices that have obtained the ACL permission [ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionkeep_background_running_system). In API version 20 and earlier versions, this task type is limited to PCs/2-in-1 devices only.

 |

#### ContinuousTaskNotification12+

Describes the information about a continuous-task notification.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| slotType | [notificationManager.SlotType](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#slottype) | No | No | 
Slot type of a continuous-task notification.

Note: After a continuous task is successfully requested or updated, no prompt tone is played.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| contentType | [notificationManager.ContentType](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md#contenttype) | No | No | 

Content type of a continuous-task notification.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| notificationId | number | No | No | 

ID of the continuous-task notification.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| continuousTaskId15+ | number | No | Yes | ID of a continuous task. |

#### ContinuousTaskCancelInfo15+

Describes the information about the cancellation of a continuous task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reason | [ContinuousTaskCancelReason](#continuoustaskcancelreason15) | No | No | Reason for canceling the continuous task. |
| id | number | No | No | ID of the continuous task canceled. |

#### ContinuousTaskCancelReason15+

Describes the reason for canceling a continuous task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| USER\_CANCEL | 1 | The task is canceled by the user. |
| SYSTEM\_CANCEL | 2 | The task is canceled by the system. |
| USER\_CANCEL\_REMOVE\_NOTIFICATION | 3 | User removal notification. This value is reserved. |
| SYSTEM\_CANCEL\_DATA\_TRANSFER\_LOW\_SPEED | 4 | A continuous task of the DATA\_TRANSFER type is requested, but the data transmission rate is low. This value is reserved. |
| SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION | 5 | A continuous task of the AUDIO\_PLAYBACK type is requested, but the [AVSession](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/avsession-overview) is not accessed. This value is reserved. |
| SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_RUNNING | 6 | A continuous task of the AUDIO\_PLAYBACK type is requested, but the audio and video are not played. This value is reserved. |
| SYSTEM\_CANCEL\_AUDIO\_RECORDING\_NOT\_RUNNING | 7 | A continuous task of the AUDIO\_RECORDING type is requested, but audio recording is not in progress. This value is reserved. |
| SYSTEM\_CANCEL\_NOT\_USE\_LOCATION | 8 | A continuous task of the LOCATION type is requested, but location and navigation are not used. This value is reserved. |
| SYSTEM\_CANCEL\_NOT\_USE\_BLUETOOTH | 9 | A continuous task of the BLUETOOTH\_INTERACTION type is requested, but Bluetooth-related services are not used. This value is reserved. |
| SYSTEM\_CANCEL\_NOT\_USE\_MULTI\_DEVICE | 10 | A continuous task of the MULTI\_DEVICE\_CONNECTION type is requested, but multi-device connection is not used. This value is reserved. |
| SYSTEM\_CANCEL\_USE\_ILLEGALLY | 11 | A continuous task of an invalid type is used. For example, a continuous task of the AUDIO\_PLAYBACK type is requested, but the audio and video playback and location and navigation services are used. This value is reserved. |

#### BackgroundSubMode16+

Defines the subtype of a continuous task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| CAR\_KEY | 1 | 
Car key.

**NOTE**

1\. The car key subtype takes effect only when a continuous task of the BLUETOOTH\_INTERACTION type is requested.

2\. Continuous tasks of this type cannot be updated through the [updateBackgroundRunning](#backgroundtaskmanagerupdatebackgroundrunning12) API.

 |

#### BackgroundModeType16+

Defines the type of a continuous task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| SUB\_MODE | 'subMode' | Subtype. |

#### ContinuousTaskSuspendInfo20+

Describes the information about continuous task suspension.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| continuousTaskId | number | No | No | ID of a suspended continuous task. |
| suspendState | boolean | No | No | Continuous task state. The value **false** indicates that the task is activated, and the value **true** indicates that the task is suspended. |
| suspendReason | [ContinuousTaskSuspendReason](#continuoustasksuspendreason20) | No | No | Reason why the continuous task is suspended. |

#### ContinuousTaskSuspendReason20+

Describes the reason why the continuous task is suspended.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| SYSTEM\_SUSPEND\_DATA\_TRANSFER\_LOW\_SPEED | 4 | A continuous task of the DATA\_TRANSFER type is requested, but the data transmission rate is low. |
| SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION | 5 | A continuous task of the AUDIO\_PLAYBACK type is requested, but the [AVSession](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/avsession-overview) is not accessed. |
| SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_RUNNING | 6 | A continuous task of the AUDIO\_PLAYBACK type is requested, but the audio and video are not played. |
| SYSTEM\_SUSPEND\_AUDIO\_RECORDING\_NOT\_RUNNING | 7 | A continuous task of the AUDIO\_RECORDING type is requested, but audio recording is not in progress. |
| SYSTEM\_SUSPEND\_LOCATION\_NOT\_USED | 8 | A continuous task of the LOCATION type is requested, but location and navigation are not used. |
| SYSTEM\_SUSPEND\_BLUETOOTH\_NOT\_USED | 9 | A continuous task of the BLUETOOTH\_INTERACTION type is requested, but Bluetooth-related services are not used. |
| SYSTEM\_SUSPEND\_MULTI\_DEVICE\_NOT\_USED | 10 | A continuous task of the MULTI\_DEVICE\_CONNECTION type is requested, but multi-device connection is not used. |
| SYSTEM\_SUSPEND\_USED\_ILLEGALLY | 11 | A continuous task of an invalid type is used. For example, a continuous task of the AUDIO\_PLAYBACK type is requested, but the audio and video playback and location and navigation services are used. This value is reserved. |
| SYSTEM\_SUSPEND\_SYSTEM\_LOAD\_WARNING | 12 | A continuous task is suspended due to high system load. This value is reserved. |

#### ContinuousTaskActiveInfo20+

Describes the activation information of a continuous task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | No | ID of the activated continuous task. |

#### ContinuousTaskInfo20+

Describes the continuous task information.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| abilityName | string | No | No | UIAbility name. |
| uid | number | No | No | Application UID. |
| pid | number | No | No | Application PID. |
| isFromWebView | boolean | No | No | Whether to request a continuous task in WebView mode, that is, whether to request a continuous task through the system proxy application. The value **true** indicates that the Webview mode is used, and the value **false** indicates that the Webview mode is not used. |
| backgroundModes | string\[\] | No | No | [Type of a continuous task](#backgroundmode). |
| backgroundSubModes | string\[\] | No | No | [Subtype of a continuous task](#backgroundsubmode16). |
| notificationId | number | No | No | Notification ID. |
| continuousTaskId | number | No | No | Continuous task ID. |
| abilityId | number | No | No | UIAbility ID. |
| wantAgentBundleName | string | No | No | Bundle name configured in [WantAgent](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md). **WantAgent** is a notification parameter used to specify the target page when a continuous task notification is tapped. |
| wantAgentAbilityName | string | No | No | Ability name configured in [WantAgent](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md). **WantAgent** is a notification parameter used to specify the target page when a continuous task notification is tapped. |
| suspendState | boolean | No | No | Whether the requested continuous task is suspended. The value **true** indicates that the task is suspended, and the value **false** indicates that the task is activated. |

#### ContinuousTaskRequest21+

Specifies details of the continuous task being requested or updated. It is typically used as input for the [startBackgroundRunning()](#backgroundtaskmanagerstartbackgroundrunning21) and [updateBackgroundRunning()](#backgroundtaskmanagerupdatebackgroundrunning21) APIs. Note that:

1.  When requesting a continuous task via [startBackgroundRunning()](#backgroundtaskmanagerstartbackgroundrunning21), notifications will be combined if the main type and subtype of the continuous task to be requested are the same as those of the existing continuous task in the current application, and the **combinedTaskNotification** value is **true** for both tasks. Otherwise, notifications will not be combined.
2.  Notifications will not be combined if the continuous task has no notification. For details about whether notifications are sent for the continuous task, see [BackgroundTaskMode](#backgroundtaskmode21).
3.  Notifications cannot be combined if the continuous task includes data transmission.
4.  Notifications that have been combined cannot be canceled. If notifications have been combined, they cannot be updated to uncombined.
5.  After notifications are combined, tapping the notification will redirect to the UIAbility corresponding to the first requested continuous task. If the update API is called, the redirection will target the UIAbility corresponding to the last updated continuous task.
6.  When the [updateBackgroundRunning()](#backgroundtaskmanagerupdatebackgroundrunning21) API is called to update a continuous task, the input **continuousTaskId** must exist. Otherwise, the update fails.
7.  Continuous tasks of the [MODE\_SPECIAL\_SCENARIO\_PROCESSING](#backgroundtaskmode21) type are supported since API version 22. This task type must be used independently and notifications cannot be combined. Specifically, when you request or update a continuous task, it must be of the **MODE\_SPECIAL\_SCENARIO\_PROCESSING** type. Otherwise, an error is returned.

#### \[h2\]Properties

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundTaskModes | [BackgroundTaskMode](#backgroundtaskmode21)\[\] | No | No | 
Main type of a continuous task.

Note: The main type must match the subtype.

 |
| backgroundTaskSubmodes | [BackgroundTaskSubmode](#backgroundtasksubmode21)\[\] | No | No | 

Subtype of a continuous task.

Note: The main type must match the subtype.

 |
| wantAgent | [WantAgent](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagent) | No | No | Notification parameters, which are used to specify the target page that is redirected to when a continuous task notification is clicked. |
| combinedTaskNotification | boolean | No | Yes | 

Whether to combine notifications. The value **true** means to combine notifications, and the value **false** (default) means the opposite.

Note: This property does not take effect in [updateBackgroundRunning](#backgroundtaskmanagerupdatebackgroundrunning21) API. If notifications need to be combined for an existing task, request the task again and set the value to **true**.

 |
| continuousTaskId | number | No | Yes | 

Continuous task ID. The default value is **\-1**.

Note: If **combinedTaskNotification** is set to true, this property is mandatory and the corresponding ID must exist.

Additionally, this property is mandatory (with the corresponding ID required) when used as an input parameter for the [updateBackgroundRunning](#backgroundtaskmanagerupdatebackgroundrunning21) API.

You can call the [getAllContinuousTasks](#backgroundtaskmanagergetallcontinuoustasks20-1) API to view information about all continuous tasks.

 |

#### \[h2\]isModeSupported21+

isModeSupported(): boolean

Checks whether **BackgroundTaskMode** specified in [ContinuousTaskRequest](#continuoustaskrequest21) is supported. For details, see [BackgroundTaskMode](#backgroundtaskmode21).

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether **BackgroundTaskMode** is supported. The value **true** means it is supported, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let isModeSupported: boolean = false;
    let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
    let modeList: Array<number> = \[backgroundTaskManager.BackgroundTaskMode.MODE\_TASK\_KEEPING\];
    continuousTaskRequest.backgroundTaskModes = modeList;
    try {
      isModeSupported = continuousTaskRequest.isModeSupported();
      console.info(\`Operation isModeSupported succeeded. isModeSupported is ${isModeSupported}\`);
    } catch (error) {
      console.error(\`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### \[h2\]requestAuthFromUser22+

requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void

Requests user authorization to run tasks continuously in the background. This API uses an asynchronous callback to return the result. If the API call is successful, a banner notification with a sound is sent. This API is applicable only to continuous tasks of the [MODE\_SPECIAL\_SCENARIO\_PROCESSING](#backgroundtaskmode21) type.

**Model restriction**: This API can be used only in the stage model.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Device behavior differences**: This API can be properly called on smartphones, tablets, and PCs/2-in-1 devices. If it is called on other devices, error code 9800005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |
| callback | Callback<[UserAuthResult](#userauthresult22)\> | Yes | Callback used to return the user authorization result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callbackAuth(authResult: backgroundTaskManager.UserAuthResult) {
  console.info('Operation requestAuthFromUser success. auth result: ' + JSON.stringify(authResult));
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
    let modeList: Array<number> = \[backgroundTaskManager.BackgroundTaskMode.MODE\_SPECIAL\_SCENARIO\_PROCESSING\];
    continuousTaskRequest.backgroundTaskModes = modeList;
    let subModeList: Array<number> = \[backgroundTaskManager.BackgroundTaskSubmode.SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION\];
    continuousTaskRequest.backgroundTaskSubmodes = subModeList;
    try {
      continuousTaskRequest.requestAuthFromUser(this.context, callbackAuth);
      console.info('Operation requestAuthFromUser succeeded.');
    } catch (error) {
      console.error(\`Operation requestAuthFromUser failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### \[h2\]checkSpecialScenarioAuth22+

checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>

Checks whether the user has authorized tasks to run continuously in the background. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Device behavior differences**: This API can be properly called on smartphones, tablets, and PCs/2-in-1 devices. If it is called on other devices, error code 9800005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

Note: Continuous tasks can be requested only by the UIAbility in the stage model and the ServiceAbility in the FA model.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UserAuthResult](#userauthresult22)\> | Promise used to return the user authorization result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [backgroundTaskManager Error Codes](../../error-codes/backgroundtaskmanager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**Example**

import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    try {
      let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
      continuousTaskRequest.checkSpecialScenarioAuth(this.context).then((res: backgroundTaskManager.UserAuthResult) => {
        console.info('Operation checkSpecialScenarioAuth succeeded. data: ' + JSON.stringify(res));
      }).catch((error: BusinessError) => {
        console.error(\`Operation checkSpecialScenarioAuth failed. code is ${error.code} message is ${error.message}\`);
      });
    } catch (error) {
      console.error(\`Operation checkSpecialScenarioAuth failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
    }
  }
};

#### BackgroundTaskMode21+

Main type of a continuous task. It is usually used together with the subtype [BackgroundTaskSubmode](#backgroundtasksubmode21). For details, see the mapping table. The two types are newly added in API version 21 for [requesting](#backgroundtaskmanagerstartbackgroundrunning21) and [updating](#backgroundtaskmanagerupdatebackgroundrunning21) continuous tasks.

When the main type of the continuous task is **MODE\_SPECIAL\_SCENARIO\_PROCESSING**, or that of a non-PC/2-in-1 device is **MODE\_TASK\_KEEPING**, you need to request the ACL permission [ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionkeep_background_running_system) before calling APIs related to continuous tasks. In other scenarios, this permission is not required.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| MODE\_DATA\_TRANSFER | 1 | 
Data transfer.

Use scenario: upload and download in non-hosting mode, for example, uploading or downloading data in the background of a browser.

**NOTE**

1\. During data transfer, the application needs to update the progress. If the progress is not updated for more than 10 minutes, the continuous task of the **DATA\_TRANSFER** type will be canceled.

2\. The notification type of the progress update must be live view. For details, see the example in [startBackgroundRunning()](#backgroundtaskmanagerstartbackgroundrunning12).

 |
| MODE\_AUDIO\_PLAYBACK | 2 | 

Audio and video playback.

Use scenario: audio/video playback in the background and audio/video casting.

Note: If a continuous task of the **MODE\_AUDIO\_PLAYBACK** type is requested or updated without connecting to AVSession, a notification will appear in the notification panel once the task is successfully requested or updated. Once AVSession is connected, notifications will be sent by AVSession instead of the background task module.

 |
| MODE\_AUDIO\_RECORDING | 3 | 

Audio recording.

Use scenario: recording and screen capture in the background.

 |
| MODE\_LOCATION | 4 | Positioning and navigation. |
| MODE\_BLUETOOTH\_INTERACTION | 5 | 

Bluetooth-related services.

Use scenario: An application moves to the background while transferring files via Bluetooth.

 |
| MODE\_MULTI\_DEVICE\_CONNECTION | 6 | 

Multi-device connection.

Use scenario: distributed service connection and casting.

 |
| MODE\_VOIP | 8 | 

Audio and video calls.

Use scenario: Chat applications (with audio and video services) transition into the background during audio and video calls.

 |
| MODE\_TASK\_KEEPING | 9 | 

Computing tasks.

Use scenario: antivirus software.

Note: This capability is available only to PCs/2-in-1 devices, or non-PCs/2-in-1 devices that have obtained the ACL permission [ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionkeep_background_running_system).

 |
| MODE\_AV\_PLAYBACK\_AND\_RECORD22+ | 12 | 

Multimedia services.

Use scenarios: audio/video playback, recording, and audio/video calls. The scenario must match that of the subtype. You can select this task type or the corresponding main type for preceding scenarios. For example, you can request a continuous task of the **MODE\_AUDIO\_PLAYBACK** or **MODE\_AV\_PLAYBACK\_AND\_RECORD** type for audio/video playback.

 |
| MODE\_SPECIAL\_SCENARIO\_PROCESSING22+ | 13 | 

Special scenarios (available only for smartphones, tablets, PCs/2-in-1 devices).

Use scenarios: An application exports media files in the background or uses a third-party component to cast content in the background. The scenario must match that of the subtype.

**NOTE**

1\. If an application needs to run in the background for a long time, it can request user authorization through the [requestAuthFromUser](#requestauthfromuser22) API and check the authorization result via [checkSpecialScenarioAuth](#checkspecialscenarioauth22).

2\. This capability is available only to applications that have obtained the ACL permission [ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionkeep_background_running_system).

3\. This task type must be used independently and notifications cannot be combined. Specifically, when you request or update a continuous task, it must be of the **MODE\_SPECIAL\_SCENARIO\_PROCESSING** type. Otherwise, an error is returned.

 |

#### BackgroundTaskSubmode21+

Defines the subtype of a continuous task. It is usually used together with the main type [BackgroundTaskMode](#backgroundtaskmode21). For details, see the mapping table. The two types are newly added in API version 21 for requesting and updating continuous tasks.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| SUBMODE\_CAR\_KEY\_NORMAL\_NOTIFICATION | 1 | **CAR\_KEY** type. It is of the normal text notification type. |
| SUBMODE\_NORMAL\_NOTIFICATION | 2 | Normal text notification. |
| SUBMODE\_LIVE\_VIEW\_NOTIFICATION | 3 | Live view notification. |
| SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION22+ | 4 | Audio and video playback. It is of the normal text notification type. You can access [AVSession](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/avsession-overview) as needed. |
| SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK22+ | 5 | Audio and video playback scenario where [AVSession](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/avsession-overview) is accessed. It is of the normal text notification type. |
| SUBMODE\_AUDIO\_RECORD\_NORMAL\_NOTIFICATION22+ | 6 | Recording. It is of the normal text notification type. |
| SUBMODE\_SCREEN\_RECORD\_NORMAL\_NOTIFICATION22+ | 7 | Recording. It is of the normal text notification type. |
| SUBMODE\_VOICE\_CHAT\_NORMAL\_NOTIFICATION22+ | 8 | Call. It is of the normal text notification type. |
| SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION22+ | 9 | Media processing. For example, an application exports media files in the background. It is of the normal text notification type. |
| SUBMODE\_VIDEO\_BROADCAST\_NORMAL\_NOTIFICATION22+ | 10 | Video casting. For example, an application uses a third-party casting component to cast a video in the background, and the notification type is common text notification. |

Mapping table of main types and subtypes of continuous tasks

| [Main Type](#backgroundtaskmode21) | [Subtype](#backgroundtasksubmode21) |
| :-- | :-- |
| MODE\_DATA\_TRANSFER | SUBMODE\_LIVE\_VIEW\_NOTIFICATION |
| MODE\_AUDIO\_PLAYBACK | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_AUDIO\_RECORDING | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_LOCATION | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_BLUETOOTH\_INTERACTION | 
SUBMODE\_NORMAL\_NOTIFICATION

SUBMODE\_CAR\_KEY\_NORMAL\_NOTIFICATION

 |
| MODE\_MULTI\_DEVICE\_CONNECTION | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_VOIP | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_TASK\_KEEPING | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_AV\_PLAYBACK\_AND\_RECORD22+ | 

SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION22+

SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK22+

SUBMODE\_AUDIO\_RECORD\_NORMAL\_NOTIFICATION22+

SUBMODE\_SCREEN\_RECORD\_NORMAL\_NOTIFICATION22+

SUBMODE\_VOICE\_CHAT\_NORMAL\_NOTIFICATION22+

 |
| MODE\_SPECIAL\_SCENARIO\_PROCESSING22+ | 

SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION22+

SUBMODE\_VIDEO\_BROADCAST\_NORMAL\_NOTIFICATION22+

 |

#### UserAuthResult22+

Represents the user authorization result.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| Name | Value | Description |
| :-- | :-- | :-- |
| NOT\_SUPPORTED | 0 | The authorization is not supported. For example, if the main type of the requested continuous task is not **MODE\_SPECIAL\_SCENARIO\_PROCESSING**, continuous task running in the background is not supported. |
| NOT\_DETERMINED | 1 | No user operation. |
| DENIED | 2 | The authorization is denied. |
| GRANTED\_ONCE | 3 | 
The authorization is granted this time.

Note: The authorization record will be cleared when the application exits.

 |
| GRANTED\_ALWAYS | 4 | 

The authorization is granted always.

**NOTE**

When the following common events are received, the related authorization records will be cleared:

[COMMON\_EVENT\_PACKAGE\_ADDED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_package_added), [COMMON\_EVENT\_PACKAGE\_REMOVED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_package_removed), [COMMON\_EVENT\_BUNDLE\_REMOVED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_bundle_removed), [COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_package_fully_removed), [COMMON\_EVENT\_PACKAGE\_CHANGED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_package_changed)

 |
