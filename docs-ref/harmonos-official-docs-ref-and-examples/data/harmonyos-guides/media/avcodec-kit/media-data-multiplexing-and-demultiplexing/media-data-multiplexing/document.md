# Media Data Multiplexing

You can call native APIs to multiplex audio and video streams, that is, to store encoded audio and video data to a file in a certain format.

For details about the supported multiplexing formats, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#media-data-multiplexing).

To multiplex HDR Vivid video streams, set MimeType to H265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC). This feature is supported since API version 11.

**When to Use**

-   Video and audio recording
    
    After you encode audio and video streams, multiplex them into files.
    
-   Audio and video editing
    
    After you edit audio and video, multiplex them into files.
    
-   Audio and video transcoding
    
    After you transcode audio and video, multiplex them into files.
    

#### Development Guidelines

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avmuxer-h).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/vdJM30BlTw-a95RN6LovAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75D2A7660684819EF78426CB920059E68F351BF92F2195B6F964CC1B6A467164)

To call the AVMuxer module to write a local file, request the ohos.permission.READ\_MEDIA and ohos.permission.WRITE\_MEDIA permissions by following the instructions provided in [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_avmuxer.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

## How to Develop

The following walks you through how to implement the entire process of audio and video multiplexing. It uses the MP4 format as an example.

For details about the keys to be configured for different container formats, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#media-data-multiplexing).

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avmuxer.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fcntl.h>
    
2.  Call **OH\_AVMuxer\_Create()** to create an OH\_AVMuxer instance.
    
    // Set the container format to MP4.
    OH\_AVOutputFormat format = AV\_OUTPUT\_FORMAT\_MPEG\_4;
    // Create an FD in read/write mode.
    int32\_t fd = open("test.mp4", O\_CREAT | O\_RDWR | O\_TRUNC, S\_IRUSR | S\_IWUSR);
    OH\_AVMuxer \*muxer = OH\_AVMuxer\_Create(fd, format);
    
3.  (Optional) Call **OH\_AVMuxer\_SetRotation()** to set the rotation angle.
    
    // Set the rotation angle when a video image needs to be rotated.
    OH\_AVMuxer\_SetRotation(muxer, 0);
    
4.  Add file-level data.
    
    For details about the defined keys of file-level data, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#media-data-multiplexing).
    
    Custom keys must start with **com.openharmony.**. The value type can be int32\_t, float, or string. The value type uint8\_t\* is supported since API version 20.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/EXRCZEWEShSCOde7VRtJhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69A0D935016CB3C5A45F71AF41FCD1FD4AB0FE5F8B44FD6DFFE7F09B4089D5FA)
    
    The defined keys must be set before **OH\_AVMuxer\_Start()** is called, and custom keys can be set before **OH\_AVMuxer\_Stop()** is called.
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create(); // Call OH\_AVFormat\_Create to create a format.
    
    // Set the defined keys.
    OH\_AVFormat\_SetStringValue(format, OH\_MD\_KEY\_CREATION\_TIME, "2024-12-28T00:00:00:000000Z"); // Set the creation time (UTC time in ISO 8601 format). This is supported since API version 14.
    OH\_AVFormat\_SetStringValue(format, OH\_MD\_KEY\_COMMENT, "comment test"); // Set the comment. The value is a string. This is supported since API version 20.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT, 1); // Set whether the moov metadata should be at the front of a media file. This is supported since API version 20. The default value is 0. The value 1 indicates that the moov metadata is at the front of a media file.
    
    // Set a custom key (starting with com.openharmony.).
    OH\_AVFormat\_SetIntValue(format, "com.openharmony.testInt", 1024); // The value type is int32\_t.
    OH\_AVFormat\_SetFloatValue(format, "com.openharmony.testFloat", 1.024); // The value type is float.
    OH\_AVFormat\_SetStringValue(format, "com.openharmony.testString", "string test"); // The value type is string, and the length cannot exceed 256 characters.
    uint8\_t testData\[\] = {1, 2, 3};
    OH\_AVFormat\_SetBuffer(format, "com.openharmony.testBuffer", testData, sizeof(testData)); // The value type is uint8\_t\*, which is supported since API version 20.
    
    int ret = OH\_AVMuxer\_SetFormat(muxer, format); // Set format data to the muxer.
    if (ret != AV\_ERR\_OK) {
       // Failed to set the format because no valid key data to be written is found.
    }
    OH\_AVFormat\_Destroy(format); // Destroy the format.
    
