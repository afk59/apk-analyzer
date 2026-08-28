# Class (UIInspector)

Provides APIs for registering the component layout and drawing completion callbacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/rnHtE4sXQRmFkPLKeqt6AQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50DDC143929EFD576AAA3C3AC4E145B35CDB369D4165F77B782BD449586ABF3F)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   In the following API examples, you must first use [getUIInspector()](../class-uicontext/document.md#getuiinspector) in **UIContext** to obtain a **UIInspector** instance, and then call the APIs using the obtained instance.
    

#### createComponentObserver

createComponentObserver(id: string): inspector.ComponentObserver

Registers a callback for layout and rendering completion notifications for a specific component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | ID of the target component, set using the universal attributes [id](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#id) or [key](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#key12). |

**Return value**

| Type | Description |
| :-- | :-- |
| [inspector.ComponentObserver](../../ohos-arkui-inspector-layout-callback/document.md#componentobserver) | Component observer, which is used to register or unregister listeners for completion of component layout or drawing. |

**Example**

import { inspector, UIInspector } from '@kit.ArkUI'

@Entry
@Component
struct UIInspectorExample {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Text("UIInspector")
            .width(110)
            .height(110)
            .border({ width: 1 })
            .id('TEXT\_ID')
        }.width(80).width(80)
      }.width(80).width(80)
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }

  uiInspector: UIInspector = this.getUIContext().getUIInspector();
  listener:inspector.ComponentObserver = this.uiInspector.createComponentObserver("TEXT\_ID")

  aboutToAppear() {
    let onLayoutComplete:()=>void=():void=>{
      console.info("TEXT\_ID layout complete")
    }
    let onDrawComplete:()=>void=():void=>{
      console.info("TEXT\_ID draw complete")
    }

    this.listener.on('layout', onLayoutComplete)
    this.listener.on('draw', onDrawComplete)

    // Unregister callbacks through the handle. You should decide when to call these APIs.
    // this.listener.off('layout', onLayoutComplete)
    // this.listener.off('draw', onDrawComplete)
  }
}
