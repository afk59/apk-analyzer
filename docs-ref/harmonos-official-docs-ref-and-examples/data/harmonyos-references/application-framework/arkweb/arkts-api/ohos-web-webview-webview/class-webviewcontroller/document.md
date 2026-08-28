# Class (WebviewController)

Represents a **WebviewController** object used to control various behaviors of **Web** components, including page navigation, lifecycle status, and JavaScript interaction. A **WebviewController** object can control only one **Web** component, and the APIs (except static APIs) in the **WebviewController** can be invoked only after it has been bound to the target **Web** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/hnpmtgW1T_6l9mGYbnJqNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6E810E3D8259BD39D088BACE5017355356E078E90F171C1AA472D23C6E19CBF)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### constructor11+

constructor(webTag?: string)

Constructs a **WebviewController** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/5jJPnOjwQhuZR_f_7eFicw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=421DE8368D92D579C18FE9EDE833ECE3B45D8F477EAE16A3CC1996E02F4AEBD5)

When no parameter is passed in **new webview.WebviewController()**, it indicates that the constructor is empty. If the C API is not used, no parameter needs to be passed.

When a valid string is passed in, such as **new webview.WebviewController("xxx")**, it can be used to distinguish multiple instances and invoke the methods of the corresponding instance.

When an empty parameter is passed in, such as **new webview.WebviewController("")** or **new webview.WebviewController(undefined)**, it is meaningless and cannot distinguish multiple instances. In this case, **undefined** is returned. You need to check whether the returned value is normal.

After the **Web** component is destroyed, it is unbound from the WebViewController. If you call a non-static method of the WebViewController, the [17100001](../../../error-codes/webview-error-codes/document.md#section17100001-webviewcontroller-not-associated-with-a-web-component) exception is thrown. Pay attention to the calling time and capture the exception to prevent the process from exiting abnormally.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| webTag | string | No | Name of the **Web** component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  @State webTestObj: WebObj = new WebObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: '', controller: this.controller })
        .javaScriptAccess(true)
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
          this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", \["webTest", "webString"\]);
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>

#### initializeWebEngine

static initializeWebEngine(): void

Before the **Web** component is initialized, the dynamic library file of the Web engine is loaded through this API to improve startup performance. The frequently visited websites are automatically pre-connected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/izB8cUtFT3arX6EKqI30Og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=323FF64B2F02619DE4DC306CCDB33A447C340265F8DEF1C71C7CFF8D0078147A)

-   **initializeWebEngine** cannot be called in an asynchronous thread. Otherwise, the system breaks down.
-   **initializeWebEngine** takes effect globally and needs to be called only once in an application lifecycle.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

The following uses EntryAbility as an example to describe how to load the dynamic library of the **Web** component during ability creation.

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.initializeWebEngine()
    console.info("EntryAbility onCreate done")
  }
}

#### setHttpDns10+

static setHttpDns(secureDnsMode:SecureDnsMode, secureDnsConfig:string): void

Sets how the **Web** component uses HTTPDNS for DNS resolution.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| secureDnsMode | [SecureDnsMode](../enums/document.md#securednsmode10) | Yes | Mode in which HTTPDNS is used. |
| secureDnsConfig | string | Yes | Information about the HTTPDNS server to use, which must use HTTPS. Only one HTTPDNS server can be configured. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    try {
      webview.WebviewController.setHttpDns(webview.SecureDnsMode.AUTO, "https://example1.test")
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }

    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done")
  }
}

#### setWebDebuggingAccess

static setWebDebuggingAccess(webDebuggingAccess: boolean): void

Sets whether to enable web debugging. For details, see [Debugging Frontend Pages by Using DevTools](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-debugging-with-devtools).

NOTE: Enabling web debugging allows users to check and modify the internal status of the web page, which poses security risks. Therefore, you are advised not to enable this feature in the officially released version of the application.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| webDebuggingAccess | boolean | Yes | 
Sets whether to enable web debugging.

The value **true** means to enable web debugging, and **false** means the opposite.

Default value: **false**.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### loadUrl

loadUrl(url: string | Resource, headers?: Array<WebHeader>): void

Loads a specified URL.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Resource | Yes | URL to load. |
| headers | Array<[WebHeader](../interfaces-others/document.md#webheader)\> | No | 
Additional HTTP request header of the URL.

Default value: **\[\]**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid. |
| 17100003 | Invalid resource path or file type. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // The URL to be loaded is of the string type.
            this.controller.loadUrl('www.example.com');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // The headers parameter is passed.
            this.controller.loadUrl('www.example.com', \[{ headerKey: "headerKey", headerValue: "headerValue" }\]);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

There are three methods for loading local resource files:

1.  Using $rawfile.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // Load a local resource file through $rawfile.
            this.controller.loadUrl($rawfile('index.html'));
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

1.  Using resources protocol.

Using the resource://rawfile/ protocol prefix avoids the limitations of the conventional $rawfile approach when processing routing links that contain the # character. When a URL contains the # character, the content after # is treated as an anchor (fragment).

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // Load local resource files through the resource protocol.
            this.controller.loadUrl("resource://rawfile/index.html#home");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
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

1.  Load the local file through the sandbox path. For details, see the sample code for loading the sandbox path in [Loading Web Pages](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-page-loading-with-web-components#loading-local-pages).

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World</p>
  </body>
</html>

#### loadData

loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void

Loads specified data.

When both **baseUrl** and **historyUrl** are empty:

If **encoding** is not base64 (including null values), ASCII encoding is used for octets within the secure URL character range, and the standard %xx hexadecimal encoding of the URL is used for octets outside the secure URL character range.

**data** must be encoded using Base64 or any hash (#) in the content must be encoded as %23. Otherwise, hash (#) is considered as the end of the content, and the remaining text is used as the document fragment identifier.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/QaYMUvx1T6GSvF98nepHfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=608EEE44172C1F1316E03B90D0CA79DF14A99469F841D0A63D00729B168F63A6)

-   To load a local image, you can assign a space to either **baseUrl** or **historyUrl**. For details, see the sample code.
    
-   In the scenario of loading a local image, **baseUrl** and **historyUrl** cannot be both empty. Otherwise, the image cannot be loaded.
    
-   If the rich text in HTML contains injected special characters such as #, you are advised to set the values of **baseUrl** and **historyUrl** to a single space.
    
-   To load texts, you need to set <meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8"> to avoid inconsistent font sizes.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | Yes | String obtained after being base64 or URL encoded. |
| mimeType | string | Yes | Media type (MIME). |
| encoding | string | Yes | Encoding type, which can be base64 or URL. |
| baseUrl | string | No | 
A specified URL path (http/https/data protocol), which is assigned by the **Web** component to window.origin. If a large number of HTML files need to be loaded, set this parameter to **data**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |
| historyUrl | string | No | 

URL used for historical records. If this parameter is not empty, historical records are managed based on this URL. This parameter is invalid when **baseUrl** is left empty.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

When both **baseUrl** and **historyUrl** are empty:

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<html><body bgcolor=\\"white\\">Source:<pre>source</pre></body></html>",
              "text/html",
              // UTF-8 is charset.
              "UTF-8"
            );
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              // Coding tests: string encoded using base64.
              "Q29kaW5nIHRlc3Rz",
              "text/html",
              "base64"
            );
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

Specify **baseURL**.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=aa/bb.jpg>", // Attempt to load the image from "https: // xxx.com/" + "aa/bb.jpg".
              "text/html",
              "UTF-8",
              "https://xxx.com/",
              "about:blank"
            );
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

Example of loading local resource:

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  updataContent: string = '<body><div><image src="resource://rawfile/xxx.png" alt="image -- end" width="500" height="250"></image></div></body>'

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            // UTF-8 is charset.
            this.controller.loadData(this.updataContent, "text/html", "UTF-8", " ", " ");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

Load the sandbox image.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=bb.jpg>", // Try to load the image from "file:///xxx/" + "bb.jpg".
              "text/html",
              "UTF-8",
              // Load the image path in the local application sandbox. Change the path to the actual sandbox path.
              "file:///data/storage/el2/base/haps/entry/files/data/.cache\_dir/",
              ""
            );
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(true) // Enable the file access functionality to load images in the application sandbox.
    }
  }
}

#### accessForward

accessForward(): boolean

Checks whether going to the next page can be performed on the current page.

