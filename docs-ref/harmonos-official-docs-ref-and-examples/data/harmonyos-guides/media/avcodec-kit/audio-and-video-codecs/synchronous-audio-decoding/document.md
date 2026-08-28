# Synchronous Audio Decoding

Starting from API version 20, audio decoding in synchronous mode is supported.

You can call native APIs to perform audio decoding in synchronous mode, which decodes media data into PCM streams.

For details about the supported decoding capabilities, see [AVCodec Supported Formats](../../avcodec-supported-formats/document.md#audio-decoding).

**When to Use**

Asynchronous mode is generally recommended for most use cases. For details, see [Audio Decoding](../audio-decoding/document.md). Synchronous mode can be used if you need to actively request buffers for frame delivery.

Decoding an audio/video file into a PCM stream typically involves the following steps: [media data demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md) -> audio decoding.

This guide outlines the audio decoding process: inputting audio frames and decoding them into PCM streams.

#### Development Guidelines

Read [AudioCodec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-audiocodec-h) for the API reference.

Refer to the code snippet below to complete the entire audio decoding process, including creating a decoder, setting decoding parameters (such as the sample rate, bit rate, and audio channel count), and starting, refreshing, resetting, and destroying the decoder.

During application development, you must call the APIs in the defined sequence. Otherwise, an exception or undefined behavior may occur.

The figure below shows the call relationship of audio decoding in synchronous mode.

-   The dotted line indicates an optional operation.
    
-   The solid line indicates a mandatory operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/31yq_9h5R16w2STP_H8uPg/en-us_image_0000002537925100.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=130F9BDAA62F6301D7A4077029512EAAA8140E6CA8D1ACD0C7DEA6C68912C7D8)

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_acodec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ZKwtikE9SWujF29I7mnxXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80B399391A313EA4CF7472CEC897502A6C976D266DAF234D8F04BFD505E8F1BC)

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
    
2.  Create a decoder instance. In the code snippet below, \*\*OH\_AVCodec \*\*\* is the pointer to the decoder instance created.
    
    You can create a decoder by MIME type or codec name.
    
    Method 1: Create a decoder by MIME type.
    
    // Create a decoder by MIME type. The following example creates an AAC decoder. The second parameter is set to false to indicate decoding.
    OH\_AVCodec \*audioDec\_ = OH\_AudioCodec\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, false);
    
    Method 2: Create a decoder by codec name.
    
    // Create a decoder by name.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, false);
    const char \*name = OH\_AVCapability\_GetName(capability);
    OH\_AVCodec \*audioDec\_ = OH\_AudioCodec\_CreateByName(name);
    
3.  (Optional) Call **OH\_AudioCodec\_SetDecryptionConfig** to set the decryption configuration.
    
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
    // Set the decryption configuration, that is, assign the decryption session to the decoder. Currently, audio decryption does not support secure decoders. Therefore, set the secureAudio parameter to false.
    bool secureAudio = false;
    ret = OH\_AudioCodec\_SetDecryptionConfig(audioDec\_, session, secureAudio);
    
4.  Call **OH\_AudioCodec\_Configure()** to configure the decoder.
    
    Key values of configuration options are described as follows:
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/bM6cJm_0Td63dkNOoByeUw/en-us_image_0000002568684877.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1751E80598A3047EB4BF9AE2FFF7F5C1999B0A667661068DCA6FCDB750A4CC41)

The sample below lists the value range of each audio decoding type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/t1HskGJuRTiN9ckq99wngw/en-us_image_0000002568764887.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8795AE432A5E55DACFD6D62E4B1C2C18D6F1E9D6EFF5CED16D8C9E343430A4E1)

Starting from API version 20, you can query the [sample rate range](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcapability-h#oh_avcapability_getaudiosupportedsamplerateranges). The following audio decoding types support decoding of any sample rate within their range:

| Audio Decoding Type | Sample Rate (Hz) |
| :-- | :-- |
| FLAC | 8000 – 384000 |
| Vorbis | 8000 – 192000 |
| APE | 1 – 2147483647 |

// (Mandatory) Configure the audio sample rate.
constexpr uint32\_t DEFAULT\_SAMPLERATE = 44100;
// (Mandatory) Configure the audio channel count.
constexpr uint32\_t DEFAULT\_CHANNEL\_COUNT = 2;
// Configure whether to use ADTS decoding (optional for AAC decoding).
constexpr uint32\_t DEFAULT\_AAC\_TYPE = 1;
OH\_AVFormat \*format = OH\_AVFormat\_Create();
// Set the format.
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, DEFAULT\_SAMPLERATE);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, DEFAULT\_CHANNEL\_COUNT);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AAC\_IS\_ADTS, DEFAULT\_AAC\_TYPE);
OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ENABLE\_SYNC\_MODE, 1); // Set synchronous mode.
// Configure the decoder.
OH\_AVErrCode ret = OH\_AudioCodec\_Configure(audioDec\_, format);
if (ret != AV\_ERR\_OK) {
    // Handle exceptions.
}

