# Using Image\_NativeModule to Receive Images

You can use the **ImageReceiver** class to obtain the surface ID of a component, read the latest image or the next image, and release ImageReceiver instances. For details about the sample code of camera preview implemented with the use of the camera API, see [Secondary Processing of Preview Streams (C/C++)](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/secondary-processing-of-preview-streams-c-c/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FaI_puUPQ_WWuKVDlXZDaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83CD86C6CE0CCF1FF747D46E4C5A1305BB6B06C7304F2C5FCEC0F73F3ACB0976)

The ImageReceiver merely serves as the recipient and consumer of images. The properties set in ImageReceiver, such as size and format, do not actually take effect. Image properties need to be configured on the sending side (the producer), such as when setting up the preview profiles for a [preview stream (C/C++)](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/preview-c-c/document.md).

#### How to Develop

## Adding Dependencies

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libohimage.so**, **libimage\_receiver.so**, **libnative\_image.so**, and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libohimage.so libimage\_receiver.so libnative\_image.so)

## Calling the Native APIs

For details about the APIs, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).

The code below mainly shows how to initialize the receiver, create a camera preview stream, obtain image information, and release the receiver.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/OD9kDLtYS1GVqeYV1fLjNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B3321B4C9D078030D333DAF70AEC7642519E52309331E4DADAFAA116549B348)

Certain APIs are supported only in API version 20 or later. You should select an appropriate API version during development.

1.  Import the required header files.
    
    #include <hilog/log.h>
    #include "napi/native\_api.h"
    #include <string>
    #include <multimedia/image\_framework/image/image\_native.h>
    #include <multimedia/image\_framework/image/image\_receiver\_native.h>
    
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    
    #include <mutex>
    #include <condition\_variable>
    
2.  Define constants.
    
    #undef LOG\_DOMAIN
    #define LOG\_DOMAIN 0x3200
    
    #undef LOG\_TAG
    #define LOG\_TAG "MY\_TAG"
    
    #define IMAGE\_WIDTH 320
    #define IMAGE\_HEIGHT 480
    #define IMAGE\_CAPACITY 2
    
3.  Define global variables.
    
    static OH\_ImageReceiverNative\* g\_receiver = nullptr;
    
    static std::mutex g\_mutex;
    static std::condition\_variable g\_condVar;
    static bool g\_imageReady = false;
    static OH\_ImageNative\* g\_imageInfoResult = nullptr;
    
