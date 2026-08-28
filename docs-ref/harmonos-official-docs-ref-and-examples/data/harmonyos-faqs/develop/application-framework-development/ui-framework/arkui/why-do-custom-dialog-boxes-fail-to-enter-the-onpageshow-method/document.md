# Why do custom dialog boxes fail to enter the onPageShow method?

Custom dialog boxes, as a type of custom component, have their own lifecycle callbacks: **aboutToAppear** and **aboutToDisappear**.

**onPageShow** and **onPageHide** are lifecycle callbacks for pages – custom components decorated with @Entry, and do not apply to custom dialog boxes.

**Reference**

[Custom Component Lifecycle](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-page-custom-components-lifecycle)
