# Matrix2D

**Matrix2D** allows you to perform matrix transformation, such as scaling, rotating, and translating.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/JuTidEHmRuOjuOrfwtXUeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=854B137EAFF89B39BDA4BD6472434DFEF517B83CE24A2DE3B4EAF17102E0183F)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Constructor

#### \[h2\]constructor10+

constructor()

Constructs a two-dimensional transformation matrix object. The default value is a matrix whose attributes are all 0.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor12+

constructor(unit: LengthMetricsUnit)

Constructs a two-dimensional transformation matrix object. The default value is a matrix whose attributes are all 0. The unit mode of the Matrix2D object can be configured.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| unit | [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12) | Yes | 
Unit mode of the **Matrix2D** object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md).

For abnormal values NaN and Infinity, the default values are used.

Default value: DEFAULT

 |

#### Attributes

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scaleX | number | No | Yes | 
Horizontal scaling coefficient. The value range is not limited.

If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

 |
| scaleY | number | No | Yes | 

Vertical scaling coefficient. The value range is not limited.

If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

 |
| rotateX | number | No | Yes | 

Horizontal skew coefficient. The value range is not limited.

If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

 |
| rotateY | number | No | Yes | 

Vertical skew coefficient. The value range is not limited.

If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

 |
| translateX | number | No | Yes | 

Horizontal translation distance. The value range is not limited.

If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

Default unit: vp.

 |
| translateY | number | No | Yes | 

Vertical translation distance. The value range is not limited.

If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

Default unit: vp.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/95Qg0NgqTNqXpUNxlbgOiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0DB86CCF55E793D6CCCBF547EDB7435E9D6FC68845790A45F4AF5B978F2ECA5)

You can use the [px2vp](../../common-definitions/pixel-units/document.md#px2vpdeprecated) API for unit conversion.

**Example**

// xxx.ets
@Entry
@Component
struct Parameter {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 20, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/pxOvHiNKSfi4Sl4X_ui92A/en-us_image_0000002537765842.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6896A2208609E31B0E0453CBD238ABF826DA15779CBB3AF7CA9BC4F43A428C4E)

#### Methods

#### \[h2\]identity

identity(): Matrix2D

Creates an identity matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Identity matrix. |

**Example**

// xxx.ets
@Entry
@Component
struct Identity {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 20, 50, 50)
          this.matrix = this.matrix.identity()
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 100, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/-2N3k-VjTlKkcSalPPxf0g/en-us_image_0000002537925782.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D8B4E7EB40C6B70FE4917BA0F5C1F69EA0C24CED71A5DDC8CE036A68303C83B)

#### \[h2\]invert

invert(): Matrix2D

Obtains an inverse of this matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Inverse of the current matrix. |

**Example**

// xxx.ets
@Entry
@Component
struct Invert {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 110, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.invert()
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 110, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/5bhYb50hRd6qSWrGcfCbfg/en-us_image_0000002568685559.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2218E0BA388D390585853A39F6B5F2C0FE02B265329D1D51C612A9ED62209A9)

## multiply(deprecated)

multiply(other?: Matrix2D): Matrix2D

Multiplies this matrix by the target matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9. This API is an empty API.

This API is deprecated since API version 10, and does not provide any actual rendering effects. Therefore, no examples are provided.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| other | Matrix2D | No | 
Target matrix.

Invalid values **undefined** and **null** are treated as invalid inputs.

Default value: **null**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Matrix of the multiplication result. |

## rotate(deprecated)

rotate(rx?: number, ry?: number): Matrix2D

Performs a rotation operation on this matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9. This API is an empty API.

This API is deprecated since API version 10. You are advised to use [rotate](#rotate10) instead.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rx | number | No | 
Horizontal coordinate of the rotation point. The value range is not limited.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default unit: vp.

 |
| ry | number | No | 

Vertical coordinate of the rotation point. The value range is not limited.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default unit: vp.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Matrix of the rotation result. |

**Example**

// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(50, 110, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.rotate(5, 5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(50, 110, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/fMgmBHiHSmq8zx43jeTH7w/en-us_image_0000002568765569.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC6FDE6ECEE0BD67D900E3115313E0387B450A64376EB597F180610B8C7A349C)

#### \[h2\]rotate10+

rotate(degree: number, rx?: number, ry?: number): Matrix2D

Performs a right multiplication rotation operation on this matrix, with the specified rotation point as the transform origin.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| degree | number | Yes | 
Rotation angle. The value range is not limited. Positive angles represent clockwise rotation. You can convert the angle to radians using the following formula: degree \* Math.PI/180.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default unit: radian

 |
| rx | number | No | 

Horizontal coordinate of the rotation point. The value range is not limited.

Default unit: vp.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default value: **0**.

 |
| ry | number | No | 

Vertical coordinate of the rotation point. The value range is not limited.

Default unit: vp.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Matrix of the rotation result. |

**Example**

// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(60, 80, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.rotate(-60 \* Math.PI / 180, 5, 5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(60, 80, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_zX2_Dl0Rce62Iycfb9qrw/en-us_image_0000002537765844.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEF5D1DE53D071302AEC687EF5735B904A2BA8939ED398E9050359A4DD745F5B)

#### \[h2\]translate

translate(tx?: number, ty?: number): Matrix2D

Performs a left multiplication translation operation on this matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tx | number | No | 
Horizontal translation distance. The value range is not limited.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default unit: vp.

Default value: **0**.

 |
| ty | number | No | 

Vertical translation distance. The value range is not limited.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default unit: vp.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Matrix of the translation result. |

**Example**

// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(40, 20, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = 0
          this.matrix.rotateY = 0
          this.matrix.translateX = 0
          this.matrix.translateY = 0
          this.matrix.translate(100, 100)
          this.context.setTransform(this.matrix)
          this.context.fillRect(40, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/rxyVUkPQTJSvnjS66H7bOA/en-us_image_0000002537925784.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D0E3E6C2E0EF725BAC74367E9DEC4CD6496B97DEED0FD03598D822E369F0612)

#### \[h2\]scale

scale(sx?: number, sy?: number): Matrix2D

Performs a right multiplication scaling operation on this matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Parameter | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sx | number | No | 
Horizontal scaling ratio coefficient. The value range is not limited.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default value: **1.0**.

 |
| sy | number | No | 

Vertical scaling ratio coefficient. The value range is not limited.

Invalid values **undefined** and **null** are treated as invalid inputs. **NaN** and **Infinity** values will trigger **Matrix2D** exceptions.

Default value: **1.0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Matrix2D | Matrix of the scale result. |

**Example**

// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(120, 70, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.scale(0.5, 0.5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(120, 70, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/-cS5EaPFTISUFzPOF1TGLw/en-us_image_0000002568685561.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD8AFA1D354B38B6FD229FC7A2F865EBA7130B9848398E7A3FEB6A75886D51F0)
