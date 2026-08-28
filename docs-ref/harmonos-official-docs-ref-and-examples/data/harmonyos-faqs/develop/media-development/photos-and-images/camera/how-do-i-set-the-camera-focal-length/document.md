# How do I set the camera focal length?

1.  Check whether the camera is a front camera. A front camera does not support focal length setting.
2.  Use **getZoomRatioRange** to obtain the focal length range supported by the device.
3.  Check whether the target focal length is within the range obtained. If yes, call **setZoomRatio** to set the focal length.

**Reference**

[getZoomRatioRange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-zoomquery#getzoomratiorange11), [setZoomRatio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-zoom#setzoomratio11)
