# Secondary Processing of Preview Streams (C/C++)

You can use the APIs in **ImageReceiver** to create a PreviewOutput instance and obtain real-time data of the preview stream for secondary processing. For example, you can add a filter algorithm to the preview stream.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK, which provides camera-related properties and methods.
    
    #include <cstdint>
    #include <cstdlib>
    #include "hilog/log.h"
    #include <memory>
    #include <new>
    #include <multimedia/image\_framework/image/image\_native.h>
    #include <multimedia/image\_framework/image/image\_receiver\_native.h>
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/camera\_device.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    
    #include <multimedia/media\_library/media\_asset\_manager\_capi.h>
    #include <multimedia/media\_library/media\_asset\_change\_request\_capi.h>
    #include <multimedia/media\_library/media\_access\_helper\_capi.h>
    #include <multimedia/image\_framework/image/image\_packer\_native.h>
    
2.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libhilog\_ndk.z.so
        libohimage.so
        libimage\_receiver.so
        libnative\_image.so
        libohcamera.so
        libnative\_buffer.so
    )
    
3.  Initialize an [ImageReceiver](../../../image-kit/image-development-c-c/image-receiving/using-image-nativemodule-to-receive-images/document.md) instance and obtain a surface ID.
    
    Call **OH\_ImageReceiverNative\_Create** of the image module to create an OH\_ImageReceiverNative instance, and call **OH\_ImageReceiverNative\_GetReceivingSurfaceId** of the instance to obtain a surface ID.
    
    void InitImageReceiver(uint64\_t &receiverSurfaceID)
    {
        OH\_ImageReceiverOptions \*options = nullptr;
        // Capture exceptions and check whether the instance is null. This example shows only the API call process.
        // Set image parameters.
        Image\_ErrorCode errCode = OH\_ImageReceiverOptions\_Create(&options);
        if (errCode != IMAGE\_SUCCESS || options == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverOptions\_Create call failed");
            return;
        }
        Image\_Size imgSize;
        imgSize.width = PREVIEW\_WIDTH; // Width of the created preview stream.
        imgSize.height = PREVIEW\_HEIGHT; // Height of the created preview stream.
        int32\_t capacity = 8; // Maximum number of images in BufferQueue. The recommended value is 8.
        errCode = OH\_ImageReceiverOptions\_SetSize(options, imgSize);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverOptions\_SetSize call failed");
        }
        errCode = OH\_ImageReceiverOptions\_SetCapacity(options, capacity);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverOptions\_SetCapacity call failed");
        }
        // Create an OH\_ImageReceiverNative instance.
        OH\_ImageReceiverNative \*receiver = nullptr;
        errCode = OH\_ImageReceiverNative\_Create(options, &receiver);
        if (errCode != IMAGE\_SUCCESS || receiver == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverNative\_Create call failed");
            return;
        }
    
        errCode = OH\_ImageReceiverNative\_On(receiver, CallbackReadNextImage);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "%{public}s image receiver on failed, errCode: %{public}d.", \_\_func\_\_, errCode);
            OH\_ImageReceiverOptions\_Release(options);
            OH\_ImageReceiverNative\_Release(receiver);
            return;
        }
        // Obtain the Surface ID of the OH\_ImageReceiverNative instance.
        errCode = OH\_ImageReceiverNative\_GetReceivingSurfaceId(receiver, &receiverSurfaceID);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageReceiverNative\_GetReceivingSurfaceId call failed");
        } else {
            OH\_LOG\_INFO(LOG\_APP, "receiver surfaceID:%{public}lu", receiverSurfaceID);
        }
    }
    
4.  Create a preview stream based on the surface ID obtained. (Note that you must convert the surface ID type to char \* before the creation of the preview stream.) For details, see step 4 in [Camera Preview (C/C++)](../preview-c-c/document.md).
    
5.  Create a session and enable it. For details, see [Camera Session Management (C/C++)](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md).
    
