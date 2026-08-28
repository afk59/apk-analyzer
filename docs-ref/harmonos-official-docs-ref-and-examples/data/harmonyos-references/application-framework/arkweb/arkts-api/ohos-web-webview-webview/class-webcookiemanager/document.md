# Class (WebCookieManager)

Implements a **WebCookieManager** instance to manage behavior of cookies in **Web** components. All **Web** components in an application share a **WebCookieManager** instance. The cookie format complies with the [RFC2965](https://www.rfc-editor.org/rfc/rfc2965) standard. Currently, the cookie obtaining API of WebCookieManager does not support partitioned cookies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Boc4eIW6Q6iZUAKJxNGBOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E06E87261CEF5C02EF33674FBC4C45089362230B477C29D3FC7695BF8C1F0E46)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    
-   Static methods must be used on the user interface (UI) thread.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### fetchCookieSync11+

static fetchCookieSync(url: string, incognito?: boolean): string

Obtains the cookie value of the specified URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/FGOaBIfgSeaLLpAXdtinIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E1732E2A5F970C146F86606725D11CA75848CA3DA450BC8EC00D8CDCB921428)

The system automatically deletes expired cookies. For data with the same key name, the new data overwrites the previous data.

To obtain the cookie value that can be used, pass a complete link to **fetchCookieSync()**.

**fetchCookieSync()** is used to obtain all cookie values. Cookie values are separated by semicolons. However, a specific cookie value cannot be obtained separately.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |
| incognito | boolean | No | 
Whether to obtain the cookie in incognito mode. The value **true** means to obtain the cookie in incognito mode, and **false** means the opposite.

