# Overlay Control

The overlay feature allows you to place elements on top of a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/3zcVGJ4ZQimxTcRBsfHqxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0223D89009D587BC94AD685ACE1BEF1FC8F35E25D781A33B86F2971996F410C)

The feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### overlay

overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions ): T

Adds an overlay to this component, which can be text, a custom component, or [ComponentContent](#componentcontent12). The overlay is positioned based on the current component. The overlay is not rendered through the component tree, meaning some APIs (for example, [getRectangleById](../../../../arkts-api/ui/ohos-arkui-componentutils-componentutils/document.md#componentutilsgetrectanglebyiddeprecated)) cannot access components within the overlay.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/1sBdlMSNT_eFt60OoALe1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B2B5EB5AE63DA64D2DFE57B49CAC424DC4D5BE09C7B5991DD513B2CC96FF334)

The overlay places the floating layer component above the bound component, blocking all user interactions with components beneath it. To enable interaction with underlying components, refer to [Example 2: Setting an Overlay Using a Custom Builder](#example-2-setting-an-overlay-using-a-custom-builder) and apply **.hitTestBehavior(HitTestMode.Transparent)** to the outermost component in the overlay builder. This configuration is particularly crucial for watermark implementations, where the overlay must not interfere with user interaction with the underlying content.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8)10+ | [ComponentContent](#componentcontent12)12+ | Yes | 
Content of the overlay, which can be text or a custom component.

**NOTE**

When the overlay is a custom component, it cannot obtain focus through sequential keyboard navigation. Using **CustomBuilder** will cause the overlay content to be destroyed and recreated on page refresh, which may incur performance overhead. For scenarios with frequent page updates, using **ComponentContent** is recommended.

 |
| options | [OverlayOptions](#overlayoptions12) | No | 

Options for positioning the overlay.

**NOTE**

In versions earlier than API version 12, **options** is defined as follows:

{

align?: [Alignment](../../../common-definitions/enums/document.md#alignment),

offset?: {x?: number, y?: number}

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/9gL5dp9HQ9WMf2HlqadEbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA1EA1494F8C5ED75D49E501228977454F1424CA38E9B167DF261857FEE7BEA1)

The overlay node does not support mount/unmount events, such as [onAppear](../../../universal-events/component-change-events/show-hide-event/document.md#onappear) and [onDisAppear](../../../universal-events/component-change-events/show-hide-event/document.md#ondisappear).

#### OverlayOptions12+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/dRawcZNuTPyDwLnqAA8bRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2F1429C248CFC8EA40E5921B76936DB9E41842FC7869EE1DF940D3CF3BCCBBD)

To standardize anonymous object definitions, the element definitions here have been revised in API version 12. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| align7+ | [Alignment](../../../common-definitions/enums/document.md#alignment) | No | Yes | 
Alignment of the overlay relative to the component.

Default value: **TopStart**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset7+ | [OverlayOffset](#overlayoffset12) | No | Yes | 

Offset of the overlay from the upper left corner. By default, the overlay is in the upper left corner of the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/xHZfR1E7QfWXYZouEzG3rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=332A519FFD69D06F54EDF56E03A3CD2763483F2548376E2288CADC25D3DA86CF)

When both **align** and **offset** are set, the effects are combined. The overlay is first aligned relative to the component and then offset from its current upper left corner.

#### OverlayOffset12+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/jptGrdYdQXiLQ7hGGmuVCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60E414B1FC4D6731F543E0E8D5816CBFD4BCBECE62796B8B3107C2903F5604D1)

To standardize anonymous object definitions, the element definitions here have been revised in API version 12. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x7+ | number | No | Yes | 
Horizontal offset.

Unit: vp.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| y7+ | number | No | Yes | 

Vertical offset.

Unit: vp.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ComponentContent12+

type ComponentContent<T = Object> = ComponentContent<T>

Represents a constructor used to create a **ComponentContent** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ComponentContent](../../../../arkts-api/ui/arkui/componentcontent/document.md)<T> | Constructor used to create a **ComponentContent** object. |

#### Example

## Example 1: Setting an Overlay Using a String

This example demonstrates how to set an overlay using a string.

// xxx.ets
@Entry
@Component
struct OverlayExample {
  build() {
    Column() {
      Column() {
        Text('floating layer')
          .fontSize(12).fontColor(0xCCCCCC).maxLines(1)
        Column() {
          // Replace $r('app.media.img') with the image resource file you use.
          Image($r('app.media.img'))
            .width(240).height(240)
            .overlay("Winter is a beautiful season, especially when it snows.", {
              align: Alignment.Bottom,
              offset: { x: 0, y: -15 }
            })
        }.border({ color: Color.Black, width: 2 })
      }.width('100%')
    }.padding({ top: 20 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Cbz_s5T8S7ySN5m4AWpfpg/en-us_image_0000002537925334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=228FF45778CCEF59BD72146AEB23F164435E33A0B4DE64601BB6589BD77351E6)

## Example 2: Setting an Overlay Using a Custom Builder

This example demonstrates how to set an overlay using a custom builder.

// xxx.ets
@Entry
@Component
struct OverlayExample {
  @Builder
  OverlayNode() {
    Column() {
      // Replace $r('app.media.img1') with the image resource file you use.
      Image($r('app.media.img1'))
      Text("This is overlayNode").fontSize(20).fontColor(Color.White)
    }
    .width(180)
    .height(180)
    .alignItems(HorizontalAlign.Center)
    .hitTestBehavior(HitTestMode.Transparent) // Configure the overlay not to block interaction.
  }

  build() {
    Column() {
      // Replace $r('app.media.img2') with the image resource file you use.
      Image($r('app.media.img2'))
        .overlay(this.OverlayNode(), { align: Alignment.Center })
        .objectFit(ImageFit.Contain)
    }.width('100%')
    .border({ color: Color.Black, width: 2 }).padding(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/G21vZ6UzQoqS_CMgzmUyRw/en-us_image_0000002568685111.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE2957BC500B785A3EBB628CB16E3C05C3CB0C047D391755AF3586B06998A80B)

## Example 3: Setting an Overlay Using ComponentContent

This example demonstrates how to use **ComponentContent** to dynamically change the background color of the overlay.

// xxx.ets
import { ComponentContent } from '@kit.ArkUI';

class Params {
  backgroundColor: string | Resource = ""

  constructor(backgroundColor: string | Resource) {
    this.backgroundColor = backgroundColor;
  }
}

@Builder
function overlayBuilder(params: Params) {
  Row() {
  }.width('100%').height('100%').backgroundColor(params.backgroundColor)
}

@Entry
@Component
struct Page\_4040 {
  @State overlayColor: string = 'rgba(0, 0, 0, 0.6)';
  private uiContext: UIContext = this.getUIContext();
  private overlayNode: ComponentContent<Params> =
    new ComponentContent(this.uiContext, wrapBuilder(overlayBuilder), new Params(this.overlayColor))

  aboutToAppear(): void {
    setInterval(() => {
      if (this.overlayColor.includes('0.6')) {
        this.overlayColor = 'rgba(0, 0, 0, 0.1)'
        this.overlayNode.update(new Params(this.overlayColor));
      } else {
        this.overlayColor = 'rgba(0, 0, 0, 0.6)'
        this.overlayNode.update(new Params(this.overlayColor));
      }
    }, 1000)
  }

  build() {
    Row() {
      Column() {
        Text(this.overlayColor)
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
    .overlay(this.overlayNode)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/r_lLMlO3ShiFtoi8Qn4Nkw/en-us_image_0000002568765121.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46B54A9EEB4DD00EA18766216EF9B64195B1625E5772DD09999DF649189B70F5)
