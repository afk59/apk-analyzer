# Using AVRecorder to Record Audio (C/C++)

You can use the AVRecorder to develop the audio or video recording service. The AVRecorder supports audio capture, audio encoding, video encoding, audio encapsulation, and video encapsulation. It is applicable to simple audio/video recording scenarios and can be used to generate local media files directly.

In this topic, you will learn how to use the AVRecorder to complete the process of starting, pausing, resuming, and stopping audio recording.

During application development, you can use the **state** property of the AVRecorder to obtain the AVRecorder state or call **OH\_AVRecorder\_SetStateCallback** to listen for state changes. Your code must meet the state machine requirements. For example, **OH\_AVRecorder\_Pause()** is called only when the AVRecorder is in the **started** state, and **OH\_AVRecorder\_Resume()** is called only when it is in the **paused** state.

**Figure 1** Recording state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/m1ijxb7bQQOYAH1BKHiztQ/en-us_image_0000002568764915.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=197110AFF2280A56BBE85EF2B87830D6D7F14F0C7311016463781393C0662B54)

For details about the states, see [AVRecorderState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-t#avrecorderstate9).

#### Requesting Permissions

Before your development, configure the following permissions for your application.

-   To use the microphone, request the ohos.permission.MICROPHONE permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To read and save audio files, preferentially use [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/VLqOdEDBTveuWBvbaU2SKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CC7ED8AEB65614BAA685E644553632DAE0210F95DB9959BF15D7A9AE4B42D79)

To clone, back up, or synchronize audio files in users' public directory, request the ohos.permission.READ\_AUDIO and ohos.permission.WRITE\_AUDIO permissions for reading and writing audio files. For details, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md), which can be used only after being approved by AppGallery Connect (AGC). To prevent the application release request from being rejected, you are advised to use alternative solutions such as Pickers and components preferentially. Restricted permissions are granted only when the [related conditions are met](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_audio)..

#### How to Develop

To record only audio, you do not need to set video-related parameters such as **videoFrameWidth** and **videoFrameHeight**. Similarly, to record only videos, you do not need to set audio-related parameters such as **audioBitrate** and **audioChannels**.

You can use C/C++ APIs related to video recording by including the header files [avrecorder.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-h), [avrecorder\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-base-h), and [native\_averrors.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h).

Read [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder) for the API reference.

Link the dynamic libraries in the CMake script.

target\_link\_libraries(entry PUBLIC libavrecorder.so)

To use [OH\_AVFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avformat-h) APIs, include the following header file:

#include <multimedia/player\_framework/native\_avformat.h>

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(entry PUBLIC libnative\_media\_core.so)

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)

1.  Create an AVRecorder instance. The AVRecorder is in the **idle** state.
    
    #include <multimedia/player\_framework/avrecorder.h>
    #include <multimedia/player\_framework/avrecorder\_base.h>
    
    static struct OH\_AVRecorder \*g\_avRecorder = nullptr;
    g\_avRecorder = OH\_AVRecorder\_Create();
    
