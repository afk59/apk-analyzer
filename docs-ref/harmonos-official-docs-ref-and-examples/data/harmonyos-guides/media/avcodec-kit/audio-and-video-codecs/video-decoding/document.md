# Video Decoding

You can call native APIs to perform video decoding, which decodes media data into a YUV file or renders it.

For details about the implementation, see [Samples](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec).

For details about the supported decoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#video-decoding).

To decode HDR Vivid video streams, set MimeType to H265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC). This feature is supported since API version 11.

Through the VideoDecoder module, your application can implement the following key capabilities.

| Capability | How to Configure |
| :-- | :-- |
| Variable resolution | The decoder supports the change of the input stream resolution. After the resolution is changed, the callback function **OnStreamChanged()** set by **OH\_VideoDecoder\_RegisterCallback** is triggered. For details, see step 3 in surface mode or step 3 in buffer mode. |
| Dynamic surface switching | Call **OH\_VideoDecoder\_SetSurface** to configure this capability. It is supported only in surface mode. For details, see step 6 in surface mode. |
| Low-latency decoding | Call **OH\_VideoDecoder\_Configure** to configure this capability. For details, see step 5 in surface mode or step 5 in buffer mode. |

#### Constraints

1.  After **flush()**, **reset()**, or **stop()** is called, the PPS/SPS must be transferred again in the **start()** call. For details about the example, see step 13 in [Surface Mode](#surface-mode).
2.  If **flush()**, **reset()**, **stop()**, or **destroy()** is executed in a non-callback thread, the execution result is returned after all callbacks are executed.
3.  Due to limited hardware decoder resources, you must call **OH\_VideoDecoder\_Destroy** to destroy every decoder instance when it is no longer needed.
4.  The input streams for video decoding support only the AnnexB format, and the supported AnnexB format supports multiple slices. However, the slices of the same frame must be sent to the decoder at a time.
5.  When **flush()**, **reset()**, or **stop()** is called, do not continue to operate the OH\_AVBuffer obtained through the previous callback function.
6.  The DRM decryption capability supports both non-secure and secure video channels in [surface mode](#surface-mode), but only non-secure video channels in buffer mode(#buffer-mode).
7.  The buffer mode and surface mode use the same APIs. Therefore, the surface mode is described as an example.
8.  In buffer mode, after obtaining the pointer to an OH\_AVBuffer instance through the callback function **OH\_AVCodecOnNewOutputBuffer**, call **OH\_VideoDecoder\_FreeOutputBuffer** to notify the system that the buffer has been fully utilized. In this way, the system can write the subsequently decoded data to the corresponding location. If the OH\_NativeBuffer instance is obtained through **OH\_AVBuffer\_GetNativeBuffer** and its lifecycle extends beyond that of the OH\_AVBuffer pointer instance, you mut perform data duplication. In this case, you should manage the lifecycle of the newly generated OH\_NativeBuffer object to ensure that the object can be correctly used and released.

-   To ensure the continuous availability of system services, the system will automatically intervene when it detects that any abnormal instances of an application occupying resources. You should be aware that improper instance management may result in the process being terminated.

#### Surface Output and Buffer Output

1.  Surface output and buffer output differ in data output modes.
    
2.  They are applicable to different scenarios.
    
    -   Surface output indicates that the OHNativeWindow is used to transfer output data. It supports connection with other modules, such as the **XComponent**.
    -   Buffer output indicates that decoded data is output in shared memory mode.
3.  The two also differ slightly in the API calling modes:
    
    -   In surface mode, you can choose to call **OH\_VideoDecoder\_FreeOutputBuffer** to free the output buffer (without rendering the data). In buffer mode, you must call **OH\_VideoDecoder\_FreeOutputBuffer** to free the output buffer.
    -   In surface mode, you must call [OH\_VideoDecoder\_SetSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_setsurface) to set an OHNativeWindow before the decoder is ready. After the decoder starts, you can call [OH\_VideoDecoder\_RenderOutputBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_renderoutputbuffer) to display and then release the decoded frame, or call [OH\_VideoDecoder\_RenderOutputBufferAtTime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_renderoutputbufferattime) to display the decoded frame at a specified time and then release it. To implement audio-video synchronization or control the display speed, you are advised to call **OH\_VideoDecoder\_RenderOutputBufferAtTime**.
    -   In buffer mode, an application can obtain the shared memory address and data from the output buffer. In surface mode, an application can obtain the data from the output buffer.

For details about the development procedure, see [Surface Mode](#surface-mode) and [Buffer Mode](#buffer-mode).

#### State Machine Interaction

The following figure shows the interaction between states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/_uziXrbQT7W3yLCW18rQLA/en-us_image_0000002537765162.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B059CEE866F62ABB6AC5C861E9B959F4416FA4C13676659F3E91E808281CAA4D)

1.  A decoder enters the Initialized state in either of the following ways:
    
    -   When a decoder instance is initially created, the decoder enters the Initialized state.
    -   When **OH\_VideoDecoder\_Reset** is called in any state, the decoder returns to the Initialized state.
2.  When the decoder is in the Initialized state, you can call **OH\_VideoDecoder\_Configure** to configure the decoder. After the configuration, the decoder enters the Configured state.
    
3.  When the decoder is in the Configured state, you can call **OH\_VideoDecoder\_Prepare** to switch it to the Prepared state.
    
4.  When the decoder is in the Prepared state, you can call **OH\_VideoDecoder\_Start** to switch it to the Executing state.
    
    -   When the decoder is in the Executing state, you can call **OH\_VideoDecoder\_Stop** to switch it back to the Prepared state.
5.  In rare cases, the decoder may encounter an error and enter the Error state. If this is the case, an invalid value can be returned or an exception can be thrown through a queue operation.
    
    -   When the decoder is in the Error state, you can either call **OH\_VideoDecoder\_Reset** to switch it to the Initialized state or call **OH\_VideoDecoder\_Destroy** to switch it to the Released state.
6.  The Executing state has three substates: Flushed, Running, and End-of-Stream.
    
    -   After **OH\_VideoDecoder\_Start** is called, the decoder enters the Running substate immediately.
    -   When the decoder is in the Executing state, you can call **OH\_VideoDecoder\_Flush** to switch it to the Flushed substate.
    -   After all data to be processed is transferred to the decoder, the [AVCODEC\_BUFFER\_FLAGS\_EOS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-info-h#oh_avcodecbufferflags) flag is added to the last input buffer in the input buffers queue. Once this flag is detected, the decoder transits to the End-of-Stream substate. In this state, the decoder does not accept new inputs, but continues to generate outputs until it reaches the tail frame.
7.  When the decoder is no longer needed, you must call **OH\_VideoDecoder\_Destroy** to destroy the decoder instance, which then transitions to the Released state.
    

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h).

The figure below shows the call relationship of video decoding.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/7LAxxdmfS76Ae5J3_qSnKg/en-us_image_0000002537925108.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DC10A8C1EFD59D23E6BDE6D598A8AA8061C606590A055FA60F290A53BC0B6C6)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_vdec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/F8gg6n3LTdGRy9oh-6mX7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D451CCB2867DAD682D4F505B3A6D19282332D7D9EFD721F5E1BD57BE45DE1132)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## Defining the Basic Structure

