# Transformation

Transformation attributes allow you to rotate, translate, scale, or transform a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ov0XAZzTTd22aKKt1gKH4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8E54BAACB72AAAC23347BD43193F7F7492C36F524F0354419A9EA15C2D52F25)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### rotate

rotate(value: RotateOptions): T

Rotates the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [RotateOptions](#rotateoptions) | Yes | 
How the component is rotated within the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system), which takes the upper-left corner of the component as the origin (as shown in the figure below). (x, y, z) specifies a vector as the axis of rotation.

The axis and center of rotation are set based on the coordinate system, which remains where it is when the component is moved.

Default value: When **x**, **y**, and **z** are not specified, their default values are **0**, **0**, and **1**, respectively. If any of **x**, **y**, and **z** is specified, the default value for the unspecified one is **0**.

{

centerX: '50%',

centerY: '50%',

centerZ: 0,

perspective: 0

}

Unit: vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/FsmoJuVVRKmqjbPB-qa9pw/en-us_image_0000002537924934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11365A7998DF705B0E4B4D99C450003DBCD29132851E814AC281F9DE909BD853)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### rotate18+

rotate(options: Optional<RotateOptions>): T

Rotates the component. Compared with [rotate](#rotate), this API supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[RotateOptions](#rotateoptions)\> | Yes | 
How the component is rotated within the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system), which takes the upper-left corner of the component as the origin (as shown in the figure below). (x, y, z) specifies a vector as the axis of rotation.

The axis and center of rotation are set based on the coordinate system, which remains where it is when the component is moved.

Default value: When **x**, **y**, and **z** are not specified, their default values are **0**, **0**, and **1**, respectively. If any of **x**, **y**, and **z** is specified, the default value for the unspecified one is **0**.

{

centerX: '50%',

centerY: '50%',

centerZ: 0,

perspective: 0

}

Unit: vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-SJN7rD0Sz-z7tvhh3S6pw/en-us_image_0000002537924934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8A58B052C21CC5B373A180FD60B5A57B20653DC08294DEB33F8217D2B5AE3E9)

If **options** is **undefined**, the component reverts to its original state with no rotation.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### rotate20+

rotate(options: Optional<RotateOptions | RotateAngleOptions>): T

Sets the component rotation effect. Compared with [rotate](#rotate18), this API supports the **RotateAngleOptions** type for the **options** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[RotateOptions](#rotateoptions) | [RotateAngleOptions](#rotateangleoptions20)\> | Yes | 
**RotateOptions**: How the component rotates in the coordinate system (as shown below) with the upper left corner of the component as the coordinate origin. (x, y, z) specifies a vector as the axis of rotation.

The rotation axis and center point are defined based on the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system). When the component moves, the coordinate system does not follow it.

Default value: When **x**, **y**, and **z** are not specified, their default values are **0**, **0**, and **1**, respectively. If any of **x**, **y**, and **z** is specified, the default value for the unspecified one is **0**.

{

centerX: '50%',

centerY: '50%',

centerZ: 0,

perspective: 0

}

**RotateAngleOptions**: How the component rotates in the coordinate system (as shown below) with the upper left corner of the component as the coordinate origin. angleX, angleY, angleZ specifies the rotation angle on the three axes.

Default value:

{

angleX:0,

angleY:0,

angleZ:0,

centerX: '50%',

centerY: '50%',

centerZ: 0,

perspective: 0

}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/3F6KjSgXRw2UTGBmp1L5aQ/en-us_image_0000002537924934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8C3CE7CBB30598842ECC76085A24B772841CDB219CFF2BBA1B2AAD9242E8036)

If **options** is **undefined**, the component reverts to its original state with no rotation.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### translate

translate(value: TranslateOptions): T

Translates the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TranslateOptions](#translateoptions) | Yes | 
How the component is translated within the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system), which takes the upper-left corner of the component as the origin (as shown in the figure below). Values of **x**, **y**, and **z** indicate the translation distance along the respective axis. A positive value indicates a forward movement towards the respective axis, and a negative value indicates a backward movement towards the respective axis. The translation distance can be a number or a string (for example, **'10px'** or **'10%'**).

Default value:

