# Dual-Edge Flowing Light Effect

#### Use Case

The [dual-edge flowing light effect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdseffect#section139655943218) is supported since version 6.0.0(20) Beta1.

Your app can call the API that implements the dual-edge flowing light effect to configure glowing effects on a component's edges. You can define the starting and ending points and color effects for both sides. This is commonly applied to capsule components and screen-edge glows.

#### Development Procedure

1.  Import the required module.
    
    import { hdsEffect } from '@kit.UIDesignKit';
    
2.  Configure the dual-edge flowing light effect.
    
    @Entry
    @Component
    struct Index {
      @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();
    
      build() {
        Column() {
          Stack() {
          }
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .shaderEffect({
              effectType: hdsEffect.EffectType.DUAL\_EDGE\_FLOW\_LIGHT,
              animation: {
                duration: 4000,
                iterations: -1,
                autoPlay: true,
                onFinish: () => {
                  console.info('Succeeded in finishing');
                }
              },
              controller: this.controller,
              params: {
                firstEdgeFlowLight: {
                  startPos: 0,
                  endPos: 1.0,
                  color: '#1AD0F1',
                },
                secondEdgeFlowLight: {
                  startPos: 0.5,
                  endPos: 1.5,
                  color: '#FFA4E5',
                }
              }
            })
            .buildEffect())
          .width(200)
          .borderRadius('50%')
          .clip(true)
          .height(200)
          .backgroundColor('#383838')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Black)
        .width('100%')
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/JQSm900_Rzm5rxomTJp64g/en-us_image_0000002500304226.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC2F382A80BCC2E35504379E50BA978DA15CCC06508FB38BEBB7A2AF8A915B6F)
