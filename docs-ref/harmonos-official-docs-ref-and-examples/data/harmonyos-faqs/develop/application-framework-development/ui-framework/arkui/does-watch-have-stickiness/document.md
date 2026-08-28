# Does @Watch have stickiness?

No. The callback function bound by @Watch is triggered only when the value of the state variable changes. The callback is not triggered during initialization.

**Reference**

[@Watch Decorator: Getting Notified of State Variable Changes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-watch)
