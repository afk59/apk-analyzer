# Photo Capture (C/C++)

#### Overview

Photo capture is one of the important functions of the camera. The photo capture module is built on complex camera logic. To ensure the quality of photos taken by users, settings such as resolution, flash, focal length, photo quality, and rotation angle can be configured during intermediate steps.

There are currently two photo capture solutions for camera development: [deferred photo capture](../deferred-photo-delivery-c-c/document.md) and one-shot photo capture. **This section uses one-shot photo capture as an example.**

-   Deferred photo capture delivers low-quality images for thumbnail display, improving the perceived capture speed, while preserving high-quality images to ensure final output matches the system camera standard. This approach satisfies image processing algorithm requirements without blocking foreground capture speed, helping deliver competitive camera performance and a better user experience.
-   One-shot photo capture produces a single high-quality image after multi-frame fusion and multiple low-level algorithmic processing. As a result, Shot2See latency—the time from when the user taps the capture control to when a thumbnail appears in the thumbnail display area—is relatively long. One-shot photo capture also supports [quality-first strategy](#quality-first-strategy) via [high-performance photo capture](#high-performance-photo-capture), allowing you to optimize for either faster image output or higher image quality.

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
        libhilog\_ndk.z.so
        libnative\_buffer.so
        libohcamera.so
        libohimage.so
        libohfileuri.so
    )
    
3.  Create and open a camera device. For details, see steps 3 to 5 in [Device Input Management (C/C++)](../../mandatory-capabilities-for-camera-application-development-c-c/device-input-management-c-c/document.md).
    
