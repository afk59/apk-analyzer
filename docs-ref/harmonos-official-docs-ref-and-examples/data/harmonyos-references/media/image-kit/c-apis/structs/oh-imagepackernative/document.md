# OH\_ImagePackerNative

typedef struct OH\_ImagePackerNative OH\_ImagePackerNative

#### Overview

The struct describes the image packer, which is used to perform operations related to an image packer.

The struct cannot be directly operated. Instead, its fields must be operated by calling functions. The table below describes the content and operation mode of the OH\_ImageNative struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| OH\_ImageSourceNative | imageSource | Image source. | [OH\_ImagePackerNative\_PackToDataFromImageSource](../../header-files/image-packer-native-h/document.md#oh_imagepackernative_packtodatafromimagesource) | Encodes an image source into data in a given format. |
| OH\_PixelmapNative | pixelmap | PixelMap at the native layer. | [OH\_ImagePackerNative\_PackToDataFromPixelmap](../../header-files/image-packer-native-h/document.md#oh_imagepackernative_packtodatafrompixelmap) | Encodes a PixelMap into data in a given format. |
| int32\_t | imagesourceFd | File descriptor of an image source. | [OH\_ImagePackerNative\_PackToFileFromImageSource](../../header-files/image-packer-native-h/document.md#oh_imagepackernative_packtofilefromimagesource) | Encodes an image source into a file. |
| int32\_t | pixelmapFd | File descriptor of a PixelMap. | [OH\_ImagePackerNative\_PackToFileFromPixelmap](../../header-files/image-packer-native-h/document.md#oh_imagepackernative_packtofilefrompixelmap) | Encodes a PixelMap into a file. |

To create an OH\_ImagePackerNative object, call [OH\_ImagePackerNative\_Create](../../header-files/image-packer-native-h/document.md#oh_imagepackernative_create).

To release an OH\_ImagePackerNative object, call [OH\_ImagePackerNative\_Release](../../header-files/image-packer-native-h/document.md#oh_imagepackernative_release).

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_packer\_native.h](../../header-files/image-packer-native-h/document.md)
