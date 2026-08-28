# Synchronous Video Decoding

Starting from API version 20, video decoding in synchronous mode is supported.

You can call native APIs to perform synchronous video decoding.

For details about the implementation, see [Samples](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec).

For details about the supported decoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#video-decoding).

For details about the restrictions, supported capabilities, and state machine call relationships of video decoding, see [Video Decoding](../video-decoding/document.md).

#### When to Use

Asynchronous mode is generally recommended for most use cases. Synchronous mode can be used if you need to actively request buffers for frame delivery.

#### How to Develop

Read [VideoDecoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h) for the API reference.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/7bVVy5o5QgSx5YwhfZdDkQ/en-us_image_0000002568764895.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0911A8AA58605731AA91D71C0891902E2D988A116D7CCF15C79DD14E43DA87EA)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_vdec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/yddfVEQ0TJCny6OSkH9d0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=716ED24A43BEA12190D3415AC0B53902EF529130295DBF7E2741969F5D4C5B24)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## Defining the Basic Structure

The sample code provided in this section adheres to the C++17 standard and is for reference only.

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>
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
    #include <string.h>
    
2.  These global variables are for reference only. They can be encapsulated into an object based on service requirements.
    
    // Video frame width.
    int32\_t width = 320;
    // Video frame height.
    int32\_t height = 240;
    // Video pixel format.
    OH\_AVPixelFormat pixelFormat = AV\_PIXEL\_FORMAT\_NV12;
    // Decoder synchronization lock.
    std::shared\_mutex codecMutex;
    // Pointer to the decoder instance.
    OH\_AVCodec \*videoDec = nullptr;
    // Decoding output.
    bool outputDone = false;
    // Decoding input.
    bool inputDone = false;
    std::unique\_ptr<std::ifstream> inFile\_;
    

## Surface Mode

The following walks you through how to implement the entire video decoding process in surface mode and implement data rotation in synchronous mode. In this example, an H.264 stream file is input, decoded, and rendered.

1.  Create a decoder instance.
    
    Create a decoder by name. In the code snippet below, the following variables are used:
    
    -   **videoDec**: pointer to the video decoder instance.
    -   **capability**: pointer to the decoder's capability.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC**: AVC video codec.
    
    // Create a hardware decoder instance.
    OH\_AVCapability \*capability= OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false, HARDWARE);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(name);
    if (videoDec == nullptr) {
        printf("create videoDec failed");
        return;
    }
    
2.  Call **OH\_VideoDecoder\_Configure()** to configure the decoder.
    
    -   For details about the configurable options, see [Media Data Key-Value Pairs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).
    -   For details about the parameter verification rules, see [OH\_VideoDecoder\_Configure()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_configure).
    -   The parameter value ranges can be obtained through the capability query interface. For details, see [Obtaining Supported Codecs](../obtaining-supported-codecs/document.md).
    
    Currently, the following options must be configured for all supported formats: video frame width and height.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set synchronous mode.
    // Configure the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Configure(videoDec, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/XzIEQgvVSceadF7llj8U4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13A8DB1489AD5BC1346A2F0A65729831E8DDFCC920B13C0CBF60BD0C7C0AE708)
    
    1.  To enable video decoding in synchronous mode, **OH\_MD\_KEY\_ENABLE\_SYNC\_MODE** must be set to **1**.
    2.  To use synchronous mode, do not call **OH\_VideoDecoder\_RegisterCallback** in prior to **OH\_VideoDecoder\_Configure**. Otherwise, the decoder will run in asynchronous mode instead.
    
