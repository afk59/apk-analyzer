# Outgoing Call

#### Use Cases

The app initiates a voice or video call.

When an outgoing call is made, the call capsule appears in the upper left corner of the screen since the app is in the foreground and no notification banner is needed. The display effect of an outgoing call is as follows.

<table><tbody><tr><td class="cellrowborder" valign="top" width="25%"><p><strong>Outgoing Voice Call (Calling)</strong></p></td><td class="cellrowborder" valign="top" width="25%"><p><strong>Outgoing Voice Call (Ongoing)</strong></p></td><td class="cellrowborder" valign="top" width="25%"><p><strong>Outgoing Video Call (Calling)</strong></p></td><td class="cellrowborder" valign="top" width="25%"><p><strong>Outgoing Video Call (Ongoing)</strong></p></td></tr><tr><td class="cellrowborder" valign="top" width="25%"><p><span><img height="502.059705" originheight="2720" originwidth="1260" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/aYNYpTawTy-suMNhphenkw/en-us_image_0000002444782180.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062101Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=3544DF6BC9D6A3575C3040CB1EE50E3FBD1ECA2A8C65CA36DF4AC18000230EF1" title="Click to enlarge" width="241.395"></span></p></td><td class="cellrowborder" valign="top" width="25%"><p><span><img height="501.190816" originheight="2720" originwidth="1260" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/jPIudJFiRWW0vK8PdYjrDw/en-us_image_0000002444622324.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062101Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=3A78D50279D498277837D52B71ACF53E3824A96CA6DB911B404552C78A040895" title="Click to enlarge" width="239.4"></span></p></td><td class="cellrowborder" valign="top" width="25%"><p><span><img height="496.22938400000004" originheight="2720" originwidth="1260" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/5TDMDQXbRv6b6ixMqSrLyA/en-us_image_0000002444622312.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062101Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=2A6DD1CF233D3C4035F3A7884F29FEE5C52646BE5C2912F38F8DD0F0147991AC" title="Click to enlarge" width="238.4025"></span></p></td><td class="cellrowborder" valign="top" width="25%"><p><span><img height="493.675784" originheight="2720" originwidth="1260" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/HGs6X6yGTauz1dgxukTEIg/en-us_image_0000002444782176.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062101Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=233D8983D42E12A087AB0A8AF04D2B30F5560E3987FE3CF772CEED0343C112BE" title="Click to enlarge" width="238.80150000000003"></span></p></td></tr></tbody></table>

For an outgoing call, the user can pull down the notification center panel to mute and unmute the call, or hang up on the live view banner.

<table><tbody><tr><td class="cellrowborder" valign="top" width="50%"><p><strong>Outgoing Call Live View Notification (Calling)</strong></p></td><td class="cellrowborder" valign="top" width="50%"><p><strong>Outgoing Call Live View Notification (Ongoing)</strong></p></td></tr><tr><td class="cellrowborder" valign="top" width="50%"><p><span><img height="502.503526" originheight="2720" originwidth="1260" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/eR6P6tI-QJKjxwYu5a7bfg/en-us_image_0000002444782184.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062101Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=AB47F54C5107C831FAC1D675BADCF0A644191319D2B2291E31D939A888E26104" title="Click to enlarge" width="241.395"></span></p></td><td class="cellrowborder" valign="top" width="50%"><p><span><img height="499.94301" originheight="2720" originwidth="1260" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/buaqVjD6RxKRpwAXpfLGGg/en-us_image_0000002444622316.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062101Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=3EDB5A554F8012ED6031BF8D6327DC8F11F8F225F3180B8A62343F2B54164A94" title="Click to enlarge" width="240.3975"></span></p></td></tr></tbody></table>

#### Restrictions

The outgoing call capability is supported on phones and tablets. Starting from version 6.0(20), it is also supported on wearables.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/1zLN_-nuRFCWgKK_62X2nw/en-us_image_0000002444782188.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B5D309F17BC741FF8AD3DAA867B6C80493FEADD6B289D7B9A008D6BA33B0A28 "Click to enlarge")

#### API Description

APIs used for outgoing calls are provided by [voipCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall). For details, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'voipCallUiEvent', callback: Callback<VoipCallUiEventInfo>): void

 | 

Subscribes to **voipCallUiEvent**.

 |
| 

