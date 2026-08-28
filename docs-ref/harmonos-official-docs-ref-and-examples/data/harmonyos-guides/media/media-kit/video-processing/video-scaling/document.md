# Video Scaling

With the [C APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-videoprocessing) provided by the VideoProcessing module, you can enhance the image detail within video streams and scale them. The processed data is suitable for use in display, playback, and recording.

Common usage scenarios are as follows: After video decoding, the video undergoes detail enhancement before being displayed by the **XComponent**.

#### Constraints

1.  To ensure real-time response, you are advised to create only one instance at a time.
2.  Only a video that meets the following conditions can be processed:
    -   The video is a standard dynamic range (SDR) video.
    -   The video pixel format is NV12 or NV21, and the output format is the same as the input format.
3.  Four levels of algorithms are provided, each offering better processing outcomes at the expense of increased performance degradation.
    
    | 
    Algorithm Level
    
     | 
    
    Input Resolution (Unit: Pixel)
    
     | 
    
    Output Resolution (Unit: Pixel)
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    NONE
    
     | 
    
    Width: (32, 2000\]
    
    Height: (32, 2000\]
    
     | 
    
    Width: (32, 2000\]
    
    Height: (32, 2000\]
    
     | 
    
    Applies only to scaling scenarios. No detail enhancement is provided.
    
     |
    | 
    
    LOW
    
     | 
    
    Width: (32, 2000\]
    
    Height: (32, 2000\]
    
     | 
    
    Width: (32, 2000\]
    
    Height: (32, 2000\]
    
     | 
    
    Applies only to scaling scenarios. No detail enhancement is provided during proportional scaling.
    
    During scaling, a basic level of detail enhancement is provided at a high processing speed.
    
    This level is the default setting.
    
     |
    | 
    
    MEDIUM
    
     | 
    
    Width: (32, 2000\]
    
    Height: (32, 2000\]
    
     | 
    
    Width: (32, 2000\]
    
    Height: (32, 2000\]
    
     | 
    
    Applies only to scaling scenarios. No detail enhancement is provided during proportional scaling.
    
    During scaling, a moderate level of detail enhancement is provided at a balanced processing speed.
    
     |
    | 
    
    HIGH
    
     | 
    
    Width: \[512, 2000\]
    
    Height: \[512, 2000\]
    
     | 
    
    Width: \[512, 2000\]
    
    Height: \[512, 2000\]
    
     | 
    
    Applies to scaling and detail enhancement scenarios. Detail enhancement is provided during proportional scaling.
    
    During scaling, a high level of detail enhancement is provided at a relatively low processing speed.
    
     |
    
4.  Do not directly call video processing APIs or perform other time-consuming operations in the video processing callback function. Instead, call them in the thread of the application.

#### Development Guidelines

For details, see [sample code](https://gitcode.com/HarmonyOS_Samples/VideoProcessing).

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libvideo\_processing.so)

## How to Develop

1.  Add the header files.
    
    #include <ace/xcomponent/native\_interface\_xcomponent.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/video\_processing\_engine/video\_processing.h>
    #include <multimedia/video\_processing\_engine/video\_processing\_types.h>
    #include <native\_window/external\_window.h>
    #include <native\_buffer/native\_buffer.h>
    
2.  (Optional) Create a decoding instance.
    
    The input of the detail enhancement module can be a video stream decoded by the system or video data filled into the window by the application (for example, the application directly fills data into the window after internal software decoding). If the system decoder is selected to process the video file or video streaming media, you can create a decoding instance as an input of the detail enhancement module.
    
    // Create a demuxer to parse audio and video information.
    OH\_AVSource\* source\_ = OH\_AVSource\_CreateWithFD(inputFd, inputFileOffset, inputFileSize);
    OH\_AVDemuxer\* demuxer\_ = OH\_AVDemuxer\_CreateWithSource(source\_);
    auto sourceFormat = std::shared\_ptr<OH\_AVFormat>(OH\_AVSource\_GetSourceFormat(source\_), OH\_AVFormat\_Destroy);
    // Create a video decoder.
    OH\_AVCodec \* decoder\_ = OH\_VideoDecoder\_CreateByMime(videoCodecMime.c\_str());
    // Configure video information.
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, videoWidth);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, videoHeight);
    OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, frameRate);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, pixelFormat);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ROTATION, rotation);
    int ret = OH\_VideoDecoder\_Configure(decoder\_, format);
    OH\_AVFormat\_Destroy(format);
    // Configure the callback function to maintain the buffer queue of the video decoder.
    OH\_VideoDecoder\_RegisterCallback(decoder\_,
            {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
             SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer}, videoDecContext\_);
    // Prepare the video decoder.
    int ret = OH\_VideoDecoder\_Prepare(decoder\_);
    // Create a decoding context.
    videoDecContext\_ = new CodecUserData;
    
