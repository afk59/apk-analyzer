# Verifying the Signature

To perform on-device verification of the signature to determine a secure image or geographical location, you can use [Crypto Architecture Kit](../../../../crypto-architecture-kit/about-this-kit/document.md). For details, please refer to [Signing and Signature Verification with an ECDSA Key Pair](../../../../crypto-architecture-kit/signing-and-signature-verification/signing-and-signature-verification-development/signing-and-signature-verification-with-an-ecdsa-key-pair-arkts/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Enk-TpaLQz-ieZXEuvKp8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B99522C44DE489B855386DD8240E688738F7682E9B8CC97834566BD0D682330B)

You are advised to verify the signature of image data or geographical location data on your app server.

#### Obtaining the Signature Data

## Format of the Data to Verify Image Security

The structure of the data to verify image security is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/P4pXMoe_Qe-w6npaXd0Z3Q/en-us_image_0000002515108423.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=507C20CFA670067119C4A2E77D8979F901C1373D07571F29B425D3F287A64E2B "Click to enlarge")

The user data and image data are the original data to be signed. The image data has a fixed length of 460,800 bytes. The signature data is encoded using Base64. Your app needs to parse these parts of data to verify the signature. The sample code is as follows:

import { util } from '@kit.ArkTS';

// Obtain the original data to be signed.
const secureImageBuffer = new ArrayBuffer(461844); // Replace it with the secure image buffer obtained from Camera Kit.
const view = new DataView(secureImageBuffer);
const imageBufferLength = 460800; // The image buffer has a fixed length of 460,800 bytes.
const userDataLength = view.getUint32(0, true); // Obtain the user data length.
const originData = secureImageBuffer.slice(4, 4 + userDataLength + imageBufferLength);
// Obtain the signature data.
const maxSignatureBufferLength = 512;
const signatureBuffer = secureImageBuffer.slice(4 + userDataLength + imageBufferLength,
  4 + userDataLength + imageBufferLength + maxSignatureBufferLength);
const signatureString = String.fromCharCode(...new Uint8Array(signatureBuffer).filter(code => code !== 0));
const base64Helper = new util.Base64Helper();
const signatureData = base64Helper.decodeSync(signatureString);

## Format of the Secure Image Data After Compression and Cropping

The structure of the secure image data after compression and cropping is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/K07YEA_pR-uaXripc_7yGA/en-us_image_0000002482788466.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEF4F873E9AF22D42C49E83B5163D83DBB15A8B6E9C1E30A400B97CB53425C52 "Click to enlarge")

The returned secure image data after processing contains the following information:

1.  **Magic**: The default value is **0x53494D47** currently. You can check the value of **Magic** to verify the correctness of returned image data.
2.  **Version**: The default value is **1** currently. You can check the value of **Version** to verify the correctness of returned image data.
3.  User data length (16 to 127 bytes) and user data: The user data is passed when you call **initializeAttestContext** to initialize the attestation session.
4.  Image data length, image width (unit: pixel, value range: 0–640), image height (unit: pixel, value range: 0–480), and image data
5.  Signature data: encoded using Base64

The user data and image data are the original data to be signed. Your app needs to parse these parts of data to verify the signature. The sample code is as follows:

import { util } from '@kit.ArkTS';

let offset = 0;
const secureImageBuffer = new ArrayBuffer(461844); // Replace it with the secure image buffer obtained from Camera Kit.
const view = new DataView(secureImageBuffer);
const magic = view.getUint32(offset, true); // Obtain the **Magic** field of the secure image. Its default value is **0x53494D47**.
offset += 4;
const version = view.getUint32(offset, true); // Obtain the **Version** field of the secure image. Its default value is **1**.
offset += 4;
const userDataLength = view.getUint32(offset, true); // Obtain the user data length.
offset += 4;
const userdata = secureImageBuffer.slice(offset, offset + userDataLength);
offset += userDataLength;
const imageLen = view.getUint32(offset, true); // Obtain the length of the image data after compression and cropping.
offset += 4;
const imageWidth = view.getUint32(offset, true); // Obtain the image width, in pixels.
offset += 4;
const imageHeight = view.getUint32(offset, true); // Obtain the image height, in pixels.
offset += 4;
const imageBuffer = secureImageBuffer.slice(offset, offset + imageLen);
offset += imageLen;
// Obtain the original data to be signed.
const totalLength = userdata.byteLength + imageBuffer.byteLength;
const originData = new Uint8Array(new ArrayBuffer(totalLength));
originData.set(new Uint8Array(userdata), 0);
originData.set(new Uint8Array(imageBuffer), userdata.byteLength);
// Obtain the signature data.
const maxSignatureLength = 512;
const signatureBuffer = secureImageBuffer.slice(offset, offset + maxSignatureLength);
const signatureString = String.fromCharCode(...new Uint8Array(signatureBuffer).filter(code => code !== 0));
const base64Helper = new util.Base64Helper();
const signatureData = base64Helper.decodeSync(signatureString);

