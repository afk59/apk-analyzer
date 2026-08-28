# Secure Mode Camera (ArkTS)

Cameras in secure mode are mainly provided for high-security applications like banking that require features such as biometric verification. To use cameras in secure mode, Crypto Architecture Kit and TrustedAppService in Device Security Kit are required in addition to Camera Kit.

The procedure for using a secure mode camera is as follows:

-   Through Camera Kit, an application enables the secure mode of a camera and obtains a **camera serial number**.
-   Through [Device Security Kit](../../../../system/security/device-security-kit/about-this-kit/document.md), the application creates an attestation key (with the camera serial number passed as an input parameter) and initializes an attestation session. After attestation session initialization is complete, Device Security Kit returns an **anonymous certificate chain**.
-   Through Camera Kit, the application configures input and output streams of the camera in secure mode, focusing on configuring a **secure data stream** and registering a callback to listen for each frame of the secure image in the secure data stream.
-   The application parses each frame of the secure image in the secure data stream, and the server verifies the signature of the secure image.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/fQBcF9mPR7G3Ts9qsI216g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7BE65E491C3E62314A03C4BF3B0C476CE846D14CADC9A5D2EC5153F1DB49764)

This topic describes the steps carried out using Camera Kit. Steps related to attestation sessions are executed using Device Security Kit. For details, see [Image Security Verification](../../../../system/security/device-security-kit/trustedappservice/image-security-verification/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/SFKKVE7cQTy5GVd9k__jZA/en-us_image_0000002303095257.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC2CAFA249C23FBD618D7085011F9F5CB2516F4F137064215C5EC2DBEBA4E821)

#### How to Develop

For details about the APIs, see [Camera API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-camera).

1.  Import dependencies. Specifically, import the camera and image modules.
    
    import { camera } from '@kit.CameraKit';
    import { image } from '@kit.ImageKit';
    
2.  Select a camera that supports the secure mode.
    
    You can call [getSupportedSceneModes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedscenemodes11) in the [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) class to obtain all modes supported by the current camera. If the camera supports the secure mode, you can use it for subsequent operations.
    
    Currently, the secure mode is available only for the front camera of mobile phones.
    
    function isSecureCamera(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice): boolean {
      let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraDevice);
      const secureMode = sceneModes.find(mode => mode === camera.SceneMode.SECURE\_PHOTO);
      if (secureMode) {
        console.info('current device support secure camera!');
        return true;
      } else {
        console.info('current device not support secure camera!');
        return false;
      }
    }
    
    let secureCamera: camera.CameraDevice;
    
    function getSecureCamera(cameraManager: camera.CameraManager): void {
      let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
      for (let index = 0; index < cameraArray.length; index++) {
        if (isSecureCamera(cameraManager, cameraArray\[index\])) {
          secureCamera = cameraArray\[index\];
        }
      }
    }
    
3.  Check the output capability supported by the camera in secure mode.
    
    You can call [getSupportedOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedoutputcapability11) of the [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) class to obtain the output capability supported by the camera in secure mode.
    
    Currently, the camera in secure mode supports only the output of preview streams, with a recommended resolution of 640 × 480 for optimal performance.
    
    function getSupportedOutputCapability(cameraManager: camera.CameraManager, secureCamera: camera.CameraDevice): void {
      let outputCap: camera.CameraOutputCapability =
        cameraManager.getSupportedOutputCapability(secureCamera, camera.SceneMode.SECURE\_PHOTO);
      let previewProfilesArray: Array<camera.Profile> = outputCap.previewProfiles;
    }
    
