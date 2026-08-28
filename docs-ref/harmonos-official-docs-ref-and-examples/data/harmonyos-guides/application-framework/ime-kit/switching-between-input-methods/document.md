# Switching Between Input Methods

You can use the APIs of the input method framework service to easily switch between input methods and input method subtypes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/90PtXyylT2WKuEXwA2Re2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F73648E96F963A7FC2F932CDC9EE8D8B09268BE92AAF2D0326B5829EFEBD7EE)

1.  The following APIs can be called only in the current input method application.
    
2.  This example assumes that an input method application has been executed. For details about how to implement an input method application, see [Implementing an Input Method Application](../implementing-an-input-method-application/document.md).
    

#### Switching Between Input Method Subtypes

1.  In the input method application in use, call [switchCurrentInputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodswitchcurrentinputmethodsubtype9) with the target [InputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) to switch to another subtype of the current input method.
    
    async switchCurrentInputMethodSubtype(item: InputMethodSubtype) {
      try {
        await inputMethod.switchCurrentInputMethodSubtype(item);
        this.currentInputMethodSubtype = inputMethod.getCurrentInputMethodSubtype().id;
      } catch (err) {
        console.error(\`SwitchCurrentInputMethodSubtype error: ${err.code} ${err.message}\`);
        let error: BusinessError = err as BusinessError;
      }
    }
    
2.  Register a listener in the input method application for subtype changes, so as to load a subtype-specific soft keyboard UI.
    
    // Register a listener in the input method application for subtype changes.
    inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
      if (inputMethodSubtype.id === 'InputMethodExtAbility') {
        AppStorage.setOrCreate('subtypeChange', 0);
      }
      if (inputMethodSubtype.id === 'InputMethodExtAbility1') {
        AppStorage.setOrCreate('subtypeChange', 1);
      }
    });
    

#### Switching Between Input Methods

In the input method application in use, call [switchInputMethod](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodswitchinputmethod9) with the target [InputMethodProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodproperty8) to switch to another input method.

async switchInputMethod(item: string) {
  try {
    this.inputMethods = await inputMethod.getSetting().getInputMethods(true); // Obtain the list of enabled input methods.
    let currentInputMethod = inputMethod.getCurrentInputMethod(); // Obtain the current input method.
    for (let i = 0; i < this.inputMethods.length; i++) {
      if (item != currentInputMethod.name) { // If the current input method is not the specified one, switch to the specified one. You can switch to a fixed input method as required.
        await inputMethod.switchInputMethod(this.inputMethods\[i\]);
      }
    }
  } catch (err) {
    let error = err as BusinessError;
    Log.showError(TAG, \`switchInputMethod catch error: ${error.code} ${error.message}\`);
  }
}

#### Switching Between Input Methods and Subtypes

In the input method application in use, call [switchCurrentInputMethodAndSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodswitchcurrentinputmethodandsubtype9) with the target [InputMethodProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodproperty8) and [InputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) to switch to the specified subtype of another input method.

import { inputMethod } from '@kit.IMEKit';

export class KeyboardController {
  async switchInputMethodAndSubtype() {
    try {
      let inputMethods: Array<inputMethod.InputMethodProperty> =
        await inputMethod.getSetting().getInputMethods(true); // Obtain the list of enabled input methods.
      let currentInputMethod: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod(); // Obtain the current input method.
      for (let i = 0; i < inputMethods.length; i++) {
        if (inputMethods\[i\].name != currentInputMethod.name) { // If the current input method is not the specified one, switch to the specified one. You can enter a fixed input method as required.
          let subTypes = await inputMethod.getSetting().listInputMethodSubtype(inputMethods\[i\]); // Obtain the subtypes of the target input method.
          if (subTypes.length > 0) {
            await inputMethod.switchCurrentInputMethodAndSubtype(inputMethods\[i\], subTypes\[0\]); // This example switches to the first obtained subtype.
          }
          return;
        }
      }
    } catch (err) {
      let error: BusinessError = err as BusinessError;
      console.error(\`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}\`);
    }
  }
}
