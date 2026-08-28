# Using AVScreenCapture to Capture Screens and Write Them to Files (C/C++)

Screen capture is mainly used to record the main screen.

You can call the C APIs of the [AVScreenCapture](../../../about-this-kit/document.md#avscreencapture) module to record the screen and collect audio and video source data output by the device and microphone. You can call the APIs to obtain audio and video files and transfer the files to other modules for playback or processing. In this way, screen content can be shared in the form of files.

The AVScreenCapture, Window, and Graphics modules together implement the entire video capture process.

The full-screen capture process involves creating an AVScreenCapture instance, configuring audio and video capture parameters, starting and stopping screen capture, and releasing the instance.

If you are in a call when screen capture starts or a call is coming during screen capture, screen capture automatically stops, and the **OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_CALL** status is reported.

Screen capture automatically stops upon system user switching, and **OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES** is reported.

This topic describes how to use the AVScreenCapture APIs to carry out one-time screen capture. For details about the API reference, see [AVScreenCapture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avscreencapture).

If microphone data collection is configured, configure the permission ohos.permission.MICROPHONE and request a continuous task. For details, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md) and [Continuous Task](../../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).

Starting from API version 22, when you perform screen capture for an application on a PC/2-in-1 device, you can request the ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK permission to maintain capture even when the screen is off but not locked. For details about the configuration, [Declaring Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

Starting from API version 22, when you perform screen capture for an application on a PC/2-in-1 device, you can request the ohos.permission.CUSTOM\_SCREEN\_RECORDING permission to prevent the privacy protection pop-up from being displayed during screen capture. For details about how to request the permission, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md).

#### How to Develop

After an AVScreenCapture instance is created, different APIs can be called to switch the AVScreenCapture to different states and trigger the required behavior.

If an API is called when the AVScreenCapture is not in the given state, the system may throw an exception or generate other undefined behavior. Therefore, you are advised to check the AVScreenCapture state before triggering state transition.

**Linking the Dynamic Libraries in the CMake Script**

target\_link\_libraries(entry PUBLIC libnative\_avscreen\_capture.so)

1.  Add the header files.
    
    #include "napi/native\_api.h"
    #include <multimedia/player\_framework/native\_avscreen\_capture.h>
    #include <multimedia/player\_framework/native\_avscreen\_capture\_base.h>
    #include <multimedia/player\_framework/native\_avscreen\_capture\_errors.h>
    #include <fcntl.h>
    #include <string>
    #include <unistd.h>
    
2.  Create an AVScreenCapture instance, named **capture** in this example.
    
    OH\_AVScreenCapture\* capture = OH\_AVScreenCapture\_Create();
    
3.  Set screen capture parameters.
    
    After creating the capture instance, you can set the parameters required for screen capture.
    
    By default, internal capture is used when captured files need to be stored. The microphone, which can be dynamically turned on or off, can be used for both internal capture and external capture.
    
    A callback function must be set to listen for the capture status when captured files need to be stored.
    
    // Obtain the external capture (using microphones) or internal capture information. The internal capture parameters are mandatory. If both parameters are set, the parameter settings for internal capture and external capture must be the same.
    OH\_AudioCaptureInfo micCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH\_MIC
    };
    
    OH\_AudioCaptureInfo innerCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH\_ALL\_PLAYBACK
    };
    //Configure audio output specifications for screen capture. audioBitrate ensures that the bit rate of the output file matches the expected bit rate and has no strong correlation with audioSampleRate.
    OH\_AudioEncInfo audioEncInfo = {
        .audioBitrate = 48000,
        .audioCodecformat = OH\_AAC\_LC
    };
    
    OH\_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = 768,
        .videoFrameHeight = 1280,
        .videoSource = OH\_VIDEO\_SOURCE\_SURFACE\_RGBA
    };
    
    OH\_VideoEncInfo videoEncInfo = {
        .videoCodec = OH\_H264,
        .videoBitrate = 2000000,
        .videoFrameRate = 30
    };
    
    OH\_AudioInfo audioInfo = {
        .innerCapInfo = innerCapInfo,
        .audioEncInfo = audioEncInfo
    };
    
    OH\_VideoInfo videoInfo = {
        .videoCapInfo = videoCapInfo,
        .videoEncInfo = videoEncInfo
    };
    
    config = {
        .captureMode = OH\_CAPTURE\_HOME\_SCREEN,
        .dataType = OH\_CAPTURE\_FILE,
        .audioInfo = audioInfo,
        .videoInfo = videoInfo,
    };
    
    OH\_AVScreenCapture\_Init(capture, config);
    
4.  Call **StartScreenRecording()** to start screen recording.
    
    OH\_AVScreenCapture\_StartScreenRecording(capture);
    
5.  Call **StopScreenRecording()** to stop screen recording.
    
    OH\_AVScreenCapture\_StopScreenRecording(capture);
    
