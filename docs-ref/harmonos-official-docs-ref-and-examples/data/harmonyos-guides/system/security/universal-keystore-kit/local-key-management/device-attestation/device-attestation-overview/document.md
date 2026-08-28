# Device Attestation Overview

The device attestation provides the capabilities of verifying whether a service request is from a real device and an application with trusted source by using an X.509 certificate chain based on cryptographic algorithms. It helps ensure the system security by blocking untrusted applications and devices.

#### Highlights

-   Hardware-based device certificate authentication
-   Application identity authentication
-   Standard X.509 certificate format

#### Scenarios

The device attestation feature defends against the following risks and attacks:

-   **Emulators, cloud phones, and other non-real devices:** Only real devices have default device certificates, and only devices with certificates have this capability. Therefore, this feature ensures that requests are sent from real devices.
-   **Repackaged applications, counterfeit applications, and other applications without a trusted source**: The certificate chain for device attestation contains the application bundle name and hash value of the signature public key, which can be verified to ensure that all signed information comes from a trusted application.
-   **Modifying or forging application requests by capturing packets**: For important business requests that are signed with a private key, the device attestation can verify the integrity of important requests and prevent replay attacks by using a challenge.

You can use device attestation in the following scenarios and more:

-   **PIN-free payment of financial payment applications**: Financial application servers can verify the authenticity and security of the device that has PIN-free payment enabled, ensuring that the application runs in a real device and the key used for PIN-free payment is secure.
-   **Preventing bonus hunting with tools in marketing activities**: By verifying whether the request comes from a real device, we can prevent black markets from counterfeiting real devices (for example, by using emulators) and sending marketing activity requests such as lottery draws, flash purchases, and coupon redemption.
-   **Preventing game cheating or plug-in and attacking automated behavior**: The game server identifies whether the request comes from a real device and application identity, and recognizes the behavior of **repackaging, emulators, cloud phones**, and other cheating and automated behavior.

#### Relationship with Other Kits

[Device Certificate Kit](../../../../device-certificate-kit/about-this-kit/document.md) provides the attestation capability based on device certificates. [Universal Keystore Kit](../../../about-this-kit/document.md) provides the APIs.

#### Constraints

-   The device authenticity attestation capability supports only real devices, and the certificate chain to be verified for the emulator will fail.

## Service Quota

| 
API

 | 

Type

 | 

Quota Description

 |
| :-- | :-- | :-- |
| 

Anonymous key attestation API

 | 

35 times/second/app

 | 

By default, the instantaneous traffic of the anonymous key attestation API ([anonAttestKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksanonattestkeyitem11)/[OH\_Huks\_AnonAttestKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_anonattestkeyitem)) called by each application does not exceed 35 requests per second. If you need to change this service quota for your application, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

 |

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/-2CDIWjaQQ25rmqO2RNUuw/en-us_image_0000002302018746.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=778F2899B2BC01B07ACA7E2554FC8193BAA7C1615CA2253B03FAA37E18B290BF "Click to enlarge")

The device attestation capability verifies device authenticity and application identity using hardware-backed device certificates.

As shown in the figure, the process is as follows:

1.  The application calls the Universal Keystore Kit API to create a public/private key pair, which is stored in a hardware-backed secure environment.
2.  The application calls the Universal Keystore Kit API to issue a certificate chain, which contains the public key of the key pair and the application identity.
3.  Based on the certificate chain, the application server verifies that the public key comes from a real device and a trusted application.
4.  After successfully verifying the certificate chain, the application server saves the application public key in the certificate chain. When processing services (for example, in PIN-free payment or marketing activities), the application calls the Universal Keystore Kit API to sign service requests using the application private key. The application server uses the saved application public key to verify the signature.

#### Interaction Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/IjPuNT2dTQ2UO0rQ-UxoJw/en-us_image_0000002335818373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=563C25A2B974F386F1199FA38977BB1F599602A71496394E951553BCBA7DA378)