The sample code provided in this section adheres to the C++17 standard and is for reference only. You can define your own buffer objects by referring to it.

1.  Add the header files.
    
    #include <condition\_variable>
    #include <memory>
    #include <mutex>
    #include <queue>
    #include <shared\_mutex>
    
2.  Define the information about the decoder callback buffer.
    
    struct CodecBufferInfo {
        CodecBufferInfo(uint32\_t index, OH\_AVBuffer \*buffer): index(index), buffer(buffer), isValid(true) {}
        // Callback buffer.
        OH\_AVBuffer \*buffer = nullptr;
        // Index of the callback buffer.
        uint32\_t index = 0;
        // Check whether the current buffer information is valid.
        bool isValid = true;
    };
    
3.  Define the input and output queue for decoding.
    
    class CodecBufferQueue {
    public:
        // Pass the callback buffer information to the queue.
        void Enqueue(const std::shared\_ptr<CodecBufferInfo> bufferInfo)
        {
            std::unique\_lock<std::mutex> lock(mutex\_);
            bufferQueue\_.push(bufferInfo);
            cond\_.notify\_all();
        }
    
        // Obtain the information about the callback buffer.
        std::shared\_ptr<CodecBufferInfo> Dequeue(int32\_t timeoutMs = 1000)
        {
            std::unique\_lock<std::mutex> lock(mutex\_);
            (void)cond\_.wait\_for(lock, std::chrono::milliseconds(timeoutMs), \[this\]() { return !bufferQueue\_.empty(); });
            if (bufferQueue\_.empty()) {
                return nullptr;
            }
            std::shared\_ptr<CodecBufferInfo> bufferInfo = bufferQueue\_.front();
            bufferQueue\_.pop();
            return bufferInfo;
        }
    
        // Clear the queue. The previous callback buffer becomes unavailable.
        void Flush()
        {
            std::unique\_lock<std::mutex> lock(mutex\_);
            while (!bufferQueue\_.empty()) {
                std::shared\_ptr<CodecBufferInfo> bufferInfo = bufferQueue\_.front();
                // After the flush, stop, reset, and destroy operations are performed, the previous callback buffer information is invalid.
                bufferInfo->isValid = false;
                bufferQueue\_.pop();
            }
        }
    
    private:
        std::mutex mutex\_;
        std::condition\_variable cond\_;
        std::queue<std::shared\_ptr<CodecBufferInfo>> bufferQueue\_;
    };
    
4.  Configure global variables.
    
    These global variables are for reference only. They can be encapsulated into an object based on service requirements.
    
    // Video frame width.
    int32\_t width = 320;
    // Video frame height.
    int32\_t height = 240;
    // Video pixel format.
     OH\_AVPixelFormat pixelFormat = AV\_PIXEL\_FORMAT\_NV12;
    // Video width stride.
    int32\_t widthStride = 0;
    // Video height stride.
    int32\_t heightStride = 0;
    // Pointer to the decoder instance.
    OH\_AVCodec \*videoDec = nullptr;
    // Decoder synchronization lock.
    std::shared\_mutex codecMutex;
    // Decoder input queue.
    CodecBufferQueue inQueue;
    // Decoder output queue.
    CodecBufferQueue outQueue;
    

## Surface Mode

The following walks you through how to implement the entire video decoding process in surface mode and implement data rotation in asynchronous mode. In this example, an H.264 stream file is input, decoded, and rendered.

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fstream>
    
2.  Create a decoder instance.
    
    You can create a decoder by name or MIME type. In the code snippet below, the following variables are used:
    
    -   **videoDec**: pointer to the video decoder instance.
    -   **capability**: pointer to the decoder's capability.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC**: AVC video codec.
    
    // To create a decoder by name, call OH\_AVCapability\_GetName to obtain the codec names available and then call OH\_VideoDecoder\_CreateByName. If your application has special requirements, for example, expecting a decoder that supports a certain resolution, you can call OH\_AVCodec\_GetCapability to query the capability first.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false);
    // Create a hardware decoder instance.
    OH\_AVCapability \*capability= OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false, HARDWARE);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(name);
    
    // Create a decoder by MIME type. Only specific codecs recommended by the system can be created in this way.
    // If multiple codecs need to be created, create hardware decoder instances first. If the hardware resources are insufficient, create software decoder instances.
    // Create an H.264 decoder for software/hardware decoding.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
    // Create an H.265 decoder for software/hardware decoding.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    
