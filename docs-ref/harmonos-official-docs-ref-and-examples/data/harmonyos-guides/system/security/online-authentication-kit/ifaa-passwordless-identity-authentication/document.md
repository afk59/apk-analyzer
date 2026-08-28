# IFAA Passwordless Identity Authentication

#### Use Cases

-   Enable IFAA passwordless identity authentication based on specified biometric features (fingerprints or 3D faces) of users on mobile devices.
-   Perform IFAA passwordless identity authentication based on biometric features (fingerprints or 3D faces) of users on mobile devices. When the specified biometric features of users are used, the authentication will succeed. When non-specified biometric features are used, the authentication will fail.
-   Disable IFAA passwordless identity authentication based on specified biometric features (fingerprints or 3D faces) of users on mobile devices.

#### Basic Concepts

The IIFAA alliance defines and maintains a biometric recognition framework that outlines how biometric data can be used for identity authentication.

#### Required Permissions

**ohos.permission.ACCESS\_BIOMETRIC**: permission for biometric recognition.

#### Restrictions

-   Your app can obtain signature data from the IIFAA central server after accessing the IIFAA alliance.
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

**Table 1** APIs required for enabling, performing, and disabling IFAA passwordless identity authentication
| 
API

 | 

Description

 |
| :-- | :-- |
| 

[register](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-ifaa-api#section52104409318)(registerData: Uint8Array): Promise<Uint8Array>

 | 

Enables IFAA passwordless identity authentication based on a biometric information type (fingerprint or 3D face) of a specified user.

 |
| 

[auth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-ifaa-api#section13182438548)(authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array>

 | 

Performs IFAA passwordless identity authentication using the biometric information type of a specified user.

 |
| 

[deregisterSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-ifaa-api#section9272165315411)(deregisterData: Uint8Array): void

 | 

Disables IFAA passwordless identity authentication based on a biometric information type (fingerprint or 3D face) of a specified user.

 |
| 

[getAnonymousIdSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-ifaa-api#section107341055618)(userToken: Uint8Array): Uint8Array

 | 

Obtains the ID of a mobile device.

 |

#### Development Procedure

1.  Enable IFAA passwordless identity authentication.
    
    import { ifaa } from '@kit.OnlineAuthenticationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Construct TLV input parameters based on the IIFAA protocol, convert them into **Uint8Array** parameters, and call the **ifaa.getAnonymousIdSync** API. Replace **new Uint8Array(\[0\])** with the user ID defined by yourself.
    let arg = new Uint8Array(\[0\]);
    let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);
    
    // Use **getAnonIdResult** to obtain the signed registration data from the server.
    // Convert the registration data (in TLV format of the IIFAA protocol) to **Uint8Array** and then use the **ifaa.register** API. Replace **new Uint8Array(\[0\])** with valid data.
    let TLV\_Register\_fp = new Uint8Array(\[0\]);
    let registerPromise: Promise<Uint8Array> = ifaa.register(TLV\_Register\_fp);
    registerPromise.then(registerResult => {
      console.info("Succeeded in doing register.");
      // The enabling is successful. Obtain the result of **ifaa.register** and process it.
    }).catch((err: BusinessError) =>{
      console.error(\`Failed to call register. Code: ${err.code}, message: ${err.message}\`);
      // The enabling fails. Obtain the error of **ifaa.register** and process it.
    });
    
2.  Perform IFAA passwordless identity authentication.
    
    import { ifaa } from '@kit.OnlineAuthenticationKit';
    import { userAuth } from '@kit.UserAuthenticationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Construct TLV input parameters based on the IIFAA protocol, convert them into **Uint8Array** parameters, and call the **ifaa.getAnonymousIdSync** API. Replace the **arg** value with your custom data.
    let arg = new Uint8Array(\[0\]);
    let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);
    
    // Use **getAnonIdResult** to obtain the signed authentication data from the server.
    
    // Obtain **challenge** of the passwordless payment.
    let ifaaChallenge: Uint8Array = ifaa.preAuthSync();
    let authParam: userAuth.AuthParam = {
      challenge: ifaaChallenge,
      authType: \[userAuth.UserAuthType.FINGERPRINT\],
      authTrustLevel: userAuth.AuthTrustLevel.ATL4,
    };
    // Use **preAuthResult** to request identity authentication.
    let userAuthInstance = userAuth.getUserAuthInstance(authParam,  {title: ' '});
    userAuthInstance.on('result', {
      async onResult (result) {
        let authToken = result.token;
        try {
          // After biometric features are successfully authenticated, call IFAA authentication.
          console.info("IFAA auth start");
          // Convert the authentication data (in TLV format of the IIFAA protocol) to **Uint8Array** and then use the **ifaa.auth** API. Replace **new Uint8Array(\[0\])** with valid data.
          let TLV\_Auth\_fp = new Uint8Array(\[0\]);
          // Select the synchronous or asynchronous API based on service requirements.
          let authResult: Uint8Array = ifaa.authSync(authToken, TLV\_Auth\_fp);
          console.info("authSyn authResult" + authResult);
          // Process **authResult**.
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call auth. Code is ${err.code}, message is ${err.message}\`);
        }
      }
    });
    userAuthInstance.start();
    
3.  Disable IFAA passwordless identity authentication.
    
    import { ifaa } from '@kit.OnlineAuthenticationKit'
    
    // Construct TLV input parameters based on the IIFAA protocol, convert them into **Uint8Array** parameters, and call the **ifaa.getAnonymousIdSync** API. Replace **new Uint8Array(\[0\])** with the user ID defined by yourself.
    let arg = new Uint8Array(\[0\]);
    let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(arg);
    
    // Use the result of **getAnonymousId** to obtain the signed deregistration data from the server.
    // Convert the deregistration data (in TLV format of the IIFAA protocol) to **Uint8Array** and then use the **ifaa.deregisterSync** API. Replace **new Uint8Array(\[0\])** with valid data.
    let TLV\_deregister\_fp = new Uint8Array(\[0\]);
    ifaa.deregisterSync(TLV\_deregister\_fp);
    

#### FAQs

Symptom: IFAA passwordless identity authentication fails to be enabled.

Possible cause: The mobile device is not connected to the Internet.

Procedure: Connect the mobile device to the Wi-Fi or hotspot and try again.
