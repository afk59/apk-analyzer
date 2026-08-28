# Text Display (Text/Span)

The **Text** component is used to display textual content. It can be bound to a custom text selection menu, allowing users to select features as needed. Additionally, you can extend this custom menu to add more options, further enhancing user experience. The **Span** component is used to display inline text.

For details, see [Text](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text) and [Span](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-span).

For details, see [FAQs About Text Display (Text/Span)](../../../ui-debugging-and-optimization/ui-development-faqs/faqs-about-text-components/document.md#faqs-about-text-display-textspan).

#### Creating Text

You can create text in either of the following ways:

-   Entering strings
    
    Text('I am a piece of text')
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SZsR5PfYRdCG_FizQiCCvQ/en-us_image_0000002537764622.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B5652ADCF5917B964471BFB743708F2E4FAB7EF4A8F0B42F8E0BD9A412ABE3E)

-   Referencing Resource objects
    
    Resource reference types can be created using $r. The resource file is located at **/resources/base/element/string.json** with the following content:
    
    {
      "string": \[
        {
          "name": "module\_desc",
          "value": "Module description"
        }
      \]
    }
    
    // Replace $r('app.string.module\_desc') with the actual resource file. In this example, the value in the resource file is "Module description."
    Text($r('app.string.module\_desc'))
      .baselineOffset(0)
      .fontSize(30)
      .border({ width: 1 })
      .padding(10)
      .width(300)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/68HLIJWPT_GTntFY02VLfQ/en-us_image_0000002537924562.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C40768052283D9249E909AD9F9053F09043E2FBFE4CDC5311270EBF95D4E5C19)
    

#### Adding Child Components

The [Span](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-span) component can only act as a child of the [Text](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text) and [RichEditor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor) components. You can add one or more **Span** child components to a **Text** component to display a piece of information, such as the product description and statement of commitment.

-   Creating a **Span** component
    
    A **Span** component is only visible when embedded within a **Text** component. Using a **Span** independently displays no content. If both **Text** and **Span** content are configured, the **Span** content overrides the **Text** content.
    
    // Replace $r('app.string.TextSpan\_textContent\_text') with the actual resource file. In this example, the value in the resource file is "I am Text."
    Text($r('app.string.TextSpan\_textContent\_text')) {
      // Replace $r('app.string.TextSpan\_textContent\_span') with the actual resource file. In this example, the value in the resource file is "I am Span."
      Span($r('app.string.TextSpan\_textContent\_span'))
    }
    .padding(10)
    .borderWidth(1)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/gofG5G5ITm-mpHihxadywA/en-us_image_0000002568684339.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64D7A639236C0F52F204DE58C58AD248C19AD457705DB52F7DCD1D63CEBB53A2)
    
-   Setting the text decoration
    
    Use the [decoration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-span#decoration) attribute to set the style and color of the text decorative line.
    
    Text() {
      // Replace $r('app.string.TextSpan\_textContent\_span\_one') with the actual resource file. In this example, the value in the resource file is "I am Span1."
      Span($r('app.string.TextSpan\_textContent\_span\_one'))
        .fontSize(16)
        .fontColor(Color.Grey)
        .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
      // Replace $r('app.string.TextSpan\_textContent\_span\_two') with the actual resource file. In this example, the value in the resource file is "I am Span2."
      Span($r('app.string.TextSpan\_textContent\_span\_two'))
        .fontColor(Color.Blue)
        .fontSize(16)
        .fontStyle(FontStyle.Italic)
        .decoration({ type: TextDecorationType.Underline, color: Color.Black })
      // Replace $r('app.string.TextSpan\_textContent\_span\_three') with the actual resource file. In this example, the value in the resource file is "I am Span3."
      Span($r('app.string.TextSpan\_textContent\_span\_three'))
        .fontSize(16)
        .fontColor(Color.Grey)
        .decoration({ type: TextDecorationType.Overline, color: Color.Green })
    }
    .borderWidth(1)
    .padding(10)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/eenH-GAjTr-cIqtXLwtOlA/en-us_image_0000002568764349.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D33BF60664125EC23D940FA4D736A3789D31B9616E6C1111DFEEC9DDDE37B5A)
    
-   Use the [textCase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-span#textcase) attribute to set the text case.
    
    Text() {
      Span('I am Upper-span').fontSize(12)
        .textCase(TextCase.UpperCase)
    }
    .borderWidth(1)
    .padding(10)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DlChX2NBRBqwoml4doBC2A/en-us_image_0000002537764624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83651A76A6EBD429D0E514EFD5640C9222FACC9BB8B8A9508A85306A68603F73)
    
