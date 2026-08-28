# Application Development Preparations

This section describes the preparations for developing an application.

#### Registering as a Developer

On the HarmonyOS Developer website, [register as a developer](https://developer.huawei.com/consumer/en/doc/start/registration-and-verification-0000001053628148) and [complete identity verification](https://developer.huawei.com/consumer/en/doc/start/rna-0000001062530373). After that, you can access various capabilities and services available on the website.

#### Creating an Application

In [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) (AGC), create a HarmonyOS application by referring to [Creating a Project](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-project-0000002242804048) and [Creating a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506).

#### Installing and Configuring DevEco Studio

Download the latest version of [DevEco Studio](https://developer.huawei.com/consumer/en/download/). For details about how to install DevEco Studio, see [Installing DevEco Studio](../../environment-setup/downloading-and-installing-deveco-studio/document.md).

#### Creating an Application Project on DevEco Studio

Create an application project on DevEco Studio. For details, see [Creating a Project](../../environment-setup/creating-a-project/creating-a-project/document.md).

#### Configuring Signing Information

You do not need to configure the signing information when using the Emulator or Previewer for debugging. If you use a real device for debugging, you must sign the HAP.

Currently, two signing modes are available:

-   [Automatic signing](../../coding-and-debugging/configuring-a-debug-signature/document.md#section18815157237): If only one debugging device is required, you are advised to use automatic signing provided by DevEco Studio.
-   Manual signing: If you use multiple debugging devices or may perform debugging with the network disconnected, you need to [request a debug certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-cert-0000002283256797), [register a device](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-device-0000002283189937), [request a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278), and [sign your application](../../coding-and-debugging/configuring-a-debug-signature/document.md#section112371245115818) in AGC.

#### (Conditionally mandatory) Adding a Public Key Fingerprint

If your application needs to use one or more of the following open capabilities, you need to add a public key fingerprint in advance to debug and run the application:

-   Account Kit
-   Game Service Kit
-   Health Service Kit
-   IAP Kit
-   Payment Kit
-   Wallet Kit
-   Wear Engine Kit

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/k5t9Ni8yRdGhxp2UPaq8bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061914Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0EC7C63701AA55CB64E40B4CEEC976BF70A80EEA0822132F819630E94916C8A)

Before releasing the application, switch the application's debug fingerprint to its release signature.

Add a public key fingerprint. For details, see [Configuring a Public Key Fingerprint](https://developer.huawei.com/consumer/en/doc/app/agc-help-cert-fingerprint-0000002278002933).
