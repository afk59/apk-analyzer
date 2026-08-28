# OhosImageReceiverInfo

struct OhosImageReceiverInfo {...}

#### Overview

The struct describes the information about an image receiver.

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_receiver\_mdk.h](../../header-files/image-receiver-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t width | Default width of the image received by the consumer, in pixels. |
| int32\_t height | Default height of the image received by the consumer, in pixels. |
| int32\_t format | Image format **OHOS\_IMAGE\_FORMAT\_JPEG** created by using the receiver. |
| int32\_t capicity | Maximum number of images that can be cached. This parameter is used only as an expected value. The actual capacity is determined by the device hardware. |