6.  Register an ImageReceiver callback to listen for the image content reported by each frame.
    
    void copyBuffer(OH\_NativeBuffer \*srcBuffer, size\_t srcSize, OHNativeWindowBuffer \*dstBuffer)
    {
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s IN", \_\_func\_\_);
        void \*srcVir = nullptr;
        OH\_NativeBuffer\_Map(srcBuffer, &srcVir);
        BufferHandle \*bufferHandle = OH\_NativeWindow\_GetBufferHandleFromNative(dstBuffer);
        OH\_LOG\_INFO(LOG\_APP,
            "ImageReceiverNativeCTest %{public}s bufferHandle info fd= %{public}d , width= %{public}d, "
            "height=%{public}d, stride= %{public}d, size= %{public}d, format= %{public}d, usage= %{public}lu",
            \_\_func\_\_, bufferHandle->fd, bufferHandle->width, bufferHandle->height, bufferHandle->stride, bufferHandle->size,
            bufferHandle->format, bufferHandle->usage);
    
        void \*mappedAddr =
            mmap(bufferHandle->virAddr, bufferHandle->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, bufferHandle->fd, 0);
        std::memcpy(static\_cast<unsigned char \*>(mappedAddr), static\_cast<unsigned char \*>(srcVir), srcSize);
        munmap(mappedAddr, bufferHandle->size);
    
        OH\_NativeBuffer\_Unmap(srcBuffer);
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", \_\_func\_\_);
    }
    
    void ShowImage(OH\_ImageNative \*image)
    {
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s IN", \_\_func\_\_);
        uint64\_t xComponentSurfaceId = std::stoull(g\_xComponentSurfaceIdSlave);
        OH\_LOG\_ERROR(LOG\_APP, "ImageReceiverNativeCTest %{public}s XComponentId is : %{public}lu.", \_\_func\_\_,
            xComponentSurfaceId);
        OHNativeWindow \*nativeWindow = nullptr;
        int32\_t res = OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(xComponentSurfaceId, &nativeWindow);
        if (res != 0) {
            OH\_LOG\_ERROR(LOG\_APP,
                "ShowImage CreateNativeWindowFromSurfaceId failed, errCode: %{public}d.", res);
            return;
        }
    
        // Critical: Adjust the size and format of nativeWindow to match the size and format of the image exactly.
        res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_BUFFER\_GEOMETRY, g\_imageWidth, g\_imageHeight);
        res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_FORMAT, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP); // NV21
        // Set the rotation angle: for the rear camera (default rotation 90°), the nativeWindow needs to be rotated by 270°; for the front camera (default rotation 270°), the nativeWindow needs to be rotated by 90°.
        if (g\_isFront) {
            res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_TRANSFORM, NATIVEBUFFER\_FLIP\_V\_ROT90);
        } else {
            res = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_TRANSFORM, NATIVEBUFFER\_ROTATE\_270);
        }
    
        OH\_NativeBuffer \*imageBuffer = nullptr;
        Image\_ErrorCode errCode = OH\_ImageNative\_GetByteBuffer(image, g\_jpegComponent, &imageBuffer);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ShowImage GetByteBuffer failed, errCode: %{public}d.", errCode);
            return;
        }
        Image\_Size imgSize = {};
        OH\_ImageNative\_GetImageSize(image, &imgSize);
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s imgSize is : %{public}u, %{public}u.", \_\_func\_\_,
            imgSize.width, imgSize.height);
        size\_t bufSize = 0;
        OH\_ImageNative\_GetBufferSize(image, g\_jpegComponent, &bufSize);
    
        OHNativeWindowBuffer \*nativeWindowBuffer = nullptr;
        int fenceFd = -1;
        res = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
        if (res != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "ShowImage RequestBuffer failed, errCode: %{public}d.", res);
            return;
        }
    
        // Copy the image data to nativeWindowBuffer.
        copyBuffer(imageBuffer, bufSize, nativeWindowBuffer);
    
        Region region1{};
        res = OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, region1);
        if (res != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "ShowImage FlushBuffer failed, errCode: %{public}d.", res);
            return;
        }
        OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", \_\_func\_\_);
    }
    
    static void CallbackReadNextImage(OH\_ImageReceiverNative \*receiver)
    {
        OH\_LOG\_INFO(LOG\_APP, "CallbackReadNextImage %{public}s IN", \_\_func\_\_);
        // Read the next image object of OH\_ImageReceiverNative.
        OH\_ImageNative \*image = nullptr;
        Image\_ErrorCode errCode = OH\_ImageReceiverNative\_ReadNextImage(receiver, &image);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP,
                "CallbackReadNextImage %{public}s get image receiver next image failed, errCode: %{public}d.", \_\_func\_\_,
                errCode);
            return;
        }
    
        ShowImage(image);
    
        // Release the OH\_ImageNative instance.
        errCode = OH\_ImageNative\_Release(image);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "CallbackReadNextImage %{public}s release image native failed, errCode: %{public}d.",
                \_\_func\_\_, errCode);
        }
        OH\_LOG\_INFO(LOG\_APP, "CallbackReadNextImage %{public}s SUCCESS", \_\_func\_\_);
    }
