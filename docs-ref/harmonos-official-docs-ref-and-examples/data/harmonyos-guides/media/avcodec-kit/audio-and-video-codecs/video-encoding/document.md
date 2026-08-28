# Video Encoding

You can call native APIs to perform video encoding, which compresses video data into a video stream.

For details about the implementation, see [Samples](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec).

For details about the supported encoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#video-encoding).

To encode HDR Vivid video streams, set MimeType to H265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC). This feature is supported since API version 11.

The following table lists the video encoding capabilities supported:

| Capability | How to Use |
| :-- | :-- |
| Configuring the encoder parameters, including the frame rate, bit rate, and QPMin/QPMax | Call OH\_VideoEncoder\_SetParameter(). For details, see step 9 in Surface Input below. |
| Setting the encoding QPMin/QPMax on a per-frame basis | Call OH\_VideoEncoder\_RegisterParameterCallback(). For details, see step 4 in Surface Input below. |
| Layered encoding and LTR setting | For details, see [Temporally Scalable Video Coding](../temporally-scalable-video-coding/document.md) |
| Obtaining the average QP and MSE of each frame | Call OnNewOutputBuffer(). For details, see step 3 in Surface Input below. |
| Variable resolution | The encoder supports the change of the input image resolution. Currently, this is supported only in surface mode, and the image width and height cannot exceed those configured by calling OH\_VideoEncoder\_Configure. For details, see step 5 in Surface Input below. |

#### Constraints

1.  The buffer mode does not support 10-bit image data.
2.  Due to limited hardware encoder resources, you must call **OH\_VideoEncoder\_Destroy** to destroy every encoder instance when it is no longer needed.
3.  If **flush()**, **reset()**, **stop()**, or **destroy()** is executed in a non-callback thread, the execution result is returned after all callbacks are executed.
4.  Once **Flush**, **Reset**, or **Stop** is called, the system reclaims the OH\_AVBuffer. Therefore, do not continue to operate the OH\_AVBuffer obtained through the previous callback function.
5.  The buffer mode and surface mode use the same APIs. Therefore, the surface mode is described as an example.
6.  In buffer mode, after obtaining the pointer to an OH\_AVBuffer instance through the callback function **OH\_AVCodecOnNeedInputBuffer**, call **OH\_VideoEncoder\_PushInputBuffer** to notify the system that the buffer has been fully utilized. In this way, the system will proceed with encoding the data contained in the buffer. If the OH\_NativeBuffer instance is obtained through **OH\_AVBuffer\_GetNativeBuffer** and its lifecycle extends beyond that of the OH\_AVBuffer pointer instance, you mut perform data duplication. In this case, you should manage the lifecycle of the newly generated OH\_NativeBuffer object to ensure that the object can be correctly used and released.

-   To ensure the continuous availability of system services, the system will automatically intervene when it detects that any abnormal instances of an application occupying resources. You should be aware that improper instance management may result in the process being terminated.

#### Surface Input and Buffer Input

1.  Surface input and buffer input differ in data sources.
    
2.  They are applicable to different scenarios.
    
    -   Surface input indicates that the OHNativeWindow is used to transfer passed-in data. It supports connection with other modules, such as the camera module.
    -   Buffer input refers to a pre-allocated memory area. You need to copy original data to this memory area. It is more applicable to scenarios such as reading video data from files.
3.  The two also differ slightly in the API calling modes:
    
    -   In buffer mode, call **OH\_VideoEncoder\_PushInputBuffer** to input data. In surface mode, before the encoder is ready, call **OH\_VideoEncoder\_GetSurface** to obtain the OHNativeWindow for video data transmission.
    -   In buffer mode, you can use **attr** in **OH\_AVBuffer** to pass in the End of Stream (EOS) flag, and the encoder stops when it reads the last frame. In surface mode, call **OH\_VideoEncoder\_NotifyEndOfStream** to notify the encoder of EOS.

For details about the development procedure, see [Surface Mode](#surface-mode) and [Buffer Mode](#buffer-mode).

#### State Machine Interaction

The following figure shows the interaction between states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/gQR1gZ-MQ3CjQbh9Ce_YIg/en-us_image_0000002537765162.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E59CF34EC7B2C8461D0A137EC829CFD8D2E6040CC30803114879FB79435FCA65)

1.  An encoder enters the Initialized state in either of the following ways:
    
    -   When an encoder instance is initially created, the encoder enters the Initialized state.
    -   When **OH\_VideoEncoder\_Reset** is called in any state, the encoder returns to the Initialized state.
2.  When the encoder is in the Initialized state, you can call **OH\_VideoEncoder\_Configure** to configure the encoder. After the configuration, the encoder enters the Configured state.
    