2.  Set the events to listen for.
    
    | Event Type | Description |
    | :-- | :-- |
    | OnStateChange | Listens for AVRecorder state changes. |
    | OnError | Listens for AVRecorder errors. |
    | OnUri | Listens for media files generated by the AVRecorder. |
    
    // Set a callback to respond to state changes.
    void OnStateChange(OH\_AVRecorder \*recorder, OH\_AVRecorder\_State state,
        OH\_AVRecorder\_StateChangeReason reason, void \*userData) {
       (void)recorder;
       (void)userData;
    
       // Convert reason into a string.
       const char \*reasonStr = (reason == OH\_AVRecorder\_StateChangeReason::AVRECORDER\_USER) ? "USER" :
                               (reason == OH\_AVRecorder\_StateChangeReason::AVRECORDER\_BACKGROUND) ? "BACKGROUND" : "UNKNOWN";
    
       if (state == OH\_AVRecorder\_State::AVRECORDER\_IDLE) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange IDLE, reason: %{public}s", reasonStr);
          // Process the state change.
       }
       if (state == OH\_AVRecorder\_State::AVRECORDER\_PREPARED) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
          // Process the state change.
       }
       if (state == OH\_AVRecorder\_State::AVRECORDER\_STARTED) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
          // Process the state change.
       }
       if (state == OH\_AVRecorder\_State::AVRECORDER\_PAUSED) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
          // Process the state change.
       }
       if (state == OH\_AVRecorder\_State::AVRECORDER\_STOPPED) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
          // Process the state change.
       }
       if (state == OH\_AVRecorder\_State::AVRECORDER\_RELEASED) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
          // Process the state change.
       }
       if (state == OH\_AVRecorder\_State::AVRECORDER\_ERROR) {
          OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
          // Process the state change.
       }
    }
    
    // Set an error callback.
    void OnError(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg, void \*userData)
    {
       (void)recorder;
       (void)userData;
       OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
                   errorCode, errorMsg);
    }
    
    // Set a callback to listen for the generation of media files. (This operation is required when AUTO\_CREATE is selected for fileGenerationMode.)
    void OnUri(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData)
    {
       (void)recorder;
       (void)userData;
       OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OnUri in!");
       if (asset != nullptr) {
          auto changeRequest = OH\_MediaAssetChangeRequest\_Create(asset);
          if (changeRequest == nullptr) {
             OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== changeRequest is null!");
             return;
          }
          MediaLibrary\_ImageFileType imageFileType = MEDIA\_LIBRARY\_IMAGE\_JPEG; // Available video interfaces are provided by the media library.
          uint32\_t result = OH\_MediaAssetChangeRequest\_SaveCameraPhoto(changeRequest, imageFileType);
          OH\_LOG\_INFO(LOG\_APP, "result of OH\_MediaAssetChangeRequest\_SaveCameraPhoto: %d", result);
    
          uint32\_t resultChange = OH\_MediaAccessHelper\_ApplyChanges(changeRequest);
          OH\_LOG\_INFO(LOG\_APP, "result of OH\_MediaAccessHelper\_ApplyChanges: %d", resultChange);
    
          OH\_MediaAsset\_Release(asset);
          OH\_MediaAssetChangeRequest\_Release(changeRequest);
       } else {
          OH\_LOG\_ERROR(LOG\_APP, "Received null media asset!");
       }
       OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OnUri out!");
    }
    
