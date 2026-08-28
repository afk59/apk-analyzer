# What should I do if vp2px and px2vp return incorrect results?

1.  [vp2px](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#vp2px12) and [px2vp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12) are global APIs of ArkUI. These APIs have been marked as deprecated and are not recommended. During application startup or when they are called by non-UI threads, the UI instance is unclear, and the virtual pixel ratio of the default screen is used for conversion. As a result, the conversion result is not as expected.
2.  [vp2px](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#vp2px12) and [px2vp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12) of **UIContext** are recommended as the alternative APIs. They ensure that the UI instance is created before being called and return correct results.

**Reference**

[Pixel Units](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-pixel-units)
