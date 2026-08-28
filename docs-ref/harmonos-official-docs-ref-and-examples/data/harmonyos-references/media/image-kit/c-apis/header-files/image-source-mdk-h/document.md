# image\_source\_mdk.h

#### Overview

The file declares the APIs used to decode an image source into a PixelMap.

**Library**: libimage\_source\_ndk.z.so

**System capability**: SystemCapability.Multimedia.Image.Core

**File to include**: <multimedia/image\_framework/image\_source\_mdk.h>

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OhosImageRegion](../../structs/ohosimageregion/document.md) | \- | Describes the region of an image source to decode. It is a member variable of [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md). |
| [ImageSourceNative\_](../../structs/imagesourcenative/document.md) | ImageSourceNative | Describes an image source object at the native layer. |
| [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) | \- | Describes the image source options. It is used in [OH\_ImageSource\_CreateFromUri](#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](#oh_imagesource_createfromfd), [OH\_ImageSource\_CreateFromData](#oh_imagesource_createfromdata), and [OH\_ImageSource\_CreateIncremental](#oh_imagesource_createincremental). |
| [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md) | \- | Describes the options for decoding an image source. It is used in [OH\_ImageSource\_CreatePixelMap](#oh_imagesource_createpixelmap) and [OH\_ImageSource\_CreatePixelMapList](#oh_imagesource_createpixelmaplist). |
| [OhosImageSourceInfo](../../structs/ohosimagesourceinfo/document.md) | \- | Describes the image source information, which is obtained by calling [OH\_ImageSource\_GetImageInfo](#oh_imagesource_getimageinfo). |
| [OhosImageSource](../../structs/ohosimagesource/document.md) | \- | Describes the input resource of an image source. Only one type of resource is accepted at a time. The image source is obtained by calling [OH\_ImageSource\_CreateFromUri](#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](#oh_imagesource_createfromfd), or [OH\_ImageSource\_CreateFromData](#oh_imagesource_createfromdata). |
| [OhosImageSourceDelayTimeList](../../structs/ohosimagesourcedelaytimelist/document.md) | \- | Describes the delay time list of an image source. The delay time list is obtained by calling [OH\_ImageSource\_GetDelayTime](#oh_imagesource_getdelaytime). |
| [OhosImageSourceSupportedFormat](../../structs/ohosimagesourcesupportedformat/document.md) | \- | Describes the format string supported by an image source. It is used in [OhosImageSourceSupportedFormatList](../../structs/ohosimagesourcesupportedformatlist/document.md) and [OH\_ImageSource\_GetSupportedFormats](#oh_imagesource_getsupportedformats). |
| [OhosImageSourceSupportedFormatList](../../structs/ohosimagesourcesupportedformatlist/document.md) | \- | Describes the format string list supported by an image source. It is obtained by calling [OH\_ImageSource\_GetSupportedFormats](#oh_imagesource_getsupportedformats). |
| [OhosImageSourceProperty](../../structs/ohosimagesourceproperty/document.md) | \- | Describes the property string (in key-value format) of an image source. It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty). |
| [OhosImageSourceUpdateData](../../structs/ohosimagesourceupdatedata/document.md) | \- | Describes the update data option of the image source. It is obtained by calling [OH\_ImageSource\_UpdateData](#oh_imagesource_updatedata). |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_ImageSource\_Create(napi\_env env, struct OhosImageSource\* src, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_create) | Creates an ImageSource object at the JavaScript native layer based on the specified OhosImageSource and OhosImageSourceOps structs. |
| [int32\_t OH\_ImageSource\_CreateFromUri(napi\_env env, char\* uri, size\_t size, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_createfromuri) | Creates an ImageSource object at the JavaScript native layer based on the specified URI and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct. |
| [int32\_t OH\_ImageSource\_CreateFromFd(napi\_env env, int32\_t fd, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_createfromfd) | Creates an ImageSource object at the JavaScript native layer based on the specified file descriptor and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct. |
| [int32\_t OH\_ImageSource\_CreateFromData(napi\_env env, uint8\_t\* data, size\_t dataSize, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_createfromdata) | Creates an ImageSource object at the JavaScript native layer based on the specified image source buffer (defined by **data**) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct. |
| [int32\_t OH\_ImageSource\_CreateFromRawFile(napi\_env env, RawFileDescriptor rawFile, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_createfromrawfile) | Creates an ImageSource object at the JavaScript native layer based on the specified [RawFileDescriptor](../../../../../application-framework/localization-kit/c-api/structs/rawfiledescriptor/document.md) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) structs. |
| [int32\_t OH\_ImageSource\_CreateIncremental(napi\_env env, struct OhosImageSource\* source, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_createincremental) | Creates an ImageSource object at the JavaScript native layer based on the specified [OhosImageSource](../../structs/ohosimagesource/document.md) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) structs. The image source data will be updated through [OH\_ImageSource\_UpdateData](#oh_imagesource_updatedata). |
| [int32\_t OH\_ImageSource\_CreateIncrementalFromData(napi\_env env, uint8\_t\* data, size\_t dataSize, struct OhosImageSourceOps\* ops, napi\_value \*res)](#oh_imagesource_createincrementalfromdata) | Creates an ImageSource object of the incremental type at the JavaScript native layer based on the specified image source buffer (defined by **data**) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct. The image data is updated through [OH\_ImageSource\_UpdateData](#oh_imagesource_updatedata). |
| [int32\_t OH\_ImageSource\_GetSupportedFormats(struct OhosImageSourceSupportedFormatList\* res)](#oh_imagesource_getsupportedformats) | Obtains all supported decoding formats. |
| [ImageSourceNative\* OH\_ImageSource\_InitNative(napi\_env env, napi\_value source)](#oh_imagesource_initnative) | Converts an ImageSource object at the JavaScript native layer into an [ImageSourceNative](../../structs/imagesourcenative/document.md) object. |
| [int32\_t OH\_ImageSource\_CreatePixelMap(const ImageSourceNative\* native, struct OhosImageDecodingOps\* ops, napi\_value \*res)](#oh_imagesource_createpixelmap) | Decodes an ImageSourceNative object to obtain a PixelMap object at the JavaScript native layer based on the specified [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md) struct. |
| [int32\_t OH\_ImageSource\_CreatePixelMapList(const ImageSourceNative\* native, struct OhosImageDecodingOps\* ops, napi\_value \*res)](#oh_imagesource_createpixelmaplist) | Decodes an ImageSourceNative object to obtain all PixelMap objects at the JavaScript native layer based on the specified [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md) struct. |
| [int32\_t OH\_ImageSource\_GetDelayTime(const ImageSourceNative\* native, struct OhosImageSourceDelayTimeList\* res)](#oh_imagesource_getdelaytime) | Obtains the delay time list from an ImageSourceNative object (such as GIF image source). |
| [int32\_t OH\_ImageSource\_GetFrameCount(const ImageSourceNative\* native, uint32\_t \*res)](#oh_imagesource_getframecount) | Obtains the number of frames from an ImageSourceNative object. |
| [int32\_t OH\_ImageSource\_GetImageInfo(const ImageSourceNative\* native, int32\_t index, struct OhosImageSourceInfo\* info)](#oh_imagesource_getimageinfo) | Obtains image source information from an ImageSourceNative object by index. |
| [int32\_t OH\_ImageSource\_GetImageProperty(const ImageSourceNative\* native, struct OhosImageSourceProperty\* key, struct OhosImageSourceProperty\* value)](#oh_imagesource_getimageproperty) | Obtains the value of an image property from an ImageSourceNative object. |
| [int32\_t OH\_ImageSource\_UpdateData(const ImageSourceNative\* native, struct OhosImageSourceUpdateData\* data)](#oh_imagesource_updatedata) | Updates the data of an ImageSourceNative object. |
| [int32\_t OH\_ImageSource\_Release(ImageSourceNative\* native)](#oh_imagesource_release) | Releases an ImageSourceNative object. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const char\* OHOS\_IMAGE\_PROPERTY\_BITS\_PER\_SAMPLE = "BitsPerSample" | 
Pointer to bits per sample, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_ORIENTATION = "Orientation" | 

Pointer to the orientation, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_IMAGE\_LENGTH = "ImageLength" | 

Pointer to the image length, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_IMAGE\_WIDTH = "ImageWidth" | 

Pointer to the image width, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE = "GPSLatitude" | 

Pointer to the GPS latitude, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE = "GPSLongitude" | 

Pointer to the GPS longitude, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE\_REF = "GPSLatitudeRef" | 

Pointer to the GPS latitude reference information, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE\_REF = "GPSLongitudeRef" | 

Pointer to the GPS longitude reference information, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_DATE\_TIME\_ORIGINAL = "DateTimeOriginal" | 

Pointer to the created date and time, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_TIME = "ExposureTime" | 

Pointer to the exposure time, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_SCENE\_TYPE = "SceneType" | 

Pointer to the scene type, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_RATINGS = "ISOSpeedRatings" | 

Pointer to the ISO speed ratings, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_F\_NUMBER = "FNumber" | 

Pointer to the f-number of the image, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |
| const char\* OHOS\_IMAGE\_PROPERTY\_COMPRESSED\_BITS\_PER\_PIXEL = "CompressedBitsPerPixel" | 

Pointer to the compressed bits per pixel, one of the image properties.

It is used in [OH\_ImageSource\_GetImageProperty](#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](#oh_imagesource_modifyimageproperty).

**Since**: 10

 |

#### Function Description

#### \[h2\]OH\_ImageSource\_Create()

int32\_t OH\_ImageSource\_Create(napi\_env env, struct OhosImageSource\* src, struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object at the JavaScript native layer based on the specified OhosImageSource and OhosImageSourceOps structs.

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_ImageSource\_CreateFromUri](#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](#oh_imagesource_createfromfd), and [OH\_ImageSource\_CreateFromData](#oh_imagesource_createfromdata)

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| struct OhosImageSource\* src | Pointer to the input resource of the image source. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_SOURCE\_DATA\_INCOMPLETE**: The image source data is incomplete.

**IMAGE\_RESULT\_SOURCE\_DATA**: The image source data is incorrect.

IMAGE\_RESULT\_GET\_DATA\_ABNORMAL: An error occurs during image data retrieval.

**IMAGE\_RESULT\_TOO\_LARGE**: The image data is too large.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

**IMAGE\_RESULT\_FILE\_DAMAGED**: The file is damaged.

**IMAGE\_RESULT\_FILE\_FD\_ERROR**: The file descriptor is incorrect.

**IMAGE\_RESULT\_STREAM\_SIZE\_ERROR**: The data stream is incorrect.

**IMAGE\_RESULT\_SEEK\_FAILED**: Seeking the file fails.

**IMAGE\_RESULT\_PEEK\_FAILED**: Peeking the file fails.

**IMAGE\_RESULT\_FREAD\_FAILED**: Reading the file fails.

 |

#### \[h2\]OH\_ImageSource\_CreateFromUri()

int32\_t OH\_ImageSource\_CreateFromUri(napi\_env env, char\* uri, size\_t size,struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object at the JavaScript native layer based on the specified URI and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| char\* uri | Pointer to the image source URI. Only a file URI or Base64 URI is accepted. Currently, only absolute paths are supported. |
| size\_t size | Length of the image source URI. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImageSource\_CreateFromFd()

int32\_t OH\_ImageSource\_CreateFromFd(napi\_env env, int32\_t fd,struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object at the JavaScript native layer based on the specified file descriptor and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| int32\_t fd | Descriptor of the image source. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImageSource\_CreateFromData()

int32\_t OH\_ImageSource\_CreateFromData(napi\_env env, uint8\_t\* data, size\_t dataSize,struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object at the JavaScript native layer based on the specified image source buffer (defined by **data**) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| uint8\_t\* data | Pointer to the image source buffer. Only a formatted packet buffer or Base64 buffer is accepted. |
| size\_t dataSize | Size of the image source buffer. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImageSource\_CreateFromRawFile()

int32\_t OH\_ImageSource\_CreateFromRawFile(napi\_env env, RawFileDescriptor rawFile,struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object at the JavaScript native layer based on the specified [RawFileDescriptor](../../../../../application-framework/localization-kit/c-api/structs/rawfiledescriptor/document.md) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) structs.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| [RawFileDescriptor](../../../../../application-framework/localization-kit/c-api/structs/rawfiledescriptor/document.md) rawFile | Descriptor of the image source resource. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImageSource\_CreateIncremental()

int32\_t OH\_ImageSource\_CreateIncremental(napi\_env env, struct OhosImageSource\* source, struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object at the JavaScript native layer based on the specified [OhosImageSource](../../structs/ohosimagesource/document.md) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) structs. The image source data will be updated through [OH\_ImageSource\_UpdateData](#oh_imagesource_updatedata).

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_ImageSource\_CreateIncrementalFromData](#oh_imagesource_createincrementalfromdata)

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| struct [OhosImageSource](../../structs/ohosimagesource/document.md)\* source | Pointer to the input resource of the image source. Only the buffer type is accepted. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImageSource\_CreateIncrementalFromData()

int32\_t OH\_ImageSource\_CreateIncrementalFromData(napi\_env env, uint8\_t\* data, size\_t dataSize,struct OhosImageSourceOps\* ops, napi\_value \*res)

**Description**

Creates an ImageSource object of the incremental type at the JavaScript native layer based on the specified image source buffer (defined by **data**) and [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md) struct. The image data is updated through [OH\_ImageSource\_UpdateData](#oh_imagesource_updatedata).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| uint8\_t\* data | Pointer to the image source buffer. Only a formatted packet buffer or Base64 buffer is accepted. |
| size\_t dataSize | Size of the image source buffer. |
| struct [OhosImageSourceOps](../../structs/ohosimagesourceops/document.md)\* ops | Pointer to the options for creating the image source. |
| napi\_value \*res | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImageSource\_GetSupportedFormats()

int32\_t OH\_ImageSource\_GetSupportedFormats(struct OhosImageSourceSupportedFormatList\* res)

**Description**

Obtains all supported decoding formats.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| struct OhosImageSourceSupportedFormatList\* res | 
Pointer to the [OhosImageSourceSupportedFormatList](../../structs/ohosimagesourcesupportedformatlist/document.md) struct. This struct contains the **supportedFormatList** and **size** properties.

This API needs to be called twice to correctly obtain the supported format list.

In the first call, **res->supportedFormatList** needs to be left empty, and **res->size** obtains the number of supported formats.

Before the second call, memory initialization must be completed. First, initialize **res->supportedFormatList** as a list containing **res->size** instances of [OhosImageSourceSupportedFormat](../../structs/ohosimagesourcesupportedformat/document.md). Then, allocate memory for each [OhosImageSourceSupportedFormat](../../structs/ohosimagesourcesupportedformat/document.md) to ensure that its **format** property has sufficient space to obtain image format information.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The check format is incorrect.

 |

#### \[h2\]OH\_ImageSource\_InitNative()

ImageSourceNative\* OH\_ImageSource\_InitNative(napi\_env env, napi\_value source)

**Description**

Converts an ImageSource object at the JavaScript native layer into an [ImageSourceNative](../../structs/imagesourcenative/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| napi\_value source | Pointer to an ImageSource object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageSourceNative](../../structs/imagesourcenative/document.md)\* | Pointer to the [ImageSourceNative](../../structs/imagesourcenative/document.md) object. If the operation fails, a null pointer is returned. |

**See also**

[OH\_ImageSource\_Release](#oh_imagesource_release)

#### \[h2\]OH\_ImageSource\_CreatePixelMap()

int32\_t OH\_ImageSource\_CreatePixelMap(const ImageSourceNative\* native,struct OhosImageDecodingOps\* ops, napi\_value \*res)

**Description**

Decodes an ImageSourceNative object to obtain a PixelMap object at the JavaScript native layer based on the specified [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md) struct.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| struct [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md)\* ops | Pointer to the options for decoding the image source. |
| napi\_value \*res | Pointer to a PixelMap object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED**: Failed to create the encoder.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The check format is incorrect.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: The shared memory does not exist.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is abnormal.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: The image is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_INIT\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_CROP**: An error occurs during image cropping.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_ENCODE\_FAILED**: Failed to add the PixelMap.

**IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT**: Image hardware decoding is not supported.

**IMAGE\_RESULT\_HW\_DECODE\_FAILED**: Hardware decoding fails.

**IMAGE\_RESULT\_ERR\_IPC**: IPC fails.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: Hardware decoding fails.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: Hardware decoding fails.

 |

#### \[h2\]OH\_ImageSource\_CreatePixelMapList()

int32\_t OH\_ImageSource\_CreatePixelMapList(const ImageSourceNative\* native,struct OhosImageDecodingOps\* ops, napi\_value \*res)

**Description**

Decodes an ImageSourceNative object to obtain all PixelMap objects at the JavaScript native layer based on the specified [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md) struct.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| struct [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md)\* ops | Pointer to the options for decoding the image source. |
| napi\_value \*res | Pointer to PixelMap objects at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED**: Failed to create the encoder.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The check format is incorrect.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: The shared memory does not exist.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is abnormal.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: The image is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_INIT\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_CROP**: An error occurs during image cropping.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_ENCODE\_FAILED**: Failed to add the PixelMap.

**IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT**: Image hardware decoding is not supported.

**IMAGE\_RESULT\_HW\_DECODE\_FAILED**: Hardware decoding fails.

**IMAGE\_RESULT\_ERR\_IPC**: IPC fails.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: Hardware decoding fails.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: Hardware decoding fails.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

 |

#### \[h2\]OH\_ImageSource\_GetDelayTime()

int32\_t OH\_ImageSource\_GetDelayTime(const ImageSourceNative\* native,struct OhosImageSourceDelayTimeList\* res)

**Description**

Obtains the delay time list from an ImageSourceNative object (such as GIF image source).

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| struct [OhosImageSourceDelayTimeList](../../structs/ohosimagesourcedelaytimelist/document.md)\* res | 
Pointer to the OhosImageSourceDelayTimeList object obtained.

When the input **delayTimeList** is a null pointer and **size** is **0**, the size of the delay time list is returned through **size** in **res**. To obtain the complete delay time list, a space greater than **size** is required.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

 |

#### \[h2\]OH\_ImageSource\_GetFrameCount()

int32\_t OH\_ImageSource\_GetFrameCount(const ImageSourceNative\* native, uint32\_t \*res)

**Description**

Obtains the number of frames from an ImageSourceNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| uint32\_t \*res | Pointer to the frame count. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

 |

#### \[h2\]OH\_ImageSource\_GetImageInfo()

int32\_t OH\_ImageSource\_GetImageInfo(const ImageSourceNative\* native, int32\_t index,struct OhosImageSourceInfo\* info)

**Description**

Obtains image source information from an ImageSourceNative object by index.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| int32\_t index | Index. |
| struct [OhosImageSourceInfo](../../structs/ohosimagesourceinfo/document.md)\* info | Pointer to the OhosImageSourceInfo object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

 |

#### \[h2\]OH\_ImageSource\_GetImageProperty()

int32\_t OH\_ImageSource\_GetImageProperty(const ImageSourceNative\* native, struct OhosImageSourceProperty\* key, struct OhosImageSourceProperty\* value)

**Description**

Obtains the value of an image property from an ImageSourceNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| struct [OhosImageSourceProperty](../../structs/ohosimagesourceproperty/document.md)\* key | Pointer to the property. For details, see **OhosImageSourceProperty**. |
| struct [OhosImageSourceProperty](../../structs/ohosimagesourceproperty/document.md)\* value | Pointer to the OhosImageSourceProperty object obtained. If the input **value** is a null pointer and **size** is **0**, the size of the property value is returned through **size** in **value**. To obtain the complete property value, a space greater than **size** is required. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

 |

#### \[h2\]OH\_ImageSource\_ModifyImageProperty()

int32\_t OH\_ImageSource\_ModifyImageProperty(const ImageSourceNative\* native, struct OhosImageSourceProperty\* key, struct OhosImageSourceProperty\* value)

**Description**

Modifies the value of an image property of an ImageSourceNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| struct [OhosImageSourceProperty](../../structs/ohosimagesourceproperty/document.md)\* key | Pointer to the property. For details, see **OhosImageSourceProperty**. |
| struct [OhosImageSourceProperty](../../structs/ohosimagesourceproperty/document.md)\* value | Pointer to the new value of the property. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia error.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT**: Exif is not supported for image decoding.

**IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST**: The image property does not exist.

 |

#### \[h2\]OH\_ImageSource\_UpdateData()

int32\_t OH\_ImageSource\_UpdateData(const ImageSourceNative\* native, struct OhosImageSourceUpdateData\* data)

**Description**

Updates the data of an ImageSourceNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |
| struct [OhosImageSourceUpdateData](../../structs/ohosimagesourceupdatedata/document.md)\* data | Pointer to the update data. For details, see **OhosImageSourceUpdateData**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: Failed to create the decoder.

**IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED**: Failed to create the encoder.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The check format is incorrect.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: An error occurs in the Skia third-party library.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: The shared memory does not exist.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is abnormal.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: Image initialization error.

**IMAGE\_RESULT\_INIT\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_CROP**: An error occurs during image cropping.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: Failed to register the plugin.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: Failed to create the plugin.

**IMAGE\_RESULT\_ENCODE\_FAILED**: Failed to add the PixelMap.

**IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT**: Image hardware decoding is not supported.

**IMAGE\_RESULT\_HW\_DECODE\_FAILED**: Hardware decoding fails.

**IMAGE\_RESULT\_ERR\_IPC**: IPC fails.

**IMAGE\_RESULT\_INDEX\_INVALID**: The index is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_ImageSource\_Release()

int32\_t OH\_ImageSource\_Release(ImageSourceNative\* native)

**Description**

Releases an ImageSourceNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ImageSourceNative](../../structs/imagesourcenative/document.md)\* native | Pointer to an ImageSourceNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: Failed to obtain image data.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The input image data is incorrect.

 |

**See also**

[OH\_ImageSource\_Create](#oh_imagesource_create), [OH\_ImageSource\_CreateIncremental](#oh_imagesource_createincremental)
