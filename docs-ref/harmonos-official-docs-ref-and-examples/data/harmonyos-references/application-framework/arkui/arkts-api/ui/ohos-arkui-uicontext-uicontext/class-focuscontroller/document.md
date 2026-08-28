# Class (FocusController)

Provides capabilities to control focus, including features such as clearing, moving, and activating focus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/kiRZy3ToT9KJ2cc7q-idcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EDD239719C9360491FAA27399F8BB36BD47388794B1D892B182367D3E579007)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   In the following API examples, you must first use [getFocusController()](../class-uicontext/document.md#getfocuscontroller12) in **UIContext** to obtain a **FocusController** instance, and then call the APIs using the obtained instance.
    

#### clearFocus12+

clearFocus(): void

Clears the focus and forcibly moves the focus to the root container node of the page, causing other nodes in the focus chain to lose focus.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

In this example, **button2** receives initial focus by default. After **clearFocus** is clicked, focus returns to the page's root container node **column1**. Pressing the **Tab** key then restores focus to **button2**. Clicking **button1** transfers focus to that button. Following another **clearFocus** click, focus again returns to **column1**, and pressing **Tab** subsequently moves focus to **button1**.

@Entry
@Component
struct ClearFocusExample {
  @State inputValue: string = '';
  @State btColor: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Button('button1')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(Color.Blue)
        Button('button2')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor)
          .defaultFocus(true)
          .onFocus(() => {
            this.btColor = Color.Red;
          })
          .onBlur(() => {
            this.btColor = Color.Blue;
          })
        Button('clearFocus')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .backgroundColor(Color.Blue)
          .onClick(() => {
            this.getUIContext().getFocusController().clearFocus();
          })
      }
      .id('column2')
    }
    .id('column1')
    .width('100%')
    .height('100%')
  }
}

#### requestFocus12+

requestFocus(key: string): void

