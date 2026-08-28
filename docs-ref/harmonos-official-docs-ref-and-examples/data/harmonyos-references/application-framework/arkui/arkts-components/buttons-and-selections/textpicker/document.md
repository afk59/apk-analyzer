# TextPicker

**TextPicker** is a component that allows users to select text, images, or hybrid content through scrolling. It supports three usage modes: single-column picker, multi-column independent picker, and multi-column cascading picker.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/I7jvcQfoTBqNKS_SSw7QKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=193608ED8D3F42BDBB826666366D628E748FEE4FBB32EB4537EC8E09EF34D240)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Avoid changing the attribute data during the animation process of this component.
    
-   The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')**.
    
-   Multi-column independent pickers and multi-column cascading pickers are collectively referred to as multi-column pickers in this document.
    

#### Child Components

Not supported

#### APIs

TextPicker(options?: TextPickerOptions)

Creates a text picker based on the specified data list.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TextPickerOptions](#textpickeroptions) | No | Parameters of the text picker. |

#### TextPickerOptions

Defines the configuration options of the text picker.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| range | 
string\[\] | string\[\]\[\]10+ | [Resource](../../common-definitions/basic-types/document.md#resource) |

[TextPickerRangeContent](#textpickerrangecontent10)\[\]10+ | [TextCascadePickerRangeContent](#textcascadepickerrangecontent10)\[\]10+

 | No | No | 

Data selection range of the picker. This parameter cannot be set to an empty array. If set to an empty array, it will not be displayed. If it is dynamically changed to an empty array, the current value remains displayed.

**NOTE**

1\. Single-column pickers: string\[\], [Resource](../../common-definitions/basic-types/document.md#resource), or [TextPickerRangeContent](#textpickerrangecontent10)\[\]

2\. Multi-column independent pickers: string\[\]\[\]

3\. Multi-column cascading pickers: [TextCascadePickerRangeContent](#textcascadepickerrangecontent10)\[\]

4\. The Resource type supports only [strarray.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#resource-group-directories).

5\. The type and number of columns in the range cannot be dynamically modified.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selected | number | number\[\]10+ | No | Yes | 

Index of the selected item in the data list. The index is zero-based.

Default value: **0**.

**NOTE**

1\. Single-column pickers: number

2\. Multi-column pickers: number\[\]

3\. Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)\[\] | No | Yes | 

Value of the selected item. The priority of this parameter is lower than that of **selected**.

Default value: value of the first item in the data list.

**NOTE**

1\. Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

2\. The [Resource](../../common-definitions/basic-types/document.md#resource) type is supported since API version 20.

3\. This parameter works only when the picker contains text only. It does not work when the picker contains images or mixed content.

4\. Single-column pickers: [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)

5\. Multi-column pickers: [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)\[\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| columnWidths18+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\[\] | No | Yes | 

Custom widths for each column.

Default value: Each column has equal width, calculated by dividing the total component width by the number of columns.

**NOTE**

1\. Text truncation occurs when content exceeds column width.

2\. Invalid values are treated as the default value.

3\. Individual array elements can be **Undefined** or **Null**, but the entire array cannot be **Undefined\[\]** or **Null\[\]**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### TextPickerRangeContent10+

Defines the content for single-column picker options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | Image resource. If the value is a string, such as **"/common/hello.png"**, it represents the path to the image. |
| text | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Text information.

An empty character string is used by default.

Note: Text truncation occurs when content exceeds column width.

 |

#### TextCascadePickerRangeContent10+

Defines the content for multi-column picker options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 
Text information.

Note: Text truncation occurs when content exceeds column width.

 |
| children | [TextCascadePickerRangeContent](#textcascadepickerrangecontent10)\[\] | No | Yes | Linkage data. |

#### DividerOptions12+

Define the divider configuration options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 
Stroke width of the divider.

Default value: **2.0px**.

Unit: vp (default) or px.

If the value is less than 0, the default value is used. The maximum value allowed is half the height of the column. Percentages are not supported.

 |
| startMargin | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Distance between the divider and the start edge of the text picker.

Default value: **0**.

Unit: vp (default) or px.

Values less than 0 are invalid. The maximum value allowed is the width of the column. Percentages are not supported.

 |
| endMargin | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Distance between the divider and the end edge of the text picker.

Default value: **0**.

Unit: vp (default) or px.

Values less than 0 are invalid. The maximum value allowed is the width of the column. Percentages are not supported.

 |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the divider.

Default value: **'#33000000'**

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]defaultPickerItemHeight

defaultPickerItemHeight(value: number | string)

Sets the height of the picker items.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Height of the picker items.

Value range:

**number** type: \[0, +∞), in vp.

**string** type: numeric string only, for example, **"56"**.

Default value: selected item 56 vp, unselected item 36 vp.

**NOTE**

The set value applies to both selected and unselected items.

 |

#### \[h2\]defaultPickerItemHeight18+

defaultPickerItemHeight(height: Optional<number | string>)

Sets the height of the picker items. Compared with [defaultPickerItemHeight](#defaultpickeritemheight), this API supports the **undefined** type for the **height** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| height | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | string> | Yes | 
Height of the picker items.

Value range:

**number** type: \[0, +∞), in vp.

**string** type: numeric string only, for example, **"56"**.

Default value: selected item 56 vp, unselected item 36 vp.

**NOTE**

1\. The set value applies to both selected and unselected items.

2\. If **height** is set to **undefined**, the previous value is retained.

 |

#### \[h2\]disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

Sets the text color, font size, and font weight of edge items (the second item above or below the selected item).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Text color, font size, and font weight for edge items.

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ll0cU7PJQfuGnHhN2AOzkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C513C80721837158711DB9164EA4F42DE50F2D057CC1BB9A0C3F0A5494F378)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

Sets the text color, font size, and font weight of edge items (the second item above or below the selected item). Compared with [disappearTextStyle10+](#disappeartextstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Text color, font size, and font weight for edge items.

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

If the value of **style** is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/qCX4nNvqRyeXn87yhDryLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=688CBAD4EE2D8E0A7703911FD88B1696507559BF1A26511C7981B27253A1770C)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]disappearTextStyle20+

disappearTextStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

Sets the text style of edge items (the second item above or below the selected item), covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode. Compared with [disappearTextStyle](#disappeartextstyle18)18+, this API supports the [TextPickerTextStyle](#textpickertextstyle15) type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)|[TextPickerTextStyle](#textpickertextstyle15)\> | Yes | 
Text style of edge items, covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode.

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

},

minFontSize: 0,

maxFontSize: 0,

overflow: TextOverflow.Clip

}

If the value of **style** is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/y3ZDarWBSaaW4S4q2vUBGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E48A580E63021501EDD674ED8E7C6E9923BA7027A062D1C581A593864FC347D)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]textStyle10+

textStyle(value: PickerTextStyle)

Sets the text color, font size, and font weight of candidate items (the first item immediately above or below the selected item).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Text color, font size, and font weight for candidate items.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/yA1gYGsTTO2A4nXHGqOhOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3F9883830E62CDDAD9B2545D9FB1580C4A72E9ABA38B174E621BD44D347D6FB)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]textStyle18+

textStyle(style: Optional<PickerTextStyle>)

Sets the text color, font size, and font weight of candidate items (the first item immediately above or below the selected item). Compared with [textStyle10+](#textstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Text color, font size, and font weight for candidate items.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

If the value of **style** is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/QMkp750pShCm-XhyZZS9rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF92E8FB55F30F559BE28ED16959392D12835BA5AA408E6D5AE1D6E65604E475)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]textStyle20+

textStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

Sets the text style of candidate items (the first item immediately above or below the selected item), covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode. Compared with [textStyle](#textstyle18)18+, this API supports the [TextPickerTextStyle](#textpickertextstyle15) type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)|[TextPickerTextStyle](#textpickertextstyle15)\> | Yes | 
Style of candidate items, covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

},

minFontSize: 0,

maxFontSize: 0,

overflow: TextOverflow.Clip

}

If the value of **style** is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/XV1iGPeWSuy1SJqeSOmDWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47BFE4928F216658802EE0FA1958A3F3B85E329513262C021F550036F5B8AC42)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

Sets the text color, font size, and font weight of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior**: This API has no effect on wearables and works on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Text color, font size, and font weight of the selected item.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

 |

#### \[h2\]selectedTextStyle18+

selectedTextStyle(style: Optional<PickerTextStyle>)

Sets the text color, font size, and font weight of the selected item. Compared with [selectedTextStyle10+](#selectedtextstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior**: This API has no effect on wearables and works on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Text color, font size, and font weight of the selected item.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

If the value of **style** is **undefined**, the default value is used.

 |

#### \[h2\]selectedTextStyle20+

selectedTextStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

Sets the text style of the selected item, covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode. Compared with [selectedTextStyle](#selectedtextstyle18)18+, this API supports the [TextPickerTextStyle](#textpickertextstyle15) type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior**: This API has no effect on wearables and works on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)|[TextPickerTextStyle](#textpickertextstyle15)\> | Yes | 
Text style of the selected item, covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

},

minFontSize: 0,

maxFontSize: 0,

overflow: TextOverflow.Clip

}

