# Getting Started

1.  Make preparations by referring to [Preparing for App Development](../../../getting-prepared/application-development-preparations/document.md).
2.  (**Required only for the scan-to-access capability**) Integrate [App Linking](../../../application-services/app-linking-kit/starting-an-app-with-the-app-link-capability-of-app-linking/document.md) to your app.
    1.  Enable App Linking in AppGallery Connect.
    2.  Associate your app in AppGallery Connect.
    3.  Configure the website domain name associated with the 2D code or 1D code that you need to create in App Linking.
    4.  Associate the domain name in the **module.json5** file of your app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/sXkjYSr0QsWZ4AtD9ePRcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08B0B2074DFEF1418D88A6961994DCB7A881279CB4D29E0E61551F8B9DE294ED)

-   Currently, App Linking supports only HTTPS-based links to in-app pages and web pages. That means if the target app has been installed, users will be redirected to the in-app page directly. Otherwise, the page will be opened in a browser for them instead.
-   App Linking is also widely used in scenarios such as social sharing, inactive user engagement, and advertising.
-   The automatic signing function provided by DevEco cannot be used for App Linking integration. In this case, you need to [manually sign](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233) your app.
