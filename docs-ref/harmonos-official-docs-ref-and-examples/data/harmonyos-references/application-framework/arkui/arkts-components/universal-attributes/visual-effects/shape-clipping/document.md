# Shape Clipping

Shape clipping changes the visible portion of a component through clipping or masking.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/7tTygaaYQtCQbvwdDHit1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E36C2E1ABF5CF76BBEF52F5F82D3DA26771E2289E39BEE5AF77830E7219B7EF)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### clip12+

clip(value: boolean): T

Sets whether to clip the areas of child components that extend beyond this component's bounds, that is, whether to perform clipping based on the edge contour of the parent container If this API is not used, the area of child components extending beyond the current component's bounds is not clipped by default.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to clip the areas of child components that extend beyond the current component's bounds.

The value **true** means to clip the areas of child components that extend beyond the current component's bounds, and **false** means the opposite.

Note: If this parameter is set to **true**, child components exceeding the current component's bounds will not respond to bound gesture events.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### clip18+

clip(clip: Optional<boolean>): T

Sets whether to clip the areas of child components that extend beyond this component's bounds, that is, whether to perform clipping based on the edge contour of the parent container If this API is not used, the area of child components extending beyond the current component's bounds is not clipped by default. Compared with [clip12+](#clip12), this API supports the **undefined** type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| clip | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to clip the areas of child components that extend beyond the current component's bounds.

Note: If this parameter is set to **true**, child components exceeding the current component's bounds will not respond to bound gesture events.

If **clip** is set to **undefined**, clipping is disabled, and child components are not clipped.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### clip(deprecated)

clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T

Sets whether to clip this component based on the given shape.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/ejX7vmaqQr61N6iy9T0i9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4A14B71231A745ADF2AEECFA7BEF01940208098E16D3EC85309789DE44740CE)

This API is supported since API version 7 and deprecated since API version 12. You are advised to use [clipShape](#clipshape12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | [CircleAttribute](../../../graphic-drawing/circle/document.md) | [EllipseAttribute](../../../graphic-drawing/ellipse/document.md) | [PathAttribute](../../../graphic-drawing/path/document.md) | [RectAttribute](../../../graphic-drawing/rect/document.md) | Yes | 
Clip mode. If the value is a shape attribute, the component is clipped based on the specified shape. If the value is of the Boolean type, it specifies whether to clip the component based on the boundaries of the parent container.

Default value: **false**.

Note: If the value is a shape attribute, the clipped area can still respond to bound gesture events. If the value is of the Boolean type, the clipped area will not respond to bound gesture events.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### clipShape12+

clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T

Clips this component according to the specified shape (which may include position information).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/vI-awoy5QyOIJD5YpcjZEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00FF383BF81C9F19694F5D5221A4D5FB7A9A75D40F2E7B80B9BFFF5E5AE17D67)

Different shapes support different ranges of attributes. A path is one type of shape, along with others like ellipses and rectangles.

Path shapes do not support setting width and height attributes. For details about the supported attributes, see the specific shape documentation.

