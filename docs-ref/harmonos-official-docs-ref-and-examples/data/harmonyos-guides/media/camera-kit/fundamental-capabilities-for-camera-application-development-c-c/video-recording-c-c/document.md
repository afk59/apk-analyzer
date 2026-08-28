# Video Recording (C/C++)

As another important function of the camera application, video recording is the process of cyclic frame capture. To smooth video recording, you can follow step 5 in [Photo Capture](../photo-capture-c-c/document.md) to set the resolution, flash, focal length, photo quality, and rotation angle.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK, which provides camera-related properties and methods.
    
    #include <cstdint>
    #include <native\_buffer/buffer\_common.h>
    #include <unistd.h>
    #include <string>
    #include <thread>
    #include <cstdio>
    #include <fcntl.h>
    #include <map>
    #include <string>
    #include <vector>
    #include <native\_buffer/native\_buffer.h>
    #include "iostream"
    #include "mutex"
    
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "napi/native\_api.h"
    #include "ohcamera/camera\_manager.h"
    #include <window\_manager/oh\_display\_info.h>
    #include <window\_manager/oh\_display\_manager.h>
    
    namespace OHOS\_CAMERA\_SAMPLE {
    class NDKCamera {
      public:
        struct CameraBuildingConfig {
            char \*str;
            uint32\_t focusMode;
            uint32\_t cameraDeviceIndex;
            bool isVideo;
            bool isHdr;
            char \*videoId;
        };
        ~NDKCamera();
        explicit NDKCamera(CameraBuildingConfig config);
        // ...
    };
    } // namespace OHOS\_CAMERA\_SAMPLE
    
2.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Obtain the surface ID.
    
    The [OH\_AVRecorder\_Create()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_create) API provided by the system can be used to create an **AVRecorder** instance. You can obtain the surface ID via the [OH\_AVRecorder\_GetInputSurface()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_getinputsurface) method of the instance.
    
4.  Create a video output stream.
    
    Based on the surface ID passed in, call [OH\_CameraManager\_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability) to obtain [Camera\_OutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-outputcapability). From there, you can access **videoProfiles** to obtain the video output streams supported by the device. Then, define video recording parameters and use **OH\_CameraManager\_CreateVideoOutput** to create a video output stream.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/udgmnvohQcCaoey_VUUCPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF517E0561335DF92AD52D03A114FCA47B77845C68AC32F4581BF71268994609)
    
    -   The aspect ratio of the resolution for the preview stream and the recording output stream must be consistent. For example, if the aspect ratio in the sample code is 640:480 (equivalent to 4:3), the aspect ratio of the resolution for the preview stream must also be 4:3. Valid resolution options include: 640:480, 960:720, 1440:1080, etc.
        
    -   Before setting the width and height of the resolution for the preview output stream, you must first query the configurable range of video frame width and height via [OH\_AVRecorder\_Profile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-profile).
        
    
    Camera\_ErrorCode NDKCamera::CreateVideoOutput(char \*videoId)
    {
        if (videoProfile\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get videoProfiles failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreateVideoOutput(cameraManager\_, videoProfile\_, videoId, &videoOutput\_);
        OH\_LOG\_ERROR(LOG\_APP, " create video width: %{public}d, height: %{public}d, format: %{public}d",
            videoProfile\_->size.width, videoProfile\_->size.height, videoProfile\_->format);
        if (videoId == nullptr || videoOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateVideoOutput failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        VideoOutputRegisterCallback();
        return ret\_;
    }
    
5.  Start video recording.
    
    Call [OH\_VideoOutput\_Start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-output-h#oh_videooutput_start) to start the video output stream.
    
    Camera\_ErrorCode NDKCamera::VideoOutputStart(void)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutputStart begin.");
        Camera\_ErrorCode ret = OH\_VideoOutput\_Start(videoOutput\_);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_VideoOutput\_Start success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_Start failed. %d ", ret);
        }
        return ret;
    }
    
6.  Stop video recording.
    
    Call [OH\_VideoOutput\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-output-h#oh_videooutput_stop) to stop the video output stream.
    
    Camera\_ErrorCode NDKCamera::VideoOutputStop(void)
    {
        OH\_LOG\_ERROR(LOG\_APP, "enter VideoOutputStop.");
        ret\_ = OH\_VideoOutput\_Stop(videoOutput\_);
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "VideoOutputStop failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret\_;
    }
    

#### Status Listening

During camera application development, you can listen for the status of the video output stream, including recording start, recording end, and video output errors.

-   Register the **'frameStart'** event to listen for recording start events. This event can be registered when a VideoOutput instance is created and is triggered when the bottom layer starts exposure for recording for the first time. Video recording starts as long as the event is triggered.
    
    void VideoOutputOnFrameStart(Camera\_VideoOutput \*videoOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutputOnFrameStart");
    }
    
-   Register the **'frameEnd'** event to listen for recording end events. This event can be registered when a VideoOutput instance is created and is triggered when the last frame of recording ends. Video recording ends as long as a result is returned.
    
    void VideoOutputOnFrameEnd(Camera\_VideoOutput \*videoOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutput frameCount = %{public}d", frameCount);
    }
    
-   Register the **'error'** event to listen for video output errors. The callback function returns an error code when a video output API is incorrectly used. For details about the error code types, see [Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    void VideoOutputOnError(Camera\_VideoOutput \*videoOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutput errorCode = %{public}d", errorCode);
    }
    
    VideoOutput\_Callbacks \*NDKCamera::GetVideoOutputListener(void)
    {
        static VideoOutput\_Callbacks videoOutputListener = {
            .onFrameStart = VideoOutputOnFrameStart,
            .onFrameEnd = VideoOutputOnFrameEnd,
            .onError = VideoOutputOnError
        };
        return &videoOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::VideoOutputRegisterCallback(void)
    {
        ret\_ = OH\_VideoOutput\_RegisterCallback(videoOutput\_, GetVideoOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
