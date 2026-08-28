# Camera\_Rect

typedef struct Camera\_Rect {...} Camera\_Rect

#### Overview

The struct describes a rectangle. The coordinate system for the returned detection points is based on the landscape device orientation, with the charging port on the right. In this coordinate system, the top-left corner is (0, 0), and the bottom-right corner is (1, 1). Here, **topLeftX** and **topLeftY** represent the coordinates of the top-left corner of the rectangle, whereas **width** and **height** represent the width and height of the rectangle, respectively. When cropping or selecting a face region based on specific requirements, the x and y coordinates of the rectangle must be multiplied by the width and height of the actual camera preview output stream to obtain the cropped face region.

The width and height of the actual preview stream refer to the resolution of the camera output stream. For details, see **size** in [profile](../../../arkts-apis/ohos-multimedia-camera-camera-management/interfaces-others/document.md#profile).

For details about how to obtain the preview stream data, see [Secondary Processing of Preview Streams (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-preview-imagereceiver).

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t topLeftX | X coordinate of the top-left corner of the rectangle, in the range of \[0, 1\]. |
| int32\_t topLeftY | Y coordinate of the top-left corner of the rectangle, in the range of \[0, 1\]. |
| int32\_t width | Width of the rectangle, in the range of \[0, 1\]. |
| int32\_t height | Height of the rectangle, in the range of \[0, 1\]. |
