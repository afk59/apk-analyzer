# Media Development at a Glance

HarmonyOS offers a comprehensive suite of open media capabilities, enabling you to efficiently develop popular media applications for everyday use cases, with excellent performance.

#### Media Subsystem Architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/EAVbWpZJR-2Dv5yqSSCYZg/en-us_image_0000002321659328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D69CC5563F16D07B53AC559B841DA8E0E8AB7384680A94F3951F27C7C9C6E2E "Click to enlarge")

The media subsystem provides the capability of processing users' visual and auditory information. For example, it can be used to collect, encode, store, decode, and play audio and video information. Based on the type of media information to process, the media subsystem is usually divided into different modules, including audio, video, and image modules.

For application development, the media subsystem provides APIs for developing audio/video, gallery, and camera applications. For device development, it offers adaptation and acceleration features to support various hardware chips. At the core, it provides essential media features and management mechanisms in the form of services.

-   Audio Kit: provides scenario-specific audio playback and recording APIs, helping you quickly implement high-definition audio capture and immersive playback.
-   AVCodec Kit: provides fundamental capabilities such as audio/video encoding and decoding, media file multiplexing and demultiplexing, and media data input.
-   AVSession Kit: delivers system-level control for audio and video, managing all media-related activities across the system.
-   Camera Kit: provides scenario-specific camera control APIs to implement features such as image preview, photo capture, and video recording.
-   DRM Kit: supports decryption of DRM-protected audio and video content, and offers device certificate management, license handling, and content decryption.
-   Image Kit: delivers comprehensive image processing capabilities, including decoding, encoding, editing, metadata processing, and image receiving.
-   Media Kit: provides features such as end-to-end playback of raw media resources, audio and video recording, screen capture, metadata and thumbnail extraction, and video transcoding.
-   Media Library Kit: provides the capability of managing albums and media files, including images and videos.
-   Ringtone Kit: provides the ringtone setting feature, offering users a simple, consistent, secure, and high-quality ringtone setting experience.
-   Scan Kit: offers system-level scanning capabilities for barcodes and QR codes.

#### Media Application Development Overview

## Camera Preview

Camera preview refers to the real-time display of images after the camera is activated, typically used before capturing photos or recording videos.

**Guide**

