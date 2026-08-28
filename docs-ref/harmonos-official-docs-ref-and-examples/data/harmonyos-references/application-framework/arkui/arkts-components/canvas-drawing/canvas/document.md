# Canvas

The **Canvas** component can be used to customize drawings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/GqE7pYTkTp-fBdGMkogDLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19D3E22A52F1B3C6D2DBC8384A1E6144A7E00084DA6CC2440FDFE26368F5BD9A)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

#### \[h2\]Canvas

Canvas(context?: CanvasRenderingContext2D | DrawingRenderingContext)

Creates a **Canvas** component. The maximum allowed size cannot exceed 10000 px × 10000 px. If the size exceeds this limit, the **Canvas** component will fail to be created.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md) | [DrawingRenderingContext12+](../drawingrenderingcontext/document.md) | No | 
2D rendering context for a canvas.

**CanvasRenderingContext2D**: Canvases cannot share one **CanvasRenderingContext2D** object. For details, see [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md). **DrawingRenderingContext**: Canvases cannot share one **DrawingRenderingContext** object. For details, see [DrawingRenderingContext](../drawingrenderingcontext/document.md).

If the value is **null** or **undefined**, **context** is considered unset.

 |

#### \[h2\]Canvas12+

Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)

Creates a **Canvas** component. You can specify a **CanvasRenderingContext2D** or **DrawingRenderingContext** object, along with AI image analysis options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md) | [DrawingRenderingContext12+](../drawingrenderingcontext/document.md) | Yes | 
2D rendering context for a canvas.

**CanvasRenderingContext2D**: Canvases cannot share one **CanvasRenderingContext2D** object. For details, see [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md). **DrawingRenderingContext**: Canvases cannot share one **DrawingRenderingContext** object. For details, see [DrawingRenderingContext](../drawingrenderingcontext/document.md).

If the value is **null** or **undefined**, **context** is considered unset.

 |
| imageAIOptions | [ImageAIOptions](../../images-and-videos/image-analysis-types/document.md#imageaioptions12) | Yes | 

AI image analysis options. You can configure the analysis type or bind an analyzer controller through this parameter.

If the value is **null** or **undefined**, the default value of [ImageAIOptions](../../images-and-videos/image-analysis-types/document.md#imageaioptions12) is used. The default value is **{ type: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\], aiController: new ImageAnalyzerController() }**, indicating that subject recognition and text recognition are enabled.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]enableAnalyzer12+

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

For the settings to take effect, this attribute must be used together with [StartImageAnalyzer](../canvasrenderingcontext2d/document.md#startimageanalyzer12) and [StopImageAnalyzer](../canvasrenderingcontext2d/document.md#stopimageanalyzer12) of [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md).

This attribute cannot be used together with the [overlay](../../universal-attributes/basic-attributes/overlay-control/document.md#overlay) attribute. If they are set at the same time, the **CustomBuilder** attribute in **overlay** has no effect. This feature depends on device capabilities.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/1edrpa92SGu9NoU_2V9jBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97D2A09ABC84FE4F0E5BADEE5DA60E3734D28D1DABB0A0C2E7A47425F6350FFB)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable the AI image analyzer for subject recognition, text recognition, and object lookup within the component content.

**true**: Enable the AI image analyzer. **false**: Disable the AI analyzer.

The **null** and **undefined** values are handled as the default value.

Default value: **false**

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onReady

onReady(event: VoidCallback)

Triggered when the **Canvas** component is initialized or when its size changes. Dynamic attribute setting using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) is supported.

When this event is triggered, the canvas is cleared. The width and height of the **Canvas** component are then determined and can be obtained, allowing you to use APIs related to the **Canvas** component for drawing. If only the position of the canvas changes, only the [onAreaChange](../../universal-events/component-change-events/component-area-change-event/document.md#onareachange) event is triggered, not the **onReady** event. The [onAreaChange](../../universal-events/component-change-events/component-area-change-event/document.md#onareachange) event is triggered after the **onReady** event.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Triggered when the **Canvas** component is initialized or when its size changes. |

#### Example

## Example 1: Using APIs in CanvasRenderingContext2D

This example describes how to use the APIs in [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md) for drawing on a canvas.

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/a6KY-JZ9SlqyRvr1LWETsQ/en-us_image_0000002568685515.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F8295D9CEF2D6DB7D6A6B6B2A50294511602607057577966F8176BA44CA9958)

## Example 2: Using APIs in DrawingRenderingContext

This example demonstrates how to use the APIs in [DrawingRenderingContext](../drawingrenderingcontext/document.md) for drawing on a canvas.

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.canvas.drawCircle(200, 200, 100)
          this.context.invalidate()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/95TaJx4cTCmR0t1lZf7Lhw/en-us_image_0000002568765525.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F4FAFD5C51EF1B8BB6028A34FBFDE023DBE92602296CAFDC0DDED337D506C4)

## Example 3: Dynamically Setting Attributes and Methods of the Canvas Component Using attributeModifier

This example demonstrates how to use [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) to dynamically set the [enableAnalyzer](#enableanalyzer12) attribute and [onReady](#onready) method of the **Canvas** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/zzHMm7jYTJm2k59LJm7VBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4746F6FCEBCBD092247983F4014EE99F2233E5F5ACA29B6F0802DB5B0287736F)

The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not packaged by default when a project or module is created. To package these resources, go to **buildOption** in the module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. For details, see the description of [copyCodeResource](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356) in **resOptions**.

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

class MyCanvasModifier implements AttributeModifier<CanvasAttribute> {
  context: CanvasRenderingContext2D = new CanvasRenderingContext2D()

  applyNormalAttribute(instance: CanvasAttribute): void {
    // Draw an image with the width and height of 200 vp from (0, 0).
    instance.onReady(() => {
      // Replace "common/img.png" with the image resource file you use.
      let image = new ImageBitmap("common/img.png")
      this.context.drawImage(image, 0, 0, 200, 200)
    })
    // Enable the AI image analyzer, which can be triggered by a long press after the start button is tapped.
    instance.enableAnalyzer(true)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyCanvasModifier = new MyCanvasModifier()
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\]
  }
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\],
    aiController: this.aiController
  }

  build() {
    Row() {
      Column() {
        Button('start')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.context.startImageAnalyzer(this.config)
              .then(() => {
                console.info("analysis complete")
              })
              .catch((error: BusinessError) => {
                let e: BusinessError = error as BusinessError
                console.error(\`Error code: ${e.code}, message: ${e.message}\`)
              })
          })
        Button('stop')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.context.stopImageAnalyzer()
          })
        Button('getTypes')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes()
          })
        Canvas(this.context, this.options)
          .borderWidth(1)
          .height(200)
          .width(200)
          .attributeModifier(this.modifier)
          .onAppear(() => {
            this.modifier.context = this.context
          })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/jFHqdR-HSKGYj3UkSnSHnA/en-us_image_0000002537765800.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83AD14FD75B511C572D5F6AC6B9FC167392B230AA1EE0704C8EE1127A44C633E)
