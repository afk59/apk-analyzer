# Implementing UI Internationalization

This topic explains how to implement UI internationalization in an application, including resource configuration and layout adaptation. For details about internationalization guidance, see [Localization Kit](../../../localization-kit/about-this-kit/document.md).

#### Configuring Internationalization Resources with Resource Qualifiers

To support multiple languages and regions, you can configure localized resources using resource qualifiers in DevEco Studio. For details, see [Resource Categories and Access](../../../../getting-started/resource-categories-and-access/document.md).

#### Using the Mirroring Capability

Different text alignment modes and reading sequences may be used for different languages. For example, English is read from left-to-right (LTR), and Arabic and Greek are read from right-to-left (RTL). To accommodate diverse user reading habits, ArkUI provides a mirroring capability that can reverse the display content along the x-axis, switching the layout from left-to-right to right-to-left.

| Before Mirroring | After Mirroring |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Ufdr_ykJTJaGhheRhnBJdg/en-us_image_0000002568684569.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061939Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E26AEF2F3E13E41342745697978C4300603BB6AC5B93DEACB6539AE21D2573F9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/jIn81C_lTMmMLOyyeUobgw/en-us_image_0000002568764579.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061939Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FE69135FCC22E4CD7D0E7ABED00CE9EAED7804A06298F7E242241D8FBCBD539) |

The mirroring capability is activated on a component under either of these conditions:

1.  The component's **direction** attribute is set to **Direction.Rtl**.
    
2.  The component's **direction** attribute is set to **Direction.Auto**, and the system language in use (such as Uyghur) is read from right to left.
    

## Basic Concepts

-   LTR: left-to-right reading direction
-   RTL: right-to-left reading direction

## Constraints

ArkUI provides built-in mirroring support for the following capabilities.

