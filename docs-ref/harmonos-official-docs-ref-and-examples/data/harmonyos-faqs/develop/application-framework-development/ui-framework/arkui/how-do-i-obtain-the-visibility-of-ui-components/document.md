# How do I obtain the visibility of UI components?

-   Method 1: Use the **if** statement to control the visibility of the component based on a variable. Use the @Watch decorator to listen for changes to the variable and detect the visibility of the component.
-   Method 2: Use the **aboutToAppear()** and **aboutToDisappear()** lifecycle callbacks, which are triggered when the component is about to appear or disappear, respectively.

The code snippet is as follows:

@Component
struct ComponentA {
  aboutToAppear(): void {
    // Perception components are visible and hidden
    console.log('Component A display');
  }

  aboutToDisappear(): void {
    // Perception components are visible and hidden
    console.log('Component A hidden');
  }

  build() {
    Column() {
      Text('Component A').fontSize(16).fontColor(Color.Black);
    }
    .width(100)
    .height(50)
  }
}

@Entry
@Component
struct ComponentB {
  @State @Watch('onCompAShowStatusChange') isShowA: boolean = false;
  onCompAShowStatusChange() {
    // Perception components are visible and hidden
    console.log('Monitor component A:' + \`${this.isShowA ? 'display' : 'hide'}\`);
  }

  build() {
    Column() {
      Button('Switch between visible and hidden').type(ButtonType.Normal).width(100).height(50).onClick(() => {
        this.isShowA = !this.isShowA;
      })
      if (this.isShowA) {
        ComponentA();
      }
    }
  }
}

**Reference**

[@Watch Decorator: Getting Notified of State Variable Changes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-watch), [if/else: Conditional Rendering](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse)
