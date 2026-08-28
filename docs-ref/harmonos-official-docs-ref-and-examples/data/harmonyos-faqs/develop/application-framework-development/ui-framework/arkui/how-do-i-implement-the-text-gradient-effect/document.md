# How do I implement the text gradient effect?

**Symptom**

When **linearGradient** is set, the background color gradient instead of the text gradient is used by default. How to implement the text gradient?

**Possible Causes**

The **linearGradient** attribute is used for the component content and is drawn on the background. Therefore, if the attribute is set only for text, the effect is displayed on the background color instead of the text. The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/WVgyPPbVTuybLoYV21nf2g/en-us_image_0000002337430672.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062557Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35C563CA8928DF8BE918E71DE0B6E4ED52915677CA28F8EC5D20600C3A2187C4)

**Solution**

To implement the text gradient effect, use the following methods:

1\. Versions earlier than API20

-   On the ArkTS side, crop the background color through **BlendMode**, which can be used to implement the cropping, mask, and brightening effects by specifying how the current pixel is mixed with the pixels below it. For details, see [BlendMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blendmode).
    
    The sample code of implementing the text gradient effect is as follows:
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        RelativeContainer() {
          Row() {
            Text(this.message)
              .fontSize(24)
              .fontWeight(FontWeight.Bold)
              .blendMode(BlendMode.DST\_IN, BlendApplyType.OFFSCREEN)
          }
          .linearGradient({
            direction: GradientDirection.Right,
            colors: \[\['#ff0631f5', 0.0\], \['#ff922626', 1\]\]
          })
          .blendMode(BlendMode.SRC\_OVER, BlendApplyType.OFFSCREEN)
        }
        .width('100%')
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/5tqgaavXTrapZlchjuqObQ/en-us_image_0000002371468633.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062557Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D464CEF737B51F23981562A25064E966AAF935FD0936C90FF8FBF51429F9EEE)
    
-   On the C-API side, the solution is the same as the preceding one. Use **NODE\_BLEND\_MODE** and **NODE\_LINEAR\_GRADIENT** of [ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) to implement the text gradient.

2\. Versions later than API20

-   Implement text gradient using ArkTS. You can use the [shaderStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#shaderstyle20) attribute of **Text** to directly implement the text gradient. The following is an example:
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
    
      build() {
        RelativeContainer() {
          Text(this.message)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .shaderStyle({
              direction: GradientDirection.Right,
              colors: \[\['#ff0631f5', 0.0\], \['#ff922626', 1\]\]
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
-   For an application developed using C-API, you can use the **NODE\_TEXT\_LINEAR\_GRADIENT** attribute of [ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) to implement text gradient.

For more text effects, see [Text Effects Based on the Text Component and Common Properties](https://gitcode.com/harmonyos_samples/text-effects).
