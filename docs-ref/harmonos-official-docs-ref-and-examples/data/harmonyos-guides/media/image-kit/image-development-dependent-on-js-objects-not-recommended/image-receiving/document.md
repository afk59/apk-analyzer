# Image Receiving

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/S8Erl8nhTJCyJI7NukLiig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3F7654D6F72EA12CC6D186A54995051923EC505E8989080C568A1FE9C2C0B24)

This guide uses the APIs provided by the [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image) module, which supports basic functionalities such as image encoding/decoding, image receiver operations, and image data processing. These APIs are introduced prior to API version 11, and no additional features will be included in later versions. Therefore, these APIs are not recommended.

You can also use the C APIs provided by the [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule) module, which includes all the foundational features of the Image module while adding new capabilities like multi-image encoding/decoding. For details about the development guide, see [Using Image\_NativeModule to Decode Images (C/C++)](../../image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md). These APIs are available since API version 12 and are expected to keep evolving. You are encouraged to use them.

You are not advised to use both sets of C APIs in your code. It may cause compatibility issues in some scenarios.

You can use the **ImageReceiver** class to obtain the surface ID of a component, read the latest image or the next image, and release ImageReceiver instances.

#### How to Develop

## Adding Dependencies

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libace\_napi.z.so**, **libimage\_ndk.z.so**, **libimage\_receiver\_ndk.z.so**, **libnative\_image.so**, and **libhilog\_ndk.z.so** (on which the native log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so libimage\_ndk.z.so libimage\_receiver\_ndk.z.so libnative\_image.so)

## Adding API Mappings

Open the **src/main/cpp/hello.cpp** file and add the following API mappings to the **Init** function:

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "createFromReceiver", nullptr, createFromReceiver, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };

    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

## Requesting Permissions

To obtain input data of an image from a camera, you must request the **ohos.permission.CAMERA** permission. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

## Calling APIs on the JS Side

1.  Open src\\main\\cpp\\types\*libentry\\index.d.ts\* (where **libentry** varies according to the project name), and import the following files:
    
    import { image } from '@kit.ImageKit';
    
    export const createFromReceiver: (a: image.ImageReceiver) => image.Image;
    
2.  Open **src\\main\\ets\\pages\\index.ets**, import **libentry.so** (where **libentry** varies according to the project name), call the native APIs, and pass in the JS resource object. The following is an example:
    
    import testNapi from 'libentry.so';
    import { image } from '@kit.ImageKit';
    import { common, abilityAccessCtrl } from '@kit.AbilityKit';
    import { camera } from '@kit.CameraKit';
    
    @Entry
    @Component
    struct Index {
      private receiver: image.ImageReceiver | undefined = undefined;
      func (){
         let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
         abilityAccessCtrl.createAtManager().requestPermissionsFromUser(context,\['ohos.permission.CAMERA'\]).then(async () => {
            let cameraManager = await camera.getCameraManager(context);
            // Obtain the supported camera devices.
            let cameraDevices: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
            if (cameraDevices.length <= 0) {
            return;
            }
            // Obtain the profiles of the cameras.
            let profiles: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevices\[0\], camera.SceneMode.NORMAL\_PHOTO);
            let previewProfiles: Array<camera.Profile> = profiles.previewProfiles;
            if (previewProfiles.length <= 0) {
            return;
            }
            let profileObj = previewProfiles\[0\];
            this.receiver = image.createImageReceiver({width:profileObj.size.width, height:profileObj.size.height}, image.ImageFormat.JPEG, 8);
            let receiverSurfaceId: string = await this.receiver.getReceivingSurfaceId();
            // Create an output object for the preview stream.
            let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(profileObj,receiverSurfaceId);
            let cameraInput : camera.CameraInput = cameraManager.createCameraInput(cameraDevices\[0\]);
            // Open the camera.
            await cameraInput.open();
            // Create a session.
            let session : camera.PhotoSession = cameraManager.createSession(camera.SceneMode.NORMAL\_PHOTO) as camera.PhotoSession;
            // Configure the session.
            session.beginConfig();
            // Add a CameraInput instance to the session.
            session.addInput(cameraInput);
            // Add the preview stream to the session.
            session.addOutput(previewOutput);
            // Commit the configuration.
            await session.commitConfig();
            // Start the session.
            await session.start();
    
            this.receiver.on('imageArrival', () => {
               let img : image.Image = testNapi.createFromReceiver(this.receiver);
               img.release();
            })
    
         });
      }
    
      build() {
         Row() {
            Column() {
            Button("start")
               .width(100)
               .height(100)
               .onClick(() => {
                  console.info("button click in");
                  if (this.receiver == undefined) {
                     this.func();
                  }
               })
            }
            .width('100%')
         }
         .height('100%')
      }
    }
    

