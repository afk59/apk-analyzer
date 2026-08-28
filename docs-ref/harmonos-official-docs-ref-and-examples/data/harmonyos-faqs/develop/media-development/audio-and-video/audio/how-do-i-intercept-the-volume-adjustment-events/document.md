# How do I intercept the volume adjustment events?

**Question**

How do I intercept the volume adjustment events to implement specific service features such as page turning through volume keys in reading scenarios?

**Solution**

You can [subscribe to system key press events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputconsumer#inputconsumeronkeypressed16) to intercept the system volume key events of the mobile phone, and insert your own service logic (such as camera shooting and page turning). The sample code is as follows:

import { inputConsumer, KeyEvent } from '@kit.InputKit';
import { KeyCode } from '@kit.InputKit';

@Entry
@Component
struct TestDemo14 {
  private volumeUpCallBackFunc: (event: KeyEvent) => void = () => {
  }
  private volumeDownCallBackFunc: (event: KeyEvent) => void = () => {
  }

  aboutToAppear(): void {
    try {
      let options1: inputConsumer.KeyPressedConfig = {
        key: KeyCode.KEYCODE\_VOLUME\_UP,
        action: 1, // The value 1 indicates a key press.
        isRepeat: false, // Key events are consumed preferentially and not reported.
      }
      let options2: inputConsumer.KeyPressedConfig = {
        key: KeyCode.KEYCODE\_VOLUME\_DOWN,
        action: 1, // The value 1 indicates a key press.
        isRepeat: false, // Key events are consumed preferentially and not reported.
      }

      // Callback invoked when the Volume Up button is pressed
      this.volumeUpCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: 'The Volume Up button was pressed.' });
        // do something
      }

      // Callback invoked when the Volume Down button is pressed
      this.volumeDownCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: 'The Volume Down button was pressed.' });
        // do something
      }
      // Register an event listener.
      inputConsumer.on('keyPressed', options1, this.volumeUpCallBackFunc);
      inputConsumer.on('keyPressed', options2, this.volumeDownCallBackFunc);
    } catch (error) {
      console.error(\`Subscribe execute failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
    }
  }

  build() {
    Column() {
      Row() {
        Button ('Cancel listening for Volume Up button events')
          .onClick(() => {
            try {
              // Cancel the callback.
              inputConsumer.off('keyPressed', this.volumeUpCallBackFunc);
              this.getUIContext().getPromptAction().showToast({ message: ''Listening for Volume Up button events is canceled successfully.' });
            } catch (error) {
              console.error(\`Unsubscribe execute failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 50 })

      Row() {
        Button ('Cancel listening for Volume Down button events')
          .onClick(() => {
            try {
              // Cancel the callback.
              inputConsumer.off('keyPressed', this.volumeDownCallBackFunc);
              this.getUIContext().getPromptAction().showToast({ message: ''Listening for Volume Down button events is canceled successfully.' });
            } catch (error) {
              console.error(\`Unsubscribe execute failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 50 })
      Row(){
        Text ('Listening for Volume Up and Volume Down button events is enabled by default.')
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }.width('100%').height('100%')
  }
}
