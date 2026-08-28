# How do I switch between the custom keyboard and the system keyboard?

To switch between a custom keyboard and the system keyboard, you can dynamically control the **customKeyboard** property based on a state variable. The sample code is as follows:

@Component
export struct CustomSystemKeyboardToggle {
  controller: TextInputController = new TextInputController();
  @State inputValue: string = '';
  @State show: boolean = false;

  // Customize keyboard components
  @Builder
  customKeyboardBuilder() {
    Column() {
      Button('x')
        .onClick(() => {
          // Turn off custom keyboard
          this.controller.stopEditing();
          this.show = !this.show;
        })
      Grid() {
        ForEach(\[1, 2, 3, 4, 5, 6, 7, 8, 9, '\*', 0, '#'\], (item: number | string) => {
          GridItem() {
            Button(item + '')
              .width(110)
              .onClick(() => {
                this.inputValue += item;
              })
          }
        })
      }
      .maxCount(3)
      .columnsGap(10)
      .rowsGap(10)
      .padding(5)
    }
    .backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      TextInput({ controller: this.controller, text: this.inputValue })// Bind custom keyboard
        .customKeyboard(this.show ? this.customKeyboardBuilder() : undefined)
        .margin(10)
        .height(48)
      Button('switch')
        .onClick(() => {
          this.show = !this.show;
        })
    }
  }
}