4.  Select the output stream capability supported by the camera device and create a photo output stream.
    
    Call [OH\_CameraManager\_CreatePhotoOutputWithoutSurface()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createphotooutputwithoutsurface) to create a photo output stream.
    
    Camera\_ErrorCode NDKCamera::CreatePhotoOutputWithoutSurfaceId()
    {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePhotoOutputWithoutSurfaceId enter.");
        profile\_ = cameraOutputCapability\_->photoProfiles\[0\];
        Camera\_Profile\* profile = cameraOutputCapability\_->photoProfiles\[0\];
        profile->size.width = NUM\_1920;
        profile->size.height = NUM\_1080;
        profile\_ = profile;
        if (profile\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get photoProfiles failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreatePhotoOutputWithoutSurface(cameraManager\_, profile\_, &photoOutput\_);
        if (photoOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreatePhotoOutputWithoutSurfaceId failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
    // ...
        return ret\_;
    }
    
5.  Register a one-time photo capture callback, which is defined as **PhotoAvailable**. If your application requires rapid image display, use the deferred photo delivery callback, which is defined as [PhotoAssetAvailable](../deferred-photo-delivery-c-c/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/BnWeImoySROBvAeMu3jpTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB7D01A53A3040AA78375683D39D2D2BC4A6725FFC81D556F24F3B6954E76C5A)
    
    If the **PhotoAssetAvailable** callback has been registered and the **PhotoAvailable** callback is registered after the session starts, the stream will be restarted. In this case, only the **PhotoAssetAvailable** callback takes effect.
    
    Therefore, you are not advised to register both **PhotoAssetAvailable** and **PhotoAvailable**.
    
    **The development process (PhotoAvailable) is as follows:**
    
    -   Register the callback before the session commits the configuration.
        
    -   Obtain the image information from the callback, parse the buffer data, and perform custom service processing.
        
    -   Pass the processed buffer to the ArkTS side through the callback for image display or storage (using a security component).
        
    -   Unregister the callback when it is no longer required.
        
        // Save the buffer processing callback registered on the NAPI side.
        Camera\_ErrorCode NDKCamera::RegisterBufferCb(void \*cb)
        {
            OH\_LOG\_INFO(LOG\_APP, " RegisterBufferCb start");
            if (cb == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, " RegisterBufferCb invalid error");
                return CAMERA\_INVALID\_ARGUMENT;
            }
            g\_bufferCb = cb;
            return CAMERA\_OK;
        }
        
        static bool ProcessImageNative(OH\_ImageNative\* imageNative, uint32\_t\*\* components,
                                       OH\_NativeBuffer\*\* nativeBuffer, size\_t\* nativeBufferSize)
        {
            if (imageNative == nullptr || components == nullptr || nativeBuffer == nullptr || nativeBufferSize == nullptr) {
                return false;
            }
        
            Image\_Size size;
            Image\_ErrorCode imageErr = OH\_ImageNative\_GetImageSize(imageNative, &size);
            if (imageErr != IMAGE\_SUCCESS) {
                return false;
            }
        
            size\_t componentTypeSize = 0;
            imageErr = OH\_ImageNative\_GetComponentTypes(imageNative, nullptr, &componentTypeSize);
            if (imageErr != IMAGE\_SUCCESS || componentTypeSize == 0) {
                OH\_LOG\_ERROR(LOG\_APP, "GetComponentTypes failed: %{public}d, size: %{public}zu",
                    imageErr, componentTypeSize);
                return false;
            }
        
            if (componentTypeSize > (SIZE\_MAX / sizeof(uint32\_t))) {
                OH\_LOG\_ERROR(LOG\_APP, "componentTypeSize too large: %{public}zu", componentTypeSize);
                return false;
            }
        
            uint32\_t\* compArray = new (std::nothrow) uint32\_t\[componentTypeSize\];
            if (!compArray) {
                return false;
            }
        
            size\_t tempSize = componentTypeSize;
            imageErr = OH\_ImageNative\_GetComponentTypes(imageNative, &compArray, &tempSize);
            if (imageErr != IMAGE\_SUCCESS) {
                delete\[\] compArray;
                return false;
            }
            \*components = compArray;
        
            imageErr = OH\_ImageNative\_GetByteBuffer(imageNative, compArray\[0\], nativeBuffer);
            if (imageErr != IMAGE\_SUCCESS) {
                delete\[\] compArray;
                return false;
            }
        
            imageErr = OH\_ImageNative\_GetBufferSize(imageNative, compArray\[0\], nativeBufferSize);
            if (imageErr != IMAGE\_SUCCESS) {
                delete\[\] compArray;
                return false;
            }
        
            int32\_t rowStride = 0;
            int32\_t pixelStride = 0;
            OH\_ImageNative\_GetRowStride(imageNative, compArray\[0\], &rowStride);
            OH\_ImageNative\_GetPixelStride(imageNative, compArray\[0\], &pixelStride);
            OH\_LOG\_INFO(LOG\_APP, "Buffer size: %{public}zu, strides: %{public}d/%{public}d",
                \*nativeBufferSize, rowStride, pixelStride);
        
            return true;
        }
        
        
        static void CleanupResources(OH\_ImageNative\* imageNative, uint32\_t\* components,
                                     OH\_NativeBuffer\* nativeBuffer, void\* virAddr)
        {
            if (components) {
                delete\[\] components;
            }
        
            if (imageNative) {
                int32\_t ret = OH\_ImageNative\_Release(imageNative);
                if (ret != 0) {
                    OH\_LOG\_ERROR(LOG\_APP, "Release image failed: %{public}d", ret);
                }
            }
        
            if (nativeBuffer && virAddr) {
                int32\_t ret = OH\_NativeBuffer\_Unmap(nativeBuffer);
                if (ret != 0) {
                    OH\_LOG\_ERROR(LOG\_APP, "Unmap buffer failed: %{public}d", ret);
                }
            }
        }
        
        void OnPhotoAvailable(Camera\_PhotoOutput \*photoOutput, OH\_PhotoNative \*photo)
        {
            OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable start!");
        
            OH\_ImageNative \*imageNative = nullptr;
            Camera\_ErrorCode errCode = OH\_PhotoNative\_GetMainImage(photo, &imageNative);
            if (errCode != CAMERA\_OK || !imageNative) {
                OH\_LOG\_ERROR(LOG\_APP, "GetMainImage failed: %{public}d", errCode);
                return;
            }
        
            uint32\_t\* components = nullptr;
            OH\_NativeBuffer\* nativeBuffer = nullptr;
            size\_t nativeBufferSize = 0;
        
            if (!ProcessImageNative(imageNative, &components, &nativeBuffer, &nativeBufferSize)) {
                CleanupResources(imageNative, components, nullptr, nullptr);
                return;
            }
        
            void\* virAddr = nullptr;
            int32\_t ret = OH\_NativeBuffer\_Map(nativeBuffer, &virAddr);
            if (ret != 0 || !virAddr) {
                OH\_LOG\_ERROR(LOG\_APP, "Map buffer failed: %{public}d", ret);
                CleanupResources(imageNative, components, nativeBuffer, nullptr);
                return;
            }
        
            auto cb = (void (\*)(void \*, size\_t))(g\_bufferCb);
            if (cb && virAddr && nativeBufferSize > 0) {
                cb(virAddr, nativeBufferSize);
                OH\_LOG\_INFO(LOG\_APP, "Buffer callback called");
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "Invalid callback parameters");
            }
        
            CleanupResources(imageNative, components, nativeBuffer, virAddr);
        
            OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable end");
        }
        
        Camera\_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAvailableCallback(void)
        {
            OH\_LOG\_INFO(LOG\_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback start!");
            Camera\_ErrorCode ret = OH\_PhotoOutput\_RegisterPhotoAvailableCallback(photoOutput\_, OnPhotoAvailable);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback failed.");
            }
            OH\_LOG\_INFO(LOG\_APP, "NDKCamera::PhotoOutputRegisterPhotoAvailableCallback return with ret code: %{public}d!",
                ret\_);
            return ret;
        }
        
        // Unregister the PhotoAvailableCallback callback.
        Camera\_ErrorCode NDKCamera::PhotoOutputUnRegisterPhotoAvailableCallback()
        {
            OH\_LOG\_INFO(LOG\_APP, "PhotoOutputUnRegisterPhotoAvailableCallback start!");
            Camera\_ErrorCode ret = OH\_PhotoOutput\_UnregisterPhotoAvailableCallback(photoOutput\_, OnPhotoAvailable);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "PhotoOutputUnRegisterPhotoAvailableCallback failed.");
            }
            OH\_LOG\_INFO(LOG\_APP, "PhotoOutputUnRegisterPhotoAvailableCallback return with ret code: %{public}d!", ret);
            return ret;
        }
        
        Sample code for buffer processing at the NAPI layer:
        
        // Buffer callback at the NAPI layer.
        static void BufferCb(void\* buffer, size\_t size)
        {
            OH\_LOG\_INFO(LOG\_APP, "BufferCb size:%{public}zu", size);
            g\_size = size;
            napi\_value asyncResource = nullptr;
            napi\_value asyncResourceName = nullptr;
            napi\_async\_work work;
        
            if (size == 0 || size > SIZE\_MAX) {
                OH\_LOG\_ERROR(LOG\_APP, "BufferCb size is invalid");
                return;
            }
            void\* copyBuffer = malloc(size);
            if (copyBuffer == nullptr) {
                return;
            }
            OH\_LOG\_INFO(LOG\_APP, "BufferCb copyBuffer:%{public}p", copyBuffer);
            // Use std::memcpy to copy the content in the buffer to the copyBuffer.
            std::memcpy(copyBuffer, buffer, size);
            napi\_create\_string\_utf8(env\_, "BufferCb", NAPI\_AUTO\_LENGTH, &asyncResourceName);
            napi\_status status = napi\_create\_async\_work(
                env\_, asyncResource, asyncResourceName, \[\](napi\_env env, void\* copyBuffer) {},
                \[\](napi\_env env, napi\_status status, void\* copyBuffer) {
                    napi\_value retVal;
                    napi\_value callback = nullptr;
                    void\* data = nullptr;
                    napi\_value arrayBuffer = nullptr;
                    size\_t bufferSize = g\_size;
                    napi\_create\_arraybuffer(env, bufferSize, &data, &arrayBuffer);
                    std::memcpy(data, copyBuffer, bufferSize);
                    OH\_LOG\_INFO(LOG\_APP, "BufferCb g\_size: %{public}zu", g\_size);
                    napi\_get\_reference\_value(env, bufferCbRef\_, &callback);
                    if (callback) {
                        OH\_LOG\_INFO(LOG\_APP, "BufferCb callback is full");
                    } else {
                        OH\_LOG\_ERROR(LOG\_APP, "BufferCb callback is null");
                    }
                    // Call the buffer processing callback function at the ArkTS side to pass the image arrayBuffer for display or storage.
                    napi\_call\_function(env, nullptr, callback, 1, &arrayBuffer, &retVal);
                },
                copyBuffer, &work);
            // Error check: The memory is released when the asynchronous work fails to be created.
            if (status != napi\_ok) {
                OH\_LOG\_ERROR(LOG\_APP, "Failed to create async work");
                free(copyBuffer); // Release the allocated memory.
                return;
            }
            napi\_queue\_async\_work\_with\_qos(env\_, work, napi\_qos\_user\_initiated);
        }
        
