# Class (ComponentUtils)

Provides API for obtaining the coordinates and size of the drawing area of a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/x0qE3_51ShOTzqRG1t5wPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F1C588156B9C5410C70EE1F2EDC0996E341A8D483226066240BB258AAFDD964)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   In the following API examples, you must first use [getComponentUtils()](../class-uicontext/document.md#getcomponentutils) in **UIContext** to obtain a **ComponentUtils** instance, and then call the APIs using the obtained instance.
    

#### getRectangleById

getRectangleById(id: string): componentUtils.ComponentInfo

Obtains the size, position, translation, scaling, rotation, and affine matrix information of the specified component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/9O2gfs8AQhChOQG2H_YSxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6CBAFC0B74C4BCF34E5A2DF65FCE190EF3870F8AF3654D26671F28E6552CF14)

This API should be called after the target component's layout is complete to obtain its size information. It is recommended that you use this API within [onAppear](../../../../arkts-components/universal-events/component-change-events/show-hide-event/document.md#onappear).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Unique component ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [componentUtils.ComponentInfo](../../ohos-arkui-componentutils-componentutils/document.md#componentinfo) | Size, position, translation, scaling, rotation, and affine matrix information of the component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 100001 | UI execution context not found. |

**Example**

import { ComponentUtils } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page\_text\_font\_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
          let modePosition = componentUtils.getRectangleById("HelloWorld");
          let width = modePosition.size.width; // Obtain the component width.
          let height = modePosition.size.height; // Obtain the component height.
          let localOffsetX = modePosition.localOffset.x; // Obtain the x-axis offset of the component relative to its parent component.
          let localOffsetY = modePosition.localOffset.y; // Obtain the y-axis offset of the component relative to its parent component.
          console.info(\`width: ${width}, height: ${height}, localOffsetX: ${localOffsetX}, localOffsetY: ${localOffsetY}\`);
        })
    }
    .height('100%')
    .width('100%')
  }
}