If the value of **style** is **undefined**, the default value is used.

 |

#### \[h2\]selectedIndex10+

selectedIndex(value: number | number\[\])

Sets the index of the selected item or items in the data list. This setting takes precedence over the **value** property in [TextPickerOptions](#textpickeroptions). Use **number** for single-column pickers. Use **number\[\]** for multi-column pickers.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | number\[\] | Yes | 
Index of the selected item or items in the data list. The index is zero-based.

Default value: **0**.

If the value is negative or exceeds the maximum index, the default value is used.

 |

#### \[h2\]selectedIndex18+

selectedIndex(index: Optional<number | number\[\]>)

Sets the index of the selected item or items in the data list. This setting takes precedence over the **value** property in [TextPickerOptions](#textpickeroptions). Use **number** for single-column pickers. Use **number\[\]** for multi-column pickers. Compared with [selectedIndex10+](#selectedindex10), this API supports the **undefined** type for the **index** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | number\[\]> | Yes | 
Index of the selected item or items in the data list. The index is zero-based.

Default value: **0**.

If **index** is **undefined**, the **selected** value of [TextPickerOptions](#textpickeroptions) is used.

If it is negative or exceeds the maximum index, the default value is used.

 |

#### \[h2\]canLoop10+

canLoop(value: boolean)

Sets whether to enable loop scrolling.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable loop scrolling.

\- **true**: Enable loop scrolling.

\- **false**: Disable loop scrolling.

Default value: **true**.

 |

#### \[h2\]canLoop18+

canLoop(isLoop: Optional<boolean>)

Sets whether to enable loop scrolling. Compared with [canLoop10+](#canloop10), this API supports the **undefined** type for the **isLoop** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLoop | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable loop scrolling.

\- **true**: Enable loop scrolling.

\- **false**: Disable loop scrolling.

Default value: **true**.

If the value of **isLoop** is **undefined**, the default value is used.

 |

#### \[h2\]divider12+

divider(value: DividerOptions | null)

Sets the divider style. If not explicitly set, the divider uses the default style.

If the sum of **startMargin** and **endMargin** in [DividerOptions](#divideroptions12) exceeds the component's width, both margins are automatically reset to 0.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DividerOptions](#divideroptions12) | null | Yes | 
Default value:

{

strokeWidth: '2px',

startMargin: 0,

endMargin: 0,

color: '#33000000'

}

1\. If **textDivider** is a valid [DividerOptions](#divideroptions12) object, the divider is rendered using the specified style.

2\. If **textDivider** is **null**, the divider is hidden.

 |

#### \[h2\]divider18+

divider(textDivider: Optional<DividerOptions | null>)

Sets the divider style. If not explicitly set, the divider uses the default style. Compared with [divider12+](#divider12), this API supports the **undefined** type for the **textDivider** parameter.

If the sum of **startMargin** and **endMargin** in [DividerOptions](#divideroptions12) exceeds the component's width, both margins are automatically reset to 0.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| textDivider | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[DividerOptions](#divideroptions12) | null> | Yes | 
Default value:

{

strokeWidth: '2px',

startMargin: 0,

endMargin: 0,

color: '#33000000'

}

1\. If the value of **textDivider** is **undefined**, the default value is used.

2\. If **textDivider** is a valid [DividerOptions](#divideroptions12) object, the divider is rendered using the specified style.

3\. If **textDivider** is **null**, the divider is hidden.

 |

#### \[h2\]gradientHeight12+

gradientHeight(value: Dimension)

Sets the height of the fade effect applied to the top and bottom edges of the content area. If no setting is specified, a default fade effect is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | Yes | 
Height of the fade effect.

Default value: **36vp**.

Value range: \[0, +∞). Percentages are supported.

**NOTE**

1\. If the value is set to a percentage, **100%** equals half the height of the text picker.

2\. A value of **0** disables the fade effect.

3\. Values exceeding half the height of the text picker revert to the default value.

4\. If the value is **undefined** or negative, the default value is used.

 |

#### \[h2\]gradientHeight18+

gradientHeight(height: Optional<Dimension>)

Sets the height of the fade effect applied to the top and bottom edges of the content area. If no setting is specified, a default fade effect is used. Compared with [gradientHeight12+](#gradientheight12), this API supports the **undefined** type for the **height** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| height | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Dimension](../../common-definitions/basic-types/document.md#dimension10)\> | Yes | 
Height of the fade effect.

Default value: **36vp**.

Value range: \[0, +∞). Percentages are supported.

**NOTE**

1\. If the value is set to a percentage, **100%** equals half the height of the text picker.

2\. A value of **0** disables the fade effect.

3\. Values exceeding half the height of the text picker revert to the default value.

4\. If the value is **undefined** or negative, the default value is used.

 |

#### \[h2\]disableTextStyleAnimation15+

disableTextStyleAnimation(disabled: boolean)

Sets whether to disable the animation effect of text style changes during scrolling.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| disabled | boolean | Yes | 
Whether to disable the animation effect of text style changes during scrolling.

\- **true**: Disable the animation effect of text style changes.

\- **false**: Do not disable the animation effect of text style changes.

Default value: **false**.

**NOTE**

When this API is used with **true**, there are no text style changes, including the font size, weight, and color, during scrolling, and all text is displayed in the style set by [defaultTextStyle](#defaulttextstyle15). If [defaultTextStyle](#defaulttextstyle15) is not set, the default style of the [Text](../../text-and-input/text/document.md) component is used.

 |

#### \[h2\]defaultTextStyle15+

defaultTextStyle(style: TextPickerTextStyle)

Sets the text style of the items when the text style change animation during the scrolling process is disabled. This setting takes effect only when [disableTextStyleAnimation](#disabletextstyleanimation15) is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [TextPickerTextStyle](#textpickertextstyle15) | Yes | 
Text style of the items when the text style change animation during the scrolling process is disabled.

Default value: same as the default value of the [Text](../../text-and-input/text/document.md) component

 |

To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[
   {
      "name": "ohos.permission.VIBRATE",
   }
\]

#### \[h2\]enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

Sets whether to enable haptic feedback.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**.

Whether this parameter takes effect after being set to **true** depends on hardware support.

 |

To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[
   {
      "name": "ohos.permission.VIBRATE",
   }
\]

#### \[h2\]digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

Sets the sensitivity to the digital crown rotation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sensitivity | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[CrownSensitivity](../../common-definitions/enums/document.md#crownsensitivity18)\> | Yes | 
Sensitivity to the digital crown rotation.

Default value: **CrownSensitivity.MEDIUM**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IrEP1YQsQXCZHV8VoAFw0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A98AA849CEDE1DFCBE3C8D28EDDEE2B3C43716213D474CEC2595A1D8994FF974)

This API is used for circular screens on wearables. The component needs to obtain focus before responding to the [crown event](../../universal-events/basic-input-events/crown-event/document.md).

#### \[h2\]selectedBackgroundStyle20+

selectedBackgroundStyle(style: Optional<PickerBackgroundStyle>)

Sets the background style of selected items.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerBackgroundStyle](#pickerbackgroundstyle20)\> | Yes | 
Background color and corner radius for selected items. Applies to all columns in multi-column mode.

Default value:

{

color: $r('sys.color.comp\_background\_tertiary'),

borderRadius: $r('sys.float.corner\_radius\_level12')

}

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: (value: string | string\[\], index: number | number\[\]) => void)

Triggered when the text picker snaps to the selected item. This event cannot be triggered by two-way bound state variables. When the picker contains text only or a combination of images and text, **value** indicates the text of the selected item. When the picker contains images only, **value** is empty.

This callback is triggered only after the scroll animation completes. To obtain real-time index changes, use [onEnterSelectedArea](#onenterselectedarea18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | string\[\]10+ | Yes | Text of the selected item. The value of the multi-column data selector is of the array type. |
| index | number | number\[\]10+ | Yes | Index of the selected item. The index is zero-based. Use the array type for multi-column pickers. |

#### \[h2\]onChange18+

onChange(callback: Optional<OnTextPickerChangeCallback>)

Triggered when the text picker snaps to the selected item. This event cannot be triggered by two-way bound state variables. When the picker contains text only or a combination of images and text, **value** indicates the text of the selected item. When the picker contains images only, **value** is empty. Compared with [onChange](#onchange), the **callback** parameter supports the **undefined** type.

This callback is triggered only after the scroll animation completes. To obtain real-time index changes, use [onEnterSelectedArea](#onenterselectedarea18) instead.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnTextPickerChangeCallback](#ontextpickerchangecallback18)\> | Yes | 
Callback invoked when an item in the picker is selected.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### \[h2\]onScrollStop14+

onScrollStop(callback: TextPickerScrollStopCallback)

Triggered when the scrolling in the text picker stops.

If the scrolling is initiated by a gesture, this event is triggered when the finger is lifted from the screen and the scrolling stops.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/qJiJ2xCVQteQq0iDoaRS0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E05F1460E07685930F87E131A2B8A5F34891B3A91CE77525CB59497A9CFE444)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [TextPickerScrollStopCallback](#textpickerscrollstopcallback14) | Yes | Triggered when the scrolling in the text picker stops. |

#### \[h2\]onScrollStop18+

onScrollStop(callback: Optional<TextPickerScrollStopCallback>)

Triggered when the scrolling in the text picker stops. Compared with [onScrollStop14+](#onscrollstop14), this API supports the **undefined** type for the **callback** parameter.

If the scrolling is initiated by a gesture, this event is triggered when the finger is lifted from the screen and the scrolling stops.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/ZBUvjfTOTbmi19Q6gUExIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=454F32AFD8E124E0133CC63750161D93AFFA1A1CF8BAA60C63927244DEAD205E)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[TextPickerScrollStopCallback](#textpickerscrollstopcallback14)\> | Yes | 
Triggered when the scrolling in the text picker stops.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### \[h2\]onEnterSelectedArea18+

onEnterSelectedArea(callback: TextPickerEnterSelectedAreaCallback)

Triggered when an option enters the selection zone during text picker scrolling (when the scroll distance exceeds half the selected item's height).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/xgM2UALxRneNi4V9uG4f0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C7D8A5F01E59A88E71125A6D27081B43D1BA93F01C72045888034BFF4140FE8)

-   This event is triggered earlier than the [onChange](#onchange) event.
    
-   In scenarios where the picker contains linked columns, the use of this callback is not recommended. The reason is that it identifies nodes where items enter the divider area during scrolling. However, items that change in response to the scrolling do not themselves scroll. As a result, the callback's return values will only reflect changes for the currently scrolling column, while other non-scrolling columns will remain unchanged.
    
-   This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [TextPickerEnterSelectedAreaCallback](#textpickerenterselectedareacallback18) | Yes | Callback triggered when an option enters the selection zone during text picker scrolling. |

#### \[h2\]onAccept(deprecated)

onAccept(callback: (value: string, index: number) => void)

Triggered when the OK button in the dialog box is clicked. This event can be triggered only in the [text picker dialog box](../../dialog-boxes/text-picker-dialog-box-textpickerdialog/document.md).

This API is supported since API version 8 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text of the selected item. |
| index | number | Yes | Index of the selected item. The index is zero-based. |

#### \[h2\]onCancel(deprecated)

onCancel(callback: () => void)

Triggered when the Cancel button in the dialog box is clicked. This event can be triggered only in the [text picker dialog box](../../dialog-boxes/text-picker-dialog-box-textpickerdialog/document.md).

This API is supported since API version 8 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Triggered when the Cancel button in the dialog box is clicked. |

#### TextPickerTextStyle15+

Defines the text style options for the text picker. Inherits from [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minFontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | Minimum font size for the text. Used with **maxFontSize** to enable font scaling. When both **minFontSize** and **maxFontSize** are set, the **size** property in **font** is ignored. By default, the maximum number of lines is 1, with the **MIN\_FONT\_SIZE\_FIRST** adaptation strategy. For details, see [minFontSize](../../text-and-input/text/document.md#minfontsize). |
| maxFontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | Maximum font size for the text. For details, see [maxFontSize](../../text-and-input/text/document.md#maxfontsize). |
| overflow | [TextOverflow](../../common-definitions/enums/document.md#textoverflow) | No | Yes | Text overflow behavior. This property has no effect when set to **MARQUEE**. For details, see [textOverflow](../../text-and-input/text/document.md#textoverflow). |

#### OnTextPickerChangeCallback18+

type OnTextPickerChangeCallback = (selectItem: string | string\[\], index: number | number\[\]) => void

Defines the **onChange** event callback signature.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectItem | string | string\[\]10+ | Yes | 
Text of the selected item. Use the array type for multi-column pickers.

**NOTE**

The return value is a text value for text or mixed content, and an empty string for image-only content.

 |
| index | number | number\[\]10+ | Yes | Index of the selected item. The index is zero-based. Use the array type for multi-column pickers. |

#### TextPickerScrollStopCallback14+

type TextPickerScrollStopCallback = (value: string | string\[\], index: number | number\[\]) => void

Defines the **onScrollStop** event callback signature.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | string\[\] | Yes | 
Text of the selected item. Use the array type for multi-column pickers.

**NOTE**

The return value is a text value for text or mixed content, and an empty string for image-only content.

 |
| index | number | number\[\] | Yes | Index of the selected item. The index is zero-based. Use the array type for multi-column pickers. |

#### TextPickerEnterSelectedAreaCallback18+

type TextPickerEnterSelectedAreaCallback = (value: string | string\[\], index: number | number\[\]) => void

Defines the **onEnterSelectedArea** event callback signature.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | string\[\] | Yes | 
Text of the selected item. Use the array type for multi-column pickers.

**NOTE**

The return value is a text value for text or mixed content, and an empty string for image-only content.

 |
| index | number | number\[\] | Yes | Index of the selected item. The index is zero-based. Use the array type for multi-column pickers. |

#### PickerBackgroundStyle20+

Defines the background style configuration for selected picker items.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the selected item.

Default value:

'sys.color.comp\_background\_tertiary'

 |
| borderRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../common-definitions/basic-types/document.md#localizedborderradiuses12) | No | Yes | 

Border radius of the selected item.

Default value: **{ value:24, unit:LengthUnit.VP }**, meaning 24 vp for all corners.

**NOTE**

1\. [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12): uniform radius with a customizable unit

2\. [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9): per-corner radius values (vp units only)

3\. [LocalizedBorderRadiuses](../../common-definitions/basic-types/document.md#localizedborderradiuses12): per-corner radius values with individual units

 |

#### Example

## Example 1: Setting the Number of Columns in the Picker

This example demonstrates how to configure single-column and multi-column text pickers by setting **range** and customizing the width of each column using **columnWidths**.

The **columnWidths** attribute of [TextPickerOptions](#textpickeroptions) is added since API version 18.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

class Bottom {
  bottom: number = 50;
}

let bott: Bottom = new Bottom();
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private apfruits: string\[\] = \['apple1', 'apple2', 'apple3', 'apple4'\];
  private orfruits: string\[\] = \['orange1', 'orange2', 'orange3', 'orange4'\];
  private pefruits: string\[\] = \['peach1', 'peach2', 'peach3', 'peach4'\];
  private multi: string\[\]\[\] = \[this.apfruits, this.orfruits, this.pefruits\];
  private cascade: TextCascadePickerRangeContent\[\] = \[
    {
      text: 'Liaoning Province',
      children: \[{ text: 'Shenyang', children: \[{ text: 'Shenhe District' }, { text: 'Heping District' }, { text: 'Hunnan District' }\] },
        { text: 'Dalian', children: \[{ text: 'Zhongshan District' }, { text: 'Jinzhou District' }, { text: 'Changhai County' }\] }\]
    },
    {
      text: 'Jilin Province',
      children: \[{ text: 'Changchun', children: \[{ text: 'Nanguan District' }, { text: 'Kuancheng District' }, { text: 'Chaoyang District' }\] },
        { text: 'Siping', children: \[{ text: 'Tiexi District' }, { text: 'Tiedong District' }, { text: 'Lishu County' }\] }\]
    },
    {
      text: 'Heilongjiang Province',
      children: \[{ text: 'Harbin', children: \[{ text: 'Daoli District' }, { text: 'Daowai District' }, { text: 'Nangang District' }\] },
        { text: 'Mudanjiang', children: \[{ text: \`Dong'an District\` }, { text: \`Xi'an District\` }, { text: 'Aimin District' }\] }\]
    }
  \];
  private singleColumnWidths: LengthMetrics\[\] = \[
    LengthMetrics.percent(50)
  \];

  private multipleColumnWidths: LengthMetrics\[\] = \[
    LengthMetrics.vp(100),
    LengthMetrics.vp(200),
    LengthMetrics.vp(100)
  \];

  private cascadeColumnWidths: LengthMetrics\[\] = \[
    LengthMetrics.percent(20),
    LengthMetrics.percent(30),
    LengthMetrics.percent(50)
  \];
  build() {
    Column() {

      TextPicker({ range: this.apfruits, selected: this.select, columnWidths: this.singleColumnWidths })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        }).margin(bott)
        .onEnterSelectedArea((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item enter selected area, value: ' + value + ', index: ' + index);
        })

      TextPicker({ range: this.multi, columnWidths: this.multipleColumnWidths })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('TextPicker multi-column: onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('TextPicker multi-column: onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        }).margin(bott)
        .onEnterSelectedArea((value: string | string\[\], index: number | number\[\]) => {
          console.info('TextPicker multi-column: onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })

      TextPicker({ range: this.cascade, columnWidths: this.cascadeColumnWidths })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('TextPicker multi-column cascading: onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('TextPicker multi-column cascading: onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
        .onEnterSelectedArea((value: string | string\[\], index: number | number\[\]) => {
          console.info('TextPicker multi-column cascading: onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/cet0uXaqStqwgHT1SIRO4Q/en-us_image_0000002568765335.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=734B38867858F1EE44700672666525C2E2ADDE3A5B40FD3FE14B77F3777B3082)

## Example 2: Setting the Text Style

This example demonstrates how to configure [disappearTextStyle](#disappeartextstyle10), [textStyle](#textstyle10), and [selectedTextStyle](#selectedtextstyle10) to customize the text style in the text picker.

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits\[this.select\]
      })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
        .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
        .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
        .defaultPickerItemHeight(50)
        .canLoop(false)
        .selectedIndex(2)
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/tG_2rfiMS-qNp_GzwT1N6g/en-us_image_0000002537765610.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE01BFE0209D53FE1852BF6737126D28CC670BA08C5D5EE13B584C3706065B05)

## Example 3: Using the No-Divider Style

This example demonstrates how to configure a text picker with no divider by setting [divider](#divider12) to **null**.

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
        .divider(null)
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/-xwUcuRISguALGGVDrrx-A/en-us_image_0000002537925550.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96B82F01E267419FCA7CFF5A9842B49059179809A4743E63E30236D4A4D0C04C)

## Example 4: Using the Divider Style

This example demonstrates how to set the divider style for the text picker by configuring **DividerOptions** for **divider**.

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
        .divider({
          strokeWidth: 10,
          color: Color.Red,
          startMargin: 10,
          endMargin: 20
        } as DividerOptions)
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/tv2l0JkhSw-nWYJKQmuV5g/en-us_image_0000002568685327.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF33BA885EBBD1B5D047BE97CF7F2C366058DC6E1FAA0DE4594794451D020970)

## Example 5: Setting the Fade Effect

This example shows how to set the gradient effect height for the text picker by configuring [gradientHeight](#gradientheight12).

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
        .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
        .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
        .gradientHeight(100)
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/B03_KmSBRKuAAEQbDXbk6w/en-us_image_0000002568765337.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9071C5084FDE40D0FA79E7AA92B7435321023E7EFBA7901E97BDC26D690AA256)

## Example 6: Setting the Item Height

This example demonstrates how to set the height of the picker items by configuring [defaultPickerItemHeight](#defaultpickeritemheight).

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .defaultPickerItemHeight(60)
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/FIxJwvlqRG-lsAtaWikLwQ/en-us_image_0000002537765612.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26FA57C4913C88CD98E9F5C9ED57C136A50C5429EA422532B24C895AD64C8F75)

## Example 7: Setting Loop Scrolling

This example demonstrates how to set whether to enable loop scrolling using [canLoop](#canloop10).

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  @State isLoop: boolean = false;
  private select: number = 1;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: this.select })
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
        .canLoop(this.isLoop)

      Row() {
        Text('Loopable scrolling').fontSize(20)

        Toggle({ type: ToggleType.Switch, isOn: false })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })

    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/sYRf9kzvSY-ADH66CxkC8g/en-us_image_0000002537925552.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB8B0C7746CD82FB6E8D9AB9715C26FB349A010C3833BD7340314B8A36A96293)

## Example 8: Setting the Selected Item Index

This example demonstrates how to set the index of the default selected item by configuring [selectedIndex](#selectedindex10).

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4'\];

  build() {
    Column() {
      TextPicker({ range: this.fruits, selected: 1 })
        .selectedIndex(2)
        .onChange((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker item changed, value: ' + value + ', index: ' + index);
        })
        .onScrollStop((value: string | string\[\], index: number | number\[\]) => {
          console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
        })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/2hxkZ6fNRlyl63BVLpqWwg/en-us_image_0000002568685329.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F754676B39954AE85F748C1CA3DC25065F9E71C928E309812A5942C55CB527F)

## Example 9: Disabling the Text Style Animation and Setting the Corresponding Text Style

This example demonstrates how to disable the text style change animation for the text picker and set the text style by configuring [disableTextStyleAnimation](#disabletextstyleanimation15) and [defaultTextStyle](#defaulttextstyle15).

The **disableTextStyleAnimation** and **defaultTextStyle** APIs are supported since API version 15.

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private select: number = 1;
  private fruits: string\[\] = \['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'\];

  build() {
    Column() {
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits\[this.select\]
      })
        .disableTextStyleAnimation(true)
        .margin({ bottom: 30 })
      TextPicker({
        range: this.fruits,
        selected: this.select,
        value: this.fruits\[this.select\]
      })
        .disableTextStyleAnimation(true)
        .defaultTextStyle({ minFontSize: 18, maxFontSize: 28, overflow: TextOverflow.Ellipsis })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/nmit0VBZROuXYMCgtOxx8g/en-us_image_0000002568765339.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=364A221AB731BF452A66D90453F993F6318F56BFD6935C95D97CB4DC43B60D09)

## Example 10: Setting the Background Style of the Selected Item

This example shows how to set the background style of the selected item by configuring [selectedBackgroundStyle](#selectedbackgroundstyle20).

import { LengthUnit } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private showText1: string \[\] =
    \['Text1', 'Text1', 'Text1', 'Text1'\]
  private showText2: string\[\] \[\] =
    \[
      \['Text2', 'Text2', 'Text2', 'Text2'\],
      \['Text3', 'Text3', 'Text3', 'Text3'\]
  \]

  build() {
    Column() {
      Row() {
        TextPicker({ range: this.showText1 })
          .selectedBackgroundStyle({
            color: '#FFD5D5D5',
            borderRadius: { value: 0, unit: LengthUnit.VP }
          })
        Column()
          .width('10%')
        TextPicker({ range: this.showText1 })
          .selectedBackgroundStyle({
            color: '#FFE3F8F9',
            borderRadius: {
              topStart: { value: 5, unit: LengthUnit.VP },
              topEnd: { value: 10, unit: LengthUnit.VP },
              bottomStart: { value: 15, unit: LengthUnit.VP },
              bottomEnd: { value: 20, unit: LengthUnit.VP },
            }
          })
      }

      Row()
        .height('10%')
      Row() {
        TextPicker({ range: this.showText2 })
          .selectedBackgroundStyle({
            borderRadius: {
              topLeft: 8,
              topRight: 8,
              bottomLeft: 8,
              bottomRight: 8
            },
            color: '#FFFFEEF6'
          })
      }
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/f9eYSTcNTYyVtL2P82TNUg/en-us_image_0000002537765614.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4986C8EBD954B33B38904C0AE0D0654337F25B7FDB413C1C4AB93532B68F9801)

## Example 11: Setting the Font Size Range and Text Overflow Mode

This example shows how to set the text color, maximum font size, minimum font size, and text overflow mode by configuring [disappearTextStyle](#disappeartextstyle20), [textStyle](#textstyle20), and [selectedTextStyle](#selectedtextstyle20).

The **disappearTextStyle**, **textStyle**, and **selectedTextStyle** APIs are supported since API version 20.

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private rangeValue: string\[\] = \['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEEEEEEEEEEEEEE'\];

  build() {
    RelativeContainer() {
      TextPicker({
        range: this.rangeValue
      })
        .disappearTextStyle({
          color: '#fff52769',
          // If minFontSize and maxFontSize are set, the size property in font is ignored.
          font: { size: 50 },
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.Ellipsis
        })
        .textStyle({
          color: Color.Orange,
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.MARQUEE
        })
        .selectedTextStyle({
          color: '#ff9eea48',
          minFontSize: 12,
          maxFontSize: 18,
          overflow: TextOverflow.Clip
        })
        .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/EbIdTYRrQeq26HdU-gSasQ/en-us_image_0000002537925554.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5177191E62ADED08FEF188101FD3A8A2D12F11E4C8AF805A435A62D6A6F5D2B5)
