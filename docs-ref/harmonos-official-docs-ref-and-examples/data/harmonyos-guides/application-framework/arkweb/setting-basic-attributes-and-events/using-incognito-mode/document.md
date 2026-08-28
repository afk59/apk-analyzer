# Using Incognito Mode

When creating a **Web** component, you can enable incognito mode for it by setting the optional parameter [incognitoMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-i#weboptions) to **true**. When incognito mode is enabled, data such as cookies and cache data during web page browsing is not stored in local persistent files. This means that such data is lost when the **Web** component is destroyed.

-   Create a [Web](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web) component in incognito mode.
    
    import { webview } from '@kit.ArkWeb';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [isIncognitoMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#isincognitomode11) to determine whether incognito mode is enabled for the current **Web** component.
    
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
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: 'www.example.com', controller: this.controller });
        }
      }
    }
    

In incognito mode, you can use the following APIs for geolocation information, cookies, and cache data:

-   Use [allowGeolocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions#allowgeolocation) to allow the specified origin to use the geolocation information.
    
    import { webview } from '@kit.ArkWeb';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
      origin: string = 'file:///';
    
      build() {
        Column() {
          Button('allowGeolocation')
            .onClick(() => {
              try {
                // The second parameter of allowGeolocation specifies whether to allow the specified origin to use the geolocation information in incognito mode (true) or in non-incognito mode (false).
                webview.GeolocationPermissions.allowGeolocation(this.origin, true);
              } catch (error) {
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [deleteGeolocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions#deletegeolocation) to clear the geolocation permission status of a specified origin.
    
    import { webview } from '@kit.ArkWeb';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
      origin: string = 'file:///';
    
      build() {
        Column() {
          Button('deleteGeolocation')
            .onClick(() => {
              try {
                // The second parameter of deleteGeolocation specifies whether to clear the geolocation permission status of a specified origin in incognito mode (true) or in non-incognito mode (false).
                webview.GeolocationPermissions.deleteGeolocation(this.origin, true);
              } catch (error) {
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [getAccessibleGeolocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions#getaccessiblegeolocation) to asynchronously obtain the geolocation permission status of the specified origin.
    
    import { webview } from '@kit.ArkWeb';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
      origin: string = 'file:///';
    
      build() {
        Column() {
          Button('getAccessibleGeolocation')
            .onClick(() => {
              try {
                // The third parameter of getAccessibleGeolocation specifies whether to obtain the geolocation permission status of the specified origin in incognito mode (true) or non-incognito mode (false).
                // This API uses an asynchronous callback to return the result.
                webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
                  if (error) {
                    console.error(\`getAccessibleGeolocationAsync error: + Code: ${error.code}, message: ${error.message}\`);
                    return;
                  }
                  console.info('getAccessibleGeolocationAsync result: ' + result);
                }, true);
              } catch (error) {
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [deleteAllData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webstorage#deletealldata) to delete all data in the Web SQL Database.
    
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
                // The parameter of deleteAllData specifies whether to delete all data in the Web SQL Database in incognito mode (true) or in non-incognito mode (false).
                webview.WebStorage.deleteAllData(true);
              } catch (error) {
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: $rawfile('index.html'), controller: this.controller, incognitoMode: true })
            .databaseAccess(true)
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
    
       var db = openDatabase('mydb','1.0','Test DB',2 \* 1024 \* 1024);
       var msg;
    
       db.transaction(function(tx){
         tx.executeSql('INSERT INTO LOGS (id,log) VALUES(1,"test1")');
         tx.executeSql('INSERT INTO LOGS (id,log) VALUES(2,"test2")');
         msg = '<p>Data table created, with two data records inserted.</p>';
    
         document.querySelector('#status').innerHTML = msg;
       });
    
       db.transaction(function(tx){
         tx.executeSql('SELECT \* FROM LOGS', \[\], function (tx, results) {
           var len = results.rows.length,i;
           msg = "<p>Number of records: " + len + "</p>";
    
           document.querySelector('#status').innerHTML += msg;
    
               for(i = 0; i < len; i++){
                 msg = "<p><b>" + results.rows.item(i).log + "</b></p>";
    
           document.querySelector('#status').innerHTML += msg;
           }
         },null);
       });
    
       </script>
    </head>
    <body>
    <div id="status" name="status">Status</div>
    </body>
    </html>
    
-   Use [fetchCookieSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#fetchcookiesync11) to obtain the cookie corresponding to the specified URL.
    
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
                // The second parameter of fetchCookieSync specifies whether to obtain the cookie in incognito mode (true) or in non-incognito mode (false).
                let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com', true);
                console.info('fetchCookieSync cookie = ' + value);
              } catch (error) {
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [configCookieSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookiesync11) to set a cookie for the specified URL.
    
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
                // The third parameter of configCookieSync specifies whether to obtain the cookie for the specified URL in incognito mode (true) or non-incognito mode (false).
                webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', true);
              } catch (error) {
                console.error(
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [existCookie](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#existcookie) to check whether cookies exist.
    
    import { webview } from '@kit.ArkWeb';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Button('existCookie')
            .onClick(() => {
              // The parameter of existCookie specifies whether to check for cookies in incognito mode (true) or in non-incognito mode (false).
              let result = webview.WebCookieManager.existCookie(true);
              console.info('result: ' + result);
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
    
-   Use [clearAllCookiesSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#clearallcookiessync11) to clear all cookies.
    
    import { webview } from '@kit.ArkWeb';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Button('clearAllCookiesSync')
            .onClick(() => {
              // The parameter of clearAllCookiesSync specifies whether to delete all cookies in incognito mode (true) or in non-incognito mode (false).
              webview.WebCookieManager.clearAllCookiesSync(true);
            })
          Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
        }
      }
    }
