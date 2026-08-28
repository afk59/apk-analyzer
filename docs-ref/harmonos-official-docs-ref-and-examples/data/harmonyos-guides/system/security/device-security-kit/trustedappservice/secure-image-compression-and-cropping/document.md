# Secure Image Compression and Cropping

#### Use Cases

In the secure image compression and cropping scenario, you can create an attestation key and initialize an attestation session to compress, crop, and re-sign the image data obtained from the [camera in secure mode](../image-security-verification/document.md). This helps reduce the size of the original image captured by the camera in secure mode while ensuring the authenticity and integrity of the image data.

#### Restrictions

This feature requires that the device supports the secure camera mode. So the devices supported by this feature are the same as those supported by the image security verification feature. You can check whether a device supports the secure camera mode by referring to [Restrictions](../image-security-verification/document.md#section104414218221) in the "Image Security Verification" section.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/v3XMif7ASoapU5AFxWxZqA/en-us_image_0000002514988429.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60A236E95E92C7CB28ACA7A3367DEC183D5C6FEC637944DD0BFA3ADD0EB452B0 "Click to enlarge")

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
| 

[procSecImageTransform](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section4271646181318)(srcSecImage: ArrayBuffer, Options: SecImageProcOptions): Promise<SecImageBuffer>

 | 

Compresses and crops a secure image.

 |

#### Development Procedure

1.  Obtain a secure image by referring to [Image Security Verification](../image-security-verification/document.md).
2.  Create an attestation key and initialize an attestation session.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/2i_xsyakR7mxrVuuIqY57w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44CFD06CBE7EFE3155B5F03B71245891168C14C905B1DB0F3D09F8CEE0FDF06E)
    
    -   An attestation session can be initialized only after an attestation key is successfully created.
    -   An attestation key is valid for seven days. To avoid repeated creation of attestation keys, you are advised to call the attestation session initialization API first. If the initialization fails, destroy and create the attestation key, and initialize the attestation key again.
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
    const initProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
        value: trustedAppService.AttestType.ATTEST\_TYPE\_SECIMAGE\_PROCESS
      },
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_ID,
        value: BigInt(0) // This parameter does not take effect in the secure image compression and cropping scenario.
      }
    \];
    const initOptions: trustedAppService.AttestOptions = {
      properties: initProperties
    };
    
    let certChainList: Array<string>;
    try {
      // Create an attestation key.
      await trustedAppService.createAttestKey(createOptions);
      // Initialize an attestation session.
      const result = await trustedAppService.initializeAttestContext(userData, initOptions);
      certChainList = result.certChains;
    } catch (err) {
      const error = err as BusinessError;
      console.error(\`Failed to initialize attest context, message:${error.message}, code:${error.code}\`);
    }
    
3.  Send a request to compress and crop the secure image.
    
    -   Image compression:
        
        const srcSecImageBuffer = new  ArrayBuffer(461844);// Replace it with the secure image buffer obtained from Camera Kit.
        
        let properties: Array<trustedAppService.SecImageProcParams> = \[
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_PROC\_OPERATION,
            value: trustedAppService.SecImageProcOperation.SECIMAGE\_COMPRESSION,
          },
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT,
            value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21, // The input image format is YUV420 NV21 for both the secure image compression and cropping commands.
          },
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT,
            value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_JPEG, // The image format returned by the secure image compression command is JPEG.
          },
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_COMPRESSION\_QUALITY,
            value: 90, // Replace it with the compression quality required by the service scenario.
          },
        \];
        let procParams: trustedAppService.SecImageProcParamsArray = {
          properties: properties,
        };
        await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
          (returnResult: trustedAppService.SecImageBuffer): void => {
            let returnSecImageBuffer = returnResult.secImage;
          }
        ).catch(
          (error: BusinessError): void => {
            let err = error as BusinessError;
            hilog.error(0x0000, 'testTag', \`Failed to process secureImage cropping, code:${err.code}, message:${err.message}\`);
          }
        );
        
    
    -   Image cropping:
        
        const srcSecImageBuffer = new  ArrayBuffer(461844);// Replace it with the secure image buffer obtained from Camera Kit.
        
        let properties: Array<trustedAppService.SecImageProcParams> = \[
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_PROC\_OPERATION,
            value: trustedAppService.SecImageProcOperation.SECIMAGE\_CROPPING,
          },
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT,
            value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21, // The input image format is YUV420 NV21 for both the secure image compression and cropping commands.
          },
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT,
            value: trustedAppService.SecImageProcFormat.SECIMAGE\_FORMAT\_YUV\_NV21, // The image format returned by the secure image cropping command is YUV420 NV21.
          },
          {
            tag: trustedAppService.SecImageProcTag.SECIMAGE\_TAG\_CROP\_REGION,
            value: { x : 0, y : 0, width : 320, height : 240 }, // Replace the value with the cropping area range required by the service scenario.
          },
        \];
        let procParams: trustedAppService.SecImageProcParamsArray = {
          properties: properties,
        };
        await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
          (returnResult: trustedAppService.SecImageBuffer): void => {
            let returnSecImageBuffer = returnResult.secImage;
          }
        ).catch(
          (error: BusinessError): void => {
            let err = error as BusinessError;
            hilog.error(0x0000, 'testTag', \`Failed to process secureImage cropping, code:${err.code}, message:${err.message}\`);
          }
        );
        
    
4.  End the attestation session.
    
    // Parameters for ending the attestation session.
    const finalProperties: Array<trustedAppService.AttestParam> = \[
      {
        tag: trustedAppService.AttestTag.ATTEST\_TAG\_DEVICE\_TYPE,
        value: trustedAppService.AttestType.ATTEST\_TYPE\_SECIMAGE\_PROCESS
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
    
    To destroy the attestation key, call the [destroyAttestKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api#section19260221152819) API after the attestation session ends. Image security verification, location security verification, and secure image compression and cropping share the same attestation key. Before destroying an attestation key, ensure that the other functions are not using the attestation key.