3.  Call **OH\_VideoDecoder\_RegisterCallback()** to register the callback functions.
    
    Register the **OH\_AVCodecCallback** struct that defines the following callback function pointers:
    
    -   **OH\_AVCodecOnError**, a callback used to report a decoder operation error. For details about the error codes, see [OH\_AVCodecOnError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconerror).
    -   **OH\_AVCodecOnStreamChanged**, a callback used to report a codec stream change, for example, stream width or height change.
    -   **OH\_AVCodecOnNeedInputBuffer**, a callback used to report input data required, which means that the decoder is ready for receiving data.
    -   **OH\_AVCodecOnNewOutputBuffer**, a callback used to report output data generated, which means that decoding is complete.
    
    You need to process the callback functions to ensure that the decoder runs properly.
    
    For details about the implementation of the callback function, see [Sample Project](https://gitee.com/harmonyos_samples/AVCodecVideo).
    
    // Implement the OH\_AVCodecOnError callback function.
    static void OnError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)
    {
        // Process the error code in the callback.
        (void)codec;
        (void)errorCode;
        (void)userData;
    }
    
    // Implement the OH\_AVCodecOnStreamChanged callback function.
    static void OnStreamChanged(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)
    {
        // The changed video width and height can be obtained through format.
        (void)codec;
        (void)userData;
        bool ret = OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height);
        if (!ret) {
            // Handle exceptions.
        }
    }
    
    // Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The data buffer of the input frame and its index are sent to inQueue.
        (void)codec;
        (void)userData;
        inQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    // Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The data buffer of the finished frame and its index are sent to outQueue.
        (void)codec;
        (void)userData;
        outQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    // Call OH\_VideoDecoder\_RegisterCallback() to register the callback functions.
    OH\_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
    // Set the asynchronous callbacks.
    OH\_AVErrCode ret = OH\_VideoDecoder\_RegisterCallback(videoDec, cb, nullptr); // nullptr: userData on which the callback depends is empty.
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/FtzwsUHlRUmjGb27T8_h7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12F8D9735247EFDD4EF730AF46700CD461F5B99886CE19514A2318CD40AADB97)
    
    1.  In the callback functions, pay attention to multi-thread synchronization for operations on the data queue.
    2.  During video playback, if the SPS of the video stream contains color information, the decoder will return the information (RangeFlag, ColorPrimary, MatrixCoefficient, and TransferCharacteristic) through the **OH\_AVFormat** parameter in the **OH\_AVCodecOnStreamChanged** callback.
    3.  In surface mode of video decoding, the internal data is processed by using High Efficiency Bandwidth Compression (HEBC) by default, and the values of **widthStride** and **heightStride** cannot be obtained.
    
4.  (Optional) Call **OH\_VideoDecoder\_SetDecryptionConfig** to set the decryption configuration. Call this API after the media key system information is obtained and a media key is obtained but before **Prepare()** is called. For details about how to obtain such information, see step 4 in [Media Data Demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md). In surface mode, the DRM decryption capability supports both secure and non-secure video channels. For details about DRM APIs, see [DRM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm).
    
    Add the header files.
    
    #include <multimedia/drm\_framework/native\_mediakeysystem.h>
    #include <multimedia/drm\_framework/native\_mediakeysession.h>
    #include <multimedia/drm\_framework/native\_drm\_err.h>
    #include <multimedia/drm\_framework/native\_drm\_common.h>
    
    Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(sample PUBLIC libnative\_drm.so)
    
    Create a channel based on the content protection level required by the DRM stream and the content protection level supported by the hardware device.
    
    If the content protection level required by the DRM stream is hardware-level protection, a secure video channel is recommended. The following is an example:
    
    // Create a media key system based on the DRM information. The following uses com.wiseplay.drm as an example.
    MediaKeySystem \*system = nullptr;
    int32\_t ret = OH\_MediaKeySystem\_Create("com.wiseplay.drm", &system);
    if (system == nullptr) {
        printf("create media key system failed");
        return;
    }
    
    // Create a decryption session. If a secure video channel is used, create a MediaKeySession with the content protection level of CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO or higher.
    MediaKeySession \*session = nullptr;
    DRM\_ContentProtectionLevel contentProtectionLevel = CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO;
    ret = OH\_MediaKeySystem\_CreateMediaKeySession(system, &contentProtectionLevel, &session);
    if (ret != DRM\_OK) {
        // If the creation fails, refer to the DRM interface document and check logs.
        printf("create media key session failed.");
        return;
    }
    if (session == nullptr) {
        printf("media key session is nullptr.");
        return;
    }
    
    // Generate a media key request and set the response to the media key request.
    
    // Set the decryption configuration, that is, set the decryption session and secure video channel flag to the decoder.
    // If the DRM scheme supports a secure video channel, set secureVideoPath to true and create a secure decoder before using the channel.
    // That is, in step 3, call OH\_VideoDecoder\_CreateByName, with a decoder name followed by .secure (for example, \[CodecName\].secure) passed in, to create a secure decoder.
    bool secureVideoPath = true;
    ret = OH\_VideoDecoder\_SetDecryptionConfig(videoDec, session, secureVideoPath);
    
    If the content protection level required by the DRM stream is software-level protection, a non-secure video channel is recommended. The following is an example:
    
    // Create a media key system based on the media key system information. The following uses com.wiseplay.drm as an example.
    MediaKeySystem \*system = nullptr;
    int32\_t ret = OH\_MediaKeySystem\_Create("com.wiseplay.drm", &system);
    if (system == nullptr) {
        printf("create media key system failed");
        return;
    }
    
    // Create a decryption session. If a secure video channel is used, create a MediaKeySession with the content protection level of CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO or higher.
    // To use a non-secure video channel, create a MediaKeySession with the content protection level of CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO or higher.
    MediaKeySession \*session = nullptr;
    DRM\_ContentProtectionLevel contentProtectionLevel = CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO;
    ret = OH\_MediaKeySystem\_CreateMediaKeySession(system, &contentProtectionLevel, &session);
    if (ret != DRM\_OK) {
        // If the creation fails, refer to the DRM interface document and check logs.
        printf("create media key session failed.");
        return;
    }
    if (session == nullptr) {
        printf("media key session is nullptr.");
        return;
    }
    
    // Generate a media key request and set the response to the media key request.
    
    // Set the decryption configuration, that is, set the decryption session and secure video channel flag to the decoder.
    // If the DRM scheme supports a secure video channel, set secureVideoPath to true and create a secure decoder before using the channel.
    // That is, in step 2, call OH\_VideoDecoder\_CreateByName, with a decoder name followed by .secure (for example, \[CodecName\].secure) passed in, to create a secure decoder.
    bool secureVideoPath = false;
    ret = OH\_VideoDecoder\_SetDecryptionConfig(videoDec, session, secureVideoPath);
    
