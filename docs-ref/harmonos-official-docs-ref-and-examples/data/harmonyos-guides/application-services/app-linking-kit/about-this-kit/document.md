# About This Kit

App Linking Kit provides a range of enhanced linking features.

-   App Linking Kit supports [starting an app with the app link capability](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md) to implement cross-app redirection. If the target app is installed, it will be started to display the intended content. If the app is not installed, the corresponding web page content will be displayed in the system browser.
    
    In addition, App Linking Kit offers competitive features such as deferred link and direct access to AppGallery, significantly enhancing App Linking capabilities, improving the link redirection experience, and boosting the link conversion rate.
    
    -   [Redirecting to an app details page with the deferred link capability](../redirecting-to-an-app-details-page-with-the-deferred-link-capability/document.md): When a user taps an app promotion link but the app is not yet installed, the system automatically caches the tapping information for 10 minutes. After the user installs and launches the app, the tapping parameters can still be obtained, avoiding conversion loss and enhancing user experience.
    -   [Redirecting to an app download page through direct access to AppGallery](../redirecting-to-an-app-download-page-through-direct-access-to-appgallery/document.md): If an app is not installed, App Linking opens the web page corresponding to the link through the system browser by default. However, with the capability of direct access to AppGallery, users are redirected straight to AppGallery when the app is not installed. This removes the need for intermediate steps, making the redirection experience smoother.
    
-   App Linking Kit supports [redirecting to an app in a specific way through a cross-platform link](../redirecting-to-an-app-in-a-specific-way-through-a-cross-platform-link/document.md). When a user taps a cross-platform link in the HarmonyOS system, the deep link is opened by the system browser by default. However, with the cross-platform link capability, users can be redirected to a HarmonyOS preview page, a details page on AppGallery, a custom URL, a deep link, or another specified page.

#### Use Cases

-   App Linking applies to scenarios such as [scan-to-access](../../../media/scan-kit/scan-to-access-capability/document.md), social sharing, inactive user engagement, and advertising.
-   App Linking applies to scenarios with high security requirements. It helps prevent app spoofing.
-   App Linking applies to apps that aim to provide ultimate user experience. Users can directly access the content regardless of whether the target app is installed.

#### Restrictions

## Supported Devices

| 
Capability

 | 

Supported Device

 |
| :-- | :-- |
| 

App link

 | 

Phones, tablets, PCs/2-in-1 devices, and TVs

 |
| 

Deferred link

 | 

Phones and tablets

 |
| 

Direct access to AppGallery

 | 

Phones, tablets, and PCs/2-in-1 devices

 |
| 

Cross-platform link

 | 

Phones, tablets, and PCs/2-in-1 devices

 |

## Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.

## Supported Signing Modes

Currently, only [manual signing](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233) is supported.

## Supported Emulators

This kit is not supported on the Emulator.