## Calling the Native APIs

For details about the APIs, see [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image).

Obtain the JS resource object from the **hello.cpp** file and convert it to a native resource object. Then you can call native APIs.

**Adding Reference Files**

#include <multimedia/image\_framework/image\_mdk.h>
#include <multimedia/image\_framework/image\_receiver\_mdk.h>
#include <malloc.h>
#include <hilog/log.h>

static napi\_value createFromReceiver(napi\_env env, napi\_callback\_info info)
{
   size\_t argc = 1;
   napi\_value args\[2\] = {nullptr};
   napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
   napi\_valuetype valuetype0;
   napi\_typeof(env, args\[0\], &valuetype0);
   napi\_ref reference;
   napi\_create\_reference(env, args\[0\], 1 ,&reference);
   napi\_value imgReceiver\_js;
   napi\_get\_reference\_value(env, reference, &imgReceiver\_js);
   
   ImageReceiverNative \* imgReceiver\_c = OH\_Image\_Receiver\_InitImageReceiverNative(env, imgReceiver\_js);

   int32\_t capacity;
   OH\_Image\_Receiver\_GetCapacity(imgReceiver\_c, &capacity);
   OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[receiver\]", "capacity: %{public}d", capacity);
   int32\_t format;
   OH\_Image\_Receiver\_GetFormat(imgReceiver\_c, &format);
   OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[receiver\]", "format: %{public}d", format);
   char \* surfaceId = static\_cast<char \*>(malloc(sizeof(char)));
   OH\_Image\_Receiver\_GetReceivingSurfaceId(imgReceiver\_c, surfaceId, sizeof(char));
   OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[receiver\]", "surfaceId: %{public}c", surfaceId\[0\]);
   OhosImageSize size;
   OH\_Image\_Receiver\_GetSize(imgReceiver\_c, &size);
   OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[receiver\]", "OH\_Image\_Receiver\_GetSize  width: %{public}d, height:%{public}d", size.width, size.height);
   
   int32\_t ret;
   napi\_value nextImage;
   // Alternatively, call OH\_Image\_Receiver\_ReadNextImage(imgReceiver\_c, &nextImage).
   ret = OH\_Image\_Receiver\_ReadLatestImage(imgReceiver\_c, &nextImage);
   
   ImageNative \* nextImage\_native = OH\_Image\_InitImageNative(env, nextImage);

   OhosImageSize imageSize;
   OH\_Image\_Size(nextImage\_native, &imageSize);
   OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[receiver\]", "OH\_Image\_Size  width: %{public}d, height:%{public}d", imageSize.width, imageSize.height);

   OhosImageComponent imgComponent;
   ret = OH\_Image\_GetComponent(nextImage\_native, 4, &imgComponent); // 4=jpeg
   
   uint8\_t \*img\_buffer = imgComponent.byteBuffer;
   
   ret = OH\_Image\_Release(nextImage\_native);
   ret = OH\_Image\_Receiver\_Release(imgReceiver\_c);
   return nextImage;
}