6.  Call **Release()** to release the instance.
    
    OH\_AVScreenCapture\_Release(capture);
    

#### Complete Sample Code

Refer to the sample code below to implement captured file storage using AVScreenCapture.

#include "napi/native\_api.h"
#include <multimedia/player\_framework/native\_avscreen\_capture.h>
#include <multimedia/player\_framework/native\_avscreen\_capture\_base.h>
#include <multimedia/player\_framework/native\_avscreen\_capture\_errors.h>
#include <fcntl.h>
#include <string>
#include <unistd.h>

int32\_t outputFd;
struct OH\_AVScreenCapture\* capture;

void OnStateChange(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureStateCode stateCode, void \*userData) {
    (void)capture;
    
    if (stateCode == OH\_SCREEN\_CAPTURE\_STATE\_STARTED) {
        // Process the state change.
    }
    if (stateCode == OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_CALL ||
        stateCode == OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES) {
        // Process screen capture interruption.
    }
    if (stateCode == OH\_SCREEN\_CAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER) {
        // Process the state change.
    }
    (void)userData;
}

// The callback OnDisplaySelected() is invoked to obtain the display ID.
void OnDisplaySelected(struct OH\_AVScreenCapture \*capture, uint64\_t displayId, void \*userData) {
    (void)capture;
    (void)displayId;
    (void)userData;
}

// OnCaptureContentChanged(), a callback function invoked when screen capture content changes.
void OnCaptureContentChanged(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureContentChangedEvent event, OH\_Rect \*area, void \*userData) {
    (void)capture;
    if (event == OH\_SCREEN\_CAPTURE\_CONTENT\_HIDE) {
        // Process the event indicating that screen capture content is hidden.
    }
    if (event == OH\_SCREEN\_CAPTURE\_CONTENT\_VISIBLE) {
        // Process the event indicating that screen capture content is visible.
        // Obtain the window area information from the area parameter returned by the callback function when the screen capture content becomes visible.
    }
    if (event == OH\_SCREEN\_CAPTURE\_CONTENT\_UNAVAILABLE) {
        // Process the event indicating that screen capture content becomes unavailable, for example, the screen capture window is closed.
    }
    (void)area;
    (void)userData;
}

// The callback OnUserSelected() is invoked to handle user selection results on the manual confirmation UI.
void OnUserSelected(OH\_AVScreenCapture\* capture, OH\_AVScreenCapture\_UserSelectionInfo\* selections, void \*userData) {
    (void)capture;
    (void)userData;
    int\* selectType = new int;
    uint64\_t\* displayId = new uint64\_t;

    // Obtain the selection type and display ID through the API. OH\_AVScreenCapture\_UserSelectionInfo\* selections is valid only in the OnUserSelected callback.
    OH\_AVSCREEN\_CAPTURE\_ErrCode errorSelectType = OH\_AVScreenCapture\_GetCaptureTypeSelected(selections, selectType);
    OH\_AVSCREEN\_CAPTURE\_ErrCode errorDisplayId = OH\_AVScreenCapture\_GetDisplayIdSelected(selections, displayId);

    // Release the allocated memory after use.
    delete selectType, displayId;
}

