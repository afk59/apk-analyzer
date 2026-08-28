# ArcAlphabetIndexer

The **ArcAlphabetIndexer** component is an arc-shaped component designed for quick navigation through alphabetically sorted items. It can be integrated with container components to quickly locate items within the visible area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/nGl34wlrQRO5b_8azwp9WA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B324688668AE247FC6E8F4EF0FB0558D0CEEF5355B50784C3265BA0FA1B0B63)

This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/0qn1vrrVShy52THuSFdbQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D936C7D113E1DE3E5CF62DCD1126D78111054C1A471172E9DA7EC0F6FF1F9CAD)

-   **ArcAlphabetIndexerAttribute** is essential for configuring the **ArcAlphabetIndexer** component. In API version 21 and earlier, you must manually import **ArcAlphabetIndexerAttribute** after importing the **ArcAlphabetIndexer** component. Otherwise, a compilation error is reported. However, starting from API version 22, the compilation toolchain automatically imports **ArcAlphabetIndexerAttribute** when it detects the **ArcAlphabetIndexer** component, so manual import is no longer necessary.
    
-   If you manually import **ArcAlphabetIndexerAttribute**, DevEco Studio shows it as disabled (grayed out). In API version 21 and earlier, removing this import causes a compilation error. But from API version 22 onward, removing it does not affect the functionality.
    

API version 21 and earlier:

import { ArcAlphabetIndexer, ArcAlphabetIndexerAttribute } from '@kit.ArkUI';

API version 22 and later:

import { ArcAlphabetIndexer } from '@kit.ArkUI';

#### Child Components

Not supported

#### APIs

ArcAlphabetIndexer(info: ArcAlphabetIndexerInitInfo)

Creates an instance of the **ArcAlphabetIndexer** component with initialization parameters.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [ArcAlphabetIndexerInitInfo](#arcalphabetindexerinitinfo) | Yes | Initialization parameters for the **ArcAlphabetIndexer** component. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]color

color(color: Optional<ColorMetrics>)

Sets the text color of the index items in the normal state.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Text color.

Default value: **0xFFFFFF**, displayed as white

 |

#### \[h2\]selectedColor

selectedColor(color: Optional<ColorMetrics>)

Sets the text color of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Text color of the selected item.

Default value: **0xFFFFFF**, displayed as white

 |

#### \[h2\]popupColor

popupColor(color: Optional<ColorMetrics>)

Sets the text color for the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Text color of the pop-up window.

Default value: **0xFFFFFF**, displayed as white

 |

#### \[h2\]selectedBackgroundColor

selectedBackgroundColor(color: Optional<ColorMetrics>)

Sets the background color of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Background color of the selected item.

Default value: **0x1F71FF**, displayed as dark blue

 |

#### \[h2\]popupBackground

popupBackground(color: Optional<ColorMetrics>)

Sets the background color of the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Background color of the pop-up window.

Default value: **0xD8404040**, displayed as dark gray with slight transparency

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/kHoeInmHS-efqopu_Jh_og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=771CC01B4DEFF8E2ACA62629FD6CF24F951BF7B615F8EC28D29F7768C562E494)

After configuring the popup background color with **popupBackground**, avoid applying background blur effects via [popupBackgroundBlurStyle](#popupbackgroundblurstyle).

#### \[h2\]usePopup

usePopup(enabled: Optional<boolean>)

Sets whether to display the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to display the pop-up window.

**true**: yes; **false**: no

Default value: **false**

 |

#### \[h2\]selectedFont

selectedFont(font: Optional<Font>)

Sets the font style of the selected item, including size, weight, style, and font family.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| font | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Font](../../common-definitions/basic-types/document.md#font)\> | Yes | 
Font style of the selected item.

Default value: {

size:'13.0fp',

style:FontStyle.Normal,

weight:500,

family:'HarmonyOS Sans'

}

 |

#### \[h2\]popupFont

popupFont(font: Optional<Font>)

Sets the font style of the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| font | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Font](../../common-definitions/basic-types/document.md#font)\> | Yes | 
Font style of the pop-up window.

Default value:

{

size:'19.0fp',

style:FontStyle.Normal,

weight:500,

family:'HarmonyOS Sans'

}

 |

#### \[h2\]font

font(font: Optional<Font>)

Sets the default font style of the index items.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| font | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Font](../../common-definitions/basic-types/document.md#font)\> | Yes | 
Default font style of the index items.

Default value:

{

size:'13.0fp',

style:FontStyle.Normal,

weight:500,

family:'HarmonyOS Sans'

}

 |

#### \[h2\]itemSize

itemSize(size: Optional<LengthMetrics>)

Sets the size of the index item area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\> | Yes | 
Size of the index item area. For the circular item area, this represents the diameter of the circle. Percentage values are not supported.

Default value: **24.0**

Unit: vp

 |

#### \[h2\]selected

selected(index: Optional<number>)

Sets the index of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | Optional<number> | Yes | 
Index of the selected item.

Default value: **0**

This parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

 |

#### \[h2\]autoCollapse

autoCollapse(enable: Optional<boolean>)

Sets whether to enable the adaptive collapse behavior for the indexer.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable the adaptive collapse behavior for the indexer.

Default value: **true**.

**true**: Enable the adaptive collapse behavior.

**false**: Disable the adaptive collapse behavior.

 |

#### \[h2\]popupBackgroundBlurStyle

popupBackgroundBlurStyle(style: Optional<BlurStyle>)

Sets the background blur style of the pop-up window. If this API is not used, the blur is disabled by default. The corresponding value is **NONE** in **BlurStyle**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/b0HN4FK8QAmMBrkoHtnTyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=894E7995D60E63312872E463066C59A1CFF0310B92A3232B4535BB65465D9FAC)

