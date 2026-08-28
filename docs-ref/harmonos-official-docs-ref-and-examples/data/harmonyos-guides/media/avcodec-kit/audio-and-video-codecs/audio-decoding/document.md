# Audio Decoding

You can call native APIs to perform audio decoding, which decodes media data into PCM streams.

For details about the supported decoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#audio-decoding).

**When to Use**

-   Audio playback
    
    Decode audio and transmit the data to the speaker for playing.
    
-   Audio rendering
    
    Decode audio and transmit the data to the audio processing module for audio rendering.
    
-   Audio editing
    
    Decode audio and transmit the data for audio editing (for example, adjusting the playback speed of a channel). Audio editing is performed based on PCM streams.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/wfRrsZc-TUWOFOA_EDI95Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5177BA246D4C006EFC8C2F0D720390309CE4AEFBBE3D21A9F531D35398B87185)

Streams generated in the MP3 audio encoding process cannot be directly decoded through the MP3 audio decoding process. The following process is recommended: PCM stream -> MP3 audio encoding -> multiplexing -> demultiplexing -> MP3 audio decoding.

#### Development Guidelines

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-audiocodec-h).

Refer to the code snippet below to complete the entire audio decoding process, including creating a decoder, setting decoding parameters (such as the sample rate, bit rate, and audio channel count), and starting, refreshing, resetting, and destroying the decoder.

During application development, you must call the APIs in the defined sequence. Otherwise, the system may throw exceptions or exhibit other undefined behaviors.

The figure below shows the call relationship of audio decoding.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/FJ7F72jvTrCxYyFUHaySYg/en-us_image_0000002537765160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23649DDEAED36BA739B0D06EEB02192E7C81533E12E54AB988C928E4B3CBCE2F)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_acodec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Vf0R4dmmQSev0jkgtQ4DmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA6EEF2CB563CF662D6ED8DE8F8B7FD7FEDB78BBA4F4369BDCB0FC48F5FC940D)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the required header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_audiocodec.h>
    #include <multimedia/native\_audio\_channel\_layout.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    
