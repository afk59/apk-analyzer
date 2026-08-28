# Audio Vivid Decoding

After obtaining the demultiplexed data, send the data to the decoder, and use the decoder to obtain the PCM data and metadata. For details about the APIs, see [AudioDecoder API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/avcodec-module).

The following table lists the specifications supported in Audio Vivid decoding.

<table><tbody><tr><th class="firstcol" id="mcps1.3.3.1.3.1.1" valign="top" width="50%"><p>Sampling Rate</p></th><td class="cellrowborder" valign="top" width="50%"><p>32000, 44100, 48000, 96000, 192000</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.1.3.2.1" valign="top" width="50%"><p>Bit Rate Range</p></th><td class="cellrowborder" valign="top" width="50%"><p>16000–3075000</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.1.3.3.1" valign="top" width="50%"><p>Audio Channel Count</p></th><td class="cellrowborder" valign="top" width="50%"><p>1–16</p></td></tr><tr><th class="firstcol" id="mcps1.3.3.1.3.4.1" valign="top" width="50%"><p>Bit Depth</p></th><td class="cellrowborder" valign="top" width="50%"><p>S16, S24</p></td></tr></tbody></table>

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC 
libnative\_media\_codecbase.so libnative\_media\_core.so 
libnative\_media\_acodec.so libnative\_media\_avdemuxer.so libnative\_media\_avsource.so
)

#### Adding Header Files

// Demuxer header file
#include "multimedia/player\_framework/native\_avdemuxer.h"
#include <string>

// Struct about the demuxer and decoder
struct AudioSampleInfo {
std::string audioCodecMime = "";
int32\_t audioSampleFormat = 0;
int32\_t audioSampleRate = 0; 
int32\_t audioChannelCount = 0;
int64\_t audioChannelLayout = 0;
uint8\_t audioCodecConfig\[100\] = {0};
size\_t audioCodecSize = 0;
};

AudioSampleInfo  info;

#### Defining Related Instances

**Define CodecBufferInfo.**

Define the properties of the decoded stream, which is used to multiplex the stream data transferred to the player.

struct CodecBufferInfo {
    uint32\_t bufferIndex = 0;
    uintptr\_t \*buffer = nullptr;
    uint8\_t \*bufferAddr = nullptr;
    OH\_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC\_BUFFER\_FLAGS\_NONE};

    CodecBufferInfo(uint8\_t \*addr) : bufferAddr(addr){};
    CodecBufferInfo(uint8\_t \*addr, int32\_t bufferSize)
        : bufferAddr(addr), attr({0, bufferSize, 0, AVCODEC\_BUFFER\_FLAGS\_NONE}){};
    CodecBufferInfo(uint32\_t argBufferIndex, OH\_AVMemory \*argBuffer, OH\_AVCodecBufferAttr argAttr)
        : bufferIndex(argBufferIndex), buffer(reinterpret\_cast<uintptr\_t \*>(argBuffer)), attr(argAttr){};
    CodecBufferInfo(uint32\_t argBufferIndex, OH\_AVMemory \*argBuffer)
        : bufferIndex(argBufferIndex), buffer(reinterpret\_cast<uintptr\_t \*>(argBuffer)){};
    CodecBufferInfo(uint32\_t argBufferIndex, OH\_AVBuffer \*argBuffer)
        : bufferIndex(argBufferIndex), buffer(reinterpret\_cast<uintptr\_t \*>(argBuffer)) {
        OH\_AVBuffer\_GetBufferAttr(argBuffer, &attr);
    };
};

**Define the decoding work queue.**

class CodecUserData {
public:
    SampleInfo \*sampleInfo = nullptr;

    // Number of input frames.
    uint32\_t inputFrameCount\_ = 0;
    // Input queue lock, which prevents multiple threads from simultaneously operating the input queue.
    std::mutex inputMutex\_;
    // Condition variable of the input thread. When the input queue is empty, the input thread is blocked.
    std::condition\_variable inputCond\_;
    // Input buffer queue, which stores the buffers provided by the codec for users to write input data.
    std::queue<CodecBufferInfo> inputBufferInfoQueue\_;

