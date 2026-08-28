# Using AVRecorder to Record Videos (C/C++)

You can use the AVRecorder to develop the audio and video recording service. The AVRecorder supports audio capture, audio encoding, video encoding, audio encapsulation, and video encapsulation. It is applicable to simple video recording scenarios and can be used to generate local media files directly.

In this topic, you will learn how to use the AVRecorder to complete the process of starting, pausing, resuming, and stopping video recording.

During application development, you can use the **state** property of the AVRecorder to obtain the AVRecorder state or call **OH\_AVRecorder\_SetStateCallback** to listen for state changes. Your code must meet the state machine requirements. For example, **pause()** is called only when the AVRecorder is in the **started** state, and **resume()** is called only when it is in the **paused** state.

**Figure 1** Recording state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/b8_w-DKkSbGDb6GvrJVwlg/en-us_image_0000002568684909.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4035080495FF5D9A3C158050CD6851331AD91CDFA46CF7C5A6E2FB51751EE22)

For details about the states, see [AVRecorderState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-t#avrecorderstate9).

#### Requesting Permissions

Before your development, configure the following permissions for your application.

-   To use the microphone, request the ohos.permission.MICROPHONE permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To use the camera for photo capture, request the ohos.permission.CAMERA permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To read images or videos from Gallery, preferentially use the media library [Picker for access](../../../../media-library-kit/selecting-media-assets-using-picker/document.md).
-   To save images or videos to Gallery, preferentially use the [security component for storage](../../../../media-library-kit/saving-media-assets/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/-7kt_dLYQPumTZteeCyV6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=884991D7E4E6A107B1E3D5536E438053D70E051306AE6389A00AE387E847E447)

To clone, back up, or synchronize images and videos in users' public directory, request the ohos.permission.READ\_IMAGEVIDEO and ohos.permission.WRITE\_IMAGEVIDEO permissions for reading and writing audio/video files. For details, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md), which can be used only after being approved by AppGallery Connect (AGC). To prevent the application release request from being rejected, you are advised to use alternative solutions such as Pickers and components preferentially. Restricted permissions are granted only when the [related conditions are met](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_imagevideo)..

#### How to Develop

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/LxiS9j8SSXOxX5Djw-29vQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5422BF27C467DCEAAD4ACCDC214EC96677BFD1BC3601DFC6A14E55C7A3025C8A)

The AVRecorder only processes video data. To complete video recording, it must work with the video data collection module, which transfers the captured video data to the AVRecorder for data processing through the surface. Currently, the commonly used data collection module is the camera module. For details, see [Camera Recording](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/video-recording-c-c/document.md).

For details about how to create and save a file, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md). By default, files are saved in the sandbox path of the application. To save them to Gallery, use the [security components](../../../../media-library-kit/saving-media-assets/document.md).

You can use C/C++ APIs related to video recording by including the header files [avrecorder.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-h), [avrecorder\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-base-h), and [native\_averrors.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h).

Read [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder) for the API reference.

Link the dynamic library in the CMake script.

target\_link\_libraries(entry PUBLIC libavrecorder.so)

To use [OH\_AVFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avformat-h) APIs, include the following header file:

#include <multimedia/player\_framework/native\_avformat.h>

In addition, link the following dynamic library in the CMake script:

target\_link\_libraries(entry PUBLIC libnative\_media\_core.so)

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic library in the CMake script:

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
        if (state == OH\_AVRecorder\_State::PREPARED) {
            OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange PREPARED, reason: %{public}s", reasonStr);
            // Process the state change.
        }
        if (state == OH\_AVRecorder\_State::STARTED) {
            OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange STARTED, reason: %{public}s", reasonStr);
            // Process the state change.
        }
        if (state == OH\_AVRecorder\_State::PAUSED) {
            OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange PAUSED, reason: %{public}s", reasonStr);
            // Process the state change.
        }
        if (state == OH\_AVRecorder\_State::STOPPED) {
            OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange STOPPED, reason: %{public}s", reasonStr);
            // Process the state change.
        }
        if (state == OH\_AVRecorder\_State::RELEASED) {
            OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange RELEASED, reason: %{public}s", reasonStr);
            // Process the state change.
        }
        if (state == OH\_AVRecorder\_State::ERROR) {
            OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnStateChange ERROR, reason: %{public}s", reasonStr);
            // Process the state change.
        }
    }
    
    // Set an error callback.
    void OnError(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg, void \*userData) {
        (void)recorder;
        (void)userData;
        OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== Recorder OnError errorCode: %{public}d, error message: %{public}s",
            errorCode, errorMsg);
    }
    
    // Set a callback to listen for the generation of media files. (This operation is required when AUTO\_CREATE is selected for fileGenerationMode.)
    void OnUri(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData) {
        (void)recorder;
        (void)userData;
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
    }
    
