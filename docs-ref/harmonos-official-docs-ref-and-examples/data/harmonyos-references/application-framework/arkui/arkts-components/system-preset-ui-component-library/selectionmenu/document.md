# SelectionMenu

The **SelectionMenu** component serves as a context menu designed specifically for text selection in the [RichEditor](../../text-and-input/richeditor/document.md) or [Text](../../text-and-input/text/document.md) component. This component must be bound to either a **RichEditor** component through its [bindSelectionMenu](../../text-and-input/richeditor/document.md#bindselectionmenu) API or a **Text** component using its [bindSelectionMenu](../../text-and-input/text/document.md#bindselectionmenu11) API to work properly, as it cannot operate as an independent UI element. It is recommended that this component be displayed through mouse right-click or text selection events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/_Uu8kWosSnWIcVH_DMPAxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A66150163D19A1800618C54B1770B63C5E8BEC2E11EC9A2C33CF9803DBA85B5D)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SelectionMenu, EditorMenuOptions, ExpandedMenuOptions, EditorEventInfo, SelectionMenuOptions } from '@kit.ArkUI';

#### Child Components

Not supported

#### SelectionMenu

SelectionMenu(options: SelectionMenuOptions): void

Defines a **SelectionMenu** component. When the input parameter is empty, both the component and its content area have a zero size, making the component invisible. For example, when a **SelectionMenu** component activated via right-click is bound to a [RichEditor](../../text-and-input/richeditor/document.md) component using [bindSelectionMenu](../../text-and-input/richeditor/document.md#bindselectionmenu), it will not be displayed when the **RichEditor** component receives a right-click event.

**Decorator**: @Builder

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SelectionMenuOptions](#selectionmenuoptions) | Yes | Configuration options of the **SelectionMenu** component. |

#### SelectionMenuOptions

Defines the configuration options of the **SelectionMenu** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| editorMenuOptions | Array<[EditorMenuOptions](#editormenuoptions)\> | No | Yes | 
Edit menu.

If **editorMenuOptions** is not set, the edit menu is not displayed.

When both **action** and **builder** in **EditorMenuOptions** are configured, clicking the edit icon will trigger both.

By default, the context menu is not closed when the edit menu icon is clicked. You can configure **closeSelectionMenu** of **RichEditorController** in **action** to enable the menu to be closed.

 |
| expandedMenuOptions | Array<[ExpandedMenuOptions](#expandedmenuoptions)\> | No | Yes | 

Expanded drop-down menu options.

If this parameter is left empty, the expanded drop-down menu is not displayed.

The options configured for **ExpandedMenuOptions** are displayed in the **More** menu option, and clicking **More** shows the expanded drop-down menu.

 |
| controller | [RichEditorController](../../text-and-input/richeditor/document.md#richeditorcontroller) | No | Yes | 

Rich text editor controller. If **controller** is set, the default system menu (including the cut, copy, and paste options) is displayed, and the preset menu features are provided.

If **controller** is left empty, the **More** menu option is not displayed. If **expandedMenuOptions** is not empty, the expanded drop-down menu is displayed.

By default, the copy and paste feature is only available for rich text. To use the feature for content that includes both text and images, define custom **onCopy** and **onPaste** APIs. If a custom **onCopy** | **onPaste** API is defined, the default copy and paste feature is ineffective, and the custom API is called instead.

**NOTE**

When the preset copy option is selected, the custom context menu on selection is hidden, while the selected text is still highlighted.

When the preset select-all option is selected, the custom context menu on selection is hidden, while all text is highlighted.

When the preset paste option is selected, the style of the copied text is retained, whether the text is pasted to a blank area or not.

When the **copyOptions** attribute of the [RichEditor](../../text-and-input/richeditor/document.md) component is set to **CopyOptions.None**, the preset copy and cut features are not restricted.

 |
| onCopy | (event?: [EditorEventInfo](#editoreventinfo)) => void | No | Yes | 

Event callback to take the place of the preset copy menu option.

It is effective only when the **controller** parameter is set and the preset menu is available.

**NOTE**

**event** indicates the returned information.

 |
| onPaste | (event?: [EditorEventInfo](#editoreventinfo)) => void | No | Yes | 

Event callback to take the place of the preset paste menu option.

It is effective only when the **controller** parameter is set and the preset menu is available.

**NOTE**

**event** indicates the returned information.

 |
| onCut | (event?: [EditorEventInfo](#editoreventinfo)) => void | No | Yes | 

Event callback to take the place of the preset cut menu option.

It is effective only when the **controller** parameter is set and the preset menu is available.

**NOTE**

**event** indicates the returned information.

 |
| onSelectAll | (event?: [EditorEventInfo](#editoreventinfo)) => void | No | Yes | 

Event callback to take the place of the preset select-all menu option.

It is effective only when the **controller** parameter is set and the preset menu is available.

**NOTE**

**event** indicates the returned information.

 |

#### EditorMenuOptions

Describes the edit menu options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Icon.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| builder | () => void | No | Yes | 

Builder of the custom component displayed upon click. It must be used with @Builder for building the custom component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| action | () => void | No | Yes | 

Action triggered when the menu option is clicked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../text-and-input/text-box-component-common-apis/document.md#symbolglyphmodifier12) | No | Yes | 

Symbol icon resource, which has higher priority than **icon**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ExpandedMenuOptions

Describes the expanded drop-down menu options.

Inherits from [MenuItemOptions](../../menus/menuitem/document.md#menuitemoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | () => void | No | Yes | Action triggered when the menu option is clicked. |

#### EditorEventInfo

Provides the information about the selected content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [RichEditorSelection](../../text-and-input/richeditor/document.md#richeditorselection) | No | Yes | Information about the selected content. |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported. The default width is 224 vp, and the height is adaptive.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Binding Context Menus on Selection with Different Trigger Methods

This example demonstrates the effects of a custom context menu on selection bound to text with different triggering modes.

import {
  SelectionMenu,
  EditorMenuOptions,
  ExpandedMenuOptions,
  EditorEventInfo,
  SelectionMenuOptions
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State select: boolean = true;
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State message: string = 'Hello world';
  @State textSize: number = 30;
  @State fontWeight: FontWeight = FontWeight.Normal;
  @State start: number = -1;
  @State end: number = -1;
  @State visibleValue: Visibility = Visibility.Visible;
  @State colorTransparent: Color = Color.Transparent;
  @State textStyle: RichEditorTextStyle = {};
  private editorMenuOptions: Array<EditorMenuOptions> =
    \[
      {
        // Replace $r('app.media.ic\_notepad\_textbold') with the image resource file you use.
        icon: $r("app.media.ic\_notepad\_textbold"), action: () => {
        if (this.controller) {
          let selection = this.controller.getSelection();
          let spans = selection.spans;
          spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
            if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
              let span = item as RichEditorTextSpanResult;
              this.textStyle = span.textStyle;
              let start = span.offsetInSpan\[0\];
              let end = span.offsetInSpan\[1\];
              let offset = span.spanPosition.spanRange\[0\];
              if (this.textStyle.fontWeight != 11) {
                this.textStyle.fontWeight = FontWeight.Bolder;
              } else {
                this.textStyle.fontWeight = FontWeight.Normal;
              }
              this.controller.updateSpanStyle({
                start: offset + start,
                end: offset + end,
                textStyle: this.textStyle
              })
            }
          })
        }
      }
      },
      {
        // Replace $r('app.media.ic\_notepad\_texttilt') with the image resource file you use.
        icon: $r("app.media.ic\_notepad\_texttilt"), action: () => {
        if (this.controller) {
          let selection = this.controller.getSelection();
          let spans = selection.spans;
          spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
            if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
              let span = item as RichEditorTextSpanResult;
              this.textStyle = span.textStyle;
              let start = span.offsetInSpan\[0\];
              let end = span.offsetInSpan\[1\];
              let offset = span.spanPosition.spanRange\[0\];
              if (this.textStyle.fontStyle == FontStyle.Italic) {
                this.textStyle.fontStyle = FontStyle.Normal;
              } else {
                this.textStyle.fontStyle = FontStyle.Italic;
              }
              this.controller.updateSpanStyle({
                start: offset + start,
                end: offset + end,
                textStyle: this.textStyle
              })
            }
          })
        }
      }
      },
      {
        // Replace $r('app.media.ic\_notepad\_underline') with the image resource file you use.
        icon: $r("app.media.ic\_notepad\_underline"),
        action: () => {
          if (this.controller) {
            let selection = this.controller.getSelection();
            let spans = selection.spans;
            spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
              if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
                let span = item as RichEditorTextSpanResult;
                this.textStyle = span.textStyle;
                let start = span.offsetInSpan\[0\];
                let end = span.offsetInSpan\[1\];
                let offset = span.spanPosition.spanRange\[0\];
                if (this.textStyle.decoration) {
                  if (this.textStyle.decoration.type == TextDecorationType.Underline) {
                    this.textStyle.decoration.type = TextDecorationType.None;
                  } else {
                    this.textStyle.decoration.type = TextDecorationType.Underline;
                  }
                } else {
                  this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black }
                }
                this.controller.updateSpanStyle({
                  start: offset + start,
                  end: offset + end,
                  textStyle: this.textStyle
                })
              }
            })
          }
        }
      },
      {
        // Replace $r('app.media.ic\_notepad\_fontsize') with the image resource file you use.
        icon: $r("app.media.ic\_notepad\_fontsize"), action: () => {
      }, builder: (): void => this.sliderPanel()
      },
      {
        // Replace $r('app.media.ic\_notepad\_textcolor') with the image resource file you use.
        icon: $r("app.media.ic\_notepad\_textcolor"), action: () => {
        if (this.controller) {
          let selection = this.controller.getSelection();
          let spans = selection.spans;
          spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
            if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
              let span = item as RichEditorTextSpanResult;
              this.textStyle = span.textStyle;
              let start = span.offsetInSpan\[0\];
              let end = span.offsetInSpan\[1\];
              let offset = span.spanPosition.spanRange\[0\];
              if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {
                this.textStyle.fontColor = Color.Black;
              } else {
                this.textStyle.fontColor = Color.Orange;
              }
              this.controller.updateSpanStyle({
                start: offset + start,
                end: offset + end,
                textStyle: this.textStyle
              })
            }
          })
        }
      }
      }\]
  private expandedMenuOptions: Array<ExpandedMenuOptions> =
    \[{
      // Replace $r('app.media.startIcon') with the image resource file you use.
      startIcon: $r("app.media.startIcon"), content: 'Dictionary', action: () => {
      }
    }, {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      startIcon: $r("app.media.startIcon"), content: 'Translate', action: () => {
      }
    }, {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      startIcon: $r("app.media.startIcon"), content: 'Search', action: () => {
      }
    }\]
  private expandedMenuOptions1: Array<ExpandedMenuOptions> = \[\];
  private selectionMenuOptions: SelectionMenuOptions = {
    editorMenuOptions: this.editorMenuOptions,
    expandedMenuOptions: this.expandedMenuOptions,
    controller: this.controller,
    onCut: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test cut' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    },
    onPaste: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test onPaste' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    },
    onCopy: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test cut' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    },
    onSelectAll: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test onPaste' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    }
  };

  @Builder
  sliderPanel() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
        Text('A').fontSize(15)
        Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })
          .width(210)
          .onChange((value: number, mode: SliderChangeMode) => {
            if (this.controller) {
              let selection = this.controller.getSelection();
              if (mode == SliderChangeMode.End) {
                if (this.textSize == undefined) {
                  this.textSize = 0;
                }
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
                    this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize);
                  }
                })
              }
              if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {
                this.start = selection.selection\[0\];
                this.end = selection.selection\[1\];
                this.textSize = value;
                this.controller.updateSpanStyle({
                  start: this.start,
                  end: this.end,
                  textStyle: { fontSize: this.textSize }
                })
              }
            }
          })
        Text('A').fontSize(20).fontWeight(FontWeight.Medium)
      }.borderRadius($r('sys.float.ohos\_id\_corner\_radius\_card'))
    }
    .shadow(ShadowStyle.OUTER\_DEFAULT\_MD)
    .backgroundColor(Color.White)
    .borderRadius($r('sys.float.ohos\_id\_corner\_radius\_card'))
    .padding(15)
    .height(48)
  }

  @Builder
  MyMenu() {
    Column() {
      SelectionMenu(this.selectionMenuOptions)
    }
    .width(256)
    .backgroundColor(Color.Transparent)
  }

  @Builder
  MyMenu2() {
    Column() {
      SelectionMenu({
        editorMenuOptions: this.editorMenuOptions,
        expandedMenuOptions: this.expandedMenuOptions1,
        controller: this.controller,
      })
    }
    .width(256)
    .backgroundColor(Color.Transparent)
  }

  @Builder
  MyMenu3() {
    Column() {
      SelectionMenu({
        editorMenuOptions: this.editorMenuOptions,
        expandedMenuOptions: this.expandedMenuOptions,
        controller: this.controller,
      })
    }
    .width(256)
    .backgroundColor(Color.Transparent)
  }

  build() {
    Column() {
      Button("SetSelection")
        .onClick((event: ClickEvent) => {
          if (this.controller) {
            this.controller.setSelection(0, 2);
          }
        })

      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } });
          this.controller.addTextSpan(this.message, { style: { fontColor: Color.Black, fontSize: 25 } });
        })
        .onSelect((value: RichEditorSelection) => {
          if (value.selection\[0\] == -1 && value.selection\[1\] == -1) {
            return;
          }
          this.start = value.selection\[0\];
          this.end = value.selection\[1\];
        })
        .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu3(), RichEditorResponseType.RIGHT\_CLICK)
        .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu2(), RichEditorResponseType.SELECT)
        .borderWidth(1)
        .borderColor(Color.Red)
        .width(200)
        .height(200)
        .margin(10)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ceWhsbcBTN6dmHU-Cyy0ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CBF08C6A3ED772D302B32315007AEFF120344CEB3ED740BAD6A30695B9149D9)

