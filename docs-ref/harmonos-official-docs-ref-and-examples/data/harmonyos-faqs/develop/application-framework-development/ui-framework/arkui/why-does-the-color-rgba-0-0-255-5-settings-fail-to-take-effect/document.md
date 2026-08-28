# Why does the color: 'rgba(0, 0, 255, .5)' settings fail to take effect?

For color values in the RGBA format, the leading zeros must not be omitted. Change **rgba(0, 0, 255, .5)** to **rgba(0, 0, 255, 0.5)** for the settings to take effect.

**Reference**

[ResourceColor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-types#resourcecolor)