5.  Add an audio track.
    
    **Method 1: Use OH\_AVFormat\_Create to create the format.**
    
    int audioTrackId = -1;
    uint8\_t \*buffer = ...; // Encoding configuration data. If there is no configuration data, leave the parameter unspecified.
    size\_t size = ...;  // Length of the encoding configuration data. Set this parameter based on project requirements.
    OH\_AVFormat \*formatAudio = OH\_AVFormat\_Create(); // Call OH\_AVFormat\_Create to create a format. The following showcases how to multiplex an AAC-LC audio with the sample rate of 44100 Hz and two audio channels.
    OH\_AVFormat\_SetStringValue(formatAudio, OH\_MD\_KEY\_CODEC\_MIME, OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatAudio, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, 44100); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatAudio, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, 2); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatAudio, OH\_MD\_KEY\_PROFILE, AAC\_PROFILE\_LC); // Optional.
    OH\_AVFormat\_SetBuffer(formatAudio, OH\_MD\_KEY\_CODEC\_CONFIG, buffer, size); // Optional.
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &audioTrackId, formatAudio);
    if (ret != AV\_ERR\_OK || audioTrackId < 0) {
        // Failure to add the audio track.
    }
    OH\_AVFormat\_Destroy (formatAudio); // Destroy the format.
    
    **Method 2: Use OH\_AVFormat\_CreateAudioFormat to create the format.**
    
    int audioTrackId = -1;
    uint8\_t \*buffer = ...; // Encoding configuration data. If there is no configuration data, leave the parameter unspecified.
    size\_t size = ...;  // Length of the encoding configuration data. Set this parameter based on project requirements.
    OH\_AVFormat \*formatAudio = OH\_AVFormat\_CreateAudioFormat(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, 44100, 2);
    OH\_AVFormat\_SetIntValue(formatAudio, OH\_MD\_KEY\_PROFILE, AAC\_PROFILE\_LC); // Optional.
    OH\_AVFormat\_SetBuffer(formatAudio, OH\_MD\_KEY\_CODEC\_CONFIG, buffer, size); // Optional.
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &audioTrackId, formatAudio);
    if (ret != AV\_ERR\_OK || audioTrackId < 0) {
        // Failure to add the audio track.
    }
    OH\_AVFormat\_Destroy (formatAudio); // Destroy the format.
    
6.  Add a video track.
    
    **Method 1: Use OH\_AVFormat\_Create to create the format.**
    
    int videoTrackId = -1;
    uint8\_t \*buffer = ...; // Encoding configuration data. If there is no configuration data, leave the parameter unspecified.
    size\_t size = ...;  // Length of the encoding configuration data. Set this parameter based on project requirements.
    OH\_AVFormat \*formatVideo = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetStringValue(formatVideo, OH\_MD\_KEY\_CODEC\_MIME, OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_WIDTH, 1280); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_HEIGHT, 720); // Mandatory.
    OH\_AVFormat\_SetBuffer(formatVideo, OH\_MD\_KEY\_CODEC\_CONFIG, buffer, size); // Optional.
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &videoTrackId, formatVideo);
    if (ret != AV\_ERR\_OK || videoTrackId < 0) {
        // Failure to add the video track.
    }
    OH\_AVFormat\_Destroy(formatVideo); // Destroy the format.
    
    **Method 2: Use OH\_AVFormat\_CreateVideoFormat to create the format.**
    
    int videoTrackId = -1;
    uint8\_t \*buffer = ...; // Encoding configuration data. If there is no configuration data, leave the parameter unspecified.
    size\_t size = ...;  // Length of the encoding configuration data. Set this parameter based on project requirements.
    OH\_AVFormat \*formatVideo = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, 1280, 720);
    OH\_AVFormat\_SetBuffer(formatVideo, OH\_MD\_KEY\_CODEC\_CONFIG, buffer, size); // Optional.
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &videoTrackId, formatVideo);
    if (ret != AV\_ERR\_OK || videoTrackId < 0) {
        // Failure to add the video track.
    }
    OH\_AVFormat\_Destroy(formatVideo); // Destroy the format.
    
