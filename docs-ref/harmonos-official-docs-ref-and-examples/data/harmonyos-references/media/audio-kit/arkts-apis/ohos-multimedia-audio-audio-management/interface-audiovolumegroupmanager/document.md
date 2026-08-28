# Interface (AudioVolumeGroupManager)

This interface implements volume management for an audio group.

Before calling any API in AudioVolumeGroupManager, you must use [getVolumeGroupManager](../interface-audiovolumemanager/document.md#getvolumegroupmanager9) to obtain an AudioVolumeGroupManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Srxgg-YORCmyOdRHy5wQrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=064E0FAA0001D35BB690DB2792263AB8FB00B3260D9031334688B5BA97300034)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

Obtains the volume of a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ljbEyxOgT_KZlrdx55W1hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EF80C49ED84D902DA4D6F5F42EB239A36CB3793A09F03DB494FCF47F779FB92)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [getVolumeByStream](../interface-audiovolumemanager/document.md#getvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the stream volume obtained; otherwise, **err** is an error object. The volume range of a specified stream can be obtained by calling [getMinVolume](#getminvolumedeprecated) and [getMaxVolume](#getmaxvolumedeprecated). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to get volume. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting volume. Volume: ${value}.\`);
});

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType): Promise<number>

Obtains the volume of a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/j5oTa8d4Q3SPdBfPVOQ6UQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24C7D08C39B1DA28B73980CC5B2300737C5288F1E77B07DEBB197917A9BC52B9)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [getVolumeByStream](../interface-audiovolumemanager/document.md#getvolumebystream20) instead.

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

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(\`Succeeded in getting volume. Volume: ${value}.\`);
});

#### getVolumeSync(deprecated)

getVolumeSync(volumeType: AudioVolumeType): number

Obtains the volume of a stream. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/_EREMd93QWO_CxvvGIT7KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2628D073191CBF3FC1B649FB4982C10DD108EDF22AF4C0E53DDB921321C71D8B)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [getVolumeByStream](../interface-audiovolumemanager/document.md#getvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume of the stream. The volume range of a specified stream can be obtained by calling [getMinVolume](#getminvolumedeprecated) and [getMaxVolume](#getmaxvolumedeprecated). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(\`Succeeded in getting volume. Volume: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get volume. Code: ${error.code}, message: ${error.message}\`);
}

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

Obtains the minimum volume allowed for a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/V0eymhhoQMqgp6kTs39r8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7A7C58F72DB1C3D1637F3C4CFA9EE373FF50E2AC9C61C4CD33E4D8ACE7E274C)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [getMinVolumeByStream](../interface-audiovolumemanager/document.md#getminvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the minimum stream volume obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to get minVolume. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting minVolume. Volume: ${value}.\`);
});

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType): Promise<number>

Obtains the minimum volume allowed for a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/H7T1fKHtRLq4t-uPmmG2JQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E7A64985F6FDC3810559ABAB3B9E93B4A7E456B2126CAF5D07F6B87DCDB4E3A)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [getMinVolumeByStream](../interface-audiovolumemanager/document.md#getminvolumebystream20) instead.

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

audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(\`Succeeded in getting minVolume. Volume: ${value}.\`);
});

#### getMinVolumeSync(deprecated)

getMinVolumeSync(volumeType: AudioVolumeType): number

Obtains the minimum volume allowed for a stream. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Wp1gDasGSeywGgiKiGtTrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E0466A1060233E5BA54A83DBDB47415E0FB47B8A477F9972DEBA05C5B3B8FCF)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [getMinVolumeByStream](../interface-audiovolumemanager/document.md#getminvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Minimum volume. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMinVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(\`Succeeded in getting minVolume. Volume: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get minVolume. Code: ${error.code}, message: ${error.message}\`);
}

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

Obtains the maximum volume allowed for a stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/xMOYHrpKRPKnfE42WXvM5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E69C917720491E358F344EC960007E78446E33957602997C68E174EC21BA595)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [getMaxVolumeByStream](../interface-audiovolumemanager/document.md#getmaxvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the maximum stream volume obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to get maxVolume. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting maxVolume. Volume: ${value}.\`);
});

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

Obtains the maximum volume allowed for a stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/9ZzXcIToQZW8tqNjTcPuyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B18340BC4DB1E5F80591761CBC48910C84964DD32EF59B69A433228003F32CCB)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [getMaxVolumeByStream](../interface-audiovolumemanager/document.md#getmaxvolumebystream20) instead.

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

audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(\`Succeeded in getting maxVolume. Volume: ${value}.\`);
});

#### getMaxVolumeSync(deprecated)

getMaxVolumeSync(volumeType: AudioVolumeType): number

Obtains the maximum volume allowed for a stream. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/lfcaddCvTkG6XLS3kIO-ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F08A72443FE16CDBDBB2B5A932D1B13249D66D55E4C986292A6319C9436CE29E)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [getMaxVolumeByStream](../interface-audiovolumemanager/document.md#getmaxvolumebystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum volume. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMaxVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(\`Succeeded in getting maxVolume. Volume: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get maxVolume. Code: ${error.code}, message: ${error.message}\`);
}

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

Checks whether a stream is muted. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/6E4QonBqSjqfG3fg1fKLig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F52FD6D5539411842B865FFB9DA6F0840E888986B2E8281F8A46643137C1337)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [isSystemMutedForStream](../interface-audiovolumemanager/document.md#issystemmutedforstream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the stream is muted or **false** if not muted; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to use isMute function. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in using isMute function. MuteState: ${value}.\`);
});

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType): Promise<boolean>

Checks whether a stream is muted. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/k29_msynT5KwDy60SLa0xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB54BCFBBFCCBE561B7C182299866014104317C411495D8117090AE6B9A87FAD)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [isSystemMutedForStream](../interface-audiovolumemanager/document.md#issystemmutedforstream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result, indicating whether the stream is muted. **true** if muted, **false** otherwise. |

**Example**

audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(\`Succeeded in using isMute function. MuteState: ${value}.\`);
});

#### isMuteSync(deprecated)

isMuteSync(volumeType: AudioVolumeType): boolean

Checks whether a stream is muted. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/1RDxOpD7SPqWgvfErNpzqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4836567B88AD325034FDF81E1E0A2F9208D86A89F3C827B26DA2598D04270DB8)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [isSystemMutedForStream](../interface-audiovolumemanager/document.md#issystemmutedforstream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the stream is muted. **true** if muted, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMuteSync(audio.AudioVolumeType.MEDIA);
  console.info(\`Succeeded in using isMuteSync function. MuteState: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to use isMuteSync function. Code: ${error.code}, message: ${error.message}\`);
}

#### getRingerMode9+

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

Obtains the ringer mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRingMode](../enums/document.md#audioringmode)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the ringer mode obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(\`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting ringerMode. AudioRingMode: ${value}.\`);
});

#### getRingerMode9+

getRingerMode(): Promise<AudioRingMode>

Obtains the ringer mode. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioRingMode](../enums/document.md#audioringmode)\> | Promise used to return the ringer mode. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(\`Succeeded in getting ringerMode. AudioRingMode: ${value}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}\`);
});

#### getRingerModeSync10+

getRingerModeSync(): AudioRingMode

Obtains the ringer mode. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioRingMode](../enums/document.md#audioringmode) | Ringer mode. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioRingMode = audioVolumeGroupManager.getRingerModeSync();
  console.info(\`Succeeded in getting ringerMode. AudioRingMode: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get ringerMode. Code: ${error.code}, message: ${error.message}\`);
}

#### on('ringerModeChange')9+

on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void

Subscribes to the ringer mode change event, which is triggered when the [AudioRingMode](../enums/document.md#audioringmode) changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'ringerModeChange'** is triggered when the ringer mode is changed. |
| callback | Callback<[AudioRingMode](../enums/document.md#audioringmode)\> | Yes | Callback used to return the changed ringer mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioVolumeGroupManager.on('ringerModeChange', (ringerMode: audio.AudioRingMode) => {
  console.info(\`Succeeded in using on function. AudioRingMode: ${ringerMode}.\`);
});

#### off('ringerModeChange')18+

off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void

Unsubscribes from the ringer mode change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'ringerModeChange'** is triggered when the ringer mode is changed. |
| callback | Callback<[AudioRingMode](../enums/document.md#audioringmode)\> | No | Callback used to return the changed ringer mode. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioVolumeGroupManager.off('ringerModeChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let ringerModeChangeCallback = (ringerMode: audio.AudioRingMode) => {
  console.info(\`Succeeded in using on or off function. AudioRingMode: ${ringerMode}.\`);
};

audioVolumeGroupManager.on('ringerModeChange', ringerModeChangeCallback);

audioVolumeGroupManager.off('ringerModeChange', ringerModeChangeCallback);

#### isMicrophoneMute9+

isMicrophoneMute(callback: AsyncCallback<boolean>): void

Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the microphone is muted or **false** if not muted; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in using isMicrophoneMute function. MuteState: ${value}.\`);
});

#### isMicrophoneMute9+

isMicrophoneMute(): Promise<boolean>

Checks whether the microphone is muted. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result, indicating whether the microphone is muted. **true** if muted, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
  console.info(\`Succeeded in using isMicrophoneMute function. MuteState: ${value}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}\`);
});

#### isMicrophoneMuteSync10+

isMicrophoneMuteSync(): boolean

Checks whether the microphone is muted. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the microphone is muted. **true** if muted, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMicrophoneMuteSync();
  console.info(\`Succeeded in using isMicrophoneMuteSync function. MuteState: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to use isMicrophoneMuteSync function. Code: ${error.code}, message: ${error.message}\`);
}

#### on('micStateChange')9+

on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void

Subscribes to the microphone state change event, which is triggered when the microphone state is changed. This API uses an asynchronous callback to return the result.

Currently, when multiple AudioManager instances are used in a single process, only the subscription of the last instance takes effect, and the subscription of other instances is overwritten (even if the last instance does not initiate a subscription). Therefore, you are advised to use a single AudioManager instance.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'micStateChange'** is triggered when the microphone state is changed. |
| callback | Callback<[MicStateChangeEvent](../interfaces-others/document.md#micstatechangeevent9)\> | Yes | Callback used to return the changed microphone state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
  console.info(\`Succeeded in using on function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.\`);
});

#### off('micStateChange')12+

off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void

Unsubscribes from the microphone state change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'micStateChange'** is triggered when the microphone state is changed. |
| callback | Callback<[MicStateChangeEvent](../interfaces-others/document.md#micstatechangeevent9)\> | No | Callback used to return the changed microphone state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioVolumeGroupManager.off('micStateChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let micStateChangeCallback = (micStateChange: audio.MicStateChangeEvent) => {
  console.info(\`Succeeded in using on or off function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.\`);
};

audioVolumeGroupManager.on('micStateChange', micStateChangeCallback);

audioVolumeGroupManager.off('micStateChange', micStateChangeCallback);

#### isVolumeUnadjustable10+

isVolumeUnadjustable(): boolean

Checks whether the fixed volume mode is enabled. When the fixed volume mode is enabled, the volume cannot be adjusted. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the fixed volume mode is enabled. **true** if enabled, **false** otherwise. |

**Example**

let volumeAdjustSwitch: boolean = audioVolumeGroupManager.isVolumeUnadjustable();
console.info(\`Succeeded in using isVolumeUnadjustable function. VolumeUnadjustable: ${volumeAdjustSwitch}.\`);

#### getSystemVolumeInDb(deprecated)

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void

Obtains the volume gain. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/3P2VDvVISCqbyVxm2pgtlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E54AF5EDF5C0F4210A8C1A29F3DC05D8421710F31A09E1361FF93A96E92C1B1)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [getVolumeInUnitOfDbByStream](../interface-audiovolumemanager/document.md#getvolumeinunitofdbbystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| volumeLevel | number | Yes | Volume level. |
| device | [DeviceType](../enums/document.md#devicetype) | Yes | Device type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the volume gain obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |
| 6800301 | System error. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER, (err: BusinessError, value: number) => {
  if (err) {
    console.error(\`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting system volume in db. DB: ${value}.\`);
  }
});

#### getSystemVolumeInDb(deprecated)

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>

Obtains the volume gain. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/BBl6gzcSRc-OYF-nPvgEXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6718B8DC948C166234F08D8F330E40A8779A6B478C3FEE6FA3FC85461C7E63F)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [getVolumeInUnitOfDbByStream](../interface-audiovolumemanager/document.md#getvolumeinunitofdbbystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| volumeLevel | number | Yes | Volume level. |
| device | [DeviceType](../enums/document.md#devicetype) | Yes | Device type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the volume gain (in dB). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER).then((value: number) => {
  console.info(\`Succeeded in getting system volume in db. DB: ${value}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}\`);
});

#### getSystemVolumeInDbSync(deprecated)

getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number

Obtains the volume gain. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/hwzvZ3aZTJGRYYUFOIlNKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=425D9E6CA08CC969DBC2EA58AE70F53571983958D205732510DCA76094AA76BE)

This API is supported since API version 10 and deprecated since API version 20. You are advised to use [getVolumeInUnitOfDbByStream](../interface-audiovolumemanager/document.md#getvolumeinunitofdbbystream20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | Yes | Audio volume type. |
| volumeLevel | number | Yes | Volume level. |
| device | [DeviceType](../enums/document.md#devicetype) | Yes | Device type. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume gain (in dB). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getSystemVolumeInDbSync(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER);
  console.info(\`Succeeded in getting system volume in db sync. DB: ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get system volume in db sync. Code: ${error.code}, message: ${error.message}\`);
}

#### getMaxAmplitudeForInputDevice12+

getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>

Obtains the maximum amplitude (in the range \[0, 1\]) of the audio stream for an input device. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputDevice | [AudioDeviceDescriptor](../interfaces-others/document.md#audiodevicedescriptor) | Yes | Descriptor of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum amplitude, which is in the range \[0, 1\]. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

audio.getAudioManager().getRoutingManager().getPreferredInputDeviceForCapturerInfo(capturerInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForInputDevice(data\[0\]).then((value) => {
    console.info(\`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}\`);
  })
}).catch((err: BusinessError) => {
  console.error(\`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}\`);
})

#### getMaxAmplitudeForOutputDevice12+

getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>

Obtains the maximum amplitude (in the range \[0, 1\]) of the audio stream for an output device. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| outputDevice | [AudioDeviceDescriptor](../interfaces-others/document.md#audiodevicedescriptor) | Yes | Descriptor of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum amplitude, which is in the range \[0, 1\]. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

audio.getAudioManager().getRoutingManager().getPreferOutputDeviceForRendererInfo(rendererInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForOutputDevice(data\[0\]).then((value) => {
    console.info(\`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}\`);
  })
}).catch((err: BusinessError) => {
  console.error(\`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}\`);
})

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

Mutes or unmutes the microphone. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/1On5n3XUTR2nOIVTRwt3lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0FAB1A756FEBBDF54577A21D244E0DE85CB69B66CB7349978AAE6582EB2380C)

This API is supported since API version 9 and deprecated since API version 11. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_AUDIO\_CONFIG (available only for system applications)

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mute | boolean | Yes | Mute status to set. **true** to mute, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set microphone mute. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting microphone mute.');
});

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean): Promise<void>

Mutes or unmutes the microphone. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/LRPXp0FZTI-27e4BwNwVwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E298D4B4F60DD8FBFB4414ACEA305E7B0A894AAFA7F022065BA5180732D73EF3)

This API is supported since API version 9 and deprecated since API version 11. Its substitute is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_AUDIO\_CONFIG (available only for system applications)

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mute | boolean | Yes | Mute status to set. **true** to mute, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise object that returns no value. |

**Example**

audioVolumeGroupManager.setMicrophoneMute(true).then(() => {
  console.info('Succeeded in setting microphone mute.');
});