3.  When the encoder is in the Configured state, you can call **OH\_VideoEncoder\_Prepare()** to switch it to the Prepared state.
    
4.  When the encoder is in the Prepared state, you can call **OH\_VideoEncoder\_Start** to switch it to the Executing state.
    
    -   When the encoder is in the Executing state, you can call **OH\_VideoEncoder\_Stop** to switch it back to the Prepared state.
5.  In rare cases, the encoder may encounter an error and enter the Error state. If this is the case, an invalid value can be returned or an exception can be thrown through a queue operation.
    
    -   When the encoder is in the Error state, you can either call **OH\_VideoEncoder\_Reset** to switch it to the Initialized state or call **OH\_VideoEncoder\_Destroy** to switch it to the Released state.
6.  The Executing state has three substates: Flushed, Running, and End-of-Stream.
    
    -   After **OH\_VideoEncoder\_Start** is called, the encoder enters the Running substate immediately.
    -   When the encoder is in the Executing state, you can call **OH\_VideoEncoder\_Flush** to switch it to the Flushed substate.
    -   After all data to be processed is transferred to the encoder, the [AVCODEC\_BUFFER\_FLAGS\_EOS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-info-h#oh_avcodecbufferflags) flag is added to the last input buffer in the input buffers queue. Once this flag is detected, the encoder transits to the End-of-Stream substate. In this state, the encoder does not accept new inputs, but continues to generate outputs until it reaches the tail frame.
7.  When the encoder is no longer needed, you must call **OH\_VideoEncoder\_Destroy** to destroy the encoder instance, which then transitions to the Released state.
    

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h).

The figure below shows the call relationship of video encoding.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/c1Bl-Y-9TiWUeMPLww9eCQ/en-us_image_0000002537925102.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=693F9E7D29E684E41E94F3909B461D6712E9DC026FE077E988DD9C4A073FA55F)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_venc.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/iibt4N_RTyu-vGbA_0COzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0719365541E430F01E3160C51EBFB78670130210516A4304F276BFF9E0979E0D)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## Defining the Basic Structure

The sample code provided in this section adheres to the C++17 standard and is for reference only. You can define your own buffer objects by referring to it.

1.  Add the header files.
    
    #include <condition\_variable>
    #include <memory>
    #include <mutex>
    #include <queue>
    #include <shared\_mutex>
    
2.  Define the information about the encoder callback buffer.
    
    struct CodecBufferInfo {
        CodecBufferInfo(uint32\_t index, OH\_AVBuffer \*buffer): index(index), buffer(buffer), isValid(true) {}
        CodecBufferInfo(uint32\_t index, OH\_AVFormat \*parameter): index(index), parameter(parameter), isValid(true) {}
        // Callback buffer.
        OH\_AVBuffer \*buffer = nullptr;
        // In surface mode, pass the frame-specific parameter of the callback, which can be used only after the frame-specific parameter callback function is registered.
        OH\_AVFormat \*parameter = nullptr;
        // Index of the callback buffer.
        uint32\_t index = 0;
        // Check whether the current buffer information is valid.
        bool isValid = true;
    };
    
3.  Define the input and output queue for encoding.
    
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
    // Pointer to the encoder instance.
    OH\_AVCodec \*videoEnc = nullptr;
    // Encoder synchronization lock.
    std::shared\_mutex codecMutex;
    // Encoder input queue.
    CodecBufferQueue inQueue;
    // Encoder output queue.
    CodecBufferQueue outQueue;
    

## Surface Mode

The following walks you through how to implement the entire video encoding process in surface mode and implement data rotation in asynchronous mode. In this example, surface data is input and encoded into a H.264 stream.

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
    -   **capability**: pointer to the encoder's capability.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC**: AVC video codec.
    
    The following is an example:
    
    // Create an encoder by name. If your application has special requirements, for example, expecting an encoder that supports a certain resolution, you can call OH\_AVCodec\_GetCapability to query the capability first.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
    // Create a hardware encoder instance.
    OH\_AVCapability \*capability= OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true, HARDWARE);
    const char \*codecName = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByName(codecName);
    
    // Create an encoder by MIME type. Only specific codecs recommended by the system can be created in this way.
    // The system preferentially creates a hardware encoder instance. If hardware encoding is not supported or all hardware encoder instances are occupied, a software encoder instance will be created.
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
    
