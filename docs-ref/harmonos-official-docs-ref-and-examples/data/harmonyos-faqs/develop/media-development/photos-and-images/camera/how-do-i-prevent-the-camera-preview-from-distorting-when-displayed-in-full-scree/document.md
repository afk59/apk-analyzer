# How do I prevent the camera preview from distorting when displayed in full screen?

You need to obtain the aspect ratio of the phone by dividing the screen's width by height, and compare it with the width-to-height ratio of the supported preview sizes to get the closest value. The preview stream and video output stream must have the same aspect ratio of the resolution. For example, the aspect ratio is 1920:1080 (which is equal to 16:9), then the aspect ratio of the resolution of the preview stream must also be 16:9. This means that the resolution can be 640:360, 960:540, 1920:1080, or the like.

**Reference**

[Camera Preview (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-preview)
