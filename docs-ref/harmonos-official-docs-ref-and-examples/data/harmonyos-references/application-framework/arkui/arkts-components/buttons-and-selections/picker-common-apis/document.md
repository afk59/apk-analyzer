# Picker Common APIs

This topic covers the common APIs of picker components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/WYr8uk4nR8G0bfT4FkKTwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE9777FAB4E20E46CA4C6606A812A81F5CD4860DE040E465F4F605E62875DAF8)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### PickerTextStyle

Defines the text style configuration for the picker component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Text color. |
| font | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | Text style. |

#### PickerDialogButtonStyle12+

Defines the button style of the picker dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ButtonType](../button/document.md#buttontype) | No | Yes | Button type. |
| style | [ButtonStyleMode](../button/document.md#buttonstylemode11) | No | Yes | Style and importance of the button. |
| role | [ButtonRole](../button/document.md#buttonrole12) | No | Yes | Role of the button. |
| fontSize | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | Font size of the button. |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Color of button text. |
| fontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | number | string | No | Yes | Font weight of button text For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. For the string type, only strings that represent a number, for example, **"200"**, and the following enumerated values of **FontWeight** are supported: **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**. |
| fontStyle | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | No | Yes | Font style of button text. |
| fontFamily | [Resource](../../common-definitions/basic-types/document.md#resource) | string | No | Yes | Font family. The 'HarmonyOS Sans' font and [registered custom fonts](../../../arkts-api/ui/ohos-font-custom-font-registration/document.md) are supported. |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Background color of the button. |
| borderRadius | [Length](../../common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | No | Yes | Corner radius of the button. |
| primary | boolean | No | Yes | 
Whether the button responds to the **Enter** key by default when the dialog box is displayed and the **Tab** key is not used for sequential focus navigation.

**true**: After the dialog box is displayed and the **Tab** key is not used for sequential focus navigation, pressing the **Enter** key triggers the event bound to the button.

**false**: After the dialog box is displayed and the **Tab** key is not used for sequential focus navigation, pressing the **Enter** key does not trigger the event bound to the button.

Default value: **false**.

 |

#### DateRange19+

Defines the date range, which specifies the start and end dates.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | Date | No | Yes | Start date of the date range. |
| end | Date | No | Yes | End date of the date range. |