5.  Call **OH\_VideoDecoder\_Configure()** to configure the decoder.
    
    For details about the configurable options, see [Video Dedicated Key-Value Paris](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).
    
    For details about the parameter verification rules, see [OH\_VideoDecoder\_Configure()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_configure).
    
    The parameter value ranges can be obtained through the capability query interface. For details, see [Obtaining Supported Codecs](../obtaining-supported-codecs/document.md).
    
    Currently, the following options must be configured for all supported formats: video frame width and height.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat);
    // (Optional) Configure low-latency decoding.
    // If supported by the platform, the video decoder outputs frames in the decoding sequence when OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY is enabled.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY, 1);
    // Configure the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Configure(videoDec, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Set the surface.
    
    You can obtain NativeWindow in either of the following ways:
    
    6.1 If the image is directly displayed after being decoded, obtain NativeWindow from the **XComponent**.
    
    Add the header files.
    
    #include <native\_window/external\_window.h>
    
    Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(sample PUBLIC libnative\_window.so)
    
    6.1.1 On ArkTS, call **getXComponentSurfaceId** of the xComponentController to obtain the surface ID of the XComponent. For details about the operation, see [Custom Rendering (XComponent)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/adding-a-component/custom-rendering-xcomponent/document.md).
    
    6.1.2 On the native side, call **OH\_NativeWindow\_CreateNativeWindowFromSurfaceId** to create a NativeWindow instance.
    
    OHNativeWindow\* nativeWindow;
    // Create a NativeWindow instance based on the surface ID obtained in step 1.1.
    OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(surfaceId, &nativeWindow);
    
    6.2 If OpenGL post-processing is performed after decoding, obtain NativeWindow from NativeImage. For details about the operation, see [NativeImage](../../../../graphics/arkgraphics-2d/native-image-development-c-c/document.md).
    
    You perform this step during decoding, that is, dynamically switch the surface.
    
    // Set the surface.
    // Set the window parameters.
    OH\_AVErrCode ret = OH\_VideoDecoder\_SetSurface(videoDec, nativeWindow);  // Obtain a NativeWindow instance using either of the preceding methods.
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Configure the matching mode between the video and screen. (Scale the buffer at the original aspect ratio to enable the smaller side of the buffer to match the window, while making the excess part transparent.)
    OH\_NativeWindow\_NativeWindowSetScalingModeV2(nativeWindow, OH\_SCALING\_MODE\_SCALE\_CROP\_V2);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kVAoREsnT7CLrQBI1jdppw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD377400E92240E40801FAFAB5F33BB27448D250FBA1272F419F2AC4E23600C5)
    
    If both decoder 1 and decoder 2 are bound to the same NativeWindow using the **OH\_VideoDecoder\_SetSurface** function, and decoder 2 is running, destroying decoder 1 with **OH\_VideoDecoder\_Destroy** will cause decoder 2's video playback to freeze.
    
    Consider the following approaches:
    
    1.  Wait for decoder 1 to be fully released before starting decoder 2 with **OH\_VideoDecoder\_Start**.
    2.  Use surface 1 for decoder 1, and create a temporary surface for decoder 2 using **OH\_ConsumerSurface\_Create**. Once decoder 1 is released, bind decoder 2 to surface 1 using **OH\_VideoDecoder\_SetSurface**. For details, see [Concurrently Creating a Video Decoder and Initializing NativeWindow](../concurrently-creating-a-video-decoder-and-initializing-nativewindow/document.md).
    