4.  Define certain helper functions to manage the NAPI return value and parameter type conversion.
    
    // Process the NAPI return value.
    napi\_value GetJsResultDemo(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
    // Convert uint64\_t to a char array terminated with null.
    std::unique\_ptr<char\[\]> ConvertUint64ToCharTemp(uint64\_t value)
    {
        std::string strValue = std::to\_string(value);
        auto charBuffer = std::make\_unique<char\[\]>(strValue.size() + 1);
        std::copy(strValue.begin(), strValue.end(), charBuffer.get());
        charBuffer\[strValue.size()\] = '\\0';
    
        return charBuffer;
    }
    
5.  Initialize the receiver.
    
    -   Create and set receiver options.
        
        static Image\_ErrorCode CreateAndConfigOptions(OH\_ImageReceiverOptions\*\* options)
        {
            Image\_ErrorCode errCode = OH\_ImageReceiverOptions\_Create(options);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Create image receiver options failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            Image\_Size imgSize = {IMAGE\_WIDTH, IMAGE\_HEIGHT};
            errCode = OH\_ImageReceiverOptions\_SetSize(\*options, imgSize);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Set image receiver options size failed, errCode: %{public}d.", errCode);
                OH\_ImageReceiverOptions\_Release(\*options);
                return errCode;
            }
            errCode = OH\_ImageReceiverOptions\_SetCapacity(\*options, IMAGE\_CAPACITY);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Set image receiver options capacity failed, errCode: %{public}d.", errCode);
                OH\_ImageReceiverOptions\_Release(\*options);
                return errCode;
            }
            return IMAGE\_SUCCESS;
        }
        
    -   Obtain the receiver options.
        
        static Image\_ErrorCode ValidateOptions(OH\_ImageReceiverOptions\* options)
        {
            Image\_Size imgSizeRead;
            Image\_ErrorCode errCode = OH\_ImageReceiverOptions\_GetSize(options, &imgSizeRead);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options size failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            if (imgSizeRead.width != IMAGE\_WIDTH || imgSizeRead.height != IMAGE\_HEIGHT) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options size failed,"
                             "width: %{public}d, height: %{public}d.", imgSizeRead.width, imgSizeRead.height);
                return IMAGE\_BAD\_PARAMETER;
            }
            int32\_t capacity = 0;
            errCode = OH\_ImageReceiverOptions\_GetCapacity(options, &capacity);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options capacity failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            if (capacity != IMAGE\_CAPACITY) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver options capacity failed, capacity: %{public}d.", capacity);
                return IMAGE\_BAD\_PARAMETER;
            }
            return IMAGE\_SUCCESS;
        }
        
    -   Create a receiver instance.
        
        static Image\_ErrorCode CreateReceiver(OH\_ImageReceiverOptions\* options, OH\_ImageReceiverNative\*\* receiver)
        {
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_Create(options, receiver);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Create image receiver failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            return IMAGE\_SUCCESS;
        }
        
    -   Define the callback for obtaining the next image.
        
        static void OnCallback(OH\_ImageReceiverNative\* receiver)
        {
            OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest buffer available.");
        
            OH\_ImageNative\* image = nullptr;
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_ReadNextImage(receiver, &image);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "ImageReceiverNativeCTest get image receiver next image failed,"
                             "errCode: %{public}d.", errCode);
                OH\_ImageNative\_Release(image);
                return;
            } else {
                std::lock\_guard<std::mutex> lock(g\_mutex);
                g\_imageInfoResult = image;
                g\_imageReady = true;
            }
            g\_condVar.notify\_one();
        }
        
    -   Register the callback.
        
        static Image\_ErrorCode RegisterCallbackAndQuery(OH\_ImageReceiverNative\* receiver)
        {
            uint64\_t surfaceID = 0;
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_On(receiver, OnCallback);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Image receiver on failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            errCode = OH\_ImageReceiverNative\_GetReceivingSurfaceId(receiver, &surfaceID);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver surfaceID failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            OH\_LOG\_INFO(LOG\_APP, "Get image receiver surfaceID: %{public}lu.", surfaceID);
            Image\_Size imgSizeRead;
            errCode = OH\_ImageReceiverNative\_GetSize(receiver, &imgSizeRead);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver size failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            OH\_LOG\_INFO(LOG\_APP, "Get image receiver size: width = %{public}d, height = %{public}d.",
                        imgSizeRead.width, imgSizeRead.height);
            int32\_t capacity = 0;
            errCode = OH\_ImageReceiverNative\_GetCapacity(receiver, &capacity);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get image receiver capacity failed, errCode: %{public}d.", errCode);
                return errCode;
            }
            OH\_LOG\_INFO(LOG\_APP, "Get image receiver capacity: %{public}d.", capacity);
            return IMAGE\_SUCCESS;
        }
        
    -   Initialize the receiver.
        
        static napi\_value ImageReceiverNativeCTest(napi\_env env, napi\_callback\_info info)
        {
            if (g\_receiver != nullptr) {
                OH\_ImageReceiverNative\_Off(g\_receiver);
                OH\_ImageReceiverNative\_Release(g\_receiver);
                g\_receiver = nullptr;
            }
        
            OH\_ImageReceiverOptions\* options = nullptr;
            Image\_ErrorCode errCode = CreateAndConfigOptions(&options);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "CreateAndConfigOptions failed errCode=%{public}d", errCode);
                return GetJsResultDemo(env, errCode);
            }
            errCode = ValidateOptions(options);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "ValidateOptions failed errCode=%{public}d", errCode);
                OH\_ImageReceiverOptions\_Release(options);
                return GetJsResultDemo(env, errCode);
            }
            errCode = CreateReceiver(options, &g\_receiver);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "CreateReceiver failed errCode=%{public}d", errCode);
                OH\_ImageReceiverOptions\_Release(options);
                return GetJsResultDemo(env, errCode);
            }
            errCode = RegisterCallbackAndQuery(g\_receiver);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "RegisterCallbackAndQuery failed errCode=%{public}d", errCode);
                OH\_ImageReceiverOptions\_Release(options);
                OH\_ImageReceiverNative\_Release(g\_receiver);
                g\_receiver = nullptr;
                return GetJsResultDemo(env, errCode);
            }
            OH\_LOG\_INFO(LOG\_APP, "ImageReceiverNativeCTest create and config success.");
            OH\_ImageReceiverOptions\_Release(options);
            return GetJsResultDemo(env, IMAGE\_SUCCESS);
        }
        
