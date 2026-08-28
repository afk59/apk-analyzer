# OH\_PackingOptions

typedef struct OH\_PackingOptions OH\_PackingOptions

#### Overview

OH\_PackingOptions is an image encoding option struct encapsulated at the native layer. It cannot be manipulated directly; instead, functions shall be called to create and release the struct, and operate on its specific fields.

To create an OH\_PackingOptions object, call [OH\_PackingOptions\_Create](../../header-files/image-packer-native-h/document.md#oh_packingoptions_create).

To release an OH\_PackingOptions object, call [OH\_PackingOptions\_Release](../../header-files/image-packer-native-h/document.md#oh_packingoptions_release).

The table below describes the content and operation mode of the OH\_PackingOptions struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| Image\_MimeType | mimeType | MIME type. | [OH\_PackingOptions\_GetMimeType](../../header-files/image-packer-native-h/document.md#oh_packingoptions_getmimetype) | Obtains the MIME type. |
| Image\_MimeType | mimeType | MIME type. | [OH\_PackingOptions\_SetMimeType](../../header-files/image-packer-native-h/document.md#oh_packingoptions_setmimetype) | Sets the MIME type. |
| uint32\_t | quality | Encoding quality. | [OH\_PackingOptions\_GetQuality](../../header-files/image-packer-native-h/document.md#oh_packingoptions_getquality) | Obtains the encoding quality. |
| uint32\_t | quality | Encoding quality. | [OH\_PackingOptions\_SetQuality](../../header-files/image-packer-native-h/document.md#oh_packingoptions_setquality) | Sets the encoding quality. |
| int32\_t | desiredDynamicRange | Desired dynamic range. | [OH\_PackingOptions\_GetDesiredDynamicRange](../../header-files/image-packer-native-h/document.md#oh_packingoptions_getdesireddynamicrange) | Obtains the desired dynamic range during encoding. |
| int32\_t | desiredDynamicRange | Desired dynamic range. | [OH\_PackingOptions\_SetDesiredDynamicRange](../../header-files/image-packer-native-h/document.md#oh_packingoptions_setdesireddynamicrange) | Sets the desired dynamic range during encoding. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_packer\_native.h](../../header-files/image-packer-native-h/document.md)
