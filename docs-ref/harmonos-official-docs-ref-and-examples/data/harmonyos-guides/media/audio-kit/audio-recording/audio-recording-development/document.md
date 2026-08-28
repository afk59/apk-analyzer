# Audio Recording Development

#### Selecting an Audio Recording Development Mode

The system provides a variety of APIs for you to develop audio recording applications. You can select them based on the recording output formats, audio usage scenarios, and even the programming language you use. Selecting a suitable class helps you reduce development workload and your application deliver a better effect.

-   [AudioCapturer](../using-audiocapturer-for-audio-recording-arkts/document.md): provides ArkTS and JS API to implement audio input. It supports only the PCM format and requires applications to continuously read audio data. The application can perform data processing after audio output. This class can be used to develop more professional and diverse recording applications. To use this class, you must have basic audio processing knowledge.
    
-   [Using OHAudio for Audio Recording](../recommended-using-ohaudio-for-audio-recording-c-c/document.md): provides a set of native APIs for audio input. These APIs are normalized in design and support both common and low-latency audio channels. They support the PCM format only. They are suitable for playback applications that implement audio input at the native layer.
    

In addition to the preceding classes, you can also use **AVRecorder** in Media Kit to implement audio recording.

-   [AVRecorder](../../../media-kit/media-development-arkts/recording/using-avrecorder-to-record-audio-arkts/document.md): provides ArkTS and JS APIs to implement audio recording. It also supports audio input, audio encoding, and media encapsulation. You can directly call device hardware, such as microphone, for recording and generate M4A audio files.

#### Precautions for Developing Audio Recording Applications

-   The application must request the **ohos.permission.MICROPHONE** permission from the user before invoking the microphone to record audio. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
    
    For details about how to use and manage microphones, see [Managing Microphone Mute Status](../managing-microphone-mute-state/document.md).
    
-   If continuous recording or background recording is required, the application must request a continuous task to prevent it from being suspended. For details, see [Continuous Task (ArkTS)](../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).
    
-   The application must start recording when it runs in the foreground. It can switch to the background after the recording is started. Recording cannot be started in the background.
    
-   To record audio, the application must use an appropriate recording stream type. For details, see [Selecting the Appropriate Audio Stream Types](../../selecting-the-appropriate-audio-stream-types/document.md).
    
-   If the application is required to record the screen, refer to [Using AVScreenCaptureRecorder to Record Screens and Write Them to Files (ArkTS)](../../../media-kit/media-development-arkts/recording/using-avscreencapturerecorder-to-record-screens-and-write-them-to-files-arkts/document.md) and [Using AVScreenCapture to Capture Screens and Write Them to Files (C/C++)](../../../media-kit/media-development-c-c/recording/using-avscreencapture-to-capture-screens-and-write-them-to-files-c-c/document.md).
