# Interface (AudioManager)

This interface implements audio volume and device management.

Before calling any API in AudioManager, you must use [getAudioManager](../functions/document.md#audiogetaudiomanager) to obtain an AudioManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/q0qAqHSJTSebEuAd5LI6ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6A97351BF8B0B847154AA29D1BF8A9FE6427CDC40C9807DAA91903DBB25C339)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### getAudioScene8+

getAudioScene(callback: AsyncCallback<AudioScene>): void

Obtains the audio scene. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioScene](../enums/document.md#audioscene8)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio scene obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioScene((err: BusinessError, value: audio.AudioScene) => {
  if (err) {
    console.error(\`Failed to obtain the audio scene mode. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the audio scene mode is obtained ${value}.\`);
});

#### getAudioScene8+

getAudioScene(): Promise<AudioScene>

Obtains the audio scene. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioScene](../enums/document.md#audioscene8)\> | Promise used to return the audio scene. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioScene().then((value: audio.AudioScene) => {
  console.info(\`Promise returned to indicate that the audio scene mode is obtained ${value}.\`);
}).catch ((err: BusinessError) => {
  console.error(\`Failed to obtain the audio scene mode ${err}\`);
});

#### getAudioSceneSync10+

getAudioSceneSync(): AudioScene

Obtains the audio scene. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioScene](../enums/document.md#audioscene8) | Audio scene. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioScene = audioManager.getAudioSceneSync();
  console.info(\`indicate that the audio scene mode is obtained ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtain the audio scene mode ${error}\`);
}

#### on('audioSceneChange')20+

on(type: 'audioSceneChange', callback: Callback<AudioScene>): void

Subscribes to the audio scene change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioSceneChange'** is triggered when the audio scene is changed. |
| callback | Callback<[AudioScene](../enums/document.md#audioscene8)\> | Yes | Callback used to return the current audio scene. |

**Example**

audioManager.on('audioSceneChange', (audioScene: audio.AudioScene) => {
  console.info(\`audio scene : ${audioScene}.\`);
});

#### off('audioSceneChange')20+

off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void

Unsubscribes from the audio scene change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioSceneChange'** is triggered when the audio scene is changed. |
| callback | Callback<[AudioScene](../enums/document.md#audioscene8)\> | No | Callback used to return the current audio scene. |

**Example**

// Cancel all subscriptions to the event.
audioManager.off('audioSceneChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let audioSceneChangeCallback = (audioScene: audio.AudioScene) => {
  console.info(\`audio scene : ${audioScene}.\`);
};

audioManager.on('audioSceneChange', audioSceneChangeCallback);

audioManager.off('audioSceneChange', audioSceneChangeCallback);

#### getVolumeManager9+

getVolumeManager(): AudioVolumeManager

Obtains an AudioVolumeManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioVolumeManager](../interface-audiovolumemanager/document.md) | AudioVolumeManager instance. |

**Example**

import { audio } from '@kit.AudioKit';

let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();

#### getStreamManager9+

getStreamManager(): AudioStreamManager

Obtains an AudioStreamManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioStreamManager](../interface-audiostreammanager/document.md) | AudioStreamManager instance. |

**Example**

import { audio } from '@kit.AudioKit';

let audioStreamManager: audio.AudioStreamManager = audioManager.getStreamManager();

#### getRoutingManager9+

getRoutingManager(): AudioRoutingManager

Obtains an AudioRoutingManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioRoutingManager](../interface-audioroutingmanager/document.md) | AudioRoutingManager instance. |

**Example**

import { audio } from '@kit.AudioKit';

let audioRoutingManager: audio.AudioRoutingManager = audioManager.getRoutingManager();

#### getSessionManager12+

getSessionManager(): AudioSessionManager

Obtains an AudioSessionManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioSessionManager](../interface-audiosessionmanager/document.md) | AudioSessionManager instance. |

**Example**

import { audio } from '@kit.AudioKit';

let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();

#### getSpatializationManager18+

getSpatializationManager(): AudioSpatializationManager

Obtains an AudioSpatializationManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Spatialization

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioSpatializationManager](../interface-audiospatializationmanager/document.md) | AudioSpatializationManager instance. |

**Example**

import { audio } from '@kit.AudioKit';
let audioSpatializationManager: audio.AudioSpatializationManager = audioManager.getSpatializationManager();

#### setAudioParameter(deprecated)

setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void

Sets an audio parameter. This API uses an asynchronous callback to return the result.

This API is used to extend the audio configuration based on the hardware capability. The supported audio parameters vary according to the device and are not common parameters. Sample parameters are used in the sample code below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/f1gochEfR8qIGCmMApJHAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6C36720EE8C6E0F9BFFB4EBFA928FD283E70D76C6FE8C687F01A601A67D7DC6)

This API is supported since API version 7 and deprecated since API version 11. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.MODIFY\_AUDIO\_SETTINGS

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the audio parameter to set. |
| value | string | Yes | Value of the audio parameter to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setAudioParameter('key\_example', 'value\_example', (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set the audio parameter. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate a successful setting of the audio parameter.');
});

#### setAudioParameter(deprecated)

setAudioParameter(key: string, value: string): Promise<void>

Sets an audio parameter. This API uses a promise to return the result.

This API is used to extend the audio configuration based on the hardware capability. The supported audio parameters vary according to the device and are not common parameters. Sample parameters are used in the sample code below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/_SGDjcQqRnuJfy-d7vhQCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA464A6BC430760C8CDDB5DBF44333CACDBBEC32F14C33F9A9D4CA66807352BA)

This API is supported since API version 7 and deprecated since API version 11. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.MODIFY\_AUDIO\_SETTINGS

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the audio parameter to set. |
| value | string | Yes | Value of the audio parameter to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioManager.setAudioParameter('key\_example', 'value\_example').then(() => {
  console.info('Promise returned to indicate a successful setting of the audio parameter.');
});

#### getAudioParameter(deprecated)

getAudioParameter(key: string, callback: AsyncCallback<string>): void

Obtains the value of an audio parameter. This API uses an asynchronous callback to return the result.

This API is used to extend the audio configuration based on the hardware capability. The supported audio parameters vary according to the device and can be obtained from the device manual. The example below is for reference only.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/VhoqM5LKS7eoT59ID94VZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B4DFEB0814480BABBFC408C806E7FA9FF9B8F7E0360FC516652579BD916BB4F)

This API is supported since API version 7 and deprecated since API version 11. Its substitute is available only to system applications.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the audio parameter whose value is to be obtained. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio parameter value obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioParameter('key\_example', (err: BusinessError, value: string) => {
  if (err) {
    console.error(\`Failed to obtain the value of the audio parameter. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the value of the audio parameter is obtained ${value}.\`);
});

#### getAudioParameter(deprecated)

getAudioParameter(key: string): Promise<string>

Obtains the value of an audio parameter. This API uses a promise to return the result.

This API is used to extend the audio configuration based on the hardware capability. The supported audio parameters vary according to the device and can be obtained from the device manual. The example below is for reference only.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/0PnnNbBLQqSbANurSOH-hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5DB507FEC0CF07381E1CCEBA7FB28F5792BEAE6AB2958EF1E1EE24FEC3033A8)

This API is supported since API version 7 and deprecated since API version 11. Its substitute is available only to system applications.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the audio parameter whose value is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the value of the audio parameter. |

**Example**

audioManager.getAudioParameter('key\_example').then((value: string) => {
  console.info(\`Promise returned to indicate that the value of the audio parameter is obtained ${value}.\`);
});

#### setVolume(deprecated)

setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void

Sets the volume for a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/DCgyglfFTPSOpQxCDyamyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24EDC131EB55C80B6F7DB273BBC13826C57DBA3E9E5F9A39CACF3725BEB5D6EE)

-   This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.
    
-   Applications cannot directly adjust the system volume. They can use the system volume panel to control the volume. For details about the examples and descriptions, see [Volume Panel](../../../arkts-components/ohos-multimedia-avvolumepanel-volume-panel/document.md) in the API reference.
    

**Required permissions**: ohos.permission.ACCESS\_NOTIFICATION\_POLICY

This permission is required only for muting or unmuting the ringer when **volumeType** is set to **AudioVolumeType.RINGTONE**.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| volume | number | Yes | Volume to set. The value range can be obtained by calling [getMinVolume](#getminvolumedeprecated) and [getMaxVolume](#getmaxvolumedeprecated). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set the volume. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate a successful volume setting.');
});

#### setVolume(deprecated)

setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>

Sets the volume for a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Jr6EOd6rQ1KiMfEZleQTNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16ABA007311BBA4D91C7B0760CC65498D63041717478B5DFB332F16BDBCF4FCA)

-   This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.
    
-   Applications cannot directly adjust the system volume. They can use the system volume panel to control the volume. For details about the examples and descriptions, see [Volume Panel](../../../arkts-components/ohos-multimedia-avvolumepanel-volume-panel/document.md) in the API reference.
    

**Required permissions**: ohos.permission.ACCESS\_NOTIFICATION\_POLICY

This permission is required only for muting or unmuting the ringer when **volumeType** is set to **AudioVolumeType.RINGTONE**.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| volume | number | Yes | Volume to set. The value range can be obtained by calling [getMinVolume](#getminvolumedeprecated) and [getMaxVolume](#getmaxvolumedeprecated). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

Obtains the volume of a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/SUHCqJszQTGjiovx6vuggg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9949899B91A9BF1D3D6E80D917814DE83B94E2853C484CEA88C68268B772955)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [getVolume](../interface-audiovolumegroupmanager/document.md#getvolumedeprecated) instead. For API version 20 and later, you are advised to use [getVolumeByStream](../interface-audiovolumemanager/document.md#getvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream volume obtained; otherwise, **err** is an error object. The volume range of a specified stream can be obtained by calling [getMinVolume](#getminvolumedeprecated) and [getMaxVolume](#getmaxvolumedeprecated). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to obtain the volume. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the volume is obtained.');
});

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType): Promise<number>

Obtains the volume of a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kADUpBlbTeKg1HglVtMN_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86681AEF4AB305C1A1D8203726AF2DEE9D8E94C3AD326429EB866B2E50B3750C)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [getVolume](../interface-audiovolumegroupmanager/document.md#getvolumedeprecated) instead. For API version 20 and later, you are advised to use [getVolumeByStream](../interface-audiovolumemanager/document.md#getvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the volume of the stream. The volume range of a specified stream can be obtained by calling [getMinVolume](#getminvolumedeprecated) and [getMaxVolume](#getmaxvolumedeprecated). |

**Example**

audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(\`Promise returned to indicate that the volume is obtained ${value} .\`);
});

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

Obtains the minimum volume allowed for a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/fyndVf1LQseAmSRP8SxLUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0779158331E2996D4691395F6385FF10A545B9463661C80E6E02A5F7CED3E14)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [getMinVolume](../interface-audiovolumegroupmanager/document.md#getminvolumedeprecated) instead. For API version 20 and later, you are advised to use [getMinVolumeByStream](../interface-audiovolumemanager/document.md#getminvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum stream volume obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to obtain the minimum volume. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the minimum volume is obtained. ${value}\`);
});

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType): Promise<number>

Obtains the minimum volume allowed for a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/3LsJk8MvTzG2zRqVEU1LTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5391C6C385503CC19CAE5D6A832A42725F2E3417B4798B568F16FABCA1C2C570)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [getMinVolume](../interface-audiovolumegroupmanager/document.md#getminvolumedeprecated) instead. For API version 20 and later, you are advised to use [getMinVolumeByStream](../interface-audiovolumemanager/document.md#getminvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the minimum volume. |

**Example**

audioManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(\`Promised returned to indicate that the minimum volume is obtained. ${value}\`);
});

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

Obtains the maximum volume allowed for a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/9P6AcqnFSRiYubrRe7_1lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8847EDDD5FEE5E8E161FDFB8D7CA085AB6D680E4233F3587FC3D5D2791BBDCD)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [getMaxVolume](../interface-audiovolumegroupmanager/document.md#getmaxvolumedeprecated) instead. For API version 20 and later, you are advised to use [getMaxVolumeByStream](../interface-audiovolumemanager/document.md#getmaxvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum stream volume obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to obtain the maximum volume. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the maximum volume is obtained. ${value}\`);
});

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

Obtains the maximum volume allowed for a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/bgIGTTpWSZOosF0zgYq5fQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF18B9AA46C5526FD5B9FF2B47990EECEB4E515205098AC92B33B860BA8667DA)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [getMaxVolume](../interface-audiovolumegroupmanager/document.md#getmaxvolumedeprecated) instead. For API version 20 and later, you are advised to use [getMaxVolumeByStream](../interface-audiovolumemanager/document.md#getmaxvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum volume. |

**Example**

audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((data: number) => {
  console.info('Promised returned to indicate that the maximum volume is obtained.');
});

#### mute(deprecated)

mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void

Mutes or unmutes a stream. This API uses an asynchronous callback to return the result.

When the minimum volume of a stream cannot be set to 0, muting the stream is not supported. Example scenarios: alarms or phone calls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/YKD6OOe9T4y2hFvcRaEQAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18D6A3EE3149347932080D4183C3536EC35F10E8C3F79F41B9D3B777109CE81A)

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| mute | boolean | Yes | Whether to mute the stream. **true** to mute, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.mute(audio.AudioVolumeType.MEDIA, true, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to mute the stream. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the stream is muted.');
});

#### mute(deprecated)

mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>

Mutes or unmutes a stream. This API uses a promise to return the result.

When the minimum volume of a stream cannot be set to 0, muting the stream is not supported. Example scenarios: alarms or phone calls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/3S6WnD7NSb-zSw4h3aXGgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EF0CDB20A5CC6CD99BE6A3C6F7D3658DD581E913A80289D077B1F536CB57A30)

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| mute | boolean | Yes | Whether to mute the stream. **true** to mute, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioManager.mute(audio.AudioVolumeType.MEDIA, true).then(() => {
  console.info('Promise returned to indicate that the stream is muted.');
});

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

Checks whether a stream is muted. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/kqET5tp-Qdykq8BjdUqwbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E262C33C547E6B78229D9D276B254D163E86F345DD5FACE70C43B2C2D4CA8E0A)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [isMute](../interface-audiovolumegroupmanager/document.md#ismutedeprecated) instead. For API version 20 and later, you are advised to use [isSystemMutedForStream](../interface-audiovolumemanager/document.md#issystemmutedforstream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the stream is muted or **false** if not muted; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to obtain the mute status. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the mute status of the stream is obtained. ${value}\`);
});

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType): Promise<boolean>

Checks whether a stream is muted. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/yYYPP0aqTsOaPcmkP7CBHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB5EBD7676A6D6F1EAAB4318AFC39563441B1695797B7E48F2230CFED5656615)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [isMute](../interface-audiovolumegroupmanager/document.md#ismutedeprecated) instead. For API version 20 and later, you are advised to use [isSystemMutedForStream](../interface-audiovolumemanager/document.md#issystemmutedforstream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise. **true** if muted, **false** otherwise. |

**Example**

audioManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(\`Promise returned to indicate that the mute status of the stream is obtained ${value}.\`);
});

#### isActive(deprecated)

isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

Checks whether a stream is active. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/4ge3aBR-Q_eS-PcWWB91lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C30DB12571D0A2FFE00E57A5321C451508E0D0F3C96231801D3C9219419AECB8)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [isActive](../interface-audiostreammanager/document.md#isactivedeprecated) instead. For API version 20 and later, you are advised to use [isStreamActive](../interface-audiostreammanager/document.md#isstreamactive20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the stream is active or **false** if not active; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to obtain the active status of the stream. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the active status of the stream is obtained ${value}.\`);
});

#### isActive(deprecated)

isActive(volumeType: AudioVolumeType): Promise<boolean>

Checks whether a stream is active. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/VY3ovtSFRyGZL7CmfSG7EA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93A3D944EC740EC36D7062CB82AAC2F6F6B6DDBCA3D013A013135254CF24812F)

This API is supported since API version 7 and deprecated since API version 9. From API version 9 to 19, you are advised to use [isActive](../interface-audiostreammanager/document.md#isactivedeprecated) instead. For API version 20 and later, you are advised to use [isStreamActive](../interface-audiostreammanager/document.md#isstreamactive20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise indicating whether the stream is active. **true** if active, **false** otherwise. |

**Example**

audioManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(\`Promise returned to indicate that the active status of the stream is obtained ${value}.\`);
});

#### setRingerMode(deprecated)

setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void

Sets the ringer mode. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/gcqbDiyaRzaOiQh8TZP_dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29A813B67D2139C21DA14BC8D454EEEC27A23115C07F275F7301D190232E7A77)

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.ACCESS\_NOTIFICATION\_POLICY

This permission is required only for muting or unmuting the ringer.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AudioRingMode](../enums/document.md#audioringmode) | Yes | Ringer mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setRingerMode(audio.AudioRingMode.RINGER\_MODE\_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set the ringer mode. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate a successful setting of the ringer mode.');
});

#### setRingerMode(deprecated)

setRingerMode(mode: AudioRingMode): Promise<void>

Sets the ringer mode. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2lLIDY4pScuYMRqn8eWJEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=528333798FBAEB10EDFF66A59D1659C488AD6092999FA6475096800C4D57B28A)

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.ACCESS\_NOTIFICATION\_POLICY

This permission is required only for muting or unmuting the ringer.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AudioRingMode](../enums/document.md#audioringmode) | Yes | Ringer mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioManager.setRingerMode(audio.AudioRingMode.RINGER\_MODE\_NORMAL).then(() => {
  console.info('Promise returned to indicate a successful setting of the ringer mode.');
});

#### getRingerMode(deprecated)

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

Obtains the ringer mode. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/2Ti8oTX9R3OJEdCrfBOnjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED2DD6D8458B5C606607BD1424FA85B20DD00B442A3F851D29B07D943603818C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getRingerMode](../interface-audiovolumegroupmanager/document.md#getringermode9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRingMode](../enums/document.md#audioringmode)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the ringer mode obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(\`Failed to obtain the ringer mode. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the ringer mode is obtained ${value}.\`);
});

#### getRingerMode(deprecated)

getRingerMode(): Promise<AudioRingMode>

Obtains the ringer mode. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/f3bWCDttQUKWJQ-N2oh6Wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4CD817C8DD29AFF8366DF51CFFB5C38B381F285299AA083344F7B77B38487C9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getRingerMode](../interface-audiovolumegroupmanager/document.md#getringermode9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioRingMode](../enums/document.md#audioringmode)\> | Promise used to return the ringer mode. |

**Example**

audioManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(\`Promise returned to indicate that the ringer mode is obtained ${value}.\`);
});

#### getDevices(deprecated)

getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void

Obtains the audio devices with a specific flag. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qeDk5olmRg-3F507cC-B7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53EB97DA44B8BBB4612F26F8B7AEA032575C01871921D474E243EDCE942E4557)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getDevices](../interface-audioroutingmanager/document.md#getdevices9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceFlag | [DeviceFlag](../enums/document.md#deviceflag) | Yes | Audio device flag. |
| callback | AsyncCallback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio devices obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getDevices(audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG, (err: BusinessError, value: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(\`Failed to obtain the device list. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the device list is obtained.');
});

#### getDevices(deprecated)

getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>

Obtains the audio devices with a specific flag. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/CtzVpa6-TtWGHjwWS-aLNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8596A9BF571F532737DD9BF5001E68A04CD4DD1208D46F7FE638CC2EF441AB6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getDevices](../interface-audioroutingmanager/document.md#getdevices9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceFlag | [DeviceFlag](../enums/document.md#deviceflag) | Yes | Audio device flag. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Promise used to return the device list. |

**Example**

audioManager.getDevices(audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG).then((data: audio.AudioDeviceDescriptors) => {
  console.info('Promise returned to indicate that the device list is obtained.');
});

#### setDeviceActive(deprecated)

setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void

Sets a device to the active state. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/QID67JwpRPKQA-0tAXl_Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDF8BF574FC3DE139DA00A89E5D338C974BEF427D90D16E72A6B72FC630CD3DF)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setCommunicationDevice](../interface-audioroutingmanager/document.md#setcommunicationdevice9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [ActiveDeviceType](../enums/document.md#activedevicetypedeprecated) | Yes | Active audio device type. |
| active | boolean | Yes | Active state to set. **true** to set the device to the active state, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set the active status of the device. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the device is set to the active status.');
});

#### setDeviceActive(deprecated)

setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>

Sets a device to the active state. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/T_xQalt2RGuq1hPJy5dokw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B5B0EAC5AFB07D2FBDC1CEDB04F4D305B20B126FC8AC5CAFE1B02050A032312)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setCommunicationDevice](../interface-audioroutingmanager/document.md#setcommunicationdevice9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [ActiveDeviceType](../enums/document.md#activedevicetypedeprecated) | Yes | Active audio device type. |
| active | boolean | Yes | Active state to set. **true** to set the device to the active state, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true).then(() => {
  console.info('Promise returned to indicate that the device is set to the active status.');
});

#### isDeviceActive(deprecated)

isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void

Checks whether a device is active. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/MqPn3_63R8KAgVwUXgP46A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B9B658BAED9ED6DF63A7A86FFEBFB62E2D7C81FDE49C3D7DAE0D430B2046A76)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [isCommunicationDeviceActive](../interface-audioroutingmanager/document.md#iscommunicationdeviceactive9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [ActiveDeviceType](../enums/document.md#activedevicetypedeprecated) | Yes | Active audio device type. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the device is active or **false** if not active; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to obtain the active status of the device. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the active status of the device is obtained.');
});

#### isDeviceActive(deprecated)

isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>

Checks whether a device is active. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/X7mKPRaGRQ-_8cMv44leTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF124822A1CDEAD7E75A166326788B13F675B5AA0B151CEC23E3596AAA078334)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [isCommunicationDeviceActive](../interface-audioroutingmanager/document.md#iscommunicationdeviceactive9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [ActiveDeviceType](../enums/document.md#activedevicetypedeprecated) | Yes | Active audio device type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise indicating whether the device is active. **true** if active, **false** otherwise. |

**Example**

audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER).then((value: boolean) => {
  console.info(\`Promise returned to indicate that the active status of the device is obtained ${value}.\`);
});

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

Mutes or unmutes the microphone. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/jbUwQvGjS3e0YsTERl9hzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50EDD0D3BF6DA6A4C5EDD1CABD460DE002EFE732ADE3B4A28ADE868C9F814F64)

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.MICROPHONE

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mute | boolean | Yes | Mute status to set. **true** to mute, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to mute the microphone. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the microphone is muted.');
});

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean): Promise<void>

Mutes or unmutes the microphone. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/w080pQ9MQeq82GxVzer9KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B77740A4456B4B5977056E6DB6F13338F523C833786F82A3FAA6862016F1E664)

This API is supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.MICROPHONE

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mute | boolean | Yes | Mute status to set. **true** to mute, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioManager.setMicrophoneMute(true).then(() => {
  console.info('Promise returned to indicate that the microphone is muted.');
});

#### isMicrophoneMute(deprecated)

isMicrophoneMute(callback: AsyncCallback<boolean>): void

Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/5xvvguCkTaCN0JqSUVxEpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC6A9B2F5565840AB0B743B4514FA53FBABBBF5474AAACBFC08FB44F7C1FCD63)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [isMicrophoneMute](../interface-audiovolumegroupmanager/document.md#ismicrophonemute9) instead.

**Required permissions**: ohos.permission.MICROPHONE

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the microphone is muted or **false** if not muted; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to obtain the mute status of the microphone. ${err}\`);
    return;
  }
  console.info(\`Callback invoked to indicate that the mute status of the microphone is obtained ${value}.\`);
});

#### isMicrophoneMute(deprecated)

isMicrophoneMute(): Promise<boolean>

Checks whether the microphone is muted. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/irKwxfgLRhuQtZ6-EdkjLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C52BEC5993A5CF9979C65670F35B1F903F5A6BCC5100B1893A0AF3C34DD62B3D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [isMicrophoneMute](../interface-audiovolumegroupmanager/document.md#ismicrophonemute9) instead.

**Required permissions**: ohos.permission.MICROPHONE

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise indicating whether the microphone is muted. **true** if muted, **false** otherwise. |

**Example**

audioManager.isMicrophoneMute().then((value: boolean) => {
  console.info(\`Promise returned to indicate that the mute status of the microphone is obtained ${value}.\`);
});

#### on('deviceChange')(deprecated)

on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void

Subscribes to the event indicating that the connection status of an audio device is changed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/o2SaQ_SkSAW9K99un3K13Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BDD3C2F6635FFAE62B7B053E50066DA636497DC64B286022AE38D30C6379B25)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [on('deviceChange')](../interface-audioroutingmanager/document.md#ondevicechange9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'deviceChange'** is triggered when the connection status of an audio device is changed. |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | Yes | Callback used to return the device change details. |

**Example**

audioManager.on('deviceChange', (deviceChanged: audio.DeviceChangeAction) => {
  console.info(\`device change type : ${deviceChanged.type} \`);
  console.info(\`device descriptor size : ${deviceChanged.deviceDescriptors.length} \`);
  console.info(\`device change descriptor : ${deviceChanged.deviceDescriptors\[0\].deviceRole} \`);
  console.info(\`device change descriptor : ${deviceChanged.deviceDescriptors\[0\].deviceType} \`);
});

#### off('deviceChange')(deprecated)

off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void

Unsubscribes from the audio device change event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/fa0bNFAZREyVGh5sQXnehg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C54EE03B0EA39508C632CE087D0D3095FA75291ECF9372F4FF035072D97D51C3)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [off('deviceChange')](../interface-audioroutingmanager/document.md#offdevicechange9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'deviceChange'** is triggered when the connection status of an audio device is changed. |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | No | Callback used to return the device change details. |

**Example**

// Cancel all subscriptions to the event.
audioManager.off('deviceChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info(\`device change type : ${deviceChanged.type} \`);
  console.info(\`device descriptor size : ${deviceChanged.deviceDescriptors.length} \`);
  console.info(\`device change descriptor : ${deviceChanged.deviceDescriptors\[0\].deviceRole} \`);
  console.info(\`device change descriptor : ${deviceChanged.deviceDescriptors\[0\].deviceType} \`);
};

audioManager.on('deviceChange', deviceChangeCallback);

audioManager.off('deviceChange', deviceChangeCallback);

#### on('interrupt')(deprecated)

on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

Same as [on('audioInterrupt')](../interface-audiorenderer/document.md#onaudiointerrupt9), this API is used to listen for focus changes. However, this API is used in scenarios without audio streams (no AudioRenderer instance is created), such as frequency modulation (FM) and voice wakeup.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/62klRvNWQWG9fvMcBg17Pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DD1FD2B16C9ABB43EB6529BFB0B27DF63CDBE7295AE558DBE7BAEEE07EAAC6D)

This API is supported since API version 7 and deprecated since API version 11. You are advised to use [on('audioInterrupt')](../interface-audiocapturer/document.md#onaudiointerrupt10) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'interrupt'** is triggered when the audio focus is changed. |
| interrupt | [AudioInterrupt](../interfaces-others/document.md#audiointerruptdeprecated) | Yes | Audio interruption event type. |
| callback | Callback<[InterruptAction](../interfaces-others/document.md#interruptactiondeprecated)\> | Yes | Callback used to return the event information. |

**Example**

import { audio } from '@kit.AudioKit';

let interAudioInterrupt: audio.AudioInterrupt = {
  streamUsage: audio.StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION,
  contentType: audio.ContentType.CONTENT\_TYPE\_UNKNOWN,
  pauseWhenDucked: true
};

audioManager.on('interrupt', interAudioInterrupt, (interruptAction: audio.InterruptAction) => {
  if (interruptAction.actionType === 0) {
    console.info('An event to gain the audio focus starts.');
    console.info(\`Focus hint: ${interruptAction.hint} \`);
  }
  if (interruptAction.actionType === 1) {
    console.info('An audio interruption event starts.');
    console.info(\`Audio interruption hint: ${interruptAction.hint} \`);
  }
});

#### off('interrupt')(deprecated)

off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void

Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/NAwECWFuRgKxhhyl6BVxEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2672987F6A022338FC193021DB27D980E5EAC47EA5DD362ABB7BF42571F6C499)

This API is supported since API version 7 and deprecated since API version 11. You are advised to use [off('audioInterrupt')](../interface-audiocapturer/document.md#offaudiointerrupt10) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'interrupt'** is triggered when the audio focus is changed. |
| interrupt | [AudioInterrupt](../interfaces-others/document.md#audiointerruptdeprecated) | Yes | Audio interruption event type. |
| callback | Callback<[InterruptAction](../interfaces-others/document.md#interruptactiondeprecated)\> | No | Callback used to return the event information. |

**Example**

import { audio } from '@kit.AudioKit';

let interAudioInterrupt: audio.AudioInterrupt = {
  streamUsage: audio.StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION,
  contentType: audio.ContentType.CONTENT\_TYPE\_UNKNOWN,
  pauseWhenDucked: true
};

// Cancel all subscriptions to the event.
audioManager.off('interrupt', interAudioInterrupt);

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let interruptCallback = (interruptAction: audio.InterruptAction) => {
  if (interruptAction.actionType === 0) {
    console.info('An event to gain the audio focus starts.');
    console.info(\`Focus hint: ${interruptAction.hint} \`);
  }
  if (interruptAction.actionType === 1) {
    console.info('An audio interruption event starts.');
    console.info(\`Audio interruption hint: ${interruptAction.hint} \`);
  }
};

audioManager.on('interrupt', interAudioInterrupt, interruptCallback);

audioManager.off('interrupt', interAudioInterrupt, interruptCallback);
