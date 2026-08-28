# HDR Vivid Video Recording

You can call the native APIs of this module to support HDR Vivid video recording.

The main process of video recording is as follows: camera capture, encoding, and multiplexing into MP4 files.

#### Encoding an HDR Vivid Video

The application creates an H.265 encoder and configures the profile (main 10) for the camera feed from the bottom surface buffer of HDR Vivid. The encoder then processes the surface buffer encoding to generate the corresponding video streams.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/qCYUjCiRTCqie-wZh6Eq0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91554F6E2135201D3EF8B8A6E6980F78D790E4FCFB640DA7F834648D89A7F679)

HDR Vivid video encoding is supported only in surface mode.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_avdemuxer.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_avsource.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/EeTMGV9MTbic5lnvTKGlaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93ACD656E56E97BCEE6F736340CEBE99DD5AAC7B956D4C9BCF1ED86019FEA8EB)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videoencoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fstream>
    
2.  Create an encoder instance.
    
    You can create an encoder by name or MIME type. In the code snippet below, the following variables are used:
    
    -   **videoEnc**: pointer to the video encoder instance.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC**: HEVC video codec.
    
    // Create an H.265 encoder by MIME type.
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    
3.  Configure the asynchronous callback function.
    
    Add the header files.
    
    #include <condition\_variable>
    #include <queue>
    #include <mutex>
    
    struct CodecBufferInfo {
        uint32\_t bufferIndex = 0;
        OH\_AVBuffer \*buffer = nullptr;
        uint8\_t \*bufferAddr = nullptr;
        OH\_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC\_BUFFER\_FLAGS\_NONE};
    };
    std::mutex outputMutex\_;
    std::condition\_variable outputCond\_;
    std::queue<CodecBufferInfo> outputBufferInfoQueue\_;
    
    // Set the OH\_AVCodecOnNewOutputBuffer callback function, which is used to send an encoded frame to the output queue.
    void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData) {
        (void)codec;
        std::unique\_lock<std::mutex> lock(outputMutex\_);
        outputBufferInfoQueue\_.emplace(index, buffer);
        outputCond\_.notify\_all();
    }
    
    For details, see "Step 3: Call OH\_VideoEncoder\_RegisterCallback() to set the callback functions" in [Video Encoding in Surface Mode](../../video-encoding/document.md#surface-mode).
    
4.  Configure the encoder.
    
    (Optional) Configure the video frame width, video frame height, and video color format.
    
    // (Mandatory) Set the encoding profile to main 10.
    int32\_t profile = static\_cast<int32\_t>(HEVC\_PROFILE\_MAIN\_10);
    // Configure the video primary color.
    int32\_t primary = static\_cast<int32\_t>(OH\_ColorPrimary::COLOR\_PRIMARY\_BT2020);
    // Configure the transfer characteristics.
    int32\_t transfer = static\_cast<int32\_t>(OH\_TransferCharacteristic::TRANSFER\_CHARACTERISTIC\_PQ);// PQ or HLG.
    // Configure the maximum matrix coefficient.
    int32\_t matrix = static\_cast<int32\_t>(OH\_MatrixCoefficient::MATRIX\_COEFFICIENT\_BT2020\_CL);
    // Configure the key frame interval, in milliseconds.
    int32\_t iFrameInterval = 100;
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, profile);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_COLOR\_PRIMARIES, primary);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS, transfer);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_MATRIX\_COEFFICIENTS, matrix);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_I\_FRAME\_INTERVAL, iFrameInterval);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_RANGE\_FLAG, 1);
    // Configure the encoder.
    int32\_t ret = OH\_VideoEncoder\_Configure(videoEnc, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    OH\_AVFormat\_Destroy(format);
    
5.  Obtain the surface and set it for the camera.
    
    For details, see "Step 6: Obtain the surface" in [Video Encoding in Surface Mode](../../video-encoding/document.md#surface-mode).
    
6.  Call **OH\_VideoEncoder\_Start()** to start the encoder.
    
    For details, see "Step 8: Call OH\_VideoEncoder\_Start() to start the encoder" in [Video Encoding in Surface Mode](../../video-encoding/document.md#surface-mode).
    

#### Multiplexing an HDR Vivid Video

You can multiplex HDR Vivid streams into a file by calling a muxer. Set the stream format to HEVC, and specify the width, height, and isHDRVivid information. Obtain color information from the encoding information, and set this color information appropriately in the muxer.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_avmuxer.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/7RuabAYISbC9_1qsaoGAXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5D749E52B8F40768E677AFCC450CD66EDF353C784324801D870EE81DDA0862A)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avmuxer.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fcntl.h>
    
2.  Call **OH\_AVMuxer\_Create()** to create an **OH\_AVMuxer** instance.
    
    // Set the multiplexing format to MP4.
    OH\_AVOutputFormat outputFormat = AV\_OUTPUT\_FORMAT\_MPEG\_4;
    // Create an FD in read/write mode.
    int32\_t fd = open("test.mp4", O\_CREAT | O\_RDWR | O\_TRUNC, S\_IRUSR | S\_IWUSR);
    OH\_AVMuxer \*muxer = OH\_AVMuxer\_Create(fd, outputFormat);
    
3.  Add a video track and set the type to HDR Vivid.
    
    int videoTrackId = -1;
    uint8\_t \*buffer = ...; // Encoding configuration data. If there is no configuration data, leave the parameter unspecified.
    size\_t size = ...;  // Length of the encoding configuration data. Set this parameter based on project requirements.
    
    OH\_AVFormat \*formatVideo = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetStringValue(formatVideo, OH\_MD\_KEY\_CODEC\_MIME, OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_WIDTH, 1280); // Mandatory.
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_HEIGHT, 720); // Mandatory.
    // (Optional) This parameter is mandatory for HDR Vivid video multiplexing. Specify the video type as HDR Vivid.
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID, 1);
    // (Optional. The muxer automatically parses the encoded stream XPS.) Set the color information.
    // The information can also be obtained from the encoder by calling OH\_VideoEncoder\_GetOutputDescription(OH\_AVCodec \*codec).
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_RANGE\_FLAG, 1);
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_COLOR\_PRIMARIES, OH\_ColorPrimary::COLOR\_PRIMARY\_BT2020);
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS, OH\_TransferCharacteristic::TRANSFER\_CHARACTERISTIC\_PQ); // PQ or HLG.
    OH\_AVFormat\_SetIntValue(formatVideo, OH\_MD\_KEY\_MATRIX\_COEFFICIENTS, OH\_MatrixCoefficient::MATRIX\_COEFFICIENT\_BT2020\_CL);
    
    ret = OH\_AVMuxer\_AddTrack(muxer, &videoTrackId, formatVideo);
    if (ret != AV\_ERR\_OK || videoTrackId < 0) {
        // Failure to add the video track.
    }
    OH\_AVFormat\_Destroy(formatVideo); // Destroy the format.
    

#### Processing Video Frame Data

1.  Write multiplexed data.
    
    // Data can be written only after Start() is called.
    int trackId = videoTrackId; // Select the track to be written.
    // Obtain the callback function OnNewOutputBuffer and save it to the frame buffer of the output queue.
    CodecBufferInfo bufferInfo = outputBufferInfoQueue\_.front();
    outputBufferInfoQueue\_.pop();
    ret = OH\_AVMuxer\_WriteSampleBuffer(muxer, trackId, bufferInfo.buffer);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
2.  Call **OH\_VideoEncoder\_FreeOutputBuffer()** to release the encoded frames.
    
    // Free the output buffer. index is the index of the buffer.
    ret = OH\_VideoEncoder\_FreeOutputBuffer(videoEnc, bufferInfo.bufferIndex);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
