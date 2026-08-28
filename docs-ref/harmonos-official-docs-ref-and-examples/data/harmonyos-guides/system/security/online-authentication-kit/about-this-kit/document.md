# About This Kit

Online Authentication Kit provides secure passwordless authentication on mobile devices, in compliance with the standards of Fast Identity Online (FIDO), FIDO2, International Internet Finance Authentication Alliance (IIFAA), and SOTER. The IIFAA alliance was originally known as the Internet Finance Authentication Alliance (IFAA). After accessing the FIDO, FIDO2, IFAA, or SOTER server, your app can use the corresponding mobile device capability to replace passwords with biometric features (for example, fingerprints or 3D faces) in service scenarios such as passwordless sign-in and payment.

#### FIDO

FIDO is a widely adopted international standard for passwordless authentication, supported by almost all device vendors. In addition, many ecosystem app vendors rely on it, including the Industrial and Commercial Bank of China, Bank of China, Agricultural Bank of China, Bank of Communications, as well as many securities and financial apps.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/djrkojeVTGiXgm4U7v1B8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062009Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=909B787179FDACF99DADB142588ED4EBB0A992DCC9F3F0C45B94FC46C5D34138)

For details, please refer to [sample-FIDOclientdemo](https://gitee.com/harmonyos_samples/online-authenticationkit_sample_-fidoclientdemo_-arkts) (here is the [website link disclaimer](../website-link-disclaimer/document.md)).

#### IFAA

IIFAA, formerly known as IFAA, is a collaborative ecosystem alliance dedicated to trusted identity authentication. It was officially established in 2015 by the China Academy of Information and Communications Technology (CAICT), Ant Group, Alibaba, Huawei, ZTE, and Samsung. The alliance aims to advance the development and industry adoption of secure authentication technologies, while leading the formulation of technical specifications. Among these, the local passwordless authentication technical specifications are used to support service scenarios such as passwordless sign-in and payment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/w6pinLQeRfSetpgE9FZwJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062009Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC16AD82C1EDF48047EA29739C0794A574101FEDF3BF01323FE60801B540A0F5)

For details, please refer to [sample-IFAAclientdemo](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit-sample-ifaaclientdemo-arkts) (here is the [website link disclaimer](../website-link-disclaimer/document.md)).

#### SOTER

SOTER is a biometric authentication platform and standard that enables services to use sensors (such as face sensors and fingerprint sensors) on devices to perform secure and efficient passwordless sign-in and payment. Currently, SOTER has been widely used in service scenarios such as WeChat mini programs and official accounts as well as fingerprint payment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ldET-b2FSsWQ8RSi-5-Pxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062009Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2881F860211C825CE6A2A401F28A955F1BFE65AFAECEBB3D7C355282F3E50971)

For details, please refer to [samplecode-SOTERclientdemo](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_samplecode_-soterclientdemo_-arkts) (here is the [website link disclaimer](../website-link-disclaimer/document.md)).

#### Passkeys

A passkey is an authentication credential based on [FIDO2 standards](https://fidoalliance.org/passkeys/) (here is the [website link disclaimer](../website-link-disclaimer/document.md)) for simple and secure sign-in. With a passkey, users can sign in to apps using their fingerprint, their face, or their phone's unlock PIN. Compared with traditional passwords, passkeys offer greater convenience and enhanced security.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Jc1r1vgHROWW-b8St9e0SQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062009Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C77E7F86A65E2AA8B0A6273A0088E77ADF256EC20EFEE49E26CD5C89F9FC022)

For details, please refer to [samplecode-FIDO2clientdemo-arkts](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_fido2clientdemo_arkts) and [samplecode-FIDO2clientdemo-cpp](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_fido2clientdemo_cpp) (here is the [website link disclaimer](../website-link-disclaimer/document.md)).

#### Use Cases

The IIFAA and FIDO scenarios are as follows:

-   Enabling: Enable passwordless identity authentication (fingerprint/3D face).
-   Authentication: Perform passwordless identity authentication (fingerprint/3D face).
-   Disabling: Disable passwordless identity authentication (fingerprint/3D face).

Note: In this document, we use "IFAA" to refer to the passwordless authentication module of the HarmonyOS system, and "IIFAA" to refer to the International Internet Finance Authentication Alliance and related technical specifications.

The passkey scenarios are as follows:

-   Passkey registration: A passkey for apps or websites can be created on a local device, using a user's authentication factors (such as their face, fingerprint, or PIN) as the platform authenticator.
-   Local passwordless authentication: A passkey can be used for passwordless authentication during app or website sign-in on the local device, using a user's authentication factors (such as their face, fingerprint, or PIN) as the platform authenticator.
-   Cross-device authentication through QR code scanning: A mobile device with a registered passkey can function as a roaming authenticator for passwordless sign-in to apps or websites on another device through cross-device QR code scanning.

#### Function Restrictions

The FIDO, IFAA, SOTER, and passkey capabilities provided by Online Authentication Kit have the following restrictions:

-   You need to deploy the corresponding server for your app.
-   To use the fingerprint- or 3D face–based passwordless authentication capability, ensure that mobile devices support corresponding biometric features. For details about how to check whether a mobile device supports biometric features, please refer to [User Authentication Kit](../../user-authentication-kit/user-authentication-development/obtaining-supported-authentication-capabilities/document.md) (the device must support the ATL4 authentication trust level).
-   Mobile devices must be connected to the Internet to use the capabilities.
-   The capabilities are currently not supported on emulators.

#### Supported Countries and Regions

Chinese mainland.
