# How does the TextInput component obtain focus?

-   Scenario 1: [Active Focus Acquisition/Loss](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#active-focus-acquisitionloss) of **TextInput**.
    
    Call the **focusControl.requestFocus** API to actively move the focus to the specified component. The code snippet is as follows:
    
    // xxx.ets
    @Entry
    @Component
    struct TextInputExample {
      build() {
        Row() {
          Column() {
            Button('The second focus acquisition')
              .onClick(() => {
                focusControl.requestFocus('BBB'); // Get focus on the second input box
              })
    
    
            TextInput({ placeholder: 'Please enter the content.' })
              .showUnderline(true)
              .width(380)
              .height(60)
              .id('AAA')
            TextInput({ placeholder: 'Please enter the content.' })
              .showUnderline(true)
              .width(380)
              .height(60)
              .id('BBB')
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   Scenario 2: When the page is initially constructed, the **TextInput** component configured as the [default focus](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#default-focus) obtains focus.
    
    Set the **defaultFocus** attribute to configure the bound component as the default focus when the page is created. The code snippet is as follows:
    
    // xxx.ets
    @Entry
    @Component
    struct TextInputExample {
      build() {
        Row() {
          Column() {
            TextInput({ placeholder: 'Please enter the content.' })
              .showUnderline(true)
              .width(380)
              .height(60)
    
    
            TextInput({ placeholder: 'Please enter the content.' })
              .showUnderline(true)
              .defaultFocus(true) // When the page is first opened, this TextInput gets focus
              .width(380)
              .height(60)
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   Scenario 3: When the page is initially constructed, the **TextInput** component configured as the default focus obtains focus, without bringing up the keyboard.
    
    Set **enableKeyboardOnFocus(false)**, so that the keyboard does not pop up when the **TextInput** component obtains focus. The code snippet is as follows:
    
    // xxx.ets
    @Entry
    @Component
    struct TextInputExample {
      build() {
        Row() {
          Column() {
            TextInput({ placeholder: 'Please enter the content.' })
              .defaultFocus(true) // When the page is first opened, this TextInput gets focus
              .enableKeyboardOnFocus(false) // Is TextInput bound to an input method when focusing through methods other than clicking.
              .placeholderColor(Color.Grey)
              .placeholderFont({ size: 14, weight: 400 })
              .caretColor(Color.Blue)
              .width('95%')
              .height(40)
              .margin(20)
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   Scenario 4: When the page is initially constructed, the **TextInput** component not configured as the default focus does not obtain focus or brings up the keyboard, which is the default behavior of the **TextInput** component.
    
    The code snippet is as follows:
    
    // xxx.ets
    @Entry
    @Component
    struct TextInputExample {
      build() {
        Column() {
          TextInput({ placeholder: 'Please enter the content.' })
        }
        .width('100%')
      }
    }
