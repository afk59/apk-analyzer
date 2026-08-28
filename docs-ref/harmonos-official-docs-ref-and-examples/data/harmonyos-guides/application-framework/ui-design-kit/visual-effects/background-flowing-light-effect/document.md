# Background Flowing Light Effect

#### Use Case

The [background flowing light effect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdseffect#section139655943218) is supported since version 6.0.0(20) Beta1.

Your app can call the background flowing light effect API to configure the animated background glow effect for a component. You can set the background color before and after the gradient change. This is commonly applied to full-screen background flowing light effects.

#### Development Procedure

1.  Import the required module.
    
    import { hdsEffect } from '@kit.UIDesignKit';
    
2.  Configure the background flowing light effect.
    
    @Entry
    @Component
    struct UVFlowLight {
      @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();
    
      build() {
        Stack() {
        }
        .visualEffect(new hdsEffect.HdsEffectBuilder()
          .shaderEffect({
            effectType: hdsEffect.EffectType.UV\_BACKGROUND\_FLOW\_LIGHT,
            animation: {
              duration: 10000,
              iterations: -1,
              autoPlay: true,
              onFinish: ()=> {
                console.info('Succeeded in finishing');
              }
            },
            controller: this.controller,
          })
          .buildEffect())
        .width('100%')
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/zR8p88wURRyxGMCq8Cab2w/en-us_image_0000002532144141.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B43F0A3EAAD37EA2E3F3B450C41231340301B48F686D987FC926DB1A3B73911 "Click to enlarge")
