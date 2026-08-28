# Component Keyboard Shortcut Event

You can set custom keyboard shortcuts for components, with the flexibility to define multiple shortcuts per component.

A component will still respond to the set custom shortcuts even if it is not in focus or visible on the active page, as long as it is part of the component tree within a window that has focus.

Better yet, you can set custom events for custom keyboard shortcuts, so that when the defined keys of a keyboard shortcut are pressed, the custom event is triggered. If no custom event is set, the behavior of a keyboard shortcut is the same as that of a click.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/MzJ4g5t0Q5ivAOMc_mwX0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F704B51F0258743AEC8535BA93F83041C077ED0DD1896731497D2F3C6F19E603)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### keyboardShortcut

keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T

Sets a keyboard shortcut for the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [FunctionKey](../../../common-definitions/enums/document.md#functionkey10) | Yes | 
Character key (which can be entered through the keyboard) or [function key](../../../common-definitions/enums/document.md#functionkey10).

An empty string means to disable the keyboard shortcut.

 |
| keys | Array<[ModifierKey](../../../common-definitions/enums/document.md#modifierkey10)\> | Yes | 

Modifier keys.

This parameter can be left empty only when **value** is set to a [function key](../../../common-definitions/enums/document.md#functionkey10).

 |
| action | () => void | No | 

Callback for a custom event after the keyboard shortcut is triggered.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Precautions for Using Keyboard Shortcuts

Keyboard shortcuts, as system keys, take precedence over the common key event **OnKeyEvent**. For details about the key event triggering logic, see [Key Event Data Flow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-development-guide-keyboard#key-event-data-flow).

| Scenario | Processing Logic | Example |
| :-- | :-- | :-- |
| Components that support the **onClick** event | Custom keyboard shortcuts are supported. | – |
| Requirements for custom keyboard shortcuts | Modifier keys (**Ctrl**, **Shift**, **Alt**, and combinations) plus a single character or [function key](../../../common-definitions/enums/document.md#functionkey10). | Button('button1').keyboardShortcut('a',\[ModifierKey.CTRL\]) |
| Multiple components with identical shortcuts | Only the shallowest node in the component tree responds. | 
Button('button1').keyboardShortcut('a',\[ModifierKey.CTRL\])

Button('button2').keyboardShortcut('a',\[ModifierKey.CTRL\])

 |
| Component focus state | Keyboard shortcuts respond when the window has focus, regardless of component focus. | – |
| Single function key shortcuts | Function keys can be used without modifier keys. | Button('button1').keyboardShortcut(FunctionKey.F2,\[\]) |
| Empty **value** parameter in **keyboardShortcut** | 

The keyboard shortcut is disabled.

Multi-bound shortcuts cannot be unbound.

 | 

Button('button1').keyboardShortcut('',\[ModifierKey.CTRL\])

Button('button2').keyboardShortcut('',\[\])

 |
| Modifier key (**Ctrl**, **Shift**, or **Alt** defined in **keys** of **keyboardShortcut**) positions | Both left and right modifier keys are recognized. | Button('button1').keyboardShortcut('a',\[ModifierKey.CTRL, ModifierKey.ALT\]) |
| Character key case sensitivity in the **value** parameter of the **keyboardShortcut** API | The response is case-insensitive. | 

Button('button1').keyboardShortcut('a',\[ModifierKey.CTRL\])

Button('button2').keyboardShortcut('A',\[ModifierKey.CTRL\])

 |
| Response to keyboard shortcuts | The component responds to a keyboard shortcut when the keys specified by **keys** are pressed and the key specified by **value** triggers a down event. (Long-pressing leads to continuous response.) | – |
| 

Hidden components

 | The component still responds to keyboard shortcuts. | – |
| Disabled components ([enabled](../../../universal-attributes/interaction-properties/enable-disable-control/document.md#enabled) set to **false**) | Disabled components do not respond to keyboard shortcuts. | – |
| 

1\. Duplicate system shortcuts (including those same as predefined ones)

2\. Multiple character keys in **value**

3\. Duplicate modifier keys in **keys**

 | In these cases, the keyboard shortcut is not added, and the previously added keyboard shortcuts still work. | 

Button('button1').keyboardShortcut(FunctionKey.F4,\[ModifierKey.ALT\])

Button('button2').keyboardShortcut('ab',\[ModifierKey.CTRL\])

Button('button3').keyboardShortcut('ab',\[ModifierKey.CTRL,ModifierKey.CTRL\])

 |

## System-Defined Keyboard Shortcuts That Cannot Be Bound

The following key combinations cannot function as keyboard shortcuts:

-   Alt + F4
-   Alt + Shift + F4
-   Alt + TAB
-   Alt + Shift + TAB
-   Ctrl + Shift + ESC

## Predefined Key Events

The following table lists the predefined key events.

The predefined key events and custom key events have priorities. Events with higher priorities intercept those with lower priorities. For details about the response priorities, see [Key Event Data Flow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-development-guide-keyboard#key-event-data-flow).

| Keyboard Shortcut | Focused Component | Usage | Event Handling Category |
| :-- | :-- | :-- | :-- |
| Arrow keys, **Shift** + Arrow keys | Text box component | Moves the cursor. | Input method |
| Arrow keys, **Shift** + Arrow keys | Universal component | Moves focus in navigation. | System keys |
| **Tab**, **Shift** + **Tab** | Universal component | Triggers focus navigation or moves focus in navigation. | System keys |

#### Example

## Example 1: Setting Component Keyboard Shortcuts

This example demonstrates how to set up keyboard shortcuts for components. This allows users to press the modifier key and accompanying key at the same time to trigger the component to respond to the shortcut and trigger the **onClick** event or a custom event.

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column({ space: 5 }) {
        Text(this.message)
        Button("Test short cut 1").onClick((event: ClickEvent) => {
          this.message = "I clicked Button 1";
          console.info("I clicked 1");
        }).keyboardShortcut('.', \[ModifierKey.SHIFT, ModifierKey.CTRL, ModifierKey.ALT\])
          .onKeyEvent((event: KeyEvent) => {
            console.info("event.keyCode: " + JSON.stringify(event));
          })
        Button("Test short cut 2").onClick((event: ClickEvent) => {
          this.message = "I clicked Button 2";
          console.info("I clicked 2");
        }).keyboardShortcut('1', \[ModifierKey.CTRL\])
        Button("Test short cut 3").onClick((event: ClickEvent) => {
          this.message = "I clicked Button 3";
          console.info("I clicked 3");
        }).keyboardShortcut('A', \[ModifierKey.SHIFT\])
        Button("Test short cut 4").onClick((event: ClickEvent) => {
          this.message = "I clicked Button 4";
          console.info("I clicked 4");
        }).keyboardShortcut(FunctionKey.F5, \[\], () => {
          this.message = "I clicked Button 4";
          console.info("I clicked user callback.");
        }).keyboardShortcut(FunctionKey.F3, \[\])
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/2PM1q2ZiSk-Pvl4j1ZCYIQ/en-us_image_0000002568765109.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08FB4A1A17AD7E3B9814D6408560B2ADBF158AC0D3C032B1493C811ADB070489)

## Example 2: Binding and Unbinding Keyboard Shortcuts

This example demonstrates how to bind and unbind keyboard shortcuts.

@Entry
@Component
struct Index {
  @State message: string = 'disable'
  @State shortCutEnable: boolean = false
  @State keyValue: string = ''

  build() {
    Row() {
      Column({ space: 5 }) {
        Text('Ctrl+A is ' + this.message)
        Button("Test short cut").onClick((event: ClickEvent) => {
          this.message = "I clicked Button";
          console.info("I clicked");
        }).keyboardShortcut(this.keyValue, \[ModifierKey.CTRL\])
        Button(this.message + 'shortCut').onClick((event: ClickEvent) => {
          this.shortCutEnable = !this.shortCutEnable;
          this.message = this.shortCutEnable ? 'enable' : 'disable';
          this.keyValue = this.shortCutEnable ? 'a' : '';
        })
        Button('multi-shortcut').onClick((event: ClickEvent) => {
          console.info('Trigger keyboard shortcut success.')
        }).keyboardShortcut('q', \[ModifierKey.CTRL\])
          .keyboardShortcut('w', \[ModifierKey.CTRL\])
          .keyboardShortcut('', \[\]) // Unbinding does not work when there are multi-bound shortcuts.
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-c5MIdM9ScOU4sjU5ycLDg/en-us_image_0000002537765384.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A13FFA21262915106DC52FB284B8838D4C18C7C21891742F9764337FD4C47A17)
