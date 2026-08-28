# Deprecated Interface (VideoPlayer, deprecated)

VideoPlayer is a class for video playback management. It provides APIs to manage and play videos. Before calling any API in VideoPlayer, you must use [createVideoPlayer()](../functions/document.md#mediacreatevideoplayerdeprecated) to create a VideoPlayer instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/nb4UO599Sy6k8ahKOBnZzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CE2D54D4A8898FE2A0CD0375291115A0F2ED6960A3D95780D610CA5799C3295)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer](../interface-avplayer/document.md) instead.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url8+ | string | No | No | 
Video URL. The video formats MP4, MPEG-TS, and MKV are supported.

**Example of supported URLs**:

1\. FD: fd://xx

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/mwPd7t3SQ1yRpB_Nh_-_Ww/en-us_image_0000002568686121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C099CED04104F08983485C5062E0916C7015CFE947250EAE774A023F60A677B6)

2\. HTTP: http://xx

3\. HTTPS: https://xx

4\. HLS: http://xx or https://xx

5\. File type: file://xx

**NOTE**

WebM is no longer supported since API version 11.

 |
| fdSrc9+ | [AVFileDescriptor](../interfaces-others/document.md#avfiledescriptor9) | No | No | 

Description of a video file. This property is required when video assets of an application are continuously stored in a file.

**Example:**

Assume that a music file that stores continuous music assets consists of the following:

Video 1 (address offset: 0, byte length: 100)

Video 2 (address offset: 101; byte length: 50)

Video 3 (address offset: 151, byte length: 150)

1\. To play video 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }

2\. To play video 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }

3\. To play video 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }

To play an independent video file, use **src=fd://xx**.

 |
| loop8+ | boolean | No | No | Whether to loop video playback. **true** to loop, **false** otherwise. |
| videoScaleType9+ | [VideoScaleType](../enums/document.md#videoscaletype9) | No | Yes | Video scale type. The default value is **VIDEO\_SCALE\_TYPE\_FIT**. |
| audioInterruptMode9+ | [audio.InterruptMode](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/enums/document.md#interruptmode9) | No | Yes | Audio interruption mode. |
| currentTime8+ | number | Yes | No | Current video playback position, in ms. |
| duration8+ | number | Yes | No | Video duration, in ms. The value **\-1** indicates the live mode. |
| state8+ | [VideoPlayState](../types/document.md#videoplaystatedeprecated) | Yes | No | Video playback state. |
| width8+ | number | Yes | No | Video width, in px. |
| height8+ | number | Yes | No | Video height, in px. |

#### setDisplaySurface(deprecated)

setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void

Sets a surface ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/VNsN3zr7QhqqqNz76rDGCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=876731E39B33E282956614507D0A1CC4392458B8EEA24F66EE380B4229EE0FC5)

-   **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must be set for video streams without audio. Otherwise, the calling of **prepare** fails.
    
-   This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.surfaceId](../interface-avplayer/document.md#properties) instead.
    

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which is obtained from the **XComponent**. For details about how to obtain it, see [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set DisplaySurface!');
  } else {
    console.info('Succeeded in setting DisplaySurface!');
  }
});

#### setDisplaySurface(deprecated)

setDisplaySurface(surfaceId: string): Promise<void>

Sets a surface ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ZYCsZGCaR9Wp7NM6eKOhOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC66F28B55EED608A569ABEA9E4B84B1E687FB3A73B6B8B936A14B704CC569CA)

-   **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must be set for video streams without audio. Otherwise, the calling of **prepare** fails.
    
-   This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.surfaceId](../interface-avplayer/document.md#properties) instead.
    

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which is obtained from the **XComponent**. For details about how to obtain it, see [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId).then(() => {
  console.info('Succeeded in setting DisplaySurface');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### prepare(deprecated)

prepare(callback: AsyncCallback<void>): void

Prepares for video playback. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/TK1mxc0-TBGIWttmKLTCvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC5AD9F88E34006711838AA084CEBEBEF33FD5F032CEF697D9D8B1F081FFA39E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.prepare](../interface-avplayer/document.md#prepare9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare((err: BusinessError) => {
  if (err) {
    console.error('Failed to prepare!');
  } else {
    console.info('Succeeded in preparing!');
  }
});

#### prepare(deprecated)

prepare(): Promise<void>

Prepares for video playback. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Ex_RLxpETMm3G87fLjUyUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF80452D828D9FBE19327D11358F41F4DE4829796ABF600479389EACE0426ABB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.prepare](../interface-avplayer/document.md#prepare9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare().then(() => {
  console.info('Succeeded in preparing');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### play(deprecated)

play(callback: AsyncCallback<void>): void

Starts video playback. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/4hgzt22QQui_DVHI5JW_qQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76AD41B176CA8B6B78806454144B0CD053EB9069B679B1F47FDD55226BA96E1F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.play](../interface-avplayer/document.md#play9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play((err: BusinessError) => {
  if (err) {
    console.error('Failed to play!');
  } else {
    console.info('Succeeded in playing!');
  }
});

