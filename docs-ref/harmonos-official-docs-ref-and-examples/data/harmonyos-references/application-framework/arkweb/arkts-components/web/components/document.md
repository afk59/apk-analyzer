# Components

This module provides **Web** components with web page display capabilities. For details about web control capabilities, see [Module Description](../../../arkts-api/ohos-web-webview-webview/module-description/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/u0-EiMJrRXKWanvNuElNyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=291723E93064791873D9F84D53DFF51CA52CB31CA8A2CE6E1FFCF4F3174C1B77)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    

This module provides the following common functionalities related to web page display:

-   [ClientAuthenticationHandler](../class-clientauthenticationhandler/document.md): Client certificate request event.
-   [ConsoleMessage](../class-consolemessage/document.md): Console information.
-   [ControllerHandler](../class-controllerhandler/document.md): **WebviewController** object of the new **Web** component.
-   [DataResubmissionHandler](../class-dataresubmissionhandler/document.md): Form data operation object.
-   [EventResult](../class-eventresult/document.md): Same-layer event consumption result.
-   [FileSelectorParam](../class-fileselectorparam/document.md): File selector object of the **Web** component.
-   [FileSelectorResult](../class-fileselectorresult/document.md): File selection result of the **Web** component.
-   [FullScreenExitHandler](../class-fullscreenexithandler/document.md): Object for exiting full screen of the **Web** component.
-   [HttpAuthHandler](../class-httpauthhandler/document.md): Object for performing operations related to HttpAuth authentication requests.
-   [JsGeolocation](../class-jsgeolocation/document.md): Geolocation permission related functionalities.
-   [JsResult](../class-jsresult/document.md): Dialog box operations.
-   [PermissionRequest](../class-permissionrequest/document.md): Permission request.
-   [ScreenCaptureHandler](../class-screencapturehandler/document.md): Screen capture permission operations.
-   [SslErrorHandler](../class-sslerrorhandler/document.md): SSL error event operations.
-   [WebContextMenuParam](../class-webcontextmenuparam/document.md): Menu information displayed when the screen is long-pressed or the right mouse button is clicked.
-   [WebContextMenuResult](../class-webcontextmenuresult/document.md): Object that controls the menu displayed when the screen is long-pressed or the right mouse button is clicked.
-   [WebCookie](../class-webcookie/document.md): Cookie management operations of the **Web** component in the current application.
-   [WebKeyboardController](../class-webkeyboardcontroller/document.md): Object that controls the custom keyboard.
-   [WebResourceError](../class-webresourceerror/document.md): Resource management error.
-   [WebResourceRequest](../class-webresourcerequest/document.md): Resource obtaining request.
-   [WebResourceResponse](../class-webresourceresponse/document.md): Resource obtaining response.

#### Required Permissions

To use online resources, the application must have the **ohos.permission.INTERNET** permission. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

#### Child Components

Not supported

#### APIs

Web(value: WebOptions)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/zVsTSqoYQBWKEU0_XQLXGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76B5FD1C0BED483FE54C878C3026F9355AA3D05F899EA4233EABD9C7CC071A0D)

Transition animation is not supported.

**Web** components on the same page must be bound to different **WebviewController** instances.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [WebOptions](../interfaces-others/document.md#weboptions) | Yes | Define web options. |

**Example**

Example of loading online web pages:

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

Example of loading online web pages in incognito mode:

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true })
    }
  }
}

Example of rendering the **Web** component in synchronous mode:

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC\_RENDER })
    }
  }
}

Example of using the **Web** component to specify the shared rendering process.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller1: webview.WebviewController = new webview.WebviewController();
  controller2: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller1, sharedRenderProcessToken: "111" })
      Web({ src: 'www.w3.org', controller: this.controller2, sharedRenderProcessToken: "111" })
    }
  }
}

Specify whether the **Web** component handles mouse events as touch events.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller1: webview.WebviewController = new webview.WebviewController();
  controller2: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller1, emulateTouchFromMouseEvent: false })
      Web({ src: 'www.w3.org', controller: this.controller2, emulateTouchFromMouseEvent: true })
    }
  }
}

Example of loading local web pages using **$rawfile()**:

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Load a local resource file through $rawfile.
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}

Load the resource file through the resources protocol.

When **$rawfile** is used to load a URL contains a number sign (#), the content following the number sign is treated as a fragment. To avoid this issue, you can use the **resource://rawfile/** protocol prefix instead.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Load a local resource file through the resource protocol.
      Web({ src: "resource://rawfile/index.html#home", controller: this.controller })
    }
  }
}

Create an **index.html** file in **src/main/resources/rawfile**.

<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<div id="content"></div>

<script>
    function loadContent() {
      var hash = window.location.hash;
      var contentDiv = document.getElementById('content');

      if (hash === '#home') {
        contentDiv.innerHTML = '<h1>Home Page</h1><p>Welcome to the Home Page!</p>';
      } else {
        contentDiv.innerHTML = '<h1>Default Page</h1><p>This is the default content.</p>';
      }
    }

    // Load the UI.
    window.addEventListener('load', loadContent);

    // Update the UI when the hash changes.
    window.addEventListener('hashchange', loadContent);
</script>
</body>
</html>

To load the local resource file in the sandbox path, you need to configure the [fileAccess](../attributes/document.md#fileaccess) permission of the file system in the application.

1.  Obtain the sandbox path through the constructed singleton object **GlobalContext**.
    
    // GlobalContext.ets
    export class GlobalContext {
      private constructor() {}
      private static instance: GlobalContext;
      private \_objects = new Map<string, Object>();
    
      public static getContext(): GlobalContext {
        if (!GlobalContext.instance) {
          GlobalContext.instance = new GlobalContext();
        }
        return GlobalContext.instance;
      }
    
      getObject(value: string): Object | undefined {
        return this.\_objects.get(value);
      }
    
      setObject(key: string, objectClass: Object): void {
        this.\_objects.set(key, objectClass);
      }
    }
    
    // xxx.ets
    import { webview } from '@kit.ArkWeb';
    import { GlobalContext } from '../GlobalContext';
    
    let url = 'file://' + GlobalContext.getContext().getObject("filesDir") + '/index.html';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          // Load the files in the sandbox.
          Web({ src: url, controller: this.controller })
          .fileAccess(true)
        }
      }
    }
    
2.  Modify the **EntryAbility.ets** file.
    
    The following uses **filesDir** as an example to describe how to obtain the path of the sandbox. For details about how to obtain other paths, see [Obtaining Application File Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#obtaining-application-file-paths).
    
    // xxx.ets
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { webview } from '@kit.ArkWeb';
    import { GlobalContext } from '../GlobalContext';
    
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // Data synchronization between the UIAbility component and UI can be implemented by binding filesDir to the GlobalContext object.
        GlobalContext.getContext().setObject("filesDir", this.context.filesDir);
        console.info("Sandbox path is " + GlobalContext.getContext().getObject("filesDir"));
      }
    }
    
    HTML file to be loaded:
    
    <!-- index.html -->
    <!DOCTYPE html>
    <html>
        <body>
            <p>Hello World</p>
        </body>
    </html>
