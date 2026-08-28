# Deferred Photo Delivery (C/C++)

As an important feature of the camera, deferred photo delivery enables the system, after receiving a photo capture task from an application, to report images of different quality levels in multiple phases.

-   In the first phase, the system promptly delivers an image that has undergone lightweight processing, offering a balance between reduced quality and swift image availability. The application receives a PhotoAsset object through the callback. Through this object, the application can call the media library APIs to read the image or flush the image to the disk.
-   In the second phase, the camera framework enhances the image to achieve full quality, either in response to the application's request for higher quality or when the system is not busy. The enhanced image is then sent back to the media library to replace the previously provided one.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK, which provides camera-related properties and methods.
    
    #include <cstdint>
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
    #include "common/log\_common.h"
    
    #include "multimedia/image\_framework/image/image\_native.h"
    #include "multimedia/image\_framework/image/image\_source\_native.h"
    #include "multimedia/image\_framework/image/image\_packer\_native.h"
    #include "multimedia/media\_library/media\_access\_helper\_capi.h"
    #include "multimedia/media\_library/media\_asset\_base\_capi.h"
    #include "multimedia/media\_library/media\_asset\_capi.h"
    #include "multimedia/media\_library/media\_asset\_change\_request\_capi.h"
    #include "multimedia/media\_library/media\_asset\_manager\_capi.h"
    #include "multimedia/media\_library/moving\_photo\_capi.h"
    #include "ohcamera/photo\_native.h"
    #include <window\_manager/oh\_display\_info.h>
    #include <window\_manager/oh\_display\_manager.h>
    
2.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libhilog\_ndk.z.so
        libohcamera.so
        libimage\_source.so
        libmedia\_asset\_manager.so
        libimage\_packer.so
    )
    
3.  Initialize the camera and trigger photo capture. For details, see [Photo Capture (C/C++)](../photo-capture-c-c/document.md).
    
