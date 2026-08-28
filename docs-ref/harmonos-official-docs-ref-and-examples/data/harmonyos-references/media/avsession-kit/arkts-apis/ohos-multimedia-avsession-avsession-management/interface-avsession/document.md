# Interface (AVSession)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/8Ixj6dB4T1WCfJXtkJFJlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45F5341571F29566CAC927EF9BC6AE9873CC779E78E31871B88FAE9776FAB1FC)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 10.

An AVSession object is created by calling [avSession.createAVSession](../functions/document.md#avsessioncreateavsession10). The object enables you to obtain the session ID and set the metadata and playback state.

#### Modules to Import

import { avSession } from '@kit.AVSessionKit';

#### Properties

**System capability**: SystemCapability.Multimedia.AVSession.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sessionId10+ | string | Yes | No | 
Unique session ID of the AVSession object.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| sessionType10+ | [AVSessionType](../types/document.md#avsessiontype10) | Yes | No | 

AVSession type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| sessionTag22+ | string | Yes | No | 

Custom tag information of the AVSession.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

**Example**

let sessionId: string = currentAVSession.sessionId;
let sessionType: avSession.AVSessionType = currentAVSession.sessionType;

#### setAVMetadata10+

setAVMetadata(data: AVMetadata): Promise<void>

Sets session metadata. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [AVMetadata](../interfaces-others/document.md#avmetadata10) | Yes | Session metadata. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let metadata: avSession.AVMetadata = {
  assetId: "121278",
  title: "lose yourself",
  artist: "Eminem",
  author: "ST",
  album: "Slim shady",
  writer: "ST",
  composer: "ST",
  duration: 2222,
  mediaImage: "https://www.example.com/example.jpg",
  subtitle: "8 Mile",
  description: "Rap",
  // The LRC contains two types of elements: time tag + lyrics, and ID tag.
  // Example: \[00:25.44\]xxx\\r\\n\[00:26.44\]xxx\\r\\n
  lyric: "Lyrics in LRC format",
  // The singleLyricText field stores a single line of lyric text without timestamps.
  // Example: "Content of a single lyric line"
  singleLyricText: "Content of a single lyric line",
  previousAssetId: "121277",
  nextAssetId: "121279"
};
currentAVSession.setAVMetadata(metadata).then(() => {
  console.info('SetAVMetadata successfully');
}).catch((err: BusinessError) => {
  console.error(\`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### setAVMetadata10+

setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void

Sets session metadata. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [AVMetadata](../interfaces-others/document.md#avmetadata10) | Yes | Session metadata. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let metadata: avSession.AVMetadata = {
  assetId: "121278",
  title: "lose yourself",
  artist: "Eminem",
  author: "ST",
  album: "Slim shady",
  writer: "ST",
  composer: "ST",
  duration: 2222,
  mediaImage: "https://www.example.com/example.jpg",
  subtitle: "8 Mile",
  description: "Rap",
  // The LRC contains two types of elements: time tag + lyrics, and ID tag.
  // Example: \[00:25.44\]xxx\\r\\n\[00:26.44\]xxx\\r\\n
  lyric: "Lyrics in LRC format",
  // The singleLyricText field stores a single line of lyric text without timestamps.
  // Example: "Content of a single lyric line"
  singleLyricText: "Content of a single lyric line",
  previousAssetId: "121277",
  nextAssetId: "121279"
};
currentAVSession.setAVMetadata(metadata, (err: BusinessError) => {
  if (err) {
    console.error(\`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('SetAVMetadata successfully');
  }
});

#### setCallMetadata11+

setCallMetadata(data: CallMetadata): Promise<void>

Sets call metadata. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [CallMetadata](../interfaces-others/document.md#callmetadata11) | Yes | Call metadata. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    try {
      let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE\_URI');
      let imageSource = await image.createImageSource(value.buffer);
      let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
      let calldata: avSession.CallMetadata = {
        name: "xiaoming",
        phoneNumber: "111xxxxxxxx",
        avatar: imagePixel
      };
      await this.currentAVSession?.setCallMetadata(calldata);
      console.info('setCallMetadata successfully');
    } catch (err) {
      if (err) {
        console.error('setCallMetadata BusinessError: code: ${err.code}, message: ${err.message}');
      } else {
        console.error('setCallMetadata Error: ${err}')
      }
    }
  }
}

#### setCallMetadata11+

setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void

Sets call metadata. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [CallMetadata](../interfaces-others/document.md#callmetadata11) | Yes | Call metadata. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    try {
      let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE\_URI');
      let imageSource = await image.createImageSource(value.buffer);
      let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
      let calldata: avSession.CallMetadata = {
        name: "xiaoming",
        phoneNumber: "111xxxxxxxx",
        avatar: imagePixel
      };
      this.currentAVSession?.setCallMetadata(calldata, (err: BusinessError) => {
        if (err) {
          console.error('setCallMetadata BusinessError: code: ${err.code}, message: ${err.message}');
        } else {
          console.info("setCallMetadata successfully");
        }
      });
    }catch (syncErr) {
      console.error('Syncronous operation failed: ${syncErr}');
    }
  }
}

#### setAVCallState11+

setAVCallState(state: AVCallState): Promise<void>

Sets the call state. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVCallState](../interfaces-others/document.md#avcallstate11) | Yes | Call state. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let calldata: avSession.AVCallState = {
  state: avSession.CallState.CALL\_STATE\_ACTIVE,
  muted: false
};
currentAVSession.setAVCallState(calldata).then(() => {
  console.info('setAVCallState successfully');
}).catch((err: BusinessError) => {
  console.error(\`setAVCallState BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### setAVCallState11+

setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void

Sets the call state. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVCallState](../interfaces-others/document.md#avcallstate11) | Yes | Call state. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avcalldata: avSession.AVCallState = {
  state: avSession.CallState.CALL\_STATE\_ACTIVE,
  muted: false
};
currentAVSession.setAVCallState(avcalldata, (err: BusinessError) => {
  if (err) {
    console.error(\`setAVCallState BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('setAVCallState successfully');
  }
});

#### setAVPlaybackState10+

setAVPlaybackState(state: AVPlaybackState): Promise<void>

Sets information related to the session playback state. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVPlaybackState](../interfaces-others/document.md#avplaybackstate10) | Yes | Information related to the session playback state. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let playbackState: avSession.AVPlaybackState = {
  state:avSession.PlaybackState.PLAYBACK\_STATE\_PLAY,
  speed: 1.0,
  position:{elapsedTime:10, updateTime:(new Date()).getTime()},
  bufferedTime:1000,
  loopMode:avSession.LoopMode.LOOP\_MODE\_SINGLE,
  isFavorite:true
};
currentAVSession.setAVPlaybackState(playbackState).then(() => {
  console.info('SetAVPlaybackState successfully');
}).catch((err: BusinessError) => {
  console.error(\`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### setAVPlaybackState10+

setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void

Sets information related to the session playback state. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AVPlaybackState](../interfaces-others/document.md#avplaybackstate10) | Yes | Information related to the session playback state. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let PlaybackState: avSession.AVPlaybackState = {
  state:avSession.PlaybackState.PLAYBACK\_STATE\_PLAY,
  speed: 1.0,
  position:{elapsedTime:10, updateTime:(new Date()).getTime()},
  bufferedTime:1000,
  loopMode:avSession.LoopMode.LOOP\_MODE\_SINGLE,
  isFavorite:true
};
currentAVSession.setAVPlaybackState(PlaybackState, (err: BusinessError) => {
  if (err) {
    console.error(\`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('SetAVPlaybackState successfully');
  }
});

#### setLaunchAbility10+

setLaunchAbility(ability: WantAgent): Promise<void>

Sets a launcher ability. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | Application properties, such as the bundle name, ability name, and deviceID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// WantAgentInfo object.
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: \[
    {
      deviceId: "deviceId",
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility",
      action: "action1",
      entities: \["entity1"\],
      type: "MIMETYPE",
      uri: "key = {true,true,false}",
      parameters:
        {
          mykey0: 2222,
          mykey1: \[1, 2, 3\],
          mykey2: "\[1, 2, 3\]",
          mykey3: "ssssssssssssssssssssssssss",
          mykey4: \[false, true, false\],
          mykey5: \["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"\],
          mykey6: true
        }
    }
  \],
  operationType: wantAgent.OperationType.START\_ABILITIES,
  requestCode: 0,
  wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent).then(() => {
    console.info('SetLaunchAbility successfully');
  }).catch((err: BusinessError) => {
    console.error(\`SetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}\`);
  });
});

#### setLaunchAbility10+

setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void

Sets a launcher ability. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | Application properties, such as the bundle name, ability name, and deviceID. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// WantAgentInfo object.
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: \[
    {
      deviceId: "deviceId",
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility",
      action: "action1",
      entities: \["entity1"\],
      type: "MIMETYPE",
      uri: "key = {true,true,false}",
      parameters:
        {
          mykey0: 2222,
          mykey1: \[1, 2, 3\],
          mykey2: "\[1, 2, 3\]",
          mykey3: "ssssssssssssssssssssssssss",
          mykey4: \[false, true, false\],
          mykey5: \["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"\],
          mykey6: true
        }
    }
  \],
  operationType: wantAgent.OperationType.START\_ABILITIES,
  requestCode: 0,
  wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent, (err: BusinessError) => {
    if (err) {
      console.error(\`SetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info('SetLaunchAbility successfully');
    }
  });
});

#### dispatchSessionEvent10+

dispatchSessionEvent(event: string, args: Record<string, Object>): Promise<void>

Dispatches a custom event in the session, including the event name and event content in key-value pair format. This API uses a promise to return the result. It is called by the provider.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Name of the session event. |
| args | Record<string, Object> | Yes | 
Content of the session event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is {\[key: string\]: Object}.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/_nzY8i6QSvSA6Pgd8rPZpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8E6FEBE8EEC8AEAADC186BEB0C67CE205B17382ECE973CE0610502E7B52FC10)

The **args** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
              } else {
                currentAVSession = data;
                let eventName = "dynamic\_lyric";
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}).then(() => {
                    console.info('dispatchSessionEvent successfully');
                  }).catch((err: BusinessError) => {
                    console.error(\`dispatchSessionEvent BusinessError: code: ${err.code}, message: ${err.message}\`);
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}

#### dispatchSessionEvent10+

dispatchSessionEvent(event: string, args: Record<string, Object>, callback: AsyncCallback<void>): void

Dispatches a custom event in the session, including the event name and event content in key-value pair format. This API uses an asynchronous callback to return the result. It is called by the provider.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Name of the session event. |
| args | Record<string, Object> | Yes | 
Content of the session event.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is {\[key: string\]: Object}.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ZIRVyWblSKKPfsrFVP2gxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A9EE099DA7AC2901FE6740F0666E67DD9DB09E5FE3FFB5F492713CF48D90404)

The **args** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
              } else {
                currentAVSession = data;
                let eventName: string = "dynamic\_lyric";
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}, (err: BusinessError) => {
                    if (err) {
                      console.error(\`dispatchSessionEvent BusinessError: code: ${err.code}, message: ${err.message}\`);
                    }
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}

#### setAVQueueItems10+

setAVQueueItems(items: Array<AVQueueItem>): Promise<void>

Sets a playlist. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\> | Yes | Playlist to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
interface ExtrasType {
  extras: string;
}

@Entry
@Component
struct Index {
  build() {
    Column() {
    }
  }
}

let currentAVSession: avSession.AVSession;

async function setAVQueueItems() {
  try {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE\_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({desiredSize:{width: 150, height: 150}});
    let queueItemDescription\_1: avSession.AVMediaDescription = {
      assetId: '001',
      title: 'music\_name',
      subtitle: 'music\_sub\_name',
      description: 'music\_description',
      mediaImage : imagePixel,
      extras: {extras:'any'}
    };
    let queueItem\_1: avSession.AVQueueItem = {
      itemId: 1,
      description: queueItemDescription\_1
    } as avSession.AVQueueItem;
    let queueItemDescription\_2: avSession.AVMediaDescription = {
      assetId: '002',
      title: 'music\_name',
      subtitle: 'music\_sub\_name',
      description: 'music\_description',
      mediaImage: imagePixel,
      extras: {extras:'any'}
    };
    let queueItem\_2: avSession.AVQueueItem = {
      itemId: 2,
      description: queueItemDescription\_2
    } as avSession.AVQueueItem;
    let queueItemsArray: avSession.AVQueueItem\[\] = \[queueItem\_1, queueItem\_2\];
    currentAVSession.setAVQueueItems(queueItemsArray).then(() => {
      console.info('SetAVQueueItems successfully');
    }).catch((err: BusinessError) => {
      console.error(\`SetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}\`);
    });
  } catch (err) {
    if (err) {
      console.error(\`ImageSource or PixelMap create Error: code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### setAVQueueItems10+

setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void

Sets a playlist. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | Array<[AVQueueItem](../interfaces-others/document.md#avqueueitem10)\> | Yes | Playlist to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit'

interface ExtrasType {
  extras: string;
}

@Entry
@Component
struct Index {
  build() {
    Column() {
    }
  }
}

let currentAVSession: avSession.AVSession;

async function setAVQueueItems() {
  try {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE\_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
    let queueItemDescription\_1: avSession.AVMediaDescription = {
      assetId: '001',
      title: 'music\_name',
      subtitle: 'music\_sub\_name',
      description: 'music\_description',
      mediaImage: imagePixel,
      extras: { extras: 'any' }
    };
    let queueItem\_1: avSession.AVQueueItem = {
      itemId: 1,
      description: queueItemDescription\_1
    };
    let queueItemDescription\_2: avSession.AVMediaDescription = {
      assetId: '002',
      title: 'music\_name',
      subtitle: 'music\_sub\_name',
      description: 'music\_description',
      mediaImage: imagePixel,
      extras: { extras: 'any' }
    };
    let queueItem\_2: avSession.AVQueueItem = {
      itemId: 2,
      description: queueItemDescription\_2
    };
    let queueItemsArray: avSession.AVQueueItem\[\] = \[queueItem\_1, queueItem\_2\];
    currentAVSession.setAVQueueItems(queueItemsArray, (err: BusinessError) => {
      if (err) {
        console.error(\`SetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}\`);
      } else {
        console.info('SetAVQueueItems successfully');
      }
    });
  } catch (err) {
    if (err) {
      console.error(\`ImageSource or PixelMap create Error: code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### setAVQueueTitle10+

setAVQueueTitle(title: string): Promise<void>

Sets a name for the playlist. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| title | string | Yes | Name of the playlist. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let queueTitle = 'QUEUE\_TITLE';
currentAVSession.setAVQueueTitle(queueTitle).then(() => {
  console.info('SetAVQueueTitle successfully');
}).catch((err: BusinessError) => {
  console.error(\`SetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### setAVQueueTitle10+

setAVQueueTitle(title: string, callback: AsyncCallback<void>): void

Sets a name for the playlist. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| title | string | Yes | Name of the playlist. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let queueTitle = 'QUEUE\_TITLE';
currentAVSession.setAVQueueTitle(queueTitle, (err: BusinessError) => {
  if (err) {
    console.error(\`SetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('SetAVQueueTitle successfully');
  }
});

#### setExtras10+

setExtras(extras: Record<string, Object>): Promise<void>

Sets a custom media packet in the form of key-value pairs. This API uses a promise to return the result. It is called by the provider.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| extras | Record<string, Object> | Yes | 
Key-value pairs of the custom media packet.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is {\[key: string\]: Object}.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ociOW2ZVSBSespCN4LNTRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8A688BD8B6FB4ED172577CE55C92FFD06356650B2363A94E80F763A94AE77A6)

The **extras** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the setting is successful, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(() => {
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
              } else {
                currentAVSession = data;
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}).then(() => {
                      console.info('setExtras successfully');
                  }).catch((err: BusinessError) => {
                      console.error(\`setExtras BusinessError: code: ${err.code}, message: ${err.message}\`);
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}

#### setExtras10+

setExtras(extras: {\[key: string\]: Object}, callback: AsyncCallback<void>): void

Sets a custom media packet in the form of key-value pairs. This API uses an asynchronous callback to return the result. It is called by the provider.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| extras | {\[key: string\]: Object} | Yes | Key-value pairs of the custom media packet. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**; otherwise, **err** is an error object. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/IsTVtGonSbu5nNjm1IkNAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B0C2B890FA72A52F951AF7FF687266703061766F776671C589BE82C91DD32B6)

The **extras** parameter supports the following data types: string, number, Boolean, object, array, and file descriptor. For details, see [@ohos.app.ability.Want(Want)](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
              } else {
                currentAVSession = data;
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}, (err: BusinessError) => {
                    if (err) {
                      console.error(\`setExtras BusinessError: code: ${err.code}, message: ${err.message}\`);
                    }
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
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

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
            if (err) {
                console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
            } else {
                currentAVSession = data;
            }
            });
            if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).sendCustomData({customData : "This is custom data"}).then(() => {
                console.info('sendCustomData successfully');
            }).catch((err: BusinessError) => {
                console.error(\`sendCustomData BusinessError: code: ${err.code}, message: ${err.message}\`);
            })
            }
          })
      }
    .width('100%')
    .height('100%')
  }
}

#### getController10+

getController(): Promise<AVSessionController>

Obtains the controller corresponding to this session. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVSessionController](../interface-avsessioncontroller/document.md)\> | Promise used to return the session controller. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  build() {
    Column() {
      Text(this.message)
        .onClick(async ()=>{
          try {
            let context: Context = this.getUIContext().getHostContext() as Context;
            let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION\_NAME', 'audio');
            let avSessionController: avSession.AVSessionController;
            currentAVSession.getController().then((avController: avSession.AVSessionController) => {
              avSessionController = avController;
              console.info(\`GetController : SUCCESS : sessionid : ${avSessionController.sessionId}\`);
            }).catch((err: BusinessError) => {
              console.error(\`GetController BusinessError: code: ${err.code}, message: ${err.message}\`);
            });
          } catch (err) {
            if (err) {
              console.error(\`AVSession create Error: ${JSON.stringify(err)}\`);
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### getController10+

getController(callback: AsyncCallback<AVSessionController>): void

Obtains the controller corresponding to this session. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVSessionController](../interface-avsessioncontroller/document.md)\> | Yes | Callback used to return the session controller. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { avSession } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(async () => {
          try {
            let context: Context = this.getUIContext().getHostContext() as Context;
            let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION\_NAME', 'audio');
            let avsessionController: avSession.AVSessionController;
            currentAVSession.getController((err: BusinessError, avcontroller: avSession.AVSessionController) => {
              if (err) {
                console.error(\`GetController BusinessError: code: ${err.code}, message: ${err.message}\`);
              } else {
                avsessionController = avcontroller;
                console.info(\`GetController : SUCCESS : sessionid : ${avsessionController.sessionId}\`);
              }
            });
          } catch (err) {
            if (err) {
              console.error(\`AVSession create Error: code: ${err.code}, message: ${err.message}\`);
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### getAVCastController10+

getAVCastController(): Promise<AVCastController>

Obtains the cast controller when a casting connection is set up. This API uses a promise to return the result. If the session is not in the cast state, the controller returns **null**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVCastController](../interface-avcastcontroller/document.md)\> | Promise used to return the cast controller. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let aVCastController: avSession.AVCastController;
currentAVSession.getAVCastController().then((avcontroller: avSession.AVCastController) => {
  aVCastController = avcontroller;
  console.info('getAVCastController : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`getAVCastController BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### getAVCastController10+

getAVCastController(callback: AsyncCallback<AVCastController>): void

Obtains the cast controller when a casting connection is set up. This API uses an asynchronous callback to return the result. If the session is not in the cast state, the controller returns **null**.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVCastController](../interface-avcastcontroller/document.md)\> | Yes | Callback used to return the cast controller. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let aVCastController: avSession.AVCastController;
currentAVSession.getAVCastController((err: BusinessError, avcontroller: avSession.AVCastController) => {
  if (err) {
    console.error(\`getAVCastController BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    aVCastController = avcontroller;
    console.info('getAVCastController : SUCCESS');
  }
});

#### getOutputDevice10+

getOutputDevice(): Promise<OutputDeviceInfo>

Obtains information about the output device for this session. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)\> | Promise used to return the output device information. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
  console.info(\`GetOutputDevice : SUCCESS : devices length : ${outputDeviceInfo.devices.length}\`);
}).catch((err: BusinessError) => {
  console.error(\`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}\`);
})

#### getOutputDevice10+

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

Obtains information about the output device for this session. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)\> | Yes | Callback used to return the information obtained. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.getOutputDevice((err: BusinessError, outputDeviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(\`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`GetOutputDevice : SUCCESS : devices length : ${outputDeviceInfo.devices.length}\`);
  }
});

#### activate10+

activate(): Promise<void>

Activates this session. A session can be used only after being activated. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the session is activated, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.activate().then(() => {
  console.info('Activate : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(\`Activate BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### activate10+

activate(callback: AsyncCallback<void>): void

Activates this session. A session can be used only after being activated. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session is activated, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.activate((err: BusinessError) => {
  if (err) {
    console.error(\`Activate BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Activate : SUCCESS ');
  }
});

#### deactivate10+

deactivate(): Promise<void>

Deactivates this session. You can use [activate](#activate10) to activate the session again. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the session is deactivated, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.deactivate().then(() => {
  console.info('Deactivate : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(\`Deactivate BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### deactivate10+

deactivate(callback: AsyncCallback<void>): void

Deactivates this session. This API uses an asynchronous callback to return the result.

Deactivates this session. You can use [activate](#activate10) to activate the session again.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session is deactivated, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.deactivate((err: BusinessError) => {
  if (err) {
    console.error(\`Deactivate BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Deactivate : SUCCESS ');
  }
});

#### destroy10+

destroy(): Promise<void>

Destroys this session. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the session is destroyed, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.destroy().then(() => {
  console.info('Destroy : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(\`Destroy BusinessError: code: ${err.code}, message: ${err.message}\`);
});

#### destroy10+

destroy(callback: AsyncCallback<void>): void

Destroys this session. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session is destroyed, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.destroy((err: BusinessError) => {
  if (err) {
    console.error(\`Destroy BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Destroy : SUCCESS ');
  }
});

#### on('play')10+

on(type: 'play', callback: () => void): void

Subscribes to play command events. The subscription means that the application supports the play command.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'play'** is triggered when the command for starting playback is sent to the session. |
| callback | () => void | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('play', () => {
  console.info('on play entry');
});

#### onPlay22+

onPlay(callback: Callback<CommandInfo>): void

Subscribes to play command events. This API uses an asynchronous callback to return the result.

The application receives [CommandInfo](../interfaces-others/document.md#commandinfo22) sent by the controller through the callback.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[CommandInfo](../interfaces-others/document.md#commandinfo22)\> | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.onPlay((info: CommandInfo) => {
  console.info('on play entry');
});

#### on('pause')10+

on(type: 'pause', callback: () => void): void

Subscribes to pause command events. The subscription means that the application supports the pause command.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'pause'** is triggered when the command for pausing the playback is sent to the session. |
| callback | () => void | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('pause', () => {
  console.info('on pause entry');
});

#### on('stop')10+

on(type:'stop', callback: () => void): void

Subscribes to stop command events. The subscription means that the application supports the stop command.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'stop'** is triggered when the command for stopping the playback is sent to the session. |
| callback | () => void | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('stop', () => {
  console.info('on stop entry');
});

#### on('playNext')10+

on(type:'playNext', callback: () => void): void

Subscribes to playNext command events. The subscription means that the application supports the playNext command.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'playNext'** is triggered when the command for playing the next item is sent to the session. |
| callback | () => void | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('playNext', () => {
  console.info('on playNext entry');
});

#### onPlayNext22+

onPlayNext(callback: Callback<CommandInfo>): void

Subscribes to playNext command events. This API uses an asynchronous callback to return the result.

The application receives [CommandInfo](../interfaces-others/document.md#commandinfo22) sent by the controller through the callback.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[CommandInfo](../interfaces-others/document.md#commandinfo22)\> | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.onPlayNext((info: CommandInfo) => {
  console.info('on playNext entry');
});

#### on('playPrevious')10+

on(type:'playPrevious', callback: () => void): void

Subscribes to playPrevious command events. The subscription means that the application supports the playPrevious command.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'playPrevious'** is triggered when the command for playing the previous item sent to the session. |
| callback | () => void | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('playPrevious', () => {
  console.info('on playPrevious entry');
});

#### onPlayPrevious22+

onPlayPrevious(callback: Callback<CommandInfo>): void

Subscribes to playPrevious command events. This API uses an asynchronous callback to return the result.

The application receives [CommandInfo](../interfaces-others/document.md#commandinfo22) sent by the controller through the callback.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[CommandInfo](../interfaces-others/document.md#commandinfo22)\> | Yes | Callback used for subscription. If the subscription is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.onPlayPrevious((info: CommandInfo) => {
  console.info('on playPrevious entry');
});

#### on('fastForward')10+

on(type: 'fastForward', callback: (time?: number) => void): void

Subscribes to fastForward command events. The subscription means that the application supports the fastForward command.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'fastForward'** is triggered when the command for fast forwarding is sent to the session. |
| callback | (time?: number) => void | Yes | Callback used for subscription. The **time** parameter in the callback indicates the time to seek to, in seconds. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('fastForward', (time?: number) => {
  console.info('on fastForward entry');
});

#### onFastForward22+

onFastForward(callback: TwoParamCallback<number, CommandInfo>): void

Subscribes to fastForward command events. This API uses an asynchronous callback to return the result.

The application receives the fast-forward time parameter and [CommandInfo](../interfaces-others/document.md#commandinfo22) sent by the controller through the callback.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | TwoParamCallback<number, [CommandInfo](../interfaces-others/document.md#commandinfo22)\> | Yes | Callback used to return the result. It is used to process the fastForward operation. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.onFastForward((time: number, info: CommandInfo) => {
  console.info('on fastForward entry');
});

#### on('rewind')10+

on(type:'rewind', callback: (time?: number) => void): void

Subscribes to rewind command events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'rewind'** is triggered when the command for rewinding is sent to the session. |
| callback | (time?: number) => void | Yes | Callback used for subscription. The **time** parameter in the callback indicates the time to seek to, in seconds. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('rewind', (time?: number) => {
  console.info('on rewind entry');
});

#### onRewind22+

onRewind(callback: TwoParamCallback<number, CommandInfo>): void

Subscribes to rewind command events. This API uses an asynchronous callback to return the result.

The application receives the rewind time parameter and [CommandInfo](../interfaces-others/document.md#commandinfo22) sent by the controller through the callback.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | TwoParamCallback<number, [CommandInfo](../interfaces-others/document.md#commandinfo22)\> | Yes | Callback used to return the result. It is used to process the rewind operation. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.onRewind((time: number, info: CommandInfo) => {
  console.info('on rewind entry');
});

#### on('playWithAssetId')20+

on(type:'playWithAssetId', callback: Callback<string>): void

Subscribes to playback events with a given media asset ID.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'playWithAssetId'** is triggered when the media asset ID is played. |
| callback | Callback<string> | Yes | Callback The **assetId** parameter in the callback indicates the media asset ID. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

let playWithAssetIdCallback = (assetId: string) => {
  console.info(\`on playWithAssetId entry,  assetId = ${assetId}\`);
}
currentAVSession.on('playWithAssetId', playWithAssetIdCallback);

#### off('playWithAssetId')20+

off(type: 'playWithAssetId', callback?: Callback<string>): void

Unsubscribes from playback events with a given media asset ID. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'playWithAssetId'** in this case. |
| callback | Callback<string> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session. The **assetId** parameter in the callback indicates the media asset ID.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('playWithAssetId');

#### on('seek')10+

on(type: 'seek', callback: (time: number) => void): void

Subscribes to seek command events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'seek'** is triggered when the seek command is sent to the session. |
| callback | (time: number) => void | Yes | Callback used for subscription. The **time** parameter in the callback indicates the time to seek to, in milliseconds. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('seek', (time: number) => {
  console.info(\`on seek entry time : ${time}\`);
});

#### on('setSpeed')10+

on(type: 'setSpeed', callback: (speed: number) => void): void

Subscribes to setSpeed command events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'setSpeed'** is triggered when the command for setting the playback speed is sent to the session. |
| callback | (speed: number) => void | Yes | Callback used for subscription. The **speed** parameter in the callback indicates the playback speed. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('setSpeed', (speed: number) => {
  console.info(\`on setSpeed speed : ${speed}\`);
});

#### on('setLoopMode')10+

on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void

Subscribes to setLoopMode command events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'setLoopMode'** is triggered when the command for setting the loop mode is sent to the session. |
| callback | (mode: [LoopMode](../enums/document.md#loopmode10)) => void | Yes | Callback used for subscription. The **mode** parameter in the callback indicates the loop mode. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('setLoopMode', (mode: avSession.LoopMode) => {
  console.info(\`on setLoopMode mode : ${mode}\`);
});

#### on('setTargetLoopMode')18+

on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void

Subscribes to setTargetLoopMode command events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The event **'setTargetLoopMode'**

is triggered when the command for setting the target loop mode is sent to the session.

 |
| callback | Callback<[LoopMode](../enums/document.md#loopmode10)\> | Yes | Callback used for subscription. The **LoopMode** parameter in the callback indicates the target loop mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [AVSession Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('setTargetLoopMode', (mode: avSession.LoopMode) => {
  console.info(\`on setTargetLoopMode mode : ${mode}\`);
});

#### on('toggleFavorite')10+

on(type: 'toggleFavorite', callback: (assetId: string) => void): void

Subscribes to toggleFavorite command events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'toggleFavorite'** is triggered when the command for favoriting the media asset is sent to the session. |
| callback | (assetId: string) => void | Yes | Callback used for subscription. The **assetId** parameter in the callback indicates the media asset ID. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('toggleFavorite', (assetId: string) => {
  console.info(\`on toggleFavorite mode : ${assetId}\`);
});

#### on('skipToQueueItem')10+

on(type: 'skipToQueueItem', callback: (itemId: number) => void): void

Subscribes to the event that indicates an item in the playlist is selected. The session can play the selected item.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'skipToQueueItem'** is triggered when an item in the playlist is selected. |
| callback | (itemId: number) => void | Yes | Callback used for subscription. The **itemId** parameter in the callback indicates the ID of the selected item. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('skipToQueueItem', (itemId: number) => {
  console.info(\`on skipToQueueItem id : ${itemId}\`);
});

#### on('handleKeyEvent')10+

on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void

Subscribes to key events of external devices such as Bluetooth and wired devices to listen for the play, pause, previous, next, fast-forward, and rewind commands in the key events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'handleKeyEvent'** is triggered when a key event is sent to the session. |
| callback | (event: [KeyEvent](../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md)) => void | Yes | Callback used for subscription. The **event** parameter in the callback indicates the key event. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { KeyEvent } from '@kit.InputKit';

currentAVSession.on('handleKeyEvent', (event: KeyEvent) => {
  console.info(\`on handleKeyEvent event : ${event}\`);
});

#### on('outputDeviceChange')10+

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

Subscribes to output device change events. After the application integrates the [AVCastPicker component](../../../arkts-components/ohos-multimedia-avcastpicker-avcastpicker/document.md), the application receives the device change callback when the user switches the device through the component.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'outputDeviceChange'** is triggered when the output device changes. |
| callback | (state: [ConnectionState](../enums/document.md#connectionstate10), device: [OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)) => void | Yes | 
Callback function, where the **device** parameter specifies the output device information.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(\`on outputDeviceChange device : ${device}\`);
});

#### on('commonCommand')10+

on(type: 'commonCommand', callback: (command: string, args: Record<string, Object>) => void): void

Subscribes to custom control command change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'commonCommand'** is triggered when a custom control command changes. |
| callback | (command: string, args: Record<string, Object>) => void | Yes | 
Callback used for subscription. The **command** parameter in the callback indicates the name of the changed custom control command, and **args** indicates the parameters carried in the command. The parameters must be the same as those set in [sendCommonCommand](../interface-avsessioncontroller/document.md#sendcommoncommand10).

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is (command :string, args:{\[key: string\]: Object}) => void.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
              } else {
                currentAVSession = data;
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).on('commonCommand', (commonCommand, args) => {
                      console.info(\`OnCommonCommand, the command is ${commonCommand}, args: ${JSON.stringify(args)}\`);
                  });
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}

#### off('play')10+

off(type: 'play', callback?: () => void): void

Unsubscribes from play command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'play'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('play');

#### offPlay22+

offPlay(callback?: Callback<CommandInfo>): void

Unsubscribes from play command events. This API uses an asynchronous callback to return the result.

If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[CommandInfo](../interfaces-others/document.md#commandinfo22)\> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.offPlay();

#### off('pause')10+

off(type: 'pause', callback?: () => void): void

Unsubscribes from pause command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'pause'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('pause');

#### off('stop')10+

off(type: 'stop', callback?: () => void): void

Unsubscribes from stop command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'stop'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('stop');

#### off('playNext')10+

off(type: 'playNext', callback?: () => void): void

Unsubscribes from playNext command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'playNext'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('playNext');

#### offPlayNext22+

offPlayNext(callback?: Callback<CommandInfo>): void

Unsubscribes from playNext command events. This API uses an asynchronous callback to return the result.

If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[CommandInfo](../interfaces-others/document.md#commandinfo22)\> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.offPlayNext();

#### off('playPrevious')10+

off(type: 'playPrevious', callback?: () => void): void

Unsubscribes from playPrevious command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'playPrevious'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('playPrevious');

#### offPlayPrevious22+

offPlayPrevious(callback?: Callback<CommandInfo>): void

Unsubscribes from playPrevious command events. This API uses an asynchronous callback to return the result.

If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[CommandInfo](../interfaces-others/document.md#commandinfo22)\> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.offPlayPrevious();

#### off('fastForward')10+

off(type: 'fastForward', callback?: () => void): void

Unsubscribes from fastForward command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'fastForward'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('fastForward');

#### offFastForward22+

offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void

Unsubscribes from fastForward command events. This API uses an asynchronous callback to return the result.

If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | TwoParamCallback<number, [CommandInfo](../interfaces-others/document.md#commandinfo22)\> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.offFastForward();

#### off('rewind')10+

off(type: 'rewind', callback?: () => void): void

Unsubscribes from rewind command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'rewind'** in this case. |
| callback | () => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('rewind');

#### offRewind22+

offRewind(callback?: TwoParamCallback<number, CommandInfo>): void

Unsubscribes from rewind command events. This API uses an asynchronous callback to return the result.

If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | TwoParamCallback<number, [CommandInfo](../interfaces-others/document.md#commandinfo22)\> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.offRewind();

#### off('seek')10+

off(type: 'seek', callback?: (time: number) => void): void

Unsubscribes from seek command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'seek'** in this case. |
| callback | (time: number) => void | No | 
Callback used for unsubscription. The **time** parameter in the callback indicates the time to seek to, in milliseconds.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('seek');

#### off('setSpeed')10+

off(type: 'setSpeed', callback?: (speed: number) => void): void

Unsubscribes from setSpeed command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setSpeed'** in this case. |
| callback | (speed: number) => void | No | 
Callback used for unsubscription. The **speed** parameter in the callback indicates the playback speed.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('setSpeed');

#### off('setLoopMode')10+

off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void

Unsubscribes from setLoopMode command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setLoopMode'** in this case. |
| callback | (mode: [LoopMode](../enums/document.md#loopmode10)) => void | No | 
Callback used for unsubscription. The **mode** parameter in the callback indicates the loop mode.

\- If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

\- The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('setLoopMode');

#### off('setTargetLoopMode')18+

off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void

Unsubscribes from setTargetLoopMode command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setTargetLoopMode'** in this case. |
| callback | Callback<[LoopMode](../enums/document.md#loopmode10)\> | No | 
Callback used for unsubscription. The **LoopMode** parameter in the callback indicates the target loop mode.

\- If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

\- The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [AVSession Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('setTargetLoopMode');

#### off('toggleFavorite')10+

off(type: 'toggleFavorite', callback?: (assetId: string) => void): void

Unsubscribes from toggleFavorite command events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'toggleFavorite'** in this case. |
| callback | (assetId: string) => void | No | 
Callback used for unsubscription. The **assetId** parameter in the callback indicates the media asset ID.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('toggleFavorite');

#### off('skipToQueueItem')10+

off(type: 'skipToQueueItem', callback?: (itemId: number) => void): void

Unsubscribes from the event that indicates an item in the playlist is selected. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'skipToQueueItem'** in this case. |
| callback | (itemId: number) => void | No | 
Callback used for unsubscription. The **itemId** parameter in the callback indicates the ID of the item.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('skipToQueueItem');

#### off('handleKeyEvent')10+

off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void

Unsubscribes from key events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'handleKeyEvent'** in this case. |
| callback | (event: [KeyEvent](../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md)) => void | No | 
Callback used for unsubscription. The **event** parameter in the callback indicates the key event.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('handleKeyEvent');

#### off('outputDeviceChange')10+

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

Unsubscribes from playback device change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'outputDeviceChange'** in this case. |
| callback | (state: [ConnectionState](../enums/document.md#connectionstate10), device: [OutputDeviceInfo](../interfaces-others/document.md#outputdeviceinfo10)) => void | No | 
Callback function, where the **device** parameter specifies the output device information.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('outputDeviceChange');

#### off('commonCommand')10+

off(type: 'commonCommand', callback?: (command: string, args: Record<string, Object>) => void): void

Unsubscribes from custom control command change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'commonCommand'** in this case. |
| callback | (command: string, args: Record<string, Object>) => void | No | 
Callback used for unsubscription. The **command** parameter in the callback indicates the name of the changed custom control command, and **args** indicates the parameters carried in the command.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

Starting from API version 20, a compatibility change occurred. In API version 19 and earlier, the parameter type is (command: string, args:{\[key: string\]: Object}) => void.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('commonCommand');

#### on('answer')11+

on(type: 'answer', callback: Callback<void>): void

Subscribes to call answer events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'answer'** is triggered when a call is answered. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('answer', () => {
  console.info('on call answer');
});

#### off('answer')11+

off(type: 'answer', callback?: Callback<void>): void

Unsubscribes from call answer events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'answer'** in this case. |
| callback | Callback<void> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('answer');

#### on('hangUp')11+

on(type: 'hangUp', callback: Callback<void>): void

Subscribes to call hangup events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'hangUp'** is triggered when a call is hung up. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('hangUp', () => {
  console.info('on call hangUp');
});

#### off('hangUp')11+

off(type: 'hangUp', callback?: Callback<void>): void

Unsubscribes from call answer events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'hangUp'** in this case. |
| callback | Callback<void> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('hangUp');

#### on('toggleCallMute')11+

on(type: 'toggleCallMute', callback: Callback<void>): void

Subscribes to call mute events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'toggleCallMute'** is triggered when a call is muted or unmuted. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('toggleCallMute', () => {
  console.info('on call toggleCallMute');
});

#### off('toggleCallMute')11+

off(type: 'toggleCallMute', callback?: Callback<void>): void

Unsubscribes from call mute events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'toggleCallMute'** in this case. |
| callback | Callback<void> | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('toggleCallMute');

#### on('castDisplayChange')12+

on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void

Subscribes to cast display change events in the case of extended screens.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'castDisplayChange'** is triggered when the cast display in the case of extended screens changes. |
| callback | Callback<[CastDisplayInfo](../interfaces-others/document.md#castdisplayinfo12)\> | Yes | Callback used to return the information about the cast display. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

let castDisplay: avSession.CastDisplayInfo;
currentAVSession.on('castDisplayChange', (display: avSession.CastDisplayInfo) => {
    if (display.state === avSession.CastDisplayState.STATE\_ON) {
        castDisplay = display;
        console.info(\`Succeeded in castDisplayChange display : ${display.id} ON\`);
    } else if (display.state === avSession.CastDisplayState.STATE\_OFF){
        console.info(\`Succeeded in castDisplayChange display : ${display.id} OFF\`);
    }
});

#### off('castDisplayChange')12+

off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void

Unsubscribes from cast display change events in the case of extended screens. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'castDisplayChange'** in this case. |
| callback | Callback<[CastDisplayInfo](../interfaces-others/document.md#castdisplayinfo12)\> | No | Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object. The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('castDisplayChange');

#### stopCasting10+

stopCasting(callback: AsyncCallback<void>): void

Stops castings. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the command is sent, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600109 | The remote connection is not established. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.stopCasting((err: BusinessError) => {
  if (err) {
    console.error(\`stopCasting BusinessError: code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('stopCasting successfully');
  }
});

#### stopCasting10+

stopCasting(): Promise<void>

Stops castings. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If casting stops, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600109 | The remote connection is not established. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.stopCasting().then(() => {
  console.info('stopCasting successfully');
}).catch((err: BusinessError) => {
  console.error(\`stopCasting BusinessError: code: ${err.code}, message: ${err.message}\`);
});

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
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentOutputDevice: avSession.OutputDeviceInfo = currentAVSession.getOutputDeviceSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getOutputDeviceSync error, error code: ${error.code}, error message: ${error.message}\`);
}

#### getAllCastDisplays12+

getAllCastDisplays(): Promise<Array<CastDisplayInfo>>

Obtains all displays that support extended screen projection in the current system. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[CastDisplayInfo](../interfaces-others/document.md#castdisplayinfo12)\>> | Promise used to return the information about all the cast displays. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let castDisplay: avSession.CastDisplayInfo;
currentAVSession.getAllCastDisplays().then((data: Array< avSession.CastDisplayInfo >) => {
    if (data.length >= 1) {
       castDisplay = data\[0\];
     }
   }).catch((err: BusinessError) => {
     console.error(\`Failed to getAllCastDisplay. Code: ${err.code}, message: ${err.message}\`);
   });

#### on('playFromAssetId')(deprecated)

on(type:'playFromAssetId', callback: (assetId: number) => void): void

Subscribes to playback events with a given media asset ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/SrNrdjJsRQ-2_79xUOgu2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A03870F01571584D94DE223EBFFABBE9B7F74E9E6E0561F2B68AAE56C19ECCD)

This API is supported since API version 11 and deprecated since API version 20. You are advised to use [on('playWithAssetId')](#onplaywithassetid20) instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'playFromAssetId'** is triggered when the media asset ID is played. |
| callback | (assetId: number) => void | Yes | Callback The **assetId** parameter in the callback indicates the media asset ID. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('playFromAssetId', (assetId: number) => {
  console.info('on playFromAssetId entry');
});

#### off('playFromAssetId')(deprecated)

off(type: 'playFromAssetId', callback?: (assetId: number) => void): void

Unsubscribes from playback events with a given media asset ID. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/4FWhxGchRsuehB9-cCnVfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41611F637A5A64C77144C82F9C3DC313304D4EFE428D8AF1CE1288DB2AD044EC)

This API is supported since API version 11 and deprecated since API version 20. You are advised to use [off('playWithAssetId')](#offplaywithassetid20) instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'playFromAssetId'** in this case. |
| callback | (assetId: number) => void | No | 
Callback used for unsubscription. If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session. The **assetId** parameter in the callback indicates the media asset ID.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('playFromAssetId');

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
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.on('customDataChange', (callback) => {
    console.info(\`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}\`);
});

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
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |

**Example**

currentAVSession.off('customDataChange');
