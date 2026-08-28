# Using AVTranscoder to Transcode Videos (C/C++)

Starting from API version 20, NDK (C/C++) APIs are provided for video transcoding.

You can use the [AVTranscoder](../../../about-this-kit/document.md#avtranscoder) to implement video transcoding. . Since API version 12, transcoding is provided as a basic capability on mobile phones, tablets, and 2-in-1 devices You can call [canIUse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/init#caniuse) to check whether the device supports AVTranscoder and continue the operations described in this topic only when the return value of **canIUse("SystemCapability.Multimedia.Media.AVTranscoder")** is **true**.

This topic describes how to use the AVTranscoder to implement video transcoding, covering the process of starting, pausing, resuming, and exiting transcoding.

**Figure 1** AVTranscoder state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/lRNqgKYDRMKGEHGLP_ZCDQ/en-us_image_0000002537925134.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB39006683075EF71DE204D0FDBD2B3B5BC073FFC64FBD4025CC6AEC28C4F9C6)

For details about the states, see [OH\_AVTranscoder\_State](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avtranscoder-base-h#oh_avtranscoder_state).

#### How to Develop

Link the dynamic libraries in the CMake script.

target\_link\_libraries(entry PUBLIC libavtranscoder.so libace\_napi.z.so)

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(sample PUBLIC libhilog\_ndk.z.so)

Import the **avtranscoder.h** and **avtranscoder\_base.h** header files to use the transcoding APIs.

Read [AVTranscoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avtranscoder) for the API reference.

1.  Call **OH\_AVTranscoder\_Create()** to create a transcoding instance.
    
    OH\_AVTranscoder \*transcoder = OH\_AVTranscoder\_Create();
    
2.  Set callback functions. Specifically, call **OH\_AVTranscoder\_SetStateCallback()**, **OH\_AVTranscoder\_SetErrorCallback()**, and **OH\_AVTranscoder\_SetProgressUpdateCallback()** to set callbacks for transcoding status changes, transcoding error events, and transcoding progress update events, respectively. The table below describes these callbacks.
    
    | Event Type | Description |
    | :-- | :-- |
    | OH\_AVTranscoder\_OnStateChange | Optional event, which is invoked when the transcoding status changes. |
    | OH\_AVTranscoder\_OnError | Optional event, which is invoked when a transcoding error occurs. |
    | OH\_AVTranscoder\_OnProgressUpdate | Optional event, which is invoked when the transcoding progress changes. |
    
    You can also customize data using **userData** in these callbacks.
    
    typedef struct NdkAVTransCoderUser {
       using StateChangeFunc = std::function<void()>;
       NdkAVTransCoderUser();
       NdkAVTransCoderUser(const NdkAVTransCoderUser &other) = delete;
       NdkAVTransCoderUser &operator=(const NdkAVTransCoderUser &other) = delete;
       ~NdkAVTransCoderUser();
    
       void OnStateChangeCb(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_State state);
       void OnErrorCb(OH\_AVTranscoder \*transcoder, int32\_t errorCode, const char  \*errorMsg);
       void OnProgressUpdateCb(OH\_AVTranscoder \*transcoder, int progress);
       std::map<uint32\_t, StateChangeFunc> stateChangeFuncs\_;
    
       OH\_AVTranscoder \*transcoder = nullptr;
       int32\_t errorCode = AV\_ERR\_OK;
       OH\_AVTranscoder\_State transCoderState = AVTRANSCODER\_PREPARED;
       int avTranscoderProgress = 0;
       int inStartStateCount = 0;
    } NdkAVTransCoderUser;
    
    void NdkAVTransCoderUser::OnProgressUpdateCb(OH\_AVTranscoder \*transcoder, int  progress)
    {
       LOG("NdkAVTransCoderUser OnProgressUpdateCb progress: %{public}d", progress);
       this->avTranscoderProgress = progress;
    }
    
    void NdkAVTransCoderUser::OnErrorCb(OH\_AVTranscoder \*transcoder, int32\_t  errorCode, const char \*errorMsg)
    {
       LOG("NdkAVTransCoderUser OnErrorCb errorCode: %{public}d ,errorMsg: %{public} s", errorCode,
          errorMsg == nullptr ? "unknown" : errorMsg);
       this->errorCode = errorCode;
    }
    
    void NdkAVTransCoderUser::OnStateChangeCb(OH\_AVTranscoder \*transcoder,  OH\_AVTranscoder\_State state)
    {
       this->transCoderState = state;
       if (transcoder == nullptr) {
          return;
       }
       int32\_t ret = -1;
       switch (state) {
          case AVTRANSCODER\_PREPARED: {
                this->transCoderState = AVTRANSCODER\_PREPARED;
                if (this->stateChangeFuncs\_.count(AVTRANSCODER\_PREPARED) > 0) {
                   this->stateChangeFuncs\_\[AVTRANSCODER\_PREPARED\]();
                }
                break;
          }
          case AVTRANSCODER\_STARTED: {
                this->transCoderState = AVTRANSCODER\_STARTED;
                if (this->stateChangeFuncs\_.count(AVTRANSCODER\_STARTED) > 0) {
                   this->stateChangeFuncs\_\[AVTRANSCODER\_STARTED\]();
                }
                break;
          }
          case AVTRANSCODER\_PAUSED: {
                this->transCoderState = AVTRANSCODER\_PAUSED;
                if (this->stateChangeFuncs\_.count(AVTRANSCODER\_PAUSED) > 0) {
                   this->stateChangeFuncs\_\[AVTRANSCODER\_PAUSED\]();
                }
                break;
          }
          case AVTRANSCODER\_CANCELLED: {
                this->transCoderState = AVTRANSCODER\_CANCELLED;
                if (this->stateChangeFuncs\_.count(AVTRANSCODER\_CANCELLED) > 0) {
                   this->stateChangeFuncs\_\[AVTRANSCODER\_CANCELLED\]();
                }
                break;
          }
          case AVTRANSCODER\_COMPLETED: {
                this->transCoderState = AVTRANSCODER\_COMPLETED;
                if (this->stateChangeFuncs\_.count(AVTRANSCODER\_COMPLETED) > 0) {
                   this->stateChangeFuncs\_\[AVTRANSCODER\_COMPLETED\]();
                }
                break;
          }
          default:
                break;
       }
    }
    
    static void AvTranscoderStateChangeCbImpl(OH\_AVTranscoder \*transcoder,  OH\_AVTranscoder\_State state, void \*userData)
    {
       LOG("AvTranscoderStateChangeCbImpl state: %{public}d", state);
       NdkAVTransCoderUser \*ndkAVTransCoderUser =  reinterpret\_cast<NdkAVTransCoderUser \*>(userData);
       if (ndkAVTransCoderUser == nullptr || transcoder == nullptr) {
          LOGE("AvTranscoderStateChangeCbImpl ndkAVTransCoderUser or transcoder is  nullptr");
          return;
       }
       ndkAVTransCoderUser->OnStateChangeCb(transcoder, state);
    }
    
    static void AvTranscoderErrorCbImpl(OH\_AVTranscoder \*transcoder, int32\_t  errorCode, const char \*errorMsg,
                                        void \*userData)
    {
       LOG("AvTranscoderErrorCbImpl errorCode: %{public}d, errorMsg: %{public}s",  errorCode,
          errorMsg == nullptr ? "unknown" : errorMsg);
       NdkAVTransCoderUser \*ndkAVTransCoderUser =  reinterpret\_cast<NdkAVTransCoderUser \*>(userData);
       if (ndkAVTransCoderUser == nullptr || transcoder == nullptr) {
          LOGE("AvTranscoderErrorCbImpl ndkAVTransCoderUser or transcoder is  nullptr");
          return;
       }
       ndkAVTransCoderUser->OnErrorCb(transcoder, errorCode, errorMsg);
    }
    
    static void AvTranscoderProgressUpdateCbImpl(OH\_AVTranscoder \*transcoder, int  progress, void \*userData)
    {
       LOG("AvTranscoderProgressUpdateCbImpl progress: %{public}d", progress);
       NdkAVTransCoderUser \*ndkAVTransCoderUser =  reinterpret\_cast<NdkAVTransCoderUser \*>(userData);
       if (ndkAVTransCoderUser == nullptr || transcoder == nullptr) {
          LOGE("AvTranscoderProgressUpdateCbImpl ndkAVTransCoderUser or transcoder is  nullptr");
          return;
       }
       ndkAVTransCoderUser->OnProgressUpdateCb(transcoder, progress);
    }
    static napi\_value OHAvTranscoderNdkPlay(napi\_env env, napi\_callback\_info info)
    {
       OH\_AVTranscoder\_SetStateCallback(transcoder, AvTranscoderStateChangeCbImpl, transcoderUser); // Set the status callback.
       OH\_AVTranscoder\_SetErrorCallback(transcoder, AvTranscoderErrorCbImpl, transcoderUser); // Set the error callback.
       OH\_AVTranscoder\_SetProgressUpdateCallback(transcoder, AvTranscoderProgressUpdateCbImpl, transcoderUser); // Set the progress callback.
    }
    
3.  Call **OH\_AVTranscoderConfig\_Create()** to create a transcoding configuration instance.
    
    OH\_AVTranscoder\_Config \*config = OH\_AVTranscoderConfig\_Create();
    
4.  Call **OH\_AVTranscoderConfig\_SetSrcFD()** to set the file descriptor of the source video.
    
    OH\_AVTranscoderConfig\_SetSrcFD(config, srcFd, srcOffset, length); // Set the file descriptor of the source video.
    
5.  Call **OH\_AVTranscoderConfig\_SetDstFD()** to set the file descriptor of the output video.
    
    OH\_AVTranscoderConfig\_SetDstFD(config, dstFd); // Set the target file descriptor dstFd for transcoding.
    
6.  (Optional) Call **OH\_AVTranscoderConfig\_SetDstVideoType()** to set the encoding format of the output video.
    
    OH\_AVTranscoderConfig\_SetDstVideoType(config, "video/avc"); // (Optional) Set the video encoding format.
    
7.  (Optional) Call **OH\_AVTranscoderConfig\_SetDstAudioType()** to set the encoding format of the output audio.
    
    OH\_AVTranscoderConfig\_SetDstAudioType(config, "audio/mp4a-latm"); // (Optional) Set the audio encoding format.
    
8.  Call **OH\_AVTranscoderConfig\_SetDstFileType()** to set the container format of the output video.
    
    OH\_AVTranscoderConfig\_SetDstFileType(config, AV\_OUTPUT\_FORMAT\_MPEG\_4); // Container format.
    
9.  (Optional) Call **OH\_AVTranscoderConfig\_SetDstAudioBitrate()** to set the bit rate of the output audio.
    
    const std::int32\_t AUDIO\_BITRATE = 200000;
    OH\_AVTranscoderConfig\_SetDstAudioBitrate(config, AUDIO\_BITRATE); // (Optional) Audio bit rate.
    
10.  (Optional) Call **OH\_AVTranscoderConfig\_SetDstVideoBitrate()** to set the bit rate of the output video.
     
     const std::int32\_t VIDEO\_BITRATE = 3000000;
     OH\_AVTranscoderConfig\_SetDstVideoBitrate(config, VIDEO\_BITRATE); // (Optional) Video bit rate.
     
11.  (Optional) Call **OH\_AVTranscoderConfig\_SetDstVideoResolution()** to set the resolution of the output video.
     
     const std::int32\_t VIDEO\_WIDTH = 1280;
     const std::int32\_t VIDEO\_HEIGHT = 720;
     OH\_AVTranscoderConfig\_SetDstVideoResolution(config, VIDEO\_WIDTH, VIDEO\_HEIGHT);
     
12.  Call **OH\_AVTranscoder\_Prepare()** to prepare for transcoding. After a successful call, the instance transitions to the **AVTRANSCODER\_PREPARED** state.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoder\_Prepare(transcoder, config); // Prepare for transcoding.
     
13.  Call **OH\_AVTranscoder\_Start()** to start transcoding. After a successful call, the instance transitions to the **AVTRANSCODER\_STARTED** state.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoder\_Start(transcoder); // Start transcoding.
     
14.  (Optional) Call **OH\_AVTranscoder\_Pause()** to pause transcoding. After a successful call, the instance transitions to the **AVTRANSCODER\_PAUSED** state.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoder\_Pause(transcoder); // Pause transcoding.
     
15.  (Optional) Call **OH\_AVTranscoder\_Resume()** to resume transcoding. After a successful call, the instance transitions to the **AVTRANSCODER\_STARTED** state.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoder\_Resume(transcoder); // Resume transcoding.
     
16.  (Optional) Call **OH\_AVTranscoder\_Cancel()** to cancel transcoding. After a successful call, the instance transitions to the **AVTRANSCODER\_CANCELLED** state.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoder\_Cancel(transcoder); // Cancel transcoding.
     
17.  Call **OH\_AVTranscoderConfig\_Release()** to destroy the transcoding configuration instance and release resources.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoderConfig\_Release(config); // Release the transcoding configuration instance.
     
18.  Call **OH\_AVTranscoder\_Release()** to destroy the transcoding instance and release resources.
     
     OH\_AVErrCode errCode = AV\_ERR\_OK;
     errCode = OH\_AVTranscoder\_Release(transcoder); // Release the transcoding instance.
     

#### Running the Sample Project

1.  Create a project, download the [sample project](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVTranscoder/AVTranscoderNDK), and copy its resources to the corresponding directories.
    
    AVTranscoderNDK
    entry/src/main/ets/
    └── pages
        │    └── Index.ets (transcoding UI)
    entry/src/main/
    ├── cpp
    │   ├── types
    │   │   └── libentry
    │   │       └── Index.d.ts (JavaScript mapping of NDK functions)
    │   ├── CMakeLists.txt (CMake script)
    │   └── napi\_init.cpp (NDK functions)
    └── resources
        ├── base
        │   └── element
        │       ├── color.json
        │       ├── float.json
        │       └── string.json
        └── rawfile
            └── src.mp4 (video resource)
    
2.  Compile and run the project.
