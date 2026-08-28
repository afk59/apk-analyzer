# @ohos.arkui.inspector (Layout Callback)

The **Inspector** module provides APIs for registering the component layout and drawing completion callbacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/px4hFDvmQyS3dJF82x903Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F7319E9C30BB9370EBCE28C7BEFDABCB88135CF2B6A93C4D4A2A69DE7F4E4C0)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { inspector } from '@kit.ArkUI';

#### inspector.createComponentObserver(deprecated)

createComponentObserver(id: string): ComponentObserver

Binds to the specified component and returns the corresponding observation handle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/mKw6wR1-QriaRhBz8LpeyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20AD32E7DAFAACD1C68C4A9E618C44E31DF7F6B965800968C71E98E5FBD1C7C0)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [createComponentObserver](../ohos-arkui-uicontext-uicontext/class-uiinspector/document.md#createcomponentobserver) instead. Obtain the [UIInspector](../ohos-arkui-uicontext-uicontext/class-uiinspector/document.md) instance using the [getUIInspector](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getuiinspector) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md), and then call the **createComponentObserver** method via this instance.
    
-   Since API version 10, you can use the [getUIInspector](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getuiinspector) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [UIInspector](../ohos-arkui-uicontext-uicontext/class-uiinspector/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | ID of the target component, set using the universal attributes [id](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#id) or [key](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md#key12). |

**Return value**

| Type | Description |
| :-- | :-- |
| [ComponentObserver](#componentobserver) | Component observer handle, which is used to register and unregister callbacks. |

**Example**

let listener:inspector.ComponentObserver = inspector.createComponentObserver('COMPONENT\_ID'); // Listen for callback events for the component whose ID is COMPONENT\_ID.

#### ComponentObserver

Implements an observer for layout and drawing completion callbacks for components, containing the initial query results from when the observer was created.

#### \[h2\]on('layout')

on(type: 'layout', callback: () => void): void

Registers a layout completion callback through this handle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value is fixed at **'layout'**.

**'layout'**: completion of component layout.

 |
| callback | () => void | Yes | Layout completion callback. |

#### \[h2\]off('layout')

off(type: 'layout', callback?: () => void): void

Unregisters the layout completion callback through this handle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value is fixed at **'layout'**.

**'layout'**: completion of component layout.

 |
| callback | () => void | No | Callback to unregister. If this parameter is not specified, all callbacks under this handle are unregistered. The callback must be the same object as the one registered with the [on('layout')](#onlayout) API to successfully unregister. |

#### \[h2\]on('draw')

on(type: 'draw', callback: () => void): void

Registers a drawing completion callback through this handle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value is fixed at **'draw'**.

**'draw'**: completion of component drawing.

 |
| callback | () => void | Yes | Drawing completion callback. |

#### \[h2\]off('draw')

off(type: 'draw', callback?: () => void): void

Unregisters the drawing completion callback through this handle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value is fixed at **'draw'**.

**'draw'**: completion of component drawing.

 |
| callback | () => void | No | Callback to unregister. If this parameter is not specified, all callbacks under this handle are unregistered. The callback must be the same object as the one registered with the [on('draw')](#ondraw) API to successfully unregister. |

#### \[h2\]on('drawChildren')20+

on(type: 'drawChildren', callback: Callback<void>): void

Registers a child component drawing completion callback through [ComponentObserver](#componentobserver). When multiple **drawChildren** callbacks exist in the component tree, only the topmost callback will be triggered. After the topmost callback is canceled, other **drawChildren** callbacks will not take effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value is fixed at **'drawChildren'**.

**'drawChildren'**: completion of child component drawing.

 |
| callback | Callback<void> | Yes | Child component drawing completion callback. |

#### \[h2\]off('drawChildren')20+

off(type: 'drawChildren', callback?: Callback<void>): void

Unregisters the child component drawing completion callback through this handle.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. The value is fixed at **'drawChildren'**.

**'drawChildren'**: completion of child component drawing.

 |
| callback | Callback<void> | No | Callback to unregister. If this parameter is not specified, all callbacks under this handle are unregistered. The callback must be the same object as the one registered with the [on('drawChildren')20+](#ondrawchildren20) API to successfully unregister. |

#### Example

The following example demonstrates how to register the component layout and drawing completion callbacks.

import { inspector } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image($r('app.media.startIcon'))
            .width(110)
            .height(110)
            .border({ width: 1 })
            .id('IMAGE\_ID')
        }
        .id('ROW\_ID')
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }

  listenerForImage: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE\_ID')
  listenerForRow: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('ROW\_ID')

  aboutToAppear() {
    let onLayoutComplete: () => void = (): void => {
      // Supplement the implementation code as required.
    }
    let onDrawComplete: () => void = (): void => {
      // Supplement the implementation code as required.
    }
    let onDrawChildrenComplete: () => void = (): void => {
      // Supplement the implementation code as required.
    }
    // Bind to the current JS instance.
    let FuncLayout = onLayoutComplete
    let FuncDraw = onDrawComplete
    let FuncDrawChildren = onDrawChildrenComplete
    let OffFuncLayout = onLayoutComplete
    let OffFuncDraw = onDrawComplete
    let OffFuncDrawChildren = onDrawChildrenComplete

    this.listenerForImage.on('layout', FuncLayout)
    this.listenerForImage.on('draw', FuncDraw)
    this.listenerForRow.on('drawChildren', FuncDrawChildren)

    // Unregister callbacks through the handle. You should decide when to call these APIs.
    // this.listenerForImage.off('layout', OffFuncLayout)
    // this.listenerForImage.off('draw', OffFuncDraw)
    // this.listenerForRow.off('drawChildren', OffFuncDrawChildren)
  }
}
