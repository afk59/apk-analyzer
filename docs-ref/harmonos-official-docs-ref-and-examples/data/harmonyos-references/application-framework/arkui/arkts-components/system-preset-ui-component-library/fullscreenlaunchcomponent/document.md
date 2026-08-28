# FullScreenLaunchComponent

**FullScreenLaunchComponent** is a component designed for launching atomic services in full screen. If the invoked application (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in full-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/VhLGhgyyQH2kvlzLL-N8Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=204AFCFF37309D41446393943950A5629368F470A85463012219A10EC09772C7)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

This component is not supported on wearables.

To implement an embeddable atomic service within this component, it must inherit from [EmbeddableUIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-embeddableuiability-embeddable-uiability/document.md). Otherwise, the system cannot guarantee that the atomic service will function properly.

#### Modules to Import

import { FullScreenLaunchComponent } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### FullScreenLaunchComponent

FullScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<TerminationInfo> })

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator Type | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | Callback<void> | Yes | @BuilderParam | 
Custom placeholder icon displayed before launching the atomic service. This allows you to create a large launch icon similar to those used by desktop applications. Clicking the placeholder icon will launch the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| appId | string | Yes | \- | 

Application ID of the atomic service to be launched. It is the unique identifier for the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 12.To obtain the required atomic service, find it in the atomic service section on AppGallery and contact the developer using the contact information provided in the atomic service's privacy statement.

 |
| options | [AtomicServiceOptions](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-atomicserviceoptions-optional-parameters-of-openatomicservice/document.md) | No | \- | 

Parameters for launching the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onError18+ | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | \- | 

Triggered when an exception occurs during the execution of an embedded atomic service. You can obtain the error information based on the **code**, **name**, and **message** parameters in the callback and rectify the exception accordingly.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onTerminated18+ | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[TerminationInfo](../../rendering-drawing/embeddedcomponent/document.md#terminationinfo)\> | No | \- | 

Triggered when an embedded atomic service exits properly by calling [terminateSelfWithResult](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateselfwithresult) or [terminateSelf](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateself)

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onReceive20+ | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<Record<string, Object>> | No | \- | 

Callback triggered when the embedded atomic service is launched through [Window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-stage) API calls.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/UsFkq1p0RtmGDnEZgu-rqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC1C24AA0C9E01290B479B18721593B5F09E8C1CDE4FDD1B156EBB90D12FA242)

-   If the atomic service exits by calling [terminateSelfWithResult](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateselfwithresult), the information it carries is passed to the callback parameter.
-   If the atomic service exits by calling [terminateSelf](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#terminateself), the callback parameter has a default **code** value of **0** and **want** of **undefined**.

#### Example

This example demonstrates component usage with extended atomic service capabilities. In real-world development, replace the sample **appId** with the actual application of your ID atomic service.

**FullScreenLaunchComponent** needs to be invoked by the user. After the provider completes local installation, the component can be launched in full-screen embedded mode within the user application or atomic service.

**User Implementation**

// The entry point file Index.ets for the user side is as follows:
import { FullScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State appId: string = '6917573653426122083'; // Application ID of the atomic service.

  build() {
    Row() {
      Column() {
        FullScreenLaunchComponent({
          content: ColumnChild,
          appId: this.appId,
          options: {},
          onTerminated: (info) => {
            console.info(\`onTerminated code: ${info.code.toString()}\`);
          },
          onError: (err) => {
            console.error(\`onError code: ${err.code}, message: ${err.message}\`);
          },
          onReceive: (data) => {
            console.info(\`onReceive, data: ${JSON.stringify(data)}\`);
          }
        }).width("80vp").height("80vp")
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Builder
function ColumnChild() {
  Column() {
    Image($r('app.media.startIcon'))
    Text('test')
  }
}

**Provider Implementation**

You need to modify the following files for the atomic service provider:

-   Entry point file: **/src/main/ets/entryability/EntryAbility.ets**

import { AbilityConstant, Want, EmbeddableUIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends EmbeddableUIAbility {
  storage = new LocalStorage();
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let mainWindow = windowStage.getMainWindowSync()
    this.storage.setOrCreate("window", mainWindow)
    this.storage.setOrCreate("windowStage", windowStage)
    windowStage.loadContent('pages/Index', this.storage);
  }

  onWindowStageDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

-   Extended ability entry page file: **/src/main/ets/pages/Index.ets**

import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();

  build() {
    Row() {
      Column() {
        GridRow({ columns: 2 }) {
          GridCol() {
            Button("setWindowSystemBar")
              .onClick(() => {
                this.testSetSystemBarEnable()
              }).width(120)
          }.height(60)

          GridCol() {
            Button("setGestureBack")
              .onClick(() => {
                this.testSetGestureBackEnable()
              }).width(120)
          }.height(60)

          GridCol() {
            Button("setImmersive")
              .onClick(() => {
                this.testSetImmersiveEnable()
              }).width(120)
          }.height(60)

          GridCol() {
            Button("setSpecificSystemBarEnabled")
              .onClick(() => {
                this.testSetSpecificSystemBarEnabled()
              }).width(120)
          }.height(60)
        }
      }
      .width('100%')
    }
    .height('100%')
  }

  testSetSystemBarEnable() {
    let window: window.Window | undefined = this.storage?.get("window");
    let p = window?.setWindowSystemBarEnable(\["status"\])
    p?.then(() => {
      console.info('setWindowSystemBarEnable success');
    }).catch((err: BusinessError) => {
      console.error(\`setWindowSystemBarEnable failed, error = ${JSON.stringify(err)}\`);
    })
  }

  testSetGestureBackEnable() {
    let window: window.Window | undefined = this.storage?.get("window");
    let p = window?.setGestureBackEnabled(true)
    p?.then(() => {
      console.info('setGestureBackEnabled success');
    }).catch((err: BusinessError) => {
      console.error(\`setGestureBackEnabled failed, error = ${JSON.stringify(err)}\`);
    })
  }

  testSetImmersiveEnable() {
    let window: window.Window | undefined = this.storage?.get("window");
    try {
      window?.setImmersiveModeEnabledState(true)
    } catch (err) {
      console.error(\`setImmersiveModeEnabledState failed, error = ${JSON.stringify(err)}\`);
    }
  }

  testSetSpecificSystemBarEnabled() {
    let window: window.Window | undefined = this.storage?.get("window");
    let p = window?.setSpecificSystemBarEnabled('navigationIndicator', false, false)
    p?.then(() => {
      console.info('setSpecificSystemBarEnabled success');
    }).catch((err: BusinessError) => {
      console.error(\`setSpecificSystemBarEnabled failed, error = ${JSON.stringify(err)}\`);
    })
  }
}
