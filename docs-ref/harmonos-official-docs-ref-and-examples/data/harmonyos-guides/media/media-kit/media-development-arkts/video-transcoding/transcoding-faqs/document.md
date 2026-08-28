# Transcoding FAQs

#### Why does the audio encoding format change when the application sends a video for transcoding?

If the audio track format is not specified during transcoding, the system converts it to AAC by default.

#### Does transcoding support conversion from HDR to SDR? Why does transcoding HDR videos recorded by devices using other systems fail?

Currently, only conversion from HDR Vivid to SDR is supported. Other HDR formats are not supported. You can call OH\_VideoProcessing\_IsColorSpaceConversionSupported to check whether the current device supports this feature. For details, see [VPE specifications](../../../video-processing/video-color-space-conversion/document.md#section181315199120).

#### Why do I still get a parameter error when setting the target video resolution according to the aspect ratio of the source video?

Check whether the target video resolution is below 240p. The width and height of the target video should not exceed those of the source video and should not be odd numbers.

For details about how to set the video resolution, see [Setting the Correct Video Width and Height](../../../../avcodec-kit/audio-and-video-codecs/obtaining-supported-codecs/document.md#setting-the-correct-video-width-and-height).

#### Why does the transcoded video file size increase even though the target resolution is lower than the source video resolution?

If the video bit rate is not specified, the system uses the default target bit rate, which is higher than the bit rate of the source video. This results in a larger file size for the transcoded video.

#### Why does the video change from landscape to portrait after transcoding, even though the source video is landscape?

The source video has a 90° rotation angle. The displayed image accounts for this rotation, making the video appear landscape to the user. Therefore, the target resolution is set with a width greater than height. After transcoding, the resulting video, when accounting for the rotation angle, has a width smaller than its height, therefore appearing portrait. It is recommended that you obtain the video's width and height through metadata and set the target resolution accordingly.

#### What should I do if the transcoding capabilities provided by the system fail to be called?

1.  Check whether the current transcoding system supports the video and the target video format settings.
    
    Topics describing the transcoding capabilities: [AVTranscoder](../../../about-this-kit/document.md#avtranscoder), [AVCodec Supported Formats](../../../../avcodec-kit/avcodec-supported-formats/document.md), [VPE specifications](../../../video-processing/video-color-space-conversion/document.md#section181315199120)
    
2.  When receiving an error event, the application should send the source video. When receiving a complete event, the application first calls **release** before performing operations such as sending or uploading the transcoded video.
