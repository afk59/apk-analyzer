# Using OpenSL ES for Audio Playback (C/C++)

OpenSL ES, short for Open Sound Library for Embedded Systems, is an embedded, cross-platform audio processing library that is free of charge. It provides high-performance and low-latency APIs for you to develop applications running on embedded mobile multimedia devices. HarmonyOS has implemented certain native APIs based on [OpenSL ES](https://www.khronos.org/opensles/) 1.0.1 API specifications developed by the [Khronos Group](https://www.khronos.org/). You can use these APIs through <OpenSLES.h> and <OpenSLES\_OpenHarmony.h>.

#### Using OHAudio to Replace OpenSL ES

HarmonyOS provides the OpenSL ES APIs for audio development at the native layer since SDK8. As the version evolves, these APIs fail to meet the capability expansion requirements of the audio system and therefore are no longer recommended.

In SDK 10, HarmonyOS provides the OHAudio APIs, which open up all audio functions of the system. The OHAudio APIs cover all the capabilities provided by OpenSL ES in HarmonyOS. They also support new features such as audio focus events and low latency.

For details about the OHAudio development guide, please refer to [(Recommended) Using OHAudio for Audio Playback (C/C++)](../../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md).

For application developers who integrated with HarmonyOS at an early stage, we provide a reference comparison for [Switching from OpenSL ES to OHAudio (C/C++)](../switching-from-opensl-es-to-ohaudio-c-c/document.md), to help you switch to using the new APIs in the latest version more quickly.

#### OpenSL ES on HarmonyOS

Currently, HarmonyOS implements parts of [OpenSL ES APIs](https://gitcode.com/openharmony/third_party_opensles/blob/master/api/1.0.1/OpenSLES.h) to implement basic audio playback functionalities.

If an API that has not been implemented on HarmonyOS is called, **SL\_RESULT\_FEATURE\_UNSUPPORTED** is returned.

The following lists the OpenSL ES APIs that have been implemented on HarmonyOS. For details, see the [OpenSL ES](https://www.khronos.org/opensles/) specifications.

-   **SLInterfaceID implemented on HarmonyOS**
    
    | SLInterfaceID | Description |
    | :-- | :-- |
    | SL\_IID\_ENGINE | Universal engine, which provides the interface for creating player objects. |
    | SL\_IID\_PLAY | Provides the player status interface. |
    | SL\_IID\_VOLUME | Provides interfaces for adjusting and reading the volume of audio playback streams. |
    | SL\_IID\_OH\_BUFFERQUEUE | Provides the callback registration interface for audio playback stream data. |
    
-   **Engine APIs implemented on HarmonyOS**
    
    -   SLresult (\*CreateAudioPlayer) (SLEngineItf self, SLObjectItf \* pPlayer, SLDataSource \*pAudioSrc, SLDataSink \*pAudioSnk, SLuint32 numInterfaces, const SLInterfaceID \* pInterfaceIds, const SLboolean \* pInterfaceRequired)
    -   SLresult (\*CreateAudioRecorder) (SLEngineItf self, SLObjectItf \* pRecorder, SLDataSource \*pAudioSrc, SLDataSink \*pAudioSnk, SLuint32 numInterfaces, const SLInterfaceID \* pInterfaceIds, const SLboolean \* pInterfaceRequired)
    -   SLresult (\*CreateOutputMix) (SLEngineItf self, SLObjectItf \* pMix, SLuint32 numInterfaces, const SLInterfaceID \* pInterfaceIds, const SLboolean \* pInterfaceRequired)
-   **Object APIs implemented on HarmonyOS**
    
    -   SLresult (\*Realize) (SLObjectItf self, SLboolean async)
    -   SLresult (\*GetState) (SLObjectItf self, SLuint32 \* pState)
    -   SLresult (\*GetInterface) (SLObjectItf self, const SLInterfaceID iid, void \* pInterface)
    -   void (\*Destroy) (SLObjectItf self)
-   **Playback APIs implemented on HarmonyOS**
    
    -   SLresult (\*SetPlayState) (SLPlayItf self, SLuint32 state)
    -   SLresult (\*GetPlayState) (SLPlayItf self, SLuint32 \*pState)
-   **Volume control APIs implemented on HarmonyOS**
    
    -   SLresult (\*SetVolumeLevel) (SLVolumeItf self, SLmillibel level)
    -   SLresult (\*GetVolumeLevel) (SLVolumeItf self, SLmillibel \*pLevel)
    -   SLresult (\*GetMaxVolumeLevel) (SLVolumeItf self, SLmillibel \*pMaxLevel)
-   **BufferQueue APIs implemented on HarmonyOS**
    
    The APIs listed below can be used only after <OpenSLES\_OpenHarmony.h> is introduced.
    
    | API | Description |
    | :-- | :-- |
    | SLresult (\*Enqueue) (SLOHBufferQueueItf self, const void \*buffer, SLuint32 size) | 
    Adds a buffer to the corresponding queue.
    
    For an audio playback operation, this API adds the buffer with audio data to the **filledBufferQ\_** queue. For an audio recording operation, this API adds the idle buffer after recording data storage to the **freeBufferQ\_** queue.
    
    The **self** parameter indicates the BufferQueue object that calls this API.
    
    The **buffer** parameter indicates the pointer to the buffer with audio data or the pointer to the idle buffer after the recording data is stored.
    
    The **size** parameter indicates the size of the buffer.
    
     |
    | SLresult (\*Clear) (SLOHBufferQueueItf self) | 
    
    Releases a BufferQueue object.
    
    The **self** parameter indicates the BufferQueue object that calls this API.
    
     |
    | SLresult (\*GetState) (SLOHBufferQueueItf self, SLOHBufferQueueState \*state) | 
    
    Obtains the state of a BufferQueue object.
    
    The **self** parameter indicates the BufferQueue object that calls this API.
    
    The **state** parameter indicates the pointer to the state of the BufferQueue object.
    
     |
    | SLresult (\*RegisterCallback) (SLOHBufferQueueItf self, SlOHBufferQueueCallback callback, void\* pContext) | 
    
    Registers a callback.
    
    The **self** parameter indicates the BufferQueue object that calls this API.
    
    The **callback** parameter indicates the callback to be registered for the audio playback or recording operation.
    
    The **pContext** parameter indicates the pointer to the audio file to be played for an audio playback operation or the pointer to the audio file to be recorded for an audio recording operation.
    
     |
    | SLresult (\*GetBuffer) (SLOHBufferQueueItf self, SLuint8\*\* buffer, SLuint32\* size) | 
    
    Obtains a buffer.
    
    For an audio playback operation, this API obtains an idle buffer from the **freeBufferQ\_** queue. For an audio recording operation, this API obtains the buffer that carries recording data from the **filledBufferQ\_** queue.
    
    The **self** parameter indicates the BufferQueue object that calls this API.
    
    The **buffer** parameter indicates the double pointer to the idle buffer or the buffer carrying recording data.
    
    The **size** parameter indicates the size of the buffer.
    
     |
    

#### Complete Sample Code

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libOpenSLES.so)

Refer to the sample code below to play an audio file.

1.  Add the header files.
    
    #include "SLES/OpenSLES.h"
    #include "SLES/OpenSLES\_OpenHarmony.h"
    #include "SLES/OpenSLES\_Platform.h"
    
2.  Use the **slCreateEngine** API to obtain an engine instance.
    
    SLObjectItf engineObject = nullptr;
    slCreateEngine(&engineObject, 0, nullptr, 0, nullptr, nullptr);
    (\*engineObject)->Realize(engineObject, SL\_BOOLEAN\_FALSE);
    
3.  Obtain the engineEngine instance of the **SL\_IID\_ENGINE** API.
    
    SLEngineItf engineEngine = nullptr;
    (\*engineObject)->GetInterface(engineObject, SL\_IID\_ENGINE, &engineEngine);
    
4.  Configure the player and create an AudioPlayer instance.
    
    SLDataLocator\_BufferQueue slBufferQueue = {
        SL\_DATALOCATOR\_BUFFERQUEUE,
        1
    };
    
    // Configure the parameters based on the audio file format.
    SLDataFormat\_PCM pcmFormat = {
        SL\_DATAFORMAT\_PCM,
        2,                           // Number of channels.
        SL\_SAMPLINGRATE\_48,          // Sampling rate.
        SL\_PCMSAMPLEFORMAT\_FIXED\_16, // Audio sample format.
        16,
        SL\_SPEAKER\_FRONT\_LEFT | SL\_SPEAKER\_FRONT\_RIGHT,
        SL\_BYTEORDER\_LITTLEENDIAN
    };
    SLDataSource slSource = {
       &slBufferQueue,
       &pcmFormat
    };
    SLObjectItf pcmPlayerObject = nullptr;
    (\*engineEngine)->CreateAudioPlayer(engineEngine,
                                       &pcmPlayerObject,
                                       &slSource,
                                       &slSink,
                                       0,
                                       nullptr,
                                       nullptr);
    (\*pcmPlayerObject)->Realize(pcmPlayerObject, SL\_BOOLEAN\_FALSE);
    
5.  Obtain the bufferQueueItf instance of the **SL\_IID\_OH\_BUFFERQUEUE** API.
    
    SLOHBufferQueueItf bufferQueueItf;
    (\*pcmPlayerObject)->GetInterface(pcmPlayerObject, SL\_IID\_OH\_BUFFERQUEUE, &bufferQueueItf);
    
6.  Open an audio file and register the **BufferQueueCallback** function.
    
    static void BufferQueueCallback (SLOHBufferQueueItf bufferQueueItf, void \*pContext, SLuint32 size)
    {
        SLuint8 \*buffer = nullptr;
        SLuint32 pSize;
        (\*bufferQueueItf)->GetBuffer(bufferQueueItf, &buffer, &pSize);
        // Write the audio data to be played to the buffer.
        (\*bufferQueueItf)->Enqueue(bufferQueueItf, buffer, size);
    }
    void \*pContext; // This callback can be used to obtain the custom context information passed in.
    (\*bufferQueueItf)->RegisterCallback(bufferQueueItf, BufferQueueCallback, pContext);
    
7.  Obtain the playItf instance of the **SL\_PLAYSTATE\_PLAYING** API and start playing.
    
    SLPlayItf playItf = nullptr;
    (\*pcmPlayerObject)->GetInterface(pcmPlayerObject, SL\_IID\_PLAY, &playItf);
    (\*playItf)->SetPlayState(playItf, SL\_PLAYSTATE\_PLAYING);
    
8.  Stop playing.
    
    (\*playItf)->SetPlayState(playItf, SL\_PLAYSTATE\_STOPPED);
    (\*pcmPlayerObject)->Destroy(pcmPlayerObject);
    (\*engineObject)->Destroy(engineObject);