4.  Create the input and output streams.
    
    Two output streams need to be created for the camera in secure mode:
    
    -   One is a common preview stream, which is used for UI display. For details about how to create a common preview stream, see [Preview](../preview-arkts/document.md).
    -   The other is a secure data stream, which is used for security service verification. For the secure data stream, you must create an [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver) instance using [image.createImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-f#imagecreateimagereceiver11), and then obtain the surface ID through [getReceivingSurfaceId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver#getreceivingsurfaceid9).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/83sY8NbbSbyAqnF0NW61jw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEC787A635B7A9F8028D71AEE4E4CE8AB539F129835105131FB1ED8D7596FC95)
        
        There is no independent data type for the secure data stream, which is a type of preview stream and has the same output capability as the preview stream, except that only the JPEG format is supported during the creation of the ImageReceiver instance.
        
    
    async function createInputAndOutputs(cameraManager: camera.CameraManager, 
                                         secureCamera: camera.CameraDevice,
                                         previewProfile: camera.Profile,
                                         previewSurfaceId: string): Promise<void> {
      // Create an input stream.
      let cameraInput: camera.CameraInput = cameraManager.createCameraInput(secureCamera);
      // Create a common preview output stream.
      let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfile, previewSurfaceId);
      // Create a secure data output stream.
      const receiver: image.ImageReceiver =
        image.createImageReceiver({ width: previewProfile.size.width, height: previewProfile.size.height },
                                  image.ImageFormat.JPEG, 8);
      const secureSurfaceId: string = await receiver.getReceivingSurfaceId();
      let secureOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfile, secureSurfaceId);
    }
    
5.  Open the camera.
    
    Call [open(isSecureEnabled)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-camerainput#open12) of [CameraInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-camerainput) to open the camera in secure mode and obtain the camera serial number, a mandatory parameter for the security module to create an attestation session.
    
    The camera can be enabled in secure mode and a serial number can be returned only when **isSecureEnabled** is set to **true**.
    
    async function openCamera(cameraInput: camera.CameraInput) {
      const seqId: bigint = await cameraInput.open(true);
    }
    
6.  Use the capabilities of Device Security Kit to create an attestation key and open an attestation session. For details, see [Image Security Verification](../../../../system/security/device-security-kit/trustedappservice/image-security-verification/document.md).
7.  Create a secure mode session, configure the streams, and commit the configuration.
    
    Create a secure mode session, add the input and output streams to the session, and mark the secure data stream as secure output using [addSecureOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-securesession#addsecureoutput12) of [SecureSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-securesession).
    
    async function openSession(cameraManager: camera.CameraManager,
                               cameraInput: camera.CameraInput,
                               previewOutput: camera.PreviewOutput,
                               secureOutput: camera.PreviewOutput): Promise<void> {
      try {
        let secureSession: camera.SecureSession = cameraManager.createSession(camera.SceneMode.SECURE\_PHOTO);
        if (secureSession === undefined) {
          console.error('create secureSession failed!');
        }
        secureSession.beginConfig();
        secureSession.addInput(cameraInput);
        secureSession.addOutput(previewOutput);
        secureSession.addOutput(secureOutput);
        secureSession.addSecureOutput(secureOutput); // Mark secureOutput as secure output.
        await secureSession.commitConfig();
        await secureSession.start();
      } catch (err) {
        console.error('openSession failed!');
      }
    }
    
8.  After the secure mode session is started normally, the data within the preview stream and secure data stream is reported frame by frame. The data of each frame of the secure data stream can be obtained by registering the [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver) callback in [imageArrival](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver#on9).
    
    function onBuffer(receiver: image.ImageReceiver): void {
      receiver.on('imageArrival', () => {
        // Read the next image from ImageReceiver.
        receiver.readNextImage().then((img: image.Image) => {
          // Obtain the component cache from the image.
          img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
            // Secure data stream content. The application parses the buffer content to complete signature authentication.
            const buffer = component.byteBuffer;
            console.info('Succeeded in getting component byteBuffer.');
          })
        })
      })
    }
    
    Parse each frame of the image in the secure data stream, and verify the signature of the secure image on the server.
    
    To verify the signature of image data or geographical location data on the device, follow the instructions provided in [Verifying the Signature](../../../../system/security/device-security-kit/trustedappservice/signature-verification/verifying-the-signature/document.md).
    
9.  Release the camera in secure mode by calling [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#release11-1) of [Session](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session).