#### play(deprecated)

play(): Promise<void>

Starts video playback. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/9iYS2PP6RgKuTNK319sHLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B6ACAA02DDD8B26A99FDE7C259FF287A8AAB9B89681F45A2D95C191BDC2C5B3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.play](../interface-avplayer/document.md#play9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play().then(() => {
  console.info('Succeeded in playing');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### pause(deprecated)

pause(callback: AsyncCallback<void>): void

Pauses video playback. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2Z3Uw3Q-R7eot9fToOy-0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0A5438C7506952FF6AF395637B783F0D75FB717E1491D1E0ECFF91B8DBF4F61)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.pause](../interface-avplayer/document.md#pause9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause((err: BusinessError) => {
  if (err) {
    console.error('Failed to pause!');
  } else {
    console.info('Succeeded in pausing!');
  }
});

#### pause(deprecated)

pause(): Promise<void>

Pauses video playback. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LKU9z8i2T-2lXcldQob5jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85EF539E58D95D4DD9E6B639B01BDD33BCF00E8EEA8CF883622674C3CCE332E4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.pause](../interface-avplayer/document.md#pause9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### stop(deprecated)

stop(callback: AsyncCallback<void>): void

Stops video playback. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/G-nlOyBMRnmf_ZWcXDoi2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E1B6325BE356643E8C66A69D87EB51BDDF76CC5FACDFB1097C2E10AD3C92C91)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.stop](../interface-avplayer/document.md#stop9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop((err: BusinessError) => {
  if (err) {
    console.error('Failed to stop!');
  } else {
    console.info('Succeeded in stopping!');
  }
});

#### stop(deprecated)

stop(): Promise<void>

Stops video playback. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/dRvKLvSmQBWQbhY_Bi5_Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8555AD4C558BAFA55212C6659DB2E35F53C712B738EFB51410641065C976FCF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.stop](../interface-avplayer/document.md#stop9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop().then(() => {
  console.info('Succeeded in stopping');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### reset(deprecated)

reset(callback: AsyncCallback<void>): void

Resets video playback. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/MkyuCUCKRjSimmEirRALYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B92450F530896F03A8B50B4D29D46816039F3E9C730752D652A12421460DFC6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.reset](../interface-avplayer/document.md#reset9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset((err: BusinessError) => {
  if (err) {
    console.error('Failed to reset!');
  } else {
    console.info('Succeeded in resetting!');
  }
});

#### reset(deprecated)

reset(): Promise<void>

Resets video playback. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/6G2kGBvUQpuHuY5kB9PaeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3096F4F2ECB8493A13A63A5FD294D92CB35A47A72EB338589A3320533DE64230)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.reset](../interface-avplayer/document.md#reset9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset().then(() => {
  console.info('Succeeded in resetting');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### seek(deprecated)

seek(timeMs: number, callback: AsyncCallback<number>): void

Seeks to the specified playback position. The previous key frame at the specified position is played. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/zZXk1QfcSh2R9WeyG65ZJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41CCFA52C32FF09277F11D74837EA573D6792A36F6778C303537E384F30B6CA7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.seek](../interface-avplayer/document.md#seek9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is \[0, duration\]. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the new playback position; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(\`Failed to create VideoPlayer, error:${error}\`);
  }
});

let seekTime: number = 5000;
videoPlayer.seek(seekTime, (err: BusinessError, result: number) => {
  if (err) {
    console.error('Failed to do seek!');
  } else {
    console.info('Succeeded in doing seek!');
  }
});

#### seek(deprecated)

seek(timeMs: number, mode:SeekMode, callback: AsyncCallback<number>): void

Seeks to the specified playback position. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/NBphGFbBSIW7fUztNWwTHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08F86DE37DA570C082F8A81DD9AF4014C3E961613830188486ACF51B15BA10A6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.seek](../interface-avplayer/document.md#seek9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is \[0, duration\]. |
| mode | [SeekMode](../enums/document.md#seekmode8) | Yes | Seek mode. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the new playback position; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(\`Failed to create VideoPlayer, error:${error}\`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK\_NEXT\_SYNC, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to do seek!');
    } else {
      console.info('Succeeded in doing seek!');
    }
  });
}

#### seek(deprecated)

seek(timeMs: number, mode?:SeekMode): Promise<number>

