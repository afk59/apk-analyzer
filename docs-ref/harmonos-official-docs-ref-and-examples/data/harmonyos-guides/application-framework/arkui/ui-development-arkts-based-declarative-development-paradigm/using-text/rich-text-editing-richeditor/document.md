# Rich Text Editing (RichEditor)

**RichEditor** is a component that supports interactive text editing and mixture of text and images. It is typically used in scenarios where mixed-content user input is expected, such as comment sections that accept both image and text submissions. For details, see [RichEditor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor).

If you only need to display images and text, the [Text](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text) component is recommended.

If you need to display a large amount of HTML content, the [RichText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richtext) component is recommended.

#### Component Composition

The following figure illustrates the component's elements.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/sOsBrcqeSVG06lBreFWMaA/en-us_image_0000002537764650.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D84F5CD6B986396C2FF6F825D6F11EC87E7F1AF672742DB013EB25A9191D3F03)

The component's elements are described as follows.

| Element | Description |
| :-- | :-- |
| Content area | Area where content is displayed. |
| Cursor | Indicates the current insertion position. |
| Handles | Left and right handles that can be dragged separately to adjust the text selection range. |
| Menu | Appears after content is selected, containing operation buttons such as copy and paste. |

#### Creating a RichEditor Component

You can create a **RichEditor** component either from a styled string or from spans. For details, see [Creating a RichEditor Component from a Styled String](#creating-a-richeditor-component-from-a-styled-string) or [Creating a RichEditor Component from Spans](#creating-a-richeditor-component-from-spans).

## Creating a RichEditor Component from a Styled String

Use the RichEditor(options: [RichEditorStyledStringOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringoptions12)) API to create a **RichEditor** component that manages content through styled strings ([StyledString/MutableStyledString](../styled-string-styledstring-mutablestyledstring/document.md)). This approach allows you to manage data by holding styled string objects on the application side, modify the content and style of those objects, and then pass the updated objects to the component to refresh the rich text content.

Compared with using controller APIs for content style updates, this approach offers greater flexibility and convenience. In addition, styled string objects can be assigned to various text components that support styled strings, enabling quick content migration.

@Entry
@Component
export struct CreateRichEditor {
  // ...
  fontStyle: TextStyle = new TextStyle({
    fontColor: Color.Pink
  })
  // Define a text style object.
  mutableStyledString: MutableStyledString =
    // Replace $r('app.string.CreateRichEditor\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Create a RichEditor component using a styled string."
    new MutableStyledString(this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.CreateRichEditor\_Text\_1').id),
    \[{
      start: 0,
      length: 5,
      styledKey: StyledStringKey.FONT,
      styledValue: this.fontStyle
    }\])
  // Create a styled string.

  controller: RichEditorStyledStringController = new RichEditorStyledStringController();
  options: RichEditorStyledStringOptions = { controller: this.controller };
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        Column({ space: 3 }) {
          // ...
          RichEditor(this.options)
            .onReady(() => {
              this.controller.setStyledString(this.mutableStyledString);
            })
        }
        // ...
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    .backgroundColor('#f1f2f3')
    // Replace $r('app.string.Create\_RichEditor\_Component\_title') with the actual resource file. In this example, the value in the resource file is "Create a RichEditor component."
    .title($r('app.string.Create\_RichEditor\_Component\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/IiW6J9t5QHmogUDq1zu9UA/en-us_image_0000002537924590.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F95A404B30C2B80BAE57065D1B83F0842EFF1BB7AAE045A30CD85113F9363DEB)

## Creating a RichEditor Component from Spans

Use the RichEditor(value: [RichEditorOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#richeditoroptions)) API to create a **RichEditor** component that manages content via spans. This component is typically used in complex content scenarios. You can use the APIs provided by **RichEditorController** to manage content and styles.

@Entry
@Component
export struct CreateRichEditor {
  controllerNoStyledString: RichEditorController = new RichEditorController();
  optionsNoStyledString: RichEditorOptions = { controller: this.controllerNoStyledString };
  // ...
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
        Column({ space: 3 }) {
          // ...
          RichEditor(this.optionsNoStyledString)
            .onReady(() => {
              this.controllerNoStyledString.addTextSpan(
                /\*\*
                 \* Replace $r('app.string.CreateRichEditor\_Text\_2') with the actual resource file.
                 \* In this example, the value in the resource file is "Create a RichEditor component without using a styled string."
                 \*/
                $r('app.string.CreateRichEditor\_Text\_2'), {
                style: {
                  fontColor: Color.Black,
                  fontSize: 15
                }
              })
            })
        }
        // ...
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    .backgroundColor('#f1f2f3')
    // Replace $r('app.string.Create\_RichEditor\_Component\_title') with the actual resource file. In this example, the value in the resource file is "Create a RichEditor component."
    .title($r('app.string.Create\_RichEditor\_Component\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/FyTmbyMAQIes-0_aW5QxOQ/en-us_image_0000002568684367.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D2557D9D657DB0103AE3A4FAB52F4844F58E6A19B4CB3C69E74B9120EBFF1B7)

#### Adding Content

The **RichEditor** component supports adding content in different forms through various APIs.

## Adding a Text Span

In addition to directly entering content into the component, you can add a text span using the [addTextSpan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#addtextspan) API.

This API enables diverse text styling, such as creating mixed-style text.

If the component is focused and the cursor is blinking, adding text via **addTextSpan** updates the cursor position, and the cursor blinks to the right of the newly added text.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  // ...
    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.AddTextContent\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to add text here."
          this.controller.addTextSpan($r('app.string.AddTextContent\_Text\_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .border({ width: 1, color: Color.Gray })
        .constraintSize({
          maxHeight: 100
        })
        .width(300)
        .margin(10)
      Row() {
        // Replace $r('app.string.AddTextContent\_Button\_1') with the actual resource file. In this example, the value in the resource file is "addTextSpan."
        Button($r('app.string.AddTextContent\_Button\_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
        .height(30)
        .fontSize(13)
        .onClick(() => {
          // Replace $r('app.string.AddTextContent\_Text\_2') with the actual resource file. In this example, the value of the resource file is "Add text."
          this.controller.addTextSpan($r('app.string.AddTextContent\_Text\_2'))
        })
      }.justifyContent(FlexAlign.Center).width('100%')
    }
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/99n87Z16SlCD8VGGUclkjQ/en-us_image_0000002568764377.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3204603C372BAB757D30A97E2CEF5B1835C9C4EF623561A17FE14788A3157B1)

## Adding an Image Span

Use the [addImageSpan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#addimagespan) API to add an image span.

This API is useful in enriching and visualizing content. For example, you can use it to add images to news or data visualization graphics to documents.

If the component is focused and the cursor is blinking, adding image content via **addImageSpan** updates the cursor position, and the cursor blinks to the right of the newly added image.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };
build() {
  // ...
    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.AddImageContent\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to add an image here."
          this.controller.addTextSpan($r('app.string.AddImageContent\_Text\_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .width(300)
        .height(100)
      Row() {
        // Replace $r('app.string.AddImageContent\_Button\_1') with the actual resource file. In this example, the value in the resource file is "addImageSpan."
        Button($r('app.string.AddImageContent\_Button\_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            // Replace $r('app.media.xxx') with the actual resource file.
            this.controller.addImageSpan($r('app.media.startIcon'), {
              imageStyle: {
                size: \['57px', '57px'\]
              }
            })
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/ZBiXcMcXRHyEewFBwXgBkw/en-us_image_0000002537764652.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=397DF43BC01CD64A7A06F1291C6DDA5FC11BC4420CFD9A52DF44FD1991C0AC4F)

## Adding @Builder Decorated Content

Use [addBuilderSpan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#addbuilderspan11) to add the content decorated by the @Builder decorator.

This approach applies when you need to integrate custom complex components, such as custom charts.

With this API, you can specify the addition position using [RichEditorBuilderSpanOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#richeditorbuilderspanoptions11). If no position is specified or an invalid value is provided, the builder content is appended to the end.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };
private myBuilder: CustomBuilder = undefined;

@Builder
TextBuilder() {
  Row() {
    Image($r('app.media.startIcon')).width(50).height(50).margin(16)
    Column() {
      // Replace $r('app.string.AddBuilderDecoratorContent\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Text.txt."
      Text($r('app.string.AddBuilderDecoratorContent\_Text\_1')).fontWeight(FontWeight.Bold).fontSize(16)
      // Replace $r('app.string.AddBuilderDecoratorContent\_Text\_2') with the actual resource file. In this example, the value in the resource file is "123.45 KB."
      Text($r('app.string.AddBuilderDecoratorContent\_Text\_2')).fontColor('#8a8a8a').fontSize(12)
    }.alignItems(HorizontalAlign.Start)
  }.backgroundColor('#f4f4f4')
  .borderRadius('20')
  .width(220)
}
build() {
  // ...
    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(
            /\*\*
             \* Replace $r('app.string.AddBuilderDecoratorContent\_Text\_3') with the actual resource file.
             \* In this example, the value in the resource file is "Click the button to add builderspan here."
             \*/
            $r('app.string.AddBuilderDecoratorContent\_Text\_3'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
      Row() {
        /\*\*
         \* Replace $r('app.string.AddBuilderDecoratorContent\_Button\_1') with the actual resource file.
         \* In this example, the value in the resource file is "addBuilderSpan."
         \*/
        Button($r('app.string.AddBuilderDecoratorContent\_Button\_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            this.myBuilder = () => {
              this.TextBuilder()
            }
            this.controller.addBuilderSpan(this.myBuilder)
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/sRGgvpJxQ8GJLm36D2lBbg/en-us_image_0000002537924592.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A455DD6725A002749A3820C524EC3817C9C34EFF28FD35EE3AA24D110C1717A)

## Adding a Symbol Span

Use the [addSymbolSpan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#addsymbolspan11) API to add symbol content. This API enables addition of special characters, such as mathematical symbols in academic papers.

When a symbol is added while the component is focused and the cursor is blinking, the cursor moves to the right of the newly inserted symbol.

Currently, gestures, copying, and dragging are not supported for the symbol content.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  // ...
    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.AddSymbolSpanContent\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to add a symbol here."
          this.controller.addTextSpan($r('app.string.AddSymbolSpanContent\_Text\_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .width(300)
        .height(100)
      Row() {
        // Replace $r('app.string.AddSymbolSpanContent\_Button\_1') with the actual resource file. In this example, the value in the resource file is "addSymbolSpan."
        Button($r('app.string.AddSymbolSpanContent\_Button\_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            // Replace $r('sys.symbol.basketball\_fill') with the resource file you use.
            this.controller.addSymbolSpan($r('sys.symbol.basketball\_fill'), {
              style: {
                fontSize: 30
              }
            })
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/h_cOy4-xQza0FatiOYIxBg/en-us_image_0000002568684369.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB1020D185AA498568DE2DBA50E0258241370FBC5976F6AB73A499A581C9CE9C)

#### Managing Content

The **RichEditor** component provides APIs for content management, for example, [obtaining image and text information within the component](#obtaining-the-image-and-text-information), [setting placeholder text when no input is present](#setting-placeholder-text), or [limiting the maximum character](#setting-the-maximum-length).

## Obtaining the Image and Text Information

Use the [getSpans](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#getspans) API to obtain information about all images and text in the component, including content, ID, style, and position. After obtaining the position information, you can update the style of the content in the specified range.

This API is useful for obtaining and checking existing content styles, such as in template use cases, and for content parsing and processing, such as in text analysis applications.

@Entry
@Component
export struct GetGraphicInfoInComponent {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  infoShowController: RichEditorController = new RichEditorController();
  infoShowOptions: RichEditorOptions = { controller: this.infoShowController };
  // Create two RichEditor components.
  build() {
    // ...
      Column({ space: 3 }) {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan(
              // Replace $r('app.string.GetGraphicInfoInComponent\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to obtain the span information."
              $r('app.string.GetGraphicInfoInComponent\_Text\_1'), {
              style: {
                fontColor: Color.Black,
                fontSize: 15
              }
            })
          })
          .width(300)
          .height(50)
        // Replace $r('app.string.GetGraphicInfoInComponent\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to obtain the span information."
        Text($r('app.string.GetGraphicInfoInComponent\_Text\_1')).fontSize(10).fontColor(Color.Gray).width(300);
        RichEditor(this.infoShowOptions)
          .width(300)
          .height(50)
        Row() {
          // Replace $r('app.string.GetGraphicInfoInComponent\_Button\_1') with the actual resource file. In this example, the value in the resource file is "getSpans."
          Button($r('app.string.GetGraphicInfoInComponent\_Button\_1'), {
            buttonStyle: ButtonStyleMode.NORMAL
          })
            .height(30)
            .fontSize(13)
            .onClick(() => {
              this.infoShowController.addTextSpan(JSON.stringify(this.controller.getSpans()), {
                style: {
                  fontColor: Color.Gray,
                  fontSize: 10
                }
              })
            })
        }.justifyContent(FlexAlign.Center).width('100%')
      }
      // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/dVK_wnWkSpWEFLuLXQQBgA/en-us_image_0000002568764379.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B92C0A6B86D04138E754191EB3CFD9F95C6070EDD7D1557BF6DDF4041590E5E7)

## Setting Placeholder Text

You can set the placeholder text, which is displayed when there is no input, using the [placeholder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#placeholder12) API.

Placeholder text provides useful guidance, helping users navigate the application UI, especially in scenarios requiring specific input, such as login screens. For example, in a text editing box, placeholder text can specify input requirements, such as "Enter up to 100 characters."

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {
    // ...
    RichEditor(this.options)
      // Replace $r('app.string.SetAttributes\_Text\_6') with the actual resource file. In this example, the value of the resource file is "This is the prompt text...".
      .placeholder(resource.resourceToString($r('app.string.SetAttributes\_Text\_6')), {
        fontColor: Color.Gray,
        font: {
          size: 15,
          weight: FontWeight.Normal,
          family: 'HarmonyOS Sans',
          style: FontStyle.Normal
        }
      })
      .width(300)
      .height(50)
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/tfQu54hlTtWztp9fzkMNcQ/en-us_image_0000002537764654.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD02B78A39936A23ADF1FCEE921E7587FEC41F382CFEACDC669C9D3F3842BF74)

## Setting the Maximum Length

You can set the maximum number of characters allowed in the **RichEditor** component using [maxLength](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#maxlength18).

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {
    // ...
    RichEditor(this.options)
      // Replace $r('app.string.SetAttributes\_Text\_8') with the actual resource file. In this example, the value in the resource file is "Maximum number of characters: 7."
      .placeholder(resource.resourceToString($r('app.string.SetAttributes\_Text\_8')))
      .maxLength(7)
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/fCrqJaFdTQSfSj-1-5mLWw/en-us_image_0000002537924594.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8C2D7A050D162291C9EE1C0AD1EC2E43472D4F528498B80202EA4948BBF761D)

#### Adding Event Callbacks

You can register callbacks to listen for component events.

## Adding Callbacks for Before and After Text and Image Changes

Use the [onWillChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#onwillchange12) API to add a callback invoked before text or image changes. This callback is applicable to real-time data verification and notification. For example, it can be used to enable features such as detecting sensitive words and displaying an alert dialog box immediately, as well as real-time character count statistics and limitation.

Use the [onDidChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#ondidchange12) API to add a callback invoked after text or image changes. This callback applies to content saving and synchronization. For example, it can be used to automatically save the latest content to the local host or synchronizing it to the server. The callback can also be used to update and re-render content status. For example, in a to-do list application, after a user edits a task description in rich-text format, the callback can update the display style of that task in the list.

Note: The **RichEditor** component constructed with [RichEditorStyledStringOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringoptions12) does not support these two types of callbacks.

  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {
    // ...
    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.AddEvent\_Text\_5') with the actual resource file. In this example, the value in the resource file is "Trigger a callback before the graphic and text changes within the component.\\nAfter the graphic and text changes, trigger a callback."
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_5')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onWillChange((value: RichEditorChangeValue) => {
          //Replace $r('app.string.AddEvent\_Text\_6') with the actual resource file. In this example, the value in the resource file is "Before the graphic and text changes within the component, trigger a callback:".
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_6')) +
          JSON.stringify(value), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
          return true;
        })
        .onDidChange((rangeBefore: TextRange, rangeAfter: TextRange) => {
          //Replace $r('app.string.AddEvent\_Text\_7') with the actual resource file. In this example, the value in the resource file is "\\nAfter the graphic and text changes, trigger a callback:\\n rangeBefore."
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_7')) +
          JSON.stringify(rangeBefore) + '\\nrangeAfter: ' + JSON.stringify(rangeBefore), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50);
      // Replace $r('app.string.AddEvent\_Text\_4') with the actual resource file. In this example, the value in the resource file is "View callback content:".
      Text(resource.resourceToString($r('app.string.AddEvent\_Text\_4'))).fontSize(10).fontColor(Color.Gray).width(300);
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70);
    }
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zlbRRMCSQxez0HQSvh_b5A/en-us_image_0000002568684371.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=381254252064C8A03A86CC5B7996503B371805E7973AD0CE0213F6B7272EADA8)

## Adding Callbacks Triggered Before and After Content Input in the Input Method

Callbacks can be triggered before and after input method content is added.

To facilitate intelligent input assistance, use [aboutToIMEInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#abouttoimeinput) to trigger a callback before adding input content, and [onDidIMEInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#ondidimeinput12) to trigger a callback after the input is complete.

These two callbacks are useful for handling service logic during text display, for example, providing word suggestions or predictive text before display and performing auto-correction or format conversion after input completes. The callbacks are triggered in this order: **aboutToIMEInput** -> **onDidIMEInput**.

Components constructed with [RichEditorStyledStringOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringoptions12) do not support these two callbacks.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {
    // ...
    Column({ space: 3 }) {
      // Replace $r('app.string.xxx') with the resource file you use.
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_8')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .aboutToIMEInput((value: RichEditorInsertValue) => {
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_9')) +
          JSON.stringify(value), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
          return true;
        })
        .onDidIMEInput((value: TextRange) => {
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_10')) +
          JSON.stringify(value), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50)
      Text(resource.resourceToString($r('app.string.AddEvent\_Text\_4'))).fontSize(10).fontColor(Color.Gray).width(300)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)

    }
    // ...
  }
  .alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/HYK0CtRqTGaBXrltneFsXA/en-us_image_0000002568764381.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31DB536F0FDEE93F248F745C2FECFB678BC67FF665DF916D3A7A82D4294B0B4B)

## Adding a Callback Triggered Before Paste Completion

The [onPaste](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#onpaste11) callback is used to add custom processing before pasting completes.

This is useful for content format handling, such as converting HTML-tagged text to a format supported by the **RichEditor** component and removing unnecessary tags or retaining only plain text content.

You can use this API to override the default paste behavior, which is limited to plain text, so that both images and text can be pasted.

import { pasteboard } from '@kit.BasicServicesKit';
// ...
@Component
struct on\_cut\_copy\_paste {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  infoShowController: RichEditorController = new RichEditorController();
  infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

  PopDataFromPasteboard() {
    let selection = this.controller.getSelection();
    let start = selection.selection\[0\];
    let end = selection.selection\[1\];
    if (start == end) {
      start = this.controller.getCaretOffset();
      end = this.controller.getCaretOffset();
    }
    let moveOffset = 0;
    let sysBoard = pasteboard.getSystemPasteboard();
    sysBoard.getData((err, data) => {
      if (err) {
        return;
      }
      if (start != end) {
        this.controller.deleteSpans({ start: start, end: end });
      }
      let count = data.getRecordCount();
      for (let i = 0; i < count; i++) {
        const element = data.getRecord(i);
        if (element && element.plainText && element.mimeType === pasteboard.MIMETYPE\_TEXT\_PLAIN) {
          this.controller.addTextSpan(element.plainText,
            {
              style: { fontSize: 26, fontColor: Color.Red },
              offset: start + moveOffset
            }
          )
          moveOffset += element.plainText.length;
        }
      }
      this.controller.setCaretOffset(start + moveOffset);
    });
  }

  build() {
    Column() {
      // ...
      Column({ space: 3 }) {
        RichEditor(this.options)
          .onReady(() => {
            // Replace $r('app.string.AddEvent\_Text\_11') with the actual resource file. In this example, the value in the resource file is "Copying and pasting the text can trigger the callback."
            this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_11')),
              { style: { fontColor: Color.Black, fontSize: 15 } })
          })
          .onPaste((event) => {
            //Replace $r('app.string.AddEvent\_Text\_12') with the actual resource file. In this example, the value in the resource file is "Trigger the onPaste callback\\n."
            this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_12')),
              { style: { fontColor: Color.Gray, fontSize: 10 } })
            if (event != undefined && event.preventDefault) {
              event.preventDefault();
            }
            this.PopDataFromPasteboard()
          })
          .width(300)
          .height(50);
        // Replace $r('app.string.AddEvent\_Text\_4') with the actual resource file. In this example, the value in the resource file is "View callback content:".
        Text(resource.resourceToString($r('app.string.AddEvent\_Text\_4'))).fontSize(10).fontColor(Color.Gray).width(300);
        RichEditor(this.infoShowOptions)
          .width(300)
          .height(70);
      }.width('100%').alignItems(HorizontalAlign.Start);
      // ...
    }.alignItems(HorizontalAlign.Start)
    .backgroundColor('#fff')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

## Adding a Callback Triggered Before Cut Completion

The [onCut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#oncut12) callback is used to add custom processing before a cut operation completes.

This callback is useful for data processing and storage. For example, when a user cuts content from the **RichEditor** component, the callback can temporarily store the cut content to ensure it can be accurately restored during a subsequent paste.

You can use this API to override the default cut behavior, which is limited to plain text, so that both images and text can be cut.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {
    // ...
    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.AddEvent\_Text\_13') with the actual resource file. In this example, the value in the resource file is "Copying and pasting the text can trigger the callback."
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_13')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onCut(() => {
          // Replace $r('app.string.AddEvent\_Text\_14') with the actual resource file. In this example, the value in the resource file is "Trigger the onCut callback\\n."
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_14')), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(70)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)
    }
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

## Adding a Callback Triggered Before Copy Completion

Use the [onCopy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#oncopy12) callback to add processing logic before copying.

This callback applies to content backup and sharing. For example, the following operations can be performed in the callback: saving the copied content and its format information to a local backup folder, or automatically generating copywriting that includes the copied content and a product purchase link for users to paste and share.

The component's default copy behavior is limited to plain text and cannot handle images. You can use this callback to implement a custom copy feature that supports both images and text, replacing the component's default behavior.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {
    // ...
    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.AddEvent\_Text\_15') with the actual resource file. In this example, the value in the resource file is "Copying and pasting the text can trigger the callback."
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_15')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onCopy(() => {
          // Replace $r('app.string.AddEvent\_Text\_16') with the actual resource file. In this example, the value in the resource file is "Trigger the onCopy callback\\n."
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_16')), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)
    }
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/RVkQMcsLTDqu1XLqnfhOFg/en-us_image_0000002537764656.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D1D92ABD38EC305AB1C783E4593CBD07223912867F4768E794CDE72EE33D578)

For details about all available events, see [RichEditor Events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#events).

#### Implementing Component Interaction

You can configure interaction element attributes through APIs to respond to changes in those elements.

## Setting the Caret and Selection Handle Colors

You can set the caret and selection handle colors in the text box using the [caretColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#caretcolor12) API.

This feature allows for a more distinct visual representation of the caret and text selection, which can significantly aid users in navigating through complex UI that incorporate various input fields. It also improves user experience by allowing the caret color to match the overall style of the application page.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {
    // ...
    RichEditor(this.options)
      .onReady(() => {
        // Replace $r('app.string.SetAttributes\_Text\_5') with the actual resource file. In this example, the value in the resource file is "The component has set the caret handle color."
        this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes\_Text\_5')), {
          style: {
            fontColor: Color.Black,
            fontSize: 15
          }
        })
      })
      .caretColor(Color.Orange)
      .width(300)
      .height(300)
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/XQvbMv_SSb2qLStHe2idng/en-us_image_0000002537924596.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82360DD16B442F6ECA846036EB3E36A12467DD42F23D3F6EEA3B12CC92AC30B3)

## Adding a Callback for Caret Position and Selection Changes

The [onSelectionChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#onselectionchange12) callback is triggered whenever the caret position or text selection range changes in the component's content area during editing.

This callback enables real-time listening of selection changes. Typical use cases include: updating toolbar state dynamically (for example, reflecting the font and paragraph formatting of the currently selected text), measuring length of the selected content, and generating a summary of the selected content. By responding immediately to selection changes and dynamically linking interactive elements, this callback enhances the feedback experience and functional flexibility of rich text editing.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {
    // ...
    Column({ space: 3 }) {
      // Replace $r('app.string.xxx') with the actual resource file.
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent\_Text\_2')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onSelectionChange((value: RichEditorRange) => {
          this.infoShowController.addTextSpan('\\n' + resource.resourceToString($r('app.string.AddEvent\_Text\_3')) +
          value.start + ',' + value.end + ')', {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50)
      Text(resource.resourceToString($r('app.string.AddEvent\_Text\_4'))).fontSize(10).fontColor(Color.Gray).width(300)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/V4TZy-TkTm-gLINx0_38-w/en-us_image_0000002568684373.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AB3D4220C4026A5EEAEF106B7A6E461A733B4B7731A39FF99A48B0AA619C989)

## Setting the Text Selection Range

Use the [setSelection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#setselection11) API to configure the component to highlight the background of the selected portion.

This API is useful for implementing text focus effects. For example, when a user taps a paragraph title or summary, you can call this API to automatically select and highlight the corresponding text segment.

If this API is called when the text box is not focused, the selection effect is not displayed.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  // ...
    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {
          // Replace $r('app.string.BackplaneHighlighting\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to select the text at position 0 to 2 here."
          this.controller.addTextSpan($r('app.string.BackplaneHighlighting\_Text\_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .width(300)
        .height(60)
      Row() {
        // Replace $r('app.string.BackplaneHighlighting\_Button\_1') with the actual resource file. In this example, the value in the resource file is "setSelection(0,2)."
        Button($r('app.string.BackplaneHighlighting\_Button\_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            this.controller.setSelection(0, 2)
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Z4i6fmxHSuWVeuaxBL1xxw/en-us_image_0000002568764383.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBFACCD594BC8C33B59E3B2863990C639635C0F5F4F912841958A7D55B2008D7)

#### Configuring the Menu

You can configure the text selection menu through APIs.

## Managing Selected Menu Items

When the rich text selection range changes, the [onPrepareMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#properties-1) callback is triggered before the menu is displayed. You can configure menu data within this callback.

@Component
struct PrepareMenu {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State endIndex: number | undefined = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    const idsToFilter = \[
      TextMenuItemId.TRANSLATE,
      TextMenuItemId.SHARE,
      TextMenuItemId.SEARCH,
      TextMenuItemId.AI\_WRITER
    \]
    const items = menuItems.filter(item => !idsToFilter.some(id => id.equals(item.id)));
    // Replace $r('app.media.xxx') with the actual resource file.
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    }
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    }
    items.push(item1);
    items.unshift(item2);
    return items;
  }

  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
      return false;
    }
    return false;
  }

  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    // Replace $r('app.media.xxx') with the actual resource file.
    let item1: TextMenuItem = {
      content: 'prepare1\_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }

  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    Column() {
      // ...
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('RichEditor editMenuOptions');
        })
        .editMenuOptions(this.editMenuOptions)
        .onSelectionChange((range: RichEditorRange) => {
          this.endIndex = range.end;
        })
        .height(50)
        .margin({ top: 100 })
        .borderWidth(1)
        .borderColor(Color.Red)
      // ...
    }.alignItems(HorizontalAlign.Start)
    .backgroundColor('#fff')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/b3RF_-QWT6mungWl1y-EDw/en-us_image_0000002537764658.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72858E580498A1ABA6440EADA2331C7A21C923AA309AE8E0E27A26126B17CE58)

## Disabling System Service Menu Items

Use [disableSystemServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20) to hide all system-provided service menu items from the text selection menu.

This API protects content security and is suitable for scenarios with restricted text operations, for example, when displaying confidential content or copyrighted text that should not be copied. By disabling system menu items, you prevent users from copying or sharing text through the system menu, reducing content leakage risks.

import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
export struct DisableSystemServiceMenu {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  aboutToAppear(): void {
    // Disable all system service menus.
    TextMenuController.disableSystemServiceMenuItems(true);
  }

  aboutToDisappear(): void {
    // Restore system service menu items when the page disappears.
    TextMenuController.disableSystemServiceMenuItems(false);
  }

  build() {
    // ...
      Column({ space: 12 }) {
        RichEditor(this.options).onReady(() => {
          // Replace $r('app.string.Demo\_richEditor') with the actual resource file. In this example, the value in the resource file is "This is a RichEditor."
          this.controller.addTextSpan($r('app.string.Demo\_richEditor'),
            {
              style:
              {
                fontSize: 30
              }
            })
        })
          .height(60)
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems no longer contains disabled system menu items.
              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false;
            }
          })
      }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/-PcVgrbfRj-4tmhaL_DEwQ/en-us_image_0000002537924598.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1245EE1D45272CE305F791CE82B9DE26EB9C94761C717014404DB456C5B460FB)

Use [disableMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20) to hide specified system-provided service menu items from the text selection menu.

This API allows you to precisely disable only the system menu items you specify, while preserving other system menu functions needed by your application. This makes the menu better suited to your actual interaction design.

import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
export struct DisableMenuItem {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  aboutToAppear(): void {
    // Disable search and translate menu items.
    TextMenuController.disableMenuItems(\[TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE\]);
  }

  aboutToDisappear(): void {
    // Restore system service menu items.
    TextMenuController.disableMenuItems(\[\]);
  }

  build() {
    // ...
      Column({ space: 12 }) {
        RichEditor(this.options)
          .onReady(() => {
            // Replace $r('app.string.Demo\_richEditor') with the actual resource file. In this example, the value in the resource file is "This is a RichEditor."
            this.controller.addTextSpan($r('app.string.Demo\_richEditor'), {
              style: {
                fontSize: 30
              }
            })
          })
          .height(60)
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              // menuItems no longer contains search and translate items.
              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false;
            }
          })
      }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/_Xnnikj1Tsa7ojCA0_lBfA/en-us_image_0000002568684375.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C03609C6DD0C8556D9E92099C99A0CC7535100C9B2DC5DAF9F7DFDE30FDBFFA4)

## Setting the Custom Context Menu on Text Selection

You can set custom context menu on text selection using the [bindSelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#bindselectionmenu) API.

By default, the context menu on text selection includes copy, cut, and select-all options. You can add custom items to provide enhanced interactions, for example, a Translate option for multilingual support, or a Bold option to emphasize the selected text.

If the custom menu is too long, consider embedding a **Scroll** component to prevent the keyboard from being blocked.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };
sliderShow: boolean = false;
private theme: SelectionMenuTheme = defaultTheme;

build() {
  Column() {
    // ...
    RichEditor(this.options)
      .onReady(() => {
        // Replace $r('app.string.SetAttributes\_Text\_4') with the actual resource file. In this example, the value in the resource file is "The component has a custom menu that can be triggered by long pressing."
        this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes\_Text\_4')), {
          style: {
            fontColor: Color.Black,
            fontSize: 18
          }
        })
      })
      .bindSelectionMenu(RichEditorSpanType.TEXT, this.SystemMenu, ResponseType.LongPress, {
        onDisappear: () => {
          this.sliderShow = false
        }
      })
      // Bind a custom menu.
      .width(300)
      .height(300)
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

@Builder
SystemMenu() {
  Column() {
    Menu() {
      if (this.controller) {
        MenuItemGroup() {
          MenuItem({
            startIcon: this.theme.cutIcon,
            // Replace $r('app.string.SetAttributes\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Cut."
            content: resource.resourceToString($r('app.string.SetAttributes\_Text\_1')),
            labelInfo: 'Ctrl+X'
          })
          MenuItem({
            startIcon: this.theme.copyIcon,
            // Replace $r('app.string.SetAttributes\_Text\_2') with the actual resource file. In this example, the value in the resource file is "Copy."
            content: resource.resourceToString($r('app.string.SetAttributes\_Text\_2')),
            labelInfo: 'Ctrl+C'
          })
          MenuItem({
            startIcon: this.theme.pasteIcon,
            // Replace $r('app.string.SetAttributes\_Text\_3') with the actual resource file. In this example, the value in the resource file is "Paste."
            content: resource.resourceToString($r('app.string.SetAttributes\_Text\_3')),
            labelInfo: 'Ctrl+V'
          })
        }
      }
    }
    .radius(this.theme.containerBorderRadius)
    .clip(true)
    .backgroundColor(Color.White)
    .width(this.theme.defaultMenuWidth)
  }
  .width(this.theme.defaultMenuWidth)
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/5FVpOpDmQ8qWwUkSd2Z_FA/en-us_image_0000002568764385.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E6DF210C4474D8E578593DD4114390A126CC8319CBDBB561577B08D61AF22B8)

#### Configuring Layout

You can configure layout rules for the component through APIs, customizing its behavior based on your application's requirements.

## Setting the Maximum Number of Lines

Use [maxLines](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#maxlines18) to set the maximum number of lines that can be displayed in the **RichEditor** component.

This API controls the text display area to prevent overly long content from disrupting the page layout. It ensures a consistent text presentation across different devices and scenarios, improving UI compatibility and visual appeal.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {
    // ...
    /\*\*
     \* Replace $r('app.string.SetAttributes\_Text\_7') with the actual resource file.
     \*In this example, the value of the resource file is "The maximum number of lines is set.\\nExcess content will be displayed in scrolling mode.\\nExceeds 1 line\\nExceeds 2 lines\\nExceeds 3 lines\\nExceeds 4 lines."
     \*/
    RichEditor(this.options)
      .onReady(() => {
        this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes\_Text\_7')),
          {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
      })
      .maxLines(2)
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/SBaxznhTTfyzQRyFluXvUw/en-us_image_0000002537764660.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAE9D8503A6DA359654F0434CBB268DAB414AF28D22A40FC0F17906AAC27AF2D)

#### Setting the Style

You can apply complex styles to content in the component.

## Setting the Active Typing Style

Use the [setTypingStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#settypingstyle11) API to define the style that will be automatically applied to newly typed text.

This allows you to deliver a personalized writing experience. For example, you might want to use this API to automatically apply corresponding formats to different levels of headings (such as level-1 and level-2 headings) as users type.

@Entry
@Component
export struct SetUserPresetTextStyles {

  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    // ...
      Column({ space: 12 }) {
        RichEditor(this.options)
          .onReady(() => {
            // Replace $r('app.string.SetUserPresetTextStyles\_Text\_1') with the actual resource file. In this example, the value in the resource file is "Click the button to change the preset typing style."
            this.controller.addTextSpan($r('app.string.SetUserPresetTextStyles\_Text\_1'),
              {
                style: {
                  fontColor: Color.Black,
                  fontSize: 15
                }
              })
          })
          .width(300)
          .height(60)
        Row() {
          // Replace $r('app.string.SetUserPresetTextStyles\_Button\_1') with the actual resource file. In this example, the value in the resource file is "setTypingStyle."
          Button($r('app.string.SetUserPresetTextStyles\_Button\_1'), {
            buttonStyle: ButtonStyleMode.NORMAL
          })
            .height(30)
            .fontSize(13)
            .onClick(() => {
              this.controller.setTypingStyle({
                fontWeight: 'medium',
                fontColor: Color.Pink,
                fontSize: 15,
                fontStyle: FontStyle.Italic,
                decoration: {
                  type: TextDecorationType.Underline,
                  color: Color.Gray
                }
              })
            })
        }.justifyContent(FlexAlign.Center).width('100%')
      }
      // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/_fMOir2VTrSAzNXp2JrLpw/en-us_image_0000002537924600.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDFFF1A70CDADFF248995E4F1DA5C6822FBFDF1D881FCAD05AD57892D6283EB8)

## Setting Text Decoration

Use [decoration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-span#decoration) to set the style, color, and thickness of text decoration lines.

Applying text decoration can highlight key information, indicate text status, and improve visual hierarchy. For example, you can add a decoration line to important titles or keywords to help users quickly locate essential content.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {
    // ...
    RichEditor(this.options)
      .onReady(() => {
        // Replace $r('app.string.Demo\_oneText') with the actual resource file. In this example, the value in the resource file is "A piece of preset text."
        this.controller.addTextSpan($r('app.string.Demo\_oneText'), {
          style: {
            fontSize: 25,
            decoration: {
              type: TextDecorationType.LineThrough,
              color: Color.Blue,
              // Set the thickness of the decoration line to 6 times the default.
              thicknessScale: 6
            }
          }
        })
      })
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/bblNGEJjRhm3a6FeTe_FZQ/en-us_image_0000002568684377.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18BDEDD89A0B669D84334D8372B5A2B899CA58FA2FA225E202D5FA9FE9CA1D2E)

Use the **enableMultiType** attribute in [DecorationOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-styled-string#decorationoptions20) to apply multiple decoration lines simultaneously, such as an underline and a strikethrough.

This API is useful in complex scenarios that require diverse text decoration. For example, in collaborative document editing, different combinations of decoration lines can be used to distinguish text states contributed by various users, improving collaboration efficiency.

RichEditor({ controller: this.styledStringController });
// Replace $r('app.string.Demo\_SetStyledStringButton') with the actual resource file. In this example, the value in the resource file is "Multiple decoration lines."
Button($r('app.string.Demo\_SetStyledStringButton'))
  .fontSize(20)
  .onClick(() => {
    let mutString: MutableStyledString = new MutableStyledString(
      // Replace $r('app.string.Demo\_styledString') with the actual resource file. In this example, the value in the resource file is "Rich text with multiple decoration lines."
      resource.resourceToString($r('app.string.Demo\_styledString')), \[
      {
        start: 0,
        length: 9,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontSize: LengthMetrics.vp(25) })
      },
      {
        start: 0,
        length: 5,
        styledKey: StyledStringKey.DECORATION,
        styledValue: new DecorationStyle(
          {
            type: TextDecorationType.Underline,
          },
          {
            // Enable multiple decoration lines.
            enableMultiType: true
          })
      },
      {
        start: 2,
        length: 4,
        styledKey: StyledStringKey.DECORATION,
        styledValue: new DecorationStyle(
          {
            type: TextDecorationType.LineThrough,
          },
          {
            // Enable multiple decoration lines.
            enableMultiType: true
          })
      }
    \])
    this.styledStringController.setStyledString(mutString);
  })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/B7H1WUd7R0mIu-W_LUl4sQ/en-us_image_0000002568764387.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF02FA0B66D95EB8A130AE8B35A2B02FCD9F26BB64034EDE0EC8046AB6E0550E)

## Setting Vertical Alignment

Use [textVerticalAlign](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textverticalalign20) to set the vertical alignment of text within a paragraph.

This API optimizes layouts containing multiple elements. When component content needs to be aligned vertically with images or icons, it ensures a more harmonious overall layout.

controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {
    // ...
    RichEditor(this.options)
      .onReady(() => {
        // Replace $r('app.media.startIcon') with the actual resource file.
        this.controller.addImageSpan($r('app.media.startIcon'), {
          imageStyle: {
            size: \[100, 100\]
          }
        })
        // Replace $r('app.string.Demo\_verticalAlignString') with the actual resource file. In this example, the value in the resource file is "This is a rich text with the vertical alignment effect."
        this.controller.addTextSpan($r('app.string.Demo\_verticalAlignString'), {
          style: {
            fontColor: Color.Pink,
            fontSize: '32'
          },
          paragraphStyle: {
            textAlign: TextAlign.Start,
            textVerticalAlign: TextVerticalAlign.CENTER,
            leadingMargin: 16
          }
        })
      })
    // ...
  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/gqs4x-cfRsiXPTpYNojrZA/en-us_image_0000002537764662.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C37F30CDD4A926E230AE5FFEE9396DB2EAC55F9119DDE86C76ADA8947D709D2)

## Enabling Automatic Spacing Between Chinese and Western Characters

Use [enableAutoSpacing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor#enableautospacing20) to control whether automatic spacing is inserted between Chinese and western characters.

This API optimizes text layout and improves readability within the component. When automatic spacing is enabled, an appropriate gap is automatically added between Chinese and western characters, making it easier to distinguish between languages and reducing visual interference.

@Component
struct EnableAutoSpacing {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State
  enableAutoSpace:boolean = false;

  build() {
    Column() {
      // ...
      Column({ space: 3 }) {
        RichEditor(this.options)
          .onReady(() => {
            // Replace $r('app.string.Demo\_autoSpacingString') with the actual resource file. In this example, the value in the resource file is "Automatic spacing between Chinese and western characters."
            this.controller.addTextSpan($r('app.string.Demo\_autoSpacingString'),
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 20
                }
              })
          })
          .enableAutoSpacing(this.enableAutoSpace)
        // Replace $r('app.string.Demo\_autoSpacingButton') with the actual resource file. In this example, the value in the resource file is "Enable."
        Button($r('app.string.Demo\_autoSpacingButton'))
          .fontSize(20)
          .onClick(() => {
            this.enableAutoSpace = true;
          })
      }
      // ...
    }.alignItems(HorizontalAlign.Start)
    .backgroundColor('#fff')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/r3NP5EwTRbOskaXXHxMvuw/en-us_image_0000002537924602.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2C9C933C2AF83D75A8C01C5F1AD05ADEFB386A4A5576E60900F0419D9762CA8)
