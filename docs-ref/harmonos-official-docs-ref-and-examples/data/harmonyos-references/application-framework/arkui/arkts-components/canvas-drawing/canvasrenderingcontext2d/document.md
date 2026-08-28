# CanvasRenderingContext2D

After the **CanvasRenderingContext2D** object is bound to the **Canvas** component, you can draw shapes, texts, and images on the **Canvas** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/GCsODZAxSRuSWi9aKxuNpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DBCA2AB3E9D7DF23EDCFAF38A3C9DE65100465119A225E4A31989145A4315E1)

-   This API is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   It is recommended that the **CanvasRenderingContext2D** object and the **Canvas** component be encapsulated into the same custom component, ensuring a one-to-one correspondence and consistent lifecycle between them.
    
-   When you call drawing APIs in this module, the commands are stored in the associated **Canvas** component's command queue. These commands are only executed when the current frame enters the rendering phase and the associated **Canvas** component is visible. Therefore, when the **Canvas** component is invisible (for example, off-screen or hidden), avoid frequent drawing calls to prevent command queue buildup and excessive memory usage. For best practices, see [Controlling Canvas Rendering Based on Component Visibility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-drawing-customization-on-canvas#controlling-canvas-rendering-based-on-component-visibility).
    
-   The following path-related APIs apply only to paths created within **CanvasRenderingContext2D** and do not affect paths defined in [OffscreenCanvasRenderingContext2D](../offscreencanvasrenderingcontext2d/document.md) or [Path2D](../path2d/document.md): [beginPath](#beginpath), [moveTo](#moveto), [lineTo](#lineto), [closePath](#closepath), [bezierCurveTo](#beziercurveto), [quadraticCurveTo](#quadraticcurveto), [arc](#arc), [arcTo](#arcto), [ellipse](#ellipse), [rect](#rect), and [roundRect](#roundrect20).
    
-   When the width or height of the **Canvas** component exceeds 8000 px, rendering via the CPU causes significant performance degradation.
    

#### Constructor

#### \[h2\]constructor

constructor(settings?: RenderingContextSettings)

Constructs a canvas object, which supports configuration of parameters for the **CanvasRenderingContext2D** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| settings | [RenderingContextSettings](#renderingcontextsettings) | No | 
Settings of the **CanvasRenderingContext2D** object. For details, see [RenderingContextSettings](#renderingcontextsettings).

If the value is **undefined** or **null**, the default value of [RenderingContextSettings](#renderingcontextsettings) is used.

 |

#### \[h2\]constructor12+

constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

Creates a **CanvasRenderingContext2D** object, allowing for initial configuration of rendering parameters and unit mode.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| settings | [RenderingContextSettings](#renderingcontextsettings) | No | 
Settings of the **CanvasRenderingContext2D** object. For details, see [RenderingContextSettings](#renderingcontextsettings).

If the value is **undefined** or **null**, the default value of [RenderingContextSettings](#renderingcontextsettings) is used.

 |
| unit | [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12) | No | 

Unit mode of the **CanvasRenderingContext2D** object. The value cannot be dynamically changed once set.

Invalid values **undefined**, **NaN** and **Infinity** are treated as the default value.

Default value: **DEFAULT**.

 |

**Example**

The following example shows how to specify the unit mode during the creation of a **CanvasRenderingContext2D** object. The default unit mode is **LengthMetricsUnit.DEFAULT**, which corresponds to the default unit vp. Once set, this unit mode cannot be changed dynamically. For details, see [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12).

// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI'

@Entry
@Component
struct LengthMetricsUnitDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
  private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.contextPX)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextPX.fillRect(10,10,100,100)
          this.contextPX.clearRect(10,10,50,50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10,10,100,100)
          this.contextVP.clearRect(10,10,50,50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/aG-NFkVzR3ualEuJyikJYA/en-us_image_0000002537765802.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECC83AFE9A6FDA224C8F0590564032089ACCEDCC7EF091237E01720BA9A818CD)

#### Attributes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/GZMR3A1MQYSYe526GHCkiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09434B9D771DCEA103A4E058BFE093CE897410FACB81BCC2799DE444B88910A9)

The string format of **fillStyle**, **shadowColor**, and **strokeStyle** is **rgb(255, 255, 255)**, **rgba(255, 255, 255, 1.0)**, or **#FFFFFF**.

#### \[h2\]fillStyle

Sets the fill color for rendering. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string |number10+ |[CanvasGradient](../canvasgradient/document.md) | [CanvasPattern](../canvaspattern/document.md) | No | No | 
\- When the type is string, this attribute indicates the color of the fill area. For details about the color format, see the description for the string type in [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor).

\- When the type is number, this attribute indicates the color of the fill area. Fully transparent colors are not supported. For details about the color format, see the description for the number type in [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor).

\- When the type is **CanvasGradient**, this attribute indicates a gradient object, which is created via the [createLinearGradient](#createlineargradient) API.

\- When the type is **CanvasPattern**, this attribute indicates a pattern, which is created via the [createPattern](#createpattern) API.

Default value: **'#000000'** (black)

Invalid values do not take effect.

 |

// xxx.ets
@Entry
@Component
struct FillStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = '#0000ff'
          this.context.fillRect(20, 20, 150, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/g1mBCsbwTRuxA7om_1ynfQ/en-us_image_0000002537925742.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A888DC778F372677AEE5DB3B129A584C24760306FCE57D13BE3C5B75F694D4D0)

#### \[h2\]lineWidth

Sets the line width. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
Default value: **1** (px)

Default unit: vp

The value of **lineWidth** cannot be **0** or a negative number. Values of **0**, negative numbers, and **NaN** are handled with the default value. **Infinity** will cause an exception on the **lineWidth** attribute.

 |

// xxx.ets
@Entry
@Component
struct LineWidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
        this.context.lineWidth = 5
        this.context.strokeRect(25, 25, 85, 105)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/wMisMhfDQxqA67TGf_IoEg/en-us_image_0000002568685519.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11042A2131A10FE7137C86734EE1B12921964CE1D9BEF5C4692AD90269F5A28A)

#### \[h2\]strokeStyle

Sets the stroke color. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string |number10+ |[CanvasGradient](../canvasgradient/document.md) | [CanvasPattern](../canvaspattern/document.md) | No | No | 
\- When the type is string, this attribute indicates the stroke color. For details about the color format, see the description for the string type in [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor).

\- When the type is number, this attribute indicates the stroke color. Fully transparent colors are not supported. For details about the color format, see the description for the number type in [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor).

\- When the type is **CanvasGradient**, this attribute indicates a gradient object, which is created via the [createLinearGradient](#createlineargradient) API.

\- When the type is **CanvasPattern**, this attribute indicates a pattern, which is created via the [createPattern](#createpattern) API.

Default value: **'#000000'** (black)

Invalid values do not take effect.

 |

// xxx.ets
@Entry
@Component
struct StrokeStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 10
          this.context.strokeStyle = '#0000ff'
          this.context.strokeRect(25, 25, 155, 105)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/qjg3Of9DQTGSf58iZc_NrA/en-us_image_0000002568765529.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49101980CC34DE4C1CC6DD93C713079D5F4ACD5C054F1425903996D767B7D54D)

#### \[h2\]lineCap

Sets the line caps. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [CanvasLineCap](#canvaslinecap) | No | No | Default value: **'butt'** |

// xxx.ets
@Entry
@Component
struct LineCapExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.lineWidth = 8
          this.context.beginPath()
          this.context.lineCap = 'round'
          this.context.moveTo(30, 50)
          this.context.lineTo(220, 50)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/uxhzkyfaSvyvMLKK2e6jVQ/en-us_image_0000002537765804.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AF09955B7037F5C732226AF7FA7578DAB341657ADC6BEF90BE5F7311B9A86FC)

#### \[h2\]lineJoin

Sets the line join. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [CanvasLineJoin](#canvaslinejoin) | No | No | 
Available values are as follows:

\- **'round'**: The shape used to join line segments is a sector, whose radius at the rounded corner is equal to the line width.

\- **'bevel'**: The shape used to join line segments is a triangle. The rectangular corner of each line is independent.

\- **'miter'**: The shape used to join line segments has a mitered corner by extending the outside edges of the lines until they meet. You can view the effect of this attribute in **miterLimit**.

Default value: **'miter'**

 |

// xxx.ets
@Entry
@Component
struct LineJoinExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
        this.context.beginPath()
        this.context.lineWidth = 8
        this.context.lineJoin = 'miter'
        this.context.moveTo(30, 30)
        this.context.lineTo(120, 60)
        this.context.lineTo(30, 110)
        this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/WIXgH_KhS9qP4TAZ83SV0w/en-us_image_0000002537925744.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=691E15603C754BB93BD969F03DE2E894CFFA961A59DC32DE2B124581A26168F2)

#### \[h2\]miterLimit

Sets the miter limit, which specifies the distance between the inner and outer angles at line joins. This attribute takes effect only when **lineJoin** is set to **miter**. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
Default value: **10** (px)

Unit: px

The value of **miterLimit** cannot be **0** or a negative number. Values of **0**, negative numbers, and **NaN** are handled with the default value. **Infinity** will cause an exception on the **miterLimit** attribute.

 |

// xxx.ets
@Entry
@Component
struct MiterLimit {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 8
          this.context.lineJoin = 'miter'
          this.context.miterLimit = 3
          this.context.moveTo(30, 30)
          this.context.lineTo(60, 35)
          this.context.lineTo(30, 37)
          this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/uI8aOyGOTaaHwD6_yB3BiA/en-us_image_0000002568685521.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3695EAC3E9DFFA4E2C60B84464A51F610F1E7A1772198A6AD142C010DA8676AD)

#### \[h2\]font

Sets the text font. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

Syntax: ctx.font = 'font-style font-weight font-size font-family'

\- (Optional) **font-style**: font style. Available values are **normal** and **italic**.

\- (Optional) **font-weight**: font weight. Available values are as follows: **normal**, **bold**, **bolder**, **lighter**, **100**, **200**, **300**, **400**, **500**, **600**, **700**, **800**, **900**.

\- (Optional) **font-size**: font size and line height. The unit can be px or vp and must be specified.

\- (Optional) **font-family**: font family. Available values are **sans-serif**, **serif**, and **monospace**.

Starting from API version 20, this API is used to set registered custom fonts (the DevEco Studio Previewer does not support custom fonts). You can register a custom font in either of the following ways:

Register a custom font by calling the asynchronous API this.uiContext.getFont().[registerFont](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-font/document.md#registerfont) of ArkUI. Immediate rendering after calling this API may result in the custom font not taking effect.

Directly call the fontCollection.[loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) API of the font engine to register the custom font. In this case, the **fontCollection** instance must be **text.FontCollection.getGlobalInstance()** because the component loads fonts from this instance by default. If you use another instance, the custom font may not take effect.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string | No | No | 
Default value: **'normal normal 14px sans-serif'**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

// xxx.ets
import { text } from '@kit.ArkGraphics2D';

@Entry
@Component
struct FontDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          // Normal font style, normal weight, font size of 30 px, and font family of sans-serif
          this.context.font = 'normal normal 30px sans-serif'
          this.context.fillText("Hello px", 20, 60)
          // Italic style, bold, font size of 30 vp, and font family of monospace
          this.context.font = 'italic bold 30vp monospace'
          this.context.fillText("Hello vp", 20, 100)
          // Load the custom font file HarmonyOS\_Sans\_Thin\_Italic.ttf in the rawfile directory.
          let fontCollection = text.FontCollection.getGlobalInstance();
          fontCollection.loadFontSync('HarmonyOS\_Sans\_Thin\_Italic', $rawfile("HarmonyOS\_Sans\_Thin\_Italic.ttf"))
          // Bold, font size of 30 vp, and font family of HarmonyOS\_Sans\_Thin\_Italic
          this.context.font = "bold 30vp HarmonyOS\_Sans\_Thin\_Italic"
          this.context.fillText("Hello customFont", 20, 140)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/lpJDnNu7TRWRJLLFMdCt4w/en-us_image_0000002568765531.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF7761A714F4F1396C5EC1856CD658A2498C4D4F7191506FCE91E7211DABE97F)

#### \[h2\]textAlign

Sets the text alignment type. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [CanvasTextAlign](#canvastextalign) | No | No | 
In the **ltr** layout mode, the value **'start'** equals **'left'**. In the **rtl** layout mode, the value **'start'** equals **'right'**.

Default value: **'left'**

 |

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.strokeStyle = 'rgb(39,135,217)'
          this.context.moveTo(140, 10)
          this.context.lineTo(140, 160)
          this.context.stroke()
          this.context.font = '50px sans-serif'
          this.context.textAlign = 'start'
          this.context.fillText('textAlign=start', 140, 60)
          this.context.textAlign = 'end'
          this.context.fillText('textAlign=end', 140, 80)
          this.context.textAlign = 'left'
          this.context.fillText('textAlign=left', 140, 100)
          this.context.textAlign = 'center'
          this.context.fillText('textAlign=center', 140, 120)
          this.context.textAlign = 'right'
          this.context.fillText('textAlign=right', 140, 140)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/nJ5UL9l2RMqaspLgG3lw6A/en-us_image_0000002537765806.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7561E5B638BCA3BEBF76DD1AA388C2D4C3D52FEE84B3764D9C325076154977D)

#### \[h2\]textBaseline

Sets the horizontal alignment baseline for text rendering. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [CanvasTextBaseline](#canvastextbaseline) | No | No | Default value: **'alphabetic'** |

// xxx.ets
@Entry
@Component
struct TextBaseline {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.strokeStyle = 'rgb(0,0,255)'
          this.context.moveTo(0, 120)
          this.context.lineTo(400, 120)
          this.context.stroke()
          this.context.font = '20px sans-serif'
          this.context.textBaseline = 'top'
          this.context.fillText('Top', 10, 120)
          this.context.textBaseline = 'bottom'
          this.context.fillText('Bottom', 55, 120)
          this.context.textBaseline = 'middle'
          this.context.fillText('Middle', 125, 120)
          this.context.textBaseline = 'alphabetic'
          this.context.fillText('Alphabetic', 195, 120)
          this.context.textBaseline = 'hanging'
          this.context.fillText('Hanging', 295, 120)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/hsXO0D6MRqabxbV_sME6dg/en-us_image_0000002537925746.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79205E8239C973543770688D96EFF88328A08255C555C97A6F1A9D0D1C075BBC)

#### \[h2\]globalAlpha

Sets the opacity. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
The value range is \[0.0, 1.0\]. **0.0** indicates completely transparent, and **1.0** indicates completely opaque. If the set value is less than 0.0, **0.0** will be used. If the set value is greater than 1.0, **1.0** will be used.

In versions earlier than API version 18, if \*\*NaN \*\*or **Infinity** is set, rendering APIs cannot be called for rendering after this API. In API version 18 and later versions, if **NaN** or **Infinity** is set, the current API does not take effect, and other rendering APIs with valid arguments can be called normally.

Default value: **1.0**

 |

// xxx.ets
@Entry
@Component
struct GlobalAlpha {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(0, 0, 50, 50)
          this.context.globalAlpha = 0.4
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(50, 50, 50, 50)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/7WqHbycTR-O0jFT6tVNImQ/en-us_image_0000002568685523.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A14147CA4156057249BECA2769EF4AAD78E0C74643042235882E4F5132BEA385)

#### \[h2\]lineDashOffset

Sets the dashed line offset of the canvas. The value is of the float type. This attribute takes effect only when **setLineDash** is set. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
In versions earlier than API version 18, if **NaN** or **Infinity** is set, dashed lines are rendered as solid lines. In API version 18 and later versions, if **NaN** or **Infinity** is set, the current API does not take effect, and dashed lines are rendered normally.

Default value: **0.0**

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as the default value.

 |

// xxx.ets
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct LineDashOffset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private animator: AnimatorResult | undefined = undefined;

  drawAntLine() { // Implement the ant line animation.
    this.animator = this.getUIContext().createAnimator({
      duration: 2000,
      easing: 'linear',
      delay: 0,
      fill: 'none',
      direction: 'normal',
      iterations: -1,
      begin: 0, // Start point of the animation interpolation.
      end: 1 // End point of the animation interpolation.
    });
    this.animator.onFrame = (value: number) => {
      this.context.reset();
      this.context.lineWidth = 2;
      this.context.setLineDash(\[10, 5\]);
      this.context.lineDashOffset = 105 \* value;
      this.context.strokeRect(10, 10, 100, 100);
    };
    this.animator.play();
  }

  aboutToDisappear() {
    this.animator?.finish();
    this.animator = undefined;
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.drawAntLine();
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/kJ3RU8HxSkqzUA8X3Uu2jw/en-us_image_0000002568765533.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CE54B5D7D9900106DAA0202237C9570B0653B1803DE0171408132808A9CBACF)

#### \[h2\]globalCompositeOperation

Sets the composite operation. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string | No | No | 
Available values are as follows: **'source-over'**, **'source-atop'**, **'source-in'**, **'source-out'**, **'destination-over'**, **'destination-atop'**, **'destination-in'**, **'destination-out'**, **'lighter'**, **'copy'**, and **'xor'**.

Default value: **'source-over'**

 |

| Name | Description |
| :-- | :-- |
| source-over | Displays the new drawing above the existing drawing. Default value. |
| source-atop | Displays the new drawing on the top of the existing drawing. |
| source-in | Displays the new drawing inside the existing drawing. |
| source-out | Displays part of the new drawing that is outside of the existing drawing. |
| destination-over | Displays the existing drawing above the new drawing. |
| destination-atop | Displays the existing drawing on the top of the new drawing. |
| destination-in | Displays the existing drawing inside the new drawing. |
| destination-out | Displays the existing drawing outside the new drawing. |
| lighter | Displays both the new and existing drawing. |
| copy | Displays the new drawing and neglects the existing drawing. |
| xor | Combines the new drawing and existing drawing using the XOR operation. |

// xxx.ets
@Entry
@Component
struct GlobalCompositeOperation {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context3: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context4: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context5: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context6: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Row() {
        // 1. source-over: The new shape is overlaid on the original shape. This attribute is used by default.
        Canvas(this.context1)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx1 = this.context1;
            ctx1.fillStyle = 'rgb(39,135,217)';
            ctx1.fillRect(25, 25, 75, 75); // Original shape
            ctx1.globalCompositeOperation = 'source-over'; // Default value, which can be omitted.
            ctx1.fillStyle = 'rgb(23,169,141)';
            ctx1.fillRect(75, 75, 75, 75); // Display the new shape overlaid on the original shape.
          })
        // 2. destination-out: The original shape is erased in the area of the new shape. (This is the core logic of the eraser.)
        Canvas(this.context2)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx2 = this.context2;
            // Draw the background first.
            ctx2.fillStyle = 'rgb(39,135,217)';
            ctx2.fillRect(0, 0, ctx2.width, ctx2.height);
            // Set the composite operation to destination-out.
            ctx2.globalCompositeOperation = 'destination-out';
            // Draw a circle as the eraser.
            ctx2.beginPath();
            ctx2.arc(ctx2.width / 2, ctx2.height / 2, 60, 0, Math.PI \* 2);
            ctx2.fill(); // Erase the background of the circle.
          })
      }
      .height('30%')

      Row() {
        // 3. source-in: Only the overlapping part between the new shape and the original shape is retained (clipping or masking).
        Canvas(this.context3)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx3 = this.context3;
            // Draw the original shape (circle mask) first.
            ctx3.beginPath();
            ctx3.arc(ctx3.width / 2, ctx3.height / 2, 80, 0, Math.PI \* 2);
            ctx3.fillStyle = '#fff';
            ctx3.fill();
            // Set the composite operation.
            ctx3.globalCompositeOperation = 'source-in';
            // Draw a new shape (gradient rectangle).
            const gradient = ctx3.createLinearGradient(0, 0, ctx3.width, ctx3.height);
            gradient.addColorStop(0, 'rgb(23,169,141)');
            gradient.addColorStop(1, 'rgb(39,135,217)');
            ctx3.fillStyle = gradient;
            ctx3.fillRect(0, 0, 200, 200); // Display gradient only in the circular area.
          })
        // 4. lighter: The new shape is overlaid on the original shape (the luminance is added, and the color filtering effect is achieved).
        Canvas(this.context4)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx4 = this.context4;
            // Original shape (a semi-transparent red circle)
            ctx4.beginPath();
            ctx4.arc(70, 100, 50, 0, Math.PI \* 2);
            ctx4.fillStyle = 'rgba(234, 67, 53, 0.7)';
            ctx4.fill();
            // Set the composite operation.
            ctx4.globalCompositeOperation = 'lighter';
            // New shape (a semi-transparent blue circle)
            ctx4.beginPath();
            ctx4.arc(110, 100, 50, 0, Math.PI \* 2);
            ctx4.fillStyle = 'rgba(66, 133, 244, 0.7)';
            ctx4.fill(); // The overlapping area turns purple (luminance blending).
          })
      }
      .height('30%')

      Row() {
        // 5. destination-atop: retains the overlapping part of the original and new shapes and removes other parts.
        Canvas(this.context5)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx5 = this.context5;
            // Original shape (a green rectangle)
            ctx5.fillStyle = 'rgb(23,169,141)';
            ctx5.fillRect(0, 0, ctx5.width, ctx5.height);
            // Set the composite operation.
            ctx5.globalCompositeOperation = 'destination-atop';
            // New shape (a small circle)
            ctx5.beginPath();
            ctx5.arc(ctx5.width / 2, ctx5.height / 2, 60, 0, Math.PI \* 2);
            ctx5.fillStyle = '#000';
            ctx5.fill(); // Only the overlapping part of the rectangle and circle is retained.
          })
        // 6. Text mask (advanced usage of source-in)
        Canvas(this.context6)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx6 = this.context6
            // Draw the text first (as a mask).
            ctx6.font = 'bold 40vp';
            ctx6.textAlign = 'center';
            ctx6.textBaseline = 'middle';
            ctx6.fillText('CANVAS', ctx6.width / 2, ctx6.height / 2);
            // Set the composite operation.
            ctx6.globalCompositeOperation = 'source-in';
            // Draw the gradient background (displayed only in the text area).
            let textGradient = ctx6.createLinearGradient(50, 0, 300, 100);
            textGradient.addColorStop(0.0, 'rgb(39,135,217)');
            textGradient.addColorStop(0.5, 'rgb(255,238,240)');
            textGradient.addColorStop(1.0, 'rgb(23,169,141)');
            ctx6.fillStyle = textGradient;
            ctx6.fillRect(0, 0, 200, 200); // The gradient fills only the text area.
          })
      }
      .height('30%')
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/ogELNdsCTl2IAuWfHKWGhQ/en-us_image_0000002537765808.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=985651560327490D5702D52AA8F37478D4C579615D70865E74122EB47DD71D71)

