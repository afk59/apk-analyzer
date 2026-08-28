# How do I bind different custom keyboards to different text boxes?

1.  Define a controller for each text box.
    
    private controller: TextInputController = new TextInputController();
    private controller1: TextInputController = new TextInputController();
    
2.  Create a custom keyboard component.
    
    // Customize keyboard components
    @Component
    export struct CustomKeyboardBuilder {
      controller?: TextInputController = new TextInputController();
      index: number = 0;
      @Link inputValue: string
    
      build() {
        Column() {
          // ...
        }
      }
    }
    
3.  Add the **customKeyboard** attribute to the **TextInput** component to bind the custom keyboard.
    
    TextInput({ controller: this.controller, text: this.inputValue })// Bind custom keyboard
      .customKeyboard(this.CustomKeyboardBuilder()).margin(10).border({ width: 1 }).height('48vp')
    
    The code snippet is as follows:
    
    @Entry
    @Component
    struct TextInputExample {
      controller: TextInputController = new TextInputController();
      @State inputValue: string = '';
      controller1: TextInputController = new TextInputController();
      @State inputValue1: string = '';
      controller2: TextInputController = new TextInputController();
      @State inputValue2: string = '';
    
    
      build() {
        Column() {
          this.input({ inputValue: this.inputValue, controller: this.controller, index: 0 });
          this.input({ inputValue: this.inputValue1, controller: this.controller1, index: 1 });
          this.input({ inputValue: this.inputValue2, controller: this.controller2, index: 2 });
        }
      }
    
    
      @Builder
      input(tmp: Tmp) {
        if (tmp.index === 0) {
          TextInput({ controller: tmp.controller, text: tmp.inputValue })
            .customKeyboard(this.keyboard())
            .margin(10)
            .border({ width: 1 })
            .height('48vp')
        } else if (tmp.index === 1) {
          TextInput({ controller: tmp.controller, text: tmp.inputValue })
            .customKeyboard(this.keyboard1())
            .margin(10)
            .border({ width: 1 })
            .height('48vp')
        } else {
          TextInput({ controller: tmp.controller, text: tmp.inputValue })
            .customKeyboard(this.keyboard2())
            .margin(10)
            .border({ width: 1 })
            .height('48vp')
        }
      }
    
    
      @Builder
      keyboard() {
        CustomKeyboardBuilder({ inputValue: this.inputValue, controller: this.controller, index: 0 });
      }
    
    
      @Builder
      keyboard1() {
        CustomKeyboardBuilder({ inputValue: this.inputValue1, controller: this.controller1, index: 1 });
      }
    
    
      @Builder
      keyboard2() {
        CustomKeyboardBuilder({ inputValue: this.inputValue2, controller: this.controller2, index: 2 });
      }
    }
    
    
    class Tmp {
      inputValue?: string;
      controller?: TextInputController;
      index?: number;
    }
    
    
    // Customize keyboard components
    @Component
    export struct CustomKeyboardBuilder {
      controller?: TextInputController = new TextInputController();
      index: number = 0;
      @Link inputValue: string;
    
    
      build() {
        Column() {
          Button('x').onClick(() => {
            // Turn off custom keyboard
            this.controller?.stopEditing();
          })
          Grid() {
            ForEach(\[1, 2, 3, 4, 5, 6, 7, 8, 9, '\*', 0, '#'\], (item: number | string) => {
              GridItem() {
                Button(item + '')
                  .backgroundColor(this.index === 0 ? Color.Blue :
                    (this.index === 1 ? Color.Green : Color.Red))
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
    }
