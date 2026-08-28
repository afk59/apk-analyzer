# ContainerSpan

As a child of the [Text](../text/document.md) component, the **ContainerSpan** component is used to manage the background colors and rounded corners of multiple [Span](../span/document.md) and [ImageSpan](../imagespan/document.md) components in a unified manner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/KXLFjPWlS1qQ4Wwa9qDjKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D4CBB73B290E092DACC57038A491C7FD70064D56C564BE01BD3800DAF3CD3B0)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component can contain the [Span](../span/document.md) and [ImageSpan](../imagespan/document.md) child components.

#### APIs

ContainerSpan()

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

Only the following attributes are supported.

#### \[h2\]textBackgroundStyle

textBackgroundStyle(style: TextBackgroundStyle)

Sets the text background style. If this attribute is not separately set for a child component, the child component inherits the settings from the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/3-I876VKRKmgMAQBbbz3rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2406AB62000D3400AE66AEDAE886A1B5BB2648B34E4A46F03A88ADBC6D9BE3A5)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [TextBackgroundStyle](../span/document.md#textbackgroundstyle11) | Yes | 
Text background style.

Default value:

{

color: Color.Transparent,

radius: 0

}

 |

#### \[h2\]attributeModifier12+

attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute>)

Creates an attribute modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [AttributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifiert)<ContainerSpanAttribute> | Yes | Modifier for dynamically setting attributes on the current component. |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Setting the Background Style

This example demonstrates how to set the background style for text using the [textBackgroundStyle](#textbackgroundstyle) attribute, available since API version 11.

// xxx.ets
@Component
@Entry
struct Index {
  build() {
    Column() {
      Text() {
        ContainerSpan() {
          // Replace $r('app.media.app\_icon') with the image resource file you use.
          ImageSpan($r('app.media.app\_icon'))
            .width('40vp')
            .height('40vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
          Span('   Hello World !   ').fontSize('16fp').fontColor(Color.White)
        }
        .textBackgroundStyle({
          color: "#7F007DFF",
          radius: {
            topLeft: 12,
            topRight: 12,
            bottomLeft: 12,
            bottomRight: 12
          }
        })
      }
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/3x-d4WjTQCyBLHUGW8bt4Q/en-us_image_0000002537765692.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB11DA040355B890BA4D862588F78C09A6EA4DE5AB6B32866F74339433C7A59C)

## Example 2: Setting the Background Style Using attributeModifier

This example demonstrates how to set the background style for text using the [attributeModifier](#attributemodifier12) attribute, available since API version 12.

import { ContainerSpanModifier } from '@kit.ArkUI';

class MyContainerSpanModifier extends ContainerSpanModifier {
  applyNormalAttribute(instance: ContainerSpanAttribute): void {
    super.applyNormalAttribute?.(instance);
    this.textBackgroundStyle({ color: "#7F007DFF", radius: "12vp" });
  }
}

@Entry
@Component
struct ContainerSpanModifierExample {
  @State containerSpanModifier: ContainerSpanModifier = new MyContainerSpanModifier();

  build() {
    Column() {
      Text() {
        ContainerSpan() {
          // Replace $r('app.media.startIcon') with the image resource file you use.
          ImageSpan($r('app.media.startIcon'))
            .width('40vp')
            .height('40vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
          Span(' I\\'m ContainerSpan attributeModifier ').fontSize('16fp').fontColor(Color.White)
        }.attributeModifier(this.containerSpanModifier as MyContainerSpanModifier)
      }
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/JRKpw27tR_C1jo1mmuSfqg/en-us_image_0000002537925632.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E70AE75AB96E294845539D8680A2B60438E2EB5B1C107BED293E0D40F413B5AB)
