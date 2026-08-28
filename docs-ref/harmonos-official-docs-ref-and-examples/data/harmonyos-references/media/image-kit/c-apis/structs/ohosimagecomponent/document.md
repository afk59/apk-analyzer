# OhosImageComponent

struct OhosImageComponent {...}

#### Overview

The struct describes the information about an image component.

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_mdk.h](../../header-files/image-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t\* byteBuffer | Pointer to the buffer that stores the pixel data. |
| size\_t size | Size of the pixel data in the memory. |
| int32\_t componentType | 
Type of the pixel data.

**1**: OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_Y, luminance information

**2**: OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_U, chrominance component.

**3**: OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_V, chrominance component.

**4**: OHOS\_IMAGE\_COMPONENT\_FORMAT\_JPEG, JPEG format.

 |
| int32\_t rowStride | Row stride of the pixel data. Camera preview stream data must be read based on the stride. For details, see [Secondary Processing of Preview Streams (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-preview-imagereceiver). |
| int32\_t pixelStride | Pixel stride of the pixel data. |
