# Audio Encoding

You can call native APIs to perform audio encoding, which compresses audio PCM data into a desired format.

PCM data can be from any source. For example, you can use a microphone to record audio data or import edited PCM data. After audio encoding, you can output streams in the desired format and encapsulate the streams into a target file.

For details about the supported encoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#audio-encoding).

**When to Use**

-   Audio recording
    
    Record PCM data, encode it into the desired format, and then [multiplex](../../media-data-multiplexing-and-demultiplexing/media-data-multiplexing/document.md) it into an audio file in the desired format.
    
-   Audio editing
    
    Export edited PCM data, encode it into the corresponding audio format, and then [multiplex](../../media-data-multiplexing-and-demultiplexing/media-data-multiplexing/document.md) it into a file.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/gxDTe1MYSyCvFsDguSVaaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC55413C2774B70B68D81F8910C33A95FC953B6A4FA7A3FF86E0DB0F355C843E)

-   AAC encoders adopt the VBR mode by default. This may result in differences from the configured parameters.
-   By default, AAC encoders include an ADTS header in its output, which occupies the first 7 bytes of each frame.

#### Development Guidelines

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-audiocodec-h).

Refer to the code snippet below to complete the entire audio encoding process, including creating an encoder, setting encoding parameters (such as the sample rate, bit rate, and audio channel count), and starting, refreshing, resetting, and destroying the encoder.

During application development, you must call the APIs in the defined sequence. Otherwise, an exception or undefined behavior may occur.

The figure below shows the call relationship of audio encoding.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/3WJ8OIwMQuKvtkoQHZOFrg/en-us_image_0000002537765160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99CA28D787463441B2BC1A5C021EAE5360BE1588CDF818B3DA174061940316A0)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_acodec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qL1Jns5ZR-enl5BmvltSxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49B49F4951196A194DF2993A42AD03C3A81D7F9EAB619DEC6C2BB8A3477FAC00)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the required header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_audiocodec.h>
    #include <multimedia/native\_audio\_channel\_layout.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    
2.  Create an encoder instance. In the code snippet below, OH\_AVCodec \* is the pointer to the encoder instance created.
    
    You can create an encoder by MIME type or codec name.
    
    Method 1: Create an encoder by MIME type.
    
    // Specify whether encoding is used. The value true means encoding.
    bool isEncoder = true;
    // Create an encoder by MIME type.
    OH\_AVCodec \*audioEnc\_ = OH\_AudioCodec\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, isEncoder);
    
    Method 2: Create an encoder by codec name.
    
    // Create an encoder by name.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, true);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*audioEnc\_ = OH\_AudioCodec\_CreateByName(name);
    
    Add the header file and namespace.
    
    #include <mutex>
    #include <queue>
    // Namespace of the C++ standard library.
    using namespace std;
    
    The sample code is as follows:
    
    // Initialize the queues.
    class AEncBufferSignal {
    public:
        std::mutex inMutex\_;
        std::mutex outMutex\_;
        std::mutex startMutex\_;
        std::condition\_variable inCond\_;
        std::condition\_variable outCond\_;
        std::condition\_variable startCond\_;
        std::queue<uint32\_t> inQueue\_;
        std::queue<uint32\_t> outQueue\_;
        std::queue<OH\_AVBuffer \*> inBufferQueue\_;
        std::queue<OH\_AVBuffer \*> outBufferQueue\_;
    };
    AEncBufferSignal \*signal\_;
    
