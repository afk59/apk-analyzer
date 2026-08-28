# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/s2enQz4RQmKFefkSOpLPKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CF130D3E3849179507170AA8B04FCEAEE1757EEECD6654A57D2E3A9A38EC064)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### media.createAVPlayer9+

createAVPlayer(callback: AsyncCallback<AVPlayer>): void

Creates an AVPlayer instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/FcYhkM9LRgWDrCR5ys1rsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=179CEFA1FA4FA8CD536C0C70BE6568ACE100A4B1AE8D5171AACF417426BB1137)

-   You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video playback scenarios.
-   Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the system might terminate applications to free up resources.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVPlayer](../interface-avplayer/document.md)\> | Yes | Callback used to return the result. If the operation is successful, an AVPlayer instance is returned; otherwise, **null** is returned. The instance can be used to play audio and video. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer;
media.createAVPlayer((error: BusinessError, video: media.AVPlayer) => {
  if (video) {
    avPlayer = video;
    console.info('Succeeded in creating AVPlayer');
  } else {
    console.error(\`Failed to create AVPlayer, error message:${error.message}\`);
  }
});

#### media.createAVPlayer9+

createAVPlayer(): Promise<AVPlayer>

Creates an AVPlayer instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/HnyPmvZXThKoneJ-9_Eg9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D09E11D96051E8B79E0B51EEE5A54F1640CB6208121C422FA4D6ACCD61EBFE43)

-   You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video playback scenarios.
-   Applications should reasonably use AVPlayer objects in accordance with actual service requirements, create them on demand, and release them in a timely manner. This avoids excessive memory consumption caused by holding too many AVPlayer instances, which may result in the system terminating the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVPlayer](../interface-avplayer/document.md)\> | Promise used to return the result. If the operation is successful, an AVPlayer instance is returned for audio and video playback. Otherwise, **null** is returned. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer;
media.createAVPlayer().then((video: media.AVPlayer) => {
  if (video) {
    avPlayer = video;
    console.info('Succeeded in creating AVPlayer');
  } else {
    console.error('Failed to create AVPlayer');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to create AVPlayer, error message:${error.message}\`);
});

#### media.createAVRecorder9+

createAVRecorder(callback: AsyncCallback<AVRecorder>): void

Creates an AVRecorder instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/FjnaTpFpSCOPjnAibAnN_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22E262A33BA2A98FF6779AC01A37A2B58A524232454148F2E71526AA5301DFBC)

An application can create multiple AVRecorder instances. However, because the device shares a common audio channel, only one instance can record audio at a time. Any attempt to create the second instance for audio recording fails due to audio channel conflicts.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVRecorder](../interface-avrecorder/document.md)\> | Yes | Callback function, which returns an **AVRecorder** instance for recording audio and video. Otherwise, **null** is returned. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let avRecorder: media.AVRecorder;

media.createAVRecorder((error: BusinessError, recorder: media.AVRecorder) => {
  if (recorder) {
    avRecorder = recorder;
    console.info('Succeeded in creating AVRecorder');
  } else {
    console.error(\`Failed to create AVRecorder, error message:${error.message}\`);
  }
});

#### media.createAVRecorder9+

createAVRecorder(): Promise<AVRecorder>

Creates an AVRecorder instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/6f6jNJMPTdCn0OUsJszxvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F192673A9FB858F31A14005B29420271AADFA30BAE1C6C6F8581BB681DF7F43)

An application can create multiple AVRecorder instances. However, because the device shares a common audio channel, only one instance can record audio at a time. Any attempt to create the second instance for audio recording fails due to audio channel conflicts.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVRecorder](../interface-avrecorder/document.md)\> | Promise used to return an **AVRecorder** instance, which can be used to record audio and video. Otherwise, **null** is returned. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let avRecorder: media.AVRecorder;
media.createAVRecorder().then((recorder: media.AVRecorder) => {
  if (recorder) {
    avRecorder = recorder;
    console.info('Succeeded in creating AVRecorder');
  } else {
    console.error('Failed to create AVRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to create AVRecorder, error message:${error.message}\`);
});

#### media.createAVTranscoder12+

createAVTranscoder(): Promise<AVTranscoder>

Creates an AVTranscoder instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/t7ZBFn5MRYazhTzdqmQf7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30A066FBC3BB4436012D7B04C71C59F8DDF1E4F8BD06EE9A11309DCB129114D5)

A maximum of 2 AVTranscoder instances can be created.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVTranscoder](../interface-avtranscoder/document.md)\> | Promise used to return the result. If the operation is successful, an AVTranscoder instance is returned; otherwise, **null** is returned. The instance can be used for video transcoding. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avTranscoder: media.AVTranscoder | undefined = undefined;
media.createAVTranscoder().then((transcoder: media.AVTranscoder) => {
  if (transcoder) {
    avTranscoder = transcoder;
    console.info('Succeeded in creating AVTranscoder');
  } else {
    console.error('Failed to create AVTranscoder');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to create AVTranscoder, error message:${error.message}\`);
});

#### media.createAVMetadataExtractor11+

createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void

Creates an AVMetadataExtractor instance. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVMetadataExtractor](../interface-avmetadataextractor/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the AVMetadataExtractor instance created; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Returned by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(\`Failed to create AVMetadataExtractor, error message:${error.message}\`);
  }
});

#### media.createAVMetadataExtractor11+

createAVMetadataExtractor(): Promise<AVMetadataExtractor>

Creates an AVMetadataExtractor instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVMetadataExtractor](../interface-avmetadataextractor/document.md)\> | Promise used to return the AVMetadataExtractor instance. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor().then((extractor: media.AVMetadataExtractor) => {
  if (extractor) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(\`Failed to create AVMetadataExtractor\`);
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to create AVMetadataExtractor, error message:${error.message}\`);
});

#### media.createSoundPool10+

createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo, callback: AsyncCallback<SoundPool>): void

Creates a SoundPool instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/AdYQ7ZfTQliIQezxQNK_1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=929EE48D57D12E5D934D2C41301C3F3635C7159AD937A4E914B4B87D89DB151F)

-   In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode. Therefore, an application process can create only one SoundPool instance.
-   In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore, an application process can create a maximum of 128 SoundPool instances.

**System capability**: SystemCapability.Multimedia.Media.SoundPool

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| maxStreams | number | Yes | Maximum number of streams that can be played by the SoundPool instance. The value is an integer ranging from 1 to 32. |
| audioRenderInfo | [audio.AudioRendererInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiorendererinfo8) | Yes | Audio renderer parameters. When the **usage** parameter in **audioRenderInfo** is set to **STREAM\_USAGE\_UNKNOWN**, **STREAM\_USAGE\_MUSIC**, **STREAM\_USAGE\_MOVIE**, or **STREAM\_USAGE\_AUDIOBOOK**, the SoundPool uses the audio mixing mode when playing a short sound, without interrupting the playback of other audios. SoundPool supports setting **rendererFlags** to **1** for low-latency playback. |
| callback | AsyncCallback<[SoundPool](../../multimedia/soundpool-sound-pool/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a SoundPool instance is returned; otherwise, **null** is returned. The instance is used for loading and playback. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by callback. |

**Example**

import { audio } from '@kit.AudioKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM\_USAGE\_MUSIC,
  rendererFlags : 0
};

media.createSoundPool(5, audioRendererInfo, (error, soundPool\_: media.SoundPool) => {
  if (error) {
    console.error(\`Failed to createSoundPool\`);
    return;
  } else {
    soundPool = soundPool\_;
    console.info(\`Succeeded in createSoundPool\`);
  }
});

#### media.createSoundPool10+

createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>

Creates a SoundPool instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/sKAfzG6rSvmuOpqlkqc3jA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D28238C47407E8FD0C5624ACB0500E50F0C91FB90CE90D49E666CEAF9DE5A86)

-   In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode. Therefore, an application process can create only one SoundPool instance.
-   In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore, an application process can create a maximum of 128 SoundPool instances.

**System capability**: SystemCapability.Multimedia.Media.SoundPool

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| maxStreams | number | Yes | Maximum number of streams that can be played by the SoundPool instance. The value is an integer ranging from 1 to 32. |
| audioRenderInfo | [audio.AudioRendererInfo](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#audiorendererinfo8) | Yes | Audio renderer parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SoundPool](../../multimedia/soundpool-sound-pool/document.md)\> | Promise used to return the result. If the operation is successful, a SoundPool instance is returned; otherwise, **null** is returned. The instance is used for loading and playback. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by promise. |

**Example**

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM\_USAGE\_MUSIC,
  rendererFlags : 0
};

media.createSoundPool(5, audioRendererInfo).then((soundpool\_: media.SoundPool) => {
  if (soundpool\_) {
    soundPool = soundpool\_;
    console.info('Succeeded in creating SoundPool');
  } else {
    console.error('Failed to create SoundPool');
  }
}, (error: BusinessError) => {
  console.error(\`soundpool catchCallback, error message:${error.message}\`);
});

#### media.createAVScreenCaptureRecorder12+

createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>

Creates an AVScreenCaptureRecorder instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVScreenCaptureRecorder](../interface-avscreencapturerecorder/document.md)\> | Promise used to return the result. If the operation is successful, an AVScreenCaptureRecorder instance is returned; otherwise, **null** is returned. The instance can be used for screen capture. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avScreenCaptureRecorder: media.AVScreenCaptureRecorder;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in createAVScreenCaptureRecorder');
  } else {
    console.error('Failed to createAVScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

#### media.createAVImageGenerator12+

createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void

Creates an AVImageGenerator instance. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVImageGenerator](../interface-avimagegenerator/document.md)\> | Yes | Callback used to return the result. If the operation is successful, an AVImageGenerator instance is returned; otherwise, **null** is returned. The API can be used to obtain a video thumbnail. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Returned by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator((error: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error(\`Failed to create AVImageGenerator, error message:${error.message}\`);
  }
});

#### media.createAVImageGenerator12+

createAVImageGenerator(): Promise<AVImageGenerator>

Creates an AVImageGenerator instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVImageGenerator](../interface-avimagegenerator/document.md)\> | Promise used to return the result. If the operation is successful, an AVImageGenerator instance is returned; otherwise, **null** is returned. The API can be used to obtain a video thumbnail. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400101 | No memory. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator().then((generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error('Failed to create AVImageGenerator');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to create AVImageGenerator, error message:${error.message}\`);
});

#### media.createMediaSourceWithUrl12+

createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource

Creates a media source for streaming media to be pre-downloaded.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | 
\- URL of the media source. The following streaming media formats are supported: HLS, HTTP-FLV, DASH, and HTTPS.

\- FD path of the local M3U8 file.

 |
| headers | Record<string, string> | No | HTTP header customized for streaming media pre-download. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaSource](../interface-mediasource/document.md) | MediaSource instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400101 | No memory. |

**Example 1**

let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);

**Example 2**

import { media } from "@kit.MediaKit";

async function test(context: Context){
    // this.getUIContext().getHostContext();
    let mgr = context?.resourceManager;
    if (!mgr) {
        return;
    }
    let fileDescriptor = await mgr.getRawFd("xxx.m3u8");

    let fd: string = fileDescriptor.fd.toString();
    let offset: string = fileDescriptor.offset.toString();
    let length: string = fileDescriptor.length.toString();
    let fdUrl: string = "fd://" + fd + "?offset=" + offset + "&size=" + length;

    let mediaSource: media.MediaSource = media.createMediaSourceWithUrl(fdUrl);
}

#### media.createMediaSourceWithStreamData19+

createMediaSourceWithStreamData(streams: Array<MediaStream>): MediaSource

Creates a multi-bitrate media source for streaming media. Currently, only the HTTP-FLV multi-bitrate media source is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| streams | Array<[MediaStream](../interfaces-others/document.md#mediastream19)\> | Yes | Array of MediaStream objects. The supported streaming media format is HTTP-FLV. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaSource](../interface-mediasource/document.md) | MediaSource instance. |

**Example**

let streams : Array<media.MediaStream> = \[\];
streams.push({url: "http://xxx/480p.flv", width: 854, height: 480, bitrate: 800000});
streams.push({url: "http://xxx/720p.flv", width: 1280, height: 720, bitrate: 2000000});
streams.push({url: "http://xxx/1080p.flv", width: 1920, height: 1080, bitrate: 2000000});
let mediaSource : media.MediaSource = media.createMediaSourceWithStreamData(streams);

#### media.createAudioPlayer(deprecated)

createAudioPlayer(): AudioPlayer

Creates an AudioPlayer instance in synchronous mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/DlQv2kYpSomv65Ke7GZwWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F46985FA39CDF11AA1FFBB0B30EA3F0A4A2BEDA9D5A4856DF760897727E8F6C8)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [createAVPlayer](#mediacreateavplayer9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioPlayer](../deprecated-interface-audioplayer-deprecated/document.md) | If the operation is successful, an AudioPlayer instance is returned; otherwise, **null** is returned. After the instance is created, you can start, pause, or stop audio playback. |

**Example**

let audioPlayer: media.AudioPlayer = media.createAudioPlayer();

#### media.createVideoPlayer(deprecated)

createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void

Creates a **VideoPlayer** instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ThFJ89X3Qx6MFAVcZfvotw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=276620F9928E61DD50FC14F6F5B2C9C832AA8EDA88ED08FF7A9A943F3F41A3DF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [createAVPlayer](#mediacreateavplayer9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[VideoPlayer](../deprecated-interface-videoplayer-deprecated/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the VideoPlayer instance created; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(\`Failed to create VideoPlayer, error:${error}\`);
  }
});

#### media.createVideoPlayer(deprecated)

createVideoPlayer(): Promise<VideoPlayer>

Creates a VideoPlayer instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/vIZcGoVjQaGQmlXhadPc4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEBB76D07E2A2FBBA679A771074E91CF23D34101A6499FD554092E66EE0463A5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [createAVPlayer](#mediacreateavplayer9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[VideoPlayer](../deprecated-interface-videoplayer-deprecated/document.md)\> | Promise used to return the result. If the operation is successful, a VideoPlayer instance is returned; otherwise, **null** is returned. The instance can be used to manage and play video. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer().then((video: media.VideoPlayer) => {
  if (video) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error('Failed to create VideoPlayer');
  }
}).catch((error: BusinessError) => {
  console.error(\`Failed to create VideoPlayer, error:${error}\`);
});

#### media.createAudioRecorder(deprecated)

createAudioRecorder(): AudioRecorder

Creates an AudioRecorder instance to control audio recording. Only one AudioRecorder instance can be created per device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/eDBPAhG9Q0m2JFYFnPS_Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0E7F2C8A6BAB6EA1092FC2CB0ABDC9A13AA207C88D7A25902600443A7C0CFF7)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [createAVRecorder](#mediacreateavrecorder9) instead.

**System capability**: SystemCapability.Multimedia.Media.AudioRecorder

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioRecorder](../deprecated-interface-audiorecorder-deprecated/document.md) | If the operation is successful, an AudioRecorder instance is returned; otherwise, **null** is returned. The instance can be used to record audio. |

**Example**

let audioRecorder: media.AudioRecorder = media.createAudioRecorder();
