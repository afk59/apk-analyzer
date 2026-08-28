# OH\_DecodingOptions

typedef struct OH\_DecodingOptions OH\_DecodingOptions

#### Overview

The OH\_DecodingOptions struct describes the decoding options encapsulated at the native layer. The struct is used to set decoding options and is passed in as an input parameter for creating a PixelMap. For details, see [OH\_ImageSourceNative\_CreatePixelmap](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createpixelmap).

The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct.

To create an OH\_DecodingOptions object, call [OH\_DecodingOptions\_Create](../../header-files/image-source-native-h/document.md#oh_decodingoptions_create).

To release an OH\_DecodingOptions object, call [OH\_DecodingOptions\_Release](../../header-files/image-source-native-h/document.md#oh_decodingoptions_release).

The table below describes the content and operation mode of the OH\_DecodingOptions struct.

| Field Type | Field Name | Field Description | Default Value | Getter Function | Setter Function |
| :-- | :-- | :-- | :-- | :-- | :-- |
| int32\_t | pixelFormat | Pixel format. | RGBA\_8888 | [OH\_DecodingOptions\_GetPixelFormat](../../header-files/image-source-native-h/document.md#oh_decodingoptions_getpixelformat) | [OH\_DecodingOptions\_SetPixelFormat](../../header-files/image-source-native-h/document.md#oh_decodingoptions_setpixelformat) |
| uint32\_t | index | Index of the image to decode. | 0 | [OH\_DecodingOptions\_GetIndex](../../header-files/image-source-native-h/document.md#oh_decodingoptions_getindex) | [OH\_DecodingOptions\_SetIndex](../../header-files/image-source-native-h/document.md#oh_decodingoptions_setindex) |
| float | rotate | Rotation angle. | **0**, in degree (deg). | [OH\_DecodingOptions\_GetRotate](../../header-files/image-source-native-h/document.md#oh_decodingoptions_getrotate) | [OH\_DecodingOptions\_SetRotate](../../header-files/image-source-native-h/document.md#oh_decodingoptions_setrotate) |
| Image\_Size | desiredSize | Desired output size. | Original image size. | [OH\_DecodingOptions\_GetDesiredSize](../../header-files/image-source-native-h/document.md#oh_decodingoptions_getdesiredsize) | [OH\_DecodingOptions\_SetDesiredSize](../../header-files/image-source-native-h/document.md#oh_decodingoptions_setdesiredsize) |
| Image\_Region | desiredRegion | Region to decode. | Entire image. | [OH\_DecodingOptions\_GetDesiredRegion](../../header-files/image-source-native-h/document.md#oh_decodingoptions_getdesiredregion) | [OH\_DecodingOptions\_SetDesiredRegion](../../header-files/image-source-native-h/document.md#oh_decodingoptions_setdesiredregion) |
| int32\_t | desiredDynamicRange | Desired dynamic range. | SDR | [OH\_DecodingOptions\_GetDesiredDynamicRange](../../header-files/image-source-native-h/document.md#oh_decodingoptions_getdesireddynamicrange) | [OH\_DecodingOptions\_SetDesiredDynamicRange](../../header-files/image-source-native-h/document.md#oh_decodingoptions_setdesireddynamicrange) |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_source\_native.h](../../header-files/image-source-native-h/document.md)
