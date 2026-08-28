# OH\_ImageSource\_Info

struct OH\_ImageSource\_Info

#### Overview

The OH\_ImageSource\_Info struct describes the image source information encapsulated at the native layer. The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct.

To create an OH\_ImageSource\_Info object, call [OH\_ImageSourceInfo\_Create](../../header-files/image-source-native-h/document.md#oh_imagesourceinfo_create).

To release an OH\_ImageSource\_Info object, call [OH\_ImageSourceInfo\_Release](../../header-files/image-source-native-h/document.md#oh_imagesourceinfo_release). After this API is called, all properties related to the OH\_ImageSource\_Info struct are released. Therefore, before calling this API, ensure that the relevant properties are no longer needed or that a deep copy of these properties has been completed.

The table below describes the content and operation mode of the OH\_ImageSource\_Info struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| uint32\_t | width | Image width. | [OH\_ImageSourceInfo\_GetWidth](../../header-files/image-source-native-h/document.md#oh_imagesourceinfo_getwidth) | Obtains the image width. |
| uint32\_t | height | Image height. | [OH\_ImageSourceInfo\_GetHeight](../../header-files/image-source-native-h/document.md#oh_imagesourceinfo_getheight) | Obtains the image height. |
| bool | isHdr | Whether the image is an HDR image. | [OH\_ImageSourceInfo\_GetDynamicRange](../../header-files/image-source-native-h/document.md#oh_imagesourceinfo_getdynamicrange) | Obtains the dynamic range of an image. |
| [Image\_MimeType](../image-string/document.md) | mimeType | Pointer to the image MIME type. | [OH\_ImageSourceInfo\_GetMimetype](../../header-files/image-source-native-h/document.md#oh_imagesourceinfo_getmimetype) | Obtains the MIME type of an image. |

**Since**: 13

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_source\_native.h](../../header-files/image-source-native-h/document.md)