3.  Call **OH\_AudioCodec\_RegisterCallback()** to register callback functions.
    
    Register the **OH\_AVCodecCallback** struct that defines the following callback function pointers:
    
    -   **OH\_AVCodecOnError**, a callback used to report a codec operation error
    -   **OH\_AVCodecOnStreamChanged**, a callback not supported by the audio encoder yet
    -   **OH\_AVCodecOnNeedInputBuffer**, a callback used to report input data required, which means that the encoder is ready for receiving PCM data
    -   **OH\_AVCodecOnNewOutputBuffer**, a callback used to report output data generated, which means that encoding is complete
    
    You need to process the callback functions to ensure that the encoder runs properly.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/dvRYM59aQxSVE4Gu4NLwlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A22C59C35A0826B15AC20386D57AA2946511B65AD233E1BEB8C402326D37D91)
    
    Do not call the encoder APIs or perform time-consuming operations in the callbacks.
    
    // Implement the OH\_AVCodecOnError callback function.
    static void OnError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)
    {
        (void)codec;
        (void)errorCode;
        (void)userData;
    }
    // Implement the OH\_AVCodecOnStreamChanged callback function.
    static void OnOutputFormatChanged(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)
    {
        (void)codec;
        (void)format;
        (void)userData;
    }
    // Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnInputBufferAvailable(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*data, void \*userData)
    {
        (void)codec;
        // The input stream is sent to the InputBuffer queue.
        AEncBufferSignal \*signal = static\_cast<AEncBufferSignal \*>(userData);
        unique\_lock<mutex> lock(signal->inMutex\_);
        signal->inQueue\_.push(index);
        signal->inBufferQueue\_.push(data);
        signal->inCond\_.notify\_all();
    }
    // Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnOutputBufferAvailable(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*data, void \*userData)
    {
        (void)codec;
        // The index of the output buffer is sent to OutputQueue\_.
        // The encoded data is sent to the outBuffer queue.
        AEncBufferSignal \*signal = static\_cast<AEncBufferSignal \*>(userData);
        unique\_lock<mutex> lock(signal->outMutex\_);
        signal->outQueue\_.push(index);
        signal->outBufferQueue\_.push(data);
        signal->outCond\_.notify\_all();
    }
    
    Configure the callback information.
    
    signal\_ = new AEncBufferSignal();
    OH\_AVCodecCallback cb\_ = {&OnError, &OnOutputFormatChanged, &OnInputBufferAvailable, &OnOutputBufferAvailable};
    // Set the asynchronous callbacks.
    int32\_t ret = OH\_AudioCodec\_RegisterCallback(audioEnc\_, cb\_, signal\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Call **OH\_AudioCodec\_Configure** to configure the encoder.
    
    Key values of configuration options are described as follows:
    
    | Key | Description | AAC | FLAC | MPEG (MP3) | G711mu | Opus | AMR-NB | AMR-WB |
    | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
    | OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | Sample rate. | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory |
    | OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | Audio channel count. | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory |
    | OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | Output audio stream format. | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory | Mandatory |
    | OH\_MD\_KEY\_BITRATE | Bit rate. | Optional | Mandatory | Mandatory | \- | Mandatory | Mandatory | Mandatory |
    | OH\_MD\_KEY\_CHANNEL\_LAYOUT | Audio channel layout. | Optional | Mandatory | \- | \- | \- | \- | \- |
    | OH\_MD\_KEY\_MAX\_INPUT\_SIZE | Maximum input length. | Optional | Optional | Optional | Optional | Optional | Optional | Optional |
    | OH\_MD\_KEY\_PROFILE | Encoding profile. | Optional | \- | \- | \- | \- | \- | \- |
    | OH\_MD\_KEY\_COMPLIANCE\_LEVEL | Compatibility level. | \- | Optional | \- | \- | \- | \- | \- |
    
    The sample below lists the value range of each audio encoding type.
    
    | AAC-LC | 8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000 | 1, 2, 3, 4, 5, 6, 8 |
    
    | HE-AAC, HE-AAC v2| 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000 | 1, 2, 3, 4, 5, 6, 8 |
    
    | Opus |8000, 12000, 16000, 24000, 48000 | 1-2 |
    
    | AMR (AMR-NB) | 8000 | 1 |
    
    | AMR (AMR-WB) | 16000 | 1 |
    
    The code snippet below shows the API call process, where AAC encoding at the bit rate of 32000 bit/s is carried out on the PCM audio with the 44100 Hz sample rate, 2-channel stereo, and SAMPLE\_S16LE sample format.
    
    int32\_t ret;
    // (Mandatory) Configure the audio sample rate.
    constexpr uint32\_t DEFAULT\_SAMPLERATE = 44100;
    // (Mandatory) Configure the audio bit rate.
    constexpr uint64\_t DEFAULT\_BITRATE = 32000;
    // (Mandatory) Configure the audio channel count.
    constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 2;
    // (Mandatory) Configure the audio channel types.
    constexpr OH\_AudioChannelLayout CHANNEL\_LAYOUT = OH\_AudioChannelLayout::CH\_LAYOUT\_STEREO;
    // (Mandatory) Configure the audio bit depth.
    constexpr OH\_BitsPerSample SAMPLE\_FORMAT = OH\_BitsPerSample::SAMPLE\_S16LE;
    // (Optional) Configure the AAC profile. The default value is AAC\_PROFILE\_LC. Other values are AAC\_PROFILE\_HE and AAC\_PROFILE\_HE\_V2.
    constexpr int32\_t AAC\_PROFILE = OH\_AACProfile::AAC\_PROFILE\_LC;
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // Set the format.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_FORMAT);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_CHANNEL\_LAYOUT, CHANNEL\_LAYOUT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, AAC\_PROFILE);
    // Configure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    The following shows the API call process in the case of FLAC encoding.
    
    int32\_t ret;
    // (Mandatory) Configure the audio sample rate.
    constexpr uint32\_t DEFAULT\_SAMPLERATE = 44100;
    // (Mandatory) Configure the audio bit rate.
    constexpr uint64\_t DEFAULT\_BITRATE = 261000;
    // (Mandatory) Configure the audio channel count.
    constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 2;
    // (Mandatory) Configure the layout of audio channels.
    // The value can be CH\_LAYOUT\_MONO, CH\_LAYOUT\_STEREO, CH\_LAYOUT\_SURROUND, CH\_LAYOUT\_QUAD, CH\_LAYOUT\_5POINT0, CH\_LAYOUT\_5POINT1, CH\_LAYOUT\_6POINT1, or CH\_LAYOUT\_7POINT1.
    constexpr OH\_AudioChannelLayout CHANNEL\_LAYOUT = OH\_AudioChannelLayout::CH\_LAYOUT\_STEREO;
    // (Mandatory) Configure the audio bit depth. Only SAMPLE\_S16LE and SAMPLE\_S32LE are available for FLAC encoding.
    constexpr OH\_BitsPerSample SAMPLE\_FORMAT = OH\_BitsPerSample::SAMPLE\_S32LE;
    // Configure the audio compliance level. The default value is 0, and the value ranges from -2 to 2.
    constexpr int32\_t COMPLIANCE\_LEVEL = 0;
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // Set the format.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
    // Configure the audio sampling precision. In versions earlier than API version 20, this parameter must be set for FLAC encoding (the value can be 1). Otherwise, OH\_AudioCodec\_Configure returns the error code AV\_ERR\_INVALID\_VAL. However, this parameter has no actual effect and does not affect the encoding result. Starting from API version 20, you do not need to set it anymore.
    // constexpr int32\_t BITS\_PER\_CODED\_SAMPLE = 1;
    // OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE, BITS\_PER\_CODED\_SAMPLE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_FORMAT);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_CHANNEL\_LAYOUT, CHANNEL\_LAYOUT);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_COMPLIANCE\_LEVEL, COMPLIANCE\_LEVEL);
    // Configure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    AMR encoding process:
    
    int32\_t ret;
    // (Mandatory) Configure the audio sample rate. The input sample rate of AMR-NB is 8000 Hz (PCM), and that of AMR-WB is 16000 Hz (PCM).
    constexpr uint32\_t DEFAULT\_SAMPLERATE = 8000;
    // (Mandatory) Configure the audio bit rate.
    // AMR-NB supports the bit rates 4750, 5150, 5900, 6700, 7400, 7950, 10200, and 12200.
    // AMR-WB supports the bit rates 6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, and 23850.
    constexpr uint64\_t DEFAULT\_BITRATE = 10200;
    // (Mandatory) Configure the audio channel count.
    constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 1;
    // (Mandatory) Configure the audio channel types.
    constexpr OH\_AudioChannelLayout CHANNEL\_LAYOUT = OH\_AudioChannelLayout::CH\_LAYOUT\_MONO;
    // (Mandatory) Configure the audio bit depth.
    constexpr OH\_BitsPerSample SAMPLE\_FORMAT = OH\_BitsPerSample::SAMPLE\_S16LE;
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // Set the format.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_FORMAT);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_CHANNEL\_LAYOUT, CHANNEL\_LAYOUT);
    // Configure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    Opus encoding process:
    
    int32\_t ret;
    // (Mandatory) Configure the audio sample rate.
    // Sample rates supported by Opus: 8000, 12000, 16000, 24000, and 48000.
    constexpr uint32\_t DEFAULT\_SAMPLERATE = 8000;
    // (Mandatory) Configure the audio bit rate.
    // Bit rates supported by Opus: \[6000, 510000\].
    constexpr uint64\_t DEFAULT\_BITRATE = 6000;
    // (Mandatory) Configure the audio channel count.
    // Audio channel count supported by Opus: 1 and 2.
    constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 1;
    // (Mandatory) Configure the audio bit depth.
    // Bit depth supported by Opus: SAMPLE\_S16LE
    constexpr OH\_BitsPerSample SAMPLE\_FORMAT = OH\_BitsPerSample::SAMPLE\_S16LE;
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // Set the format.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_FORMAT);
    // Configure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Call **OH\_AudioCodec\_Prepare()** to prepare internal resources for the encoder.
    
    int32\_t ret = OH\_AudioCodec\_Prepare(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Call **OH\_AudioCodec\_Start()** to start the encoder.
    
    Add the header file.
    
    #include <fstream>
    
    The sample code is as follows:
    
    ifstream inputFile\_;
    ofstream outFile\_;
    
    // Set the input file path based on the actual situation.
    const char\* inputFilePath = "/";
    // Set the output file path based on the actual situation.
    const char\* outputFilePath = "/";
    // Open the path of the binary file to be encoded. (A PCM file is used as an example.)
    inputFile\_.open(inputFilePath, ios::in | ios::binary);
    // Set the path of the output file. (An encoded stream file is used as an example.)
    outFile\_.open(outputFilePath, ios::out | ios::binary);
    // Start encoding.
    int32\_t ret = OH\_AudioCodec\_Start(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
7.  Call **OH\_AudioCodec\_PushInputBuffer()** to write the data to encode. You should fill in complete input data before calling this API.
    
    The method for determining the number of samples per frame (**SAMPLES\_PER\_FRAME**) is as follows:
    
    AAC-LC encodes 1024 PCM samples per frame. Therefore, you are advised to input exactly 1024 samples at a time.
    
    HE-AAC encodes 2048 PCM samples per frame. Therefore, you are advised to input exactly 2048 samples at a time.
    
    For FLAC encoding, set **SAMPLES\_PER\_FRAME** based on the table below.
    
    | Sample Rate | Sample Count |
    | :-- | :-- |
    | 8000 | 576 |
    | 16000 | 1152 |
    | 22050 | 2304 |
    | 24000 | 2304 |
    | 32000 | 2304 |
    | 44100 | 4608 |
    | 48000 | 4608 |
    | 88200 | 8192 |
    | 96000 | 8192 |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/6ODuPJBXTd-9GSDOlq1vRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=753DC31A30F8EFE0822FA6E607A6C12C95DF65AB498864FF82C77A0F6AA3505B)
    
    Data volume (in bytes) of a single encoding input: Number of samples (**SAMPLES\_PER\_FRAME**) \* Number of channels \* Number of bytes per sample.
    
    In the case of FLAC encoding, use the table below to set the number of samples based on the sample rate to prevent possible file corruption.
    
    // Audio channel count.
    constexpr int32\_t DEFAULT\_CHANNEL\_COUNT = 2;
    // Number of samples. For example, the number of samples for AAC-LC is 1024.
    constexpr int32\_t SAMPLES\_PER\_FRAME = 1024;
    // Data volume (in bytes) of a single encoding input: Number of samples \* Number of channels \* Number of bytes per sample. (The sample format SAMPLE\_S16LE is used as an example.)
    // If the last frame of data does not meet the required length,you are advised to discard it or add padding.
    constexpr int32\_t INPUT\_FRAME\_BYTES = SAMPLES\_PER\_FRAME \* DEFAULT\_CHANNEL\_COUNT \* sizeof(short);
    uint32\_t index = signal\_->inQueue\_.front();
    auto buffer = signal\_->inBufferQueue\_.front();
    OH\_AVCodecBufferAttr attr = {0};
    if (!inputFile\_.eof()) {
        inputFile\_.read((char \*)OH\_AVBuffer\_GetAddr(buffer), INPUT\_FRAME\_BYTES);
        attr.size = INPUT\_FRAME\_BYTES;
        attr.flags = AVCODEC\_BUFFER\_FLAGS\_NONE;
    } else {
        attr.size = 0;
        attr.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
    }
    OH\_AVBuffer\_SetBufferAttr(buffer, &attr);
    // Send the data to the input queue for encoding. The index is the subscript of the queue.
    int32\_t ret = OH\_AudioCodec\_PushInputBuffer(audioEnc\_, index);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    In the preceding example, **attr.flags** indicates the type of the buffer flag.
    
    When finished, set the flags to **AVCODEC\_BUFFER\_FLAGS\_EOS**.
    
    | Value | Description |
    | :-- | :-- |
    | AVCODEC\_BUFFER\_FLAGS\_NONE | Common frame. |
    | AVCODEC\_BUFFER\_FLAGS\_EOS | The buffer is an end-of-stream frame. |
    | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | The buffer contains codec-specific data. |
    
8.  Call **OH\_AudioCodec\_FreeOutputBuffer()** to release the encoded data.
    
    Once you have retrieved the encoded stream, call **OH\_AudioCodec\_FreeOutputBuffer()** to free up the data.
    
    uint32\_t index = signal\_->outQueue\_.front();
    OH\_AVBuffer \*avBuffer = signal\_->outBufferQueue\_.front();
    if (avBuffer == nullptr) {
        // Handle exceptions.
    }
    // Obtain the buffer attributes.
    OH\_AVCodecBufferAttr attr = {0};
    int32\_t ret = OH\_AVBuffer\_GetBufferAttr(avBuffer, &attr);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Write the encoded data (specified by data) to the output file.
    outFile\_.write(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(avBuffer)), attr.size);
    // Release the output buffer.
    ret = OH\_AudioCodec\_FreeOutputBuffer(audioEnc\_, index);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    if (attr.flags == AVCODEC\_BUFFER\_FLAGS\_EOS) {
        // End.
    }
    
9.  (Optional) Call **OH\_AudioCodec\_Flush()** to refresh the encoder.
    
    After **OH\_AudioCodec\_Flush()** is called, the current encoding queue is cleared.
    
    To continue encoding, you must call **OH\_AudioCodec\_Start()** again.
    
    Usage:
    
    -   To use the same encoder configuration after **AVCODEC\_BUFFER\_FLAGS\_EOS** of the output buffer is set, call **OH\_AudioCodec\_Flush()** to refresh the encoder.
    -   If a recoverable error occurs during the execution (**OH\_AudioCodec\_IsValid()** returns **true**), you can call **OH\_AudioCodec\_Flush()** to refresh the encoder and then call **OH\_AudioCodec\_Start()** to start encoding again.
    
    // Refresh the encoder.
    int32\_t ret = OH\_AudioCodec\_Flush(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Start encoding again.
    ret = OH\_AudioCodec\_Start(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
10.  (Optional) Call **OH\_AudioCodec\_Reset()** to reset the encoder.
     
     After **OH\_AudioCodec\_Reset()** is called, the encoder returns to the initialized state. The input and output buffers obtained before the reset cannot be used. You must call **OH\_AudioCodec\_Configure()** to reconfigure the encoder and then call **OH\_AudioCodec\_Start()** to start encoding again. Obtain the input and output buffers again after the encoder is started.
     
     // Reset the encoder.
     int32\_t ret = OH\_AudioCodec\_Reset(audioEnc\_);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     // Reconfigure the encoder.
     ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
11.  Call **OH\_AudioCodec\_Stop()** to stop the encoder.
     
     After the encoder is stopped, you can call **OH\_AudioCodec\_Start()** to start it again. The input and output buffers obtained before the encoder is stopped cannot be reused. You must obtain them again after the encoder is started.
     
     // Stop the encoder.
     int32\_t ret = OH\_AudioCodec\_Stop(audioEnc\_);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     }
     
12.  Call **OH\_AudioCodec\_Destroy()** to destroy the encoder instance and release resources.
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/_nT3iQFLT_O_r1yFHfTvAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E1A8F72DDC02F00444C56105D32239CB657143981B06E568814F98E06CFE6B9)
     
     You only need to call this API once.
     
     // Call OH\_AudioCodec\_Destroy to destroy the encoder.
     int32\_t ret = OH\_AudioCodec\_Destroy(audioEnc\_);
     if (ret != AV\_ERR\_OK) {
         // Handle exceptions.
     } else {
         audioEnc\_ = NULL; // The encoder cannot be destroyed repeatedly.
     }