2.  Create a decoder instance. In the code snippet below, OH\_AVCodec \* is the pointer to the decoder instance created.
    
    You can create a decoder by MIME type or codec name.
    
    Method 1: Create a decoder by MIME type.
    
    // Specify whether encoding is used. The value false means decoding.
    bool isEncoder = false;
    // Create a decoder by MIME type.
    OH\_AVCodec \*audioDec\_ = OH\_AudioCodec\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, isEncoder);
    
    Method 2: Create a decoder by codec name.
    
    // Create a decoder by name.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, false);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*audioDec\_ = OH\_AudioCodec\_CreateByName(name);
    
    Add the header files and namespace.
    
    #include <mutex>
    #include <queue>
    // Namespace of the C++ standard library.
    using namespace std;
    
    The sample code is as follows:
    
    // Initialize the queues.
    class ADecBufferSignal {
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
    ADecBufferSignal \*signal\_;
    
3.  Call **OH\_AudioCodec\_RegisterCallback()** to register callback functions.
    
    Register the **OH\_AVCodecCallback** struct that defines the following callback function pointers:
    
    -   **OH\_AVCodecOnError**, a callback used to report a codec operation error
    -   **OH\_AVCodecOnStreamChanged**, a callback used to report stream information changes, including changes in the sample rate, audio channel count, and audio sample format. The decoding formats that can detect these changes include Audio Vivid, AAC, FLAC, MP3, and VORBIS. (This callback is supported since API version 15.)
    -   **OH\_AVCodecOnNeedInputBuffer**, a callback used to report input data required, which means that the decoder is ready for receiving data
    -   **OH\_AVCodecOnNewOutputBuffer**, a callback used to report output data generated, which means that decoding is complete
    
    You need to process the callback functions to ensure that the decoder runs properly.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/fNGzTFAbTISlLsVVMAn4UQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B77B48F2940A17DD97E45E776FF4B9C6ABECCA7840170A1273176491AE4A32B)
    
    Do not call the decoder APIs or perform time-consuming operations in the callbacks.
    
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
        (void)userData;
        // Callback processing after the decoding output parameters are changed. The application performs processing as required.
        int32\_t sampleRate;
        int32\_t channelCount;
        int32\_t sampleFormat;
        if (OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, &sampleRate)) {
            // Check whether the sample rate changes and perform processing as required.
        }
        if (OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, &channelCount)) {
            // Check whether the number of audio channels changes and perform processing as required.
        }
        if (OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, &sampleFormat)) {
            // Check whether the audio sample format changes and perform processing as required.
        }
    }
    // Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnInputBufferAvailable(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*data, void \*userData)
    {
        (void)codec;
        ADecBufferSignal \*signal = static\_cast<ADecBufferSignal \*>(userData);
        unique\_lock<mutex> lock(signal->inMutex\_);
        signal->inQueue\_.push(index);
        signal->inBufferQueue\_.push(data);
        signal->inCond\_.notify\_all();
        // The input stream is sent to inBufferQueue\_.
    }
    // Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnOutputBufferAvailable(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*data, void \*userData)
    {
        (void)codec;
        ADecBufferSignal \*signal = static\_cast<ADecBufferSignal \*>(userData);
        unique\_lock<mutex> lock(signal->outMutex\_);
        signal->outQueue\_.push(index);
        signal->outBufferQueue\_.push(data);
        signal->outCond\_.notify\_all();
        // The index of the output buffer is sent to outQueue\_.
        // The decoded data is sent to outBufferQueue\_.
    }
    
    Configure the callback information.
    
    signal\_ = new ADecBufferSignal();
    OH\_AVCodecCallback cb\_ = {&OnError, &OnOutputFormatChanged, &OnInputBufferAvailable, &OnOutputBufferAvailable};
    // Set the asynchronous callbacks.
    int32\_t ret = OH\_AudioCodec\_RegisterCallback(audioDec\_, cb\_, signal\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  (Optional) Call **OH\_AudioCodec\_SetDecryptionConfig** to set the decryption configuration.
    
    Call this API after the media key system information is obtained but before **Prepare()** is called. For details about how to obtain such information, see step 4 in [Media Data Demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md).
    
    For details about DRM APIs, see [DRM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drm).
    
    Add the header files.
    
    #include <multimedia/drm\_framework/native\_mediakeysystem.h>
    #include <multimedia/drm\_framework/native\_mediakeysession.h>
    #include <multimedia/drm\_framework/native\_drm\_err.h>
    #include <multimedia/drm\_framework/native\_drm\_common.h>
    
    Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(sample PUBLIC libnative\_drm.so)
    
    The sample code is as follows:
    
    // Create a media key system based on the media key system information. The following uses com.wiseplay.drm as an example.
    MediaKeySystem \*system = nullptr;
    int32\_t ret = OH\_MediaKeySystem\_Create("com.wiseplay.drm", &system);
    if (system == nullptr) {
        printf("create media key system failed");
        return;
    }
    
    // Create a media key session.
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
    // Set the decryption configuration, that is, set the decryption session and secure channel flag to the decoder. (Currently, the secure channel is not supported for audio decryption and therefore the secure channel flag should be set to false.)
    bool secureAudio = false;
    ret = OH\_AudioCodec\_SetDecryptionConfig(audioDec\_, session, secureAudio);
    
5.  Call **OH\_AudioCodec\_Configure()** to configure the decoder.
    
    Key values of configuration options are described as follows:
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/PDaOyJIMSFqAzPu76c2qBw/en-us_image_0000002568684877.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=003D0C3FF13A1EC3DC421B2D02ACC582831D45671C9E38958A2445211E23F8AC)

The sample below lists the value range of each audio decoding type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/K_r-bZPYQuaXKDTuK65EGQ/en-us_image_0000002568764887.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BCFB61246D3765BEDE112A580E20A6F2C05E2297EFE4D6A63761F4A51A597F8)

