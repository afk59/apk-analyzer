# Developing the ABR Capability

#### Service Process

The following figure shows the main ABR service process based on camera motion perception.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/bV-FDbcbRQuudg82TtPJpA/en-us_image_0000002423177560.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062051Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1622B81B05D38F3200AED41E15CE29B06713E929F8F9955E25E80CC5F3685848)

1.  A user enters a game scene suitable for the ABR capability.
2.  The game app calls the [HMS\_ABR\_CreateContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga8f785903a5382ff31baef78a3968f66a) API, specifying the graphics API type, to create an ABR context instance.
3.  The game app calls the [HMS\_ABR\_SetTargetFps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga6c613e02088d559b9dc1450fde15bc2a) API to initialize the ABR context instance and set the target frame rate. The ABR capability will perceive the GPU load status in real time based on the target frame rate.
4.  The game app calls the [HMS\_ABR\_SetScaleRange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga1001c6a7739d8ce57bf851986f121bf5) API to initialize the ABR context instance and set the buffer resolution factor range.
5.  The game app calls the [HMS\_ABR\_Activate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga463d8d5396bfd5f6ed800ddab616479a) API to activate the ABR context instance.
6.  The game app calls the [HMS\_ABR\_UpdateCameraData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga5b895e36d31e46f71d04aba78c8f3716) API, passing camera motion data, including the camera rotation and position information.
7.  The game app calls the [HMS\_ABR\_MarkFrameBuffer\_GLES](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga821fb33620312d3adba51d30254c1ef0) API to mark a buffer before rendering it.
8.  The game app executes buffer rendering.
9.  The game app draws the UI.
10.  The game app sends the frame for display.
11.  The user exits the game scene suitable for the ABR capability.
12.  The game app calls the [HMS\_ABR\_DestroyContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gaf3c03179b9bcf1b8475230cbbb0d877c) API to destroy the ABR context instance and release memory resources.

#### Development Procedure

The following describes an example of the implementation and API call of each step in the ABR service process based on camera motion perception.

## Configuring Project Information

Add the following configuration under **module** in the **src/main/module.json5** file:

"metadata": \[
  {
    "name": "GraphicsAccelerateKit\_ABR",
    "value": "true"
  }
\]

## Including a Header File

Include the Graphics Accelerate Kit ABR header file **abr\_gles.h**.

// Include the ABR header file **abr\_gles.h**.
#include <graphics\_game\_sdk/abr\_gles.h>
#include <GLES3/gl32.h>

## Compiling CMakeLists.txt

find\_library(
    # Sets the name of the path variable.
    abr-lib
    # Specifies the name of the NDK library that you want CMake to locate.
    libabr.so
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
    ${abr-lib} ${GLES-lib} ${hilog-lib}
)

## Performing ABR Initialization

When a surface is created for your app, the event callback function **Core::OnSurfaceCreated()** is triggered. Perform the following operations in this function: Create an ABR context instance, set ABR attributes, and activate the instance. The ABR context instance is used for managing the entire ABR lifecycle.

1.  Call the [HMS\_ABR\_CreateContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga8f785903a5382ff31baef78a3968f66a) API to create an ABR context instance and specify the graphics API type. If **nullptr** is returned, it indicates that the ABR context instance fails to be created or the current device does not support the ABR function.
    
    // Create an ABR context instance and specify the graphics API type.
    ABR\_Context \*context\_ = HMS\_ABR\_CreateContext(RENDER\_API\_GLES);
    if (context\_ == nullptr) {
          return false;
    }
    
2.  Call the [HMS\_ABR\_SetTargetFps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga6c613e02088d559b9dc1450fde15bc2a) API to initialize the ABR context instance and set the target frame rate of the ABR capability based on the target frame rate of the game.
    
    // Initialize the error code of ABR API calls.
    ABR\_ErrorCode errorCode = ABR\_SUCCESS;
    
    // Initialize the ABR context instance and set the target frame rate of the ABR capability. For example, if the target frame rate of a game is 120 FPS, set the target frame rate of the ABR capability to 120 FPS.
    errorCode = HMS\_ABR\_SetTargetFps(context\_, 120);
    if (errorCode != ABR\_SUCCESS) {
        return false;
    }
    
3.  Call the [HMS\_ABR\_SetScaleRange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga1001c6a7739d8ce57bf851986f121bf5) API to initialize the ABR context instance and set the buffer resolution factor range.
    
    // Initialize the ABR context instance and set a proper buffer resolution factor range based on the game resolution and image quality.
    // For example, set a factor of 0.5 to 1.0 times for adaptive buffer resolution adjustment.
    errorCode = HMS\_ABR\_SetScaleRange(context\_, 0.5f, 1.0f);
    if (errorCode != ABR\_SUCCESS) {
        return false;
    }
    
4.  Call the [HMS\_ABR\_Activate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga463d8d5396bfd5f6ed800ddab616479a) API to activate the ABR context instance.
    
    // Activate the ABR context instance.
    errorCode = HMS\_ABR\_Activate(context\_);
    if (errorCode != ABR\_SUCCESS) {
        return false;
    }
    

## Updating Camera Motion Data

In the frame loop, the ABR capability determines the buffer resolution factor based on the camera motion data obtained in real time.

Call the [HMS\_ABR\_UpdateCameraData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga5b895e36d31e46f71d04aba78c8f3716) API, passing camera motion data, including the camera rotation and position information.

// Camera motion data struct. Set the real-time camera motion data of each frame.
ABR\_CameraData cameraData;
// Position of each frame.
ABR\_Vector3 position\_;
// Camera rotation angle of each frame. The value range is \[0, 360\].
ABR\_Vector3 rotation\_;
cameraData.position = position\_;
cameraData.rotation = rotation\_;

// Update the camera motion data of each frame.
errorCode = HMS\_ABR\_UpdateCameraData(context\_, &cameraData);
if (errorCode != ABR\_SUCCESS) {
    return false;
}

## Performing Adaptive Rendering

In the frame loop, the ABR capability performs adaptive rendering on a marked buffer.

1.  Select a buffer with high shader cost and bind the buffer before rendering it.
    
    // Create a buffer object.
    GLuint fbo;
    glGenFramebuffers(1, &fbo);
    // Bind the buffer.
    glBindFramebuffer(GL\_FRAMEBUFFER, fbo);
    
2.  Call the [HMS\_ABR\_MarkFrameBuffer\_GLES](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#ga821fb33620312d3adba51d30254c1ef0) API to mark the buffer.
    
    // Call this API before buffer rendering. If the operation fails, buffer rendering will not be affected.
    errorCode = HMS\_ABR\_MarkFrameBuffer\_GLES(context\_);
    if (errorCode != ABR\_SUCCESS) {
        return false;
    }
    
3.  Execute the original rendering process of the buffer.

## Destroying an ABR Context Instance

When a surface is destroyed, the event callback function **Core::OnSurfaceDestroyed()** is triggered. Destroy an ABR context instance in this function.

Call the [HMS\_ABR\_DestroyContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_graphics_accelerate#gaf3c03179b9bcf1b8475230cbbb0d877c) API to destroy an ABR context instance and release memory resources.

// Destroy an ABR context instance and release memory resources.
ABR\_ErrorCode errorCode = HMS\_ABR\_DestroyContext(&context\_);
if (errorCode != ABR\_SUCCESS) {
     return false;
}
