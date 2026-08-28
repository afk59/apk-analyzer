# Overview

From HarmonyOS 6.0.0(20), Online Authentication Kit provides the passkey feature, supporting the following capabilities:

-   Passkey registration: A passkey for apps or websites can be created on a local device, using a user's authentication factors (such as their face, fingerprint, or PIN) as the platform authenticator.
-   Local passwordless authentication: A passkey can be used for passwordless authentication during app or website sign-in on the local device, using a user's authentication factors (such as their face, fingerprint, or PIN) as the platform authenticator.
-   Cross-device authentication through QR code scanning: A mobile device with a registered passkey can function as a roaming authenticator for passwordless sign-in to apps or websites on another device through cross-device QR code scanning.

#### Use Cases

The following describes the application scenarios.

## Registering a Passkey

To enable easy, fast, and secure sign-in to local apps or websites, you can create a passkey for users through the passkey registration capability of the passkey service.

## Using a Passkey to Sign In to an App or Website on the Local Device

To authenticate a user who wants to sign in to an app or website, you can use the local passwordless authentication capability of the passkey service.

## Scanning a QR Code to Sign In to an App or Website on Another Device

To authenticate a user who wants to sign in to an app or website on another device, you can use the cross-device authentication capability of the passkey service through QR code scanning.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/kKSZp8-cQO2B0ztS2A-8PQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062009Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60CC724582FE122227723B8CAC235280DD1557FAD0E133DEB04AC0C241882692)

To support the preceding scenarios, you need to deploy a FIDO server that complies with FIDO2 standards.

#### Basic Concepts

A passkey is an authentication credential based on [FIDO2 standards](https://fidoalliance.org/passkeys/) (here is the [website link disclaimer](../../website-link-disclaimer/document.md)) for simple and secure sign-in. With a passkey, users can sign in to apps or websites using their fingerprint, their face, or their phone's unlock PIN. Compared with traditional passwords, passkeys offer greater convenience and enhanced security. For more information about FIDO, please refer to [FIDO specifications](https://fidoalliance.org/specifications-overview/) (here is the [website link disclaimer](../../website-link-disclaimer/document.md)).

#### Restrictions

This function can be used only when the following conditions are met:

-   Your services must adopt the protocols that comply with FIDO2 standards, and you need to deploy a FIDO2-compliant FIDO server.
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
    
-   The passkey service requires an Internet connection and Bluetooth to provide a complete online identity authentication service. Before calling this service's APIs, your app must explicitly inform users that the passkey service will use an Internet connection and Bluetooth, and obtain user consent.
-   According to the [FIDO specifications](https://fidoalliance.org/specifications-overview/) (here is the [website link disclaimer](../../website-link-disclaimer/document.md)), the passkey service needs to upload user nickname and identifier information in third-party apps to a network relay server, for use in cross-device authentication through QR code scanning, to implement authentication data communication between two devices. Before calling this service's APIs, your app must explicitly inform users of the personal data collected, and obtain user consent.

#### Service Process

**Registration process**

1.  An app or a browser integrates the passkey module of Online Authentication Kit and sends a registration request to the FIDO server.
2.  The FIDO server returns the registration information (such as a challenge) to the app. The app assembles the registration message and uses the passkey service for registration.
3.  After successful user verification by the authenticator, the passkey service generates a credential key pair. It then uses the preset private key to sign the generated public key and registration information (such as the challenge).
4.  The passkey service returns the signature to the app. The app sends the signature to the FIDO server for registration.
5.  The FIDO server verifies the signature, stores the public key, and returns the processing result to the app.

**Authentication process**

1.  An app or a browser integrates the passkey module of Online Authentication Kit and sends an authentication request to the FIDO server.
2.  The FIDO server returns the authentication information (such as a challenge) to the app. The app assembles the authentication message and uses the passkey service for authentication.
3.  After successful user verification by the authenticator, the passkey service uses the stored private key to sign the authentication information (such as a challenge).
4.  The passkey service returns the signature to the app. The app sends the signature to the FIDO server for authentication.
5.  The FIDO server verifies the signature and returns the processing result to the app.