Icons in bold and italics are not preset in the system. The sample code uses the default icons. You need to replace the icons in **editorMenuOptions** with the desired icons.

## Example 2: Setting the Symbol Icon

This example demonstrates how to use **symbolStyle** in [EditorMenuOptions](#editormenuoptions) to set custom symbol icons. This functionality is supported since API version 11.

import {
  SelectionMenu,
  EditorMenuOptions,
  ExpandedMenuOptions,
  EditorEventInfo,
  SelectionMenuOptions,
  SymbolGlyphModifier
} from '@kit.ArkUI'

@Entry
@Component
struct Index {
  @State select: boolean = true;
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State message: string = 'Hello world';
  @State textSize: number = 30;
  @State fontWeight: FontWeight = FontWeight.Normal;
  @State start: number = -1;
  @State end: number = -1;
  @State visibleValue: Visibility = Visibility.Visible;
  @State colorTransparent: Color = Color.Transparent;
  @State textStyle: RichEditorTextStyle = {};
  private editorMenuOptions: Array<EditorMenuOptions> =
    \[
      {
        icon: $r("sys.media.wifi\_router\_fill"),
        symbolStyle: new SymbolGlyphModifier($r('sys.symbol.save')),
        action: () => {
          if (this.controller) {
            let selection = this.controller.getSelection();
            let spans = selection.spans;
            spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
              if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
                let span = item as RichEditorTextSpanResult;
                this.textStyle = span.textStyle;
                let start = span.offsetInSpan\[0\];
                let end = span.offsetInSpan\[1\];
                let offset = span.spanPosition.spanRange\[0\];
                if (this.textStyle.fontWeight != 11) {
                  this.textStyle.fontWeight = FontWeight.Bolder;
                } else {
                  this.textStyle.fontWeight = FontWeight.Normal;
                }
                this.controller.updateSpanStyle({
                  start: offset + start,
                  end: offset + end,
                  textStyle: this.textStyle
                })
              }
            })
          }
        }
      },
      {
        icon: $r("sys.media.save\_button\_picture"),
        symbolStyle: new SymbolGlyphModifier($r('sys.symbol.camera')),
        action: () => {
          if (this.controller) {
            let selection = this.controller.getSelection();
            let spans = selection.spans;
            spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
              if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
                let span = item as RichEditorTextSpanResult;
                this.textStyle = span.textStyle;
                let start = span.offsetInSpan\[0\];
                let end = span.offsetInSpan\[1\];
                let offset = span.spanPosition.spanRange\[0\];
                if (this.textStyle.fontStyle == FontStyle.Italic) {
                  this.textStyle.fontStyle = FontStyle.Normal;
                } else {
                  this.textStyle.fontStyle = FontStyle.Italic;
                }
                this.controller.updateSpanStyle({
                  start: offset + start,
                  end: offset + end,
                  textStyle: this.textStyle
                })
              }
            })
          }
        }
      },
      {
        icon: $r("sys.media.waveform\_folder\_fill"),
        symbolStyle: new SymbolGlyphModifier($r('sys.symbol.car')),
        action: () => {
          if (this.controller) {
            let selection = this.controller.getSelection();
            let spans = selection.spans;
            spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
              if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
                let span = item as RichEditorTextSpanResult;
                this.textStyle = span.textStyle;
                let start = span.offsetInSpan\[0\];
                let end = span.offsetInSpan\[1\];
                let offset = span.spanPosition.spanRange\[0\];
                if (this.textStyle.decoration) {
                  if (this.textStyle.decoration.type == TextDecorationType.Underline) {
                    this.textStyle.decoration.type = TextDecorationType.None;
                  } else {
                    this.textStyle.decoration.type = TextDecorationType.Underline;
                  }
                } else {
                  this.textStyle.decoration = { type: TextDecorationType.Underline, color: Color.Black }
                }
                this.controller.updateSpanStyle({
                  start: offset + start,
                  end: offset + end,
                  textStyle: this.textStyle
                })
              }
            })
          }
        }
      },
      {
        // Replace $r('app.media.app\_icon') with the image resource file you use.
        icon: $r("app.media.app\_icon"), action: () => {
      }, builder: (): void => this.sliderPanel()
      },
      {
        icon: $r("sys.media.thermometer\_fill"), action: () => {
        if (this.controller) {
          let selection = this.controller.getSelection();
          let spans = selection.spans;
          spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
            if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
              let span = item as RichEditorTextSpanResult;
              this.textStyle = span.textStyle;
              let start = span.offsetInSpan\[0\];
              let end = span.offsetInSpan\[1\];
              let offset = span.spanPosition.spanRange\[0\];
              if (this.textStyle.fontColor == Color.Orange || this.textStyle.fontColor == '#FFFFA500') {
                this.textStyle.fontColor = Color.Black;
              } else {
                this.textStyle.fontColor = Color.Orange;
              }
              this.controller.updateSpanStyle({
                start: offset + start,
                end: offset + end,
                textStyle: this.textStyle
              })
            }
          })
        }
      }
      }\]
  private expandedMenuOptions: Array<ExpandedMenuOptions> =
    \[{
      // Replace $r('app.media.startIcon') with the image resource file you use.
      startIcon: $r("app.media.startIcon"), content: 'Dictionary', action: () => {
      }
    }, {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      startIcon: $r("app.media.startIcon"), content: 'Translate', action: () => {
      }
    }, {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      startIcon: $r("app.media.startIcon"), content: 'Search', action: () => {
      }
    }\]
  private expandedMenuOptions1: Array<ExpandedMenuOptions> = \[\]
  private editorMenuOptions1: Array<EditorMenuOptions> = \[\]
  private selectionMenuOptions: SelectionMenuOptions = {
    editorMenuOptions: this.editorMenuOptions,
    expandedMenuOptions: this.expandedMenuOptions,
    controller: this.controller,
    onCut: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test cut' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    },
    onPaste: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test onPaste' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    },
    onCopy: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test cut' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    },
    onSelectAll: (event?: EditorEventInfo) => {
      if (event && event.content) {
        event.content.spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
          if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
            let span = item as RichEditorTextSpanResult;
            console.info('test onPaste' + span.value);
            console.info('test start ' + span.offsetInSpan\[0\] + ' end: ' + span.offsetInSpan\[1\]);
          }
        })
      }
    }
  }

  @Builder
  sliderPanel() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
        Text('A').fontSize(15)
        Slider({ value: this.textSize, step: 10, style: SliderStyle.InSet })
          .width(210)
          .onChange((value: number, mode: SliderChangeMode) => {
            if (this.controller) {
              let selection = this.controller.getSelection();
              if (mode == SliderChangeMode.End) {
                if (this.textSize == undefined) {
                  this.textSize = 0;
                }
                let spans = selection.spans;
                spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult, index) => {
                  if (typeof (item as RichEditorTextSpanResult)\['textStyle'\] != 'undefined') {
                    this.textSize = Math.max(this.textSize, (item as RichEditorTextSpanResult).textStyle.fontSize);
                  }
                })
              }
              if (mode == SliderChangeMode.Moving || mode == SliderChangeMode.Click) {
                this.start = selection.selection\[0\];
                this.end = selection.selection\[1\];
                this.textSize = value;
                this.controller.updateSpanStyle({
                  start: this.start,
                  end: this.end,
                  textStyle: { fontSize: this.textSize }
                })
              }
            }
          })
        Text('A').fontSize(20).fontWeight(FontWeight.Medium)
      }.borderRadius($r('sys.float.ohos\_id\_corner\_radius\_card'))
    }
    .shadow(ShadowStyle.OUTER\_DEFAULT\_MD)
    .backgroundColor(Color.White)
    .borderRadius($r('sys.float.ohos\_id\_corner\_radius\_card'))
    .padding(15)
    .height(48)
  }

  @Builder
  MyMenu() {
    Column() {
      SelectionMenu(this.selectionMenuOptions)
    }
    .width(256)
    .backgroundColor(Color.Transparent)
  }

  @Builder
  MyMenu2() {
    Column() {
      SelectionMenu({
        editorMenuOptions: this.editorMenuOptions,
        expandedMenuOptions: this.expandedMenuOptions1,
        controller: this.controller,
      })
    }
    .width(256)
    .backgroundColor(Color.Transparent)
  }

  @Builder
  MyMenu3() {
    Column() {
      SelectionMenu({
        editorMenuOptions: this.editorMenuOptions1,
        expandedMenuOptions: this.expandedMenuOptions,
        controller: this.controller,
      })
    }
    .width(256)
    .backgroundColor(Color.Transparent)
  }

  build() {
    Column() {
      Button("SetSelection")
        .onClick((event: ClickEvent) => {
          if (this.controller) {
            this.controller.setSelection(0, 2);
          }
        })

      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(this.message, { style: { fontColor: Color.Orange, fontSize: 30 } });
          this.controller.addTextSpan(this.message, { style: { fontColor: Color.Black, fontSize: 25 } });
        })
        .onSelect((value: RichEditorSelection) => {
          if (value.selection\[0\] == -1 && value.selection\[1\] == -1) {
            return;
          }
          this.start = value.selection\[0\];
          this.end = value.selection\[1\];
        })
        .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu3(), RichEditorResponseType.RIGHT\_CLICK)
        .bindSelectionMenu(RichEditorSpanType.TEXT, this.MyMenu2(), RichEditorResponseType.SELECT)
        .borderWidth(1)
        .borderColor(Color.Red)
        .width(200)
        .height(200)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/lT4yo0rTT9qAoIxF-QqL9A/en-us_image_0000002568765717.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=789C5AAF0948B9077FFC64F8C1480CF4AC88D5F30CA52709C29C7AE4F32A63D6)
