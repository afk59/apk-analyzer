# @ohos.app.ability.sendableContextManager (Sendable Context Management)

The sendableContextManager module provides APIs for converting between Context and [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/GC98Y7aPSVeX-2lqQmgdvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE5820D984A70D1591EBAB6601594119A238A64CBA0E24DC4827F270B14DB45F)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### When to Use

This module is used to transfer data between concurrent ArkTS instances (including the main thread and the worker thread of TaskPool or Worker).

When the main thread transfers sendable data (data that complies with the [Sendable protocol](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-protocol)) to the child thread (such as the TaskPool or Worker thread), the conversion between the Context and SendableContext is required. The process is as follows:

-   Conversion from Context to SendableContext for the main thread to transfer sendable data to the child thread.
-   Conversion from SendableContext to Context for the child thread to use the sendable data.

The Context here is different from that created by [createModuleContext](../ohos-app-ability-application-application-utility-class/document.md#applicationcreatemodulecontext). The differences are as follows:

-   Context involved in the conversion: ArkTS concurrent instances hold different application-side Context instances that correspond to the same underlying Context object. When the Context properties and methods in an instance are modified, the Context properties and methods in the related instances are modified accordingly. The eventHub attribute in the Context instance is special. The eventHub objects in different instances are independent of each other and cannot be used across ArkTS instances. If you want to use [EventHub](../../dependent-elements-and-definitions/application/eventhub/document.md) to transfer data across instances, call [setEventHubMultithreadingEnabled](#sendablecontextmanagerseteventhubmultithreadingenabled20) to enable the cross-thread data transfer feature.
    
-   Context created using [createModuleContext](../ohos-app-ability-application-application-utility-class/document.md#applicationcreatemodulecontext): ArkTS concurrent instances hold different application-side Context instances that correspond to different underlying Context objects.
    

#### Constraints

The Context types used in the conversion must be the same. For example, if the main thread uses [convertFromContext](#sendablecontextmanagerconvertfromcontext) to convert the [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) to the SendableContext, the child thread must call [convertToUIAbilityContext](#sendablecontextmanagerconverttouiabilitycontext) to convert the received SendableContext to the [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md).

Currently, the following types of Context support conversion: [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md), [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md), [AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md), and [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md).

#### Modules to Import

import { sendableContextManager } from '@kit.AbilityKit';

#### SendableContext

type SendableContext = \_SendableContext

Defines the Sendable context. It complies with the [Sendable protocol](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-protocol) and inherits from [lang.ISendable](../../../../arkts/arkts-apis/arkts-lang-arkts-base-capability/document.md#langisendable).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [\_SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) | Sendable context, which can be converted to a Context object to implement data transmission between concurrent ArkTS instances (including the main thread and the worker thread of TaskPool or Worker). |

#### sendableContextManager.convertFromContext

convertFromContext(context: common.Context): SendableContext

Converts a Context object to a SendableContext object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context object. The Context base class, and its child classes [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md), [AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md), and [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) are supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| SendableContext | [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

import { AbilityConstant, UIAbility, Want, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext) {
    this.sendableContext = sendableContext;
  }

  sendableContext: sendableContextManager.SendableContext;
  // other sendable object
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext);
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
  }
}

#### sendableContextManager.convertToContext

convertToContext(sendableContext: SendableContext): common.Context

Converts a SendableContext object to a Context object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sendableContext | [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) | Yes | SendableContext object. |

**Return value**

| Type | Description |
| :-- | :-- |
| common.Context | [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

Context passed by the main thread:

import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let context: common.Context = this.context as common.Context;
      let sendableContext: sendableContextManager.SendableContext = sendableContextManager.convertFromContext(context);
      let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
  }
}

Context received by the Worker thread:

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'BaseContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to context.');
    try {
      let context: common.Context = sendableContextManager.convertToContext(sendableContext);
      // Obtain the sandbox path after obtaining the Context object.
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToContext failed %{public}s', JSON.stringify(error));
    }
  }
}

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}

#### sendableContextManager.convertToApplicationContext

convertToApplicationContext(sendableContext: SendableContext): common.ApplicationContext

Converts a SendableContext object to an ApplicationContext object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sendableContext | [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) | Yes | SendableContext object. |

**Return value**

| Type | Description |
| :-- | :-- |
| common.ApplicationContext | [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

Context passed by the main thread:

import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let context: common.Context = this.context as common.Context;
      let applicationContext = context.getApplicationContext();
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(applicationContext);
      let object: SendableObject = new SendableObject(sendableContext, 'ApplicationContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
  }
}

Context received by the Worker thread:

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'ApplicationContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to application context.');
    try {
      let context: common.ApplicationContext = sendableContextManager.convertToApplicationContext(sendableContext);
      // Obtain the sandbox path after obtaining the Context object.
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToApplicationContext failed %{public}s', JSON.stringify(error));
    }
  }
}

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}

#### sendableContextManager.convertToAbilityStageContext

convertToAbilityStageContext(sendableContext: SendableContext): common.AbilityStageContext

Converts a SendableContext object to an AbilityStageContext object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sendableContext | [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) | Yes | SendableContext object. |

**Return value**

| Type | Description |
| :-- | :-- |
| common.AbilityStageContext | [AbilityStageContext](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

Context passed by the main thread:

import { UIAbility, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext, 'AbilityStageContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
  }
}

