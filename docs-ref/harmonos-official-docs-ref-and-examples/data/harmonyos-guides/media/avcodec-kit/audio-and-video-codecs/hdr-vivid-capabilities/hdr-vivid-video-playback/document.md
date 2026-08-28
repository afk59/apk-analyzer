# HDR Vivid Video Playback

You can call the native APIs of this module to support HDR Vivid video playback.

The main process of video playback is as follows: demultiplexing, decoding, displaying, and playing video files.

#### Parsing an HDR Vivid Video

Check whether a video is an HDR Vivid video by parsing the video file. If the video source is an HDR Vivid video, related information, such as metadata and color information, can be parsed.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_avdemuxer.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_avsource.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/xZbzLkuWRaqJgGR2USzqJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D2447F6BBFF7179793EE0F81FFA83B92B4460712CDFC1B9133FA75F4ABA29FE)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avdemuxer.h>
    #include <multimedia/player\_framework/native\_avsource.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fcntl.h>
    #include <sys/stat.h>
    #include <string>
    
2.  Configure the file parser.
    
    // Create the FD. You must have the read permission on the file instance to open the file. (filePath indicates the path of the file to be demultiplexed. The file must exist.)
    std::string filePath = "test.mp4";
    int fd = open(filePath.c\_str(), O\_RDONLY);
    struct stat fileStatus {};
    // Obtain the file size.
    size\_t fileSize = 0;
    if (stat(filePath.c\_str(), &fileStatus) == 0) {
       fileSize = static\_cast<size\_t>(fileStatus.st\_size);
    } else {
        printf("get stat failed");
        return;
    }
    // Create a source instance for the resource file specified by the FD.
    OH\_AVSource \*source = OH\_AVSource\_CreateWithFD(fd, 0, fileSize);
    if (source == nullptr) {
       printf("create source failed");
       return;
    }
    
3.  Obtain the video track information and query the HDR type of a file.
    
    int32\_t trackCount = 0;
    uint32\_t audioTrackIndex = 0;
    uint32\_t videoTrackIndex = 0;
    int32\_t trackType;
    
    // Obtain the number of tracks from the file source information.
    OH\_AVFormat \*sourceFormat = OH\_AVSource\_GetSourceFormat(source);
    if (sourceFormat == nullptr) {
       printf("get source format failed");
       return;
    }
    bool getTrackRet = OH\_AVFormat\_GetIntValue(sourceFormat, OH\_MD\_KEY\_TRACK\_COUNT, &trackCount);
    if (!getTrackRet) {
        // Handle exceptions.
    }
    OH\_AVFormat\_Destroy(sourceFormat);
    for (uint32\_t index = 0; index < (static\_cast<int32\_t>(trackCount)); index++) {
       // Obtain the track format.
       OH\_AVFormat \*format = OH\_AVSource\_GetTrackFormat(source, index);
       if (format == nullptr) {
          printf("get track format failed");
          return;
       }
       // Determine the track type.
       static\_cast<OH\_MediaType>(trackType) == OH\_MediaType::MEDIA\_TYPE\_AUD ? audioTrackIndex = index : videoTrackIndex = index;
       // Check whether the video file is an HDR Vivid video.
       int32\_t isHDRVivid = 0;
       bool getHdrRet = OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID, &isHDRVivid);
       if (getHdrRet == false || isHDRVivid == 0) {
          printf("is not HDRVivid ");
          return;
       }
       OH\_AVFormat\_Destroy(format); // Destroy the format.
    }
    

#### Decoding an HDR Vivid Video

The application creates an H.265 decoder and configures the width, height, and format information. The decoder parses the streams and generates the corresponding video frame data and metadata.

Currently, the surface output and buffer output are supported.

The two differ slightly in the API calling modes:

-   In surface mode, the application must call **OH\_VideoDecoder\_SetSurface** to set an OHNativeWindow before the decoder is ready.
-   In buffer mode, the application can call **OH\_AVBuffer\_GetNativeBuffer** to convert the buffer to a native buffer, and then call **OH\_NativeBuffer\_GetMetadataValue** to obtain the metadata.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_vdec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/fBh85QV8Twamr8RryKjbyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A26C9C5FCF2662673523236F2A8B94BCB87793321AC79A7651F926663322C0B)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## Defining the Basic Structure

The sample code provided in this section adheres to the C++17 standard and is for reference only. You can define your own buffer objects by referring to it.

1.  Add the header files.
    
    #include <condition\_variable>
    #include <memory>
    #include <mutex>
    #include <queue>
    #include <shared\_mutex>
    #include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fstream>
    
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
    
4.  Define global variables.
    
    These global variables are for reference only. They can be encapsulated into an object based on service requirements.
    
    // Pointer to the decoder instance.
    OH\_AVCodec \*videoDec = nullptr;
    // Decoder synchronization lock.
    std::shared\_mutex codecMutex;
    // Decoder input queue.
    CodecBufferQueue inQueue;
    // Decoder output queue.
    CodecBufferQueue outQueue;
    

## How to Develop

**Surface Mode**

1.  Create an H.265 decoder instance.
    
    You can create a decoder by name or MIME type. In the code snippet below, the following variables are used:
    
    -   **videoDec**: pointer to the video decoder instance.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC**: HEVC video codec.
    
    // Create an H.265 decoder by MIME type.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    
