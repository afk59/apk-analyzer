# Developing the OpenGTX Capability

#### Overview

OpenGTX is an open entry of GPU Turbo X. It enables the LTPO game acceleration solution to achieve a dynamic frame rate or refresh rate based on key information provided by game apps. It can help you create an ultimate game experience with high image quality, high smoothness, and low power consumption. The LTPO technology can dynamically adjust the frame rate or refresh rate of a game and the SoC/DDR frequency of a device based on the game rendering status, game scene, device status, and other key information perceived in real time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/EYL8SpQ_SO-WSethLpj9tA/en-us_image_0000002385317998.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062051Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89C3E4E59D2C8F85993310F6C175E4014F4DCD7A8854062C9EB473C73FB0CD1B "Click to enlarge")

#### Service Process

The following figure shows the main LTPO service process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/dZRB33LhQ9CS56XGzk17Ug/en-us_image_0000002503192951.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062051Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1A21FD137B793D3C0EC4EA8F0031B6CA71755BC019BB736FB98EBEB55D043E3)

1.  A user enters a game.
2.  The game app calls the [HMS\_OpenGTX\_CreateContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga94aadbb64ffb5382a4661790c040f1c3) API to create an OpenGTX context instance.
3.  The game app calls the [HMS\_OpenGTX\_SetConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gaaa09a16f113a0a9e0014b495ff961b6e) API to set the instance attributes, including the LTPO mode, target frame rate, package name, game type, resolution, and game key threads.
4.  The game app calls the [HMS\_OpenGTX\_Activate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga67e6cc5b491539c5e219f9e9ef15abca) API to activate the OpenGTX context instance.
5.  The game app calls the [HMS\_OpenGTX\_DispatchGameSceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gafd01b1b2726f10b10968cdcd73da632f) API upon game scene switchover to send game scene information, including the scene type, specified frame rate, frame rate range, and current resolution.
6.  The game app calls the [HMS\_OpenGTX\_DispatchFrameRenderInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga0c0b0034e4a6337e509888b2a9611489) API before the rendering of each frame to send game frame rendering information, including the position and Euler angle of the main camera.
7.  If the network latency level changes before each frame is rendered, the game app calls the [HMS\_OpenGTX\_DispatchNetworkInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gad7a6544a832f28ef068df580ac8a1b78) API to send the game's network information, including the server IP address and network latency.
8.  The game app draws a frame.
9.  The game app sends the frame for display.
10.  At the end of each frame, the OpenGTX notifies the user device of the frame rate and SoC/DDR frequency to be used.
11.  The user exits the game.
12.  The game app calls the [HMS\_OpenGTX\_DestroyContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga0b757b487acf42e92b06178e159b03ac) API to destroy the OpenGTX context instance and release memory resources.

#### Development Procedure

The following describes an example of the implementation and API call of each step in the OpenGTX service process.

## Configuring Project Information

Add the following configuration under **module** in the **src/main/module.json5** file:

"metadata": \[
  {
    "name": "GraphicsAccelerateKit\_LTPO",
    "value": "true"
  }
\]

## Including a Header File

Include the Graphics Accelerate Kit OpenGTX header file **opengtx\_base.h**.

// Include the OpenGTX header file **opengtx\_base.h**.
#include <graphics\_game\_sdk/opengtx\_base.h>

## Compiling CMakeLists.txt

find\_library(
    # Sets the name of the path variable.
    opengtx-lib
    # Specifies the name of the NDK library that you want CMake to locate.
    libopengtx.so
)
find\_library(
    # Sets the name of the path variable.
    GLES-lib
    # Specifies the name of the NDK library that you want CMake to locate.
    GLESv3
)
find\_library(
    # Sets the name of the path variable.
    hilog-lib
    # Specifies the name of the NDK library that you want CMake to locate.
    hilog\_ndk.z
)

target\_link\_libraries(entry PUBLIC
    ${opengtx-lib} ${GLES-lib} ${hilog-lib}
)

## Performing OpenGTX Initialization

When a surface is created for your app, the event callback function **Core::OnSurfaceCreated()** is triggered. Perform the following operations in this function: Create an OpenGTX context instance, set OpenGTX attributes, and activate the instance. The OpenGTX context instance is used for managing the entire OpenGTX lifecycle.

1.  Call the [HMS\_OpenGTX\_CreateContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga94aadbb64ffb5382a4661790c040f1c3) API to create an OpenGTX context instance. If **nullptr** is returned, it indicates that the OpenGTX context instance fails to be created or the current device does not support the OpenGTX function.
    
    // Create an OpenGTX context instance.
    OpenGTX\_Context \*context\_ = HMS\_OpenGTX\_CreateContext(nullptr);
    if (context\_ == nullptr) {
        return false;
    }
    