7.  Call **OH\_VideoDecoder\_Prepare()** to prepare internal resources for the decoder.
    
    OH\_AVErrCode ret = OH\_VideoDecoder\_Prepare(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
8.  Call **OH\_VideoDecoder\_Start()** to start the decoder.
    
    // Start the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Start(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
9.  (Optional) Call **OH\_VideoDecoder\_SetParameter()** to set the surface parameters of the decoder.
    
    For details about the configurable options, see [Video Dedicated Key-Value Paris](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Configure the display rotation angle.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_ROTATION, 90);
    OH\_AVErrCode ret = OH\_VideoDecoder\_SetParameter(videoDec, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  (Optional) Call **OH\_AVCencInfo\_SetAVBuffer()** to set the Common Encryption Scheme (CENC) information.
     
     If the program to play is DRM encrypted and the application implements media demultiplexing instead of using the system's [demuxer](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md), you must call **OH\_AVCencInfo\_SetAVBuffer()** to set the CENC information to the AVBuffer. In this way, the AVBuffer carries the data to be decrypted and CENC information, so that the media data in the AVBuffer can be decrypted. You do not need to call this API when the application uses the system's [demuxer](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md).
     
     Add the header files.
     
     #include <multimedia/player\_framework/native\_cencinfo.h>
     
     Link the dynamic libraries in the CMake script.
     
     target\_link\_libraries(sample PUBLIC libnative\_media\_avcencinfo.so)
     
     In the code snippet below, the following variable is used:
     
     -   **buffer**: parameter passed by the callback function **OnNeedInputBuffer**.
     
     uint32\_t keyIdLen = DRM\_KEY\_ID\_SIZE;
     uint8\_t keyId\[\] = {
         0xd4, 0xb2, 0x01, 0xe4, 0x61, 0xc8, 0x98, 0x96,
         0xcf, 0x05, 0x22, 0x39, 0x8d, 0x09, 0xe6, 0x28};
     uint32\_t ivLen = DRM\_KEY\_IV\_SIZE;
     uint8\_t iv\[\] = {
         0xbf, 0x77, 0xed, 0x51, 0x81, 0xde, 0x36, 0x3e,
         0x52, 0xf7, 0x20, 0x4f, 0x72, 0x14, 0xa3, 0x95};
     uint32\_t encryptedBlockCount = 0;
     uint32\_t skippedBlockCount = 0;
     uint32\_t firstEncryptedOffset = 0;
     uint32\_t subsampleCount = 1;
     DrmSubsample subsamples\[1\] = { {0x10, 0x16} };
     // Create a CencInfo instance.
     OH\_AVCencInfo \*cencInfo = OH\_AVCencInfo\_Create();
     if (cencInfo == nullptr) {
         // Handle exceptions.
     }
     // Set the decryption algorithm.
     OH\_AVErrCode errNo = OH\_AVCencInfo\_SetAlgorithm(cencInfo, DRM\_ALG\_CENC\_AES\_CTR);
     if (errNo != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Set KeyId and Iv.
     errNo = OH\_AVCencInfo\_SetKeyIdAndIv(cencInfo, keyId, keyIdLen, iv, ivLen);
     if (errNo != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Set the sample information.
     errNo = OH\_AVCencInfo\_SetSubsampleInfo(cencInfo, encryptedBlockCount, skippedBlockCount, firstEncryptedOffset,
         subsampleCount, subsamples);
     if (errNo != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Set the mode. KeyId, Iv, and SubSamples have been set.
     errNo = OH\_AVCencInfo\_SetMode(cencInfo, DRM\_CENC\_INFO\_KEY\_IV\_SUBSAMPLES\_SET);
     if (errNo != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Set CencInfo to the AVBuffer.
     errNo = OH\_AVCencInfo\_SetAVBuffer(cencInfo, buffer);
     if (errNo != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Destroy the CencInfo instance.
     errNo = OH\_AVCencInfo\_Destroy(cencInfo);
     if (errNo != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
11.  Call **OH\_VideoDecoder\_PushInputBuffer()** to push the stream to the input buffer for decoding.
     
     In the code snippet below, the following variables are used:
     
     -   **size**, **offset**, **pts**, and **frameData**: size, offset, timestamp, and frame data. For details about how to obtain such information, see step 9 in [Media Data Demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md).
     -   **flags**: type of the buffer flag. For details, see [OH\_AVCodecBufferFlags](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-info-h#oh_avcodecbufferflags).
     
     The member variables of **bufferInfo** are as follows:
     
     -   **buffer**: parameter passed by the callback function **OnNeedInputBuffer**. You can obtain the virtual address of the input stream by calling [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr).
     -   **index**: parameter passed by the callback function **OnNeedInputBuffer**, which uniquely corresponds to the buffer.
     -   **isValid**: whether the buffer instance stored in **bufferInfo** is valid.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // Write stream data.
     uint8\_t \*addr = OH\_AVBuffer\_GetAddr(bufferInfo->buffer);
     if (addr == nullptr) {
        // Handle exceptions.
     }
     int32\_t capacity = OH\_AVBuffer\_GetCapacity(bufferInfo->buffer);
     if (size > capacity) {
         // Handle exceptions.
     }
     memcpy(addr, frameData, size);
     // Configure the size, offset, and timestamp of the frame data.
     OH\_AVCodecBufferAttr info;
     info.size = size;
     info.offset = offset;
     info.pts = pts;
     info.flags = flags;
     // Write the information to the buffer.
     OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(bufferInfo->buffer, &info);
     if (setBufferRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Send the data to the input buffer for decoding.
     OH\_AVErrCode pushInputRet = OH\_VideoDecoder\_PushInputBuffer(videoDec, bufferInfo->index);
     if (pushInputRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
12.  Call **OH\_VideoDecoder\_RenderOutputBuffer()** or **OH\_VideoDecoder\_RenderOutputBufferAtTime()** to render the data and free the output buffer, or call **OH\_VideoDecoder\_FreeOutputBuffer()** to directly free the output buffer.
     
     In the following example, the member variables of **bufferInfo** are as follows:
     
     -   **index**: parameter passed by the callback function **OnNewOutputBuffer**, which uniquely corresponds to the buffer.
     -   **buffer**: parameter passed by the callback function **OnNewOutputBuffer**. In surface mode, you cannot obtain the virtual address of the image by calling [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr).
     -   **isValid**: whether the buffer instance stored in **bufferInfo** is valid.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // Obtain the decoded information.
     OH\_AVCodecBufferAttr info;
     OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(bufferInfo->buffer, &info);
     if (getBufferRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // You can determine the value.
     bool isRender;
     bool isNeedRenderAtTime;
     OH\_AVErrCode ret = AV\_ERR\_OK;
     if (isRender) {
         // Render the data and free the output buffer. index is the index of the buffer.
         if (isNeedRenderAtTime){
             // Obtain the system absolute time, and call renderTimestamp to display the time based on service requirements.
             int64\_t renderTimestamp =
                 std::chrono::duration\_cast<std::chrono::nanoseconds>(std::chrono::high\_resolution\_clock::now().time\_since\_epoch()).count();
             ret = OH\_VideoDecoder\_RenderOutputBufferAtTime(videoDec, bufferInfo->index, renderTimestamp);
         } else {
             ret = OH\_VideoDecoder\_RenderOutputBuffer(videoDec, bufferInfo->index);
         }
     
     } else {
         // Free the output buffer.
         ret = OH\_VideoDecoder\_FreeOutputBuffer(videoDec, bufferInfo->index);
     }
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/dyhJcuN2RtOzzX7Y19sr2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9DE53F09763E977C5A6C51F67A153EFD920D7C51EF5C389BEC5D2A1343C1BF4)
     
     1.  To obtain the buffer attributes, such as **pixel\_format** and **stride**, call [OH\_NativeWindow\_NativeWindowHandleOpt](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-external-window-h#oh_nativewindow_nativewindowhandleopt).
     2.  To render the data and free the output buffer, you are advised to call [OH\_VideoDecoder\_RenderOutputBufferAtTime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videodecoder-h#oh_videodecoder_renderoutputbufferattime) first.
     
13.  (Optional) Call **OH\_VideoDecoder\_Flush()** to refresh the decoder.
     
     After **OH\_VideoDecoder\_Flush** is called, the decoder remains in the Running state, but the input and output data and parameter set (such as the H.264 PPS/SPS) buffered in the decoder are cleared. To continue decoding, you must call **OH\_VideoDecoder\_Start** again.
     
     In the code snippet below, the following variables are used:
     
     -   **xpsData** and **xpsSize**: PPS/SPS information. For details about how to obtain such information, see [Media Data Demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md).
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Refresh the decoder.
     OH\_AVErrCode flushRet = OH\_VideoDecoder\_Flush(videoDec);
     if (flushRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     inQueue.Flush();
     outQueue.Flush();
     // Start decoding again.
     OH\_AVErrCode startRet = OH\_VideoDecoder\_Start(videoDec);
     if (startRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // Retransfer PPS/SPS.
     // Configure the frame PPS/SPS information.
     uint8\_t \*addr = OH\_AVBuffer\_GetAddr(bufferInfo->buffer);
     if (addr == nullptr) {
        // Handle exceptions.
     }
     int32\_t capacity = OH\_AVBuffer\_GetCapacity(bufferInfo->buffer);
     if (xpsSize > capacity) {
         // Handle exceptions.
     }
     memcpy(addr, xpsData, xpsSize);
     OH\_AVCodecBufferAttr info;
     info.flags = AVCODEC\_BUFFER\_FLAG\_CODEC\_DATA;
     // Write the information to the buffer.
     OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(bufferInfo->buffer, &info);
     if (setBufferRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Push the frame data to the decoder. index is the index of the corresponding queue.
     OH\_AVErrCode pushInputRet = OH\_VideoDecoder\_PushInputBuffer(videoDec, bufferInfo->index);
     if (pushInputRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/-HFkVw-9S6qfCxT9myqHJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FA054109133DF06EEC3BF7E45961B4128411DE48970E58E12D2510734206AFF)
     
     When **OH\_VideoDecoder\_Start** is called again after the flush operation, the PPS/SPS must be retransferred.
     
14.  (Optional) Call **OH\_VideoDecoder\_Reset()** to reset the decoder.
     
     After **OH\_VideoDecoder\_Reset** is called, the decoder returns to the Initialized state. To continue decoding, you must call **OH\_VideoDecoder\_Configure**, **OH\_VideoDecoder\_SetSurface**, and **OH\_VideoDecoder\_Prepare** in sequence.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Reset the decoder.
     OH\_AVErrCode resetRet = OH\_VideoDecoder\_Reset(videoDec);
     if (resetRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     inQueue.Flush();
     outQueue.Flush();
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
     
15.  (Optional) Call **OH\_VideoDecoder\_Stop()** to stop the decoder.
     
     After **OH\_VideoDecoder\_Stop()** is called, the decoder retains the decoding instance and releases the input and output buffers. You can directly call **OH\_VideoDecoder\_Start** to continue decoding. The first input buffer must carry the parameter set, starting from the IDR frame.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Stop the decoder.
     OH\_AVErrCode ret = OH\_VideoDecoder\_Stop(videoDec);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     inQueue.Flush();
     outQueue.Flush();
     
16.  Call **OH\_VideoDecoder\_Destroy()** to destroy the decoder instance and release resources.
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/d7yGdeMRQWGnrZLcF40eVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D33A1DE2966360130FCF7E7F1BC0FB6AEBD5C3828C4F94B009E0ACB5A9324EE)
     
     1.  This API cannot be called in the callback function.
     2.  After the call, you must set a null pointer to the decoder to prevent program errors caused by wild pointers.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Release the nativeWindow instance.
     if(nativeWindow != nullptr){
         OH\_NativeWindow\_DestroyNativeWindow(nativeWindow);
         nativeWindow = nullptr;
     }
     // Call OH\_VideoDecoder\_Destroy to destroy the decoder.
     OH\_AVErrCode ret = AV\_ERR\_OK;
     if (videoDec != nullptr) {
         OH\_VideoDecoder\_Destroy(videoDec);
         videoDec = nullptr;
     }
     inQueue.Flush();
     outQueue.Flush();
     

## Buffer Mode

The following walks you through how to implement the entire video decoding process in buffer mode and implement data rotation in asynchronous mode. In this example, an H.264 stream file is input and decoded into a YUV file.

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <native\_buffer/native\_buffer.h>
    #include <fstream>
    
2.  Create a decoder instance.
    
    The procedure is the same as that in surface mode and is not described here.
    
    // To create a decoder by name, call OH\_AVCapability\_GetName to obtain the codec names available and then call OH\_VideoDecoder\_CreateByName. If your application has special requirements, for example, expecting a decoder that supports a certain resolution, you can call OH\_AVCodec\_GetCapability to query the capability first.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(name);
    
    // Create a decoder by MIME type. Only specific codecs recommended by the system can be created in this way.
    // If multiple codecs need to be created, create hardware decoder instances first. If the hardware resources are insufficient, create software decoder instances.
    // Create an H.264 decoder for software/hardware decoding.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
    // Create an H.265 decoder for hardware decoding.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    
3.  Call **OH\_VideoDecoder\_RegisterCallback()** to register the callback functions.
    
    Register the **OH\_AVCodecCallback** struct that defines the following callback function pointers:
    
    -   **OH\_AVCodecOnError**, a callback used to report a decoder operation error. For details about the error codes, see [OH\_AVCodecOnError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconerror).
    -   **OH\_AVCodecOnStreamChanged**, a callback used to report a codec stream change, for example, stream width or height change.
    -   **OH\_AVCodecOnNeedInputBuffer**, a callback used to report input data required, which means that the decoder is ready for receiving data.
    -   **OH\_AVCodecOnNewOutputBuffer**, a callback used to report output data generated, which means that decoding is complete.
    
    You need to process the callback functions to ensure that the decoder runs properly.
    
    For details about the implementation of the callback function, see [Sample Project](https://gitee.com/harmonyos_samples/AVCodecVideo).
    
    int32\_t cropTop = 0;
    int32\_t cropBottom = 0;
    int32\_t cropLeft = 0;
    int32\_t cropRight = 0;
    bool isFirstFrame = true;
    // Implement the OH\_AVCodecOnError callback function.
    static void OnError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)
    {
        // Process the error code in the callback.
        (void)codec;
        (void)errorCode;
        (void)userData;
    }
    
    // Implement the OH\_AVCodecOnStreamChanged callback function.
    static void OnStreamChanged(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)
    {
        // Optional. Configure the data when you want to obtain the video width, height, and stride.
        // The changed video width, height, and stride can be obtained through format.
        (void)codec;
        (void)userData;
        bool ret = OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_STRIDE, &widthStride) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &heightStride) &&
                   // (Optional) Obtain the cropped rectangle information.
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_CROP\_TOP, &cropTop) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM, &cropBottom) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_CROP\_LEFT, &cropLeft) &&
                   OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT, &cropRight);
        if (!ret) {
            // Handle exceptions.
        }
    }
    
    // Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The data buffer of the input frame and its index are sent to inQueue.
        (void)codec;
        (void)userData;
        inQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    // Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // Optional. Configure the data when you want to obtain the video width, height, and stride.
        // Obtain the video width, height, and stride.
        if (isFirstFrame) {
            auto format = std::shared\_ptr<OH\_AVFormat>(OH\_VideoDecoder\_GetOutputDescription(codec), OH\_AVFormat\_Destroy);
            if (format == nullptr) {
                // Handle exceptions.
            }
            bool ret = OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_STRIDE, &widthStride) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &heightStride) &&
                       // (Optional) Obtain the cropped rectangle information.
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_TOP, &cropTop) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM, &cropBottom) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_LEFT, &cropLeft) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT, &cropRight);
            if (!ret) {
                // Handle exceptions.
            }
            isFirstFrame = false;
        }
        // The data buffer of the finished frame and its index are sent to outQueue.
        (void)userData;
        outQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    // Call OH\_VideoDecoder\_RegisterCallback() to register the callback functions.
    OH\_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
    // Set the asynchronous callbacks.
    OH\_AVErrCode ret = OH\_VideoDecoder\_RegisterCallback(videoDec, cb, nullptr); // nullptr: userData on which the callback depends is empty.
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/pA7FdhsWR02G4tBLnCGexA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=367433259110938BBDCC6A6AF8EBA7D9FF5763976C7ECFD2D146255213E58088)
    
    In the callback functions, pay attention to multi-thread synchronization for operations on the data queue.
    
4.  (Optional) Call **OH\_VideoDecoder\_SetDecryptionConfig** to set the decryption configuration. Call this API after the media key system information is obtained and a media key is obtained but before **Prepare()** is called. For details about how to obtain such information, see step 4 in [Media Data Demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md). In buffer mode, the DRM decryption capability supports only non-secure video channels. For details about DRM APIs, see [DRM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm).
    
    Add the header files.
    
    #include <multimedia/drm\_framework/native\_mediakeysystem.h>
    #include <multimedia/drm\_framework/native\_mediakeysession.h>
    #include <multimedia/drm\_framework/native\_drm\_err.h>
    #include <multimedia/drm\_framework/native\_drm\_common.h>
    
    Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(sample PUBLIC libnative\_drm.so)
    
    The sample code is as follows.
    
    // Create a media key system based on the media key system information. The following uses com.wiseplay.drm as an example.
    MediaKeySystem \*system = nullptr;
    int32\_t ret = OH\_MediaKeySystem\_Create("com.wiseplay.drm", &system);
    if (system == nullptr) {
        printf("create media key system failed");
        return;
    }
    
    // Create a media key session.
    // To use a non-secure video channel, create a MediaKeySession with the content protection level of CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO or higher.
    MediaKeySession \*session = nullptr;
    DRM\_ContentProtectionLevel contentProtectionLevel = CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO;
    ret = OH\_MediaKeySystem\_CreateMediaKeySession(system, &contentProtectionLevel, &session);
    if (ret != DRM\_OK) {
        // If the creation fails, refer to the DRM interface document and check logs.
        printf("create media key session failed.");
        return;
    }
    if (session == nullptr) {
        printf("media key session is nullptr.");
        return;
    }
    // Generate a media key request and set the response to the media key request.
    // Set the decryption configuration, that is, set the decryption session and secure video channel flag to the decoder.
    bool secureVideoPath = false;
    ret = OH\_VideoDecoder\_SetDecryptionConfig(videoDec, session, secureVideoPath);
    
5.  Call **OH\_VideoDecoder\_Configure()** to configure the decoder.
    
    The procedure is the same as that in surface mode and is not described here.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat);
    // Configure the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Configure(videoDec, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Call **OH\_VideoDecoder\_Prepare()** to prepare internal resources for the decoder.
    
    OH\_AVErrCode ret = OH\_VideoDecoder\_Prepare(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
7.  Call **OH\_VideoDecoder\_Start()** to start the decoder.
    
    std::unique\_ptr<std::ofstream> outputFile = std::make\_unique<std::ofstream>();
    if (outputFile != nullptr) {
        outputFile->open("/\*yourpath\*.yuv", std::ios::out | std::ios::binary | std::ios::ate);
    }
    // Start the decoder.
    OH\_AVErrCode ret = OH\_VideoDecoder\_Start(videoDec);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
8.  (Optional) Call **OH\_VideoDecoder\_SetParameter()** to set the decoder parameters.
    
    For details about the configurable options, see [Video Dedicated Key-Value Paris](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the frame rate.
    OH\_AVFormat\_SetDoubleValue(format.get(), OH\_MD\_KEY\_FRAME\_RATE, 30.0);
    OH\_AVErrCode ret = OH\_VideoDecoder\_SetParameter(videoDec, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
9.  (Optional) Call **OH\_AVCencInfo\_SetAVBuffer()** to set the CENC information.
    
    The procedure is the same as that in surface mode and is not described here.
    
    The sample code is as follows.
    
    uint32\_t keyIdLen = DRM\_KEY\_ID\_SIZE;
    uint8\_t keyId\[\] = {
        0xd4, 0xb2, 0x01, 0xe4, 0x61, 0xc8, 0x98, 0x96,
        0xcf, 0x05, 0x22, 0x39, 0x8d, 0x09, 0xe6, 0x28};
    uint32\_t ivLen = DRM\_KEY\_IV\_SIZE;
    uint8\_t iv\[\] = {
        0xbf, 0x77, 0xed, 0x51, 0x81, 0xde, 0x36, 0x3e,
        0x52, 0xf7, 0x20, 0x4f, 0x72, 0x14, 0xa3, 0x95};
    uint32\_t encryptedBlockCount = 0;
    uint32\_t skippedBlockCount = 0;
    uint32\_t firstEncryptedOffset = 0;
    uint32\_t subsampleCount = 1;
    DrmSubsample subsamples\[1\] = { {0x10, 0x16} };
    // Create a CencInfo instance.
    OH\_AVCencInfo \*cencInfo = OH\_AVCencInfo\_Create();
    if (cencInfo == nullptr) {
        // Handle exceptions.
    }
    // Set the decryption algorithm.
    OH\_AVErrCode errNo = OH\_AVCencInfo\_SetAlgorithm(cencInfo, DRM\_ALG\_CENC\_AES\_CTR);
    if (errNo != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Set KeyId and Iv.
    errNo = OH\_AVCencInfo\_SetKeyIdAndIv(cencInfo, keyId, keyIdLen, iv, ivLen);
    if (errNo != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Set the sample information.
    errNo = OH\_AVCencInfo\_SetSubsampleInfo(cencInfo, encryptedBlockCount, skippedBlockCount, firstEncryptedOffset,
        subsampleCount, subsamples);
    if (errNo != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Set the mode. KeyId, Iv, and SubSamples have been set.
    errNo = OH\_AVCencInfo\_SetMode(cencInfo, DRM\_CENC\_INFO\_KEY\_IV\_SUBSAMPLES\_SET);
    if (errNo != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Set CencInfo to the AVBuffer.
    errNo = OH\_AVCencInfo\_SetAVBuffer(cencInfo, buffer);
    if (errNo != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Destroy the CencInfo instance.
    errNo = OH\_AVCencInfo\_Destroy(cencInfo);
    if (errNo != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  Call **OH\_VideoDecoder\_PushInputBuffer()** to push the stream to the input buffer for decoding.
     
     The procedure is the same as that in surface mode and is not described here.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // Write stream data.
     uint8\_t \*addr = OH\_AVBuffer\_GetAddr(bufferInfo->buffer);
     if (addr == nullptr) {
        // Handle exceptions.
     }
     int32\_t capacity = OH\_AVBuffer\_GetCapacity(bufferInfo->buffer);
     if (size > capacity) {
         // Handle exceptions.
     }
     memcpy(addr, frameData, size);
     // Configure the size, offset, and timestamp of the frame data.
     OH\_AVCodecBufferAttr info;
     info.size = size;
     info.offset = offset;
     info.pts = pts;
     info.flags = flags;
     // Write the information to the buffer.
     OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(bufferInfo->buffer, &info);
     if (setBufferRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Send the data to the input buffer for decoding. index is the index of the buffer.
     OH\_AVErrCode pushInputRet = OH\_VideoDecoder\_PushInputBuffer(videoDec, bufferInfo->index);
     if (pushInputRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
11.  Call **OH\_VideoDecoder\_FreeOutputBuffer()** to free the output buffer.
     
     In the following example, the member variables of **bufferInfo** are as follows:
     
     -   **index**: parameter passed by the callback function **OnNewOutputBuffer**, which uniquely corresponds to the buffer.
     -   **buffer**: parameter passed by the callback function **OnNewOutputBuffer**. You can obtain the virtual address of an image by calling [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr).
     -   **isValid**: whether the buffer instance stored in **bufferInfo** is valid.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // Obtain the decoded information.
     OH\_AVCodecBufferAttr info;
     OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(bufferInfo->buffer, &info);
     if (getBufferRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Write the decoded data (specified by data) to the output file.
     uint8\_t \*addr = OH\_AVBuffer\_GetAddr(bufferInfo->buffer);
     if (addr == nullptr) {
        // Handle exceptions.
     }
     if (outputFile != nullptr && outputFile->is\_open()) {
         outputFile->write(reinterpret\_cast<char \*>(addr), info.size);
     }
     // Free the buffer that stores the output data. index is the index of the buffer.
     OH\_AVErrCode freeOutputRet = OH\_VideoDecoder\_FreeOutputBuffer(videoDec, bufferInfo->index);
     if (freeOutputRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
     To copy the Y, U, and V components of an NV12 or NV21 image to another buffer in sequence, perform the following steps (taking an NV12 image as an example),
     
     presenting the image layout of **width**, **height**, **wStride**, and **hStride**.
     
     -   **OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH** corresponds to **width**.
     -   **OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT** corresponds to **height**.
     -   **OH\_MD\_KEY\_VIDEO\_STRIDE** corresponds to **wStride**.
     -   **OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT** corresponds to **hStride**.
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5TfSkJJPRLe0nSBEQhxbEQ/en-us_image_0000002568684885.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B63421A4B018F0685D131CE4BE759CB7159AEB8ADBCE85E4B1CE590EDA219755)
     
     Add the header files.
     
     #include <string.h>
     
     The sample code is as follows.
     
     // Obtain the width and height of the source buffer by using the callback function OnStreamChanged or OH\_VideoDecoder\_GetOutputDescription.
     struct Rect
     {
         int32\_t width;
         int32\_t height;
     };
     
     struct DstRect // Width stride and height stride of the destination buffer. They are set by the caller.
     {
         int32\_t wStride;
         int32\_t hStride;
     };
     // Obtain the width stride and height stride of the source buffer by using the callback function OnStreamChanged or OH\_VideoDecoder\_GetOutputDescription.
     struct SrcRect
     {
         int32\_t wStride;
         int32\_t hStride;
     };
     
     Rect rect = {320, 240};
     DstRect dstRect = {320, 240};
     SrcRect srcRect = {320, 256};
     uint8\_t\* dst = new uint8\_t\[dstRect.hStride \* dstRect.wStride \* 3 / 2\]; // Pointer to the target memory area.
     uint8\_t\* src = new uint8\_t\[srcRect.hStride \* srcRect.wStride \* 3 / 2\]; // Pointer to the source memory area.
     uint8\_t\* dstTemp = dst;
     uint8\_t\* srcTemp = src;
     rect.height = ((rect.height + 1) / 2)  \* 2 // This ensures the height is always even.
     rect.width = ((rect.width + 1) / 2)  \* 2 // This ensures the width is always even.
     
     // Y: Copy the source data in the Y region to the target data in another region.
     for (int32\_t i = 0; i < rect.height; ++i) {
         // Copy a row of data from the source to a row of the target.
         memcpy(dstTemp, srcTemp, rect.width);
         // Update the pointers to the source data and target data to copy the next row. The pointers to the source data and target data are moved downwards by one wStride each time the source data and target data are updated.
         dstTemp += dstRect.wStride;
         srcTemp += srcRect.wStride;
     }
     // Padding.
     // Update the pointers to the source data and target data. The pointers move downwards by one padding.
     dstTemp += (dstRect.hStride - rect.height) \* dstRect.wStride;
     srcTemp += (srcRect.hStride - rect.height) \* srcRect.wStride;
     rect.height >>= 1;
     // UV: Copy the source data in the UV region to the target data in another region.
     for (int32\_t i = 0; i < rect.height; ++i) {
         memcpy(dstTemp, srcTemp, rect.width);
         dstTemp += dstRect.wStride;
         srcTemp += srcRect.wStride;
     }
     
     delete\[\] dst;
     dst = nullptr;
     delete\[\] src;
     src = nullptr;
     
     When processing buffer data (before releasing data) during hardware decoding, the output callback AVBuffer receives the image data after width and height alignment.
     
     Generally, copy the image width, height, stride, and pixel format to ensure correct processing of the decoded data.
     
     For details, see step 3 in [Buffer Mode](#buffer-mode).
     

The subsequent processes (including refreshing, resetting, stopping, and destroying the decoder) are the same as those in surface mode. For details, see steps 13–16 in [Surface Mode](#surface-mode).

#### Sample Code

-   [AVCodec Based Video Codec](https://gitee.com/harmonyos_samples/AVCodecVideo)
