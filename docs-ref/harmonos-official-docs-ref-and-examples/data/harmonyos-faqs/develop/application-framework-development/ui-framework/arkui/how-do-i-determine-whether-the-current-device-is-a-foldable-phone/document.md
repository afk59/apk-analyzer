# How do I determine whether the current device is a foldable phone?

-   Screen layout issues:
    
    The screen layout should be determined by dynamic attributes such as window form (the folded or unfolded state), width, and aspect ratio instead of static device types. For example, the window in the folded state of a foldable device should use the same layout rules as those of a common phone, while a separate layout should be designed for the unfolded state of the Mate X5. For details, see [Breakpoints](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-responsive-layout#section1532120147301).
    
-   Non-screen layout or feature issues (for example, when a device switched between the folded and unfolded states, the camera need to be reselected to reset the preview stream):
    
    The [DeviceTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-device-info#devicetypes20) API of mobile phones (including common mobile phones and foldable phones) returns **phone**. You can use [display.isFoldable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#displayisfoldable10) of the screen attribute @ohos.display to check whether it is a foldable phone. Note that the **isFoldable** API of HUAWEI Pocket 2 (vertical foldable phone) returns **false**, which requires special processing.
    

For details about foldable device development, see [Foldable Device Application Development](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-foldable-guide).