{

x: 0,

y: 0,

z: 0

}

Unit: vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/qY98LlNfR1COt-_EioAmYQ/en-us_image_0000002537924934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A2448C547715A9749336E74D6BAAAE5A5FA9CAB87859F5EF595215745D05D2F)

**NOTE**

When the component is translated along the z-axis, the position of the observation point remains unchanged. As such, the component appears larger when the value of **z** places it closer to the observation point and smaller when the value of **z** places it further away from the observation point.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2VO8lV-RRsOcgW_OyUtp0A/en-us_image_0000002537925358.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C576EB738E6F280249B3935F8749929CF6DD13189CF81931FD912B625595815C)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### translate18+

translate(translate: Optional<TranslateOptions>): T

Translates the component. Compared with [translate](#translate), this API supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| translate | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[TranslateOptions](#translateoptions)\> | Yes | 
How the component is translated within the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system), which takes the upper-left corner of the component as the origin (as shown in the figure below). Values of **x**, **y**, and **z** indicate the translation distance along the respective axis. A positive value indicates a forward movement towards the respective axis, and a negative value indicates a backward movement towards the respective axis. The translation distance can be a number or a string (for example, **'10px'** or **'10%'**).

Default value:

{

x: 0,

y: 0,

z: 0

}

Unit: vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Inc_S-ANR5-cB_oGFZ3DFg/en-us_image_0000002537924934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=646C6916343CECDB844351DD298A5934E413117636E9E7C4CEB2700277D0DB56)

**NOTE**

When the component is translated along the z-axis, the position of the observation point remains unchanged. As such, the component appears larger when the value of **z** places it closer to the observation point and smaller when the value of **z** places it further away from the observation point.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/quHUHA08S_qAirIiO_aEIQ/en-us_image_0000002537925358.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A3D0B71F5D66EBCFB55A257E8C951D0081B59236FF9590D46A62AE03CB11E47)

If **translate** is **undefined**, the component reverts to its original state with no translation.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### scale

scale(value: ScaleOptions): T

