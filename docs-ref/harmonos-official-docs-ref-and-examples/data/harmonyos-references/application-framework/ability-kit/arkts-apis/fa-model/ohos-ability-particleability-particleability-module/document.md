# @ohos.ability.particleAbility (ParticleAbility Module)

The particleAbility module provides APIs for operating a DataAbility and ServiceAbility. You can use the APIs to start and terminate a ParticleAbility, obtain a dataAbilityHelper object, and connect to or disconnect from a ServiceAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/1HsHkpVvSoKRKDFPGeUMRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3CF64A0DBA37F005F84887F34DB82F26CE91C940203D4230D5B7D7604F39577)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Constraints

The ParticleAbility module is used to perform operations on abilities of the Data and Service types.

#### Modules to Import

import { particleAbility } from '@kit.AbilityKit';

#### particleAbility.startAbility

startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<void>): void

Starts a ParticleAbility. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/yUJGaXdSS8q1qWWn_qQFVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=182CA647B50373644C7ABF64DD692AFFCC6F74B270090F64F393B4017C9BBB0D)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](../ability/startabilityparameter/document.md) | Yes | Ability to start. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the ParticleAbility is started, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { particleAbility, wantConstant } from '@kit.AbilityKit';

particleAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.Data',
      abilityName: 'com.example.Data.EntryAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(\`startAbility fail, error: ${JSON.stringify(error)}\`);
    } else {
      console.info(\`startAbility success, data: ${JSON.stringify(data)}\`);
    }
  },
);

#### particleAbility.startAbility

startAbility(parameter: StartAbilityParameter): Promise<void>

Starts a ParticleAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/vSy2-MzvRkC-HPH2wlsriQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1D1C4793152DB77B40CB71D845AB71E9422258D7D5F8C173DF8E967B55E2CF7)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](../ability/startabilityparameter/document.md) | Yes | Ability to start. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Example**

import { particleAbility, wantConstant } from '@kit.AbilityKit';

particleAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.Data',
      abilityName: 'com.example.Data.EntryAbility',
      uri: ''
    },
  },
).then(() => {
  console.info('particleAbility startAbility');
});

#### particleAbility.terminateSelf

terminateSelf(callback: AsyncCallback<void>): void

Terminates this ParticleAbility. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the ParticleAbility is terminated, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf(
  (error) => {
    if (error && error.code !== 0) {
      console.error(\`terminateSelf fail, error: ${JSON.stringify(error)}\`);
    }
  }
);

#### particleAbility.terminateSelf

terminateSelf(): Promise<void>

Terminates this ParticleAbility. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Example**

import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf().then(() => {
  console.info('particleAbility terminateSelf');
});

#### particleAbility.acquireDataAbilityHelper

acquireDataAbilityHelper(uri: string): DataAbilityHelper

Obtains a dataAbilityHelper object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/vVU6slpfQhOs_R_9rI_bLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66CCB7CE96792B11FFE24AD6FE99B92855AEF7C7B768C6B60E49D97F34A0D282)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

To access a DataAbility of another application, the target application must be configured with associated startup (**AssociateWakeUp** set to **true**).

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to open. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityHelper](../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | A utility class used to help other abilities access a DataAbility. |

**Example**

import { particleAbility } from '@kit.AbilityKit';

let uri = '';
particleAbility.acquireDataAbilityHelper(uri);

#### particleAbility.startBackgroundRunning(deprecated)

startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void

Requests a continuous task from the system. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/WFv6AxgQTEKgkZ3PQ6AcCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A34A7EE80C57C5403955FFD7ED392212EACB57186C6259C899BDD25B4AF0A04E)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [backgroundTaskManager.startBackgroundRunning](../../../../background-tasks-kit/arkts-apis/ohos-resourceschedule-backgroundtaskmanager-background-task-management/document.md#backgroundtaskmanagerstartbackgroundrunning) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID of the continuous task. |
| request | [NotificationRequest](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#notificationrequest) | Yes | Notification parameter, which is used to display information in the notification bar. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the continuous task is requested, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { particleAbility, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import notification from '@ohos.notification';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(\`Operation failed error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`Operation succeeded, data: ${data}\`);
  }
}

let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: \[
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  \],
  operationType: wantAgent.OperationType.START\_ABILITY,
  requestCode: 0,
  wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let id = 1;
  particleAbility.startBackgroundRunning(id, {
    content:
    {
      contentType: notification.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
      normal:
      {
        title: 'title',
        text: 'text'
      }
    },
    wantAgent: wantAgentObj
  }, callback);
});

#### particleAbility.startBackgroundRunning(deprecated)

startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>

Requests a continuous task from the system. This API uses a promise to return the result.

**Required permissions**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/4D1cyJ9VRAi4ROAJfXiAaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FA78DEB21CC062043019721DBCF54905B1BD3E3617F61D8F3FD7910BDDA51D0)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [backgroundTaskManager.startBackgroundRunning](../../../../background-tasks-kit/arkts-apis/ohos-resourceschedule-backgroundtaskmanager-background-task-management/document.md#backgroundtaskmanagerstartbackgroundrunning-1) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Notification ID of the continuous task. |
| request | [NotificationRequest](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md#notificationrequest) | Yes | Notification parameter, which is used to display information in the notification bar. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Example**

import { particleAbility, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import notification from '@ohos.notification';

let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: \[
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  \],
  operationType: wantAgent.OperationType.START\_ABILITY,
  requestCode: 0,
  wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let id = 1;
  particleAbility.startBackgroundRunning(id, {
    content:
    {
      contentType: notification.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
      normal:
      {
        title: 'title',
        text: 'text'
      }
    },
    wantAgent: wantAgentObj
  }).then(() => {
    console.info('Operation succeeded');
  }).catch((err: BusinessError) => {
    console.error(\`Operation failed cause: ${JSON.stringify(err)}\`);
  });
});

#### particleAbility.cancelBackgroundRunning(deprecated)

cancelBackgroundRunning(callback: AsyncCallback<void>): void

Requests to cancel a continuous task from the system. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/u8O8z_gBSseNyfkOvK6L4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFACB7D322084A27BE2E8FA4684272D364258B195416AEF35F2BC96B2B90A1B6)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [backgroundTaskManager.stopBackgroundRunning](../../../../background-tasks-kit/arkts-apis/ohos-resourceschedule-backgroundtaskmanager-background-task-management/document.md#backgroundtaskmanagerstopbackgroundrunning) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the continuous task is canceled, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(\`Operation failed error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`Operation succeeded, data: ${data}\`);
  }
}

particleAbility.cancelBackgroundRunning(callback);

#### particleAbility.cancelBackgroundRunning(deprecated)

cancelBackgroundRunning(): Promise<void>

Requests to cancel a continuous task from the system. This API uses a promise to return the result.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/srxrGTm3T066HoXBzAXMeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68526142E9EF5211FDA21FAE8033931062FEDFB45061267EF5AAB5F878258746)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [backgroundTaskManager.stopBackgroundRunning](../../../../background-tasks-kit/arkts-apis/ohos-resourceschedule-backgroundtaskmanager-background-task-management/document.md#backgroundtaskmanagerstopbackgroundrunning-1) instead.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Example**

import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

particleAbility.cancelBackgroundRunning().then(() => {
  console.info('Operation succeeded');
}).catch((err: BusinessError) => {
  console.error(\`Operation failed cause: ${JSON.stringify(err)}\`);
});

#### particleAbility.connectAbility

connectAbility(request: Want, options:ConnectOptions): number

Connects this ability to a ServiceAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/XoeRf3fVT_O7ASt54zZD1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E2416F86F8FC328ACAE0742054C8F4C3AD135E8B2EF518BDD66829A7E35473A)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

To connect to a ServiceAbility of another application, the target application must be configured with associated startup (**AssociateWakeUp** set to **true**).

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [Want](../../apis-no-longer-maintained/ohos-application-want-want/document.md) | Yes | ServiceAbility to connect. |
| options | [ConnectOptions](../../dependent-elements-and-definitions/ability/connectoptions/document.md) | Yes | Connection options. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | ID of the connected ServiceAbility. The ID starts from 0 and is incremented by 1 each time a connection is set up. |

**Example**

import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(\`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}\`);
    },
    onDisconnect: (element) => {
      console.info(\`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}\`);
    },
    onFailed: (code) => {
      console.error(\`particleAbilityTest ConnectAbility onFailed errCode: ${code}\`);
    },
  },
);

particleAbility.disconnectAbility(connId).then((data) => {
  console.info(\`data: ${data}\`);
}).catch((error: BusinessError) => {
  console.error(\`particleAbilityTest result errCode: ${error.code}\`);
});

#### particleAbility.disconnectAbility

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

Disconnects this ability from a specific ServiceAbility. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the ServiceAbility to disconnect. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the disconnection is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(\`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}\`);
    },
    onDisconnect: (element) => {
      console.info(\`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}\`);
    },
    onFailed: (code) => {
      console.error(\`particleAbilityTest ConnectAbility onFailed errCode: ${code}\`);
    },
  },
);

particleAbility.disconnectAbility(connId, (err) => {
  console.error(\`particleAbilityTest disconnectAbility err: ${JSON.stringify(err)}\`);
});

#### particleAbility.disconnectAbility

disconnectAbility(connection: number): Promise<void>

Disconnects this ability from a specific ServiceAbility. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the ServiceAbility to disconnect. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Example**

import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(\`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}\`);
    },
    onDisconnect: (element) => {
      console.info(\`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}\`);
    },
    onFailed: (code) => {
      console.error(\`particleAbilityTest ConnectAbility onFailed errCode: ${code}\`);
    },
  },
);

particleAbility.disconnectAbility(connId).then(() => {
  console.info('disconnectAbility success');
}).catch((error: BusinessError) => {
  console.error(\`particleAbilityTest result errCode : ${error.code}\`);
});

#### ErrorCode

Enumerates the error codes that may be returned when an ability is started.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Value | Description |
| :-- | :-- | :-- |
| INVALID\_PARAMETER | \-1 | Invalid parameter. |