-   [Preview (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/preview-arkts/document.md)
-   [Dual-Channel Preview (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/dual-channel-preview-arkts/document.md)
-   [Dynamically Adjusting the Preview Frame Rate (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/dynamically-adjusting-the-preview-frame-rate-arkts/document.md)
-   [Adjusting Camera Rotation Angles (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/camera-rotation/adjusting-camera-rotation-angles-arkts/document.md)
-   [Preview (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/preview-c-c/document.md)
-   [Secondary Processing of Preview Streams (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/secondary-processing-of-preview-streams-c-c/document.md)
-   [Dynamically Adjusting the Preview Frame Rate (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/dynamically-adjusting-the-preview-frame-rate-c-c/document.md)

**API Reference**

-   ArkTS APIs: [camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-camera)
-   C APIs: [OH\_Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera)

**Best Practices**

-   [Solution to Screen Artifacts During Camera Preview](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-deal-stride-solution)

## Photo Capture

Photo capture is one of the most essential functions of a camera. Camera Kit supports multiple shooting modes, allowing you to directly launch the system camera to take photos, use preconfigured settings to simplify application development, or build a professional camera application using open APIs.

**Guide**

-   [Using the System Camera to Take Photos and Record Videos (CameraPicker)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/using-the-system-camera-to-take-photos-and-record-videos-camerapicker/document.md)
-   [Photo Capture (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/photo-capture-arkts/document.md)
-   [Deferred Photo Delivery (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/deferred-photo-delivery-arkts/document.md)
-   [Moving Photos (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/moving-photos-arkts/document.md)
-   [Using Camera Preconfiguration (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/using-camera-preconfiguration-arkts/document.md)
-   [HDR Vivid Photo Capture (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/hdr-vivid-photo-capture-arkts/document.md)
-   [Adjusting Camera Rotation Angles (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/camera-rotation/adjusting-camera-rotation-angles-arkts/document.md)
-   [Photo Capture (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/photo-capture-c-c/document.md)
-   [Deferred Photo Delivery (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/deferred-photo-delivery-c-c/document.md)
-   [Using Camera Preconfiguration (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/using-camera-preconfiguration-c-c/document.md)

**API Reference**

-   ArkTS APIs: [camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-camera)
-   ArkTS components: [cameraPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-camerapicker)
-   C APIs: [OH\_Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera)

**Best Practices**

-   [Optimizing Deferred Photo Delivery](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-camera-shot2see)

**Samples**

-   [Starting the System Camera](https://gitcode.com/HarmonyOS_Samples/camera-picker)
-   [Collecting and Saving Camera Data](https://gitcode.com/HarmonyOS_Samples/camera)
-   [Collecting and Saving Camera Data (C++)](https://gitcode.com/HarmonyOS_Samples/camera-data-collection)

## Video Playback

AVPlayer provides integrated playback capabilities and supports a wide range of audio and video formats and streaming protocols. With AVPlayer, applications can perform basic playback controls and deliver an enhanced audiovisual experience through features such as subtitle support, picture-in-picture mode, custom UI components, and content copyright protection.

**Guide**

-   [Introduction to AVPlayer (Including Supported Formats and Protocols)](../media-kit/about-this-kit/document.md#avplayer)
-   [Using AVPlayer to Play Videos (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-play-videos-arkts/document.md)
-   [Using AVPlayer to Set Playback URLs (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-set-playback-urls-arkts/document.md)
-   [Using AVPlayer to Play Streaming Media (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-play-streaming-media-arkts/document.md)
-   [Using AVPlayer to Add External Subtitles to Videos (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-add-external-subtitles-to-videos-arkts/document.md)
-   [Using AVPlayer to Play Videos (C/C++)](../media-kit/media-development-c-c/playback/using-avplayer-to-play-videos-c-c/document.md)
-   [HDR Vivid Video Playback](../avcodec-kit/audio-and-video-codecs/hdr-vivid-capabilities/hdr-vivid-video-playback/document.md)
-   [Accessing Background Tasks Kit for Background Playback](../../application-framework/background-tasks-kit/continuous-task-arkts/document.md)
-   [Accessing AVSession](../avsession-kit/local-avsession/accessing-avsession/document.md)
-   [Self-Check for Playback Control Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/playback-control-access-selfcheck)
-   [Using AVPlayer to Play DRM Content (ArkTS)](../drm-kit/drm-playback-with-avplayer-arkts/document.md)
-   [Video Transcoding (ArkTS)](../media-kit/media-development-arkts/video-transcoding/document.md)
-   [Using PiP in Applications](../../application-framework/arkui/window-manager/using-pip-in-applications/document.md)

**API Reference**

-   ArkTS APIs: [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer)
-   C APIs: [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer)

**Best Practices**

-   [Video Playback](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-video-playback-development-practice)
-   [Minimizing Stuttering in Online Video Playback](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-online-video-playback-lags-practice)
-   [AV Synchronization](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-audio-video-synchronization)
-   [Obtaining Video Thumbnails Using System Capabilities](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-video-thumbnail)

**Samples**

-   [Video Playback Using AVPlayer](https://gitcode.com/HarmonyOS_Samples/video-play)
-   [Playing While Caching](https://gitcode.com/HarmonyOS_Samples/video-cache)
-   [Video Player](https://gitcode.com/HarmonyOS_Samples/video-player)
-   [Obtaining Video Thumbnails Using System Capabilities](https://gitcode.com/HarmonyOS_Samples/VideoThumbnail)
-   [Smooth Switching of Short Videos](https://gitcode.com/HarmonyOS_Samples/SmoothSwitchShortVideos)
-   [Synchronous Audio and Video Playback](https://gitcode.com/HarmonyOS_Samples/AudioToVideoSync)

**Design Experience**

-   [Audio Control Panel](https://developer.huawei.com/consumer/en/doc/design-guides/broadcasting-control-0000001957017133)
-   [PiP](https://developer.huawei.com/consumer/en/doc/design-guides/pip-0000001927422624)

## Video Recording

AVRecorder enables audio and video recording, whereas AVScreenCapture supports screen capture with multi-source input and flexible configuration options, helping you easily implement recording functionality.

**Guide**

-   [Introduction to AVRecorder (Including Formats Supported)](../media-kit/about-this-kit/document.md#avrecorder)
-   [Using AVRecorder to Record Videos (ArkTS)](../media-kit/media-development-arkts/recording/using-avrecorder-to-record-videos-arkts/document.md)
-   [Introduction to AVScreenCapture (Including Formats Supported)](../media-kit/about-this-kit/document.md#avscreencapture)
-   [Using AVScreenCaptureRecorder to Record Screens and Save Them to Files (ArkTS)](../media-kit/media-development-arkts/recording/using-avscreencapturerecorder-to-record-screens-and-write-them-to-files-arkts/document.md)
-   [Using AVScreenCapture to Capture Screens and Obtain Streams (C/C++)](../media-kit/media-development-c-c/recording/using-avscreencapture-to-capture-screens-and-obtain-streams-c-c/document.md)
-   [Using AVScreenCapture to Capture Screens and Write Them to Files (C/C++)](../media-kit/media-development-c-c/recording/using-avscreencapture-to-capture-screens-and-write-them-to-files-c-c/document.md)
-   [HDR Vivid Camera Recording](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/hdr-vivid-camera-recording-arkts/document.md)
-   [HDR Vivid Video Recording](../avcodec-kit/audio-and-video-codecs/hdr-vivid-capabilities/hdr-vivid-video-recording/document.md)
-   [Using Camera Kit for Video Recording (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/video-recording-arkts/document.md)

**API Reference**

-   ArkTS APIs: [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder)
-   C APIs: [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder)
-   ArkTS APIs: [AVScreenCaptureRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder)
-   C APIs: [AVScreenCapture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avscreencapture)

**Samples**

-   [Video Recording Using Camera Kit and AVRecorder](https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder)

## Video Casting

With the media controller, users can seamlessly cast audio and video to other HarmonyOS devices. For example, they can continue playback on a 2-in-1 device after starting it on a smartphone.

**Guide**

-   [Using the Call Device Switching Component](../avsession-kit/distributed-avsession/using-the-call-device-switching-component/document.md)
-   [AVCastPicker Development](../avsession-kit/distributed-avsession/using-avcastpicker/avcastpicker-development/document.md)
-   [Extended Screen Casting Development](../avsession-kit/distributed-avsession/using-avcastpicker/extended-screen-casting-development/document.md)

**API Reference**

-   ArkTS APIs: [avsession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-avsession)
-   ArkTS components: [AVCastPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avcastpicker)

**Samples**

-   [Video Casting](https://gitcode.com/HarmonyOS_Samples/VideoCast)

## Audio Playback

You can use AVPlayer to play media resources, such as MP4, MP3, MKV, and MPEG-TS files, or use AudioRenderer to play raw PCM audio data.

**AVPlayer Guide**

-   [Using AVPlayer to Play Audio (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-play-audio-arkts/document.md)

-   [Using AVPlayer to Set Playback URLs (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-set-playback-urls-arkts/document.md)
-   [Using AVPlayer to Play Streaming Media (ArkTS)](../media-kit/media-development-arkts/playback/using-avplayer-to-play-streaming-media-arkts/document.md)

-   [Using SoundPool to Play Short Sounds (ArkTS)](../media-kit/media-development-arkts/playback/using-soundpool-to-play-short-sounds-arkts/document.md)

-   [Using AVPlayer to Play Audio (C/C++)](../media-kit/media-development-c-c/playback/using-avplayer-to-play-audio-c-c/document.md)

**AVPlayer API Reference**

-   ArkTS APIs: [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer)
-   C APIs: [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer)

**AudioRenderer Guide**

-   [Using AudioRenderer for Audio Playback](../audio-kit/audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md)
-   [Responding to Audio Output Device Changes](../audio-kit/audio-device-routing-management/handling-output-device-changes-gracefully/document.md)
-   [Using OHAudio for Audio Playback (C/C++)](../audio-kit/audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md)
-   [Using AudioHaptic for Audio-Haptic Playback](../audio-kit/audio-playback/using-audiohaptic-for-audio-haptic-playback-arkts/document.md)

**AudioRenderer API Reference**

-   ArkTS APIs: [AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer)
-   ArkTS APIs: [audioHaptic](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic)
-   C APIs: [OHAudio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio)

**General Guide**

-   [Accessing Background Tasks Kit for Background Playback](../../application-framework/background-tasks-kit/continuous-task-arkts/document.md)
-   [Accessing AVSession](../avsession-kit/local-avsession/accessing-avsession/document.md)
-   [Self-Check for Playback Control Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/playback-control-access-selfcheck)
-   [Selecting the Appropriate Audio Stream Types](../audio-kit/selecting-the-appropriate-audio-stream-types/document.md)
-   [Introduction to Audio Focus and Audio Sessions](../audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md)
-   [Using AudioSession to Manage Audio Focus (ArkTS)](../audio-kit/audio-focus-and-audio-session-management/audio-session-management/document.md)
-   [Using AudioSession to Manage Audio Focus (C/C++)](../audio-kit/audio-focus-and-audio-session-management/using-ohaudio-for-audio-session-c-c/document.md)

**Best Practices**

-   [Audio Focus Management](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-audio-focus-management)
-   [Audio Playback Interaction](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-audio-interaction-practice)

**Samples**

-   [AVSession Provider](https://gitcode.com/HarmonyOS_Samples/media-provider)
-   [Low-Latency Audio Recording and Playback](https://gitcode.com/HarmonyOS_Samples/audio-native)
-   [Audio Playback Control Based on AudioRenderer](https://gitcode.com/HarmonyOS_Samples/audio-interaction)

**Design Experience**

-   [Audio Control Panel](https://developer.huawei.com/consumer/en/doc/design-guides/broadcasting-control-0000001957017133)

## Audio Capture

AudioCapture provides audio capture capabilities, enabling you to obtain raw PCM data.

**Guide**

-   [Using AudioCapturer for Audio Recording](../audio-kit/audio-recording/using-audiocapturer-for-audio-recording-arkts/document.md)
-   [Using OHAudio for Audio Recording (C/C++)](../audio-kit/audio-recording/recommended-using-ohaudio-for-audio-recording-c-c/document.md)

**API Reference**

-   ArkTS APIs: [AudioCapturer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiocapturer)
-   C APIs: [OHAudio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio)

**Samples**

-   [Low-Latency Audio Recording and Playback](https://gitcode.com/HarmonyOS_Samples/audio-native)
-   [Audio Playback Control Based on AudioRenderer](https://gitcode.com/HarmonyOS_Samples/audio-interaction)

## Audio Recording

AVRecorder provides the audio recording capability to help you record pure audio files.

**Guide**

-   [Using AVRecorder to Record Audio (ArkTS)](../media-kit/media-development-arkts/recording/using-avrecorder-to-record-audio-arkts/document.md)

**API Reference**

-   ArkTS APIs: [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder)
-   C APIs: [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder)

## Media Resource Selection and Saving

**Guide**

-   [Selecting Media Assets Using Picker](../media-library-kit/selecting-media-assets-using-picker/document.md)
-   [Accessing Images/Videos Using PhotoPickerComponent](../media-library-kit/accessing-images-videos-using-photopickercomponent/document.md)
-   [Saving Media Assets](../media-library-kit/saving-media-assets/document.md)

**API Reference**

-   ArkTS APIs: [photoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-photoaccesshelper)
-   ArkTS components: [AlbumPickerComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-albumpickercomponent)
-   ArkTS components: [PhotoPickerComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent)
-   ArkTS components: [RecentPhotoComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-recentphotocomponent)

**Best Practices**

-   [Obtaining and Storing Images](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image_get_and_save)

**Samples**

-   [Obtaining and Saving an Image](https://gitcode.com/HarmonyOS_Samples/ImageGetAndSave)
-   [Implementing Image Recommendation with PhotoPicker](https://gitcode.com/HarmonyOS_Samples/SmartPhotoPicker)

## Privacy and Security

During media application development, access to personal data (such as photos, videos, and audio files) and device resources (like the camera or microphone) is often required. These resources are protected by the system. To use them, applications must either use **Picker** or request corresponding permissions.

**Accessing Personal Data**

-   [Selecting Media Assets Using Picker](../media-library-kit/selecting-media-assets-using-picker/document.md)
-   [Saving Media Assets](../media-library-kit/saving-media-assets/document.md)
-   [Selecting Audio Clips](../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/selecting-user-files/document.md#selecting-audio-clips)
-   [Saving Audio Clips](../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/saving-user-files/document.md#saving-audio-clips)

If an application needs to clone, back up, or synchronize image or video files, it may [request restricted permissions to read from and write to the media library](../media-library-kit/restricted-open-capabilities/before-you-start/document.md#requesting-permissions).

**Accessing Device Data**

ohos.permission.MICROPHONE, ohos.permission.CAMERA, and ohos.permission.MEDIA\_LOCATION are all user-granted permissions. For details on how to apply for them, see [Requesting User Authorization](../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

#### More Resources

**Audio Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Audio focus

 | 

-   Guide: [Selecting the Appropriate Audio Stream Types](../audio-kit/selecting-the-appropriate-audio-stream-types/document.md)
-   Guide: [Introduction to Audio Focus and Audio Sessions](../audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md)
-   ArkTS API reference: [AudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager)
-   ArkTS API reference: [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage)

 |
| 

Audio call

 | 

-   Guide: [Using AudioRenderer to Play the Peer Voice](../audio-kit/audio-call/developing-audio-call/document.md#using-audiorenderer-to-play-the-peer-voice)
-   Guide: [Using AudioCapturer to Record the Local Voice](../audio-kit/audio-call/developing-audio-call/document.md#using-audiocapturer-to-record-the-local-voice)

 |
| 

More

 | 

[Audio Kit Development Guide](../audio-kit/document.md)

[Audio Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/audio-api)

 |

**AVCodec Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Audio codec

 | 

-   Guide: [Audio Encoding](../avcodec-kit/audio-and-video-codecs/audio-encoding/document.md)
-   Guide: [Audio Decoding](../avcodec-kit/audio-and-video-codecs/audio-decoding/document.md)
-   Samples: [AudioEncoder](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/AudioEncoder.cpp)
-   Samples: [AudioDecoder](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/AudioDecoder.cpp)
-   C API reference: [AudioCodec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-audiocodec-h)

 |
| 

Video codec

 | 

-   Guide: [Video Encoding](../avcodec-kit/audio-and-video-codecs/video-encoding/document.md)
-   Samples: [VideoEncoder](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec/entry/src/main/cpp/capbilities/video_encoder.cpp)
-   C API reference: [VideoEncoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h)
-   Guide: [Video Decoding](../avcodec-kit/audio-and-video-codecs/video-decoding/document.md)
-   Samples: [VideoDecoder](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec/entry/src/main/cpp/capbilities/video_decoder.cpp)
-   C API reference: [VideoDecoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h)

 |
| 

More

 | 

[AVCodec Kit Development Guide](../avcodec-kit/document.md)

[AVCodec Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/avcodec-api)

 |

**AVSession Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Local AVSession

 | 

-   ArkTS API reference: [AVSession Management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-avsession)
-   Guide: [Accessing AVSession](../avsession-kit/local-avsession/accessing-avsession/document.md)
-   Samples: [AVSession Provider](https://gitcode.com/HarmonyOS_Samples/media-provider)
-   Samples: [Audio Playback Control Based on AudioRenderer](https://gitcode.com/HarmonyOS_Samples/audio-interaction)

 |
| 

More

 | 

[AVSession Kit Development Guide](../avsession-kit/document.md)

[AVSession Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/avsession-api)

 |

**Camera Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Video recording

 | 

-   ArkTS API reference: [Camera Management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-camera)

-   Guide: [Video Recording (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/video-recording-arkts/document.md)
-   Guide: [Video Recording (C/C++)](../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/video-recording-c-c/document.md)
-   Practices: [Video Recording Practices (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/video-recording-practices-arkts/document.md)

 |
| 

Secure mode camera

 | 

-   ArkTS API reference: [SecureSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-securesession)

-   Guide: [Secure Mode Camera (ArkTS)](../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/secure-mode-camera-arkts/document.md)

 |
| 

More

 | 

[Camera Kit Development Guide](../camera-kit/document.md)

[Camera Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/camera-api)

 |

**DRM Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Using AVPlayer to play DRM content

 | 

-   ArkTS API reference: [DRM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-drm)
-   Guide: [DRM Development (ArkTS)](../drm-kit/drm-development-arkts/document.md)
-   Practices: [Using AVPlayer to Play DRM Content (ArkTS)](../drm-kit/drm-playback-with-avplayer-arkts/document.md)

 |
| 

Using AVCodec to play DRM content

 | 

-   C API reference: [Drm (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm)
-   Guide: [DRM Development (C/C++)](../drm-kit/drm-development-c-c/document.md)
-   Practices: [Using AVCodec to Play DRM Content (C/C++)](../drm-kit/drm-playback-with-avcodec-c-c/document.md)

 |
| 

More

 | 

[DRM Kit Development Guide](../drm-kit/document.md)

[DRM Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/drm-api)

 |

**Image Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Image decoding

 | 

Decodes images in HEIF, JPEG, PNG, WebP, GIF, BMP, SVG, ICO, and DNG formats.

-   ArkTS guide: [Using ImageSource to Decode Images](../image-kit/image-development-arkts/image-decoding/using-imagesource-to-decode-images/document.md)
-   C/C++ guide: [Using Image\_NativeModule to Decode Images](../image-kit/image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md)

Allocates memory for decoding images, optimizing the decoding efficiency.

-   ArkTS guide: [Allocating Memory for Image Decoding (ArkTS)](../image-kit/image-development-arkts/image-decoding/optimizing-memory-for-image-decoding-arkts/document.md)
-   C/C++ guide: [Allocating Memory for Image Decoding (C/C++)](../image-kit/image-development-c-c/image-decoding/optimizing-memory-for-image-decoding-c-c/document.md)

 |
| 

Image encoding

 | 

Encodes images in HEIF, JPEG, PNG, WebP, and GIF formats.

-   ArkTS guide: [Using ImagePacker to Encode Images](../image-kit/image-development-arkts/image-encoding/using-imagepacker-to-encode-images/document.md)
-   C/C++ guide: [Using Image\_NativeModule to Encode Images](../image-kit/image-development-c-c/image-encoding/using-image-nativemodule-to-encode-images/document.md)

 |
| 

Image receiving

 | 

Receives and processes images as a consumer.

-   ArkTS guide: [Using ImageReceiver to Receive Images](../image-kit/image-development-arkts/image-receiving/using-imagereceiver-to-receive-images/document.md)
-   C/C++ guide: [Using Image\_NativeModule to Receive Images](../image-kit/image-development-c-c/image-receiving/using-image-nativemodule-to-receive-images/document.md)
-   C/C++ guide: [Using Image\_NativeModule to Process Image Information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-info-c)

 |
| 

Image editing and processing

 | 

Supports image transformations such as cropping, scaling, translation, rotation, flipping, and opacity setting, and PixelMap operations such as pixel data writing to specific regions of an image.

-   ArkTS guide: [Using PixelMap to Transform Images](../image-kit/image-development-arkts/image-editing-and-processing/using-pixelmap-to-transform-images/document.md)
-   ArkTS guide: [Using PixelMap for PixelMap Operations](../image-kit/image-development-arkts/image-editing-and-processing/using-pixelmap-for-pixelmap-operations/document.md)
-   C/C++ guide: [Using Image\_NativeModule for PixelMap Operations](../image-kit/image-development-c-c/image-editing-and-processing/using-image-nativemodule-for-pixelmap-operations/document.md)

Reads and edits EXIF information of images.

-   ArkTS guide: [Editing EXIF Data](../image-kit/image-development-arkts/image-editing-and-processing/editing-exif-data/document.md)
-   C/C++ guide: [Using Image\_NativeModule to Edit EXIF Data](../image-kit/image-development-c-c/image-editing-and-processing/using-image-nativemodule-to-edit-exif-data/document.md)

Adds personalized filters to images.

-   C/C++: [Using ImageEffect to Edit Images](../image-kit/image-development-c-c/image-editing-and-processing/using-imageeffect-to-edit-images/document.md)

Enhances image clarity, converts color spaces, and converts HDR effects.

-   C/C++ guide: [Scaling Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-scaling)
-   C/C++ guide: [Color Space Conversion for Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-csc)
-   C/C++ guide: [Dynamic Metadata Generation for Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-dynamic-metadata-generation)
-   C/C++ guide: [Converting HDR Images from Single-Layer to Dual-Layer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdr-single-to-dual)
-   C/C++ guide: [Converting HDR Images from Dual-Layer to Single-Layer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdr-dual-to-single)

 |
| 

More

 | 

[Image Kit Development Guide](../image-kit/document.md)

[Image Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/image-api)

 |

**Media Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Video transcoding

 | 

-   ArkTS API reference: [AVTranscoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avtranscoder)
-   Guide: [Using AVTranscoder to Transcode Videos (ArkTS)](../media-kit/media-development-arkts/video-transcoding/using-avtranscoder-to-transcode-videos-arkts/document.md)
-   Guide: [Creating an Asynchronous Thread for AVTranscoder Video Transcoding (ArkTS)](../media-kit/media-development-arkts/video-transcoding/creating-an-asynchronous-thread-for-avtranscoder-video-transcoding-arkts/document.md)

 |
| 

Metadata

 | 

-   ArkTS API reference: [AVMetadataExtractor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avmetadataextractor)
-   C API reference: [AVMetadataExtractor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadataextractor)
-   Guide: [Using AVMetadataExtractor to Extract Audio and Video Metadata (ArkTS)](../media-kit/media-development-arkts/media-information-query/using-avmetadataextractor-to-extract-audio-and-video-metadata-arkts/document.md)
-   Guide: [Using AVMetadataExtractor to Obtain Metadata (C/C++)](../media-kit/media-development-c-c/media-information-query/using-avmetadataextractor-to-obtain-metadata-c-c/document.md)

 |
| 

Thumbnail

 | 

-   ArkTS API reference: [AVImageGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avimagegenerator)
-   C API reference: [AVImageGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimagegenerator)

-   Guide: [Using AVImageGenerator to Extract Video Images at a Specified Time (ArkTS)](../media-kit/media-development-arkts/media-information-query/using-avimagegenerator-to-extract-video-images-at-a-specified-time-arkts/document.md)
-   Guide: [Using AVImageGenerator to Obtain Video Frames (C/C++)](../media-kit/media-development-c-c/media-information-query/using-avimagegenerator-to-obtain-video-frames-c-c/document.md)
-   Best practices: [Obtaining Video Thumbnails Using System Capabilities](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-video-thumbnail)

 |
| 

More

 | 

[Media Kit Development Guide](../media-kit/document.md)

[Media Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/media-api)

 |

**Media Library Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Moving photos

 | 

-   Guide: [Accessing and Managing Moving Photos](../media-library-kit/moving-photos/accessing-and-managing-moving-photos/document.md)
-   Guide: [Playing Moving Photos with MovingPhotoView](../media-library-kit/moving-photos/playing-moving-photos-with-movingphotoview/document.md)

 |
| 

More

 | 

[Media Library Kit Development Guide](../media-library-kit/document.md)

[Media Library Kit API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/media-library-api)

 |

**Ringtone Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Ringtone setting

 | 

-   ArkTS API reference: [Ringtone Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ringtone-ringtone)
-   Guide: [Setting a Ringtone](../ringtone-kit/setting-a-ringtone/document.md)

 |

**Scan Kit**

| 
Category

 | 

Resource Link

 |
| :-- | :-- |
| 

Barcode scan by default UI

 | 

-   ArkTS API reference: [Scanning Barcodes Using the Default UI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api)
-   Guide: [Barcode Scanning by Default UI](../scan-kit/barcode-scanning-by-default-ui/document.md)

 |
| 

Barcode scan by custom UI

 | 

-   ArkTS API reference: [Scanning Barcodes Using the Custom UI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api)
-   Guide: [Barcode Scanning by Custom UI](../scan-kit/barcode-scanning-by-custom-ui/document.md)

 |
| 

Image recognition

 | 

-   ArkTS API reference: [Recognizing Barcodes in an Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode)
-   Guide: [Scanning Barcodes in a Saved Image](../scan-kit/recognizing-barcodes-in-an-image/scanning-barcodes-in-a-saved-image/document.md)
-   Guide: [Recognizing Barcodes in Image Data](../scan-kit/recognizing-barcodes-in-an-image/recognizing-barcodes-in-image-data/document.md)

 |
| 

Barcode image generation

 | 

-   ArkTS API reference: [Generating a Barcode Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode)
-   Guide: [Generating a Barcode Image from Text](../scan-kit/barcode-image-generation/generating-a-barcode-image-from-text/document.md)
-   Guide: [Generating a Barcode Image from a Byte Array](../scan-kit/barcode-image-generation/generating-a-barcode-image-from-a-byte-array/document.md)

 |
