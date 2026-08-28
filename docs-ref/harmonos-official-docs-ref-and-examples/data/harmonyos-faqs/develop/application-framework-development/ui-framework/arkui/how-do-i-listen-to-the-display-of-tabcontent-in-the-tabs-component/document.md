# How do I listen to the display of TabContent in the Tabs component?

**Background**

The **onWillShow** callback is triggered when **TabContent** is about to be displayed. The scenarios include:

1.  **TabContent** first-time display.
2.  **TabContent** switching.
3.  Page switching.
4.  Window switching between foreground and background.

The **onWillHide** callback is triggered when **TabContent** is about to be hidden. The scenarios include:

1.  **TabContent** switching.
2.  Page switching.
3.  Window switching between foreground and background.

**Solution**

You can use the [onWillShow()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabcontent#onwillshow12) and [onWillHide()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabcontent#onwillhide12) events of **TabContent** to report the disappearance and appearance of **TabContent** during tab pages switching.

**FAQs**

Q: How do I detect the appearance or disappearance of a child component of **TabContent**?

A: You can use **onVisibleAreaChange** to listen to the display or disappearance of a child component on the screen. When the ratio of the component's visible area to its total area increases, it indicates that the child component appears. When the ratio decreases, it indicates that the child component disappears. The sample code is as follows:

@Component
struct MonitorTabContent {
  build() {
    Column() {
      Tabs() {
        TabContent() {
          ChildrenComponent1();
        }
        // ...
      }
      .height('60%')
      .barMode(BarMode.Fixed)
      .backgroundColor(0xf1f3f5)
    }
    .width('100%')
    .height(500)
    .padding(24)
  }
}

@Component
struct ChildrenComponent1 {
  build() {
    Column() {
      Text('Tab 1 Content')
    }
    .onVisibleAreaChange(\[0, 1\], (isExpanding, currentRatio) => {
      if(isExpanding && currentRatio > 0) {
        console.log('Tab 1 Appear');
      } else if(!isExpanding && currentRatio === 0) {
        console.log('Tab 1 Disappear');
      }
    })
  }
}
