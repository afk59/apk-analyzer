# Capturing the Specified Area on a Screen

#### Basic Concepts

Starting from API version 20, you can capture a specified rectangular area of the screen during recording. This feature enhances the existing screen capture capability by allowing you to select a specific area to record. You can define this area by providing a screen capture ID (**displayId**) and the target capture area (**area**).

Before implementing this feature, familiarize yourself with the following concepts:

-   Screen capture ID (**displayId**): ID of the screen where rectangular area capture will be performed.
-   Target capture area (**area**): coordinates and dimensions of the region to be captured, including the starting point (x, y) and the width and height of the rectangular area.

#### When to Use

This feature is particularly useful in scenarios such as:

-   **Online education**: When teachers present various materials on a large screen, selectively capturing a specific rectangular area helps minimize distractions, allowing students to focus better on the core content.
-   **Game streaming**: Players can capture only the game window during live streams or recordings, keeping the audience focused purely on the gameplay.

#### How to Develop

**Linking Dynamic Libraries in the CMake Script**

target\_link\_libraries(sample PUBLIC libnative\_avscreen\_capture.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/5JttnOeSRJqfd98XNc_pKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D47740305F8697B51ABE8E34843851AB271097D56462E9B7F6BC587765A86D3)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

**Adding Header Files**

#include "napi/native\_api.h"
#include <multimedia/player\_framework/native\_avscreen\_capture.h>
#include <multimedia/player\_framework/native\_avscreen\_capture\_base.h>
#include <multimedia/player\_framework/native\_avscreen\_capture\_errors.h>
#include <fcntl.h>
#include <string>

Call [OH\_AVScreenCapture\_SetCaptureArea()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_setcapturearea) to specify the rectangular area you want to capture.

In the code snippet below, the following variables are used:

-   **capture**: pointer to an [OH\_AVScreenCapture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture) instance.
-   **displayId**: ID of the screen where the capture area is located.
-   **area**: coordinates and width and height of the capture area. The type is OH\_Rect, including member variables **x**, **y**, **width**, and **height**.
    -   **x** and **y** indicate the horizontal and vertical coordinates of the start point of the rectangular area, respectively.
    -   **width** and **height** indicate the width and height of the rectangular area, respectively.
    -   Multiple parameters are separated by semicolons (;). All parameters are integers.
    -   Before using, ensure that the input parameters are valid and avoid negative coordinates, width, and height.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/LaPzsubPSI6flgSLMgHWmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4BB674A0CE9D4C658553112C3894696BD6828D4BDD8E630D15FCBD67FB9975B)

**Capture area restrictions**:

-   Security layers cannot be captured.
-   Capturing across multiple screens is not supported.

**Changing the capture area**: The capture area can be updated while recording is in progress.

**Error handling**: If setting a new area fails, the system continues using the previous valid area. Implement proper error handling to ensure the expected area is used.

**Parameter requirements**: Coordinates, width, and height must be non-negative integers, and the capture area must remain within a single screen.

struct OH\_AVScreenCapture \*capture = OH\_AVScreenCapture\_Create();
// Initialize the screen capture parameters and pass in an OH\_AVScreenRecorderConfig struct.
OH\_AudioCaptureInfo miccapinfo = {.audioSampleRate = 16000, .audioChannels = 2, .audioSource = OH\_MIC};
OH\_VideoCaptureInfo videocapinfo = {
    .videoFrameWidth = 768, .videoFrameHeight = 1280, .videoSource = OH\_VIDEO\_SOURCE\_SURFACE\_RGBA};
OH\_AudioInfo audioinfo = {
    .micCapInfo = miccapinfo,
};
OH\_VideoInfo videoinfo = {.videoCapInfo = videocapinfo};
OH\_AVScreenCaptureConfig config = {.captureMode = OH\_CAPTURE\_HOME\_SCREEN,
                                   .dataType = OH\_ORIGINAL\_STREAM,
                                   .audioInfo = audioinfo,
                                   .videoInfo = videoinfo};
OH\_AVScreenCapture\_Init(capture, config);
// 1. (Optional) Set the coordinates and dimensions of the capture area. For example, the following creates a 100\*100 rectangular area starting at (0, 0).
OH\_Rect\* region = new OH\_Rect;
region->x = 0;
region->y = 0;
region->width = 100;
region->height = 100;
// 2. Set the ID of the display where the rectangular area is located.
uint64\_t regionDisplayId = 0;
OH\_AVScreenCapture\_SetCaptureArea(capture, regionDisplayId, region);

// Start screen capture.
OH\_AVScreenCapture\_StartScreenCapture(capture);