2.  Call the [HMS\_OpenGTX\_SetConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gaaa09a16f113a0a9e0014b495ff961b6e) API to set the instance attributes, including the LTPO mode, target frame rate, package name, game type, resolution, and game key threads.
    
    // Initialize the error code of OpenGTX API calls.
    OpenGTX\_ErrorCode errorCode = OPENGTX\_SUCCESS;
    // Struct for setting OpenGTX attributes.
    OpenGTX\_ConfigDescription config;
    // LTPO mode.
    config.mode = ADAPTIVE\_MODE;
    // Target frame rate of the game.
    config.targetFPS = 120;
    // Game package name.
    config.packageName = (char\*)"OpenGTX";
    // Game version.
    config.appVersion = (char\*)"1.1.0";
    // Engine type.
    config.engineType = UNREAL;
    // Engine version.
    config.engineVersion = (char\*)"4.26.2";
    // Game type.
    config.gameType = RPG;
    // Highest image quality level of the game.
    config.pictureQualityMaxLevel = HD;
    // Maximum resolution of the game.
    config.resolutionMaxValue = OpenGTX\_ResolutionValue { 1280, 720};
    // Game logic thread.
    config.gameMainThreadId = 11;
    // Game rendering thread.
    config.gameRenderThreadId = 11;
    // Other key threads for game running.
    config.gameKeyThreadIds\[0\] = 0;
    config.gameKeyThreadIds\[1\] = 0;
    config.gameKeyThreadIds\[2\] = 0;
    config.gameKeyThreadIds\[3\] = 0;
    config.gameKeyThreadIds\[4\] = 0;
    // Indicates whether the game graphics API is Vulkan.
    config.vulkanSupport = false;
    // Initialize the OpenGTX context instance and set OpenGTX attributes.
    errorCode = HMS\_OpenGTX\_SetConfiguration(context\_, &config);
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
    
3.  Call the [HMS\_OpenGTX\_Activate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga67e6cc5b491539c5e219f9e9ef15abca) API to activate the OpenGTX context instance.
    
    // Activate the OpenGTX context instance.
    errorCode = HMS\_OpenGTX\_Activate(context\_);
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
    
4.  Call the [HMS\_OpenGTX\_Deactivate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gaa741745687d067180d27d3be30db7422) API to deactivate the OpenGTX context instance. (Call this API when you need to disable the OpenGTX function. After the deactivation, calling APIs such as [HMS\_OpenGTX\_DispatchGameSceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gafd01b1b2726f10b10968cdcd73da632f) will not work.)
    
    // Deactivate the OpenGTX context instance.
    errorCode = HMS\_OpenGTX\_Deactivate(context\_);
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
    

## Updating OpenGTX Key Information

1.  Call the [HMS\_OpenGTX\_DispatchGameSceneInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gafd01b1b2726f10b10968cdcd73da632f) API upon game scene switchover to send game scene information, including the scene type, specified frame rate, frame rate range, and current resolution.
    
    // Struct of the OpenGTX game scene information.
    OpenGTX\_GameSceneInfo gameSceneInfo;
    // Game scene type ID.
    gameSceneInfo.sceneID = OTHERS\_SCENE;
    // Game scene description.
    gameSceneInfo.description = (char\*)"Other scenes";
    // Recommended frame rate for a game scene.
    gameSceneInfo.recommendFPS = 60;
    // Minimum frame rate for a game scene.
    gameSceneInfo.minFPS = 30;
    // Maximum frame rate for a game scene.
    gameSceneInfo.maxFPS = 90;
    // Screen resolution height.
    gameSceneInfo.resolutionCurValue.height = 360;
    // Screen resolution width.
    gameSceneInfo.resolutionCurValue.width = 7680;
    // OpenGTX receives game scene information.
    errorCode = HMS\_OpenGTX\_DispatchGameSceneInfo(context\_, &gameSceneInfo); 
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
    
2.  Call the [HMS\_OpenGTX\_DispatchFrameRenderInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga0c0b0034e4a6337e509888b2a9611489) API before the rendering of each frame to send game frame rendering information, including the position and Euler angle of the main camera.
    
    // Struct of the OpenGTX game frame rendering information.
    OpenGTX\_FrameRenderInfo frameRenderInfo;
    // Position of the main camera.
    frameRenderInfo.mainCameraPosition = { 0.0f, 0.0f, 0.0f };
    // Euler angle of the main camera.
    frameRenderInfo.mainCameraRotate = { 0.0f, 0.0f, 0.0f };
    // OpenGTX receives game frame rendering information.
    errorCode = HMS\_OpenGTX\_DispatchFrameRenderInfo(context\_, &frameRenderInfo);
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
    
3.  Call the [HMS\_OpenGTX\_DispatchNetworkInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gad7a6544a832f28ef068df580ac8a1b78) API to send the game's network information before each frame is rendered if the network latency level changes. The information includes the server IP address and network latency.
    
    // Struct of the OpenGTX game network information.
    OpenGTX\_NetworkInfo networkInfo;
    // Struct of the OpenGTX game network latency.
    OpenGTX\_NetworkLatency networkLatency;
    // Total network latency.
    networkLatency.total = 50;
    // Uplink network latency.
    networkLatency.up = 10;
    // Downlink network latency.
    networkLatency.down = 40;
    // Game network latency.
    networkInfo.networkLatency = networkLatency;
    // Game server IP address.
    networkInfo.networkServerIP = (char\*)"10.10.10.10";
    // OpenGTX receives game network information.
    errorCode = HMS\_OpenGTX\_DispatchNetworkInfo(context\_, &networkInfo); 
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
    

## Destroying an OpenGTX Context Instance

When a surface is destroyed, the event callback function **Core::OnSurfaceDestroyed()** is triggered. Destroy an OpenGTX context instance in this function.

1.  Call the [HMS\_OpenGTX\_DestroyContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga0b757b487acf42e92b06178e159b03ac) API to destroy an OpenGTX context instance and release memory resources.
    
    // Destroy an OpenGTX context instance and release memory resources.
    errorCode = HMS\_OpenGTX\_DestroyContext(&context\_);
    if (errorCode != OPENGTX\_SUCCESS) {
        return false;
    }
