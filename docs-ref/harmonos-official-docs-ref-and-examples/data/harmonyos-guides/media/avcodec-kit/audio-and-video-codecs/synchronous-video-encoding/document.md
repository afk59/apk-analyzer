# Synchronous Video Encoding

Starting from API version 20, video encoding in synchronous mode is supported.

You can call native APIs to perform synchronous video encoding.

For details about the implementation, see [Samples](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec).

For details about the supported encoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#video-encoding).

For details about the restrictions, supported capabilities, and state machine call relationships of video encoding, see [Video Encoding](../video-encoding/document.md).

#### When to Use

Asynchronous mode is generally recommended for most use cases. Synchronous mode can be used if you need to actively request buffers for frame delivery.

#### How to Develop

Read [VideoEncoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h) for the API reference.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/hVFwMdvPS7SwV5ff8CSmHQ/en-us_image_0000002568764889.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5C2BF0B8ECD4E17FB77996333D70EE26C03BC1543DAA1EFE7F100F161588BC5)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_venc.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/qgV2wE6gQgSZhA7blJWRdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=411BA4826F10B45CB41DDA6F5FA8726389DB9D5CC455FAD7EA1DDE20137AB136)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## Defining the Basic Structure

The sample code provided in this section adheres to the C++17 standard and is for reference only.

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videoencoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <multimedia/player\_framework/native\_averrors.h>
    #include <native\_buffer/native\_buffer.h>
    #include <memory>
    #include <fstream>
    #include <mutex>
    #include <shared\_mutex>
    
2.  These global variables are for reference only. They can be encapsulated into an object based on service requirements.
    
    // Video frame width.
    int32\_t width = 320;
    // Video frame height.
    int32\_t height = 240;
    // Video width stride.
    int32\_t widthStride = 0;
    // Video height stride.
    int32\_t heightStride = 0;
    // Video pixel format.
    OH\_AVPixelFormat pixelFormat = AV\_PIXEL\_FORMAT\_NV12;
    // Encoder synchronization lock.
    std::shared\_mutex codecMutex;
    // Pointer to the encoder instance.
    OH\_AVCodec \*videoEnc = nullptr;
    // Encoding output.
    bool outputDone = false;
    // Encoding input.
    bool inputDone = false;
    std::unique\_ptr<std::ifstream> inFile\_;
    

## Surface Mode

The following walks you through how to implement the entire video encoding process in surface mode and implement data rotation in synchronous mode. In this example, surface data is input and encoded into a H.264 stream.

1.  Create an encoder instance.
    
    Create an encoder by name. In the code snippet below, the following variables are used:
    
    -   **videoEnc**: pointer to the video encoder instance.
    -   **capability**: pointer to the encoder's capability.
    -   [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#variables): AVC video codec.
    
    // Create a hardware encoder instance.
    OH\_AVCapability \*capability= OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true, HARDWARE);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByName(name);
    if (videoEnc == nullptr) {
        printf("create videoEnc failed");
        return;
    }
    
2.  Call **OH\_VideoEncoder\_Configure()** to configure the encoder.
    
    -   For details about the configurable options, see [Media Data Key-Value Pairs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).
    -   For details about the parameter verification rules, see [OH\_VideoEncoder\_Configure()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_configure).
    -   The parameter value ranges can be obtained through the capability query interface. For details, see [Obtaining Supported Codecs](../obtaining-supported-codecs/document.md).
    
    Currently, the following options must be configured for all supported formats: video frame width, video frame height, and video pixel format.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set the synchronous mode.
    // Configure the encoder.
    OH\_AVErrCode ret = OH\_VideoEncoder\_Configure(videoEnc, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/QVFyA185TDeAy5V8VCZ8Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8ADA59F7AE2FFAADE1D257691185C4C1022421AD64B99EC835930F9CCFEEBF62)
    
    1.  To enable video encoding in synchronous mode, **OH\_MD\_KEY\_ENABLE\_SYNC\_MODE** must be set to **1**.
    2.  To use synchronous mode, do not call **OH\_VideoEncoder\_RegisterCallback** or **OH\_VideoEncoder\_RegisterParameterCallback** in prior to **OH\_VideoEncoder\_Configure**. Otherwise, the encoder will run in asynchronous mode instead.
    3.  Synchronous mode is not supported for frame-specific channels in surface mode.
    
