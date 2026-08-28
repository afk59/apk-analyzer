# @ohos.arkui.componentUtils (componentUtils)

The **componentUtils** module provides API for obtaining the coordinates and size of the drawing area of a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/-gggjzcSQ8GUPR5vsTEGBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A6A399AF1BF55D1775802CC246B6BCC4E0EFDFE049350CE06D8550A42811EF1)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    

#### Modules to Import

import { componentUtils } from '@kit.ArkUI';

#### componentUtils.getRectangleById(deprecated)

getRectangleById(id: string): ComponentInfo

Obtains a **ComponentInfo** object based on the component ID and synchronously returns the geometric properties of the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Vi5I1b8lSfWcOUOJf4JYeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5112FADCB0F3E16A4C9D960C4D63BC1E6A2D5574CAB380086CF2B29CF658B70F)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [getRectangleById](../ohos-arkui-uicontext-uicontext/class-componentutils/document.md#getrectanglebyid) instead. Before calling this API, you need to obtain the [ComponentUtils](../ohos-arkui-uicontext-uicontext/class-componentutils/document.md) object using the [getComponentUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentutils) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getComponentUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentutils) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [ComponentUtils](../ohos-arkui-uicontext-uicontext/class-componentutils/document.md) object associated with the current UI context. This API provides access to component coordinates and size information after the target component completes layout. It is recommended that you invoke this API within [layout completion callbacks](../ohos-arkui-inspector-layout-callback/document.md). Note that dynamically created components must be mounted to the component tree before this API can obtain their information, as unmounted components are not measured or laid out by the UI framework. Always ensure that component mounting precedes information retrieval attempts.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Component ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ComponentInfo](#componentinfo) | **ComponentInfo** object, which provides the size, position, translation, scaling, rotation, and affine matrix information of the component. |

**Error codes**

For details about the error codes, see [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 100001 | UI execution context not found. |

**Example**

import { componentUtils } from '@kit.ArkUI';
let modePosition:componentUtils.ComponentInfo = componentUtils.getRectangleById("onClick");

#### ComponentInfo

Implements a **ComponentInfo** object, which provides the size, position, translation, scaling, rotation, and affine matrix information of the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | [Size](#size) | No | No | Component size. |
| localOffset | [Offset](#offset) | No | No | Offset of the component relative to the parent component. |
| windowOffset | [Offset](#offset) | No | No | Offset of the component relative to the window. |
| screenOffset | [Offset](#offset) | No | No | Offset of the component relative to the screen. |
| translate | [TranslateResult](#translateresult) | No | No | Translation of the component. |
| scale | [ScaleResult](#scaleresult) | No | No | Scaling of the component. |
| rotate | [RotateResult](#rotateresult) | No | No | Rotation of the component. |
| transform | [Matrix4Result](#matrix4result) | No | No | Affine matrix of the component, which is a 4x4 matrix object created based on the input parameter. |

#### \[h2\]Size

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | No | 
Component width.

Unit: px

 |
| height | number | No | No | 

Component height.

Unit: px

 |

#### \[h2\]Offset

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X-coordinate.

Unit: px

 |
| y | number | No | No | 

Y-coordinate.

Unit: px

 |

#### \[h2\]TranslateResult

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
Translation distance along the x-axis.

Unit: px

 |
| y | number | No | No | 

Translation distance along the y-axis.

Unit: px

 |
| z | number | No | No | 

Translation distance along the z-axis.

Unit: px

 |

#### \[h2\]ScaleResult

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
Scale factor along the x-axis.

Unit: px

 |
| y | number | No | No | 

Scale factor along the y-axis.

Unit: px

 |
| z | number | No | No | 

Scale factor along the z-axis.

Unit: px

 |
| centerX | number | No | No | 

X-coordinate of the center point.

Unit: px

 |
| centerY | number | No | No | 

Y-coordinate of the center point.

Unit: px

 |

#### \[h2\]RotateResult

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X-coordinate of the rotation vector.

Unit: px

 |
| y | number | No | No | 

Y-coordinate of the rotation vector.

Unit: px

 |
| z | number | No | No | 

Z coordinate of the rotation vector.

Unit: px

 |
| angle | number | No | No | 

Rotation angle.

Unit: px

 |
| centerX | number | No | No | 

X-coordinate of the center point.

Unit: px

 |
| centerY | number | No | No | 

Y-coordinate of the center point.

Unit: px

 |

#### \[h2\]Matrix4Result

type Matrix4Result = \[number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number\]

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| 
\[number,number,number,number,

number,number,number,number,

number,number,number,number,

number,number,number,number\]

 | 

A number array whose length is 16 (4 x 4). For details, see **4 x 4 matrix description**.

Unit: px

 |

**4 x 4 matrix description**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| m00 | number | Yes | Scale factor along the x-axis. Defaults to **1** for the identity matrix. |
| m01 | number | Yes | The second value, which is affected by the rotation of the x, y, and z axes. |
| m02 | number | Yes | The third value, which is affected by the rotation of the x, y, and z axes. |
| m03 | number | Yes | Meaningless value. |
| m10 | number | Yes | The fifth value, which is affected by the rotation of the x, y, and z axes. |
| m11 | number | Yes | Scale factor along the y-axis. Defaults to **1** for the identity matrix. |
| m12 | number | Yes | The seventh value, which is affected by the rotation of the x, y, and z axes. |
| m13 | number | Yes | Meaningless value. |
| m20 | number | Yes | The ninth value, which is affected by the rotation of the x, y, and z axes. |
| m21 | number | Yes | The tenth value, which is affected by the rotation of the x, y, and z axes. |
| m22 | number | Yes | Scale factor along the z-axis. Defaults to **1** for the identity matrix. |
| m23 | number | Yes | Meaningless value. |
| m30 | number | Yes | Translation value of the x-axis, in px. The default value is **0** for the identity matrix. |
| m31 | number | Yes | Translation value of the y-axis, in px. The default value is **0** for the identity matrix. |
| m32 | number | Yes | Translation value of the z-axis, in px. The default value is **0** for the identity matrix. |
| m33 | number | Yes | Valid in homogeneous coordinates, presenting the perspective projection effect. |

#### Example

## Example 1: Obtaining the ComponentUtils Object

You are advised to use [getComponentUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentutils) to obtain the **ComponentUtils** object associated with the current UI context.

import { matrix4, componentUtils } from '@kit.ArkUI';

@Entry
@Component
struct Utils {
  @State x: number = 120;
  @State y: number = 10;
  @State z: number = 100;
  @State value: string = '';
  private matrix1 = matrix4.identity().translate({ x: this.x, y: this.y, z: this.z });

  build() {
    Column() {
      // Replace $r("app.media.img") with the image resource file you use.
      Image($r("app.media.img"))
        .transform(this.matrix1)
        .translate({ x: 20, y: 20, z: 20 })
        .scale({ x: 0.5, y: 0.5, z: 1 })
        .rotate({
          x: 1,
          y: 1,
          z: 1,
          centerX: '50%',
          centerY: '50%',
          angle: 300
        })
        .width(300)
        .height(100)
        .key("image\_01")
      Button('getRectangleById')
        .onClick(() => {
          this.value = JSON.stringify(this.getUIContext()
            .getComponentUtils()
            .getRectangleById("image\_01")) // You are advised to use this.getUIContext().getComponentUtils().
        }).margin(10).id('onClick')
      Text(this.value)
        .margin(20)
        .width(300)
        .height(300)
        .borderWidth(2)
    }.margin({ left: 50 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/mRpLfLF8RyOyWqW0V_vWEg/en-us_image_0000002537925256.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47A503BBA237784B4A42E5168814A4824ACBAB9452EF98B49926E7A06ABC33B8)
