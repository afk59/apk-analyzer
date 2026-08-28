# Using Smart Text Data Detector

Since API version 20, ArkWeb provides the text segmentation and recognition feature on HTML5 pages, enabling segmented-text highlighting, long-press preview, and text-selection menus extension. To use this feature, set [enableDataDetector](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#enabledatadetector20) to **true**. The default value is **false**.

This feature is mainly used to automatically identify entities such as phone numbers and URLs on HTML5 pages and provide convenient interaction operations. For example, a user can click a phone number to make a call or click an URL to view the address on the map, improving user experience.

The recognizable entity types include phone numbers, URLs, email addresses, addresses, and time. For details, see [TextDataDetectorType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#textdatadetectortype11).

#### Segmented Text Highlighting

After the HTML5 page in the **Web** component is loaded, the special entities on the page are automatically identified and highlighted. Entities that appear after the page changes are not highlighted.

The filtering rules for highlighting special entities are as follows:

-   Text entities in the text box and editable area are not processed.
-   Text entities in the <a></a> tag are not processed.
-   Text entities in cross-domain iframes and nested iframes are not processed.
-   Text entities that cross nodes are not highlighted, for example, <p>Sa<span>turday</span></p>.

After being highlighted, text entities on the page are converted into hyperlinks. When they are touched or left-clicked, the operation menu is displayed based on the entity type.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  webController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('Refresh')
          .onClick(() => {
            this.webController.refresh();
          })
      }

      Web({
        src: $rawfile('index.html'),
        controller: this.webController
      })
        .enableDataDetector(true)
        .dataDetectorConfig({
          types: \[\]  // Entity recognition type. If this parameter is left empty, all types are recognized.
        })
    }
    .height('100%')
    .width('100%')
  }
}

HTML file to be loaded:

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <p>Telephone: 400-123-4567</p>
    <p>Email address: test@example.com</p>
    <p>URL: https://www.example.com/</p>
    <p>Date: 2025.06.01</p>
    <p>Address: Zhongguancun, Haidian District, Beijing</p>
    <p>Sa<span>turday</span> will not be highlighted and Saturday will be highlighted</p>
</body>
</html>

Click a text entity to display the corresponding operation menu, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/WSP-6PnzTpqo6g3yLkIHJA/en-us_image_0000002568764753.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C44B228CE6B5CD573239DF14D0A8314B8B020AA8C812C0860F428F99E3B9DEF)

Right-clicking or dragging the mouse triggers the default behavior of the hyperlink.

When the [dataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#datadetectorconfig20) API is not used or **enablePreviewMenu** of the [TextDataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11) attribute is set to **false**, long-pressing or dragging triggers the default behavior of the hyperlink, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/HvCTJ-bWTCWOYop7tBEUzQ/en-us_image_0000002537765028.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2949DBBD4E39577D9ACE59924ABE4C0B4930AE1E870D330B69163819D527ED7)

If the computed style of the text element on the page contains **user-select:none**, the **Select text** option in the entity menu is invalid. However, the entity text can still be copied when [copyOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#copyoptions11) is not **CopyOptions.None**.

#### Long Press Preview

To use the long-press preview functionality, you need to configure [dataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#datadetectorconfig20) as follows:

Web({
src: $rawfile('index.html'),
controller: this.webController
})
.enableDataDetector(true)
.dataDetectorConfig({
  enablePreviewMenu: true,  // Enable the long-press preview functionality.
  types: \[\]
})

If [copyOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#copyoptions11) is not set to **CopyOptions.None**, a preview menu is displayed when you long-press the highlighted entity text, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ZlU-cE9mTAKfBXZiBlS0MQ/en-us_image_0000002537924968.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1BA0350A413BB210C4F84D4313CEC84A77DE18E1963479E0DEF3A7F3DDB851B)

The [custom menu](../using-web-menus/document.md#custom-menu) bound by [bindSelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#bindselectionmenu13) does not affect the long-press preview menu of text segmentation. Long-pressing the highlighted text segmentation hyperlink does not display the custom hyperlink menu, and long-pressing a common hyperlink does not display the text segmentation preview menu.

#### Text Selection Menu Extension

Since API version 22, the [enableSelectedDataDetector](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#enableselecteddatadetector22) can be used to configure whether to enable the AI option in the text selection menu.

In the non-editing area, if the selected text meets the following conditions, the corresponding AI option are displayed in the text selection menu:

-   The UTF-8-encoded selected text does not exceed 255 bytes.
-   The selected text contains only one entity word that matches the recognition type. (You can configure the recognition type supported by [dataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#datadetectorconfig20).)
-   The text is not in the **Select all** operation state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Z8sdqeyLTJmbgrZY0njFIw/en-us_image_0000002568684745.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBCA67E8849A52F9FB50EE58DB8EAB372033BCE4878121A8B49D59238778A454)

The AI menu item is displayed as long as the preceding conditions are met, regardless of whether the highlighted entity text is selected.