3.  Set the surface.
    
    In the code snippet below, the following variables are used:
    
    **nativeWindow**: For details about how to obtain the native window, see step 6 in [Surface Mode](../video-encoding/document.md#surface-mode).
    
    // Obtain the surface used for data input.
    OH\_AVErrCode ret = OH\_VideoEncoder\_GetSurface(videoEnc, &nativeWindow);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Call **OH\_VideoEncoder\_Prepare()** to prepare internal resources for the encoder.
    
    OH\_AVErrCode ret = OH\_VideoEncoder\_Prepare(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Call **OH\_VideoEncoder\_Start()** to start the encoder.
    
    // Configure the paths of the input and output files.
    std::string\_view outputFilePath = "/\*yourpath\*.h264";
    std::unique\_ptr<std::ofstream> outputFile = std::make\_unique<std::ofstream>();
    if (outputFile != nullptr) {
        outputFile->open(outputFilePath.data(), std::ios::out | std::ios::binary | std::ios::ate);
    }
    // Start the encoder.
    OH\_AVErrCode ret = OH\_VideoEncoder\_Start(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Obtain an available buffer and release the encoded frame.
    
    -   Call [OH\_VideoEncoder\_QueryOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_queryoutputbuffer) to obtain the index of the next available output buffer.
    -   Based on this index, call [OH\_VideoEncoder\_GetOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_getoutputbuffer) to obtain the buffer instance.
    -   Call [OH\_VideoEncoder\_FreeOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_freeoutputbuffer) to release the encoded frame.
    
    bool EncoderOutput(OH\_AVCodec \*videoEnc, int64\_t timeoutUs)
    {
        uint32\_t index;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoEncoder\_QueryOutputBuffer(videoEnc, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoEncoder\_GetOutputBuffer(videoEnc, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
            
                // Obtain the encoded information.
                OH\_AVCodecBufferAttr info;
                OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(buffer, &info);
                if (getBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                if (info.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                    outputDone = 1;
                }
    
                // Write the encoded frame data (specified by buffer) to the output file.
                uint8\_t \*addr = OH\_AVBuffer\_GetAddr(buffer);
                if (addr == nullptr) {
                   // Handle exceptions.
                   return false;
                }
                if (outputFile != nullptr && outputFile->is\_open()) {
                    outputFile->write(reinterpret\_cast<char \*>(addr), info.size);
                }
                // Free the output buffer. index is the index of the buffer.
                OH\_AVErrCode freeOutputRet = OH\_VideoEncoder\_FreeOutputBuffer(videoEnc, index);
                if (freeOutputRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                break;
            }
            case AV\_ERR\_TRY\_AGAIN\_LATER: {
                break;
            }
            case AV\_ERR\_STREAM\_CHANGED: {
                auto format = std::shared\_ptr<OH\_AVFormat>(OH\_VideoEncoder\_GetOutputDescription(videoEnc), OH\_AVFormat\_Destroy);
                if (format == nullptr) {
                    // Handle exceptions.
                }
                // Obtain the new width and height.
                bool getIntRet = OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, &width) &&
                                 OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, &height);
                if (!getIntRet) {
                    // Handle exceptions.
                }
                break;
            }
            default: {
                // Handle exceptions.
                return false;
            }
        }
        return true;
    }
    
7.  Enable the encoder to output frames in a loop.
    
    bool result = true;
    int64\_t timeoutUs = 0; // Unit: μs. A negative value means to wait infinitely. The value 0 means to return immediately. A positive value means to wait for the specified time before exiting.
    
    while (!outputDone && result) {
        if (!outputDone ) {
            result = EncoderOutput(videoEnc, timeoutUs);
        }
    }
    
8.  Call **OH\_VideoEncoder\_NotifyEndOfStream()** to notify the encoder of EOS.
    
    // In surface mode, you only need to call this API to notify the encoder of EOS.
    OH\_AVErrCode ret = OH\_VideoEncoder\_NotifyEndOfStream(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
9.  (Optional) Call **OH\_VideoEncoder\_Flush()** to refresh the encoder.
    
    After **OH\_VideoEncoder\_Flush** is called, the encoder remains in the Running state, but the input and output data and parameter set (such as the H.264 PPS/SPS) buffered in the encoder are cleared. To continue encoding, you must call **OH\_VideoEncoder\_Start** again.
    
    // Use codecMutex to avoid the problem where the encoding thread keeps running and exits the loop after the Flush API is called and the state is changed.
    std::unique\_lock<std::shared\_mutex> lock(codecMutex);
    // Refresh the encoder.
    OH\_AVErrCode flushRet = OH\_VideoEncoder\_Flush(videoEnc);
    if (flushRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    // Start encoding again.
    OH\_AVErrCode startRet = OH\_VideoEncoder\_Start(videoEnc);
    if (startRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  (Optional) Call **OH\_VideoEncoder\_Reset()** to reset the encoder.
     
     After **OH\_VideoEncoder\_Reset** is called, the encoder returns to the initialized state. To continue encoding, you must call [OH\_VideoEncoder\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_configure) and [OH\_VideoEncoder\_Prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_prepare).
     
     // Reset the encoder.
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     OH\_AVErrCode resetRet = OH\_VideoEncoder\_Reset(videoEnc);
     if (resetRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     // Reconfigure the encoder.
     auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
     if (format == nullptr) {
         // Handle exceptions.
     }
     OH\_AVErrCode configRet = OH\_VideoEncoder\_Configure(videoEnc, format.get());
     if (configRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     // The encoder is ready again.
     OH\_AVErrCode prepareRet = OH\_VideoEncoder\_Prepare(videoEnc);
     if (prepareRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/tdi22KNWRKy9-4wJBi94VA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3F5EDBAC168A402F431FDA40B239599C36F0060FE1D66D8B08EC37470572073)
     
     When the encoder returns to the initialized state, you must call **OH\_VideoEncoder\_Configure** to set **OH\_MD\_KEY\_ENABLE\_SYNC\_MODE** to **1** to reconfigure the encoder parameters. Otherwise, the encoder will run in asynchronous mode.
     
11.  (Optional) Call **OH\_VideoEncoder\_Stop()** to stop the encoder.
     
     After **OH\_VideoEncoder\_Stop** is called, the encoder retains the encoding instance and releases the input and output buffers. You can call **OH\_VideoEncoder\_Start** to continue encoding.
     
     // Stop the encoder.
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     OH\_AVErrCode ret = OH\_VideoEncoder\_Stop(videoEnc);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
12.  Call **OH\_VideoEncoder\_Destroy()** to destroy the encoder instance and release resources.
     
     // Destroy the encoder.
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     OH\_AVErrCode ret = AV\_ERR\_OK;
     if (videoEnc != nullptr) {
         OH\_VideoEncoder\_Destroy(videoEnc);
         videoEnc = nullptr;
     }
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Loox2jMyQtOjJGqaRyt6FQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3332AE4C44793858D4B878C30D7BD10E41F2793E5AF3F2264BFB706A0D11BFA7)
     
     After the call, you must set a null pointer to the encoder to prevent program errors caused by wild pointers.
     

## Buffer Mode

The following walks you through how to implement the entire video encoding process in buffer mode and implement data rotation in synchronous mode. It uses the YUV file input and H.264 encoding format as an example.

1.  Create an encoder instance.
    
    The procedure is the same as that in surface mode and is not described here.
    
    // Create an encoder by name. If your application has special requirements, for example, expecting an encoder that supports a certain resolution, you can call OH\_AVCodec\_GetCapability to query the capability first.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByName(name);
    if (videoEnc == nullptr) {
        printf("create videoEnc failed");
        return;
    }
    
2.  Call **OH\_VideoEncoder\_Configure()** to configure the encoder.
    
    The procedure is the same as that in surface mode and is not described here.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set the synchronous mode.
    // Configure the encoder.
    OH\_AVErrCode ret = OH\_VideoEncoder\_Configure(videoEnc, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/a4jVRhGbS4ubR0G3XgbunA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F1EC168ADFF3EE669B204CC4D86994E57AF5E3EDB72B3233B8547618BF80CE5)
    
    1.  To enable video encoding in synchronous mode, **OH\_MD\_KEY\_ENABLE\_SYNC\_MODE** must be set to **1**.
    2.  To use synchronous mode, do not call **OH\_VideoEncoder\_RegisterCallback** or **OH\_VideoEncoder\_RegisterParameterCallback** in prior to **OH\_VideoEncoder\_Configure**. Otherwise, the encoder will run in asynchronous mode instead.
    
3.  Call **OH\_VideoEncoder\_Prepare()** to prepare internal resources for the encoder.
    
    ret = OH\_VideoEncoder\_Prepare(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Call **OH\_VideoEncoder\_Start()** to start the encoder.
    
    Configure the input and output files.
    
    // Configure the paths of the input and output files.
    std::string\_view inputFilePath = "/\*yourpath\*.yuv";
    std::string\_view outputFilePath = "/\*yourpath\*.h264";
    std::unique\_ptr<std::ifstream> inputFile = std::make\_unique<std::ifstream>();
    std::unique\_ptr<std::ofstream> outputFile = std::make\_unique<std::ofstream>();
    if (inputFile != nullptr) {
        inputFile->open(inputFilePath.data(), std::ios::in | std::ios::binary);
    }
    if (outputFile != nullptr) {
        outputFile->open(outputFilePath.data(), std::ios::out | std::ios::binary | std::ios::ate);
    }
    // Start the encoder.
    OH\_AVErrCode ret = OH\_VideoEncoder\_Start(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Obtain an available buffer and write the bitstream to the encoder.
    
    -   Call [OH\_VideoEncoder\_QueryInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_queryinputbuffer) to obtain the index of the next available input buffer.
    -   Based on this index, call [OH\_VideoEncoder\_GetInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_getinputbuffer) to obtain the buffer instance.
    -   Write the data to be encoded to the buffer, and call [OH\_VideoEncoder\_PushInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_pushinputbuffer) to push it into the encoding input queue for encoding. Once the last frame of data is sent to the input buffer for encoding, set the flag to [AVCODEC\_BUFFER\_FLAGS\_EOS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-info-h#oh_avcodecbufferflags) to notify the encoder that the input is complete.
    
    The meanings of the variables **size**, **offset**, **pts**, **frameData**, and **flags** in the example are the same as those in surface mode.
    
    bool EncoderInput(OH\_AVCodec \*videoEnc, int64\_t timeoutUs)
    {
        uint32\_t index;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoEncoder\_QueryInputBuffer(videoEnc, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoEncoder\_GetInputBuffer(videoEnc, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
    
                // Write image data.
                int32\_t frameSize = 0;
                bool isFirstFrame = true;
                // Obtain the video width stride and height stride.
                if (isFirstFrame) {
                    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_VideoEncoder\_GetInputDescription(videoEnc), OH\_AVFormat\_Destroy);
                    if (format == nullptr) {
                        // Handle exceptions.
                    }
                    bool getIntRet = OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_STRIDE, &widthStride) &&
                                     OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &heightStride);
                     if (!getIntRet) {
                        // Handle exceptions.
                     }
                    isFirstFrame = false;
                }
                if (widthStride == width && heightStride == height) {
                    frameSize = width \* height \* 3 / 2; // Formula for calculating the data size of each frame in NV12 pixel format.
                    // Process the file stream and obtain the frame length, and then write the data to encode to the buffer of the specified index.
                    uint8\_t \*addr = OH\_AVBuffer\_GetAddr(buffer);
                    if (addr == nullptr) {
                       // Handle exceptions.
                       return false;
                    }
                    if (inputFile != nullptr && inputFile->is\_open()) {
                        inputFile->read(reinterpret\_cast<char \*>(addr), frameSize);
                    }
                } else {
                    // If the stride is not equal to the width, perform offset based on the stride. For details, see step 8 in "Buffer Mode in Video Encoding".
                }
    
                // Configure the buffer information.
                OH\_AVCodecBufferAttr info;
                info.size = frameSize;
                info.offset = 0;
                // Unlike the surface mode, in buffer mode, the application must explicitly set pts. Compute it based on the intended display time, for example, frameIndex \* 1000000 / frameRate.
                info.pts = 0;
                // Set the AVCODEC\_BUFFER\_FLAGS\_EOS flag when the last frame of data is input.
                // info.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
                // To prevent the flags from being randomly initialized to AVCODEC\_BUFFER\_FLAGS\_EOS and causing abnormal usage, the flags must be assigned a value such as 0 (identifier for normal frames).
                info.flags = 0;
                OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(buffer, &info);
                if (setBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                // Send the data to the input buffer for encoding. index is the index of the buffer.
                OH\_AVErrCode pushInputRet = OH\_VideoEncoder\_PushInputBuffer(videoEnc, index);
                if (pushInputRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                if (inFile\_->eof()) {
                    inputDone = 1;
                }
                break;
            }
            case AV\_ERR\_TRY\_AGAIN\_LATER: {
                break;
            }
            default: {
                // Handle exceptions.
                return false;
            }
        }
        return true;
    }
    
6.  Obtain an available buffer and release the encoded frame.
    
    -   Call [OH\_VideoEncoder\_QueryOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_queryoutputbuffer) to obtain the index of the next available output buffer.
    -   Based on this index, call [OH\_VideoEncoder\_GetOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_getoutputbuffer) to obtain the buffer instance.
    -   Call [OH\_VideoEncoder\_FreeOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_freeoutputbuffer) to release the encoded frame.
    
    bool EncoderOutput(OH\_AVCodec \*videoEnc, int64\_t timeoutUs)
    {
        uint32\_t index;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoEncoder\_QueryOutputBuffer(videoEnc, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoEncoder\_GetOutputBuffer(videoEnc, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
            
                // Obtain the encoded information.
                OH\_AVCodecBufferAttr info;
                OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(buffer, &info);
                if (getBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                // Write the encoded frame data (specified by buffer) to the output file.
                uint8\_t \*addr = OH\_AVBuffer\_GetAddr(buffer);
                if (addr == nullptr) {
                   // Handle exceptions.
                   return false;
                }
                if (outputFile != nullptr && outputFile->is\_open()) {
                    outputFile->write(reinterpret\_cast<char \*>(addr), info.size);
                }
                if (info.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                    outputDone = 1;
                }
                // Free the output buffer. index is the index of the buffer.
                OH\_AVErrCode freeOutputRet = OH\_VideoEncoder\_FreeOutputBuffer(videoEnc, index);
                if (freeOutputRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                break;
            }
            case AV\_ERR\_TRY\_AGAIN\_LATER: {
                break;
            }
            case AV\_ERR\_STREAM\_CHANGED: {
                break;
            }
            default: {
                // Handle exceptions.
                return false;
            }
        }
        return true;
    }
    
7.  Enable the encoder to input and output frames in a loop.
    
    bool result = true;
    int64\_t timeoutUs = 0; // Unit: μs. A negative value means to wait infinitely. The value 0 means to return immediately. A positive value means to wait for the specified time before exiting.
    
    while (!outputDone && result) {
        if (!inputDone) {
            result = EncoderInput(videoEnc, timeoutUs);
        }
        if (!outputDone) {
            result = EncoderOutput(videoEnc, timeoutUs);
        }
    }
    

The subsequent processes (including refreshing, resetting, stopping, and destroying the encoder) are the same as those in surface mode. For details, see steps 9–12 in [Surface Mode](#surface-mode).