3.  Set audio recording parameters and call **OH\_AVRecorder\_Prepare()**. The AVRecorder enters the **prepared** state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/RBeNj9qOTFeLYXS7duLeiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89C0001E272A8C39D8DED47275F735C8FA82A066128258FA46897FDFBEC3A06A)
    
    Pay attention to the following when configuring parameters:
    
    -   Before parameter configuration, ensure that you have gained the required permissions. For details, see [Requesting Permissions](#requesting-permissions).
        
    -   Set only audio-related parameters in **OH\_AVRecorder\_Config** of **prepare()**, as shown in the sample code.
        
    -   The recording output URL (URL in **OH\_AVRecorder\_Config** in the sample code) must be in the format of fd://xx (where xx indicates a file descriptor). You must call the basic file operation APIs to implement access to the application file. For details, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-c-c/document.md).
        
    
    void SetConfig(OH\_AVRecorder\_Config &config)
    {
        config.audioSourceType = AVRECORDER\_MIC;
    
        // Set media properties.
        config.profile.audioBitrate = 100000;
        config.profile.audioChannels = 2;
        config.profile.audioCodec = AVRECORDER\_AUDIO\_AAC;
        config.profile.audioSampleRate = 48000;
     
        config.profile.fileFormat = AVRECORDER\_CFT\_MPEG\_4A;
        config.fileGenerationMode = AVRECORDER\_APP\_CREATE;
     }
    
     // Prepare for recording.
     static napi\_value PrepareAVRecorder(napi\_env env, napi\_callback\_info info)
     {
         (void)info;
         OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== PrepareAVRecorder in!");
         g\_avRecorder = OH\_AVRecorder\_Create();
         OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== AVRecorder Create ok! g\_avRecorder: %{public}p", g\_avRecorder);
         if (g\_avRecorder == nullptr) {
             OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Create failed!");
         }
         OH\_AVRecorder\_Config \*config = new OH\_AVRecorder\_Config();
    
         SetConfig(\*config);
    
         // 1. Set the URL. (This operation is required when APP\_CREATE is selected for fileGenerationMode.)
         const std::string AVRECORDER\_ROOT = "/data/storage/el2/base/files/";
         int32\_t outputFd = open((AVRECORDER\_ROOT + "avrecorder01.mp3").c\_str(), O\_RDWR | O\_CREAT, 0777); // Set the file name.
         std::string fileUrl = "fd://" + std::to\_string(outputFd);
         config->url = const\_cast<char \*>(fileUrl.c\_str());
         OH\_LOG\_INFO(LOG\_APP, "config.url is: %s", const\_cast<char \*>(fileUrl.c\_str()));
    
         // 2. Set the callbacks.
         // State callback.
         OH\_AVRecorder\_SetStateCallback(g\_avRecorder, OnStateChange, nullptr);
    
         // Callback triggered when an error occurs.
         OH\_AVRecorder\_SetErrorCallback(g\_avRecorder, OnError, nullptr);
    
         // Callback triggered when a media file is generated. (This operation is required when AUTO\_CREATE is selected for fileGenerationMode.)
         OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OH\_AVRecorder\_SetUriCallback in!");
         OH\_AVErrCode ret = OH\_AVRecorder\_SetUriCallback(g\_avRecorder, OnUri, nullptr);
         OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OH\_AVRecorder\_SetUriCallback out!");
         if (ret == AV\_ERR\_OK) {
             OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OH\_AVRecorder\_SetUriCallback succeed!");
         } else {
             OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== Failed to set URI callback, error code: %d", ret);
         }
    
         // 3. Call the prepare API.
         int result = OH\_AVRecorder\_Prepare(g\_avRecorder, config);
         if (result != AV\_ERR\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
         }
    
         napi\_value res;
         napi\_create\_int32(env, result, &res);
         return res;
     }
    
4.  Call **OH\_AVRecorder\_Start()** to start recording. The AVRecorder enters the **started** state.
    
    OH\_AVRecorder\_Start(g\_avRecorder);
    
5.  Call **OH\_AVRecorder\_Pause()** to pause recording. The AVRecorder enters the **paused** state. In addition, pause data input.
    
    OH\_AVRecorder\_Pause(g\_avRecorder);
    
6.  Call **OH\_AVRecorder\_Resume()** to resume recording. The AVRecorder enters the **started** state again.
    
    OH\_AVRecorder\_Resume(g\_avRecorder);
    
7.  Call **OH\_AVRecorder\_Stop()** to stop recording. The AVRecorder enters the **stopped** state.
    
    OH\_AVRecorder\_Stop(g\_avRecorder);
    
8.  Call **OH\_AVRecorder\_Reset()** to reset the resources. The AVRecorder enters the **idle** state. In this case, you can reconfigure the recording parameters.
    
    OH\_AVRecorder\_Reset(g\_avRecorder);
    
9.  Call **OH\_AVRecorder\_Release()** to switch the AVRecorder to the **released** state. Now your application exits the recording.
    
    OH\_AVRecorder\_Release(g\_avRecorder);
    

#### Complete Sample Code

Refer to the sample code below to complete the process of creating a recorder instance; preparing for recording; starting, pausing, resuming, and stopping recording; resetting the recording state; and releasing the recording resources.

#include <unistd.h>
#include <fcntl.h>
#include "hilog/log.h"
#include <multimedia/player\_framework/avrecorder.h>
#include <multimedia/player\_framework/avrecorder\_base.h>
#include <multimedia/media\_library/media\_asset\_change\_request\_capi.h>
#include <multimedia/media\_library/media\_access\_helper\_capi.h>
#include <multimedia/media\_library/media\_asset\_capi.h>

static struct OH\_AVRecorder \*g\_avRecorder = nullptr;
static int32\_t g\_outputFd;

// Set a callback to respond to state changes.
void OnStateChange(OH\_AVRecorder \*recorder, OH\_AVRecorder\_State state,
    OH\_AVRecorder\_StateChangeReason reason, void \*userData) {
   (void)recorder;
   (void)userData;

   // Convert reason into a string.
   const char \*reasonStr = (reason == OH\_AVRecorder\_StateChangeReason::AVRECORDER\_USER) ? "USER" :
                           (reason == OH\_AVRecorder\_StateChangeReason::AVRECORDER\_BACKGROUND) ? "BACKGROUND" : "UNKNOWN";

   if (state == OH\_AVRecorder\_State::AVRECORDER\_IDLE) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange IDLE, reason: %{public}s", reasonStr);
      // Process the state change.
   }
   if (state == OH\_AVRecorder\_State::AVRECORDER\_PREPARED) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
      // Process the state change.
   }
   if (state == OH\_AVRecorder\_State::AVRECORDER\_STARTED) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
      // Process the state change.
   }
   if (state == OH\_AVRecorder\_State::AVRECORDER\_PAUSED) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
      // Process the state change.
   }
   if (state == OH\_AVRecorder\_State::AVRECORDER\_STOPPED) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
      // Process the state change.
   }
   if (state == OH\_AVRecorder\_State::AVRECORDER\_RELEASED) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
      // Process the state change.
   }
   if (state == OH\_AVRecorder\_State::AVRECORDER\_ERROR) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
      // Process the state change.
   }
}

