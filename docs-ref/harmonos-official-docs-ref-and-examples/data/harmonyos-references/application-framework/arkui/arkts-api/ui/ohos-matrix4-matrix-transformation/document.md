# @ohos.matrix4 (Matrix Transformation)

Provides matrix transformation capabilities for components, including translation, rotation, and scaling. For details, see [Transformation](../../../arkts-components/universal-attributes/visual-effects/transformation/document.md).

**Matrix4** can be used in the following scenarios:

In [Transformation](../../../arkts-components/universal-attributes/visual-effects/transformation/document.md), the [transform](../../../arkts-components/universal-attributes/visual-effects/transformation/document.md#transform18) API uses the **Matrix4** object to display the matrix transformation in two-dimensional transformation, and the [transform3D](../../../arkts-components/universal-attributes/visual-effects/transformation/document.md#transform3d20) API uses the **Matrix4** object to set the three-dimensional transformation matrix for a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/a7siZbM1RFWZupDKcRRf1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54BDEE89CFDBB8245CE11784BF7B4F70F851B86AB1BCE99F46F63279C3A740E9)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { matrix4 } from '@kit.ArkUI';

#### matrix4.init

init(options: \[number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number\]): Matrix4Transit

Matrix constructor, which is used to create a 4 x 4 matrix with the input parameters. Column-major order is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | 
\[number,number,number,number,

number,number,number,number,

number,number,number,number,

number,number,number,number\]

 | Yes | 

A number array whose length is 16 (4 x 4). For details, see **4 x 4 matrix description**.

Value range of each number: (-∞, +∞)

Default value:

\[1, 0, 0, 0,

0, 1, 0, 0,

0, 0, 1, 0,

0, 0, 0, 1\]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | 4 x 4 matrix object created based on the input parameters. |

**4 x 4 matrix description**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| m00 | number | Yes | Scaling value of the x-axis. The default value is **1** for the identity matrix. |
| m01 | number | Yes | The second value, which is affected by the rotation or tilt of the x, y, and z axes. |
| m02 | number | Yes | The third value, which is affected by the rotation of the x, y, and z axes. |
| m03 | number | Yes | The fourth value, which is affected by perspective projection. |
| m10 | number | Yes | The fifth value, which is affected by the rotation or tilt of the x, y, and z axes. |
| m11 | number | Yes | Scaling value of the y-axis. The default value is **1** for the identity matrix. |
| m12 | number | Yes | The seventh value, which is affected by the rotation of the x, y, and z axes. |
| m13 | number | Yes | The eighth value, which is affected by perspective projection. |
| m20 | number | Yes | The ninth value, which is affected by the rotation of the x, y, and z axes. |
| m21 | number | Yes | The tenth value, which is affected by the rotation of the x, y, and z axes. |
| m22 | number | Yes | Scaling value of the z-axis. The default value is **1** for the identity matrix. |
| m23 | number | Yes | The 12th value, which is affected by perspective projection. |
| m30 | number | Yes | Translation value of the x-axis, in px. The default value is **0** for the identity matrix. |
| m31 | number | Yes | Translation value of the y-axis, in px. The default value is **0** for the identity matrix. |
| m32 | number | Yes | Translation value of the z-axis, in px. The default value is **0** for the identity matrix. |
| m33 | number | Yes | Valid in homogeneous coordinates, presenting the perspective projection effect. |

**Example**

import { matrix4 } from '@kit.ArkUI';

// Create a 4 x 4 matrix.
let matrix = matrix4.init(
  \[1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0\]);

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // Replace $r("app.media.zh") with the image resource file you use.
      Image($r("app.media.zh"))
        .width("40%")
        .height(100)
        .transform(matrix)
    }
  }
}

#### matrix4.identity

identity(): Matrix4Transit

Constructs an identity matrix.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Identity matrix object. |

**Example**

// The effect of matrix 1 is the same as that of matrix 2.
import { matrix4 } from '@kit.ArkUI';

let matrix1 = matrix4.init(
  \[1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0\]);