#### \[h2\]shadowBlur

Sets the blur level for drawing shadows. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
Blur level. A larger value produces a greater blur effect. The value is of float type and must be greater than or equal to 0.

Default value: **0.0**

Unit: px

The value of **shadowBlur** cannot be a negative number. A negative number, **NaN**, and **Infinity** are treated as the default value.

 |

// xxx.ets
@Entry
@Component
struct ShadowBlur {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 30
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 100, 80)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/kbWY37xeRnWcMoS7sXU-vw/en-us_image_0000002537925748.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7B8CF3ED97172815220C582ACDC5CF55D1B5309E96BD49FD8ADD9E1A711E051)

#### \[h2\]shadowColor

Sets the shadow color. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string | No | No | 
For details about the color format, see the description for the string type in [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor).

Default value: **'#00000000'** (transparent black)

 |

// xxx.ets
@Entry
@Component
struct ShadowColor {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 30
          this.context.shadowColor = 'rgb(0,0,255)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(30, 30, 100, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/EnN8nv-xSEKw94N6_vQ3bQ/en-us_image_0000002568685525.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B91BACF08C309199294B38F3F4617EA1F811C3193606AFC1EAF0CA7F2E4B04EC)

#### \[h2\]shadowOffsetX

Sets the horizontal offset between the drawn shadow and the original object. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
Default value: **0.0**

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as the default value.

 |

// xxx.ets
@Entry
@Component
struct ShadowOffsetX {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 10
          this.context.shadowOffsetX = 20
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 100, 80)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/AiSp_IO8SYSa3BihzTWyqg/en-us_image_0000002568765535.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0794F0797DE4911B5FAB9AB1DD55AFF43FB9897753EC335CF8BEA47E087F737)

#### \[h2\]shadowOffsetY

Sets the vertical offset between the drawn shadow and the original object. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | No | No | 
Default value: **0.0**

Default unit: vp

Invalid values **NaN** and **Infinity** are treated as the default value.

 |

// xxx.ets
@Entry
@Component
struct ShadowOffsetY {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 10
          this.context.shadowOffsetY = 20
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(30, 30, 100, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/pdAErqUCRbaGs6jlYV211g/en-us_image_0000002537765810.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26E44C17ECE8F94A0E0CB54FD2BAC57B1914ABAB09E2359A081AD381FC3983AA)

#### \[h2\]imageSmoothingEnabled

Indicates whether to apply image smoothing adjustments when drawing images. The value **true** means to enable smoothing ,and **false** means to disable it. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| boolean | No | No | Default value: **true** |

// xxx.ets
@Entry
@Component
struct ImageSmoothingEnabled {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // Replace "common/images/icon.jpg" with the image resource file you use.
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.imageSmoothingEnabled = false
          this.context.drawImage( this.img,0,0,400,200)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/XgAQqp2ESymyflFjygerDw/en-us_image_0000002537925750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06D1C5737699F5ACD1011CA7C2471528396A29761D5570CFD8775CE29A0B2C17)

#### \[h2\]height

Component height.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | Yes | No | Default unit: vp |

// xxx.ets
@Entry
@Component
struct HeightExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let h = this.context.height
          this.context.fillRect(0, 0, 300, h/2)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/hQ-wvtqdSGyivvZvthxjAQ/en-us_image_0000002568685527.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B902835A976CCDDE4659F6972971775B05F01EC1C28B29FA4C208BB230A60D4)

#### \[h2\]width

Component width.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| number | Yes | No | Default unit: vp |

// xxx.ets
@Entry
@Component
struct WidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let w = this.context.width
          this.context.fillRect(0, 0, w/2, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/5zznVkrnS-W-gRG42KfQYQ/en-us_image_0000002568765537.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F520492F9038490BA6F141D6CDC37FA911E8749728F4CC8DDD810F865BB4D460)

#### \[h2\]canvas13+

FrameNode instance of the **Canvas** component associated with **CanvasRenderingContext2D**. It can be used to listen for the visibility status of the associated **Canvas** component.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [FrameNode](../../../arkts-api/ui/arkui/framenode/document.md) | Yes | No | Default value: **null** |

import { FrameNode } from '@kit.ArkUI'
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private text: string = ''

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let node: FrameNode = this.context.canvas
          node?.commonEvent.setOnVisibleAreaApproximateChange(
            { ratios: \[0, 1\], expectedUpdateInterval: 10},
            (isVisible: boolean, currentRatio: number) => {
              if (!isVisible && currentRatio <= 0.0) {
                this.text = 'Canvas is completely invisible.'
              }
              if (isVisible && currentRatio >= 1.0) {
                this.text = 'Canvas is fully visible.'
              }
              this.context.reset()
              this.context.font = '30vp sans-serif'
              this.context.fillText(this.text, 50, 50)
            }
          )
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/k1FPcOi8QAKi9Lc_tK9x6A/en-us_image_0000002537765812.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8BC030E3ADEE4E8B6CE97ED71A8B4A0E2740492D27CA6B87FCFC621B2B05AE2)

#### \[h2\]imageSmoothingQuality

Sets the image smoothing quality when **imageSmoothingEnabled** is set to **true**. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [ImageSmoothingQuality](#imagesmoothingquality) | No | No | Default value: **"low"** |

  // xxx.ets
  @Entry
  @Component
  struct ImageSmoothingQualityDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // Replace "common/images/example.jpg" with the image resource file you use.
    private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let ctx = this.context
            ctx.imageSmoothingEnabled = true
            ctx.imageSmoothingQuality = 'high'
            ctx.drawImage(this.img, 0, 0, 400, 200)
          })
      }
      .width('100%')
      .height('100%')
    }
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/TAk3kDGPRiGNWnBACqTTGA/en-us_image_0000002537925752.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F29D3EB3A53E189721FA33E1451C4B35DC0B99A51923B964308F8AF3798A674B)

#### \[h2\]direction

Sets the text direction. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| [CanvasDirection](#canvasdirection) | No | No | Default value: **"inherit"** |

  // xxx.ets
  @Entry
  @Component
  struct DirectionDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let ctx = this.context
            ctx.font = '48px serif';
            ctx.textAlign = 'start'
            ctx.fillText("Hi ltr!", 200, 50);

            ctx.direction = "rtl";
            ctx.fillText("Hi rtl!", 200, 100);
          })
      }
      .width('100%')
      .height('100%')
    }
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/ctjKx3lUQ7etIRvSs7RAeg/en-us_image_0000002568685529.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F424D635FC3789BF1FF3870EF12F8369DC888756A5F54B26C1FDF94628EA3C99)

#### \[h2\]filter

Sets the filter for an image. Any number of filters can be combined. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string | No | No | 
Available values are as follows:

\- **'none'**: no filter effect.

\- 'blur(<length>)': applies the Gaussian blur to the image. The value must be greater than or equal to 0. The unit can be px, vp, or rem. The default value is **blur(0px)**.

\- 'brightness(\[<number>|<percentage>\])': applies a linear multiplication to the image to make it look brighter or darker. The value can be a number or percentage. It must be greater than or equal to 0. The default value is **brightness(1)**.

\- 'contrast(\[<number>|<percentage>\])': adjusts the image contrast. The value can be a number or percentage. It must be greater than or equal to 0. The default value is **contrast(1)**.

\- 'grayscale(\[<number>|<percentage>\])': converts the image to a grayscale image. The value can be a number or percentage. The value range is \[0, 1\]. The default value is **grayscale(0)**.

\- 'hue-rotate(<angle>)': applies hue rotation to the image. The value ranges from 0deg to 360deg. The default value is **hue-rotate(0deg)**.

\- 'invert(\[<number>|<percentage>\])': inverts the input image. The value can be a number or percentage. The value range is \[0, 1\]. The default value is **invert (0)**.

\- 'opacity(\[<number>|<percentage>\])': sets the opacity of the image. The value can be a number or percentage. The value range is \[0, 1\]. The default value is **opacity(1)**.

\- 'saturate(\[<number>|<percentage>\])': sets the saturation of the image. The value can be a number or percentage. It must be greater than or equal to 0. The default value is **saturate(1)**.

\- 'sepia(\[<number>|<percentage>\])': converts the image to dark brown. The value can be a number or percentage. The value range is \[0, 1\]. The default value is **sepia(0)**.

 |

  // xxx.ets
  @Entry
  @Component
  struct FilterDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // Replace "common/images/example.jpg" with the image resource file you use.
    private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            let ctx = this.context
            let img = this.img

            ctx.drawImage(img, 0, 0, 100, 100);

            ctx.filter = 'grayscale(50%)';
            ctx.drawImage(img, 100, 0, 100, 100);

            ctx.filter = 'sepia(60%)';
            ctx.drawImage(img, 200, 0, 100, 100);

            ctx.filter = 'saturate(30%)';
            ctx.drawImage(img, 0, 100, 100, 100);

            ctx.filter = 'hue-rotate(90deg)';
            ctx.drawImage(img, 100, 100, 100, 100);

            ctx.filter = 'invert(100%)';
            ctx.drawImage(img, 200, 100, 100, 100);

            ctx.filter = 'opacity(25%)';
            ctx.drawImage(img, 0, 200, 100, 100);

            ctx.filter = 'brightness(0.4)';
            ctx.drawImage(img, 100, 200, 100, 100);

            ctx.filter = 'contrast(200%)';
            ctx.drawImage(img, 200, 200, 100, 100);

            ctx.filter = 'blur(5px)';
            ctx.drawImage(img, 0, 300, 100, 100);

            // Applying multiple filters
            ctx.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
            ctx.drawImage(img, 100, 300, 100, 100);
          })
      }
      .width('100%')
      .height('100%')
    }
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/1W4nNTybSIKbqYtND2HW1g/en-us_image_0000002568765539.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CF9573B185934F9D760C7CFFBFA26AB563E8ACA246EB45D15ADBEC8A814810F)

#### \[h2\]letterSpacing18+

Sets the letter spacing. This attribute is write-only. You can set its value through an assignment statement, but cannot obtain its current value through a read operation. If you attempt to read its current value, **undefined** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- |
| string | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | No | 
Spacing between characters.

When the LengthMetrics type is used:

The spacing is set according to the specified unit.

The FP, PERCENT, and LPX units are not supported and will be treated as invalid values.

Negative and fractional values are supported. When set to a fraction, the spacing is not rounded.

When the string type is used:

Percentage values are not supported and will be treated as invalid.

Negative and decimal values are supported. When set to a decimal value, the spacing is not rounded.

If no unit is specified (for example, **letterSpacing = '10'**) and **LengthMetricsUnit** is not set, the default unit is vp.

If **LengthMetricsUnit** is set to px, the default unit is px.

If the value of **letterSpacing** is specified with a unit (for example, **letterSpacing='10vp'**), the letter spacing is set based on the specified unit.

Default value: **0** (Invalid values are treated as the default value.)

**NOTE**

The LengthMetrics type is recommended for better performance.

 |

  // xxx.ets
  import { LengthMetrics, LengthUnit } from '@kit.ArkUI'

  @Entry
  @Component
  struct letterSpacingDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true)
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('rgb(213,213,213)')
          .onReady(() => {
            this.context.font = '30vp'
            this.context.letterSpacing = '10vp'
            this.context.fillText('hello world', 30, 50)
            this.context.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
            this.context.fillText('hello world', 30, 100)
          })
      }
      .width('100%')
      .height('100%')
    }
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/TnCoBRHPSdeICj8gwHxJsA/en-us_image_0000002537765814.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9B6D72E48567DF48E72B5C0748BB78B5E84023B652D3E92AA9002FB1D7EFA35)

#### Methods

Calls the following methods on hidden pages will result in cache data. Therefore, avoid frequent canvas refreshes on hidden pages.

#### \[h2\]fillRect

fillRect(x: number, y: number, w: number, h: number): void

Fills a rectangle on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the rectangle's top-left corner.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the rectangle's top-left corner.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| w | number | Yes | 

Width of the rectangle.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| h | number | Yes | 

Height of the rectangle.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct FillRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillRect(30, 30, 100, 100)
       })
      }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/H5VyCYJzQtmtbTDqxPVaig/en-us_image_0000002537925754.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABEE71A581982636E5F90D4B6B120C40A3A7DEA8A6C929C4B113979DEFCEAEE5)

#### \[h2\]strokeRect

strokeRect(x: number, y: number, w: number, h: number): void

Draws an outlined rectangle on the canvas without filling its interior.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the rectangle's top-left corner.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the rectangle's top-left corner.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| w | number | Yes | 

Width of the rectangle.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| h | number | Yes | 

Height of the rectangle.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct StrokeRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.strokeRect(30, 30, 200, 150)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Cq2cjmYERXu6WAw2hY6Z2A/en-us_image_0000002568685531.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8BE2D1DCC4DD16721B249EE815A025915FDA8E9FE7BEBC4FC61A041592B707D)

#### \[h2\]clearRect

clearRect(x: number, y: number, w: number, h: number): void

Clears the content in a rectangle on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the rectangle's top-left corner.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the rectangle's top-left corner.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| w | number | Yes | 

Width of the rectangle.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| h | number | Yes | 

Height of the rectangle.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct ClearRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(20,20,200,200)
          this.context.clearRect(30,30,150,100)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/isiDD7t6RySjFmNL-VqcAw/en-us_image_0000002568765541.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDBEF79C47BF97267951F4B3C26D417374FEBF9C389C32E548576A467D45EA87)

#### \[h2\]fillText

fillText(text: string, x: number, y: number, maxWidth?: number): void

Draws filled text on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | 
Text to draw.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| x | number | Yes | 

X-coordinate of the start point for text rendering.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the start point for text rendering.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| maxWidth | number | No | 

Maximum width allowed for the text.

**null** is treated as an invalid value and no rendering will be performed. **undefined**, **NaN**, or **Infinity** is treated as the default value.

Default value: no width restriction

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct FillText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.font = '30px sans-serif'
          this.context.fillText("Hello World!", 20, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/OK5Dw4QwSfOPovqDjim1Cg/en-us_image_0000002537765816.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDDF8A8E6545404AF003927AC9619065FEE38B0C96D2E4563BB8D9818FDE2F08)

#### \[h2\]strokeText

strokeText(text: string, x: number, y: number, maxWidth?: number): void

Draws stroked text on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | 
Text to draw.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| x | number | Yes | 

X-coordinate of the start point for text rendering.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the start point for text rendering.

**undefined**, **null**, **NaN**, and **Infinity** are treated as invalid values and no rendering will be performed.

Default unit: vp

 |
| maxWidth | number | No | 

Maximum width of the text.

**null** is treated as an invalid value and no rendering will be performed. **undefined**, **NaN**, or **Infinity** is treated as the default value.

Default unit: vp

Default value: no width restriction

 |

**Example**

// xxx.ets
@Entry
@Component
struct StrokeText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.font = '50vp sans-serif'
          this.context.strokeText("Hello World!", 20, 60)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3R3JfBi3T0mp7oy9uU5IJw/en-us_image_0000002537925756.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8F956D86F07457A9E374170954FBC458766AB3C1A3F24794880F82DD591E755)

#### \[h2\]measureText

measureText(text: string): TextMetrics

Returns a **TextMetrics** object used to obtain the width of specified text. Note that the width obtained may vary by device.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | 
Text to measure.

If the input value is **undefined** or **null**, the value is calculated based on "undefined" or "null".

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [TextMetrics](#textmetrics) | **TextMetrics** object. |

**Example**

// xxx.ets
@Entry
@Component
struct MeasureText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.font = '50px sans-serif'
          this.context.fillText("Hello World!", 20, 100)
          this.context.fillText("width:" + this.context.measureText("Hello World!").width, 20, 200)
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/L85x7AUvTsW-2jCTKwolOg/en-us_image_0000002568685533.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2B8E080316ABDA7D7B6E4A4B303220F9B1FEC6E9469927D323C53503AA0D58B)

#### \[h2\]stroke

stroke(): void

Strokes (outlines) this path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct Stroke {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.moveTo(125, 25)
          this.context.lineTo(125, 105)
          this.context.lineTo(175, 105)
          this.context.lineTo(175, 25)
          this.context.strokeStyle = 'rgb(255,0,0)'
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ECIt_sVjT5-kOgxxzulXDQ/en-us_image_0000002568765543.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B651FC5FD655141A85DD6A23CF6F945340C510C47FA0FD8A2F41A331899CD9FA)

#### \[h2\]stroke

stroke(path: Path2D): void

Strokes (outlines) a specified path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | [Path2D](../path2d/document.md) | Yes | 
**Path2D** path to draw.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |

**Example**

// xxx.ets
@Entry
@Component
struct Stroke {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private path2Da: Path2D = new Path2D()

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Da.moveTo(25, 25)
          this.path2Da.lineTo(25, 105)
          this.path2Da.lineTo(75, 105)
          this.path2Da.lineTo(75, 25)
          this.context.strokeStyle = 'rgb(0,0,255)'
          this.context.stroke(this.path2Da)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Y7WnyKKCQ7CLzPuV1FN9KQ/en-us_image_0000002537765818.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE766BBC75FE70BAA01B4F3C1EED0EFD45F3974DD0A91C5228D81B921AEBED7F)

#### \[h2\]beginPath

beginPath(): void

Creates a drawing path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct BeginPath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.lineWidth = 6
          this.context.strokeStyle = 'rgb(39,135,217)'
          this.context.moveTo(15, 80)
          this.context.lineTo(280, 160)
          this.context.stroke()
          this.context.beginPath()
          this.context.lineTo(300, 240)
          this.context.lineTo(15, 240)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/uNRlxRYeSKq0klihqm_-tg/en-us_image_0000002537925758.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B5D84884A2CE1A0F03543054D356B157059034F47790825386632AC13B4BE71)

#### \[h2\]moveTo

moveTo(x: number, y: number): void

Moves a drawing path from the current position to a target position on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the target position.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the target position.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/cqmUlGVHQ-6ZR7lpxkqpwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF3309B13A86CAF3F6C0A5975F0380F0B346E64DAC34FCAE1D374E271F3B8172)

In versions earlier than API version 18, if the **moveTo** API is not called or invalid arguments are passed to it, the path starts from (0,0).

Starting from API version 18, if the **moveTo** API is not executed or invalid arguments are passed to it, the path will begin at the start point of the first valid call to **lineTo**, **arcTo**, **bezierCurveTo**, or **quadraticCurveTo**.

**Example**

// xxx.ets
@Entry
@Component
struct MoveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/vfm748lPSAaLe3e6SGfmLg/en-us_image_0000002568685535.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88EAD5381FC2A5778404019290B501E1A22D25433047F2F407BDD32A2E6C8F38)

#### \[h2\]lineTo

lineTo(x: number, y: number): void

Connects the current point to a target position using a line.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the target position.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the target position.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/0i89d3oZSBeB4G_4XyQTiQ/en-us_image_0000002568765545.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=122CA4166D43E7C9CDA91A2CF952364767A68DEB730778D84DE6BF5CC69BDF54)

#### \[h2\]closePath

closePath(): void

Draws a closed path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
            this.context.beginPath()
            this.context.moveTo(30, 30)
            this.context.lineTo(110, 30)
            this.context.lineTo(70, 90)
            this.context.closePath()
            this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/7yTHybchRtOVs7aYsrA5Uw/en-us_image_0000002537765820.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA2736377A043D44C87166F05C788F4A31B2B96C414C3CE4A6E64B3B37B47057)

#### \[h2\]createPattern

createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null

Creates a pattern for image filling based on a specified source image and repetition mode.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| image | [ImageBitmap](../imagebitmap/document.md) | Yes | 
Source image. For details, see **ImageBitmap**.

**undefined** and **null** are treated as invalid values.

 |
| repetition | string | null | Yes | 

Repetition mode.

**'repeat'**: The image is repeated along both the x-axis and y-axis.

**'repeat-x'**: The image is repeated along the x-axis.

**'repeat-y'**: The image is repeated along the y-axis.

**'no-repeat'**: The image is not repeated.

**'clamp'**: Coordinates outside the original bounds are clamped to the edge of the image.

**'mirror'**: The image is mirrored with each repetition along the x-axis and y-axis.

**undefined** and **null** are treated as invalid values.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [CanvasPattern](../canvaspattern/document.md) | null | Pattern for image filling based on a specified source image and repetition mode. |

**Example**

// xxx.ets
@Entry
@Component
struct CreatePattern {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // Replace "common/images/icon.jpg" with the image resource file you use.
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let pattern = this.context.createPattern(this.img, 'repeat')
          if (pattern) {
            this.context.fillStyle = pattern
          }
          this.context.fillRect(0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/R0IMyP1HRO6uQ51Xe39WWw/en-us_image_0000002537925760.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4CC3C900359CED8E6EB33EB09F78C71623F235207B185E4CAEC0477C8A2D0F4)

#### \[h2\]bezierCurveTo

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

Creates a path for a cubic Bezier curve.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cp1x | number | Yes | 
X-coordinate of the first parameter of the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| cp1y | number | Yes | 

Y-coordinate of the first parameter of the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| cp2x | number | Yes | 

X-coordinate of the second parameter of the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| cp2y | number | Yes | 

Y-coordinate of the second parameter of the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| x | number | Yes | 

X-coordinate of the end point on the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the end point on the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private start: Point = { x: 50, y: 50 };
  private end: Point = { x: 250, y: 100 };
  private cp1: Point = { x: 200, y: 30 };
  private cp2: Point = { x: 130, y: 80 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let ctx = this.context;
          // Cubic Bezier curve
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          ctx.stroke();

          // Start point and end point
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 \* Math.PI); // Start point
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 \* Math.PI); // End point
          ctx.fill();

          // Control points
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp1.x, this.cp1.y, 5, 0, 2 \* Math.PI); // Control point 1
          ctx.arc(this.cp2.x, this.cp2.y, 5, 0, 2 \* Math.PI); // Control point 2
          ctx.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/aQJzvFCDS8a50URl2uqMqg/en-us_image_0000002568685537.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0866CB7974ED4C73776C7BDDEA23E2D29053B3AA278D0A4DEBB31A2A1AC008B)

#### \[h2\]quadraticCurveTo

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

Create a path for a quadratic Bezier curve.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cpx | number | Yes | 
X-coordinate of the Bezier curve parameter.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| cpy | number | Yes | 

Y-coordinate of the Bezier curve parameter.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| x | number | Yes | 

X-coordinate of the end point on the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the end point on the Bezier curve.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct QuadraticCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private start: Point = { x: 50, y: 20 };
  private end: Point = { x: 50, y: 100 };
  private cp: Point = { x: 230, y: 30 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let ctx = this.context;
          // Quadratic Bezier curve
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          ctx.stroke();

          // Start point and end point
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 \* Math.PI); // Start point
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 \* Math.PI); // End point
          ctx.fill();

          // Control point
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp.x, this.cp.y, 5, 0, 2 \* Math.PI);
          ctx.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/AIBmN8sRQwqkAMMy9qFcoQ/en-us_image_0000002568765547.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8ACE7658084CC5DD8692E6F8E46E665FC9266113F6E65D5D9BC226CDCE365CAD)

#### \[h2\]arc

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

Draws an arc on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the center point of the arc.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the center point of the arc.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| radius | number | Yes | 

Radius of the arc.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| startAngle | number | Yes | 

Start radian of the arc.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Unit: radian

 |
| endAngle | number | Yes | 

End radian of the arc.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Unit: radian

 |
| counterclockwise | boolean | No | 

Whether to draw the arc counterclockwise.

**true**: Draw the arc counterclockwise.

**false**: Draw the arc clockwise.

The default value is **false**. If this parameter is set to **null** or **undefined**, the default value is used.

 |

**Example**

// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/3WVOCGvUTC67mI6HrUiBNA/en-us_image_0000002537765822.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07DDBEF8B7884C5F30AAB3EB862F975D36E7E4A209B29DF93B7896D202FC8D0F)

#### \[h2\]arcTo

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

Creates a circular arc using the given control points and radius.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x1 | number | Yes | 
X-coordinate of the first control point.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y1 | number | Yes | 

Y-coordinate of the first control point.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| x2 | number | Yes | 

X-coordinate of the second control point.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y2 | number | Yes | 

Y-coordinate of the second control point.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| radius | number | Yes | 

Radius of the arc.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct ArcTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          // Tangent
          this.context.beginPath()
          this.context.strokeStyle = '#808080'
          this.context.lineWidth = 1.5;
          this.context.moveTo(360, 20);
          this.context.lineTo(360, 170);
          this.context.lineTo(110, 170);
          this.context.stroke();
          
          // Arc
          this.context.beginPath()
          this.context.strokeStyle = '#000000'
          this.context.lineWidth = 3;
          this.context.moveTo(360, 20)
          this.context.arcTo(360, 170, 110, 170, 150)
          this.context.stroke()
          
          // Start point
          this.context.beginPath();
          this.context.fillStyle = '#00ff00';
          this.context.arc(360, 20, 4, 0, 2 \* Math.PI);
          this.context.fill();
          
          // Control points
          this.context.beginPath();
          this.context.fillStyle = '#ff0000';
          this.context.arc(360, 170, 4, 0, 2 \* Math.PI);
          this.context.arc(110, 170, 4, 0, 2 \* Math.PI);
          this.context.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Y2oKyPfvRZ6hBQdwx2XQpQ/en-us_image_0000002537925762.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B1D9C0F11306D007B8ED384DA2B848C9F7CBEB595A5881478FCA7E8E6F664E3)

In this example, the arc created by **arcTo()** is black, and the two tangents of the arc are gray. The control points are marked in red, and the start point is indicated in green.

You can visualize two tangents: One tangent extends from the start point to the first control point, and the other tangent extends from the first control point to the second control point. The **arcTo()** API creates an arc between these two tangents, ensuring that the arc is tangent to both lines at the points of contact.

#### \[h2\]ellipse

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

Draws an ellipse in the specified rectangular region on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the ellipse center.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the ellipse center.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| radiusX | number | Yes | 

Radius of the ellipse on the x-axis.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| radiusY | number | Yes | 

Radius of the ellipse on the y-axis.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| rotation | number | Yes | 

Rotation angle of the ellipse.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Unit: radian

 |
| startAngle | number | Yes | 

Angle of the start point for drawing the ellipse.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Unit: radian

 |
| endAngle | number | Yes | 

Angle of the end point for drawing the ellipse.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Unit: radian

 |
| counterclockwise | boolean | No | 

Whether to draw the ellipse counterclockwise.

**true**: Draw the ellipse counterclockwise.

**false**: Draw the ellipse clockwise.

The default value is **false**. If this parameter is set to **null** or **undefined**, the default value is used.

 |

**Example**

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.ellipse(200, 200, 50, 100, Math.PI \* 0.25, Math.PI \* 0.5, Math.PI \* 2, false)
          this.context.stroke()
          this.context.beginPath()
          this.context.ellipse(200, 300, 50, 100, Math.PI \* 0.25, Math.PI \* 0.5, Math.PI \* 2, true)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/4VAb5Tf2Rui1-w-s8Imj8A/en-us_image_0000002568685539.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D989E688D9A346106D1E7F9D9EC307654E05567943ED377B6C83A59F8854484)

#### \[h2\]rect

rect(x: number, y: number, w: number, h: number): void

Creates a rectangle on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the rectangle's top-left corner.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the rectangle's top-left corner.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| w | number | Yes | 

Width of the rectangle.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| h | number | Yes | 

Height of the rectangle.

In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100\*100 rectangle at (20, 20)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/tqisksvrTqe0kCq88usZUA/en-us_image_0000002568765549.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D5919326E2080E699018AB2423118548F8AB5047BD2B3B1D6BAD39AA47C2DA8)

#### \[h2\]roundRect20+

roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void

Creates a rounded rectangle path. This API does not directly render content. To draw the rounded rectangle on the canvas, use **fill** or **stroke**.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
X-coordinate of the rectangle's top-left corner.

The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.

To draw a complete rectangle, the value range is \[0, Canvas width).

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the rectangle's top-left corner.

The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.

To draw a complete rectangle, the value range is \[0, Canvas height).

Default unit: vp

 |
| w | number | Yes | 

Width of the rectangle. A negative value indicates that the rectangle is drawn from right to left.

The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.

To draw a complete rectangle, the value range is \[-x, Canvas width - x\].

Default unit: vp

 |
| h | number | Yes | 

Height of the rectangle. A negative value indicates upward drawing.

The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.

To draw a complete rectangle, the value range is \[-y, Canvas height - y\].

Default unit: vp

 |
| radii | number | Array<number> | No | 

Number or list of arc radii used for the rectangle corners.

If the parameter type is number, it applies to the arc radius of all rectangle corners.

If the parameter type is Array<number>, the array contains 1 to 4 numbers, interpreted as follows:

\[Arc radius of all rectangle corners\]

\[Arc radius of the top-left and bottom-right rectangle corners, and arc radius of the top-right and bottom-left rectangle corners\]

\[Arc radius of the top-left rectangle corner, arc radius of the top-right and bottom-left rectangle corners, and arc radius of the bottom-right rectangle corner\]

\[Arc radius of the top-left rectangle corner, arc radius of the top-right rectangle corner, arc radius of the bottom-right rectangle corner, and arc radius of the bottom-left rectangle corner\]

If **radii** contains a negative number or the number of items in the list is not within \[1,4\], error code 103701 is reported.

Default value: **0**. **null** and **undefined** are treated as the default value.

If the arc radius exceeds the width and height of the rectangle, it will be proportionally scaled down to match the corresponding dimensions.

Default unit: vp

 |

**Error codes**

For details about the error codes, see [Canvas Component Error Codes](../../../error-codes/ui/canvas-component-error-codes/document.md).

| ID | Error Message | Possible Causes |
| :-- | :-- | :-- |
| 103701 | Parameter error. | 1\. The param radii is a list that has zero or more than four elements; 2. The param radii contains negative value. |

**Example**

The following example shows how to draw six rounded rectangles:

1.  Create a rounded rectangle with the start point at (10 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners, and fill the rectangle.
    
2.  Create a rounded rectangle with the start point at (120 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners, and fill the rectangle.
    
3.  Create a rounded rectangle with the start point at (10 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the top-left and bottom-right rectangle corners, arc radius of 20 vp for the top-right and bottom-left rectangle corners, and stroke the rectangle.
    
4.  Create a rounded rectangle with the start point at (120 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the top-left rectangle corner, arc radius of 20 vp for the top-right and bottom-left rectangle corners, arc radius of 30 vp for the bottom-right rectangle corner, and stroke the rectangle.
    
5.  Create a rounded rectangle with the start point at (10 vp, 230 vp), width and height of 100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively. Then, stroke the rectangle.
    
6.  Create a rounded rectangle with the start point at (220 vp, 330 vp), width and height of -100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively. Then, stroke the rectangle.
    

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

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
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          try {
            this.context.fillStyle = '#707070'
            this.context.beginPath()
            // Create a rounded rectangle with the start point at (10 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners.
            this.context.roundRect(10, 10, 100, 100, 10)
            // Create a rounded rectangle with the start point at (120 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners.
            this.context.roundRect(120, 10, 100, 100, \[10\])
            this.context.fill()
            this.context.beginPath()
            // Create a rounded rectangle with the start point at (10 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the top-left and bottom-right rectangle corners, and arc radius of 20 vp for the top-right and bottom-left rectangle corners.
            this.context.roundRect(10, 120, 100, 100, \[10, 20\])
            // Create a rounded rectangle with the start point at (120 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the top-left rectangle corner, arc radius of 20 vp for the top-right and bottom-left rectangle corners, and arc radius of 30 vp for the bottom-right rectangle corner.
            this.context.roundRect(120, 120, 100, 100, \[10, 20, 30\])
            // Create a rounded rectangle with the start point at (10 vp, 230 vp), width and height of 100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively.
            this.context.roundRect(10, 230, 100, 100, \[10, 20, 30, 40\])
            // Create a rounded rectangle with the start point at (220 vp, 330 vp), width and height of -100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively.
            this.context.roundRect(220, 330, -100, -100, \[10, 20, 30, 40\])
            this.context.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(\`Failed to create roundRect. Code: ${e.code}, message: ${e.message}\`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/3IM2of2ERDe_LaOJ0YsdXA/en-us_image_0000002537765824.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6E3FD276359BB4DA90507072E7A480AEF2062CCDC0FB4129C36485D49ED3C00)

#### \[h2\]fill

fill(fillRule?: CanvasFillRule): void

Fills the current path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fillRule | [CanvasFillRule](#canvasfillrule) | No | 
Rule by which to determine whether a point is inside or outside the area to fill.

The options are **"nonzero"** and **"evenodd"**.

Invalid values **undefined** and **null** are treated as the default value.

Default value: **"nonzero"**

 |

**Example**

// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100\*100 rectangle at (20, 20)
          this.context.fill()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/_Qoh1GORTqC_6tofnJW5FQ/en-us_image_0000002537925764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06B51BF739BF057DB5BEA0C4152ADFC31F882BBF9D8C33D2B1F14FF2D590AE38)

#### \[h2\]fill

fill(path: Path2D, fillRule?: CanvasFillRule): void

Fills a specified path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | [Path2D](../path2d/document.md) | Yes | 
**Path2D** path to fill.

**undefined** and **null** are treated as invalid values.

 |
| fillRule | [CanvasFillRule](#canvasfillrule) | No | 

Rule by which to determine whether a point is inside or outside the area to fill.

The options are **"nonzero"** and **"evenodd"**.

Invalid values **undefined** and **null** are treated as the default value.

Default value: **"nonzero"**

 |

**Example**

// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          // Fill path
          this.context.fillStyle = '#00ff00'
          this.context.fill(region, "evenodd")
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/cAyBufGfRfSJHo5_19WL0A/en-us_image_0000002568685541.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=161880BF065839AE90B37D42EE4EEC86DB7B1D8AC0A7B685A0FF4869B9845417)

#### \[h2\]clip

clip(fillRule?: CanvasFillRule): void

Sets the current path to a clipping path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fillRule | [CanvasFillRule](#canvasfillrule) | No | 
Rule by which to determine whether a point is inside or outside the area to clip.

The options are **"nonzero"** and **"evenodd"**.

Invalid values **undefined** and **null** are treated as the default value.

Default value: **"nonzero"**

 |

**Example**

// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(0, 0, 100, 200)
          this.context.stroke()
          this.context.clip()
          this.context.fillStyle = "rgb(255,0,0)"
          this.context.fillRect(0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/jzCmicbgTUWLZzFassaIig/en-us_image_0000002568765551.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61D658AE66DB92E63C38414DDDA22B04FC519929132A839EC3D2C0165934875D)

#### \[h2\]clip

clip(path: Path2D, fillRule?: CanvasFillRule): void

Sets a specified path as the clipping path.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | [Path2D](../path2d/document.md) | Yes | 
**Path2D** path to clip.

**undefined** and **null** are treated as invalid values.

 |
| fillRule | [CanvasFillRule](#canvasfillrule) | No | 

Rule by which to determine whether a point is inside or outside the area to clip.

The options are **"nonzero"** and **"evenodd"**.

Invalid values **undefined** and **null** are treated as the default value.

Default value: **"nonzero"**

 |

**Example**

// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          this.context.clip(region,"evenodd")
          this.context.fillStyle = "rgb(0,255,0)"
          this.context.fillRect(0, 0, this.context.width, this.context.height)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/pXKW61GdQ3q-NP5WLFjgbQ/en-us_image_0000002537765826.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=203953E11FDB4475CB6948C037A280E2C1F3573C28F8D96E3A58FBC36D46AC84)

#### \[h2\]reset12+

reset(): void

Resets this **CanvasRenderingContext2D** object to its default state and clears the background buffer, drawing state stack, defined paths, and styles.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct Reset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = '#0000ff'
          this.context.fillRect(20, 20, 150, 100)
          this.context.reset()
          this.context.fillRect(20, 150, 150, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eYoeIs6vSXCOk9q1_czwbQ/en-us_image_0000002537925766.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FEEB246502C64AF451EEC5507DB0938F9988AC4F5F8CFFBBB28C7A4109AEAB1)

#### \[h2\]saveLayer12+

saveLayer(): void

Saves this layer.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct saveLayer {
private settings: RenderingContextSettings = new RenderingContextSettings(true)
private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

build() {
  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
    Canvas(this.context)
      .width('100%')
      .height('100%')
      .backgroundColor('#ffff00')
      .onReady(() =>{
        this.context.fillStyle = "#0000ff"
        this.context.fillRect(50,100,300,100)
        this.context.fillStyle = "#00ffff"
        this.context.fillRect(50,150,300,100)
        this.context.globalCompositeOperation = 'destination-over'
        this.context.saveLayer()
        this.context.globalCompositeOperation = 'source-over'
        this.context.fillStyle = "#ff0000"
        this.context.fillRect(100,50,100,300)
        this.context.fillStyle = "#00ff00"
        this.context.fillRect(150,50,100,300)
        this.context.restoreLayer()
      })
  }
  .width('100%')
  .height('100%')
}
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/1D3g_c_zR6icJ850k_gigw/en-us_image_0000002568685543.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A06B29BED5B8807CE23A4BB94C5335804E12C897ACFB2E01FF12B483B1D09C7C)

#### \[h2\]restoreLayer12+

restoreLayer(): void

Restores the image transformation and cropping state to the state before **saveLayer**, and then draws the layer onto the canvas. For the sample code, see the code for **saveLayer**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]resetTransform

resetTransform(): void

Resets the current transform to the identity matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct ResetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.setTransform(1,0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.resetTransform()
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/eIPAY17rSM-jVeXgwE5B9g/en-us_image_0000002568765553.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65F5FAEB134A6DBD9D6DCBF545B2B6493992BD87A01584726B3788C9C9CB4344)

#### \[h2\]rotate

rotate(angle: number): void

Rotates a canvas clockwise around its coordinate axes.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| angle | number | Yes | 
Clockwise rotation angle. You can convert degrees to radians using the following formula: degree \* Math.PI/180.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Unit: radian

 |

**Example**

// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rotate(45 \* Math.PI / 180)
          this.context.fillRect(70, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/dq4Z8Ks1TwmgVaAvHl5hDQ/en-us_image_0000002537765828.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D8B38BFBF2D23518EDE341E18A432F1CFEE4B04DAF23D23C536F98B0F43623A)

#### \[h2\]scale

scale(x: number, y: number): void

Scales the canvas based on the given scale factors.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
Horizontal scale factor.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **0**, **null**, **undefined**, and negative numbers cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **0**, **null**, **undefined**, and negative numbers cause the current API to have no effect, and other APIs with valid arguments continue to render correctly.

 |
| y | number | Yes | 

Vertical scaling factor. Negative numbers are not supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **0**, **null**, **undefined**, and negative numbers cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **0**, **null**, **undefined**, and negative numbers cause the current API to have no effect, and other APIs with valid arguments continue to render correctly.

 |

**Example**

// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 3
          this.context.strokeRect(30, 30, 50, 50)
          this.context.scale(2, 2) // Scale to 200%
          this.context.strokeRect(30, 30, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/1NDPhg-GQmuWGM_T2Q4Fkg/en-us_image_0000002537925768.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=553949E5589C67B864FAAF222EC307F1F5D7B22A1392235B0D7BE8C33BAAD651)

#### \[h2\]transform

transform(a: number, b: number, c: number, d: number, e: number, f: number): void

Defines a transformation matrix. To transform a graph, you only need to set parameters of the matrix. The coordinates of the graph are multiplied by the matrix values to obtain new coordinates of the transformed graph. You can use the matrix to implement multiple transform effects.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/fRyugCvFT0K-omsYM51ptw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD8BC233DADBDAB2B12B2F9118B204C2D19B9FFC06CE7CD70E7722B533675CE6)

The coordinates of each point in the graph after transformation can be calculated using the following formula:

**x** and **y** represent coordinates before transformation, and **x'** and **y'** represent coordinates after transformation.

-   x' = a \* x + c \* y + e
    
-   y' = b \* x + d \* y + f
    

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| a | number | Yes | 
Cell at row 1, column 1 of the transformation matrix. **scaleX**: horizontal scaling value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| b | number | Yes | 

Cell at row 2, column 1 of the transformation matrix. **skewY**: vertical skewing value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| c | number | Yes | 

Cell at row 1, column 2 of the transformation matrix. **skewX**: horizontal skewing value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| d | number | Yes | 

Cell at row 2, column 2 of the transformation matrix. **scaleY**: vertical scaling value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| e | number | Yes | 

Cell at row 1, column 3 of the transformation matrix. **translateX**: horizontal translation distance. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| f | number | Yes | 

Cell at row 2, column 3 of the transformation matrix. **translateY**: vertical translation distance. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct Transform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(0,74,175)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/bm_znuhBRiaWapoB0BKf_g/en-us_image_0000002568685545.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=372DF0D40827F6B6AC43A1443DD53209A20C238FEE865B177E2C3F4031B10DB2)

#### \[h2\]setTransform

setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void

Resets the existing transformation matrix and creates a new transformation matrix by using the same parameters as the **transform()** API.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/tY61vnsAQrGz9GpTHj2KNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4AE03BE6FEE76AF24FD33A5FF9CC9198E4DC5783525382A406C46FCFD50FB81)

The coordinates of each point in the graph after transformation can be calculated using the following formula:

**x** and **y** represent coordinates before transformation, and **x'** and **y'** represent coordinates after transformation.

-   x' = a \* x + c \* y + e
    
-   y' = b \* x + d \* y + f
    

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| a | number | Yes | 
**scaleX**: horizontal scaling value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| b | number | Yes | 

**skewY**: vertical skewing value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| c | number | Yes | 

**skewX**: horizontal skewing value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| d | number | Yes | 

**scaleY**: vertical scaling value. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

 |
| e | number | Yes | 

**translateX**: horizontal translation distance. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| f | number | Yes | 

**translateY**: vertical translation distance. A negative value is supported.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct SetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(23,169,141)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.setTransform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/UHE7eR11SVGC92CmXlHCbQ/en-us_image_0000002568765555.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C011BB0A33E9E2562462F21918C0A91B9E334AEFA9DC371412FB249D4DDFADA0)

#### \[h2\]setTransform

setTransform(transform?: Matrix2D): void

Resets the current transformation to the identity matrix, and then creates a new transformation matrix based on the specified **Matrix2D** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transform | [Matrix2D](../matrix2d/document.md) | No | 
Transformation matrix.

**undefined** and **null** are treated as invalid values.

Default value: **null**

 |

**Example**

// xxx.ets
@Entry
@Component
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(100, 20, 50, 50);
          this.context1.setTransform(1, 0.5, -0.5, 1, 10, 10);
          this.context1.fillRect(100, 20, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(100, 20, 50, 50);
          let storedTransform = this.context1.getTransform();
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(100, 20, 50, 50);
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ceJOa3VUQraMfsQwy5sOPQ/en-us_image_0000002537765830.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F8B01C90A35B5FD6C21271A9BEFEB6FBBD3EE1ADDA9A2B95844B13142C340B6)

#### \[h2\]getTransform

getTransform(): Matrix2D

Obtains the current transformation matrix being applied to the context.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix2D](../matrix2d/document.md) | Current transformation matrix applied to the context. |

**Example**

// xxx.ets
@Entry
@Component
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(50, 50, 50, 50);
          this.context1.setTransform(1.2, Math.PI/8, Math.PI/6, 0.5, 30, -25);
          this.context1.fillRect(50, 50, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(50, 50, 50, 50);
          let storedTransform = this.context1.getTransform();
          console.info("Matrix \[scaleX = " + storedTransform.scaleX + ", scaleY = " + storedTransform.scaleY +
          ", rotateX = " + storedTransform.rotateX + ", rotateY = " + storedTransform.rotateY +
          ", translateX = " + storedTransform.translateX + ", translateY = " + storedTransform.translateY + "\]")
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(50,50,50,50);
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/JoWnRigxRaappvNuIGiIIw/en-us_image_0000002537925770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35FF83D6FC93F79D86997CC7A7E35524CE6098D99C0203DBE926A87D990D48C6)

#### \[h2\]translate

translate(x: number, y: number): void

Moves the origin of the coordinate system.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | 
Distance to translate on the x-axis.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |
| y | number | Yes | 

Distance to translate on the y-axis.

In versions earlier than API version 18, values **NaN** and **Infinity** cause the failure to call the drawing APIs following this API for rendering. Values **null** and **undefined** cause the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** value causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillRect(10, 10, 50, 50)
          this.context.translate(70, 70)
          this.context.fillRect(10, 10, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/9e34Qrx8Toem3AetJA2ZDw/en-us_image_0000002568685547.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E4F6AA3FB5AFAB28A4E74C42395F7BA4030622CCCA705DB25AFBE45CD25AD3E)

#### \[h2\]drawImage

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

Draws an image on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9, except that **PixelMap** objects are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| image | [ImageBitmap](../imagebitmap/document.md) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | 
Image resource. For details, see **ImageBitmap** or **PixelMap**.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| dx | number | Yes | 

X-coordinate of the top-left corner of the drawing area on the canvas.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |
| dy | number | Yes | 

Y-coordinate of the top-left corner of the drawing area on the canvas.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Replace "common/images/example.jpg" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ojkzZgjrQ--sG7MlmdtUqQ/en-us_image_0000002568765557.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B08210C8E93265CB98C6F320D8BBF8C0313925F552627508295AAC66921408A)

#### \[h2\]drawImage

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

Draws an image by stretching or compressing it to the specified dimensions.

**Widget capability**: This API can be used in ArkTS widgets since API version 9, except that **PixelMap** objects are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| image | [ImageBitmap](../imagebitmap/document.md) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | 
Image resource. For details, see **ImageBitmap** or **PixelMap**.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| dx | number | Yes | 

X-coordinate of the top-left corner of the drawing area on the canvas.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |
| dy | number | Yes | 

Y-coordinate of the top-left corner of the drawing area on the canvas.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |
| dw | number | Yes | 

Width of the drawing area. If the width of the drawing area is different from that of the cropped image, the latter will be stretched or compressed to the former.

Negative values, **undefined**, and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |
| dh | number | Yes | 

Height of the drawing area. If the height of the drawing area is different from that of the cropped image, the latter will be stretched or compressed to the former.

Negative values, **undefined**, and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Replace "common/images/example.jpg" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 300, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/d2fv-6-yQ8K3XuttfIK51A/en-us_image_0000002537765832.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEF4E9FAED2804D199296107A7D0049F46D4459D09B142B23667702B1CB9D705)

#### \[h2\]drawImage

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

Draws a cropped portion of an image by stretching or compressing it to the specified dimensions.

**Widget capability**: This API can be used in ArkTS widgets since API version 9, except that **PixelMap** objects are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| image | [ImageBitmap](../imagebitmap/document.md) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | 
Image resource. For details, see **ImageBitmap** or **PixelMap**.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| sx | number | Yes | 

X-coordinate of the top-left corner of the rectangle used to crop the source image.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

If the type of **image** is **ImageBitmap**, the default unit is vp.

If the type of **image** is **PixelMap**, the default unit is px in versions earlier than API version 18 and vp in API version 18 and later.

 |
| sy | number | Yes | 

Y-coordinate of the top-left corner of the rectangle used to crop the source image.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

If the type of **image** is **ImageBitmap**, the default unit is vp.

If the type of **image** is **PixelMap**, the default unit is px in versions earlier than API version 18 and vp in API version 18 and later.

 |
| sw | number | Yes | 

Target width to crop the source image.

Negative values, **undefined**, and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

If the type of **image** is **ImageBitmap**, the default unit is vp.

If the type of **image** is **PixelMap**, the default unit is px in versions earlier than API version 18 and vp in API version 18 and later.

 |
| sh | number | Yes | 

Target height to crop the source image.

Negative values, **undefined**, and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

If the type of **image** is **ImageBitmap**, the default unit is vp.

If the type of **image** is **PixelMap**, the default unit is px in versions earlier than API version 18 and vp in API version 18 and later.

 |
| dx | number | Yes | 

X-coordinate of the top-left corner of the drawing area on the canvas.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |
| dy | number | Yes | 

Y-coordinate of the top-left corner of the drawing area on the canvas.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed.

Default unit: vp

 |
| dw | number | Yes | 

Width of the drawing area.

Negative values, **undefined**, and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed. If the width of the drawing area is different from that of the cropped image, the latter will be stretched or compressed to the former.

Default unit: vp

 |
| dh | number | Yes | 

Height of the drawing area.

Negative values, **undefined**, and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid and no rendering will be performed. If the height of the drawing area is different from that of the cropped image, the latter will be stretched or compressed to the former.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Replace "common/images/example.jpg" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/zmVRnG26QH6icx2LBViRMA/en-us_image_0000002537925772.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3988E85B45BB4854E86FD4037B1A1C642A099D82D38CCACAC5B813384C72AFA9)

#### \[h2\]createImageData

createImageData(sw: number, sh: number): ImageData

Creates a blank [ImageData](../imagedata/document.md) object of a specified size. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it. The **createImageData** example is identical to the [putImageData](#putimagedata) example.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sw | number | Yes | 
Width of the **ImageData** object.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sh | number | Yes | 

Height of the **ImageData** object.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageData](../imagedata/document.md) | New **ImageData** object. |

#### \[h2\]createImageData

createImageData(imageData: ImageData): ImageData

Creates an [ImageData](../imagedata/document.md) object with the same width and height of an existing **ImageData** object. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it. The **createImageData** example is identical to the [putImageData](#putimagedata) example.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| imageData | [ImageData](../imagedata/document.md) | Yes | 
Existing **ImageData** object.

Values **undefined** and **null** are treated as **ImageData** with its width and height set to **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageData](../imagedata/document.md) | New **ImageData** object. |

#### \[h2\]getPixelMap

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

Obtains the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) object created with the pixels within the specified area on the canvas. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sx | number | Yes | 
X-coordinate of the top-left corner of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sy | number | Yes | 

Y-coordinate of the top-left corner of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sw | number | Yes | 

Width of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sh | number | Yes | 

Height of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | **PixelMap** object. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dW8kRqhUT4m55jWfoedtDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F89D3FBBC65083681FA425B13DD26D401A9816E6966474C427A6EF979BF0792)

The DevEco Studio Previewer does not support displaying content drawn with **setPixelMap**.

// xxx.ets
@Entry
@Component
struct GetPixelMap {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // Replace "common/images/example.jpg" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 100, 100, 130, 130)
          let pixelmap = this.context.getPixelMap(150, 150, 130, 130)
          this.context.setPixelMap(pixelmap)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ZO_OzEZpSo2TLlCUczCZ3g/en-us_image_0000002568685549.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DA602E5C879E9773295CEC8C3EA92A84915DB578244E6BE1AAF10F51B169636)

#### \[h2\]setPixelMap

setPixelMap(value?: PixelMap): void

Draws the input [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) object on the canvas. The example is the same as that of **getPixelMap**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | 
**PixelMap** object that contains pixel values.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

Default value: **null**

 |

#### \[h2\]getImageData

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

Obtains the [ImageData](../imagedata/document.md) object created with the pixels within the specified area on the canvas. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sx | number | Yes | 
X-coordinate of the top-left corner of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sy | number | Yes | 

Y-coordinate of the top-left corner of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sw | number | Yes | 

Width of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| sh | number | Yes | 

Height of the output area.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageData](../imagedata/document.md) | New **ImageData** object. |

**Example**

// xxx.ets
@Entry
@Component
struct GetImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // Replace "/common/images/1234.png" with the image resource file you use.
  private img:ImageBitmap = new ImageBitmap("/common/images/1234.png")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.drawImage(this.img,0,0,130,130)
          let imageData = this.context.getImageData(50,50,130,130)
          this.context.putImageData(imageData,150,150)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/9fN3SjgeRFq_WgFpkRRIyA/en-us_image_0000002568765559.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=534DDDCFB74642E4F720C1B62FB70C8C2FEED964CC4CC18C58AED79850F1B898)

#### \[h2\]putImageData

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

Puts an [ImageData](../imagedata/document.md) object onto a rectangular area on the canvas.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| imageData | [ImageData](../imagedata/document.md) | Yes | 
**ImageData** object with pixels to put onto the canvas.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| dx | number | string10+ | Yes | 

X-axis offset of the rectangular area on the canvas.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| dy | number | string10+ | Yes | 

Y-axis offset of the rectangular area on the canvas.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let imageDataNum = this.context.createImageData(100, 100)
          let imageData = this.context.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data\[i + 0\] = 112
            imageData.data\[i + 1\] = 112
            imageData.data\[i + 2\] = 112
            imageData.data\[i + 3\] = 255
          }
          this.context.putImageData(imageData, 10, 10)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/yzl2qbVCSPKszt9x1q7pqg/en-us_image_0000002537765834.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A83E597A1E9D4463F3DF230E0FBEC46DAC9979B20F6B74855DF804BB15CDBD6)

#### \[h2\]putImageData

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void

Fills the new rectangular area with the [ImageData](../imagedata/document.md) data after cropping.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| imageData | [ImageData](../imagedata/document.md) | Yes | 
**ImageData** object with pixels to put onto the canvas.

**undefined** and **null** are treated as invalid values and no rendering will be performed.

 |
| dx | number | string10+ | Yes | 

X-axis offset of the rectangular area on the canvas.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| dy | number | string10+ | Yes | 

Y-axis offset of the rectangular area on the canvas.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| dirtyX | number | string10+ | Yes | 

X-axis offset of the upper left corner of the rectangular area relative to that of the source image.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| dirtyY | number | string10+ | Yes | 

Y-axis offset of the upper left corner of the rectangular area relative to that of the source image.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| dirtyWidth | number | string10+ | Yes | 

Width of the rectangular area to crop the source image.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |
| dirtyHeight | number | string10+ | Yes | 

Height of the rectangular area to crop the source image.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as **0**.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let imageDataNum = this.context.createImageData(100, 100)
          let imageData = this.context.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data\[i + 0\] = 112
            imageData.data\[i + 1\] = 112
            imageData.data\[i + 2\] = 112
            imageData.data\[i + 3\] = 255
          }
          this.context.putImageData(imageData, 10, 10, 0, 0, 100, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/REDF-iJtRkm4fE2X_1HkWg/en-us_image_0000002537925774.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE21CD9AAB3F46198084AB33EBE1E258A557261210A6B51DFC300AA74C21DFE0)

#### \[h2\]setLineDash

setLineDash(segments: number\[\]): void

Sets the dash line style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| segments | number\[\] | Yes | 
An array of numbers that specify distances to alternately draw a line and a gap.

**undefined** and **null** are treated as invalid values.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct SetLineDash {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() =>{
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.setLineDash(\[10,20\])
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/DJ_L2-WLR_iJN4k81y4ImQ/en-us_image_0000002568685551.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87D6BEEE2FDC64C6AC7A2F904952531017EC3B30754844597AA7831B9280285C)

#### \[h2\]getLineDash

getLineDash(): number\[\]

Obtains the dash line style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | 
Interval of alternate line segments and the length of spacing.

Default unit: vp

 |

**Example**

// xxx.ets
@Entry
@Component
struct CanvasGetLineDash {
  @State message: string = 'Hello World'
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#D5D5D5')
          .onReady(() => {
            this.context.arc(100, 75, 50, 0, 6.28)
            this.context.setLineDash(\[10, 20\])
            this.context.stroke()
            let res = this.context.getLineDash()
            this.message = JSON.stringify(res)
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/AyZeixLuQCepu7yy-zCptg/en-us_image_0000002568765561.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17ECB1E92C2FC92C2C470FE8E1B19E96A33FF2ABA7F28F8A5F791AB9E002573A)

#### \[h2\]transferFromImageBitmap

transferFromImageBitmap(bitmap: ImageBitmap): void

Displays the specified **ImageBitmap** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bitmap | [ImageBitmap](../imagebitmap/document.md) | Yes | **ImageBitmap** object to display. |

**Example**

// xxx.ets
@Entry
@Component
struct TransferFromImageBitmap {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let imageData = this.offContext.createImageData(100, 100)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data\[i + 0\] = 255
            imageData.data\[i + 1\] = 0
            imageData.data\[i + 2\] = 60
            imageData.data\[i + 3\] = 80
          }
          this.offContext.putImageData(imageData, 10, 10)
          let image = this.offContext.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/m3csgxsRRSSGzJJU_f-6Rw/en-us_image_0000002537765836.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29A70E9A3AD022F01E2E6A1B35524B2698022E33BB35A6109B79BFBD525AFE05)

#### \[h2\]toDataURL

toDataURL(type?: string, quality?: any): string

Creates a data URL that contains a representation of an image. This API involves time-consuming memory copy. Therefore, avoid frequent calls to it.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | No | 
Image format.

The options are **image/png**, **image/jpeg**, and **image/webp**.

Invalid values **undefined** and **null** are treated as the default value.

Default value: **image/png**

 |
| quality | any | No | 

Image quality, which ranges from 0 to 1, when the image format is **image/jpeg** or **image/webp**. If the set value is beyond the value range, the default value **0.92** is used.

Invalid values **undefined**, **null**, **NaN**, and **Infinity** are treated as the default value.

Default value: **0.92**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Image URL. |

**Example**

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  @State toDataURL: string = ""

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(100)
        .height(100)
        .onReady(() =>{
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(0,0,100,100)
          this.toDataURL = this.context.toDataURL("image/png", 0.92)
        })
      Text(this.toDataURL)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffff00')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/5fqEh8J6QM-BdEEJ9EoJLQ/en-us_image_0000002537925776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BE3E698C44D2DE1917E01A846D5EDA1C5CDEF50D18F1F3C36863E79123B72D4)

#### \[h2\]restore

restore(): void

Restores the saved drawing context.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/TtS7NexdSJWTPtLU37hpmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E53C92547EE19A5611DDAF4D40A3D3EE798BD52439E6DDF7A9DBD1602D900A4F)

When the number of calls to **restore()** does not exceed the number of calls to **save()**, this API pops the saved drawing state from the stack and restores the attributes, clipping path, and transformation matrix of the **CanvasRenderingContext2D** object.

If the number of calls to **restore()** exceeds the number of calls to **save()**, this API does nothing.

If there is no saved state, this API does nothing.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.save() // save the default state
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(20, 20, 100, 100)
          this.context.restore() // restore to the default state
          this.context.fillRect(150, 75, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/IZ7-S0zZSKC9ggHqTEH2dw/en-us_image_0000002568685553.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B3BA2B02EAD2727C9E418D2B57C40F1D19CE62BA999E551DDBFA70001623D45)

#### \[h2\]save

save(): void

Saves all states of the canvas in the stack. This API is usually called when the drawing state needs to be saved.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.save() // save the default state
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(20, 20, 100, 100)
          this.context.restore() // restore to the default state
          this.context.fillRect(150, 75, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/XzHPUxHAQyGOrzajia8ejA/en-us_image_0000002568685553.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34EC7EB5D821C77619DD460C225869EBE207034024450B6AA8CC1847504372C8)

#### \[h2\]createLinearGradient

createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient

Creates a linear gradient.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x0 | number | Yes | 
X-coordinate of the start point.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| y0 | number | Yes | 

Y-coordinate of the start point.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| x1 | number | Yes | 

X-coordinate of the end point.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| y1 | number | Yes | 

Y-coordinate of the end point.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [CanvasGradient](../canvasgradient/document.md) | New **CanvasGradient** object used to create a gradient on the canvas. |

**Example**

// xxx.ets
@Entry
@Component
struct CreateLinearGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let grad = this.context.createLinearGradient(50,0, 300,100)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(23,169,141)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 400, 400)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/7qCFkPUBQTOSkTyR8ud4Ng/en-us_image_0000002537925740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=573A180788E82D11168BD380A49E07E2A5478A26D625DC896B2C289B63BB4927)

#### \[h2\]createRadialGradient

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient

Creates a radial gradient.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x0 | number | Yes | 
X-coordinate of the center of the start circle.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| y0 | number | Yes | 

Y-coordinate of the center of the start circle.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| r0 | number | Yes | 

Radius of the start circle, which must be a non-negative finite number.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| x1 | number | Yes | 

X-coordinate of the center of the end circle.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| y1 | number | Yes | 

Y-coordinate of the center of the end circle.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |
| r1 | number | Yes | 

Radius of the end circle, which must be a non-negative finite number.

If the value is **undefined** or **null**, this API returns **undefined**. **NaN** and **Infinity** are treated as invalid values.

Default unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [CanvasGradient](../canvasgradient/document.md) | New **CanvasGradient** object used to create a gradient on the canvas. |

**Example**

// xxx.ets
@Entry
@Component
struct CreateRadialGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let grad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(112,112,112)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 440, 440)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/j-fmGcgPT02xdOW-NMnqTw/en-us_image_0000002568765563.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F9677DEFF44DD75EE295B0AC6CD500DA9801EF211C060326A4F880B2AB065D4)

#### \[h2\]createConicGradient10+

createConicGradient(startAngle: number, x: number, y: number): CanvasGradient

Creates a conic gradient.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startAngle | number | Yes | 
Angle at which the gradient starts. The angle measurement starts horizontally from the right side of the center and moves clockwise.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid.

Unit: radian

 |
| x | number | Yes | 

X-coordinate of the center of the conic gradient.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid.

Default unit: vp

 |
| y | number | Yes | 

Y-coordinate of the center of the conic gradient.

Invalid values **undefined** and **null** are treated as **0**. **NaN** and **Infinity** are treated as invalid.

Default unit: vp

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [CanvasGradient](../canvasgradient/document.md) | New **CanvasGradient** object used to create a gradient on the canvas. |

**Example**

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffff')
        .onReady(() => {
          let grad = this.context.createConicGradient(0, 50, 80)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(213,213,213)')
          grad.addColorStop(1.0, 'rgb(23,160,141)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/paj9XS23T1KnnXv5l0ZFUQ/en-us_image_0000002537765838.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D75DFB5089BD31C3371B465F365B25C727135227BDCA0FBF4062C7CE34FF0CE1)

#### \[h2\]on('onAttach')13+

on(type: 'onAttach', callback: () => void): void

Subscribes to the event when a **CanvasRenderingContext2D** object is bound to a **Canvas** component.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'onAttach'** in this case.

**undefined** and **null** are treated as invalid values.

 |
| callback | () => void | Yes | 

Callback triggered when the **CanvasRenderingContext2D** object is bound to the **Canvas** component.

**undefined** and **null** are treated as invalid values.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/waMv_sxwRyq9R1gtj0fQiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=597DD4D048AB4D73E6E1D2C2F74F84237BEFB33C94AB6BAC1BB2ED72DC80D7BD)

A **CanvasRenderingContext2D** object can only be bound to one **Canvas** component at a time.

When a **CanvasRenderingContext2D** object is bound to a **Canvas** component, the **onAttach** callback is triggered, indicating that the [canvas](#canvas13) object is accessible.

Avoid performing drawing operations in the **onAttach** callback. Make sure the **Canvas** component has completed its **[onReady](../canvas/document.md#events)** event before performing any drawing.

The **onAttach** callback is triggered when:

1.  A **Canvas** component is created and bound to a **CanvasRenderingContext2D** object.
    
2.  A **CanvasRenderingContext2D** object is bound to a new **Canvas** component.
    

#### \[h2\]on('onDetach')13+

on(type: 'onDetach', callback: () => void): void

Subscribes to the event when a **CanvasRenderingContext2D** object is unbound from a **Canvas** component.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'onDetach'** in this case.

**undefined** and **null** are treated as invalid values.

 |
| callback | () => void | Yes | 

Callback triggered when the **CanvasRenderingContext2D** object is unbound from the **Canvas** component.

**undefined** and **null** are treated as invalid values.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/UfM5UjtYSMS82mLHm4fOWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AFE64BD8BE85558666D6FDDF234C6E1044FF2CE9DA3C5B7555C69EE84AB8C54)

When a **CanvasRenderingContext2D** object is unbound from a **Canvas** component, the **onDetach** callback is triggered. In this case, cease any drawing operations.

The **onDetach** callback is triggered when:

1.  A **Canvas** component is destroyed and unbound from a **CanvasRenderingContext2D** object.
    
2.  A **CanvasRenderingContext2D** object is bound to a different\*\* Canvas\*\* component, causing the existing binding to be released.
    

#### \[h2\]off('onAttach')13+

off(type: 'onAttach', callback?: () => void): void

Unsubscribes from the event when a **CanvasRenderingContext2D** object is bound to a **Canvas** component.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'onAttach'** in this case.

**undefined** and **null** are treated as invalid values.

 |
| callback | () => void | No | 

If this parameter is left empty, all callbacks triggered after the **CanvasRenderingContext2D** object is bound to the **Canvas** component are unsubscribed.

If this parameter is not left empty, the callback corresponding to the bind event is unsubscribed.

**undefined** and **null** are treated as invalid values.

 |

#### \[h2\]off('onDetach')13+

off(type: 'onDetach', callback?: () => void): void

Unsubscribes from the event when a **CanvasRenderingContext2D** object is unbound from a **Canvas** component.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'onDetach'** in this case.

**undefined** and **null** are treated as invalid values.

 |
| callback | () => void | No | 

If this parameter is left empty, all callbacks triggered after the **CanvasRenderingContext2D** object is unbound from the **Canvas** component are unsubscribed.

If this parameter is not left empty, the callback corresponding to the unbind event is unsubscribed.

**undefined** and **null** are treated as invalid values.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { FrameNode } from '@kit.ArkUI'

// xxx.ets
@Entry
@Component
struct AttachDetachExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private scroller: Scroller = new Scroller()
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15\]
  private node: FrameNode | null = null
  attachCallback = () => {
    console.info('CanvasRenderingContext2D attached to the canvas frame node.')
    this.node = this.context.canvas
  }
  detachCallback = () => {
    console.info('CanvasRenderingContext2D detach from the canvas frame node.')
    this.node = null
  }

  aboutToAppear(): void {
    try {
      this.context.on('onAttach', this.attachCallback)
      this.context.on('onDetach', this.detachCallback)
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(\`Error code: ${e.code}, message: ${e.message}\`);
    }
  }

  aboutToDisappear(): void {
    try {
      this.context.off('onAttach')
      this.context.off('onDetach')
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(\`Error code: ${e.code}, message: ${e.message}\`);
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Scroll(this.scroller) {
        Flex({ direction: FlexDirection.Column }) {
          ForEach(this.arr, (item: number) => {
            Row() {
              if (item == 3) {
                Canvas(this.context)
                  .width('100%')
                  .height(150)
                  .backgroundColor('rgb(213,213,213)')
                  .onReady(() => {
                    this.context.font = '30vp sans-serif'
                    this.node?.commonEvent.setOnVisibleAreaApproximateChange(
                      { ratios: \[0, 1\], expectedUpdateInterval: 10 },
                      (isVisible: boolean, currentRatio: number) => {
                        if (!isVisible && currentRatio <= 0.0) {
                          console.info('Canvas is completely invisible.')
                        }
                        if (isVisible && currentRatio >= 1.0) {
                          console.info('Canvas is fully visible.')
                        }
                      }
                    )
                  })
              } else {
                Text(item.toString())
                  .width('100%')
                  .height(150)
                  .backgroundColor('rgb(39,135,217)')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 5 })
              }
            }
          }, (item: number) => item.toString())
        }
      }
      .width('90%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/PImXjs9wTQCkHEhD46mO5w/en-us_image_0000002537925778.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35899969EC8484F61FF8D37D2D424B1B989F440157A583BEEBC94035246D900C)

#### \[h2\]startImageAnalyzer12+

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

Configures and starts the AI analyzer. This API uses a promise to return the result. Before use, set [enableAnalyzer](../canvas/document.md#enableanalyzer12) to **true** to enable the image AI analyzer.

Because the image frame used for analysis is the one captured when this API is called, pay attention to the invoking time of this API.

Repeated calls to this method before completion trigger an error callback. For the sample code, see the code for **stopImageAnalyzer**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/0zVKoenkQ9K8Ww7JEQErbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C091A424E13FCDACB42874E058F58811C6353F689BFF78F7A19ACA3DA2DD5CC8)

The image analysis type cannot be dynamically modified.

When image changes are detected, the analysis result is automatically destroyed. You can call this API again to start analysis.

This API depends on device capabilities. If it is called on an incompatible device, an error code is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [ImageAnalyzerConfig](../../images-and-videos/image-analysis-types/document.md#imageanalyzerconfig12) | Yes | 
Settings of the AI analyzer.

**undefined** and **null** are treated as invalid values.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [AI Image Analyzer Error Codes](../../../error-codes/ui/ai-image-analyzer-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |

#### \[h2\]stopImageAnalyzer12+

stopImageAnalyzer(): void

Stops AI image analysis. The content displayed by the AI image analyzer will be destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/nmTstCUHR5uDh-47MEWf-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F98ADEEF8F2DD15B21A488A4A8CA1EAC5103CC62850FE5F562C6A9455D8479E)

If this API is called when the **startImageAnalyzer** API has not yet returned any result, an error is reported.

This feature depends on device capabilities.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageAnalyzerExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\]
  }
  // Replace 'common/images/example.png' with the image resource file you use.
  private img = new ImageBitmap('common/images/example.png')
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\],
    aiController: this.aiController
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
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
              console.info("error code: " + error.code)
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
        .width(200)
        .height(200)
        .enableAnalyzer(true)
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### CanvasDirection

type CanvasDirection = "inherit" | "ltr" | "rtl"

Defines the current text direction. The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| inherit | Inherits the text direction set in the general attributes of the canvas component. If the **direction** attribute is not set on the canvas component, the system text direction is used. |
| ltr | The text direction is from left to right. |
| rtl | The text direction is from right to left. |

#### CanvasFillRule

type CanvasFillRule = "evenodd" | "nonzero"

Defines the fill pattern algorithm used to determine whether a point is inside or outside a path. The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| evenodd | 
The inside part of a shape is determined based on whether the counting result is an odd number or not.

This rule determines whether a point is inside a shape by casting a ray from the point on the canvas in any direction and counting the number of intersections between the ray and the shape path. If the number of intersections is odd, the point is inside the shape. Otherwise, the point is outside the shape.

 |
| nonzero | 

The inside part of a shape is determined based on whether the counting result is zero or not.

This rule determines whether a point is inside a shape by casting a ray from the point on the canvas in any direction and checking the intersections between the ray and the shape path. The initial count is **0**: assign a direction value to each segment of the path, add 1 each time the path crosses the ray from left to right, and subtract 1 each time it crosses the ray from right to left. If the final result is **0**, the point is outside the shape. Otherwise, the point is inside the shape.

 |

**Example**

// xxx.ets
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213, 213, 213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '60px sans-serif'
          offContext.fillStyle = 'rgb(39, 135, 217)';
          // Non-zero rule (nonzero).
          offContext.beginPath();
          offContext.arc(100, 100, 60, 0, Math.PI \* 2);
          offContext.arc(100, 100, 20, 0, Math.PI \* 2);
          offContext.fill('nonzero'); // Use the non-zero rule.
          offContext.fillText('nonzero', 65, 200)
          // Even-odd rule (evenodd).
          offContext.beginPath();
          offContext.arc(250, 100, 60, 0, Math.PI \* 2);
          offContext.arc(250, 100, 20, 0, Math.PI \* 2);
          offContext.fill('evenodd'); // Use the even-odd rule.
          offContext.fillText('evenodd', 215, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/wr2Xlh9sQSqdjez_bjkeyA/en-us_image_0000002568685555.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1533CB1B19E13899C28F2F20AF02B3EB85A00E21800D48D57E819DEFAAD70A72)

#### CanvasLineCap

type CanvasLineCap = "butt" | "round" | "square"

Defines the end caps for each line being drawn. The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| butt | The ends of the line are squared off, and the line does not extend beyond its two endpoints. |
| round | The line is extended at the endpoints by a half circle whose diameter is equal to the line width. |
| square | The line is extended at the endpoints by a rectangle whose width is equal to half the line width and height equal to the line width. |

#### CanvasLineJoin

type CanvasLineJoin = "bevel" | "miter" | "round"

Defines the type of join between two non-zero-length segments (lines, arcs, and curves). The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| bevel | The intersection is a triangle. The rectangular corner of each line is independent. |
| miter | The intersection has a miter corner by extending the outside edges of the lines until they meet. You can view the effect of this attribute in **miterLimit**. |
| round | The intersection is a sector, whose radius at the rounded corner is equal to the line width. |

#### CanvasTextAlign

type CanvasTextAlign = "center" | "end" | "left" | "right" | "start"

Defines the type of text alignment. The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| center | The text is center-aligned. |
| start | The text is aligned with the start bound. |
| end | The text is aligned with the end bound. |
| left | The text is left-aligned. |
| right | The text is right-aligned. |

#### CanvasTextBaseline

type CanvasTextBaseline = "alphabetic" | "bottom" | "hanging" | "ideographic" | "middle" | "top"

Defines the text baseline type. The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| alphabetic | The text baseline is the normal alphabetic baseline. |
| bottom | The text baseline is at the bottom of the text bounding box. Its difference from the ideographic baseline is that the ideographic baseline does not consider letters in the next line. |
| hanging | The text baseline is a hanging baseline over the text. |
| ideographic | The text baseline is the ideographic baseline. If a character exceeds the alphabetic baseline, the ideographic baseline is located at the bottom of the excessive character. |
| middle | The text baseline is in the middle of the text bounding box. |
| top | The text baseline is on the top of the text bounding box. |

#### ImageSmoothingQuality

type ImageSmoothingQuality = "high" | "low" | "medium"

Defines the image smoothing quality. The value type is a union of the types listed in the table below.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| low | Low quality. |
| medium | Medium quality. |
| high | High quality. |

#### TextMetrics

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | Yes | No | Width of the text. Read-only. |
| height | number | Yes | No | Height of the text. Read-only. |
| actualBoundingBoxAscent | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the top of the bounding rectangle used to render the text. Read-only. |
| actualBoundingBoxDescent | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the bottom of the bounding rectangle used to render the text. Read-only. |
| actualBoundingBoxLeft | number | Yes | No | Distance parallel to the baseline from the alignment point determined by the [CanvasRenderingContext2D.textAlign](#canvastextalign) attribute to the left side of the bounding rectangle of the text. Read-only. |
| actualBoundingBoxRight | number | Yes | No | Distance parallel to the baseline from the alignment point determined by the [CanvasRenderingContext2D.textAlign](#canvastextalign) attribute to the right side of the bounding rectangle of the text. Read-only. |
| alphabeticBaseline | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the alphabetic baseline of the line box. Read-only. |
| emHeightAscent | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the top of the em square in the line box. Read-only. |
| emHeightDescent | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the bottom of the em square in the line box. Read-only. |
| fontBoundingBoxAscent | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the top of the bounding rectangle of all the fonts used to render the text. Read-only. |
| fontBoundingBoxDescent | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the bottom of the bounding rectangle of all the fonts used to render the text. Read-only. |
| hangingBaseline | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the hanging baseline of the line box. Read-only. |
| ideographicBaseline | number | Yes | No | Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](#canvastextbaseline) attribute to the ideographic baseline of the line box. Read-only. |

#### RenderingContextSettings

Configures the settings of a **CanvasRenderingContext2D** object, including whether to enable anti-aliasing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/9kdK-whJReGIxfVsjzymXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D22AEC02B7D9FDC3804FC33D567F3CBFF34F41C5030100565D625CB3C6F1E041)

The anti-aliasing effect configured in **RenderingContextSettings** does not apply to text drawing.

#### \[h2\]constructor

constructor(antialias?: boolean)

Constructs a **CanvasRenderingContext2D** object. Anti-aliasing can be enabled.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| antialias | boolean | No | 
Whether to enable anti-aliasing.

A value of **undefined** is treated as the default value.

**false**: Disable anti-aliasing. **true**: Enable anti-aliasing.

Default value: **false**

 |

#### \[h2\]Attributes

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| antialias | boolean | No | Yes | 
Whether to enable anti-aliasing.

A value of **undefined** is treated as the default value.

**false**: Disable anti-aliasing. **true**: Enable anti-aliasing.

Default value: **false**

 |