The development process of device attestation can be divided into two sub-processes:

1.  [Key attestation and storage process](#section57291448154110): Register and save the key attestation certificate of a real device and a correct application to the application server. This process is performed only once for a device or once when a user logs in.
    -   For the scenario where a user logs in, you are advised to perform the key attestation and storage process after the user logs in. The application server binds the user ID when saving the application public key to the database.
    -   For the scenario where no user logs in, you are advised to perform the key attestation and storage process when the application is started for the first time or when the device authenticity attestation capability is used for the first time. The application server saves the application public key to the database.
2.  [Service request verification process](#section165197911437): Use the application public key saved in the application server database to verify the service request. Do not carry the key attestation certificate chain in the service request.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/_lFRuWdqREeDkMcWMiLtSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03949ED20A655C0A11ED65858CF9B0FB6C860BFA5F5280A43D7CE9A29A9661C0)
    
    The device attestation server may limit the authentication traffic from a specific application to prevent traffic overload of a single application and subsequent processing failures of other applications. Therefore, do not attest the application public key for each service request.
    
    When the device attestation capability is unavailable due to traffic overload or other reasons, the application needs to consider the exception handling solution to prevent the unavailability of basic application functions.
    

## Key Attestation and Storage Process

1.  **Check whether the public/private key pair of the application exists.** If the public/private key pair of the application exists, the process ends (indicating that the application has completed the key attestation and storage process).
2.  **Create a public/private key pair for the application.** Create an asymmetric key pair (including a public key and a private key), for example, an RSA or EC key pair, for device attestation.
    
3.  **Obtain a challenge value.** To prevent replay attacks in step 7, you are advised to obtain a one-time challenge value from the application server. The application server uses a random number to generate a challenge value and caches it to the server.
4.  **Attest the public key.** The Universal Keystore Kit API is called to prove the generated public key and the called application identity, attesting that the public key comes from a real device. The application can pass in the challenge value.
5.  **Request the server to issue the key attestation certificate chain.** The device attestation server attests the authenticity of the device and issues the key attestation certificate chain.
6.  **Obtain the key attestation certificate chain.** Universal Keystore Kit returns the key attestation certificate chain, which includes the application public key, challenge value, and application identity.
7.  **Send the key attestation certificate chain.** The application sends the key attestation certificate chain to the application server.
8.  **Verify the key attestation certificate chain.** The application server uses the root certificate provided by the Universal Keystore Kit official website to verify the validity of the certificate chain, challenge value, and application identity.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/umKj1aaKTfSIBb-FL7u4mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A16A7C50450179AFB054796090C831193210400BB21191FBBD3B4B5DCB1D28D)
    
    Regardless of whether the verification is successful, the challenge value cached on the server must be deleted.
    
9.  **Save the application public key.** After a successful attestation, the application server saves the application public key parsed from the key attestation certificate to its database.

## Process of Verifying Service Requests

1.  **Obtain a challenge value.** To prevent replay attacks in step 4, it is recommended that the application obtain a one-time challenge value from the application server first. The application server uses a random number to generate a challenge value and caches it to the server.
2.  **Use the application private key to sign a service request.** Call the Universal Keystore Kit API to sign the service data using the specified application private key.
3.  **Obtain the signature data.** Universal Keystore Kit returns the signature data to the application.
4.  **Send a service request.** The application sends a service request to the application server. The service request carries the signature data, ID of the application public key, and challenge value.
5.  **Search for the application public key based on the public key ID.** The application server searches for the application public key based on the ID of the application public key, and verifies the challenge value.
6.  **Verify the signature of the request using the application public key.** The application server uses the application public key to verify the signature in the request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/x2RWDc0DRTSxJ9KfbIYyzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B31D6E94BF60E96FA8F2B7D6E6E1E84BAFE19E3E7926D27A41B1A0CA31FC6E9F)

Regardless of whether the verification is successful, the challenge value cached on the server must be deleted.
