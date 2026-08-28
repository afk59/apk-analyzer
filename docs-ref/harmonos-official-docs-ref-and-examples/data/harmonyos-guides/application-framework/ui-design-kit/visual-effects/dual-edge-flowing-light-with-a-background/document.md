# Dual-Edge Flowing Light with a Background

#### Use Case

The [dual-edge flowing light with a background](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hds-visual-component#section92774418495) is supported since version 6.0.0(20) Beta1.

Your app can call the API provided by the common visual effect component **HdsVisualComponent** to configure the dual-edge flowing light with a background. You can define the starting and ending points and color effects for both sides, as well as the background color that overlays the flowing light. This is commonly applied to capsule components and screen-edge glows.

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsVisualComponentAttribute. For details, refer to the "Modules to Import" section of the HdsVisualComponent reference document.
    import {
      HdsVisualComponent,
      HdsVisualComponentAttribute,
      HdsSceneController,
      HdsSceneType
    } from '@kit.UIDesignKit';
    
2.  Call the **HdsVisualComponent**, specify the scenario type as **DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK**, and set scenario parameters.
    
    @Entry
    @Component
    struct EdgeFlowLightVisualComponent {
      @State sceneController: HdsSceneController = new HdsSceneController()
        .setSceneParams({
          backgroundMaskColors: \[Color.Green, Color.Red\],
          firstEdgeFlowLight: {
            startPos: 0,
            endPos: 0.5,
            color: Color.Red
          },
          secondEdgeFlowLight: {
            startPos: 0,
            endPos: -0.5,
            color: Color.Green
          }
        })
    
      build() {
        Stack() {
          HdsVisualComponent()
            .scene(HdsSceneType.DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK, this.sceneController, () => {
              console.info('Succeeded in finishing');
            })
            .width('100%')
            .height('50%')
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/IxSF_eaxThm3Spr2CRvrBQ/en-us_image_0000002532304105.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2756D66131000AF02752EC5858D450B9CB74172B238F96C45CCB7C8141B09F28 "Click to enlarge")
