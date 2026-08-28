# @ohos.app.ability.UIAbility (Ability with UI)

UIAbility is an application component that has the UI. It inherits from [Ability](../ohos-app-ability-ability-ability-base-class/document.md) and provides [lifecycle](#uiability-lifecycle-states) callbacks such as component creation, destruction, and foreground/background switching. It also provides the [background communication capability](#background-communication-capability).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/wdXuUuv_Q3ibJhINXNqdAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFB7E843D7BFB7CA1587BAE10900D158FF5ABF0AE7343FCA662F5E768FCE7F35)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

For details about the inheritance relationship of each ability, see [Inheritance Relationship](../ohos-app-ability-ability-ability-base-class/document.md#ability-inheritance-relationship).

#### UIAbility Lifecycle States

**Figure 1** UIAbility lifecycle states

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/hF4Lll_mRUaDx9ctCeBvLw/en-us_image_0000002537925250.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADF7B5B35CB8265CA9912FB3CF48D57FF345C77C9DBEB1E588C957FF54643018)

-   **Create**: A UIAbility instance has been created. The system triggers the [onCreate](#oncreate) callback in this state, where you can perform initialization operations.
-   **Foreground**: The UIAbility has been brought to the foreground. The system triggers the [onForeground](#onforeground) callback in this state, where you can request resources required by the application.
-   **Background**: The UIAbility has been moved to the background. The system triggers the [onBackground](#onbackground) callback in this state, where you can release some application resources.
-   **Destroy**: The UIAbility instance is about to be destroyed. The system triggers the [onDestroy](#ondestroy) callback in this state, where you can save data.

#### Background Communication Capability

**Call** invocations can be used for background communication with the target UIAbility. The following figure shows the Call invocation.

**Figure 2** Diagram of Call invocation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/eRAI5QC7T-ufQo8XXyH7ww/en-us_image_0000002537764348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B9933792D62EE50724E58086BEB2710F76F36784523822320F0ED7C6D09B638)

-   The Caller UIAbility uses [startAbilityByCall()](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startabilitybycall) to obtain a [Caller](#caller) object and then uses the [call](#call) API of the Caller object to send data to the Callee UIAbility.
    
-   The Callee UIAbility holds a [Callee](#callee) object and uses the [on](#on) API of the Callee object to register a callback function for receiving data sent by the Caller object.
    

#### Modules to Import

import { UIAbility } from '@kit.AbilityKit';

#### UIAbility

Application component that has the UI. It provides lifecycle callbacks such as component creation, destruction, and foreground/background switching, and supports background communication.

#### \[h2\]Properties

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) | No | No | 
Context of the UIAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| launchWant | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | No | No | 

Want in the request used to [cold start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-intra-device-interaction#cold-starting-uiability) the UIAbility. The value is the Want received in [onCreate](#oncreate).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| lastRequestWant | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | No | No | 

Want in the most recent request to launch the UIAbility.

\- On the first launch of a UIAbility, it is the Want parameter received in [onCreate](#oncreate).

\- On subsequent launches, it is the most recent Want received in [onNewWant](#onnewwant).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| callee | [Callee](#callee) | No | No | Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object. |

#### \[h2\]onCreate

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void

Called when a UIAbility instance is created. You can execute initialization logic (such as defining variables and loading resources) in this callback. This callback is invoked during a [cold start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-intra-device-interaction#cold-starting-uiability) of the UIAbility.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Data passed by the caller when launching the UIAbility. |
| launchParam | [AbilityConstant.LaunchParam](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#launchparam) | Yes | Parameters for application launch, including the reason for application launch and the reason for the last application exit. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // Execute an asynchronous task.
    hilog.info(0x0000, 'testTag',
      \`onCreate, want: ${want.abilityName}, the launchReason is ${launchParam.launchReason}, the lastExitReason is ${launchParam.lastExitReason}\`);
  }
}

#### \[h2\]onWindowStageCreate

onWindowStageCreate(windowStage: window.WindowStage): void

Called when a [WindowStage](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md) instance is created. You can load a page through the WindowStage instance in this callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowStage | [window.WindowStage](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md) | Yes | WindowStage instance. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  // The main window has been created. Set the main page for the UIAbility.
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(0x0000, 'testTag', \`Succeeded in loading the content. Data: ${JSON.stringify(data)}\`);
    });
  }
}

#### \[h2\]onWindowStageWillDestroy12+

onWindowStageWillDestroy(windowStage: window.WindowStage): void

Called when the WindowStage instance is about to be destroyed. You can cancel the listening of WindowStage events in this lifecycle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowStage | [window.WindowStage](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md) | Yes | WindowStage instance. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  onWindowStageWillDestroy(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', \`onWindowStageWillDestroy\`);
  }
}

#### \[h2\]onWindowStageDestroy

onWindowStageDestroy(): void

Called when the WindowStage instance has been destroyed. It informs applications that the WindowStage instance is no longer available for use.

The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits (for example, process termination due to low memory conditions).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onWindowStageDestroy() {
    // The main window is destroyed. It is time to release UI resources.
    hilog.info(0x0000, 'testTag', \`onWindowStageDestroy\`);
  }
}

#### \[h2\]onWindowStageRestore

onWindowStageRestore(windowStage: window.WindowStage): void

Called when the page stack is restored for the target UIAbility during cross-device migration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/42y5WHaPQXeJXeVoR-eeOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67428D96309C2563EDA61E627121AAADD44340C87F69B54A93EF0AE0968621DE)

When an application is launched as a result of a migration, the **onWindowStageRestore()** lifecycle callback function, rather than **onWindowStageCreate()**, is triggered following [onCreate()](#oncreate) or [onNewWant()](#onnewwant). This sequence occurs for both [cold start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-intra-device-interaction#cold-starting-uiability) and [hot start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-intra-device-interaction#hot-starting-uiability).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowStage | [window.WindowStage](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md) | Yes | WindowStage instance. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  onWindowStageRestore(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', \`onWindowStageRestore\`);
  }
}

#### \[h2\]onDestroy

onDestroy(): void | Promise<void>

Called when the UIAbility is destroyed (for example, when the UIAbility is terminated using the [terminateSelf](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateself) API). You can clear resources and save data during this lifecycle.

This API returns the result synchronously or uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/i5HzLuJ8RsKS9YSFKa08KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=684C3347E590CCBE98DC3CD1B79FB1D020C81A7F65AA5567528FA8C4169E4C11)

-   Once the **onDestroy** lifecycle callback completes, the application may exit. This can interrupt any pending asynchronous operations (such as asynchronously writing data to a database), preventing them from finishing successfully. In this case, you are advised to use a promise to return the result.
-   The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits (for example, process termination due to low memory conditions).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value**

| Type | Description |
| :-- | :-- |
| void | Promise<void> | No return value or a Promise object that returns no result. |

**Example**

-   A synchronous callback example is as follows:
    
    import { UIAbility } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    export default class MyUIAbility extends UIAbility {
      onDestroy() {
        hilog.info(0x0000, 'testTag', \`onDestroy\`);
        // Call the synchronous function.
      }
    }
    
-   A promise asynchronous callback example is as follows:
    
    import { UIAbility } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    export default class MyUIAbility extends UIAbility {
      async onDestroy() {
        hilog.info(0x0000, 'testTag', \`onDestroy\`);
        // Call the asynchronous function.
      }
    }
    

#### \[h2\]onWillForeground20+

onWillForeground(): void

Called just before the application transitions to the foreground. It is called before [onForeground](#onforeground). It can be used to capture the moment when the application starts to transition to the foreground. When paired with [onDidForeground](#ondidforeground20), it can also measure the duration from the application's initial foreground entry to its full transition into the foreground state.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWillForeground(): void {
    // Start to log the event that the application starts moving to the foreground.
    let eventParams: Record<string, number> = { 'xxxx': 100 };
    let eventInfo: hiAppEvent.AppEventInfo = {
      // Define the event domain.
      domain: "lifecycle",
      // Define the event name.
      name: "onwillforeground",
      // Define the event type.
      eventType: hiAppEvent.EventType.BEHAVIOR,
      // Define the event parameters.
      params: eventParams,
    };
    hiAppEvent.write(eventInfo).then(() => {
      hilog.info(0x0000, 'testTag', \`HiAppEvent success to write event\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`HiAppEvent err.code: ${err.code}, err.message: ${err.message}\`);
    });
  }

  // ...

  onDidForeground(): void {
    // Start to log the event that the application fully transitions to the foreground.
    let eventParams: Record<string, number> = { 'xxxx': 100 };
    let eventInfo: hiAppEvent.AppEventInfo = {
      // Define the event domain.
      domain: "lifecycle",
      // Define the event name.
      name: "ondidforeground",
      // Define the event type.
      eventType: hiAppEvent.EventType.BEHAVIOR,
      // Define the event parameters.
      params: eventParams,
    };
    hiAppEvent.write(eventInfo).then(() => {
      hilog.info(0x0000, 'testTag', \`HiAppEvent success to write event\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`HiAppEvent err.code: ${err.code}, err.message: ${err.message}\`);
    });
  }
}

#### \[h2\]onForeground

onForeground(): void

Called when the application is initially launched into the foreground or transitions from the background to the foreground. You can request necessary system resources, for example, requesting location services when the application transitions to the foreground, within this callback.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onForeground() {
    hilog.info(0x0000, 'testTag', \`onForeground\`);
  }
}

#### \[h2\]onDidForeground20+

onDidForeground(): void

Called after the application has transitioned to the foreground. It is called after [onForeground](#onforeground). It can be used to capture the moment when the application fully transitions to the foreground. When paired with [onWillForeground](#onwillforeground20), it can also measure the duration from the application's initial foreground entry to its full transition into the foreground state.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

For details, see [onWillForeground](#onwillforeground20).

#### \[h2\]onWillBackground20+

onWillBackground(): void

Called just when the application transitions to the background. It is called before [onBackground](#onbackground). It can be used to log various types of data, such as faults, statistics, security information, and user behavior that occur during application running.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyUIAbility extends UIAbility {
  onWillBackground(): void {
    let eventParams: Record<string, number | string> = {
      "int\_data": 100,
      "str\_data": "strValue",
    };
    // Record the application fault information.
    hiAppEvent.write({
      domain: "test\_domain",
      name: "test\_event",
      eventType: hiAppEvent.EventType.FAULT,
      params: eventParams,
    }, (err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, 'testTag', \`hiAppEvent code: ${err.code}, message: ${err.message}\`);
        return;
      }
      hilog.info(0x0000, 'testTag', \`hiAppEvent success to write event\`);
    });
  }
}

#### \[h2\]onBackground

onBackground(): void

Called when the application transitions from the foreground to the background. You can release resources when the UI is no longer visible, for example, stopping location services, within this callback.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onBackground() {
    // The UIAbility transitions to the background.
    hilog.info(0x0000, 'testTag', \`onBackground\`);
  }
}

#### \[h2\]onDidBackground20+

onDidBackground(): void

Called after the application has transitioned to the background. It is called after [onBackground](#onbackground). It can be used to release resources after the application has entered the background, for example, stopping audio playback.

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { audio } from '@kit.AudioKit';

export default class MyUIAbility extends UIAbility {
  static audioRenderer: audio.AudioRenderer;

  // ...
  onForeground(): void {
    let audioStreamInfo: audio.AudioStreamInfo = {
      samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
      channels: audio.AudioChannel.CHANNEL\_2, // Channel.
      sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
      encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
    };

    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
      rendererFlags: 0 // AudioRenderer flag.
    };

    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo,
      rendererInfo: audioRendererInfo
    };

    // Request an AudioRenderer in the foreground to play Pulse Code Modulation (PCM) audio data.
    audio.createAudioRenderer(audioRendererOptions).then((data) => {
      MyUIAbility.audioRenderer = data;
      hilog.info(0x0000, 'testTag', \`AudioRenderer Created : Success : Stream Type: SUCCESS.\`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`AudioRenderer Created : F : ${JSON.stringify(err)}.\`);
    });
  }

  onDidBackground() {
    // Release the AudioRenderer after transitioning to the background.
    MyUIAbility.audioRenderer.release((err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, 'testTag', \`AudioRenderer release failed, error: ${JSON.stringify(err)}.\`);
      } else {
        hilog.info(0x0000, 'testTag', \`AudioRenderer released.\`);
      }
    });
  }
}

#### \[h2\]onContinue

onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult>

Called when a UIAbility is to be migrated across devices. You can save service data to be migrated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/M2OanzEFTT2l9HgRLcGtvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2411A2A6FC6E3BCFD2D2FF8C375208D526B5C0156684A966B380167B498B046)

For versions prior to API version 18, only synchronous calls are supported. Starting from API version 18, asynchronous calls are also supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wantParam | Record<string, Object> | Yes | Data to be migrated. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityConstant.OnContinueResult](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#oncontinueresult) | Promise<[AbilityConstant.OnContinueResult](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#oncontinueresult)\> | 
Whether the migration is accepted. The options are as follows:

\- **AGREE**: The migration is allowed.

\- **REJECT**: The migration is rejected, for example, when an application is abnormal in **onContinue()**.

\- **MISMATCH**: The application versions of the source and target devices do not match. The application on the source device can obtain the version of the target application from **onContinue**. If the ability continuation cannot be performed due to version mismatch, this result is returned.

This callback comes in pairs with **onWindowStageRestore**. In ability continuation scenarios, the source UIAbility triggers **onContinue** to save custom data, and the target UIAbility triggers **onWindowStageRestore** to restore the custom data.

 |

**Example**

-   The following is an example of saving data using a synchronous API during application migration:
    
    import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
    
    export default class MyUIAbility extends UIAbility {
      onContinue(wantParams: Record<string, Object>) {
        console.info('onContinue');
        wantParams\['myData'\] = 'my1234567';
        return AbilityConstant.OnContinueResult.AGREE;
      }
    }
    
-   The following is an example of saving data using an asynchronous API during application migration:
    
    import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
    
    export default class MyUIAbility extends UIAbility {
      async setWant(wantParams: Record<string, Object>) {
        console.info('setWant start');
        for (let time = 0; time < 1000; ++time) {
          wantParams\[time\] = time;
        }
        console.info('setWant end');
      }
    
      async onContinue(wantParams: Record<string, Object>) {
        console.info('onContinue');
        return this.setWant(wantParams).then(() => {
          return AbilityConstant.OnContinueResult.AGREE;
        });
      }
    }
    

#### \[h2\]onNewWant

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void

Called when a started UIAbility instance is brought up again. If there are specific scenarios where you do not want this lifecycle callback to be triggered, you can use [setOnNewWantSkipScenarios](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#setonnewwantskipscenarios20) to set those [scenarios](../ohos-app-ability-contextconstant-context-related-constants/document.md#scenarios20).

This API returns the result synchronously and does not support asynchronous callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Data passed by the caller when re-launching the UIAbility. |
| launchParam | [AbilityConstant.LaunchParam](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#launchparam) | Yes | UIAbility launch parameters, including the launch reason. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info(\`onNewWant, want: ${want.abilityName}\`);
    console.info(\`onNewWant, launchParam: ${JSON.stringify(launchParam)}\`);
  }
}

#### \[h2\]onDump

onDump(params: Array<string>): Array<string>

Called when UIAbility data is dumped by running the dump command during application debugging. You can return non-sensitive information to be dumped by the UIAbility in this callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | Array<string> | Yes | Parameters for the dump command. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Information returned by the dump operation. |

**Example**

import { UIAbility } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onDump(params: Array<string>) {
    console.info(\`dump, params: ${JSON.stringify(params)}\`);
    return \['params'\];
  }
}

#### \[h2\]onSaveState

onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult

This API must be used with [appRecovery](../../both-models-recommended/ohos-app-ability-apprecovery-application-recovery/document.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](../../both-models-recommended/ohos-app-ability-apprecovery-application-recovery/document.md#apprecoveryenableapprecovery) set to **SAVE\_WHEN\_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/bJx4G6BsQLuFHxXfWmTdbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDD2F11FFFCB661DDB9BA6A5391DFE1E09667C4A9D6C53EE46C924DB04B8E7D5)

Starting from API version 20, this callback is not executed when [onSaveStateAsync](#onsavestateasync20) is implemented.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reason | [AbilityConstant.StateType](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#statetype) | Yes | Reason for triggering the application to save its state. Currently, only **APP\_RECOVERY** (fault recovery scenario) is supported. |
| wantParam | Record<string, Object> | Yes | Custom application state data, which is stored in **Want.parameters** in [onCreate](#oncreate) when the application restarts. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityConstant.OnSaveResult](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#onsaveresult) | An object indicating the data-saving policy (for example, all denied, all allowed, or only allowed in fault recovery scenarios). |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    console.info('onSaveState');
    wantParam\['myData'\] = 'my1234567';
    return AbilityConstant.OnSaveResult.RECOVERY\_AGREE;
  }
}

#### \[h2\]onSaveStateAsync20+

onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult>

This API must be used with [appRecovery](../../both-models-recommended/ohos-app-ability-apprecovery-application-recovery/document.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](../../both-models-recommended/ohos-app-ability-apprecovery-application-recovery/document.md#apprecoveryenableapprecovery) set to **SAVE\_WHEN\_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stateType | [AbilityConstant.StateType](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#statetype) | Yes | Reason for triggering the application to save its state. Currently, only **APP\_RECOVERY** (fault recovery scenario) is supported. |
| wantParam | Record<string, Object> | Yes | Custom application state data, which is stored in **Want.parameters** in [onCreate](#oncreate) when the application restarts. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityConstant.OnSaveResult](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#onsaveresult)\> | Promise used to return the result. An object indicating the data-saving policy (for example, all denied, all allowed, or only allowed in fault recovery scenarios). |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  async onSaveStateAsync(reason: AbilityConstant.StateType,
    wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // Execute the operation after 1 second.
    });
    return AbilityConstant.OnSaveResult.RECOVERY\_AGREE;
  }
}

#### \[h2\]onShare10+

onShare(wantParam: Record<string, Object>): void

Called when an atomic service is shared across devices. You can set the title, abstract, and URL of the atomic service to be shared in this callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wantParam | Record<string, Object> | Yes | Data to share. |

**Example**

import { UIAbility } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onShare(wantParams: Record<string, Object>) {
    console.info('onShare');
    wantParams\['ohos.extra.param.key.shareUrl'\] = 'example.com';
  }
}

#### \[h2\]onPrepareToTerminate10+

onPrepareToTerminate(): boolean

Triggered by the system just before the UIAbility is about to close (for example, when the user clicks the close button in the top-right corner of the application window or exits from the dock or system tray), allowing for additional operations to be performed before the UIAbility is officially shut down. You can return **true** to block the current closure attempt and then manually call [terminateSelf](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateself) at an appropriate time to close it. For example, you might ask the user to confirm whether they want to close the UIAbility and then proceed with the closure manually.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/AARrzbVCTB-3duloV__RWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10CC0BE6DDD20778CA4DC4F6203A402867DD25C64BA1C85D47DD1E83C9E33419)

-   Starting from API version 15, this callback is not executed when[UIAbility.onPrepareToTerminateAsync](#onpreparetoterminateasync15) is implemented. When [AbilityStage.onPrepareTerminationAsync](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onprepareterminationasync15) or [AbilityStage.onPrepareTermination](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onpreparetermination15) is implemented, this callback is not executed if the user right-clicks the dock bar or system tray to close the UIAbility.
-   Additionally, if the application or a third-party framework registers a listener for [window.WindowStage.on('windowStageClose')](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md#onwindowstageclose14), this callback function is not executed.

**Required permissions**: ohos.permission.PREPARE\_APP\_TERMINATE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Device behavior differences**: This API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether to terminate the UIAbility. **true** if the termination process is canceled; **false** to continue terminating the UIAbility. |

**Example**

import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onPrepareToTerminate() {
    // Define a pre-termination operation,
    // for example, starting another UIAbility and performing asynchronous termination based on the startup result.
    let want: Want = {
      bundleName: "com.example.myapplication",
      moduleName: "entry",
      abilityName: "SecondAbility"
    }
    this.context.startAbilityForResult(want)
      .then((result) => {
        // Obtain the startup result and terminate the current UIAbility when resultCode in the return value is 0.
        console.info('startAbilityForResult success, resultCode is ' + result.resultCode);
        if (result.resultCode === 0) {
          this.context.terminateSelf();
        }
      }).catch((err: BusinessError) => {
      // Exception handling.
      console.error('startAbilityForResult failed, err:' + JSON.stringify(err));
      this.context.terminateSelf();
    })

    return true; // The pre-termination operation is defined. The value true means that the UIAbility termination process is canceled.
  }
}

#### \[h2\]onPrepareToTerminateAsync15+

onPrepareToTerminateAsync(): Promise<boolean>

Triggered by the system just before the UIAbility is close (for example, when the user clicks the close button in the top-right corner of the application window or exits from the dock or system tray), allowing for additional operations to be performed before the UIAbility is officially shut down.

You can return **true** to block the current closure attempt and then manually call [terminateSelf](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateself) at an appropriate time to close it. For example, you might ask the user to confirm whether they want to close the UIAbility and then proceed with the closure manually.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/RIS-GCnpTk-JFJxqusYRKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14D09D989C7515CCCF5FB98A73DEFC797BA7E7983BCE3FDE9C8608A4B0A42656)

-   When [AbilityStage.onPrepareTerminationAsync](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onprepareterminationasync15) or [AbilityStage.onPrepareTermination](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onpreparetermination15) is implemented, this callback is not executed if the user right-clicks the dock bar or system tray to close the UIAbility.
    
-   Additionally, if the application or a third-party framework registers a listener for [window.WindowStage.on('windowStageClose')](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md#onwindowstageclose14), this callback function is not executed.
    
-   If an asynchronous callback crashes, it will be handled as a timeout. If the UIAbility does not respond within 10 seconds, it will be terminated forcibly.
    

**Required permissions**: ohos.permission.PREPARE\_APP\_TERMINATE

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Device behavior differences**

-   Starting from API version 15, this API executes the callback normally only on 2-in-1 devices. It does not execute the callback on other devices.
-   Starting from API version 19, this API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if the termination process is canceled; **false** to continue terminating the UIAbility. |

**Example**

import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  async onPrepareToTerminateAsync(): Promise<boolean> {
    await new Promise<boolean>((res, rej) => {
      setTimeout (res, 2000); // Execute the operation 2 seconds later.
    });
    return true; // The pre-termination operation is defined. The value true means that the UIAbility termination process is canceled.
  }
}

#### \[h2\]onBackPressed10+

onBackPressed(): boolean

Called when an operation of going back to the previous page is triggered on this UIAbility. The return value determines whether to destroy the UIAbility instance.

-   When the target SDK version is earlier than 12, the default return value is **false**, indicating that the UIAbility will be destroyed.
-   When the target SDK version is 12 or later, the default return value is **true**, indicating that the UIAbility will be moved to the background and will not be destroyed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the UIAbility instance will be moved to the background and will not be destroyed; **false** if the UIAbility instance will be destroyed. |

**Example**

import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onBackPressed() {
    return true;
  }
}

#### \[h2\]onCollaborate18+

onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult

Callback invoked to return the collaboration result in multi-device collaboration scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/mYnei3cNR_-F--tCNU0SHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F3298C4C0B9606B99FB4AFBABCA036DBBE15F942E895C8297EA59281ED5B38D)

-   This callback does not support ability launch in [specified mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#specified).
-   When you use methods such as [startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability) to start an application, you must include **FLAG\_ABILITY\_ON\_COLLABORATE** in [Flags](../../both-models-recommended/ohos-app-ability-wantconstant-want-constants/document.md#flags) in the Want object.
-   During a [cold start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-intra-device-interaction#cold-starting-uiability), this callback must be invoked before [onForeground](#onforeground) or after [onBackground](#onbackground). During a [hot start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-intra-device-interaction#hot-starting-uiability), this callback must be invoked before [onNewWant](#onnewwant).

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wantParam | Record<string, Object> | Yes | Want parameter, which supports only the key **"ohos.extra.param.key.supportCollaborateIndex"**. The key can be used to obtain the data passed by the caller and perform corresponding processing. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityConstant.CollaborateResult](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#collaborateresult18) | Whether the coordinator accepts the collaboration result. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}

#### Caller

A Caller UIAbility can use the [startAbilityByCall](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startabilitybycall) API to start the target Callee UIAbility. After the target UIAbility is started successfully, a Caller object is returned to the caller for communication.

#### \[h2\]call

call(method: string, data: rpc.Parcelable): Promise<void>

Used by a Caller UIAbility to send serialized data, as agreed upon by both parties, to the Callee UIAbility. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| method | string | Yes | Method name agreed upon by the Caller UIAbility and Callee UIAbility, used by the Callee UIAbility to identify the type of message. |
| data | [rpc.Parcelable](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#parcelable9) | Yes | Message content sent from the Caller UIAbility to the Callee UIAbility, which is in serialized form. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyMessageAble implements rpc.Parcelable { // Custom parcelable data structure.
  name: string;
  str: string;
  num: number = 1;

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(\`MyMessageAble marshalling num\[${this.num}\] str\[${this.str}\]\`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(\`MyMessageAble unmarshalling num\[${this.num}\] str\[${this.str}\]\`);
    return true;
  }
}

let method = 'call\_Function'; // Agreed notification message string

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      let caller: Caller = obj;
      let msg = new MyMessageAble('msg', 'world'); // See the definition of Parcelable.
      caller.call(method, msg)
        .then(() => {
          console.info('Caller call() called');
        })
        .catch((callErr: BusinessError) => {
          console.error(\`Caller.call catch error, error.code: ${callErr.code}, error.message: ${callErr.message}\`);
        });
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### \[h2\]callWithResult

callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence>

Used by a Caller UIAbility to send serialized data to a Callee UIAbility and return the result after the Callee UIAbility processes the message. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| method | string | Yes | Method name agreed upon by the Caller UIAbility and Callee UIAbility, used by the Callee UIAbility to identify the type of message. |
| data | [rpc.Parcelable](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#parcelable9) | Yes | Message content sent from the Caller UIAbility to the Callee UIAbility, which is in serialized form. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[rpc.MessageSequence](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9)\> | Promise used to return the response data from the Callee UIAbility. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyMessageAble implements rpc.Parcelable {
  name: string
  str: string
  num: number = 1

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(\`MyMessageAble marshalling num\[${this.num}\] str\[${this.str}\]\`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(\`MyMessageAble unmarshalling num\[${this.num}\] str\[${this.str}\]\`);
    return true;
  }
}

let method = 'call\_Function';
let caller: Caller;

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      caller = obj;
      let msg = new MyMessageAble('msg', 'world');
      caller.callWithResult(method, msg)
        .then((data) => {
          console.info('Caller callWithResult() called');
          let retMsg = new MyMessageAble('msg', 'world');
          data.readParcelable(retMsg);
        })
        .catch((callErr: BusinessError) => {
          console.error(\`Caller.callWithResult catch error, error.code: ${callErr.code}, error.message: ${callErr.message}\`);
        });
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### \[h2\]release

release(): void

Used by a Caller UIAbility to proactively release the connection with the Callee UIAbility. After this API is called, the Caller UIAbility can no longer use **call** or **callWithResult** to send messages to the Callee UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |

**Example**

import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let caller: Caller;

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      caller = obj;
      try {
        caller.release();
      } catch (releaseErr) {
        console.error(\`Caller.release catch error, error.code: ${releaseErr.code}, error.message: ${releaseErr.message}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### \[h2\]onRelease

onRelease(callback: OnReleaseCallback): void

Used by the Caller UIAbility to register a listener for disconnection notifications from the Callee UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnReleaseCallback](#onreleasecallback) | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        caller.onRelease((str) => {
          console.info(\`Caller OnRelease CallBack is called ${str}\`);
        });
      } catch (error) {
        console.error(\`Caller.onRelease catch error, error.code: ${error.code}, error.message: ${error.message}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### \[h2\]onRemoteStateChange10+

onRemoteStateChange(callback: OnRemoteStateChangeCallback): void

Called when the remote UIAbility state changes in the collaboration scenario. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnRemoteStateChangeCallback](#onremotestatechangecallback) | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let dstDeviceId: string = 'xxxxx';
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: dstDeviceId
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        caller.onRemoteStateChange((str) => {
          console.info('Remote state changed ' + str);
        });
      } catch (error) {
        console.error(\`Caller.onRemoteStateChange catch error, error.code: ${JSON.stringify(error.code)}, error.message: ${JSON.stringify(error.message)}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${JSON.stringify(err.code)}, error.message: ${JSON.stringify(err.message)}\`);
    });
  }
}

#### \[h2\]on('release')

on(type: 'release', callback: OnReleaseCallback): void

Used by the Caller UIAbility to register a listener for disconnection notifications from the Callee UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'release'**. |
| callback | [OnReleaseCallback](#onreleasecallback) | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Caller } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let dstDeviceId: string = 'xxxx';
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: dstDeviceId
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        caller.on('release', (str) => {
          console.info(\`Caller OnRelease CallBack is called ${str}\`);
        });
      } catch (error) {
        console.error(\`Caller.on catch error, error.code: ${error.code}, error.message: ${error.message}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### \[h2\]off('release')

off(type: 'release', callback: OnReleaseCallback): void

Unregisters the listener for disconnection notifications from the Callee UIAbility. This is the reverse operation of [on('release')](#onrelease-1). It is currently not supported.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'release'**. |
| callback | [OnReleaseCallback](#onreleasecallback) | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { UIAbility, Caller, OnReleaseCallback } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      let caller: Caller = obj;
      try {
        let onReleaseCallBack: OnReleaseCallback = (str) => {
          console.info(\`Caller OnRelease CallBack is called ${str}\`);
        };
        caller.on('release', onReleaseCallBack);
        caller.off('release', onReleaseCallBack);
      } catch (error) {
        console.error(\`Caller.on or Caller.off catch error, error.code: ${error.code}, error.message: ${error.message}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### \[h2\]off('release')

off(type: 'release'): void

Unregisters the listener for disconnection notifications from the Callee UIAbility. This is the reverse operation of [Caller.on('release')](#onrelease-1). It is currently not supported.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'release'**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { UIAbility, Caller, OnReleaseCallback } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let caller: Caller;

export default class MainUIAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    this.context.startAbilityByCall({
      bundleName: 'com.example.myservice',
      abilityName: 'MainUIAbility',
      deviceId: ''
    }).then((obj) => {
      caller = obj;
      try {
        let onReleaseCallBack: OnReleaseCallback = (str) => {
          console.info(\`Caller OnRelease CallBack is called ${str}\`);
        };
        caller.on('release', onReleaseCallBack);
        caller.off('release');
      } catch (error) {
        console.error(\`Caller.on or Caller.off catch error, error.code: ${error.code}, error.message: ${error.message}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}\`);
    });
  }
}

#### Callee

Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object.

#### \[h2\]on

on(method: string, callback: CalleeCallback): void

Registers a caller notification callback, which is invoked when the target UIAbility registers a function.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| method | string | Yes | Method name agreed upon by the Caller UIAbility and Callee UIAbility, used by the Callee UIAbility to identify the type of message. |
| callback | [CalleeCallback](#calleecallback) | Yes | JS notification synchronization callback of the [rpc.MessageSequence](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) type. The callback must return at least one empty [rpc.Parcelable](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#parcelable9) object. Otherwise, the function execution fails. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200004 | The method has been registered. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

class MyMessageAble implements rpc.Parcelable {
  name: string
  str: string
  num: number = 1

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(\`MyMessageAble marshalling num\[${this.num}\] str\[${this.str}\]\`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(\`MyMessageAble unmarshalling num\[${this.num}\] str\[${this.str}\]\`);
    return true;
  }
}

let method = 'call\_Function';

function funcCallBack(pdata: rpc.MessageSequence) {
  let msg = new MyMessageAble('test', '');
  pdata.readParcelable(msg);
  return new MyMessageAble('test1', 'Callee test');
}

export default class MainUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('Callee onCreate is called');
    try {
      this.callee.on(method, funcCallBack);
    } catch (error) {
      console.error(\`Callee.on catch error, error.code: ${error.code}, error.message: ${error.message}\`);
    }
  }
}

#### \[h2\]off

off(method: string): void

Unregisters a caller notification callback, which is invoked when the target UIAbility registers a function.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| method | string | Yes | Registered notification message string. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200005 | The method has not been registered. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

let method = 'call\_Function';

export default class MainUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('Callee onCreate is called');
    try {
      this.callee.off(method);
    } catch (error) {
      console.error(\`Callee.off catch error, error.code: ${error.code}, error.message: ${error.message}\`);
    }
  }
}

#### OnReleaseCallback

#### \[h2\](msg: string)

(msg: string): void

Defines the callback that is invoked when the stub on the target UIAbility is disconnected.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Message used for disconnection. |

#### OnRemoteStateChangeCallback

#### \[h2\](msg: string)10+

(msg: string): void

Defines the callback that is invoked when the remote UIAbility state changes in the collaboration scenario.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Message used for disconnection. |

#### CalleeCallback

#### \[h2\](indata: rpc.MessageSequence)

(indata: rpc.MessageSequence): rpc.Parcelable

Defines the callback of the registration message notification of the UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| indata | [rpc.MessageSequence](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) | Yes | Data to be transferred. |

**Return value**

| Type | Description |
| :-- | :-- |
| [rpc.Parcelable](../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#parcelable9) | Returned data object. |