    // Number of output frames.
    uint32\_t outputFrameCount\_ = 0;
    // Output queue lock, which prevents multiple threads from simultaneously operating the output queue.
    std::mutex outputMutex\_;
    // Condition variable of the output thread. When the output queue is empty, the output thread is blocked.
    std::condition\_variable outputCond\_;
    std::mutex renderMutex\_;
    std::condition\_variable renderCond\_;
    // Output buffer queue, which stores the buffers provided by the codec for users to store output data.
    std::queue<CodecBufferInfo> outputBufferInfoQueue\_;

    std::shared\_ptr<AudioDecoder> audioCodec\_;
    std::queue<unsigned char> renderQueue\_;

    void ClearQueue() {
        {
            std::unique\_lock<std::mutex> lock(inputMutex\_);
            auto emptyQueue = std::queue<CodecBufferInfo>();
            inputBufferInfoQueue\_.swap(emptyQueue);
        }
        {
            std::unique\_lock<std::mutex> lock(outputMutex\_);
            auto emptyQueue = std::queue<CodecBufferInfo>();
            outputBufferInfoQueue\_.swap(emptyQueue);
        }
    }
};

**Define the callback functions.**

class SampleCallback {
public:
    // Error callback function, which is called when an internal error occurs in the codec and returns the corresponding error code to the user.
    static void OnCodecError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData);
    // Parameter modification callback function, which is called when the codec parameters are modified and returns the new format parameter to the user.
    static void OnCodecFormatChange(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData);
    // Input callback function, which is called when the codec requires input and returns the buffer for writing the input data and the corresponding index to the user.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData);
    // Output callback function, which is called when the codec generates new output data and returns the buffer for storing the output data and the corresponding index to the user.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData);
};
void SampleCallback::OnCodecError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData) {
    (void)codec;
    (void)errorCode;
    (void)userData;
}
void SampleCallback::OnCodecFormatChange(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData) {
}
void SampleCallback::OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData) {
    if (userData == nullptr) {
        return;
    }
    (void)codec;
    CodecUserData \*codecUserData = static\_cast<CodecUserData \*>(userData);
    std::unique\_lock<std::mutex> lock(codecUserData->inputMutex\_);
    // Place the input buffer in the input queue.
    codecUserData->inputBufferInfoQueue\_.emplace(index, buffer);
    // Notify the input thread to start running.
    codecUserData->inputCond\_.notify\_all();
}

void SampleCallback::OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData) {
    if (userData == nullptr) {
        return;
    }
    (void)codec;
    CodecUserData \*codecUserData = static\_cast<CodecUserData \*>(userData);
    std::unique\_lock<std::mutex> lock(codecUserData->outputMutex\_);
    // Place the output buffer in the output queue.
    codecUserData->outputBufferInfoQueue\_.emplace(index, buffer);
    // Notify the output thread to start running.
    codecUserData->outputCond\_.notify\_all();
}

#### How to Develop

1.  Create a decoder instance.
    
    // Create a decoder.
    OH\_AVCodec \* decoder = OH\_AudioCodec\_CreateByMime(info.audioCodecMime,false);
    
    // Set parameters.
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, SAMPLE\_S16LE); // S24LE is also acceptable.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, sampleInfo.audioChannelCount);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, sampleInfo.audioSampleRate);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AAC\_IS\_ADTS, 1);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, 96422); // Bit rate, which is for reference only. It can also be obtained during demultiplexing.
    OH\_AVFormat\_SetBuffer(format, OH\_MD\_KEY\_CODEC\_CONFIG, sampleInfo.audioCodecConfig, sampleInfo.audioCodecSize);
    bool res = OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_CHANNEL\_LAYOUT, sampleInfo.audioChannelLayout);
    ret = OH\_AudioCodec\_Configure(decoder, format);
    OH\_AVFormat\_Destroy(format);
    format = nullptr;
    
    // Set the callback functions, which are called by the system after the input and output buffers are prepared.
    int32\_t ret = OH\_AudioCodec\_RegisterCallback(decoder,
        {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
         SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},codecUserData);
    // After the callback and parameter setting are complete, notify the system that the decoder is ready and the next step can continue.
    ret = OH\_AudioCodec\_Prepare(decoder)
    
