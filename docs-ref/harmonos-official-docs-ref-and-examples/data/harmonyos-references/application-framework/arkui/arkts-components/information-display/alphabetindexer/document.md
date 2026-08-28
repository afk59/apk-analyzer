# AlphabetIndexer

The **AlphabetIndexer** component can create a logically indexed array of items in a container for instant location.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/7PazrdEYRLi_fWpaVui1tA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=886A75E44053E447397977FD4393980C7D9F65F324306040E920B26FF3E61620)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

AlphabetIndexer(options: AlphabetIndexerOptions)

Creates an **AlphabetIndexer** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AlphabetIndexerOptions](#alphabetindexeroptions18) | Yes | Options of the **AlphabetIndexer** component. |

#### AlphabetIndexerOptions18+

Defines the options of the **AlphabetIndexer** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/U55L6jR8QtiWdOyjHe0y9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5B36C3946E53AB904D08C61F133FB65CEB8BD8C74B2479142231365046C06F8)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| arrayValue7+ | Array<string> | No | No | 
Array of index items.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selected7+ | number | No | No | 

Index of the initial selected item. If the value is out of range, the default value **0** is used.

This parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

When the [width](../../universal-attributes/layout-and-borders/sizing/document.md#width) attribute is set to **"auto"**, the width is adaptive. This means that the width will adjust according to the maximum width of the index items.

The default value of the [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) attribute is 4 vp.

The [maxFontScale](../../text-and-input/text/document.md#maxfontscale12) and [minFontScale](../../text-and-input/text/document.md#minfontscale12) attributes are both set to a constant value of 1, which means that they do not change with the system font size.

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]color

color(value: ResourceColor)

Sets the text color for unselected items.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Text color of unselected items.

Default value: **0x99182431**, which is a slightly transparent brown.

 |

#### \[h2\]selectedColor

selectedColor(value: ResourceColor)

Sets the text color for the selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Text color of the selected item.

Default value: **0xFF007DFF**, which is blue.

 |

#### \[h2\]popupColor

popupColor(value: ResourceColor)

Sets the text color for the primary index item in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Text color of the primary index item in the pop-up window.

Default value: **0xFF007DFF**, which is blue.

 |

#### \[h2\]selectedBackgroundColor

selectedBackgroundColor(value: ResourceColor)

Sets the background color of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the selected item.

Default value: **0x1A007DFF**, which is semi-transparent blue-green.

 |

#### \[h2\]popupBackground

popupBackground(value: ResourceColor)

Sets the background color for the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the pop-up window.

The background blur effect of the pop-up text can affect the background color. You can disable the effect by setting [popupBackgroundBlurStyle](#popupbackgroundblurstyle12) to **NONE**.

Default value:

API version 11 and earlier: **0xFFFFFFFF**, which is white.

Since API version 12: **#66808080**, which is semi-transparent gray.

 |

#### \[h2\]usingPopup

usingPopup(value: boolean)

Sets whether to display the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the pop-up window.

Default value: **false**.

**true**: Display the pop-up window.

**false**: Do not display the pop-up window.

 |

#### \[h2\]selectedFont

selectedFont(value: Font)

Sets the text style for the selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text style of the selected item.

Default value:

API version 11 and earlier:

{

size:'12.0fp',

style:FontStyle.Normal,

weight:FontWeight.Regular,

family:'HarmonyOS Sans'

}

API version 12 and later:

{

size:'10.0vp',

style:FontStyle.Normal,

weight:FontWeight.Medium,

family:'HarmonyOS Sans'

}

 |

#### \[h2\]popupFont

popupFont(value: Font)

Sets the text style for the primary index item in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text style of the primary index item in the pop-up window.

Default value:

{

size:'24.0vp',

style:FontStyle.Normal,

weight:FontWeight.Medium,

family:'HarmonyOS Sans'

}

 |

#### \[h2\]font

font(value: Font)

Sets the text style for unselected items.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text style of unselected items.

Default value:

API version 11 and earlier:

{

size:'12.0fp',

style:FontStyle.Normal,

weight:FontWeight.Regular,

family:'HarmonyOS Sans'

}

API version 12 and later:

{

size:'10.0vp',

style:FontStyle.Normal,

weight:FontWeight.Medium,

family:'HarmonyOS Sans'

}

 |

#### \[h2\]itemSize

itemSize(value: string | number)

Sets the size of the index item area.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | number | Yes | 
Size of the index item area, which is a square, meaning the side length of the square. This attribute cannot be set in percentage.

The actual value is restricted by the component size. The maximum width of an index item is the component width minus the left and right [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding), and the maximum height of an index item is (component height minus the top and bottom [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding))/number of index items. If the input value is less than or equal to 0, the default value is used.

Default value: **16.0**

Unit: vp

 |

#### \[h2\]alignStyle

alignStyle(value: IndexerAlign, offset?: Length)

Sets the alignment style of the indexer pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [IndexerAlign](#indexeralign) | Yes | 
Alignment style of the indexer pop-up window. The pop-up window can be displayed on the right or left of the indexer.

Default value: **IndexerAlign.END**

 |
| offset10+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Spacing between the pop-up window and the alphabetic index bar. A value greater than or equal to **0** is valid. If this parameter is set to a value less than **0** or is not set, the spacing is the same as **popupPosition**. When this parameter and [popupPosition](#popupposition8) are set at the same time, **offset** takes effect in the horizontal direction, and **popupPosition.y** takes effect in the vertical direction. |

#### \[h2\]selected8+

selected(index: number)

Sets the index of the selected item.

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the selected item.

Default value: **0**

 |

#### \[h2\]popupPosition8+

popupPosition(value: Position)

Sets the position of the pop-up window relative to the center of the indexer's top border.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Position](../../common-definitions/basic-types/document.md#position) | Yes | 
Position of the pop-up window relative to the center of the indexer's top border.

Default value: **{x: 60.0, y: 48.0}**

 |

#### \[h2\]popupSelectedColor10+

popupSelectedColor(value: ResourceColor)

Sets the text color for the selected secondary index item in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Text color of the selected secondary index items in the pop-up window.

Default value: **#FF182431**, which is dark blue.

 |

#### \[h2\]popupUnselectedColor10+

popupUnselectedColor(value: ResourceColor)

Sets the text color for the unselected secondary index items in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Text color of the unselected secondary index items in the pop-up window.

Default value: **#FF182431**, which is dark blue.

 |

#### \[h2\]popupItemFont10+

popupItemFont(value: Font)

Sets the text style for the secondary index item in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Text style of the secondary index item in the pop-up window.

Default value:

{

size:24,

weight:FontWeight.Medium

}

 |

#### \[h2\]popupItemBackgroundColor10+

popupItemBackgroundColor(value: ResourceColor)

Sets the background color for the secondary index item in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the secondary index item in the pop-up window.

Default value:

API version 11 and earlier: **#FFFFFFFF**, which is white.

Since API version 12: **#00000000**, which is black.

 |

#### \[h2\]autoCollapse11+

autoCollapse(value: boolean)

Sets whether to enable the adaptive collapse behavior for the indexer.

When the first index item is **"#"**: Remaining items ≤ 9: Full display mode; 9 < Remaining items ≤ 13: Adapts between full display and short collapse modes based on the indexer height; remaining items > 13: Adapts between short and long collapse modes based on the indexer height.

When the first index item is not **"#"**: All items ≤ 9: Full display mode; 9 < All items ≤ 13: Adapts between full display and short collapse modes based on the indexer height; all items > 13: Adapts between short and long collapse modes based on the indexer height.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/YU7j4wSNQ9em_zCuWXHUHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DE6B81F4DEED1F71DEE1CE00B1D7FE465D20DBADA3F4957FCB0349F4B2828EF)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to auto-collapse or expand the indexer bar.

Default value:

Before API version 12: **false**

Since API version 12: **true**

**true**: Enable the adaptive collapse behavior.

**false**: Disable the adaptive collapse behavior.

 |

#### \[h2\]popupItemBorderRadius12+

popupItemBorderRadius(value: number)

Sets the radius of the index border corners in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Radius of the index background border corners in the pop-up window.

Default value: **24vp**.

This parameter cannot be set in percentage. If the value specified is less than **0**, **0** is used.

The radius of the index background border corners in the pop-up window is automatically adaptive (radius of the index corners + 4 vp).

 |

#### \[h2\]itemBorderRadius12+

itemBorderRadius(value: number)

Sets the radius of the index background border corners in the alphabetic index bar.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Radius of the index background border corners in the alphabetic index bar.

Default value: **8vp**

This parameter cannot be set in percentage. If the value specified is less than **0**, **0** is used.

The radius of the index background border corners in the alphabetic index bar is automatically adaptive (radius of the index corners + 4 vp).

 |

#### \[h2\]popupBackgroundBlurStyle12+

popupBackgroundBlurStyle(value: BlurStyle)

Sets the background blur style of the pop-up window. If this API is not called, the component is regularly blurred by default. The corresponding value is **COMPONENT\_REGULAR** in **BlurStyle**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | Yes | 
Background blur style of the pop-up window.

The background blur effect can affect [popupBackground](#popupbackground). You can disable the effect by setting it to **NONE**.

 |

#### \[h2\]popupTitleBackground12+

popupTitleBackground(value: ResourceColor)

Sets the background color for the primary index item in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color for the primary index item in the pop-up window.

Default value:

If the pop-up window has only one index: **#00FFFFFF**.

If the pop-up window has multiple indexes: **#0c182431**.

 |

#### \[h2\]enableHapticFeedback12+

enableHapticFeedback(value: boolean)

Sets whether to enable haptic feedback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable haptic feedback.

**true**: To enable haptic feedback.

**false**: Not to enable haptic feedback.

Default value: **true**

To enable haptic feedback, you must declare the **ohos.permission.VIBRATE** permission under **requestPermissions** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file of the project.

"requestPermissions": \[{"name": "ohos.permission.VIBRATE"}\]

 |

#### IndexerAlign

Enumerates the alignment styles of the indexer pop-up window.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Left | 0 | 
The pop-up window is displayed on the right of the indexer.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Right | 1 | 

The pop-up window is displayed on the left of the indexer.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| START12+ | 2 | 

The pop-up window is displayed on the right of the indexer for left-to-right scripts, and on the left of the indexer for right-to-left scripts.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| END12+ | 3 | 

The pop-up window is displayed on the left of the indexer for left-to-right scripts, and on the right of the indexer for right-to-left scripts.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onSelected(deprecated)

onSelected(callback: (index: number) => void)

Triggered when an index item is selected, with the callback parameter being the index of the currently selected item.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/8Ijkj-k5Q8OiIHMz_cM5fw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=202F6C49BDB0F8A7E26EDFEDB243A5971028E87476DFE23CE9383AA5BE3AE342)

This API is supported since API version 7 and deprecated since API version 8. You are advised to use [onSelect](#onselect8) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected item. |

#### \[h2\]onSelect8+

onSelect(callback: OnAlphabetIndexerSelectCallback)

Triggered when an index item is selected, with the callback parameter being the index of the currently selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnAlphabetIndexerSelectCallback](#onalphabetindexerselectcallback18) | Yes | Event triggered when an index item is selected. |

#### \[h2\]onRequestPopupData8+

onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback)

Triggered for a secondary index item content event in the pop-up window. The callback parameter is the index of the selected secondary index item. The return value is the secondary index item content to be displayed in the pop-up window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](#onalphabetindexerrequestpopupdatacallback18) | Yes | Callback for setting the secondary index item content event in the pop-up window. |

#### \[h2\]onPopupSelect8+

onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback)

Triggered when a secondary index item in the pop-up window is selected. The callback parameter is the index of the selected secondary index item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnAlphabetIndexerPopupSelectCallback](#onalphabetindexerpopupselectcallback18) | Yes | Event triggered when a secondary index item in the pop-up window is selected. |

#### OnAlphabetIndexerSelectCallback18+

type OnAlphabetIndexerSelectCallback = (index: number) => void

Represents the callback invoked when an index item is selected.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the currently selected index item. |

#### OnAlphabetIndexerPopupSelectCallback18+

type OnAlphabetIndexerPopupSelectCallback = (index: number) => void

Represents the callback invoked when a secondary index item in the pop-up window is selected.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the currently selected secondary index item in the pop-up window. |

#### OnAlphabetIndexerRequestPopupDataCallback18+

type OnAlphabetIndexerRequestPopupDataCallback = (index: number) => Array<string>

Represents the callback invoked when an index item is selected and [usingPopup](#usingpopup) is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the currently selected index item. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Array of secondary index items to be displayed in the pop-up window. Up to 5 items can be displayed vertically, with scrollable support for more items. |

#### Example

## Example 1: Setting the Display Text for the Index Pop-up Window

This example demonstrates how to customize the display text for the index pop-up window using the [onRequestPopupData](#onrequestpopupdata8) event.

// xxx.ets
@Entry
@Component
struct AlphabetIndexerSample {
  private arrayA: string\[\] = \['An'\];
  private arrayB: string\[\] = \['Bu', 'Bai', 'Bao', 'Bi', 'Bing'\];
  private arrayC: string\[\] = \['Cao', 'Cheng', 'Chen', 'Cui'\];
  private arrayL: string\[\] = \['Liu', 'Li', 'Lou', 'Liang', 'Lei', 'Lv', 'Liu', 'Lu'\];
  private value: string\[\] = \['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'\];

  build() {
    Stack({ alignContent: Alignment.Start }) {
      Row() {
        List({ space: 20, initialIndex: 0 }) {
          ForEach(this.arrayA, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayB, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayC, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayL, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)
        }
        .width('50%')
        .height('100%')

        AlphabetIndexer({ arrayValue: this.value, selected: 0 })
          .autoCollapse (false) // Disable the auto-collapse mode.
          .enableHapticFeedback(false) // Disable haptic feedback.
          .selectedColor(0xFFFFFF) // Text color of the selected item.
          .popupColor(0xFFFAF0) // Text color of the primary index item in the pop-up window.
          .selectedBackgroundColor(0xCCCCCC) // Background color of the selected item.
          .popupBackground (0xD2B48C) // Background color of the pop-up window.
          .usingPopup(true) // Display a pop-up window when an index item is selected.
          .selectedFont({ size: 16, weight: FontWeight.Bolder }) // Text style of the selected item.
          .popupFont({ size: 30, weight: FontWeight.Bolder }) // Text style of the primary index item in the pop-up window.
          .itemSize(28) // Size of each index item.
          .alignStyle (IndexerAlign.Left) // The pop-up window is displayed on the right of the indexer.
          .popupItemBorderRadius(24) // Set the radius of the index background rounded corners in the pop-up window.
          .itemBorderRadius(14) // Set the radius of the index background rounded corners.
          .popupBackgroundBlurStyle(BlurStyle.NONE) // Set the background blur style of the pop-up window.
          .popupTitleBackground(0xCCCCCC) // Background color of the primary index item in the pop-up window.
          .popupSelectedColor(0x00FF00) // Text color of the selected secondary index items in the pop-up window.
          .popupUnselectedColor(0x0000FF) // Text color of the unselected secondary index item in the pop-up window.
          .popupItemFont({ size: 30, style: FontStyle.Normal }) // Text style of the secondary index item in the pop-up window.
          .popupItemBackgroundColor(0xCCCCCC) // Background color of the secondary index item in the pop-up window.
          .onSelect((index: number) => {
            console.info(this.value\[index\] + ' Selected!');
          })
          .onRequestPopupData((index: number) => {
            // When A is selected, the secondary index item list in the pop-up window displays arrayA. Similarly, selecting B, C, or L will display their respective arrays.
            // For other index items, the pop-up window will only show the primary index item.
            if (this.value\[index\] == 'A') {
              return this.arrayA;
            } else if (this.value\[index\] == 'B') {
              return this.arrayB;
            } else if (this.value\[index\] == 'C') {
              return this.arrayC;
            } else if (this.value\[index\] == 'L') {
              return this.arrayL;
            } else {
              return \[\];
            }
          })
          .onPopupSelect((index: number) => {
            console.info('onPopupSelected:' + index);
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/lRhRyk0yQ5uMlIHP-pT_Ww/en-us_image_0000002537925714.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBCAE72B0520CD7E7E9EA6310445240D8D4A3A143781B4159D964CA8BC5A10C2)

## Example 2: Enabling Adaptive Collapse Mode

This example demonstrates how to enable adaptive collapse mode using the [autoCollapse](#autocollapse11) attribute.

// xxx.ets
@Entry
@Component
struct AlphabetIndexerSample {
  private arrayA: string\[\] = \['An'\];
  private arrayB: string\[\] = \['Bu', 'Bai', 'Bao', 'Bi', 'Bing'\];
  private arrayC: string\[\] = \['Cao', 'Cheng', 'Chen', 'Cui'\];
  private arrayJ: string\[\] = \['Jia', 'Jia'\];
  private value: string\[\] = \['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'\];
  @State isNeedAutoCollapse: boolean = false;
  @State indexerHeight: string = '75%';

  build() {
    Stack({ alignContent: Alignment.Start }) {
      Row() {
        List({ space: 20, initialIndex: 0 }) {
          ForEach(this.arrayA, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayB, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayC, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayJ, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)
        }
        .width('50%')
        .height('100%')

        Column() {
          Column() {
            AlphabetIndexer({ arrayValue: this.value, selected: 0 })
              .autoCollapse (this.isNeedAutoCollapse) // Enable or disable adaptive collapse mode.
              .height (this.indexerHeight) // Indexer height.
              .enableHapticFeedback(false) // Disable haptic feedback.
              .selectedColor(0xFFFFFF) // Text color of the selected item.
              .popupColor(0xFFFAF0) // Text color of the primary index item in the pop-up window.
              .selectedBackgroundColor(0xCCCCCC) // Background color of the selected item.
              .popupBackground (0xD2B48C) // Background color of the pop-up window.
              .usingPopup(true) // Display a pop-up window when an index item is selected.
              .selectedFont({ size: 16, weight: FontWeight.Bolder }) // Text style of the selected item.
              .popupFont({ size: 30, weight: FontWeight.Bolder }) // Text style of the pop-up window.
              .itemSize(28) // Size of an item in the alphabetic index bar.
              .alignStyle(IndexerAlign.Right) // The pop-up window is displayed on the left of the indexer.
              .popupTitleBackground("#D2B48C") // Background color of the primary index item in the pop-up window.
              .popupSelectedColor(0x00FF00) // Text color of the unselected secondary index items in the pop-up window.
              .popupUnselectedColor(0x0000FF) // Text color of the selected secondary index item in the pop-up window.
              .popupItemFont({ size: 30, style: FontStyle.Normal }) // Text style of the secondary index item in the pop-up window.
              .popupItemBackgroundColor(0xCCCCCC) // Background color of the secondary index item in the pop-up window.
              .onSelect((index: number) => {
                console.info(this.value\[index\] + ' Selected!');
              })
              .onRequestPopupData((index: number) => {
                // When A is selected, the secondary index item list in the pop-up window displays arrayA. Similarly, selecting B, C, or L will display their respective arrays.
                // For other index items, the pop-up window will only show the primary index item.
                if (this.value\[index\] == 'A') {
                  return this.arrayA;
                } else if (this.value\[index\] == 'B') {
                  return this.arrayB;
                } else if (this.value\[index\] == 'C') {
                  return this.arrayC;
                } else if (this.value\[index\] == 'J') {
                  return this.arrayJ;
                } else {
                  return \[\];
                }
              })
              .onPopupSelect((index: number) => {
                console.info('onPopupSelected:' + index);
              })
          }
          .height('80%')
          .justifyContent(FlexAlign.Center)

          Column() {
            Button('Collapse')
              .margin('5vp')
              .onClick(() => {
                this.isNeedAutoCollapse = true;
              })
            Button('30% of Index Bar Height')
              .margin('5vp')
              .onClick(() => {
                this.indexerHeight = '30%';
              })
            Button('70% of Index Bar Height')
              .margin('5vp')
              .onClick(() => {
                this.indexerHeight = '70%';
              })
          }.height('20%')
        }
        .width('50%')
        .justifyContent(FlexAlign.Center)
      }
      .width('100%')
      .height(720)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/RIWq32u7RHyLWGSsm2fVGw/en-us_image_0000002568685491.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7DDEEBEABEFD74D5E9B665B6AE9FF35DCBF05DF6F08EC397ABB4684881E120E)

## Example 3: Setting the Background Blur Style of the Pop-up Window

This example demonstrates how to apply a background blur effect to the pop-up window using the [popupBackgroundBlurStyle](#popupbackgroundblurstyle12) attribute.

// xxx.ets
@Entry
@Component
struct AlphabetIndexerSample {
  private arrayA: string\[\] = \['An'\];
  private arrayB: string\[\] = \['Bu', 'Bai', 'Bao', 'Bi', 'Bing'\];
  private arrayC: string\[\] = \['Cao', 'Cheng', 'Chen', 'Cui'\];
  private arrayL: string\[\] = \['Liu', 'Li', 'Lou', 'Liang', 'Lei', 'Lv', 'Liu', 'Lu'\];
  private value: string\[\] = \['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'\];
  @State customBlurStyle: BlurStyle = BlurStyle.NONE;

  build() {
    Stack({ alignContent: Alignment.Start }) {
      Row() {
        List({ space: 20, initialIndex: 0 }) {
          ForEach(this.arrayA, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayB, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayC, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)

          ForEach(this.arrayL, (item: string) => {
            ListItem() {
              Text(item)
                .width('80%')
                .height('5%')
                .fontSize(30)
                .textAlign(TextAlign.Center)
            }
          }, (item: string) => item)
        }
        .width('30%')
        .height('100%')

        Column() {
          Column() {
            Text('Switch Blur Style: ')
              .fontSize(24)
              .fontColor(0xcccccc)
              .width('100%')
            Button('COMPONENT\_REGULAR')
              .margin('5vp')
              .width(200)
              .onClick(() => {
                this.customBlurStyle = BlurStyle.COMPONENT\_REGULAR;
              })
            Button('BACKGROUND\_THIN')
              .margin('5vp')
              .width(200)
              .onClick(() => {
                this.customBlurStyle = BlurStyle.BACKGROUND\_THIN;
              })
          }.height('20%')

          Column() {
            AlphabetIndexer({ arrayValue: this.value, selected: 0 })
              .usingPopup(true) // Display a pop-up window when an index item is selected.
              .alignStyle (IndexerAlign.Left) // The pop-up window is displayed on the right of the indexer.
              .popupItemBorderRadius(24) // Set the radius of the index background rounded corners in the pop-up window.
              .itemBorderRadius(14) // Set the radius of the index background rounded corners.
              .popupBackgroundBlurStyle(this.customBlurStyle) // Set the background blur style of the pop-up window.
              .popupTitleBackground(0xCCCCCC) // Background color of the primary index item in the pop-up window.
              .onSelect((index: number) => {
                console.info(this.value\[index\] + ' Selected!');
              })
              .onRequestPopupData((index: number) => {
                // When A is selected, the secondary index item list in the pop-up window displays arrayA. Similarly, selecting B, C, or L will display their respective arrays.
                // For other index items, the pop-up window will only show the primary index item.
                if (this.value\[index\] == 'A') {
                  return this.arrayA;
                } else if (this.value\[index\] == 'B') {
                  return this.arrayB;
                } else if (this.value\[index\] == 'C') {
                  return this.arrayC;
                } else if (this.value\[index\] == 'L') {
                  return this.arrayL;
                } else {
                  return \[\];
                }
              })
              .onPopupSelect((index: number) => {
                console.info('onPopupSelected:' + index);
              })
          }
          .height('80%')
        }
        .width('70%')
      }
      .width('100%')
      .height('100%')
      // Replace $r('app.media.image') with the image resource file you use.
      .backgroundImage($r("app.media.image"))
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/3yaM1PJEQnKI0iU2e8QMcA/en-us_image_0000002568765501.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A21BEAFDF4B6162E9B56D88C9D4CF91B3541DAE6B4C317E9A81D33EE2B672766)