Seeks to the specified playback position. If **mode** is not specified, the previous key frame at the specified position is played. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/6gUN2GjRSQGhqRuhe9W2pA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BB9BDE44DCE8F7903DBBD624E7DB033C75CEBDEB82010221F65DD4DFF162427)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.seek](../interface-avplayer/document.md#seek9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is \[0, duration\]. |
| mode | [SeekMode](../enums/document.md#seekmode8) | No | Seek mode based on the video I frame. The default value is **SEEK\_PREV\_SYNC**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the playback position, in ms. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(\`Failed to create VideoPlayer, error:${error}\`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime).then((seekDoneTime: number) => { // seekDoneTime indicates the position after the seek operation is complete.
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(\`video catchCallback, error:${error}\`);
  });

  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK\_NEXT\_SYNC).then((seekDoneTime: number) => {
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(\`video catchCallback, error:${error}\`);
  });
}

#### setVolume(deprecated)

setVolume(vol: number, callback: AsyncCallback<void>): void

Sets the volume. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/NuhtX4D8SwCOymMhoL0qoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=169734C07D69CF7D42AB781D7C329FB5E02A07C6F2E1095DE7572E76A1577BD2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.setVolume](../interface-avplayer/document.md#setvolume9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vol | number | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set Volume!');
  } else {
    console.info('Succeeded in setting Volume!');
  }
});

#### setVolume(deprecated)

setVolume(vol: number): Promise<void>

Sets the volume. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/76H7KchyQTG03E1CQVUOvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C8D09E021EDA87FB803C037A941D8BE4F9B9DF6C79C097B6A86645E814AA113)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.setVolume](../interface-avplayer/document.md#setvolume9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vol | number | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol).then(() => {
  console.info('Succeeded in setting Volume');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### release(deprecated)

release(callback: AsyncCallback<void>): void

Releases the video playback resources. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/TSON18TcQryaGb3Eio5ngA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E1910093C50F53FC2D9B79A063EF8BBD652CF7DD90C7EE0CA38BCC2DED7639C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.release](../interface-avplayer/document.md#release9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});

#### release(deprecated)

release(): Promise<void>

Releases the video playback resources. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/OBonH0UVTFGmM4OSdUnkYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5034A0472ACAC243BF907DD5D1261A6818B63B164D31446D2729BF8F4406FCA7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.release](../interface-avplayer/document.md#release9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### getTrackDescription(deprecated)

getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void

Obtains the video track information. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/CsGglR7AQqyDMxG_qTckkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD3EB3A7AD8FB4B33B6F57C3FAD6355232D97C38393210C91135660A6825FBCF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.getTrackDescription](../interface-avplayer/document.md#gettrackdescription9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[MediaDescription](../interfaces-others/document.md#mediadescription8)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if ((arrList) != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error(\`Failed to get TrackDescription, error:${error}\`);
  }
});

#### getTrackDescription(deprecated)

getTrackDescription(): Promise<Array<MediaDescription>>

Obtains the video track information. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/5Lv914w9SZy-Zj0dqESL2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5EEEBC4A92A4C10061B3CEFEF7174136306A2E55E649AFF982A14C2D07DCAAD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.getTrackDescription](../interface-avplayer/document.md#gettrackdescription9-1) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[MediaDescription](../interfaces-others/document.md#mediadescription8)\>> | Promise used to return the MediaDescription array that holds the video track information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error('Failed to get TrackDescription');
  }
}).catch((error: BusinessError) => {
  console.error(\`video catchCallback, error:${error}\`);
});

#### setSpeed(deprecated)

setSpeed(speed: number, callback: AsyncCallback<number>): void

Sets the playback speed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/YcgZr6JcT9ms0bFcZi2ULA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59CF33BB0ADF6666FE634EA9CC26DA4FD765CE4A0965C265E2E794B58685AAEC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.setSpeed](../interface-avplayer/document.md#setspeed9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | number | Yes | Video playback speed. For details, see [PlaybackSpeed](../enums/document.md#playbackspeed8). |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the playback speed; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(\`Failed to create VideoPlayer, error:${error}\`);
  }
});
let speed = media.PlaybackSpeed.SPEED\_FORWARD\_2\_00\_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to set Speed!');
    } else {
      console.info('Succeeded in setting Speed!');
    }
  });
}

#### setSpeed(deprecated)

setSpeed(speed: number): Promise<number>

Sets the playback speed. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/LO6CmgMcSq-76XVVbUG3tg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36664BA1CF3F9E95EE9F4F493962E89A587D9F8BDD6D919C19F9FCF95A93A1B7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.setSpeed](../interface-avplayer/document.md#setspeed9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | number | Yes | Video playback speed. For details, see [PlaybackSpeed](../enums/document.md#playbackspeed8). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the playback speed. For details, see [PlaybackSpeed](../enums/document.md#playbackspeed8). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(\`Failed to create VideoPlayer, error:${error}\`);
  }
});
let speed = media.PlaybackSpeed.SPEED\_FORWARD\_2\_00\_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed).then((result: number) => {
    console.info('Succeeded in setting Speed');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to set Speed, error:${error}\`);// todo:: error.
  });
}

#### on('playbackCompleted')(deprecated)

on(type: 'playbackCompleted', callback: Callback<void>): void

Subscribes to the video playback completion event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/hbWSxvEzSByerlm1h8sXXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7B506ABC2AAF601BED46CE8B0015C1FB862E39494139EF7E973CC6A5B2A0B04)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.on('stateChange')](../interface-avplayer/document.md#onstatechange9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'playbackCompleted'** in this case. |
| callback | Callback<void> | Yes | Callback invoked when the event is triggered. |

**Example**

videoPlayer.on('playbackCompleted', () => {
  console.info('playbackCompleted called!');
});

#### on('bufferingUpdate')(deprecated)

on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void

Subscribes to the video buffering update event. This API works only under online playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/EvGWw8TyT8qdw3amIWYsOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA0962D6B9C9B194C67ADE1610DAA5204B3E575641BAADC5A0AF68A9EA9681EA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.on('bufferingUpdate')](../interface-avplayer/document.md#onbufferingupdate9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'bufferingUpdate'** in this case. |
| callback | function | Yes | 
Callback invoked when the event is triggered.

The value of [BufferingInfoType](../enums/document.md#bufferinginfotype8) is fixed at **0**.

 |

**Example**

videoPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
  console.info('video bufferingInfo type: ' + infoType);
  console.info('video bufferingInfo value: ' + value);
});

#### on('startRenderFrame')(deprecated)

on(type: 'startRenderFrame', callback: Callback<void>): void

Subscribes to the frame rendering start event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/lsaI4SnASeSzJV_T664hdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77262B9709261058B7C92E146F04D45403707D7D5B634934F56454E2ED56D6F4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.on('startRenderFrame')](../interface-avplayer/document.md#onstartrenderframe9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'startRenderFrame'** in this case. |
| callback | Callback<void> | Yes | Callback invoked when the event is triggered. |

**Example**

videoPlayer.on('startRenderFrame', () => {
  console.info('startRenderFrame called!');
});

#### on('videoSizeChanged')(deprecated)

on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void

Subscribes to the video width and height change event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/uv3rfrRUSbCcqz7220mlyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15296D9B6E67C9D366547D673315076B523F6487985DD46EDF5AFCED86E8DAAB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.on('videoSizeChange')](../interface-avplayer/document.md#onvideosizechange9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'videoSizeChanged'** in this case. |
| callback | function | Yes | Callback invoked when the event is triggered. **width** indicates the video width, and **height** indicates the video height. |

**Example**

videoPlayer.on('videoSizeChanged', (width: number, height: number) => {
  console.info('video width is: ' + width);
  console.info('video height is: ' + height);
});

#### on('audioInterrupt')(deprecated)

on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void

Subscribes to the audio interruption event. For details, see [audio.InterruptEvent](../../../../audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interfaces-others/document.md#interruptevent9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/r0uY_qZyQuax8oQBpGObmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7433F548B0B7161C3ACF0A1F5064026F62C39914305FD7760D5C6F67F06EC063)

This API is supported since API version 9 and deprecated since API version 9. You are advised to use [AVPlayer.on('audioInterrupt')](../interface-avplayer/document.md#onaudiointerrupt9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'audioInterrupt'** in this case. |
| callback | function | Yes | Callback invoked when the event is triggered. |

**Example**

import { audio } from '@kit.AudioKit';

videoPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
  console.info('audioInterrupt called,and InterruptEvent info is:' + info);
});

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

Subscribes to video playback error events. After an error event is reported, you must handle the event and exit the playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/-6_g79_jSeCZ8CCPF1x_Kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062438Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C9F15155C72E7A2F14B5AE29649392CF265CADAC528D768B5318E91643A09A0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [AVPlayer.on('error')](../interface-avplayer/document.md#onerror9) instead.

**System capability**: SystemCapability.Multimedia.Media.VideoPlayer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'error'** in this case.

This event is triggered when an error occurs during video playback.

 |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback invoked when the event is triggered. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.on('error', (error: BusinessError) => {  // Set the 'error' event callback.
  console.error(\`video error called, error: ${error}\`);
});
videoPlayer.url = 'fd://error';  // Set an incorrect URL to trigger the 'error' event.