2.  Write audio to the decoder.
    
    int32\_t PushInputData(CodecBufferInfo &info)
    {
        int32\_t  ret = OH\_AVBuffer\_SetBufferAttr(reinterpret\_cast<OH\_AVBuffer \*>(info.buffer), &info.attr);
        ret = OH\_AudioCodec\_PushInputBuffer(decoder, info.bufferIndex);
        return 0;
    }
    
3.  Release the used output stream.
    
    int32\_t AudioDecoder::FreeOutputData(uint32\_t bufferIndex)
    {
        int32\_t ret = 0;
        ret = OH\_AudioCodec\_FreeOutputBuffer(decoder, bufferIndex);
        return ret ;
    }
    
4.  Implement the audio write thread.
    
    CodecUserData\*audioDecContext\_ = new CodecUserData;
    void AudioDecInputThread()
    {
        while (true) {
            if(!isStarted\_){
               return;  
            }
            std::unique\_lock<std::mutex> lock(audioDecContext\_->inputMutex\_);
            // Block the input thread until the program execution ends, or the input queue is not empty.
            bool condRet = audioDecContext\_->inputCond\_.wait\_for(
                lock, 5s, \[this\]() { return !isStarted\_ || !audioDecContext\_->inputBufferInfoQueue\_.empty(); });
            if(!isStarted\_ || audioDecContext\_->inputBufferInfoQueue\_.empty()){
               return;  
            }
            // Obtain the input buffer.
            CodecBufferInfo bufferInfo = audioDecContext\_->inputBufferInfoQueue\_.front();
            audioDecContext\_->inputBufferInfoQueue\_.pop();
            audioDecContext\_->inputFrameCount\_++;
            lock.unlock();
            // Read a frame of data from the demuxer and write it to the input buffer.
            demuxer\_->ReadSample(demuxer\_->GetAudioTrackId(), reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer), bufferInfo.attr);
            int32\_t ret = audioDecoder\_->PushInputData(bufferInfo);
            if(ret != 0){
                return;
            }
            if(bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS){
                return;
            }
        }
        // StartRelease();
    }
    
5.  Implement the audio decoding output thread.
    
    void AudioDecOutputThread()
    {
        while (true) {
            if(!isStarted\_){
               return;  
            }
            std::unique\_lock<std::mutex> lock(audioDecContext\_->outputMutex\_);
            // Block the output thread until the program execution ends, or the output queue is not empty.
            bool condRet = audioDecContext\_->outputCond\_.wait\_for(
                lock, 5s, \[this\]() { return !isStarted\_ || !audioDecContext\_->outputBufferInfoQueue\_.empty(); });
            if(!isStarted\_ || audioDecContext\_->outputBufferInfoQueue\_.empty()){
               return;  
            }
            // Obtain the output buffer.
            CodecBufferInfo bufferInfo = audioDecContext\_->outputBufferInfoQueue\_.front();
            audioDecContext\_->outputBufferInfoQueue\_.pop();
            if(bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS){
               return;  
            }
            audioDecContext\_->outputFrameCount\_++;
            // Obtain the decoded PCM data.
            uint8\_t \*source = OH\_AVBuffer\_GetAddr(reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer));
            OH\_AVFormat \* format = OH\_AVBuffer\_GetParameter(reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer));
            uint8\_t \* metadata;
            size\_t size;
            // **Obtain metadata.**
            OH\_AVFormat\_GetBuffer(format, OH\_MD\_KEY\_AUDIO\_VIVID\_METADATA, &metadata, &size); 
    #ifdef DEBUG\_DECODE
            if (audioOutputFile\_.is\_open()) {
                audioOutputFile\_.write((const char\*)OH\_AVBuffer\_GetAddr(reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer)), bufferInfo.attr.size);
            }
    #endif
            lock.unlock();
            int32\_t ret = audioDecoder\_->FreeOutputData(bufferInfo.bufferIndex);
            if(ret != 0){
                return;
            }
        }
    }
    
6.  Start the decoder.
    
    int ret = OH\_AudioCodec\_Start(decoder);
    
7.  Stop the decoder, and release the decoder instance.
    
    OH\_AudioCodec\_Stop(decoder);
    OH\_AudioCodec\_Destroy(decoder);
    decoder = nullptr;