3.  Call **OH\_VideoEncoder\_RegisterCallback()** to register the callback functions.
    
    Register the **OH\_AVCodecCallback** struct that defines the following callback function pointers:
    
    -   **OH\_AVCodecOnError**, a callback used to report a codec operation error. For details about the error codes, see [OH\_AVCodecOnError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconerror).
    -   **OH\_AVCodecOnStreamChanged**, a callback used to report a codec stream change, for example, format change.
    -   **OH\_AVCodecOnNeedInputBuffer**, a callback used to report input data required. This callback does not take effect, since you input data through the obtained surface.
    -   **OH\_AVCodecOnNewOutputBuffer**, a callback used to report output data generated, which means that encoding is complete.
    
    For details about the implementation of the callback function, see [Sample Project](https://gitee.com/harmonyos_samples/AVCodecVideo).
    
    The following is an example:
    
    // Set the OH\_AVCodecOnError callback function, which is used to report a codec operation error.
    static void OnError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)
    {
        // Process the error code in the callback.
        (void)codec;
        (void)errorCode;
        (void)userData;
    }
    
    // Set the OH\_AVCodecOnStreamChanged callback function, which is used to report an encoding stream change.
    static void OnStreamChanged(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)
    {
        (void)codec;
        (void)format;
        (void)userData;
        // Obtain the video width and height after the resolution change through format.
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height);
    }
    
    // Set the OH\_AVCodecOnNeedInputBuffer callback function, which is used to send an input frame to the data queue.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // In surface mode, this callback function does not take effect. Data is input through the obtained surface.
        (void)userData;
        (void)index;
        (void)buffer;
    }
    
    // Set the OH\_AVCodecOnNewOutputBuffer callback function, which is used to send an encoded frame to the output queue.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The data buffer of the finished frame and its index are sent to outQueue.
        (void)codec;
        (void)userData;
        outQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    // Call OH\_VideoEncoder\_RegisterCallback() to register the callback functions.
    OH\_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
    OH\_AVErrCode ret = OH\_VideoEncoder\_RegisterCallback(videoEnc, cb, nullptr); // nullptr: userData on which the callback depends is empty.
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/l-c_wVHcRxq8wPKrUfDtNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC1BCAC1CCE5FD743282C3C0570DB031A1CB766DB9444FDB6F3DD18F2DD87F82)
    
    In the callback functions, pay attention to multi-thread synchronization for operations on the data queue.
    
4.  (Optional) Call **OH\_VideoEncoder\_RegisterParameterCallback()** to register the frame-specific parameter callback function.
    
    For details, see [Temporally Scalable Video Coding](../temporally-scalable-video-coding/document.md).
    
     // 5.1 Implement the OH\_VideoEncoder\_OnNeedInputParameter callback function.
     static void OnNeedInputParameter(OH\_AVCodec \*codec, uint32\_t index, OH\_AVFormat \*parameter, void \*userData)
     {
         // The index of the input frame parameter is sent to InParameterIndexQueue.
         // The input frame data (specified by parameter) is sent to InParameterQueue.
         // Data processing
         // Write the frame-specific parameter.
         // The value of OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX must be greater than or equal to that of OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN.
         OH\_AVFormat\_SetIntValue(parameter, OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX, 30);
         OH\_AVFormat\_SetIntValue(parameter, OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN, 20);
     }
    
     // 5.2 Register the frame-specific parameter callback function.
     OH\_VideoEncoder\_OnNeedInputParameter inParaCb = OnNeedInputParameter;
     OH\_VideoEncoder\_RegisterParameterCallback(videoEnc, inParaCb, NULL); // NULL: userData is null.
    
