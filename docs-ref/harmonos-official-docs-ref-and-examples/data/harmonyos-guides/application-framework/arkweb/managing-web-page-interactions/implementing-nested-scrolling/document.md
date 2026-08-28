# Implementing Nested Scrolling

There may be times when you want to implement nested scrolling for the **Web** component. A typical use case is a page that contains multiple scrollable areas including the **Web** component, whose scrolling is intrinsically linked with the scroll positions in other areas. To implement nested scrolling between **Web** components and ArkUI scrollable containers ([Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list), [Scroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll), [Swiper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper), [Tabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabs), [WaterFlow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow), [Refresh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-refresh) and [bindSheet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)), you should set the ArkUI [NestedScrollMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-appendix-enums#nestedscrollmode10) attribute for the **Web** components after receiving the scrolling gesture events.

The following provides two solutions for implementing nested scrolling of **Web** components: Solution 1: [Using the nestedScroll Attribute](#using-the-nestedscroll-attribute); Solution 2: [Distributing Scrolling Offsets Through the Parent Scroll Component](#distributing-scrolling-offsets-through-the-parent-scroll-component). You can select a solution based on the specific service scenario. To associate **Web** components with other parent components, you are advised to use solution 1. To customize the scrolling of **Web** components and other scrolling components, especially in some complex scenarios, you are advised to use solution 2.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/4NP2Iy4CSKucaHoWjUV4WA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BB405A119419DC2436A1E9EFFA79C35AD36F19825BE49AE4AC9BAD74434311B)

If a **Web** component uses full expansion (**layoutMode** is set to **WebLayoutMode.FIT\_CONTENT**), the rendering mode (**RenderMode.SYNC\_RENDER**) must be explicitly specified. For details, see [layoutMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#layoutmode11).

#### Using the nestedScroll Attribute

Call the [nestedScroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#nestedscroll11) attribute of the **Web** component to set the nested scrolling mode in the up, down, left, and right directions or in the forward and backward directions to implement the scrolling association with the parent component. This attribute also allows the nested scrolling mode to be dynamically changed during the process.

**Complete Code**

import { webview } from '@kit.ArkWeb';

@Entry
@ComponentV2
struct NestedScroll {
  private scrollerForScroll: Scroller = new Scroller();
  private listScroller: Scroller = new Scroller();
  controller: webview.WebviewController = new webview.WebviewController();
  @Local arr: Array<number> = \[\];

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
    this.arr.push(i);
  }
}

build() {
  Scroll(this.scrollerForScroll) {
    Column() {
      Web({ src: $rawfile('scroll.html'), controller: this.controller })
        .nestedScroll({
          scrollUp: NestedScrollMode.PARENT\_FIRST,//Scroll up the parent component first.
          scrollDown: NestedScrollMode.SELF\_FIRST,//Scroll down the child component first.
        }).height('100%')
      Repeat<number>(this.arr)
        .each((item: RepeatItem<number>) => {
          Text('Scroll Area')
            .width('100%')
            .height('40%')
            .backgroundColor(0X330000FF)
            .fontSize(16)
            .textAlign(TextAlign.Center)
        })
    }
  }
}
}

HTML file to be loaded:

<!-- scroll.html -->
<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
            background-color: lightblue;
        }

        .green {
            background-color: lightgreen;
        }

        .blue,
        .green {
            font-size: 16px;
            height: 200px;
            text-align: center;
            /\* Horizontally centered \*/
            line-height: 200px;
            /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>

<body>
    <div class="blue">webArea</div>
    <div class="green">webArea</div>
    <div class="blue">webArea</div>
    <div class="green">webArea</div>
    <div class="blue">webArea</div>
    <div class="green">webArea</div>
    <div class="blue">webArea</div>
</body>

</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NphCxM8IRzieRW5FeXhzJg/en-us_image_0000002568764729.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38BFD3FB8BBC822F1A5FA2A9DDB31BC4201B0747089D49E2F47478337081777D)

#### Distributing Scrolling Offsets Through the Parent Scroll Component

**How to Implement**

1.  Scrolling up:
    
    (1) If the web page does not scroll to the bottom, the **Scroll** component sends the scrolling offset to the **Web** component, and the **Scroll** component does not scroll.
    
    (2) If the web page scrolls to the bottom but the **Scroll** component does not scroll to the bottom, only the **Scroll** component scrolls and it does not send the scrolling offset to the **Web** and **List** components.
    
    (3) If the **Scroll** component scrolls to the bottom, the scrolling offset is sent to the **List** component, and the **Scroll** component does not scroll.
    
2.  Scrolling down:
    
    (1) If the **List** component does not scroll to the top, the **Scroll** component sends the scrolling offset to the **List** component, and the **Scroll** component does not scroll.
    
    (2) When the **List** component scrolls to the top but the **Scroll** component does not, the **Scroll** component automatically scrolls. The scrolling offset is not sent to the **List** component and **Web** component.
    
    (3) If the **Scroll** component scrolls to the top, the scrolling offset is sent to the **Web** component, and the **Scroll** component does not scroll.
    

**Implementation**

1.  Disable the scrolling gestures of the **Web** component.
    
    (1) Call [setScrollable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setscrollable12) to disable touch scrolling.
    
    this.webController.setScrollable(false, webview.ScrollType.EVENT);
    
    (2) Call [onGestureRecognizerJudgeBegin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-gesture-blocking-enhancement#ongesturerecognizerjudgebegin13) to disable the scrolling gesture of the **Web** component.
    
    .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer, otherArray<GestureRecognizer>) => {
      if (current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN\_GESTURE) {
        return GestureJudgeResult.REJECT;
      }
      return GestureJudgeResult.CONTINUE;
    })
    