You can use [getBackForwardEntries](#getbackforwardentries) to obtain the historical information list of the current WebView and use [accessStep](#accessstep) to determine whether to move forward or backward based on the specified number of steps.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if going to the next page can be performed on the current page; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('accessForward')
        .onClick(() => {
          try {
            let result = this.controller.accessForward();
            console.info('result:' + result);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### forward

forward(): void

Moves to the next page based on the history stack. This API is generally used together with **accessForward**.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('forward')
        .onClick(() => {
          try {
            this.controller.forward();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### accessBackward

accessBackward(): boolean

Checks whether going to the previous page can be performed on the current page.

You can use [getBackForwardEntries](#getbackforwardentries) to obtain the historical information list of the current WebView and use [accessStep](#accessstep) to determine whether to move forward or backward based on the specified number of steps.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/s4Ms35DlTmS-hHqsgl8o3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB274150B73AF861597604D595A0611B86719E76F7203B7E4A4E19E757F4F9DA)

If [setCustomUserAgent](#setcustomuseragent10) is called when the **Web** component is loaded for the first time, the value of **accessBackward** may be **false** when there are multiple historical entries. That is, there is no backward entry. You are advised to call the **setCustomUserAgent** method to set a user agent before using **loadUrl** to load a specific page.

Causes: When the **Web** component is loaded for the first time, calling [setCustomUserAgent](#setcustomuseragent10) causes the component to reload and retain the initial history entry. Then the new entry replaces the initial history entry and no new history entry is generated. As a result, the value of **accessBackward** is false.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if going to the previous page can be performed on the current page. Otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('accessBackward')
        .onClick(() => {
          try {
            let result = this.controller.accessBackward();
            console.info('result:' + result);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### backward

backward(): void

Moves to the previous page based on the history stack. This API is generally used together with [accessBackward](#accessbackward).

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('backward')
        .onClick(() => {
          try {
            this.controller.backward();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### onActive

onActive(): void

Called when the **Web** component enters the active state.

The application can interact with the user while in the active foreground state, and it remains in this state until the focus is moved away from it due to some event (for example, an incoming call is received or the device screen is turned off).

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('onActive')
        .onClick(() => {
          try {
            this.controller.onActive();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### onInactive

onInactive(): void

Called when the **Web** component enters the inactive state. You can implement the behavior to perform after the application loses focus.

When this API is called, any content that can be safely paused, such as animations and geographical locations, is paused as much as possible. However, the JavaScript is not paused. To pause the JavaScript globally, use [pauseAllTimers](#pausealltimers12). To reactivate the **Web** component, use [onActive](#onactive).

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('onInactive')
        .onClick(() => {
          try {
            this.controller.onInactive();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### refresh

refresh(): void

Called when the **Web** component refreshes the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### accessStep

accessStep(step: number): boolean

Checks whether a specific number of steps forward or backward can be performed on the current page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| step | number | Yes | Number of the steps to take. A positive number means to move forward, and a negative number means to move backward. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether a specific number of steps forward or backward can be performed on the current page.

**true** is returned if a specific number of steps forward or backward can be performed on the current page; otherwise, **false** is returned.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State steps: number = 2;

  build() {
    Column() {
      Button('accessStep')
        .onClick(() => {
          try {
            let result = this.controller.accessStep(this.steps);
            console.info('result:' + result);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearHistory

clearHistory(): void

Clears the browsing history. You are not advised to call **clearHistory()** in **onErrorReceive()** and **onPageBegin()**. Otherwise, abnormal exit occurs.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearHistory')
        .onClick(() => {
          try {
            this.controller.clearHistory();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### registerJavaScriptProxy

registerJavaScriptProxy(object: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void

Registers a proxy for interaction between the application and web pages loaded by the **Web** component. Registers a JavaScript object with the window. APIs of this object can then be invoked in the window.

For the example, see [Invoking Application Functions on the Frontend Page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-in-page-app-function-invoking).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Wr60yV5SRE2LGUCqIsL4Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D453D8EA856DA942A49ADDF357B335947409CF571F18DA0A5283F7C34A0F77A)

-   The **registerJavaScriptProxy** API must be used together with the **deleteJavaScriptRegister** API to prevent memory leak.
-   It is recommended that **registerJavaScriptProxy** be used only with trusted URLs and over secure HTTPS connections. Injecting JavaScript objects into untrusted web components can expose your application to malicious attacks.
-   After **registerJavaScriptProxy** is called, the application exposes the registered JavaScript object to all page frames.
-   If a **registerJavaScriptProxy** is both registered in the synchronous and asynchronous lists, it is called asynchronously by default.
-   You should register **registerJavaScriptProxy** either in synchronous list or in asynchronous list. Otherwise, this API fails to be registered.
-   After the HTML5 thread submits an asynchronous JavaScript task to the ETS main thread, the HTML5 thread can continue to execute subsequent tasks without waiting for the task execution to complete and return a result. In this way, scenarios where the HTML5 thread is blocked due to long-running JavaScript tasks or a congested ETS thread can be effectively reduced. However, an asynchronous JavaScript task cannot return a value, and a task execution sequence cannot be ensured. Therefore, you should determine whether to use a synchronous or asynchronous function based on a specific scenario.
-   The injected object does not appear in JavaScript until the page is reloaded.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| object | object | Yes | 
Application-side JavaScript object to be registered. Methods and attributes can be declared separately, but cannot be registered and used at the same time. If an object contains only attributes, HTML5 can access the attributes in the object. If an object contains only methods, HTML5 can access the methods in the object.

1\. The parameter and return value can be any of the following types:

string, number, boolean.

2\. Dictionary or Array, with a maximum of 10 nested layers and 10,000 data records per layer.

3\. Object, which must contain the **methodNameListForJsProxy:\[fun1, fun2\]** attribute, where **fun1** and **fun2** are methods that can be called.

4\. The parameter also supports Function and Promise. Their callback cannot have return values.

5\. The return value supports Promise. Its callback cannot have a return value.

 |
| name | string | Yes | Name of the object to be registered, which is the same as that invoked in the window. After registration, the window can use this name to access the JavaScript object at the application side. |
| methodList | Array<string> | Yes | Synchronous methods of the JavaScript object to be registered at the application side. |
| asyncMethodList12+ | Array<string> | No | 

Asynchronous methods of the JavaScript object to be registered at the application side. The default value is null. Asynchronous methods cannot obtain return values.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |
| permission12+ | string | No | 

JSON string, which is empty by default. This string is used to configure JSBridge permission control and define the URL trustlist at the object and method levels.

1\. The **scheme** and **host** parameters cannot be empty. The **host** does not support wildcards and can contain only complete host names.

2\. You can configure only the object-level trustlist, which takes effect for all JSBridge methods.

3\. If method-level trustlists are configured for JSBridge method A, the intersection of object-level and method-level trustlists takes effect.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr);
    return testStr;
  }

  toString(): void {
    console.info('Web Component toString');
  }

  testNumber(testNum: number): number {
    console.info('Web Component number' + testNum);
    return testNum;
  }

  asyncTestBool(testBol: boolean): void {
    console.info('Web Component boolean' + testBol);
  }
}

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
  }
}

class AsyncObj {
  constructor() {
  }

  asyncTest(): void {
    console.info('Async test');
  }

  asyncString(testStr: string): void {
    console.info('Web async string' + testStr);
  }
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();
  @State webTestObj: WebObj = new WebObj();
  @State asyncTestObj: AsyncObj = new AsyncObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            // Register both synchronous and asynchronous functions.
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", \["test", "toString", "testNumber"\], \["asyncTestBool"\]);
            // Register only the synchronous function.
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", \["webTest", "webString"\]);
            // Register only the asynchronous function.
            this.controller.registerJavaScriptProxy(this.asyncTestObj, "objAsyncName", \[\], \["asyncTest", "asyncString"\]);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
            this.controller.deleteJavaScriptRegister("objTestName");
            this.controller.deleteJavaScriptRegister("objAsyncName");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <p id="asyncDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "ArkUI Web Component"
          let str=objName.test("webtest data");
          objName.testNumber(1);
          objName.asyncTestBool(true);
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)

          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)

          objAsyncName.asyncTest();
          objAsyncName.asyncString("async test data");
        }
      </script>
    </body>
</html>

For more examples, see [Invoking Application Functions on the Frontend Page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-in-page-app-function-invoking).

#### runJavaScript

runJavaScript(script: string, callback : AsyncCallback<string>): void

Executes a JavaScript script asynchronously in the context of the current page. This API uses an asynchronous callback to return the script execution result. This method and its callback must be used on the UI thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/l18N1g_KQl-GLb-baLuDVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D267FEE2F91D7B4C79F256D5DFBF192B536591C9A88522D5857A0097696CB3D)

-   The JavaScript status is no longer retained during navigation operations (such as **loadUrl**). For example, the global variables and functions defined before **loadUrl** is called do not exist on the loaded page.
-   You are advised to use **registerJavaScriptProxy** to maintain the JavaScript status during page navigation.
-   Currently, objects cannot be transferred, but structs can be transferred.
-   The asynchronous method cannot obtain the return value. You need to determine whether to use the synchronous or asynchronous method based on the specific scenario.
-   The string data type passed from the frontend page to native is treated as JSON-formatted and need to be deserialized with JSON.parse.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| script | string | Yes | JavaScript script. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. **null** is returned if the JavaScript script fails to be executed or no value is returned. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100003 | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScript(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(\`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                  return;
                }
                if (result) {
                  this.webResult = result;
                  console.info(\`The test() return value is: ${result}\`);
                }
              });
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    Hello world!
    <script type="text/javascript">
      function test() {
        console.info('Ark WebComponent')
        return "This value is from index.html"
      }
    </script>
  </body>
</html>

#### runJavaScript

runJavaScript(script: string): Promise<string>

Executes a JavaScript script asynchronously in the context of the current page. This API uses a promise to return the script execution result. This method and its callback must be used on the UI thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/MEWWBkCAQsKklx67UTXM0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03563DF8E569D398E90F620EF4EF8A1E014544A7D75D8E74B9903E1907C5D8AD)

-   The JavaScript status is no longer retained during navigation operations (such as **loadUrl**). For example, the global variables and functions defined before **loadUrl** is called do not exist on the loaded page.
-   You are advised to use **registerJavaScriptProxy** to maintain the JavaScript status during page navigation.
-   Currently, objects cannot be transferred, but structs can be transferred.
-   The asynchronous method cannot obtain the return value. You need to determine whether to use the synchronous or asynchronous method based on the specific scenario.
-   The string data type passed from the frontend page to native is treated as JSON-formatted and need to be deserialized with JSON.parse.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| script | string | Yes | JavaScript script. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result if the operation is successful and null otherwise. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100003 | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScript('test()')
              .then((result) => {
                console.info('result: ' + result);
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              })
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    Hello world!
    <script type="text/javascript">
      function test() {
        console.info('Ark WebComponent')
        return "This value is from index.html"
      }
    </script>
  </body>
</html>

#### runJavaScriptExt10+

runJavaScriptExt(script: string | ArrayBuffer, callback : AsyncCallback<JsMessageExt>): void

Executes a JavaScript script. This API uses an asynchronous callback to return the script execution result. **runJavaScriptExt** can be invoked only after **loadUrl** is executed. For example, it can be invoked in **onPageEnd**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/VELIcYw6QQKDlqVcx77_Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C30C48A697AD28D5C317FDBD9639E380EBA4D62F6F761B2A05DD2A96CDCBA5C)

-   The string data type passed from the frontend page to native is treated as JSON-formatted and need to be deserialized with JSON.parse.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| script | string | ArrayBuffer12+ | Yes | JavaScript script. |
| callback | AsyncCallback<[JsMessageExt](../class-jsmessageext/document.md)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScriptExt(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(\`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`)
                  return;
                }
                if (result) {
                  try {
                    if (result.getErrorDescription()) {
                      // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                      console.info(\`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}\`);
                      return;
                    }
                    let type = result.getType();
                    switch (type) {
                      case webview.JsMessageType.STRING: {
                        this.msg1 = "result type:" + typeof (result.getString());
                        this.msg2 = "result getString:" + ((result.getString()));
                        break;
                      }
                      case webview.JsMessageType.NUMBER: {
                        this.msg1 = "result type:" + typeof (result.getNumber());
                        this.msg2 = "result getNumber:" + ((result.getNumber()));
                        break;
                      }
                      case webview.JsMessageType.BOOLEAN: {
                        this.msg1 = "result type:" + typeof (result.getBoolean());
                        this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                        break;
                      }
                      case webview.JsMessageType.ARRAY\_BUFFER: {
                        this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                        this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                        break;
                      }
                      case webview.JsMessageType.ARRAY: {
                        this.msg1 = "result type:" + typeof (result.getArray());
                        this.msg2 = "result getArray:" + result.getArray();
                        break;
                      }
                      default: {
                        this.msg1 = "default break, type:" + type;
                        break;
                      }
                    }
                  }
                  catch (resError) {
                    console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
                  }
                }
              });
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (resError) {
            console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
          }
        })
    }
  }
}

// Use the ArrayBuffer input parameter to obtain the JavaScript script data from the file.
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = ''
  @State msg2: string = ''

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let uiContext : UIContext = this.getUIContext();
            let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // Create a file and open it.
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
            // Write data to the file.
            fileIo.writeSync(file.fd, "test()");
            // Read data from the file.
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // Close the file.
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(
              arrayBuffer,
              (error, result) => {
                if (error) {
                  console.error(\`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`)
                  return;
                }
                if (result) {
                  try {
                    if (result.getErrorDescription()) {
                      // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                      console.info(\`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}\`);
                      return;
                    }
                    let type = result.getType();
                    switch (type) {
                      case webview.JsMessageType.STRING: {
                        this.msg1 = "result type:" + typeof (result.getString());
                        this.msg2 = "result getString:" + ((result.getString()));
                        break;
                      }
                      case webview.JsMessageType.NUMBER: {
                        this.msg1 = "result type:" + typeof (result.getNumber());
                        this.msg2 = "result getNumber:" + ((result.getNumber()));
                        break;
                      }
                      case webview.JsMessageType.BOOLEAN: {
                        this.msg1 = "result type:" + typeof (result.getBoolean());
                        this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                        break;
                      }
                      case webview.JsMessageType.ARRAY\_BUFFER: {
                        this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                        this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                        break;
                      }
                      case webview.JsMessageType.ARRAY: {
                        this.msg1 = "result type:" + typeof (result.getArray());
                        this.msg2 = "result getArray:" + result.getArray();
                        break;
                      }
                      default: {
                        this.msg1 = "default break, type:" + type;
                        break;
                      }
                    }
                  }
                  catch (resError) {
                    console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
                  }
                }
              });
          } catch (resError) {
            console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, world";
}
</script>
</html>

#### runJavaScriptExt10+

runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>

Executes a JavaScript script. This API uses a promise to return the script execution result. **runJavaScriptExt** can be invoked only after **loadUrl** is executed. For example, it can be invoked in **onPageEnd**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/nOkwfaLtRSaffvE43G5OZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DF5471C5BA6A04164A880C5AB21818B19882755DA43566ABEE50E1C87B2227C)

-   The string data type passed from the frontend page to native is treated as JSON-formatted and need to be deserialized with JSON.parse.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| script | string | ArrayBuffer12+ | Yes | JavaScript script. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[JsMessageExt](../class-jsmessageext/document.md)\> | Promise used to return the script execution result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(() => {
          this.controller.runJavaScriptExt('test()')
            .then((result) => {
              try {
                if (result.getErrorDescription()) {
                  // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                  console.info(\`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}\`);
                  return;
                }
                let type = result.getType();
                switch (type) {
                  case webview.JsMessageType.STRING: {
                    this.msg1 = "result type:" + typeof (result.getString());
                    this.msg2 = "result getString:" + ((result.getString()));
                    break;
                  }
                  case webview.JsMessageType.NUMBER: {
                    this.msg1 = "result type:" + typeof (result.getNumber());
                    this.msg2 = "result getNumber:" + ((result.getNumber()));
                    break;
                  }
                  case webview.JsMessageType.BOOLEAN: {
                    this.msg1 = "result type:" + typeof (result.getBoolean());
                    this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                    break;
                  }
                  case webview.JsMessageType.ARRAY\_BUFFER: {
                    this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                    this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                    break;
                  }
                  case webview.JsMessageType.ARRAY: {
                    this.msg1 = "result type:" + typeof (result.getArray());
                    this.msg2 = "result getArray:" + result.getArray();
                    break;
                  }
                  default: {
                    this.msg1 = "default break, type:" + type;
                    break;
                  }
                }
              }
              catch (resError) {
                console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
              }
            }).catch((error: BusinessError) => {
            console.error("error: " + error);
          })
        })
    }
  }
}

// Use the ArrayBuffer input parameter to obtain the JavaScript script data from the file.
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let uiContext : UIContext = this.getUIContext();
            let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // Create a file and open it.
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
            // Write data to the file.
            fileIo.writeSync(file.fd, "test()");
            // Read data from the file.
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // Close the file.
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(arrayBuffer)
              .then((result) => {
                try {
                  if (result.getErrorDescription()) {
                    // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                    console.info(\`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}\`);
                    return;
                  }
                  let type = result.getType();
                  switch (type) {
                    case webview.JsMessageType.STRING: {
                      this.msg1 = "result type:" + typeof (result.getString());
                      this.msg2 = "result getString:" + ((result.getString()));
                      break;
                    }
                    case webview.JsMessageType.NUMBER: {
                      this.msg1 = "result type:" + typeof (result.getNumber());
                      this.msg2 = "result getNumber:" + ((result.getNumber()));
                      break;
                    }
                    case webview.JsMessageType.BOOLEAN: {
                      this.msg1 = "result type:" + typeof (result.getBoolean());
                      this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                      break;
                    }
                    case webview.JsMessageType.ARRAY\_BUFFER: {
                      this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                      this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                      break;
                    }
                    case webview.JsMessageType.ARRAY: {
                      this.msg1 = "result type:" + typeof (result.getArray());
                      this.msg2 = "result getArray:" + result.getArray();
                      break;
                    }
                    default: {
                      this.msg1 = "default break, type:" + type;
                      break;
                    }
                  }
                }
                catch (resError) {
                  console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
                }
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, world";
}
</script>
</html>

#### deleteJavaScriptRegister

deleteJavaScriptRegister(name: string): void

Deletes a JavaScript object with the specified name on the application side that is registered with the window using [registerJavaScriptProxy](#registerjavascriptproxy) or [javaScriptProxy](../../../arkts-components/web/attributes/document.md#javascriptproxy). The deletion takes effect after the page is reloaded.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the registered JavaScript object, which can be used to invoke the corresponding object on the application side from the web side. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100008 | Failed to delete JavaScriptProxy because it does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component";
  }

  toString(): void {
    console.info('Web Component toString');
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();
  @State name: string = 'objName';
  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            this.controller.registerJavaScriptProxy(this.testObjtest, this.name, \["test", "toString"\]);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister(this.name);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <script type="text/javascript">
        function htmlTest() {
          let str=objName.test();
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)
        }
      </script>
    </body>
</html>

#### zoom

zoom(factor: number): void

Zooms in or out of this web page. This API is effective only when [zoomAccess](../../../arkts-components/web/attributes/document.md#zoomaccess) is **true**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| factor | number | Yes | 
Relative zoom ratio. The value must be greater than 0. The value **1** indicates that the page is not zoomed. A value smaller than **1** indicates zoom-out, and a value greater than **1** indicates zoom-in.

Value range: (0, 100\]

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State factor: number = 2;

  build() {
    Column() {
      Button('zoom')
        .onClick(() => {
          try {
            this.controller.zoom(this.factor);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}

#### searchAllAsync

searchAllAsync(searchString: string): void

Searches the web page for content that matches the keyword specified by **'searchString'** and highlights the matches on the page. This API returns the result asynchronously through [onSearchResultReceive](../../../arkts-components/web/events/document.md#onsearchresultreceive9).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| searchString | string | Yes | Search keyword. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State searchString: string = "Hello World";

  build() {
    Column() {
      Button('searchString')
        .onClick(() => {
          try {
            this.controller.searchAllAsync(this.searchString);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onSearchResultReceive(ret => {
          if (ret) {
            console.info("on search result receive:" + "\[cur\]" + ret.activeMatchOrdinal +
              "\[total\]" + ret.numberOfMatches + "\[isDone\]" + ret.isDoneCounting);
          }
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World Highlight Hello World</p>
  </body>
</html>

#### clearMatches

clearMatches(): void

Clears the matches found through [searchAllAsync](#searchallasync).

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearMatches')
        .onClick(() => {
          try {
            this.controller.clearMatches();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HMTL file loaded using [searchAllAsync](#searchallasync).

#### searchNext

searchNext(forward: boolean): void

Searches for and highlights the next match.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| forward | boolean | Yes | 
Whether to search forward or backward.

The value **true** indicates a forward search, and the value **false** indicates a backward search.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('searchNext')
        .onClick(() => {
          try {
            this.controller.searchNext(true);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HMTL file loaded using [searchAllAsync](#searchallasync).

#### clearSslCache

clearSslCache(): void

Clears the user operation corresponding to the SSL certificate error event recorded by the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearSslCache')
        .onClick(() => {
          try {
            this.controller.clearSslCache();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearClientAuthenticationCache

clearClientAuthenticationCache(): void

Clears the user operation corresponding to the client certificate request event recorded by the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearClientAuthenticationCache')
        .onClick(() => {
          try {
            this.controller.clearClientAuthenticationCache();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### createWebMessagePorts

createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>

Creates web message ports.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isExtentionType10+ | boolean | No | 
Whether to use the extended interface.

The value **true** means to use the extended interface, and **false** means the opposite.

Default value: **false**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WebMessagePort](../interface-webmessageport/document.md)\> | List of web message ports. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

#### postMessage

postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void

Sends a web message to an HTML window.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the message to send. |
| ports | Array<[WebMessagePort](../interface-webmessageport/document.md)\> | Yes | Message ports for sending the message. |
| uri | string | Yes | URI for receiving the message. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  ports: webview.WebMessagePort\[\] = \[\];
  @State sendFromEts: string = 'Send this message from ets to HTML';
  @State receivedFromHtml: string = 'Display received message send from HTML';

  build() {
    Column() {
      // Display the received HTML content.
      Text(this.receivedFromHtml)
      // Send the content in the text box to an HTML window.
      TextInput({ placeholder: 'Send this message from ets to HTML' })
        .onChange((value: string) => {
          this.sendFromEts = value;
        })

      Button('postMessage')
        .onClick(() => {
          try {
            // 1. Create two message ports.
            this.ports = this.controller.createWebMessagePorts();
            // 2. Register a callback on a message port (for example, port 1) on the application side.
            this.ports\[1\].onMessageEvent((result: webview.WebMessage) => {
              let msg = 'Got msg from HTML:';
              if (typeof (result) == "string") {
                console.info("received string message from html5, string is:" + result);
                msg = msg + result;
              } else if (typeof (result) == "object") {
                if (result instanceof ArrayBuffer) {
                  console.info("received arraybuffer from html5, length is:" + result.byteLength);
                  msg = msg + "length is " + result.byteLength;
                } else {
                  console.info("not support");
                }
              } else {
                console.info("not support");
              }
              this.receivedFromHtml = msg;
            })
            // 3. Send another message port (for example, port 0) to the HTML side, which can then save the port for future use.
            this.controller.postMessage('\_\_init\_port\_\_', \[this.ports\[0\]\], '\*');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })

      // 4. Use the port on the application side to send messages to the port that has been sent to the HTML side.
      Button('SendDataToHTML')
        .onClick(() => {
          try {
            if (this.ports && this.ports\[1\]) {
              this.ports\[1\].postMessageEvent(this.sendFromEts);
            } else {
              console.error(\`ports is null, Please initialize first\`);
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebView Message Port Demo</title>
</head>

  <body>
    <h1>WebView Message Port Demo</h1>
    <div>
        <input type="button" value="SendToEts" onclick="PostMsgToEts(msgFromJS.value);"/><br/>
        <input id="msgFromJS" type="text" value="send this message from HTML to ets"/><br/>
    </div>
    <p class="output">display received message send from ets</p>
  </body>
  <script src="xxx.js"></script>
</html>

// xxx.js
var h5Port;
var output = document.querySelector('.output');
window.addEventListener('message', function (event) {
    if (event.data == '\_\_init\_port\_\_') {
        if (event.ports\[0\] != null) {
            h5Port = event.ports\[0\]; // 1. Save the port number sent from the eTS side.
            h5Port.onmessage = function (event) {
              // 2. Receive the message sent from the eTS side.
              var msg = 'Got message from ets:';
              var result = event.data;
              if (typeof(result) == "string") {
                console.info("received string message from html5, string is:" + result);
                msg = msg + result;
              } else if (typeof(result) == "object") {
                if (result instanceof ArrayBuffer) {
                  console.info("received arraybuffer from html5, length is:" + result.byteLength);
                  msg = msg + "length is " + result.byteLength;
                } else {
                  console.info("not support");
                }
              } else {
                console.info("not support");
              }
              output.innerHTML = msg;
            }
        }
    }
})

// 3. Use h5Port to send messages to the eTS side.
function PostMsgToEts(data) {
    if (h5Port) {
      h5Port.postMessage(data);
    } else {
      console.error("h5Port is null, Please initialize first");
    }
}

#### requestFocus

requestFocus(): void

Requests focus for this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('requestFocus')
        .onClick(() => {
          try {
            this.controller.requestFocus();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### zoomIn

zoomIn(): void

Zooms in on this web page by 25%.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('zoomIn')
        .onClick(() => {
          try {
            this.controller.zoomIn();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### zoomOut

zoomOut(): void

Zooms out of this web page by 20%.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100004 | Function not enabled. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('zoomOut')
        .onClick(() => {
          try {
            this.controller.zoomOut();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getWebId

getWebId(): number

Obtains the index value of this **Web** component, which can be used for **Web** component management.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Index value of the current **Web** component. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getWebId')
        .onClick(() => {
          try {
            let id = this.controller.getWebId();
            console.info("id: " + id);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getUserAgent

getUserAgent(): string

Obtains the default user agent of this web page.

For details about the default **User-Agent**, see [Developing User-Agent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Default user agent. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUserAgent')
        .onClick(() => {
          try {
            let userAgent = this.controller.getUserAgent();
            console.info("userAgent: " + userAgent);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

You can customize **User-Agent** based on the default **User-Agent**.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State ua: string = "";

  aboutToAppear(): void {
    webview.once('webInited', () => {
      try {
        // Customize a User-Agent on the application side.
        this.ua = this.controller.getUserAgent() + 'xxx';
        this.controller.setCustomUserAgent(this.ua);
      } catch (error) {
        console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
      }
    })
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getTitle

getTitle(): string

Obtains the title of the current web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Title of the current web page. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getTitle')
        .onClick(() => {
          try {
            let title = this.controller.getTitle();
            console.info("title: " + title);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getPageHeight

getPageHeight(): number

Obtains the height of this web page. For details, see [Obtaining the Web Page Content Height](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-getpage-height).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Height of the current web page. Unit: vp |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getPageHeight')
        .onClick(() => {
          try {
            let pageHeight = this.controller.getPageHeight();
            console.info("pageHeight : " + pageHeight);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### storeWebArchive

storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void

Stores this web page. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| baseName | string | Yes | Save path of the web page. The value cannot be null. |
| autoName | boolean | Yes | 
Whether to automatically generate a file name.

The value **false** means to name and store a file based on the **baseName** value. The value **true** means to automatically generate a file name based on the current URL and store the file in the **baseName** directory.

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the save path if the operation is successful and null otherwise. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100003 | Invalid resource path or file type. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true, (error, filename) => {
              if (error) {
                console.error(\`save web archive error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              if (filename != null) {
                console.info(\`save web archive success: ${filename}\`);
              }
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### storeWebArchive

storeWebArchive(baseName: string, autoName: boolean): Promise<string>

Stores this web page. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| baseName | string | Yes | Save path of the web page. The value cannot be null. |
| autoName | boolean | Yes | 
Whether to automatically generate a file name.

The value **false** means to name and store a file based on the **baseName** value. The value **true** means to automatically generate a file name based on the current URL and store the file in the **baseName** directory.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the save path if the operation is successful and null otherwise. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100003 | Invalid resource path or file type. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true)
              .then(filename => {
                if (filename != null) {
                  console.info(\`save web archive success: ${filename}\`)
                }
              })
              .catch((error: BusinessError) => {
                console.error(\`ErrorCode: ${error.code},  Message: ${error.message}\`);
              })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getUrl

getUrl(): string

Obtains the URL of this page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the current page. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### stop

stop(): void

Stops page loading.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('stop')
        .onClick(() => {
          try {
            this.controller.stop();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### backOrForward

backOrForward(step: number): void

Performs a specific number of steps forward or backward on the current page based on the history stack. No redirection will be performed if the corresponding page does not exist in the history stack.

Because the previously loaded web pages are used for the operation, no page reloading is involved.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| step | number | Yes | Number of the steps to take. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State step: number = -2;

  build() {
    Column() {
      Button('backOrForward')
        .onClick(() => {
          try {
            this.controller.backOrForward(this.step);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### scrollTo

scrollTo(x:number, y:number, duration?:number): void

Scrolls the page to the specified absolute position within a specified period.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X coordinate of the absolute position. If the value is a negative number, the value 0 is used.

Unit: vp

 |
| y | number | Yes | 

Y coordinate of the absolute position. If the value is a negative number, the value 0 is used.

Unit: vp

 |
| duration14+ | number | No | 

Scrolling animation duration,

in milliseconds.

If no value is input or the input value is a negative number or 0, the animation is disabled.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('scrollTo')
        .onClick(() => {
          try {
            this.controller.scrollTo(50, 50, 500);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
        Button('stopScroll')
        .onClick(() => {
          try {
            this.controller.scrollBy(0, 0, 1); // To stop the animation generated by the current scroll, you can generate another 1 ms animation to interrupt the animation.
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### scrollBy

scrollBy(deltaX:number, deltaY:number,duration?:number): void

Scrolls the page by the specified amount within a specified period.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deltaX | number | Yes | 
Amount to scroll by along the x-axis. The positive direction is rightward.

Unit: vp

 |
| deltaY | number | Yes | 

Amount to scroll by along the y-axis. The positive direction is downward.

Unit: vp

 |
| duration14+ | number | No | 

Scrolling animation duration,

in milliseconds.

If no value is input or the input value is a negative number or 0, the animation is disabled.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/FMk6476sTTm_EWW5OsO-Og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33583726F64C94E250896A29BA786F25B4FAD5A0A030C7487125736F78C51611)

Calling **scrollBy** does not trigger the nested scrolling of the parent component.

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('scrollBy')
        .onClick(() => {
          try {
            this.controller.scrollBy(50, 50, 500);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('stopScroll')
        .onClick(() => {
          try {
            this.controller.scrollBy(0, 0, 1); // To stop the animation generated by the current scroll, you can generate another 1 ms animation to interrupt the animation.
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### scrollByWithResult12+

scrollByWithResult(deltaX: number, deltaY: number): boolean

Scrolls the page by the specified amount and returns value to indicate whether the scrolling is successful.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deltaX | number | Yes | 
Amount to scroll by along the x-axis. The positive direction is rightward.

Unit: vp

 |
| deltaY | number | Yes | 

Amount to scroll by along the y-axis. The positive direction is downward.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the current web page can be scrolled. The value **true** indicates that the current web page can be scrolled, and the value **false** indicates the opposite.

Default value: **false**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/2GIq0qapSXaZgPocPnUzIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20A63D4E5A294167D1EA4DCA61BEA9DC9F15789884F67C583BF9A698A8AD3B8D)

-   If the web page is being touched, **false** is returned. Otherwise, **true** is returned.
-   If the rendering area at the same layer of the web page is being touched, **true** is returned.
-   Calling **scrollByWithResult** does not trigger the nested scrolling of the parent component.
-   This API does not support the high frame rate of scrolling performance.

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('scrollByWithResult')
        .onClick(() => {
          try {
          let result = this.controller.scrollByWithResult(50, 50);
          console.info("original result: " + result);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### slideScroll

slideScroll(vx:number, vy:number): void

Simulates a slide-to-scroll action on the page at the specified velocity.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vx | number | Yes | 
Horizontal velocity component of the slide-to-scroll action, where the positive direction is rightward.

Unit: vp/ms.

 |
| vy | number | Yes | 

Vertical velocity component of the slide-to-scroll action, where the positive direction is downward.

Unit: vp/ms.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('slideScroll')
        .onClick(() => {
          try {
            this.controller.slideScroll(500, 500);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:3000px;
            height:3000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### getOriginalUrl

getOriginalUrl(): string

Obtains the original URL of this page.

Risk warning: If you want to obtain the URL for JavaScriptProxy communication API authentication, use [getLastJavascriptProxyCallingFrameUrl12+](#getlastjavascriptproxycallingframeurl12).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Original URL of the current page. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getOrgUrl')
        .onClick(() => {
          try {
            let url = this.controller.getOriginalUrl();
            console.info("original url: " + url);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getFavicon

getFavicon(): image.PixelMap

Obtains the favicon of this page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| image.[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | **PixelMap** object of the favicon of the page. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State pixelmap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Button('getFavicon')
        .onClick(() => {
          try {
            this.pixelmap = this.controller.getFavicon();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setNetworkAvailable

setNetworkAvailable(enable: boolean): void

Sets the **window.navigator.onLine** attribute in JavaScript.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable the **window.navigator.onLine** attribute.

The value **true** indicates that the **window.navigator.onLine** attribute is enabled, and the value **false** indicates the opposite.

Default value: **true**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setNetworkAvailable')
        .onClick(() => {
          try {
            this.controller.setNetworkAvailable(true);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<h1>online attribute </h1>
<p id="demo"></p>
<button onclick="func()">click</button>
<script>
    // Check whether the browser is online.
    var online1 = navigator.onLine;
    document.getElementById("demo").innerHTML = "Browser online:" + online1;

    function func(){
      var online2 = navigator.onLine;
      document.getElementById("demo").innerHTML = "Browser online:" + online2;
    }
</script>
</body>
</html>

#### hasImage

hasImage(callback: AsyncCallback<boolean>): void

Checks whether this page contains images. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | 
Callback used to return the result.

The value **true** indicates that this page contains images, and the value **false** indicates the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('hasImageCb')
        .onClick(() => {
          try {
            this.controller.hasImage((error, data) => {
              if (error) {
                console.error(\`hasImage error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              console.info("hasImage: " + data);
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### hasImage

hasImage(): Promise<boolean>

Checks whether this page contains images. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

The value **true** indicates that this page contains images, and the value **false** indicates the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('hasImagePm')
        .onClick(() => {
          try {
            this.controller.hasImage().then((data) => {
              console.info('hasImage: ' + data);
            }).catch((error: BusinessError) => {
              console.error("error: " + error);
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### removeCache

removeCache(clearRom: boolean): void

Removes all Webview cache files in an application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/uI3wz3hoQkWJaMdIFEyDrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47BB6E7849E5E6B88FEA24A5780E848B6B3E758FD5293979FB7259874AF02F06)

You can view the Webview cache in the **data/storage/el2/base/cache/web/Cache** directory.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clearRom | boolean | Yes | Whether to clear the cache files in both ROM and RAM. If this parameter is set to **true**, the cache files in both ROM and RAM are cleared. If this parameter is set to **false**, only the cache files in RAM are cleared. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeCache')
        .onClick(() => {
          try {
            this.controller.removeCache(false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### removeAllCache18+

static removeAllCache(clearRom: boolean): void

Removes all Webview cache files in an application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/SYVGI4g5SX-PCoLvZZLfjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BFC6AD374CC16F0D35FE61FC45B8EF08F1918FEAE42F9F5A92EDC70047C5773)

You can view the WebView cache files in the **data/app/el2/100/base/<applicationPackageName>/cache/web/** directory.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clearRom | boolean | Yes | Whether to clear the cache files in both ROM and RAM. If this parameter is set to **true**, the cache files in both ROM and RAM are cleared. If this parameter is set to **false**, only the cache files in RAM are cleared. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeAllCache')
        .onClick(() => {
          try {
            webview.WebviewController.removeAllCache(false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### pageUp

pageUp(top: boolean): void

Scrolls the page up by half the viewport or jumps to the top of the page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| top | boolean | Yes | 
Whether to jump to the top of the page.

The value **false** means to scroll the page up by half the viewport, and the value **true** means to jump to the top of the page.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('pageUp')
        .onClick(() => {
          try {
            this.controller.pageUp(false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /\* Horizontally centered \*/
         line-height: 200px;       /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>

#### pageDown

pageDown(bottom: boolean): void

Scrolls the page down by half the viewport or jumps to the bottom of the page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bottom | boolean | Yes | 
Whether to jump to the bottom of the page.

The value **false** means to scroll the page down by half the viewport, and the value **true** means to jump to the bottom of the page.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('pageDown')
        .onClick(() => {
          try {
            this.controller.pageDown(false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /\* Horizontally centered \*/
         line-height: 200px;       /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>

#### getBackForwardEntries

getBackForwardEntries(): BackForwardList

Obtains the historical information list of the current webview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/UyOunCksR2Kr-G5C_miRoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=287C6E9FF9D2F684840F20EBC0430121383D2486A2E22B59783C6EF33884858E)

[onLoadIntercept](../../../arkts-components/web/events/document.md#onloadintercept10) is triggered when the loading starts. At this time, no historical node is generated. Therefore, the historical stack obtained by calling **getBackForwardEntries** in **onLoadIntercept** does not include the page that is being loaded.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [BackForwardList](../interface-backforwardlist/document.md) | The historical information list of the current webview. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getBackForwardEntries')
        .onClick(() => {
          try {
            let list = this.controller.getBackForwardEntries()
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### serializeWebState

serializeWebState(): Uint8Array

Serializes the page status history of the current Webview.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Serialized data of the page status history of the current WebView. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

1.  To perform operations on files, you must first import the **fs** module. For details, see [File Management](../../../../core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md).

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('serializeWebState')
        .onClick(() => {
          try {
            let state = this.controller.serializeWebState();
            let path:string | undefined = AppStorage.get("cacheDir");
            if (path) {
              path += '/WebState';
              // Synchronously open a file.
              let file = fileIo.openSync(path, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
              fileIo.writeSync(file.fd, state.buffer);
              fileIo.closeSync(file.fd);
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

1.  Modify the **EntryAbility.ets** file.

Obtain the path of the application cache file.

// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // Data synchronization between the UIAbility component and the page can be implemented by binding cacheDir to the AppStorage object.
        AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
    }
}

#### restoreWebState

restoreWebState(state: Uint8Array): void

Restores the page status history from the serialized data of the current WebView.

If the value of **state** is too large, exceptions may occur. It is recommended that the page status history be not restored when the **state** value is greater than 512 KB.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | Uint8Array | Yes | Serialized data of the page status history. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

1.  To perform operations on files, you must first import the **fs** module. For details, see [File Management](../../../../core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md).

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('RestoreWebState')
        .onClick(() => {
          try {
            let path: string | undefined = AppStorage.get("cacheDir");
            if (path) {
              path += '/WebState';
              // Synchronously open a file.
              let file = fileIo.openSync(path, fileIo.OpenMode.READ\_WRITE);
              let stat = fileIo.statSync(path);
              let size = stat.size;
              let buf = new ArrayBuffer(size);
              fileIo.read(file.fd, buf, (err, readLen) => {
                if (err) {
                  console.error("console error with error message: " + err.message + ", error code: " + err.code);
                } else {
                  console.info("read file data succeed");
                  this.controller.restoreWebState(new Uint8Array(buf.slice(0, readLen)));
                  fileIo.closeSync(file);
                }
              });
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

1.  Modify the **EntryAbility.ets** file.

Obtain the path of the application cache file.

// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // Data synchronization between the UIAbility component and the page can be implemented by binding cacheDir to the AppStorage object.
    AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
  }
}

#### customizeSchemes

static customizeSchemes(schemes: Array<WebCustomScheme>): void

Grants the cross-domain request and fetch request permissions for the specified URL schemes (also known as protocols) to the web kernel. A cross-domain fetch request for any of the specified URL schemes can be intercepted by the [onInterceptRequest](../../../arkts-components/web/events/document.md#oninterceptrequest9) API, so that you can further process the request. It is recommended that this API be called before any **Web** component is initialized.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| schemes | Array<[WebCustomScheme](../interfaces-others/document.md#webcustomscheme)\> | Yes | Array of up to 10 custom schemes. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100020 | Failed to register custom schemes. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
  scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
  scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

  aboutToAppear(): void {
    try {
      webview.WebviewController.customizeSchemes(\[this.scheme1, this.scheme2, this.scheme3\]);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptRequest((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
          }
          return this.responseWeb;
        })
    }
  }
}

#### customizeSchemes21+

static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void

Grants the cross-domain request and fetch request permissions for the specified URL schemes (also known as protocols) to the web kernel. A cross-domain fetch request for any of the specified URL schemes can be intercepted by the [onInterceptRequest](../../../arkts-components/web/events/document.md#oninterceptrequest9) API, so that you can further process the request. It is recommended that this API be called before any **Web** component is initialized.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| schemes | Array<[WebCustomScheme](../interfaces-others/document.md#webcustomscheme)\> | Yes | Array of up to 10 custom schemes. |
| lazyInitWebEngine | boolean | Yes | 
Whether to skip WebEngine initialization in the API.

The value **true** means to skip the WebEngine initialization and store the registered schemes temporarily. When the WebEngine is initialized, the schemes are transferred to the WebEngine. The value false means to initialize the WebEngine automatically in the API.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. The length of the schemes array is greater than 10. 2. The character length of the scheme is greater than 32. 3. The character in the scheme is not within the allowed range of lowercase English letters, numbers, and the symbols ".", "+", "-". |
| 17100020 | Failed to register custom schemes. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
  scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
  scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

  aboutToAppear(): void {
    try {
      webview.WebviewController.customizeSchemes(\[this.scheme1, this.scheme2, this.scheme3\], true);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getCertificate10+

getCertificate(): Promise<Array<cert.X509Cert>>

Obtains the certificate information of this website. When the **Web** component is used to load an HTTPS website, SSL certificate verification is performed. This API uses a promise to return the [X.509 certificate](../../../../../system/security/device-certificate-kit/arkts-apis/ohos-security-cert-certificate/document.md#x509cert) of the current website.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<cert.X509Cert>> | Promise used to obtain the X.509 certificate array of the current HTTPS website. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray\[i\]);
  }
  return dataString;
}

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
  let res: string = 'getCertificate success: len = ' + x509CertArray.length;
  for (let i = 0; i < x509CertArray.length; i++) {
    res += ', index = ' + i + ', issuer name = '
      + Uint8ArrayToString(x509CertArray\[i\].getIssuerName().data) + ', subject name = '
      + Uint8ArrayToString(x509CertArray\[i\].getSubjectName().data) + ', valid start = '
      + x509CertArray\[i\].getNotBeforeTime()
      + ', valid end = ' + x509CertArray\[i\].getNotAfterTime();
  }
  return res;
}

@Entry
@Component
struct Index {
  // outputStr displays debug information on the UI.
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ListItem() {
            Button() {
              Text('load bad ssl')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an expired certificate website and view the obtained certificate information.
              this.webviewCtl.loadUrl('https://expired.badssl.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('load example')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an HTTPS website and view the certificate information of the website.
              this.webviewCtl.loadUrl('https://www.example.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate Promise')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
                  this.outputStr = ParseX509CertInfo(x509CertArray);
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate AsyncCallback')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
                  if (error) {
                    this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
                  } else {
                    this.outputStr = ParseX509CertInfo(x509CertArray);
                  }
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }
        }
        .listDirection(Axis.Horizontal)
        .height('10%')

        Text(this.outputStr)
          .width('100%')
          .fontSize(10)

        Web({ src: 'https://www.example.com', controller: this.webviewCtl })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .onPageEnd((e) => {
            if (e) {
              this.outputStr = 'onPageEnd : url = ' + e.url;
            }
          })
          .onSslErrorEventReceive((e) => {
            // Ignore SSL certificate errors to test websites whose certificates have expired, for example, https://expired.badssl.com.
            e.handler.handleConfirm();
          })
          .width('100%')
          .height('70%')
      }
      .height('100%')
    }
  }
}

#### getCertificate10+

getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void

Obtains the certificate information of this website. When the **Web** component is used to load an HTTPS website, SSL certificate verification is performed. This API uses an asynchronous callback to return the [X.509 certificate](../../../../../system/security/device-certificate-kit/arkts-apis/ohos-security-cert-certificate/document.md#x509cert) of the current website.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<cert.X509Cert>> | Yes | Callback used to obtain the X.509 certificate array of the current website. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray\[i\]);
  }
  return dataString;
}

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
  let res: string = 'getCertificate success: len = ' + x509CertArray.length;
  for (let i = 0; i < x509CertArray.length; i++) {
    res += ', index = ' + i + ', issuer name = '
      + Uint8ArrayToString(x509CertArray\[i\].getIssuerName().data) + ', subject name = '
      + Uint8ArrayToString(x509CertArray\[i\].getSubjectName().data) + ', valid start = '
      + x509CertArray\[i\].getNotBeforeTime()
      + ', valid end = ' + x509CertArray\[i\].getNotAfterTime();
  }
  return res;
}

@Entry
@Component
struct Index {
  // outputStr displays debug information on the UI.
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ListItem() {
            Button() {
              Text('load bad ssl')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an expired certificate website and view the obtained certificate information.
              this.webviewCtl.loadUrl('https://expired.badssl.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('load example')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an HTTPS website and view the certificate information of the website.
              this.webviewCtl.loadUrl('https://www.example.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate Promise')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
                  this.outputStr = ParseX509CertInfo(x509CertArray);
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate AsyncCallback')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
                  if (error) {
                    this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
                  } else {
                    this.outputStr = ParseX509CertInfo(x509CertArray);
                  }
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }
        }
        .listDirection(Axis.Horizontal)
        .height('10%')

        Text(this.outputStr)
          .width('100%')
          .fontSize(10)

        Web({ src: 'https://www.example.com', controller: this.webviewCtl })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .onPageEnd((e) => {
            if (e) {
              this.outputStr = 'onPageEnd : url = ' + e.url;
            }
          })
          .onSslErrorEventReceive((e) => {
            // Ignore SSL certificate errors to test websites whose certificates have expired, for example, https://expired.badssl.com.
            e.handler.handleConfirm();
          })
          .width('100%')
          .height('70%')
      }
      .height('100%')
    }
  }
}

#### setAudioMuted10+

setAudioMuted(mute: boolean): void

Mutes this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mute | boolean | Yes | 
Whether to mute the web page.

The value **true** means to mute the web page, and **false** means the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State muted: boolean = false;

  build() {
    Column() {
      Button("Toggle Mute")
        .onClick(event => {
          if (event) {
            this.muted = !this.muted;
            this.controller.setAudioMuted(this.muted);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### prefetchPage21+

prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void

Prefetches resources in the background for a page that is likely to be accessed in the near future, without executing the page JavaScript code or presenting the page. This can significantly reduce the load time for the prefetched page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/cV2AZvU3RMaw53-UQ4Ju-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCDFB1C9D2A846FED5D2A5844A3329F5F199033860512DA266118CEEB57C32D2)

-   The downloaded page resources are cached for about 5 minutes. After this period, the **Web** component automatically releases the resources.
    
-   **prefetchPage** can also prefetch 302 redirect pages.
    
-   When a page is loaded after **prefetchPage** is executed, the prefetched resources are directly loaded from the cache.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL to be preloaded. |
| additionalHeaders | Array<[WebHeader](../interfaces-others/document.md#webheader)\> | No | 
Additional HTTP headers of the URL.

Default value: **\[\]**.

 |
| prefetchOptions | [PrefetchOptions](../class-prefetchoptions/document.md) | No | Options for customizing the prefetch behavior. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // Replace 'https://www.example.com' with a real URL for the API to work.
            let options = new webview.PrefetchOptions();
            options.ignoreCacheControlNoStore = true;
            options.minTimeBetweenPrefetchesMs = 100;
            this.controller.prefetchPage('https://www.example.com', \[{ headerKey: "headerKey", headerValue: "headerValue" }\], options);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      // Replace 'www.example1.com' with a real URL for the API to work.
      Web({ src: 'www.example1.com', controller: this.controller })
    }
  }
}

#### prefetchPage10+

prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void

Prefetches resources in the background for a page that is likely to be accessed in the near future, without executing the page JavaScript code or presenting the page. This can significantly reduce the load time for the prefetched page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/iEFSpHUJRNOY9letgi63Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CB694D477212D3FA96442607B851A01F43893862BAB1BBB3C0ADA597A6A1A4F)

-   The downloaded page resources are cached for about 5 minutes. After this period, the **Web** component automatically releases the resources.
    
-   **prefetchPage** can also prefetch 302 redirect pages.
    
-   When a page is loaded after **prefetchPage** is executed, the prefetched resources are directly loaded from the cache.
    
-   If multiple URLs are specified for **prefetchPage**, only the first URL takes effect.
    
-   **prefetchPage** cannot be executed twice within 500 ms.
    

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL to be preloaded. |
| additionalHeaders | Array<[WebHeader](../interfaces-others/document.md#webheader)\> | No | 
Additional HTTP headers of the URL.

Default value: **\[\]**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // Replace 'https://www.example.com' with a real URL for the API to work.
            this.controller.prefetchPage('https://www.example.com');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      // Replace 'www.example1.com' with a real URL for the API to work.
      Web({ src: 'www.example1.com', controller: this.controller })
    }
  }
}

#### prefetchResource12+

static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void

Prefetches resource requests based on specified request information and additional HTTP request headers, saves the requests to the memory cache, and specifies the cache key and validity period to accelerate loading. Currently, only POST requests whose Content-Type is application/x-www-form-urlencoded are supported. A maximum of six POST requests can be pre-obtained. To prefetch the seventh post request, call [clearPrefetchedResource](#clearprefetchedresource12) to clear the cache of unnecessary post requests. Otherwise, the cache of the earliest prefetched POST request will be automatically cleared. To use the prefetched resource cache, you need to add the key value **ArkWebPostCacheKey** to the header of the POST request. The content of the key value is the cacheKey of the corresponding cache.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [RequestInfo](../interfaces-others/document.md#requestinfo12) | Yes | Information about the prefetched request. |
| additionalHeaders | Array<[WebHeader](../interfaces-others/document.md#webheader)\> | No | 
Additional HTTP request header of the prefetched request.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |
| cacheKey | string | No | 

Key used to query the cache of prefetched resources. The value can contain only letters and digits. If this parameter is not passed or is left empty, **url** is used by default.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |
| cacheValidTime | number | No | 

Validity period for caching prefetched resources.

Value range: (0, 2147483647\]

Default value: **300s**

Unit: second.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**Example**

// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Replace "https://www.example1.com/post?e=f&g=h" with a real URL to visit.
    webview.WebviewController.prefetchResource(
      {
        url: "https://www.example1.com/post?e=f&g=h",
        method: "POST",
        formData: "a=x&b=y",
      },
      \[{
        headerKey: "c",
        headerValue: "z",
      },\],
      "KeyX", 500);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}

#### clearPrefetchedResource12+

static clearPrefetchedResource(cacheKeyList: Array<string>): void

Clears the cache of prefetched resources based on the specified cache key list. The cache key in the input parameter must be the prefetched resource cache key specified by [prefetchResource](#prefetchresource12).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cacheKeyList | Array<string> | Yes | Key used to query the cache of prefetched resources. The value can contain only letters and digits. If this parameter is not passed or is left empty, **url** is used by default. |

**Example**

// Index.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: "https://www.example.com/", controller: this.controller })
        .onAppear(() => {
          // Replace "https://www.example1.com/post?e=f&g=h" with a real URL to visit.
          webview.WebviewController.prefetchResource(
            {
              url: "https://www.example1.com/post?e=f&g=h",
              method: "POST",
              formData: "a=x&b=y",
            },
            \[{
              headerKey: "c",
              headerValue: "z",
            },\],
            "KeyX", 500);
        })
        .onPageEnd(() => {
          // Clear the prefetch cache that is no longer used.
          webview.WebviewController.clearPrefetchedResource(\["KeyX",\]);
        })
    }
  }
}

#### prepareForPageLoad10+

static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void

Preconnects to a URL. This API can be called before the URL is loaded, to resolve the DNS and establish a socket connection, without obtaining the resources.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL to be preconnected. |
| preconnectable | boolean | Yes | Whether to perform preconnection, which involves DNS resolution and socket connection establishment. The value **true** means to perform pre-connection, and **false** means the opposite. |
| numSockets | number | Yes | Number of sockets to be preconnected. The value must be greater than 0. A maximum of six socket connections are allowed. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |
| 17100013 | The number of preconnect sockets is invalid. |

**Example**

// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Replace 'https://www.example.com' with a real URL for the API to work.
    webview.WebviewController.prepareForPageLoad("https://www.example.com", true, 2);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}

#### setCustomUserAgent10+

setCustomUserAgent(userAgent: string): void

Sets a custom user agent, which will overwrite the default user agent.

When **src** of the **Web** component is set to a URL, set **User-Agent** in **onControllerAttached**. For details, see the following example. Avoid setting the **User-Agent** in **onLoadIntercept**. Otherwise, the setting may fail occasionally.

When **src** of the **Web** component is set to an empty string, call **setCustomUserAgent** to set **User-Agent** and then use **loadUrl** to load a specific page.

For details about the default **User-Agent**, see [Developing User-Agent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/nKEJkaT0QJi12uS3Rz8GwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=409DA2E3D22940170B67B12C61100D8B00375B43120C952DA7F49486BC2E2F5F)

If a URL is set for the **Web** component **src** and **User-Agent** is not set in the **onControllerAttached** callback, calling **setCustomUserAgent** may cause mismatches between the loaded page and the intended **User-Agent**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userAgent | string | Yes | Information about the custom user agent. It is recommended that you obtain the current default user agent through [getUserAgent](#getuseragent) and then customize the obtained user agent. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State customUserAgent: string = ' DemoApp';

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .onControllerAttached(() => {
        console.info("onControllerAttached");
        try {
          let userAgent = this.controller.getUserAgent() + this.customUserAgent;
          this.controller.setCustomUserAgent(userAgent);
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
    }
  }
}

#### setDownloadDelegate11+

setDownloadDelegate(delegate: WebDownloadDelegate): void

Sets a **WebDownloadDelegate** for the current **Web** component. The delegate is used to receive the download progress triggered within the page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| delegate | [WebDownloadDelegate](../class-webdownloaddelegate/document.md) | Yes | Delegate used to receive the download progress. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### startDownload11+

startDownload(url: string): void

Downloads a file, such as an image, from the specified URL.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | Download URL. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('startDownload')
        .onClick(() => {
          try {
            this.controller.startDownload('https://www.example.com');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getCustomUserAgent10+

getCustomUserAgent(): string

Obtains a custom user agent.

For details about the default **User-Agent**, see [Developing User-Agent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Information about the custom user agent. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent: string = '';

  build() {
    Column() {
      Button('getCustomUserAgent')
        .onClick(() => {
          try {
            this.userAgent = this.controller.getCustomUserAgent();
            console.info("userAgent: " + this.userAgent);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setAppCustomUserAgent20+

static setAppCustomUserAgent(userAgent: string): void

Sets the application-level custom user agent, which will overwrite the system user agent and take effect for all **Web** components in the application.

If you need to set the application-level custom user agent, you are advised to call the **setAppCustomUserAgent** method to set the **User-Agent** before creating the **Web** component, and then create the **Web** component with the specified src or load the page using [loadUrl](#loadurl).

For details about the default **User-Agent** definition, application scenarios, and API priorities, see [Developing User-Agent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userAgent | string | Yes | Information about the custom user agent. It is recommended that you obtain the current default user agent through [getDefaultUserAgent](#getdefaultuseragent14) and then customize the obtained user agent. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.initializeWebEngine();
      let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
      let appUA = defaultUserAgent + " appUA";
      webview.WebviewController.setAppCustomUserAgent(appUA);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setUserAgentForHosts20+

static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void

Sets a custom user agent for a specific website, which overwrites the system user agent and takes effect for all **Web** components in the application.

To set a custom user agent for a specific website, you are advised to call the **setUserAgentForHosts** method to set **User-Agent** before creating a **Web** component, and then create a **Web** component with a specified src or use [loadUrl](#loadurl) to load a specific page.

For details about the default **User-Agent** definition, application scenarios, and API priorities, see [Developing User-Agent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userAgent | string | Yes | Information about the custom user agent. It is recommended that you obtain the current default user agent through [getDefaultUserAgent](#getdefaultuseragent14) and then customize the obtained user agent. |
| hosts | Array<string> | Yes | List of domain names related to the custom user agent. Only the latest list is retained each time the API is called. The maximum number of entries is 20,000, and the excessive entries are automatically truncated. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.initializeWebEngine();
      let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
      let appUA = defaultUserAgent + " appUA";
      webview.WebviewController.setUserAgentForHosts(
        appUA,
        \[
          "www.example.com",
          "www.baidu.com"
        \]
      );
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setConnectionTimeout11+

static setConnectionTimeout(timeout: number): void

Sets the network connection timeout interval. You can use the **onErrorReceive** method in the **Web** component to obtain the timeout error code. If this API is not called, the default timeout interval is **30** seconds.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | Timeout interval of the socket connection, in seconds. The value must be an integer greater than 0. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setConnectionTimeout')
        .onClick(() => {
          try {
            webview.WebviewController.setConnectionTimeout(5);
            console.info("setConnectionTimeout: 5s");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onErrorReceive((event) => {
          if (event) {
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
          }
        })
    }
  }
}

#### warmupServiceWorker12+

static warmupServiceWorker(url: string): void

Warms up the ServiceWorker to enhance the loading speed of the first screen (only applicable to pages that will use ServiceWorker). This API is called before the URL is loaded.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the ServiceWorker to warm up. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        console.info("EntryAbility onCreate");
        webview.WebviewController.initializeWebEngine();
        webview.WebviewController.warmupServiceWorker("https://www.example.com");
        AppStorage.setOrCreate("abilityWant", want);
    }
}

#### enableSafeBrowsing11+

enableSafeBrowsing(enable: boolean): void

Enables the safe browsing feature. This feature is forcibly enabled and cannot be disabled for identified untrusted websites.

By default, this feature does not take effect. HarmonyOS provides only the malicious website blocking web UI. The website risk detection and web UI display features are implemented by the vendor. You are advised to listen for [DidStartNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h) and [DidRedirectNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h) in **WebContentsObserver** for detection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/ywzOCBIuQl6m-ODViQF1qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C912BA9BD076876BA3F1B0D9EB94A3A0A7092585ED2C83D7E387E5E02058739)

This API does not take effect.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable the safe browsing feature.

The value **true** means to enable the safe browsing feature, and **false** means the opposite.

Default value: **false**.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('enableSafeBrowsing')
        .onClick(() => {
          try {
            this.controller.enableSafeBrowsing(true);
            console.info("enableSafeBrowsing: true");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isSafeBrowsingEnabled11+

isSafeBrowsingEnabled(): boolean

Checks whether the safe browsing feature is enabled for this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the safe browsing feature is enabled for this web page.

The value **true** indicates that the safe browsing feature is enabled, and **false** indicates the opposite.

Default value: **false**.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isSafeBrowsingEnabled')
        .onClick(() => {
          let result = this.controller.isSafeBrowsingEnabled();
          console.info("result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### enableIntelligentTrackingPrevention12+

enableIntelligentTrackingPrevention(enable: boolean): void

Enables intelligent tracking prevention.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior differences**: This API can be used on phones, tablets, PCs, and 2-in-1 devices. Since API version 18, error code **801** is returned for other device types.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable intelligent tracking prevention.

The value **true** means to enable intelligent tracking prevention, and **false** means the opposite.

Default value: **false**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
            console.info("enableIntelligentTrackingPrevention: true");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isIntelligentTrackingPreventionEnabled12+

isIntelligentTrackingPreventionEnabled(): boolean

Obtains whether intelligent tracking prevention is enabled on this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior differences**: This API can be used on phones, tablets, PCs, and 2-in-1 devices. Since API version 18, error code **801** is returned for other device types.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether intelligent tracking prevention is enabled on this web page.

The value **true** indicates that intelligent tracking prevention is enabled, and **false** indicates the opposite.

Default value: **false**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isIntelligentTrackingPreventionEnabled')
        .onClick(() => {
          try {
            let result = this.controller.isIntelligentTrackingPreventionEnabled();
            console.info("result: " + result);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### addIntelligentTrackingPreventionBypassingList12+

static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void

Adds a list of domain names that bypass intelligent tracking prevention.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior differences**: This API can be used on phones, tablets, PCs, and 2-in-1 devices. Since API version 18, error code **801** is returned for other device types.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hostList | Array<string> | Yes | List of domain names that bypass intelligent tracking prevention. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('addIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = \["www.test1.com", "www.test2.com", "www.test3.com"\];
            webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### removeIntelligentTrackingPreventionBypassingList12+

static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void

Deletes the domain names from the list of domain names added through the **addIntelligentTrackingPreventionBypassingList** API.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior differences**: This API can be used on phones, tablets, PCs, and 2-in-1 devices. Since API version 18, error code **801** is returned for other device types.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hostList | Array<string> | Yes | List of domain names that bypass intelligent tracking prevention. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('removeIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = \["www.test1.com", "www.test2.com"\];
            webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearIntelligentTrackingPreventionBypassingList12+

static clearIntelligentTrackingPreventionBypassingList(): void

Deletes all domain names from the list of domain names added through the **addIntelligentTrackingPreventionBypassingList** API.

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior differences**: This API can be used on phones, tablets, PCs, and 2-in-1 devices. Since API version 18, error code **801** is returned for other device types.

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getDefaultUserAgent14+

static getDefaultUserAgent(): string

Obtains the default user agent.

This API can be called only in the UI thread.

For details about the default **User-Agent**, see [Developing User-Agent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-default-useragent).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Default **User-Agent** string of ArkWeb. |

**Example**

// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
    console.info("defaultUserAgent: " + defaultUserAgent);
  }
}

#### enableAdsBlock12+

enableAdsBlock(enable: boolean): void

Enables ad blocking.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/JvhvUnlvQhyS5T5fGHuHFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1921BBFD88B5B64CC52779FC8043F25E84EDC3F4CE3CE0E95D11D7220561E32E)

-   The ad blocking feature works only for the release-type application, not the debug-type application.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable ad blocking.

The value **true** means to enable ad blocking, and **false** means the opposite.

Default value: **false**.

 |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/8k7pgCf2TiOC_yIK1a7QdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DF93D6FCA7CD5434B58AA7D89D4932903A1B62D1A5406D22F2F85832FDEF218)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('enableAdsBlock')
        .onClick(() => {
          try {
            this.controller.enableAdsBlock(true);
            console.info("enableAdsBlock: true")
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isAdsBlockEnabled12+

isAdsBlockEnabled() : boolean

Checks whether ad blocking is enabled.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
**true** is returned if ad blocking is enabled; otherwise, **false** is returned.

Default value: **false**.

 |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/6l5DalC7SIy7k2f24go9bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=334F6059567F4FF7F0A228A1738D2B1E46469FB6B0DF2CCD8E91E1798AEAC0C3)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isAdsBlockEnabled')
        .onClick(() => {
          try {
            let isAdsBlockEnabled: boolean = this.controller.isAdsBlockEnabled();
            console.info("isAdsBlockEnabled:", isAdsBlockEnabled);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isAdsBlockEnabledForCurPage12+

isAdsBlockEnabledForCurPage() : boolean

Checks whether ad blocking is enabled on this web page.

After ads blocking is enabled for the **Web** component, this feature is enabled for all web pages by default. You can call [addAdsBlockDisallowedList](../class-adsblockmanager/document.md#addadsblockdisallowedlist12) to disable the feature for specific domains.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if ad blocking is enabled; otherwise, **false** is returned. |

**Error codes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/k6150QJPTUiYn2QP8jr8Kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D7947B6B1966E91A74C0C690F57E2F486C0C1A160BD75206A74D30DD23BB085)

Since API version 18, exception 801 will be thrown when this API is called on a device that does not support ad blocking.

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isAdsBlockEnabledForCurPage')
        .onClick(() => {
          try {
            let isAdsBlockEnabledForCurPage: boolean = this.controller.isAdsBlockEnabledForCurPage();
            console.info("isAdsBlockEnabledForCurPage:", isAdsBlockEnabledForCurPage);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setRenderProcessMode12+

static setRenderProcessMode(mode: RenderProcessMode): void

Sets the ArkWeb render subprocess mode.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [RenderProcessMode](../enums/document.md#renderprocessmode12) | Yes | 
Render subprocess mode.

You can call [getRenderProcessMode()](#getrenderprocessmode12) to view the ArkWeb rendering subprocess mode of the current device. The enumerated value **0** indicates the single render subprocess mode, and **1** indicates the multi-render subprocess mode.

By default, mobile phones use the single render subprocess mode, and tablets and PCs/2in1 devices use the multi-render subprocess mode.

If an invalid number other than the enumerated value of **RenderProcessMode** is passed, the multi-render subprocess mode is used by default.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setRenderProcessMode')
        .onClick(() => {
          try {
            webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getRenderProcessMode12+

static getRenderProcessMode(): RenderProcessMode

Obtains the ArkWeb render subprocess mode.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RenderProcessMode](../enums/document.md#renderprocessmode12) | 
Render subprocess mode.

You can call **getRenderProcessMode()** to obtain the ArkWeb child render process mode of the current device. The enumerated value **0** indicates the single child render process mode, and **1** indicates the multi-child render process mode.

If the obtained value is not an enumerated value of **RenderProcessMode**, the multi-render subprocess mode is used by default.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getRenderProcessMode')
        .onClick(() => {
          let mode = webview.WebviewController.getRenderProcessMode();
          console.info("getRenderProcessMode: " + mode);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### terminateRenderProcess12+

terminateRenderProcess(): boolean

Terminates this render process.

Calling this API will destroy the associated render process. If the render process has not been started or has been destroyed, there is no impact. In addition, destroying the render process affects all other instances associated with the render process.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the render process is terminated.

The value **true** indicates that the render process can be destroyed or has been destroyed, and **false** indicates the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('terminateRenderProcess')
        .onClick(() => {
          let result = this.controller.terminateRenderProcess();
          console.info("terminateRenderProcess result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### postUrl11+

postUrl(url: string, postData: ArrayBuffer): void

Loads the specified URL with **postData** using the POST method. If **url** is not a network URL, it will be loaded with [loadUrl](#loadurl) instead, and the **postData** parameter will be ignored.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL to load. |
| postData | ArrayBuffer | Yes | Data to transfer using the POST method. The request must be encoded in "application/x-www-form-urlencoded" format. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(str: string): ArrayBuffer {
    let buf = new ArrayBuffer(str.length);
    let buff = new Uint8Array(buf);

    for (let i = 0; i < str.length; i++) {
      buff\[i\] = str.charCodeAt(i);
    }
    return buf;
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();

  build() {
    Column() {
      Button('postUrl')
        .onClick(() => {
          try {
            // Convert data to the ArrayBuffer type.
            let postData = this.testObjtest.test("Name=test&Password=test");
            this.controller.postUrl('www.example.com', postData);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: '', controller: this.controller })
    }
  }
}

#### createWebPrintDocumentAdapter11+

createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter

Creates a **PrintDocumentAdapter** instance to provide content for printing.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| jobName | string | Yes | Name of the file to print. |

**Return value**

| Type | Description |
| :-- | :-- |
| print.[PrintDocumentAdapter](../../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-print-print/document.md#printdocumentadapter11) | **PrintDocumentAdapter** instance created. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError, print } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('createWebPrintDocumentAdapter')
        .onClick(() => {
          try {
            let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
            print.print('example\_jobid', webPrintDocadapter, null, this.getUIContext().getHostContext());
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isIncognitoMode11+

isIncognitoMode(): boolean

Checks whether this Webview is in incognito mode.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the Webview is in incognito mode.

The value **true** indicates that incognito mode is enabled for WebView, and **false** indicates the opposite.

Default value: **false**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isIncognitoMode')
        .onClick(() => {
          try {
            let result = this.controller.isIncognitoMode();
            console.info('isIncognitoMode' + result);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getSecurityLevel11+

getSecurityLevel(): SecurityLevel

Obtains the security level of this web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [SecurityLevel](../enums/document.md#securitylevel11) | Security level of the web page. The value can be **NONE**, **SECURE**, **WARNING**, or **DANGEROUS**. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd((event) => {
          if (event) {
            let securityLevel = this.controller.getSecurityLevel();
            console.info('securityLevel: ', securityLevel);
          }
        })
    }
  }
}

#### setScrollable12+

setScrollable(enable: boolean, type?: ScrollType): void

Sets whether this web page is scrollable.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether this web page is scrollable.

The value **true** indicates that this web page is scrollable, and **false** indicates the opposite.

Default value: **true**.

 |
| type | [ScrollType](../enums/document.md#scrolltype12) | No | 

Scrolling type supported by the web page. The default value is supported.

\- If the value of **enable** is set to **false**, the specified **ScrollType** is disabled. If **ScrollType** is set to the default value, all scrolling types are disabled.

\- If the value of **enable** is set to **true**, all scrolling types are enabled regardless of the value of **ScrollType**.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setScrollable')
        .onClick(() => {
          try {
            this.controller.setScrollable(true);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getScrollable12+

getScrollable(): boolean

Obtains whether this web page is scrollable.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether this web page is scrollable.

The value **true** indicates that this web page is scrollable, and **false** indicates the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getScrollable')
        .onClick(() => {
          try {
            let scrollEnabled = this.controller.getScrollable();
            console.info("scrollEnabled: " + scrollEnabled);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setPrintBackground12+

setPrintBackground(enable: boolean): void

Sets whether to print the web page background.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to print the web page background.

The value **true** means to print the web page background, and **false** means the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setPrintBackground')
        .onClick(() => {
          try {
            this.controller.setPrintBackground(false);
          } catch (error) {
            console.error(\`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getPrintBackground12+

getPrintBackground(): boolean

Obtains whether the web page background is printed.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the web page background is printed.

The value **true** indicates that the web page background is printed, and **false** indicates the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setPrintBackground')
        .onClick(() => {
          try {
            let enable = this.controller.getPrintBackground();
            console.info("getPrintBackground: " + enable);
          } catch (error) {
            console.error(\`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getLastJavascriptProxyCallingFrameUrl12+

getLastJavascriptProxyCallingFrameUrl(): string

Obtains the URL of the last frame from which the JavaScript proxy object was called. You can inject a JavaScript object into the window object using APIs like [registerJavaScriptProxy](#registerjavascriptproxy) or [javaScriptProxy](../../../arkts-components/web/attributes/document.md#javascriptproxy). This API can be used to obtain the URL of the frame of the object that is injected last time.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the last frame from which the JavaScript proxy object was called. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testStr;
  }

  toString(): void {
    console.info('Web Component toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
  }

  testNumber(testNum: number): number {
    console.info('Web Component number' + testNum + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testNum;
  }

  testBool(testBol: boolean): boolean {
    console.info('Web Component boolean' + testBol + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testBol;
  }
}

class WebObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  webTest(): string {
    console.info('Web test ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
  }
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj(this.controller);
  @State webTestObj: WebObj = new WebObj(this.controller);

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", \["test", "toString", "testNumber", "testBool"\]);
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", \["webTest", "webString"\]);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "ArkUI Web Component"
          let str=objName.test("webtest data");
          objName.testNumber(1);
          objName.testBool(true);
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)

          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>

#### pauseAllTimers12+

static pauseAllTimers(): void

Pauses all WebView timers.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!DOCTYPE html>
<html>
    <body>
        <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
        <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
        <input style="width:300px;height:150px;font-size:50px" value="0" id="show\_num">
    </body>
</html>
<script>
    var timer = null;
    var num = 0;

    function startTimer() {
        timer = setInterval(function() {
            document.getElementById("show\_num").value = ++num;
        }, 1000);
    }
    
    function resetTimer() {
        clearInterval(timer);
        document.getElementById("show\_num").value = 0;
        num = 0;
    }
</script>

#### resumeAllTimers12+

static resumeAllTimers(): void

Resumes all timers that are paused from the **pauseAllTimers()** API.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('ResumeAllTimers')
          .onClick(() => {
            webview.WebviewController.resumeAllTimers();
          })
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}

HTML file to be loaded:

<!DOCTYPE html>
<html>
    <body>
        <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
        <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
        <input style="width:300px;height:150px;font-size:50px" value="0" id="show\_num">
    </body>
</html>
<script>
    var timer = null;
    var num = 0;

    function startTimer() {
        timer = setInterval(function() {
            document.getElementById("show\_num").value = ++num;
        }, 1000);
    }

    function resetTimer() {
        clearInterval(timer);
        document.getElementById("show\_num").value = 0;
        num = 0;
    }
</script>

#### stopAllMedia12+

stopAllMedia(): void

Stops all audio and video on a web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('stopAllMedia')
        .onClick(() => {
          try {
            this.controller.stopAllMedia();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### pauseAllMedia12+

pauseAllMedia(): void

Pauses all audio and video on a web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('pauseAllMedia')
        .onClick(() => {
          try {
            this.controller.pauseAllMedia();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### resumeAllMedia12+

resumeAllMedia(): void

Resumes the playback of the audio and video that are paused by the pauseAllMedia interface.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('resumeAllMedia')
        .onClick(() => {
          try {
            this.controller.resumeAllMedia();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### closeAllMediaPresentations12+

closeAllMediaPresentations(): void

Closes all full-screen videos on a web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('closeAllMediaPresentations')
        .onClick(() => {
          try {
            this.controller.closeAllMediaPresentations();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getMediaPlaybackState12+

getMediaPlaybackState(): MediaPlaybackState

Queries the audio and video playback status of the current web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaPlaybackState](../enums/document.md#mediaplaybackstate12) | Playback control status of the current web page. The options are **NONE**, **PLAYING**, **PAUSED**, and **STOPPED**. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getMediaPlaybackState')
        .onClick(() => {
          try {
            console.info("MediaPlaybackState : " + this.controller.getMediaPlaybackState());
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setWebSchemeHandler12+

setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void

Sets the [WebSchemeHandler](../class-webschemehandler/document.md) class for the current Web component to intercept requests of the specified scheme.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scheme | string | Yes | Protocol to be intercepted. |
| handler | [WebSchemeHandler](../class-webschemehandler/document.md) | Yes | Interceptor that intercepts this protocol. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('setWebSchemeHandler')
        .onClick(() => {
          try {
            this.controller.setWebSchemeHandler('http', this.schemeHandler);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearWebSchemeHandler12+

clearWebSchemeHandler(): void

Clears all WebSchemeHandlers set for the current Web component.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearWebSchemeHandler')
        .onClick(() => {
          try {
            this.controller.clearWebSchemeHandler();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setServiceWorkerWebSchemeHandler12+

setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void

Sets the WebSchemeHandler used to intercept ServiceWorker for all Web components of the current application.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scheme | string | Yes | Protocol to be intercepted. |
| handler | [WebSchemeHandler](../class-webschemehandler/document.md) | Yes | Interceptor that intercepts this protocol. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('setWebSchemeHandler')
        .onClick(() => {
          try {
            webview.WebviewController.setServiceWorkerWebSchemeHandler('http', this.schemeHandler);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearServiceWorkerWebSchemeHandler12+

clearServiceWorkerWebSchemeHandler(): void

Clears all WebSchemeHandlers that are set in the application and used to intercept ServiceWorker.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearServiceWorkerWebSchemeHandler')
        .onClick(() => {
          webview.WebviewController.clearServiceWorkerWebSchemeHandler();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### startCamera12+

startCamera(): void

Enables the camera capture of the current web page. Before using the camera, add the **ohos.permission.CAMERA** permission to **module.json5**. For details about how to add the permission, see [Declaring Permissions in the Configuration File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, \['ohos.permission.CAMERA'\], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("startCamera").onClick(() => {
        try {
          this.controller.startCamera();
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
      Button("stopCamera").onClick(() => {
        try {
          this.controller.stopCamera();
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
      Button("closeCamera").onClick(() => {
        try {
          this.controller.closeCamera();
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
    }
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <video id="video" width="400px" height="400px" autoplay>
    </video>
    <input type="button" title="HTML5 Camera" value="Enable Camera" onclick="getMedia()" />
    <script>
      function getMedia() {
        let constraints = {
          video: {
            width: 500,
            height: 500
          },
          audio: true
        }
        let video = document.getElementById("video");
        let promise = navigator.mediaDevices.getUserMedia(constraints);
        promise.then(function(mediaStream) {
          video.srcObject = mediaStream;
          video.play();
        })
      }
    </script>
  </body>
</html>

#### stopCamera12+

stopCamera(): void

Stops the camera capture of the current web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

For the complete sample code, see [startCamera](#startcamera12).

#### closeCamera12+

closeCamera(): void

Disables the camera capture of the current web page.

**System capability**: SystemCapability.Web.Webview.Core

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

For the complete sample code, see [startCamera](#startcamera12).

#### precompileJavaScript12+

precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>

Precompiles JavaScript to generate the bytecode cache or update the existing bytecode cache based on the provided parameters.

The API determines whether to update the existing bytecode cache based on the provided file information, E-Tag response header, and Last-Modified response header.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | Network address corresponding to the local JavaScript file, that is, the network address used when the service web page requests the server version of the file. The network address supports only the HTTP and HTTPS protocols and contains a maximum of 2048 characters. If the cache corresponding to the network address is invalid, the service web page requests the corresponding resource through the network. |
| script | string | Uint8Array | Yes | Text content of the local JavaScript. The content cannot be empty. |
| cacheOptions | [CacheOptions](../interfaces-others/document.md#cacheoptions12) | Yes | Whether to update the bytecode cache. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the error code for generating the bytecode cache. The value **0** indicates no error, and the value **\-1** indicates an internal error. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid input parameter.Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

The API is recommended for use in conjunction with dynamic components. Employ offline **Web** components to generate bytecode caches, and at the appropriate time, load service **Web** components to utilize these bytecode caches. The following is a code example:

1.  First, store [UIContext](../../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) in [localStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) in the EntryAbility.
    
    // EntryAbility.ets
    import { UIAbility } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    
    const localStorage: LocalStorage = new LocalStorage('uiContext');
    
    export default class EntryAbility extends UIAbility {
      storage: LocalStorage = localStorage;
    
      onWindowStageCreate(windowStage: window.WindowStage) {
        windowStage.loadContent('pages/Index', this.storage, (err, data) => {
          if (err.code) {
            return;
          }
    
          this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
        });
      }
    }
    
2.  Write the basic code required by the dynamic component.
    
    // DynamicComponent.ets
    import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
    
    export interface BuilderData {
      url: string;
      controller: WebviewController;
      context: UIContext;
    }
    
    let storage : LocalStorage | undefined = undefined;
    
    export class NodeControllerImpl extends NodeController {
      private rootNode: BuilderNode<BuilderData\[\]> | null = null;
      private wrappedBuilder: WrappedBuilder<BuilderData\[\]> | null = null;
    
      constructor(wrappedBuilder: WrappedBuilder<BuilderData\[\]>, context: UIContext) {
        storage = context.getSharedLocalStorage();
        super();
        this.wrappedBuilder = wrappedBuilder;
      }
    
      makeNode(): FrameNode | null {
        if (this.rootNode != null) {
          return this.rootNode.getFrameNode();
        }
        return null;
      }
    
      initWeb(url: string, controller: WebviewController) {
        if(this.rootNode != null) {
          return;
        }
    
        const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
        if (!uiContext) {
          return;
        }
        this.rootNode = new BuilderNode(uiContext);
        this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
      }
    }
    
    export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData\[\]>, data: BuilderData) => {
      const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
      baseNode.initWeb(data.url, data.controller);
      return baseNode;
    }
    
3.  Write a component for generating bytecode caches. In this example, the local JavaScript resource content is read through the file reading API from a local file in the **rawfile** directory.
    
    // PrecompileWebview.ets
    import { BuilderData } from "./DynamicComponent";
    import { Config, configs } from "./PrecompileConfig";
    
    @Builder
    function WebBuilder(data: BuilderData) {
      Web({ src: data.url, controller: data.controller })
        .onControllerAttached(() => {
          precompile(data.controller, configs, data.context);
        })
        .fileAccess(true)
    }
    
    export const precompileWebview = wrapBuilder<BuilderData\[\]>(WebBuilder);
    
    export const precompile = async (controller: WebviewController, configs: Array<Config>, context: UIContext) => {
      for (const config of configs) {
        let content = await readRawFile(config.localPath, context);
    
        try {
          controller.precompileJavaScript(config.url, content, config.options)
            .then(errCode => {
              console.error("precompile successfully! " + errCode);
            }).catch((errCode: number) => {
              console.error("precompile failed. " + errCode);
          });
        } catch (err) {
          console.error("precompile failed. " + err.code + " " + err.message);
        }
      }
    }
    
    async function readRawFile(path: string, context: UIContext) {
      try {
        return await context.getHostContext()!.resourceManager.getRawFileContent(path);
      } catch (err) {
        return new Uint8Array(0);
      }
    }
    
    JavaScript resources can also be obtained through [network requests](../../../../../system/network/network-kit/arkts-apis/ohos-net-http-data-request/document.md). However, the HTTP response header obtained using this method is not in the standard HTTP response header format. Additional steps are required to convert the response header into the standard HTTP response header format before use. If the response header obtained through a network request is e-tag, convert it to E-Tag before using it.
    
4.  Compile the code of the service component.
    
    // BusinessWebview.ets
    import { BuilderData } from "./DynamicComponent";
    
    @Builder
    function WebBuilder(data: BuilderData) {
      // The component can be extended based on service requirements.
      Web({ src: data.url, controller: data.controller })
        .cacheMode(CacheMode.Default)
    }
    
    export const businessWebview = wrapBuilder<BuilderData\[\]>(WebBuilder);
    
5.  Write the resource configuration information.
    
    // PrecompileConfig.ets
    import { webview } from '@kit.ArkWeb'
    
    export interface Config {
      url:  string,
      localPath: string, // Local resource path
      options: webview.CacheOptions
    }
    
    export let configs: Array<Config> = \[
      {
        url: "https://www.example.com/example.js",
        localPath: "example.js",
        options: {
          responseHeaders: \[
            { headerKey: "E-Tag", headerValue: "aWO42N9P9dG/5xqYQCxsx+vDOoU="},
            { headerKey: "Last-Modified", headerValue: "Wed, 21 Mar 2024 10:38:41 GMT"}
          \]
        }
      }
    \]
    
6.  Use the component on the page.
    
    // Index.ets
    import { webview } from '@kit.ArkWeb';
    import { NodeController } from '@kit.ArkUI';
    import { createNode } from "./DynamicComponent"
    import { precompileWebview } from "./PrecompileWebview"
    import { businessWebview } from "./BusinessWebview"
    
    @Entry
    @Component
    struct Index {
      @State precompileNode: NodeController | undefined = undefined;
      precompileController: webview.WebviewController = new webview.WebviewController();
    
      @State businessNode: NodeController | undefined = undefined;
      businessController: webview.WebviewController = new webview.WebviewController();
    
      aboutToAppear(): void {
        // Initialize the Web component used to inject local resources.
        this.precompileNode = createNode(precompileWebview,
          { url: "https://www.example.com/empty.html", controller: this.precompileController, context: this.getUIContext()});
      }
    
      build() {
        Column() {
          // Load the Web component used by the service at a proper time. In this example, the button is clicked.
          Button("Load Page")
            .onClick(() => {
              this.businessNode = createNode(businessWebview, {
                url:  "https://www.example.com/business.html",
                controller: this.businessController,
                context: this.getUIContext()
              });
            })
          // The Web component used for the service.
          NodeContainer(this.businessNode);
        }
      }
    }
    

To update the locally generated compiled bytecode, change the value of E-Tag or Last-Modified in responseHeaders of the cacheOptions parameter and call the API again.

#### onCreateNativeMediaPlayer12+

onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void

Called when the [application takes over media playback of the web page](../../../arkts-components/web/attributes/document.md#enablenativemediaplayer12) and a media file is played on the web page.

If the application does not take over media playback on the web page, this callback is not invoked.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [CreateNativeMediaPlayerCallback](../types/document.md#createnativemediaplayercallback12) | Yes | Callback when the application takes over media playback on the web page. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

class ActualNativeMediaPlayerListener {
  handler: webview.NativeMediaPlayerHandler;

  constructor(handler: webview.NativeMediaPlayerHandler) {
    this.handler = handler;
  }

  onPlaying() {
    // The native media player starts playback.
    this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
  }
  onPaused() {
    // The native media player pauses the playback.
    this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
  }
  onSeeking() {
    // The local player starts to jump to the target time point.
    this.handler.handleSeeking();
  }
  onSeekDone() {
    // The native media player seeks to the target time point.
    this.handler.handleSeekFinished();
  }
  onEnded() {
    // The playback on the native media player is ended.
    this.handler.handleEnded();
  }
  onVolumeChanged() {
    // Obtain the volume of the local player.
    let volume: number = getVolume();
    this.handler.handleVolumeChanged(volume);
  }
  onCurrentPlayingTimeUpdate() {
    // Update the playback time.
    let currentTime: number = getCurrentPlayingTime();
    // Convert the time unit to second.
    let currentTimeInSeconds = convertToSeconds(currentTime);
    this.handler.handleTimeUpdate(currentTimeInSeconds);
  }
  onBufferedChanged() {
    // The cache is changed.
    // Obtain the cache duration of the native media player.
    let bufferedEndTime: number = getCurrentBufferedTime();
    // Convert the time unit to second.
    let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
    this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

    // Check the cache status.
    // If the cache status changes, notify the ArkWeb engine of the cache status.
    let lastReadyState: webview.ReadyState = getLastReadyState();
    let currentReadyState:  webview.ReadyState = getCurrentReadyState();
    if (lastReadyState != currentReadyState) {
      this.handler.handleReadyStateChanged(currentReadyState);
    }
  }
  onEnterFullscreen() {
    // The native media player enters the full screen mode.
    let isFullscreen: boolean = true;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onExitFullscreen() {
    // The native media player exits the full screen mode.
    let isFullscreen: boolean = false;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onUpdateVideoSize(width: number, height: number) {
    // Notify the ArkWeb kernel when the native media player parses the video width and height.
    this.handler.handleVideoSizeChanged(width, height);
  }
  onDurationChanged(duration: number) {
    // Notify the ArkWeb kernel when the native media player parses the video duration.
    this.handler.handleDurationChanged(duration);
  }
  onError(error: webview.MediaError, errorMessage: string) {
    // Notify the ArkWeb kernel that an error occurs in the native media player.
    this.handler.handleError(error, errorMessage);
  }
  onNetworkStateChanged(state: webview.NetworkState) {
    // Notify the ArkWeb kernel that the network state of the native media player changes.
    this.handler.handleNetworkStateChanged(state);
  }
  onPlaybackRateChanged(playbackRate: number) {
    // Notify the ArkWeb kernel that the playback rate of the native media player changes.
    this.handler.handlePlaybackRateChanged(playbackRate);
  }
  onMutedChanged(muted: boolean) {
    // Notify the ArkWeb kernel that the native media player is muted.
    this.handler.handleMutedChanged(muted);
  }

  // Listen for other state of the native media player.
}

class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
  constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
    // 1. Create a listener for the native media player.
    let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
    // 2. Create a native media player.
    // 3. Listen for the local player.
    // ...
  }

  updateRect(x: number, y: number, width: number, height: number) {
    // The position and size of the <video> tag are changed.
    // Make changes based on the information change.
  }

  play() {
    // Start the native media player for playback.
  }

  pause() {
    //Pause the playback on the local player.
  }

  seek(targetTime: number) {
    // The local player jumps to a specified time point.
  }

  release() {
    // Destroy the local player.
  }

  setVolume(volume: number) {
    // The ArkWeb kernel requires to adjust the volume of the local player.
    // Set the volume of the local player.
  }

  setMuted(muted: boolean) {
    // Mute or unmute the local player.
  }

  setPlaybackRate(playbackRate: number) {
    // Adjust the playback speed of the local player.
  }

  enterFullscreen() {
    // Set the local player to play in full screen mode.
  }

  exitFullscreen() {
    // Set the local player to exit full screen mode.
  }

  resumePlayer() {
    // Create a player again.
    // Resume the status information of the player.
  }

  suspendPlayer(type: webview.SuspendType) {
    // Record the status information of the player.
    // Destroy the player.
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
        .onPageBegin((event) => {
          this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
            if (!shouldHandle(mediaInfo)) {
              // The local player does not take over the media.
              // The ArkWeb engine will play the media with its own player.
              return null;
            }
            let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
            return nativePlayer;
          });
        })
    }
  }
}

// stub
function getVolume() {
  return 1;
}
function getCurrentPlayingTime() {
  return 1;
}
function getCurrentBufferedTime() {
  return 1;
}
function convertToSeconds(input: number) {
  return input;
}
function getLastReadyState() {
  return webview.ReadyState.HAVE\_NOTHING;
}
function getCurrentReadyState() {
  return webview.ReadyState.HAVE\_NOTHING;
}
function shouldHandle(mediaInfo: webview.MediaInfo) {
  return true;
}

#### enableWholeWebPageDrawing12+

static enableWholeWebPageDrawing(): void

Enables the full drawing capability for the web page. This API works only during **Web** component initialization.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.enableWholeWebPageDrawing();
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### webPageSnapshot12+

webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void

Obtains the full drawing result of the web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/L96AyRFZSLiLk3xVLBUaiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1784991F1EBD371D3C6F6687061ED5D6E335D9A6198DB7EB8563C8904D9F425)

This API does not support concurrent calls.

Only static images and texts in the rendering process can be captured.

If there is a video on the page, the placeholder image of the video is displayed when you take a snapshot. If there is no placeholder image, the page is blank.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [SnapshotInfo](../interfaces-others/document.md#snapshotinfo12) | Yes | Information for obtaining the full drawing result. |
| callback | AsyncCallback<[SnapshotResult](../interfaces-others/document.md#snapshotresult12)\> | Yes | Callback used to return the result. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('webPageSnapshot')
        .onClick(() => {
          try {
            this.controller.webPageSnapshot({ id: "1234", size: { width: 100, height: 100 } }, (error, result) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              if (result) {
                console.info(\`return value is:${result}\`);
                // You can process the returned result as required.
              }
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### injectOfflineResources12+

injectOfflineResources(resourceMaps: Array<[OfflineResourceMap](../interfaces-others/document.md#offlineresourcemap12)\>): void

Injects local offline resources to the memory cache to improve the initial page startup speed.

Resources in the memory cache are automatically managed by the ArkWeb engine. When the injected resources are excessive and cause significant memory pressure, the engine will automatically release unused resources. It is advisable to avoid injecting a large number of resources into the memory cache.

Under normal circumstances, the validity period of the resources is controlled by the provided Cache-Control or Expires response header, with a default validity period of 86,400 seconds, which is one day.

The MIME type of the resources is configured through the provided Content-Type response header. The Content-Type must comply with standards; otherwise, the resources cannot be used correctly. For resources of type MODULE\_JS, a valid MIME type must be provided. For other types, the MIME type is optional.

Resources injected in this mode can be loaded only through HTML tags. If a **script** tag on the web page uses the **crossorigin** attribute, the **Cross-Origin** response header must be set in the **responseHeaders** parameter of the API. The value for this header should be **anonymous** or **use-credentials**.

After **webview.WebviewController.SetRenderProcessMode(webview.RenderProcessMode.MULTIPLE)** is called, the application starts the multi-rendering process mode. This API does not take effect in this scenario.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resourceMaps | Array<[OfflineResourceMap](../interfaces-others/document.md#offlineresourcemap12)\> | Yes | Configuration object for local offline resources. A maximum of 30 resources can be injected in a single call, with a maximum size of 10 MB per individual resource. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 17100002 | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2\*1024\*1024. |

**Example**

When appropriate, use this API in conjunction with dynamic components. Offline **Web** components are used to inject resources into the engine's memory cache, and at the appropriate time, the service **Web** components load and utilize these resources. The following is a code example:

1.  First, store [UIContext](../../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) in [localStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) in the EntryAbility.
    
    // EntryAbility.ets
    import { UIAbility } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    
    const localStorage: LocalStorage = new LocalStorage('uiContext');
    
    export default class EntryAbility extends UIAbility {
      storage: LocalStorage = localStorage;
    
      onWindowStageCreate(windowStage: window.WindowStage) {
        windowStage.loadContent('pages/Index', this.storage, (err, data) => {
          if (err.code) {
            return;
          }
    
          this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
        });
      }
    }
    
2.  Write the basic code required by the dynamic component.
    
    // DynamicComponent.ets
    import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
    
    export interface BuilderData {
      url: string;
      controller: WebviewController;
      context: UIContext;
    }
    
    let storage : LocalStorage | undefined = undefined;
    
    export class NodeControllerImpl extends NodeController {
      private rootNode: BuilderNode<BuilderData\[\]> | null = null;
      private wrappedBuilder: WrappedBuilder<BuilderData\[\]> | null = null;
    
      constructor(wrappedBuilder: WrappedBuilder<BuilderData\[\]>, context: UIContext) {
        storage = context.getSharedLocalStorage();
        super();
        this.wrappedBuilder = wrappedBuilder;
      }
    
      makeNode(): FrameNode | null {
        if (this.rootNode != null) {
          return this.rootNode.getFrameNode();
        }
        return null;
      }
    
      initWeb(url: string, controller: WebviewController) {
        if(this.rootNode != null) {
          return;
        }
    
        const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
        if (!uiContext) {
          return;
        }
        this.rootNode = new BuilderNode(uiContext);
        this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
      }
    }
    
    export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData\[\]>, data: BuilderData) => {
      const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
      baseNode.initWeb(data.url, data.controller);
      return baseNode;
    }
    
3.  Write the component code for injecting resources. In this example, the local resource content reads the local file in the **rawfile** directory through the file reading API.
    
    // InjectWebview.ets
    import { webview } from '@kit.ArkWeb';
    import { resourceConfigs } from "./Resource";
    import { BuilderData } from "./DynamicComponent";
    
    @Builder
    function WebBuilder(data: BuilderData) {
      Web({ src: data.url, controller: data.controller })
        .onControllerAttached(async () => {
          try {
            data.controller.injectOfflineResources(await getData (data.context));
          } catch (err) {
            console.error("error: " + err.code + " " + err.message);
          }
        })
        .fileAccess(true)
    }
    
    export const injectWebview = wrapBuilder<BuilderData\[\]>(WebBuilder);
    
    export async function getData(context: UIContext) {
      const resourceMapArr: Array<webview.OfflineResourceMap> = \[\];
    
      // Read the configuration and read the file content from the rawfile directory.
      for (let config of resourceConfigs) {
        let buf: Uint8Array = new Uint8Array(0);
        if (config.localPath) {
          buf = await readRawFile(config.localPath, context);
        }
    
        resourceMapArr.push({
          urlList: config.urlList,
          resource: buf,
          responseHeaders: config.responseHeaders,
          type: config.type,
        })
      }
    
      return resourceMapArr;
    }
    
    export async function readRawFile(url: string, context: UIContext) {
      try {
        return await context.getHostContext()!.resourceManager.getRawFileContent(url);
      } catch (err) {
        return new Uint8Array(0);
      }
    }
    
4.  Compile the code of the service component.
    
    // BusinessWebview.ets
    import { BuilderData } from "./DynamicComponent";
    
    @Builder
    function WebBuilder(data: BuilderData) {
      // The component can be extended based on service requirements.
      Web({ src: data.url, controller: data.controller })
        .cacheMode(CacheMode.Default)
    }
    
    export const businessWebview = wrapBuilder<BuilderData\[\]>(WebBuilder);
    
5.  Write the resource configuration information.
    
    // Resource.ets
    import { webview } from '@kit.ArkWeb';
    
    export interface ResourceConfig {
      urlList: Array<string>,
      type: webview.OfflineResourceType,
      responseHeaders: Array<Header>,
      localPath: string, // Path for storing local resources in the rawfile directory.
    }
    
    export const resourceConfigs: Array<ResourceConfig> = \[
      {
        localPath: "example.png",
        urlList: \[
          "https://www.example.com/",
          "https://www.example.com/path1/example.png",
          "https://www.example.com/path2/example.png",
        \],
        type: webview.OfflineResourceType.IMAGE,
        responseHeaders: \[
          { headerKey: "Cache-Control", headerValue: "max-age=1000" },
          { headerKey: "Content-Type", headerValue: "image/png" },
        \]
      },
      {
        localPath: "example.js",
        urlList: \[ // Only one URL is provided. This URL is used as both the resource origin and the network request address of the resource.
          "https://www.example.com/example.js",
        \],
        type: webview.OfflineResourceType.CLASSIC\_JS,
        responseHeaders: \[
          // Used in <script crossorigin="anonymous" /> mode to provide additional response headers.
          { headerKey: "Cross-Origin", headerValue:"anonymous" }
        \]
      },
    \];
    
6.  Use the component on the page.
    
    // Index.ets
    import { webview } from '@kit.ArkWeb';
    import { NodeController } from '@kit.ArkUI';
    import { createNode } from "./DynamicComponent"
    import { injectWebview } from "./InjectWebview"
    import { businessWebview } from "./BusinessWebview"
    
    @Entry
    @Component
    struct Index {
      @State injectNode: NodeController | undefined = undefined;
      injectController: webview.WebviewController = new webview.WebviewController();
    
      @State businessNode: NodeController | undefined = undefined;
      businessController: webview.WebviewController = new webview.WebviewController();
    
      aboutToAppear(): void {
        // Initialize the Web component used to inject local resources and provide an empty HTML page as the URL.
        this.injectNode = createNode(injectWebview,
            { url: "https://www.example.com/empty.html", controller: this.injectController, context: this.getUIContext()});
      }
    
      build() {
        Column() {
          // Load the Web component used by the service at a proper time. In this example, the button is clicked.
          Button("Load Page")
            .onClick(() => {
              this.businessNode = createNode(businessWebview, {
                url: "https://www.example.com/business.html",
                controller: this.businessController,
                context: this.getUIContext()
              });
            })
          // The Web component used for the service.
          NodeContainer(this.businessNode);
        }
      }
    }
    
7.  Example of a loaded HTML web page:
    
    <!DOCTYPE html>
    <html lang="en">
    <head></head>
    <body>
      <img src="https://www.example.com/path1/request.png" />
      <img src="https://www.example.com/path2/request.png" />
      <script src="https://www.example.com/example.js" crossorigin="anonymous"></script>
    </body>
    </html>
    

#### setHostIP12+

static setHostIP(hostName: string, address: string, aliveTime: number): void

Sets the IP address of the host after domain name resolution.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hostName | string | Yes | Domain name of the host whose DNS records are to be added. |
| address | string | Yes | Host domain name resolution address (IPv4 and IPv6). |
| aliveTime | number | Yes | Cache validity period, in seconds. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

**Example**

For details, see [clearHostIP](#clearhostip12).

#### clearHostIP12+

static clearHostIP(hostName: string): void

Clears the IP address of a specified host after domain name resolution.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hostName | string | Yes | Domain name of the host whose DNS records are to be cleared. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // The setting takes effect before the URL is loaded.
      Button('setHostIP')
        .onClick(() => {
          try {
            webview.WebviewController.setHostIP('www.example.com', '127.0.0.1', 30);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('clearHostIP')
        .onClick(() => {
          try {
            webview.WebviewController.clearHostIP('www.example.com');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getSurfaceId12+

getSurfaceId(): string

Obtains the ID of the surface corresponding to ArkWeb. The ID can be used to capture a screenshot of the web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/pSQ7Gk-HTpO7O577ST0kHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A52F8B07D284AAB6C1C1D98F37EBC69C503EB908325EDAE49D196EA8B71D913)

This API is valid only when the **Web** component rendering mode is **ASYNC\_RENDER**. The value of **getSurfaceId** can be obtained only after the **Web** component is initialized.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | ID of the surface held by ArkWeb. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Example{
  controller: webview.WebviewController = new webview.WebviewController();

  @State imagePixelMap: image.PixelMap | undefined = undefined;

  build(){
    Column(){
      Button("Screenshot")
        .onClick(()=>{
          try {
            let surfaceId = this.controller.getSurfaceId();
            console.info("surfaceId: " + surfaceId);
            if(surfaceId.length != 0) {
              let region:image.Region = { x: 0, y: 0, size: { height: 800, width: 1000}}
              this.imagePixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region)
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Image(this.imagePixelMap)
        .height(100)
      Web({src: 'www.example.com', controller: this.controller})
    }
  }
}

#### setUrlTrustList12+

setUrlTrustList(urlTrustList: string): void

Sets the URL trustlist of the web page. Only URLs in the trustlist can be loaded or redirected. Otherwise, the URL is blocked and an alarm page is displayed.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| urlTrustList | string | Yes | 
URL trustlist, which is configured in JSON format. The maximum size is 10 MB.

**setUrlTrustList()** is used in overwrite mode. If it is called for multiple times, the latest setting overwrites the previous setting.

If this parameter is left blank, the trustlist is canceled and access to all URLs is allowed.

Example in JSON format:

{

"UrlPermissionList": \[

{

"scheme": "https",

"host": "www.example1.com",

"port": 443,

"path": "pathA/pathB"

},

{

"scheme": "http",

"host": "www.example2.com",

"port": 80,

"path": "test1/test2/test3"

}

\]

}

 |

**Parameters in JSON format**:

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scheme | string | No | Optional parameter. The supported protocols are HTTP and HTTPS. |
| host | string | Yes | Mandatory parameter. The URL is permitted only when its host field is the same as the rule field. Multiple rules for the same host at the same time are allowed. |
| port | number | No | Optional parameter. |
| path | string | No | Optional field. If not set, this item will not be matched. The matching mode is prefix matching. Taking **pathA/pathB/pathC** as an example: all content under the three-level directory **pathA/pathB/pathC** is allowed to be accessed. Among them, **pathC** must be a complete directory name or file name and partial matching is not allowed. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Parameter string is too long.3. Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  urltrustList: string = "{\\"UrlPermissionList\\":\[{\\"scheme\\":\\"http\\", \\"host\\":\\"trust.example.com\\", \\"port\\":80, \\"path\\":\\"test\\"}\]}"

  build() {
    Column() {
      Button('Setting the trustlist')
        .onClick(() => {
          try {
            // Set a trustlist to allow access only to trust web pages.
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // Input an empty string to setUrlTrustList() to disable the trustlist, and all URLs can be accessed.
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // The trustlist is enabled and trust web pages can be accessed.
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // The trustlist is enabled that untrust web pages cannot be accessed and an error page is displayed.
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // Set the trustlist using onControllerAttached() to enable the trustlist before the URL starts to be loaded. The untrusted web page cannot be accessed, and an error page is displayed.
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
    }
  }
}

#### setPathAllowingUniversalAccess12+

setPathAllowingUniversalAccess(pathList: Array<string>): void

Sets a path list. When the file protocol accesses resources in the path list, cross-origin access to local files and other online resources is allowed. In addition, when a path list is set, the file protocol can access only the resources in the path list. The behavior of [fileAccess](../../../arkts-components/web/attributes/document.md#fileaccess) will be overwritten by that of this API.

Allowing cross-origin access to directories by using setPathAllowingUniversalAccess is a high-risk operation. Based on the principle of least privilege, the paths accessible for el1 and el2 are fixed.Paths in the path list must conform to any one of the following path formats:

1.  The path of subdirectory of the application file directory. (The application file directory is obtained using [Context.filesDir](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#properties) in the Ability Kit.) For example:

-   /data/storage/el2/base/files/example
-   /data/storage/el2/base/haps/entry/files/example

1.  The path of application resource directory and its subdirectory. (The application resource directory is obtained from [Context.resourceDir](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#properties) in the Ability Kit.) For example:

-   /data/storage/el1/bundle/entry/resources/resfile
-   /data/storage/el1/bundle/entry/resources/resfile/example

1.  Since API version 21, the application cache directory and its subdirectories are also supported. (The application cache directory is obtained through [Context.cacheDir](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#properties) in the Ability Kit). For example:

-   /data/storage/el2/base/cache
-   /data/storage/el2/base/haps/entry/cache/example
-   The **cache/web** directory is not allowed. If it is included, an exception with the code **401** will be thrown. If the **cache** directory is set, **cache/web** cannot be accessed.

1.  Since API version 21, the temporary application directory and its subdirectories are also supported. (The temporary application directory is obtained through [Context.tempDir](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#properties) in the Ability Kit). For example:

-   /data/storage/el2/base/temp
-   /data/storage/el2/base/haps/entry/temp/example

If a path in the list is not of the preceding paths, error code 401 is reported and the path list fails to be set. When the path list is set to empty, the accessible files for the file protocol are subject to the behavior of the [fileAccess](../../../arkts-components/web/attributes/document.md#fileaccess).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pathList | Array<string> | Yes | The path list. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Row() {
      Web({ src: "", controller: this.controller })
        .onControllerAttached(() => {
          try {
            // Set the list of paths that can be accessed across domains.
            this.controller.setPathAllowingUniversalAccess(\[
              this.uiContext.getHostContext()!.resourceDir,
              this.uiContext.getHostContext()!.filesDir + "/example"
            \])
            this.controller.loadUrl("file://" + this.getUIContext().getHostContext()!.resourceDir + "/index.html")
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
        .javaScriptAccess(true)
        .fileAccess(true)
        .domStorageAccess(true)
    }
  }
}

Load the HTML file, which is located in the application resource directory **resource/resfile/index.html**.

<!-- index.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, viewport-fit=cover">
    <script>
        function getFile() {
            var file = "file:///data/storage/el1/bundle/entry/resources/resfile/js/script.js";
            var xmlHttpReq = new XMLHttpRequest();
            xmlHttpReq.onreadystatechange = function(){
                console.info("readyState:" + xmlHttpReq.readyState);
                console.info("status:" + xmlHttpReq.status);
                if(xmlHttpReq.readyState == 4){
                    if (xmlHttpReq.status == 200) {
                // If the path list is set on the eTS, resources can be obtained.
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " success";
                    } else {
                // If the path list is not set on the eTS, a CORS error is triggered.
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " failed";
                    }
                }
            }
            xmlHttpReq.open("GET", file);
            xmlHttpReq.send(null);
        }

    </script>
</head>

<body>
<div class="page">
    <button id="example" onclick="getFile()">stealFile</button>
</div>
<div id="text"></div>
</body>

</html>

In the HTML file, use the file protocol to access the local JS file through **XMLHttpRequest**. The JS file is stored in **resource/resfile/js/script.js**.

const body = document.body;
const element = document.createElement('div');
element.textContent = 'success';
body.appendChild(element);

#### enableBackForwardCache12+

static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void

Enables the back-forward cache of a **Web** component. You can specify whether to add a specific page to the back-forward cache.

This API must be called before [initializeWebEngine()](#initializewebengine) initializes the kernel.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| features | [BackForwardCacheSupportedFeatures](../class-backforwardcachesupportedfeatures/document.md) | Yes | Features of the pages, which allow them to be added to the back-forward cache. |

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        let features = new webview.BackForwardCacheSupportedFeatures();
        features.nativeEmbed = true;
        features.mediaTakeOver = true;
        // If a page uses the same-layer rendering and takes over media playback at the same time,
        // you need to set the values of nativeEmbed and mediaTakeOver to true to add the page to the back-forward cache.
        webview.WebviewController.enableBackForwardCache(features);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
}

#### setBackForwardCacheOptions12+

setBackForwardCacheOptions(options: BackForwardCacheOptions): void

Sets the back-forward cache options of the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [BackForwardCacheOptions](../class-backforwardcacheoptions/document.md) | Yes | Options to control the back-forward cache of the **Web** component. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button("Add options").onClick((event: ClickEvent) => {
          let options = new webview.BackForwardCacheOptions();
          options.size = 3;
          options.timeToLive = 10;
          this.controller.setBackForwardCacheOptions(options);
        })
        Button("Backward").onClick((event: ClickEvent) => {
          this.controller.backward();
        })
        Button("Forward").onClick((event: ClickEvent) => {
          this.controller.forward();
        })
      }
      Web({ src: "https://www.example.com", controller: this.controller })
    }
    .height('100%')
    .width('100%')
  }
}

#### trimMemoryByPressureLevel14+

trimMemoryByPressureLevel(level: PressureLevel): void

Clears the cache occupied by **Web** component based on the specified memory pressure level.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| level | [PressureLevel](../enums/document.md#pressurelevel14) | Yes | Pressure level of the memory to be cleared. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Row() {
        Button('trim\_Memory')
          .onClick(() => {
            try {
              // Set the current memory pressure level to moderate and release a small amount of memory.
              webview.WebviewController.trimMemoryByPressureLevel(
                webview.PressureLevel.MEMORY\_PRESSURE\_LEVEL\_MODERATE);
            } catch (error) {
              console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
            }
          })
      }.height('10%')
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### createPdf14+

createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void

Obtains the data stream of a specified web page using an asynchronous callback.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configuration | [PdfConfiguration](../interfaces-others/document.md#pdfconfiguration14) | Yes | Parameters required for creating a PDF file. |
| callback | AsyncCallback<[PdfData](../class-pdfdata/document.md)\> | Yes | Callback used to return the data stream of an online PDF file. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid input parameter. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  }

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(
            this.pdfConfig,
            (error, result: webview.PdfData) => {
              try {
                // Obtain the component context.
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // Obtain the sandbox path and set the PDF file name.
                let filePath = context.filesDir + "/test.pdf";
                let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
                fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeed and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fs.closeSync(file);
                });
              } catch (resError) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            });
        })
      Web({ src: "www.example.com", controller: this.controller })
    }
  }
}

#### createPdf14+

createPdf(configuration: PdfConfiguration): Promise<PdfData>

Obtains the data stream of a specified web page using a promise.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configuration | [PdfConfiguration](../interfaces-others/document.md#pdfconfiguration14) | Yes | Parameters required for creating a PDF file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PdfData](../class-pdfdata/document.md)\> | Promise used to return the data stream of a web page. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid input parameter. |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  }

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(this.pdfConfig)
            .then((result: webview.PdfData) => {
              try {
                // Obtain the component context.
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // Obtain the sandbox path and set the PDF file name.
                let filePath = context.filesDir + "/test.pdf";
                let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
                fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeed and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fs.closeSync(file);
                });
              } catch (resError) {
                console.error(\`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}\`);
              }
            })
        })
      Web({ src: "www.example.com", controller: this.controller })
    }
  }
}

#### getScrollOffset13+

getScrollOffset(): ScrollOffset

Obtains the current scrolling offset (including the over-scrolling offset) of the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ScrollOffset](../interfaces-others/document.md#scrolloffset13) | Current scrolling offset (including the over-scrolling offset) of the web page. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State testTitle: string = 'webScroll'
  controller: webview.WebviewController = new webview.WebviewController();
  @State controllerX: number =-100;
  @State controllerY: number =-100;
  @State mode: OverScrollMode = OverScrollMode.ALWAYS;

  build() {
    Column() {
      Row() {
        Text(this.testTitle)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin(5)
      }
      Column() {
        Text(\`controllerX: ${this.controllerX}, controllerY: ${this.controllerY}\`)
      }
      .margin({ top: 10, bottom: 10 })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .key("web\_01")
        .overScrollMode(this.mode)
        .onTouch(() => {
          this.controllerX = this.controller.getScrollOffset().x;
          this.controllerY = this.controller.getScrollOffset().y;
          let componentInfo = this.getUIContext().getComponentUtils().getRectangleById("web\_01");
          let webHeight = this.getUIContext().px2vp(componentInfo.size.height);
          let pageHeight = this.controller.getPageHeight();
          if (this.controllerY < 0) {
            // Case 1: When a web page is scrolled down, use ScrollOffset.y directly.
            console.info(\`get downwards overscroll offsetY = ${this.controllerY}\`);
          } else if ((this.controllerY != 0) && (this.controllerY > (pageHeight - webHeight))) {
            // Case 2: When a web page is scrolled up, calculate the offset between the lower boundary of the web page and that of the Web component.
            console.info(\`get upwards overscroll offsetY = ${this.controllerY - (pageHeight >= webHeight ? (pageHeight - webHeight) : 0)}\`);
          } else {
            // Case 3: If the web page is not scrolled, use ScrollOffset.y directly.
            console.info(\`get scroll offsetY = ${this.controllerY}\`);
          }
        })
        .height(600)
    }
    .width('100%')
    .height('100%')
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>

#### getPageOffset20+

getPageOffset(): ScrollOffset

Obtains the current scrolling offset of the web page (excluding the over-scrolling offset).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ScrollOffset](../interfaces-others/document.md#scrolloffset13) | Current scrolling offset of the web page (excluding the over-scrolling offset). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onScroll((event) => {
          try {
            console.info("getPageOffset x:" + this.controller.getPageOffset().x + ",y:" +
            this.controller.getPageOffset().y);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
    }
  }
}

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /\* Horizontally centered \*/
         line-height: 200px;       /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>

#### getLastHitTest18+

getLastHitTest(): HitTestValue

Obtains the element information of the area being clicked last time.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [HitTestValue](../interfaces-others/document.md#hittestvalue) | Element information of the area being clicked. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getLastHitTest')
        .onClick(() => {
          try {
            let hitValue = this.controller.getLastHitTest();
            console.info("hitType: " + hitValue.type);
            console.info("extra: " + hitValue.extra);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getAttachState20+

getAttachState(): ControllerAttachState

Checks whether the current **WebViewController** is bound to a **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ControllerAttachState](../interfaces-others/document.md#controllerattachstate20) | Attach status of **WebViewController** and the **Web** component. |

**Example**

Click the button to obtain the attach status of the current **WebViewController** and output logs.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getAttachState')
        .onClick(() => {
          try {
            if (this.controller.getAttachState() == webview.ControllerAttachState.ATTACHED) {
              console.info('Controller is attached.');
            } else {
              console.info('Controller is unattached.');
            }
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### on('controllerAttachStateChange')20+

on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void

Registers the attach state event of **WebViewController**, which obtains the attach state change notification through a callback.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Attach state event of **WebViewController**, whose value is fixed to **controllerAttachStateChange**. |
| callback | Callback<[ControllerAttachState](../interfaces-others/document.md#controllerattachstate20)\> | Yes | Callback triggered when the attach state of **WebViewController** changes. |

**Example**

For details, see [off](#offcontrollerattachstatechange20).

#### off('controllerAttachStateChange')20+

off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void

Deregisters the attach state event of **WebViewController**. After the deregistration, callback notifications will not be received.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Attach state event of **WebViewController**, whose value is fixed to **controllerAttachStateChange**. |
| callback | Callback<[ControllerAttachState](../interfaces-others/document.md#controllerattachstate20)\> | No | 
Callback triggered when the attach state of **WebViewController** changes. By default, this parameter is left blank. If **Callback** is specified, only the specified callback is deregistered. Otherwise, all callbacks will be deregistered.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Example**

Use **on** to register multiple callbacks, which are triggered when the attach state changes. Use **off** to deregister a callback or all callbacks.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  // Build a callback.
  handleControllerAttachStateChange = (state: webview.ControllerAttachState) => {
    if (state == webview.ControllerAttachState.UNATTACHED) {
      console.info('handleControllerAttachStateChange: Controller is unattached.');
    } else {
      console.info('handleControllerAttachStateChange: Controller is attached.');
    }
  };
  aboutToAppear() {
    try {
      this.controller.on('controllerAttachStateChange', this.handleControllerAttachStateChange);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
    try {
      // Register a callback to receive the notification of the controller attach state change.
      this.controller.on('controllerAttachStateChange', (state: webview.ControllerAttachState) => {
        if (state == webview.ControllerAttachState.UNATTACHED) {
          console.info('Controller is unattached.');
        } else {
          console.info('Controller is attached.');
        }
      })
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }
  aboutToDisappear() {
    // Cancel the specified registered callback.
    // this.controller.off('controllerAttachStateChange', this.handleControllerAttachStateChange);
    // Cancel all registered callbacks.
    this.controller.off('controllerAttachStateChange');
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### waitForAttached20+

waitForAttached(timeout: number):Promise<ControllerAttachState>

Asynchronously waits for the **WebViewController** to be attached to the **Web** component. If the attachment is complete or times out, a callback is triggered to return the current [ControllerAttachState](../interfaces-others/document.md#controllerattachstate20) through a promise.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | 
Asynchronous waiting duration.

Value range: \[0, 65535\]

Unit: ms.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ControllerAttachState](../interfaces-others/document.md#controllerattachstate20)\> | Promise used to return the current [ControllerAttachState](../interfaces-others/document.md#controllerattachstate20). |

**Example**

In the initialization phase, set the **WebViewController** to wait for the attachment to complete. The timeout interval is 1000 ms. If the attachment is complete or times out, the callback is triggered.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  async aboutToAppear() {
    this.controller.waitForAttached(1000).then((state: webview.ControllerAttachState) => {
      if (state == webview.ControllerAttachState.ATTACHED) {
        // The callback is triggered when the attachment is complete or times out.
        console.info('Controller is attached.');
      }
    })
    try {
      const state = await this.controller.waitForAttached(1000);
      if (state == webview.ControllerAttachState.ATTACHED) {
        console.info('Controller is attached.');
      }
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setWebDebuggingAccess20+

static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void

Sets whether to enable wireless web debugging. By default, wireless web debugging is disabled.

-   If no port is specified, this API is equivalent to the [setWebDebuggingAccess](#setwebdebuggingaccess) API. In this case, ArkWeb starts a local domain socket listener.
-   When a port is specified, ArkWeb starts a TCP socket listener. In this case, you can debug the web page wirelessly. For details, see [Wireless Debugging](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-debugging-with-devtools#wireless-debugging).

A port number smaller than 1024 is a well-known or system port and can be enabled only with privileges in the operating system. Therefore, the value of port must be greater than 1024. Otherwise, the API throws an exception.

NOTE: Enabling web debugging allows users to check and modify the internal status of the web page, which poses security risks. Therefore, you are advised not to enable this feature in the officially released version of the application.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| webDebuggingAccess | boolean | Yes | 
Sets whether to enable web debugging.

The value **true** indicates that web page debugging is enabled, and **false** indicates the opposite.

 |
| port | number | Yes | 

Specifies the TCP port number of the DevTools service. If no port is specified, this API is equivalent to the \[setWebDebuggingAccess\] (#setwebdebuggingaccess) API.

Value range: (1024, 65535\]

If the value of port is within the range of \[0, 1024\], the **BusinessError** exception is thrown. The error code is **17100023**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100023 | The port number is not within the allowed range. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true, 8888);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getProgress20+

getProgress(): number

Obtains the loading progress of the current web page.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Loading progress of the current page. The value range is \[0, 100\]. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin(() => {
          let curProgress = this.controller.getProgress();
          console.info("current page loading progress is :" + curProgress);
        })
    }
  }
}

#### getHitTest(deprecated)

getHitTest(): WebHitTestType

Obtains the element type of the area being clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/XuI8IA7SRGOpu5U6XJKCJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA2972D6D3A35F2C96B32CF8272FD15C29C181027997FB9D0E6B3D42B25AB903)

This API is supported since API version 11 and deprecated since API version 18. You are advised to use [getLastHitTest](#getlasthittest18) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [WebHitTestType](../enums/document.md#webhittesttype) | Element type of the area being clicked. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getHitTest')
        .onClick(() => {
          try {
            let hitTestType = this.controller.getHitTest();
            console.info("hitTestType: " + hitTestType);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getHitTestValue(deprecated)

getHitTestValue(): HitTestValue

Obtains the element information of the area being clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/BPs0SaB2SmGY4XZ6yu9VrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=329F4086DA97D9B6F892BD457EA9A57D75A738CB8E6AC4AC03E627FFFCEF574E)

This API is supported since API version 11 and deprecated since API version 18. You are advised to use [getLastHitTest](#getlasthittest18) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [HitTestValue](../interfaces-others/document.md#hittestvalue) | Element information of the area being clicked. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getHitTestValue')
        .onClick(() => {
          try {
            let hitValue = this.controller.getHitTestValue();
            console.info("hitType: " + hitValue.type);
            console.info("extra: " + hitValue.extra);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### avoidVisibleViewportBottom20+

avoidVisibleViewportBottom(avoidHeight: number): void

Sets the bottom avoidance height of the visible viewport on the web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/COIkd8BhRjGO4UODfYUhyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03991D7564EAB143F68E840EE83178F9C77E0380356918B9C6B83673066C31CC)

-   The valid value range of **avoidHeight** is \[0, height of the **Web** component\]. Values outside this range are adjusted to the nearest boundary.
-   When a non-zero value is specified for **avoidHeight**, the position and size of the **Web** component remain unchanged, but the visible viewport shift upwards by the specified height, lifting the web page content by the **avoidHeight**. This API is used to customize the avoidance area at the bottom of a web page. It is not recommended that this API be used when the editable area of the web page is tapped to pull up the keyboard. If this API is used in this scenario, the keyboard avoidance mode is set to **OVERLAYS\_CONTENT**.
-   When the height of this API is set to **0**, the web page content can be restored, and the keyboard avoidance mode is specified by [keyboardAvoidMode()](../../../arkts-components/web/attributes/document.md#keyboardavoidmode12).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| avoidHeight | number | Yes | 
Bottom avoidance height of the visible viewport on the web page.

Unit: vp.

Value range: \[0, height of the **Web** component\]

If the value is less than 0, the value **0** is used. If the value is greater than the height of the **Web** component, the height of the **Web** component is used.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |
| 801 | Capability not supported. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  avoidHeight: number = 100;

  build() {
    Column() {
      Button('avoid')
        .onClick(() => {
          try {
            this.controller.avoidVisibleViewportBottom(this.avoidHeight);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('reset')
        .onClick(() => {
          try {
            this.controller.avoidVisibleViewportBottom(0);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setErrorPageEnabled20+

setErrorPageEnabled(enable: boolean): void

Sets whether to enable the default error page.

When this API is set to true, if an error occurs during page loading, the [onOverrideErrorPage](../../../arkts-components/web/events/document.md#onoverrideerrorpage20) callback is triggered. You can customize the error display page in the callback.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to enable the default error page. The value **true** means to enable the default error page, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
    }
  }
}

#### getErrorPageEnabled20+

getErrorPageEnabled(): boolean

Queries whether the default error page is enabled.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the default error page is enabled.

The value true indicates that the default error page is enabled, and false indicates the opposite.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
    }
  }
}

#### enablePrivateNetworkAccess20+

static enablePrivateNetworkAccess(enable: boolean): void

Sets the private network access check feature.

After this feature is enabled, the **Web** component performs CORS preflight on private network requests (such as requests for accessing local servers or intranet resources). It sends an OPTIONS preflight request to obtain explicit authorization from the target server and then transmits the actual data. Disabling this feature will skip the security check.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to enable the private network access check feature. The value **true** means to enable the private network access check feature, and **false** means the opposite. |

**Example**

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // If the value is set to false, ArkWeb does not check whether the private network request is valid.
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
  }
}

#### isPrivateNetworkAccessEnabled20+

static isPrivateNetworkAccessEnabled(): boolean

Obtains whether the private network access check feature is enabled for the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the private network access check feature is enabled for the **Web** component. The value **true** indicates that the private network access check feature is enabled, and **false** indicates the opposite. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isPrivateNetworkAccessEnabled')
        .onClick(() => {
          try {
            let isEnabled: boolean = webview.WebviewController.isPrivateNetworkAccessEnabled();
            console.info("isPrivateNetworkAccessEnabled:", isEnabled);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // If the value is set to false, ArkWeb does not check whether the private network request is valid.
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
  }
}

#### getBlanklessInfoWithKey20+

getBlanklessInfoWithKey(key: string): BlanklessInfo

Obtains the prediction information about blankless loading (for details, see [BlanklessInfo](../interfaces-others/document.md#blanklessinfo20)) and starts to generate the loading transition frame. The application determines whether to enable blankless loading based on the information. This API must be used together with the [setBlanklessLoadingWithKey](#setblanklessloadingwithkey20) API before the page loading API is triggered or in **onLoadIntercept**, and after the **WebViewController** is bound to the **Web** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Zj9A1dK7T5OrQKCn7my-Bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81608C9B72AFEC23E20D2206BBEE38E5721932CEC80A632E66280D9CE508AC3E)

-   The default size of the persistent cache capacity is 30 MB (about 30 pages). You can set the cache capacity by calling [setBlanklessLoadingCacheCapacity](#setblanklessloadingcachecapacity20). For details, see the description of this API. When the maximum capacity is exceeded, the cache is updated based on the Least Recently Used (LRU) mechanism. The persistent cache data that has been stored for more than seven days is automatically cleared. After the cache is cleared, the optimization effect appears when the page is loaded for the third time.
-   If the snapshot similarity (**similarity** in [BlanklessInfo](../interfaces-others/document.md#blanklessinfo20)) is extremely low, check whether the **key** value is correct.
-   After this API is called, page loading snapshot detection and transition frame generation calculation are enabled, which generates certain resource overhead.
-   Blankless loading consumes certain resources, which depends on the resolution of the **Web** component. When the width and height of the resolution are respectively **w** and **h**, the peak memory usage increases by about **12 × w × h** B in the page-opening phase. After the page is opened, the memory is reclaimed, which does not affect the stable memory usage. When the size of the solid-state application cache is increased, the increased cache of each page is about **w × h/10** B and the cache is located in the application cache.
-   Add the **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO** permissions to **module.json5**. For details, see [Declaring Permissions in the Configuration File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions#declaring-permissions-in-the-configuration-file).

**System capability**: SystemCapability.Web.Webview.Core

**Device behavior differences**: This API can be called on phones. For other device types, error code **801** is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | 
Key value that uniquely identifies the page.

The value cannot be empty and can contain a maximum of 2048 characters.

Invalid values do not take effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [BlanklessInfo](../interfaces-others/document.md#blanklessinfo20) | Prediction information about blankless loading, including the first screen similarity and first screen loading duration. The application determines whether to enable blankless loading based on the prediction information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // Enable frame interpolation only when the similarity exceeds 50% and the loading duration is less than 1000 ms.
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                if (info.similarity >= 0.5 && info.loadingTime < 1000) {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
                } else {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
                }
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
            }
            return false;
        })
    }
  }
}

#### setBlanklessLoadingWithKey20+

setBlanklessLoadingWithKey(key: string, is\_start: boolean): WebBlanklessErrorCode

Sets whether to enable blankless loading. This API must be used together with [getBlanklessInfoWithKey](#getblanklessinfowithkey20).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/IzqK0lqVTRCP9M7aH2_wvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=382CF95D223B71355500127EAC8FB9DC257D742E2D3D6BD09AB358C9812DEB9F)

-   This API must be called after the page loading API is triggered. Other restrictions are the same as those of [getBlanklessInfoWithKey](#getblanklessinfowithkey20).
-   The page must be loaded in the component that calls this API.
-   When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail.
-   Add the **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO** permissions to **module.json5**. For details, see [Declaring Permissions in the Configuration File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions#declaring-permissions-in-the-configuration-file).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | 
Key value that uniquely identifies the page. This value must be the same as the **key** value of the **getBlanklessInfoWithKey** API.

The value cannot be empty and can contain a maximum of 2048 characters.

When an invalid value is set, the error code **WebBlanklessErrorCode** is returned, and the API does not take effect.

 |
| is\_start | boolean | Yes | 

Whether to enable frame interpolation. The value **true** means to enable frame interpolation, and **false** means the opposite.

If **undefined** or **null** is passed in, the value is **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [WebBlanklessErrorCode](../enums/document.md#webblanklesserrorcode20) | Whether the API is successfully called. For details, see [WebBlanklessErrorCode](../enums/document.md#webblanklesserrorcode20). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // Enable frame interpolation only when the similarity exceeds 50% and the loading duration is less than 1000 ms.
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                if (info.similarity >= 0.5 && info.loadingTime < 1000) {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
                } else {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
                }
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
            }
            return false;
        })
    }
  }
}

#### clearBlanklessLoadingCache20+

static clearBlanklessLoadingCache(keys?: Array<string>): void

Clears the blankless loading cache of the page with a specified key value.

In an applet or web application, when the content changes significantly during page loading, an obvious scene change may occur. If you are concerned about this change, you can use this API to clear the page cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/vv5YArLYRZaE7nxTdtGv9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91C5FD015C10385BA5745DA828CDA05EE2B5A69EB9DBCB96041F64B00F76518D)

-   After the page is cleared, the optimization effect appears when the page is loaded for the third time.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | Array<string> | No | 
Key value list on the pages using the blankless optimization solution. The **key** value has been specified in [getBlanklessInfoWithKey](#getblanklessinfowithkey20).

Default value: key list of all pages cached by the blankless optimization solution.

Valid value range: The key length cannot exceed 2048 characters, and the number of keys must be less than or equal to 100. The key value is the same as that input to the **Web** component during page loading.

Invalid value setting behavior: If **undefined** or **null** is passed, error code **401** is thrown. If the key length exceeds 2048, the key does not take effect. If the key length exceeds 100, the first 100 values are used. If the key is empty, the default value is used.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    // If the web page of the application will be greatly changed on June 10, 2025, for example, during product promotion activities, you are advised to clear the frame interpolation to optimize the cache.
    webview.WebviewController.initializeWebEngine();
    let pageUpdateTime: number = Date.UTC(2025, 5, 10, 0, 0, 0, 0);
    let pageUpdateTime1: number = Date.UTC(2025, 5, 11, 0, 0, 0, 0);
    let pageUpdateTimeNow: number = Date.now();
    if (pageUpdateTimeNow > pageUpdateTime && pageUpdateTime < pageUpdateTime1) {
      // Clear the cache of the frame interpolation on the specified page.
      try {
        webview.WebviewController.clearBlanklessLoadingCache(\["https://www.example.com", "https://www.example1.com"\]);
      } catch (error) {
        console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
      }
    }
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}

#### setBlanklessLoadingCacheCapacity20+

static setBlanklessLoadingCacheCapacity(capacity: number): number

Sets the persistent cache capacity of the blankless loading solution and returns the value that takes effect. If the API is not explicitly called, the default cache capacity is 30 MB. When this limit is exceeded, transition frames that are not frequently used are eliminated.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capacity | number | Yes | 
Persistent cache capacity, in MB. The maximum value is 100 MB.

Valid value range: \[0, 100\]. If the value is set to **0**, no cache space is available and the function is disabled globally.

When a value less than 0 is set, the value **0** takes effect. When a value greater than 100 is set, the value **100** takes effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Effective value that ranges from 0 MB to 100 MB.

When a value less than 0 is set, the value **0** takes effect. When a value greater than 100 is set, the value **100** takes effect.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Set the cache capacity to 10 MB.
    try {
      webview.WebviewController.setBlanklessLoadingCacheCapacity(10);
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
    }
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}

#### setWebDestroyMode20+

setWebDestroyMode(mode: WebDestroyMode): void

Sets the destroy mode of the **Web** component. The destroy mode of the **Web** component affects the time when web kernel resources, such as the JavaScript running context and rendering context, are released. The default value is [WebDestroyMode.NORMAL\_MODE](../enums/document.md#webdestroymode20) (normal mode), indicating that the system determines the destroy time. You can set [WebDestroyMode.FAST\_MODE](../enums/document.md#webdestroymode20) (fast mode) to destroy resources immediately, improving performance in specific scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/zs7E2FlnSO64rkhgOPFyAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCA9A8FAFCA71C37A8CFC23A87F37D0E838A41D277D1D42A614E071179733F8E)

[WebDestroyMode.FAST\_MODE](../enums/document.md#webdestroymode20) changes the time when the **Web** component is destroyed. When it is used, pay attention to the incorrect implementation that depends on the destroy time of the **Web** component. For example, when a **WebViewController** is called in fast mode rather than using [WebDestroyMode.NORMAL\_MODE](../enums/document.md#webdestroymode20), the unbinding exception (**17100001**) is more likely to be triggered. In this case, the application needs to capture the exception, or use [getAttachState](#getattachstate20) to obtain the attach state to avoid stability problems.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WebDestroyMode](../enums/document.md#webdestroymode20) | Yes | 
Destroy mode of the **Web** component.

Default value: **WebDestroyMode.NORMAL\_MODE**

 |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Set the fast destroy mode.
    webview.WebviewController.setWebDestroyMode(webview.WebDestroyMode.FAST\_MODE);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}

#### setActiveWebEngineVersion20+

static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void

Sets the ArkWeb kernel version. If the system does not support the specified version, the setting is invalid. This API is a global static API and must be called before **initializeWebEngine** is called. If any **Web** component has been loaded, the setting of this API is invalid.

**Legacy kernel adaptation**

Since HarmonyOS 6.0, some ArkWeb APIs do not take effect when the legacy kernel is used. For details, see [Adaptation Guide for the M114 Kernel on HarmonyOS 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/keNQjA63RT68Gshfdn-8QQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81991C7D1DA60841A614DA67553F9D913F9CD4F8324FEB1BF940C621718101F4)

-   **setActiveWebEngineVersion** cannot be called in an asynchronous thread.
-   **setActiveWebEngineVersion** takes effect globally and needs to be called only once in an application lifecycle.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| engineVersion | [ArkWebEngineVersion](../enums/document.md#arkwebengineversion20) | Yes | ArkWeb kernel version. |

**Example**

This example shows how to set the ArkWeb kernel version in the EntryAbility creation phase.

// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.setActiveWebEngineVersion(webview.ArkWebEngineVersion.M114)
    if (webview.WebviewController.getActiveWebEngineVersion() == webview.ArkWebEngineVersion.M114) {
      console.info("Active Web Engine Version set to M114")
    }
    console.info("EntryAbility onCreate done")
  }
}

#### getActiveWebEngineVersion20+

static getActiveWebEngineVersion(): ArkWebEngineVersion

Obtains the current ArkWeb kernel version.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkWebEngineVersion](../enums/document.md#arkwebengineversion20) | The ArkWeb kernel version defined by [ArkWebEngineVersion](../enums/document.md#arkwebengineversion20). |

**Example**

For details, see [setActiveWebEngineVersion](#setactivewebengineversion20).

#### setAutoPreconnect21+

static setAutoPreconnect(enabled: boolean): void

Sets the automatic preconnection status of the Web kernel. If this API is not set, automatic preconnection is enabled by default.

This API must be called before [initializeWebEngine()](#initializewebengine) is called to initialize the kernel or create a **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable automatic preconnection of the Web kernel. The value **true** means to enable the private network access check feature, and **false** means the opposite. |

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        webview.WebviewController.setAutoPreconnect(false);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
}

#### isAutoPreconnectEnabled21+

static isAutoPreconnectEnabled(): boolean

Queries the automatic preconnection status of the Web kernel.

If the automatic preconnection status of the Web kernel is not set by using [setAutoPreconnect](#setautopreconnect21), automatic preconnection is enabled by default, and **true** is returned.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether auto preconnection is enabled for the Web kernel. The value **true** indicates that the private network access check feature is enabled, and **false** indicates the opposite. |

**Example**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  build() {
    Column() {
      Button('isAutoPreconnectEnabled')
        .onClick(() => {
          try {
            let isEnabled: boolean = webview.WebviewController.isAutoPreconnectEnabled();
            console.info("isAutoPreconnectEnabled:", isEnabled);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
    }
  }
}

#### getSiteIsolationMode21+

static getSiteIsolationMode(): SiteIsolationMode

Queries the currently effective site isolation mode.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [SiteIsolationMode](../enums/document.md#siteisolationmode21) | 
Site isolation mode.

getSiteIsolationMode() queries the currently effective site isolation mode.

 |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getSiteIsolationMode')
        .onClick(() => {
          let mode = webview.WebviewController.getSiteIsolationMode();
          console.info("getSiteIsolationMode: " + mode);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setSiteIsolationMode21+

setSiteIsolationMode(mode: SiteIsolationMode): void

Sets the site isolation mode. Enumerates the site isolation modes. The site isolation mechanism isolates websites from different sources in different render processes to reduce the cross-domain attack surface. For example, on a PC, if site isolation is disabled, each tab page corresponds to a render process. After site isolation is enabled, iframes from different sources in a tab page can run in independent render processes.

For third-party applications that load only trusted web pages, you can disable this functionality to improve performance, reduce memory usage, and reduce interception of cross-domain access. The default value varies according to the device. [SiteIsolationMode.STRICT](../enums/document.md#siteisolationmode21) is used for PCs and tablets, and [SiteIsolationMode.PARTIAL](../enums/document.md#siteisolationmode21) is used for phones. In [Secure Shield mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-secure-shield-mode), strict site isolation is used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/vxY23C8aT4C3og7jgLSnaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1C7FF663334701B4B3F098182B809AD65A5CBD4E74FEEAC26A299482D788BC2)

Strict site isolation cannot be set in single-process mode.

This API can be called only once during initialization. The site isolation mode cannot be repeatedly changed.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SiteIsolationMode](../enums/document.md#siteisolationmode21) | Yes | 
Site isolation mode.

The default value depends on the device type and device mode. For PCs and tablets, strict site isolation is used by default. For phones, partial site isolation is used by default. In Secure Shield mode, strict site isolation is used by default.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. Possible causes: 1. Site Isolation mode is already set by the developer. 2. Site Isolation mode cannot be strict in single-render-process mode. 3. Site Isolation mode cannot be changed while Secure Shield mode is active. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setSiteIsolationMode')
        .onClick(() => {
          try {
            webview.WebviewController.setSiteIsolationMode(webview.SiteIsolationMode.PARTIAL);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setSocketIdleTimeout21+

static setSocketIdleTimeout(timeout: number): void

Sets the timeout interval for used sockets to stay idle in the **Web** component. If the value is different from the timeout interval of existing idle sockets, the existing idle sockets are cleared according to the new value.

If this API is not used to set the timeout interval for idle sockets, the default value **300s** is used for the **Web** component.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | 
Timeout interval for used sockets to stay idle in the **Web** component, in seconds.

Value range: \[30, 300\].

If the value is less than 30, the value **30** takes effect. If the value is greater than 300, the value **300** takes effect.

 |

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        webview.WebviewController.setSocketIdleTimeout(200);
        AppStorage.setOrCreate("abilityWant", want);
    }
}

#### setSoftKeyboardBehaviorMode22+

setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void

Set the behavior mode of the soft keyboard. If this API is not explicitly called, the system automatically hides or shows the soft keyboard when the **Web** component loses or gains focus, or when its status becomes inactive or active.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WebSoftKeyboardBehaviorMode](../enums/document.md#websoftkeyboardbehaviormode22) | Yes | Behavior mode of the web soft keyboard. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100001 | Init error. The WebviewController must be associated with a Web component. |

**Example**

// index.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('Web InActive').onClick(() => {
        this.controller.setSoftKeyboardBehaviorMode(webview.WebSoftKeyboardBehaviorMode.DISABLE\_AUTO\_KEYBOARD\_ON\_ACTIVE);
      })
      Web({ src: 'www.example.com', controller: this.controller })
        .keyboardAvoidMode(WebKeyboardAvoidMode.RETURN\_TO\_UICONTEXT)
    }
  }
}