-   Adding events
    
    Because **Span** components do not have independent size information, they only support the [onClick](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-click#onclick) and [onHover](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-hover#onhover) events.
    
    // xxx.ets
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    @Entry
    @Component
    export struct TextSpanOnHover {
      @State textStr1: string = '';
      @State textStr2: string = '';
    
      build() {
        NavDestination() {
          Row() {
            Column() {
              Text() {
                Span('I am Upper-span')
                  .textCase(TextCase.UpperCase)
                  .fontSize(30)
                  .onClick(() => {
                    hilog.info(0x0000, 'Sample\_TextComponent', 'Span onClick is triggering');
                    this.textStr1 = 'Span onClick is triggering';
                  })
                  .onHover(() => {
                    hilog.info(0x0000, 'Sample\_TextComponent', 'Span onHover is triggering');
                    this.textStr2 = 'Span onHover is triggering';
                  })
              }
    
              Text('onClick: ' + this.textStr1)
                .fontSize(20)
              Text('onHover: ' + this.textStr2)
                .fontSize(20)
            }.width('100%')
          }
          .height('100%')
        }
        // ···
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/xoVE4HuXQdC-D0y1KjHVAg/en-us_image_0000002537924564.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69263F9D16BF0839EC595B10B682FBBF7400842FE35BEF7EDE665E6F103F9251)
    

#### Creating a Custom Text Style

The **Text** component supports custom text style configuration. The following table lists the key attributes for text styling.

| Name | Description |
| :-- | :-- |
| baselineOffset | Offset of the text baseline. |
| contentTransition | Digital flip animation effect. |
| copyOption | Whether text can be copied and pasted. |
| decoration | Text decoration, such as the line style, color, and thickness. |
| enableAutoSpacing | Whether to enable automatic spacing between Chinese and Western characters. |
| enableDataDetector | Whether to enable recognition for special entities within the text. |
| font | Font-related attributes. |
| fontColor | Text color. |
| fontFamily | Font family. |
| fontFeature | Typographic features, such as numeric width adjustment. |
| fontSize | Font size. |
| fontStyle | Font style. |
| fontWeight | Font weight. |
| halfLeading | Whether half leading is enabled. |
| heightAdaptivePolicy | Font size adjustment strategy for adaptive text layout. |
| letterSpacing | Letter spacing. |
| lineHeight | Line height. |
| lineSpacing | Spacing between lines. |
| marqueeOptions | Marquee behavior, including the enabled status, step, loop count, and direction. |
| maxFontSize | Maximum font size for adaptive scaling. |
| maxLines | Maximum number of visible lines. |
| minFontSize | Minimum font size for adaptive scaling. |
| optimizeTrailingSpace | Whether to optimize trailing spaces at line endings. |
| privacySensitive | Whether to enable privacy mode on widgets. |
| shaderStyle | Gradient color effect. |
| textCase | Text case conversion. |
| textAlign | Horizontal alignment mode of text paragraphs. |
| textIndent | Indent of the first line of text. |
| textOverflow | Handling of overflow text. |
| textSelectable | Whether text can be selected. |
| textVerticalAlign | Vertical alignment mode of text paragraphs. |
| wordBreak | Word breaking rule. |

The following examples demonstrate usage of common APIs.

-   Use the [textAlign](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textalign) attribute to set the alignment mode of text.
    
    // Replace $r('app.string.TextAlign\_Start') with the actual resource file. In this example, the value in the resource file is "Left-aligned."
    Text($r('app.string.TextAlign\_Start'))
      .width(300)
      .textAlign(TextAlign.Start)
      .border({ width: 1 })
      .padding(10)
    // Replace $r('app.string.TextAlign\_Center') with the actual resource file. In this example, the value in the resource file is "Center-aligned."
    Text($r('app.string.TextAlign\_Center'))
      .width(300)
      .textAlign(TextAlign.Center)
      .border({ width: 1 })
      .padding(10)
    // Replace $r('app.string.TextAlign\_End') with the actual resource file. In this example, the value in the resource file is "Right-aligned."
    Text($r('app.string.TextAlign\_End'))
      .width(300)
      .textAlign(TextAlign.End)
      .border({ width: 1 })
      .padding(10)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/vUUcrdpbS6WaXYCEcDxbLA/en-us_image_0000002568684341.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=793D1AD3CDBAC799080C6814ACF39D3450C4B214D5ADFA4E4983E24CAC1F64F4)
    
-   Use the [textOverflow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textoverflow) attribute to set the display mode for when the text is too long. This attribute must be used together with [maxLines](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#maxlines). By default, the text is automatically wrapped. Since API version 18, when text overflow is set to marquee mode, you can configure marquee parameters such as enabled status, scroll step, loop count, and direction.
    
    Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +
      'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +
      'of textOverflow to None text content.')
      .width(250)
      .textOverflow({ overflow: TextOverflow.None })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
    // The value in the 'app.string.CustomTextStyle\_textContent\_epsis' resource file is
    // 'I am extra long text, with an ellipse displayed for any excess.'
    Text($r('app.string.CustomTextStyle\_textContent\_epsis'))
      .width(250)
      .textOverflow({ overflow: TextOverflow.Ellipsis })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
    // The value in the 'app.string.CustomTextStyle\_textContent\_marq' resource file is
    // 'When the text overflows its size,
    // the text is displayed in scrolling mode.'
    Text($r('app.string.CustomTextStyle\_textContent\_marq'))
      .width(250)
      .textOverflow({ overflow: TextOverflow.MARQUEE })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
    // The value in the 'app.string.CustomTextStyle\_textContent\_marq\_def' resource file is
    // 'When text exceeds its container dimensions, it scrolls to display fully.
    // Custom marquee parameters can be configured.'
    Text($r('app.string.CustomTextStyle\_textContent\_marq\_def'))
      .width(250)
      .textOverflow({ overflow: TextOverflow.MARQUEE })
      .maxLines(1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .marqueeOptions({
        start: true,
        fromStart: true,
        step: 6,
        loop: -1,
        delay: 0,
        fadeout: false,
        marqueeStartPolicy: MarqueeStartPolicy.DEFAULT
      })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/jIoO_u4gQ7yW5g6ir-Y5Zw/en-us_image_0000002568764351.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83AE8E275267C65AB22F35B42C84B778D82671E55B9F836D8921A798554D03AD)
    
-   Use the [lineHeight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#lineheight) attribute to set the text line height.
    
    Text('This is the text with the line height set. This is the text with the line height set.')
      .width(300).fontSize(12).border({ width: 1 }).padding(10)
    Text('This is the text with the line height set. This is the text with the line height set.')
      .width(300)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .lineHeight(20)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/gxx7Pd2NTICfUJm9_DL6ug/en-us_image_0000002537764626.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B400D2889EF8E0B57F42900776CB106F4115AC2693BBC471C732E999A93B4E4B)
    
-   Use the [decoration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#decoration) attribute to set the style, color, and thickness of the text decoration line.
    
    Text('This is the text')
      .decoration({
        type: TextDecorationType.LineThrough,
        color: Color.Red
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Overline,
        color: Color.Red
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Red
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.DASHED
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.DOTTED
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.DOUBLE
      })
      .borderWidth(1).padding(15).margin(5)
    Text('This is the text')
      .decoration({
        type: TextDecorationType.Underline,
        color: Color.Blue,
        style: TextDecorationStyle.WAVY,
        thicknessScale: 4
      })
      .borderWidth(1).padding(15).margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/dyg9_LAzRnmPtsCuJs8I1w/en-us_image_0000002537924566.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54B586863D7DC7DB0EEB3BC2C102923861A5AC6D6175B86F22EDD5EE37725648)
    
-   Use the [baselineOffset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#baselineoffset) attribute to set the baseline offset of the text.
    
    Text('This is the text content with baselineOffset 0.')
      .baselineOffset(0)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with baselineOffset 30.')
      .baselineOffset(30)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with baselineOffset -20.')
      .baselineOffset(-20)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/bD-rBb9oSaycOpvQbuqxWA/en-us_image_0000002568684343.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AB297336F4723D3DFFDB71502AD85C6C4B461A57215041635913FD32DBED8CC)
    
-   Use the [letterSpacing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#letterspacing) attribute to set the letter spacing.
    
    Text('This is the text content with letterSpacing 0.')
      .letterSpacing(0)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with letterSpacing 3.')
      .letterSpacing(3)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    Text('This is the text content with letterSpacing -1.')
      .letterSpacing(-1)
      .fontSize(12)
      .border({ width: 1 })
      .padding(10)
      .width('100%')
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/lEVox7VxTGmuGHwZQXxHXA/en-us_image_0000002568764353.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27334668D0459E84BB63C4A21D2EE68424579A432695CB5C67DACB7287B59757)
    
-   Use the [minFontSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#minfontsize) and [maxFontSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#maxfontsize) attributes
    
    to set the minimum and maximum font size, respectively. For the settings to take effect, these attributes must be used together with [maxLines](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#maxlines) or layout constraint settings.
    
    /\* Replace $r('app.string.CustomTextStyle\_textContent\_one\_style') with the actual resource file.
     In this example, the value in the resource file is "My maximum font size is 30, minimum font size is 5, width is 250, and maximum number of lines is 1." \*/
    Text($r('app.string.CustomTextStyle\_textContent\_one\_style'))
      .width(250)
      .maxLines(1)
      .maxFontSize(30)
      .minFontSize(5)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    /\* Replace $r('app.string.CustomTextStyle\_textContent\_two\_style') with the actual resource file.
     In this example, the value in the resource file is "My maximum font size is 30, minimum font size is 5, width is 250, and maximum number of lines is 2." \*/
    Text($r('app.string.CustomTextStyle\_textContent\_two\_style'))
      .width(250)
      .maxLines(2)
      .maxFontSize(30)
      .minFontSize(5)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    /\* Replace $r('app.string.CustomTextStyle\_textContent\_no\_max') with the actual resource file.
      In this example, the value in the resource file is "My maximum font size is 30, minimum font size is 15, width is 250, and line height is 50." \*/
    Text($r('app.string.CustomTextStyle\_textContent\_no\_max'))
      .width(250)
      .height(50)
      .maxFontSize(30)
      .minFontSize(15)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    /\* Replace $r('app.string.CustomTextStyle\_textContent\_high') with the actual resource file.
      In this example, the value in the resource file is "My maximum font size is 30, minimum font size is 15, width is 250, and line height is 100." \*/
    Text($r('app.string.CustomTextStyle\_textContent\_high'))
      .width(250)
      .height(100)
      .maxFontSize(30)
      .minFontSize(15)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/aD8EGk8WS0imN3F9Gsfrpw/en-us_image_0000002537764628.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70563543F822E93E97C2C04319552E61B3E89B52EA58121CEF33A62556091798)
    
-   Use the [textCase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textcase) attribute to set the text case.
    
    Text('This is the text content with textCase set to Normal.')
      .textCase(TextCase.Normal)
      .padding(10)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    // The text is displayed in lowercase.
    Text('This is the text content with textCase set to LowerCase.')
      .textCase(TextCase.LowerCase)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    // The text is displayed in uppercase.
    Text('This is the text content with textCase set to UpperCase.')
      .textCase(TextCase.UpperCase)
      .border({ width: 1 })
      .padding(10)
      .margin(5)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Z-PUw2Y7SPGY7a2rl4SofQ/en-us_image_0000002537924568.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0954EB928784B2E0982F0A710303D1F6188DF2F811DC35FFF73781A623311695)
    
-   Use the [copyOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#copyoption9) attribute to set whether copy and paste is allowed.
    
    // Replace $r('app.string.CustomTextStyle\_textContent\_incopy') with the actual resource file. In this example, the value in the resource file is "This text can be copied."
    Text($r('app.string.CustomTextStyle\_textContent\_incopy'))
      .fontSize(30)
      .copyOption(CopyOptions.InApp)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/FDRFRcgdRsOLSis24Bsanw/en-us_image_0000002568684345.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC2E6EB9906CCE074CF8757F1D841DF09CC75D63DB7A8F02109973ECAB256BB3)
    
-   Use the [fontFamily](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#fontfamily) attribute to specify font families. The 'HarmonyOS Sans' font and [registered custom fonts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-font) are supported for applications.
    
    Text('This is the text content with fontFamily')
      .fontSize(30)
      .fontFamily('HarmonyOS Sans')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/bXaZ0sEhRKedcUbmU99boQ/en-us_image_0000002568764355.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DA0B4E8A8D06EC828F60884F6B99B2B0F9B0FF6BD01595FCE9F2569311F83F7)
    
-   Since API version 20, you can use the [contentTransition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#contenttransition20) attribute to configure digital flip animation effects.
    
    @Entry
    @Component
    export struct ContentTransition {
      private static readonly INITIAL\_SCORE: number = 98;
      @State number: number = ContentTransition.INITIAL\_SCORE;
      @State numberTransition: NumericTextTransition =
        new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });
      build() {
        NavDestination() {
          Column() {
            Text(this.number + '')
              .borderWidth(1)
              .fontSize(40)
              .contentTransition(this.numberTransition)
            Button('chang number')
              .onClick(() => {
                this.number++
              })
              .margin(10)
          }
          .width('100%')
          .height('100%')
        }
        // ···
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/aOka8Ud_SDyfdCFx2oRv_w/en-us_image_0000002537764630.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF9D07F03B386173D7509C08F531CFAE4DB0398EB6CF5E04192A1A84D9F6118C)
    
-   Since API version 20, you can use [optimizeTrailingSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#optimizetrailingspace20) to control whether trailing spaces at the end of each line are optimized during text layout. This addresses alignment issues caused by trailing spaces.
    
    Column() {
      // Trailing spaces at the end of each line are optimized.
      Text('Trimmed space enabled     ')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 20 })
        .optimizeTrailingSpace(true)
        .textAlign(TextAlign.Center)
      // Trailing spaces at the end of each line are not optimized.
      Text('Trimmed space disabled     ')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 20 })
        .optimizeTrailingSpace(false)
        .textAlign(TextAlign.Center)
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/ellO9DVbRkC19T7ONKyYmw/en-us_image_0000002537924570.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=974D53E9125975B52DD9F76A056FE262DC53033101C43668F151D56118338F08)
    
