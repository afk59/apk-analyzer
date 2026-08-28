# Synchronous Audio Encoding

Starting from API version 20, audio encoding in synchronous mode is supported.

You can call native APIs to perform audio encoding, which compresses audio PCM data into a desired format.

PCM data can be from any source. For example, you can use a microphone to record audio data or import edited PCM data. After audio encoding, you can output streams in the desired format and encapsulate the streams into a target file.

For details about the supported encoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#audio-encoding).

**When to Use**

Asynchronous mode is generally recommended for most use cases. For details, see [Audio Encoding](../audio-encoding/document.md). Synchronous mode can be used if you need to actively request buffers for PCM encoding.

-   Audio recording
    
    Record PCM data, encode it into the desired format, and then multiplex it in the target file format. For details about multiplexing, see [Media Data Multiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-multiplexing/document.md).
    
-   Audio editing
    
    Export edited PCM data, encode it into the corresponding audio format, and then multiplex it into a file. For details about multiplexing, see [Media Data Multiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-multiplexing/document.md).
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/FsJap4WuQdu0ll1dj1evNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28355FCC70445EA031CCA60B466EA262DFB68FA5B9BA45D0A7EC7AE8D5BD0C4D)

-   AAC encoders adopt the VBR mode by default. This may result in differences from the expected bit rate.
-   By default, AAC encoders include an ADTS header in its output, which occupies the first 7 bytes of each frame.

#### Development Guidelines

Read [AudioCodec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-audiocodec-h) for the API reference.

Refer to the code snippet below to complete the entire audio encoding process, including creating an encoder, setting encoding parameters (such as the sample rate, bit rate, and audio channel count), and starting, refreshing, resetting, and destroying the encoder.

During application development, you must call the APIs in the defined sequence. Otherwise, an exception or undefined behavior may occur.

The figure below shows the call relationship of audio codec in synchronous mode.

-   The dotted line indicates an optional operation. Audio encoding does not involve decryption. Therefore, you do not need to call **OH\_AudioCodec\_SetDecryptionConfig**.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/G3hG6Mz1T2qliM2UdWnDGA/en-us_image_0000002537925100.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FFD4F694B1484C1AB34233B2477EC1B2834317345EFAE725EA99A4488DC0814)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_acodec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Fxz77SpgRoGdEqK8kguhAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4660896453E46A47AD86E7A36D52EB909744BDF14EB4CE32BCB2970CB057CFA4)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the header files and namespace.
    
    #include <multimedia/player\_framework/native\_avcodec\_audiocodec.h>
    #include <multimedia/native\_audio\_channel\_layout.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    
    // Namespace of the C++ standard library.
    using namespace std;
    
2.  Create an encoder instance. In the code snippet below, \*\*OH\_AVCodec \*\*\* is the pointer to the encoder instance created.
    
    You can create an encoder by MIME type or codec name.
    
    Method 1: Create an encoder by MIME type.
    
    // Create an encoder by MIME type. The following example creates an AAC encoder. The second parameter is set to true to indicate encoding.
    OH\_AVCodec \*audioEnc\_ = OH\_AudioCodec\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, true);
    
    Method 2: Create an encoder by codec name.
    
    // Create an encoder by name.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, true);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*audioEnc\_ = OH\_AudioCodec\_CreateByName(name);
    
