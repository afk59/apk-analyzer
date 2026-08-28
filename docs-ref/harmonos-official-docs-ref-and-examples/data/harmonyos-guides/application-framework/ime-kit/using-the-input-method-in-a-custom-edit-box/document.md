# Using the Input Method in a Custom Edit Box

In the inputmethod framework, use [getController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodgetcontroller9) to obtain the [InputMethodController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodcontroller) instance for binding the input method and listening to various events of the input method application, such as insertion, deletion, selection, and cursor movement. In this way, the input method can be used in the custom edit box, implementing more flexible and free editing operations.

#### How to Develop

1.  In your project in DevEco Studio, create an .ets file and name it the name of the target custom component, for example, **CustomInput**. Define a custom component in the file, and import **inputMethod** from @kit.IMEKit.
    
    import { inputMethod } from '@kit.IMEKit';
    
    @Component
    export struct CustomInput {
      build() {
      }
    }
    
2.  In the component, use the **Text** component to show the text in the custom edit box, and the **inputText** state variable to specify the text to display in the text input box.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { inputMethod } from '@kit.IMEKit';
    import Log from '../model/Log';
    
    const TAG = '\[Submenu\]';
    
    @Component
    export struct CustomInput {
      @State inputText: string = ''; // inputText is the content to be displayed by the Text component.
      private isAttach: boolean = false;
      private inputController: inputMethod.InputMethodController = inputMethod.getController();
    
      build() {
        Text(this.inputText) // Use the Text component to show the text in the custom edit box.
          .fontSize(16)
          .width('100%')
          .lineHeight(40)
          .id('customInput')
          .height(45)
          .border({ color: '#554455', radius: 30, width: 1 })
          .maxLines(1)
          .onBlur(() => {
            this.off();
          })
          .onClick(() => {
            this.attachAndListener(); // Click the component.
          })
      }
    
3.  In the component, obtain an **inputMethodController** instance. When the text is clicked, call the **controller** instance's **attach** method to bind and activate the soft keyboard, and register the input method to listen for text insertion and deletion events. This example only demonstrates insertion and deletion.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { inputMethod } from '@kit.IMEKit';
    import Log from '../model/Log';
    
    const TAG = '\[Submenu\]';
    
    @Component
    export struct CustomInput {
      @State inputText: string = ''; // inputText is the content to be displayed by the Text component.
      private isAttach: boolean = false;
      private inputController: inputMethod.InputMethodController = inputMethod.getController();
    
      build() {
        Text(this.inputText) // Use the Text component to show the text in the custom edit box.
          .fontSize(16)
          .width('100%')
          .lineHeight(40)
          .id('customInput')
          .height(45)
          .border({ color: '#554455', radius: 30, width: 1 })
          .maxLines(1)
          .onBlur(() => {
            this.off();
          })
          .onClick(() => {
            this.attachAndListener(); // Click the component.
          })
      }
      async attachAndListener() { // Bind and set a listener.
        focusControl.requestFocus('customInput');
        try {
          await this.inputController.attach(true, {
            inputAttribute: {
              textInputType: inputMethod.TextInputType.TEXT,
              enterKeyType: inputMethod.EnterKeyType.SEARCH
            }
          });
          if (!this.isAttach) {
            this.inputController.on('insertText', (text) => {
              this.inputText += text;
            })
            this.inputController.on('deleteLeft', (length) => {
              this.inputText = this.inputText.substring(0, this.inputText.length - length);
            })
            this.isAttach = true;
          }
        } catch (err) {
          let error = err as BusinessError;
          Log.showError(TAG, \`attach catch error: ${error.code} ${error.message}\`);
        }
      }
    
      off() {
        this.isAttach = false;
        this.inputController.off('insertText');
        this.inputController.off('deleteLeft');
      }
    }
    
4.  Import the component to the application UI layout. In this example, the **Index.ets** and **CustomInput.ets** files are in the same directory.
    
    CustomInput()
    

#### Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/_FEe3cmHST2HYMnILJFe7A/en-us_image_0000002568684787.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9225902A93B7D89F14683A8AC9FC3E3C6AFC4C1746D43FC02EF2341F931774D)
