# Audio Vivid Demultiplexing

After obtaining an MP4 file encapsulated by Audio Vivid, call the demuxer APIs to select an audio track, read each frame of data, and [send the frames to the decoder](../audio-vivid-decoding/document.md). For details about the APIs, see [AVDemuxer API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/avcodec-module).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC 
libnative\_media\_codecbase.so libnative\_media\_core.so 
libnative\_media\_acodec.so libnative\_media\_avdemuxer.so libnative\_media\_avsource.so
)

#### Adding Header Files

// Demuxer header file
#include "multimedia/player\_framework/native\_avdemuxer.h"
#include <string.h>

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

#### How to Develop

1.  Create a demuxer instance.
    
    // Obtain the FD and size from the TS code.
    let inputFile = fs.openSync(filepath,fs.OpenMode.READ\_ONLY);
    if (inputFile) {
        let inputFileState = fs.statSync(inputFile.fd);
        let inputFileSize = inputFileState.size;
    }
    
    //C++ code
    OH\_AVSource \*source = OH\_AVSource\_CreateWithFD(inputFd,0,inputFileSize);
    OH\_AVDemuxer \*demuxer = OH\_AVDemuxer\_CreateWithSource(source);
    auto sourceFormat = std::shared\_ptr<OH\_AVFormat>(OH\_AVSource\_GetSourceFormat(source\_), OH\_AVFormat\_Destroy);
    int32\_t trackCount = 0;
    OH\_AVFormat\_GetIntValue(sourceFormat.get(), OH\_MD\_KEY\_TRACK\_COUNT, &trackCount);
    
2.  Select an audio track.
    
    int32\_t trackCount = 0;
    OH\_AVFormat\_GetIntValue(sourceFormat.get(), OH\_MD\_KEY\_TRACK\_COUNT, &trackCount);
    for (int32\_t index = 0; index < trackCount; index++) {
    int trackType = -1;
    auto trackFormat =
        std::shared\_ptr<OH\_AVFormat>(OH\_AVSource\_GetTrackFormat(source\_, index), OH\_AVFormat\_Destroy);
    // Obtain the track type.
    OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_TRACK\_TYPE, &trackType);
    // Determine whether the current track is an audio track.
    if (trackType == MEDIA\_TYPE\_AUD) { 
        // Select an audio track.
        OH\_AVDemuxer\_SelectTrackByID(demuxer, index);
        // Obtain the bit depth.
        OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT, &info.audioSampleFormat);
        // Obtain the number of audio channels.
        OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, &info.audioChannelCount);
        // Obtain the audio channel layout.
        OH\_AVFormat\_GetLongValue(trackFormat.get(), OH\_MD\_KEY\_CHANNEL\_LAYOUT, &info.audioChannelLayout);
        // Obtain the sampling rate.
        OH\_AVFormat\_GetIntValue(trackFormat.get(), OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, &info.audioSampleRate);
        // Obtain additional configuration information.
        uint8\_t \*addr = nullptr;
        OH\_AVFormat\_GetBuffer(trackFormat.get(), OH\_MD\_KEY\_CODEC\_CONFIG, &addr, &info.audioCodecSize);
        memcpy((void \*)info.audioCodecConfig, (void \*)addr, info.audioCodecSize);
        // Obtain the decoder type.
        char \*audioCodecMime;
        OH\_AVFormat\_GetStringValue(trackFormat.get(), OH\_MD\_KEY\_CODEC\_MIME, const\_cast<char const \*\*>(&audioCodecMime));
        info.audioCodecMime = audioCodecMime;
        int32\_t trackId = index;
        break;
        }
    }
    
3.  Read each frame of data.
    
    OH\_AVBuffer \*buffer;
    int32\_t ret = OH\_AVDemuxer\_ReadSampleBuffer(demuxer, trackId, buffer);
    
4.  Release the demuxer instance.
    
    int32\_t Release()
    {
        if (demuxer != nullptr) {
            OH\_AVDemuxer\_Destroy(demuxer);
            demuxer = nullptr;
        }
        if (source != nullptr) {
            OH\_AVSource\_Destroy(source);
            source = nullptr;
        }
        return AVCODEC\_SAMPLE\_ERR\_OK;
    }
