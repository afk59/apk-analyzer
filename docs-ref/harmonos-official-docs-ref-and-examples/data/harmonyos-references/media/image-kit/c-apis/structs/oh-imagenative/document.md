# OH\_ImageNative

typedef struct OH\_ImageNative OH\_ImageNative

#### Overview

The struct describes the alias for an image object at the native layer.

The struct cannot be directly operated. Instead, its fields must be operated by calling functions. The table below describes the content and operation mode of the OH\_ImageNative struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| Image\_Size | imageSize | Image size. | [OH\_ImageNative\_GetImageSize](../../header-files/image-native-h/document.md#oh_imagenative_getimagesize) | Obtains the image size of an OH\_ImageNative object. |
| uint32\_t | types | Component type, which is used to describe the image's color component. | [OH\_ImageNative\_GetComponentTypes](../../header-files/image-native-h/document.md#oh_imagenative_getcomponenttypes) | Obtains the component types of an OH\_ImageNative object. |
| OH\_NativeBuffer | nativeBuffer | Component buffer. | [OH\_ImageNative\_GetByteBuffer](../../header-files/image-native-h/document.md#oh_imagenative_getbytebuffer) | Obtains the buffer corresponding to a component type in an OH\_ImageNative object. |
| size\_t | bufferSize | Buffer size. | [OH\_ImageNative\_GetBufferSize](../../header-files/image-native-h/document.md#oh_imagenative_getbuffersize) | Obtains the size of the buffer corresponding to a component type in an OH\_ImageNative object. |
| int32\_t | rowStride | Row stride. | [OH\_ImageNative\_GetRowStride](../../header-files/image-native-h/document.md#oh_imagenative_getrowstride) | Obtains the row stride corresponding to a component type in an OH\_ImageNative object. |
| int32\_t | pixelStride | Pixel stride. | [OH\_ImageNative\_GetPixelStride](../../header-files/image-native-h/document.md#oh_imagenative_getpixelstride) | Obtains the pixel stride corresponding to a component type in an OH\_ImageNative object. |

To release an OH\_ImageNative object, call [OH\_ImageNative\_Release](../../header-files/image-native-h/document.md#oh_imagenative_release).

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_native.h](../../header-files/image-native-h/document.md)
