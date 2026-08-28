# Enable/Disable Control

You can enable or disable a component to control whether it responds to user interactions. When a component is enabled, it can respond to the following events: [click event](../../../universal-events/interaction-response-events/click-event/document.md), [touch event](../../../universal-events/basic-input-events/touch-event/document.md), [drag event](../../../universal-events/interaction-response-events/drag-event/document.md), [key event](../../../universal-events/basic-input-events/key-event/document.md), [focus event](../../../universal-events/interaction-response-events/focus-event/document.md), [mouse event](../../../universal-events/basic-input-events/mouse-event/document.md), [axis event](../../../universal-events/basic-input-events/axis-event/document.md), [hover event](../../../universal-events/interaction-response-events/hover-event/document.md), [accessibility hover event](../../../universal-events/accessibility-related/accessibility-hover-event/document.md), [gesture event](../../../gesture-handling/gesture-binding/gesture-binding/document.md), [focus axis event](../../../universal-events/basic-input-events/focus-axis-event/document.md), and [crown event](../../../universal-events/basic-input-events/crown-event/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Gk_aiKfATeuKG5pft-t-zA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BA25F771D1E92A795B6F4A85AF0BDEC9A3C669D2FCF0B4EC85AE092895C3FC1)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

The **enabled** attribute takes effect only when the component is pressed. Changes to it during interaction will not be applied.

#### enabled

enabled(value: boolean): T

Sets whether the component responds to user interactions. If **enabled** is not set, the component responds to user interactions by default.

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | Whether the component responds to user interactions, including clicks and touches. The value **true** means that the component responds to user interactions, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to use **enabled** to set whether a button responds to user interactions.

// xxx.ets
@Entry
@Component
struct EnabledExample {
  build() {
    Flex({ justifyContent: FlexAlign.SpaceAround }) {
      // The button does not respond to clicks.
      Button('disable').enabled(false).backgroundColor(0x317aff).opacity(0.4)
      Button('enable').backgroundColor(0x317aff)
    }
    .width('100%')
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/WQCgK1jzQYyP-5KpGhhuOQ/en-us_image_0000002568765163.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3F0D5F136A0055C6C13732CC1B19C435699701E2182056F3F9BDBF71CC62AB2)
