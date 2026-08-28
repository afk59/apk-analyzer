# How do I clear the focus in a text box?

You can use the [clearFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12) method of **FocusController** to clear the focus and close the soft keyboard. The sample code is as follows:

this.getUIContext().getFocusController().clearFocus()