// Set an error callback.
void OnError(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg, void \*userData)
{
   (void)recorder;
   (void)userData;
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
               errorCode, errorMsg);
}

// Set a callback to listen for the generation of media files. (This operation is required when AUTO\_CREATE is selected for fileGenerationMode.)
void OnUri(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData)
{
   (void)recorder;
   (void)userData;
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OnUri in!");
   if (asset != nullptr) {
      auto changeRequest = OH\_MediaAssetChangeRequest\_Create(asset);
      if (changeRequest == nullptr) {
         OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== changeRequest is null!");
         return;
      }
      MediaLibrary\_ImageFileType imageFileType = MEDIA\_LIBRARY\_IMAGE\_JPEG; // Available video interfaces are provided by the media library.
      uint32\_t result = OH\_MediaAssetChangeRequest\_SaveCameraPhoto(changeRequest, imageFileType);
      OH\_LOG\_INFO(LOG\_APP, "result of OH\_MediaAssetChangeRequest\_SaveCameraPhoto: %d", result);

      uint32\_t resultChange = OH\_MediaAccessHelper\_ApplyChanges(changeRequest);
      OH\_LOG\_INFO(LOG\_APP, "result of OH\_MediaAccessHelper\_ApplyChanges: %d", resultChange);

      OH\_MediaAsset\_Release(asset);
      OH\_MediaAssetChangeRequest\_Release(changeRequest);
   } else {
      OH\_LOG\_ERROR(LOG\_APP, "Received null media asset!");
   }
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== OnUri out!");
}

void SetConfig(OH\_AVRecorder\_Config &config)
{
   config.audioSourceType = AVRECORDER\_MIC;

   // Set media properties.
   config.profile.audioBitrate = 96000;
   config.profile.audioChannels = 2;
   config.profile.audioCodec = AVRECORDER\_AUDIO\_AAC;
   config.profile.audioSampleRate = 48000;

   config.profile.fileFormat = AVRECORDER\_CFT\_MPEG\_4;
   config.fileGenerationMode = AVRECORDER\_APP\_CREATE;

   config.metadata.location.latitude = 27.791863;
   config.metadata.location.longitude = 64.574687;
}