Transfers focus to a component node by the component ID, which is effective immediately.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | [Component ID](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target node. |

**Error codes**

For details about the error codes, see [Focus Error Codes](../../../../error-codes/ui/focus-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 150001 | the component cannot be focused. |
| 150002 | This component has an unfocusable ancestor. |
| 150003 | the component is not on tree or does not exist. |

**Example**

@Entry
@Component
struct RequestExample {
  @State btColor: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Button('Button')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor)
          .onFocus(() => {
            this.btColor = Color.Red;
          })
          .onBlur(() => {
            this.btColor = Color.Blue;
          })
          .id("testButton")

        Divider()
          .vertical(false)
          .width("80%")
          .backgroundColor(Color.Black)
          .height(10)

        Button('requestFocus')
          .width(200)
          .height(70)
          .onClick(() => {
            this.getUIContext().getFocusController().requestFocus("testButton");
          })

        Button('requestFocus fail')
          .width(200)
          .height(70)
          .onClick(() => {
            try {
              this.getUIContext().getFocusController().requestFocus("eee");
            } catch (error) {
              console.error(\`requestFocus failed code is ${error.code} message is ${error.message}\`);
            }
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}

#### activate14+

activate(isActive: boolean, autoInactive?: boolean): void

Sets the [focus activation state](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event) of this page.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isActive | boolean | Yes | 
Whether to enter or exit the focus activation state.

The value **true** means to enter the focus activation state, and **false** means to exit the focus activation state.

 |
| autoInactive | boolean | No | 

Logic for exiting the focus activation state.

The value **true** means the focus activation state will be exited automatically when touch or mouse events are triggered, and **false** means the state is controlled solely by API calls.

Default value: **true**

 |

**Example**

// This example demonstrates how to enter the focus activation state when the page loading is completed. In this state, arrow keys can be used for focus navigation.
@Entry
@Component
struct ActivateExample {
  aboutToAppear() {
    this.getUIContext().getFocusController().activate(true, false);
  }

  aboutToDisappear() {
    this.getUIContext().getFocusController().activate(false);
  }

  build() {
    Row() {
      Button('Button1')
        .width(200)
        .height(70)
        .defaultFocus(true)

      Button('Button2')
        .width(200)
        .height(70)

      Button('Button3')
        .width(200)
        .height(70)
    }
    .padding(10)
    .justifyContent(FlexAlign.SpaceBetween)
    .width(800)
  }
}

#### isActive20+

isActive(): boolean

Obtains the focus activation state of the UI instance.

For details about the focus activation state, see [Basic Concepts](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Focus activation state of the UI instance. The value **true** means that the instance has entered the focus activation state, and **false** means that the instance has exited the focus activation state. |

**Example**

The following example verifies that **isActive()** returns the focus activation state of the UI instance.

@Entry
@Component
struct ClearFocusExample {
  @State inputValue: string = '';
  @State btColor: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Button('button1')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(Color.Blue)
          .onClick(() => {
            console.info("button1 onClick");
            this.getUIContext().getFocusController().activate(true);
            console.info(\`focus status ${this.getUIContext().getFocusController().isActive()}\`);
          })
        Button('button2')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor)
          .defaultFocus(true)
          .onClick(() => {
            console.info("button2 onClick");
            this.getUIContext().getFocusController().activate(false);
            console.info(\`focus status ${this.getUIContext().getFocusController().isActive()}\`);
          })
          .onFocus(() => {
            this.btColor = Color.Red;
          })
          .onBlur(() => {
            this.btColor = Color.Blue;
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}

#### setAutoFocusTransfer14+

setAutoFocusTransfer(isAutoFocusTransfer: boolean): void

Sets whether the new page automatically obtains focus during page switching.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isAutoFocusTransfer | boolean | Yes | Whether the new page automatically obtains focus during page switching using navigation components or APIs, such as [Router](../../ohos-router-page-routing-not-recommended/document.md), [Navigation](../../../../arkts-components/navigation-and-switching/navigation/document.md), [Menu](../../../../arkts-components/menus/menu/document.md), [Dialog](../../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md), and [Popup](../../../../arkts-components/system-preset-ui-component-library/popup/document.md). The value **true** means the new page automatically obtains focus, and **false** means the opposite. Default value: **true**. |

**Example**

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('This is a custom dialog box')
        .fontSize(30)
        .height(100)
      Text('The dialog box should not automatically acquire focus')
        .fontSize(20)
        .height(100)
      Button('Close Dialog Box')
        .onClick(() => {
          if (this.controller != undefined) {
            this.getUIContext().getFocusController().setAutoFocusTransfer(true);
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({}),
  });

  aboutToDisappear() {
    this.dialogController = null;
  }

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.getUIContext().getFocusController().setAutoFocusTransfer(false);
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

#### setKeyProcessingMode15+

setKeyProcessingMode(mode: KeyProcessingMode): void

Sets the mode for processing key events.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [KeyProcessingMode](../../../../arkts-components/universal-attributes/interaction-properties/focus-control/document.md#keyprocessingmode15) | Yes | Mode for processing key events. |

**Example**

// This example demonstrates how to set the focus behavior after the page is loaded.
@Entry
@Component
struct Index {
  aboutToAppear() {
    this.getUIContext().getFocusController().setKeyProcessingMode(KeyProcessingMode.ANCESTOR\_EVENT);
  }

  build() {
    Row() {
      Row() {
        Button('Button1').id('Button1').onKeyEvent((event) => {
          console.info("Button1");
          return true;
        })
        Button('Button2').id('Button2').onKeyEvent((event) => {
          console.info("Button2");
          return true;
        })
      }
      .width('100%')
      .height('100%')
      .id('Row1')
      .onKeyEventDispatch((event) => {
        let context = this.getUIContext();
        context.getFocusController().requestFocus('Button1');
        return context.dispatchKeyEvent('Button1', event);
      })
    }
    .height('100%')
    .width('100%')
    .onKeyEventDispatch((event) => {
      if (event.type == KeyType.Down) {
        let context = this.getUIContext();
        context.getFocusController().requestFocus('Row1');
        return context.dispatchKeyEvent('Row1', event);
      }
      return true;
    })
  }
}
