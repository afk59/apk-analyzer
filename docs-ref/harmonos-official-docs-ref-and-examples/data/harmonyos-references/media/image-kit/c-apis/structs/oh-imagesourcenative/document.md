# OH\_ImageSourceNative

struct OH\_ImageSourceNative

#### Overview

The struct describes the image source, which is encapsulated at the native layer and is used to create image data. The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct.

You can create an OH\_ImageSourceNative object in multiple ways, as described below.

| API | Description |
| :-- | :-- |
| [OH\_ImageSourceNative\_CreateFromUri](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createfromuri) | Creates an OH\_ImageSourceNative object based on a URI. |
| [OH\_ImageSourceNative\_CreateFromFd](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createfromfd) | Creates an OH\_ImageSourceNative object based on a file descriptor. |
| [OH\_ImageSourceNative\_CreateFromData](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createfromdata) | Creates an OH\_ImageSourceNative object based on buffer data. |
| [OH\_ImageSourceNative\_CreateFromRawFile](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createfromrawfile) | Creates an OH\_ImageSourceNative object by using the raw file descriptor of an image resource file. |
| [OH\_ImageSourceNative\_CreatePixelmap](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createpixelmap) | Creates an OH\_PixelmapNative object based on decoding options. |
| [OH\_ImageSourceNative\_CreatePixelmapList](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_createpixelmaplist) | Creates an array of OH\_PixelmapNative objects based on decoding options. |

To release an OH\_ImageSourceNative object, call [OH\_ImageSourceNative\_Release](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_release).

The table below describes the content and operation mode of the OH\_ImageSourceNative struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| int32\_t | delayTimeList | Image delay time list. | [OH\_ImageSourceNative\_GetDelayTimeList](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_getdelaytimelist) | Obtains the image delay time list. |
| OH\_ImageSource\_Info | info | Image source information. | [OH\_ImageSourceNative\_GetImageInfo](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_getimageinfo) | Obtains the information about an image with a given index. |
| Image\_String | value | Configuration item. | [OH\_ImageSourceNative\_GetImageProperty](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_getimageproperty) | Obtains the value of an image property. |
| Image\_String | value | Configuration item. | [OH\_ImageSourceNative\_ModifyImageProperty](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_modifyimageproperty) | Modifies the value of an image property. |
| uint32\_t | frameCount | Number of frames. | [OH\_ImageSourceNative\_GetFrameCount](../../header-files/image-source-native-h/document.md#oh_imagesourcenative_getframecount) | Obtains the number of image frames. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_source\_native.h](../../header-files/image-source-native-h/document.md)
