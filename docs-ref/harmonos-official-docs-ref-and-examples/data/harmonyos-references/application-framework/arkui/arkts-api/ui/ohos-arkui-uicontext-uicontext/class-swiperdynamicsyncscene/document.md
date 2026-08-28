# Class (SwiperDynamicSyncScene)

Provides frame rate configuration APIs for the **Swiper** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/c0DhUkc3R0GJTbfay-37dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AB29A720FFF20EA885636169B8DAAB9C41FA1C5E32709ECB34DBED8929C853E)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   **SwiperDynamicSyncScene** inherits from [DynamicSyncScene](../class-dynamicsyncscene/document.md) and represents the dynamic sync scene of the **Swiper** component.
    

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type12+ | [SwiperDynamicSyncSceneType](../enums/document.md#swiperdynamicsyncscenetype12) | Yes | No | Dynamic sync scene of the **Swiper** component. |

**Example**

import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct Frame {
  @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
  @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30};
  private scenes: SwiperDynamicSyncScene\[\] = \[\];

  build() {
    Column() {
      Text("Animation "+ JSON.stringify(this.ANIMATION))
      Text("Gesture "+ JSON.stringify(this.GESTURE))
      Row(){
        Swiper() {
          Text("one")
          Text("two")
          Text("three")
        }
        .width('100%')
        .height('300vp')
        .id("dynamicSwiper")
        .backgroundColor(Color.Blue)
        .autoPlay(true)
        .onAppear(()=>{
          let scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene\[\];
          if (scenes) {
            this.scenes = scenes;
          }
        })
      }

      Button("set frame")
        .onClick(() => {
          this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

            if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
              scenes.setFrameRateRange(this.ANIMATION);
            }

            if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
              scenes.setFrameRateRange(this.GESTURE);
            }
          });
        })
    }
  }
}