7.  Add an auxiliary track.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/i94dsNGzRuyoijQYl1nUjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F01668E4C565036A009927942EB39724D706D0584FCFA49AA285C43A17C04275)
    
    To add an auxiliary track, set **OH\_MD\_KEY\_TRACK\_TYPE** to **MEDIA\_TYPE\_AUXILIARY**.
    
    When setting **OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE**, choose from **hint**, **cdsc**, **font**, **hind**, **vdep**, **vplx**, **subt**, **thmb**, **auxl**, **cdtg**, **shsc**, or **aest**.
    
    When setting **OH\_MD\_KEY\_TRACK\_DESCRIPTION**, use a string that starts with **"com.openharmony."** and contains no more than 256 characters.
    
    When setting **OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS**, ensure that the track ID is greater than or equal to 0 and refers to an existing track.
    
    Add an audio auxiliary track.
    
    int32\_t audioAuxlTrackId = -1;
    std::vector<int32\_t> audioTrackIDsVector = {0}; // Set the IDs of the audio auxiliary tracks based on the actual situation. Multiple values can be entered.
    int32\_t \*audioAuxlTrackIDs = audioTrackIDsVector.data();
    OH\_AVFormat \*audioAuxlFormat = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetStringValue(audioAuxlFormat, OH\_MD\_KEY\_CODEC\_MIME, OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC); // Mandatory.
    OH\_AVFormat\_SetIntValue(audioAuxlFormat, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, 44100); // Mandatory.
    OH\_AVFormat\_SetIntValue(audioAuxlFormat, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, 2); // Mandatory.
    OH\_AVFormat\_SetIntValue(audioAuxlFormat, OH\_MD\_KEY\_PROFILE, AAC\_PROFILE\_LC); // Optional.
    OH\_AVFormat\_SetIntValue(audioAuxlFormat, OH\_MD\_KEY\_TRACK\_TYPE, static\_cast<int32\_t>(OH\_MediaType::MEDIA\_TYPE\_AUXILIARY)); // Mandatory.
    OH\_AVFormat\_SetStringValue(audioAuxlFormat, OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE, "auxl"); // Mandatory.
    OH\_AVFormat\_SetStringValue(audioAuxlFormat, OH\_MD\_KEY\_TRACK\_DESCRIPTION, "com.openharmony.audiomode.auxiliary"); // Mandatory.
    OH\_AVFormat\_SetIntBuffer(audioAuxlFormat, OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS, audioAuxlTrackIDs, audioTrackIDsVector.size()); // Mandatory.
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &audioAuxlTrackId, audioAuxlFormat);
    if (ret != AV\_ERR\_OK || audioAuxlTrackId < 0) {
        // Failed to add the audio auxiliary track.
    }
    
    Add a video auxiliary track.
    
    int32\_t videoAuxlTrackId = -1;
    std::vector<int32\_t> videoTrackIDsVector = {0}; // Set the IDs of the video auxiliary tracks based on the actual situation. Multiple values can be entered.
    int32\_t \*videoAuxlTrackIDs = videoTrackIDsVector.data();
    OH\_AVFormat \*videoAuxlFormat = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetStringValue(videoAuxlFormat, OH\_MD\_KEY\_CODEC\_MIME, OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC); // Mandatory.
    OH\_AVFormat\_SetIntValue(videoAuxlFormat, OH\_MD\_KEY\_WIDTH, 1280); // Mandatory.
    OH\_AVFormat\_SetIntValue(videoAuxlFormat, OH\_MD\_KEY\_HEIGHT, 720); // Mandatory.
    OH\_AVFormat\_SetIntValue(videoAuxlFormat, OH\_MD\_KEY\_TRACK\_TYPE, static\_cast<int32\_t>(OH\_MediaType::MEDIA\_TYPE\_AUXILIARY)); // Mandatory.
    OH\_AVFormat\_SetStringValue(videoAuxlFormat, OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE, "vdep"); // Mandatory.
    OH\_AVFormat\_SetStringValue(videoAuxlFormat, OH\_MD\_KEY\_TRACK\_DESCRIPTION, "com.openharmony.moviemode.depth"); // Mandatory.
    OH\_AVFormat\_SetIntBuffer(videoAuxlFormat, OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS, videoAuxlTrackIDs, videoTrackIDsVector.size()); // Mandatory.
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &videoAuxlTrackId, videoAuxlFormat);
    if (ret != AV\_ERR\_OK || videoAuxlTrackId < 0) {
        // Failed to add the video auxiliary track.
    }
    