6.  Call the camera photo stream to take a photo and trigger the callback.
    
    -   Create a CameraManager instance.
        
        Camera\_ErrorCode InitCameraManagerAndInput(Camera\_Manager\*& cameraManager,
                                                   Camera\_Device\*& cameras,
                                                   uint32\_t& size,
                                                   Camera\_Input\*& cameraInput)
        {
            cameraManager = nullptr;
            cameras = nullptr;
            size = 0;
            cameraInput = nullptr;
            Camera\_ErrorCode ret = OH\_Camera\_GetCameraManager(&cameraManager);
            if (cameraManager == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_GetCameraManager failed.");
                return ret;
            }
            ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, &cameras, &size);
            if (cameras == nullptr || size < 1 || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
                return ret;
            }
        
            for (uint32\_t i = 0; i < size; ++i) {
                OH\_LOG\_INFO(LOG\_APP, "Camera\[%{public}u\]: id=%{public}s, position=%{public}d, type=%{public}d, "
                    "connectionType=%{public}d", i, cameras\[i\].cameraId, cameras\[i\].cameraPosition, cameras\[i\].cameraType,
                    cameras\[i\].connectionType);
            }
        
            ret = OH\_CameraManager\_CreateCameraInput(cameraManager, &cameras\[0\], &cameraInput);
            if (cameraInput == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCameraInput failed.ret:%{public}d", ret);
                return ret;
            }
            return CAMERA\_OK;
        }
        
    -   Obtain the camera output capability.
        
        Camera\_ErrorCode GetCameraOutputCapability(Camera\_Manager\* cameraManager,
                                                   Camera\_Device\* cameras,
                                                   uint32\_t cameraDeviceIndex,
                                                   Camera\_OutputCapability\*& capability)
        {
            capability = nullptr;
            Camera\_ErrorCode ret = OH\_CameraManager\_GetSupportedCameraOutputCapability(cameraManager,
                                                                                       &cameras\[cameraDeviceIndex\],
                                                                                       &capability);
            if (capability == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameraOutputCapability failed.");
            }
            return ret;
        }
        
    -   Create a camera capture session, which is used to capture photos taken using the camera.
        
        Camera\_CaptureSession\* CreateAndStartSession(Camera\_Manager\* cameraManager, Camera\_Input\* cameraInput, int sessionMode)
        {
            Camera\_CaptureSession\* captureSession = nullptr;
            Camera\_ErrorCode ret = OH\_CameraManager\_CreateCaptureSession(cameraManager, &captureSession);
            if (captureSession == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCaptureSession failed.");
                return nullptr;
            }
            ret = OH\_CaptureSession\_SetSessionMode(captureSession, static\_cast<Camera\_SceneMode>(sessionMode));
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetSessionMode failed.");
                return nullptr;
            }
            ret = OH\_CaptureSession\_BeginConfig(captureSession);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_BeginConfig failed.");
                return nullptr;
            }
            ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
                return nullptr;
            }
            return captureSession;
        }
        
    -   Start the capture session.
        
        static Camera\_ErrorCode StartCaptureSession(Camera\_Manager\* mgr, Camera\_Input\* input,
                                                    Camera\_PreviewOutput\* previewOutput,
                                                    Camera\_CaptureSession\*\* sessionOut)
        {
            \*sessionOut = CreateAndStartSession(mgr, input, NORMAL\_PHOTO);
            if (\*sessionOut == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "CreateAndStartSession failed.");
                return CAMERA\_INVALID\_ARGUMENT;
            }
        
            Camera\_ErrorCode ret = OH\_CaptureSession\_AddPreviewOutput(\*sessionOut, previewOutput);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
                return ret;
            }
        
            ret = OH\_CaptureSession\_CommitConfig(\*sessionOut);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
                return ret;
            }
        
            ret = OH\_CaptureSession\_Start(\*sessionOut);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
            }
            
            return ret;
        }
        
    -   Create a camera photo stream.
        
        Camera\_ErrorCode StartTakePhoto(char\* str)
        {
            char\* photoSurfaceId = str;
            Camera\_Manager\* cameraManager = nullptr;
            Camera\_Device\* cameras = nullptr;
            uint32\_t size = 0;
            Camera\_Input\* cameraInput = nullptr;
            Camera\_ErrorCode ret = InitCameraManagerAndInput(cameraManager, cameras, size, cameraInput);
            if (ret != CAMERA\_OK) return ret;
        
            Camera\_OutputCapability\* cameraOutputCapability = nullptr;
            ret = GetCameraOutputCapability(cameraManager, cameras, 0, cameraOutputCapability);
            if (ret != CAMERA\_OK) return ret;
            
            const Camera\_Profile\* photoProfile = cameraOutputCapability->previewProfiles\[0\];
            Camera\_PreviewOutput\* previewOutput = nullptr;
            ret = OH\_CameraManager\_CreatePreviewOutput(cameraManager, photoProfile, photoSurfaceId, &previewOutput);
            if (photoProfile == nullptr || previewOutput == nullptr || ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreatePreviewOutput failed.");
                return ret;
            }
        
            ret = OH\_CameraInput\_Open(cameraInput);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_open failed.");
                return ret;
            }
        
            Camera\_CaptureSession\* captureSession = nullptr;
            ret = StartCaptureSession(cameraManager, cameraInput, previewOutput, &captureSession);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "StartCaptureSession failed.");
                return ret;
            }
            
            return CAMERA\_OK;
        }
        
    -   Call the camera to take a photo.
        
        static napi\_value TakePhoto(napi\_env env, napi\_callback\_info info)
        {
            if (g\_receiver == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "ImageReceiver not initialized.");
                return GetJsResultDemo(env, IMAGE\_BAD\_PARAMETER);
            }
            uint64\_t surfaceId = 0;
            Image\_ErrorCode errCode = OH\_ImageReceiverNative\_GetReceivingSurfaceId(g\_receiver, &surfaceId);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "Get surfaceId failed.");
                return GetJsResultDemo(env, errCode);
            }
        
            auto surfaceId\_c = ConvertUint64ToCharTemp(surfaceId);
            Camera\_ErrorCode photoRet = StartTakePhoto(surfaceId\_c.get());
            return GetJsResultDemo(env, photoRet);
        }
        