// Call StartScreenCapture to start screen capture.
static napi\_value StartScreenCapture(napi\_env env, napi\_callback\_info info) {
    // Initialize the screen capture parameters and pass an OH\_AVScreenCaptureConfig struct.
    OH\_AVScreenCaptureConfig config;
    OH\_AudioCaptureInfo micCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH\_MIC
    };

    OH\_AudioCaptureInfo innerCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH\_ALL\_PLAYBACK
    };

    OH\_AudioEncInfo audioEncInfo = {
        .audioBitrate = 48000,
        .audioCodecformat = OH\_AudioCodecFormat::OH\_AAC\_LC
    };

    OH\_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = 768,
        .videoFrameHeight = 1280,
        .videoSource = OH\_VIDEO\_SOURCE\_SURFACE\_RGBA
    };

    OH\_VideoEncInfo videoEncInfo = {
        .videoCodec = OH\_VideoCodecFormat::OH\_H264,
        .videoBitrate = 2000000,
        .videoFrameRate = 30
    };

    OH\_AudioInfo audioInfo = {
        .micCapInfo = micCapInfo,
        .innerCapInfo = innerCapInfo,
        .audioEncInfo = audioEncInfo
    };

    OH\_VideoInfo videoInfo = {
        .videoCapInfo = videoCapInfo,
        .videoEncInfo = videoEncInfo
    };

    config = {
        .captureMode = OH\_CAPTURE\_HOME\_SCREEN,
        .dataType = OH\_CAPTURE\_FILE,
        .audioInfo = audioInfo,
        .videoInfo = videoInfo,
    };

    // Instantiate AVScreenCapture.
    capture = OH\_AVScreenCapture\_Create();

    OH\_RecorderInfo recorderInfo;
    const std::string SCREEN\_CAPTURE\_ROOT = "/data/storage/el2/base/files/";
    outputFd = open((SCREEN\_CAPTURE\_ROOT + "screen01.mp4").c\_str(), O\_RDWR | O\_CREAT, 0777);

    // If opening or creation fails, handle the failure and return the error information.
    if (outputFd == -1) {
        napi\_value errCode;
        napi\_create\_double(env, AV\_SCREEN\_CAPTURE\_ERR\_IO, &errCode);
        return errCode;
    }

    std::string fileUrl = "fd://" + std::to\_string(outputFd);
    recorderInfo.url = const\_cast<char \*>(fileUrl.c\_str());
    recorderInfo.fileFormat = OH\_ContainerFormatType::CFT\_MPEG\_4;
    config.recorderInfo = recorderInfo;

    // Set a callback to respond to state changes.
    OH\_AVScreenCapture\_SetStateCallback(capture, OnStateChange, nullptr);

    // (Optional) Set a callback for screen capture content changes.
    OH\_Rect\* area = nullptr;
    OH\_AVScreenCapture\_SetCaptureContentChangedCallback(capture, OnCaptureContentChanged, area);

    // (Optional) Set the privacy window masking mode.
    int value = 0;
    OH\_AVScreenCapture\_CaptureStrategy\* strategy = OH\_AVScreenCapture\_CreateCaptureStrategy();
    OH\_AVScreenCapture\_StrategyForPrivacyMaskMode(strategy, value);
    OH\_AVScreenCapture\_SetCaptureStrategy(capture, strategy);

    // (Optional) Set a callback to obtain the display ID. This operation must be performed before screen capture starts.
    OH\_AVScreenCapture\_SetDisplayCallback(capture, OnDisplaySelected, nullptr);

    // (Optional) Set a callback to handle user selection results on the manual confirmation UI. This operation must be performed before screen capture starts.
    OH\_AVScreenCapture\_SetSelectionCallback(capture, OnUserSelected, nullptr);

    // (Optional) Set the cursor display switch. This operation can be performed before or after screen capture starts.
    OH\_AVScreenCapture\_ShowCursor(capture, false);

    // Initialize AVScreenCapture.
    int32\_t retInit = OH\_AVScreenCapture\_Init(capture, config);

    // Optional (supported since API version 20) Set the coordinates and size of the area to capture. The example below creates a 100 px \* 100 px rectangle area starting at (0, 0). This API can also be set after screen capture starts.
    OH\_Rect\* region = new OH\_Rect;
    region->x = 0;
    region->y = 0;
    region->width = 100;
    region->height = 100;
    uint64\_t regionDisplayId = 0; // ID of the display where the rectangle area is located.
    OH\_AVScreenCapture\_SetCaptureArea(capture, regionDisplayId, region);
    
    // Release the allocated memory.
    delete region;

    // Start screen capture.
    int32\_t retStart = OH\_AVScreenCapture\_StartScreenRecording(capture);

    // If starting screen capture fails, handle the failure and return the error information.
    if (retStart != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
        napi\_value errCode;
        napi\_create\_double(env, retStart, &errCode);
        return errCode;
    }

    // Call StopScreenCapture to stop screen capture.
    
    // Return the call result. In the example, only a random number is returned.
    napi\_value code;
    napi\_create\_double(env, AV\_SCREEN\_CAPTURE\_ERR\_OK, &code);

    return code;
}

// Call StopScreenCapture to stop screen capture.
static napi\_value StopScreenCapture(napi\_env env, napi\_callback\_info info) {
    if (capture != nullptr) {
        // Stop screen capture.
        int32\_t retStop = OH\_AVScreenCapture\_StopScreenRecording(capture);

        // Close the file access.
        close(outputFd);

        // If stopping screen capture fails, handle the failure and return the error information.
        if (retStop != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
            napi\_value errCode;
            napi\_create\_double(env, retStop, &errCode);
            return errCode;
        }

        // Release the AVScreenCapture instance.
        int32\_t retRelease = OH\_AVScreenCapture\_Release(capture);

        // If releasing the AVScreenCapture instance fails, handle the failure and return the error information.
        if (retRelease != AV\_SCREEN\_CAPTURE\_ERR\_OK) {
            napi\_value errCode;
            napi\_create\_double(env, retRelease, &errCode);
            return errCode;
        }

        capture = nullptr;
    }

    // Return a success message.
    napi\_value code;
    napi\_create\_double(env, AV\_SCREEN\_CAPTURE\_ERR\_OK, &code);

    return code;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports) {
    napi\_property\_descriptor desc\[\] = {
        {"startScreenCapture", nullptr, StartScreenCapture, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"stopScreenCapture", nullptr, StopScreenCapture, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }
