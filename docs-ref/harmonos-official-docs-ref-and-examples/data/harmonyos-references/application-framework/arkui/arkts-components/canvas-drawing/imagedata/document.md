# ImageData

An **ImageData** object stores pixel data rendered on a canvas.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/9lHoZ06ZS-KT2K05exMOCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A1030958381CE1721474885B89164AD156FB556BE304816EBC2C172D1B2883D)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

A constructor used to create an **ImageData** object. To ensure successful drawing, make sure the object's area does not exceed 16000 x 16000, with its width and height not greater than 16384 px. If the created area exceeds 536870911 px, the returned width and height are both 0 px, and **data** is **undefined**.

#### constructor

constructor(width: number, height: number, data?: Uint8ClampedArray)

Creates an **ImageData** object with the specified width, height, and color. If data is not defined, it is populated with a one‑dimensional array of 0s.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | 
Width of the rectangle.

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as **0**.

 |
| height | number | Yes | 

Height of the rectangle.

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as **0**.

 |
| data | [Uint8ClampedArray](../../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8clampedarray/document.md) | No | 

A one-dimensional array of color values. The values range from 0 to 255.

If the value specified is **undefined**, **data** is **undefined**.

Default value: a one-dimensional array of all 0s

 |

#### constructor12+

constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)

Creates an **ImageData** object with the specified width, height, and color. If data is not defined, it is populated with a one‑dimensional array of 0s. The unit of the **ImageData** object can be configured using **unit**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | 
Width of the rectangle.

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as **0**.

 |
| height | number | Yes | 

Height of the rectangle.

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as **0**.

 |
| data | [Uint8ClampedArray](../../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8clampedarray/document.md) | No | 

A one-dimensional array of color values. The values range from 0 to 255.

If the value specified is **undefined**, **data** is **undefined**.

Default value: a one-dimensional array of all 0s

 |
| unit | [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12) | No | 

Unit mode of the **ImageData** object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md).

Invalid values **undefined**, **NaN** and **Infinity** are treated as the default value.

Default value: **DEFAULT**.

 |

#### Properties

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | Yes | No | 
Actual width of the rectangle on the canvas.

The unit is px.

 |
| height | number | Yes | No | 

Actual height of the rectangle on the canvas.

The unit is px.

 |
| data | [Uint8ClampedArray](../../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8clampedarray/document.md) | Yes | No | A one-dimensional array of color values. The values range from 0 to 255. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/QmiTFc9OTwW4_VmURdXQyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB3301142B7F03BA7BF05FCAF89C7A31D767F1EAF6E3AA01E20A9F2763BDABB2)

The [px2vp](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2vp12) API can be used for unit conversion.

#### Example

This example shows how to use the **getImageData** API to obtain an **ImageData** object.

// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Replace "common/images/1234.png" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/1234.png");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 130, 130)
          let imageData = this.context.getImageData(50, 50, 130, 130)
          this.context.putImageData(imageData, 150, 150)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/OlyyNNJwRoKfWRat3mYJDA/en-us_image_0000002568765559.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C330DF1433CB098143F08A1E61F97D8E8FA8C5232970C9366859827F2EFFB063)
