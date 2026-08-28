# voipCall (In-App Call Management)

This module provides in-app call management functions, including reporting incoming and outgoing calls and call status to the system, as well as obtaining user touch events.

To obtain user touch events, you need to use [voipCall.on](#section7587131203319) to subscribe to **voipCallUiEvent** before the service process begins. When the service process ends, you can use [voipCall.off](#section84793361325) to cancel the subscription.

**Start version**: 4.1.0(11)

#### Module Import

import { voipCall } from '@kit.CallServiceKit';

#### VoipCallType

Enumerates call types.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

VOIP\_CALL\_VOICE

 | 

0

 | 

Voice call.

 |
| 

VOIP\_CALL\_VIDEO

 | 

1

 | 

Video call.

 |

#### VoipCallState

Enumerates call statuses.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

VOIP\_CALL\_STATE\_IDLE

 | 

0

 | 

Idle.

 |
| 

VOIP\_CALL\_STATE\_RINGING

 | 

1

 | 

Ringing.

 |
| 

VOIP\_CALL\_STATE\_ACTIVE

 | 

2

 | 

Active.

 |
| 

VOIP\_CALL\_STATE\_HOLDING

 | 

3

 | 

Holding.

 |
| 

VOIP\_CALL\_STATE\_DISCONNECTED

 | 

4

 | 

Disconnected.

 |
| 

VOIP\_CALL\_STATE\_DIALING

 | 

5

 | 

Dialing.

**Start version**: 5.0.0(12)

 |
| 

VOIP\_CALL\_STATE\_ANSWERED

 | 

6

 | 

Answering.

**Start version**: 5.0.0(12)

 |
| 

VOIP\_CALL\_STATE\_DISCONNECTING

 | 

7

 | 

Disconnecting.

**Start version**: 5.0.0(12)

 |

#### VoipCallUiEvent

Enumerates call events.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

VOIP\_CALL\_EVENT\_NONE

 | 

0

 | 

No event.

 |
| 

VOIP\_CALL\_EVENT\_VOICE\_ANSWER

 | 

1

 | 

Voice call answering event.

 |
| 

VOIP\_CALL\_EVENT\_VIDEO\_ANSWER

 | 

2

 | 

Video call answering event.

 |
| 

VOIP\_CALL\_EVENT\_REJECT

 | 

3

 | 

Call rejection event.

 |
| 

VOIP\_CALL\_EVENT\_HANGUP

 | 

4

 | 

Call hangup event.

 |
| 

VOIP\_CALL\_EVENT\_MUTED

 | 

5

 | 

Mute event.

**Start version**: 5.0.0(12)

 |
| 

VOIP\_CALL\_EVENT\_UNMUTED

 | 

6

 | 

Unmute event.

**Start version**: 5.0.0(12)

 |
| 

VOIP\_CALL\_EVENT\_SPEAKER\_ON

 | 

7

 | 

Speaker turn-on event.

**Start version**: 5.0.0(12)

(Reserved and not supported for now.)

 |
| 

VOIP\_CALL\_EVENT\_SPEAKER\_OFF

 | 

8

 | 

Speaker turn-off event.

**Start version**: 5.0.0(12)

(Reserved and not supported for now.)

 |

#### ErrorReason

Enumerates error code types.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

ERROR\_NONE

 | 

0

 | 

No error.

 |
| 

CELLULAR\_CALL\_EXISTS

 | 

1

 | 

A cellular call already exists.

 |
| 

VOIP\_CALL\_EXISTS

 | 

2

 | 

An in-app call already exists.

 |
| 

INVALID\_CALL

 | 

3

 | 

Certain call attributes (for example, call ID) are invalid.

 |
| 

USER\_ANSWER\_CELLULAR\_FIRST

 | 

4

 | 

The user chooses to answer the cellular call.

 |

#### VoipCallUiEventInfo

Defines call event information.

**System capability**: SystemCapability.Telephony.VoipCallManager

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

callId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of an in-app call.

 |
| 

voipCallUiEvent

 | 

[VoipCallUiEvent](#section26961727970)

 | 

No

 | 

No

 | 

In-app call event.

 |
| 

errorReason

 | 

[ErrorReason](#section15252018876)

 | 

No

 | 

No

 | 

Error code of an in-app call.

 |

#### VoipCallFailureCause

Enumerates incoming call failure causes.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

OTHER

 | 

0

 | 

Other failure causes.

 |
| 

ROUTE\_BUSY

 | 

1

 | 

Line busy.

 |
| 

CONNECTION\_FAILED

 | 

2

 | 

Call connection failure.

 |

#### VoipCallAttribute

Defines call attributes.

**System capability**: SystemCapability.Telephony.VoipCallManager

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

callId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of an in-app call.

 |
| 

voipCallType

 | 

[VoipCallType](#section0933646875)

 | 

No

 | 

No

 | 

In-app call type.

 |
| 

userName

 | 

string

 | 

No

 | 

No

 | 

User nickname of an in-app call.

 |
| 

userProfile

 | 

image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

User avatar. The image processing module needs to be imported. For details, please refer to [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md).

The imported image cannot exceed 221 x 221 pixels, and 112 x 112 pixels is recommended. The image obtained through the [getPixelBytesNumber](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md#getpixelbytesnumber7) API of [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) must be less than 196,608 bytes.

 |
| 

abilityName

 | 

string

 | 

No

 | 

No

 | 

Name of the app UI ability to be loaded after a call is answered.

 |
| 

voipCallState

 | 

[VoipCallState](#section24523814719)

 | 

No

 | 

No

 | 

In-app call status.

 |
| 

showBannerForIncomingCall

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the app displays a notification banner for an incoming or outgoing call.

**true**: yes

**false**: no

The default value is **true**.

**Start version**: 5.0.0(12)

 |
| 

isConferenceCall

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the call is a conference call.

**true**: yes

**false**: no

The default value is **false**.

**Start version**: 5.0.0(12)

 |
| 

isVoiceAnswerSupported

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether incoming or outgoing video calls support voice-only answering.

**true**: yes

**false**: no

The default value is **true**.

**Start version**: 5.0.0(12)

 |

#### CallAudioEvent

Enumerates mute and speaker events.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

AUDIO\_EVENT\_MUTED

 | 

0

 | 

The call is muted.

 |
| 

AUDIO\_EVENT\_UNMUTED

 | 

1

 | 

The call is unmuted.

 |
| 

AUDIO\_EVENT\_SPEAKER\_ON

 | 

2

 | 

The speaker is on.

 |
| 

AUDIO\_EVENT\_SPEAKER\_OFF

 | 

3

 | 

The speaker is off.

 |

#### voipCall.on('voipCallUiEvent')

on(type: 'voipCallUiEvent', callback: Callback<VoipCallUiEventInfo>): void

Subscribes to **voipCallUiEvent**. This API uses a callback to return the subscription result.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

type

 | 

string

 | 

Yes

 | 

Call event type. The value is fixed at **voipCallUiEvent**.

 |
| 

callback

 | 

Callback<[VoipCallUiEventInfo](#section1178710819715)\>

 | 

Yes

 | 

Callback for returning the call event information.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.on('voipCallUiEvent', (data: voipCall.VoipCallUiEventInfo) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in reading callback. CallId: ${data.callId}, voipCallUiEvent: ${data.voipCallUiEvent}\`);
});

#### voipCall.off('voipCallUiEvent')

off(type: 'voipCallUiEvent', callback?: Callback<VoipCallUiEventInfo>): void

Unsubscribes from **voipCallUiEvent**. This API uses a callback to return the unsubscription result.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

type

 | 

string

 | 

Yes

 | 

Call event type. The value is fixed at **voipCallUiEvent**.

 |
| 

callback

 | 

Callback<[VoipCallUiEventInfo](#section1178710819715)\>

 | 

No

 | 

Callback that needs to be cancelled. A **VoipCallUiEventInfo** object will be returned. If this parameter is not specified, all callbacks for this event will be cancelled.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.off('voipCallUiEvent', (data: voipCall.VoipCallUiEventInfo) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in reading callback. CallId: ${data.callId}, voipCallUiEvent: ${data.voipCallUiEvent}\`);
});

#### voipCall.reportIncomingCall

reportIncomingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

Notifies the system of incoming calls. This API returns the result asynchronously through a promise. If the call connection fails, you can call [reportIncomingCallError](#section155796451716) to notify the system of the call connection failure. Detailed call information needs to be set for using this API. For details, please refer to [VoipCallAttribute](#section4221135015444).

**System capability**: SystemCapability.Telephony.VoipCallManager

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

voipCallAttribute

 | 

[VoipCallAttribute](#section4221135015444)

 | 

Yes

 | 

Detailed call information, including the user avatar, nickname, and call ID. For details, please refer to [VoipCallAttribute](#section4221135015444). (When the app reports an outgoing call, the **voipCallState** attribute in **VoipCallAttribute** must be **VOIP\_CALL\_STATE\_DIALING**.)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ErrorReason](#section15252018876)\>

 | 

Promise that throws an error.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { image } from '@kit.ImageKit';
import { voipCall } from '@kit.CallServiceKit';
import { resourceManager } from '@kit.LocalizationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';

interface Content {
  data: string;
  callId: string;
}

export default class VoipAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
    pushService.receiveMessage('VoIP', this, async (data) => {
      let content: Content = JSON.parse(data.data);
      let callId: string = content.callId;

      hilog.info(0x0000, 'testTag', 'Get voip message successfully: %{public}s', callId);

      // Create an image of the **PixelMap** type as the avatar.
      const resourceMgr : resourceManager.ResourceManager = this.context.resourceManager;
      const fileData : Uint8Array = await resourceMgr.getRawFileContent('example.png');
      const buffer = fileData.buffer;
      const imageSource : image.ImageSource = image.createImageSource(buffer);
      const pixelMap : image.PixelMap = await imageSource.createPixelMap();
      if (pixelMap) {
        pixelMap.getImageInfo((err, imageInfo) => {
          if (imageInfo) {
            hilog.info(0x0000, 'testTag', \`DemoPushMessageAbility imageInfo: ${imageInfo.size.width} \* ${imageInfo.size.height}.\`);
          }
        });
      }

      // Construct a **VoipCallAttribute** object.
      let callInfo: voipCall.VoipCallAttribute = {
        callId: callId,
        voipCallType: voipCall.VoipCallType.VOIP\_CALL\_VOICE,
        userName: "name",
        userProfile: pixelMap,
        abilityName: 'ability',
        voipCallState: voipCall.VoipCallState.VOIP\_CALL\_STATE\_RINGING
      };

      // Notify the system of incoming calls.
      let error = await voipCall.reportIncomingCall(callInfo);
      if (error != voipCall.ErrorReason.ERROR\_NONE) {
        hilog.error(0x0000, 'testTag', 'Failed to report incoming call: %{public}d', error);
        return;
      }

      hilog.info(0x0000, 'testTag', 'Get voip message end.');
    });
    hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
  }
}

#### voipCall.reportOutgoingCall

reportOutgoingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

Reports outgoing calls. Detailed call information needs to be set for using this API. For details, please refer to [VoipCallAttribute](#section4221135015444). This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Telephony.VoipCallManager

**Start version**: 5.0.0(12)

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

voipCallAttribute

 | 

[VoipCallAttribute](#section4221135015444)

 | 

Yes

 | 

Detailed call information, including the user avatar, nickname, and call ID. For details, please refer to [VoipCallAttribute](#section4221135015444).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ErrorReason](#section15252018876)\>

 | 

Promise that throws an error.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { image } from '@kit.ImageKit';
import { voipCall } from '@kit.CallServiceKit';
import { resourceManager } from '@kit.LocalizationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';

interface Content {
  data: string;
  callId: string;
}

export default class VoipExtAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
    pushService.receiveMessage('VoIP', this, async (data) => {
      let content: Content = JSON.parse(data.data);
      let callId: string = content.callId;

      hilog.info(0x0000, 'testTag', 'Get voip message successfully: %{public}s', callId);

      // Create an image of the PixelMap type as the avatar.
      const resourceMgr : resourceManager.ResourceManager = this.context.resourceManager;
      const fileData : Uint8Array = await resourceMgr.getRawFileContent('example.png');
      const buffer = fileData.buffer;
      const imageSource : image.ImageSource = image.createImageSource(buffer);
      const pixelMap : image.PixelMap = await imageSource.createPixelMap();
      if (pixelMap) {
        pixelMap.getImageInfo((err, imageInfo) => {
          if (imageInfo) {
            hilog.info(0x0000, 'testTag', \`DemoPushMessageAbility imageInfo: ${imageInfo.size.width} \* ${imageInfo.size.height}.\`);
          }
        });
      }

      // Construct a **VoipCallAttribute** object.
      let callInfo: voipCall.VoipCallAttribute = {
        callId: callId,
        voipCallType: voipCall.VoipCallType.VOIP\_CALL\_VOICE,
        userName: "name",
        userProfile: pixelMap,
        abilityName: 'ability',
        voipCallState: voipCall.VoipCallState.VOIP\_CALL\_STATE\_DIALING
      };

      // Notify the system of outgoing calls.
      let error = await voipCall.reportOutgoingCall(callInfo);
      if (error != voipCall.ErrorReason.ERROR\_NONE) {
        hilog.error(0x0000, 'testTag', 'Failed to report outgoing call: %{public}d', error);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Get voip message end.');
    });
    hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
  }
}

#### voipCall.reportCallAudioEventChange

reportCallAudioEventChange(callId: string, callAudioEvent: CallAudioEvent): Promise<void>

Reports call mute and speaker events. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Telephony.VoipCallManager

**Start version**: 5.0.0(12)

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

callId

 | 

string

 | 

Yes

 | 

Unique ID of an in-app call.

 |
| 

callAudioEvent

 | 

[CallAudioEvent](#section312217120409)

 | 

Yes

 | 

VoIP call mute/unmute and speaker events. For details, please refer to [CallAudioEvent](#section312217120409).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { voipCall } from '@kit.CallServiceKit';
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

interface Content {
  data: string;
  callId: string;
}

export default class VoipExtAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', 'VoipExtAbility onCreate.');
    pushService.receiveMessage('VoIP', this, async (data) => {
      let content: Content = JSON.parse(data.data);
      let callId: string = content.callId;

      let callAudioEvent : voipCall.CallAudioEvent = voipCall.CallAudioEvent.AUDIO\_EVENT\_MUTED;

      // Report call mute and speaker events.
      voipCall.reportCallAudioEventChange(callId, callAudioEvent).then(() => {
        hilog.info(0x0000, 'testTag', \`Succeeded in reporting call audio event change.\`);
      });
    });
    hilog.info(0x0000, 'testTag', 'Succeeded in registering VoIP.');
  }
}

#### voipCall.reportCallStateChange

reportCallStateChange(callId: string, callState: VoipCallState): Promise<void>

Notifies the system of in-app call status changes. This API returns the result asynchronously through a promise.

This API cannot be used to change the call type. For example, a voice call cannot be upgraded to a video call, and a video call cannot be downgraded to a voice call. To upgrade or downgrade a call, call the [voipCall.reportCallStateChange](#section5360122718341) API.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

callId

 | 

string

 | 

Yes

 | 

Call ID.

 |
| 

callState

 | 

[VoipCallState](#section24523814719)

 | 

Yes

 | 

Call status. For details, please refer to [VoipCallState](#section24523814719).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.reportCallStateChange("callId123", voipCall.VoipCallState.VOIP\_CALL\_STATE\_ACTIVE).then(() => {
  hilog.info(0x0000, 'testTag', \`Succeeded in reporting call state change.\`);
});

#### voipCall.reportCallStateChange

reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>

Notifies an in-app call status change and specifies the call type. This API returns the result asynchronously through a promise.

This API supports voice answering for an incoming video call and allows switching between video and voice during an ongoing call. The correct call type must be passed.

**System capability**: SystemCapability.Telephony.VoipCallManager

**Start version**: 5.0.0(12)

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

callId

 | 

string

 | 

Yes

 | 

Call ID.

 |
| 

callState

 | 

[VoipCallState](#section24523814719)

 | 

Yes

 | 

Call status. For details, please refer to [VoipCallState](#section24523814719).

 |
| 

callType

 | 

[VoipCallType](#section0933646875)

 | 

Yes

 | 

Call type. For details, please refer to [VoipCallType](#section0933646875).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.reportCallStateChange("callId123", voipCall.VoipCallState.VOIP\_CALL\_STATE\_ACTIVE, voipCall.VoipCallType.VOIP\_CALL\_VOICE).then(() => {
  hilog.info(0x0000, 'testTag', \`Succeeded in reporting call state change.\`);
});

#### voipCall.reportIncomingCallError

reportIncomingCallError(callId: string, voipCallFailureCause: VoipCallFailureCause): Promise<void>

Notifies the system of the call connection failure cause. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Telephony.VoipCallManager

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

callId

 | 

string

 | 

Yes

 | 

Unique ID of an in-app call.

 |
| 

voipCallFailureCause

 | 

[VoipCallFailureCause](#section157617591167)

 | 

Yes

 | 

Call connection failure cause.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1007200001

 | 

Invalid parameter value.

 |
| 

1007200002

 | 

Operation failed. Cannot connect to service.

 |
| 

1007200003

 | 

System internal error.

 |
| 

1007200999

 | 

Unknown error code.

 |

**Example**:

import { voipCall } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

voipCall.reportIncomingCallError("callId123", voipCall.VoipCallFailureCause.OTHER).then(() => {
  hilog.info(0x0000, 'testTag', \`Succeeded in reporting incoming call error.\`);
});
