# Custom Event Interception

The custom event interception capability provided for components allows you to dynamically determine the **HitTestMode** attribute of a component based on the position where the event is triggered on the component, as well as other event information such as the input source.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/yStVKnD6Q2iIiOIB9euW7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F287F6DB34A3D37316F8DD17FAA720B2AF2892CEF282EBE8E6C486E6B819B57)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### onTouchIntercept

onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T

Binds a custom event interception callback to a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/6whCBld3QS-yYGogFnO-mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=839B384C6E24D970099057453AFB310B9F3DBC512DAE92436F6E180E45509DB1)

This API can be called in [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[TouchEvent](../../basic-input-events/touch-event/document.md#touchevent), [HitTestMode](../../../common-definitions/enums/document.md#hittestmode9)\> | Yes | Custom event interception callback. Triggered during [hit testing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#hit-testing) and sets the [hit test behavior](../../../universal-attributes/interaction-properties/touch-interactions/hit-test-control/document.md) for the component based on the return value. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to modify the **HitTestMode** attribute of a component using **onTouchIntercept**.

// xxx.ets
@Entry
@Component
struct Index {
  isPolygon(event: TouchEvent) {
    return true;
  }

  build() {
    Row() {
      Column() {
        Text("hello world")
          .backgroundColor(Color.Blue)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            console.info("Text click");
          })
      }
      .width(400)
      .height(300)
      .backgroundColor(Color.Pink)
      .onClick(() => {
        console.info("Column click");
      })
      // Call onTouchIntercept to modify the HitTestMode attribute of the component.
      .onTouchIntercept((event: TouchEvent) => {
        console.info("OnTouchIntercept + " + JSON.stringify(event));
        // Check whether touches is empty before using it.
        if (event && event.touches) {
          let touches = event.touches;
          for (let i = 0; touches\[i\] != null; i++) {
            console.info('onTouchIntercept touches:', JSON.stringify(touches\[i\]));
          }
        }
        if (this.isPolygon(event)) {
          return HitTestMode.None;
        }
        return HitTestMode.Default;
      })
    }
    .width('100%')
  }
}
