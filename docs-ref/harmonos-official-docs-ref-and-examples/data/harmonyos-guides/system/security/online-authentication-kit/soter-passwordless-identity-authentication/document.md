# SOTER Passwordless Identity Authentication

#### Use Cases

Users can use biometric features, instead of traditional passwords, to implement passwordless identity authentication.

-   Enable SOTER passwordless identity authentication based on biometric features (fingerprints or 3D faces) on mobile devices.
-   Perform SOTER passwordless identity authentication based on biometric features (fingerprints or 3D faces) on mobile devices.
-   Disable SOTER passwordless identity authentication based on biometric features (fingerprints or 3D faces) on mobile devices.

#### Basic Concepts

SOTER is a biometric authentication platform and standard that enables services to use sensors (such as face sensors and fingerprint sensors) on devices to perform secure and efficient passwordless sign-in and payment. Currently, SOTER has been widely used in service scenarios such as WeChat mini programs and official accounts as well as fingerprint payment.

#### Required Permissions

-   **ohos.permission.INTERNET**: permission to access the Internet.
-   **ohos.permission.VIBRATE**: permission to vibrate.
-   **ohos.permission.ACCESS\_BIOMETRIC**: permission for biometric recognition.

#### Restrictions

-   You need to deploy the SOTER server for your app.
-   Mobile devices must support biometric features (fingerprints or 3D faces). Check whether a mobile device supports the ATL4 authentication trust level.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { userAuth } from '@kit.UserAuthenticationKit';
    
    try {
    // Example: Check whether the device supports the ATL4 authentication trust level for facial recognition.
      userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
      console.info('current auth trust level is supported');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}\`);
    }
    
-   Mobile devices must be connected to the Internet to use the service.

#### API Description

**Table 1** APIs required for enabling, performing, and disabling SOTER passwordless identity authentication
| 
API

 | 

Description

 |
| :-- | :-- |
| 

[generateAppSecureKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section14596181356)(keyType: [KeyType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section186410451429)): Promise<Uint8Array>

 | 

Generates an app secure key.

 |
| 

[generateAuthKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section425383419374)(keyAlias: string, keyType: [KeyType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section186410451429)): Promise<[SignedResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section13572542154913)\>

 | 

Generates an authentication key.

 |
| 

[generateChallengeSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section9821133893810)(keyAlias: string): Uint8Array

 | 

Generates a challenge.

 |
| 

[signWithAuthKeySync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section20654821123913)(keyAlias: string, authToken: Uint8Array, info: string): [SignedResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section13572542154913)

 | 

Uses an authentication key to sign service data.

 |
| 

[deleteAuthKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-soter-api#section157772313406)(keyAlias: string): Promise<void>

 | 

Deletes an authentication key.

 |

#### Development Procedure

1.  Import the SOTER modules.
    
    import { soter } from '@kit.OnlineAuthenticationKit';
    import { userAuth } from '@kit.UserAuthenticationKit';
    
2.  Generate an app secure key and authentication key, which will be used for the subsequent enabling and authentication processes.
    
    let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Encryption type. Only ECC\_P256 is supported.
    let keyAlias: string = 'keyAlias'; // Customize a key alias for yourself.
    
    // Generate an app secure key.
    let appSecureKey: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
    // Generate an authentication key.
    let authKey: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
    
3.  Use the authentication key for signature to implement SOTER passwordless authentication.
    
    let keyType: soter.KeyType = soter.KeyType.ECC\_P256; // Encryption type. Only ECC\_P256 is supported.
    let keyAlias: string = 'keyAlias'; // Customize a key alias for yourself.
    let info: string = 'Message to be signed.'; // Here, **info** needs to be delivered by your app server. The SOTER service will sign the data and then upload the data to your app server.
    
    // Obtain **challenge** of the passwordless payment.
    let soterChallenge: Uint8Array = soter.generateChallengeSync(keyAlias);
    let authParam: userAuth.AuthParam = {
      challenge: soterChallenge,
      authType: \[userAuth.UserAuthType.FINGERPRINT\],
      authTrustLevel: userAuth.AuthTrustLevel.ATL4,
    };
    // Use **preAuthResult** to request identity authentication.
    let userAuthInstance = userAuth.getUserAuthInstance(authParam,  {title: ' '});
    // If **authToken** is not obtained, error code 1 is returned.
    userAuthInstance.on('result', {
      async onResult (result) {
        let authToken = result.token;
        try {
          // After biometric features are successfully authenticated, call SOTER authentication.
          console.info('soter auth start');
          // Use the **soter.signWithAuthKeySync** API to sign the data to be authenticated. You can choose to return the result synchronously or asynchronously based on your service needs.
          let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info);
          console.info('Succeeded in doing authSyn authResult');
          // Process **authResult**.
        } catch (err) {
          console.error(\`Failed to signWithAuthKeySync. Code: ${err.code}, message: ${err.message}\`);
        }
      }
    });
    userAuthInstance.start();
    
4.  Delete the authentication key once passwordless authentication is disabled.
    
    // Delete the authentication key.
    soter.deleteAuthKey(keyAlias);
