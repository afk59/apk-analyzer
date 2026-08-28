# Immersive Mode of the Input Method Application

#### When to Use

To implement consistent immersive experience, a communication mechanism between foreground applications and input method applications is provided. You can set the immersive input mode based on the immersive mode of the foreground application.

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/INAsYPaJQzWo7vHrEnkmZw/en-us_image_0000002568764797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43C0C1458EB17A16835053E83AA825E254ADB37677DA4188A0CD2179A8E6BEC1)

-   The foreground application sets the desired immersive mode based on the application scenario.
-   The desired immersive mode of the foreground application is then passed to the input method application through the input method framework.
-   The input method application determines the final immersive mode for the input method framework based on the immersive mode of the foreground application.

#### Access Guide

1.  The foreground application [sets the immersive mode for the text box](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea#keyboardappearance15). The sample code is as follows:
    
    TextArea({placeholder: 'Immersive mode'})
      .keyboardAppearance(KeyboardAppearance.IMMERSIVE)
    
    TextArea({placeholder: 'Non-immersive mode'})
      .keyboardAppearance(KeyboardAppearance.NONE\_IMMERSIVE)
    
2.  The input method application [subscribes to the text box attribute change event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethodengine#oneditorattributechanged10) and detects the immersive mode desired by the foreground application through the **immersiveMode** field in the **EditorAttribute** callback. The sample code is as follows:
    
    // Check whether the immersive mode is used. If the immersive mode is used, select the immersive mode.
    inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
      console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
      if (attr.immersiveMode == 1) {
        this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK\_IMMERSIVE);
        console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
      }
    })
    
3.  The input method application [sets the immersive mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethodengine#setimmersivemode15).
    
    -   The **IMMERSIVE** mode is determined by the input method application.
    -   The input method application cannot set the **IMMERSIVE** mode to the input method framework.
    -   If the input method application receives **IMMERSIVE** from the foreground application, it is recommended that the input method application set the final immersive mode to **LIGHT\_IMMERSIVE** or **DARK\_IMMERSIVE** based on the current system color mode.
    
    The following sample code shows how to set the immersive mode. You must first use [createPanel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethodengine#createpanel10) to obtain a panel instance, and then call the **setImmersiveMode** API using the obtained instance.
    
    // Check whether the immersive mode is used. If the immersive mode is used, select the immersive mode.
    inputMethodEngine.getKeyboardDelegate().on("editorAttributeChanged", (attr : inputMethodEngine.EditorAttribute) => {
      console.info('recv editorAttributeChanged, immersiveMode: ', attr.immersiveMode);
      if (attr.immersiveMode == 1) {
        this.panel?.setImmersiveMode(inputMethodEngine.ImmersiveMode.DARK\_IMMERSIVE);
        console.info('recv editorAttributeChanged, panel:', this.panel?.getImmersiveMode());
      }
    })
