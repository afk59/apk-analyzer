# liveViewManager

This module provides basic capabilities of Live View Kit, including creating, updating, and ending a live view, obtaining a live view, and checking whether the live view function is enabled.

**Start version**: 4.1.0(11)

#### Module Import

import { liveViewManager } from '@kit.LiveViewKit';

**Device behavior differences**: This module is supported on phones and tablets, but does not work on other devices.

#### liveViewManager.isLiveViewEnabled

isLiveViewEnabled(): Promise<boolean>

Checks whether the live view function is enabled. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Indicates whether the live view function is enabled. The result is returned through a promise.

-   **true**: yes
-   **false**: no

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1003500001](../arkts-api-error-codes/document.md#section539558125020)

 | 

Internal error.

 |
| 

[1003500002](../arkts-api-error-codes/document.md#section1865682663012)

 | 

Marshalling or unmarshalling error.

 |
| 

[1003500003](../arkts-api-error-codes/document.md#section7391431175215)

 | 

Failed to connect service.

 |

**Example**:

import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  liveViewManager.isLiveViewEnabled().then((isEnabled: boolean) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in checking whether liveView is enabled, liveView is : %{public}s', isEnabled);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to check whether liveView is enabled: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to check whether liveView is enabled: %{public}d %{public}s', e.code, e.message);
}

#### liveViewManager.startLiveView

startLiveView(liveView: LiveView): Promise<LiveViewResult>

Creates a live view. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

liveView

 | 

[LiveView](#section411410371767)

 | 

Yes

 | 

A live view instance.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[LiveViewResult](#section186814291982)\>

 | 

Live view creation result, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

[1003500001](../arkts-api-error-codes/document.md#section539558125020)

 | 

Internal error.

 |
| 

[1003500002](../arkts-api-error-codes/document.md#section1865682663012)

 | 

Marshalling or unmarshalling error.

 |
| 

[1003500003](../arkts-api-error-codes/document.md#section7391431175215)

 | 

Failed to connect service.

 |
| 

[1003500004](../arkts-api-error-codes/document.md#section19393182117481)

 | 

LiveView is not enabled.

 |
| 

[1003500005](../arkts-api-error-codes/document.md#section105385290506)

 | 

The right of liveView is not enabled.

 |
| 

[1003500006](../arkts-api-error-codes/document.md#section1722812135214)

 | 

The liveView already exists.

 |
| 

[1003500007](../arkts-api-error-codes/document.md#section1495704455311)

 | 

Couldn't connect to server.

 |
| 

[1003500008](../arkts-api-error-codes/document.md#section1769374975513)

 | 

Over max number liveViews per second.

 |

**Example**:

import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, wantAgent } from '@kit.AbilityKit';

async function startLiveView(): Promise<void> {
  try {
    // Define the live view to be created.
    let liveView: liveViewManager.LiveView = {
      id: 123,
      event: "PICK\_UP",
      sequence: 1,
      isMute: false,
      liveViewData: {
        primary: {
          title: "The meal is ready.",
          content: \[
            { text: "Go to" }, 
            { text: "Window 1", textColor: "#FFFF0000" }
          \],
          keepTime: 1,
          clickAction: await buildWantAgent(),
          extensionData: {
            text: "Ready for pickup",
            type: liveViewManager.ExtensionType.EXTENSION\_TYPE\_COMMON\_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT\_TYPE\_PICKUP,
            title: "Pickup code",
            content: "72988",
            underlineColor: "#FFFF0000",
            descPic: "coffee.jpg"
          }
        },
        capsule: {
          type: liveViewManager.CapsuleType.CAPSULE\_TYPE\_TEXT,
          status: 1,
          icon: "coffee.jpg",
          title: "Ready for pickup",
          content: "Pickup code: 72988",
          backgroundColor: "#FF308977"
        }
      }
    };

    liveViewManager.startLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in starting liveView, result: %{public}s', JSON.stringify(liveViewResult));
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to start liveView: %{public}d %{public}s', err.code, err.message);
    });
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to start liveView: %{public}d %{public}s', e.code, e.message);
  }
}

async function buildWantAgent(): Promise<Want> {
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: \[
      {
        bundleName: 'xxx.xxx.xxx',
        abilityName: 'EntryAbility'
      } as Want
    \],
    actionType: wantAgent.OperationType.START\_ABILITIES,
    requestCode: 0,
    actionFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
  };
  try {
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  } catch (e) {
    const err: BusinessError = e as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
    throw e as Error;
  }
}

#### liveViewManager.updateLiveView

updateLiveView(liveView: LiveView): Promise<LiveViewResult>

Updates a live view. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

liveView

 | 

[LiveView](#section411410371767)

 | 

Yes

 | 

A live view instance. Unless otherwise specified, optional parameters that are not passed in **liveView** this time will use their previous values by default.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[LiveViewResult](#section186814291982)\>

 | 

Live view update result, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

[1003500001](../arkts-api-error-codes/document.md#section539558125020)

 | 

Internal error.

 |
| 

[1003500002](../arkts-api-error-codes/document.md#section1865682663012)

 | 

Marshalling or unmarshalling error.

 |
| 

[1003500003](../arkts-api-error-codes/document.md#section7391431175215)

 | 

Failed to connect service.

 |
| 

[1003500004](../arkts-api-error-codes/document.md#section19393182117481)

 | 

LiveView is not enabled.

 |
| 

[1003500008](../arkts-api-error-codes/document.md#section1769374975513)

 | 

Over max number liveViews per second.

 |
| 

[1003500009](../arkts-api-error-codes/document.md#section17529152105718)

 | 

The liveView does not exist.

 |
| 

[1003500010](../arkts-api-error-codes/document.md#section1456815218586)

 | 

The liveView has ended.

 |
| 

[1003500011](../arkts-api-error-codes/document.md#section269192512108)

 | 

The liveView sequence is incorrect.

 |

**Example**:

import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, wantAgent } from '@kit.AbilityKit';

async function updateLiveView(): Promise<void> {
  try {
    // Define the live view to be updated.
    let liveView: liveViewManager.LiveView = {
      id: 123,
      event: "PICK\_UP",
      sequence: 2,
      isMute: false,
      liveViewData: {
        primary: {
          title: "The meal is ready.",
          content: \[
            { text: "Go to" }, 
            { text: "Window 1", textColor: "#FFFF0000" }
          \],
          keepTime: 1,
          clickAction: await buildWantAgent(),
          extensionData: {
            text: "Ready for pickup",
            type: liveViewManager.ExtensionType.EXTENSION\_TYPE\_COMMON\_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT\_TYPE\_PICKUP,
            title: "Pickup code",
            content: "72988",
            underlineColor: "#FFFF0000",
            descPic: "coffee.jpg"
          }
        },
        capsule: {
          type: liveViewManager.CapsuleType.CAPSULE\_TYPE\_TEXT,
          status: 1,
          icon: "coffee.jpg",
          title: "Ready for pickup",
          content: "Pickup code: 72988",
          backgroundColor: "#FF308977"
        }
      }
    };

    liveViewManager.updateLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in updating liveView, result: %{public}s', JSON.stringify(liveViewResult));
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to update liveView: %{public}d %{public}s', err.code, err.message);
    });
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to update liveView: %{public}d %{public}s', e.code, e.message);
  }
}

async function buildWantAgent(): Promise<Want> {
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: \[
      {
        bundleName: 'xxx.xxx.xxx',
        abilityName: 'EntryAbility'
      } as Want
    \],
    actionType: wantAgent.OperationType.START\_ABILITIES,
    requestCode: 0,
    actionFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
  };
  try {
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  } catch (e) {
    const err: BusinessError = e as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
    throw e as Error;
  }
}

#### liveViewManager.stopLiveView

stopLiveView(liveView: LiveView): Promise<LiveViewResult>

Ends a live view. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

liveView

 | 

[LiveView](#section411410371767)

 | 

Yes

 | 

A live view instance. Unless otherwise specified, optional parameters that are not passed in **liveView** this time will use their previous values by default.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[LiveViewResult](#section186814291982)\>

 | 

Live view ending result, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

[1003500001](../arkts-api-error-codes/document.md#section539558125020)

 | 

Internal error.

 |
| 

[1003500002](../arkts-api-error-codes/document.md#section1865682663012)

 | 

Marshalling or unmarshalling error.

 |
| 

[1003500003](../arkts-api-error-codes/document.md#section7391431175215)

 | 

Failed to connect service.

 |
| 

[1003500004](../arkts-api-error-codes/document.md#section19393182117481)

 | 

LiveView is not enabled.

 |
| 

[1003500008](../arkts-api-error-codes/document.md#section1769374975513)

 | 

Over max number liveViews per second.

 |
| 

[1003500009](../arkts-api-error-codes/document.md#section17529152105718)

 | 

The liveView does not exist.

 |
| 

[1003500010](../arkts-api-error-codes/document.md#section1456815218586)

 | 

The liveView has ended.

 |
| 

[1003500011](../arkts-api-error-codes/document.md#section269192512108)

 | 

The liveView sequence is incorrect.

 |

**Example**:

import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, wantAgent } from '@kit.AbilityKit';

async function stopLiveView(): Promise<void> {
  try {
    // Define the live view to be ended.
    let liveView: liveViewManager.LiveView = {
      id: 123,
      event: "PICK\_UP",
      sequence: 3,
      isMute: false,
      liveViewData: {
        primary: {
          title: "The meal is ready.",
          content: \[
            { text: "Go to" }, 
            { text: "Window 1", textColor: "#FFFF0000" }
          \],
          keepTime: 1,
          clickAction: await buildWantAgent(),
          extensionData: {
            text: "Ready for pickup",
            type: liveViewManager.ExtensionType.EXTENSION\_TYPE\_COMMON\_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT\_TYPE\_PICKUP,
            title: "Pickup code",
            content: "72988",
            underlineColor: "#FFFF0000",
            descPic: "coffee.jpg"
          }
        },
        capsule: {
          type: liveViewManager.CapsuleType.CAPSULE\_TYPE\_TEXT,
          status: 1,
          icon: "coffee.jpg",
          title: "Ready for pickup",
          content: "Pickup code: 72988",
          backgroundColor: "#FF308977"
        }
      }
    };

    liveViewManager.stopLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in stopping liveView, result: %{public}s', JSON.stringify(liveViewResult));
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', err.code, err.message);
    });
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', e.code, e.message);
  }
}

async function buildWantAgent(): Promise<Want> {
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: \[
      {
        bundleName: 'xxx.xxx.xxx',
        abilityName: 'EntryAbility'
      } as Want
    \],
    actionType: wantAgent.OperationType.START\_ABILITIES,
    requestCode: 0,
    actionFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
  };
  try {
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  } catch (e) {
    const err: BusinessError = e as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
    throw e as Error;
  }
}

#### liveViewManager.getActiveLiveView

getActiveLiveView(id: number): Promise<LiveView>

Obtains an active live view. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

Yes

 | 

Live view ID. The value range is \[–2147483648, 2147483647\].

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[LiveView](#section411410371767)\>

 | 

Active live view instance, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[1003500001](../arkts-api-error-codes/document.md#section539558125020)

 | 

Internal error.

 |
| 

[1003500002](../arkts-api-error-codes/document.md#section1865682663012)

 | 

Marshalling or unmarshalling error.

 |
| 

[1003500003](../arkts-api-error-codes/document.md#section7391431175215)

 | 

Failed to connect service.

 |
| 

[1003500009](../arkts-api-error-codes/document.md#section17529152105718)

 | 

The liveView does not exist.

 |

**Example**:

import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define the ID of the live view to be obtained.
const id = 1;
try {
  liveViewManager.getActiveLiveView(id).then((liveView: liveViewManager.LiveView) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting active liveView, liveView is : %{public}s', JSON.stringify(liveView));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to get active liveView: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get active liveView: %{public}d %{public}s', e.code, e.message);
}

#### LiveView

Live view object parameters. For specific examples, please refer to [Creating a Live View](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/liveview-create-locally#section69141150182715).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

Yes

 | 

Unique ID of a live view, which is generated by you. The value range is \[–2147483648, 2147483647\]. This parameter corresponds to [activityId](../../../push-kit/rest-apis/scenario-specific-message/request-body-parameters/document.md#section66881469306) of **LiveViewPayload** in Push Kit.

 |
| 

event

 | 

string

 | 

Yes

 | 

Application scenario of a live view.

-   **TAXI**: ride hailing
-   **DELIVERY**: instant delivery (takeout and fresh food)
-   **FLIGHT**: flight
-   **TRAIN**: high-speed train/common train
-   **QUEUE**: queueing
-   **PICK\_UP**: meal pickup
-   **SCORE**: live scores
-   **RENT**: shared leasing
-   **TIMER**: timing
-   **WORKOUT**: workout
-   **NAVIGATION**: navigation

To use specific scenarios, you need to apply for corresponding permissions. For details, please refer to [Enabling Live View Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/liveview-rights).

 |
| 

sequence

 | 

number

 | 

No

 | 

Live view version number. The value range is \[0, 2147483647\]. In the live view update and ending scenarios, the new live view version number must be greater than the current one. Otherwise, the update or ending will fail. If no value is passed for this parameter, Live View Kit does not automatically generate a live view version number or perform live view version number verification. (When no live view version number is generated, the value of **sequence** in the returned result of the **getActiveLiveView** API is **4294967295**. This is an invalid value and cannot be used for live view update.) This parameter corresponds to [version](../../../push-kit/rest-apis/scenario-specific-message/request-body-parameters/document.md#section66881469306) in Push Kit.

 |
| 

isMute

 | 

boolean

 | 

No

 | 

Indicates whether the message notification is silent. If this parameter is not passed when you create a live view or change the live view status, the silent notification mode is used by default.

-   **true**: silent
-   **false**: ringtone or vibration

 |
| 

timer

 | 

[LiveViewTimer](#section954195316811)

 | 

No

 | 

Live view timer, which counts per second during display.

NOTE:

Start version: 5.0.0(12)

After a timer is configured, you can use the placeholder **${placeholder.timer}** in some parameters. The system will replace the placeholder with the timer.

Currently, the following parameters support the placeholder:

-   liveViewData.primary.[title](#section452772611408)
-   liveViewData.primary.[content](#section452772611408)
-   liveViewData.primary.layoutData.[content](#section129929595142)
-   liveViewData.primary.layoutData.[competitionTime](#section16706148183416)

 |
| 

liveViewData

 | 

[LiveViewData](#section980821010388)

 | 

Yes

 | 

Details about a live view.

 |

#### LiveViewTimer

Timer parameters of a live view.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

time

 | 

number

 | 

No

 | 

Initial value of a timer, in ms. The default value is **0**. The value range is \[0, 9223372036854775807\]. The value is updated every second.

 |
| 

isCountdown

 | 

boolean

 | 

No

 | 

Indicates whether a timer is a countdown timer. The default value is **false**.

-   **true**: yes
-   **false**: no

 |
| 

isPaused

 | 

boolean

 | 

No

 | 

Indicates whether a timer is paused. The default value is **false**. A paused timer displays the time when it is paused.

-   **true**: yes
-   **false**: no (default value)

 |
| 

countdownPreset

 | 

[CountdownPreset](#section39351532053)

 | 

No

 | 

When the countdown reaches 0, the system automatically updates the extension area title (specified by **title**) and extension area content (specified by **content**) of a live view widget to the values of **presetTitle** and **presetContent** in **countdownPreset**, respectively.

The preceding function takes effect only when the following conditions are met:

-   The value of [layoutType](#section1765911975020) is **LAYOUT\_TYPE\_PICKUP**, indicating an emphasized text template.
-   The placeholder **${placeholder.timer}** is used in liveViewData.primary.layoutData.[content](#section129929595142).

NOTE:

**Start version**: 6.0.0(20)

 |
| 

capsuleCountdownPreset

 | 

[CountdownPreset](#section39351532053)

 | 

No

 | 

When the countdown reaches 0, the system automatically updates the primary text (specified by **time**) and secondary text (specified by **content**) of a timer live view capsule to the values of **presetTitle** and **presetContent** in **capsuleCountdownPreset**, respectively.

The preceding function takes effect only when the following condition is met:

-   The value of [capsuleType](#section136243383011) is **CAPSULE\_TYPE\_TIMER**, indicating a timer live view capsule.

NOTE:

**Start version**: 6.0.0(20)

 |

#### CountdownPreset

Timer preset parameters of a live view.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

presetTitle

 | 

string

 | 

No

 | 

Preset primary text used for automatically updating the title of an extension area or primary text of a live view capsule. Time placeholders are not supported. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

presetContent

 | 

string

 | 

No

 | 

Preset secondary text used for automatically updating the text content of an extension area or secondary text of a live view capsule. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |

#### LiveViewData

Details about a live view.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

primary

 | 

[PrimaryData](#section452772611408)

 | 

Yes

 | 

Widget content.

 |
| 

capsule

 | 

[TextCapsule](#section1440294811375) | [TimerCapsule](#section613411226413) | [ProgressCapsule](#section147361526184415)

 | 

No

 | 

Live view capsule content.

 |
| 

external

 | 

[ExternalData](#section92302515457)

 | 

No

 | 

Cover screen content for small-size foldable devices.

 |

#### PrimaryData

Widget parameters.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

Creation: Yes

Update/Ending: No

 | 

Title of the fixed area. If this parameter is passed, its value cannot be empty. The length must be less than 1024 characters.

 |
| 

content

 | 

Array<[RichText](#section28871613124714)\>

 | 

Creation: Yes

Update/Ending: No

 | 

Content in the fixed area. If this parameter is passed, its value cannot be empty.

-   The total length of text fields of all objects in the array must be less than 1024 characters.
-   If **textColor** is not set for an object in the array, the default text color **#99000000** will be used. If **textColor** is set for some objects in the array, its values for all these objects must be the same.

 |
| 

keepTime

 | 

number

 | 

No

 | 

Duration for storing a live view message in the notification panel after the live view is ended, in seconds. The value range is \[0, 3600\]. The default value is **0**.

 |
| 

clickAction

 | 

[WantAgent](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md)

 | 

Creation: Yes

Update/Ending: No

 | 

Default action executed after a user taps a live view. Call wantAgent.[getWantAgent()](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagentgetwantagent-1) to construct this parameter value.

 |
| 

extensionData

 | 

[ExtensionData](#section14934174734616)

 | 

No

 | 

Content in the auxiliary area.

 |
| 

[layoutData](#section1258265220124)

 | 

[ProgressLayout](#section199131329165016) | [PickupLayout](#section129929595142) | [FlightLayout](#section636916193215) | [ScoreLayout](#section16706148183416) | [NavigationLayout](#section19117745094)

 | 

Creation: Yes

Update/Ending: No

 | 

Content in the extension area.

NOTE:

In 5.0.0(12) and later versions, the parameter type **NavigationLayout** is also supported.

 |
| 

liveViewLockScreenPicture

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

File name of a large image for a lock screen immersive live view, in a specified path. If an actual image is passed, when a user taps the app icon in the live view capsule, presses and holds the live view capsule content, or presses and holds the widget content on the lock screen, the large image will be displayed for an immersive effect. If no image is passed or the passed image does not exist, user taps will not trigger the immersive state.

-   A value of the string type is the name of a file in **/resources/rawfile**. The length must be less than 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   You are advised to use a 1000 x 1000 image. GIF images are not supported.

NOTE:

Start version: 5.0.0(12)

 |
| 

liveViewLockScreenAbilityName

 | 

string

 | 

No

 | 

Name of the extension ability of lock screen immersive live views ([LiveViewLockScreenExtensionAbility](../liveviewlockscreenextensionability/document.md)). This parameter is valid only during live view creation. The value passed cannot be empty and can contain a maximum of 128 characters. If both this parameter and the **liveViewLockScreenPicture** parameter are passed during live view creation, only this parameter takes effect.

NOTE:

Start version: 5.0.0(12)

 |
| 

liveViewLockScreenAbilityParameters

 | 

Record<string, string>

 | 

No

 | 

Custom parameters passed to [LiveViewLockScreenExtensionAbility](../liveviewlockscreenextensionability/document.md) (the extension ability of lock screen immersive live views). If this parameter is passed, its value cannot be empty. A maximum of 50 key-value pairs are supported. After the custom parameters are passed, they can be obtained in **onSessionCreate()** of the ability through **want.parameters**.

NOTE:

Start version: 5.0.0(12)

 |
| 

backgroundType

 | 

[BackgroundType](#section15834105743213)

 | 

No

 | 

Background type of a live view widget. The background can be displayed only for the left-right text template ([layoutType](#section1765911975020) is set to **LAYOUT\_TYPE\_FLIGHT**).

When the passed background type is the moon-viewing flight or sunset flight and a special weather type (specified by [WeatherInfo](#section145641518183913)) such as rain or snow is passed, the weather background is preferentially displayed on the widget. For other non-special weather types, the moon-viewing flight or sunset flight background is preferentially displayed on the widget.

NOTE:

**Start version**: 6.0.0(20)

 |

#### BackgroundType

Widget background type in the flight scenario. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SYS\_BACKGROUND\_UNDEFINED

 | 

0

 | 

Undefined. No background is displayed on the widget.

 |
| 

SYS\_BACKGROUND\_FLIGHT\_MOON

 | 

100

 | 

Moon-viewing flight. The moon-viewing background is displayed on the widget.

 |
| 

SYS\_BACKGROUND\_FLIGHT\_SUNSET

 | 

101

 | 

Sunset flight. The sunset background is displayed on the widget.

 |

#### ExtensionData

Auxiliary area parameters.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

[ExtensionType](#section171431441533)

 | 

No

 | 

Type of an auxiliary area. The default value is [EXTENSION\_TYPE\_DEFAULT](#section171431441533), indicating that no auxiliary area is displayed.

 |
| 

text

 | 

string

 | 

Creation: Yes (only when **type** is set to **ExtensionType.EXTENSION\_TYPE\_COMMON\_TEXT** or **ExtensionType.EXTENSION\_TYPE\_CAPSULE\_TEXT**)

Update/Ending: No

 | 

Text information displayed in an auxiliary area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

pic

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes (only when **type** is set to **ExtensionType.EXTENSION\_TYPE\_PIC** or **ExtensionType.EXTENSION\_TYPE\_ICON**)

Update/Ending: No

 | 

Image displayed in an auxiliary area. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

clickAction

 | 

[WantAgent](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md)

 | 

No

 | 

Action executed after a user taps an auxiliary area. Call wantAgent.[getWantAgent()](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagentgetwantagent-1) to construct this parameter value.

 |

#### LayoutData

Defines the template type and public parameters of an extension area. This is used when [layoutType](#section1765911975020) is set to **LayoutType.LAYOUT\_TYPE\_DEFAULT**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

layoutType

 | 

[LayoutType](#section1765911975020)

 | 

Yes

 | 

Template type.

 |
| 

serviceButtons

 | 

Array<[ServiceButton](#section637116431585)\>

 | 

No

 | 

Structure array of passed associated service buttons. During associated service button update, you need to update also **clickAction** in [ExtensionData](#section14934174734616) of the auxiliary area.

NOTE:

**Start version**: 5.1.1(19)

 |
| 

isServiceButtonsDisplayed

 | 

boolean

 | 

No

 | 

Indicates whether to display the associated service buttons. The default value is **false**.

-   **true**: yes
-   **false**: no

NOTE:

**Start version**: 5.1.1(19)

 |
| 

weatherInfo

 | 

[WeatherInfo](#section145641518183913)

 | 

No

 | 

Passed weather information structure.

The destination weather type supports only the left-right text template (that is, [layoutType](#section1765911975020) is set to **LAYOUT\_TYPE\_FLIGHT**).

The local weather type supports only the basic template, progress visualization template, and emphasized text template (that is, [layoutType](#section1765911975020) is set to **LAYOUT\_TYPE\_DEFAULT**, **LAYOUT\_TYPE\_PROGRESS**, or **LAYOUT\_TYPE\_PICKUP**).

When weather information is passed and the background type (specified by [backgroundType](#section15834105743213)) passed is the moon-viewing flight (**SYS\_BACKGROUND\_FLIGHT\_MOON**) or sunset flight (**SYS\_BACKGROUND\_FLIGHT\_SUNSET**), the weather background is preferentially displayed on the live view widget for a special weather type related to rain or snow, and the moon-viewing flight or sunset flight background is preferentially displayed for other non-special weather types.

NOTE:

**Start version**:

The destination weather effect can be displayed since version 6.0.0(20).

The local weather effect can be displayed since version 6.0.2(22).

 |

#### WeatherInfo

Base class of weather information passed by the app.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

weatherType

 | 

[WeatherType](#section2062895313473)

 | 

No

 | 

Weather type. If **weatherType** is not passed or an invalid value is passed, the weather effect will not be displayed.

 |
| 

locationType

 | 

[WeatherLocationType](#section1597237195618)

 | 

No

 | 

Weather location type. If **locationType** is not passed or an invalid value is passed, the weather effect will not be displayed.

 |
| 

highTemperature

 | 

number

 | 

No

 | 

Highest temperature. Only Celsius is supported. The highest temperature must be less than or equal to 58°C and greater than the lowest temperature (specified by **lowTemperature**). If this parameter is not passed or an invalid value is passed, the temperature will not be displayed.

 |
| 

lowTemperature

 | 

number

 | 

No

 | 

Lowest temperature. Only Celsius is supported. The lowest temperature must be greater than or equal to –95°C and less than the highest temperature (specified by **highTemperature**). If this parameter is not passed or an invalid value is passed, the temperature will not be displayed.

 |

#### WeatherType

Weather type. The values are enumerated values. The weather background can be displayed on the widget only for the following weather types: light rain, moderate rain, heavy rain, light snow, moderate snow, and heavy snow. Other weather types (except **WEATHER\_TYPE\_UNDEFINED**) cannot be displayed as the weather background on the widget, and only the weather icon and temperature will be displayed on the widget.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

WEATHER\_TYPE\_UNDEFINED

 | 

0

 | 

No weather effect is displayed.

 |
| 

WEATHER\_TYPE\_SUNNY

 | 

1

 | 

Sunny.

 |
| 

WEATHER\_TYPE\_HAZY

 | 

5

 | 

Hazy.

 |
| 

WEATHER\_TYPE\_CLOUDY

 | 

7

 | 

Cloudy.

 |
| 

WEATHER\_TYPE\_OVERCAST

 | 

8

 | 

Overcast.

 |
| 

WEATHER\_TYPE\_FOG

 | 

11

 | 

Foggy.

 |
| 

WEATHER\_TYPE\_SHOWERS

 | 

12

 | 

Shower. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_T\_STORMS

 | 

15

 | 

Thundershower. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_RAIN

 | 

18

 | 

Rainy. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_SNOW

 | 

22

 | 

Snowy. A dynamic snow background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_RAIN\_AND\_SNOW

 | 

29

 | 

Sleet. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_HOT

 | 

30

 | 

Hot.

 |
| 

WEATHER\_TYPE\_COLD

 | 

31

 | 

Cold.

 |
| 

WEATHER\_TYPE\_WINDY

 | 

32

 | 

Windy.

 |
| 

WEATHER\_TYPE\_THUNDERSHOWER\_WITH\_HAIL

 | 

45

 | 

Hail.

 |
| 

WEATHER\_TYPE\_LIGHT\_RAIN

 | 

46

 | 

Light rain. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.0(20).

 |
| 

WEATHER\_TYPE\_MODERATE\_RAIN

 | 

47

 | 

Moderate rain. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.0(20).

 |
| 

WEATHER\_TYPE\_HEAVY\_RAIN

 | 

48

 | 

Heavy rain. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.0(20).

 |
| 

WEATHER\_TYPE\_STORM

 | 

49

 | 

Rainstorm. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_SEVERE\_STORM

 | 

51

 | 

Severe rainstorm. A dynamic rain background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_LIGHT\_SNOW

 | 

52

 | 

Light snow. A dynamic snow background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.0(20).

 |
| 

WEATHER\_TYPE\_MODERATE\_SNOW

 | 

53

 | 

Moderate snow. A dynamic snow background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.0(20).

 |
| 

WEATHER\_TYPE\_HEAVY\_SNOW

 | 

54

 | 

Heavy snow. A dynamic snow background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.0(20).

 |
| 

WEATHER\_TYPE\_SNOW\_STORM

 | 

55

 | 

Snowstorm. A dynamic snow background can be displayed for this weather type on the live view widget.

NOTE:

The dynamic weather background is supported since version 6.0.2(22).

 |
| 

WEATHER\_TYPE\_DUST\_STORM

 | 

56

 | 

Sand and dust storm.

 |
| 

WEATHER\_TYPE\_DUST

 | 

65

 | 

Floating dust.

 |
| 

WEATHER\_TYPE\_SAND

 | 

66

 | 

Blowing sand.

 |
| 

WEATHER\_TYPE\_SAND\_STORM

 | 

67

 | 

Severe sand and dust storm.

 |

#### WeatherLocationType

Weather location type. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

LOCATION\_TYPE\_LOCAL

 | 

1

 | 

Local weather. It only supports the basic template, progress visualization template, and emphasized text template (that is, [layoutType](#section1765911975020) is set to **LAYOUT\_TYPE\_DEFAULT**, **LAYOUT\_TYPE\_PROGRESS**, or **LAYOUT\_TYPE\_PICKUP**). The weather icon will be displayed on the right of the title in the fixed area.

NOTE:

The local weather effect can be displayed since version 6.0.2(22).

 |
| 

LOCATION\_TYPE\_DESTINATION

 | 

2

 | 

Destination weather. It only supports the left-right text template (that is, [layoutType](#section1765911975020) is set to **LAYOUT\_TYPE\_FLIGHT**). The weather icon and temperature will be displayed on the right in the extension area of the left-right text template, specifically, on the left of the title and content.

NOTE:

The destination weather effect can be displayed since version 6.0.0(20).

 |

#### ServiceButton

Base class of an associated service button passed by the app.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.1.1(19)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

Name of an associated service button. The length must be less than 128 characters. Any characters exceeding this limit will be truncated.

 |
| 

clickAction

 | 

[WantAgent](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md)

 | 

No

 | 

Redirection action triggered when a user taps the associated service button. Call wantAgent.[getWantAgent()](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagentgetwantagent-1) to construct this parameter value.

 |

#### ProgressLayout

Extension area parameters of the progress visualization template, which are inherited from [LayoutData](#section1258265220124). This is used when [layoutType](#section1765911975020) is set to **LayoutType.LAYOUT\_TYPE\_PROGRESS**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

progress

 | 

number

 | 

Yes

 | 

Progress percentage, which determines the position of the indicator in a progress bar. The value range is \[0, 100\].

 |
| 

color

 | 

string

 | 

No

 | 

Progress bar color. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. The default color is **#FF317AF7**.

 |
| 

backgroundColor

 | 

string

 | 

No

 | 

Progress bar background color. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. The default color is **#19000000**. For the dark mode, the default color is **#19FFFFFF**.

 |
| 

indicatorType

 | 

[IndicatorType](#section71841624105515)

 | 

No

 | 

Display type of the small indicator icon in an extension area. By default, the small icon is not displayed.

 |
| 

indicatorIcon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes (only when **indicatorType** is set to **IndicatorType.INDICATOR\_TYPE\_UP** or **IndicatorType.INDICATOR\_TYPE\_OVERLAY**)

Update/Ending: No

 | 

Progress bar indicator icon. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

lineType

 | 

[LineType](#section1888635517564)

 | 

No

 | 

Display type of a progress bar in an extension area. By default, the progress bar uses dotted lines.

 |
| 

nodeIcons

 | 

Array<string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

Creation: Yes

Update/Ending: No

 | 

Icon of each node in a progress bar. The array length range is \[2, 5\]. If this parameter is not passed during live view update or ending, the previous images will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |

#### PickupLayout

Extension area parameters of the emphasized text template, which are inherited from [LayoutData](#section1258265220124). This is used when [layoutType](#section1765911975020) is set to **LayoutType.LAYOUT\_TYPE\_PICKUP**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Title of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

content

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Content in an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

underlineColor

 | 

string

 | 

No

 | 

Underline color of the content in an extension area. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. By default, underlines are not displayed.

 |
| 

descPic

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes

Update/Ending: No

 | 

Product description image on the right of an extension area. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |

#### FlightLayout

Extension area parameters of the left-right text template, which are inherited from [LayoutData](#section1258265220124). This is used when [layoutType](#section1765911975020) is set to **LayoutType.LAYOUT\_TYPE\_FLIGHT**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

style

 | 

[FlightLayoutStyle](#section1181383342218)

 | 

No

 | 

Left-right text style type. If this parameter is not set, the emphasized style is used by default.

-   **0**: emphasized
-   **1**: balanced

NOTE:

Start version: 5.0.2(14)

 |
| 

firstTitle

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Title on the left of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

firstContent

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Content on the left of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

lastTitle

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Title on the right of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

lastContent

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Content on the right of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

lastTitleSuperscript

 | 

string

 | 

No

 | 

Superscript of a title on the right of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters. If this parameter is used to indicate that a journey spans more than one day, the passed value contains 2 characters, in +_X_ format, where _X_ is a digit. Example: +1 or +2

NOTE:

Start version: 5.0.2(14)

 |
| 

lastContentSuperscript

 | 

string

 | 

No

 | 

Superscript of the content on the right of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters. If this parameter is used to indicate that a journey spans more than one day, the passed value contains 2 characters, in +_X_ format, where _X_ is a digit. Example: +1 or +2

NOTE:

Start version: 5.0.2(14)

 |
| 

spaceType

 | 

[SpaceType](#section173441342102410)

 | 

No

 | 

Display type in the middle of an extension area of the left-right text template.

-   If this parameter is not passed or the value is **0**, the spacing icon specified by **spaceIcon** is displayed.
-   If the value is **1**, the spacing text specified by **spaceText** is displayed.

NOTE:

Start version: 5.0.2(14)

 |
| 

spaceIcon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes when **spaceType** is not set or set to **SpaceType.SPACE\_TYPE\_ICON**

 | 

Spacing icon in the middle of an extension area. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

spaceText

 | 

string

 | 

Creation: Yes when **spaceType** is set to **SpaceType.SPACE\_TYPE\_TEXT**

 | 

Spacing text in the middle of an extension area, which is used to display the date, for example, **10/28 Saturday** or **2025/09/15**.

The parameter value can contain a maximum of 12 characters and will be truncated if the length exceeds this limit.

If this parameter is not passed during live view update or ending, the previous text will be displayed.

NOTE:

Start version: 5.0.2(14)

 |
| 

isHorizontalLineDisplayed

 | 

boolean

 | 

No

 | 

Indicates whether to display the dividing line of an extension area. By default, the dividing line is displayed.

-   **true**: yes
-   **false**: no

 |
| 

additionalText

 | 

string

 | 

No

 | 

Content at the bottom of an extension area. The length must be less than 1024 characters.

NOTE:

Start version: 5.0.0(12)

 |

#### ScoreLayout

Extension area parameters of the live scores template, which are inherited from [LayoutData](#section1258265220124). This is used when [layoutType](#section1765911975020) is set to **LayoutType.LAYOUT\_TYPE\_SCORE**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

hostName

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Name on the left of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

hostIcon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes

Update/Ending: No

 | 

Icon on the left of an extension area. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

hostScore

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Score on the left of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

guestName

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Name on the right of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

guestIcon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes

Update/Ending: No

 | 

Icon on the right of an extension area. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

guestScore

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Score on the right of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

competitionDesc

 | 

string | Array<[RichText](#section28871613124714)\>

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Competition description in the upper middle part of an extension area. If this parameter is passed, its value cannot be empty.

-   When the value type is string, the value must be a string of less than 128 characters.
-   When the value type is Array<[RichText](#section28871613124714)\>:
    1.  The total length of text fields of all objects in the array must be less than 128 characters.
    2.  If **textColor** is not set for an object in the array, the default text color **#99000000** will be used. If **textColor** is set for some objects in the array, its values for all these objects must be the same.

NOTE:

In 5.0.0(12) and later versions, the input parameter type Array<[RichText](#section28871613124714)\> is also supported.

 |
| 

competitionTime

 | 

string

 | 

Creation or template change: Yes

Update/Ending: No

 | 

Competition time in the lower middle part of an extension area. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

isHorizontalLineDisplayed

 | 

boolean

 | 

No

 | 

Indicates whether to display the dividing line of an extension area. By default, the dividing line is displayed.

-   **true**: yes
-   **false**: no

 |

#### NavigationLayout

Extension area parameters of the navigation template, which are inherited from [LayoutData](#section1258265220124). This is used when [layoutType](#section1765911975020) is set to **LayoutType.LAYOUT\_TYPE\_NAVIGATION**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

currentNavigationIcon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes

Update/Ending: No

 | 

Current navigation direction.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 128 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
    If the local resource file does not exist, the live view creation will fail or the navigation template extension area will fail to be updated during live view update or ending.
    
    NOTE:
    
    To ensure optimal image display in both light and dark modes, the system applies color adaptation to PNG and SVG images. Images in other formats are displayed as-is and do not support color adaptation. For details, please refer to the navigation-dedicated template description in [widget templates](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section1511241615274).
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

navigationIcons

 | 

Array<string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

No

 | 

Images of arrows indicating navigation directions. The number of images can range from 1 to 11. If this parameter is not passed during live view creation, the extension area will not be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 128 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
    If the local resource files do not exist, the live view creation will fail or the navigation template extension area will fail to be updated during live view update or ending.
    
    NOTE:
    
    To ensure optimal image display in both light and dark modes, the system applies color adaptation to PNG and SVG images. Images in other formats are displayed as-is and do not support color adaptation. For details, please refer to the navigation-dedicated template description in [widget templates](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section1511241615274).
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

isNavigationIconsDisplayed

 | 

boolean

 | 

No

 | 

Indicates whether to display the images of arrows indicating navigation directions. If this parameter is not set during live view update or ending, the value passed in the previous state change will be used. If this parameter is not passed in other cases, the value **true** is used by default.

-   **true**: yes
-   **false**: no

**Start version**: 5.0.3(15)

 |

#### CapsuleData

Base class that defines basic attributes of a live view capsule.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

[CapsuleType](#section136243383011)

 | 

Yes

 | 

Type of a live view capsule.

 |
| 

status

 | 

number

 | 

Yes

 | 

Display status of a live view capsule.

-   **1**: The live view capsule is displayed.
-   **\-1**: The live view capsule display has ended.

 |
| 

icon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes

Update/Ending: No

 | 

Icon of a live view capsule. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 255 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |
| 

tailIcon

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

Tail icon of a live view capsule. If this parameter is not passed during live view update or ending, the previous image will be displayed.

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 255 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

NOTE:

**Start version**: 6.0.0(20)

 |
| 

backgroundColor

 | 

string

 | 

Creation: Yes

Update/Ending: No

 | 

Background color of a live view capsule. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. If this parameter is not set during live view update or ending, the color passed in the previous state change will be used.

The following colors are not recommended:

-   #FF000000
-   #FFFFFFFF
-   #FFF1F3F5

 |
| 

isContentDisplayed

 | 

boolean

 | 

No

 | 

Indicates whether to display the secondary text of a live view capsule. If this parameter is not set, the value passed during the previous live view creation or update will be used. If this parameter is not passed in other cases, the value **true** is used by default.

-   **true**: yes
-   **false**: no

If **isContentDisplayed** and **isTailIconDisplayed** are both set to **false**, the secondary text and tail icon of the live view capsule will not be displayed.

NOTE:

**Start version**: 5.0.3(15)

 |
| 

isTailIconDisplayed

 | 

boolean

 | 

No

 | 

Indicates whether to display the tail icon of a live view capsule. If this parameter is not set, the value passed during the previous live view creation or update will be used. If this parameter is not passed in other cases, the value **false** is used by default.

-   **true**: yes
-   **false**: no

If **isContentDisplayed** and **isTailIconDisplayed** are both set to **false**, the secondary text and tail icon of the live view capsule will not be displayed.

NOTE:

**Start version**: 6.0.0(20)

 |

#### TextCapsule

Text live view capsule parameters, which are inherited from [CapsuleData](#section1600824135815). This is used when [type](#section1600824135815) is set to **CapsuleType.CAPSULE\_TYPE\_TEXT**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

Creation: Yes

Update/Ending: No

 | 

Primary text of a live view capsule. The length must be less than 128 characters. If this parameter is passed, the value cannot be **null**, **undefined**, an empty string, or a string of spaces.

NOTE:

In 6.0.0(20) and later versions, if the input value is in the format of "Number:Number" and [layoutType](#section1765911975020) is set to **LAYOUT\_TYPE\_SCORE**, the system will automatically extract the images and scores on both sides of the extension area on a live view widget, update the live view capsule style, and display the team icons and scores.

 |
| 

content

 | 

string

 | 

No

 | 

Secondary text of a live view capsule. The length must be less than 128 characters. If this parameter is passed, the value cannot be **null**, **undefined**, an empty string, or a string of spaces.

 |

#### TimerCapsule

Timer live view capsule parameters, which are inherited from [CapsuleData](#section1600824135815). This is used when [type](#section1600824135815) is set to **CapsuleType.CAPSULE\_TYPE\_TIMER**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

content

 | 

string

 | 

No

 | 

Secondary text of a live view capsule. The length must be less than 128 characters. If this parameter is passed, the value cannot be **null**, **undefined**, an empty string, or a string of spaces.

 |
| 

time

 | 

number

 | 

No

 | 

Initial value of a live view capsule timer, in milliseconds. The value is updated every second. The default value is **0**.

 |
| 

isCountdown

 | 

boolean

 | 

No

 | 

Indicates whether to display a countdown timer.

-   **true**: yes
-   **false**: no (default value)

 |
| 

isPaused

 | 

boolean

 | 

No

 | 

Indicates whether a live view capsule timer is paused. A paused timer displays the time when it is paused.

-   **true**: yes
-   **false**: no (default value)

 |

#### ProgressCapsule

Progress live view capsule parameters, which are inherited from [CapsuleData](#section1600824135815). This is used when [type](#section1600824135815) is set to **CapsuleType.CAPSULE\_TYPE\_PROGRESS**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

max

 | 

number

 | 

No

 | 

Maximum value of a progress bar. The default value is **1**. The value range is \[1, 2147483647\].

 |
| 

progress

 | 

number

 | 

No

 | 

Current value of a progress bar. The default value is **0**. The value range is \[0, 2147483647\]. The actual progress is calculated as **progress**/**max**.

 |
| 

indeterminate

 | 

boolean

 | 

No

 | 

Progress display type. The progress is displayed as a ratio by default.

-   **true**: percentage
-   **false**: ratio (default value)

 |
| 

content

 | 

string

 | 

No

 | 

Secondary text of a live view capsule. The length must be less than 128 characters. If this parameter is passed, the value cannot be **null**, **undefined**, an empty string, or a string of spaces.

NOTE:

**Start version**: 6.0.0(20)

 |

#### ExternalData

Cover screen template parameters.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

Creation: Yes

Update/Ending: No

 | 

Title on a cover screen. If this parameter is passed, its value cannot be empty. The length must be less than 128 characters.

 |
| 

content

 | 

Array<[RichText](#section28871613124714)\>

 | 

Creation: Yes

Update/Ending: No

 | 

Content on a cover screen. You can set the color of some text in the character string for your app. If this parameter is passed, its value cannot be empty.

-   The total length of text fields of all objects in the array must be less than 128 characters.
-   If **textColor** is not set for an object in the array, the default text color **#99000000** will be used. If **textColor** is set for some objects in the array, its values for all these objects must be the same.

 |
| 

type

 | 

[ExternalType](#section5925948161213)

 | 

No

 | 

Background style type of a cover screen. By default, the background color is used.

NOTE:

Start version: 5.0.0(12)

 |
| 

backgroundColor

 | 

string

 | 

No

 | 

Background color of a cover screen. The value is in #RGB format, with a number sign (#) and 6 hexadecimal digits. The default color is **#F1F3F5**.

 |
| 

backgroundPicture

 | 

string | image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

Creation: Yes (only when **type** is set to **ExternalType.BACKGROUND\_PICTURE**)

Update/Ending: No (This parameter is valid when **type** is set to **ExternalType.BACKGROUND\_PICTURE**.)

 | 

Background image of a cover screen. If this parameter is not passed during live view update or ending, the previous image will be displayed.

NOTE:

Start version: 5.0.0(12)

-   When the value type is string, the value is the name of a local resource file in **/resources/rawfile**. The maximum length is 256 characters.
    
    Example: For the image file **icon.png** stored in **/resources/rawfile** of the app, the value is **icon.png**.
    
-   When the value type is image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), the image size cannot exceed 30 KB.

 |

#### RichText

Rich text parameters.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

string

 | 

Yes

 | 

Text content. The length must be less than 128 characters.

 |
| 

textColor

 | 

string

 | 

No

 | 

Text color. The value is in #ARGB format, with a number sign (#) and 8 hexadecimal digits. If **textColor** is not set, the default text color **#99000000** will be used. If **textColor** is set, its values for all objects in the array must be the same.

 |

#### LiveViewResult

Live view result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

resultCode

 | 

number

 | 

Live view result code.

-   **0**: success.
-   **1**: Failed to update/end the fixed area.
-   **2**: Failed to update/end the auxiliary area.
-   **3**: Failed to update/end the extension area.
-   **4**: Failed to update/end the live view capsule.
-   **5**: Failed to update/end the cover screen.

 |
| 

message

 | 

String

 | 

Live view result message.

 |

#### LayoutType

Type of an extension area. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

LAYOUT\_TYPE\_DEFAULT

 | 

\-1

 | 

The extension area is not displayed.

 |
| 

LAYOUT\_TYPE\_PROGRESS

 | 

3

 | 

Progress visualization.

 |
| 

LAYOUT\_TYPE\_PICKUP

 | 

4

 | 

Emphasized text.

 |
| 

LAYOUT\_TYPE\_FLIGHT

 | 

5

 | 

Left-right text.

 |
| 

LAYOUT\_TYPE\_SCORE

 | 

7

 | 

Live scores.

 |
| 

LAYOUT\_TYPE\_NAVIGATION

 | 

8

 | 

Navigation.

NOTE:

Start version: 5.0.0(12)

 |

#### ExtensionType

Type of an auxiliary area. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

EXTENSION\_TYPE\_DEFAULT

 | 

0

 | 

The auxiliary area is not displayed.

 |
| 

EXTENSION\_TYPE\_COMMON\_TEXT

 | 

1

 | 

Common text.

 |
| 

EXTENSION\_TYPE\_CAPSULE\_TEXT

 | 

2

 | 

Live view capsule text.

 |
| 

EXTENSION\_TYPE\_PIC

 | 

3

 | 

Image.

 |
| 

EXTENSION\_TYPE\_ICON

 | 

4

 | 

Icon.

 |

#### IndicatorType

Indicator type. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

INDICATOR\_TYPE\_UNDISPLAYED

 | 

0

 | 

The small indicator icon is not displayed.

 |
| 

INDICATOR\_TYPE\_UP

 | 

1

 | 

The indicator is displayed above the progress line.

 |
| 

INDICATOR\_TYPE\_OVERLAY

 | 

2

 | 

The indicator is displayed on the progress line.

 |

#### LineType

Type of a progress bar in an extension area. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

LINE\_TYPE\_DOTTED\_LINE

 | 

0

 | 

Dotted lines.

 |
| 

LINE\_TYPE\_NORMAL\_SOLID\_LINE

 | 

1

 | 

Solid lines.

 |
| 

LINE\_TYPE\_THICK\_SOLID\_LINE

 | 

2

 | 

Thick solid lines.

 |

#### CapsuleType

Live view capsule type. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CAPSULE\_TYPE\_TEXT

 | 

1

 | 

Text live view capsule.

 |
| 

CAPSULE\_TYPE\_TIMER

 | 

2

 | 

Timer live view capsule.

 |
| 

CAPSULE\_TYPE\_PROGRESS

 | 

3

 | 

Progress live view capsule.

 |

#### ExternalType

Background style type of a cover screen. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BACKGROUND\_COLOR

 | 

0

 | 

Background color.

 |
| 

BACKGROUND\_PICTURE

 | 

1

 | 

Background image.

 |

#### FlightLayoutStyle

Left-right text style type. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

STYLE\_FLIGHT\_EMPHASIS

 | 

0

 | 

Emphasized style.

 |
| 

STYLE\_FLIGHT\_BALANCE

 | 

1

 | 

Balanced style.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/JbTWnSnjRlWQFl6w_mi6wQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=970F6468137C7C53CFB7AD77882617B544E275788C2D0D5A003A24176955698E)

The extension area supports two styles: emphasized and balanced. The only difference lies in the font sizes of the title and content in the left-right text. The balanced style features a smaller title and larger content, delivering a more harmonious look compared to the emphasized style. For details about the template design styles, go to [Live View Design Guide > General Widget Templates > Template Types > Left-right text template](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section1511241615274).

#### SpaceType

Display type in the middle of an extension area of the left-right text template. The values are enumerated values.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SPACE\_TYPE\_ICON

 | 

0

 | 

Spacing icon.

 |
| 

SPACE\_TYPE\_TEXT

 | 

1

 | 

Spacing text.

 |