6.  Create a photo session. For details, see [Camera Session Management (C/C++)](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md).
    
7.  (Optional) Set photo capture parameters.
    
    You can set camera parameters to adjust photo capture functions, including the flash, zoom ratio, and focal length.
    
    Camera\_ErrorCode NDKCamera::HasFlashFn(uint32\_t mode)
    {
        Camera\_FlashMode flashMode = static\_cast<Camera\_FlashMode>(mode);
        //Check the flash.
        bool hasFlash = false;
        Camera\_ErrorCode ret = OH\_CaptureSession\_HasFlash(captureSession\_, &hasFlash);
        if (captureSession\_ == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_HasFlash failed.");
        }
        if (hasFlash) {
            OH\_LOG\_INFO(LOG\_APP, "hasFlash success-----");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "hasFlash fail-----");
        }
    
        //Check whether the flash mode is supported.
        bool isSupported = false;
        ret = OH\_CaptureSession\_IsFlashModeSupported(captureSession\_, flashMode, &isSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_IsFlashModeSupported failed.");
        }
        if (isSupported) {
            OH\_LOG\_INFO(LOG\_APP, "isFlashModeSupported success-----");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "isFlashModeSupported fail-----");
        }
    
        // Set the flash mode.
        ret = OH\_CaptureSession\_SetFlashMode(captureSession\_, flashMode);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetFlashMode success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetFlashMode failed. %{public}d ", ret);
        }
    
        // Obtain the flash mode in use.
        ret = OH\_CaptureSession\_GetFlashMode(captureSession\_, &flashMode);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetFlashMode success. flashMode: %{public}d ", flashMode);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetFlashMode failed. %d ", ret);
        }
        return ret;
    }
    
    // Focus mode.
    Camera\_ErrorCode NDKCamera::IsFocusModeSupported(uint32\_t mode)
    {
        Camera\_FocusMode focusMode = static\_cast<Camera\_FocusMode>(mode);
        ret\_ = OH\_CaptureSession\_IsFocusModeSupported(captureSession\_, focusMode, &isFocusModeSupported\_);
        if (&isFocusModeSupported\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "IsFocusModeSupported failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret\_;
    }
    
    Camera\_ErrorCode NDKCamera::IsFocusMode(uint32\_t mode)
    {
        OH\_LOG\_INFO(LOG\_APP, "IsFocusMode start.");
        Camera\_FocusMode focusMode = static\_cast<Camera\_FocusMode>(mode);
        ret\_ = OH\_CaptureSession\_IsFocusModeSupported(captureSession\_, focusMode, &isFocusModeSupported\_);
        if (&isFocusModeSupported\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "IsFocusModeSupported failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CaptureSession\_SetFocusMode(captureSession\_, focusMode);
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "SetFocusMode failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CaptureSession\_GetFocusMode(captureSession\_, &focusMode);
        if (&focusMode == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "GetFocusMode failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        OH\_LOG\_INFO(LOG\_APP, "IsFocusMode end.");
        return ret\_;
    }
    
    Camera\_ErrorCode NDKCamera::setZoomRatioFn(uint32\_t zoomRatio)
    {
        float zoom = float(zoomRatio);
        // Obtain the supported zoom ratio range.
        float minZoom;
        float maxZoom;
        Camera\_ErrorCode ret = OH\_CaptureSession\_GetZoomRatioRange(captureSession\_, &minZoom, &maxZoom);
        if (captureSession\_ == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatioRange failed.");
        } else {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
                minZoom, maxZoom);
        }
    
        // Set the zoom ratio.
        ret = OH\_CaptureSession\_SetZoomRatio(captureSession\_, zoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio failed. %{public}d ", ret);
        }
    
        // Obtain the zoom ratio in use.
        ret = OH\_CaptureSession\_GetZoomRatio(captureSession\_, &zoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio success. zoom: %{public}f ", zoom);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio failed. %{public}d ", ret);
        }
        return ret;
    }
    
8.  Trigger photo capture.
    
    Call [OH\_PhotoOutput\_Capture\_WithCaptureSetting()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_capture_withcapturesetting) to trigger photo capture.
    
    Camera\_ErrorCode NDKCamera::TakePicture(int32\_t degree)
    {
        Camera\_ErrorCode ret = CAMERA\_OK;
        Camera\_ImageRotation imageRotation;
        bool isMirSupported;
        OH\_PhotoOutput\_IsMirrorSupported(photoOutput\_, &isMirSupported);
        OH\_PhotoOutput\_GetPhotoRotation(photoOutput\_, degree, &imageRotation);
    
        Camera\_PhotoCaptureSetting curPhotoSetting = {
            quality : QUALITY\_LEVEL\_HIGH,
            rotation : imageRotation,
            mirror : isMirSupported
        };
        ret = OH\_PhotoOutput\_Capture\_WithCaptureSetting(photoOutput\_, curPhotoSetting);
        OH\_LOG\_INFO(LOG\_APP, "TakePicture get quality %{public}d, rotation %{public}d, mirror %{public}d",
            curPhotoSetting.quality, curPhotoSetting.rotation, curPhotoSetting.mirror);
        OH\_LOG\_INFO(LOG\_APP, "TakePicture ret = %{public}d.", ret);
        return ret;
    }
    

#### High-Performance Photo Capture

High-performance photo capture is supported starting from API version 21. This feature allows you to set an explicit [quality-first strategy](#quality-first-strategy) for one-shot photo capture.

User experience of one-shot photo capture is primarily measured by image output speed and final image quality. To meet differentiated requirements across scenarios, the emphasis on these two metrics varies. For example, street photography requires fast capture of fleeting moments, while landscape or portrait photography prioritizes optimal image quality.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/h2P4JoYfRX-xHnf7nxv0pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57B27A8D608EDA449D291841D8B0BA69E5C6E0D757AF588FFBE197B6D75E3EEC)

Quality-first strategy is supported only for one-shot photo capture. Any such settings configured for deferred photo capture will not take effect.

## Quality-First Strategy

For one-shot photo capture, two quality-first strategies are supported, each mapped to a distinct [Camera\_PhotoQualityPrioritization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_photoqualityprioritization) enumeration value:

-   [CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_SPEED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_photoqualityprioritization): prioritizes speed by reducing image quality to accelerate capture. This is the **default strategy** for one-shot photo capture if no explicit quality-first strategy is configured.
-   [CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_HIGH\_QUALITY](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_photoqualityprioritization): prioritizes quality by allowing longer processing time to produce higher-quality images.

## How to Correctly Set a Quality-First Strategy

To properly set a quality-first strategy for one-shot photo capture, the high-performance photo capture feature provides the following two APIs:

-   [OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_isphotoqualityprioritizationsupported): queries whether the current device supports a specified quality-first strategy. Returns **true** if supported, **false** if not. You must verify support for the target strategy on the current device before configuration.
-   [OH\_PhotoOutput\_SetPhotoQualityPrioritization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_setphotoqualityprioritization): The core API for setting a quality-first strategy. Use this API to configure the desired strategy and enable high-performance photo capture.

## How to Develop

APIs related to high-performance photo capture must be called during the [camera session management (C/C++)](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md) workflow.

The specific call timing is as follows:

-   Call the following APIs after the completion of [OH\_CaptureSession\_CommitConfig()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) in the enablement step of the [camera session management (C/C++)](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md) workflow.
    
    Camera\_ErrorCode StartSession(Camera\_CaptureSession\* captureSession, Camera\_Input\* cameraInput,
      Camera\_PreviewOutput\* previewOutput, Camera\_PhotoOutput\* photoOutput)
    {
      // Add the camera input stream to the session.
      Camera\_ErrorCode ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
        return ret;
      }
    
      // Add the preview output stream to the session.
      ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
        return ret;
      }
    
      // Add the photo output stream to the session.
      ret = OH\_CaptureSession\_AddPhotoOutput(captureSession, photoOutput);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPhotoOutput failed.");
        return ret;
      }
    
      // Commit the session configuration.
      ret = OH\_CaptureSession\_CommitConfig(captureSession);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
        return ret;
      }
    
      // Start the session.
      ret = OH\_CaptureSession\_Start(captureSession);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
      }
    
      SetHighQualityPhotoQualityPrioritization(photoOutput);
      return ret;
    }
    
    void SetHighQualityPhotoQualityPrioritization(Camera\_PhotoOutput\* photoOutput)
    {
      Camera\_PhotoQualityPrioritization quality = Camera\_PhotoQualityPrioritization::CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_HIGH\_QUALITY;
      bool isSupported = false;
      Camera\_ErrorCode ret = OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
      if (isSupported) {
        ret = OH\_PhotoOutput\_SetPhotoQualityPrioritization(photoOutput, quality);
        if (ret != 0) {
          OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_SetPhotoQualityPrioritization failed.");
        }
      } else {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported not supported.");
      }
    }
    
