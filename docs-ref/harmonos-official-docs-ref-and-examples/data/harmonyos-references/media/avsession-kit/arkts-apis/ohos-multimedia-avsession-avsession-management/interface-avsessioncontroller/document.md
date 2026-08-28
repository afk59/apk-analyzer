# Interface (AVSessionController)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/yp_Q1hxtQJ-Jsg8Wi6hHKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A813D2D380D667F8ADA799CE6986319FA31C6FFC4B7C64E3C189D22590537F0)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 10.

Through the AV session controller, you can query the session ID, send commands and events to a session, and obtain session metadata and playback state information.

#### Modules to Import

import { avSession } from '@kit.AVSessionKit';

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sessionId10+ | string | Yes | No | Unique session ID of the AVSessionController object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private AVSessionController?: avSession.AVSessionController;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio").then(async (data: avSession.AVSession) => {
      this.currentAVSession = data;
      this.sessionId = this.currentAVSession.sessionId;
      this.AVSessionController = await this.currentAVSession.getController();
      console.info('CreateAVSession :  SUCCESS :sessionId = ${this.sessionId}');
    }).catch((err: BusinessError) => {
      console.error(\`CreateController BusinessError: code: ${err.code}, message: ${err.message}\`);
    });
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### getAVPlaybackState10+

getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void

Obtains the remote playback state. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVPlaybackState](../interfaces-others/document.md#avplaybackstate10)\> | Yes | Callback used to return the remote playback state. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVPlaybackState((err: BusinessError, state: avSession.AVPlaybackState) => {
  if (err) {
    console.error(\`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('getAVPlaybackState : SUCCESS');
  }
});

#### getAVPlaybackState10+

getAVPlaybackState(): Promise<AVPlaybackState>

Obtains the remote playback state. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVPlaybackState](../interfaces-others/document.md#avplaybackstate10)\> | Promise used to return the remote playback state. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
  console.info('getAVPlaybackState : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getAVMetadata10+

getAVMetadata(): Promise<AVMetadata>

Obtains the session metadata. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVMetadata](../interfaces-others/document.md#avmetadata10)\> | Promise used to return the metadata obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVMetadata().then((metadata: avSession.AVMetadata) => {
  console.info(\`GetAVMetadata : SUCCESS : assetId : ${metadata.assetId}\`);
}).catch((err: BusinessError) => {
  console.error(\`GetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getAVMetadata10+

getAVMetadata(callback: AsyncCallback<AVMetadata>): void

Obtains the session metadata. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVMetadata](../interfaces-others/document.md#avmetadata10)\> | Yes | Callback used to return the metadata obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVMetadata((err: BusinessError, metadata: avSession.AVMetadata) => {
  if (err) {
    console.error(\`GetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`GetAVMetadata : SUCCESS : assetId : ${metadata.assetId}\`);
  }
});

#### getAVQueueTitle10+

getAVQueueTitle(): Promise<string>

Obtains the name of the playlist. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the playlist name. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueTitle().then((title: string) => {
  console.info(\`GetAVQueueTitle : SUCCESS : title : ${title}\`);
}).catch((err: BusinessError) => {
  console.error(\`GetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getAVQueueTitle10+

getAVQueueTitle(callback: AsyncCallback<string>): void

Obtains the name of the playlist. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the playlist name. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueTitle((err: BusinessError, title: string) => {
  if (err) {
    console.error(\`GetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`GetAVQueueTitle : SUCCESS : title : ${title}\`);
  }
});

#### getAVQueueItems10+

getAVQueueItems(): Promise<Array<AVQueueItem>>

Obtains the information related to the items in the queue. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\>> | Promise used to return the items in the queue. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueItems().then((items: avSession.AVQueueItem\[\]) => {
  console.info(\`GetAVQueueItems : SUCCESS : length : ${items.length}\`);
}).catch((err: BusinessError) => {
  console.error(\`GetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getAVQueueItems10+

getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void

Obtains the information related to the items in the playlist. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\>> | Yes | Callback used to return the items in the playlist. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueItems((err: BusinessError, items: avSession.AVQueueItem\[\]) => {
  if (err) {
    console.error(\`GetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`GetAVQueueItems : SUCCESS : length : ${items.length}\`);
  }
});

#### skipToQueueItem10+

skipToQueueItem(itemId: number): Promise<void>

Sends the ID of an item in the playlist to the session for processing. The session can play the song. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemId | number | Yes | ID of an item in the playlist. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the item ID is sent, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let queueItemId = 0;
avsessionController.skipToQueueItem(queueItemId).then(() => {
  console.info('SkipToQueueItem successfully');
}).catch((err: BusinessError) => {
  console.error(\`SkipToQueueItem BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### skipToQueueItem10+

skipToQueueItem(itemId: number, callback: AsyncCallback<void>): void

Sends the ID of an item in the playlist to the session for processing. The session can play the song. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemId | number | Yes | ID of an item in the playlist. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let queueItemId = 0;
avsessionController.skipToQueueItem(queueItemId, (err: BusinessError) => {
  if (err) {
    console.error(\`SkipToQueueItem BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('SkipToQueueItem successfully');
  }
});

#### getOutputDevice10+

getOutputDevice(): Promise<OutputDeviceInfo>

Obtains the output device information. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)\> | Promise used to return the information obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getOutputDevice().then((deviceInfo: avSession.OutputDeviceInfo) => {
  console.info('GetOutputDevice : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getOutputDevice10+

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

Obtains the output device information. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)\> | Yes | Callback used to return the information obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getOutputDevice((err: BusinessError, deviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(\`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('GetOutputDevice : SUCCESS');
  }
});

#### sendAVKeyEvent10+

sendAVKeyEvent(event: KeyEvent): Promise<void>

Sends a key event to the session corresponding to this controller. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [KeyEvent](../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md) | Yes | Key event. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the event is sent, no value is returned; otherwise, an error object is returned. |

**Example**

import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:\[keyItem\], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

avsessionController.sendAVKeyEvent(event).then(() => {
  console.info('SendAVKeyEvent Successfully');
}).catch((err: BusinessError) => {
  console.error(\`SendAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### sendAVKeyEvent10+

sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void

Sends a key event to the session corresponding to this controller. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [KeyEvent](../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md) | Yes | Key event. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the event is sent, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |

**Example**

import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:\[keyItem\], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};
avsessionController.sendAVKeyEvent(event, (err: BusinessError) => {
  if (err) {
    console.error(\`SendAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('SendAVKeyEvent Successfully');
  }
});

#### getLaunchAbility10+

getLaunchAbility(): Promise<WantAgent>

Obtains the WantAgent object saved by the application in the session. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md)\> | Promise used to return the object saved by calling [setLaunchAbility](../interface-avsession/document.md#setlaunchability10). The object includes the application property, such as the bundle name, ability name, and device ID. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getLaunchAbility().then((agent: object) => {
  console.info(\`GetLaunchAbility : SUCCESS : wantAgent : ${agent}\`);
}).catch((err: BusinessError) => {
  console.error(\`GetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getLaunchAbility10+

getLaunchAbility(callback: AsyncCallback<WantAgent>): void

Obtains the WantAgent object saved by the application in the session. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md)\> | Yes | Callback used to return the object saved by calling [setLaunchAbility](../interface-avsession/document.md#setlaunchability10). The object includes the application property, such as the bundle name, ability name, and device ID. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getLaunchAbility((err: BusinessError, agent: object) => {
  if (err) {
    console.error(\`GetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`GetLaunchAbility : SUCCESS : wantAgent : ${agent}\`);
  }
});

#### getRealPlaybackPositionSync10+

getRealPlaybackPositionSync(): number

Obtains the playback position.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Playback position, in milliseconds. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

let time: number = avsessionController.getRealPlaybackPositionSync();

#### isActive10+

isActive(): Promise<boolean>

Checks whether the session is activated. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result indicating whether the session is activated. **true** if activated, **false** otherwise. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.isActive().then((isActive: boolean) => {
  console.info(\`IsActive : SUCCESS : isactive : ${isActive}\`);
}).catch((err: BusinessError) => {
  console.error(\`IsActive BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### isActive10+

isActive(callback: AsyncCallback<boolean>): void

Checks whether the session is activated. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result indicating whether the session is activated. **true** if activated, **false** otherwise. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.isActive((err: BusinessError, isActive: boolean) => {
  if (err) {
    console.error(\`IsActive BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`IsActive : SUCCESS : isactive : ${isActive}\`);
  }
});

#### destroy10+

destroy(): Promise<void>

Destroys this controller. A controller can no longer be used after being destroyed. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the controller is destroyed, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.destroy().then(() => {
  console.info('Destroy : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(\`Destroy BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### destroy10+

destroy(callback: AsyncCallback<void>): void

Destroys this controller. A controller can no longer be used after being destroyed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the controller is destroyed, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.destroy((err: BusinessError) => {
  if (err) {
    console.error(\`Destroy BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Destroy : SUCCESS ');
  }
});

#### getValidCommands10+

getValidCommands(): Promise<Array<AVControlCommandType>>

Obtains valid commands supported by the session. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AVControlCommandType](../types/document.md#avcontrolcommandtype10)\>> | Promise used to return a set of valid commands. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getValidCommands().then((validCommands: avSession.AVControlCommandType\[\]) => {
  console.info(\`GetValidCommands : SUCCESS : size : ${validCommands.length}\`);
}).catch((err: BusinessError) => {
  console.error(\`GetValidCommands BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getValidCommands10+

getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void

Obtains valid commands supported by the session. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AVControlCommandType](../types/document.md#avcontrolcommandtype10)\>> | Yes | Callback used to return a set of valid commands. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getValidCommands((err: BusinessError, validCommands: avSession.AVControlCommandType\[\]) => {
  if (err) {
    console.error(\`GetValidCommands BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`GetValidCommands : SUCCESS : size : ${validCommands.length}\`);
  }
});

#### sendControlCommand10+

sendControlCommand(command: AVControlCommand): Promise<void>

Sends a control command to the session through the controller. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/MX9hpbbZQWi0jAGhGcrbGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E84017E82EB641B989FC7311079887963A3B28A429DB2D8F0FFE5F6CDB7C66F)

Before using **sendControlCommand**, the controller must ensure that the corresponding listeners are registered for the media session. For details about how to register the listeners, see [on'play'](../interface-avsession/document.md#onplay10), [on'pause'](../interface-avsession/document.md#onpause10), and the like.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| command | [AVControlCommand](../interfaces-others/document.md#avcontrolcommand10) | Yes | Command to send. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the command is sent, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVControlCommand = {command:'play'};
avsessionController.sendControlCommand(avCommand).then(() => {
  console.info('SendControlCommand successfully');
}).catch((err: BusinessError) => {
  console.error(\`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### sendControlCommand10+

sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void

Sends a control command to the session through the controller. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/idJiBw-PTICbEy6_bqRDFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E8A9A466A89AFD068E4FC15415784C1D027B4CB39FF777B0D29BE46492B3876)

Before using **sendControlCommand**, the controller must ensure that the corresponding listeners are registered for the media session. For details about how to register the listeners, see [on'play'](../interface-avsession/document.md#onplay10), [on'pause'](../interface-avsession/document.md#onpause10), and the like.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| command | [AVControlCommand](../interfaces-others/document.md#avcontrolcommand10) | Yes | Command to send. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the command is sent, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVControlCommand = {command:'play'};
avsessionController.sendControlCommand(avCommand, (err: BusinessError) => {
  if (err) {
    console.error(\`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('SendControlCommand successfully');
  }
});

#### sendCommonCommand10+

sendCommonCommand(command: string, args: Record<string, Object>): Promise<void>

Sends a custom control command to the session through the controller. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| command | string | Yes | Name of the custom control command. |
| args | Record<string, Object> | Yes | 
Parameters in key-value pair format carried in the custom control command.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is {\[key: string\]: Object}.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/7apRf8QnQpe2kZkPZj1WpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C362D87AC55860C0BDDA47A187C41861F51D6F95B83FE5460CE11F04DA93256)

The **args** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the command is sent, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(\`CreateAVSession : SUCCESS :sessionId = ${sessionId}\`);
}).catch((err: BusinessError) => {
  console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
});
let commandName = "my\_command";
if (controller !== undefined) {
  (controller as avSession.AVSessionController).sendCommonCommand(commandName, {command : "This is my command"}).then(() => {
    console.info('SendCommonCommand successfully');
  }).catch((err: BusinessError) => {
    console.error(\`SendCommonCommand BusinessError: code: ${err.code}, message: ${err.message}\`);
  })
}

#### sendCommonCommand10+

sendCommonCommand(command: string, args: Record<string, Object>, callback: AsyncCallback<void>): void

Sends a custom control command to the session through the controller. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| command | string | Yes | Name of the custom control command. |
| args | Record<string, Object> | Yes | 
Parameters in key-value pair format carried in the custom control command.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is {\[key: string\]: Object}.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the command is sent, **err** is **undefined**; otherwise, **err** is an error object. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/vqw_k69gTzapg4N0VcUmeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60825431D777F1996654E5E72BC2D3162D48C84601310B03AA548333A3EAC480)

The **args** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
          
let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(\`CreateAVSession : SUCCESS :sessionId = ${sessionId}\`);
}).catch((err: BusinessError) => {
  console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
});
let commandName = "my\_command";
if (controller !== undefined) {
  (controller as avSession.AVSessionController).sendCommonCommand(commandName, {command : "This is my command"}, (err: BusinessError) => {
    if (err) {
      console.error(\`SendCommonCommand BusinessError: code: ${err.code}, message: ${err.message}\`);
    }
  })
}

#### sendCustomData20+

sendCustomData(data: Record<string, Object>): Promise<void>

Sends custom data to the remote device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | Record<string, Object> | Yes | Custom data filled by the application. Only objects with the key **'customData'** and of the type string are parsed on the server. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {
    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(\`CreateAVSession : SUCCESS :sessionId = ${this.sessionId}\`);
      })
      .catch((err: BusinessError) => {
        console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
      });

    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).sendCustomData({ customData: "This is my data" })
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### getExtras10+

getExtras(): Promise<Record<string, Object>>

Obtains the custom media packet set by the provider. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Record<string, Object>> | 
Promise used to return the custom media packet. The content of the packet is the same as that set in **setExtras**.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the return value type is Promise<{\[key: string\]: Object}>.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(\`CreateAVSession : SUCCESS :sessionId = ${this.sessionId}\`);
      }).catch((err: BusinessError) => {
      console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
    });
    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).getExtras().then((extras) => {
        console.info(\`getExtras : SUCCESS : ${extras}\`);
      }).catch((err: BusinessError) => {
        console.error(\`getExtras BusinessError: code: ${err.code}, message: ${err.message}\`);
      });
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### getExtras10+

getExtras(callback: AsyncCallback<Record<string, Object>>): void

Obtains the custom media packet set by the provider. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Record<string, Object>> | Yes | 
Callback used to return the custom media packet. The content of the packet is the same as that set in **setExtras**.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is AsyncCallback<{\[key: string\]: Object}>.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(\`CreateAVSession : SUCCESS :sessionId = ${sessionId}\`);
}).catch((err: BusinessError) => {
  console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).getExtras((err, extras) => {
    if (err) {
      console.error(\`getExtras BusinessError: code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info(\`getExtras : SUCCESS : ${extras}\`);
    }
  });
}

#### getExtrasWithEvent18+

getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>

Obtains the custom media packet set by the remote distributed media provider based on the remote distributed event type. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| extraEvent | string | Yes | 
Remote distributed event type.

Currently, the following event types are supported:

**'AUDIO\_GET\_VOLUME'**: obtains the volume of the remote device.

**'AUDIO\_GET\_AVAILABLE\_DEVICES'**: obtains all remote devices that can be connected.

**'AUDIO\_GET\_PREFERRED\_OUTPUT\_DEVICE\_FOR\_RENDERER\_INFO'**: obtains the actual remote audio device.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ExtraInfo](../types/document.md#extrainfo18)\> | 
Promise used to return the custom media packet set by the remote distributed media provider.

The **ExtraInfo** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let controller: avSession.AVSessionController | ESObject;
const COMMON\_COMMAND\_STRING\_1 = 'AUDIO\_GET\_VOLUME';
const COMMON\_COMMAND\_STRING\_2 = 'AUDIO\_GET\_AVAILABLE\_DEVICES';
const COMMON\_COMMAND\_STRING\_3 = 'AUDIO\_GET\_PREFERRED\_OUTPUT\_DEVICE\_FOR\_RENDERER\_INFO';
if (controller !== undefined) {
  controller.getExtrasWithEvent(COMMON\_COMMAND\_STRING\_1).then(() => {
    console.info(\`${\[COMMON\_COMMAND\_STRING\_1\]}\`);
  }).catch((err: BusinessError) => {
    console.error(\`getExtrasWithEvent failed with err: ${err.code}, ${err.message}\`);
  })

  controller.getExtrasWithEvent(COMMON\_COMMAND\_STRING\_2).then(() => {
    console.info(\`${\[COMMON\_COMMAND\_STRING\_2\]}\`);
  }).catch((err: BusinessError) => {
    console.error(\`getExtrasWithEvent failed with err: ${err.code}, ${err.message}\`);
  })

  controller.getExtrasWithEvent(COMMON\_COMMAND\_STRING\_3).then(() => {
    console.info(\`${\[COMMON\_COMMAND\_STRING\_3\]}\`);
  }).catch((err: BusinessError) => {
    console.error(\`getExtrasWithEvent failed with err: ${err.code}, ${err.message}\`);
  })
}

#### on('metadataChange')10+

on(type: 'metadataChange', filter: Array<string> | 'all', callback: (data: AVMetadata) => void): void

Subscribes to metadata change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The event **'metadataChange'** is triggered when the session metadata requires an update.

"Requires an update" means the corresponding property value has been reset, regardless of whether the new value matches the old one.

 |
| filter | Array<string>|'all' | Yes | 

The value **'all'** indicates that any call state field change will trigger the event, and **Array<string>** indicates that only changes to the listed call state field will trigger the event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is Array<keyof AVMetadata> | 'all'.

 |
| callback | (data: [AVMetadata](../interfaces-others/document.md#avmetadata10)) => void | Yes | Callback used for subscription. The **data** parameter in the callback indicates the metadata that requires an update, but not the complete current metadata set. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('metadataChange', 'all', (metadata: avSession.AVMetadata) => {
  console.info(\`on metadataChange assetId : ${metadata.assetId}\`);
});

avsessionController.on('metadataChange', \['assetId', 'title', 'description'\], (metadata: avSession.AVMetadata) => {
  console.info(\`on metadataChange assetId : ${metadata.assetId}\`);
});

#### off('metadataChange')10+

off(type: 'metadataChange', callback?: (data: AVMetadata) => void): void

Unsubscribes from metadata change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'metadataChange'** in this case. |
| callback | (data: [AVMetadata](../interfaces-others/document.md#avmetadata10)) => void | No | 
Callback used for subscription. The **data** parameter in the callback indicates the metadata that requires an update, but not the complete current metadata set.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('metadataChange');

#### on('playbackStateChange')10+

on(type: 'playbackStateChange', filter: Array<string> | 'all', callback: (state: AVPlaybackState) => void): void

Subscribes to playback state change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The event **'playbackStateChange'** is triggered when the playback state requires an update.

"Requires an update" means the corresponding property value has been reset, regardless of whether the new value matches the old one.

 |
| filter | Array<string>|'all' | Yes | 

The value **'all'** indicates monitoring for updates to all playback state fields,

Array<string> indicates listening for updates to fields in the array,

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is Array<keyof AVPlaybackstate> | 'all'.

 |
| callback | (state: [AVPlaybackState](../interfaces-others/document.md#avplaybackstate10)) => void | Yes | Callback function, where the **state** parameter indicates the playback state that requires an update, but not the complete current playback state set. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  console.info(\`on playbackStateChange state : ${playbackState.state}\`);
});

avsessionController.on('playbackStateChange', \['state', 'speed', 'loopMode'\], (playbackState: avSession.AVPlaybackState) => {
  console.info(\`on playbackStateChange state : ${playbackState.state}\`);
});

#### off('playbackStateChange')10+

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)

Unsubscribes from playback state change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'playbackStateChange'** in this case. |
| callback | (state: [AVPlaybackState](../interfaces-others/document.md#avplaybackstate10)) => void | No | 
Callback function, where the **state** parameter indicates the playback state that requires an update, but not the complete current playback state set.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('playbackStateChange');

#### on('callMetadataChange')11+

on(type: 'callMetadataChange', filter: Array<string> | 'all', callback: Callback<CallMetadata>): void

Subscribes to call metadata change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'callMetadataChange'** is triggered when the call metadata changes. |
| filter | Array<string>|'all' | Yes | 
The value **'all'** indicates that any call metadata field change will trigger the event, and **Array<string>** indicates that only changes to the listed metadata field will trigger the event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is Array<keyof CallMetadata> | 'all'.

 |
| callback | Callback<[CallMetadata](../interfaces-others/document.md#callmetadata11)\> | Yes | Callback used for subscription. The **callmetadata** parameter in the callback indicates the changed call metadata. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('callMetadataChange', 'all', (callmetadata: avSession.CallMetadata) => {
  console.info(\`on callMetadataChange state : ${callmetadata.name}\`);
});

avsessionController.on('callMetadataChange', \['name'\], (callmetadata: avSession.CallMetadata) => {
  console.info(\`on callMetadataChange state : ${callmetadata.name}\`);
});

#### off('callMetadataChange')11+

off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void

Unsubscribes from call metadata change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'callMetadataChange'** in this case. |
| callback | Callback<[CallMetadata](../interfaces-others/document.md#callmetadata11)\> | No | 
Callback used for unsubscription. The **calldata** parameter in the callback indicates the changed call metadata.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('callMetadataChange');

#### on('callStateChange')11+

on(type: 'callStateChange', filter: Array<string> | 'all', callback: Callback<AVCallState>): void

Subscribes to call state change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'callStateChange'** is triggered when the call state changes. |
| filter | Array<string>|'all' | Yes | 
The value **'all'** indicates that any call state field change will trigger the event, and **Array<string>** indicates that only changes to the listed call state field will trigger the event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is Array<keyof AVCallState> | 'all'.

 |
| callback | Callback<[AVCallState](../interfaces-others/document.md#avcallstate11)\> | Yes | Callback function, where the **callstate** parameter indicates the new call state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [AVSession Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('callStateChange', 'all', (callstate: avSession.AVCallState) => {
  console.info(\`on callStateChange state : ${callstate.state}\`);
});

avsessionController.on('callStateChange', \['state'\], (callstate: avSession.AVCallState) => {
  console.info(\`on callStateChange state : ${callstate.state}\`);
});

#### off('callStateChange')11+

off(type: 'callStateChange', callback?: Callback<AVCallState>): void

Unsubscribes from call state change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'callStateChange'** in this case. |
| callback | Callback<[AVCallState](../interfaces-others/document.md#avcallstate11)\> | No | 
Callback function, where the **callstate** parameter indicates the new call metadata.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [AVSession Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('callMetadataChange');

#### on('sessionDestroy')10+

on(type: 'sessionDestroy', callback: () => void): void

Subscribes to session destruction events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'sessionDestroy'** is triggered when a session is destroyed. |
| callback | () => void | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('sessionDestroy', () => {
  console.info('on sessionDestroy : SUCCESS ');
});

#### off('sessionDestroy')10+

off(type: 'sessionDestroy', callback?: () => void): void

Unsubscribes from session destruction events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'sessionDestroy'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('sessionDestroy');

#### on('activeStateChange')10+

on(type: 'activeStateChange', callback: (isActive: boolean) => void): void

Subscribes to session activation state change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'activeStateChange'** is triggered when the activation state of the session changes. |
| callback | (isActive: boolean) => void | Yes | Callback used for subscription. The **isActive** parameter in the callback specifies whether the session is activated. **true** if activated, **false** otherwise. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('activeStateChange', (isActive: boolean) => {
  console.info(\`on activeStateChange : SUCCESS : isActive ${isActive}\`);
});

#### off('activeStateChange')10+

off(type: 'activeStateChange', callback?: (isActive: boolean) => void): void

Unsubscribes from session activation state change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'activeStateChange'** in this case. |
| callback | (isActive: boolean) => void | No | 
Callback used for unsubscription. The **isActive** parameter in the callback specifies whether the session is activated. **true** if activated, **false** otherwise.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('activeStateChange');

#### on('validCommandChange')10+

on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void): void

Subscribes to valid command change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'validCommandChange'** is triggered when the valid commands supported by the session changes. |
| callback | (commands: Array<[AVControlCommandType](../types/document.md#avcontrolcommandtype10)\>) => void | Yes | Callback used for subscription. The **commands** parameter in the callback is a set of valid commands. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('validCommandChange', (validCommands: avSession.AVControlCommandType\[\]) => {
  console.info(\`validCommandChange : SUCCESS : size : ${validCommands.length}\`);
  console.info(\`validCommandChange : SUCCESS : validCommands : ${validCommands.values()}\`);
});

#### off('validCommandChange')10+

off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void): void

Unsubscribes from valid command change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'validCommandChange'** in this case. |
| callback | (commands: Array<[AVControlCommandType](../types/document.md#avcontrolcommandtype10)\>) => void | No | 
Callback used for unsubscription. The **commands** parameter in the callback is a set of valid commands.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('validCommandChange');

#### on('outputDeviceChange')10+

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

Subscribes to output device change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'outputDeviceChange'** is triggered when the output device changes. |
| callback | (state: [ConnectionState](../enums/document.md#connectionstate10), device: [OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)) => void | Yes | Callback used for subscription. The **device** parameter in the callback indicates the output device information. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(\`on outputDeviceChange state: ${state}, device : ${device}\`);
});

#### off('outputDeviceChange')10+

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

Unsubscribes from output device change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'outputDeviceChange'** in this case. |
| callback | (state: [ConnectionState](../enums/document.md#connectionstate10), device: [OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)) => void | No | 
Callback function, where the **device** parameter specifies the output device information.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('outputDeviceChange');

#### on('sessionEvent')10+

on(type: 'sessionEvent', callback: (sessionEvent: string, args: Record<String, Object>) => void): void

Subscribes to session event change events. This API is called by the controller.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'sessionEvent'** is triggered when the session event changes. |
| callback | (sessionEvent: string, args: Record<String, Object>) => void | Yes | 
Callback used for subscription. **sessionEvent** in the callback indicates the name of the session event that changes, and **args** indicates the parameters carried in the event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is (sessionEvent: string, args: {\[key: string\]: Object}) => void.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
       
let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(\`CreateAVSession : SUCCESS :sessionId = ${sessionId}\`);
}).catch((err: BusinessError) => {
  console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('sessionEvent', (sessionEvent, args) => {
    console.info(\`OnSessionEvent, sessionEvent is ${sessionEvent}, args: ${JSON.stringify(args)}\`);
  });
}

#### off('sessionEvent')10+

off(type: 'sessionEvent', callback?: (sessionEvent: string, args: Record<String, Object>) => void): void

Unsubscribes from session events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'sessionEvent'** in this case. |
| callback | sessionEvent: string, args: Record<String, Object> => void | No | 
Callback used for unsubscription. **sessionEvent** in the callback indicates the name of the session event that changes, and **args** indicates the parameters carried in the event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is (sessionEvent: string, args: {\[key: string\]: Object}) => void.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('sessionEvent');

#### on('queueItemsChange')10+

on(type: 'queueItemsChange', callback: (items: Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\>) => void): void

Subscribes to playlist item change events. This API is called by the controller.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'queueItemsChange'** is triggered when one or more items in the playlist changes. |
| callback | (items: Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\>) => void | Yes | Callback used for subscription. The **items** parameter in the callback indicates the changed items in the playlist. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('queueItemsChange', (items: avSession.AVQueueItem\[\]) => {
  console.info(\`OnQueueItemsChange, items length is ${items.length}\`);
});

#### off('queueItemsChange')10+

off(type: 'queueItemsChange', callback?: (items: Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\>) => void): void

Unsubscribes from playback item change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'queueItemsChange'** in this case. |
| callback | (items: Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\>) => void | No | 
Callback used for unsubscription. The **items** parameter in the callback indicates the changed items in the playlist.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('queueItemsChange');

#### on('queueTitleChange')10+

on(type: 'queueTitleChange', callback: (title: string) => void): void

Subscribes to playlist name change events. This API is called by the controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'queueTitleChange'** is triggered when the playlist name changes. |
| callback | (title: string) => void | Yes | Callback used for subscription. The **title** parameter in the callback indicates the changed playlist name. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.on('queueTitleChange', (title: string) => {
  console.info(\`queueTitleChange, title is ${title}\`);
});

#### off('queueTitleChange')10+

off(type: 'queueTitleChange', callback?: (title: string) => void): void

Unsubscribes from playlist name change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'queueTitleChange'** in this case. |
| callback | (title: string) => void | No | 
Callback used for unsubscription. The **items** parameter in the callback indicates the changed playlist name.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('queueTitleChange');

#### on('extrasChange')10+

on(type: 'extrasChange', callback: (extras: Record<string, Object>) => void): void

Subscribes to custom media packet change events. This API is called by the controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'extrasChange'** is triggered when the provider sets a custom media packet. |
| callback | (extras: Record<string, Object>) => void | Yes | 
Callback used for subscription. The **extras** parameter in the callback indicates the custom media packet set by the provider. This packet is the same as that set in **dispatchSessionEvent**.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is (extras: {\[key: string\]: Object}) => void.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(\`CreateAVSession : SUCCESS :sessionId = ${sessionId}\`);
}).catch((err: BusinessError) => {
  console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('extrasChange', (extras) => {
    console.info(\`Caught extrasChange event,the new extra is: ${JSON.stringify(extras)}\`);
  });
}

#### off('extrasChange')10+

off(type: 'extrasChange', callback?: (extras: Record<string, Object>) => void): void

Unsubscribes from custom media packet change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'extrasChange'** in this case. |
| callback | (extras: Record<string, Object>) => void | No | 
Callback used for unsubscription.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is (extras: {\[key: string\]: Object}) => void.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('extrasChange');

#### on('customDataChange')20+

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

Subscribes to events indicating that custom data is sent to a remote device.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'customDataChange'** is triggered when the provider sends custom data. |
| callback | Callback<Record<string, Object>> | Yes | Callback used to receive the custom data. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(\`CreateAVSession : SUCCESS :sessionId = ${sessionId}\`);
}).catch((err: BusinessError) => {
  console.error(\`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}\`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('customDataChange', (callback) => {
    console.info(\`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}\`);
  });
}

#### off('customDataChange')20+

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

Unsubscribes from events indicating that custom data is sent to a remote device.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'customDataChange'** in this case. |
| callback | Callback<Record<string, Object>> | No | Callback used for unsubscription. The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

avsessionController.off('customDataChange');

#### getAVPlaybackStateSync10+

getAVPlaybackStateSync(): AVPlaybackState;

Obtains the playback state of this session. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AVPlaybackState](../interfaces-others/document.md#avplaybackstate10) | Playback state of the session. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let playbackState: avSession.AVPlaybackState = avsessionController.getAVPlaybackStateSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getAVPlaybackStateSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### getAVMetadataSync10+

getAVMetadataSync(): AVMetadata

Obtains the session metadata. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AVMetadata](../interfaces-others/document.md#avmetadata10) | Session metadata. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let metaData: avSession.AVMetadata = avsessionController.getAVMetadataSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getAVMetadataSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### getAVCallState11+

getAVCallState(): Promise<AVCallState>

Obtains the call state. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVCallState](../interfaces-others/document.md#avcallstate11)\> | Promise used to return the call state obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVCallState().then((callstate: avSession.AVCallState) => {
  console.info(\`getAVCallState : SUCCESS : state : ${callstate.state}\`);
}).catch((err: BusinessError) => {
  console.error(\`getAVCallState BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getAVCallState11+

getAVCallState(callback: AsyncCallback<AVCallState>): void

Obtains the call state. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVCallState](../interfaces-others/document.md#avcallstate11)\> | Yes | Callback used to return the call state obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVCallState((err: BusinessError, callstate: avSession.AVCallState) => {
  if (err) {
    console.error(\`getAVCallState BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`getAVCallState : SUCCESS : state : ${callstate.state}\`);
  }
});

#### getCallMetadata11+

getCallMetadata(): Promise<CallMetadata>

Obtains the call metadata. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CallMetadata](../interfaces-others/document.md#callmetadata11)\> | Promise used to return the metadata obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getCallMetadata().then((calldata: avSession.CallMetadata) => {
  console.info(\`getCallMetadata : SUCCESS : name : ${calldata.name}\`);
}).catch((err: BusinessError) => {
  console.error(\`getCallMetadata BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getCallMetadata11+

getCallMetadata(callback: AsyncCallback<CallMetadata>): void

Obtains the call metadata. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[CallMetadata](../interfaces-others/document.md#callmetadata11)\> | Yes | Callback used to return the metadata obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getCallMetadata((err: BusinessError, calldata: avSession.CallMetadata) => {
  if (err) {
    console.error(\`getCallMetadata BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`getCallMetadata : SUCCESS : name : ${calldata.name}\`);
  }
});

#### getAVQueueTitleSync10+

getAVQueueTitleSync(): string

Obtains the name of the playlist of this session. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Playlist name. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentQueueTitle: string = avsessionController.getAVQueueTitleSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getAVQueueTitleSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### getAVQueueItemsSync10+

getAVQueueItemsSync(): Array<AVQueueItem>

Obtains the information related to the items in the playlist of this session. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\> | Items in the queue. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentQueueItems: Array<avSession.AVQueueItem> = avsessionController.getAVQueueItemsSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getAVQueueItemsSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### getOutputDeviceSync10+

getOutputDeviceSync(): OutputDeviceInfo

Obtains the output device information. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10) | Information about the output device. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentOutputDevice: avSession.OutputDeviceInfo = avsessionController.getOutputDeviceSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getOutputDeviceSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### isActiveSync10+

isActiveSync(): boolean

Checks whether the session is activated. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the session is activated. **true** if activated, **false** otherwise. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isActive: boolean = avsessionController.isActiveSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`isActiveSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### getValidCommandsSync10+

getValidCommandsSync(): Array<AVControlCommandType>

Obtains valid commands supported by the session. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[AVControlCommandType](../types/document.md#avcontrolcommandtype10)\> | A set of valid commands. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validCommands: Array<avSession.AVControlCommandType> = avsessionController.getValidCommandsSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getValidCommandsSync error, error code: ${error.code}, error message: ${error.message}\`);
}
