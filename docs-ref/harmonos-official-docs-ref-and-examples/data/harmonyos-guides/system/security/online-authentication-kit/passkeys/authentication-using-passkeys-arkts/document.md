# Authentication Using Passkeys (ArkTS)

#### API Description

The following table lists the main APIs provided by the passkey service.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getClientCapabilities](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section1122315266414)(context: common.Context): Promise<Map<[ClientCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section44620019103), boolean>>

 | 

Queries the client capabilities supported by the current device or version.

 |
| 

[getPlatformAuthenticators](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section36194215542)(context: common.Context): Promise<Array<[AuthenticatorMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section107571524911)\>>

 | 

Queries the platform authenticator capabilities (face, fingerprint, and PIN) supported by the current device or version.

 |
| 

[register](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section1447385117810)(context: common.Context, options: [CredentialCreationOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section3125554145615), tokenBinding?: [TokenBinding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section3745131173015)): Promise<[PublicKeyAttestationCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section10797172295315)\>

 | 

Registers a passkey.

 |
| 

[authenticate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section193521359131510)(context: common.Context, options: [CredentialRequestOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section433810416530), tokenBinding?: [TokenBinding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section3745131173015)): Promise<[PublicKeyAssertionCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-passkey-api#section16498195211554)\>

 | 

Performs authentication using a passkey.

 |

#### Development Procedure

The passkey service provides a FIDO client implementation based on FIDO2 standards. The following only demonstrates the usage of FIDO client APIs. You are responsible for implementing the logic related to the FIDO server. For details, please refer to [FIDO2 standards](https://fidoalliance.org/passkeys/) (here is the [website link disclaimer](../../website-link-disclaimer/document.md)).

1.  Deploy the FIDO server in accordance with FIDO2 standards.
2.  Import required modules.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { UIContext } from '@kit.ArkUI';
    import { common } from '@kit.AbilityKit';
    import { fido2 } from '@kit.OnlineAuthenticationKit';
    
3.  Register a passkey.
    1.  Obtain capability information. Call the **getClientCapabilities** API to obtain the client capability list, and call the **getPlatformAuthenticators** API to obtain the platform authenticator capability list.
        
        uiContext1: UIContext = this.getUIContext();
        uiContext: common.UIAbilityContext = this.uiContext1.getHostContext() as common.UIAbilityContext; // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
        
        try {
          // Obtain the client capability list.
          let clientCapabilities: Map<fido2.ClientCapability, boolean> = await fido2.getClientCapabilities(this.uiContext);
          console.info("Succeeded in doing getClientCapabilities.");
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(\`Failed to call getClientCapabilities error code is ${code}, message is ${message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
        }
        
        try {
          // Obtain the platform authenticator capability list.
          let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
            await fido2.getPlatformAuthenticators(this.uiContext);
          console.info("Succeeded in doing getPlatformAuthenticators.");
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(\`Failed to call getPlatformAuthenticators error code is ${code}, message is ${message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
        }
        
    2.  Access the FIDO server, obtain the registration message, and call the **register** API for registration.
        
        // **pkOptions** is the registration message obtained by the app from the FIDO server, and **credentialCreationOp** is the registration information assembled by the app.
        let credentialCreationOp: fido2.CredentialCreationOptions = {
          publicKey: pkOptions
        };
        
        try {
          // Call **register** to register a passkey.
          let publicKeyAttestationCredential: fido2.PublicKeyAttestationCredential =
            await fido2.register(this.uiContext, credentialCreationOp);
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(\`Failed to call register error code is ${code}, message is ${message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
        }
        
    3.  Assemble a registration response message based on the registration result (**publicKeyAttestationCredential**), send the message to the FIDO server for verification, and obtain the registration result message.
4.  Use the password for authentication.
    1.  Obtain capability information. Call the **getClientCapabilities** API to obtain the client capability list, and call the **getPlatformAuthenticators** API to obtain the platform authenticator capability list.
        
        // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
        let uiContext: common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
        
        try {
          // Obtain the client capability list.
          let clientCapabilities: Map<fido2.ClientCapability, boolean> = await fido2.getClientCapabilities(this.uiContext);
          console.info("Succeeded in doing getClientCapabilities.");
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(\`Failed to call getClientCapabilities error code is ${code}, message is ${message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
        }
        
        try {
          // Obtain the platform authenticator capability list.
          let platformAuthenticators: Array<fido2.AuthenticatorMetadata> =
            await fido2.getPlatformAuthenticators(this.uiContext);
          console.info("Succeeded in doing getPlatformAuthenticators.");
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(\`Failed to call getPlatformAuthenticators error code is ${code}, message is ${message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
        }
        
    2.  Access the FIDO server, obtain the authentication message, and call the **authenticate** API for authentication.
        
        // **authPub** is the authentication message obtained by the app from the FIDO server, and **authCredentialRequestOptions** is the authentication information assembled by the app.
        let authCredentialRequestOptions: fido2.CredentialRequestOptions = {
          publicKey: authPub,
          mediation: "optional" as fido2.CredentialMediationRequirement
        }
        
        try {
          // Call the **authenticate** API to perform authentication.
          let pkAssertionCredential: fido2.PublicKeyAssertionCredential =
            await fido2.authenticate(this.uiContext, authCredentialRequestOptions);
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          console.error(\`Failed to call authenticateerror code is ${code}, message is ${message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
        }
        
    3.  Assemble an authentication response message based on the authentication result (**pkAssertionCredential**), send the message to the FIDO server for verification, and obtain the authentication result message.