## Format of the Data to Verify Location Security

For details about the structure of the data to verify location security, please refer to [TrustedAppService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-taas-api).

To verify the signature in the data to verify location security, the data in the returned structure needs to be concatenated into a character string. The format requirements are as follows:

1.  The data must be arranged in the following order: latitude, longitude, altitude, accuracy, timestamp, and user data.
2.  The latitude, longitude, and altitude are floating-point numbers accurate to 15 decimal places. The accuracy is a floating-point number accurate to 6 decimal places. The timestamp is a 64-bit positive integer. The user data is a character string.
3.  Use commas (,) to separate different parts of data.

The signature data is encoded using Base64. The following is the reference code for obtaining the signature and the original data that is signed. Note that the reference code does not include exception handling, which should be implemented by yourself based on service needs.

import { trustedAppService } from '@kit.DeviceSecurityKit';
import { util } from '@kit.ArkTS';

// The following are sample values, provided only to demonstrate how to obtain the original data and signature data.
const location: trustedAppService.Location = {
  latitude: 40.053903635898685,
  longitude: 116.17356591910897,
  altitude: 0,
  accuracy: 11.160304069519043,
  timestamp: 1722151680187
};
const userData = "trusted\_app\_service\_userdata";
const secureLocation: trustedAppService.SecureLocation = {
  originalLocation: location,
  userData: userData,
  signature: "MEQCIEAcJHgaU8aAoMqD1wgoxiXR5I4jmwVG6ncgSKkW4uBHAiBnfv96T+gt1ef83kNZ+U0gBLsq9byuBLP1RBx30hByuQ=="
};
// Obtain the original data.
const originString = secureLocation.originalLocation.latitude.toFixed(15) + ',' +
  secureLocation.originalLocation.longitude.toFixed(15) + ',' +
  secureLocation.originalLocation.altitude.toFixed(15) + ',' +
  secureLocation.originalLocation.accuracy.toFixed(6) + ',' +
  secureLocation.originalLocation.timestamp + ',' + secureLocation.userData.toString();
const textEncoder = new util.TextEncoder();
const originData = textEncoder.encodeInto(originString);
// Obtain the signature data.
const base64Helper = new util.Base64Helper();
const signatureData = base64Helper.decodeSync(secureLocation.signature.toString());

#### Verifying the Signature

Image security verification and location security verification share the same attestation key. Therefore, the signature verification process is the same. The following provides the reference code for signature verification based on the original data and signature data obtained in [Image Security Verification](../../image-security-verification/document.md) and [Location Security Verification](../../location-security-verification/document.md). Note that the reference code does not include exception handling, which should be implemented by yourself based on service needs.

1.  Obtain the public key from an anonymous certificate chain.
    
    import { cert } from '@kit.DeviceCertificateKit';
    import { cryptoFramework } from '@kit.CryptoArchitectureKit';
    import { util } from '@kit.ArkTS';
    import { trustedAppService } from '@kit.DeviceSecurityKit';
    
    // Take image security verification as an example (ignoring exception handling).
    const userData = "trusted\_app\_service\_demo";
    const deviceId = 7483679320805398131;
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
    const returnResult = await trustedAppService.initializeAttestContext(userData, initOptions);
    // Parse the anonymous certificate chain data to obtain the level-3 certificate.
    const certChain = returnResult.certChains;
    const certList = certChain\[0\].split('-----BEGIN CERTIFICATE-----');
    const thirdCert = '-----BEGIN CERTIFICATE-----' + certList\[1\];
    // Obtain the public key.
    const textEncoder = new util.TextEncoder();
    const encodingBlob: cert.EncodingBlob = {
      data: textEncoder.encodeInto(thirdCert),
      encodingFormat: cert.EncodingFormat.FORMAT\_PEM
    };
    const x509Cert = await cert.createX509Cert(encodingBlob);
    const asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
    const keyPair = asyKeyGenerator.convertKeySync(x509Cert.getPublicKey().getEncoded(), null);
    const pubKey = keyPair.pubKey; // The public key in the certificate needs to be converted into a format required by the cryptoFramework.
    
2.  Create a **verify** instance whose asymmetric key type is **ECC256** and digest algorithm is **SHA256**, and use the public key obtained in [Step 1](#li67510253287) for initialization.
    
    const verifier = cryptoFramework.createVerify('ECC256|SHA256');
    verifier.initSync(pubKey);
    
3.  Use the original data and signature data to verify the signature.
    
    const originData = ...; // Use the obtained original image data.
    const signatureData = ...; // Use the obtained signature data.
    const inputData: cryptoFramework.DataBlob = {
      data: new Uint8Array(originData)
    };
    const signature: cryptoFramework.DataBlob = {
      data: new Uint8Array(signatureData)
    };
    // Verify the signature data.
    const result = verifier.verifySync(inputData, signature);
