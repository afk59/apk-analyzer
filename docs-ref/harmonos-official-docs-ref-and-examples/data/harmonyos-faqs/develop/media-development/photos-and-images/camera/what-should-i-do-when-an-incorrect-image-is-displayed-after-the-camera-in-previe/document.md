# What should I do when an incorrect image is displayed after the camera in preview mode is switched to the background and then switched back?

After the switching from the background to the foreground, you must re-initialize the camera. After the application is switched to the background, all camera resources are reclaimed.

**Reference**

[Practices for Camera Recovery from the Background (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-background-recovery)
