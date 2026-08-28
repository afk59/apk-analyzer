# Custom Property

Sets custom properties for a component. These custom properties can be obtained on their corresponding FrameNodes, allowing for more flexible component management.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/dtEcd3HNT5i7wUqDNbW0TA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F3BF21399E990A8EC5BE3B0BCCAFDCD9ADD3A2BDB0C1ACDB4CBAD47D80C573C)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### customProperty

customProperty(name: string, value: Optional<Object>): T

Sets a custom property for this component. This API does not work for [custom components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the custom property. |
| value | [Optional](#optionalt)<Object> | Yes | Value of the custom property. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Optional<T>

type Optional<T> = T | undefined

Defines the Optional type. The value can be **undefined**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

| Type | Description |
| :-- | :-- |
| T | The object can be of any custom type. |
| undefined | The object can be **undefined**. |

#### Example

This example shows how to set custom properties on the [Column](../../../rows-columns-and-stacking/column/document.md) component and obtain the set custom properties from its corresponding [FrameNode](../../../../arkts-api/ui/arkui/framenode/document.md#framenode-1).

// xxx.ets
import { FrameNode, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct CustomPropertyExample {
  build() {
    Column() {
      Text('text')
      Button('print').onClick(() => {
        // Obtain the frameNode corresponding to the Column and query the set custom properties.
        const uiContext: UIContext = this.getUIContext();
        if (uiContext) {
          const node: FrameNode | null = uiContext.getFrameNodeById("Test\_Column") || null;
          if (node) {
            for (let i = 1; i < 4; i++) {
              const key = 'customProperty' + i;
              const property = node.getCustomProperty(key);
              console.info(key, JSON.stringify(property));
            }
          }
        }
      })
    }
    .id('Test\_Column')
    // Set custom properties for the Column component.
    .customProperty('customProperty1', {
      'number': 10,
      'string': 'this is a string',
      'bool': true,
      'object': {
        'name': 'name',
        'value': 100
      }
    })
    .customProperty('customProperty2', {})
    .customProperty('customProperty3', undefined)
    .width('100%')
    .height('100%')
  }
}
