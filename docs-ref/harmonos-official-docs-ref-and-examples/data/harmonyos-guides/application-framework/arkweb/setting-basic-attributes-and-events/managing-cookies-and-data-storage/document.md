# Managing Cookies and Data Storage

Cookies are data sent from the server to the client. The client holds cookies so that the server can quickly identify its identity and status.

For cookies, the default value of **SameSite** is **Lax**, indicating that cookies are sent only when a user navigates to the source site and are not sent in cross-site requests.

#### Cookie Management

The **Web** component provides the [WebCookieManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager) class to manage cookie information. Cookies are stored in the **/proc/{pid}/root/data/storage/el2/base/cache/web/Cookies** file in the application sandbox directory.

The following uses the [configCookieSync()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookiesync11) API to set a cookie value to **test** for **www.example.com**.

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('configCookieSync')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookieSync('https://www.example.com', 'value=test');
          } catch (error) {
            console.error(
              \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller });
    }
  }
}

Since API version 22, you can use the [setLazyInitializeWebEngine()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#setlazyinitializewebengine22) API to skip ArkWeb kernel initialization when the value of a single cookie is set to **value=test** for **www.example.com**, thereby reducing the [configCookieSync()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookiesync11) API call time. For details about features and usage of other APIs, see [WebCookieManager()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager).

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

webview.WebCookieManager.setLazyInitializeWebEngine(true);

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebCookieManager.configCookieSync('https://www.example.com', 'value=test');
    } catch (error) {
      console.error(
        \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/SIr6lf33R0mQrzoAXJ-HUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDC7BA4039281964CFA3F0E14CACF67E1AF6D05D2678333918B26CB0C201358E)

Cookies are saved to disks every 30 seconds. You can also use the [saveCookieAsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#savecookieasync) API to forcibly save cookies to disks. (Even if **saveCookieAsync** is called, session cookies are not written to disks in PCs/2-in-1 devices and tablets.)

#### Cache and Storage Management

Network resource requests are relatively time-consuming during website access. You can store resources locally by means of **cache** and **Dom Storage** to fasten the access to the same website.

## Cache

Use [cacheMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#cachemode) to configure the cache mode for page resources. Four cache modes are supported:

-   **Default**: Page resources in a cache that has not expired are preferentially used. If the cache does not exist, page resources are obtained from the network.
    
-   **None**: Page resources are loaded from the cache. If the cache does not contain the page resources, page resources are obtained from the network.
    
-   **Online**: Page resources are not loaded from the cache. They are all obtained from the network.
    
-   **Only**: Page resources are only loaded from the cache.
    

In the following example, the cache mode is set to **None**.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State mode: CacheMode = CacheMode.None;
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .cacheMode(this.mode)
    }
  }
}

To obtain up-to-date resources, you can use [removeCache()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#removecache) to clear cached resources. The sample code is as follows:

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  @State mode: CacheMode = CacheMode.None;
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeCache')
        .onClick(() => {
          try {
            // If this parameter is set to true, the cache in both the ROM and RAM is cleared. If this parameter is set to false, only the cache in the RAM is cleared.
            this.controller.removeCache(true);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
        .cacheMode(this.mode)
    }
  }
}

## Dom Storage

Dom Storage falls into Session Storage and Local Storage. Session Storage holds temporary data and it is stored and released based on the session lifecycle. Local Storage holds persistent data and is stored in the application directory. In both storage modes, data is stored in a form of key-value pair, and used when a page that needs to be stored on the client is accessed. You can use [domStorageAccess()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#domstorageaccess) to enable Dom Storage. The following is the sample code:

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .domStorageAccess(true)
    }
  }
}

#### FAQs

## What is the size limit for the static resource file cache of the ArkWeb component?

The size limit for the static resource cache of a single application in ArkWeb is 100 MB.
