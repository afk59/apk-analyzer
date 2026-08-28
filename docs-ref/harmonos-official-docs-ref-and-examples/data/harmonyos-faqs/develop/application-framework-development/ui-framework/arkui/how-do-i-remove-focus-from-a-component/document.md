# How do I remove focus from a component?

When a component is in the focused state, setting its **focusable** or **enabled** attribute to **false** will automatically removes focus from the component. The focus will then move to another component according to the [focus traversal rules](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#focus-traversal-guidelines). The code snippet is as follows:

@Entry
@Component
struct ClearComponentFocus {
  // Whether textInput is focus
  @State textFocusable: boolean = true;
  @State text: string = 'Gain focus';

  build() {
    Column() {
      TextInput({ text: this.text })
        .focusable(this.textFocusable)
        .onFocus(() => {
          this.text = 'Gain focus';
        })
        .onBlur(() => {
          this.text = 'Lost Focus';
        })
      Button('Button1')
        .width(160)
        .height(70)
        .margin({ top: 20 })
        .onClick(() => {
          this.textFocusable = !this.textFocusable;
        })
    }
    .width('100%')
    .height('100%')
  }
}

**Reference**

[Setting Whether a Component Is Focusable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#setting-whether-a-component-is-focusable)
