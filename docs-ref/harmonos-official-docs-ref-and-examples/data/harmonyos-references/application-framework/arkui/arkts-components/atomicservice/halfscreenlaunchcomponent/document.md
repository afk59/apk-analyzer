# HalfScreenLaunchComponent

**HalfScreenLaunchComponent** is a component designed for launching atomic services in half screen. If the invoked application (the one being launched) grants the invoker the authorization to run the atomic service in an embedded manner, the invoker can operate the atomic service in half-screen embedded mode. If authorization is not provided, the invoker will launch the atomic service in a pop-up manner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/1NgzS55oQXqSf6AsjHHr-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67EAE6F4DDD77EEAE9B2276DEAC81298B805A0716C920BB7E49239894CA99F29)

This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

To implement an embeddable atomic service, make sure it inherits from [EmbeddableUIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-embeddableuiability-embeddable-uiability/document.md). If the atomic service does not inherit from **EmbeddableUIAbility**, the system cannot guarantee its proper operation.

#### Modules to Import

import { HalfScreenLaunchComponent } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### HalfScreenLaunchComponent

HalfScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<TerminationInfo>})

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | Callback<void> | Yes | @BuilderParam | 
Content displayed in the component.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| appId | string | Yes | \- | 

Application ID for the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| options | [AtomicServiceOptions](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-atomicserviceoptions-optional-parameters-of-openatomicservice/document.md) | No | \- | 

Parameters for starting the atomic service. The default value is empty.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onError | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | \- | 

Invoked when an error occurs during the running of the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onTerminated | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[TerminationInfo](../../rendering-drawing/embeddedcomponent/document.md#terminationinfo)\> | No | \- | 

Callback used to return the result of the atomic service. The input parameter is of type **TerminationInfo**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onReceive20+ | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<Record<string, Object>> | No | \- | 

Callback triggered when the embedded atomic service is launched through [Window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-stage) API calls.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### Example

This example demonstrates how to start a top-up service in embedded mode.

import { HalfScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  appId: string = "576\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"; // Application ID for the atomic service.

  build() {
    Column() {
      HalfScreenLaunchComponent({
        appId: this.appId,
        options: {},
        onTerminated:  (info:TerminationInfo)=> {
          console.info('onTerminated info = '+ info.want);
        },
        onError: (err) => {
          console.error(" onError code: " + err.code + ", message: ", err.message);
        },
        onReceive: (data) => {
          console.info("onReceive, data: " + data\['ohos.atomicService.window'\]);
        }
      }) {
        Column() {
          Image($r('app.media.app\_icon'))
          Text('Start top-up')
        }.width("80vp").height("80vp").margin({bottom:30})
      } // Pass content through the trailing closure.
    }
  }

}