7.  Obtain the image information received by the receiver.
    
    -   Wait for the OnCallback notification.
        
        // Synchronous waiting.
        static OH\_ImageNative\* NotifyJsImageInfoSync()
        {
            std::unique\_lock<std::mutex> lock(g\_mutex);
            g\_imageReady = false;
            g\_imageInfoResult = nullptr;
        
            // Wait for the OnCallback notification.
            bool ret = g\_condVar.wait\_for(lock, std::chrono::seconds(1), \[\] {
                OH\_LOG\_INFO(LOG\_APP, "NotifyJsImageInfoSync: wait\_for wakeup, g\_imageReady=%{public}d", g\_imageReady);
                return g\_imageReady;
            });
            if (!ret) {
                OH\_LOG\_ERROR(LOG\_APP, "NotifyJsImageInfoSync: wait\_for timeout.");
                return nullptr;
            }
            return g\_imageInfoResult;
        }
        
    -   Obtain the image size.
        
        // Obtain the image size.
        static napi\_value GetImageSizeInfo(napi\_env env, OH\_ImageNative\* image)
        {
            OH\_LOG\_INFO(LOG\_APP, "GetImageSizeInfo: enter, image=%{public}p", image);
        
            Image\_Size imgSizeRead;
            Image\_ErrorCode errCode = OH\_ImageNative\_GetImageSize(image, &imgSizeRead);
            OH\_LOG\_INFO(LOG\_APP, "GetImageSizeInfo: GetImageSize errCode=%{public}d, width=%{public}d, height=%{public}d",
                        errCode, imgSizeRead.width, imgSizeRead.height);
        
            if (errCode == IMAGE\_SUCCESS) {
                napi\_value resultObj;
                napi\_create\_object(env, &resultObj);
        
                napi\_value width;
                napi\_value height;
                napi\_create\_int32(env, imgSizeRead.width, &width);
                napi\_create\_int32(env, imgSizeRead.height, &height);
        
                napi\_set\_named\_property(env, resultObj, "width", width);
                napi\_set\_named\_property(env, resultObj, "height", height);
        
                OH\_LOG\_INFO(LOG\_APP, "GetImageSizeInfo: exit");
                return resultObj;
            }
        
            OH\_LOG\_ERROR(LOG\_APP, "GetImageSizeInfo: Failed to get image size");
            return nullptr;
        }
        
    -   Obtain the component type.
        
        // Obtain the component type.
        static size\_t GetComponentTypeSize(OH\_ImageNative\* image, size\_t& componentTypeSize)
        {
            OH\_LOG\_INFO(LOG\_APP, "GetComponentTypeSize: enter, image=%{public}p", image);
            // Obtain the size of the component type.
            Image\_ErrorCode errCode = OH\_ImageNative\_GetComponentTypes(image, nullptr, &componentTypeSize);
            OH\_LOG\_INFO(LOG\_APP, "GetComponentTypeSize: GetComponentTypes (query size) errCode=%{public}d,"
                        "componentTypeSize=%{public}zu", errCode, componentTypeSize);
            return componentTypeSize;
        }
        
    -   Obtain the component information.
        
        // Obtain the component information.
        static napi\_value GetComponentInfo(napi\_env env, size\_t componentTypeSize, OH\_ImageNative\* image, napi\_value resultObj)
        {
            if (componentTypeSize > 0) {
                uint32\_t\* components = new uint32\_t\[componentTypeSize\];
                Image\_ErrorCode errCode = OH\_ImageNative\_GetComponentTypes(image, &components, &componentTypeSize);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetComponentTypes (get types) errCode=%{public}d,"
                            "firstComponent=%{public}u", errCode, componentTypeSize > 0 ? components\[0\] : 0);
                if (errCode != IMAGE\_SUCCESS) {
                    OH\_LOG\_ERROR(LOG\_APP, "GetImageInfoObject: GetComponentTypes (get types) failed");
                    delete \[\] components;
                    return resultObj;
                }
                
                OH\_NativeBuffer\* nativeBuffer = nullptr;
                errCode = OH\_ImageNative\_GetByteBuffer(image, components\[0\], &nativeBuffer);
                if (errCode == IMAGE\_SUCCESS) {
                    OH\_LOG\_INFO(LOG\_APP, "Get native buffer success.");
                }
            
                size\_t nativeBufferSize = 0;
                errCode = OH\_ImageNative\_GetBufferSize(image, components\[0\], &nativeBufferSize);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetBufferSize errCode=%{public}d, nativeBufferSize=%{public}zu",
                            errCode, nativeBufferSize);
                if (errCode == IMAGE\_SUCCESS) {
                    napi\_value bufSize;
                    napi\_create\_int32(env, static\_cast<int32\_t>(nativeBufferSize), &bufSize);
                    napi\_set\_named\_property(env, resultObj, "bufferSize", bufSize);
                }
            
                int32\_t rowStride = 0;
                errCode = OH\_ImageNative\_GetRowStride(image, components\[0\], &rowStride);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetRowStride errCode=%{public}d,"
                            "rowStride=%{public}d", errCode, rowStride);
                if (errCode == IMAGE\_SUCCESS) {
                    napi\_value jsRowStride;
                    napi\_create\_int32(env, rowStride, &jsRowStride);
                    napi\_set\_named\_property(env, resultObj, "rowStride", jsRowStride);
                }
            
                int32\_t pixelStride = 0;
                errCode = OH\_ImageNative\_GetPixelStride(image, components\[0\], &pixelStride);
                OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetPixelStride errCode=%{public}d, pixelStride=%{public}d",
                            errCode, pixelStride);
                if (errCode == IMAGE\_SUCCESS) {
                    napi\_value jsPixelStride;
                    napi\_create\_int32(env, pixelStride, &jsPixelStride);
                    napi\_set\_named\_property(env, resultObj, "pixelStride", jsPixelStride);
                }
                delete \[\] components;
            }
            return resultObj;
        }
        
    -   Obtain the image properties and encapsulate them into an NAPI object.
        
        // Obtain the image properties and encapsulate them into an NAPI object.
        static napi\_value GetImageInfoObject(napi\_env env, OH\_ImageNative\* image)
        {
            OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: enter, image=%{public}p", image);
            napi\_value resultObj;
            napi\_create\_object(env, &resultObj);
            resultObj = GetImageSizeInfo(env, image);
            
            size\_t componentTypeSize = 0;
            componentTypeSize = GetComponentTypeSize(image, componentTypeSize);
            if (componentTypeSize > 0) {
                resultObj = GetComponentInfo(env, componentTypeSize, image, resultObj);
            }
        
            int64\_t timestamp = 0;
            Image\_ErrorCode errCode = OH\_ImageNative\_GetTimestamp(image, &timestamp);
            OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: GetTimestamp errCode=%{public}d, timestamp=%{public}ld",
                        errCode, timestamp);
            if (errCode == IMAGE\_SUCCESS) {
                napi\_value jsTimestamp;
                napi\_create\_int64(env, timestamp, &jsTimestamp);
                napi\_set\_named\_property(env, resultObj, "timestamp", jsTimestamp);
            }
        
            OH\_LOG\_INFO(LOG\_APP, "GetImageInfoObject: exit");
            return resultObj;
        }
        
    -   Obtain the ReceiverImageInfo.
        
        static napi\_value GetReceiverImageInfo(napi\_env env, napi\_callback\_info info)
        {
            OH\_ImageNative\* image = NotifyJsImageInfoSync();
            if (!image) {
                napi\_value undefined;
                napi\_get\_undefined(env, &undefined);
                return undefined;
            }
            napi\_value resultObj = GetImageInfoObject(env, image);
            OH\_ImageNative\_Release(image);
            return resultObj;
        }
        
8.  Release the receiver.
    
    static napi\_value ReleaseImageReceiver(napi\_env env, napi\_callback\_info info)
    {
        if (g\_receiver == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "No image receiver to release.");
            return nullptr;
        }
        Image\_ErrorCode errCode = OH\_ImageReceiverNative\_Off(g\_receiver);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ImageReceiverNativeCTest image receiver off failed, errCode: %{public}d.", errCode);
        }
        errCode = OH\_ImageReceiverNative\_Release(g\_receiver);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "Release image receiver failed, errCode: %{public}d.", errCode);
        }
        g\_receiver = nullptr;
    
        return GetJsResultDemo(env, errCode);
    }
