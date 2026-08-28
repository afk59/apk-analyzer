# Integration Design Practice

This topic walks you through on how to implement key attestation and verify security-critical service requests for an application that requires user login. In this case, the user ID is associated with the key for security purposes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/KGcBQ7FGR1Oua0LjbbkhcQ/en-us_image_0000002301859046.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A56F94E0760788C6CFDB79C34145C9400BC720CF988B9D1883C64127B156FCE)

The sample code in this topic is applicable to the application that requires user login (the user ID is associated with the application key for security purposes).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/kDoyne6RQS2SnxHlTYKEcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A15495789B71B3DAF5CB9256F62B3795B7A4728AAA7F0E2D79A0195DBE5150D)

If user login is not involved in your application:

1.  The key attestation process is triggered when the application is started.
2.  During device-cloud processing, the user ID does not need to be carried or verified. The alias of the application public/private key pair has a fixed value of **serviceKey**.

#### Key Attestation and Storage Process

The key attestation and storage process is triggered only once after a user successfully logs in.

1.  **Check whether the application public/private key pair exists in the universal keystore.** The alias of the public/private key pair is in the **serviceKey** + _User\_ID_ format.
    
    If the application public/private key pair exists, the user has logged in to the device and the process ends. Otherwise, go to step 2.
    
2.  **Create a public/private key pair for the application.** Create an asymmetric key pair (including a public key and a private key), for example, an RSA or EC key pair, for device attestation.
    
3.  **Obtain a challenge value.** To prevent replay attacks in step 6, you are advised to obtain a one-time challenge value from the application server. The application server uses a random number to generate a challenge value and caches it to the server. The cache contains the following fields:
    
    User ID, challenge value, and service process (for example "key attestation and storage process")
    
4.  **Attest the public key.** The Universal Keystore Kit API is called to prove the generated public key and the called application identity, attesting that the public key comes from a real device. The application passes in the challenge value.
5.  **Obtain the key attestation certificate chain.** Universal Keystore Kit returns the key attestation certificate chain, which includes the application public key, challenge value, and application identity.
6.  **Send the key attestation certificate chain.** The application sends the key attestation certificate chain to the application server.
    
    (1) The request message includes the user ID, key ID, and key certificate chain.
    
    (2) The key ID is a hash value of the application public key. For instance, Key ID = base64 (SHA-256, application public key). The public key can be obtained by using the [key export APIs](../../other-operations/exporting-a-key/exporting-a-key-arkts/document.md) of Universal Keystore Kit.
    
7.  **Verify the key attestation certificate chain.** The application server uses the root certificate provided by the Universal Keystore Kit official website to verify the validity of the certificate chain, challenge value, and application identity.
    
    (1) Verify the certificate chain validity and parse the application public key, challenge value, application identity information, and key management component ID.
    
    (2) Based on the user ID and challenge in the request message, check for the record with the "key attestation and storage process" in the server cache, and delete the challenge record if a match is found.
    
    (3) Check whether the application identity information, including the bundle name and application signature key, is the same as expected.
    
    (4) Check whether the key management component ID is **0x28c4fb4944afec11b9090242ac120002**, which indicates Universal Keystore Kit.
    
8.  **Save the application public key.** After a successful attestation, the application server saves the application public key parsed from the key attestation certificate to its database.
    
    The database record includes the following fields: user ID, key ID, and application public key.
    

#### Service Request Verification Process

The service request verification process is triggered when the application processes security-critical services, such as rush purchase or coupon claiming.

1.  **Obtain a challenge value.** The application obtains a one-time challenge value from the application server. The application server uses a random number to generate a challenge value and caches it to the server. The cache contains the following fields:
    
    User ID, challenge value, and service process (for example "key usage process")
    
2.  **Use the application private key to sign a service request.** Call the Universal Keystore Kit API to sign the service data using the specified application private key.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/MOioHJn8TfOMg51mzl5k6A/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48D0917F03CE181E325827D1E45363B05CA3D26F6CB29A47AC13A9E88A8BDC3F)
    
    Sign the challenge and service request data.
    
3.  **Obtain the signature data.** Universal Keystore Kit returns the signature data to the application.
4.  **Send a service request.** The application sends a service request to the application server.
    
    (1) The request message includes the user ID, public key ID of the application, challenge, and signature data.
    
    (2) The key ID is a hash value of the public key.
    
5.  **Search for the application public key based on the public key ID.** The application server searches for the application public key based on the ID of the application public key, and verifies the challenge value.
    
    (1) Based on the user ID and challenge in the request message, check for the record with the "key usage process" in the server cache, and delete the challenge record if a match is found.
    
    (2) Query the application public key from the database based on the user ID and key ID.
    
6.  **Verify the signature of the request using the application public key.** The application server uses the application public key to verify the signature in the request.
7.  **If the application public key does not exist in the server's database,** the server returns an error code to the application, indicating that the application public key is not registered.
    
    Then, the application performs steps 1.3 to 1.8 shown in the figure. If the key attestation is successful and the key is stored, the application performs steps 2.1 to 2.6.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/IA1P4KZJQXue4TG8zr189A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96A2AC225862325B7BC08E1B9BC1F687C022D9FE12718780D1D4A7639C1916E0)
    
    The application may delete unused application public key records to ensure adequate database capacity on the server. This will trigger step 7 in the process.