4.  Register a deferred photo delivery callback, which is defined as **PhotoAssetAvailable**. Compared with one-time photo capture, only the callback registered is different.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/CKxe_s2LR92zvPeY0MJYag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D5F6846387295DD25B2F4B9889E17C8A765700071D091FCB828E141F6BF8C1C)
    
    If the **PhotoAssetAvailable** callback has been registered and the **PhotoAvailable** callback is registered after the session starts, the stream will be restarted. In this case, only the **PhotoAssetAvailable** callback takes effect.
    
    Therefore, you are not advised to register both **PhotoAssetAvailable** and **PhotoAvailable**.
    
    Register **PhotoAssetAvailableCallback** to receive images delivered in both phases.
    
    The development process is as follows:
    
    -   Register the callback before the session commits the configuration.
    -   Obtain a media asset through the callback.
    -   Through the media asset, either save the images or request images and after service processing, save them through a buffer or display them. For details, see step 5 in [Photo Capture (C/C++)](../photo-capture-c-c/document.md).
    -   Unregister the callback when it is no longer required.
    
    // Deferred phot delivery callback.
    void onPhotoAssetAvailable(Camera\_PhotoOutput \*photoOutput, OH\_MediaAsset \*mediaAsset)
    {
        if (mediaAsset == nullptr) {
            DRAWING\_LOGI("onPhotoAssetAvailable mediaAsset is nullptr !");
            return;
        }
        DRAWING\_LOGD("onPhotoAssetAvailable start!");
        NDKCamera::MediaAssetRelease();
        g\_mediaAsset = mediaAsset;
        NDKCamera::MediaAssetGetUri(mediaAsset);
        NDKCamera::MediaAssetGetDisplayName(mediaAsset);
        NDKCamera::MediaAssetGetSize(mediaAsset);
        NDKCamera::MediaAssetGetDateModifiedMs(mediaAsset);
        NDKCamera::MediaAssetGetWidth(mediaAsset);
        NDKCamera::MediaAssetGetHeight(mediaAsset);
        NDKCamera::MediaAssetGetOrientation(mediaAsset);
        NDKCamera::MediaAssetManagerCreate();
        NDKCamera::MediaAssetChangeRequest(mediaAsset);
        DRAWING\_LOGD("onPhotoAssetAvailable finish!");
        return;
    }
    
    // Register the PhotoAssetAvailableCallback callback.
    Camera\_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback(void)
    {
        DRAWING\_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback start!");
        MediaAssetManagerCreate();
        ret\_ = OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback(photoOutput\_, onPhotoAssetAvailable);
        if (ret\_ != CAMERA\_OK) {
            DRAWING\_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback failed.");
        }
        DRAWING\_LOGD(
            "NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback return with ret code: %{public}d!",
            ret\_);
        return ret\_;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetChangeRequest(OH\_MediaAsset \*mediaAsset)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequest start!");
        MediaAssetChangeRequestCreate(mediaAsset);
        MediaAssetManagerRequestImage(mediaAsset);
        DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequest finish!");
        return MEDIA\_LIBRARY\_OK;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetChangeRequestCreate(OH\_MediaAsset \*mediaAsset)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequestCreate start!");
        g\_changeRequest = OH\_MediaAssetChangeRequest\_Create(mediaAsset);
        if (g\_changeRequest == nullptr) {
            DRAWING\_LOGD("NDKCamera::MediaAssetChangeRequestCreate failed.");
        }
        return MEDIA\_LIBRARY\_OK;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetManagerCreate(void)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetManagerCreate start!");
        mediaAssetManager = OH\_MediaAssetManager\_Create();
        if (mediaAssetManager == nullptr) {
            DRAWING\_LOGD("NDKCamera::MediaAssetManagerCreate failed.");
        }
        return MEDIA\_LIBRARY\_OK;
    }
    
    void OnRequsetImageDataPreparedWithDetails(MediaLibrary\_ErrorCode result, MediaLibrary\_RequestId requestId,
        MediaLibrary\_MediaQuality mediaQuality, MediaLibrary\_MediaContentType type, OH\_ImageSourceNative \*imageSourceNative)
    {
        auto cb = (void (\*)(char \*))(g\_requestImageCallback);
        auto qCb = (void (\*)(char \*))(g\_requestImageQualityCallback);
        DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails start!");
        if (mediaQuality == MediaLibrary\_MediaQuality::MEDIA\_LIBRARY\_QUALITY\_FAST) {
            DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails into fast quality mode!");
            g\_mediaQualityCb = "fast";
            qCb(g\_mediaQualityCb);
        } else {
            DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails into high quality mode!");
            g\_mediaQualityCb = "high";
            qCb(g\_mediaQualityCb);
        }
        DRAWING\_LOGD("OnRequsetImageDataPreparedWithDetails GetUri uri\_ = %{public}s", URI);
        cb(const\_cast<char \*>(URI));
        NDKCamera::ChangeRequestAddResourceWithBuffer(imageSourceNative);
        return;
    }
    
    // Request image data: deliveryMode/quality and other parameters are controlled via requestOptions. After completion, the OnRequsetImageDataPreparedWithDetails callback is triggered.
    MediaLibrary\_ErrorCode NDKCamera::MediaAssetManagerRequestImage(OH\_MediaAsset \*mediaAsset)
    {
        DRAWING\_LOGD("NDKCamera::MediaAssetManagerRequestImage start! g\_deliveryMode = %{public}d",
            g\_deliveryMode);
        requestOptions.deliveryMode = g\_deliveryMode;
        result = OH\_MediaAssetManager\_RequestImage(mediaAssetManager, mediaAsset, requestOptions, &g\_requestId,
            OnRequsetImageDataPreparedWithDetails);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::MediaAssetManagerRequestImage failed.");
        }
        DRAWING\_LOGD("NDKCamera::MediaAssetManagerRequestImage return with ret code: %{public}d!", result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestAddResourceWithBuffer(OH\_ImageSourceNative \*imageSourceNative)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer start!");
        size\_t bufferSize = BUFFER\_SIZE;
        char buffer\[BUFFER\_SIZE\];
        int fd = open("/data/storage/el2/base/haps/test.jpg", O\_RDONLY);
        int fr = read(fd, buffer, bufferSize);
        if (fr == -1) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read failed.");
            return MEDIA\_LIBRARY\_OK;
        }
        if (fr == BUFFER\_SIZE) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read not complete.");
            return MEDIA\_LIBRARY\_OK;
        }
        result = OH\_MediaAssetChangeRequest\_AddResourceWithBuffer(g\_changeRequest,
            MediaLibrary\_ResourceType::MEDIA\_LIBRARY\_IMAGE\_RESOURCE, (uint8\_t \*)buffer, (uint32\_t)bufferSize);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed.");
            DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed %{public}d.", result);
            return MEDIA\_LIBRARY\_OK;
        }
        result = OH\_MediaAccessHelper\_ApplyChanges(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD(
                "NDKCamera::ChangeRequestAddResourceWithBuffer OH\_MediaAccessHelper\_ApplyChanges failed.");
            return MEDIA\_LIBRARY\_OK;
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer OH\_MediaAccessHelper\_ApplyChanges return "
                     "with ret code: %{public}d!",
            result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestSaveCameraPhoto(void)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto start!");
        result = OH\_MediaAssetChangeRequest\_SaveCameraPhoto(g\_changeRequest,
            MediaLibrary\_ImageFileType::MEDIA\_LIBRARY\_IMAGE\_JPEG);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD(
                "NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAssetChangeRequest\_SaveCameraPhoto failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAssetChangeRequest\_SaveCameraPhoto "
                     "return with ret code: %{public}d!",
            result);
        result = OH\_MediaAccessHelper\_ApplyChanges(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAccessHelper\_ApplyChanges failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH\_MediaAccessHelper\_ApplyChanges return with "
                     "ret code: %{public}d!",
            result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestDiscardCameraPhoto(void)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto start!");
        result = OH\_MediaAssetChangeRequest\_DiscardCameraPhoto(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto "
                         "OH\_MediaAssetChangeRequest\_DiscardCameraPhoto failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH\_MediaAssetChangeRequest\_DiscardCameraPhoto "
                     "return with ret code: %{public}d!",
            result);
        result = OH\_MediaAccessHelper\_ApplyChanges(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD(
                "NDKCamera::ChangeRequestDiscardCameraPhoto OH\_MediaAccessHelper\_ApplyChanges failed.");
        }
        DRAWING\_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH\_MediaAccessHelper\_ApplyChanges return with "
                     "ret code: %{public}d!",
            result);
        return result;
    }
    
    MediaLibrary\_ErrorCode NDKCamera::ChangeRequestRelease(void)
    {
        DRAWING\_LOGD("NDKCamera::ChangeRequestRelease start!");
        result = OH\_MediaAssetChangeRequest\_Release(g\_changeRequest);
        if (result != MEDIA\_LIBRARY\_OK) {
            DRAWING\_LOGD("NDKCamera::ChangeRequestRelease failed.");
        }
        g\_changeRequest = nullptr;
        DRAWING\_LOGD("NDKCamera::ChangeRequestRelease return with ret code: %{public}d!", result);
        return result;
    }
