# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fAl9_sJMSRCMKrr4dt5iBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F52F8C9E6F3CC24B03FF12F0119539117FF5631428E369555C91FE79849B1214)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    

#### Module to Import

import { webview } from '@kit.ArkWeb';

#### webview.once

once(type: string, callback: Callback<void>): void

Registers a one-time callback for web events of the specified type. Currently, only **webInited** is supported. This callback is triggered when the Web engine initialization is complete.

When the first **Web** component is loaded in an application, the web engine is initialized. When other **Web** components are loaded in the same application, **once()** is not triggered. When the first **Web** component is loaded after the last **Web** component is destroyed in the application, the web engine will be initialized again.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Web event type. The value can be **"webInited"**, indicating completion of web initialization. |
| callback | Callback<void> | Yes | Callback to register. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

webview.once("webInited", () => {
  console.info("configCookieSync");
  webview.WebCookieManager.configCookieSync("https://www.example.com", "a=b");
})

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