Starting from API version 20, you can query the [sample rate range](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcapability-h#oh_avcapability_getaudiosupportedsamplerateranges). The following audio decoding types support decoding of any sample rate within their range:

| Audio Decoding Type | Sample Rate (Hz) |
| :-- | :-- |
| FLAC | 8000 – 384000 |
| Vorbis | 8000 – 192000 |
| APE | 1 – 2147483647 |

// (Mandatory) Configure the audio sample rate.
constexpr uint32\_t DEFAULT\_SAMPLERATE = 44100;
// (Optional) Configure the audio bit rate.
constexpr uint32\_t DEFAULT\_BITRATE = 32000;
// (Mandatory) Configure the audio channel count.
constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 2;
// (Optional) Configure the maximum input length.
constexpr uint32\_t DEFAULT\_MAX\_INPUT\_SIZE = 1152;
// Configure whether to use ADTS decoding (optional for AAC decoding).
constexpr uint32\_t DEFAULT\_AAC\_TYPE = 1;
// (Optional) Configure the byte count of each audio data block. This parameter is supported since API version 22 and must be configured only for WMAV1, WMAV2, and WMA PRO decoding.
constexpr int32\_t DEFAULT\_BLOCK\_ALIGN = 1;
OH\_AVFormat \*format = OH\_AVFormat\_Create();
// Set the format.
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_BITRATE, DEFAULT\_BITRATE);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_MAX\_INPUT\_SIZE, DEFAULT\_MAX\_INPUT\_SIZE);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AAC\_IS\_ADTS, DEFAULT\_AAC\_TYPE);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_BLOCK\_ALIGN, DEFAULT\_BLOCK\_ALIGN);
// Configure the decoder.
int32\_t ret = OH\_AudioCodec\_Configure(audioDec\_, format);
if (ret != AV\_ERR\_OK) {
    // Handle exceptions.
}

1.  Call **OH\_AudioCodec\_Prepare()** to prepare internal resources for the decoder.
    
    int32\_t ret = OH\_AudioCodec\_Prepare(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
2.  Call **OH\_AudioCodec\_Start()** to start the decoder.
    
    Add the header file.
    
    #include <fstream>
    
    The sample code is as follows:
    
    ifstream inputFile\_;
    ofstream outFile\_;
    
    // Set the input file path based on the actual situation.
    const char\* inputFilePath = "/";
    // Set the output file path based on the actual situation.
    const char\* outputFilePath = "/";
    // Open the path of the binary file to be decoded.
    inputFile\_.open(inputFilePath, ios::in | ios::binary);
    // Set the path of the output file.
    outFile\_.open(outputFilePath, ios::out | ios::binary);
    // Start decoding.
    int32\_t ret = OH\_AudioCodec\_Start(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
3.  (Optional) Call **OH\_AVCencInfo\_SetAVBuffer()** to set the Common Encryption Scheme (CENC) information.
    
    If the content being played is DRM encrypted and [demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md) is performed by the upper-layer application, call **OH\_AVCencInfo\_SetAVBuffer()** to set the CENC information to the AVBuffer so that the media data can be decrypted in the AVBuffer.
    
    Add the header file.
    
    #include <multimedia/player\_framework/native\_cencinfo.h>
    
    Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(sample PUBLIC libnative\_media\_avcencinfo.so)
    
    The sample code is as follows:
    
    auto buffer = signal\_->inBufferQueue\_.front();
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
    
4.  Call **OH\_AudioCodec\_PushInputBuffer()** to write the data to decode.
    
    You should fill in complete input data before calling this API.
    
    When finished, set the flags to **AVCODEC\_BUFFER\_FLAGS\_EOS**.
    
    uint32\_t index = signal\_->inQueue\_.front();
    auto buffer = signal\_->inBufferQueue\_.front();
    int32\_t size;
    int64\_t pts;
    // size is the length of each frame of the data to decode. pts is the timestamp of each frame and is used to indicate when the audio should be played.
    // The values of size and pts are obtained from an audio and video resource file or data stream to decode.
    // In the case of an audio and video resource file, the values are obtained from the buffer in the demultiplexed OH\_AVDemuxer\_ReadSampleBuffer.
    // In the case of a data stream, the values are obtained from the data stream provider.
    // In this example, the values of size and pts are obtained from the test file.
    inputFile\_.read(reinterpret\_cast<char \*>(&size), sizeof(size));
    inputFile\_.read(reinterpret\_cast<char \*>(&pts), sizeof(pts));
    inputFile\_.read((char \*)OH\_AVBuffer\_GetAddr(buffer), size);
    OH\_AVCodecBufferAttr attr = {0};
    if (inputFile\_.eof()) {
        attr.size = 0;
        attr.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
    } else {
        attr.size = size;
        attr.flags = AVCODEC\_BUFFER\_FLAGS\_NONE;
    }
    attr.pts = pts;
    OH\_AVBuffer\_SetBufferAttr(buffer, &attr);
    int32\_t ret = OH\_AudioCodec\_PushInputBuffer(audioDec\_, index);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
5.  Call **OH\_AudioCodec\_FreeOutputBuffer()** to release the decoded data.
    
    Once you have retrieved the decoded PCM stream, call **OH\_AudioCodec\_FreeOutputBuffer()** to free up the data.
    
    uint32\_t index = signal\_->outQueue\_.front();
    OH\_AVBuffer \*data = signal\_->outBufferQueue\_.front();
    if (data == nullptr) {
        // Handle exceptions.
    }
    // Obtain the buffer attributes.
    OH\_AVCodecBufferAttr attr = {0};
    int32\_t ret = OH\_AVBuffer\_GetBufferAttr(data, &attr);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Write the decoded data (specified by data) to the output file.
    outFile\_.write(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(data)), attr.size);
    ret = OH\_AudioCodec\_FreeOutputBuffer(audioDec\_, index);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    if (attr.flags == AVCODEC\_BUFFER\_FLAGS\_EOS) {
        // End.
    }
    
    Since API version 11, the API for obtaining Audio Vivid metadata is added.
    
    uint32\_t index = signal\_->outQueue\_.front();
    OH\_AVBuffer \*data = signal\_->outBufferQueue\_.front();
    // Obtain buffer attributes.
    OH\_AVCodecBufferAttr attr = {0};
    int32\_t ret = OH\_AVBuffer\_GetBufferAttr(data, &attr);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Write the decoded data to the output file.
    outFile\_.write(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(data)), attr.size);
    // API version 11 and later provide the API for obtaining Audio Vivid metadata.
    OH\_AVFormat \*format = OH\_AVBuffer\_GetParameter(data);
    uint8\_t \*metadata = nullptr;
    size\_t metaSize;
    OH\_AVFormat\_GetBuffer(format, OH\_MD\_KEY\_AUDIO\_VIVID\_METADATA, &metadata, &metaSize);
    ret = OH\_AudioCodec\_FreeOutputBuffer(audioDec\_, index);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    if (attr.flags == AVCODEC\_BUFFER\_FLAGS\_EOS) {
        // End.
    }
    
