# Display Development FAQs

#### What does the FoldDisplayMode value of 5 obtained by calling the on('FoldDisplayModeChange') listening API mean on a tri-fold phone?

**Symptom**

On a tri-fold phone, the value **5** is returned by the [on('foldDisplayModeChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#displayonfolddisplaymodechange10) API to listen for display mode changes, while the returned value of the [getFoldDisplayMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#displaygetfolddisplaymode10) API is not **5**.

**Cause**

1.  What is **FoldDisplayMode=5**?
    
    On a tri-fold phone, when the value of **FoldDisplayMode** is **5**, it indicates that the device is currently in the fully unfolded display mode, that is, the screen is fully unfolded, and the device displays content in the maximum available screen size.
    
2.  Why does the **on('foldDisplayModeChange')** event return **5**?
    
    The **on('foldDisplayModeChange')** API is used to listen for display mode change events in real time. Therefore, it returns all actual display mode values including **5**. When the value **5** is detected, it can be determined that the device is in the fully unfolded display mode.
    
3.  Why does not the **getFoldDisplayMode()** API return **5**?
    
    The **getFoldDisplayMode()** API does not return **5** because it is not bound to the device form to reduce the development cost of multi-device adaptation. You need to use a unified breakpoint management mechanism to adapt to different display mode and use the [One-Time Development for Multi-Device Deployment](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-overview) solution to simplify the development process of layout adaptation.
    

**Suggestions**

For better development efficiency and compatibility, you are advised to use the [One-Time Development for Multi-Device Deployment](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-overview) solution for UI layout adaptation. For details about the tri-fold phone application development, see [Mate XT Triple Foldable Phone](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-matext-guide). This spares you from repeated development, while ensuring the consistency and stability of applications across devices.
