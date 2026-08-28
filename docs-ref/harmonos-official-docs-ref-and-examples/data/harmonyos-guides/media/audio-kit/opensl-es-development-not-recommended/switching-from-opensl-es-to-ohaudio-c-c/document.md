# Switching from OpenSL ES to OHAudio (C/C++)

You are advised to use OHAudio APIs instead of OpenSL ES APIs to develop audio services, since the latter may fail to provide extended audio capabilities. This topic describes how to switch the audio service code from the OpenSL ES APIs to the OHAudio APIs.

#### Differences in Features Supported

Different from the OpenSL ES APIs, the OHAudio APIs support low-latency playback/recording and service change listening.

The table below lists the differences in the features supported by the APIs.

| Feature | OpenSL ES | OHAudio |
| :-- | :-- | :-- |
| Audio streaming playback | Supported | Supported |
| Audio streaming recording | Supported | Supported |
| Low-latency audio playback | Not supported | Supported |
| Low-latency audio recording | Not supported | Supported |
| Switching the state of a playback object | Supported | Supported |
| Switching the state of a recording object | Supported | Supported |
| Obtaining the state of an audio stream object | Supported | Supported |
| Clearing the playback cache | Not supported | Supported |
| Listening for audio interruption events | Not supported | Supported |
| Listening for audio stream events | Not supported | Supported |
| Listening for stream exception events | Not supported | Supported |
| Listening for output device update events | Not supported | Supported |

#### Differences in Development Modes

This section describes the differences between OHAudio and OpenSL ES APIs in development modes based on the development procedure of audio playback. The implementation of audio recording is similar.

## Constructing Instances

OpenSL ES:

Obtain an Engine object through the global interface, and construct an audio playback object based on the Engine object and the input and output parameters.

// Generate an Engine Interface object.
SLEngineItf engine;
// ...

// Configure audio input slSource as required.
SLDataSource slSource;
// ...

// Configure audio output slSink as required.
SLDataSink slSink;
// ...

// Generate an audio playback object.
SLObjectItf playerObject;
(\*engine)->CreateAudioPlayer(engine,
                             &playerObject,
                             &slSource,
                             &slSink,
                             0,
                             nullptr,
                             nullptr);

(\*playerObject)->Realize(playerObject,
                         SL\_BOOLEAN\_FALSE);

OHAudio:

Use the builder mode to generate an audio playback object based on custom parameters.

// Create a builder.
OH\_AudioStreamBuilder \*builder;
OH\_AudioStreamBuilder\_Create(&builder, AUDIOSTREAM\_TYPE\_RENDERER);

// Set custom parameters. Otherwise, the default parameters will be used.
OH\_AudioStreamBuilder\_SetSamplingRate(builder, 48000);
OH\_AudioStreamBuilder\_SetChannelCount(builder, 2);
OH\_AudioStreamBuilder\_SetSampleFormat(builder, AUDIOSTREAM\_SAMPLE\_S16LE);
OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW);
// This parameter specifies the audio usage and is supported only by OHAudio. The system implements audio strategy adaptation based on the parameter.
OH\_AudioStreamBuilder\_SetRendererInfo(builder, AUDIOSTREAM\_USAGE\_MUSIC);
// ...

// Generate an audio playback object.
OH\_AudioRenderer \*audioRenderer;
OH\_AudioStreamBuilder\_GenerateRenderer(builder, &audioRenderer);

## State Switching

OpenSL ES:

Obtain the state switching interface based on the audio playback object and use the interface to switch the state. There are three states: **SL\_PLAYSTATE\_STOPPED**, **SL\_PLAYSTATE\_PAUSED**, and **SL\_PLAYSTATE\_PLAYING**.

// Obtain the playback operation interface based on the audio playback object.
SLPlayItf playItf = nullptr;
(\*playerObject)->GetInterface(playerObject, SL\_IID\_PLAY, &playItf);
// Switch the state.
(\*playItf)->SetPlayState(playItf, SL\_PLAYSTATE\_PLAYING);
(\*playItf)->SetPlayState(playItf, SL\_PLAYSTATE\_PAUSED);
(\*playItf)->SetPlayState(playItf, SL\_PLAYSTATE\_STOPPED);

OHAudio:

There are independent state switching interfaces. The state is switched based on the state machine. There are six states, which are mainly switched between **AUDIOSTREAM\_STATE\_PREPARED**, **AUDIOSTREAM\_STATE\_RUNNING**, **AUDIOSTREAM\_STATE\_STOPPED**, **AUDIOSTREAM\_STATE\_PAUSED**, and **AUDIOSTREAM\_STATE\_RELEASED**.

// Switch the state.
OH\_AudioRenderer\_Start(audioRenderer);
OH\_AudioRenderer\_Pause(audioRenderer);
OH\_AudioRenderer\_Stop(audioRenderer);

## Data Processing

OpenSL ES:

Based on the extended **OHBufferQueue** APIs, you can register a custom callback function to write audio data to be played to the system buffer.

static void MyBufferQueueCallback(SLOHBufferQueueItf bufferQueueItf, void \*pContext, SLuint32 size)
{
    SLuint8 \*buffer = nullptr;
    SLuint32 bufferSize;
    // Obtain the buffer provided by the system.
    (\*bufferQueueItf)->GetBuffer(bufferQueueItf, &buffer, &bufferSize);
    // Write the audio data to be played to the buffer.
    // ...
    // Enqueue the buffer.
    (\*bufferQueueItf)->Enqueue(bufferQueueItf, buffer, bufferSize);
}

// Obtain the OHBufferQueue APIs.
SLOHBufferQueueItf bufferQueueItf;
(\*playerObject)->GetInterface(playerObject, SL\_IID\_OH\_BUFFERQUEUE, &bufferQueueItf);
// This callback can be used to obtain the custom context information passed in.
void \*pContext;
(\*bufferQueueItf)->RegisterCallback(bufferQueueItf, MyBufferQueueCallback, pContext);

OHAudio:

The callback mode is used. When the audio playback object is constructed, a data input callback is registered to implement custom data filling. During playback, a data request callback is automatically triggered at a proper time based on the system scheduling and delay configuration.

static int32\_t MyOnWriteData(
    OH\_AudioRenderer \*renderer,
    void \*userData,
    void \*buffer,
    int32\_t bufferLen)
{
    // Write the data to be played to the buffer based on the requested buffer length.
    // After the function is returned, the system automatically fetches data from the buffer.
}

OH\_AudioRenderer\_Callbacks callbacks;
callbacks.OH\_AudioRenderer\_OnWriteData = MyOnWriteData;

// Set the callback function for outputting audio streams. The callback function is automatically registered when the audio playback object is generated.
void \*userData = nullptr;
OH\_AudioStreamBuilder\_SetRendererCallback(builder, callbacks, userData);

## Releasing Resources

OpenSL ES:

Call **SLObjectItf** to release object resources.

// Release the playback object resources.
(\*playerObject)->Destroy(playerObject);

OHAudio:

Call the release interface of the module to release object resources.

// Release the builder resources.
OH\_AudioStreamBuilder\_Destroy(builder);

// Release the playback object resources.
OH\_AudioRenderer\_Release(audioRenderer);
