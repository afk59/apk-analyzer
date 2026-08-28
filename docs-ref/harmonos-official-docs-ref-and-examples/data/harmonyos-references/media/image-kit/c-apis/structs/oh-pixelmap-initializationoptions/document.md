# OH\_Pixelmap\_InitializationOptions

struct OH\_Pixelmap\_InitializationOptions

#### Overview

The OH\_Pixelmap\_InitializationOptions struct describes the initialization options encapsulated at the native layer. The struct is used to set the initialization parameters for a PixelMap.

To create an OH\_Pixelmap\_InitializationOptions object, call [OH\_PixelmapInitializationOptions\_Create](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_create).

To release an OH\_Pixelmap\_InitializationOptions object, call [OH\_PixelmapInitializationOptions\_Release](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_release).

The table below describes the content and operation mode of the OH\_Pixelmap\_InitializationOptions struct.

| Field type. | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| uint32\_t | width | Image width. | [OH\_PixelmapInitializationOptions\_GetWidth](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_getwidth) | Obtains the image width. |
| uint32\_t | width | Image width. | [OH\_PixelmapInitializationOptions\_SetWidth](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_setwidth) | Sets the image width. |
| uint32\_t | height | Image height. | [OH\_PixelmapInitializationOptions\_GetHeight](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_getheight) | Obtains the image height. |
| uint32\_t | height | Image height. | [OH\_PixelmapInitializationOptions\_SetHeight](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_setheight) | Sets the image height. |
| int32\_t | pixelFormat | Pixel format. | [OH\_PixelmapInitializationOptions\_GetPixelFormat](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_getpixelformat) | Obtains the pixel format. |
| int32\_t | pixelFormat | Pixel format. | [OH\_PixelmapInitializationOptions\_SetPixelFormat](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_setpixelformat) | Sets the pixel format. |
| int32\_t | alphaType | Alpha type. | [OH\_PixelmapInitializationOptions\_GetAlphaType](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_getalphatype) | Obtains the alpha type. |
| int32\_t | alphaType | Alpha type. | [OH\_PixelmapInitializationOptions\_SetAlphaType](../../header-files/pixelmap-native-h/document.md#oh_pixelmapinitializationoptions_setalphatype) | Sets the alpha type. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [pixelmap\_native.h](../../header-files/pixelmap-native-h/document.md)