Context received by the Worker thread:

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'AbilityStageContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to abilitystage context.');
    try {
      let context: common.AbilityStageContext = sendableContextManager.convertToAbilityStageContext(sendableContext);
      // Obtain the sandbox path after obtaining the Context object.
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToAbilityStageContext failed %{public}s', JSON.stringify(error));
    }
  }
}

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}

#### sendableContextManager.convertToUIAbilityContext

convertToUIAbilityContext(sendableContext: SendableContext): common.UIAbilityContext

Converts a SendableContext object to a UIAbilityContext object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sendableContext | [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) | Yes | SendableContext object. |

**Return value**

| Type | Description |
| :-- | :-- |
| common.UIAbilityContext | [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

Context passed by the main thread:

import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

export default class EntryAbility extends UIAbility {
  worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // convert and post
    try {
      let sendableContext: sendableContextManager.SendableContext =
        sendableContextManager.convertFromContext(this.context);
      let object: SendableObject = new SendableObject(sendableContext, 'EntryAbilityContext');
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
      this.worker.postMessageWithSharedSendable(object);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertFromContext failed %{public}s', JSON.stringify(error));
    }
  }
}

Context received by the Worker thread:

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'EntryAbilityContext') {
    hilog.info(0x0000, 'testTag', '%{public}s', 'convert to UIAbility context.');
    try {
      let context: common.UIAbilityContext = sendableContextManager.convertToUIAbilityContext(sendableContext);
      // Obtain the sandbox path after obtaining the Context object.
      hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'convertToUIAbilityContext failed %{public}s', JSON.stringify(error));
    }
  }
}

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
}

workerPort.onerror = (e: ErrorEvent) => {
  hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
}

#### sendableContextManager.setEventHubMultithreadingEnabled20+

setEventHubMultithreadingEnabled(context: common.Context, enabled: boolean): void

Enables the cross-thread data transfer feature of [EventHub](../../dependent-elements-and-definitions/application/eventhub/document.md) in [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/xv14DC63T0qe6Pvy-GWJJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E234828DA1576F3F84711ADE5BECBD96019476EEB71650AC5962AF326E194914)

-   When multiple Context objects communicate, you need to call this API to set each Context object to support EventHub cross-thread data transfer.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Context object. For details about the serialization data types supported by Eventhub, see [Sequenceable Data Types](../../../../arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md#sequenceable-data-types). The data size cannot exceed 16 MB. |
| enabled | boolean | Yes | 
Whether to enable the cross-thread data transfer feature.

\- **true**: The cross-thread data transfer feature is enabled, and data is passed by reference.

\- **false**: The cross-thread data transfer feature is disabled. Data is passed through serialization, which means that the data of the sender thread is independent of that of the receiver thread.

 |

**Example**

Enable the cross-thread data transfer feature of [EventHub](../../dependent-elements-and-definitions/application/eventhub/document.md) in a [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) object on the main thread, convert the **Context** object to a [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) object, and send the **SendableContext** object to the [Worker](../../../../arkts/arkts-apis/ohos-worker-starting-the-worker/document.md) thread.

import { common, sendableContextManager } from '@kit.AbilityKit';
import { worker } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

@Entry
@Component
struct Index {
  @State context: common.Context | undefined = this.getUIContext().getHostContext();
  worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

  aboutToAppear(): void {
    let context: common.Context = this.context as common.Context;
    context.eventHub.on('event1', this.eventFunc);
    context.eventHub.emit('event1', 'xingming', 22);
  }

  eventFunc(name: string, age: number) {
    hilog.info(DOMAIN, 'testTag', 'name %{public}s age %{public}d', name, age);
  }

  build() {
    Column() {
      Row() {
        Button('thread 1')
          .size({ width: 100, height: 100 })
          .onClick(() => {
            if (this.context == undefined) {
              return;
            }
            sendableContextManager.setEventHubMultithreadingEnabled(this.context, true);
            let sendableContext: sendableContextManager.SendableContext =
              sendableContextManager.convertFromContext(this.context);
            let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
            this.worker1.postMessageWithSharedSendable(object);
          })
      }
    }
  }
}

After receiving the [SendableContext](../../dependent-elements-and-definitions/application/sendablecontext/document.md) object on the [Worker](../../../../arkts/arkts-apis/ohos-worker-starting-the-worker/document.md) thread, convert it to a [Context](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) object. Then, enable the cross-thread data transfer feature of [EventHub](../../dependent-elements-and-definitions/application/eventhub/document.md) in the Context object on the Worker thread, and send a message back to the main thread using this feature.

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { common, sendableContextManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = e.data;
  let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
  if (object.contextName == 'BaseContext') {
    let context: common.Context = sendableContextManager.convertToContext(sendableContext);
    sendableContextManager.setEventHubMultithreadingEnabled(context, true);
    context.eventHub.emit('event1', 'xingming', 40);
  }
};

workerPort.onmessageerror = (e: MessageEvents) => {
  hilog.error(DOMAIN, 'testTag', '%{public}s', 'onmessageerror');
};

workerPort.onerror = (e: ErrorEvent) => {
  hilog.error(DOMAIN, 'testTag', '%{public}s', 'onerror');
};