5.  Call **OH\_VideoEncoder\_Configure()** to configure the encoder.
    
    For details about the configurable options, see [Video Dedicated Key-Value Paris](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-codecbase#media-data-key-value-pairs).
    
    For details about the parameter verification rules, see [OH\_VideoEncoder\_Configure()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-videoencoder-h#oh_videoencoder_configure).
    
    The parameter value ranges can be obtained through the capability query interface. For details, see [Obtaining Supported Codecs](../obtaining-supported-codecs/document.md).
    
    Currently, the following options must be configured for all supported formats: video frame width, video frame height, and video pixel format.
    
    // Configure the video frame rate.
    double frameRate = 30.0;
    // Configure the video YUV range flag.
    int32\_t rangeFlag = 0;
    // Configure the video primary color.
    int32\_t primary = static\_cast<int32\_t>(OH\_ColorPrimary::COLOR\_PRIMARY\_BT709);
    // Configure the transfer characteristics.
    int32\_t transfer = static\_cast<int32\_t>(OH\_TransferCharacteristic::TRANSFER\_CHARACTERISTIC\_BT709);
    // Configure the maximum matrix coefficient.
    int32\_t matrix = static\_cast<int32\_t>(OH\_MatrixCoefficient::MATRIX\_COEFFICIENT\_IDENTITY);
    // Configure the encoding profile.
    int32\_t profile = static\_cast<int32\_t>(OH\_AVCProfile::AVC\_PROFILE\_HIGH);
    // Configure the encoding bit rate mode.
    int32\_t rateMode = static\_cast<int32\_t>(OH\_BitrateMode::BITRATE\_MODE\_VBR);
    // Configure the key frame interval, in milliseconds.
    int32\_t iFrameInterval = 1000;
    // Configure the SQR factor.
    int32\_t sqrFactor = 30;
    // Configure the maximum bit rate, in bit/s.
    int64\_t maxBitRate = 20000000;
    // Configure the bit rate, in bit/s.
    int64\_t bitRate = 5000000;
    // Set the encoding quality.
    int64\_t quality = 90;
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat); // Mandatory.
    
    OH\_AVFormat\_SetDoubleValue(format.get(), OH\_MD\_KEY\_FRAME\_RATE, frameRate);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_RANGE\_FLAG, rangeFlag);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_COLOR\_PRIMARIES, primary);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS, transfer);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_MATRIX\_COEFFICIENTS, matrix);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_I\_FRAME\_INTERVAL, iFrameInterval);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PROFILE, profile);
    // Configure OH\_MD\_KEY\_QUALITY only when OH\_BitrateMode is set to BITRATE\_MODE\_CQ.
    if (rateMode == static\_cast<int32\_t>(OH\_BitrateMode::BITRATE\_MODE\_CQ)) {
        OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_QUALITY, quality);
    } else if (rateMode == static\_cast<int32\_t>(OH\_BitrateMode::BITRATE\_MODE\_SQR)) {
        // Configure OH\_MD\_KEY\_MAX\_BITRATE and OH\_MD\_KEY\_SQR\_FACTOR only when OH\_BitrateMode is set to BITRATE\_MODE\_SQR.
        OH\_AVFormat\_SetLongValue(format.get(), OH\_MD\_KEY\_MAX\_BITRATE, maxBitRate);
        OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_SQR\_FACTOR, sqrFactor);
    } else if (rateMode == static\_cast<int32\_t>(OH\_BitrateMode::BITRATE\_MODE\_CBR) ||
               rateMode == static\_cast<int32\_t>(OH\_BitrateMode::BITRATE\_MODE\_VBR)){
        OH\_AVFormat\_SetLongValue(format.get(), OH\_MD\_KEY\_BITRATE, bitRate);
    }
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, rateMode);
    OH\_AVErrCode ret = OH\_VideoEncoder\_Configure(videoEnc, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/2JmniGiVRWOQvwEDI0vb9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B553E5AAB2CA78CB4F129449C9EFAD8C894D6E51100B9BF7A3C9352BCCE4D72)
    
    If an optional parameter is incorrectly configured, the error code **AV\_ERR\_INVALID\_VAL** is returned. However, **OH\_VideoEncoder\_Configure()** does not fail. Instead, its execution continues with the default value.
    
6.  Obtain a surface.
    
    Obtain the OHNativeWindow in surface mode. The surface must be obtained before **OH\_VideoEncoder\_Prepare** is called.
    
    // Obtain the surface used for data input.
    OHNativeWindow \*nativeWindow;
    OH\_AVErrCode ret = OH\_VideoEncoder\_GetSurface(videoEnc, &nativeWindow);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Use the OHNativeWindow\* variable to obtain the address of the data to be filled through the producer interface.
    
    For details about how to use the OHNativeWindow\* variable-type, see [OHNativeWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativewindow).
    
7.  Call **OH\_VideoEncoder\_Prepare()** to prepare internal resources for the encoder.
    
    OH\_AVErrCode ret = OH\_VideoEncoder\_Prepare(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
8.  Call **OH\_VideoEncoder\_Start()** to start the encoder.
    
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
    
9.  (Optional) Call **OH\_VideoEncoder\_SetParameter()** to dynamically configure encoder parameters during running.
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    
    // Dynamically request IDR frames.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_REQUEST\_I\_FRAME, true);
    // Dynamically reset the bit rate.
    int64\_t bitRate = 2000000;
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, bitRate);
    // Dynamically reset the video frame rate.
    double frameRate = 60.0;
    OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, frameRate);
    // The QP can be dynamically set.
    // The value of OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX must be greater than or equal to that of OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX, 30);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN, 20);
    
    int32\_t ret = OH\_VideoEncoder\_SetParameter(videoEnc, format);
    if (ret != AV\_ERR\_OK) {
        // Exception handling.
    }
    OH\_AVFormat\_Destroy(format);
    
