# Class (GeolocationPermissions)

Implements a **GeolocationPermissions** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/lSCmn9lvRu-wljFZknJvXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9542B907B30926CF30CD9A28F3FE4A1E703545F63910FA69F183698895B68DF0)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    
-   You must load the **Web** component before calling the APIs in **GeolocationPermissions**.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### Required Permissions

**ohos.permission.LOCATION**, **ohos.permission.APPROXIMATELY\_LOCATION**, and **ohos.permission.LOCATION\_IN\_BACKGROUND**, which are required for accessing the location information. For details about the permissions, see [@ohos.geolocation (Geolocation)](../../../../../application-services/location-kit/arkts-apis/apis-no-longer-maintained/ohos-geolocation-geolocation/document.md).

#### allowGeolocation

static allowGeolocation(origin: string, incognito?: boolean): void

Allows the specified origin to use the geolocation information.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| incognito11+ | boolean | No | 
Whether to allow the specified origin to use the geolocation information in incognito mode. The value **true** means to allow the specified origin to use the geolocation information in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed in, the value is **false**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('allowGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.allowGeolocation(this.origin);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### deleteGeolocation

static deleteGeolocation(origin: string, incognito?: boolean): void

Clears the geolocation permission status of a specified origin.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| incognito11+ | boolean | No | 
Whether to clear the geolocation permission status of a specified origin in incognito mode. The value **true** means to clear the geolocation permission status of a specified origin in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed in, the value is **false**.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('deleteGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.deleteGeolocation(this.origin);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getAccessibleGeolocation

static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void

Obtains the geolocation permission status of the specified origin. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| callback | AsyncCallback<boolean> | Yes | 
Callback used to return the geolocation permission status of the specified origin.

If the operation is successful, the value **true** means that the geolocation permission is granted, and **false** means the opposite.

If the operation fails, the geolocation permission status of the specified origin is not found.

 |
| incognito11+ | boolean | No | 

Whether to obtain the geolocation permission status of the specified origin in incognito mode. The value **true** means to obtain the geolocation permission status of the specified origin in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('getAccessibleGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
              if (error) {
                console.error(\`getAccessibleGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              console.info('getAccessibleGeolocationAsync result: ' + result);
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getAccessibleGeolocation

static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>

Obtains the geolocation permission status of the specified origin. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| incognito11+ | boolean | No | 
Whether to obtain the geolocation permission status of the specified origin in incognito mode. The value **true** means to obtain the geolocation permission status of the specified origin in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the geolocation permission status of the specified origin.

If the operation is successful, the value **true** means that the geolocation permission is granted, and **false** means the opposite.

If the operation fails, the geolocation permission status of the specified origin is not found.

 |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('getAccessibleGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getAccessibleGeolocation(this.origin)
              .then(result => {
                console.info('getAccessibleGeolocationPromise result: ' + result);
              }).catch((error: BusinessError) => {
              console.error(\`getAccessibleGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}\`);
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getStoredGeolocation

static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void

Obtains the geolocation permission status of all origins. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the geolocation permission status of all origins. |
| incognito11+ | boolean | No | 
Whether to obtain the geolocation permission status of all origins in incognito mode. The value **true** means to obtain the geolocation permission status of all origins in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed, error code **401** is thrown.

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
      Button('getStoredGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getStoredGeolocation((error, origins) => {
              if (error) {
                console.error(\`getStoredGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              let origins\_str: string = origins.join();
              console.info('getStoredGeolocationAsync origins: ' + origins\_str);
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### getStoredGeolocation

static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>

Obtains the geolocation permission status of all origins. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| incognito11+ | boolean | No | 
Whether to obtain the geolocation permission status of all origins in incognito mode. The value **true** means to obtain the geolocation permission status of all origins in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed, error code **401** is thrown.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the geolocation permission status of all origins. |

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
      Button('getStoredGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getStoredGeolocation()
              .then(origins => {
                let origins\_str: string = origins.join();
                console.info('getStoredGeolocationPromise origins: ' + origins\_str);
              }).catch((error: BusinessError) => {
              console.error(\`getStoredGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}\`);
            });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### deleteAllGeolocation

static deleteAllGeolocation(incognito?: boolean): void

Clears the geolocation permission status of all sources.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| incognito11+ | boolean | No | 
Whether to clear the geolocation permission status of all sources in incognito mode. The value **true** means to clear the geolocation permission status of all sources in incognito mode, and **false** means the opposite.

Default value: **false**.

If **null** or **undefined** is passed in, the value is **false**.

 |

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
      Button('deleteAllGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.deleteAllGeolocation();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