// 1. Prepare for recording.
static napi\_value PrepareAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== PrepareAVRecorder in!");
   g\_avRecorder = OH\_AVRecorder\_Create();
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== AVRecorder Create ok! g\_avRecorder: %{public}p", g\_avRecorder);
   if (g\_avRecorder == nullptr) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Create failed!");
   }
   OH\_AVRecorder\_Config \*config = new OH\_AVRecorder\_Config();

   SetConfig(\*config);

   // 1.1 Set the URL. (This operation is required when APP\_CREATE is selected for fileGenerationMode.)
   const std::string AVRECORDER\_ROOT = "/data/storage/el2/base/files/";
   g\_outputFd = open((AVRECORDER\_ROOT + "avrecorder01.mp3").c\_str(), O\_RDWR | O\_CREAT, 0777); // Set the file name.
   std::string fileUrl = "fd://" + std::to\_string(g\_outputFd);
   config->url = const\_cast<char \*>(fileUrl.c\_str());
   OH\_LOG\_INFO(LOG\_APP, "config.url is: %s", const\_cast<char \*>(fileUrl.c\_str()));

   // 1.2 Set the callbacks.
   // State callback.
   OH\_AVRecorder\_SetStateCallback(g\_avRecorder, OnStateChange, nullptr);

   // Callback triggered when an error occurs.
   OH\_AVRecorder\_SetErrorCallback(g\_avRecorder, OnError, nullptr);

   // Callback triggered when a media file is generated. (This operation is required when AUTO\_CREATE is selected for fileGenerationMode.)
   OH\_AVErrCode ret = OH\_AVRecorder\_SetUriCallback(g\_avRecorder, OnUri, nullptr);
   if (ret == AV\_ERR\_OK) {
      OH\_LOG\_INFO(LOG\_APP, "==NDKDemo==  OH\_AVRecorder\_SetUriCallback succeed!");
   } else {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo==  Failed to set URI callback, error code: %d", ret);
   }

   // 1.3 Call the prepare API.
   int result = OH\_AVRecorder\_Prepare(g\_avRecorder, config);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
   }

   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 2. Start recording.
static napi\_value StartAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== g\_avRecorder start: %{public}p", g\_avRecorder);
   int result = OH\_AVRecorder\_Start(g\_avRecorder);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Start failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 3. Pause recording.
static napi\_value PauseAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   int result = OH\_AVRecorder\_Pause(g\_avRecorder);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Pause failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 4. Resume recording.
static napi\_value ResumeAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   int result = OH\_AVRecorder\_Resume(g\_avRecorder);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Resume failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 5. Stop recording.
static napi\_value StopAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   int result = OH\_AVRecorder\_Stop(g\_avRecorder);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Stop failed %{public}d", result);
   }
   close(g\_outputFd);
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 6. Reset the recording state.
static napi\_value ResetAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   // Check whether g\_avRecorder is valid.
   if (g\_avRecorder == nullptr) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== g\_avRecorder is nullptr!");
      napi\_value res;
      napi\_create\_int32(env, AV\_ERR\_INVALID\_VAL, &res);
      return res;
   }

   int result = OH\_AVRecorder\_Reset(g\_avRecorder);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Reset failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 7. Release recording resources.
static napi\_value ReleaseAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   // Check whether g\_avRecorder is valid.
   if (g\_avRecorder == nullptr) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== g\_avRecorder is nullptr!");
      napi\_value res;
      napi\_create\_int32(env, AV\_ERR\_INVALID\_VAL, &res);
      return res;
   }
   
   int result = OH\_AVRecorder\_Release(g\_avRecorder);
   g\_avRecorder = nullptr;   // After recording resources are released, the g\_avRecorder pointer must be explicitly set to null.
   
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Release failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}