Scales the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScaleOptions](#scaleoptions) | Yes | 
Scale ratio along the x-, y-, and z-axis. The default value is **1**. **centerX** and **centerY** are used to set the scale center point.

Default value:

{

x: 1,

y: 1,

z: 1,

centerX:'50%',

centerY:'50%'

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### scale18+

scale(options: Optional<ScaleOptions>): T

Scales the component. Compared with [scale](#scale), this API supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[ScaleOptions](#scaleoptions)\> | Yes | 
Scale ratio along the x-, y-, and z-axis. The default value is **1**. **centerX** and **centerY** are used to set the scale center point.

Default value:

{

x: 1,

y: 1,

z: 1,

centerX:'50%',

centerY:'50%'

}

If **options** is **undefined**, the component reverts to its original state with no scaling.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### transform

transform(value: object): T

Displays the matrix transformation when 2D transformation is performed. If 3D transformation is included, the [transform3D](#transform3d20) API is required.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | object | Yes | Transformation matrix of the component. Only the [Matrix4Transit](../../../../arkts-api/ui/ohos-matrix4-matrix-transformation/document.md) object type is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### transform18+

transform(transform: Optional<object>): T

Displays the matrix transformation when 2D transformation is performed. If 3D transformation is included, the [transform3D](#transform3d20) API is required. Compared with [transform](#transform), the transform18+ parameter supports the undefined type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transform | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<object> | Yes | 
Transformation matrix of the component. Only the [Matrix4Transit](../../../../arkts-api/ui/ohos-matrix4-matrix-transformation/document.md) object type is supported.

If **transform** is **undefined**, the component reverts to the identity matrix (no transformation).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### transform3D20+

transform3D(transform: Optional<Matrix4Transit>): T

Sets the 3D transformation matrix of the component. When 3D transformation with the perspective effect is involved, the display effect of the transform interface may be incorrect. In this case, the transform3D interface is recommended.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transform | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[Matrix4Transit](#matrix4transit20)\> | Yes | 
3D transformation matrix.

If **transform** is **undefined**, the component reverts to the identity matrix (no transformation).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Matrix4Transit20+

type Matrix4Transit = Matrix4Transit

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](../../../../arkts-api/ui/ohos-matrix4-matrix-transformation/document.md#matrix4transit) | Identity matrix object. |

#### RotateOptions

Defines component rotation parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | Yes | 
X coordinate of the rotation axis vector.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| y | number | No | Yes | 

Y coordinate of the rotation axis vector.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| z | number | No | Yes | 

Z coordinate of the rotation axis vector.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| angle | number | string | No | No | 

Angle to rotate. A positive angle indicates a clockwise rotation, and a negative angle indicates a counterclockwise rotation. The value can be of the string type, for example, **'90deg'**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| centerX | number | string | No | Yes | 

X coordinate of the transformation center point (anchor). The value can be of the string type, for example, **'50'** and **'50%'**.

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| centerY | number | string | No | Yes | 

Y coordinate of the transformation center point (anchor). The value can be of the string type, for example, **'50'** and **'50%'**.

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| centerZ10+ | number | No | Yes | 

Z-axis anchor, that is, the z-component of the 3D rotation center point.

Default value: **0**.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| perspective10+ | number | No | Yes | 

Z-axis coordinate of the camera. The value indicates the viewing distance, that is, the distance between the camera and the z=0 plane. The positive and negative values of the parameter determine the camera observation direction. When perspective is set to 0, the system automatically calculates a proper camera Z-axis position. The value is negative.

The rotation axis and center point are defined based on the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system). When the component moves, the coordinate system does not follow it.

Default value: **0**.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |

#### RotateAngleOptions20+

Rotation parameter option of the rotation angle on each axis.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| angleX | number | string | No | Yes | 
Rotation angle along the x-axis. A positive value indicates clockwise rotation relative to the rotation axis, and a negative value indicates counterclockwise rotation. The value can be of the string type, for example, **'90deg'**.

Default value: **0**.

Value range: (-∞, +∞).

 |
| angleY | number | string | No | Yes | 

Rotation angle along the y-axis. A positive value indicates clockwise rotation relative to the rotation axis, and a negative value indicates counterclockwise rotation. The value can be of the string type, for example, **'90deg'**.

Default value: **0**.

Value range: (-∞, +∞).

 |
| angleZ | number | string | No | Yes | 

Rotation angle along the z-axis. A positive value indicates clockwise rotation relative to the rotation axis, and a negative value indicates counterclockwise rotation. The value can be of the string type, for example, **'90deg'**.

Default value: **0**.

Value range: (-∞, +∞).

 |
| centerX | number | string | No | Yes | 

X coordinate of the transformation center point (anchor).

Unit: vp

Default value: **'50%'**.

Value range: (-∞, +∞).

 |
| centerY | number | string | No | Yes | 

Y coordinate of the transformation center point (anchor).

Unit: vp

Default value: **'50%'**.

Value range: (-∞, +∞).

 |
| centerZ | number | No | Yes | 

Z-axis anchor, that is, the z-component of the 3D rotation center point.

Default value: **0**.

Unit: px

Value range: (-∞, +∞).

 |
| perspective | number | No | Yes | 

Z-axis coordinate of the camera. The value indicates the viewing distance, that is, the distance between the camera and the z=0 plane. The positive and negative values of the parameter determine the camera observation direction. When perspective is set to 0, the system automatically calculates a proper camera Z-axis position. The value is negative.

The rotation axis and center point are defined based on the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system). When the component moves, the coordinate system does not follow it.

Default value: **0**.

Unit: px

Value range: (-∞, +∞).

 |

#### TranslateOptions

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | string | No | Yes | 
Translation distance along the x-axis.

For the number type, the unit is vp, and the value range is (-∞, +∞).

Default value: **0**.

For the string type, the value follows the format of [Length](../../../common-definitions/basic-types/document.md#length) string type.

 |
| y | number | string | No | Yes | 

Translation distance along the y-axis.

For the number type, the unit is vp, and the value range is (-∞, +∞).

Default value: **0**.

For the string type, the value follows the format of [Length](../../../common-definitions/basic-types/document.md#length) string type.

 |
| z | number | string | No | Yes | 

Translation distance along the z-axis.

For the number type, the unit is vp, and the value range is (-∞, +∞).

Default value: **0**.

For the string type, the value follows the format of [Length](../../../common-definitions/basic-types/document.md#length) string type.

 |

#### ScaleOptions

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | Yes | 
Scale ratio along the x-axis. x > 1: The component is scaled up along the x-axis.

0 < x < 1: The component is scaled down along the x-axis.

x < 0: The component is scaled in the reverse direction of the x-axis.

 |
| y | number | No | Yes | 

Scale ratio along the y-axis. y > 1: The component is scaled up along the y-axis.

0 < y < 1: The component is scaled down along the y-axis.

y < 0: The component is scaled in the reverse direction of the y-axis.

 |
| z | number | No | Yes | 

Scale ratio along the z-axis. z > 1: The component is scaled up along the z-axis.

0 < z < 1: The component is scaled down along the z-axis.

z < 0: The component is scaled in the reverse direction of the z-axis.

 |
| centerX | number | string | No | Yes | 

X coordinate of the transformation center point (anchor). The value can be of the string type, for example, **'50'** and **'50%'**.

Unit: vp

 |
| centerY | number | string | No | Yes | 

Y coordinate of the transformation center point (anchor). The value can be of the string type, for example, **'50'** and **'50%'**.

Unit: vp

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/MmNmLLniQq-tzeg5Ac0ltw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=030D026BAA5AA2031EBE5DC5CDCFB27C137209E9825B73964BB5EC924DBBD8D2)

If the [rotate](#rotate) and [scale](#scale) attributes are both set for a component, the values of **centerX** and **centerY** conflict. In this case, their values will be determined by the attribute that was set last.

#### Example

## Example 1: Adding Graphical Transformation Effects

This example applies rotation, translation, scaling, and transformation matrix effects to the component using [rotate](#rotate), [translate](#translate), [scale](#scale), and [transform](#transform).

// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct TransformExample {
  build() {
    Column() {
      Text('rotate').width('90%').fontColor(0xCCCCCC).padding(15).fontSize(14)
      Row()
        .rotate({
          x: 0,
          y: 0,
          z: 1,
          centerX: '50%',
          centerY: '50%',
          angle: 300
        })// The component rotates around the center point of the rotation axis (0, 0, 1) clockwise by 300 degrees.
        .width(100).height(100).backgroundColor(0xAFEEEE)

      Text('translate').width('90%').fontColor(0xCCCCCC).padding(10).fontSize(14)
      Row()
        .translate({ x: 100, y: 10 })// The component translates by 100 along the x-axis and by 10 along the y-axis.
        .width(100)
        .height(100)
        .backgroundColor(0xAFEEEE)
        .margin({ bottom: 10 })

      Text('scale').width('90%').fontColor(0xCCCCCC).padding(15).fontSize(14)
      Row()
        .scale({ x: 2, y: 0.5 })// The height is reduced by half, and the width is doubled. The z-axis has no effect in 2D.
        .width(100).height(100).backgroundColor(0xAFEEEE)

      Text('Matrix4').width('90%').fontColor(0xCCCCCC).padding(15).fontSize(14)
      Row()
        .width(100).height(100).backgroundColor(0xAFEEEE)
        .transform(matrix4.identity().translate({ x: 50, y: 50 }).scale({ x: 1.5, y: 1 }).rotate({
          x: 0,
          y: 0,
          z: 1,
          angle: 60
        }))
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/nrTz9nsiQfmB9gTICSj5xg/en-us_image_0000002568685135.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAE6B2A5D5845DC2E7A32BDE410F53B2FC97BAF7F485C893A25E683CC9434DA8)

## Example 2: Setting the Rotation Perspective

This example demonstrates how to set the rotation perspective for a component by using [perspective](#rotateoptions).

// xxx.ets
@Entry
@Component
struct Index {
  @State prep: number = 10;

  build() {
    Row() {
      Column() {
        Stack()
          .width(100)
          .height(100)
          .backgroundColor(Color.Red)
          .rotate({ y: 1, angle: 45, perspective: this.prep })
        Button('change prep')
          .margin({ top: 100 })
          .onClick(() => {
            this.getUIContext()?.animateTo({
              duration: 2000,
              curve: Curve.EaseIn,
              iterations: 1,
              playMode: PlayMode.Normal,
              onFinish: () => {
                console.info('play end');
              }
            }, () => {
              this.prep = 500 // Change the component's perspective from 10 to 500.
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/5V37rhuuSNi3Wm31JQ6zhQ/en-us_image_0000002568765145.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D89F2171B6B8A28299C89D0FB67D1B8A3E493458E2401C35084DC4D441EA3213)

## Example 3: Implementing Rotation Around a Center Point

This example shows how to achieve the same rotation effect by setting different parameters for [rotate](#rotate) and [transform](#transform).

import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)

      Text('Hello2')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          // Rotate 90 degrees around the anchor (100 vp, 60 vp), where the value of centerX and centerY in rotate or scale are the component's anchors.
          z: 1,
          angle: 90,
          centerX: 100,
          centerY: 60
        })

      Text('Hello3')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .transform(matrix4.identity()
          .rotate({
            // The component's anchor (centerX, centerY) is (50%, 50%) by default, which is (50 vp, 30 vp).
            // Set (centerX, centerY) of rotate in transform to (50 vp, 30 vp), which is an additional offset from the component's own anchor.
            // This transformation is equivalent to rotating around (100 vp, 60 vp), achieving the same rotation effect as "Hello2."
            z: 1,
            angle: 90,
            centerX: this.getUIContext().vp2px(50),
            centerY: this.getUIContext().vp2px(30)
          }))

      Text('Hello4')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .scale({
          // centerX and centerY take effect only when x or y is set.
          // Set the component anchor to (100 vp, 60 vp).
          x: 1,
          y: 1,
          centerX: 100,
          centerY: 60
        })// If centerX and centerY are not specified, the rotation uses the component's own anchor as the center.
          // Here, the component rotates around (100 vp, 60 vp) through the anchor set by scale, achieving the same rotation effect as "Hello2."
        .transform(matrix4.identity().rotate({ z: 1, angle: 90 }))
    }.width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ewmfs1gIS-mrFtuTcKfTpg/en-us_image_0000002537765420.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A0111AB3C4DCB76854F69A5E3DFF385C28BC49C7DAC3353A3BF453FB77C5791)

## Example 4: Implementing Graphical Transformation Through transform3D

This example demonstrates how to implement image transformation by setting [transform3D](#transform3d20). This functionality is supported since API version 20.

import { matrix4 } from '@kit.ArkUI';

let matrix: matrix4.Matrix4Transit = matrix4.init(\[
  0.53033, 0, -0.53033, 0.00053033,
  0, 0.75, 0, 0,
  0.707107, 0, 0.707107, -0.000707107,
  0, 0, 0, 1
\])

@Entry
@Component
struct Tests {
  build() {
    Column() {
      Stack() {
        Stack()
          .width(200)
          .height(100)
          .backgroundColor(Color.Grey)
        Stack()
          .width(200)
          .height(100)
          .backgroundColor(Color.Blue)
          .transform3D(matrix)
      }
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/9U5_r9KCSLi4rEx0RlP1bA/en-us_image_0000002537925360.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5908781A4555C34910C54D24005F5E1950C292B68FC2EB0746366A969F8B5575)

## Example 5: Rotating an Image Based on Angles of Each Axis

This example demonstrates how to implement rotation by setting the [RotateAngleOptions](#rotateangleoptions20) parameter of **rotate**. This functionality is supported since API version 20.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Stack()
          .width(100)
          .height(100)
          .backgroundColor(Color.Blue)
          .rotate({ angleZ: -45 })
        Button('rotateAngle')
          .width("40%")
          .margin({ top: 100 })
          .rotate({ angleY: 30, centerX: '90%', perspective: 10 })
        Image($r("app.media.startIcon"))
          .width(200)
          .height(200)
          .rotate({
            angleX: 60,
            angleY: -125,
            angleZ: 75,
            centerX: 100,
            centerZ: 20
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/oQKD2aRkQxGocz-HZRJsgA/en-us_image_0000002568685137.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D961521273E1551B455708E5EBAC2232F16545D3A3E461D5803F9ACD716166B4)