-   Call the following APIs before [OH\_CaptureSession\_CommitConfig()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) in the enablement step of the [camera session management (C/C++)](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md) workflow.
    
    Camera\_ErrorCode StartSession(Camera\_CaptureSession\* captureSession, Camera\_Input\* cameraInput,
      Camera\_PreviewOutput\* previewOutput, Camera\_PhotoOutput\* photoOutput)
    {
      // Add the camera input stream to the session.
      Camera\_ErrorCode ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
        return ret;
      }
    
      // Add the preview output stream to the session.
      ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
        return ret;
      }
    
      // Add the photo output stream to the session.
      ret = OH\_CaptureSession\_AddPhotoOutput(captureSession, photoOutput);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPhotoOutput failed.");
        return ret;
      }
    
      SetHighQualityPhotoQualityPrioritization(photoOutput);
      
      // Commit the session configuration.
      ret = OH\_CaptureSession\_CommitConfig(captureSession);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
        return ret;
      }
    
      // Start the session.
      ret = OH\_CaptureSession\_Start(captureSession);
      if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
      }
    
      return ret;
    }
    
    void SetHighQualityPhotoQualityPrioritization(Camera\_PhotoOutput\* photoOutput)
    {
      Camera\_PhotoQualityPrioritization quality = Camera\_PhotoQualityPrioritization::CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_HIGH\_QUALITY;
      bool isSupported = false;
      Camera\_ErrorCode ret = OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
      if (isSupported) {
        ret = OH\_PhotoOutput\_SetPhotoQualityPrioritization(photoOutput, quality);
        if (ret != 0) {
          OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_SetPhotoQualityPrioritization failed.");
        }
      } else {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported not supported.");
      }
    }
    

