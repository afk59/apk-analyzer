# Class (WebDownloadManager)

Implements a **WebDownloadManager** class. You can use the APIs of this class to resume failed download tasks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/99MaOfM6Rf6JH8Ye_nz0Uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=454C4B5D9F291EED2AB0CAE2DCB637FD148687A73138B96A137BE1E54ED98D67)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 11.
    
-   The sample effect is subject to the actual device.
    

#### Modules to Import

import { webview } from '@kit.ArkWeb';

#### setDownloadDelegate11+

static setDownloadDelegate(delegate: WebDownloadDelegate): void

Sets the delegate used to receive download progress triggered by **WebDownloadManager**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/oQpFoQbdS5G-CiC2pVZaQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C5605BC437151DA32DC503673730247B53113EBC11D5C44E35D0BA1C5FBEC75)

Before calling this API, you must call the **initializeWebEngine** method to initialize the web kernel. Otherwise, calling this API is invalid.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| delegate | [WebDownloadDelegate](../class-webdownloaddelegate/document.md) | Yes | Delegate used to receive the download progress. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
  download: webview.WebDownloadItem = new webview.WebDownloadItem();
  failedData: Uint8Array = new Uint8Array();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
              console.info("will start a download.");
              // Pass in a download path and start the download.
              webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
            })
            this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
              console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
              this.download = webDownloadItem;
            })
            this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
              console.error("download failed guid: " + webDownloadItem.getGuid());
              // Serialize the failed download to a byte array.
              this.failedData = webDownloadItem.serialize();
            })
            this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
              console.info("download finish guid: " + webDownloadItem.getGuid());
            })
            this.controller.setDownloadDelegate(this.delegate);
            webview.WebDownloadManager.setDownloadDelegate(this.delegate);
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
      Button('resumeDownload')
        .onClick(() => {
          try {
            webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('cancel')
        .onClick(() => {
          try {
            this.download.cancel();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('pause')
        .onClick(() => {
          try {
            this.download.pause();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('resume')
        .onClick(() => {
          try {
            this.download.resume();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### resumeDownload11+

static resumeDownload(webDownloadItem: WebDownloadItem): void

Resumes a failed download task.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/csudpjzZTC6DkD3wIBuvbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24B37E9EE8D54C185442F785C43DF8F1C5B92B5C46D7FCF5D4A846C756B6DB7F)

Before calling this API, you must call the **initializeWebEngine** method to initialize the web kernel. Otherwise, calling this API is invalid.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| webDownloadItem | [WebDownloadItem](../class-webdownloaditem/document.md) | Yes | Download task to resume. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 17100018 | No WebDownloadDelegate has been set yet. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
  download: webview.WebDownloadItem = new webview.WebDownloadItem();
  failedData: Uint8Array = new Uint8Array();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
              console.info("will start a download.");
              // Pass in a download path and start the download.
              webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
            })
            this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
              console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
              this.download = webDownloadItem;
            })
            this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
              console.error("download failed guid: " + webDownloadItem.getGuid());
              // Serialize the failed download to a byte array.
              this.failedData = webDownloadItem.serialize();
            })
            this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
              console.info("download finish guid: " + webDownloadItem.getGuid());
            })
            this.controller.setDownloadDelegate(this.delegate);
            webview.WebDownloadManager.setDownloadDelegate(this.delegate);
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
      Button('resumeDownload')
        .onClick(() => {
          try {
            webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('cancel')
        .onClick(() => {
          try {
            this.download.cancel();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('pause')
        .onClick(() => {
          try {
            this.download.pause();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('resume')
        .onClick(() => {
          try {
            this.download.resume();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
