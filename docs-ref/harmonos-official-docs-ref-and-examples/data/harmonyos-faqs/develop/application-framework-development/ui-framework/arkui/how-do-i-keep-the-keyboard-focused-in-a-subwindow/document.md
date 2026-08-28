# How do I keep the keyboard focused in a subwindow?

**Solution**

You can use the [keepKeyboardOnFocus](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#keepkeyboardonfocus11 >) API of the window to keep the soft keyboard created by others when a window has focus. This API takes effect only for a system window or an application subwindow. Before calling this API, ensure that the window has been focused. This API is valid only when the soft keyboard is created by another window.