#### Status Listening

During camera application development, you can listen for the status of the photo output stream, including the start of the photo stream, the start and end of the photo frame, and the errors of the photo output stream.

-   Register the **'onFrameStart'** event to listen for photo capture start events. This event can be registered when a PhotoOutput instance is created and is triggered when the bottom layer starts exposure for photo capture for the first time. The capture ID is returned.
    
    // PhotoOutput Callback
    void PhotoOutputOnFrameStart(Camera\_PhotoOutput \*photoOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutputOnFrameStart");
    }
    
    void PhotoOutputOnFrameShutter(Camera\_PhotoOutput \*photoOutput, Camera\_FrameShutterInfo \*info)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutputOnFrameShutter");
    }
    
-   Register the **'onFrameEnd'** event to listen for photo capture end events. This event can be registered when a PhotoOutput instance is created.
    
    void PhotoOutputOnFrameEnd(Camera\_PhotoOutput \*photoOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutput frameCount = %{public}d", frameCount);
    }
    
-   Register the **'onError'** event to listen for photo output errors. The callback function returns an error code when an API is incorrectly used. For details about the error code types, see [Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    void PhotoOutputOnError(Camera\_PhotoOutput \*photoOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "PhotoOutput errorCode = %{public}d", errorCode);
    }
    
    PhotoOutput\_Callbacks \*NDKCamera::GetPhotoOutputListener(void)
    {
        static PhotoOutput\_Callbacks photoOutputListener = {
            .onFrameStart = PhotoOutputOnFrameStart,
            .onFrameShutter = PhotoOutputOnFrameShutter,
            .onFrameEnd = PhotoOutputOnFrameEnd,
            .onError = PhotoOutputOnError
        };
        return &photoOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::PhotoOutputRegisterCallback(void)
    {
        ret\_ = OH\_PhotoOutput\_RegisterCallback(photoOutput\_, GetPhotoOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
