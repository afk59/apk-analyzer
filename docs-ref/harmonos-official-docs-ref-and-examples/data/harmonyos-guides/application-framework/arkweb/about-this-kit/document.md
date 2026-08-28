# About This Kit

#### When to Use

ArkWeb provides **Web** components to display web page content in applications. You can use the components in the following scenarios:

-   Web page integration: Applications can use **Web** components to embed web page content to reduce development costs and improve development and O&M efficiency.
    
-   Web browsing: Browser applications can use **Web** components to open third-party web pages, browse web pages in traceless mode, and set advertisement blocking.
    
-   Applet: Host applications of applets can use **Web** components to render the pages of the applets, implement same-layer rendering, and take over video playback.
    

#### Available Capabilities

The **Web** component provides various capabilities for you to control web pages, including:

-   Web page loading: declarative loading and off-screen loading of web pages.
    
-   Lifecycle management: component lifecycle status change and web page loading status change notification.
    
-   Common attributes and events: management of user agent, cookie and storage, font and dark mode, and permission.
    
-   Interaction with the application UI: The custom text selection menu, context menu, and file upload page can interact with the application UI.
    
-   Interaction between applications and web pages through JavaScriptProxy.
    
-   Security and privacy: traceless browsing mode, advertisement blocking, and Secure Shield mode.
    
-   Maintenance and debugging capability: [DevTools](../web-debugging/debugging-frontend-pages-by-using-devtools/document.md) for debugging, crashpad for collecting crash information of the Web component, and troubleshooting white screen issues on web pages.
    
-   Other advanced capabilities: same-layer rendering with system components, network and media playback takeovers, [Adding Password Vault for Web Pages](../../../system/security/password-autofill-service/adding-password-vault-for-web-pages/document.md)and custom input method for **Web** component text boxes.
    

#### Required Permissions

The **ohos.permission.INTERNET** permission is required for accessing online web pages. For details about how to apply for a permission, see [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

"requestPermissions":\[
    {
      "name" : "ohos.permission.INTERNET"
    }
  \]

#### Constraints

-   You can obtain the support for W3C standards based on the ArkWeb kernel version at related websites. For example, **[https://developer.mozilla.org/en-US/](https://developer.mozilla.org/en-US/)** and **[https://webassembly.org/features/](https://webassembly.org/features/)**.
    
-   Web kernel version: ArkWeb is developed based on the Google Chromium kernel. The following table lists the mapping between the system version and the Chromium version.
    
    | OS Version | Chromium Version |
    | :-- | :-- |
    | HarmonyOS 4.0 and earlier | M99 |
    | HarmonyOS 4.1-5.1 | M114 |
    | HarmonyOS 6.0 | 
    M132 (Default value, which is recommended.)
    
    M114 (Alternative. If the application needs to use this kernel, see [Adaptation Guide for the M114 Kernel on HarmonyOS 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md).)
    
     |
