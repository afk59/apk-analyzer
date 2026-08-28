# DRM Playback with AVCodec (C/C++)

#### When to Use

To play DRM-protected content using AVCodec, you can use the native APIs provided by DRM Kit.

Currently, the following decryption capabilities are supported:

| Audio Container | Audio Decryption |
| :-- | :-- |
| mp4 | AAC |

| Video Container | Video Decryption |
| :-- | :-- |
| ts | AVC(H.264) |
| mp4 | AVC(H.264) |
| mp4 | HEVC(H.265) |

**Usage Scenario**

Before setting up DRM, obtain the DRM information. For details, see step 4 in [Media Data Demultiplexing](../../avcodec-kit/media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md#how-to-develop).

#### Development Guidelines

For details on the APIs, see [DRM API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm).

Follow the sample code below to implement the entire DRM workflow, including obtaining a name and ID list of the DRM solutions supported by the device, creating a MediaKeySystem, creating a MediaKeySession, generating a media key request, processing a media key response, checking for secure video decoding requirements, and cleaning up resources.

When developing your application, follow the specified order of API calls to avoid exceptions or undefined behaviors. The development steps and explanations below outline the correct sequence.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_drm.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/FJyugFNyRmOo2h9zSd5HYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3ED24DAE68A8554BC390AD753FC66A40854F3041EF8A2AAFA0254C61ADFCEAA)

Replace 'sample' with your actual project name as needed.

#### How to Develop

1.  Import the DRM Kit module.
    
    #include "multimedia/drm\_framework/native\_drm\_common.h"
    #include "multimedia/drm\_framework/native\_drm\_err.h"
    #include "multimedia/drm\_framework/native\_mediakeysession.h"
    #include "multimedia/drm\_framework/native\_mediakeysystem.h"
    
2.  Obtain the name and ID list of the DRM solutions supported by the device.
    
    uint32\_t count = 3; // count specifies the number of DRM plugins supported by the device. Pass in the actual number.
    DRM\_MediaKeySystemDescription descriptions\[3\];
    memset(descriptions, 0, sizeof(descriptions));
    Drm\_ErrCode ret = OH\_MediaKeySystem\_GetMediaKeySystems(descriptions, &count);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_GetMediaKeySystems failed.");
    }
    
    After obtaining the name and ID list of the DRM solutions supported by the device, match this list with the DRM information to create the appropriate DRM solution. You can obtain the DRM information by referring to step 4 in [Media Data Demultiplexing](../../avcodec-kit/media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md#how-to-develop).
    
    Alternatively, directly parse the media protocol or media data to extract the unique identifier of the DRM solution and the PSSH data to generate the DRM information.
    
3.  Create a MediaKeySystem instance.
    
    MediaKeySystem \*mediaKeySystem = nullptr;
    ret = OH\_MediaKeySystem\_Create("com.wiseplay.drm", &mediaKeySystem);
    if (ret != DRM\_ERR\_OK || mediaKeySystem == nullptr) {
        printf("OH\_MediaKeySystem\_Create failed.");
    }
    
4.  Create a MediaKeySession instance.
    
    MediaKeySession \*mediaKeySession = nullptr;
    DRM\_ContentProtectionLevel contentProtectionLevel = CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO; // Set the content protection level supported by the device.
    ret = OH\_MediaKeySystem\_CreateMediaKeySession(mediaKeySystem, &contentProtectionLevel, &mediaKeySession);
    if (ret != DRM\_ERR\_OK || mediaKeySession == nullptr) {
        printf("OH\_MediaKeySystem\_CreateMediaKeySession failed.");
    }
    
5.  Check whether secure decoding is required.
    
    bool requireSecureDecoder;
    ret = OH\_MediaKeySession\_RequireSecureDecoderModule(mediaKeySession, "video/avc", &requireSecureDecoder);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySession\_RequireSecureDecoderModule failed.");
    }
    
6.  Generate a media key request and process its response.
    
    #define MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE 24576 // 24576: (2 \* 12 \* 1024)
    DRM\_MediaKeyRequest mediaKeyRequest;
    DRM\_MediaKeyRequestInfo info;
    // initData corresponds to PSSH data in the stream. Pass in the actual data.
    unsigned char initData\[512\] = {0x00};
    memset(&info, 0, sizeof(DRM\_MediaKeyRequestInfo));
    info.initDataLen = sizeof(initData);
    info.type = MEDIA\_KEY\_TYPE\_ONLINE; // MEDIA\_KEY\_TYPE\_ONLINE: online media key request; MEDIA\_KEY\_TYPE\_OFFLINE: offline media key request.
    if (sizeof("video/mp4") <= sizeof(info.mimeType)) {
    memcpy(info.mimeType, "video/mp4", sizeof("video/mp4"));
    }
    if (info.initDataLen <= sizeof(info.initData)) {
    memcpy(info.initData, initData, info.initDataLen);
    }
    if (sizeof("optionalDataName") <= sizeof(info.optionName\[0\])) {
    memcpy(info.optionName\[0\], "optionalDataName", sizeof("optionalDataName"));
    }
    
    if (sizeof("optionalDataValue") <= sizeof(info.optionData\[0\])) {
    memcpy(info.optionData\[0\], "optionalDataValue", sizeof("optionalDataValue"));
    }
    info.optionsCount = 1;
    ret = OH\_MediaKeySession\_GenerateMediaKeyRequest(mediaKeySession, &info, &mediaKeyRequest);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySession\_GenerateMediaKeyRequest failed.");
    }
    /\*
      The application requests the DRM service through the network, obtains a media key response, and sends the response to OH\_MediaKeySession\_ProcessMediaKeyResponse.
      If the response is an offline media key response, the offline media key ID is returned. Set mediaKeyId based on the actual data and length.
    \*/
    unsigned char mediaKeyId\[128\] = {0x00};
    int32\_t mediaKeyIdLen = 128;
    // MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE specifies the maximum length of a media key response. Pass in the actual length.
    unsigned char mediaKeyResponse\[MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE\] = {0x00};
    int32\_t mediaKeyResponseLen = MAX\_DRM\_MEDIA\_KEY\_RESPONSE\_BUF\_SIZE;
    ret = OH\_MediaKeySession\_ProcessMediaKeyResponse(mediaKeySession, mediaKeyResponse,
        mediaKeyResponseLen, mediaKeyId, &mediaKeyIdLen);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySession\_ProcessMediaKeyResponse failed.");
    }
    
    If required, set the audio decryption configuration by following step 4 in [Audio Decoding](../../avcodec-kit/audio-and-video-codecs/audio-decoding/document.md#how-to-develop), and set the video decryption configuration by following step 4 in [Surface Mode in Video Decoding](../../avcodec-kit/audio-and-video-codecs/video-decoding/document.md#surface-mode) or step 4 in [Buffer Mode in Video Decoding](../../avcodec-kit/audio-and-video-codecs/video-decoding/document.md#buffer-mode).
    
7.  Destroy the MediaKeySession instance.
    
    ret = OH\_MediaKeySession\_Destroy(mediaKeySession);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySession\_Destroy failed.");
    }
    
8.  Destroy the MediaKeySystem instance.
    
    ret = OH\_MediaKeySystem\_Destroy(mediaKeySystem);
    if (ret != DRM\_ERR\_OK) {
        printf("OH\_MediaKeySystem\_Destroy failed.");
    }
