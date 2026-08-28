# Class (Magnifier)

Provides the capability of displaying and hiding of the magnifier. The magnifier enlarges the component content for you to view the component details.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/WiKuYFb1ScStIt-3tpd-Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6498263816BE6DDF908613DF4D11CCB9324B1009B19A2C3E992BD551597A0B62)

-   The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 22.
    
-   In the following API examples, you must first use [getMagnifier()](../class-uicontext/document.md#getmagnifier22) in **UIContext** to obtain a **Magnifier** instance, and then call the APIs using the obtained instance.
    
-   The magnifier capability of this class does not affect that of text components. For text components, you are advised to use the built-in magnifier capability.
    

#### bind

bind(id: string): void

Binds the magnifier to the component with the specified ID.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Parameter | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Component ID, which can be set through the universal attribute [id](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#id) or [key](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#key12). If the component ID is an empty string or no component is found based on the specified ID, the magnifier is not displayed. |

**Example**

This example listens to the onTouch event to control the magnifier to zoom in on an image.

import { Magnifier } from '@kit.ArkUI';

@Entry
@Component
struct MagnifierExample {
  private magnifier: Magnifier = this.getUIContext().getMagnifier();

  build() {
    Column() {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      Image($r('app.media.startIcon'))
        .draggable(false)
        .width(200)
        .height(200)
        .margin(50)
        .id('image')
        .onTouch((event?: TouchEvent) => {
          if (event && event.sourceTool === SourceTool.Finger) {
            if (event.type === TouchType.Down) {
              this.magnifier.bind('image')
            } else if (event.type === TouchType.Move) {
              let x = event.touches\[0\].x
              let y = event.touches\[0\].y
              this.magnifier.show(x, y)
            } else if (event.type === TouchType.Up) {
              this.magnifier.unbind()
            } else if (event.type === TouchType.Cancel) {
              this.magnifier.unbind()
            }
          }
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Bm0nsqRNRjmVJ-3ONh2RNg/en-us_image_0000002537765326.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E14BFC572B593AFB0F4111BDC0E741E5F123E35C17604299411153B922BDEF4C)

#### show

show(x: number, y: number): void

Sets the position of the component content displayed by the magnifier relative to the upper left corner of the component. After the setting is successful, the magnifier displays the content centered at the coordinate point.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/iN6MfRsHS_2KPU1D5SdYcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36698559D26D6A474616058EB961EAC4E0DB41B6A9AE0A2011E84D6E7FC1B3D6)

When the content of the component bound to the magnifier changes, the magnifier does not automatically update the displayed content. You need to call the **show** API to update the displayed content of the magnifier.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Parameter | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Horizontal coordinate of the component content displayed by the magnifier, relative to the component itself, in vp. If the coordinate value is greater than the component width or less than 0, the magnifier is not displayed. If the value is **undefined**, the current display status of the magnifier is retained. |
| y | number | Yes | Vertical coordinate of the component content displayed by the magnifier, relative to the component itself, in vp. If the coordinate value is greater than the component height or less than 0, the magnifier is not displayed. If the value is **undefined**, the current display status of the magnifier is retained. |

**Example**

For details, see the [bind](#bind) example.

#### unbind

unbind(): void

Unbinds the magnifier from the current component.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

For details, see the [bind](#bind) example.
