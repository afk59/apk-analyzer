# Sizing

The sizing attributes set the width, height, and margins of a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/w78kgp6tRVCg-ZMubJTndw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1ED1E4443DD0A1073483188EFC05A203FCD2393116D2CAE49D27E9F49DCB6FA)

-   The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   When a component's size is set by percentage, the actual size is calculated based on the size of the nearest ancestor node with a fixed size.
    
-   Since API version 10, some internal properties related to size setting support the calc calculation feature. For specific supported properties, see the corresponding property description. The calc calculation feature is a function for dynamically computing length values, commonly used to flexibly set layout dimensions (such as width, height, margins, etc.). It allows combining different units and values through mathematical expressions, and supports the use of operators (addition, subtraction, multiplication, division, and parentheses) to form calculation expressions to achieve dynamic responsive design. Note that when using calc, spaces must be used between operators and values. For specific usage scenarios, see [Example 1: Setting the Component Width, Height, Margin, and Padding](#example-1-setting-the-component-width-height-margin-and-padding).
    

#### width

width(value: Length): T

Sets the width of the component. By default, the width required to fully hold the component content is used. If a component is wider than its parent, it will overflow.

Since API version 10, this API supports the calc calculation feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../../common-definitions/basic-types/document.md#length) | Yes | 
Width of the component to set.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/dTByZZbwTdKz8tTDFJSbFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1550F037DAE3BFCB61191458557AD4A67875E5ECB4D67E39C46E71702641900)

-   In the [TextInput](../../../text-and-input/textinput/document.md) component, setting **width** to **auto** means that the width adapts to the width of the text content.
    
-   In the [AlphabetIndexer](../../../information-display/alphabetindexer/document.md) component, setting **width** to **auto** means that the width adapts to the maximum width of index entries.
    

#### height

height(value: Length): T

Sets the height of the component. By default, the height required to fully hold the component content is used. If a component is higher than its parent, it will overflow.

Since API version 10, this API supports the calc calculation feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../../common-definitions/basic-types/document.md#length) | Yes | 
Height of the component to set.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/15xl2aJlQWG2VlpHdMHsIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79D7AA78ED9E191F49B227B0C6F1655DDB185920F5EA0D7EAD503F9881BFD246)

In the [Row](../../../rows-columns-and-stacking/row/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), and [RelativeContainer](../../../rows-columns-and-stacking/relativecontainer/document.md) components, setting **width** and **height** to **auto** means that the size adapts to the size of their child components.

#### width15+

width(widthValue: Length | LayoutPolicy): T

