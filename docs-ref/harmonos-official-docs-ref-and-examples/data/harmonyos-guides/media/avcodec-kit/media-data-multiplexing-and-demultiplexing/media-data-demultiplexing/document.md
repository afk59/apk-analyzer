# Media Data Demultiplexing

You can call native APIs to demultiplex media data. The demultiplexing involves extracting media samples such as audio, video, and subtitles from bit stream data, and obtaining information related to Digital Rights Management (DRM).

Currently, two data input types are supported: remote connection (over HTTP) and File Descriptor (FD).

For details about the supported demultiplexing formats, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#media-data-demultiplexing).

**When to Use**

-   Audio and video playback
    
    Demultiplex media streams, decode the samples obtained through demultiplexing, and play the samples.
    
-   Audio and video editing
    
    Demultiplex media streams, and edit the specified samples.
    
-   Media file format conversion
    
    Demultiplex media streams, and encapsulate them into a new file format.
    

#### Development Guidelines

Read [AVDemuxer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avdemuxer) and [AVSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avsource) for the API reference.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/623s2tHxSei-yt1gYnHueQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=402F3B0524143772E2281D2F2F169A80FB34ADDC844DC3CADBA409F672EF3B01)

-   To call the demuxer APIs to parse a network playback path, declare the ohos.permission.INTERNET permission by following the instructions provided in [Declaring Permissions](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
-   To call the demuxer APIs to write a local file, request the ohos.permission.READ\_MEDIA permission by following the instructions provided in [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   You can also use **ResourceManager.getRawFd** to obtain the FD of a file packed in the HAP file. For details, see [ResourceManager API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getrawfd9).

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_avdemuxer.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_avsource.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/A6lxipzWTgm6wi0J7b2o2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B905FE17AA1A1E9A7515611B5A28E0BDE98DF5EA896521981FE2E3D23D896694)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avdemuxer.h>
    #include <multimedia/player\_framework/native\_avsource.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fcntl.h>
    #include <sys/stat.h>
    #include <string>
    
2.  Create a resource instance.
    
    When using **open** to obtain the FD, convert the value of **filepath** to a [sandbox path](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md#mappings-between-application-sandbox-paths-and-physical-paths) to obtain sandbox resources.
    
    // Create the FD. You must have the read permission on the file instance to open the file. (filePath indicates the path of the file to be demultiplexed. The file must exist.)
    std::string filePath = "test.mp4";
    int32\_t fd = open(filePath.c\_str(), O\_RDONLY);
    struct stat fileStatus {};
    int64\_t fileSize = 0;
    if (stat(filePath.c\_str(), &fileStatus) == 0) {
       fileSize = static\_cast<int64\_t>(fileStatus.st\_size);
    } else {
       printf("get stat failed");
       return;
    }
    // Note: The offset (start offset of the file) and fileSize (file size) must match the file to be parsed.
    // If fd points to a single resource file, set offset to 0 and fileSize to the size of the resource file.
    // If fd points to multiple consecutive resource files (for example, multiple MP3 binary files), set offset and fileSize based on the actual offset and size of the resource file to be parsed.
    OH\_AVSource \*source = OH\_AVSource\_CreateWithFD(fd, 0, fileSize);
    if (source == nullptr) {
       printf("create source failed");
       return;
    }
    // (Optional) Create a source resource instance for the URI resource file.
    // OH\_AVSource \*source = OH\_AVSource\_CreateWithURI(uri);
    
    // (Optional) Create a source resource instance for the custom data source. Before the operation, you must implement AVSourceReadAt.
    // Add g\_filePath when OH\_AVSource\_CreateWithDataSource is used.
    // g\_filePath = filePath ;
    // OH\_AVDataSource dataSource = {fileSize, AVSourceReadAt};
    // OH\_AVSource \*source = OH\_AVSource\_CreateWithDataSource(&dataSource);
    
    Implement the **AVSourceReadAt** API before creating the resource instance.
    
    // Add the header file.
    #include <fstream>
    
    static std::string g\_filePath;
    
    enum MediaDataSourceError : int32\_t {
       SOURCE\_ERROR\_IO = -2,
       SOURCE\_ERROR\_EOF = -1
    };
    
    int32\_t AVSourceReadAt(OH\_AVBuffer \*data, int32\_t length, int64\_t pos)
    {
       if (data == nullptr) {
          printf("AVSourceReadAt : data is nullptr!\\n");
          return MediaDataSourceError::SOURCE\_ERROR\_IO;
       }
    
       std::ifstream infile(g\_filePath, std::ofstream::binary);
       if (!infile.is\_open()) {
          printf("AVSourceReadAt : open file failed! file:%s\\n", g\_filePath.c\_str());
          return MediaDataSourceError::SOURCE\_ERROR\_IO; // Failed to open the file.
       }
    
       infile.seekg(0, std::ios::end);
       int64\_t fileSize = infile.tellg();
       if (pos >= fileSize) {
          printf("AVSourceReadAt : pos over or equals file size!\\n");
          return MediaDataSourceError::SOURCE\_ERROR\_EOF; // pos is already at the end of the file and cannot be read.
       }
    
       if (pos + length > fileSize) {
          length of length = fileSize - pos; // When the sum of pos and length exceeds the file size, the data from pos to the end of the file is read.
       }
    
       infile.seekg(pos, std::ios::beg);
       if (length <= 0) {
          printf("AVSourceReadAt : read length less than zero!\\n");
          return MediaDataSourceError::SOURCE\_ERROR\_IO;
       }
       char\* buffer = new char\[length\];
       infile.read(buffer, length);
       infile.close();
    
       memcpy(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(data)),
          buffer, length);
       delete\[\] buffer;
    
       return length;
    }
    
3.  Create a demuxer instance.
    
    // Create a demuxer for the resource instance.
    OH\_AVDemuxer \*demuxer = OH\_AVDemuxer\_CreateWithSource(source);
    if (demuxer == nullptr) {
       printf("create demuxer failed");
       return;
    }
    
4.  (Optional) Register a [callback to obtain the media key system information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avdemuxer-h#demuxer_mediakeysysteminfocallback). If the stream is not a DRM stream or the [media key system information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm-drm-mediakeysysteminfo) has been obtained, you can skip this step.
    
    In the API for setting DRM information listeners, the callback function can return a demuxer instance. It is suitable for the scenario where multiple demuxer instances are used.
    
    // Implement the OnDrmInfoChangedWithObj callback.
    static void OnDrmInfoChangedWithObj(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*drmInfo)
    {
       // Parse the media key system information, including the quantity, DRM type, and corresponding PSSH.
    }
    
    Demuxer\_MediaKeySystemInfoCallback callback = &OnDrmInfoChangedWithObj;
    Drm\_ErrCode ret = OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback(demuxer, callback);
    
    After the callback is invoked, you can call the API to proactively obtain the media key system information (UUID and corresponding PSSH).
    
    DRM\_MediaKeySystemInfo mediaKeySystemInfo;
    OH\_AVDemuxer\_GetMediaKeySystemInfo(demuxer, &mediaKeySystemInfo);
    
    After obtaining and parsing DRM information, create [MediaKeySystem and MediaKeySession](../../../drm-kit/drm-development-c-c/document.md) instances of the corresponding DRM scheme to obtain a media key. If required, set the audio decryption configuration by following step 4 in [Audio Decoding](../../audio-and-video-codecs/audio-decoding/document.md#how-to-develop), and set the video decryption configuration by following step 5 in [Surface Mode in Video Decoding](../../audio-and-video-codecs/video-decoding/document.md#surface-mode) or step 4 in [Buffer Mode in Video Decoding](../../audio-and-video-codecs/video-decoding/document.md#buffer-mode).
    
5.  Obtain file information.
    
    // (Optional) Obtain custom file attributes. If custom file attributes are not required, skip this step.
    // Obtain custom attributes from the source file.
    OH\_AVFormat \*customMetadataFormat = OH\_AVSource\_GetCustomMetadataFormat(source);
    if (customMetadataFormat == nullptr) {
       // Release resources from the previous steps. For details, see step 10.
       printf("get custom metadata format failed");
       return;
    }
    // Precautions:
    // 1. customKey must exactly match the key used during multiplexing (including the complete naming hierarchy).
    // The example key is for demonstration only. Replace it with the actual custom string.
    // For example, if the key used during multiplexing is com.openharmony.custom.meta.abc.efg,
    // you must use the full key. Using a truncated key like com.openharmony.custom.meta.abc will fail.
    // 2. The value type must match the data type used during multiplexing. In this example, it is a string. For other types, use the right API. The types ints and floats are supported. Starting from API version 20, the type buffer is also supported.
    const char \*customKey = "com.openharmony.custom.meta.string"; // Replace it with the actual key used during multiplexing.
    const char \*customValue;
    if (!OH\_AVFormat\_GetStringValue(customMetadataFormat, customKey, &customValue)) {
       printf("get custom metadata from custom metadata format failed");
    }
    OH\_AVFormat\_Destroy(customMetadataFormat);
    customMetadataFormat = nullptr;
    
    // (Optional) Obtain the number of tracks. If you know the track information, skip this step.
    // Obtain the number of tracks from the file source information. You can call the API to obtain file-level attributes. For details, see Table 1 in Appendix 1.
    OH\_AVFormat \*sourceFormat = OH\_AVSource\_GetSourceFormat(source);
    if (sourceFormat == nullptr) {
       // Release resources from the previous steps. For details, see step 10.
       printf("get source format failed");
       return;
    }
    int32\_t trackCount = 0;
    if (!OH\_AVFormat\_GetIntValue(sourceFormat, OH\_MD\_KEY\_TRACK\_COUNT, &trackCount)) {
       printf("get track count from source format failed");
    }
    if (trackCount == 0) {
       // If the file does not contain any track, perform other operations based on the service.
       printf("no track");
    }
    OH\_AVFormat\_Destroy(sourceFormat);
    sourceFormat = nullptr;
    
6.  (Optional) Obtain the track index and format. If you know the track information, skip this step.
    
    uint32\_t audioTrackIndex = 0;
    uint32\_t videoTrackIndex = 0;
    int32\_t w = 0;
    int32\_t h = 0;
    int64\_t bitRate = 0; // Configure the bit rate, in bit/s.
    double frameRate = 0.0;
    const char\* mimetype = nullptr;
    uint8\_t \*codecConfig = nullptr;
    size\_t bufferSize = 0;
    int32\_t trackType = -1;
    for (uint32\_t index = 0; index < (static\_cast<uint32\_t>(trackCount)); index++) {
       // Obtain the track information. You can call the API to obtain track-level attributes. For details, see Table 2 in Appendix.
       OH\_AVFormat \*trackFormat = OH\_AVSource\_GetTrackFormat(source, index);
       if (trackFormat == nullptr) {
          printf("get track format failed");
          return;
       }
       // Obtain the track type. Unsupported types will not modify the value of trackType.
       // It is recommended that the initial value of trackType be set to an invalid value (for example, -1) to prevent misuse.
       if (!OH\_AVFormat\_GetIntValue(trackFormat, OH\_MD\_KEY\_TRACK\_TYPE, &trackType)) {
          printf("get track type from track format failed");
          return;
       }
       if (trackType == OH\_MediaType::MEDIA\_TYPE\_AUXILIARY) {
          const char \*referenceType;
          if (!OH\_AVFormat\_GetStringValue(trackFormat, OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE, &referenceType)) {
             printf("get reference type from auxiliary track failed");
          }
          int32\_t\* referenceIds;
          size\_t referenceIdsCount;
          if (!OH\_AVFormat\_GetIntBuffer(trackFormat, OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE, &referenceIds, &referenceIdsCount)) {
             printf("get reference track ids from auxiliary track failed");
          }
          // Process the track reference relationship based on the auxiliary track type.
       }
       static\_cast<OH\_MediaType>(trackType) == OH\_MediaType::MEDIA\_TYPE\_AUD ? audioTrackIndex = index : videoTrackIndex = index;
       // Obtain the width and height of the video track.
       if (trackType == OH\_MediaType::MEDIA\_TYPE\_VID) {
          if (!OH\_AVFormat\_GetIntValue(trackFormat, OH\_MD\_KEY\_WIDTH, &w)) {
             printf("get track width from track format failed");
             return;
          }
          if (!OH\_AVFormat\_GetIntValue(trackFormat, OH\_MD\_KEY\_HEIGHT, &h)) {
             printf("get track height from track format failed");
             return;
          }
          if (!OH\_AVFormat\_GetLongValue(trackFormat, OH\_MD\_KEY\_BITRATE, &bitRate)) {
             printf("get track bitRate from track format failed");
             return;
          }
          if (!OH\_AVFormat\_GetDoubleValue(trackFormat, OH\_MD\_KEY\_FRAME\_RATE, &frameRate)) {
             printf("get track frameRate from track format failed");
             return;
          }
          if (!OH\_AVFormat\_GetStringValue(trackFormat, OH\_MD\_KEY\_CODEC\_MIME, &mimetype)) {
             printf("get track mimetype from track format failed");
             return;
          }
          if (!OH\_AVFormat\_GetBuffer(trackFormat, OH\_MD\_KEY\_CODEC\_CONFIG, &codecConfig, &bufferSize)) {
             printf("get track codecConfig from track format failed");
             return;
          }
          printf(" track width%d, track height: %d, track bitRate: %ld, track frameRate: %f, track mimetype: %s\\n", w, h, bitRate, frameRate, mimetype);
       }
       OH\_AVFormat\_Destroy(trackFormat);
       trackFormat = nullptr;
    }
    
7.  Select a track, from which the demuxer reads data.
    
    if(OH\_AVDemuxer\_SelectTrackByID(demuxer, audioTrackIndex) != AV\_ERR\_OK){
       printf("select audio track failed: %d", audioTrackIndex);
       return;
    }
    if(OH\_AVDemuxer\_SelectTrackByID(demuxer, videoTrackIndex) != AV\_ERR\_OK){
       printf("select video track failed: %d", videoTrackIndex);
       return;
    }
    // (Optional) Deselect the track.
    // OH\_AVDemuxer\_UnselectTrackByID(demuxer, audioTrackIndex);
    
8.  (Optional) Seek to the specified time for the selected track.
    
    // Demultiplexing is performed from this time.
    // Note:
    // 1. If OH\_AVDemuxer\_SeekToTime is called for an MPEG TS or MPG file, the target position may be a non-key frame. You can then call OH\_AVDemuxer\_ReadSampleBuffer to check whether the current frame is a key frame based on the obtained OH\_AVCodecBufferAttr. If it is a non-key frame, which causes display issues on the application side, cyclically read the frames until you reach the first key frame, where you can perform processing such as decoding.
    // 2. If OH\_AVDemuxer\_SeekToTime is called for an OGG file, the file seeks to the start of the time interval (second) where the input parameter millisecond is located, which may cause a certain number of frame errors.
    // 3. The seek operation of the demuxer is performed only on streams with consistent decoding behavior. If a stream requires the decoder to reconfigure or re-input parameter data after seeking to decode correctly, it may result in artifacts or decoder freezing.
    OH\_AVDemuxer\_SeekToTime(demuxer, 0, OH\_AVSeekMode::SEEK\_MODE\_CLOSEST\_SYNC);
    
9.  Start demultiplexing and cyclically obtain samples. The code snippet below uses a file that contains audio and video tracks as an example.
    
    A BufferAttr object contains the following attributes.
    
    -   **size**: sample size.
    -   **offset**: offset of the data in the AVBuffer. The value is generally 0.
    -   **pts**: timestamp when the file is multiplexed.
    -   **flags**: sample attributes.
    
    | flag | Description |
    | :-- | :-- |
    | AVCODEC\_BUFFER\_FLAGS\_NONE | Default value. |
    | AVCODEC\_BUFFER\_FLAGS\_EOS | End of Stream (EOS). The data is empty. |
    | AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME | IDR frame or I-frame. |
    | AVCODEC\_BUFFER\_FLAGS\_INCOMPLETE\_FRAME | Incomplete sample. Generally, a complete sample fails to be copied because the buffer is too small. |
    | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | Frame containing parameter set information. |
    | AVCODEC\_BUFFER\_FLAGS\_DISCARD | Frames that can be discarded. |
    
    The **OH\_AVDemuxer\_ReadSampleBuffer** function can be time-consuming, particularly due to file I/O operations. You are advised to call this function in asynchronous mode.
    
    // Define a processing function for each thread.
    void ReadTrackSamples(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, int32\_t buffer\_size,
                          std::atomic<bool>& isEnd, std::atomic<bool>& threadFinished)
    {
       // Create a buffer.
       OH\_AVBuffer \*buffer = OH\_AVBuffer\_Create(buffer\_size);
       if (buffer == nullptr) {
          printf("Create buffer failed for track %d\\n", trackIndex);
          threadFinished.store(true);
          return;
       }
       OH\_AVCodecBufferAttr info;
       int32\_t ret;
    
       while (!isEnd.load()) {
          // Before calling OH\_AVDemuxer\_ReadSampleBuffer, call OH\_AVDemuxer\_SelectTrackByID to select the track from which the demuxer reads data.
          // Note:
          // For AVI, MPG, and WMV formats, since the container standard does not support encapsulating timestamp information, the demultiplexed frames do not contain PTS information. The caller needs to calculate display timestamps based on the frame rate and the display order of the decoded frames.
          ret = OH\_AVDemuxer\_ReadSampleBuffer(demuxer, trackIndex, buffer);
          if (ret == AV\_ERR\_OK) {
                OH\_AVBuffer\_GetBufferAttr(buffer, &info);
                printf("Track %d sample size: %d\\n", trackIndex, info.size);
                // Check the EOS flag.
                if (info.flags == OH\_AVCodecBufferFlags::AVCODEC\_BUFFER\_FLAGS\_EOS) {
                   isEnd.store(true);
                }
                // Process the buffer data (decode the data as required).
          } else {
                printf("Read sample failed for track %d\\n", trackIndex);
                break;
          }
       }
       // Destroy the buffer.
       OH\_AVBuffer\_Destroy(buffer);
       buffer = nullptr;
       threadFinished.store(true);
    }
    
    // Calculate the buffer size based on your requirements.
    int32\_t audioBufferSize = 4096;  // Typical audio buffer size.
    int32\_t videoBufferSize = w \* h \* 3 >> 1;  // Raw video buffer size.
    
    // Create atomic variables for thread communication.
    std::atomic<bool> audioIsEnd{false}, videoIsEnd{false}; // Specify whether the stream ends.
    std::atomic<bool> audioThreadFinished{false}, videoThreadFinished{false}; // Specify whether the thread is paused.
    
    // Create a thread.
    std::thread audioThread(ReadTrackSamples, demuxer, audioTrackIndex, audioBufferSize,
                            std::ref(audioIsEnd), std::ref(audioThreadFinished));
    std::thread videoThread(ReadTrackSamples, demuxer, videoTrackIndex, videoBufferSize,
                            std::ref(videoIsEnd), std::ref(videoThreadFinished));
    audioThread.join();
    videoThread.join();
    
10.  Destroy the demuxer instance.
     
     // Manually set the instance to nullptr after OH\_AVSource\_Destroy is called. Do not call this API repeatedly for the same instance; otherwise, a program error occurs.
     if (OH\_AVSource\_Destroy(source) != AV\_ERR\_OK) {
        printf("destroy source pointer error");
     }
     source = nullptr;
     // Manually set the instance to nullptr after OH\_AVDemuxer\_Destroy is called. Do not call this API repeatedly for the same instance; otherwise, a program error occurs.
     if (OH\_AVDemuxer\_Destroy(demuxer) != AV\_ERR\_OK) {
        printf("destroy demuxer pointer error");
     }
     demuxer = nullptr;
     close(fd);
     

#### Appendix

## Supported File-Level Attributes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/QzzqK_YHT5ejMILTz-kr7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29B5CDB96C1D99B5FB7E858A958D9C64E6E6C211E3D8715ABC639CE12750ED7B)

Attribute data can be obtained only when the file is parsed normally. If the file information is incorrect or missing, the parsing is abnormal and the corresponding data cannot be obtained.

Currently, data in the GBK character set is converted to UTF-8. If other character sets need to be converted to UTF-8, you must handle the conversion. For details, see [icu4c](https://developer.huawei.com/consumer/en/doc/harmonyos-references/icu4c).

For details about the data type and value range, see [Media Data Key-Value Pairs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).

**Table 1** Supported file-level attributes

| Name | Description |
| :-- | :-- |
| OH\_MD\_KEY\_TITLE | Title. |
| OH\_MD\_KEY\_ARTIST | Artist. |
| OH\_MD\_KEY\_ALBUM | Album. |
| OH\_MD\_KEY\_ALBUM\_ARTIST | Album artist. |
| OH\_MD\_KEY\_DATE | Date. |
| OH\_MD\_KEY\_COMMENT | Comment. |
| OH\_MD\_KEY\_GENRE | Genre. |
| OH\_MD\_KEY\_COPYRIGHT | Copyright. |
| OH\_MD\_KEY\_LANGUAGE | Language. |
| OH\_MD\_KEY\_DESCRIPTION | Description. |
| OH\_MD\_KEY\_LYRICS | Lyrics. |
| OH\_MD\_KEY\_TRACK\_COUNT | Track count. |
| OH\_MD\_KEY\_DURATION | Duration. |
| OH\_MD\_KEY\_START\_TIME | Start time. |

## Supported Track-Level Attributes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/WeYWQDIHSa-fcJ8EGDjNuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5B29D3261F276168E926D461D6B5396FC137EC329D7432298226BF1F6670371)

Attribute data can be obtained only when the file is parsed normally. If the file information is incorrect or missing, the parsing is abnormal and the corresponding data cannot be obtained.

The supported attributes of the auxiliary track must match the actual media type (audio or video).

For details about the data type and value range, see [Media Data Key-Value Pairs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).

**Table 2** Supported track-level attributes

| Name | Description | Supported by Video Tracks | Supported by Audio Tracks | Supported by Subtitle Tracks | Supported by Auxiliary Tracks |
| :-- | :-- | :-- | :-- | :-- | :-- |
| OH\_MD\_KEY\_CODEC\_MIME | Stream codec type. | Supported | Supported | Supported | Supported |
| OH\_MD\_KEY\_TRACK\_TYPE | Stream track type. | Supported | Supported | Supported | Supported |
| OH\_MD\_KEY\_TRACK\_START\_TIME | Start time of the stream. | Supported | Supported | Supported | Supported |
| OH\_MD\_KEY\_BITRATE | Stream bit rate. | Supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_LANGUAGE | Stream language type. | Supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_CODEC\_CONFIG | Codec-specific data. In the case of video, a parameter set is transferred. In the case of audio, parameter configuration information of the decoder is transferred. | Supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_WIDTH | Video stream width. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_HEIGHT | Video stream height. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_FRAME\_RATE | Video stream frame rate. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_ROTATION | Rotation angle of the video stream. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_VIDEO\_SAR | Aspect ratio of the video stream sample. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_PROFILE | Encoding profile of the video stream. This key is valid only for H.265 streams. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_RANGE\_FLAG | Video YUV value range flag of the video stream. This key is valid only for H.265 streams. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | Video primary color of the video stream. This key is valid only for H.265 streams. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | Video transfer characteristics of the video stream. This key is valid only for H.265 streams. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | Video matrix coefficient. This key is valid only for H.265 streams. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | Flag indicating whether the video stream is HDR Vivid. This key is valid only for HDR Vivid streams. | Supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Audio stream sample rate. | Not supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Number of audio stream channels. | Not supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | Encoding channel layout required by the audio stream. | Not supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Audio stream sample format. | Not supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_AAC\_IS\_ADTS | AAC format. This key is valid only for AAC streams. | Not supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE | Number of bits per coded sample in the audio stream. | Not supported | Supported | Not supported | Supported |
| OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | Reference relationship between media file tracks. | Supported | Supported | Supported | Supported |
| OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | Auxiliary track type of the media file. | Not supported | Not supported | Not supported | Supported |
| OH\_MD\_KEY\_TRACK\_DESCRIPTION | Description of the auxiliary track of the media file. | Not supported | Not supported | Not supported | Supported |