10.  Write the image to encode.
     
     In step 6, you have configured the **OHNativeWindow**\* variable type returned by **OH\_VideoEncoder\_GetSurface**. The data required for encoding is continuously input by the surface. Therefore, you do not need to process the **OnNeedInputBuffer** callback function or use **OH\_VideoEncoder\_PushInputBuffer** to input data.
     
     This rule also applies in variable resolution scenarios.
     
11.  (Optional) Call **OH\_VideoEncoder\_PushInputParameter()** to notify the encoder that the frame-specific parameter configuration is complete.
     
     In step 4, you have registered the frame-specific parameter callback function.
     
     In the code snippet below, the following variables are used:
     
     -   **index**: parameter passed by the callback function **OnNeedInputParameter**, which uniquely corresponds to the buffer.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // You can determine the value.
     int32\_t isIFrame;
     OH\_AVFormat\_SetIntValue(bufferInfo->parameter, OH\_MD\_KEY\_REQUEST\_I\_FRAME, isIFrame);
     OH\_AVErrCode ret = OH\_VideoEncoder\_PushInputParameter(videoEnc, bufferInfo->index);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
12.  Call **OH\_VideoEncoder\_NotifyEndOfStream()** to notify the encoder of EOS.
     
     // In surface mode, you only need to call this API to notify the encoder of EOS.
     // In buffer mode, you need to set the AVCODEC\_BUFFER\_FLAGS\_EOS flag and then call OH\_VideoEncoder\_PushInputBuffer to notify the encoder of EOS.
     OH\_AVErrCode ret = OH\_VideoEncoder\_NotifyEndOfStream(videoEnc);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
13.  Call **OH\_VideoEncoder\_FreeOutputBuffer()** to release encoded frames.
     
     In the following example, the member variables of **bufferInfo** are as follows:
     
     -   **index**: parameter passed by the callback function **OnNewOutputBuffer**, which uniquely corresponds to the buffer.
     -   **buffer**: parameter passed by the callback function **OnNewOutputBuffer**. You can obtain the pointer to the shared memory address by calling [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr).
     -   **isValid**: whether the buffer instance stored in **bufferInfo** is valid.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     int32\_t qpAverage = 20;
     double mseValue = 0.0;
     OH\_AVFormat \*format = OH\_AVBuffer\_GetParameter(bufferInfo->buffer);
     OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_AVERAGE, &qpAverage);
     OH\_AVFormat\_GetDoubleValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_MSE, &mseValue);
     OH\_AVFormat\_Destroy(format);
     // Obtain the encoded information.
     OH\_AVCodecBufferAttr info;
     int32\_t ret = OH\_AVBuffer\_GetBufferAttr(bufferInfo->buffer, &info);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Write the encoded frame data (specified by buffer) to the output file.
     outputFile->write(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(bufferInfo->buffer)), info.size);
     // Free the output buffer. index is the index of the buffer.
     ret = OH\_VideoEncoder\_FreeOutputBuffer(videoEnc, bufferInfo->index);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
