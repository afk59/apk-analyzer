# Image Security Verification

#### Use Cases

Image data captured by a camera in secure mode is signed by creating an attestation key and initializing an attestation session, to ensure authenticity and integrity of the image data.

#### Restrictions

This feature requires that the device supports the secure camera mode.

You can call the [getSupportedSceneModes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedscenemodes11) method to check whether a device supports the secure camera mode. If the return value is **camera.SceneMode.SECURE\_PHOTO**, the device supports the secure camera mode. If other values are returned, the device does not support the secure camera mode. The following is an example:

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
// Obtain the secure camera.
function getSecureCameraDevice(cameraManager: camera.CameraManager): camera.CameraDevice {
    // Obtain the list of cameras supported by the device.
    const cameraDevices = cameraManager.getSupportedCameras();
    if (cameraDevices.length < 1) {
      throw new Error('no camera devices');
    }
    // Obtain the front camera object. Currently, the secure camera must be a front camera.
    const frontCamera: camera.CameraDevice | undefined = cameraDevices.find((profile: camera.CameraDevice) => {
      return profile.cameraPosition != camera.CameraPosition.CAMERA\_POSITION\_BACK;
    });
    if (frontCamera === undefined) {
      throw new Error('no front cameras');
    }
    // Check whether the front camera supports the secure camera mode. If yes, the front camera can be used for subsequent secure camera operations.
    const modes = cameraManager.getSupportedSceneModes(frontCamera);
    if (modes.indexOf(camera.SceneMode.SECURE\_PHOTO) === -1) {
      throw new Error('current device not support secure camera');
    }
    return frontCamera;
  }

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/vxSeIrcfS5mygX8nyac2EQ/en-us_image_0000002514988417.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6C74322985EB5C5EB208318BFF06EDB2973108BA19A6CE770CCFCE663C39E60 "Click to enlarge")

#### API Description

For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section81796536265)(options: AttestOptions): Promise<void>

 | 

Creates an attestation key.

 |
| 

[initializeAttestContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section166716269293)(userData: string, options: AttestOptions): Promise<AttestReturnResult>

 | 

Initializes an attestation session.

 |
| 

[finalizeAttestContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section18667940102912)(options: AttestOptions): Promise<void>

 | 

Ends an attestation session.

 |
| 

[destroyAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section19260221152819)(): Promise<void>

 | 

Destroys an attestation key.

 |

#### Development Procedure

1.  Import the camera module, trustedAppService module, and dependent modules.
    
    import { camera } from '@kit.CameraKit';
    import { trustedAppService } from '@kit.DeviceSecurityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Initialize the camera in secure mode.
    
    You need to:
    
    -   Select a camera that supports the secure mode.
    -   Check the output capability supported by the camera in secure mode.
    -   Create the input and output streams.
    -   Turn on the camera in secure mode and obtain the device serial number.
    
3.  Create an attestation key and initialize an attestation session.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/6f0UbxTwTxCcZoaBS8C3KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E706604637B1DD5531A34EA81F5544704BE1B660344969933D126AEC9A6C760E)
    
    -   An attestation session can be initialized only after an attestation key is successfully created.
    -   An attestation key is valid for seven days. To avoid repeated creation of attestation keys, you are advised to call the attestation session initialization API first. If the initialization fails, destroy and create the attestation key, and initialize the attestation key again.
    -   The device serial number needs to be obtained each time the secure mode is enabled for a camera, and passed for initializing an attestation session for the camera in secure mode. In other scenarios, the value **0** can be passed.
    -   When **initializeAttestContext** is called to initialize an attestation session, the value of **userData** must contain 16 to 127 bytes.
    
    // Parameters for creating an attestation key.
    const createProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_ALGORITHM,
        value: trustedAppService.AttestKeyAlg.ATTEST\_ALG\_ECC
      },
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_KEY\_SIZE,
        value: trustedAppService.AttestKeySize.ATTEST\_ECC\_KEY\_SIZE\_256
      }
    \];
    const createOptions: trustedAppService.AttestOptions = {
      properties: createProperties
    };
    // Parameters for initializing an attestation session.
    const userData = "trusted\_app\_service\_demo"; // Example value. Generate a value on your own, which contains 16 to 127 bytes.
    const deviceId = 7483679320805398131; // Example value. Obtain the value from Camera Kit.
    const initProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
        value: trustedAppService.AttestType.ATTEST\_TYPE\_CAMERA
      },
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_ID,
        value: BigInt(deviceId)
      }
    \];
    const initOptions: trustedAppService.AttestOptions = {
      properties: initProperties
    };
    // Create an attestation key and initialize an attestation session.
    let certChainList: Array<string>;
    try {
      await trustedAppService.createAttestKey(createOptions);
      const result = await trustedAppService.initializeAttestContext(userData, initOptions);
      certChainList = result.certChains;
    } catch (err) {
      const error = err as BusinessError;
      console.error(\`Failed to initialize attest context, message:${error.message}, code:${error.code}\`);
    }
    
4.  Create a secure mode session, configure the input and output streams, and start the preview stream and secure data stream.
5.  End the attestation session.
    
    // Parameters for ending the attestation session.
    const finalProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
        value: trustedAppService.AttestType.ATTEST\_TYPE\_CAMERA
      }
    \];
    const finalOptions: trustedAppService.AttestOptions = {
      properties: finalProperties,
    };
    // End the attestation session.
    try {
      await trustedAppService.finalizeAttestContext(finalOptions);
    } catch (err) {
      const error = err as BusinessError;
      console.error(\`Failed to finalize attest context, message:${error.message}, code:${error.code}\`);
    }
    
    To destroy the attestation key, call the [destroyAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section19260221152819) API after the attestation session ends. Image security verification, location security verification, and secure image compression and cropping share the same attestation key. Before destroying an attestation key, ensure that the location security verification function is not using the attestation key.