The [fill](../../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#fill) attribute of shapes has no effect on the **clipShape** API.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CircleShape](#circleshape12) | [EllipseShape](#ellipseshape12) | [PathShape](#pathshape12) | [RectShape](#rectshape12) | Yes | 
Shape (which may include position information) to clip the current component.

Note: The clipped area remains responsive to bound gesture events.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### clipShape18+

clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T

Clips this component according to the specified shape (which may include position information). Compared with [clipShape12+](#clipshape12), this API supports the **undefined** type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/8oBEWXN3RQ-DnOIOyJpuHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E92D7F4448D9525F4DA8E725D07AFFF91F847754C75D4A76CC055C8D684A4F9C)

Different shapes support different ranges of attributes. A path is one type of shape, along with others like ellipses and rectangles.

Path shapes do not support setting width and height attributes. For details about the supported attributes, see the specific shape documentation.

The [fill](../../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#fill) attribute of shapes has no effect on the **clipShape** API.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shape | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[CircleShape](#circleshape12) | [EllipseShape](#ellipseshape12) | [PathShape](#pathshape12) | [RectShape](#rectshape12)\> | Yes | 
Shape (which may include position information) to clip the current component.

Note: The clipped area remains responsive to bound gesture events.

If the value of **shape** is **undefined**, the current setting will be reset to its default state.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### CircleShape12+

type CircleShape = CircleShape

Defines the CircleShape type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [CircleShape](../../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#circleshape) | Circle shape. |

#### EllipseShape12+

type EllipseShape = EllipseShape

Defines the EllipseShape type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [EllipseShape](../../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#ellipseshape) | Ellipse shape. |

#### PathShape12+

type PathShape = PathShape

Defines the PathShape type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [PathShape](../../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#pathshape) | Path shape. |

#### RectShape12+

type RectShape = RectShape

Defines the RectShape type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [RectShape](../../../../arkts-api/ui/ohos-arkui-shape-shape/document.md#rectshape) | Rectangle shape. |

#### mask12+

mask(value: ProgressMask): T

Adds a mask to the component to indicate the progress.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ProgressMask](#progressmask10) | Yes | Mask to add to the component, which allows for dynamic adjustment of progress, maximum value, and color settings. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### mask18+

mask(mask: Optional<ProgressMask>): T

Adds a mask to the component to indicate the progress. Compared with [mask12+](#mask12), this API supports the **undefined** type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mask | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[ProgressMask](#progressmask10)\> | Yes | 
Mask to add to the component, which allows for dynamic adjustment of progress, maximum value, and color settings.

If **mask** is set to **undefined**, the component to revert to its original effect without the mask to indicate the progress.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### mask(deprecated)

mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T

Adds a mask of the specified shape to the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/mBGoYmKoSGe28nz2XqNzqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=334E4DD340F6B73A0C67A758B51E3DA7599164AC08E96355D1EE1C3411D19665)

This API is supported since API version 7 and deprecated since API version 12. You are advised to use [maskShape](#maskshape12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CircleAttribute](../../../graphic-drawing/circle/document.md) | [EllipseAttribute](../../../graphic-drawing/ellipse/document.md) | [PathAttribute](../../../graphic-drawing/path/document.md) | [RectAttribute](../../../graphic-drawing/rect/document.md) | [ProgressMask](#progressmask10)10+ | Yes | Mask of the specified shape to add to the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### maskShape12+

maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T

Adds a mask of the specified shape to the component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CircleShape](#circleshape12) | [EllipseShape](#ellipseshape12) | [PathShape](#pathshape12) | [RectShape](#rectshape12) | Yes | Mask of the specified shape to add to the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### maskShape18+

maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T

Adds a mask of the specified shape to the component. Compared with [maskShape12+](#maskshape12), this API supports the **undefined** type.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shape | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[CircleShape](#circleshape12) | [EllipseShape](#ellipseshape12) | [PathShape](#pathshape12) | [RectShape](#rectshape12)\> | Yes | 
Mask of the specified shape to add to the component.

If the value of **shape** is **undefined**, the current setting will be reset to its default state.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ProgressMask10+

Sets the progress, maximum value, and color for a mask.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor10+

constructor(value: number, total: number, color: ResourceColor)

Constructs a **ProgressMask** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Current value of the progress mask.

Value range: \[0.0, +∞)

 |
| total | number | Yes | 

Maximum value of the progress mask.

Value range: \[0.0, +∞)

 |
| color | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Color of the progress mask. |

#### \[h2\]updateProgress10+

updateProgress(value: number): void

Updates the progress value of the progress mask.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Current value of the progress mask. |

#### \[h2\]updateColor10+

updateColor(value: ResourceColor): void

Updates the color of the progress mask.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Color of the progress mask. |

#### \[h2\]enableBreathingAnimation12+

enableBreathingAnimation(value: boolean): void

Sets whether to enable the breathing animation when the progress indicator is full. If this API is not set, the breathing animation is disabled by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable the breathing animation.

**true**: The breathing animation is enabled.

**false**: The breathing halo animation is disabled.

 |

#### Example

## Example 1: Using Different Clipping Attributes

This example demonstrates how to clip and mask an image using [clipShape](#clipshape12), [clip](#clip12), and [maskShape](#maskshape12).

// xxx.ets
import { CircleShape, RectShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipAndMaskExample {
  build() {
    Column({ space: 15 }) {
      Text('clip').fontSize(12).width('75%').fontColor('#DCDCDC')
      Row() {
        // Replace $r("app.media.testImg") with the image resource file you use.
        Image($r('app.media.testImg')).width('500px').height('280px')
      }
      .clip(true) // If clip is not set to true, the image is not confined by the rounded corners of the <Row> component and may extend beyond the <Row> component.
      .borderRadius(20)

      // Clip the image based on a circle with a diameter of 280 px.
      // Replace $r("app.media.testImg") with the image resource file you use.
      Image($r('app.media.testImg'))
        .clipShape(new CircleShape({ width: '280px', height: '280px' }))
        .width('500px').height('280px')

      Text('mask').fontSize(12).width('75%').fontColor('#DCDCDC')
      // Add a 500 × 280 px square mask to the image.
      // Replace $r("app.media.testImg") with the image resource file you use.
      Image($r('app.media.testImg'))
        .maskShape(new RectShape({ width: '500px', height: '280px' }).fill(Color.Gray))
        .width('500px').height('280px')

      // Add a 280 × 280 px circular mask to the image.
      // Replace $r("app.media.testImg") with the image resource file you use.
      Image($r('app.media.testImg'))
        .maskShape(new CircleShape({ width: '280px', height: '280px' }).fill(Color.Gray))
        .width('500px').height('280px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/_ClQ77m9QNCYIKUd698qIQ/en-us_image_0000002537925368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AE583E61DF1F040EE4C26FF2FF83102DE3C67F78BDD17012BB5A73ED0AB0721)

## Example 2: Implementing Component Masking

This example demonstrates how to mask an image using [mask](#mask12).

@Entry
@Component
struct ProgressMaskExample {
  @State progressFlag1: boolean = true;
  @State color: Color = 0x01006CDE;
  @State value: number = 10.0;
  @State enableBreathingAnimation: boolean = false;
  @State progress: ProgressMask = new ProgressMask(10.0, 100.0, Color.Gray);

  build() {
    Column({ space: 15 }) {
      Text('progress mask').fontSize(12).width('75%').fontColor('#DCDCDC')
      // Add a 280 × 280 px progress mask to the image.
      // Replace $r("app.media.testImg") with the image resource file you use.
      Image($r('app.media.testImg'))
        .width('500px').height('280px')
        .mask(this.progress)
        .animation({
          duration: 2000, // Animation duration.
          curve: Curve.Linear, // Animation curve.
          delay: 0, // Animation delay.
          iterations: 1, // Number of playback times.
          playMode: PlayMode.Normal // Animation playback mode.
        }) // Animation configuration for the width and height attributes of the <Button> component.

      // Update the progress value of the progress mask.
      Button('updateProgress')
        .onClick((event?: ClickEvent) => {
          this.value += 10;
          this.progress.updateProgress(this.value);
        }).width(200).height(50).margin(20)

      // Update the color of the progress mask.
      Button('updateColor')
        .onClick((event?: ClickEvent) => {
          if (this.progressFlag1) {
            this.progress.updateColor(0x9fff0000);
          } else {
            this.progress.updateColor(0x9f0000ff);
          }
          this.progressFlag1 = !this.progressFlag1
        }).width(200).height(50).margin(20)

      // Enable or disable the breathing animation.
      Button('enableBreathingAnimation:' + this.enableBreathingAnimation)
        .onClick((event?: ClickEvent) => {
          this.enableBreathingAnimation = !this.enableBreathingAnimation;
          this.progress.enableBreathingAnimation(this.enableBreathingAnimation);
        }).width(200).height(50).margin(20)

      // Restore the progress mask.
      Button('click reset!')
        .onClick((event?: ClickEvent) => {
          this.value = 0;
          this.progress.updateProgress(this.value);
        }).width(200).height(50).margin(20)
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/cxIbTw64QkSzN9R7-ZHqyQ/en-us_image_0000002568685145.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2150495A0F7A9F433FF71A3E3F8BCE9FFEA3EA58E25A8D5A8D64C86880A39544)