14.  (Optional) Call **OH\_VideoEncoder\_Flush()** to refresh the encoder.
     
     After **OH\_VideoEncoder\_Flush** is called, the encoder remains in the Running state, but the input and output data and parameter set (such as the H.264 PPS/SPS) buffered in the encoder are cleared.
     
     To continue encoding, you must call **OH\_VideoEncoder\_Start** again.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Refresh the encoder.
     OH\_AVErrCode flushRet = OH\_VideoEncoder\_Flush(videoEnc);
     if (flushRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     inQueue.Flush();
     outQueue.Flush();
     // Start encoding again.
     OH\_AVErrCode startRet = OH\_VideoEncoder\_Start(videoEnc);
     if (startRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
15.  (Optional) Call **OH\_VideoEncoder\_Reset()** to reset the encoder.
     
     After **OH\_VideoEncoder\_Reset** is called, the encoder returns to the initialized state. To continue encoding, you must call **OH\_VideoEncoder\_Configure** and then **OH\_VideoEncoder\_Prepare**.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Reset the encoder.
     OH\_AVErrCode resetRet = OH\_VideoEncoder\_Reset(videoEnc);
     if (resetRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     inQueue.Flush();
     outQueue.Flush();
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
     
16.  (Optional) Call **OH\_VideoEncoder\_Stop()** to stop the encoder.
     
     After **OH\_VideoEncoder\_Stop** is called, the encoder retains the encoding instance and releases the input and output buffers. You can call **OH\_VideoEncoder\_Start** to continue encoding.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Stop the encoder.
     OH\_AVErrCode ret = OH\_VideoEncoder\_Stop(videoEnc);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     inQueue.Flush();
     outQueue.Flush();
     
17.  Call **OH\_VideoEncoder\_Destroy()** to destroy the encoder instance and release resources.
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/m4ivOqEgSWmc9zvePmoT4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=035FA80BC173F3CB96C64F7E9A118E0CEEFDFA6EFA3BF1F31C369A20C7863DE2)
     
     1.  This API cannot be called in the callback function.
     2.  After the call, you must set a null pointer to the encoder to prevent program errors caused by wild pointers.
     
     std::unique\_lock<std::shared\_mutex> lock(codecMutex);
     // Release the nativeWindow instance.
     if(nativeWindow != nullptr){
         OH\_NativeWindow\_DestroyNativeWindow(nativeWindow);
         nativeWindow = nullptr;
     }
     // Call OH\_VideoEncoder\_Destroy to destroy the encoder.
     OH\_AVErrCode ret = AV\_ERR\_OK;
     if (videoEnc != nullptr) {
         OH\_VideoEncoder\_Destroy(videoEnc);
         videoEnc = nullptr;
     }
     inQueue.Flush();
     outQueue.Flush();
     

## Buffer Mode

The following walks you through how to implement the entire video encoding process in buffer mode and implement data rotation in asynchronous mode. It uses the YUV file input and H.264 encoding format as an example.

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videoencoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fstream>
    
2.  Create an encoder instance.
    
    The procedure is the same as that in surface mode and is not described here.
    
    // Create an encoder by name. If your application has special requirements, for example, expecting an encoder that supports a certain resolution, you can call OH\_AVCodec\_GetCapability to query the capability first.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
    const char \*codecName = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByName(codecName);
    
    // Create an encoder by MIME type. Only specific codecs recommended by the system can be created in this way.
    // If multiple codecs need to be created, create hardware encoder instances first. If the hardware resources are insufficient, create software encoder instances.
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
    
3.  Call **OH\_VideoEncoder\_RegisterCallback()** to register the callback functions.
    
    Register the **OH\_AVCodecCallback** struct that defines the following callback function pointers:
    
    -   **OH\_AVCodecOnError**, a callback used to report a codec operation error. For details about the error codes, see [OH\_AVCodecOnError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconerror).
    -   **OH\_AVCodecOnStreamChanged**, a callback used to report a codec stream change, for example, format change.
    -   **OH\_AVCodecOnNeedInputBuffer**, a callback used to report input data required, which means that the encoder is ready for receiving YUV/RGB data.
    -   **OH\_AVCodecOnNewOutputBuffer**, a callback used to report output data generated, which means that encoding is complete.
    
    You need to process the callback functions to ensure that the encoder runs properly.
    
    For details about the implementation of the callback function, see [Sample Project](https://gitee.com/harmonyos_samples/AVCodecVideo).
    
    bool isFirstFrame = true;
    int32\_t qpAverage = 20;
    double mseValue = 0.0;
    
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
        // In buffer mode, this callback function does not take effect.
        (void)codec;
        (void)format;
        (void)userData;
    }
    
    // Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // Obtain the video width stride and height stride.
        if (isFirstFrame) {
            auto format = std::shared\_ptr<OH\_AVFormat>(OH\_VideoEncoder\_GetInputDescription(codec), OH\_AVFormat\_Destroy);
            if (format == nullptr) {
                // Handle exceptions.
            }
            bool ret = OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_STRIDE, &widthStride) &&
                       OH\_AVFormat\_GetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT, &heightStride);
            if (!ret) {
                // Handle exceptions.
            }
            isFirstFrame = false;
        }
        // The data buffer of the input frame and its index are sent to inQueue.
        (void)codec;
        (void)userData;
        inQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    // Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // Obtain the average QP and MSE of the video frame.
        OH\_AVFormat \*format = OH\_AVBuffer\_GetParameter(buffer);
        OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_AVERAGE, &qpAverage);
        OH\_AVFormat\_GetDoubleValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_MSE, &mseValue);
        OH\_AVFormat\_Destroy(format);
        // The data buffer of the finished frame and its index are sent to outQueue.
        (void)userData;
        outQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    // Call OH\_VideoEncoder\_RegisterCallback() to register the callback functions.
    OH\_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
    OH\_AVErrCode ret = OH\_VideoEncoder\_RegisterCallback(videoEnc, cb, nullptr);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/MRdaf-5SQ_2615OdaLs1KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7730AF627D43E9CBC742B004D5CCB79CEE35575FF3A9AEB58873135A0C67951)
    
    In the callback functions, pay attention to multi-thread synchronization for operations on the data queue.
    
