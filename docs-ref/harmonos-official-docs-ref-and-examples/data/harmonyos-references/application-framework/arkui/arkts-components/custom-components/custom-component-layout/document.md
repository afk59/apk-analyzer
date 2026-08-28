# Custom Component Layout

The custom layout of a custom component is used to lay out its child components through data calculation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/L9V-bqlhTOW65n_wkZFEVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93633D4B21A77BC506CCDB21C0D3793004DADD6C8C2EA9E62010C62644ADFE8E)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

A custom component is considered to have a custom layout when either of the **onMeasureSize** or **onPlaceChildren** methods is implemented. For complete layout control, implement both methods simultaneously. For details about the specifications, see the API descriptions for these methods.

Since API version 20, when child components within a custom layout have their [LayoutPolicy](../../universal-attributes/layout-and-borders/sizing/document.md#layoutpolicy15) object's **fixAtIdealSize** property set to **true**, these components will ignore any layout constraints from their parent component. Instead, they will adhere to the size ranges explicitly defined by the developer in the custom layout implementation.

Lazy loading (including [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat) and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)) is not supported in custom layouts.

#### onMeasureSize10+

onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult

Invoked when the custom component needs to determine its size. Through this callback the component receives its layout information and size constraints from the ArkUI framework. State variables should not be changed in this callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selfLayoutInfo | [GeometryInfo](#geometryinfo10) | Yes | 
Information about the component's computed layout properties after measurement.

**NOTE**

During the first layout, the component will use its own set attributes as the basis for layout.

 |
| children | Array<[Measurable](#measurable10)\> | Yes | 

Array containing layout information for all child components after measurement.

**NOTE**

When a child component does not have its layout information set, it retains the previous layout settings or, if no previous layout settings are available, stays at the default size of 0.

 |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | Layout constraints applied to the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SizeResult](#sizeresult10) | Component size information. |

#### onPlaceChildren10+

onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void

Invoked when the custom component needs to determine the positions of its child components. Through this callback the component receives its child component size constraints from the ArkUI framework. State variables should not be changed in this callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selfLayoutInfo | [GeometryInfo](#geometryinfo10) | Yes | Information about the component's computed layout properties after measurement. |
| children | Array<[Layoutable](#layoutable10)\> | Yes | Array containing layout information for all child components after measurement. |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | Layout constraints applied to the component. |

**Example**

See the [example for customizing a layout](#example).

#### GeometryInfo10+

Provides layout geometry information of the parent component (a custom component). Inherits from [SizeResult](#sizeresult10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| borderWidth | [EdgeWidth](../../common-definitions/basic-types/document.md#edgewidths9) | No | No | 
Width of the parent component's border.

Unit: vp.

 |
| margin | [Margin](../../common-definitions/basic-types/document.md#margin) | No | No | 

Margin values of the parent component.

Unit: vp.

 |
| padding | [Padding](../../common-definitions/basic-types/document.md#padding) | No | No | 

Padding values of the parent component.

Unit: vp.

 |

#### Layoutable10+

Provides the child component layout information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Name

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| measureResult | [MeasureResult](#measureresult10) | No | No | 
Measurement result of the child component.

**Atomic service API**: This API can be used in atomic services since API version 11.

Unit: vp

 |
| uniqueId18+ | number | No | Yes | 

Unique ID that the system assigns to the child component.

Value range: \[0, +∞).

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### \[h2\]layout

layout(position: Position): void

Applies the specified position constraints to the child component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | [Position](../../common-definitions/basic-types/document.md#position) | Yes | Absolute position. |

#### \[h2\]getMargin12+

getMargin(): DirectionalEdgesT<number>

Obtains the margin values of the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DirectionalEdgesT<number>](../../common-definitions/basic-types/document.md#directionaledgestt12) | Margin values of the child component. |

#### \[h2\]getPadding12+

getPadding(): DirectionalEdgesT<number>

Obtains the padding values of the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DirectionalEdgesT<number>](../../common-definitions/basic-types/document.md#directionaledgestt12) | Padding values of the child component. |

#### \[h2\]getBorderWidth12+

getBorderWidth(): DirectionalEdgesT<number>

Obtains the border widths of the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DirectionalEdgesT<number>](../../common-definitions/basic-types/document.md#directionaledgestt12) | Border widths of the child component. |

#### Measurable10+

Provides the child component position information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Name

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uniqueId18+ | number | No | Yes | Unique ID that the system assigns to the child component. |

#### \[h2\]measure

measure(constraint: ConstraintSizeOptions) : MeasureResult

Imposes size constraints on the child component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | Size constraint. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MeasureResult](#measureresult10) | Provides the measurement result of the component. |

#### \[h2\]getMargin12+

getMargin(): DirectionalEdgesT<number>

Obtains the margin values of the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DirectionalEdgesT<number>](../../common-definitions/basic-types/document.md#directionaledgestt12) | Margin values of the child component. |

#### \[h2\]getPadding12+

getPadding(): DirectionalEdgesT<number>

Obtains the padding values of the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DirectionalEdgesT<number>](../../common-definitions/basic-types/document.md#directionaledgestt12) | Padding values of the child component. |

#### \[h2\]getBorderWidth12+

getBorderWidth(): DirectionalEdgesT<number>

Obtains the border widths of the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DirectionalEdgesT<number>](../../common-definitions/basic-types/document.md#directionaledgestt12) | Border widths of the child component. |

#### MeasureResult10+

Provides the measurement result of the component. This API inherits from [SizeResult](#sizeresult10).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### SizeResult10+

Provides the component size information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/686JLBWqQam3RihaxWNPWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27EF767630FC8424671EEE03B6A2878E0F42E8304D8BB7656C34FFD73F7BE371)

-   The custom layout does not support the LazyForEach syntax.
-   When a custom layout is created in builder mode, only **this.builder()** is allowed in the **build()** method of a custom component, as shown in the recommended usage in the example below.
-   The size parameters of the parent component (custom component), except **aspectRatio**, are at a lower priority than those specified by **onMeasureSize**.
-   The position parameters of the child component, except **offset**, **position**, and **markAnchor**, are at a lower priority than those specified by **onPlaceChildren**, and do not take effect.
-   When using the custom layout method, you must call **onMeasureSize** and **onPlaceChildren** at the same time for the layout to display properly.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | No | 
Width obtained from the measurement result.

Unit: vp.

 |
| height | number | No | No | 

Height obtained from the measurement result.

Unit: vp.

 |

#### onLayout(deprecated)

onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void

Invoked when the custom component lays out its child components. Through this callback the component receives its child component layout information and size constraint from the ArkUI framework. State variables should not be changed in this callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Q7KAnPS8RymAwSygXJa5AQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EB6AB15BD7BD1E0985A2691F6ABD41632B7C69C7000E4DB30F559654D2DADAC)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [onPlaceChildren](#onplacechildren10) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| children | Array<[LayoutChild](#layoutchilddeprecated)\> | Yes | Child component layout information. |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | Size constraint of the parent component. |

#### onMeasure(deprecated)

onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void

Invoked when the custom component needs to determine its size. Through this callback the component receives its child component layout information and its own size constraints from the ArkUI framework. State variables should not be changed in this callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/6ZsDBbENTj-5cbHgJ7oesg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1445D29632CED4A793B152214ECE44BE46B539B52A776EF3461761FD8BB24F07)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [onMeasureSize](#onmeasuresize10) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| children | Array<[LayoutChild](#layoutchilddeprecated)\> | Yes | Child component layout information. |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | Size constraint of the parent component. |

#### LayoutChild(deprecated)

Provides the child component layout information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/1M_juZ4uQ7ql8B5V6Q8qzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15CB1E12A52AD8237AA9BD21B70D61CF16A7388D881701650BA29783094E8F92)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [Measurable](#measurable10) or [Layoutable](#layoutable10) instead.

#### \[h2\]Name

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the child component. |
| id | string | No | No | ID of the child component. |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | No | No | Constraint size of the child component. |
| borderInfo | [LayoutBorderInfo](#layoutborderinfodeprecated) | No | No | Provides the border information of the child component. |
| position | [Position](../../common-definitions/basic-types/document.md#position) | No | No | Position coordinates of the child component. |

#### \[h2\]measure(deprecated)

measure(childConstraint: ConstraintSizeOptions)

Applies the specified size constraints to the child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/2hurmgFOTZCMs1tjoR1FOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B21DE0E52E71FF49913FEDA0B9C3339FA58F28615FD87B5E39F4E633A2D657F0)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [Measurable](#measurable10) or [Layoutable](#layoutable10) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| childConstraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | Yes | Size constraints to apply to child components. |

#### \[h2\]layout(deprecated)

layout(childLayoutInfo: LayoutInfo)

Applies the specified layout constraints to the child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8HRjjxuDQKqR_4oVvOiO3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EB11B755731FB4899AACE641B7B5F3F920409A66859D9B5FC71234341925F2D)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [Measurable](#measurable10) or [Layoutable](#layoutable10) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| childLayoutInfo | [LayoutInfo](#layoutinfodeprecated) | Yes | Layout information of the child component. |

#### LayoutBorderInfo(deprecated)

Provides the border information of the child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7_h4EJF1RHCQ8IGiU0zDcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F971BE702C451728D0FF1A7C1E0E82DD4451A7E650BE50002DBA832AC07E78C7)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [getBorderWidth](#getborderwidth12), [getMargin](#getmargin12), and [getPadding](#getpadding12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| borderWidth | [EdgeWidths](../../common-definitions/basic-types/document.md#edgewidths9) | No | No | Edge widths in different directions of the component. |
| margin | [Margin](../../common-definitions/basic-types/document.md#margin) | No | No | Margin values in different directions of the component. |
| padding | [Padding](../../common-definitions/basic-types/document.md#padding) | No | No | Padding values in different directions of the component. |

#### LayoutInfo(deprecated)

Provides the child component layout information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/y5yLZZtDQfaXHguvCmBG8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06328F6545EBB84EE59F4931DE8F4903EBDF89545700570221063E00E9205EEA)

This API is supported since API version 9 and deprecated since API version 10.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | [Position](../../common-definitions/basic-types/document.md#position) | No | No | Position coordinates of the child component. |
| constraint | [ConstraintSizeOptions](../../common-definitions/basic-types/document.md#constraintsizeoptions) | No | No | Constraint size of the child component. |

#### Example

## Example 1: Implementing a Custom Layout

This example demonstrates how to implement a custom layout.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      CustomLayout({ builder: ColumnChildren })
    }
  }
}

@Builder
function ColumnChildren() {
  ForEach(\[1, 2, 3\], (index: number) => { // LazyForEach is not supported.
    Text('S' + index)
      .fontSize(30)
      .width(100)
      .height(100)
      .borderWidth(2)
      .offset({ x: 10, y: 20 })
  })
}

@Component
struct CustomLayout {
  @Builder
  doNothingBuilder() {
  };

  @BuilderParam builder: () => void = this.doNothingBuilder;
  @State startSize: number = 100;
  result: SizeResult = {
    width: 0,
    height: 0
  };

  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
    let startPos = 300;
    children.forEach((child) => {
      let pos = startPos - child.measureResult.height;
      child.layout({ x: pos, y: pos })
    })
  }

  onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
    let size = 100;
    children.forEach((child) => {
      let result: MeasureResult = child.measure({
        minHeight: size,
        minWidth: size,
        maxWidth: size,
        maxHeight: size
      })
      size += result.width / 2;
    })
    this.result.width = 100;
    this.result.height = 400;
    return this.result;
  }

  build() {
    this.builder()
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PuDRXBN1Q2CGwsqc0w3IGw/en-us_image_0000002568685671.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84A428080CE1AC3B15B08955C11AC8C1212EA472FF69898B5EBD5C6A1A65B74A)

## Example 2: Determining Whether to Participate in Layout Calculation

This example shows how to determine whether a component participates in layout calculation based on its position.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      CustomLayout({ builder: ColumnChildren })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

@Builder
function ColumnChildren() {
  ForEach(\[1, 2, 3\], (item: number, index: number) => { // LazyForEach is not supported.
    Text('S' + item)
      .fontSize(20)
      .width(60 + 10 \* index)
      .height(100)
      .borderWidth(2)
      .margin({ left:10 })
      .padding(10)
  })
}

@Component
struct CustomLayout {
  // Lay out only one row, and hide child components that are too large for the available space.
  @Builder
  doNothingBuilder() {
  };

  @BuilderParam builder: () => void = this.doNothingBuilder;
  result: SizeResult = {
    width: 0,
    height: 0
  };
  overFlowIndex: number = -1;

  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
    let currentX = 0;
    let infinity = 100000;
    if (this.overFlowIndex == -1) {
      this.overFlowIndex = children.length;
    }
    for (let index = 0; index < children.length; ++index) {
      let child = children\[index\];
      if (index >= this.overFlowIndex) {
        // Hide any child component that extends beyond the area of its parent component by placing it in a distant position.
        child.layout({x: infinity, y: 0});
        continue;
      }
      child.layout({ x: currentX, y: 0 })
      let margin = child.getMargin();
      currentX += child.measureResult.width + margin.start + margin.end;
    }
  }

  onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
    let width = 0;
    let height = 0;
    this.overFlowIndex = -1;
    // Restrict the maximum width of the parent component to the smaller value between 200 vp and the maximum width from layout constraints.
    let maxWidth = Math.min(200, constraint.maxWidth as number);
    for (let index = 0; index < children.length; ++index) {
      let child = children\[index\];
      let childResult: MeasureResult = child.measure({
          minHeight: constraint.minHeight,
          minWidth: constraint.minWidth,
          maxWidth: constraint.maxWidth,
          maxHeight: constraint.maxHeight
      })
      let margin = child.getMargin();
      let newWidth = width + childResult.width + margin.start + margin.end;
      if (newWidth > maxWidth) {
        // Record the index of the component that should not be laid out.
        this.overFlowIndex = index;
        break;
      }
      // Update the parent component's cumulative width and height.
      width = newWidth;
      height = Math.max(height, childResult.height + margin.top + margin.bottom);
    }
    this.result.width = width;
    this.result.height = height;
    return this.result;
  }

  build() {
    this.builder()
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ANo3-6E9RsibIj0PgttikQ/en-us_image_0000002568765681.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F58E60C32FBC4A1457A3C9A7E6FA78D5C2AF642FDEA76B10F1045E3B45617F44)

## Example 3: Obtaining the Child Component FrameNode and Setting Related Attributes

This example shows how to obtain the [FrameNode](../../../arkts-api/ui/arkui/framenode/document.md) of a child component using **uniqueId** and change its size and background color using the FrameNode API.

import { FrameNode, NodeController } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  build() {
    Column() {
      CustomLayout()
    }
  }
}

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext)
    return this.rootNode
  }
}

@Component
struct CustomLayout {
  @Builder
  childrenBuilder() {
    ForEach(\[1, 2, 3\], (index: number) => { // LazyForEach is not supported.
      NodeContainer(new MyNodeController())
    })
  };

  @BuilderParam builder: () => void = this.childrenBuilder;
  result: SizeResult = {
    width: 0,
    height: 0
  };

  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
    let prev = 0;
    children.forEach((child) => {
      let pos = prev + 10;
      prev = pos + child.measureResult.width
      child.layout({ x: pos, y: 0 })
    })
  }

  onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
    let size = 100;
    children.forEach((child) => {
      console.info('child uniqueId: ', child.uniqueId)
      const uiContext = this.getUIContext()
      if (uiContext) {
        let node: FrameNode | null = uiContext.getFrameNodeByUniqueId(child.uniqueId) // Obtain the FrameNode of the NodeContainer component.
        if (node) {
          node.getChild(0)!.commonAttribute.width(100)
          node.getChild(0)!.commonAttribute.height(100)
          node.getChild(0)!.commonAttribute.backgroundColor(Color.Pink) // Change the size and background color of the FrameNode.
        }
      }
      child.measure({ minHeight: size, minWidth: size, maxWidth: size, maxHeight: size })
    })
    this.result.width = 320;
    this.result.height = 100;
    return this.result;
  }

  build() {
    this.builder()
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/lWtfrXVeSTeP6MUfnLZQtA/en-us_image_0000002537765956.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C898BBC5A71FFA458C3232982141255EB6B03692BCD8B245D8C2C6CED59EE5E)

## Example 4: Allowing the Child Component to Ignore Parent Component Size Constraints

This example demonstrates how to use the **fixAtIdealSize** property of the [LayoutPolicy](../../universal-attributes/layout-and-borders/sizing/document.md#layoutpolicy15) object to allow the child component to ignore parent component size constraints.

@Entry
@Component
struct Index {
  @Builder
  ColumnChildrenText() {
    Text('=====Text=====Text=====Text=====Text=====Text=====Text=====Text=====Text' )
      .fontSize(16).fontColor(Color.Black)
      .borderWidth(2).backgroundColor('#fff8dc')
      .width(LayoutPolicy.fixAtIdealSize) // Set the child component's width to be unrestricted by the parent component.
      .height(LayoutPolicy.fixAtIdealSize)  // Set the child component's height to be unrestricted by the parent component.
  }

  build() {
    Column() {
      Column() {
        CustomLayoutText({ builder: this.ColumnChildrenText })
          .backgroundColor('#f0ffff').borderRadius(20).margin(10)
      }
      .width(300)
      .height(150)
      .margin(10)
      .backgroundColor(Color.Pink)
    }
    .width(350)
    .height(680)
    .margin(20)
    .alignItems(HorizontalAlign.Center)
  }
}

@Component
struct CustomLayoutText {
  @Builder
  doSomethingBuilder() {
  };

  @BuilderParam
  builder: () => void = this.doSomethingBuilder;
  result: SizeResult = {
    width: 0,
    height: 0
  };
  // The custom component implements custom layout.
  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
    let posY = 20;
    children.forEach((child) => {
      let posX = (selfLayoutInfo.width - child.measureResult.width) / 2;
      child.layout({ x: posX, y: posY })
      posY += child.measureResult.height + 30;
    })
  }

  onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
    children.forEach((child) => {
      let result: MeasureResult = child.measure({ maxWidth: 335, maxHeight: 50 }) // Set constraints on the size of the child component of the custom component.
    })
    this.result.width = 200;
    this.result.height = 130;
    return this.result;
  }

  build() {
    this.builder()
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/edT3hG8dQfmpQAgMDqsHgg/en-us_image_0000002537925896.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DAD9EBFB0B168F214D9E72C8179024D9D345C3BC5613F36802455F02114999A)
