# Interface (BackForwardList)

Defines the backforward list of the current WebView.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/d1nZyVdKR7uEPWweHflz4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F5A46B7077F480EBE8BA930BF814B37D9448713C12E264683A2BE92D21E0E87)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this interface are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### Module to Import

import { webview } from '@kit.ArkWeb';

#### Attributes

**System capability**: SystemCapability.Web.Webview.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentIndex | number | No | No | Index of the current page in the backforward list. |
| size | number | No | No | Number of indexes in the backforward list. A maximum of 50 indexes can be stored. If this limit is exceeded, the start records will be overwritten. |

#### getItemAtIndex

getItemAtIndex(index: number): HistoryItem

Obtains information about a history item with a specified index in the backforward list.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the history item in the backforward list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HistoryItem](../interfaces-others/document.md#historyitem) | History item. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**Example**

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State icon: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Button('getBackForwardEntries')
        .onClick(() => {
          try {
            let list = this.controller.getBackForwardEntries();
            let historyItem = list.getItemAtIndex(list.currentIndex);
            console.info("HistoryItem: " + JSON.stringify(historyItem));
            this.icon = historyItem.icon;
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
