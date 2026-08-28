# How do I enable the soft keyboard to disappear on touching a button?

Call the **stopInputSession()** API of @kit.IMEKit to hide the soft keyboard. The sample code snippet is as follows:

import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct ClickBlankHideKeyboard {
  build() {
    Column({ space: 12 }) {
      TextInput({ placeholder: 'Please enter your account' })
        .height(40)
      TextInput({ placeholder: 'Please input a password' })
        .height(40)
      Button('log on').width('100%')
        .onClick(() => {
          // Exit text editing mode
          try {
            this.inputRef.blur(); 
            // Close the current input session and hide the soft keyboard.
            inputMethod.getController().stopInputSession();
          } catch (err) {
            console.error('Failed to hide keyboard: ' + err);
          }
        })
    }
  }
}

**Reference**

[@ohos.inputMethod (Input Method Framework)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod)
