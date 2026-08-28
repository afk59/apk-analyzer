# ExceptionPrompt

The exception prompt component is used to show an error message when an error arises.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/4FvXmmhBR9a-DGP_lkjzjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5F50CCECE678AA05448B99DA74AF0F9AE214B635A995B72289E03D85C569EED)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ExceptionPrompt, PromptOptions, MarginType } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### ExceptionPrompt

ExceptionPrompt({ options: PromptOptions, onTipClick?: ()=>void, onActionTextClick?: ()=>void })

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [PromptOptions](#promptoptions) | Yes | @Prop | Exception prompt configuration. |
| onTipClick | ()=>void | No | \- | Callback invoked when the prompt text on the left is clicked. |
| onActionTextClick | ()=>void | No | \- | Callback invoked when the icon on the right is clicked. |

#### PromptOptions

Defines the exception prompt options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Icon style of the exception prompt.

If this parameter is not set or is set to **undefined**, the icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon style of the exception prompt, which has higher priority than **icon**.

If this parameter is not set or is set to **undefined**, the symbol icon is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| tip | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text content of the exception prompt.

By default, the following text resources are provided:

1\. **ohos\_network\_not\_connected**: displayed when no Internet connection.

2\. **ohos\_network\_connected\_unstable**: displayed when the Internet connection is unstable.

3\. **ohos\_unstable\_connect\_server**: displayed when the server fails to be connected.

4\. **ohos\_custom\_network\_tips\_left**: displayed when an Internet connection is available but the location fails to be obtained.

If this parameter is not set or is set to **undefined**, the text content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| marginType | [MarginType](#margintype) | No | No | 

Margin type of the exception prompt.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| actionText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Text of the icon on the right of the exception prompt.

If this parameter is not set or is set to **undefined**, the text is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| marginTop | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | No | 

Top margin of the exception prompt.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isShown | boolean | No | Yes | 

Whether the exception prompt is displayed.

**true**: The exception prompt is displayed.

**false**: The exception prompt is hidden.

Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### MarginType

Defines the margin type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT\_MARGIN | 0 | 
Default margin:

Margin 1: referenced from **ohos\_id\_card\_margin\_start**.

Margin 2: referenced from **ohos\_id\_card\_margin\_end**.

 |
| FIT\_MARGIN | 1 | 

Adaptable margin:

Margin 1: referenced from **ohos\_id\_max\_padding\_start**.

Margin 2: referenced from **ohos\_id\_max\_padding\_end**.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Configuring an Exception Prompt

This example demonstrates how to configure an exception prompt, including the exception icon, text, margin, and the text content of the right-side icon button.

import { ExceptionPrompt, PromptOptions, MarginType } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State options: PromptOptions = {
    icon: $r('sys.media.ohos\_ic\_public\_fail'),
    tip: 'Error',
    marginType: MarginType.DEFAULT\_MARGIN,
    actionText: 'Set network',
    marginTop: 80,
    isShown: true,
  }

  build() {
    Column() {
      ExceptionPrompt({
        options: this.options,
        onTipClick: () => {
          // Handle clicks on the left text to switch to a connected state.
        },
        onActionTextClick: () => {
          // Handle clicks on the Set network button to open the network settings dialog box.
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/6xryUbHNTIyQbZInznuP5Q/en-us_image_0000002568685687.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94019C4A792F579E4AF18123AEE8F292A8F6414120BB9CABDA369C881A474872)

## Example 2: Setting a Dialog-Type Exception Prompt

This example uses a custom dialog box to set a dialog-type exception prompt.

import { ExceptionPrompt, PromptOptions, MarginType } from '@kit.ArkUI';

@CustomDialog
struct CustomDialogExample {
  @Link textValue: string;
  @Link inputValue: string;
  @State options: PromptOptions = {
    icon: $r('sys.media.ohos\_ic\_public\_fail'),
    tip: 'Error',
    marginType: MarginType.DEFAULT\_MARGIN,
    actionText: 'Settings',
    marginTop: 5,
    isShown: true,
  };
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };
  controller?: CustomDialogController;

  // To pass multiple other controllers into a CustomDialog to open another or several other custom dialog boxes within it,
  // place the controller pointing to itself last.
  build() {
    Column() {
      ExceptionPrompt({
        options: this.options,
      })
      TextInput({ placeholder: '', text: this.textValue }).margin({ top: 70 }).height(60).width('90%')
        .onChange((value: string) => {
          this.textValue = value;
        })
      Text('Are you sure you want to change the text?').fontSize(16).margin({ bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('No')
          .onClick(() => {
            this.controller?.close();
            this.cancel();
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('OK')
          .onClick(() => {
            this.inputValue = this.textValue;
            this.controller?.close();
            this.confirm();
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })
    }
  }
}

@Entry
@Component
struct Index1 {
  @State ButtonText: string = '';
  @State MAP\_HEIGHT: string = '30%';
  @State duration: number = 2500;
  @State tips: string = '';
  @State actionText: string = '';
  controller: TextInputController = new TextInputController();
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };
  @State options: PromptOptions = {
    icon: $r('sys.media.ohos\_ic\_public\_fail'),
    tip: '',
    marginType: MarginType.DEFAULT\_MARGIN,
    actionText: '',
    marginTop: 80,
    isShown: true,
  }
  @State textValue: string = '';
  @State inputValue: string = 'click me';
  dialogController: CustomDialogController | undefined = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: this.onCancel,
      confirm: this.onAccept,
      textValue: $textValue,
      inputValue: $inputValue,
    }),
    cancel: this.existApp,
    autoCancel: true,
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
  })

  aboutToDisappear() {
    this.dialogController = undefined; // Set dialogController to undefined.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('Click Me')
        .width('30%')
        .margin({ top: 420 })
        .zIndex(999)
        .onClick(() => {
          if (this.dialogController != undefined) {
            this.dialogController.open();
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/hH1tfMTvTIWtqrwRubfAOQ/en-us_image_0000002568765697.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=886620CFAE26593FAE0891280F6860E4C8B53FEB10F8F088203B4FD1CEF9AC92)

## Example 3: Setting the Symbol Icon

This example demonstrates how to use **symbolStyle** in **PromptOptions** to set custom symbol icons. This functionality is supported since API version 18.

import { ExceptionPrompt, MarginType, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      ExceptionPrompt({
        options: {
          icon: $r('sys.symbol.house'),
          tip: 'Error',
          marginType: MarginType.DEFAULT\_MARGIN,
          actionText: 'Set network',
          marginTop: 80,
          isShown: true,
        },
      })
      ExceptionPrompt({
        options: {
          icon: $r('sys.symbol.house'),
          symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor(\[Color.Red\]),
          tip: 'Error',
          marginType: MarginType.DEFAULT\_MARGIN,
          actionText: 'Set network',
          marginTop: 200,
          isShown: true,
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/aFkaa3dLTvubWg2FlDlL5Q/en-us_image_0000002537765972.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57338C15DE52DA95711038FA6F610AE857C74AD64AEDE2304EB150949B9812AC)
