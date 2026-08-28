# Soft Keyboard Management

The soft keyboard serves as a critical user interaction channel for text input. This topic explains how to control soft keyboard display and hiding when using system input components ([TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput), [TextArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea), [Search](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-search), and [RichEditor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor)).

#### Displaying the Soft Keyboard

By default, the soft keyboard automatically appears when an input component gains focus

through the following methods:

1.  Interactive focus: tapping, double-tapping, or long-pressing the input field
    
2.  Programmatic focus: using [requestFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9) or [defaultFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus#defaultfocus9) APIs
    
3.  External keyboard navigation: pressing **Tab**, **Shift+Tab**, or arrow keys (which shows the physical keyboard toolbar instead of the soft keyboard)
    

The system distinguishes between system soft keyboards and custom keyboards. The [enableKeyboardOnFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea#enablekeyboardonfocus10) attribute affects system keyboard display but not custom keyboards. When **enableKeyboardOnFocus** is set to **false**, the system soft keyboard only appears when focus is acquired through clicking or key press interactions. **enableKeyboardOnFocus** does not affect custom keyboards. External physical keyboards suppress system soft keyboards but do not affect custom keyboards.

## Interactive Focus

The following demonstrates soft keyboard behavior during input field tapping, double-tapping, or long-pressing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sgDT2ff6T7ed5sziQQWeLw/en-us_image_0000002568764405.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D382C6861F1ECFAAC3574D8D40462D27FC75E8A57B51DA83FFC2178E346505F3)

## Programmatic Focus

Use focus control methods, such as [defaultFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus#defaultfocus9) and [requestFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9), to programmatically focus input fields and trigger keyboard display. For details, see [Implementing Focus Support](../../implementing-interaction-responses/implementing-focus-support/document.md).

The following example demonstrates transferring focus to a text input field and displaying the soft keyboard when a button is clicked.

@Entry
@Component
struct demo {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = "";

  build() {
    Column({ space: 20 }) {
      Button('Focus Input Field').onClick(() => {
        this.getUIContext().getFocusController().requestFocus("textInput1")
      })
      TextInput({ controller: this.controller, text: this.inputValue })
        .id("textInput1")
    }
    .height('100%')
    .width('80%')
    .margin('10%')
    .justifyContent(FlexAlign.Center)
  }
}

## External Keyboard Navigation

When a physical keyboard is connected, users can use **Tab**, **Shift+Tab**, or arrow keys to navigate focus. When focus moves to an input field, the physical keyboard's floating toolbar appears. For details, see [Focus Traversal Guidelines](../../implementing-interaction-responses/implementing-focus-support/document.md#focus-traversal-guidelines).

The following example demonstrates focus navigation with a connected physical keyboard. Repeatedly pressing the **Tab** key cycles focus among the three page components. Focus transitions are visually indicated by the **Text** component's blue border and the **TextInput** component's blinking cursor. When the **TextInput** component gains focus, the cursor appears and the physical keyboard's floating toolbar is displayed.

@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Text('Text.focusable(true)')
        .focusable(true)

      TextInput({ placeholder: "TextInput" })

      TextInput({ placeholder: "TextInput" })
    }
    .height('100%')
    .width('80%')
    .margin('10%')
    .justifyContent(FlexAlign.Center)
  }
}

#### Hiding the Soft Keyboard

When a text input field gains focus, the soft keyboard appears. However, the keyboard does not automatically hide when the text input field loses focus. Instead, the keyboard's visibility depends on the next focused component: It remains visible if the new component requires text input, but hides if the component does not need the keyboard. Typically, only text input components require soft keyboard access.

The soft keyboard hides in the following common scenarios when focus moves to components that do not require text input:

1.  Tapping the keyboard's close button
    
2.  Dragging selected text
    
3.  Swipe gestures on the text input field
    
4.  Page navigation
    