let matrix2 = matrix4.identity();

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // Replace $r("app.media.zh") with the image resource file you use.
      Image($r("app.media.zh"))
        .width("40%")
        .height(100)
        .transform(matrix1)
      // Replace $r("app.media.zh") with the image resource file you use.
      Image($r("app.media.zh"))
        .width("40%")
        .height(100)
        .margin({ top: 150 })
        .transform(matrix2)
    }
  }
}

#### Matrix4Transit

Implements a **Matrix4Transit** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]copy

copy(): Matrix4Transit

Copies this matrix object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Copy object of the current matrix. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().scale({ x: 1.5 });
  private matrix2 = this.matrix1.copy().translate({ x: 200 });
  imageSize: Length = '300px';

  build() {
    Column({ space: "50px" }) {
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
        .transform(this.matrix1)
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
        .transform(this.matrix2)
    }.alignItems(HorizontalAlign.Center)
    .height('100%').width("100%")
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ltFUndT5SaKOFdgUjxeeNQ/en-us_image_0000002568685047.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E09F58EB1A66E1D7B62C35C929CDDD1C32C77EB9C03FDF0D1013616E9DBFC5F5)

#### \[h2\]combine

combine(options: Matrix4Transit): Matrix4Transit

Combines the effects of two matrices to generate a new matrix object. The matrix that calls this API will be changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Matrix4Transit](#matrix4transit) | Yes | Matrix object to be combined. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Object after matrix combination. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 200 });
  private matrix2 = matrix4.identity().scale({ x: 2 });

  build() {
    Column() {
      // Before matrix transformation
      // Replace $r("app.media.icon") with the image resource file you use.
      Image($r("app.media.icon"))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
      // Translate the x-axis by 200px, and then scale it twice to obtain the resultant matrix.
      // Replace $r("app.media.icon") with the image resource file you use.
      Image($r("app.media.icon"))
        .transform(this.matrix1.copy().combine(this.matrix2))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/7fDOf6UbTJmC63udxm4QNQ/en-us_image_0000002568765057.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=310B76A8E2C3F6F90FB9ACBB0280F48ABBB0D5220E7D28F21FDCE4CB527620C8)

#### \[h2\]invert

invert(): Matrix4Transit

Inverts this matrix object. The matrix that calls this API will be changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Inverse matrix object of the current matrix. |

**Example**

import { matrix4 } from '@kit.ArkUI';

// The effect of matrix 1 (width scaled up by 2x) is opposite to that of matrix 2 (width scaled down by 2x).
let matrix1 = matrix4.identity().scale({ x: 2 });
let matrix2 = matrix1.copy().invert();

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // Replace $r("app.media.zh") with the image resource file you use.
      Image($r("app.media.zh"))
        .width(200)
        .height(100)
        .transform(matrix1)
        .margin({ top: 100 })
      // Replace $r("app.media.zh") with the image resource file you use.
      Image($r("app.media.zh"))
        .width(200)
        .height(100)
        .margin({ top: 150 })
        .transform(matrix2)
    }
  }
}

#### \[h2\]translate

translate(options: TranslateOption): Matrix4Transit

Translates this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TranslateOption](#translateoption) | Yes | Translation configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after the translation. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 100, y: 200, z: 30 });

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1")).transform(this.matrix1)
        .width("40%")
        .height(100)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/bg70-4gjRjKk5ItmSp2PHw/en-us_image_0000002537765332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E4675000479D2EE46D1DD313A4DB13C9AFF6B21F5A04AE55B626B8C0D59E626)

#### \[h2\]scale

scale(options: ScaleOption): Matrix4Transit

Scales this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ScaleOption](#scaleoption) | Yes | Scaling configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after the scaling. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .scale({
      x: 2,
      y: 3,
      z: 4,
      centerX: 50,
      centerY: 50
    });

  build() {
    Column() {
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage")).transform(this.matrix1)
        .width("300px")
        .height("300px")
    }.width("100%").height("100%").justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Nw567wXgR-aqzRkVg5ymaw/en-us_image_0000002537925272.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78CE17440F74D0489BE00D8441A0EA411E50E78D09B0DD278089D32A5CDE6A8F)