6.  (Optional) Call **OH\_AudioCodec\_Flush()** to refresh the decoder.
    
    After **OH\_AudioCodec\_Flush()** is called, the decoder remains in the running state, but the current queue is cleared and the buffer storing the decoded data is freed.
    
    To continue decoding, you must call **OH\_AudioCodec\_Start()** again.
    
    You need to call **OH\_AudioCodec\_Start()** in the following cases:
    
    -   To use the same decoder configuration after **AVCODEC\_BUFFER\_FLAGS\_EOS** of the output buffer is set, call **OH\_AudioCodec\_Flush()** to refresh the decoder.
    -   If a recoverable error occurs during the execution (**OH\_AudioCodec\_IsValid()** returns **true**), you can call **OH\_AudioCodec\_Flush()** to refresh the decoder and then call **OH\_AudioCodec\_Start()** to start decoding again.
    
    // Refresh the decoder.
    int32\_t ret = OH\_AudioCodec\_Flush(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Start decoding again.
    ret = OH\_AudioCodec\_Start(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
7.  (Optional) Call **OH\_AudioCodec\_Reset()** to reset the decoder.
    
    After **OH\_AudioCodec\_Reset()** is called, the decoder returns to the initialized state. The input and output buffers obtained before the reset cannot be used. You must call **OH\_AudioCodec\_Configure()** to reconfigure the decoder and then call **OH\_AudioCodec\_Start()** to start decoding again. Obtain the input and output buffers again after the decoder is started.
    
    // Reset the decoder.
    int32\_t ret = OH\_AudioCodec\_Reset(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Reconfigure the decoder.
    ret = OH\_AudioCodec\_Configure(audioDec\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
8.  Call **OH\_AudioCodec\_Stop()** to stop the decoder.
    
    After the decoder is stopped, you can call **OH\_AudioCodec\_Start()** to start it again. The input and output buffers obtained before the decoder is stopped cannot be reused. You must obtain them again after the decoder is started.
    
    // Stop the decoder.
    int32\_t ret = OH\_AudioCodec\_Stop(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
9.  Call **OH\_AudioCodec\_Destroy()** to destroy the decoder instance and release resources.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/etYeWSLGTQqzNgip2pmVuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55465875F79D6958F4C7071647553EF5438FF41A4866AA7D69034B982F0FBFAA)
    
    You only need to call this API once.
    
    // Call OH\_AudioCodec\_Destroy to destroy the decoder.
    int32\_t ret = OH\_AudioCodec\_Destroy(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    } else {
        audioDec\_ = NULL; // The decoder cannot be destroyed repeatedly.
    }
