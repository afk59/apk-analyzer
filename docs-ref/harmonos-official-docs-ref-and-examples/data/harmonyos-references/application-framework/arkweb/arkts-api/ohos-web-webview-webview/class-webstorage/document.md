# Class (WebStorage)

Implements a **WebStorage** object to manage the Web SQL database and HTML5 Web Storage APIs. All **Web** components in an application share a **WebStorage** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/x-IdpstoQx-0BuYuUk76BQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DA1F85F0F1BAAA714416D58FA807EE01AE0BB6594D0A5C886AAB74992C323EC)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    
-   You must load the **Web** component before calling the APIs in **WebStorage**.
    
-   After the ArkWeb kernel is upgraded to M132, the Web SQL database management becomes invalid because the kernel discards Web SQL. For details about the ArkWeb kernel version, see [Constraints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-component-overview#constraints).
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### deleteOrigin

static deleteOrigin(origin: string): void

Deletes all data in the specified origin.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin, which is obtained through [getOrigins](#getorigins). |

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
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('deleteOrigin')
        .onClick(() => {
          try {
            webview.WebStorage.deleteOrigin(this.origin);
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
 <head>
   <meta charset="UTF-8">
   <title>test</title>
   <script type="text/javascript">

       // Open or create a database.
       var request = indexedDB.open('myDatabase', 1);

       // Triggered when the database version changes or the database is created for the first time.
       request.onupgradeneeded = function(event) {
           var db = event.target.result;

           // Create an object store (table) and set the primary key to id.
           var objectStore = db.createObjectStore('customers', { keyPath: 'id' });

           // Create an index for name.
           objectStore.createIndex('name', 'name', { unique: false });
       };

       // Called when the database is successfully opened.
       request.onsuccess = function(event) {
           var db = event.target.result;

           const customerData = \[
               {id: 1, name: 'John Doe', email: 'john@example.com'},
               {id: 2, name: 'John Doe', email: 'john@example.com'},
           \]

           // Insert data.
           var transaction = db.transaction('customers', 'readwrite');
           var objectStore = transaction.objectStore('customers');

           customerData.forEach((customer) => {
               objectStore.add(customer);
           });

           transaction.oncomplete = function () {
               console.info('Transaction completed: data added');
           }
           
           transaction.onerror = function (event) {
               console.error("Transaction failed", event);
           }
           
           // Query data.
           var queryTransaction = db.transaction(\['customers'\]);
           var queryObjectStore = queryTransaction.objectStore('customers');
           var query = queryObjectStore.get(2);
           
           query.onsuccess = function (event) {
               console.info('query succ');
               console.info('Customer:', event.target.result);
               console.info('Customer id:', event.target.result.id);
               console.info('Customer name:', event.target.result.name);
               console.info('Customer email:', event.target.result.email);
           };
           
           queryObjectStore.openCursor().onsuccess = (event) => {
               const cursor = event.target.result;
               if (cursor) {
                   var msg = "<p>Query record: " + cursor.key + "</p>";
                   document.querySelector("#status").innerHTML += msg;
                   var msg = "<p><b>" + cursor.value.name + "</b></p>";
                   document.querySelector("#status").innerHTML += msg;
                   console.info(\`SSN ${cursor.key} corresponds to ${cursor.value.name}\`);
                   cursor.continue();
               } else {
                   console.info("No more records")
               }
           }
       };

       // Error handling.
       request.onerror = function(event) {
           console.error('Database error:', event.target.error);
       };

     </script>
 </head>
 <body>
 <div id="status" name="status">Status</div>
 </body>
 </html>

#### getOrigins

static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void

Obtains information about origins that are currently using the Web SQL Database and HTML5-supported Web Storage APIs. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[WebStorageOrigin](../interfaces-others/document.md#webstorageorigin)\>> | Yes | Callback used to return the information about the origins. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100012 | Invalid web storage origin. |
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
      Button('getOrigins')
        .onClick(() => {
          try {
            webview.WebStorage.getOrigins((error, origins) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              for (let i = 0; i < origins.length; i++) {
                console.info('origin: ' + origins\[i\].origin);
                console.info('usage: ' + origins\[i\].usage);
                console.info('quota: ' + origins\[i\].quota);
              }
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.

#### getOrigins

static getOrigins(): Promise<Array<WebStorageOrigin>>

Obtains information about origins that are currently using the Web SQL Database and HTML5-supported Web Storage APIs. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[WebStorageOrigin](../interfaces-others/document.md#webstorageorigin)\>> | Target Promise used to return the information about the origins. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100012 | Invalid web storage origin. |
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
      Button('getOrigins')
        .onClick(() => {
          try {
            webview.WebStorage.getOrigins()
              .then(origins => {
                for (let i = 0; i < origins.length; i++) {
                  console.info('origin: ' + origins\[i\].origin);
                  console.info('usage: ' + origins\[i\].usage);
                  console.info('quota: ' + origins\[i\].quota);
                }
              })
              .catch((e: BusinessError) => {
                console.error('error: ' + JSON.stringify(e));
              })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.

#### getOriginQuota

static getOriginQuota(origin: string, callback: AsyncCallback<number>): void

Obtains the storage quota of an origin in Web SQL Database and HTML5-supported Web Storage APIs, in bytes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| callback | AsyncCallback<number> | Yes | 
Storage quota of the origin.

**number** is a long integer, and the range is \[-2147483648, 2147483647\].

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
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginQuota')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginQuota(this.origin, (error, quota) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              console.info('quota: ' + quota);
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.

#### getOriginQuota

static getOriginQuota(origin: string): Promise<number>

Obtains the storage quota of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the storage quota of the origin. |

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
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginQuota')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginQuota(this.origin)
              .then(quota => {
                console.info('quota: ' + quota);
              })
              .catch((e: BusinessError) => {
                console.error('error: ' + JSON.stringify(e));
              })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.

#### getOriginUsage

static getOriginUsage(origin: string, callback: AsyncCallback<number>): void

Obtains the storage usage of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |
| callback | AsyncCallback<number> | Yes | Storage usage of the origin. |

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
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginUsage')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginUsage(this.origin, (error, usage) => {
              if (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
                return;
              }
              console.info('usage: ' + usage);
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.

#### getOriginUsage

static getOriginUsage(origin: string): Promise<number>

Obtains the storage usage of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes. This API uses a promise to return the result.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| origin | string | Yes | Index of the origin. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the storage usage of the origin. |

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
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginUsage')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginUsage(this.origin)
              .then(usage => {
                console.info('usage: ' + usage);
              }).catch((e: BusinessError) => {
              console.error('error: ' + JSON.stringify(e));
            })
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.

#### deleteAllData

static deleteAllData(incognito?: boolean): void

Deletes all storage data used by JavaScript storage APIs, including the Web SQL Database and HTML5-supported Web storage APIs.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| incognito11+ | boolean | No | 
Whether to delete all data in the Web SQL Database in incognito mode. The value **true** means to delete all data in the Web SQL Database in incognito mode, and **false** means the opposite.

Default value: **false**.

If **undefined** or **null** is passed, the value is **false**.

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
      Button('deleteAllData')
        .onClick(() => {
          try {
            webview.WebStorage.deleteAllData();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}

For details about the HTML file loaded, see the HTML file loaded using the [deleteOrigin](#deleteorigin) API.