2.  Configure the asynchronous callback function.
    
    // Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The data buffer of the input frame and its index are sent to inQueue.
        (void)codec;
        (void)userData;
        inQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    For details, see "Step 3: Call OH\_VideoDecoder\_RegisterCallback() to set the callback functions" in [Video Decoding in Surface Mode](../../video-decoding/document.md#surface-mode).
    
3.  Configure the decoder.
    
    For details, see "Step 5: Call OH\_VideoDecoder\_Configure() to configure the decoder" in [Video Decoding in Surface Mode](../../video-decoding/document.md#surface-mode).
    
4.  Set the surface.
    
    For details, see "Step 6: Set the surface" in [Video Decoding in Surface Mode](../../video-decoding/document.md#surface-mode).
    
5.  Call **OH\_VideoDecoder\_Start()** to start the decoder.
    
    For details, see "Step 8: Call OH\_VideoDecoder\_Start() to start the decoder" in [Video Decoding in Surface Mode](../../video-decoding/document.md#surface-mode).
    

**Buffer Mode**

1.  Create an H.265 decoder instance.
    
    You can create a decoder by name or MIME type. In the code snippet below, the following variables are used:
    
    -   **videoDec**: pointer to the video decoder instance.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC**: HEVC video codec.
    
    // Create an H.265 decoder by MIME type.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    
2.  Configure the asynchronous callback function.
    
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
        (void)userData;
        outQueue.Enqueue(std::make\_shared<CodecBufferInfo>(index, buffer));
    }
    
    For details, see "Step 3: Call OH\_VideoDecoder\_RegisterCallback() to set the callback functions" in [Video Decoding in Buffer Mode](../../video-decoding/document.md#buffer-mode).
    
3.  Configure the decoder.
    
    For details, see "Step 5: Call OH\_VideoDecoder\_Configure() to configure the decoder" in [Video Decoding in Buffer Mode](../../video-decoding/document.md#buffer-mode).
    
4.  Call **OH\_VideoDecoder\_Start()** to start the decoder.
    
    For details, see "Step 7: Call OH\_VideoDecoder\_Start() to start the decoder" in [Video Decoding in Buffer Mode](../../video-decoding/document.md#buffer-mode).
    
5.  Obtain the metadata.
    
    Linking the Dynamic Libraries in the CMake Script
    
    target\_link\_libraries(sample PUBLIC libnative\_buffer.so)
    
    Add the header files.
    
    #include <string.h>
    #include <native\_buffer/native\_buffer.h>
    
    The sample code is as follows:
    
    // Size of the metadata.
    int32\_t size = 0;
    // Pointer to the metadata instance.
    uint8\_t \*metadata = nullptr;
    // Container of the metadata.
    std::vector<uint8\_t> meta;
    
    // Obtain the callback function OnNewOutputBuffer and save it to the frame buffer of the output queue.
    std::shared\_ptr<CodecBufferInfo> bufferInfo = outQueue.Dequeue();
    std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    if (bufferInfo == nullptr || !bufferInfo->isValid) {
        // Handle exceptions.
    }
    // Obtain the OH\_NativeBuffer pointer instance.
    OH\_NativeBuffer \*nativeBuffer = OH\_AVBuffer\_GetNativeBuffer(bufferInfo.buffer);
    if (nativeBuffer != nullptr){
        // Obtain the static metadata.
        if (OH\_NativeBuffer\_GetMetadataValue(nativeBuffer, OH\_HDR\_STATIC\_METADATA, &size, &metadata) != 0){
            // Handle exceptions.
        } else {
            meta.resize(size);
            memcpy(&meta\[0\], metadata, size);
            delete\[\] metadata;
            metadata = nullptr;
        }
        // Obtain the dynamic metadata.
        if (OH\_NativeBuffer\_GetMetadataValue(nativeBuffer, OH\_HDR\_DYNAMIC\_METADATA, &size, &metadata) != 0){
            // Handle exceptions.
        } else {
            meta.resize(size);
            memcpy(&meta\[0\], metadata, size);
            delete\[\] metadata;
            metadata = nullptr;
        }
    }
    // Destroy the native buffer.
    if (nativeBuffer != nullptr) {
        OH\_NativeBuffer\_Unreference(nativeBuffer);
        nativeBuffer = nullptr;
    }
    

#### Processing Video Frame Data

1.  Demultiplex packets and obtain frame data cyclically.
    
    bool videoIsEnd = false;
    // Create a demuxer for the resource instance.
    OH\_AVDemuxer \*demuxer = OH\_AVDemuxer\_CreateWithSource(source);
    // Obtain the callback function OnNeedInputBuffer and save it to the frame buffer of the input queue.
    std::shared\_ptr<CodecBufferInfo> bufferInfo = inQueue.Dequeue();
    std::shared\_lock<std::shared\_mutex> lock(codecMutex);
    if (bufferInfo == nullptr || !bufferInfo->isValid) {
        // Handle exceptions.
    }
    // Demultiplex frame data.
    int32\_t ret = OH\_AVDemuxer\_ReadSampleBuffer(demuxer, videoTrackIndex, bufferInfo->buffer);
    if (ret == AV\_ERR\_OK) {
       // Obtain and process the video frame data in the buffer.
        OH\_AVCodecBufferAttr info;
        OH\_AVErrCode getBufferRet = OH\_AVBuffer\_GetBufferAttr(bufferInfo->buffer, &info);
        if (getBufferRet != AV\_ERR\_OK) {
            // Handle exceptions.
        }
        if (info.flags == OH\_AVCodecBufferFlags::AVCODEC\_BUFFER\_FLAGS\_EOS) {
            videoIsEnd = true;
        }
    }
    
2.  Send the demultiplexed video frame data to the input buffer for decoding.
    
    // Send the data to the input buffer for decoding. index is the index of the buffer.
    ret = OH\_VideoDecoder\_PushInputBuffer(videoDec, bufferInfo->index);
    if (ret != AV\_ERR\_OK) {
       // Handle exceptions.
    }
    
    For details about the subsequent steps, see [Video Decoding](../../video-decoding/document.md).