3.  Set video recording parameters and call **OH\_AVRecorder\_Prepare()**. The AVRecorder enters the **prepared** state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/w8c-iPycQu6tuBESh_EUsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=709EFC79BE9372ED33BB0B72867FF1852A27B89DA847D84DB32157B44B40A282)
    
    Pay attention to the following when configuring parameters:
    
    -   Before parameter configuration, ensure that you have gained the required permissions. For details, see [Requesting Permissions](#requesting-permissions).
        
    -   In pure video recording scenarios, set only video-related parameters in **OH\_AVRecorder\_Config** of **OH\_AVRecorder\_Prepare()**.
        
    -   The [recording specifications](../../../about-this-kit/document.md#supported-formats) in use must be those supported. The video bit rate, resolution, and frame rate are subject to the ranges supported by the hardware device.
        
    -   The recording output URL (URL in **OH\_AVRecorder\_Config** in the sample code) must be in the format of fd://xx (where xx indicates a file descriptor). You must call the basic file operation APIs to implement access to the application file. For details, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-c-c/document.md).
        
    
    void SetConfig(OH\_AVRecorder\_Config &config)
    {
        config.audioSourceType = AVRECORDER\_MIC;
        config.videoSourceType = AVRECORDER\_SURFACE\_ES;
    
        // Set media properties.
        config.profile.audioBitrate = 96000;
        config.profile.audioChannels = 2;
        config.profile.audioCodec = AVRECORDER\_AUDIO\_AAC;
        config.profile.audioSampleRate = 48000;
    
        config.profile.videoBitrate = 2000000;
        config.profile.videoFrameWidth = 1280;
        config.profile.videoFrameHeight = 720;
        config.profile.videoFrameRate = 30;
        config.profile.videoCodec = AVRECORDER\_VIDEO\_AVC;
        config.profile.isHdr = false;
        config.profile.enableTemporalScale = false;
     
        config.profile.fileFormat = AVRECORDER\_CFT\_MPEG\_4;
        config.fileGenerationMode = AVRECORDER\_APP\_CREATE;
    
        config.metadata.videoOrientation = new char\[2\]; // You should release the memory allocated.
        if (config.metadata.videoOrientation != nullptr) {
            strcpy(config.metadata.videoOrientation, "0"); // Video rotation angle, which can be 0, 90, 180, or 270.
        }
        OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== videoOrientation: %{public}s", config.metadata.videoOrientation);
    
        config.metadata.location.latitude = 27.791863;
        config.metadata.location.longitude = 64.574687;
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
         OH\_AVRecorder\_Config \*config = new OH\_AVRecorder\_Config(); // You should release the memory allocated.
         
         SetConfig(\*config);
     
         // 1. Set the URL. (This operation is required when APP\_CREATE is selected for fileGenerationMode.)
         const std::string AVRECORDER\_ROOT = "/data/storage/el2/base/files/";
         int32\_t outputFd = open((AVRECORDER\_ROOT + "avrecorder01.mp4").c\_str(), O\_RDWR | O\_CREAT, 0777); // Set the file name.
         std::string fileUrl = "fd://" + std::to\_string(outputFd);
         config->url = const\_cast<char \*>(fileUrl.c\_str());
         OH\_LOG\_INFO(LOG\_APP, "config.url is: %s", const\_cast<char \*>(fileUrl.c\_str()));
     
         // 2. Set the callbacks.
         // Callback triggered when the state changes.
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
         
         // 3. Call the prepare API.
         int result = OH\_AVRecorder\_Prepare(g\_avRecorder, config);
         if (result != AV\_ERR\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Prepare failed %{public}d", result);
         }
       
         // 4. Release the memory.
         delete config->metadata.videoOrientation;
         delete config;
         config = nullptr;
       
         napi\_value res;
         napi\_create\_int32(env, result, &res);
         return res;
     }
    
4.  Obtain the surface ID required for video recording and initialize the video data input source. This step is performed in the video data collection module. For the camera module, you need to create a Camera instance, obtain the camera list, create a camera input stream, and create a video output stream. For details, see [Video Recording](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/video-recording-c-c/document.md).
    
    Call **getInputSurface()**. The returned surface ID is transferred to the video data collection module, which is generally the camera module. The following sample code demonstrates only the procedure for obtaining the surface ID.
    
    The video data collection module obtains the surface based on the surface ID and transmits video data to the AVRecorder through the surface. Then the AVRecorder processes the video data.
    
    // Obtain the surface ID.
    OHNativeWindow \*window = nullptr;
    int resultCode = OH\_AVRecorder\_GetInputSurface(g\_avRecorder, &window);
    uint64\_t surfaceId = 0;
    if (resultCode == AV\_ERR\_OK && window != nullptr) {
       OH\_NativeWindow\_GetSurfaceId(window, &surfaceId);
    }
    
5.  Initialize the video data input source. This step is performed in the video data collection module. For the camera module, you need to create a Camera instance, obtain the camera list, create a camera input stream, and create a video output stream. For details, see [Video Recording](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/video-recording-c-c/document.md).
    
6.  Start recording. Start the input source to input video data, for example, by calling **OH\_VideoOutput\_Start()** of the camera module. Then call **OH\_AVRecorder\_Start()** to switch the AVRecorder to the **started** state.
    
    OH\_AVRecorder\_Start(g\_avRecorder);
    
7.  Call **OH\_AVRecorder\_Pause()** to pause recording. The AVRecorder enters the **paused** state. In addition, pause data input, for example, by calling **OH\_VideoOutput\_Stop()** of the camera module.
    
    OH\_AVRecorder\_Pause(g\_avRecorder);
    
8.  Call **OH\_AVRecorder\_Resume()** to resume recording. The AVRecorder enters the **started** state again.
    
    OH\_AVRecorder\_Resume(g\_avRecorder);
    
9.  Call **OH\_AVRecorder\_Stop()** to stop recording. The AVRecorder enters the **stopped** state again. In addition, stop camera recording.
    
    OH\_AVRecorder\_Stop(g\_avRecorder);
    
10.  Call **OH\_AVRecorder\_Reset()** to reset the resources. The AVRecorder enters the **idle** state. In this case, you can reconfigure the recording parameters.
     
     OH\_AVRecorder\_Reset(g\_avRecorder);
     
11.  Call **OH\_AVRecorder\_Release()** to release the resources. The AVRecorder enters the **released** state. In addition, release the video data input source resources (camera resources in this example).
     
     OH\_AVRecorder\_Release(g\_avRecorder);
     

#### Complete Sample Code

Refer to the sample code below to complete the process of creating a recorder instance, preparing for, starting, pausing, resuming, and stopping recording, resetting the recording state, and releasing the recording resources.

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
                   OH\_AVRecorder\_StateChangeReason reason, void \*userData)
{
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
   config.videoSourceType = AVRECORDER\_SURFACE\_ES;

   // Set media properties.
   config.profile.audioBitrate = 96000;
   config.profile.audioChannels = 2;
   config.profile.audioCodec = AVRECORDER\_AUDIO\_AAC;
   config.profile.audioSampleRate = 48000;

   config.profile.videoBitrate = 2000000;
   config.profile.videoFrameWidth = 1280;
   config.profile.videoFrameHeight = 720;
   config.profile.videoFrameRate = 30;
   config.profile.videoCodec = AVRECORDER\_VIDEO\_AVC;
   config.profile.isHdr = false;
   config.profile.enableTemporalScale = false;

   config.profile.fileFormat = AVRECORDER\_CFT\_MPEG\_4;
   config.fileGenerationMode = AVRECORDER\_APP\_CREATE;

   config.metadata.videoOrientation = new char\[2\]; // You should release the memory allocated.
   if (config.metadata.videoOrientation != nullptr) {
      strcpy(config.metadata.videoOrientation, "0"); // Video rotation angle, which can be 0, 90, 180, or 270.
   }
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== videoOrientation: %{public}s", config.metadata.videoOrientation);

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
   OH\_AVRecorder\_Config \*config = new OH\_AVRecorder\_Config(); // You should release the memory allocated.

   SetConfig(\*config);

   // 1.1 Set the URL. (This operation is required when APP\_CREATE is selected for fileGenerationMode.)
   const std::string AVRECORDER\_ROOT = "/data/storage/el2/base/files/";
   g\_outputFd = open((AVRECORDER\_ROOT + "avrecorder01.mp4").c\_str(), O\_RDWR | O\_CREAT, 0777); // Set the file name.
   std::string fileUrl = "fd://" + std::to\_string(g\_outputFd);
   config->url = const\_cast<char \*>(fileUrl.c\_str());

   // 1.2 Set the callbacks.
   // Callback triggered when the state changes.
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
   
   // 1.4 Release the memory.
   delete config->metadata.videoOrientation;
   delete config;
   config = nullptr;

   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 2. Start the camera.
static napi\_value PrepareCamera(napi\_env env, napi\_callback\_info info)
{
   OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== AVRecorder PrepareCamera");
   (void)info;

   OHNativeWindow \*window = nullptr;
   int resultCode = OH\_AVRecorder\_GetInputSurface(g\_avRecorder, &window);
   if (resultCode != AV\_ERR\_OK || window == nullptr) {
       OH\_LOG\_INFO(LOG\_APP, "==NDKDemo== AVRecorder OH\_AVRecorder\_GetInputSurface failed!");
       napi\_value errorResult;
       napi\_create\_int32(env, -1, &errorResult); // -1 indicates an error.
       return errorResult;
   }
   uint64\_t surfaceId = 0;
   OH\_NativeWindow\_GetSurfaceId(window, &surfaceId);

   // Pass the surface ID to the data collection module. For details, see the camera module.

   int result = 0;
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 3. Start recording.
static napi\_value StartAVRecorder(napi\_env env, napi\_callback\_info info)
{
   (void)info;
   int result = OH\_AVRecorder\_Start(g\_avRecorder);
   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Start failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}

// 4. Pause recording.
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

// 5. Resume recording.
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

// 6. Stop recording.
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

// 7. Reset the recording state.
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

// 8. Release recording resources.
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
   g\_avRecorder = nullptr; // After recording resources are released, the g\_avRecorder pointer must be explicitly set to null.

   if (result != AV\_ERR\_OK) {
      OH\_LOG\_ERROR(LOG\_APP, "==NDKDemo== AVRecorder Release failed %{public}d", result);
   }
   napi\_value res;
   napi\_create\_int32(env, result, &res);
   return res;
}