#### \[h2\]skew12+

skew(x: number, y: number): Matrix4Transit

Skews this matrix object along the x and y axes. The matrix that calls this API will be changed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Amount of skewing on the x-axis. |
| y | number | Yes | Amount of skewing on the y-axis. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after the skewing. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().skew(2, 3);

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1")).transform(this.matrix1)
        .height(100)
        .margin({
          top: 300
        })
    }
    .width("100%")
    .height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zav4hx9qQTK7vT4RXvULYg/en-us_image_0000002568685049.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23403048CC3AC576129A23757E99E5000BF32A290E5561703E0156170ED0229B)

#### \[h2\]rotate

rotate(options: RotateOption): Matrix4Transit

Rotates this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RotateOption](#rotateoption) | Yes | Rotation configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after the rotation. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .rotate({
      x: 1,
      y: 1,
      z: 2,
      angle: 30
    });

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1")).transform(this.matrix1)
        .width("40%")
        .height(100)
    }.width("100%").margin({ top: 50 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/nUP_xPlMRVapMUC8VIHkzg/en-us_image_0000002568765059.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6BA3F0C185163B26953AB8307D5BEFBB18D28B1190ACCDE3C6DA45BD23290AD)

#### \[h2\]transformPoint

transformPoint(options: \[number, number\]): \[number, number\]

Applies the current transformation effect to a coordinate point.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | \[number, number\] | Yes | Point to be transformed. |

**Return value**

| Type | Description |
| :-- | :-- |
| \[number, number\] | Point object after matrix transformation |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private originPoint: number\[\] = \[50, 50\];
  private matrix\_1 = matrix4.identity().translate({ x: 150, y: -50 });
  private transformPoint = this.matrix\_1.transformPoint(\[this.originPoint\[0\], this.originPoint\[1\]\]);
  private matrix\_2 = matrix4.identity().translate({ x: this.transformPoint\[0\], y: this.transformPoint\[1\] });

  build() {
    Column() {
      Text(\`Coordinates before matrix transformation: \[${this.originPoint}\]\`)
        .fontSize(16)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r("app.media.image"))
        .width('600px')
        .height('300px')
        .margin({ top: 50 })
      Text(\`Coordinates after matrix transformation: \[${this.transformPoint}\]\`)
        .fontSize(16)
        .margin({ top: 100 })
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r("app.media.image"))
        .width('600px')
        .height('300px')
        .margin({ top: 50 })
        .transform(this.matrix\_2)
    }.width("100%").padding(50)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Bokjq5NbSBmioFaVbAEcag/en-us_image_0000002537765334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66F371ECD1F2804307468091D1FEE362B21FBA4586C62850F181DECA8B0F1307)

#### \[h2\]setPolyToPoly12+

setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit

Maps the vertex coordinates of a polygon to those of another polygon.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PolyToPolyOptions](#polytopolyoptions12) | Yes | Parameters for mapping. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after the mapping. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/iIjSPgt1RragR397G2aT3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=993EDEA63E46B9F753EB97D29FAEB44D9D1976127B3CF24DEE0423F7CF674331)

This API must be used with **scale({centerX:0,centerY:0,x:1})** to ensure that the transformation is centered in the upper left corner of the component.

**Example**

import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private matrix1 = matrix4.identity().setPolyToPoly({
    src: \[{ x: 0, y: 0 }, { x: 500, y: 0 }, { x: 0, y: 500 }, { x: 500, y: 500 }\],
    dst: \[{ x: 0, y: 0 }, { x: 500, y: 0 }, { x: 0, y: 500 }, { x: 750, y: 1000 }\], pointCount: 4
  });

  build() {
    Stack() {
      Column().backgroundColor(Color.Blue)
        .width('500px')
        .height('500px')
      // Replace $r("app.media.transition\_image1") with the image resource file you use.
      Image($r('app.media.transition\_image1'))
        .scale({ centerX: 0, centerY: 0, x: 1 })
        .transform(this.matrix1)
        .width('500px')
        .height('500px')
    }.width("100%").height("100%").opacity(0.5)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/XqYmKuXGSg6ZDuQwEGtzHQ/en-us_image_0000002537925274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42C0177FF15CDEE6FF353C366B663732A1F556DD06FA968B3C3269E48952FD20)

#### TranslateOption

Describes the translation parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | Yes | 
Translation distance along the x-axis.

Unit: px

Default value: **0**

Value range: (-∞, +∞)

 |
| y | number | No | Yes | 

Translation distance along the y-axis.

Unit: px

Default value: **0**

Value range: (-∞, +∞)

 |
| z | number | No | Yes | 

Translation distance along the z-axis.

Unit: px

Default value: **0**

Value range: (-∞, +∞)

 |

#### ScaleOption

Describes the scale parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | Yes | 
Scaling multiple along the x-axis. x > 1: The image is scaled up along the x-axis.

0 < x < 1: The image is scaled down along the x-axis.

x < 0: The image is scaled in the reverse direction along the x-axis.

Default value: **1**

Value range: (-∞, +∞)

 |
| y | number | No | Yes | 

Scaling multiple along the y-axis. y > 1: The image is scaled up along the y-axis.

0 < y < 1: The image is scaled down along the y-axis.

y < 0: The image is scaled in the reverse direction along the y-axis.

Default value: **1**

Value range: (-∞, +∞)

 |
| z | number | No | Yes | 

Scaling multiple along the z-axis. z > 1: The image is scaled up along the z-axis.

0 < z < 1: The image is scaled down along the z-axis.

z < 0: The image is scaled in the reverse direction along the z-axis.

Default value: **1**

Value range: (-∞, +∞)

 |
| centerX | number | No | Yes | 

X-coordinate of the center point.

Unit: px

Default value: X-coordinate of the component center

Value range: (-∞, +∞)

 |
| centerY | number | No | Yes | 

Y-coordinate of the center point.

Unit: px

Default value: Y-coordinate of the component center

Value range: (-∞, +∞)

 |

#### RotateOption

Describes the rotation parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | Yes | 
X-coordinate of the rotation axis vector.

Default value: **0**

Value range: (-∞, +∞)

 |
| y | number | No | Yes | 

Y-coordinate of the rotation axis vector.

Default value: **0**

Value range: (-∞, +∞)

 |
| z | number | No | Yes | 

Z-coordinate of the rotation axis vector.

Default value: **0**

Value range: (-∞, +∞)

**NOTE**

The rotation axis vector is valid only when at least one of **x**, **y**, and **z** is not 0.

 |
| angle | number | No | Yes | 

Rotation angle.

Default value: **0**

 |
| centerX | number | No | Yes | 

Additional x-axis offset of the transformation center relative to the component's anchor.

Unit: px

Default value: **0**

**NOTE**

The value **0** indicates that the transformation center coincides with the component's x-axis anchor. For details about the implementation, see [Example 3: Implementing Rotation Around a Center Point](../../../arkts-components/universal-attributes/visual-effects/transformation/document.md#example-3-implementing-rotation-around-a-center-point).

 |
| centerY | number | No | Yes | 

Additional y-axis offset of the transformation center relative to the component's anchor.

Unit: px

Default value: **0**

**NOTE**

The value **0** indicates that the transformation center coincides with the component's y-axis anchor. For details about the implementation, see [Example 3: Implementing Rotation Around a Center Point](../../../arkts-components/universal-attributes/visual-effects/transformation/document.md#example-3-implementing-rotation-around-a-center-point).

 |

#### PolyToPolyOptions12+

Describes the configuration options for polygon-to-polygon transformation mapping.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | Array<[Point](#point12)\> | No | No | Coordinates of the source point. |
| srcIndex | number | No | Yes | 
Start index of the source point coordinates.

Default value: **0**.

Value range: \[0, +∞).

 |
| dst | Array<[Point](#point12)\> | No | No | Coordinates of the destination point. |
| dstIndex | number | No | Yes | 

Start index of the destination point coordinates.

Default value: **src.length/2**.

Value range: \[0, +∞).

 |
| pointCount | number | No | Yes | 

Number of used points. **0**: returns an identity matrix. **1**: returns a translation matrix. 2-4: returns a transformation matrix.

Default value: **0**.

Value range: \[0, +∞).

 |

#### Point12+

Defines the data structure of a coordinate point.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X-coordinate.

Value range: (-∞, +∞)

 |
| y | number | No | No | 

Y-coordinate.

Value range: (-∞, +∞)

 |

#### matrix4.copy(deprecated)

copy(): Matrix4Transit

Copies this matrix object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/IAEYLnCtQ7erq1AzR4O8Vg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3193DB798FE7504BC4E52D911E60AF4E0236B653ABBEEDD48238EB8EF124B3A7)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Copy object of the current matrix. |

**Example**

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 100 });
  // Perform the scale operation on the copy matrix of matrix1, which does not affect matrix1.
  private matrix2 = this.matrix1.copy().scale({ x: 2 });

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1"))
        .width("40%")
        .height(100)
        .transform(this.matrix1)
      // Replace $r("app.media.bg2") with the image resource file you use.
      Image($r("app.media.bg2"))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
        .transform(this.matrix2)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xiJTGTKJQcCUhqLlE3xTlQ/en-us_image_0000002568685051.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DFD4656C3589FA46EEAF2F9489E3D04089608C97C32878E5869BC3436CD60D5)

#### matrix4.invert(deprecated)

invert(): Matrix4Transit

Inverts this matrix object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/HfVyttHRQvuYDMVLFYFrvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD79CB47062D622186656F8A4984C782748311793198AE6BBBFB6B32CD258A73)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Inverse matrix object of the current matrix. |

#### matrix4.combine(deprecated)

combine(options: Matrix4Transit): Matrix4Transit

Combines the effects of two matrices to generate a new matrix object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/dBPI7l-FTSmhAcnGJAuf0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A7E11DA5AC3C3A855DBC0C5246A1A9C80BDCBAF07FCAD92827B0322848C80B2)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Matrix4Transit](#matrix4transit) | Yes | Matrix object to be combined. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after combination. |

#### matrix4.translate(deprecated)

translate(options: TranslateOption): Matrix4Transit

Translates this matrix object along the x, y, and z axes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/X71IrLI7RMW071FOQUYXRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11DC9001AE429EF6B4F3422E352C2B97D01C1DAB6ED90BBC37AF5FF82095F1E4)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TranslateOption](#translateoption) | Yes | Translation configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after translation. |

#### matrix4.scale(deprecated)

scale(options: ScaleOption): Matrix4Transit

Scales this matrix object along the x, y, and z axes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/2rDEC2nLT5arqGY8XfV4Cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A03F31B390E9B5750C76292488B2D0A4DD92AD197BB65C961DB4548369515CA)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ScaleOption](#scaleoption) | Yes | Scaling configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after scaling. |

#### matrix4.rotate(deprecated)

rotate(options: RotateOption): Matrix4Transit

Rotates this matrix object along the x, y, and z axes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/1lEozzSlR6-IrPMevu6R4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6F3713BC023F924B5FB2D8BB0A0B46873713E0F74E14DBA86ACE7F62FCD60D2)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RotateOption](#rotateoption) | Yes | Rotation configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](#matrix4transit) | Matrix object after rotation. |

#### matrix4.transformPoint(deprecated)

transformPoint(options: \[number, number\]): \[number, number\]

Applies the current transformation effect to a coordinate point.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/k5gygIKNSrC4fEb3NfeBKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=810250849E444607DAD031D97B7FE238982D8598F548F17B0FD9064F3DA82A5E)

This API is supported since API version 7 and deprecated since API version 10. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | \[number, number\] | Yes | Point to be transformed. |

**Return value**

| Type | Description |
| :-- | :-- |
| \[number, number\] | Point object after matrix transformation |
