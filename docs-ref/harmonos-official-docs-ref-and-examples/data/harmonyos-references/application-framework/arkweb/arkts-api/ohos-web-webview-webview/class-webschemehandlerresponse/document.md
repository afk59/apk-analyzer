# Class (WebSchemeHandlerResponse)

Represents a request response. You can create a response for an intercepted request, fill in custom content, and return the response to the **Web** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/AuuYfzgCTAePkY6naGcnsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E5A8BA0F6E2261D58AA609F5EADD2D4ECF5A710373F20E9616917BD9A40D75E)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### constructor12+

constructor()

Constructs a **Response** object.

**System capability**: SystemCapability.Web.Webview.Core

**Example**

// xxx.ets
import { webview, WebNetErrorList } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('response').onClick(() => {
        let response = new webview.WebSchemeHandlerResponse();
        try {
          response.setUrl("http://www.example.com")
          response.setStatus(200)
          response.setStatusText("OK")
          response.setMimeType("text/html")
          response.setEncoding("utf-8")
          response.setHeaderByName("header1", "value1", false)
          response.setNetErrorCode(WebNetErrorList.NET\_OK)
          console.info("\[schemeHandler\] getUrl:" + response.getUrl())
          console.info("\[schemeHandler\] getStatus:" + response.getStatus())
          console.info("\[schemeHandler\] getStatusText:" + response.getStatusText())
          console.info("\[schemeHandler\] getMimeType:" + response.getMimeType())
          console.info("\[schemeHandler\] getEncoding:" + response.getEncoding())
          console.info("\[schemeHandler\] getHeaderByValue:" + response.getHeaderByName("header1"))
          console.info("\[schemeHandler\] getNetErrorCode:" + response.getNetErrorCode())

        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
      Web({ src: 'https://www.example.com', controller: this.controller })
    }
  }
}

#### setUrl12+

setUrl(url: string): void

Sets the redirection URL or the URL changed due to HSTS for this response. After the URL is set, a redirection to the new URL is triggered.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL to be redirected to. |

**Example**

For details about the sample code, see [constructor](#constructor12).

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

#### setNetErrorCode12+

setNetErrorCode(code: WebNetErrorList): void

Sets the network error code for this response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | [WebNetErrorList](../../ohos-web-neterrorlist-the-list-of-arkweb-network-protocol-stack-errors/document.md#webneterrorlist) | Yes | Network error code. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### setStatus12+

setStatus(code: number): void

Sets the HTTP status code for this response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | HTTP status code. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### setStatusText12+

setStatusText(text: string): void

Sets the status text for this response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Status text. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### setMimeType12+

setMimeType(type: string): void

Sets the MIME type for this response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | MIME type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### setEncoding12+

setEncoding(encoding: string): void

Sets the character set for this response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | Yes | Character set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### setHeaderByName12+

setHeaderByName(name: string, value: string, overwrite: boolean): void

Sets the header information for this response.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the header. |
| value | string | Yes | Value of the header. |
| overwrite | boolean | Yes | Whether to override the existing header. The value **true** means to override the existing header, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getUrl12+

getUrl(): string

Obtains the redirection URL or the URL changed due to HSTS.

NOTE: To obtain a URL for the JavaScriptProxy communication API authentication, use [getLastJavascriptProxyCallingFrameUrl12+](../class-webviewcontroller/document.md#getlastjavascriptproxycallingframeurl12).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Redirection URL or the URL changed due to HSTS. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getNetErrorCode12+

getNetErrorCode(): WebNetErrorList

Obtains the network error code of the response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [WebNetErrorList](../../ohos-web-neterrorlist-the-list-of-arkweb-network-protocol-stack-errors/document.md#webneterrorlist) | Obtains the network error code of the response. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getStatus12+

getStatus(): number

Obtains the HTTP status code of the response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | HTTP status code of the response. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getStatusText12+

getStatusText(): string

Obtains the status text of this response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Status text. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getMimeType12+

getMimeType(): string

Obtains the MIME type of this response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | MIME type. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getEncoding12+

getEncoding(): string

Obtains the character set of this response.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Character set. |

**Example**

For details about the sample code, see [constructor](#constructor12).

#### getHeaderByName12+

getHeaderByName(name: string): string

Obtains the value of a response header field by name.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the header. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the header. |

**Example**

For details about the sample code, see [constructor](#constructor12).
