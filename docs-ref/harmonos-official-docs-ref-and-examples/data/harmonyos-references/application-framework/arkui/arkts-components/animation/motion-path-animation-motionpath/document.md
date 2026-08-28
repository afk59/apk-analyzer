# Motion Path Animation (motionPath)

The motion path animation is used to animate a component along a custom path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/MI1czwTMRMaot_kqZnSt1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC2F332A85AF40E346D20AA25BD85B3EDCB646E1DC335916CDFB860277028946)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### motionPath

motionPath(value: MotionPathOptions): T

Sets a path animation for the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [MotionPathOptions](#motionpathoptions) | Yes | Motion path of the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### MotionPathOptions

Defines motion path configuration options of the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| path | string | No | No | 
Motion path of the translation animation. The [svg path string](../../graphic-drawing/path/document.md#svg-path-syntax) is used. In the value, **start** and **end** can be used in place of the start point and end point, for example, **'Mstart.x start.y L50 50 Lend.x end.y Z'**. For details, see [Path Drawing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ui-js-components-svg-path).

If this parameter is set to an empty string, the path animation is not set.

 |
| from | number | No | Yes | 

Start point of the motion path.

Default value: **0.0**

Value range: \[0.0, 1.0\].

Values less than 0.0 or greater than 1.0 are treated as the default value 0.0.

 |
| to | number | No | Yes | 

End point of the motion path.

Default value: **1.0**

Value range: \[0.0, 1.0\].

Values less than 0.0 or greater than 1.0 are treated as the default value 1.0. After this normalization, the **to** value must be greater than or equal to the **from** value.

 |
| rotatable | boolean | No | Yes | 

Whether to rotate along the path. The value **true** means to rotate along the path, and **false** means the opposite.

Default value: **false**

 |

#### Example

This example demonstrates how to animate a component along a custom path.

// xxx.ets
@Entry
@Component
struct MotionPathExample {
  @State toggle: boolean = true;

  build() {
    Column() {
      Button('click me').margin(50)
        .motionPath({
          path: 'Mstart.x start.y L300 200 L300 500 Lend.x end.y',
          from: 0.0,
          to: 1.0,
          rotatable: true
        }) // Execute the animation: Move from the start point to (300,200), then to (300,500), and finally to the end point.
        .onClick(() => {
          this.getUIContext()?.animateTo({ duration: 4000, curve: Curve.Linear }, () => {
            this.toggle = !this.toggle; // Change the component's position using this.toggle.
          });
        })
    }.width('100%').height('100%').alignItems(this.toggle ? HorizontalAlign.Start : HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/rcIQ_Wj8QS-xa8Kxywhvkg/en-us_image_0000002568765627.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=499D7B44C4DD2BDDA1AD4B009C38C3E86904B80CE5FA461905DACF6608B79BE0)