2.  Disable the gestures of the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component.
    
    .enableScrollInteraction(false)
    
3.  Check whether the **List** and **Scroll** components scroll to the boundary.
    
    (1) The component scrolls to the top boundary: **scroller.currentOffset().yOffset <= 0**;
    
    (2) The component scrolls to the bottom boundary: **scroller.isAtEnd() == true**;
    
4.  Check whether the **Web** component scrolls to the boundary.
    
    (1) Obtain the height, content height, and current scrolling offset of the **Web** component.
    
    (2) The component scrolls to the top boundary: **webController.getPageOffset().y == 0**;
    
    (3) The component scrolls to the bottom boundary: **webController.getPageOffset().y + this.webHeight >= webController.getPageHeight()**;
    
    (4) Height of the **Web** component: **webController.[getPageHeight()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getpageheight)**;
    
    (5) Height of the **Web** component window: **webController?.[runJavaScriptExt](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascriptext10)('window.innerHeight')**;
    
    (6) Scrolling offset of the **Web** component: **webController.[getPageOffset()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getpageoffset20)**;
    
5.  Disable the scrolling feature of the **Scroll** component.
    
    Bind the **Scroll** component to the [onScrollFrameBegin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll#onscrollframebegin9) event and set the remaining scrolling offset to **0**. Then the **Scroll** component does not scroll, and the inertial scrolling animation does not stop.
    
6.  Distribute the scrolling offset to the **List** component.
    
    this.listScroller.scrollBy(0, offset)
    
7.  Distribute the scrolling offset to the **Web** component.
    
    this.webController.scrollBy(0, offset)
    
8.  Set [bypassVsyncCondition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#bypassvsynccondition20) of the **Web** component to **WebBypassVsyncCondition.SCROLLBY\_FROM\_ZERO\_OFFSET** to accelerate the drawing of the first scrolling frame.
    
    .bypassVsyncCondition(WebBypassVsyncCondition.SCROLLBY\_FROM\_ZERO\_OFFSET)
    

**Complete Code**

import { webview } from '@kit.ArkWeb';

@Entry
@ComponentV2
struct Index {
  private scroller: Scroller = new Scroller()
  private listScroller: Scroller = new Scroller()
  private webController: webview.WebviewController = new webview.WebviewController()
  private isWebAtEnd: boolean = false
  private webHeight: number = 0
  @Local arr: Array<number> = \[\]

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.arr.push(i)
    }
  }

  getWebHeight() {
    try {
      this.webController?.runJavaScriptExt('window.innerHeight',
        (error, result) => {
          if (error || !result) {
            return;
          }
          if (result.getType() === webview.JsMessageType.NUMBER) {
            this.webHeight = result.getNumber()
          }
        })
    } catch (error) {
    }
  }

  checkScrollBottom() {
    this.isWebAtEnd = false;
    if (this.webController.getPageOffset().y + this.webHeight >= this.webController.getPageHeight()) {
      this.isWebAtEnd = true;
    }
  }

  build() {
    Scroll(this.scroller) {
      Column() {
        Web({
          src: $rawfile('scroll.html'),
          controller: this.webController,
        }).height('100%')
          .bypassVsyncCondition(WebBypassVsyncCondition.SCROLLBY\_FROM\_ZERO\_OFFSET)
          .onPageEnd(() => {
            this.webController.setScrollable(false, webview.ScrollType.EVENT);
            this.getWebHeight();
          })
          // When the recognizer is about to succeed, set whether to enable the recognizer based on the current component status.
          .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
            others: Array<GestureRecognizer>) => {
            if (current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN\_GESTURE) {
              return GestureJudgeResult.REJECT;
            }
            return GestureJudgeResult.CONTINUE;
          })
        List({ scroller: this.listScroller }) {
          Repeat<number>(this.arr)
            .each((item: RepeatItem<number>) => {
              ListItem() {
                Text('Scroll Area')
                  .width('100%')
                  .height('40%')
                  .backgroundColor(0X330000FF)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
              }
            })
        }.height('100%')
        .maintainVisibleContentPosition(true)
        .enableScrollInteraction(false)
      }
    }
    .onScrollFrameBegin((offset: number, state: ScrollState) => {
      this.checkScrollBottom();
      if (offset > 0) {
        if (!this.isWebAtEnd) {
          this.webController.scrollBy(0, offset)
          return { offsetRemain: 0 }
        } else if (this.scroller.isAtEnd()) {
          this.listScroller.scrollBy(0, offset)
          return { offsetRemain: 0 }
        }
      } else if (offset < 0) {
        if (this.listScroller.currentOffset().yOffset > 0) {
          this.listScroller.scrollBy(0, offset)
          return { offsetRemain: 0 }
        } else if (this.scroller.currentOffset().yOffset <= 0) {
          this.webController.scrollBy(0, offset)
          return { offsetRemain: 0 }
        }
      }
      return { offsetRemain: offset }
    })
  }
}

HTML file to be loaded:

<!-- scroll.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /\* Horizontally centered \*/
         line-height: 200px;       /\* Vertically centered (the height matches the container height) \*/
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/4yCW8f5nTmupPjM1ETmVGg/en-us_image_0000002537765004.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8B579719837CBAD25DD98F13E8F14618EC9B4EFB62A9901E3D469A4C0A47E01)
