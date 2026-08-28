# FIDO Passwordless Identity Authentication

#### Use Cases

-   Enable FIDO passwordless identity authentication based on existing biometric features of users.
-   Perform FIDO passwordless identity authentication based on existing biometric features of users.
-   Disable FIDO passwordless identity authentication based on existing biometric features of users.

#### Basic Concepts

Before you get started, be sure to understand the following basic concepts:

-   FIDO protocols
    
    FIDO is a set of identity authentication standards released and maintained by the FIDO Alliance. The FIDO specifications outline a technical framework for online identity authentication.
    
-   UAF
    
    UAF is a universal authentication framework. It aims to provide users with passwordless identity authentication experience through biometric recognition (such as fingerprint recognition) and encryption technologies.
    

#### Required Permissions

**ohos.permission.ACCESS\_BIOMETRIC**: permission for biometric recognition.

#### Restrictions

This function can be used only when the following conditions are met:

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
    
-   The FIDO service needs to be connected to the Internet to provide a complete online identity authentication service. Before calling FIDO service APIs, your app must explicitly inform users of the Internet connection behavior required by the FIDO service and obtain user consent.

#### API Description

Your app can call APIs to enable, use, and disable the FIDO passwordless identity authentication function.

**Table 1** Functions of the FIDO passwordless identity authentication APIs
| 
API

 | 

Description

 |
| :-- | :-- |
| 

[discover](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section144826162913)(context: common.Context): Promise<[DiscoveryData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section11682103284015)\>

 | 

Discovers the authentication capability of a device and returns the authenticator data supported by the current device software.

 |
| 

[checkPolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section86041155123616)(context: common.Context, uafRequest: [UAFMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section2134351143710)): Promise<void>

 | 

Checks whether a message complies with an operation-specific policy.

 |
| 

[processUAFOperation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section7520171415134)(context: common.Context, uafRequest: [UAFMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section2134351143710), channelBindings?: [ChannelBinding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section1081123302517)): Promise<[UAFMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section2134351143710)\>

 | 

User UAF operation API, which processes UAF protocol messages.

 |
| 

[notifyUAFResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section4815641306)(context: common.Context, uafResponse: [UAFMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/onlineauthentication-fido-api#section2134351143710)): Promise<void>

 | 

Notifies the enabling result.

 |

#### Development Procedure

1.  Deploy the FIDO server in accordance with FIDO standards.
2.  Import required modules.
    
    import { fido } from '@kit.OnlineAuthenticationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
3.  Enable FIDO passwordless identity authentication.
    1.  Initialize authenticators.
        
        // To use **this.uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
        **//** Method: uiContext:common.UIAbilityContext = getHostContext(this) as common.UIAbilityContext;
        try {
          // Call the **discover** method to initialize authenticators.
          let discoverData = await fido.discover(this.uiContext);
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
        
    2.  Access the FIDO server, obtain the message for policy check, and check whether the user has enabled FIDO authentication.
        
        // **uafMessage** is the policy check message obtained from the FIDO server.
        let uafAuthMessage: fido.UAFMessage = {
          /\*
          Policy check message format: \[{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"","serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":\[\[{"aaid":\["001B#1001"\],"keyIDs":\["test keyIDs"\],"authenticationAlgorithms":\[1\]}\]\]}}\]
          \*/
          uafProtocolMessage: uafMessage, // Policy check message obtained from the server.
          additionalData: "" // (Optional) Additional information.
        };
        let isRegistered: boolean = true;
        try {
          // Check whether FIDO authentication is enabled.
          await fido.checkPolicy(this.uiContext, uafAuthMessage);
        } catch (error) {
          isRegistered = false;
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}\`);
          // Determine the status based on the error code and rectify the fault accordingly.
        }
        if (isRegistered) {
          console.info("has registered, no need to register again.");
          // Registered. The service executes the subsequent process as required.
        }
        
    3.  Access the FIDO server, obtain the registration message, and call the **processUAFOperation** API for FIDO registration.
        
        // **regMessage** is the registration message obtained from the FIDO server.
        let uafRegMessage: fido.UAFMessage = {
         /\*
          Registration message format: \[{"header":{"upv":{"major":1,"minor":0},"op":"Reg","appID":"","serverData":"test server data"},"challenge":"test challenge","username":"test user name","policy":{"accepted":\[\[{"aaid":\["001B#1001"\],"attachmentHint":1,"authenticationAlgorithms":\[1\],"authenticatorVersion":1}\]\]}}\]
          \*/
          uafProtocolMessage: regMessage, // Registration message obtained from the server.
          additionalData: "" // (Optional) Additional information.
        };
        // (Optional) Pass channel binding parameters.
        let channelBinding: fido.ChannelBinding = {};
        try {
          // Call the **processUAFOperation** API for FIDO registration.
          let messageResp = await fido.processUAFOperation(this.uiContext, uafRegMessage, channelBinding);
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
        
    4.  Send a registration response message to the FIDO server for verification and obtain the registration result message.
        
        // **notifyMessage** is the registration result message obtained from the FIDO server.
        let notifyMessage:string = "";
        let notifyUafMessage: fido.UAFMessage = {
          /\*
          Response message format: {"authenticatorsSucceeded":\[{"description":"Attention completed successfully.","aaid":"001B#1001","keyID":"test keyID"}\]}
          \*/
          uafProtocolMessage: notifyMessage, // Registration result message obtained from the server.
          additionalData: "" // (Optional) Additional information.
        };
        
    5.  Call **notifyUAFResult** to send the registration result notification.
        
        try {
          // Call **notifyUAFResult** to send the registration result notification.
          fido.notifyUAFResult(this.uiContext, notifyUafMessage).then(notify => {
            console.info("Succeeded in doing notifyUAFResult.");
          })
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call notifyUAFResult. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
        
4.  Perform FIDO passwordless identity authentication.
    1.  Initialize authenticators. (Skip this step if you have performed the initialization.)
        
        // Obtain the context of the current screen.
        try {
          // Call the **discover** method to initialize authenticators.
          let discoverData = await fido.discover(this.uiContext);
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
        
    2.  Access the FIDO server, obtain the message for policy check, and check whether the user has enabled FIDO authentication.
        
        // **uafMessage** is the policy check message obtained from the FIDO server.
        let uafAuthMessage: fido.UAFMessage = {
          /\*
          Policy check message format: \[{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"","serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":\[\[{"aaid":\["001B#1001"\],"keyIDs":\["test keyIDs"\],"authenticationAlgorithms":\[1\]}\]\]}}\]
          \*/
          uafProtocolMessage: uafMessage, // Policy check message obtained from the server.
          additionalData: "" // (Optional) Additional information.
        };
        let isRegistered: boolean = true;
        try {
          // Check whether FIDO authentication is enabled.
          await fido.checkPolicy(this.uiContext, uafAuthMessage);
        } catch (error) {
          isRegistered = false;
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}\`);
          // Determine the status based on the error code and rectify the fault accordingly.
        }
        if (isRegistered) {
          console.info("has registered, no need to register again.");
          // Registered. The service executes the subsequent process as required.
        }
        
    3.  Access the FIDO server, obtain the authentication message, and call the **processUAFOperation** API for FIDO authentication.
        
        // **regMessage** is the authentication message obtained from the FIDO server.
        let uafRegMessage: fido.UAFMessage = {
          /\*
          Authentication message format: \[{"header":{"upv":{"major":1,"minor":0},"op":"Auth","appID":"","serverData":"test server data"},"challenge":"test challenge","policy":{"accepted":\[\[{"aaid":\["001B#1001"\],"keyIDs":\["test keyIDs"\],"authenticationAlgorithms":\[1\]}\]\]}}\]
          \*/
          uafProtocolMessage: regMessage, // Authentication message obtained from the server.
          additionalData: "" // (Optional) Additional information.
        };
        // (Optional) Pass channel binding parameters.
        let channelBinding: fido.ChannelBinding = {};
        try {
          // Call the **processUAFOperation** API for FIDO authentication.
          let messageResp = await fido.processUAFOperation(this.uiContext, uafRegMessage, channelBinding);
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
         // Send an authentication response message to the FIDO server for verification and return the authentication result.
        
5.  Disable FIDO passwordless identity authentication.
    1.  Initialize authenticators. (Skip this step if you have performed the initialization.)
        
        try {
          // Call the **discover** method to initialize authenticators.
          let discoverData = await fido.discover(this.uiContext);
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
        
    2.  Access the FIDO server, obtain the deregistration message, and call the **processUAFOperation** API for FIDO deregistration.
        
        // **deregMessage** is the deregistration message obtained from the FIDO server.
        let uafRegMessage: fido.UAFMessage = {
          /\*
          Deregistration message format: \[{"header":{"upv":{"major":1,"minor":0},"op":"Dereg","appID":""},"authenticators":\[{"aaid":"001B#1001","keyID":"test keyID"}\]}\]
          \*/
          uafProtocolMessage: deregMessage, // Deregistration message obtained from the server.
          additionalData: "" // (Optional) Additional information.
        };
        // (Optional) Pass channel binding parameters.
        let channelBinding: fido.ChannelBinding = {};
        try {
          // Call the **processUAFOperation** API for FIDO deregistration.
          let messageResp = await fido.processUAFOperation(this.uiContext, uafRegMessage, channelBinding);
        } catch (error) {
          const err: BusinessError = error as BusinessError;  
          console.error(\`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}\`);
          // Determine the error type based on the error code and rectify the fault accordingly.
        }
         // Send an authentication response message to the FIDO server for verification and return the authentication result.
