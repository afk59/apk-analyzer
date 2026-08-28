# Deprecated Interface (AudioRecorder, deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/qNQ7xaKrTXe9ISzNrI7JvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65D1DA21EEECF909CAD9AEB5241E1472527B196191DF827FDA5D5513EB5C46CA)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder](../interface-avrecorder/document.md) instead.

AudioRecorder is a class for audio recording management. It provides APIs to record audio. Before calling any API in AudioRecorder, you must use [createAudioRecorder()](../functions/document.md#mediacreateaudiorecorderdeprecated) to create an AudioRecorder instance.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### prepare(deprecated)

prepare(config: AudioRecorderConfig): void

Prepares for recording.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/-PeviZu0SPK9HsquF0reGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=412B74623EFDE59FDDFD2A4930D66D9CE6BF77965182B8B44BF4E5710162812F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.prepare](../interface-avrecorder/document.md#prepare9) instead.

**Required permissions:** ohos.permission.MICROPHONE

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [AudioRecorderConfig](../interfaces-others/document.md#audiorecorderconfigdeprecated) | Yes | Audio recording parameters, including the audio output URI, encoding format, sample rate, audio channel count, and output format. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permission denied |

**Example**

let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC\_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC\_ADTS,
  uri : 'fd://1',       // The file must be created by the caller and granted with proper permissions.
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // Set the 'prepare' event callback.
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);

#### start(deprecated)

start(): void

Starts audio recording. This API can be called only after the **'prepare'** event is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/3fzB2Z8iRW2pI2MAqxv2Rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A04D7170B47DC465763708BCED9D92BAB5C50A43B1225598D45FE7FDC285777)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.start](../interface-avrecorder/document.md#start9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Example**

audioRecorder.on('start', () => {    // Set the 'start' event callback.
  console.info('audio recorder start called');
});
audioRecorder.start();

#### pause(deprecated)

pause():void

Pauses audio recording. This API can be called only after the **'start'** event is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/ZBt2VkPsQxiyv0bzyUEa_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC0B672ED73F6C921C1777D60FEEF4754FF514F45608B9C8045FE49A82EA72CC)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.pause](../interface-avrecorder/document.md#pause9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Example**

audioRecorder.on('pause', () => {    // Set the 'pause' event callback.
  console.info('audio recorder pause called');
});
audioRecorder.pause();

#### resume(deprecated)

resume():void

Resumes audio recording. This API can be called only after the **'pause'** event is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/61kltlWmSBGTMM0VRxwCvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22FCCB51CC53470DD0729F1E69B0C48DF34D8DAD2375C65E2F123895953B7C4A)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.resume](../interface-avrecorder/document.md#resume9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Example**

audioRecorder.on('resume', () => {    // Set the 'resume' event callback.
  console.info('audio recorder resume called');
});
audioRecorder.resume();

#### stop(deprecated)

stop(): void

Stops audio recording.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/u03DGXztQkKRLRiZpkQ1sA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3402CCE9BF8DF01EDAD5F0D9BF1B8BEB714E7B6D31974B4CE914C94D6EDC4BA5)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.stop](../interface-avrecorder/document.md#stop9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Example**

audioRecorder.on('stop', () => {    // Set the 'stop' event callback.
  console.info('audio recorder stop called');
});
audioRecorder.stop();

#### release(deprecated)

release(): void

Releases the audio recording resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Vegs4EklQSe4Uo8NI944ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2FB28AF33404C766341DD43AE1EDCA9C620996BE8373B637767D388F0704489)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.release](../interface-avrecorder/document.md#release9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Example**

audioRecorder.on('release', () => {    // Set the 'release' event callback.
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;

#### reset(deprecated)

reset(): void

Resets audio recording.

Before resetting audio recording, you must call **stop()** to stop recording. After audio recording is reset, you must call **prepare()** to set the recording configurations for another recording.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ghFuYMqfR_qDTXBOI9dLUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61CAA3DCB49870A1C8992F5E833B9C0895711C33E82A9A33C3063A4B8DA59EF7)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.reset](../interface-avrecorder/document.md#reset9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Example**

audioRecorder.on('reset', () => {    // Set the 'reset' event callback.
  console.info('audio recorder reset called');
});
audioRecorder.reset();

#### on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')(deprecated)

on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void

Subscribes to the audio recording events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ROMu56Q9Qz-al_9UJQgPlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51425123E49BCFA6A19165AD48A87C4C9E7AAB295D58C9917E6DF5476EF48B7E)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.on('stateChange')](../interface-avrecorder/document.md#onstatechange9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The following events are supported: 'prepare'|'start'| 'pause' | 'resume' |'stop'|'release'|'reset'

\- 'prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.

\- 'start': triggered when the **start()** API is called and audio recording starts.

\- 'pause': triggered when the **pause()** API is called and audio recording is paused.

\- 'resume': triggered when the **resume()** API is called and audio recording is resumed.

\- 'stop': triggered when the **stop()** API is called and audio recording stops.

\- 'release': triggered when the **release()** API is called and the recording resources are released.

\- 'reset': triggered when the **reset()** API is called and audio recording is reset.

 |
| callback | ()=>void | Yes | Callback invoked when the event is triggered. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorder: media.AudioRecorder = media.createAudioRecorder(); // Create an AudioRecorder instance.
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC\_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC\_ADTS,
  uri : 'fd://xx',  // The file must be created by the caller and granted with proper permissions.
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // Set the 'error' event callback.
  console.error(\`audio error called, error: ${error}\`);
});
audioRecorder.on('prepare', () => {  // Set the 'prepare' event callback.
  console.info('prepare called');
  audioRecorder.start();  // // Start recording and trigger the 'start' event callback.
});
audioRecorder.on('start', () => {  // Set the 'start' event callback.
  console.info('audio recorder start called');
});
audioRecorder.on('pause', () => {  // Set the 'pause' event callback.
  console.info('audio recorder pause called');
});
audioRecorder.on('resume', () => {  // Set the 'resume' event callback.
  console.info('audio recorder resume called');
});
audioRecorder.on('stop', () => {  // Set the 'stop' event callback.
  console.info('audio recorder stop called');
});
audioRecorder.on('release', () => {  // Set the 'release' event callback.
  console.info('audio recorder release called');
});
audioRecorder.on('reset', () => {  // Set the 'reset' event callback.
  console.info('audio recorder reset called');
});
audioRecorder.prepare(audioRecorderConfig)  // Set recording parameters and trigger the 'prepare' event callback.

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

Subscribes to audio recording error events. After an error event is reported, you must handle the event and exit the recording.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/zK7lbyaISNaC-kSxSJwWJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=044F054333FC0E68103CDDC0DFFBF6A3974C258ED2F78F94E2A911BD0AA56B1A)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [AVRecorder.on('error')](../interface-avrecorder/document.md#onerror9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'error'** in this case.

This event is triggered when an error occurs during audio recording.

 |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback invoked when the event is triggered. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC\_LC,
  audioEncodeBitRate : 22050,
  audioSampleRate : 22050,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC\_ADTS,
  uri : 'fd://xx',   // The file must be created by the caller and granted with proper permissions.
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // Set the 'error' event callback.
  console.error(\`audio error called, error: ${error}\`);
});
audioRecorder.prepare(audioRecorderConfig);  // Do not set any parameter in prepare and trigger the 'error' event callback.
