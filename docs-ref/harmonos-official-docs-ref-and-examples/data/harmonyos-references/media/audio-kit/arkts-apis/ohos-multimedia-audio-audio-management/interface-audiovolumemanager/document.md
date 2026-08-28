# Interface (AudioVolumeManager)

This interface implements audio volume management.

Before calling any API in AudioVolumeManager, you must use [getVolumeManager](../interface-audiomanager/document.md#getvolumemanager9) to obtain an AudioVolumeManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/IlhwvjJuTdSRzC4c2i5m-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D33FD644BAF71C312D7B2ADF21864503E3C680EC936F060ABFD87547E83E7AE)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### getVolumeGroupManager9+

getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void

Obtains a VolumeGroupManager instance. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupId | number | Yes | Volume group ID. The default value is **DEFAULT\_VOLUME\_GROUP\_ID**. |
| callback | AsyncCallback<[AudioVolumeGroupManager](../interface-audiovolumegroupmanager/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the VolumeGroupManager instance obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number = audio.DEFAULT\_VOLUME\_GROUP\_ID;

audioVolumeManager.getVolumeGroupManager(groupId, (err: BusinessError, audioVolumeGroupManager: audio.AudioVolumeGroupManager) => {
  if (err) {
    console.error(\`Failed to get volume group manager. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting volume group manager.');
});

#### getVolumeGroupManager9+

getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>

Obtains a VolumeGroupManager instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupId | number | Yes | Volume group ID. The default value is **DEFAULT\_VOLUME\_GROUP\_ID**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise< [AudioVolumeGroupManager](../interface-audiovolumegroupmanager/document.md) > | Promise used to return the VolumeGroupManager instance. |

**Example**

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number = audio.DEFAULT\_VOLUME\_GROUP\_ID;

audioVolumeManager.getVolumeGroupManager(groupId).then((audioVolumeGroupManager: audio.AudioVolumeGroupManager) => {
  console.info('Succeeded in getting volume group manager.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to get volume group manager. Code: ${err.code}, message: ${err.message}\`);
});

#### getVolumeGroupManagerSync10+

getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager

Obtains a VolumeGroupManager instance. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| groupId | number | Yes | Volume group ID. The default value is **DEFAULT\_VOLUME\_GROUP\_ID**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioVolumeGroupManager](../interface-audiovolumegroupmanager/document.md) | VolumeGroupManager instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioVolumeGroupManager: audio.AudioVolumeGroupManager = audioVolumeManager.getVolumeGroupManagerSync(audio.DEFAULT\_VOLUME\_GROUP\_ID);
  console.info('Succeeded in getting volume group manager.');
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get volume group manager. Code: ${error.code}, message: ${error.message}\`);
}

#### getAppVolumePercentage19+

getAppVolumePercentage(): Promise<number>

Obtains the volume of the application. (The volume range is 0 to 100.) This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the application volume. |

**Example**

import { audio } from '@kit.AudioKit';

audioVolumeManager.getAppVolumePercentage().then((value: number) => {
  console.info(\`app volume is ${value}.\`);
});

#### setAppVolumePercentage19+

setAppVolumePercentage(volume: number): Promise<void>

Sets the volume (within a range of 0 to 100) for the application. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| volume | number | Yes | Volume to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Crash or blocking occurs in system process. |

**Example**

import { audio } from '@kit.AudioKit';

audioVolumeManager.setAppVolumePercentage(20).then(() => {
  console.info(\`set app volume success.\`);
});

#### on('volumeChange')(deprecated)

on(type: 'volumeChange', callback: Callback<VolumeEvent>): void

Subscribes to the system volume change event, which is triggered when the system volume is changed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/R2OmLiwbQsCT2faXlCo4cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E0DEB80A055C4E5CA6C564701E6260AEDACD5A3DE93A40FC07EED9FFB9DDC83)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [on('streamVolumeChange')](#onstreamvolumechange20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'volumeChange'** is triggered when the system volume is changed. |
| callback | Callback<[VolumeEvent](../interfaces-others/document.md#volumeevent9)\> | Yes | Callback used to return the changed volume. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioVolumeManager.on('volumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(\`VolumeType of stream: ${volumeEvent.volumeType} \`);
  console.info(\`Volume level: ${volumeEvent.volume} \`);
  console.info(\`Whether to updateUI: ${volumeEvent.updateUi} \`);
});

#### off('volumeChange')(deprecated)

off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void

Unsubscribes from the system volume change event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/UAtJ-FbLRnqChFjPOmLn0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=342C4832D6D7C2AA03A81D642A7302351B0AB4E559CFC24B672C67311D1D6023)

This API is supported since API version 12 and deprecated since API version 20. You are advised to use [off('streamVolumeChange')](#offstreamvolumechange20) instead.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'volumeChange'** is triggered when the system volume is changed. |
| callback | Callback<[VolumeEvent](../interfaces-others/document.md#volumeevent9)\> | No | Callback used to return the changed volume. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioVolumeManager.off('volumeChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let volumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(\`VolumeType of stream: ${volumeEvent.volumeType} \`);
  console.info(\`Volume level: ${volumeEvent.volume} \`);
  console.info(\`Whether to updateUI: ${volumeEvent.updateUi} \`);
};

audioVolumeManager.on('volumeChange', volumeChangeCallback);

audioVolumeManager.off('volumeChange', volumeChangeCallback);

#### on('appVolumeChange')19+

on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void

Subscribes to the application-level volume change event of the application (triggered when the application-level volume is changed). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'appVolumeChange'** is triggered when the application-level volume is changed. |
| callback | Callback<[VolumeEvent](../interfaces-others/document.md#volumeevent9)\> | Yes | Callback used to return the changed volume. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

audioVolumeManager.on('appVolumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(\`VolumeType of stream: ${volumeEvent.volumeType} \`);
  console.info(\`Volume level: ${volumeEvent.volume} \`);
  console.info(\`Whether to updateUI: ${volumeEvent.updateUi} \`);
});

#### off('appVolumeChange')19+

off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void

Unsubscribes from the application-level volume change event of the application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'appVolumeChange'** is triggered when the application-level volume is changed. |
| callback | Callback<[VolumeEvent](../interfaces-others/document.md#volumeevent9)\> | No | Callback used to return the changed volume. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioVolumeManager.off('appVolumeChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(\`VolumeType of stream: ${volumeEvent.volumeType} \`);
  console.info(\`Volume level: ${volumeEvent.volume} \`);
  console.info(\`Whether to updateUI: ${volumeEvent.updateUi} \`);
};

audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);

audioVolumeManager.off('appVolumeChange', appVolumeChangeCallback);

#### getVolumeByStream20+

getVolumeByStream(streamUsage: StreamUsage): number

Obtains the volume of a specified audio stream.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream for which the volume is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Obtain the volume of a specified audio stream.
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volume : number = audio.getAudioManager().getVolumeManager().getVolumeByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);
  console.info(\`Obtains the volume of a stream success.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtains the volume of a stream, error: ${error}\`);
}

#### getMinVolumeByStream20+

getMinVolumeByStream(streamUsage: StreamUsage): number

Obtains the minimum volume of a specified audio stream.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream for which the minimum volume is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Obtain the minimum volume of a specified audio stream.
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volume : number = audio.getAudioManager().getVolumeManager().getMinVolumeByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);
  console.info(\`Obtains the minimum volume allowed for a stream success.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtains the minimum volume allowed for a stream, error: ${error}\`);
}

#### getMaxVolumeByStream20+

getMaxVolumeByStream(streamUsage: StreamUsage): number

Obtains the maximum volume of a specified audio stream.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream for which the maximum volume is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Obtain the maximum volume of a specified audio stream.
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volume : number = audio.getAudioManager().getVolumeManager().getMaxVolumeByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);
  console.info(\`Obtains the maximum volume allowed for a stream success.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtains the maximum volume allowed for a stream, error: ${error}\`);
}

#### isSystemMutedForStream20+

isSystemMutedForStream(streamUsage: StreamUsage): boolean

Checks whether a specified audio stream is muted.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the audio stream is muted. **true** if muted, **false** otherwise. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Check whether a specified audio stream is muted.
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let isMuted : boolean = audio.getAudioManager().getVolumeManager().isSystemMutedForStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);
  console.info(\`Checks whether the system is muted based on the stream success.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to checks whether the system is muted based on the stream, error: ${error}\`);
}

#### getVolumeInUnitOfDbByStream20+

getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number

Obtains the volume (in dB) calculated by the system based on the audio stream, volume level, and device type.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream. |
| volumeLevel | number | Yes | Volume level. |
| device | [DeviceType](../enums/document.md#devicetype) | Yes | Device type. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Volume of the audio stream, in dB. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

// Obtain the volume (in dB) calculated by the system based on the audio stream, volume level, and device type.
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volumeInDb : number = audio.getAudioManager().getVolumeManager().getVolumeInUnitOfDbByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC, 5, audio.DeviceType.SPEAKER);
  console.info(\`Gets the volume db value that system calculate by volume stream, volume level and device type.
 success.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to gets the volume db value that system calculate by volume stream, volume level and device type., error: ${error}\`);
}

#### on('streamVolumeChange')20+

on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void

Subscribes to the system audio volume change event, which is triggered when the system audio volume is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'streamVolumeChange'** is triggered when the system audio volume is changed. |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | Yes | Audio stream usage. |
| callback | Callback<[StreamVolumeEvent](../interfaces-others/document.md#streamvolumeevent20)\> | Yes | Callback used to return the changed volume. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**Example**

audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM\_USAGE\_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(\`StreamUsage of stream: ${streamVolumeEvent.streamUsage} \`);
  console.info(\`Volume level: ${streamVolumeEvent.volume} \`);
  console.info(\`Whether to updateUI: ${streamVolumeEvent.updateUi} \`);
});

#### off('streamVolumeChange')20+

off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void

Unsubscribes from the system audio volume change event, which is triggered when the system audio volume is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Volume

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'volumeChange'** is triggered when the system volume is changed. |
| callback | Callback<[StreamVolumeEvent](../interfaces-others/document.md#streamvolumeevent20)\> | No | Callback used to return the changed volume. |

**Example**

// Cancel all subscriptions to the event.
audioVolumeManager.off('streamVolumeChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let streamVolumeChangeCallback = (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(\`StreamUsage of stream: ${streamVolumeEvent.streamUsage} \`);
  console.info(\`Volume level: ${streamVolumeEvent.volume} \`);
  console.info(\`Whether to updateUI: ${streamVolumeEvent.updateUi} \`);
};

audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM\_USAGE\_MUSIC, streamVolumeChangeCallback);

audioVolumeManager.off('streamVolumeChange', streamVolumeChangeCallback);