8.  Add a cover track.
    
    **Method 1: Use OH\_AVFormat\_Create to create the format.**
    
    int coverTrackId = -1;
    OH\_AVFormat \*formatCover = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetStringValue(formatCover, OH\_MD\_KEY\_CODEC\_MIME, OH\_AVCODEC\_MIMETYPE\_IMAGE\_JPG);
    OH\_AVFormat\_SetIntValue(formatCover, OH\_MD\_KEY\_WIDTH, 1280);
    OH\_AVFormat\_SetIntValue(formatCover, OH\_MD\_KEY\_HEIGHT, 720);
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &coverTrackId, formatCover);
    if (ret != AV\_ERR\_OK || coverTrackId < 0) {
        // Failure to add the cover track.
    }
    OH\_AVFormat\_Destroy(formatCover); // Destroy the format.
    
    **Method 2: Use OH\_AVFormat\_CreateVideoFormat to create the format.**
    
    int coverTrackId = -1;
    OH\_AVFormat \*formatCover = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_IMAGE\_JPG, 1280, 720);
    
    int ret = OH\_AVMuxer\_AddTrack(muxer, &coverTrackId, formatCover);
    if (ret != AV\_ERR\_OK || coverTrackId < 0) {
        // Failure to add the cover track.
    }
    OH\_AVFormat\_Destroy(formatCover); // Destroy the format.
    
9.  Call **OH\_AVMuxer\_Start()** to start multiplexing.
    
    // Call Start() to write the file header. After this API is called, you cannot set media parameters or add tracks.
    if (OH\_AVMuxer\_Start(muxer) != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  Call **OH\_AVMuxer\_WriteSampleBuffer()** to write data.
     
     The encapsulated data includes video, audio, and cover data.
     
     // Data can be written only after Start() is called.
     int size = ...;
     OH\_AVBuffer \*sample = OH\_AVBuffer\_Create(size); // Create an AVBuffer instance.
     // Write data to the sample buffer by using OH\_AVBuffer\_GetAddr(sample). For details, see the usage of OH\_AVBuffer.
     // Multiplex the cover. One image must be written at a time.
     
     // Set buffer information.
     OH\_AVCodecBufferAttr info = {0};
     info.pts =...; // Playback start time of the current data, in microseconds. The relative time is used.
     info.size = size; // Length of the current data.
     info.offset = 0; // Offset. Generally, the value is 0.
     info.flags |= AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME; // Flag of the current data. For details, see OH\_AVCodecBufferFlags.
     info.flags |= AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA; // The AVC in annex-b format contains the codec configuration flag.
     OH\_AVBuffer\_SetBufferAttr(sample, &info); // Set the buffer attribute.
     int trackId = audioTrackId; // Select the audio or video track to be written.
     
     int ret = OH\_AVMuxer\_WriteSampleBuffer(muxer, trackId, sample);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
11.  Call **OH\_AVMuxer\_Stop()** to stop multiplexing.
     
     // Call Stop() to write the file trailer. After this API is called, you cannot write media data.
     if (OH\_AVMuxer\_Stop(muxer) != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
12.  Call **OH\_AVMuxer\_Destroy()** to release the instance.
     
     Do not repeatedly destroy the instance. Otherwise, the program may crash.
     
     if (OH\_AVMuxer\_Destroy(muxer) != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     muxer = NULL;
     close(fd); // Close the FD.