4.  Call **OH\_VideoEncoder\_Configure()** to configure the encoder.
    
    The procedure is the same as that in surface mode and is not described here.
    
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // Set the format.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_WIDTH, width); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_HEIGHT, height); // Mandatory.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat); // Mandatory.
    // Configure the encoder.
    OH\_AVErrCode ret = OH\_VideoEncoder\_Configure(videoEnc, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Call **OH\_VideoEncoder\_Prepare()** to prepare internal resources for the encoder.
    
    OH\_AVErrCode ret = OH\_VideoEncoder\_Prepare(videoEnc);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Call **OH\_VideoEncoder\_Start()** to start the encoder.
    
    As soon as the encoder starts, the callback functions will be triggered to respond to events. Therefore, you must configure the input file and output file first.
    
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
    
7.  (Optional) Dynamically configure encoder parameters during running.
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    
    // Dynamically request IDR frames.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_REQUEST\_I\_FRAME, true);
    // Dynamically reset the bit rate.
    int64\_t bitRate = 2000000;
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, bitRate);
    // Dynamically reset the video frame rate.
    double frameRate = 60.0;
    OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, frameRate);
    
    int32\_t ret = OH\_VideoEncoder\_SetParameter(videoEnc, format);
    if (ret != AV\_ERR\_OK) {
        // Exception handling.
    }
    OH\_AVFormat\_Destroy(format);
    
