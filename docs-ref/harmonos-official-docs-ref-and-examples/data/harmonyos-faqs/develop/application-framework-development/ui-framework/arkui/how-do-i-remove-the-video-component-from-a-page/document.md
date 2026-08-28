# How do I remove the Video component from a page?

**Symptom**

When **ForEach** is used to refresh the UI, the **Video** component in the array is removed, while the previous **Video** component still occupies the screen.

**Solution**

You can call the [exitFullscreen()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video#exitfullscreen) method to exit full-screen playing before removing the **Video** component. Only in this way can the **Video** component be removed.

**Reference**

[Video](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video)
