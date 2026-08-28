# Interface (AudioStreamManager)

This interface implements audio stream management.

Before calling any API in AudioStreamManager, you must use [getStreamManager](../interface-audiomanager/document.md#getstreammanager9) to obtain an AudioStreamManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/g-rtRT52T3-jqpWoe9IYKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACE650358AA6A232CB79CA51607974B8AFB35693BE12A282707C1470CC33F46F)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### getCurrentAudioRendererInfoArray9+

getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void

Obtains the information about this audio renderer. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/PXRxAe_LS3W5V_adEnxJtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82BACCAD4B8A08EB76864C1013486E40AD4AE4E91EEAC965BE3AC1D3BEDB2C4A)

The audio renderer information returned by this API may include internal audio playback streams, such as cellular calls and ultrasonic streams.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRendererChangeInfoArray](../types/document.md#audiorendererchangeinfoarray9)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio renderer information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioRendererInfoArray((err: BusinessError, audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  if (err) {
    console.error(\`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.\`);
  }
});

#### getCurrentAudioRendererInfoArray9+

getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>

Obtains the information about this audio renderer. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/wCcoSFLVS9uinl17BIEjfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC9D4E3B27AFF545A90896801C1821EAAE0FDAFB82F4847D9CEF2110E695EF12)

The audio renderer information returned by this API may include internal audio playback streams, such as cellular calls and ultrasonic streams.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioRendererChangeInfoArray](../types/document.md#audiorendererchangeinfoarray9)\> | Promise used to return the audio renderer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioRendererInfoArray().then((audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  console.info(\`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}\`);
});

#### getCurrentAudioRendererInfoArraySync10+

getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray

Obtains the information about this audio renderer. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/-OEd7pfLSVGZDdU0GXXNeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77D0E483AA6168B595540C196B35128FDE2FE83B5C8ACC2F1D4D5535E66CCC39)

The audio renderer information returned by this API may include internal audio playback streams, such as cellular calls and ultrasonic streams.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioRendererChangeInfoArray](../types/document.md#audiorendererchangeinfoarray9) | Audio renderer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray = audioStreamManager.getCurrentAudioRendererInfoArraySync();
  console.info(\`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get current audio renderer info array. Code: ${error.code}, message: ${error.message}\`);
}

#### getCurrentAudioCapturerInfoArray9+

getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void

Obtains the information about this audio capturer. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/pcd8ET79TzCOMf36ZGRS_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C977FE6F90242A2F965A86AD18F6B0B317888246A4D2ECC2C4D9FF74D47890F8)

The audio capturer information returned by this API may include internal audio recording streams, such as voice wakeup and cellular calls.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioCapturerChangeInfoArray](../types/document.md#audiocapturerchangeinfoarray9)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio capturer information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioCapturerInfoArray((err: BusinessError, audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
  if (err) {
    console.error(\`Failed to get current audio capturer info array. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.\`);
  }
});

#### getCurrentAudioCapturerInfoArray9+

getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>

Obtains the information about this audio capturer. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/_khl2EZmSUeymUzT3BH52g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B23B5B955F37FD1A2D45388D9B9941D1F5953D800699C4801463E5C7F318AB73)

The audio capturer information returned by this API may include internal audio recording streams, such as voice wakeup and cellular calls.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioCapturerChangeInfoArray](../types/document.md#audiocapturerchangeinfoarray9)\> | Promise used to return the audio capturer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioCapturerInfoArray().then((audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
  console.info(\`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get current audio capturer info array. Code: ${err.code}, message: ${err.message}\`);
});

#### getCurrentAudioCapturerInfoArraySync10+

getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray

Obtains the information about this audio capturer. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/q4jBwUvJTaq5QZc7EG7sBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB61A8843D296D062CC19A9F7E6312967D6E6E328BC5FFB75B6D5548474AFEEF)

The audio capturer information returned by this API may include internal audio recording streams, such as voice wakeup and cellular calls.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioCapturerChangeInfoArray](../types/document.md#audiocapturerchangeinfoarray9) | Audio capturer information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioCapturerChangeInfoArray = audioStreamManager.getCurrentAudioCapturerInfoArraySync();
  console.info(\`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get current audio capturer info array. Code: ${error.code}, message: ${error.message}\`);
}

#### on('audioRendererChange')9+

on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void

Subscribes to the audio renderer change event, which is triggered when the audio playback stream status or device is changed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/VcboGuW6TJGDJvQ-UZKAQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAD9A130F55DE5F5F856B6E25765328E73C97C1960443639BB23D923DB07572A)

The audio renderer information returned by this API may include internal audio playback streams, such as cellular calls and ultrasonic streams.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioRendererChange'** is triggered when the audio playback stream status or device is changed. |
| callback | Callback<[AudioRendererChangeInfoArray](../types/document.md#audiorendererchangeinfoarray9)\> | Yes | Callback used to return the audio renderer information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioStreamManager.on('audioRendererChange',  (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  console.info(\`Succeeded in using on function, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.\`);
});

#### off('audioRendererChange')9+

off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void

Unsubscribes from the audio renderer change event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/cn10_WB1QjSBpU8b5e1qfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5515D0188EB4B98A1C9D94A506D9468FE3E8F5551CA1050331C3ABC8BDA0F6BD)

The audio renderer information returned by this API may include internal audio playback streams, such as cellular calls and ultrasonic streams.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioRendererChange'** is triggered when the audio playback stream status or device is changed. |
| callback18+ | Callback<[AudioRendererChangeInfoArray](../types/document.md#audiorendererchangeinfoarray9)\> | No | Callback used to return the audio renderer information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
// When there are multiple listeners for this event, you can use audioStreamManager.off('audioRendererChange'); to unregister all of them.
let audioRendererChangeCallback = (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  console.info(\`Succeeded in using on or off function, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.\`);
};

audioStreamManager.on('audioRendererChange', audioRendererChangeCallback);

audioStreamManager.off('audioRendererChange', audioRendererChangeCallback);

#### on('audioCapturerChange')9+

on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void

Subscribes to the audio capturer change event, which is triggered when the audio recording stream status or device is changed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/9QtQ1NV4QTanCfIKFSNuIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7865230B6E96E0B8AF4AE04F16D43EE82F6141DF7B393B5E4F9CD0B7D5289B2)

The audio capturer information returned by this API may include internal audio recording streams, such as voice wakeup and cellular calls.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioCapturerChange'** is triggered when the audio recording stream status or device is changed. |
| callback | Callback<[AudioCapturerChangeInfoArray](../types/document.md#audiocapturerchangeinfoarray9)\> | Yes | Callback used to return the audio capturer information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioStreamManager.on('audioCapturerChange', (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
  console.info(\`Succeeded in using on function, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.\`);
});

#### off('audioCapturerChange')9+

off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void

Unsubscribes from the audio capturer change event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/D69BoZ37TZu1CrWHAEKVmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEDD989746C52870007E41DB03B37484045AFDF60DF0822AC4B70E243357E1E1)

The audio capturer information returned by this API may include internal audio recording streams, such as voice wakeup and cellular calls.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioCapturerChange'** is triggered when the audio capturer is changed. |
| callback18+ | Callback<[AudioCapturerChangeInfoArray](../types/document.md#audiocapturerchangeinfoarray9)\> | No | Callback used to return the audio capturer information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
// When there are multiple listeners for this event, you can use audioStreamManager.off('audioCapturerChange'); to unregister all of them.
let audioCapturerChangeCallback = (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
  console.info(\`Succeeded in using on or off function, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.\`);
};

audioStreamManager.on('audioCapturerChange', audioCapturerChangeCallback);

audioStreamManager.off('audioCapturerChange', audioCapturerChangeCallback);

#### isActive(deprecated)

isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

Checks whether a stream is active. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/m8ljD9D9RjKKPM91Shb4oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=698B34A8283FD231EE68828EBA5E5919184A87EE6F9328F85BAA68DDEFCF1B75)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [isStreamActive](#isstreamactive20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio stream types. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the stream is active or **false** if not active; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
if (err) {
  console.error(\`Failed to obtain the active status of the stream. ${err}\`);
  return;
}
  console.info(\`Callback invoked to indicate that the active status of the stream is obtained ${value}.\`);
});

#### isActive(deprecated)

isActive(volumeType: AudioVolumeType): Promise<boolean>

Checks whether a stream is active. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/37gD6_IAQTOw2LbgKB3pxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA0F6607B2054D54B253692370EEB4DB191F80213BC9AFE20DC25C4CCA297778)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [isStreamActive](#isstreamactive20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio stream types. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result, indicating whether the stream is active. **true** if active, **false** otherwise. |

**Example**

audioStreamManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(\`Promise returned to indicate that the active status of the stream is obtained ${value}.\`);
});

#### isActiveSync(deprecated)

isActiveSync(volumeType: AudioVolumeType): boolean

Checks whether a stream is active. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/nmZVWX6KSAe1IS92iffC_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1C693338665429B16050EA289B25E1DC421208D27047BB681390B1D3EFC0A5D)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [isStreamActive](#isstreamactive20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio stream types. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the stream is active. **true** if active, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioStreamManager.isActiveSync(audio.AudioVolumeType.MEDIA);
  console.info(\`Indicate that the active status of the stream is obtained ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtain the active status of the stream ${error}.\`);
}

#### isStreamActive20+

isStreamActive(streamUsage: StreamUsage): boolean

Checks whether a stream is active. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream usage. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the stream is active. **true** if active, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isStreamActive = audioStreamManager.isStreamActive(audio.StreamUsage.STREAM\_USAGE\_MUSIC);
  console.info(\`Succeeded in using isStreamActive function, IsStreamActive: ${isStreamActive}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to use isStreamActive function. code: ${error.code}, message: ${error.message}\`);
}

#### getAudioEffectInfoArray10+

getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void

Obtains information about the audio effect mode in use. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| usage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream usage. |
| callback | AsyncCallback<[AudioEffectInfoArray](#getaudioeffectinfoarray10)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the information about the audio effect mode obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getAudioEffectInfoArray(audio.StreamUsage.STREAM\_USAGE\_MUSIC, (err: BusinessError, audioEffectInfoArray: audio.AudioEffectInfoArray) => {
  if (err) {
    console.error(\`Failed to get audio effect info array. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.\`);
  }
});

#### getAudioEffectInfoArray10+

getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>

Obtains information about the audio effect mode in use. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| usage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream usage. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioEffectInfoArray](#getaudioeffectinfoarray10)\> | Promise used to return the information about the audio effect mode obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getAudioEffectInfoArray(audio.StreamUsage.STREAM\_USAGE\_MUSIC).then((audioEffectInfoArray: audio.AudioEffectInfoArray) => {
  console.info(\`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get audio effect info array. Code: ${err.code}, message: ${err.message}\`);
});

#### getAudioEffectInfoArraySync10+

getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray

Obtains information about the audio effect mode in use. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| usage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream usage. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioEffectInfoArray](#getaudioeffectinfoarray10) | Information about the audio effect mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioEffectInfoArray = audioStreamManager.getAudioEffectInfoArraySync(audio.StreamUsage.STREAM\_USAGE\_MUSIC);
  console.info(\`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get audio effect info array. Code: ${error.code}, message: ${error.message}\`);
}

#### isAcousticEchoCancelerSupported20+

isAcousticEchoCancelerSupported(sourceType: SourceType): boolean

Checks whether the specified audio source type supports echo cancellation.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sourceType | [SourceType](../enums/document.md#sourcetype8) | Yes | Audio source type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether echo cancellation is supported. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isAcousticEchoCancelerSupported = audioStreamManager.isAcousticEchoCancelerSupported(audio.SourceType.SOURCE\_TYPE\_LIVE);
  console.info(\`Succeeded in using isAcousticEchoCancelerSupported function, IsAcousticEchoCancelerSupported: ${isAcousticEchoCancelerSupported}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to use isAcousticEchoCancelerSupported function. code: ${error.code}, message: ${error.message}\`);
}

#### isAudioLoopbackSupported20+

isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean

Checks whether the current system supports the specified audio loopback mode.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [AudioLoopbackMode](../enums/document.md#audioloopbackmode20) | Yes | Audio loopback mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the audio loopback mode is supported. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isAudioLoopbackSupported = audioStreamManager.isAudioLoopbackSupported(audio.AudioLoopbackMode.HARDWARE);
  console.info(\`Succeeded in using isAudioLoopbackSupported function, IsAudioLoopbackSupported: ${isAudioLoopbackSupported}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to use isAudioLoopbackSupported function. code: ${error.code}, message: ${error.message}\`);
}

#### isRecordingAvailable20+

isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean

Checks whether recording can be started based on the audio source type in the audio capturer information.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capturerInfo | [AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8) | Yes | Audio capturer information. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Check result for whether recording can be started. **true** if recording can be started, **false** otherwise.

This API checks whether the specified audio source type in the capturer information can acquire focus. It should be called before starting audio recording to avoid conflicts with existing recording streams.

 |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000,
  channels: audio.AudioChannel.CHANNEL\_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC,
  capturerFlags: 0
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

audio.createAudioCapturer(audioCapturerOptions, (err: BusinessError, audioCapturer: audio.AudioCapturer) => {
  if (err) {
    console.error(\`Failed to create AudioCapturer. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info('Succeeded in creating AudioCapturer.');
    try {
      let isRecordingAvailable = audioStreamManager.isRecordingAvailable(audioCapturerInfo);
      console.info(\`Succeeded in using isRecordingAvailable function, IsRecordingAvailable: ${isRecordingAvailable}.\`);
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to use isRecordingAvailable function. code: ${error.code}, message: ${error.message}\`);
    }
  }
});

#### isIntelligentNoiseReductionEnabledForCurrentDevice21+

isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean

Checks whether the intelligent noise reduction feature is enabled for the audio stream of the specified source type.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sourceType | [SourceType](../enums/document.md#sourcetype8) | Yes | Audio source type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the intelligent noise reduction feature is enabled. **true** if enabled, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSupport = audioStreamManager.isIntelligentNoiseReductionEnabledForCurrentDevice(audio.SourceType.SOURCE\_TYPE\_LIVE);
  console.info(\`SourceType: ${audio.SourceType.SOURCE\_TYPE\_LIVE} intelligent noise reduction enabled is: ${isSupport}\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`isIntelligentNoiseReductionEnabledForCurrentDevice ERROR: ${error}\`);
}
