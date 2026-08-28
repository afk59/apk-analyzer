# GridRow

The responsive grid layout provides rules for layout design and resolves issues of dynamic layout across devices with different sizes, thereby ensuring layout consistency across layouts on different devices.

The **GridRow** component is used in a grid layout, together with its child component [GridCol](../gridcol/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/2Zo-TJdXQA2vyfvlzy4DDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=821A26210086D25261283886A4BEABDA1F243E84FB8178D85E62FA4F6ED1FB50)

This component is supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component can contain the **GridCol** child component.

#### APIs

GridRow(option?: GridRowOptions)

Creates a **GridRow** container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [GridRowOptions](#gridrowoptions) | No | Child component options of the grid layout. |

#### GridRowOptions

Defines layout options of the **GridRow** container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| columns | number | [GridRowColumnOption](#gridrowcolumnoption) | No | Yes | 
Number of columns in the grid layout.

The value is an integer greater than 0.

\- Before API version 20: The default value is 12.

\- API version 20 or later: The default value is { xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }.

Invalid values are treated as the default value.

 |
| gutter | [Length](../../common-definitions/basic-types/document.md#length) | [GutterOption](#gutteroption) | No | Yes | 

Gutter of the grid layout.

Default value: **0**

Invalid values are treated as the default value.

Unit: vp.

 |
| breakpoints | [BreakPoints](#breakpoints) | No | Yes | 

Array of breakpoint values and the corresponding reference based on the application window or container size.

Default value:

{

value: \["320vp", "600vp", "840vp"\],

reference: BreakpointsReference.WindowSize

}

Invalid values are treated as the default value.

Unit: vp.

 |
| direction | [GridRowDirection](#gridrowdirection) | No | Yes | 

Arrangement direction of the grid layout.

Default value: **GridRowDirection.Row**

Invalid values are treated as the default value.

 |

#### GutterOption

Provides the gutter options for the grid layout to define the spacing between child components in different directions.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | [Length](../../common-definitions/basic-types/document.md#length) | [GridRowSizeOption](#gridrowsizeoption) | No | Yes | Horizontal spacing between grid child components. |
| y | [Length](../../common-definitions/basic-types/document.md#length) | [GridRowSizeOption](#gridrowsizeoption) | No | Yes | Vertical spacing between grid child components. |

#### GridRowColumnOption

Describes the numbers of grid columns for devices with different grid sizes.

In versions earlier than API version 20: When **GridRow** column spans are configured only at specific breakpoints, unconfigured breakpoints inherit values from the next smaller configured breakpoint. If no smaller breakpoint exists, the default column count (12) is used for unconfigured breakpoints.

columns: {xs:2, md:4, lg:8} // Equivalent to columns: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}.
columns: {md:4, lg:8} // Equivalent to columns: {xs:12, sm:12, md:4, lg:8, xl:8, xxl:8}.

Since API version 20: When **GridRow** column spans are configured only at specific breakpoints, unconfigured breakpoints inherit values from the next smaller configured breakpoint. If no smaller breakpoint exists, values are inherited from the next larger configured breakpoint.

columns: {xs:2, md:4, lg:8} // Equivalent to columns: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}.
columns: {md:4, lg:8} // Equivalent to columns: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8}.

Recommendation: Explicitly configure **GridRow** column spans for all required breakpoints to prevent unexpected layout behavior caused by automatic value inheritance.

The width of each column is the content area size of the **GridRow** component minus the gutter of the grid child components, and then divided by the total number of columns. For example, if **columns** is set to **12**, **gutter** is set to **10px**, and **padding** is set to **20px** for a **GridRow** component with a width of 800 px, the width of each column is (800 – 20 × 2 – 10 × 11)/12.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| xs | number | No | Yes | Number of grid columns on the device where the grid size is xs. |
| sm | number | No | Yes | Number of grid columns on the device where the grid size is sm. |
| md | number | No | Yes | Number of grid columns on the device where the grid size is md. |
| lg | number | No | Yes | Number of grid columns on the device where the grid size is lg. |
| xl | number | No | Yes | Number of grid columns on the device where the grid size is xl. |
| xxl | number | No | Yes | Number of grid columns on the device where the grid size is xxl. |

#### GridRowSizeOption

Describes the gutter sizes for different device width types.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| xs | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Gutter size for minimum device width.

Default value: **0vp**

 |
| sm | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Gutter size for small device width.

Default value: **0vp**

 |
| md | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Gutter size for medium device width.

Default value: **0vp**

 |
| lg | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Gutter size for large device width.

Default value: **0vp**

 |
| xl | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Gutter size for extra large device width.

Default value: **0vp**

 |
| xxl | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Gutter size for extra extra large device width.

Default value: **0vp**

 |

#### BreakPoints

Sets breakpoints for the responsive grid container. For details about breakpoints, see [Breakpoints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | Array<string> | No | Yes | 
Array of monotonically increasing breakpoints.

Default value: **\["320vp", "600vp", "840vp"\]**

Invalid values are treated as the default value.

Unit: vp.

 |
| reference | [BreakpointsReference](#breakpointsreference) | No | Yes | 

Breakpoint switching reference.

Default value: **BreakpointsReference.WindowSize**

Invalid values are treated as the default value.

 |

  // Enable the xs, sm, and md breakpoints.
  breakpoints: {value: \['100vp', '200vp'\]}
  // Enable four breakpoints: xs, sm, md, and lg. The breakpoint range must be monotonically increasing.
  breakpoints: {value: \['320vp', '600vp', '840vp'\]}
  // Enable five breakpoints: xs, sm, md, lg, and xl. The number of breakpoint ranges cannot exceed the number of breakpoints minus 1.
  breakpoints: {value: \['320vp', '600vp', '840vp', '1080vp'\]}

#### BreakpointsReference

Breakpoint reference of the grid container component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| WindowSize | The window is used as a reference. |
| ComponentSize | The container is used as a reference. |

#### GridRowDirection

Grid element arrangement direction.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/e7VLoK9rTBiaF8PCRResXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F7327651DE7D4160220E9E3ED0854496EA8CBD65F50AC2D260776E234E8D834)

-   Grid elements can be arranged only in the **Row** or **RowReverse** direction, but not in the **Column** or **ColumnReverse** direction.
    
-   The location and size of a grid child component can be calculated only based on **span** and **offset**. If the **span** values of child components add up to a number greater than the allowed number of columns, the grid will automatically wrap lines.
    
-   If the **span** value of a single child component exceeds the maximum number of columns, the maximum number of columns is used.
    
-   If a child component takes up more than the total number of columns according to its **offset** and **span** settings, it will be placed in a new row.
    
-   Example: Item1: GridCol({ span: 6 }), Item2: GridCol({ span: 8, offset:11 })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/QcZbX_FIQpqp4TsyTpJhkg/en-us_image_0000002537765508.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED6829F1DAD17E933EC019839FCE88FA59F43519DD24B4D610FB4E229BEC93A3)
    

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Row | 0 | Grid elements are arranged in the row direction. |
| RowReverse | 1 | Grid elements are arranged in the reverse row direction. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]alignItems10+

alignItems(value: ItemAlign)

Sets the alignment mode of the **GridCol** components along the vertical main axis of the **GridRow** component. The alignment mode of the **GridCol** component can also be set using **alignSelf([ItemAlign](../../common-definitions/enums/document.md#itemalign))**. If both of the preceding methods are used, the setting of **alignSelf(ItemAlign)** prevails.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ItemAlign](../../common-definitions/enums/document.md#itemalign) | Yes | 
Alignment mode of the **GridCol** components along the vertical main axis of the **GridRow** component.

Default value: **ItemAlign.Start**

Invalid values are treated as the default value.

**NOTE**

**ItemAlign** supports the following enums: **ItemAlign.Start**, **ItemAlign.Center**, **ItemAlign.End**, and **ItemAlign.Stretch**.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onBreakpointChange

onBreakpointChange(callback: (breakpoints: string) => void)

Triggered when the breakpoint changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/wpqd7u-CSt2BLJwt3q1Xeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BA36FB0477140F590B0CF2DD4C7CEF186AA2364AF75EC4DCEBD2BCC5C155EA2)

-   When [breakpointsreference](#breakpointsreference) is set to **BreakpointsReference.ComponentSize**, you are not advised to dynamically change the [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) or [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin) attribute value of the **GridRow** component in the **onBreakpointChange** callback.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (breakpoints: string) => void | Yes | Breakpoint change. The value can be **"xs"**, **"sm"**, **"md"**, **"lg"**, **"xl"**, or **"xxl"**. |

#### Example

## Example 1: Basic Usage of Grid Layout

This example demonstrates the basic usage of the **GridRow** component.

// xxx.ets
@Entry
@Component
struct GridRowExample {
  @State bgColors: Color\[\] = \[Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown\]
  @State currentBp: string = 'unknown'

  build() {
    Column() {
      GridRow({
        columns: 5,
        gutter: { x: 5, y: 10 },
        breakpoints: { value: \['400vp', '600vp', '800vp'\],
          reference: BreakpointsReference.WindowSize },
        direction: GridRowDirection.Row
      }) {
        ForEach(this.bgColors, (color: Color) => {
          GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 }, offset: 0, order: 0 }) {
            Row().width('100%').height('20vp')
          }.borderColor(color).borderWidth(2)
        })
      }.width('100%').height('100%')
      .onBreakpointChange((breakpoint) => {
        this.currentBp = breakpoint
      })
    }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height(200)
    .border({ color: '#880606', width: 2 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/oMj_IGT2RQWqwX6AfvETGg/en-us_image_0000002537925448.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A605392D3582F589F90BEC6584E7D339C0D2863CFAB6140ECC2AF1EB7B8DCA08)

## Example 2: Basic Usage of AlignItems

This example demonstrates the effect of the **GridCol** component in different **alignItems** alignment modes.

@ComponentV2
struct AlignItemsDemo {
  bgColors: Color\[\] = \[Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink\];
  @Param alignment: ItemAlign = ItemAlign.Start; // Receive the alignItems attribute value passed from the parent component.

  ToString(alignment: ItemAlign): string {
    switch (alignment) {
      case ItemAlign.Start:
        return "ItemAlign.Start";
      case ItemAlign.Center:
        return "ItemAlign.Center";
      case ItemAlign.End:
        return "ItemAlign.End";
      case ItemAlign.Stretch:
        return "ItemAlign.Stretch";
      default:
        return "ItemAlign.Auto";
    }
  }

  build() {
    Column() {
      Text(this.ToString(this.alignment))
        .fontSize(9)
        .fontColor(0xCCCCCC)
        .width('90%')
        .alignSelf(ItemAlign.Start)
      GridRow({
        columns: 5,
        gutter: { x: 5, y: 10 },
      }) {
        ForEach(this.bgColors, (color: Color, index: number) => {
          GridCol({ span: 1 }) {
            Row() {
            }.width('100%').height(\`${(index + 1) \* 20}%\`) // Set different heights for GridCol to facilitate observing the effect of the alignItems attribute.
          }.borderColor(color).borderWidth(2)
        })
      }
      .border({ color: '#880606', width: 2 })
      .alignItems(this.alignment)
      .width('100%')
    }
    .height("20%")
  }
}

@Entry
@ComponentV2
struct GridRowExample {
  alignmentArray: ItemAlign\[\] = \[ItemAlign.Start, ItemAlign.Center, ItemAlign.End, ItemAlign.Stretch\];

  build() {
    Column({ space: 15 }) {
      ForEach(this.alignmentArray, (ele: ItemAlign) => {
        AlignItemsDemo({ alignment: ele })
      })
    }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/X31ew9Z5Q5aHjor8TkQlbw/en-us_image_0000002568685225.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AACED4B8B08620A58F8A1F183707FB4648060B166F7262DEC52B94BF899A899F)