| Category | Name |
| :-- | :-- |
| Basic components | [Swiper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper), [Tabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabs), [TabContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabcontent), [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list), [Progress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-progress), [CalendarPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-calendarpicker), [CalendarPickerDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-calendarpicker-dialog), [TextPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textpicker), [TextPickerDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-textpicker-dialog), [DatePicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-datepicker), [DatePickerDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-datepicker-dialog), [Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [WaterFlow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow), [Scroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll), [ScrollBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-scrollbar), [AlphabetIndexer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-alphabet-indexer), [Stepper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-stepper), [SideBarContainer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-sidebarcontainer), [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation), [NavDestination](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navdestination), [Rating](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-rating), [Slider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-slider), [Toggle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-toggle), [Badge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-badge), [Counter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-counter), [Chip](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-chip), [SegmentButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton), [bindMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-menu#bindmenu), [bindContextMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu8), [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput), [TextArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea), [Search](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-search), [Stack](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-stack), [GridRow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-gridrow), [Text](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text), [Select](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-select), [Marquee](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-marquee), [Row](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-row), [Column](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-column), [Flex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-flex), [RelativeContainer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-relativecontainer), [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup) |
| Advanced components | [SelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu), [TreeView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-treeview), [Filter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-filter), [SplitLayout](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-splitlayout), [ToolBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-toolbar), [ComposeListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-composelistitem), [EditableTitleBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar), [ProgressButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-progressbutton), [SubHeader](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-subheader), [Popup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-popup), [Dialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-dialog), [SwipeRefresher](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-arkui-advanced-swiperefresher) |
| Universal attributes | [position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#position), [markAnchor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#markanchor), [offset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#offset), [alignRules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#alignrules12), [borderWidth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#borderwidth), [borderColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#bordercolor), [borderRadius](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#borderradius), [padding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#padding), [margin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#margin) |
| APIs | [AlertDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-alert-dialog-box), [ActionSheet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-action-sheet), [promptAction.showDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-promptaction#promptactionshowdialogdeprecated), [promptAction.showToast](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-promptaction#promptactionshowtoastdeprecated) |

However, adaptation is still required in the following three scenarios:

1.  For layout and border settings, use the generalized direction terms **start** and **end** as parameter types instead of absolute terms such as **left**, **right**, **x**, and **y**, to accommodate mirroring.
    
2.  The **Canvas** component offers limited support for mirroring in text drawing only.
    
3.  The **XComponent** component does not support mirroring capabilities.
    

## Layout and Border Settings

To adapt to mirroring capabilities, update the following universal attributes with new parameter types:

Position settings: [position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#position), [markAnchor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#markanchor), [offset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#offset), [alignRules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#alignrules12)

Border settings: [borderWidth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#borderwidth), [borderColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#bordercolor), [borderRadius](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#borderradius)

Size settings: [padding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#padding), [margin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#margin)

For example, with **position**, change the absolute directional descriptions of **x** and **y** to the new parameter types of **start** and **end**.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct InterfaceLayoutBorderSettings {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Stack({ alignContent: Alignment.TopStart }) {
        Column()
          .width(100)
          .height(100)
          .backgroundColor(Color.Red)
          .position({
            start: LengthMetrics.px(200),
            top: LengthMetrics.px(200)
          }) // Use the new LocalizedEdges parameter type added since API version 12 for supporting both LTR and RTL.
        // It is equivalent to .position({ x: '200px', y: '200px' }) when only LTR is supported.

      }.backgroundColor(Color.Blue)
    }.width('100%').height('100%').border({ color: '#880606' })
  }
}

## Custom Drawing with the Canvas Component

The drawings and coordinates of the **Canvas** component do not support mirroring. Content drawn on it does not automatically mirror when the system language changes.

[CanvasRenderingContext2D](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-canvasrenderingcontext2d) supports mirroring for text rendering, which should be used with the **Canvas** component's **direction** attribute and the **direction** attribute of **CanvasRenderingContext2D**. The following table lists the specifications.

1.  Priority: The **direction** attribute of **CanvasRenderingContext2D** takes precedence over the **Canvas** component's **direction** attribute, which in turn follows the system language's horizontal display direction.
2.  The **Canvas** component does not automatically mirror with system language changes; applications must listen for system language changes and redraw the content on their own.
3.  Only symbols follow the direction setting during text drawing with **CanvasRenderingContext2D**; Latin characters and numbers do not.

import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

@Entry
@Component
struct CustomizeCanvasComponentDrawing {
  @State message: string = 'Hello world';
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  aboutToAppear(): void {
    // Listen for the system language changes.
    let subscriber: commonEventManager.CommonEventSubscriber | null = null;
    let subscribeInfo2: commonEventManager.CommonEventSubscribeInfo = {
      events: \['usual.event.LOCALE\_CHANGED'\],
    }
    commonEventManager.createSubscriber(subscribeInfo2,
      (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
        if (err) {
          console.error(\`Failed to create subscriber. Code is ${err.code}, message is ${err.message}\`);
          return;
        }

        subscriber = data;
        if (subscriber !== null) {
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              return;
            }
            // After detecting the language switch, redraw the content on the Canvas component.
            this.drawText();
          })
        } else {
          console.error(\`MayTest Need create subscriber\`);
        }
      })
  }

  drawText(): void {
    console.error('MayTest drawText')
    this.context.reset()
    this.context.direction = 'inherit'
    this.context.font = '30px sans-serif'
    this.context.fillText('ab%123&\*@', 50, 50)
  }

  build() {
    Row() {
      Canvas(this.context)
        .direction(Direction.Auto)
        .width('100%')
        .height('100%')
        .onReady(() =>{
          this.drawText()
        })
        .backgroundColor(Color.Pink)
    }
    .height('100%')
  }

}

| Before Mirroring | After Mirroring |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/IdJpQXhHSImr5GhEmChVyA/en-us_image_0000002537764854.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061939Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE8015B1D4FAE95B16FBB57012FA4767FA9518EA6EDDC4410D9C2AB901CD2AE4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/G5YR8V5ET92AFkY_8eiw6Q/en-us_image_0000002537924794.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061939Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3A5D896705BAF41C465882DE31FCEAF653EF3A9A3FBBBACED53FD1A0449EDCB) |

## Bidirectional Text Layout and Alignment

Text direction ([Direction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-appendix-enums#direction)) defines the order of characters when text is presented on the screen. In left-to-right (LTR) scripts, the display order is from left to right; in right-to-left (RTL) scripts, the display order is from right to left.

Text alignment ([TextAlign](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-appendix-enums#textalign)) affects the layout of text as a whole, with specific positioning influenced by **Direction**. For example, when **TextAlign** is set to **start**, the text is left-aligned if **Direction** is **LTR**, and is right-aligned if **Direction** is **RTL**.

When LTR and RTL scripts are mixed (for example, an English sentence containing Arabic words or phrases), the display order can become complex. The following figure shows the logical order of characters when numbers and Uyghur are mixed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/xiwTIjcvQeyQj9m-lx83Kw/en-us_image_0000002568684571.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061939Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14235FAF8AFA7980E0A7F9A67FC297B3B6B12C4AFCBF2821E9FADC9F892D7CD0)

In this case, the text rendering engine uses a method called the Unicode Bidirectional Algorithm to determine the character display order. The following figure illustrates the character display order for mixed LTR and RTL scripts. The basic principles for determining character direction are as follows:

1.  Strong characters: Strong characters have a definite directionality. For example, Chinese characters are LTR, and Arabic characters are RTL. These characters influence the directionality of surrounding neutral characters.
    
2.  Weak characters: Weak characters do not have a definite directionality. These characters do not affect the directionality of surrounding neutral characters.
    
3.  Neutral characters: Neutral characters do not have a fixed directionality. They inherit the directionality of the nearest strong character. If there are no strong characters nearby, they adopt the global direction.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/LPtnPDDbQzugyvnSgfHqUA/en-us_image_0000002568764581.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061939Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCCE7E730007B7F845487E4E1878AD08E95E8CD50C4901541937638ED5E5F3D8)