3.  Set the surface.
    
    In the code snippet below, the following variables are used:
    
    **nativeWindow**: For details about how to obtain the native window, see step 6 in [Surface Mode](../video-decoding/document.md#surface-mode).
    
    // Set the surface.
    // Set the window parameters.
    OH\_AVErrCode ret = OH\_VideoDecoder\_SetSurface(videoDec, nativeWindow);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Call **OH\_VideoDecoder\_Prepare()** to prepare internal resources for the decoder.
    
    OH\_AVErrCode ret = OH\_VideoDecoder\_Prepare(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Call **OH\_VideoDecoder\_Start()** to start the decoder.
    
    // Start the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Start(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Obtain an available buffer and write the bitstream to the decoder.
    
    -   Call [OH\_VideoDecoder\_QueryInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_queryinputbuffer) to obtain the index of the next available input buffer.
    -   Based on this index, call [OH\_VideoDecoder\_GetInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_getinputbuffer) to obtain the buffer instance.
    -   Write the data to be decoded into the buffer, and call [OH\_VideoDecoder\_PushInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_pushinputbuffer) to push it to the decoder for decoding. When all the data to be processed has been passed to the decoder, set flag to **AVCODEC\_BUFFER\_FLAGS\_EOS** to notify the decoder that the input is complete.
    
    Send the input queue for decoding. In the code snippet below, the following variables are used:
    
    -   **size**, **offset**, **pts**, and **frameData**: size, offset, timestamp, and frame data. For details about how to obtain such information, see step 9 in [Media Data Demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md#how-to-develop).
    -   **flags**: type of the buffer flag. For details, see [OH\_AVCodecBufferFlags](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-info-h#oh_avcodecbufferflags).
    
    bool DecoderInput(OH\_AVCodec \*videoDec, int64\_t timeoutUs)
    {
        uint32\_t index;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoDecoder\_QueryInputBuffer(videoDec, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoDecoder\_GetInputBuffer(videoDec, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
                // Write stream data.
                uint8\_t \*addr = OH\_AVBuffer\_GetAddr(buffer);
                if (addr == nullptr) {
                   // Handle exceptions.
                   return false;
                }
                // Fill in the buffer.
                int32\_t capacity = OH\_AVBuffer\_GetCapacity(buffer);
                if (size > capacity) {
                    // Handle exceptions.
                }
                memcpy(addr, frameData, size);
    
                OH\_AVCodecBufferAttr info;
                // Set the buffer attributes.
                // Configure the size, offset, and timestamp of the frame data.
                info.size = size;
                info.offset = offset;
                info.pts = pts;
                if (inFile\_->eof()) {
                    info.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
                } else {
                    info.flags = flags;
                }
                OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(buffer, &info);
                if (setBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                OH\_AVErrCode pushInputRet = OH\_VideoDecoder\_PushInputBuffer(videoDec, index);
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
    
7.  Obtain an available buffer and release the decoded frame.
    
    -   Call [OH\_VideoDecoder\_QueryOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_queryoutputbuffer) to obtain the index of the next available output buffer.
    -   Based on this index, call [OH\_VideoDecoder\_GetOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_getoutputbuffer) to obtain the buffer instance.
    -   Determine the subsequent operations based on the **isRender** flag. If the decoded frame does not need to be rendered, call [OH\_VideoDecoder\_FreeOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_freeoutputbuffer) to release the decoded frame. If the decoded frame needs to be rendered, you can call [OH\_VideoDecoder\_RenderOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_renderoutputbuffer) to display the decoded frame and automatically release it, or call [OH\_VideoDecoder\_RenderOutputBufferAtTime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_renderoutputbufferattime) to display the decoded frame at a specified time and then release it.
    
    bool DecoderOutput(OH\_AVCodec \*videoDec, int64\_t timeoutUs)
    {
        uint32\_t index;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoDecoder\_QueryOutputBuffer(videoDec, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoDecoder\_GetOutputBuffer(videoDec, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
            
                // Obtain the decoded information.
                OH\_AVCodecBufferAttr info;
                OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(buffer, &info);
                if (getBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                if (info.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                    outputDone = 1;
                }
                
                // Handle the decoded output data.
                // You can determine the value.
                bool isRender;
                bool isNeedRenderAtTime;
                OH\_AVErrCode result = AV\_ERR\_OK;
                if (isRender) {
                    // Render the data and free the output buffer. index is the index of the buffer.
                    if (isNeedRenderAtTime){
                        // Obtain the system absolute time, and call renderTimestamp to display the time based on service requirements.
                        int64\_t renderTimestamp =
                            std::chrono::duration\_cast<std::chrono::nanoseconds>(std::chrono::high\_resolution\_clock::now().time\_since\_epoch()).count();
                        result = OH\_VideoDecoder\_RenderOutputBufferAtTime(videoDec, index, renderTimestamp);
                    } else {
                        result = OH\_VideoDecoder\_RenderOutputBuffer(videoDec, index);
                    }
                } else {
                    // Free the output buffer.
                    result = OH\_VideoDecoder\_FreeOutputBuffer(videoDec, index);
                }
                if (result != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                break;
            }
            case AV\_ERR\_TRY\_AGAIN\_LATER: {
                break;
            }
            case AV\_ERR\_STREAM\_CHANGED: {
                auto format = std::shared\_ptr<OH\_AVFormat>(OH\_VideoDecoder\_GetOutputDescription(videoDec), OH\_AVFormat\_Destroy);
                if (format == nullptr) {
                    // Handle exceptions.
                }
                // Obtain the new width and height.
                bool getIntRet = OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width) &&
                                 OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height);
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
    
8.  Enable the decoder to input and output frames in a loop.
    
    bool result = true;
    int64\_t timeoutUs = 0; // Unit: μs. A negative value means to wait infinitely. The value 0 means to return immediately. A positive value means to wait for the specified time before exiting.
    
    while (!outputDone && result) {
        if (!inputDone) {
            result = DecoderInput(videoDec, timeoutUs);
        }
        if (!outputDone) {
            result = DecoderOutput(videoDec, timeoutUs);
        }
    }
    
9.  (Optional) Call **OH\_VideoDecoder\_Flush()** to refresh the decoder.
    
    After **OH\_VideoDecoder\_Flush** is called, the decoder remains in the Running state, but the input and output data and parameter set (such as the H.264 PPS/SPS) buffered in the decoder are cleared. To continue decoding, you must call **OH\_VideoDecoder\_Start** again.
    
    // Use codecMutex to avoid the problem where the decoding thread keeps running and exits the loop after the Flush API is called and the state is changed.
    std::unique\_lock<std::shared\_mutex> lock(codecMutex);
    // Refresh the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Flush(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    // Start decoding again.
    ret = OH\_VideoDecoder\_Start(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  (Optional) Call **OH\_VideoDecoder\_Reset()** to reset the decoder.
     
     After **OH\_VideoDecoder\_Reset** is called, the decoder returns to the Initialized state. To continue decoding, you must call [OH\_VideoDecoder\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_configure), [OH\_VideoDecoder\_SetSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_setsurface), and [OH\_VideoDecoder\_Prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_prepare).
     
     // Reset the decoder.
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     OH\_AVErrCode resetRet = OH\_VideoDecoder\_Reset(videoDec);
     if (resetRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     // Reconfigure the decoder.
     auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
     if (format == nullptr) {
         // Handle exceptions.
     }
     OH\_AVErrCode configRet = OH\_VideoDecoder\_Configure(videoDec, format.get());
     if (configRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     // Reconfigure the surface in surface mode. This is not required in buffer mode.
     OH\_AVErrCode setRet = OH\_VideoDecoder\_SetSurface(videoDec, nativeWindow);
     if (setRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // The decoder is ready again.
     OH\_AVErrCode prepareRet = OH\_VideoDecoder\_Prepare(videoDec);
     if (prepareRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/UEJ3vQ7qQ2S80r4yOceDTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2AC77E01389F18CC5D45F5A26F480BF48F94C20E53F3D7CF3F47A1020EC9528)
     
     When the decoder returns to the initialized state, you must call **OH\_VideoDecoder\_Configure** to set **OH\_MD\_KEY\_ENABLE\_SYNC\_MODE** to **1** to reconfigure the decoder parameters. Otherwise, the decoder will run in asynchronous mode.
     
11.  (Optional) Call **OH\_VideoDecoder\_Stop()** to stop the decoder.
     
     After **OH\_VideoDecoder\_Stop()** is called, the decoder retains the decoding instance and releases the input and output buffers.
     
     // Stop the decoder.
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     OH\_AVErrCode ret = OH\_VideoDecoder\_Stop(videoDec);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
12.  Call **OH\_VideoDecoder\_Destroy()** to destroy the decoder instance and release resources.
     
     // Call OH\_VideoDecoder\_Destroy to destroy the decoder.
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     OH\_AVErrCode ret = AV\_ERR\_OK;
     if (videoDec != nullptr) {
         OH\_VideoDecoder\_Destroy(videoDec);
         videoDec = nullptr;
     }
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/gNOcIQLUSY-YAFuVQ63HGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72ED7196523523F2653EB82769627AE2459943735E3558646153F362874A34CC)
     
     After the call, you must set a null pointer to the decoder to prevent program errors caused by wild pointers.
     

## Buffer Mode

The following walks you through how to implement the entire video decoding process in buffer mode and implement data rotation in synchronous mode. In this example, an H.264 stream file is input and decoded into a YUV file.

1.  Create a decoder instance.
    
    The procedure is the same as that in surface mode and is not described here.
    
    // To create a decoder by name, call OH\_AVCapability\_GetName to obtain the codec names available and then call OH\_VideoDecoder\_CreateByName. If your application has special requirements, for example, expecting a decoder that supports a certain resolution, you can call OH\_AVCodec\_GetCapability to query the capability first.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(name);
    if (videoDec == nullptr) {
        printf("create videoDec failed");
        return;
    }
    
2.  Call **OH\_VideoDecoder\_Configure()** to configure the decoder.
    
    The procedure is the same as that in surface mode and is not described here.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set synchronous mode.
    // Configure the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Configure(videoDec, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/9wJ95kCnQROU1q0Mn0wSlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B427B43C59708352478874918FB86EBC23C3802883C0DC7B09A87425D5A0AA9A)
    
    1.  To enable video decoding in synchronous mode, **OH\_MD\_KEY\_ENABLE\_SYNC\_MODE** must be set to **1**.
    2.  To use synchronous mode, do not call **OH\_VideoDecoder\_RegisterCallback** in prior to **OH\_VideoDecoder\_Configure**. Otherwise, the decoder will run in asynchronous mode instead.
    
3.  Call **OH\_VideoDecoder\_Prepare()** to prepare internal resources for the decoder.
    
    OH\_AVErrCode ret = OH\_VideoDecoder\_Prepare(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Call **OH\_VideoDecoder\_Start()** to start the decoder.
    
    std::unique\_ptr<std::ofstream> outputFile = std::make\_unique<std::ofstream>();
    if (outputFile != nullptr) {
        outputFile->open("/\*yourpath\*.yuv", std::ios::out | std::ios::binary | std::ios::ate);
    }
    // Start the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Start(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Obtain an available buffer and write the bitstream to the decoder.
    
    -   Call [OH\_VideoDecoder\_QueryInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_queryinputbuffer) to obtain the index of the next available input buffer.
    -   Based on this index, call [OH\_VideoDecoder\_GetInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_getinputbuffer) to obtain the buffer instance.
    -   Write the data to be decoded into the buffer, and call [OH\_VideoDecoder\_PushInputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_pushinputbuffer) to push it to the decoder for decoding. When all the data to be processed has been passed to the decoder, set flag to **AVCODEC\_BUFFER\_FLAGS\_EOS** to notify the decoder that the input is complete.
    
    The meanings of the variables **size**, **offset**, **pts**, **frameData**, and **flags** in the example are the same as those in surface mode.
    
    bool DecoderInput(OH\_AVCodec \*videoDec, int64\_t timeoutUs)
    {
        uint32\_t index;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoDecoder\_QueryInputBuffer(videoDec, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoDecoder\_GetInputBuffer(videoDec, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
                // Write stream data.
                uint8\_t \*addr = OH\_AVBuffer\_GetAddr(buffer);
                if (addr == nullptr) {
                   // Handle exceptions.
                   return false;
                }
                // Fill in the buffer.
                int32\_t capacity = OH\_AVBuffer\_GetCapacity(buffer);
                if (size > capacity) {
                    // Handle exceptions.
                }
                memcpy(addr, frameData, size);
    
                OH\_AVCodecBufferAttr info;
                // Set the buffer attributes.
                // Configure the size, offset, and timestamp of the frame data.
                info.size = size;
                info.offset = offset;
                info.pts = pts;
                if (inFile\_->eof()) {
                    info.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
                } else {
                    info.flags = flags;
                }
                OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(buffer, &info);
                if (setBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                OH\_AVErrCode pushInputRet = OH\_VideoDecoder\_PushInputBuffer(videoDec, index);
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
    
6.  Obtain an available buffer and release the decoded frame.
    
    -   Call [OH\_VideoDecoder\_QueryOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_queryoutputbuffer) to obtain the index of the next available output buffer.
    -   Based on this index, call [OH\_VideoDecoder\_GetOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_getoutputbuffer) to obtain the buffer instance.
    -   Call [OH\_VideoDecoder\_FreeOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_freeoutputbuffer) to release the decoded frame.
    
    bool DecoderOutput(OH\_AVCodec \*videoDec, int64\_t timeoutUs)
    {
        uint32\_t index;
        int32\_t cropTop = 0;
        int32\_t cropBottom = 0;
        int32\_t cropLeft = 0;
        int32\_t cropRight = 0;
        int32\_t widthStride = 0;
        int32\_t heightStride = 0;
        std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    
        OH\_AVErrCode ret = OH\_VideoDecoder\_QueryOutputBuffer(videoDec, &index, timeoutUs);
        switch (ret) {
            case AV\_ERR\_OK: {
                OH\_AVBuffer \*buffer = OH\_VideoDecoder\_GetOutputBuffer(videoDec, index);
                if (buffer == nullptr) {
                    // Handle exceptions.
                    return false;
                }
            
                // Obtain the decoded information.
                OH\_AVCodecBufferAttr info;
                OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(buffer, &info);
                if (getBufferRet != AV\_ERR\_OK) {
                    // Handle exceptions.
                    return false;
                }
                if (info.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                    outputDone = 1;
                }
                
                // Free the output buffer. index is the index of the buffer.
                OH\_AVErrCode freeOutputRet = OH\_VideoDecoder\_FreeOutputBuffer(videoDec, index);
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
                auto format = std::shared\_ptr<OH\_AVFormat>(OH\_VideoDecoder\_GetOutputDescription(videoDec), OH\_AVFormat\_Destroy);
                if (format == nullptr) {
                    // Handle exceptions.
                }
                // Obtain the new video width, height, and stride.
                bool getIntRet = OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width) &&
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height) &&
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_STRIDE, &widthStride) &&
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &heightStride) &&
                           // (Optional) Obtain the cropped rectangle information.
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_TOP, &cropTop) &&
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM, &cropBottom) &&
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_LEFT, &cropLeft) &&
                           OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT, &cropRight);
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
    
7.  Enable the decoder to input and output frames in a loop.
    
    bool result = true;
    int64\_t timeoutUs = 0; // Unit: μs. A negative value means to wait infinitely. The value 0 means to return immediately. A positive value means to wait for the specified time before exiting.
    
    while (!outputDone && result) {
        if (!inputDone) {
            result = DecoderInput(videoDec, timeoutUs);
        }
        if (!outputDone) {
            result = DecoderOutput(videoDec, timeoutUs);
        }
    }
    

The subsequent processes (including refreshing, resetting, stopping, and destroying the decoder) are the same as those in surface mode. For details, see steps 9–12 in [Surface Mode](#surface-mode).