off(type: 'voipCallUiEvent', callback?: Callback<VoipCallUiEventInfo>): void

 | 

Unsubscribes from **voipCallUiEvent**.

 |
| 

reportOutgoingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>

 | 

Reports the outgoing call.

 |
| 

reportCallAudioEventChange(callId: string, callAudioEvent: CallAudioEvent): Promise<void>

 | 

Reports the audio event.

 |
| 

reportCallStateChange(callId: string, callState: VoipCallState): Promise<void>

 | 

Reports the call status change.

 |
| 

reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>

 | 

Reports the call status change and specifies the call type.

 |

#### Development Procedure

The development procedure for outgoing calls is similar to that for incoming calls.

1.  Import dependencies.
    
    import { voipCall } from '@kit.CallServiceKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Subscribe to **voipCallUiEvent** to detect the user's mute, unmute, and hang-up operations on the live view notification banner. It is recommended to complete the step before reporting the outgoing call.
    
    Sample code:
    
    // Subscribe to **voipCallUiEvent**.
    voipCall.on('voipCallUiEvent', callback => {
      hilog.info(0x0000, 'CallDemo', 'Succeeded in registering voipCallUiEvent');
    });
    
3.  After a call connection is established within the app, the outgoing call must be reported to Call Service Kit along with call details. For more information, please refer to  [VoipCallAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section4221135015444).
    
    The system displays the call capsule in the upper-left corner of the screen.
    
    Sample code:
    
    // Construct parameters for reporting the outgoing call.
    let voipCallAttribute: voipCall.VoipCallAttribute = {
      callId: '1234567890',
      voipCallType: voipCall.VoipCallType.VOIP\_CALL\_VOICE,
      userName: 'Jack',
      userProfile: image.createPixelMapSync(new ArrayBuffer(100), { size: { width: 90, height: 90 } }),
      abilityName: 'VoipCallAbility',
      voipCallState: voipCall.VoipCallState.VOIP\_CALL\_STATE\_DIALING,  // The status for the outgoing call must be **DIALING**.
      showBannerForIncomingCall: true
    };
    
    // Report the outgoing call to Call Service Kit.
    voipCall.reportOutgoingCall(voipCallAttribute).then(errorReason => {
      if (errorReason == voipCall.ErrorReason.ERROR\_NONE) {
        hilog.info(0x0000, 'CallDemo', 'Succeeded in reporting the outgoing call');
      } else {
        hilog.error(0x0000, 'CallDemo', 'Failed to report the outgoing call: %{public}d', errorReason);
      }
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/HDSCl5PvS2e2v9OKDarXfg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6BBA38C1868FF0FCAEEB0CB6410CB02C5B68BC65B0E5476E05A92444C93C384)
    
    When the outgoing call is reported, it must be in **VOIP\_CALL\_STATE\_DIALING** state. Otherwise, Call Service Kit will consider the parameter invalid and return error code [1007200001](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-error-code#section13010304159).
    
4.  If the call is answered, the app needs to report the [VOIP\_CALL\_STATE\_ACTIVE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section24523814719) state to Call Service Kit. The system will then update the call capsule and begin displaying the elapsed call time.
    
    Sample code:
    
    // The app server receives a message indicating that the call is answered.
    let answeredCallId = '123456';
    
    // Report the call status to Call Service Kit.
    voipCall.reportCallStateChange(answeredCallId, voipCall.VoipCallState.VOIP\_CALL\_STATE\_ACTIVE);
    
5.  For the outgoing call, the user can also pull down the notification center panel to mute or unmute the call on the live view notification banner.
    
    The development procedure is the same as that for an incoming call. For details, please refer to [the instructions for muting or unmuting an incoming call](../incoming-call/document.md#li161271020155311).
    
6.  Additionally, the user can pull down the notification center panel to hang up on the live view banner.
    
    The development procedure is the same as that for an incoming call. For details, please refer to [the instructions for hanging up an incoming call](../incoming-call/document.md#li12946111323712).
    
7.  Unsubscribe from **voipCallUiEvent** after the call is ended.
    
    Sample code:
    
    // Unsubscribe from **voipCallUiEvent**.
    voipCall.off('voipCallUiEvent', callback => {
      hilog.info(0x0000, 'CallDemo', \`Succeeded in unRegistering voipCallUiEvent, callId: ${callback.callId}\`);
    });
