# Key Event

A key event is triggered when a focusable component, such as **Button**, receives input from a physical keyboard, remote control, or any other key-based input devices. For components that are not focusable by default, like **Text** and **Image**, you can set the [focusable](../../../universal-attributes/interaction-properties/focus-control/document.md#focusable) attribute to **true** to enable key events.

For details about the process and specific timing of the key event triggering, see [Key Event Data Flow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-development-guide-keyboard#key-event-data-flow).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/rK6RaG-GT12MgJn3LsDKhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97D28652D4422E460B1D783DCD9F0ABE561B3EF59616656BB91BAFCDB85B7D16)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### onKeyEvent

onKeyEvent(event: (event: KeyEvent) => void): T

Triggered when a key event occurs.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | (event: [KeyEvent](#keyevent)) => void | Yes | **KeyEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onKeyEvent15+

onKeyEvent(event: Callback<KeyEvent, boolean>): T

Triggered when a key operation is performed on the bound component after it obtains focus. If the callback returns **true**, the key event is considered handled.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[KeyEvent](#keyevent), boolean> | Yes | Callback for handling the key event. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onKeyPreIme12+

onKeyPreIme(event: Callback<KeyEvent, boolean>): T

Triggered before other callbacks when a key operation is performed on the bound component after it obtains focus.

If the return value of this callback is **true**, the key event is considered consumed, and subsequent event callbacks (**keyboardShortcut**, input method events, **onKeyEventDispatch**, and **onKeyEvent**) will be intercepted and no longer triggered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[KeyEvent](#keyevent), boolean> | Yes | Callback for handling the key event. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onKeyEventDispatch15+

onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T

Triggered when the bound component receives a key event. The key event will not be dispatched to its child components. Only existing key events can be intercepted; creating new **KeyEvent** objects for dispatch is not supported.

If the callback returns **true**, the key event is marked as consumed and will not [bubble up](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) to parent components.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../../common-definitions/basic-types/document.md#callback12)<[KeyEvent](#keyevent), boolean> | Yes | Callback for handling key event dispatch. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### KeyEvent

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [KeyType](../../../common-definitions/enums/document.md#keytype) | No | No | 
Key type.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| keyCode | number | No | No | 

Key value. For details about the key values provided by the key-based input devices, see [KeyCode](../../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| keyText | string | No | No | 

Name of the key.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| keySource | [KeySource](../../../common-definitions/enums/document.md#keysource) | No | No | 

Type of the input device that triggers the key event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| deviceId | number | No | No | 

ID of the input device that triggers the key event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| metaKey | number | No | No | 

State of the Meta key (the key located next to the **Ctrl** key in the lower left corner of the keyboard, or the key marked with a window logo) when the key event occurs. The value **1** indicates that the Meta key is pressed, and **0** indicates that it is not pressed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| timestamp | number | No | No | 

Timestamp of the event. It is the interval between the time when the event is triggered and the time when the system starts, in nanoseconds.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| stopPropagation | () => void | No | No | 

Blocks [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| intentionCode10+ | [IntentionCode](#intentioncode10) | No | No | 

Intention corresponding to the key.

Default value: **IntentionCode.INTENTION\_UNKNOWN**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| unicode14+ | number | No | Yes | 

Unicode value of the key. Non-space basic Latin characters in the 0x0021-0x007E range are supported. Characters with a value of 0 are not supported. In the case of key combination, this API returns the Unicode value of the key corresponding to the key event.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| isNumLockOn19+ | boolean | No | Yes | 

NumLock state. **true**: locked. **false**: unlocked.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| isCapsLockOn19+ | boolean | No | Yes | 

CapsLock state. **true**: locked. **false**: unlocked.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| isScrollLockOn19+ | boolean | No | Yes | 

ScrollLock state. **true**: locked. **false**: unlocked.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### \[h2\]getModifierKeyState12+

getModifierKeyState?(keys: Array<string>): boolean

Obtains the pressed status of modifier keys.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | Array<string> | Yes | 
Obtains the pressed status of modifier keys. For details about the error message, see the following error codes. The following modifier keys are supported: 'Ctrl'| 'Alt' | 'Shift'.

**NOTE**

This API is not supported in stylus scenarios.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the modifier key is pressed. **true** if the modifier key is pressed; **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

#### IntentionCode10+

type IntentionCode = IntentionCode

Intention corresponding to the key.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [IntentionCode](../../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-intentioncode-intention-code/document.md#intentioncode) | Intention corresponding to the key. |

#### Example

## Example 1: Triggering the onKeyEvent Callback

This example demonstrates key event handling through a **Button** component. When the button is focused, pressing a key triggers the **onKeyEvent** callback. For details about the process and specific timing of the key event triggering, see [Key Event Data Flow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-development-guide-keyboard#key-event-data-flow).

// xxx.ets
@Entry
@Component
struct KeyEventExample {
  @State text: string = ''
  @State eventType: string = ''

  build() {
    Column() {
      Button('KeyEvent')
        .defaultFocus(true)
        .onKeyEvent((event?: KeyEvent) => {
          if (event) {
            if (event.type === KeyType.Down) {
              this.eventType = 'Down'
            }
            if (event.type === KeyType.Up) {
              this.eventType = 'Up'
            }
            this.text = 'KeyType:' + this.eventType + '\\nkeyCode:' + event.keyCode + '\\nkeyText:' + event.keyText +
              '\\nintentionCode:' + event.intentionCode
          }
        })
      Text(this.text).padding(15)
    }.height(300).width('100%').padding(35)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/WkdDXITARoWhfr7D0dJ7ag/en-us_image_0000002537765376.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E8015ECBCB942860788C97194D73A73D24CD967B6D1ED1BEB4C8B901930FAF5)

## Example 2: Obtaining the Unicode Code Point

This example demonstrates how to obtain the Unicode code point of the pressed key using the key event.

// xxx.ets
@Entry
@Component
struct KeyEventExample {
  @State text: string = ''
  @State eventType: string = ''
  @State keyType: string = ''

  build() {
    Column({ space: 10 }) {
      Button('KeyEvent')
        .onKeyEvent((event?: KeyEvent) => {
          if (event) {
            if (event.type === KeyType.Down) {
              this.eventType = 'Down'
            }
            if (event.type === KeyType.Up) {
              this.eventType = 'Up'
            }
            if (event.unicode == 97) {
              this.keyType = 'a'
            } else if (event.unicode == 65) {
              this.keyType = 'A'
            } else {
              this.keyType = ' '
            }
            this.text =
              'KeyType:' + this.eventType + '\\nUnicode:' + event.unicode + '\\nkeyCode:' + event.keyCode + '\\nkeyType:' +
              this.keyType
          }
        })
      Text(this.text).padding(15)
    }.height(300).width('100%').padding(35)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/tFhzIVCRRWuIBqZF4PB46w/en-us_image_0000002537925316.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83362B1A2EBB024624CFFE92EE3D502F6CD34F56996785E347E869E6E480F348)

## Example 3: Triggering the onKeyPreIme Callback

This example demonstrates how to use the **onKeyPreIme** callback to intercept and disable the left arrow key in a text box.

import { KeyCode } from '@kit.InputKit';

@Entry
@Component
struct PreImeEventExample {
  @State buttonText: string = '';
  @State buttonType: string = '';
  @State columnText: string = '';
  @State columnType: string = '';

  build() {
    Column() {
      Search({
        placeholder: "Search..."
      })
        .width("80%")
        .height("40vp")
        .border({ radius: "20vp" })
        .onKeyPreIme((event: KeyEvent) => {
          // Prevent the left arrow key from working.
          if (event.keyCode == KeyCode.KEYCODE\_DPAD\_LEFT) {
            return true;
          }
          return false;
        })
    }
  }
}

## Example 4: Preventing Event Bubbling

This example demonstrates event bubbling prevention using **stopPropagation**. Adding **event.stopPropagation()** to the **Button** component's **onKeyEvent** callback ensures only the **Button** component responds to keyboard events, while the parent **Column** remains unresponsive.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/gQ39_xYZTQm5U6Omghwk-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E15F1CF2522B458243A6403D546A52AE8ECE524242A8455EC115855551B02783)

1.  **onKeyEvent** events bubble by default.
2.  Event bubbling is a form of event propagation in the document object model (DOM), where an event is first handled by an element and then passed to its parent element for further processing.
3.  In [onKeyEvent15+](#onkeyevent15), returning **true** consumes the key event and prevents bubbling, achieving the same effect as **stopPropagation**.

@Entry
@Component
struct KeyEventExample {
  @State buttonText: string = '';
  @State buttonType: string = '';
  @State columnText: string = '';
  @State columnType: string = '';

  build() {
    Column() {
      Button('onKeyEvent')
        .defaultFocus(true)
        .width(112).height(56)
        .onKeyEvent((event?: KeyEvent) => {
          // Use stopPropagation to prevent the key event from bubbling up.
          if (event) {
            if (event.stopPropagation) {
              event.stopPropagation();
            }
            if (event.type === KeyType.Down) {
              this.buttonType = 'Down';
            }
            if (event.type === KeyType.Up) {
              this.buttonType = 'Up';
            }
            this.buttonText = 'Button: \\n' +
              'KeyType:' + this.buttonType + '\\n' +
              'KeyCode:' + event.keyCode + '\\n' +
              'KeyText:' + event.keyText;
          }
        })

      Divider()
      Text(this.buttonText).fontColor(Color.Green)

      Divider()
      Text(this.columnText).fontColor(Color.Red)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    .onKeyEvent((event?: KeyEvent) => { // Set the onKeyEvent event for the parent container Column.
      if (event) {
        if (event.type === KeyType.Down) {
          this.columnType = 'Down';
        }
        if (event.type === KeyType.Up) {
          this.columnType = 'Up';
        }
        this.columnText = 'Column: \\n' +
          'KeyType:' + this.columnType + '\\n' +
          'KeyCode:' + event.keyCode + '\\n' +
          'KeyText:' + event.keyText;
      }
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/L5jGojqzR2aMlwM8J6z6xQ/en-us_image_0000002568685093.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF4D3D5108F2C3650CDAAC9D9A6799D0C698FF1BD27C9A67612FC71D3238E943)
