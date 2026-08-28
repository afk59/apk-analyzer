# Setting Input Method Subtypes

The input method subtypes allow the input method to switch to a specific mode or language, for example, the Chinese or English keyboard.

#### Configuring and Implementing an Input Method Subtype

1.  Implement an **InputMethodExtensionAbility** instance for an input method, which will be shared by all subtypes of the input method. Add **metadata** with the name **ohos.extension.input\_method** to the [module.json5](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file to configure resource information for all subtypes.
    
    "extensionAbilities": \[
      {
        "srcEntry": "./ets/InputMethodExtensionAbility/InputMethodService.ets",
        "name": "InputMethodService",
        "label": "$string:MainAbility\_label",
        "description": "$string:extension\_ability\_descriptor",
        "type": "inputMethod",
        "exported": true,
        "metadata": \[
          {
            "name": "ohos.extension.input\_method",
            "resource": "$profile:input\_method\_config"
          }
        \]
      }
    \],
    
2.  Configure the subtype information based on the configuration file format and fields, and place the subtype configuration file input\_method\_config.json in the **profile** folder under the application's resource directory. For details about the fields, see [InputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype). For details about how to configure the **locale** field, see [i18n-locale-culture](../../localization-kit/application-internationalization/locale-id-and-cultural-habit-division/document.md#how-it-works).
    
    {
      "subtypes": \[
        {
          "icon": "$media:icon",
          "id": "InputMethodExtAbility",
          "label": "$string:english",
          "locale": "en-US",
          "mode": "lower"
        },
        {
          "icon": "$media:icon",
          "id": "InputMethodExtAbility1",
          "label": "$string:chinese",
          "locale": "zh-CN",
          "mode": "lower"
        }
      \]
    }
    
3.  Register a listener in the input method application for subtype changes, so as to load a subtype-specific soft keyboard UI. You can also use a state variable to change the soft keyboard layout.
    
    // Register a listener in the input method application for subtype changes.
    inputMethodAbility.on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
      if (inputMethodSubtype.id === 'InputMethodExtAbility') {
        AppStorage.setOrCreate('subtypeChange', 0);
      }
      if (inputMethodSubtype.id === 'InputMethodExtAbility1') {
        AppStorage.setOrCreate('subtypeChange', 1);
      }
    });
    \`\`
    

#### Obtaining Information About Input Method Subtypes

1.  To obtain the current subtype of the current input method, call [getCurrentInputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodgetcurrentinputmethodsubtype9).
    
2.  To obtain all subtypes of the current input method, call [listCurrentInputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#listcurrentinputmethodsubtype9).
    
3.  To obtain all subtypes of a specified input method, call [listInputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#listinputmethodsubtype9).
    

#### Switching Between Input Method Subtypes

1.  To switch to another subtype of the current input method, call [switchCurrentInputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodswitchcurrentinputmethodsubtype9).
    
2.  To switch to a specified subtype of a specified input method, call [switchCurrentInputMethodAndSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod#inputmethodswitchcurrentinputmethodandsubtype9).