The default value is **false**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Cookie value corresponding to the specified URL. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
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
      Button('fetchCookieSync')
        .onClick(() => {
          try {
            let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
            console.info("fetchCookieSync cookie = " + value);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### fetchCookie11+

static fetchCookie(url: string, callback: AsyncCallback<string>): void

Obtains the cookie value of a specified URL. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |

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
      Button('fetchCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.fetchCookie('https://www.example.com', (error, cookie) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              if (cookie) {
                console.info('fetchCookie cookie = ' + cookie);
              }
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### fetchCookie11+

static fetchCookie(url: string): Promise<string>

Obtains the cookie value of a specified URL. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |

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
      Button('fetchCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.fetchCookie('https://www.example.com')
              .then(cookie => {
                console.info("fetchCookie cookie = " + cookie);
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

#### fetchCookie14+

static fetchCookie(url: string, incognito: boolean): Promise<string>

Obtains the cookie value of a specified URL. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |
| incognito | boolean | Yes | Whether to obtain the cookie in incognito mode. The value **true** means to obtain the cookie in incognito mode, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |

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
      Button('fetchCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.fetchCookie('https://www.example.com', false)
              .then(cookie => {
                console.info("fetchCookie cookie = " + cookie);
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

#### configCookieSync11+

static configCookieSync(url: string, value: string, incognito?: boolean): void

Sets a cookie for the specified URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Of7KNrBpQ1CjosrHWalhCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17BC0E0569FAC5E3B98977AFA48BAB446081B40295A610AC2C3ED7FB4E9802B6)

You can set **url** in **configCookieSync** to a domain name so that the cookie is attached to the requests on the page.

It is recommended that cookie syncing be completed before the **Web** component is loaded.

If **configCookieSync()** is used to set cookies for two or more times, the cookies set each time are separated by semicolons.

Cookies are periodically saved to the disk every 30s. You can also use the [saveCookieAsync](#savecookieasync) API to forcibly save cookies to the disk.

If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie has expired, it will not be stored. To set multiple cookies, call this method multiple times.

The **value** parameter must comply with the format of the Set-Cookie HTTP response header. The value is in the format of "key=value", followed by a list of cookie attributes separated by semicolons, for example, **"key=value;Max-Age=100"**.

If the specified value contains the **Secure** attribute, the URL must use the **https://** protocol.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to set. A complete URL is recommended. |
| value | string | Yes | Cookie value to set. |
| incognito | boolean | No | 
Whether to set the cookies in incognito mode. The value **true** means to set the cookies in incognito mode, and **false** means the opposite.

The default value is **false**.

If **undefined** or **null** is passed, error code **401** will be thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
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
      Button('configCookieSync')
        .onClick(() => {
          try {
            // Only one cookie value can be set in configCookieSync at a time.
            webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### configCookieSync14+

static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void

Sets a cookie value for a specified URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/uuftgpOOQbu1Ddh2cbQ4hQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E543805FDB09E4D5A271B9C435C012C987A2DF8571AF9BADF0CA9187A40D6B4)

You can set **url** in **configCookieSync** to a domain name so that the cookie is attached to the requests on the page.

It is recommended that cookie syncing be completed before the **Web** component is loaded.

If **configCookieSync()** is used to set cookies for two or more times, the cookies set each time are separated by semicolons.

Cookies are periodically saved to the disk every 30s. You can also use the [saveCookieAsync](#savecookieasync) API to forcibly save cookies to the disk.

If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie has expired, it will not be stored. To set multiple cookies, call this method multiple times.

The **value** parameter must comply with the format of the Set-Cookie HTTP response header. The value is in the format of "key=value", followed by a list of cookie attributes separated by semicolons, for example, **"key=value;Max-Age=100"**.

If the specified value contains the **Secure** attribute, the URL must use the **https://** protocol.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to set. A complete URL is recommended. |
| value | string | Yes | Cookie value to set. |
| incognito | boolean | Yes | Whether to set the cookies in incognito mode. The value **true** means to set the cookies in incognito mode, and **false** means the opposite. |
| includeHttpOnly | boolean | Yes | Whether to overwrite cookies containing **HttpOnly**. The value **true** means to overwrite cookies containing **HttpOnly**, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
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
      Button('configCookieSync')
        .onClick(() => {
          try {
            // Only a single cookie value can be set.
            webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', false, false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### configCookie11+

static configCookie(url: string, value: string, callback: AsyncCallback<void>): void

Sets the value of a single cookie for a specified URL. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |
| value | string | Yes | Cookie value to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |

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
      Button('configCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookie('https://www.example.com', "a=b", (error) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### configCookie11+

static configCookie(url: string, value: string): Promise<void>

Sets the value of a single cookie for a specified URL. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |
| value | string | Yes | Cookie value to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |

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
      Button('configCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookie('https://www.example.com', 'a=b')
              .then(() => {
                console.info('configCookie success!');
              })
              .catch((error: BusinessError) => {
                console.info('error: ' + JSON.stringify(error));
              })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### configCookie14+

static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>

Sets the value of a single cookie for a specified URL. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |
| value | string | Yes | Cookie value to set. |
| incognito | boolean | Yes | Whether to set the cookies in incognito mode. The value **true** means to set the cookies in incognito mode, and **false** means the opposite. |
| includeHttpOnly | boolean | Yes | Whether to overwrite cookies containing **HttpOnly**. The value **true** means to overwrite cookies containing **HttpOnly**, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |

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
      Button('configCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookie('https://www.example.com', 'a=b', false, false)
              .then(() => {
                console.info('configCookie success!');
              })
              .catch((error: BusinessError) => {
                console.info('error: ' + JSON.stringify(error));
              })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### saveCookieSync15+

static saveCookieSync(): void

Synchronously saves all cookies (that can be obtained through **fetchCookie** and need to be persisted) to the disk.

**System capability**: SystemCapability.Web.Webview.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/4C5RpvwITimB7tgETB3nlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC71D1D2ED0C55AA469659CC77E2863EE83760BA60C0059D4C61B1DCA9659D2C)

**saveCookieSync** is used to forcibly write cookies that need to be persisted to disks. Session cookies are not persisted on PCs, 2-in-1 devices, or tablets, even if **saveCookieSync** is invoked.

**saveCookieSync** blocks the caller until the operation is complete. During this period, I/O operations may be performed.

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
      Button('saveCookieSync')
        .onClick(() => {
          try {
            webview.WebCookieManager.saveCookieSync();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### saveCookieAsync

static saveCookieAsync(callback: AsyncCallback<void>): void

Asynchronously saves all cookies (that can be obtained through **fetchCookie** and need to be persisted) to the disk.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/9p011TfJTSKj7EOZeHtdYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4E46C0CEFDB30A16394F7EC09FCE6C63E887189CD767FFE17E3B009CCA8202B)

Cookie information is stored in the application sandbox path **/proc/{pid}/root/data/storage/el2/base/cache/web/Cookies**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return whether the cookies are successfully saved. |

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

  build() {
    Column() {
      Button('saveCookieAsync')
        .onClick(() => {
          try {
            webview.WebCookieManager.saveCookieAsync((error) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### saveCookieAsync

static saveCookieAsync(): Promise<void>

Saves all cookies (that can be obtained through **fetchCookie** and need to be persisted) to the disk using a promise.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the operation result. |

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

  build() {
    Column() {
      Button('saveCookieAsync')
        .onClick(() => {
          try {
            webview.WebCookieManager.saveCookieAsync()
              .then(() => {
                console.info("saveCookieAsyncCallback success!");
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### putAcceptCookieEnabled

static putAcceptCookieEnabled(accept: boolean): void

Sets whether the **WebCookieManager** instance has the permission to send and receive cookies.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| accept | boolean | Yes | Whether the **WebCookieManager** instance has the permission to send and receive cookies. The default value is **true**, indicating that the **WebCookieManager** instance has the permission to send and receive cookies. |

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

  build() {
    Column() {
      Button('putAcceptCookieEnabled')
        .onClick(() => {
          try {
            webview.WebCookieManager.putAcceptCookieEnabled(false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isCookieAllowed

static isCookieAllowed(): boolean

Checks whether the **WebCookieManager** instance has the permission to send and receive cookies.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the **WebCookieManager** instance has the permission to send and receive cookies.

The value **true** indicates that the **WebCookieManager** instance has the permission to send and receive cookies, and **false** indicates the opposite.

Default value: **true**.

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
      Button('isCookieAllowed')
        .onClick(() => {
          let result = webview.WebCookieManager.isCookieAllowed();
          console.info("result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### putAcceptThirdPartyCookieEnabled

static putAcceptThirdPartyCookieEnabled(accept: boolean): void

Sets whether the **WebCookieManager** instance has the permission to send and receive third-party cookies.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| accept | boolean | Yes | 
Whether to allow the setting and obtaining of third-party cookies.

The value **true** means to allow the setting and obtaining of third-party cookies, and **false** means the opposite.

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

  build() {
    Column() {
      Button('putAcceptThirdPartyCookieEnabled')
        .onClick(() => {
          try {
            webview.WebCookieManager.putAcceptThirdPartyCookieEnabled(false);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### isThirdPartyCookieAllowed

static isThirdPartyCookieAllowed(): boolean

Checks whether the **WebCookieManager** instance has the permission to send and receive third-party cookies.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the **WebCookieManager** instance has the permission to send and receive third-party cookies.

The value **true** indicates that the **WebCookieManager** instance has the permission to send and receive third-party cookies, and **false** indicates the opposite.

The default value is **false**.

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
      Button('isThirdPartyCookieAllowed')
        .onClick(() => {
          let result = webview.WebCookieManager.isThirdPartyCookieAllowed();
          console.info("result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### existCookie

static existCookie(incognito?: boolean): boolean

Checks whether cookies exist.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| incognito11+ | boolean | No | 
Whether to check for cookies in incognito mode. The value **true** means to check for cookies in incognito mode, and **false** means the opposite.

The default value is **false**.

If **undefined** or **null** is passed, **undefined** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether cookies exist. The value **true** means that cookies exist, and **false** means the opposite. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('existCookie')
        .onClick(() => {
          let result = webview.WebCookieManager.existCookie();
          console.info("result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearAllCookiesSync11+

static clearAllCookiesSync(incognito?: boolean): void

Deletes all cookies.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| incognito | boolean | No | 
Whether to clear all cookies in incognito mode. The value **true** means to clear all cookies in incognito mode, and **false** means the opposite.

The default value is **false**.

If **undefined** or **null** is passed, cookies are not cleared.

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
      Button('clearAllCookiesSync')
        .onClick(() => {
          webview.WebCookieManager.clearAllCookiesSync();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearAllCookies11+

static clearAllCookies(callback: AsyncCallback<void>): void

Clears all cookies. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

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
      Button('clearAllCookies')
        .onClick(() => {
          try {
            webview.WebCookieManager.clearAllCookies((error) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearAllCookies11+

static clearAllCookies(): Promise<void>

Clears all cookies. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
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
      Button('clearAllCookies')
        .onClick(() => {
          webview.WebCookieManager.clearAllCookies()
            .then(() => {
              console.info("clearAllCookies success!");
            })
            .catch((error: BusinessError) => {
              console.error("error: " + error);
            });
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearSessionCookieSync11+

static clearSessionCookieSync(): void

Deletes all session cookies.

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
      Button('clearSessionCookieSync')
        .onClick(() => {
          webview.WebCookieManager.clearSessionCookieSync();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearSessionCookie11+

static clearSessionCookie(callback: AsyncCallback<void>): void

Clears all session cookies. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

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
      Button('clearSessionCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.clearSessionCookie((error) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### clearSessionCookie11+

static clearSessionCookie(): Promise<void>

Clears all session cookies. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
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
      Button('clearSessionCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.clearSessionCookie()
              .then(() => {
                console.info("clearSessionCookie success!");
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setLazyInitializeWebEngine22+

static setLazyInitializeWebEngine(lazy: boolean): void

Sets whether to delay the initialization of the ArkWeb kernel. If this method is not called, the ArkWeb kernel is not delayed by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/2FflQUVgS0agT6dA_AE4Lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CB79B7373E3CE6FF56FC6F2CC764B00EC78DE858283E4893CB7DD8A6694C5B4)

This API is a global static method and must be called before the **Web** component is used and the ArkWeb kernel is initialized. Otherwise, the setting is invalid.

This API applies only to APIs that initialize the CookieManager after being called, for example, other APIs of the **WebCookieManager** class. When this API is called and the parameter is set to **true**, the ArkWeb kernel is not initialized during the initialization of CookieManager. You need to initialize the ArkWeb kernel later.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lazy | boolean | Yes | Whether to delay the initialization of the ArkWeb kernel. The value **true** means to delay the initialization, and **false** means the opposite. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';

webview.WebCookieManager.setLazyInitializeWebEngine(true);

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
    webview.WebCookieManager.fetchCookieSync('https://www.example.com');
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getCookie(deprecated)

static getCookie(url: string): string

Obtains the cookie value of the specified URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/MghD0DxKTqmdTP56FrDR8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34A7A1936EE9C33987C8F49C5E675F00FE2AB5F05FB4B96BE68132A4FBD81794)

This API is supported since API version 9 and deprecated since API version 11. You are advised to use [fetchCookieSync](#fetchcookiesync11) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to obtain. A complete URL is recommended. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Cookie value corresponding to the specified URL. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
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
      Button('getCookie')
        .onClick(() => {
          try {
            let value = webview.WebCookieManager.getCookie('https://www.example.com');
            console.info("value: " + value);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### setCookie(deprecated)

static setCookie(url: string, value: string): void

Sets a cookie for the specified URL.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/4hQ6irEpRLS6SuUz_wnKSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D9988E0B31B1BAF4CBA16C47E19C7F08B9CA4140FDED911C93199A3739B1569)

This API is supported since API version 9 and deprecated since API version 11. You are advised to use [configCookieSync11+](#configcookiesync11) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL of the cookie to set. A complete URL is recommended. |
| value | string | Yes | Cookie value to set. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
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
      Button('setCookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.setCookie('https://www.example.com', 'a=b');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### deleteEntireCookie(deprecated)

static deleteEntireCookie(): void

Deletes all cookies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/p7clCvVETr-H4Pr1rcO3-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D66D3BA588207613BF83B8776A3C64DA70345B849CA600D0C67DE8309A105088)

This API is supported since API version 9 and deprecated since API version 11. You are advised to use [clearAllCookiesSync](#clearallcookiessync11) instead.

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
      Button('deleteEntireCookie')
        .onClick(() => {
          webview.WebCookieManager.deleteEntireCookie();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### deleteSessionCookie(deprecated)

static deleteSessionCookie(): void

Deletes all session cookies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/K-pRYfdkS_WgHlkAjl9lTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A586154CBF3549FF2A31AD0A0854A7F9679ECD2B2030B90362FF9F52FA6160E5)

This API is supported since API version 9 and deprecated since API version 11. You are advised to use [clearSessionCookieSync](#clearsessioncookiesync11) instead.

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
      Button('deleteSessionCookie')
        .onClick(() => {
          webview.WebCookieManager.deleteSessionCookie();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