1.  Call **OH\_AudioCodec\_Prepare()** to prepare internal resources for the decoder.
    
    OH\_AVErrCode ret = OH\_AudioCodec\_Prepare(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
2.  Call **OH\_AudioCodec\_Start()** to start the decoder.
    
    Add the header file.
    
    #include <fstream>
    
    The sample code is as follows:
    
    ifstream inputFile\_;
    ofstream outFile\_;
    
    // Set the input file path based on the actual situation. To demonstrate audio decoding, the input file here contains audio frames and related information (not a directly playable audio file).
    const char\* inputFilePath = "/";
    // Set the output file path based on the actual situation. This guide only demonstrates audio decoding; decoded PCM data is saved to a file without further processing.
    const char\* outputFilePath = "/";
    // Open the path of the binary file to be decoded.
    inputFile\_.open(inputFilePath, ios::in | ios::binary);
    // Set the path of the output file.
    outFile\_.open(outputFilePath, ios::out | ios::binary);
    // Start decoding.
    OH\_AVErrCode ret = OH\_AudioCodec\_Start(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
3.  (Optional) Call **OH\_AVCencInfo\_SetAVBuffer()** to set the Common Encryption Scheme (CENC) information.
    
    If the content being played is DRM encrypted and [demultiplexing](../../media-data-multiplexing-and-demultiplexing/media-data-demultiplexing/document.md) is performed by the upper-layer application, call **OH\_AVCencInfo\_SetAVBuffer()** to set the CENC information to the AVBuffer for media data decryption.
    
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
    
4.  Invoke synchronous mode to write the data to decode and obtain the decoded output.
    
    Read data:
    
    // size is the length of each frame of the data to decode. pts is the timestamp of each frame and is used to indicate when the audio should be played.
    // The values of size and pts are obtained from an audio and video resource file or data stream to decode.
    // In the case of an audio and video resource file, the values are obtained from the buffer in the demultiplexed OH\_AVDemuxer\_ReadSampleBuffer.
    // In the case of a data stream, the values are obtained from the data stream provider.
    // In this example, the values of size and pts are obtained from the test file.
    bool DecoderFillInputBuffer(OH\_AVBuffer \*buffer, ifstream &inputFile)
    {
        OH\_AVCodecBufferAttr attr;
        memset(&attr, 0, sizeof(attr));
        attr.flags = AVCODEC\_BUFFER\_FLAGS\_EOS;
        bool finished = true;
        do {
            int64\_t size;
            inputFile.read(reinterpret\_cast<char \*>(&size), sizeof(size));
            if (inputFile.eof() || inputFile.gcount() != sizeof(size)) {
                break;
            }
            inputFile.read(reinterpret\_cast<char \*>(&attr.pts), sizeof(attr.pts));
            if (inputFile.gcount() != sizeof(attr.pts)) {
                break;
            }
            attr.size = static\_cast<int32\_t>(size);
            if (attr.size > 0) {
                inputFile.read((char \*)OH\_AVBuffer\_GetAddr(buffer), attr.size);
                attr.flags = AVCODEC\_BUFFER\_FLAGS\_NONE;
                finished = false;
            }
        } while (0);
        OH\_AVBuffer\_SetBufferAttr(buffer, &attr);
        return finished;
    }
    bool InputOneFrame(OH\_AVCodec \*codec, ifstream &inputFile)
    {
        uint32\_t index = 0;
        bool finished = true;
        OH\_AVErrCode ret = OH\_AudioCodec\_QueryInputBuffer(codec, &index, 20000); // 20000us
        if (ret == AV\_ERR\_TRY\_AGAIN\_LATER) {
            // Timeout: exception handling. The timeout period is too short, or input/output buffers are not consumed/released (causing decoding blocking).
            return finished;
        }
        if (ret != AV\_ERR\_OK) {
            // Handle exceptions.
            return finished;
        }
        OH\_AVBuffer \*inputBuf = OH\_AudioCodec\_GetInputBuffer(codec, index);
        if (inputBuf == nullptr) {
            // Handle exceptions.
            return finished;
        }
        finished = DecoderFillInputBuffer(inputBuf, inputFile);
        OH\_AudioCodec\_PushInputBuffer(codec, index);
        return finished;
    }
    
    You should fill in complete input data before calling this API.
    
    When finished, set the flags to **AVCODEC\_BUFFER\_FLAGS\_EOS**.
    
    bool inputFinished = false;
    for (;;) {
        if (!inputFinished) {
            inputFinished = InputOneFrame(audioDec\_, inputFile\_);
        }
        uint32\_t index;
        OH\_AVErrCode ret = OH\_AudioCodec\_QueryOutputBuffer(audioDec\_, &index, 20000); // 20000us
        if (ret == AV\_ERR\_TRY\_AGAIN\_LATER) {
            // Timeout: exception handling. The timeout period is too short, or input/output buffers are not consumed/released (causing decoding blocking).
            continue;
        } else if (ret == AV\_ERR\_STREAM\_CHANGED) {
            // Callback processing after the decoding output parameters are changed. The application performs processing as required.
            OH\_AVFormat \*outFormat = OH\_AudioCodec\_GetOutputDescription(audioDec\_);
            int32\_t sampleRate;
            int32\_t channelCount;
            int32\_t sampleFormat;
            if (OH\_AVFormat\_GetIntValue(outFormat, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, &sampleRate)) {
                // Check whether the sample rate changes and perform processing as required.
            }
            if (OH\_AVFormat\_GetIntValue(outFormat, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, &channelCount)) {
                // Check whether the audio channel count changes and perform processing as required.
            }
            if (OH\_AVFormat\_GetIntValue(outFormat, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, &sampleFormat)) {
                // Check whether the audio sample format changes and perform processing as required.
            }
            continue;
        }
        if (ret != AV\_ERR\_OK) {
            // Handle exceptions.
            break;
        }
        OH\_AVBuffer \*outputBuf = OH\_AudioCodec\_GetOutputBuffer(audioDec\_, index);
        if (outputBuf == nullptr) {
            // Handle exceptions.
            break;
        }
        OH\_AVCodecBufferAttr attr;
        if (OH\_AVBuffer\_GetBufferAttr(outputBuf, &attr) != AV\_ERR\_OK) {
            // Handle exceptions.
            break;
        }
        if (attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
            OH\_AudioCodec\_FreeOutputBuffer(audioDec\_, index);
            // Decoding output completed.
            break;
        }
        outFile\_.write(reinterpret\_cast<char \*>(OH\_AVBuffer\_GetAddr(outputBuf)), attr.size);
        OH\_AudioCodec\_FreeOutputBuffer(audioDec\_, index);
    }
    
5.  (Optional) Call **OH\_AudioCodec\_Flush()** to refresh the decoder.
    
    After **OH\_AudioCodec\_Flush()** is called, the decoder remains in the running state, but the current queue is cleared and the buffer storing the decoded data is freed. The input and output buffers obtained before flushing cannot be reused.
    
    To continue decoding, you must call **OH\_AudioCodec\_Start()** again.
    
    You need to call **OH\_AudioCodec\_Start()** in the following cases:
    
    -   Previously input data is no longer needed, for example, after seeking during demultiplexing.
    -   To use the same decoder configuration after **AVCODEC\_BUFFER\_FLAGS\_EOS** of the output buffer is set, call **OH\_AudioCodec\_Flush()** to refresh the decoder.
    -   If a recoverable error occurs during the execution (**OH\_AudioCodec\_IsValid()** returns **true**), you can call **OH\_AudioCodec\_Flush()** to refresh the decoder and then call **OH\_AudioCodec\_Start()** to start decoding again.
    
    // Refresh the decoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Flush(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Start decoding again.
    ret = OH\_AudioCodec\_Start(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
6.  (Optional) Call **OH\_AudioCodec\_Reset()** to reset the decoder.
    
    After **OH\_AudioCodec\_Reset()** is called, the decoder returns to the initialized state. The input and output buffers obtained before the reset cannot be used. You must call **OH\_AudioCodec\_Configure()** to reconfigure the decoder and then call **OH\_AudioCodec\_Start()** to start decoding again. Obtain the input and output buffers again after the decoder is started.
    
    // Reset the decoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Reset(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // Reconfigure the decoder.
    ret = OH\_AudioCodec\_Configure(audioDec\_, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
7.  Call **OH\_AudioCodec\_Stop()** to stop the decoder.
    
    After the decoder is stopped, you can call **OH\_AudioCodec\_Start()** to start it again. The input and output buffers obtained before the decoder is stopped cannot be reused. You must obtain them again after the decoder is started.
    
    // Stop the decoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Stop(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
8.  Call **OH\_AudioCodec\_Destroy()** to destroy the decoder instance and release resources.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/CA71i8wMQlylAxn_3dM7ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8338B2206A0EBE5C14FA7A8DCFAF0347075B5B88150AFFD2CBE1D795745EC96E)
    
    You only need to call this API once.
    
    // Call OH\_AudioCodec\_Destroy to destroy the decoder.
    OH\_AVErrCode ret = OH\_AudioCodec\_Destroy(audioDec\_);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    } else {
        audioDec\_ = NULL; // The decoder cannot be destroyed repeatedly.
    }