5.  Calling [TextInputController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#textinputcontroller8)
    
6.  Moving focus to non-text-input components
    

## Keyboard Close Button

The soft keyboard provides a close button that users can tap to hide the keyboard.

The following example demonstrates this dismissal scenario:

@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Blank()
        .height(350)
      Flex({ direction: FlexDirection.Row }) {
        TextInput({ placeholder: 'TextInput' })
      }
      .width(250)
    }
    .height('100%')
    .width('90%')
    .padding('5%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/48JrxF2_R8ypG5-DLbvRoA/en-us_image_0000002537764680.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59DF7923F95AB01E94435DBFAD1B6387B5B5DD52DFBCEA280BEB2310D9F2865B)

## Text Dragging

Dragging selected text in the text input field automatically hides the keyboard. For details, see [Implementing Unified Drag and Drop](../../implementing-interaction-responses/implementing-unified-drag-and-drop/document.md).

The following example demonstrates keyboard dismissal during text dragging operations:

@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Blank()
        .height(350)
      Flex({ direction: FlexDirection.Row }) {
        TextInput({ text: 'Drag this text to hide keyboard' })
          .selectAll(true)
          .defaultFocus(true)
      }
      .width(250)
    }
    .height('100%')
    .width('90%')
    .padding('5%')
  }
}

## Swipe Gestures

Swipe gestures hide the soft keyboard. The figure below demonstrates this dismissal scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/HI22--rnQDuIRyqcC6ftsw/en-us_image_0000002537924620.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A914B7966FD3EDA682AD17E72CF40F2808A69C29C7C3A5DB9B87C2AD7436F995)

## Page Navigation

Navigating away from the text input pages hides the keyboard.

For details about the page navigation syntax, see [Component Navigation (Recommended)](../../setting-component-navigation-and-page-routing/component-navigation-recommended/document.md).

Source page:

// Index.ets
@Entry
@Component
struct Index {
  // Create a navigation controller object and pass it to the Navigation component.
  pathStack: NavPathStack = new NavPathStack()

  build() {
    Navigation(this.pathStack) {
      Column({ space: 30 }) {
        Blank().height(150)
        TextInput({ placeholder: 'TextInput' })
        Button('Navigate to Next Page')
          .onClick(() => {
            this.pathStack.pushPath({ name: 'demo\_text\_1' })
          })
      }
      .height('100%')
      .width('80%')
      .margin('10%')
    }
    .title('Page Navigation Example')
  }
}

Destination page:

// demo\_text\_1.ets
@Builder
export function demo\_text\_1\_Builder() {
  demo\_text\_1()
}

@Component
struct demo\_text\_1 {
  pathStack: NavPathStack = new NavPathStack()
  // Destination page
  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Text('This page contains no keyboard-requiring components')
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack
    })
  }
}

Route configuration:

Add the route table configuration to the **module.json5** file of the redirection target module.

{
  "module": {
    //...
    "routerMap": "$profile:route\_map",
    //...
  }
}

Create the **route\_map.json** file in the **resources/base/profile** directory of the project. Add the following configuration information:

// route\_map.json
{
  "routerMap": \[
    {
      "name": "demo\_text\_1",
      "pageSourceFile": "src/main/ets/pages/demo\_text\_1.ets",
      "buildFunction": "demo\_text\_1\_Builder"
    }
  \]
}

## Controller-Based Dismissal