3.  (Optional) Initialize the environment.
    
    This is usually executed on the initial use within a process to preemptively handle certain time-consuming operations.
    
    VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_InitializeEnvironment();
    
4.  Create a detail enhancement module.
    
    The application may create a detail enhancement module by using a video processing engine type. In the code snippet below, the following variables are used:
    
    -   **videoProcessor**: detail enhancement module instance.
    -   **VIDEO\_PROCESSING\_TYPE\_DETAIL\_ENHANCER**: detail enhancement type.
    -   **VIDEO\_PROCESSING\_SUCCESS**: expected return value.
    
    // Create a detail enhancement module instance by specifying the video processing engine type.
    VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Create(&videoProcessor, VIDEO\_PROCESSING\_TYPE\_DETAIL\_ENHANCER);
    
5.  Configure the asynchronous callback function.
    
    // Create a callback instance.
    ret = OH\_VideoProcessingCallback\_Create(&callback);
    // Bind the callback function.
    OH\_VideoProcessingCallback\_BindOnError(callback, OnError);
    OH\_VideoProcessingCallback\_BindOnState(callback, OnState);
    OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
    // Register the callback function.
    ret = OH\_VideoProcessing\_RegisterCallback(videoProcessor, callback, this);
    // Declare the callback function (userData is the user data passed during callback registration, for example, this pointer.)
    void OnError(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_ErrorCode error, void\* userData);
    void OnState(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_State state, void\* userData);
    void OnNewOutputBuffer(OH\_VideoProcessing\* videoProcessor, uint32\_t index, void\* userData);
    
6.  (Optional) Configure the detail enhancement level, which can be HIGH, MEDIUM, LOW, or NONE. If it is not configured, the LOW level is used by default.
    
    // Create a format instance.
    OH\_AVFormat\* parameter = OH\_AVFormat\_Create();
    // Specify the level.
    OH\_AVFormat\_SetIntValue(parameter, VIDEO\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL, VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_HIGH);
    // Configure parameters.
    OH\_VideoProcessing\_SetParameter(videoProcessor, parameter);
    
7.  Obtain a surface.
    
    // Configure the input for the algorithm.
    ret = OH\_VideoProcessing\_GetSurface(videoProcessor, inputWindow);
    // Bind the output of the decoder to the input of the algorithm, with the decoder's output window resolution being the algorithm's input resolution.
    OH\_VideoDecoder\_SetSurface(decoder\_,  inputWindow\_);
    
8.  Set the surface (for display).
    
    // Configure the output of the algorithm, with the configured output window resolution being the algorithm's output resolution.
    ret = OH\_VideoProcessing\_SetSurface(videoProcessor, outWindow);
    
9.  Create the input and output threads of the decoder.
    
    std::unique\_ptr<std::thread> videoDecInputThread\_ = std::make\_unique<std::thread>(&Player::VideoDecInputThread, this);
    std::unique\_ptr<std::thread> videoDecOutputThread\_ = std::make\_unique<std::thread>(&Player::VideoDecOutputThread, this);
    
10.  Start detail enhancement.
     
     // Start decoding.
     int ret = OH\_VideoDecoder\_Start(decoder\_);
     // Start detail enhancement.
     ret = OH\_VideoProcessing\_Start(videoProcessor);
     
11.  Call [OH\_VideoProcessing\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_stop) to disable detail enhancement.
     
     VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Stop(videoProcessor);
     
12.  Release the video processing instance.
     
     VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Destroy(videoProcessor);
     videoProcessor = nullptr;
     VideoProcessing\_ErrorCode ret = OH\_VideoProcessingCallback\_Destroy(callback);
     callback = nullptr;
     
13.  Release the video processing resources.
     
     VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_DeinitializeEnvironment();