8.  Call **OH\_VideoEncoder\_PushInputBuffer()** to push the image to the input queue for encoding.
    
    In the code snippet below, the following variables are used:
    
    -   **widthStride**: width stride of the obtained buffer data.
    -   **heightStride**: height stride of the obtained buffer data.
    
    The member variables of **bufferInfo** are as follows:
    
    -   **buffer**: parameter passed by the callback function **OnNeedInputBuffer**. You can obtain the pointer to the shared memory address by calling [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr).
    -   **index**: parameter passed by the callback function **OnNeedInputBuffer**, which uniquely corresponds to the buffer.
    -   **isValid**: whether the buffer instance stored in **bufferInfo** is valid.
    
    std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    if (bufferInfo == nullptr || !bufferInfo->isValid) {
        // Handle exceptions.
    }
    // Write image data.
    int32\_t frameSize = 0;
    if (widthStride == width && heightStride == height) {
        frameSize = width \* height \* 3 / 2; // Formula for calculating the data size of each frame in NV12 pixel format.
        int32\_t capacity = OH\_AVBuffer\_GetCapacity(bufferInfo->buffer);
        if (frameSize > capacity) {
            // Handle exceptions.
        }
        // Process the file stream and obtain the frame length, and then write the data to encode to the buffer of the specified index.
        uint8\_t \*addr = OH\_AVBuffer\_GetAddr(bufferInfo->buffer);
        if (addr == nullptr) {
           // Handle exceptions.
        }
        if (inputFile != nullptr && inputFile->is\_open()) {
            inputFile->read(reinterpret\_cast<char \*>(addr), frameSize);
        }
    } else {
        // If the stride is not equal to the width, perform offset based on the stride. For details, see the following example.
    }
    // Configure the buffer information.
    OH\_AVCodecBufferAttr info;
    info.size = frameSize;
    info.offset = 0;
    // Unlike the surface mode, in buffer mode, the application must explicitly set pts. Compute it based on the intended display time, for example, frameIndex \* 1000000 / frameRate.
    info.pts = 0;
    // To prevent the flags from being randomly initialized to AVCODEC\_BUFFER\_FLAGS\_EOS and causing abnormal usage, the flags must be assigned a value such as 0 (identifier for normal frames).
    info.flags = 0;
    OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(bufferInfo->buffer, &info);
    if (setBufferRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Configure the buffer frame-specific information.
    // You can determine the value.
    int32\_t isIFrame;
    auto parameter = std::shared\_ptr<OH\_AVFormat>(OH\_AVBuffer\_GetParameter(bufferInfo->buffer), OH\_AVFormat\_Destroy);
    if (parameter == nullptr) {
        // Handle exceptions.
    }
    OH\_AVFormat\_SetIntValue(parameter.get(), OH\_MD\_KEY\_REQUEST\_I\_FRAME, isIFrame);
    OH\_AVErrCode parameterRet = OH\_AVBuffer\_SetParameter(bufferInfo->buffer, parameter.get());
    if (parameterRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Send the data to the input buffer for encoding. index is the index of the buffer.
    OH\_AVErrCode pushInputRet = OH\_VideoEncoder\_PushInputBuffer(videoEnc, bufferInfo->index);
    if (pushInputRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    Offset the stride.
    
    The following uses an NV12 image as an example, presenting the image layout of **width**, **height**, **wStride**, and **hStride**.
    
    -   **OH\_MD\_KEY\_WIDTH** corresponds to **width**.
    -   **OH\_MD\_KEY\_HEIGHT** corresponds to **height**.
    -   **OH\_MD\_KEY\_VIDEO\_STRIDE** corresponds to **wStride**.
    -   **OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT** corresponds to **hStride**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/pHFv_qd7SXeFoHPfB_LRTQ/en-us_image_0000002568684879.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB7B900EFCCB08DBC5FF8189D8D1ADFDB339EFC23BC0AEA5CC84FAFDA3ED8020)
    
    Add the header files.
    
    #include <string.h>
    
    The sample code is as follows:
    
    struct Rect // Width and height of the source buffer. You can set them as required.
    {
        int32\_t width;
        int32\_t height;
    };
    
    struct DstRect // Width stride and height stride of the destination buffer. They are obtained by calling OH\_VideoEncoder\_GetInputDescription.
    {
        int32\_t wStride;
        int32\_t hStride;
    };
    
    struct SrcRect // Width stride and height stride of the source buffer. You can set them as required.
    {
        int32\_t wStride;
        int32\_t hStride;
    };
    
    Rect rect = {320, 240};
    DstRect dstRect = {320, 256};
    SrcRect srcRect = {320, 250};
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
    
    When processing buffer data (before pushing data) during hardware encoding, you must copy the image data after width and height alignment to the input callback AVBuffer.
    
    Generally, copy the image width, height, stride, and pixel format to ensure correct processing of the data to encode.
    
    For details, see step 3 in [Buffer Mode](#buffer-mode).
    
9.  Notify the encoder of EOS.
    
    During encoding, once the last frame of data is sent to the input buffer for encoding, set the flag of bufferInfo to AVCODEC\_BUFFER\_FLAGS\_EOS to notify the encoder that the input is complete.
    
    In the following example, the member variables of **bufferInfo** are as follows:
    
    -   **index**: parameter passed by the callback function **OnNeedInputBuffer**, which uniquely corresponds to the buffer.
    -   **buffer**: parameter passed by the callback function **OnNeedInputBuffer**. You can obtain the pointer to the shared memory address by calling [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr).
    -   **isValid**: whether the buffer instance stored in **bufferInfo** is valid.
    
    std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    if (bufferInfo == nullptr || !bufferInfo->isValid) {
        // Handle exceptions.
    }
    // Write the last frame of image data. For details, see step 8.
    // Configure the buffer information and set the AVCODEC\_BUFFER\_FLAGS\_EOS flag.
    OH\_AVCodecBufferAttr info;
    info.size = frameSize;
    info.offset = 0;
    // Unlike the surface mode, in buffer mode, the application must explicitly set pts. Compute it based on the intended display time, for example, frameIndex \* 1000000 / frameRate.
    info.pts = 0;
    info.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
    OH\_AVErrCode setBufferRet = OH\_AVBuffer\_SetBufferAttr(bufferInfo->buffer, &info);
    if (setBufferRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    OH\_AVErrCode pushInputRet = OH\_VideoEncoder\_PushInputBuffer(videoEnc, bufferInfo->index);
    if (pushInputRet != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  Call **OH\_VideoEncoder\_FreeOutputBuffer()** to release encoded frames.
     
     The procedure is the same as that in surface mode and is not described here.
     
     std::shared\_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
     std::shared\_lock<std::shared\_mutex> lock(codecMutex);
     if (bufferInfo == nullptr || !bufferInfo->isValid) {
         // Handle exceptions.
     }
     // Obtain the encoded information.
     OH\_AVCodecBufferAttr info;
     OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(bufferInfo->buffer, &info);
     if (getBufferRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Write the encoded frame data (specified by buffer) to the output file.
     uint8\_t \*addr = OH\_AVBuffer\_GetAddr(bufferInfo->buffer);
     if (addr == nullptr) {
        // Handle exceptions.
     }
     if (outputFile != nullptr && outputFile->is\_open()) {
         outputFile->write(reinterpret\_cast<char \*>(addr), info.size);
     }
     // Free the output buffer. index is the index of the buffer.
     OH\_AVErrCode freeOutputRet = OH\_VideoEncoder\_FreeOutputBuffer(videoEnc, bufferInfo->index);
     if (freeOutputRet != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     

The subsequent processes (including refreshing, resetting, stopping, and destroying the encoder) are the same as those in surface mode. For details, see steps 14–17 in [Surface Mode](#surface-mode).