-   Since API version 20, you can use [lineSpacing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#linespacing20) to configure text line spacing. If [LineSpacingOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#linespacingoptions20) is not specified, line spacing is applied above the first line and below the last line by default. When **onlyBetweenLines** is set to **true**, line spacing is applied only between lines, with no extra spacing above the first line.
    
    import { LengthMetrics } from '@kit.ArkUI';
    
    @Extend(Text)
    function style() {
      .width(250)
      .height(100)
      .maxFontSize(30)
      .minFontSize(15)
      .border({ width: 1 })
    }
    
    @Entry
    @Component
    export struct LineSpacing {
      build() {
        NavDestination() {
          Column() {
            Text('The line spacing of this context is set to 20\_px, and the spacing is effective only between the lines.')
              .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
              .style()
          }
        }
        // ···
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/wVEwkkD6S3qT7AMQLg65EQ/en-us_image_0000002568684347.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A442683FE84FBC5555D56019CDFE91A4DA1313F44B2E5958D2D13D9861E48B5)
    
-   Since API version 20, use [enableAutoSpacing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#enableautospacing20) to enable automatic spacing between Chinese and English characters.
    
    @Entry
    @Component
    export struct EnableAutoSpacing {
      @State enableSpacing: boolean = false;
    
      build() {
        NavDestination() {
        Column() {
          Row({ space: 20 }) {
            // Replace $r('app.string.Enable\_automatic\_spacing') with the actual resource file. In this example, the value in the resource file is "Enable automatic spacing."
            Button($r('app.string.Enable\_automatic\_spacing'))
              .onClick(() => this.enableSpacing = true)
              .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')
              .fontColor(this.enableSpacing ? Color.White : Color.Black)
            // Replace $r('app.string.off\_automatic\_spacing') with the actual resource file. In this example, the value in the resource file is "Disable automatic spacing."
            Button($r('app.string.off\_automatic\_spacing'))
              .onClick(() => this.enableSpacing = false)
              .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')
              .fontColor(!this.enableSpacing ? Color.White : Color.Black)
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ top: 30, bottom: 20 })
          // Replace $r('app.string.Automatic\_spacing\_has\_been\_enabled') with the actual resource file. In this example, the value in the resource file is "Current status: Automatic spacing enabled."
          // Replace $r('app.string.Automatic\_spacing\_has\_been\_turned\_off') with the actual resource file. In this example, the value in the resource file is "Current status: Automatic spacing disabled."
          Text(this.enableSpacing ? $r('app.string.Automatic\_spacing\_has\_been\_enabled') : $r('app.string.Automatic\_spacing\_has\_been\_turned\_off'))
            .fontSize(16)
            .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')
            .margin({ bottom: 20 })
    
          // Set whether to enable automatic spacing between Chinese and English characters.
          /\* Replace $r('app.string.Chinese\_and\_Western\_Auto\_Spacing\_automatic\_spacing') with the actual resource file.
            In this example, the value in the resource file is "Automatic Spacing Between Chinese and Western Characters." \*/
          Text($r('app.string.Chinese\_and\_Western\_Auto\_Spacing\_automatic\_spacing'))
            .fontSize(24)
            .padding(15)
            .backgroundColor('#F5F5F5')
            .width('90%')
            .enableAutoSpacing(this.enableSpacing)
        }
        .width('100%')
        .height('100%')
        .padding(20)
        }
        // ...
      }
    }
    
-   Since API version 20, you can use [shaderStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#shaderstyle20) to apply gradient color effects to text.
    
    @Entry
    @Component
    export struct ShaderStyle {
      @State message: string = 'Hello World';
      @State linearGradientOptions: LinearGradientOptions =
        {
          direction: GradientDirection.LeftTop,
          colors: \[\[Color.Red, 0.0\], \[Color.Blue, 0.3\], \[Color.Green, 0.5\]\],
          repeating: true,
        };
    
      build() {
        NavDestination() {
          Column({ space: 5 }) {
            // Replace $r('app.string.direction\_LeftTop') with the actual resource file. In this example, the value in the resource file is "Linear gradient (top left direction)."
            Text($r('app.string.direction\_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)
              .margin({ top: 40, left: 40 })
            Text(this.message)
              .fontSize(50)
              .width('80%')
              .height(50)
              .shaderStyle(this.linearGradientOptions)
          }
          .height('100%')
          .width('100%')
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/NcNun1q7T2SUr03YO0JtvQ/en-us_image_0000002568764357.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7A50656F1CEAAE87C15F586A876EE4E073F3B9481ED1BDE2FB6CCCBAE2562F8)
    

#### Adding Events

You can bind the **Text** component to the [onClick](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-click#onclick), [onTouch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-touch#ontouch), or other universal events to respond to user operations.

// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
export struct GeneralEvents {
  @State textStr1: string = '';
  @State textStr2: string = '';

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text('This is a text component.')
            .fontSize(30)
            .onClick(() => {
              hilog.info(0x0000, 'Sample\_TextComponent', 'Text onClick is triggering');
              this.textStr1 = 'Text onClick is triggering';
            })
            .onTouch(() => {
              hilog.info(0x0000, 'Sample\_TextComponent', 'Text onTouch is triggering');
              this.textStr2 = 'Text onTouch is triggering';
            })
          Text('onClick: ' + this.textStr1)
            .fontSize(20)
          Text('onTouch: ' + this.textStr2)
            .fontSize(20)
        }.width('100%')
      }
      .height('100%')
    }
    // ···
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/MuGfw-nVSB-k5CPpCjAn6Q/en-us_image_0000002537764632.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FAA38E6D62ED2B7DBAA6A8341A3629623828438DAC31CED0F7A1D81352AC035)

#### Setting Vertical Alignment

Since API version 20, use the [textVerticalAlign](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textverticalalign20) attribute to vertically align text paragraphs.

-   The following example demonstrates how to use the **textVerticalAlign** attribute to center text vertically:
    
    // Replace $r('app.media.startIcon') with the actual resource file.
    Text() {
      Span('Hello')
        .fontSize(50)
      ImageSpan($r('app.media.startIcon'))
        .width(30).height(30)
        .verticalAlign(ImageSpanAlignment.FOLLOW\_PARAGRAPH)
      Span('World')
    }
    .textVerticalAlign(TextVerticalAlign.CENTER)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/WPMkCMuUQbi3KLdx7vxlJQ/en-us_image_0000002537924572.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFABA0B74F14B9F88CE4A50652CAA9E4063F9214EFBD2F6EEC7A9663C152B6E2)
    

#### Configuring the Selection Menu

## Displaying the Selection Menu

-   When text is selected, a menu containing the copy, translate, and search options is displayed.
    
    The [copyOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#copyoption9) attribute must be set for text selection to be enabled.
    
    // Replace $r('app.string.selected\_menu') with the actual resource file. In this example, the value in the resource file is "This is text used to demonstrate the selection menu."
    Text($r('app.string.selected\_menu'))
      .fontSize(30)
      .copyOption(CopyOptions.InApp)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/n8sWoJEER5an2nZg0-S_vg/en-us_image_0000002568684349.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F998AD1BDCD8770E34038A999FFE1E92F5D9B4178B9C611526ACCFBD873C316D)
    
-   Use the [bindSelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11) attribute to bind a custom selection menu to the **Text** component.
    
    controller: TextController = new TextController();
    options: TextOptions = { controller: this.controller };
    
    // Replace $r('app.string.show\_selected\_menu') with the actual resource file. In this example, the value in the resource file is "This is text used to demonstrate the selection menu."
    Text($r('app.string.show\_selected\_menu'), this.options)
      .fontSize(30)
      .copyOption(CopyOptions.InApp)
      .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT\_CLICK, {
        onAppear: () => {
          // Replace $r('app.string.SelectMenu\_Text\_Ejected') with the actual resource file. In this example, the value in the resource file is "This callback is triggered when the custom selection menu is displayed."
          hilog.info(0x0000, 'Sample\_TextComponent',
            this.getUIContext()
              .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_Ejected').id));
        },
        onDisappear: () => {
          // The value in the 'SelectMenu\_Text\_Close' resource file is 'This callback is triggered when the custom selection menu is closed.'
          hilog.info(0x0000, 'Sample\_TextComponent',
            this.getUIContext()
              .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_Close').id));
        }
      })
    
    // Define menu items.
    @Builder
    RightClickTextCustomMenu() {
      Column() {
        Menu() {
          MenuItemGroup() {
            // Replace $r('app.media.app\_icon') with the actual resource file.
            MenuItem({ startIcon: $r('app.media.app\_icon'), content: 'CustomMenu One', labelInfo: '' })
              .onClick(() => {
                // Use the closeSelectionMenu API to close the menu.
                this.controller.closeSelectionMenu();
              })
            MenuItem({ startIcon: $r('app.media.app\_icon'), content: 'CustomMenu Two', labelInfo: '' })
            MenuItem({ startIcon: $r('app.media.app\_icon'), content: 'CustomMenu Three', labelInfo: '' })
          }
        }.backgroundColor('#F0F0F0')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/juS0mQslSwaKwM32NEi4uA/en-us_image_0000002568764359.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CF13FD826B4572944942BE497F65ED17B8DE308D93D4C0CBD929A56226362CF)
    
-   Customize menu items by configuring the [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12) attribute of the **Text** component. You can set the text content, icons, and callbacks for extended menu items.
    
    // Replace $r('app.string.show\_selected\_menu') with the actual resource file. In this example, the value in the resource file is "This is text used to demonstrate the selection menu."
    Text($r('app.string.show\_selected\_menu'))
      .fontSize(20)
      .copyOption(CopyOptions.LocalDevice)
      .editMenuOptions({
        onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick
      })
    
    // Define onCreateMenu and onMenuItemClick.
    // Replace $r('app.media.app\_icon') with the actual resource file.
    onCreateMenu = (menuItems: Array<TextMenuItem>) => {
      let item1: TextMenuItem = {
        content: 'customMenu1',
        icon: $r('app.media.app\_icon'),
        id: TextMenuItemId.of('customMenu1'),
      };
      let item2: TextMenuItem = {
        content: 'customMenu2',
        id: TextMenuItemId.of('customMenu2'),
        icon: $r('app.media.app\_icon'),
      };
      menuItems.push(item1);
      menuItems.unshift(item2);
      return menuItems;
    }
    onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
      if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {
        // Replace $r('app.string.SelectMenu\_Text\_customMenu') with the actual resource file. In this example, the value in the resource file is "Intercept id: customMenu2 start:".
        hilog.info(0x0000, 'Sample\_TextComponent',
          this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_customMenu')
            .id) + textRange.start + '; end:' +
          textRange.end);
        return true;
      }
      if (menuItem.id.equals(TextMenuItemId.COPY)) {
        // Replace $r('app.string.SelectMenu\_Text\_copy') with the actual resource file. In this example, the value in the resource file is "Intercept COPY start:".
        hilog.info(0x0000, 'Sample\_TextComponent',
          this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_copy').id) +
          textRange.start + '; end:' + textRange.end);
        return true;
      }
      if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
        // Replace $r('app.string.SelectMenu\_Text\_SelectionAll') with the actual resource file. In this example, the value in the resource file is "Do not intercept SELECT\_ALL start:".
        hilog.info(0x0000, 'Sample\_TextComponent',
          this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu\_Text\_SelectionAll').id) +
          textRange.start + '; end:' +
          textRange.end);
        return false;
      }
      return false;
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/3mwm7ZmtSPGBkCi5pw9vbw/en-us_image_0000002537764634.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52AD69B980925A941861FE5C8181C2D102565D84F521719BF60C04D778FAE352)
    

## Closing the Selection Menu

When using the **Text** component, you can close the selection state and menu by clicking blank areas in the following scenarios:

-   Clicking blank areas within the **Text** component's layout boundaries closes the selection state and menu.
    
-   Clicking blank areas outside the **Text** component requires the [selection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#selection11) attribute to be set on the **Text** component. Example:
    
    // xxx.ets
    @Entry
    @Component
    export struct SelectionChange {
      @State text: string =
        'This is set selection to Selection text content This is set selection to Selection text content.';
      @State start: number = 0;
      @State end: number = 20;
    
      build() {
        NavDestination() {
          Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
            Text(this.text)
              .fontSize(12)
              .border({ width: 1 })
              .lineHeight(20)
              .margin(30)
              .copyOption(CopyOptions.InApp)
              .selection(this.start, this.end)
              .onTextSelectionChange((selectionStart, selectionEnd) => {
                // Update the selection range position.
                this.start = selectionStart;
                this.end = selectionEnd;
              })
          }
          .height(600)
          .width(335)
          .borderWidth(1)
          .onClick(() => {
            // Listen for click events on the parent component and clear the selection by setting start and end positions to -1.
            this.start = -1;
            this.end = -1;
          })
        }
        // ···
      }
    }
    

## Disabling System Menu Callbacks and Custom Extended Menu Items

Since API version 12, use [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12) to disable system menu callbacks and custom extended menu items .

// xxx.ets
@Entry
@Component
export struct CustomAndBlockMenus {
  private static readonly CREATE\_MENU\_ITEM\_ID\_1: string = 'create1';
  private static readonly CREATE\_MENU\_ITEM\_ID\_2: string = 'create2';
  private static readonly PREPARE\_MENU\_ITEM\_ID: string = 'prepare1';
  @State private text: string = 'Text editMenuOptions';
  @State private endIndex: number = 0;
  @State blockCallbackText: string = '';

  // Auxiliary method for creating a menu item.
  private createMenuItem(id: string, content: string): TextMenuItem {
    // Replace $r('app.media.startIcon') with the image resource file you use.
    return {
      content: content,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of(id)
    };
  }

  // Search for the menu item index.
  private findMenuItemIndex(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): number {
    return menuItems.findIndex((item: TextMenuItem) => item.id.equals(menuItemId));
  }

  // Callback triggered when a menu is created.
  private onCreateMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const createItem1: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE\_MENU\_ITEM\_ID\_1,
      'create1'
    );

    const createItem2: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE\_MENU\_ITEM\_ID\_2,
      'create2'
    );

    // Add a custom menu item.
    menuItems.push(createItem1);
    menuItems.unshift(createItem2);

    // Remove unnecessary system menu items.
    this.removeMenuItemById(menuItems, TextMenuItemId.AI\_WRITER);
    this.removeMenuItemById(menuItems, TextMenuItemId.TRANSLATE);

    return menuItems;
  }

  // Remove a specified menu item.
  private removeMenuItemById(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): void {
    const targetIndex: number = this.findMenuItemIndex(menuItems, menuItemId);
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
  }

  // Callback triggered when a menu item is clicked.
  private onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange): boolean => {
    const menuItemId: TextMenuItemId = menuItem.id;

    // Process the custom menu item.
    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.CREATE\_MENU\_ITEM\_ID\_2))) {
      let msg = 'Intercept id: create2 start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.PREPARE\_MENU\_ITEM\_ID))) {
      let msg = 'Intercept id: prepare1 start:' + textRange.start + '; end:+' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    // Process the system menu item.
    if (menuItemId.equals(TextMenuItemId.COPY)) {
      let msg = 'Intercept COPY start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.SELECT\_ALL)) {
      let msg = 'Allow SELECT\_ALL start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return false;
    }

    return false;
  }
  // Callback triggered when the menu is prepared.
  private onPrepareMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const prepareItem: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.PREPARE\_MENU\_ITEM\_ID,
      \`prepare1\_${this.endIndex}\`
    );

    menuItems.unshift(prepareItem);
    return menuItems;
  }
  // Edit menu options.
  @State private editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };
  // Callback triggered when the text selection changes.
  private onTextSelectionChange = (selectionStart: number, selectionEnd: number): void => {
    this.endIndex = selectionEnd;
  }

  build() {
    NavDestination() {
      Column() {
        Text(this.text)
          .fontSize(20)
          .copyOption(CopyOptions.LocalDevice)
          .editMenuOptions(this.editMenuOptions)
          .margin({ top: 100 })
          .onTextSelectionChange(this.onTextSelectionChange)
        Text(this.blockCallbackText).borderWidth(1)
      }
      .width('90%')
      .margin('5%')
    }
  }
}

## Disabling System Service Menu Items

-   Since API version 20, use [disableSystemServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20) to disable all system service menu items in the text selection menu.
    
    import { TextMenuController } from '@kit.ArkUI';
    // xxx.ets
    @Entry
    @Component
    export struct ServiceMenuItems {
      aboutToAppear(): void {
        // Disable all system service menus.
        TextMenuController.disableSystemServiceMenuItems(true);
      }
    
      aboutToDisappear(): void {
        // Restore system service menu items when the page disappears.
        TextMenuController.disableSystemServiceMenuItems(false);
      }
      build() {
        NavDestination() {
          Row() {
            Column() {
              // Replace $r('app.string.Service\_MenuItems\_Text') with the actual resource file. In this example, the value in the resource file is "This is a piece of text. Long press to display the text selection menu."
              Text($r('app.string.Service\_MenuItems\_Text'))
                .height(60)
                .fontStyle(FontStyle.Italic)
                .fontWeight(FontWeight.Bold)
                .textAlign(TextAlign.Center)
                .copyOption(CopyOptions.InApp)
                .editMenuOptions({
                  onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                    // menuItems does not contain the disabled system menu items.
                    return menuItems;
                  },
                  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                    return false;
                  }
                })
            }.width('100%')
          }
          .height('100%')
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/crbADtCZRrauE14ewPUoog/en-us_image_0000002537924574.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=021169E69065A3CCFB3BC766AE59AE49B571B58F6AAB1810A357F6C4BA0F3FCC)
    
-   Since API version 20, use [disableMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20) to disable specified system service menu items in the text selection menu.
    
    import { TextMenuController } from '@kit.ArkUI';
    
    // xxx.ets
    @Entry
    @Component
    export struct DisableMenuItems {
      aboutToAppear(): void {
        // Disable the search menu item.
        TextMenuController.disableMenuItems(\[TextMenuItemId.SEARCH\])
      }
    
      aboutToDisappear(): void {
        // Restore system service menu items.
        TextMenuController.disableMenuItems(\[\])
      }
    
      build() {
        NavDestination() {
          Row() {
            Column() {
              // Replace $r('app.string.Service\_MenuItems\_Text') with the actual resource file. In this example, the value in the resource file is "This is a piece of text. Long press to display the text selection menu."
              Text($r('app.string.Service\_MenuItems\_Text'))
                .height(60)
                .fontStyle(FontStyle.Italic)
                .fontWeight(FontWeight.Bold)
                .textAlign(TextAlign.Center)
                .copyOption(CopyOptions.InApp)
                .editMenuOptions({
                  onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                    // menuItems does not contain the search menu item.
                    return menuItems;
                  },
                  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                    return false
                  }
                })
            }.width('100%')
          }
          .height('100%')
        }
        // ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/d_60x879T_uCx60f29egBA/en-us_image_0000002568684351.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95E16FCF0BF4A35C3111B9B0D9B9C1D9CD372862E1E094422023FEA775AD80A5)
    

## Customizing the Default Menu Refresh Behavior

Since API version 20, the [onPrepareMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#properties-1) callback is triggered before the menu is displayed when the text selection range changes. You can configure menu data within this callback.

// Replace $r('app.media.xxx') with the actual resource file.
// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0000;
@Entry
@Component

export struct PrepareMenu {
  @State text: string = 'Text editMenuOptions';
  @State endIndex: number = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: create2 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: prepare1 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept COPY start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT\_ALL)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'No interception SELECT\_ALL start:' + textRange.start + '; end:' + textRange.end);
      return false;
    }
    return false;
  }
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
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
    NavDestination() {
    Column() {
      Text(this.text)
        .fontSize(20)
        .copyOption(CopyOptions.LocalDevice)
        .editMenuOptions(this.editMenuOptions)
        .margin({ top: 100 })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.endIndex = selectionEnd;
        })
    }
    .width('90%')
    .margin('5%')
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/-eqsc09HSZW0xUlj5-WSgA/en-us_image_0000002568764361.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55A99A008B9475CFACFC5EC0C461908E281FC0A688965033B956CD8711AE780A)

#### Configuring the AI Menu

The **Text** component enables AI menu display through the [enableDataDetector](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11) and [dataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11) attributes. The AI menu appears in the following scenarios: (1) Clicking an AI entity (recognizable content such as addresses and email addresses) displays entity recognition options. (2) After text selection, entity recognition options appear in both the text selection menu and right-click context menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/sW40yfd6T3mz_V7QdvIbjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E8AE404F1BEE01D88305BD817D672A433D54561453615DD98DFF17B74BEA728)

Since API version 20, entity recognition options can be displayed in both text selection menus and right-click context menus. This feature takes effect when [enableDataDetector](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11) is set to **true** and [copyOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#copyoption9) is set to **CopyOptions.LocalDevice**. The menu options include **url** (opening a link), **email** (creating an email), **phoneNumber** (calling), **address** (navigating to the location), and **dateTime** (creating a calendar reminder) in [TextMenuItemId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#textmenuitemid12).

The selection range must encompass a complete AI entity for the corresponding options to appear.

-   To display entity recognition options when AI entities are clicked, set [enableDataDetector](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11) to **true**.
    
-   To display entity recognition options in both text selection menus and right-click context menus, set [enableDataDetector](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11) to **true** and [copyOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#copyoption9) to **CopyOptions.LocalDevice**. The following is an example:
    
    // The value in the 'app.string.AIMenu\_Text\_One' resource file is 'Phone number: (86) (755)  \*\*\*\*\*\*\*\*  \\n \\n URL: www.\*\*\*\*\*\*\*\*.com
    // \\n \\n Email: \*\*\*@example.com\\n \\n Address: XXXX, XX District, XX City, XX Province \\n \\n Time: XX:XX, MM, DD, YYYY.'
    Text($r('app.string.AIMenu\_Text\_One'))
      .fontSize(16)
      .copyOption(CopyOptions.LocalDevice)
      .enableDataDetector(true) // Enable entity recognition.
      .dataDetectorConfig({
        // Configure recognition styles.
        // types can be PHONE\_NUMBER (phone number), URL (link), EMAIL (email), ADDRESS (address), and DATE\_TIME (time).
        // If types is set to null or \[\], all types of entities are recognized.
        types: \[\], onDetectResultUpdate: (result: string) => {
        }
      })
    
-   Use [dataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11) to customize entity recognition styles. For details, see [TextDataDetectorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11).
    
-   Use [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12) to adjust the menu position. For implementation details, see [Example 12: Setting Custom Menu Extensions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#example-12-setting-custom-menu-extensions).
    

#### Implementing Hot Search Rankings

This example demonstrates how to implement a hot search list using the [maxLines](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#maxlines), [textOverflow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textoverflow), [textAlign](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text#textalign), and [constraintSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#constraintsize) attributes.

import { ComponentCard } from '../../common/Card';

@Entry
@Component
export struct TextHotSearch {
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Column() {
            Row() {
              Text('1').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
              // Replace $r('app.string.TextHotSearch\_textContent\_one') with the actual resource file. In this example, the value in the resource file is "I am entry 1."
              Text($r('app.string.TextHotSearch\_textContent\_one'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .fontWeight(300)
              // Replace $r('app.string.TextHotSearch\_textContent\_two') with the actual resource file. In this example, the value in the resource file is "Top Hit."
              Text($r('app.string.TextHotSearch\_textContent\_two'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0x770100)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('2').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
              /\* Replace $r('app.string.TextHotSearch\_textContent\_three') with the actual resource file.
                In this example, the value in the resource file is "I am entry 2 I am entry 2 I am entry 2 I am entry 2 I am entry 2." \*/
              Text($r('app.string.TextHotSearch\_textContent\_three'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
              // Replace $r('app.string.TextHotSearch\_textContent\_four') with the actual resource file. In this example, the value in the resource file is "Hot."
              Text($r('app.string.TextHotSearch\_textContent\_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('3').fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })
              // Replace $r('app.string.TextHotSearch\_textContent\_five') with the actual resource file. In this example, the value in the resource file is "I am entry 3."
              Text($r('app.string.TextHotSearch\_textContent\_five'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .maxLines(1)
                .constraintSize({ maxWidth: 200 })
                .textOverflow({ overflow: TextOverflow.Ellipsis })
              // Replace $r('app.string.TextHotSearch\_textContent\_four') with the actual resource file. In this example, the value in the resource file is "Hot."
              Text($r('app.string.TextHotSearch\_textContent\_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('4').fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })
              /\* Replace $r('app.string.TextHotSearch\_textContent\_six') with the actual resource file.
                In this example, the value in the resource file is "I am entry 4 I am entry 4 I am entry 4 I am entry 4 I am entry 4." \*/
              Text($r('app.string.TextHotSearch\_textContent\_six'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
            }.width('100%').margin(5)
          }.width('100%')
        // ...
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/bHwQTUEoQNmqyUq5KuDZvg/en-us_image_0000002537764636.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C25D2A6A7875F5F36D9D0A30D3D028998B3E93BC83EEFE570C060889D8399F1)
