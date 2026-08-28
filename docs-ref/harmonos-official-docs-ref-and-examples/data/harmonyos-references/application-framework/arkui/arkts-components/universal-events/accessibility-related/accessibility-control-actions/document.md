# Accessibility Control Actions

When accessibility mode is enabled, you can choose whether to intercept accessibility control actions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/DjZ8CuCGRQyw2GBMtmSeVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=070C3541C684238CF181C7368687A0D85FADEA87978C264626DBD5F1ABC80274)

-   The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   Currently, accessibility events can be triggered only when accessibility mode is enabled.

#### onAccessibilityFocus

onAccessibilityFocus(callback: AccessibilityFocusCallback): T

Triggered when the accessibility component gains or loses focus. Callback triggered when the component gains or loses focus.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [AccessibilityFocusCallback](#accessibilityfocuscallback) | Yes | Callback that notifies the registered component of focus and blur events. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AccessibilityFocusCallback

type AccessibilityFocusCallback = (isFocus: boolean) => void

Defines the callback type used in **onAccessibilityFocus**.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFocus | boolean | Yes | 
Whether the component has gained or lost focus.

**true**: The component has gained focus.

**false**: The component has lost focus.

 |

#### onAccessibilityActionIntercept20+

onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T

Registers a callback to intercept accessibility control actions in accessibility mode. The callback is invoked before an accessibility action is triggered, allowing the component to determine whether to intercept the action. This callback is not supported by components that lack click capability.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [AccessibilityActionInterceptCallback](#accessibilityactioninterceptcallback20) | Yes | 
Callback to be invoked before an accessibility action is triggered. The application that registers this callback can decide whether to intercept the action.

Set to **undefined** to unregister the callback.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AccessibilityActionInterceptCallback20+

type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult

Defines the callback type used in **onAccessibilityActionIntercept** to handle accessibility event interception.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | [AccessibilityAction](#accessibilityaction20) | Yes | Type of accessibility action being triggered. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AccessibilityActionInterceptResult](#accessibilityactioninterceptresult20) | Decision on whether to intercept the accessibility action. |

#### AccessibilityAction20+

Enumerates types of accessibility control operations triggered by components.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| UNDEFINED\_ACTION | 0 | Undefined accessibility action. |
| ACCESSIBILITY\_CLICK | 1 | Accessibility click action. |

#### AccessibilityActionInterceptResult20+

Enumerates possible results for accessibility action interception.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_INTERCEPT | 0 | Intercept the accessibility control action received by the current component. After the callback processing is complete, the component won't respond. |
| ACTION\_CONTINUE | 1 | Allow the accessibility control action received by the current component. After the callback processing is complete, the component processes it normally. |
| ACTION\_RISE | 2 | Intercept accessibility control action received by the current component. After the callback processing is complete, the component responds and executes its own processing logic. The action information is then passed to the parent component. This triggers the **onAccessibilityActionIntercept** callback of the parent (if registered) but not the parent's default processing logic. The parent can continue passing the action upward using **ACTION\_RISE**. |

#### Example

## Example 1: Setting onAccessibilityActionIntercept to Intercept Click Events

The example demonstrates how to use the **onAccessibilityActionIntercept** event to intercept a click event on a **Toggle** component in accessibility mode before the click event is processed.

// xxx.ets
@Entry
@Component
struct SwitchBootcamp {
  @State private isOn: boolean = false;

  build() {
    NavDestination() {
      Column() {
        Text('onTouchIntercept')
        Row() {
          Text('Label message')
          Blank()
          Toggle({ type: ToggleType.Switch, isOn: $$this.isOn })
            .onAccessibilityActionIntercept((action : AccessibilityAction) => {
              if (action === AccessibilityAction.ACCESSIBILITY\_CLICK) {
                this.getUIContext().showAlertDialog({
                  title: 'Title',
                  message: 'Message content',
                  primaryButton: {
                    value: 'OK',
                    action: () => {
                      this.isOn = !this.isOn;
                    }
                  },
                  secondaryButton: {
                    value: 'Cancel',
                    action: () => {
                    }
                  }
                })
                return AccessibilityActionInterceptResult.ACTION\_INTERCEPT;
              } else {
                return AccessibilityActionInterceptResult.ACTION\_CONTINUE;
              }
            })
        }.width('100%')
      }
      .padding(24)
      .width('100%')
    }
  }
}

## Example 2: Setting the onAccessibilityFocus Callback

Since API version 18, this callback is triggered when the focus status changes. This example demonstrates the basic usage of [onAccessibilityFocus](#onaccessibilityfocus). When the focus is on **onAccessibilityFocus takes effect**, **\[testingTag\] isFocus current is true** is logged. When the focus is on any other area, **\[testingTag\] isFocus current is false** is logged.

// xxx.ets
@Entry
@Component
struct OnAccessibilityFocusExample {

  build() {
    NavDestination() {
      Column() {
        Text("onAccessibilityFocus doesn't take effect")
        Text("onAccessibilityFocus takes effect")
        .onAccessibilityFocus((isFocus)=>{
          console.info('\[testingTag\] isFocus current is ${isFocus}')
          })
      }
      .padding(24)
      .width('100%')
    }
  }
}