Sets the width of the component or its horizontal layout policy. By default, the component uses the width required for its content. If a component is wider than its parent, it will overflow.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| widthValue | [Length](../../../common-definitions/basic-types/document.md#length) | [LayoutPolicy](#layoutpolicy15) | Yes | 
Width of the component to set.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### height15+

height(heightValue: Length | LayoutPolicy): T

Sets the height of the component or its vertical layout policy. By default, the component uses the height required for its content. If a component is higher than its parent, it will overflow.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| heightValue | [Length](../../../common-definitions/basic-types/document.md#length) | [LayoutPolicy](#layoutpolicy15) | Yes | 
Height of the component to set.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### size

size(value: SizeOptions): T

Sets the width and height of the component.

Since API version 10, this API supports the calc calculation feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SizeOptions](../../../common-definitions/basic-types/document.md#sizeoptions) | Yes | 
The **SizeOptions** type is used to set the width and height.

Exception handling: If the parameter is **undefined**, the attribute setting does not take effect. For other invalid values, the **size** attribute reverts to its default behavior when unconfigured.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### padding

padding(value: Padding | Length | LocalizedPadding): T

Sets the padding of the component.

Since API version 10, this API supports the calc calculation feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Padding](../../../common-definitions/basic-types/document.md#padding) | [Length](../../../common-definitions/basic-types/document.md#length) | [LocalizedPadding](../../../common-definitions/basic-types/document.md#localizedpadding12)12+ | Yes | 
Padding of the component to set.

When the parameter is of the **Length** type, the four paddings take effect.

Default value: **0**

Unit: vp

When **padding** is set to a percentage, the width of the parent container is used as the basic value.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### margin

margin(value: Margin | Length | LocalizedMargin): T

Sets the margin of the component. The margin is considered as a part of the component's size during position calculation, thereby affecting the component's placement.

Since API version 10, this API supports the calc calculation feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Margin](../../../common-definitions/basic-types/document.md#margin) | [Length](../../../common-definitions/basic-types/document.md#length) | [LocalizedMargin](../../../common-definitions/basic-types/document.md#localizedmargin12)12+ | Yes | 
Margin of the component to set.

When the parameter is of the **Length** type, the four margins take effect.

Default value: **0**

Unit: vp

When **margin** is set to a percentage, the width of the parent container is used as the basic value. When child components are laid out along the cross axis of the [Row](../../../rows-columns-and-stacking/row/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), or [Flex](../../../rows-columns-and-stacking/flex/document.md) container, the cross axis size of the child components and the margins add up to the total size of the container.

For example, if the width of the **Column** container is 100, the width of the child component is 50, the left margin is 10, and the right margin is 20, then the actual horizontal offset of the child component is 10.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### safeAreaPadding14+

safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T

Sets the safe area padding. This allows the container to add a component-level safe area for its child components to extend into. This attribute can be dynamically set using [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/f3znA1grRUq5BB3bDaXEdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D13CD63925682A20396B602FE9AC123CB10109E87147D4230FFD85B25EFFBF79)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 18.

**Widget capability**: This API can be used in ArkTS widgets since API version 14.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| paddingValue | [Padding](../../../common-definitions/basic-types/document.md#padding) | [LengthMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | [LocalizedPadding](../../../common-definitions/basic-types/document.md#localizedpadding12) | Yes | 
Safe area padding.

Default value: **0**

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/446EaKtgT9ahGxGhHjmqyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4432F6BCCDD6BA984713564134095F8F6A93B719CC94DBE0C34FA35905C06501)

When parent and ancestor containers define component-level safe areas, child components can detect and utilize these areas, referred to as Accumulated Safe Area Expansion (SAE), which represents the maximum extendable length in each direction. When ancestor containers have contiguous **safeAreaPadding** (undivided by margin, border, or padding), SAE accumulates recursively outward until no adjacent outer **safeAreaPadding** exists or the recursion extends beyond the page container. System-level avoid areas (status bar, navigation bar, notch areas, and more) are treated as the page container's inherent **safeAreaPadding** and participate in SAE calculations. For details about the avoid areas, see [Safe Area](../safe-area/document.md).

These component-level safe areas can be leveraged by combining with other attributes. For example, setting the [ignoreLayoutSafeArea](../safe-area/document.md#ignorelayoutsafearea20) attribute on a child component allows it to extend its layout into the SAE region.

#### layoutWeight

layoutWeight(value: number | string): T

Sets the weight of the component during layout. A component with this attribute set is allocated space along the main axis of its parent container ([Row](../../../rows-columns-and-stacking/row/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), or [Flex](../../../rows-columns-and-stacking/flex/document.md)) based on its specified weight.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Layout weight of the component.

When the parent container size is determined:

Elements without **layoutWeight** or with **layoutWeight** set to **0** take precedence in occupying space.

The remaining space on the main axis is then allocated proportionally among elements with a **layoutWeight** value greater than 0, ignoring their own size settings.

Default value: **0**

**NOTE**

This parameter is only effective in [Row](../../../rows-columns-and-stacking/row/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), and [Flex](../../../rows-columns-and-stacking/flex/document.md) container components.

The value can be a number greater than or equal to 0 or a string that can be converted to a number.

If any child component in a container has the **layoutWeight** attribute set to a value greater than 0, then child components will no longer be laid out based on [flexShrink](../flex-layout/document.md#flexshrink) and [flexGrow](../flex-layout/document.md#flexgrow).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### constraintSize

constraintSize(value: ConstraintSizeOptions): T

Sets the constraint size of the component, which is used to limit the size range during component layout.

Since API version 10, this API supports the calc calculation feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ConstraintSizeOptions](../../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | 
Constraint size of the component to set. **constraintSize** takes precedence over **width** and **height**. See **Impact of constraintSize on width/height**.

Default value:

{

minWidth: 0,

maxWidth: Infinity,

minHeight: 0,

maxHeight: Infinity

}

Exception handling: For strings beginning with numerals, only the numeric part is parsed. Strings not beginning with numerals are parsed as 0. For other invalid values, the **constraintSize** attribute reverts to its default behavior when unconfigured.

Unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

**Impact of constraintSize(minWidth/maxWidth/minHeight/maxHeight) on width/height**

| Default Value | Result |
| :-- | :-- |
| \\ | 
width=MAX(minWidth,MIN(maxWidth,width))

height=MAX(minHeight,MIN(maxHeight,height))

 |
| maxWidth, maxHeight | 

width=MAX(minWidth,width)

height=MAX(minHeight,height)

 |
| minWidth, minHeight | 

width=MIN(maxWidth,width)

height=MIN(maxHeight,height)

 |
| width, height | 

If minWidth < maxWidth, the layout logic of the component takes effect, and the value range of **width** is \[minWidth, maxWidth\]. Otherwise, width = MAX(minWidth, maxWidth).

If minHeight < maxHeight, the layout logic of the component takes effect, and the value range of **height** is \[minHeight, maxHeight\]. Otherwise, height = MAX (minHeight, maxHeight).

 |
| width and maxWidth; height and maxHeight | 

width = minWidth

height = minHeight

 |
| width and minWidth; and height and minHeight | 

The layout logic of the component takes effect, and the value of **width** cannot be greater than that of **maxWidth**.

The layout logic of the component takes effect, and the value of **height** cannot be greater than that of **maxHeight**.

 |
| minWidth and maxWidth; minHeight and maxHeight | 

The width of the component is initially determined by the value of **width**, and it may be adjusted based on other layout attributes.

The height of the component is initially determined by the value of **height**, and it may be adjusted based on other layout attributes.

 |
| width, minWidth, and maxWidth | The layout restrictions passed by the parent container are used for layout. |
| height, minHeight, and maxHeight | The layout restrictions passed by the parent container are used for layout. |

#### LayoutPolicy15+

Enumerates the layout policies for component width and height.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| matchParent | [LayoutPolicy](#layoutpolicy15) | Yes | No | 
When the component adapts to the parent component's layout, its size equals the parent component's content area (excluding the areas defined by **padding**, **border**, and **safeAreaPadding**).

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| wrapContent20+ | [LayoutPolicy](#layoutpolicy15) | Yes | No | 

When the component adapts to its child components (content), its size equals the child components (content) and is constrained by the parent component's content area size.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| fixAtIdealSize20+ | [LayoutPolicy](#layoutpolicy15) | Yes | No | 

When the component adapts to its child components (content), its size equals the child components (content) and is not constrained by the parent component's content area size.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/m4Ftq0tjQeygcuyI44fp6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5DEF3552586756CA257611B31A9ED51FC7724131CD22102934A64388BA44D99)

-   **LayoutPolicy** supports three layout policies: **matchParent** (adapts to the parent component's layout), **wrapContent** (adapts to content but does not exceed the parent component's size), **fixAtIdealSize** (adapts to content and may exceed the parent component's size). For the implementation example, see [Example 5: Setting the Layout Policy](#example-5-setting-the-layout-policy).
    
-   For **wrapContent** and **fixAtIdealSize**: If the component's size cannot be determined by its content, it uses the default size (if available); otherwise, it calculates the size as (0, 0).
    
-   When a container is set to **wrapContent** and contains child components set to **matchParent** (including cases where only one side is set to **matchParent**): (1) The container is first expanded by child components with determinate sizes. (2) Child components set to **matchParent** then adapt to the container's size. (3) If no child components have determinate sizes, both the container and its child components have a zero size.
    
-   **LayoutPolicy** has lower priority than **constraintSize**.
    
-   Since API version 15, only the width and height attributes of **Row** and **Column** components support the **LayoutPolicy** type. Setting **LayoutPolicy** on other components produces the same behavior as having no width or height specified. Since API version 20, all basic components support the **LayoutPolicy** type.
    

#### Example

## Example 1: Setting the Component Width, Height, Margin, and Padding

This example demonstrates how to set the width, height, padding, and margin of a component.

// xxx.ets
@Entry
@Component
struct SizeExample {
  build() {
    Column({ space: 10 }) {
      Text('margin and padding:').fontSize(12).fontColor(0xCCCCCC).width('90%')
      Row() {
        // Width: 80; height: 80; margin: 20 (blue area); top, bottom, left, and right paddings: 5, 15, 10, and 20 (white area)
        Row() {
          Row()
            .size({ width: '100%', height: '100%' })
            .backgroundColor(Color.Yellow)
        }
        .width(80)
        .height(80)
        .padding({
          top: 5,
          left: 10,
          bottom: 15,
          right: 20
        })
        .margin(20)
        .backgroundColor(Color.White)
      }.backgroundColor(Color.Blue)

      Text('constraintSize')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Text('this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text')
        .width('90%')
        .constraintSize({ maxWidth: 200 })

      Text('layoutWeight')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      // When the container size is determined, the component occupies the space along the main axis based on the layout weight, and the component size setting is ignored.
      Row() {
        // Weight 1: The component occupies 1/3 of the remaining space along the main axis.
        Text('layoutWeight(1)')
          .size({ width: '30%', height: 110 }).backgroundColor(0xFFEFD5).textAlign(TextAlign.Center)
          .layoutWeight(1)
        // Weight 2: The component occupies 2/3 of the remaining space along the main axis.
        Text('layoutWeight(2)')
          .size({ width: '30%', height: 110 }).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
          .layoutWeight(2)
        // If layoutWeight is not set, the component is rendered based on its own size setting.
        Text('no layoutWeight')
          .size({ width: '30%', height: 110 }).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
      }
      .size({ width: '90%', height: 140 })
      .backgroundColor(0xAFEEEE)

      // calc calculation feature
      Text('calc:')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Column() {
        Row() {
          Text('width 50%')
            .fontSize(14)
            .borderWidth(1)
            .textAlign(TextAlign.Center)
            .size({ width: '50%', height: 50 })
          Text('width 50vp')
            .fontSize(14)
            .borderWidth(1)
            .textAlign(TextAlign.Center)
            .size({ width: '50vp', height: 50 })
        }
        .width('100%')
        .justifyContent(FlexAlign.Center)

        Text('width:calc(50% + 50vp), height:calc(50%)')
          .fontSize(14)
          .borderWidth(1)
          .fontWeight(FontWeight.Bold)
          .backgroundColor(0xFFFAF0)
          .textAlign(TextAlign.Center)
          .size({ width: 'calc(50% + 50vp)', height: 'calc(50%)' })
          // If width or height is set to a percentage, the width or height of the parent container are used as the base values. The calculation result of calc for the width equals the sum of the widths of the two text components above.
      }.width("100%").height(100)
    }
    .width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/206QDSF-Rqm6KXakKwubZQ/en-us_image_0000002537765400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D98D40F032DFAC467E06684008DA833E1CC283E98EA40738A6AC6AB96533E205)

## Example 2: Using LocalizedPadding and LocalizedMargin Types

This example demonstrates how to use **LocalizedPadding** and **LocalizedMargin** types to define the **padding** and **margin** attributes.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct SizeExample {
  build() {
    Column({ space: 10 }) {
      Text('margin and padding:')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Row() {
        // Set the width to 80, height to 80, top, bottom, start, and end paddings to 40, 20, 30, and 10, respectively (blue area), and top, bottom, start, and end margins to 5, 15, 10, and 20, respectively (white area).
        Row() {
          Row()
            .size({ width: '100%', height: '100%' })
            .backgroundColor(Color.Yellow)
        }
        .width(80)
        .height(80)
        .padding({
          top: LengthMetrics.vp(5),
          bottom: LengthMetrics.vp(15),
          start: LengthMetrics.vp(10),
          end: LengthMetrics.vp(20)
        })
        .margin({
          top: LengthMetrics.vp(40),
          bottom: LengthMetrics.vp(20),
          start: LengthMetrics.vp(30),
          end: LengthMetrics.vp(10)
        })
        .backgroundColor(Color.White)
      }
      .backgroundColor(Color.Blue)
    }
    .width('100%')
    .margin({ top: 5 })
  }
}

The following shows how the example is represented with left-to-right scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/MjsQ6b3JSFGt_mAR8x6MMA/en-us_image_0000002537925340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39F13C7ECC47E4D7D8E3902F7FD8F37BC64572F3789BC7F790D0A80150D4274E)

The following shows how the example is represented with right-to-left scripts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/A3tNMhhmQKiAcKhHD7R0yA/en-us_image_0000002568685117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3C407721D6F9BF1D0626A9BF479A5F3D43B73E5A8A1CFB0363C3AE720ED0A63)

## Example 3: Setting a Component-Level Safe Area

This example demonstrates how to set a component-level safe area for a container.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SafeAreaPaddingExample {
  build() {
    Column() {
      Column() {
        Column()
          .width("100%")
          .height("100%")
          .backgroundColor(Color.Pink)
      }
      .width(200)
      .height(200)
      .backgroundColor(Color.Yellow)
      .borderWidth(10)
      .padding(10)
      .safeAreaPadding(LengthMetrics.vp(40))
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/gXwRzQolQm2612PgGMxlrA/en-us_image_0000002568765127.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81ACCF536C5AE34023B954C519B0D6AEE34C2538A18A0A4DECC945B620853A9A)

## Example 4: Using attributeModifier to Dynamically Set a Safe Area

This example demonstrates how to use **attributeModifier** to dynamically set a component-level safe area for a container.

// xxx.ets
class MyModifier implements AttributeModifier<CommonAttribute> {
  applyNormalAttribute(instance: CommonAttribute): void {
    instance.safeAreaPadding({
      left: 10,
      top: 20,
      right: 30,
      bottom: 40
    })
  }
}

@Entry
@Component
struct SafeAreaPaddingExample {
  @State modifier: MyModifier = new MyModifier()

  build() {
    Column() {
      Column() {
        Column()
          .width("100%")
          .height("100%")
          .backgroundColor(Color.Pink)
      }
      .width(200)
      .height(200)
      .backgroundColor(Color.Yellow)
      .borderWidth(10)
      .padding(10)
      .attributeModifier(this.modifier)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/_oRx7xLsSq-Weg7J5hixxA/en-us_image_0000002537765402.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B81E6005AC0854442E7BE387D0753D1DE37E324735D0E6D4B8201C016C5BAEAC)

## Example 5: Setting the Layout Policy

This example demonstrates how to set the layout policy for a container's size.

// xxx.ets
@Entry
@Component
struct LayoutPolicyExample {
  build() {
    Column() {
      Column() {
        // When matchParent is effective, the current component's size is equal to its parent component's content area size (180x180 vp) and is subject to its own constraintSize (150x150 vp), so the current component's size is 150x150 vp.
        Text("matchParent")
        Flex()
          .backgroundColor('rgb(0, 74, 175)')
          .width(LayoutPolicy.matchParent)
          .height(LayoutPolicy.matchParent)
          .constraintSize({ maxWidth: 150, maxHeight: 150 })

        // When wrapContent is effective, the current component's size is equal to its child component size (300x300 vp), but it cannot exceed the parent component's content size (180x180 vp) and is subject to its own constraintSize (250x250 vp), so the current component's size is 180x180 vp.
        Text("wrapContent")
        Row() {
          Flex()
            .width(300)
            .height(300)
        }
        .backgroundColor('rgb(39, 135, 217)')
        .width(LayoutPolicy.wrapContent)
        .height(LayoutPolicy.wrapContent)
        .constraintSize({ maxWidth: 250, maxHeight: 250 })

        // Since API version 20, layoutPolicy supports wrapContent and fixAtIdealSize. When fixAtIdealSize is effective, the current component's size is equal to its child component size (300x300 vp), it can exceed the parent component's content size (180x180 vp) but is subject to its own constraintSize (250x250 vp), so the current component's size is 250x250 vp.
        Text("fixAtIdealSize")

        Row() {
          Flex()
            .width(300)
            .height(300)
        }
        .backgroundColor('rgb(240, 250, 255)')
        .width(LayoutPolicy.fixAtIdealSize)
        .height(LayoutPolicy.fixAtIdealSize)
        .constraintSize({ maxWidth: 250, maxHeight: 250 })
      }
      .width(200)
      .height(200)
      .padding(10)
    }
    .width("100%")
    .height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/9BgpcgJqTqCIlQoglZ6CWQ/en-us_image_0000002537925342.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7859979CE4DA08ABB586553F817971F21B286AFF70EE1F6D6B7F73CD853B1A1B)
