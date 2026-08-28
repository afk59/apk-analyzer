# Low-Power Audio Playback

Starting from API version 11, low-power audio playback is available.

Low-power audio playback is an audio rendering solution that leverages software-hardware-chip synergy. It works by increasing the internal buffer of the audio renderer, allowing the system to fill a large amount of audio data at once. This enables the main processor to sleep for extended periods, reducing power consumption associated with frequent audio data processing and significantly lowering the system-level power load.

#### Prerequisites

Low-power functionality is currently supported for external speakers, wired headphones, and some Bluetooth headphones.

#### Development Guidelines

The low-power audio renderer provides the same APIs as the regular audio renderer. However, you should pay attention to the application data cycle and playback progress. For details about how to use the audio renderer, see [Using AudioRenderer for Audio Playback (ArkTs)](../using-audiorenderer-for-audio-playback-arkts/document.md) and [(Recommended) Using OHAudio for Audio Playback (C/C++)](../recommended-using-ohaudio-for-audio-playback-c-c/document.md).

**Data cycle diagram**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/io0B4lzmT2qvpinShNNqkg/en-us_image_0000002537925090.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8E36192AEAD2FF9DB26B36E4935BD4810D1F0867152DCA6AA0E8F5D5688F282)

During the data cycle, when data is quickly requested to fill the buffer, the system enters a sleep state. When the buffer data is consumed, the next cycle is triggered.

**Playback progress diagram**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/bwutWKZFRzCRzG_sZ0D5cw/en-us_image_0000002568684867.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CE4AA267F798BA5FF7352B72057F3EE848EFC5262B2523EE7CB0A6A623BE022)

During the data cycle, when data is quickly requested to fill the buffer, playback progress is calculated based on the actual playback amount. When the buffer data is consumed (for example, playback progress reaches the amount of data written), the next cycle is triggered.

## Precautions

1.  For stream types using [STREAM\_USAGE\_MUSIC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage), [STREAM\_USAGE\_AUDIOBOOK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage), [AUDIOSTREAM\_USAGE\_MUSIC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_usage), or [AUDIOSTREAM\_USAGE\_AUDIOBOOK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_usage), the low-power renderer is used by default.
    
2.  Low-power renderer buffer: up to 1000 ms in screen-on scenarios; up to 10000 ms in screen-off scenarios. The main processor is woken up when the buffer data is consumed, triggering the application to send data. The data transmission cycle is consistent with the buffer size.
    
    -   It is normal for the application not to request data within the sensing cycle. There is no need to stop the stream. The system automatically stops the stream if data is not received for a long time. When the application sends data again, the system resumes the stream.
    -   In screen-off scenarios, after the buffer is filled, the main processor enters sleep mode, and the application enters the suspended state. If the application requires background playback or screen-off playback, refer to [Development Precautions for Background Playback](../audio-playback-development/document.md#development-precautions-for-background-playback).
    -   The low-power renderer requests data of the same length as the regular renderer, filling the buffer through high request frequency. It is expected to request data every 1 ms, but the actual duration is affected by the application and hardware. If the application cannot provide data quickly, it is downgraded to the regular renderer cycle. If the regular renderer cycle cannot ensure timely data, the application needs to optimize data processing.
    -   When the application data is insufficient for one callback length, do not fill with empty data to avoid playback stuttering (except when reaching EOS). You are advised to wait for sufficient data or return an error code. For details, see [AudioRenderer Audio Data Callback](../using-audiorenderer-for-audio-playback-arkts/document.md#how-to-develop) and [OHAudio Audio Data Callback](../recommended-using-ohaudio-for-audio-playback-c-c/document.md#how-to-develop).
3.  Low-power renderers and low-latency renderers do not support concurrency, following the first-come, first-served principle, meaning the first one to start takes effect, and the later one is downgraded to a regular renderer. Specific examples are as follows:
    
    -   If low-power renderer A is started first, followed by low-power renderer B, then B is downgraded to a regular renderer.
    -   If a low-power renderer is started first, followed by a low-latency renderer, then the low-latency renderer is downgraded to a regular renderer.
    -   If a low-latency renderer is started first, followed by a low-power renderer, then the low-power renderer is downgraded to a regular renderer.
4.  Writing application data does not mean that the playback is complete. You need to call [getAudioTimestampInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#getaudiotimestampinfo19) or [OH\_AudioRenderer\_GetAudioTimestampInfo()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_getaudiotimestampinfo) to obtain the audio timestamp to determine the actual playback progress.
    
    -   You are advised to call the API for obtaining the timestamp at an interval greater than 200 ms to avoid affecting the system performance.
    -   After the application calls [flush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#flush11) or [OH\_AudioRenderer\_Flush()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_flush), the amount of data played back will be reset to 0.
    -   Due to the system frame length and latency mechanism, the amount of data played is always less than the amount of data written.
    -   You can obtain the timestamp after finishing writing data. If the timestamp obtained remains unchanged for two cycles, playback is finished. You can also estimate the remaining playback duration based on the set speed. If the estimated duration exceeds the actual duration, playback is finished. For example, let the total written data amount be p1, obtain the timestamp p2 after writing, the set speed be α where α>0, the audio sampling rate be fs where fs\>0, and the remaining playable duration be t. The formula is as follows: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/yk5ReIxQRdi7J6LDKcYVUw/en-us_image_0000002568764877.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF40D5C303ACF727B82544D0AB1E856B08C24C329F6059B49B8ABD1C40059402)