3.  Call **OH\_AudioCodec\_Configure** to configure the encoder.
    
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
    
    OH\_AVErrCode ret;
    // (Mandatory) Configure the audio sample rate.
    constexpr uint32\_t DEFAULT\_SAMPLERATE = 44100;
    // (Mandatory) Configure the audio bit rate.
    constexpr uint64\_t DEFAULT\_BITRATE = 32000;
    // (Mandatory) Configure the audio channel count.
    constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 2;
    // (Mandatory) Configure the audio bit depth.
    constexpr OH\_BitsPerSample SAMPLE\_FORMAT = OH\_BitsPerSample::SAMPLE\_S16LE;
    // (Optional) Configure the AAC profile. The default value is AAC\_PROFILE\_LC. Other values are AAC\_PROFILE\_HE and AAC\_PROFILE\_HE\_V2.
    constexpr int32\_t AAC\_PROFILE = OH\_AACProfile::AAC\_PROFILE\_LC;
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // Set the format.
    OH\_AVFormat\_SetIntValue(format,OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
    OH\_AVFormat\_SetIntValue(format,OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
    OH\_AVFormat\_SetLongValue(format,OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_FORMAT);
    OH\_AVFormat\_SetLongValue(format,OH\_MD\_KEY\_CHANNEL\_LAYOUT, CHANNEL\_LAYOUT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, AAC\_PROFILE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set the synchronous mode.
    // Configure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    FLAC encoding example:
    
    OH\_AVErrCode ret;
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
    // Configure the audio compliance level. The default value is 0, and the value range is \[-2,2\].
    constexpr int32\_t COMPLIANCE\_LEVEL = 0;
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // Set the format.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_FORMAT);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_CHANNEL\_LAYOUT, CHANNEL\_LAYOUT);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_COMPLIANCE\_LEVEL, COMPLIANCE\_LEVEL);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set synchronous mode.
    // Configure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Call **OH\_AudioCodec\_Prepare()** to prepare internal resources for the encoder.
    
    OH\_AVErrCode ret = OH\_AudioCodec\_Prepare(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Call **OH\_AudioCodec\_Start()** to start the encoder.
    
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
    // Set the path of the output file. (In this example, the output file is an encoded stream file, instead of a playable audio file. To create a playable audio file, you must encapsulate the audio bit stream into a container).
    outFile\_.open(outputFilePath, ios::out | ios::binary);
    // Start encoding.
    OH\_AVErrCode ret = OH\_AudioCodec\_Start(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  Invoke synchronous mode to write PCM samples to encode and obtain the encoded audio frames.
    
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
    
    Data volume (in bytes) of a single encoding input: Number of samples (**SAMPLES\_PER\_FRAME**) \* Number of channels \* Number of bytes per sample.
    
    The sample code is as follows:
    
    int32\_t SAMPLES\_PER\_FRAME = 1024;
    // AAC LC encoding involves 1024 samples per frame, 2 channels, and uses S16LE format for the input data. Each 16-bit sample occupies 2 bytes.
    int32\_t inputFrameBytes = SAMPLES\_PER\_FRAME \* 2 \* 2;
    bool inputFinished = false;
    OH\_AVErrCode ret;
    OH\_AVCodecBufferAttr attr;
    
    for (;;) {
        uint32\_t index = 0;
        if (!inputFinished) {
            ret = OH\_AudioCodec\_QueryInputBuffer(audioEnc\_, &index, 20000); // 20000us
            if (ret == AV\_ERR\_TRY\_AGAIN\_LATER) {
                continue;
            }
            if (ret != AV\_ERR\_OK) {
                // Handle exceptions.
                break;
            }
            OH\_AVBuffer \*inputBuf = OH\_AudioCodec\_GetInputBuffer(audioEnc\_, index);
            if (inputBuf == nullptr) {
                // Handle exceptions.
                break;
            }
            memset(&attr, 0, sizeof(attr));
            if (!inputFile\_.eof()) {
                inputFile\_.read((char \*)OH\_AVBuffer\_GetAddr(inputBuf), inputFrameBytes);
                int32\_t readSize = inputFile\_.gcount();
                attr.size = readSize;
                attr.flags = readSize != 0 ? AVCODEC\_BUFFER\_FLAGS\_NONE : AVCODEC\_BUFFER\_FLAGS\_EOS;
            } else {
                inputFinished = true;
                attr.size = 0;
                attr.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
            }
            if (OH\_AVBuffer\_SetBufferAttr(inputBuf, &attr) != AV\_ERR\_OK) {
                // Handle exceptions.
            }
            if (OH\_AudioCodec\_PushInputBuffer(audioEnc\_, index) != AV\_ERR\_OK) {
                // Handle exceptions.
            }
        }
        // If the input data can generate multiple encoded frames, you need to call the output buffer several times to obtain all the encoded data.
        ret = OH\_AudioCodec\_QueryOutputBuffer(audioEnc\_, &index, 20000); // 20000us
        if (ret == AV\_ERR\_TRY\_AGAIN\_LATER) {
            // Timeout: There is not enough input data to encode a frame, or the timeout period is too short.
            continue;
        }
        if (ret != AV\_ERR\_OK) {
            // Handle exceptions.
            break;
        }
        OH\_AVBuffer \*outputBuf = OH\_AudioCodec\_GetOutputBuffer(audioEnc\_, index);
        if (outputBuf == nullptr) {
            // Handle exceptions.
            break;
        }
        if (OH\_AVBuffer\_GetBufferAttr(outputBuf, &attr) != AV\_ERR\_OK) {
            // Handle exceptions.
            break;
        }
        if (attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
            // The output ends.
            break;
        }
        // In this example, the data is written to a file for logging purposes. To encapsulate the data into an audio file, call OH\_AVMuxer\_WriteSampleBuffer.
        outFile\_.write(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(outputBuf)), attr.size);
        OH\_AudioCodec\_FreeOutputBuffer(audioEnc\_, index);
    }
    
    In the preceding example, **attr.flags** indicates the type of the buffer flag.
    
    When finished, set the flags to **AVCODEC\_BUFFER\_FLAGS\_EOS**.
    
    | Value | Description |
    | :-- | :-- |
    | AVCODEC\_BUFFER\_FLAGS\_NONE | Common frame. |
    | AVCODEC\_BUFFER\_FLAGS\_EOS | The buffer is an end-of-stream frame. |
    | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | The buffer contains codec-specific data. |
    
7.  (Optional) Call **OH\_AudioCodec\_Reset()** to reset the encoder.
    
    After **OH\_AudioCodec\_Reset()** is called, the encoder returns to the initialized state. The input and output buffers obtained before the reset cannot be used. You must call **OH\_AudioCodec\_Configure()** to reconfigure the encoder and then call **OH\_AudioCodec\_Start()** to start encoding again. Obtain the input and output buffers again after the decoder is started.
    
    // Reset the encoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Reset(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Reconfigure the encoder.
    ret = OH\_AudioCodec\_Configure(audioEnc\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
8.  (Optional) Call **OH\_AudioCodec\_Stop()** to stop the encoder.
    
    After the encoder is stopped, you can call **OH\_AudioCodec\_Start()** to start it again. The input and output buffers obtained before the decoder is stopped cannot be reused. You must obtain them again after the decoder is started.
    
    // Stop the encoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Stop(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
9.  Call **OH\_AudioCodec\_Destroy()** to destroy the encoder instance and release resources.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/lPYMTXwPQnWPyB9v00AnCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=945DF0F69601C160613FF7913DF00DD09FBEE6DE95F5D4E8C00E93EADC30CBEB)
    
    You only need to call this API once.
    
    // Call OH\_AudioCodec\_Destroy to destroy the encoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Destroy(audioEnc\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    } else {
        audioEnc\_ = NULL; // The encoder cannot be destroyed repeatedly.
    }