After configuring the pop-up window background blur style with **popupBackgroundBlurStyle**, avoid applying background colors via [popupBackground](#popupbackground).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9)\> | Yes | Background blur style of the pop-up window. |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onSelect

onSelect(handler: Optional<OnSelectCallback>)

Triggered when an index item is selected. The return value is the index of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnSelectCallback](#onselectcallback)\> | Yes | Callback used to return the result. |

#### ArcAlphabetIndexerInitInfo

Initialization parameters for the **ArcAlphabetIndexer** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| arrayValue | string\[\] | No | No | Array of alphabet index strings. It cannot be set to empty. |
| selected | number | No | No | 
Index of the initial selected item. If the value is out of range, the default value **0** is used.

This parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

 |

#### OnSelectCallback

type OnSelectCallback = (index: number) => void

Defines the callback used in [onSelect](#onselect).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected item. |

#### Example

This example demonstrates how to link an **ArcAlphabetIndexer** component with an **ArcList** component for synchronized control and navigation.

// xxx.ets
import {
  LengthMetrics,
  ColorMetrics,
  ArcList,
  ArcListItem,
  ArcListAttribute,
  ArcListItemAttribute,
  ArcAlphabetIndexer,
  ArcAlphabetIndexerAttribute
} from '@kit.ArkUI';
// Starting from API version 22, you do not need to manually import ArcListAttribute, ArcListItemAttribute, and ArcAlphabetIndexerAttribute. For details, refer to the Modules to Import section of ArcList, ArcListItem, and ArcAlphabetIndexer.

@Entry
@Component
struct ArcListAndIndexer {
  private fullValue: string\[\] = \[
    '#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  \];
  private arrName : string\[\] = \[
    '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',
    '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38',
    '39','40', '41','42',
  \];

  private scrollerForList: Scroller = new Scroller();
  @State indexerIndex: number = 0;

  private watchSize: string = '466px'; // Default watch size: 233\*233
  private itemSize: number = 24;  // Default size of the index item area: 24

  build() {
    Column() {
      Row() {
        Stack() {
          ArcList({ scroller : this.scrollerForList, initialIndex: 0 }) {
            ForEach(this.arrName, (itemName: string, index: number) => {
              ArcListItem() {
                Text(itemName)
                  .width('90%')
                  .height('92px')
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(index % 2 == 0 ? 0xAFEEEE : 0x00FFFF)
                  .borderRadius(23)
              }
            })
          }
          .scrollBar(BarState.Off)
          .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
            this.indexerIndex = centerIndex;
          })
          .borderWidth(1)
          .width(this.watchSize)
          .height(this.watchSize)
          .borderRadius(this.watchSize)
          .space(LengthMetrics.px(4))

          ArcAlphabetIndexer({ arrayValue: this.fullValue, selected: 0 })
            .autoCollapse(true)
            .width(this.watchSize)
            .height(this.watchSize)
            .usePopup(false)
            .selected(this.indexerIndex)
            .onSelect((index: number) => {
              this.indexerIndex = index;
              this.scrollerForList.scrollToIndex(this.indexerIndex);
            })
            .borderWidth(1)
            .hitTestBehavior(HitTestMode.Transparent)
            .selectedColor(ColorMetrics.resourceColor(0xFFFFFF))
            .selectedBackgroundColor(ColorMetrics.resourceColor(0x1F71FF))
            .color(ColorMetrics.resourceColor(0xFFFFFF))
            .popupColor(ColorMetrics.resourceColor(0xFFFFFF))
            .popupBackground(ColorMetrics.resourceColor(0xD8404040))
            .itemSize(LengthMetrics.px(this.itemSize))
            .selectedFont({
              size:'11.0fp',
              style:FontStyle.Normal,
              weight:500,
              family:'HarmonyOS Sans'
            })
            .font({
              size:'11.0fp',
              style:FontStyle.Normal,
              weight:500,
              family:'HarmonyOS Sans'
            })

        }.width('100%').height('100%')
      }.width('100%').height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/tite1KAVRt-sp5Bo9UwZ5Q/en-us_image_0000002537765776.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=387544A9FE3735E2C53D341C216EC79A8F666D5570ADEEFB608879FBB62B60A7)