You can use [TextInputController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#textinputcontroller8) to call [stopEditing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#stopediting10) to programmatically hide the keyboard.

The following example shows how to hide the soft keyboard using the [TextInputController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#textinputcontroller8).

@Entry
@Component
struct demo {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = "";

  build() {
    Column({ space: 30 }) {
      Button('Dismiss Keyboard').onClick(() => {
        this.controller.stopEditing()
      })
      TextInput({ controller: this.controller, text: this.inputValue })
    }
    .width('80%')
    .height('100%')
    .margin('10%')
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/CFPwCTUxR_-bzCo1wJ62og/en-us_image_0000002568684397.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CC89DAD868F2681BE4E9E8485622F67D9A596B22267B14E000EA1FF1DD2211C)

## Focus Transfer

Moving focus to non-input components automatically hides the soft keyboard.

Focus transfer can be controlled programmatically using [requestFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9) and [clearFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12). For details, see [Implementing Focus Support](../../implementing-interaction-responses/implementing-focus-support/document.md).

Compared with using text input controllers to exit edit mode, focus transfer offers better scalability for pages with multiple input fields, eliminating the need for configuring individual controllers for each text input.

The following example demonstrates keyboard dismissal by transferring focus to a button using [requestFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9):

@Entry
@Component
struct TextInputExample {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = "";

  build() {
    Column({ space: 20 }) {
      Button('change focus').onClick(() => {
        this.getUIContext().getFocusController().requestFocus("button")
      }).id("button")
      TextInput({ controller: this.controller, text: this.inputValue })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('80%')
    .margin('10%')
  }
}

The following example demonstrates automatic soft keyboard dismissal when scrolling begins. As the scroll container [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) starts scrolling, the [clearFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12) API clears current focus, transferring it to the page's root container node. Since root containers do not require soft keyboard input, the keyboard automatically hides.

@Entry
@Component
struct Index {
  private arr: number\[\] = Array.from<number, number>(
    { length: 100 } as ArrayLike<number>,
    (\_, i: number) => i + 1
  );

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number, index?: number) => {
          ListItem() {
            Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
              TextInput({ placeholder: 'TextInput ' + item })
            }
          }
        }, (item: string) => item)
      }
      .onScrollStart(() => {
        // Clear current focus when the List component starts to scroll.
        this.getUIContext().getFocusController().clearFocus()
      })
      .width('80%')
      .height('80%')
      .margin('10%')
    }
    .justifyContent(FlexAlign.Center)
  }
}

#### FAQs

You may encounter specific scenarios or customization requirements when working with soft keyboards. This section addresses common challenges to help you better manage the keyboard behavior.

## Preventing Soft Keyboard Display When the Text Input Field Gains Focus

**Question**

How do I prevent the soft keyboard from appearing when tapping a text input field?

**Analysis**

By default, tapping a text input field triggers focus acquisition and automatically displays the system soft keyboard. However, when a custom keyboard is configured using [customKeyboard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#customkeyboard10), the system keyboard is suppressed and the custom keyboard appears instead.

**Answer**

Configure an empty custom keyboard to prevent any keyboard display while maintaining the input field focus.

The sample code is as follows:

@Entry
@Component
struct demo {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = "";

  // Create a custom keyboard component.
  @Builder
  CustomKeyboardBuilder() {
    Column() {
    }
  }

  build() {
    Column() {
      TextInput({ placeholder: 'TextInput', controller: this.controller, text: this.inputValue })// Bind a custom keyboard.
        .customKeyboard(this.CustomKeyboardBuilder())
    }
    .justifyContent(FlexAlign.Center)
    .width('80%')
    .margin('10%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/9GDo01dCSUO_gew1a8STlA/en-us_image_0000002568764407.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F57BA5F944E7C5EC451216EE906DD2008E2558AA6225334F40436141D2999CAB)

## Maintaining the Keyboard After the Send Action

**Question**

How do I keep the keyboard visible after the send button is tapped?

**Analysis**

The [enterKeyType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea#enterkeytype11) attribute configures the Enter key style, including send variants. Tapping the Enter key typically causes input fields to lose focus and dismiss the keyboard on non-TV devices.

**Answer**

Configure [enterKeyType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea#enterkeytype11) for the soft keyboard based on your needs. When **enterKeyType** is set to any value except **EnterKeyType.NEW\_LINE**, the [onSubmit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea#onsubmit14) event triggers on return key press. In the **onSubmit** callback of **TextArea**, call [keepEditableState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput#keepeditablestate11) to maintain the edit state and keyboard visibility.

The following example demonstrates a send-style Enter key that maintains keyboard visibility after being tapped:

@Entry
@Component
struct demo {
  build() {
    Column({ space: 20 }) {
      TextArea({ placeholder: 'The keyboard dismisses after the send key is tapped' })
        .enterKeyType(EnterKeyType.Send)

      TextArea({ placeholder: 'The keyboard persists after the send key is tapped' })
        .enterKeyType(EnterKeyType.Send)
        .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
          // Call keepEditableState to maintain the edit state of the text input field.
          event.keepEditableState();
        })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('80%')
    .margin('10%')
  }
}
