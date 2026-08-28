# image\_packer\_mdk.h

#### Overview

The file declares the APIs used to pack an image or a PixelMap into a buffer or file.

The packing process is as follows:

Create an encoder object using **OH\_ImagePacker\_Create**.

Convert the encoder object to a native encoder object using **OH\_ImagePacker\_InitNative**.

Call **OH\_ImagePacker\_PackToData** or OH\_ImagePacker\_PackToFile to pack the source into the target area with the specified packing options.

Release the encoder object using **OH\_ImagePacker\_Release**.

**File to include**: <multimedia/image\_framework/image\_packer\_mdk.h>

**Library**: libimage\_packer\_ndk.z.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 11

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ImagePacker\_Opts\_](../../structs/imagepacker-opts/document.md) | ImagePacker\_Opts | Describes the image packing options. |
| [ImagePacker\_Native\_](../../structs/imagepacker-native/document.md) | ImagePacker\_Native | Describes the ImagePacker instance at the native layer. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_ImagePacker\_Create(napi\_env env, napi\_value \*res)](#oh_imagepacker_create) | Obtains an ImagePacker object at the JavaScript native layer. |
| [ImagePacker\_Native\* OH\_ImagePacker\_InitNative(napi\_env env, napi\_value packer)](#oh_imagepacker_initnative) | Converts an ImagePacker object at the JavaScript native layer into an ImagePacker\_Native object. |
| [int32\_t OH\_ImagePacker\_PackToData(ImagePacker\_Native\* native, napi\_value source,ImagePacker\_Opts\* opts, uint8\_t\* outData, size\_t\* size)](#oh_imagepacker_packtodata) | Packs a PixelMap object or an ImagePacker object at the JavaScript native layer to a buffer (defined by **outData**) based on the specified ImagePacker\_Opts struct. |
| [int32\_t OH\_ImagePacker\_PackToFile(ImagePacker\_Native\* native, napi\_value source, ImagePacker\_Opts\* opts, int fd)](#oh_imagepacker_packtofile) | Packs a PixelMap object or an ImagePacker object at the JavaScript native layer to a file based on the specified ImagePacker\_Opts struct. |
| [int32\_t OH\_ImagePacker\_Release(ImagePacker\_Native\* native)](#oh_imagepacker_release) | 
Releases an [ImagePacker\_Native](../../structs/imagepacker-native/document.md) object.

It is not used to release the ImagePacker object at the JavaScript native layer.

 |

#### Function Description

#### \[h2\]OH\_ImagePacker\_Create()

int32\_t OH\_ImagePacker\_Create(napi\_env env, napi\_value \*res)

**Description**

Obtains an ImagePacker object at the JavaScript native layer.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| napi\_value \*res | Pointer to an ImagePacker object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

 |

#### \[h2\]OH\_ImagePacker\_InitNative()

ImagePacker\_Native\* OH\_ImagePacker\_InitNative(napi\_env env, napi\_value packer)

**Description**

Converts an ImagePacker object at the JavaScript native layer into an ImagePacker\_Native object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| napi\_value packer | ImagePacker object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImagePacker\_Native](../../structs/imagepacker-native/document.md)\* | Pointer to an ImagePacker\_Native object. If the operation fails, a null pointer is returned. |

**See also**

[OH\_ImagePacker\_Release](#oh_imagepacker_release)

#### \[h2\]OH\_ImagePacker\_PackToData()

int32\_t OH\_ImagePacker\_PackToData(ImagePacker\_Native\* native, napi\_value source,ImagePacker\_Opts\* opts, uint8\_t\* outData, size\_t\* size)

**Description**

Packs a PixelMap object or an ImagePacker object at the JavaScript native layer to a buffer (defined by **outData**) based on the specified ImagePacker\_Opts struct.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [ImagePacker\_Native](../../structs/imagepacker-native/document.md)\* native | Pointer to an ImagePacker\_Native object. |
| napi\_value source | PixelMap object or ImageSource object at the JavaScript native layer. |
| [ImagePacker\_Opts](../../structs/imagepacker-opts/document.md)\* opts | Pointer to the packing options. |
| uint8\_t\* outData | Pointer to the output buffer. |
| size\_t\* size | Pointer to the size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**ERR\_IMAGE\_DATA\_ABNORMAL**: The output buffer is abnormal.

**ERR\_IMAGE\_MISMATCHED\_FORMAT**: The format is incorrect.

**ERR\_IMAGE\_MALLOC\_ABNORMAL**: An error occurs in the malloc internal buffer.

**ERR\_IMAGE\_DECODE\_ABNORMAL**: An internal error occurs during codec initialization.

**ERR\_IMAGE\_ENCODE\_FAILED**: An error occurs during encoding.

 |

**See also**

[OH\_ImagePacker\_PackToFile](#oh_imagepacker_packtofile)

#### \[h2\]OH\_ImagePacker\_PackToFile()

int32\_t OH\_ImagePacker\_PackToFile(ImagePacker\_Native\* native, napi\_value source,ImagePacker\_Opts\* opts, int fd)

**Description**

Packs a PixelMap object or an ImagePacker object at the JavaScript native layer to a file based on the specified ImagePacker\_Opts struct.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [ImagePacker\_Native](../../structs/imagepacker-native/document.md)\* native | Pointer to an ImagePacker\_Native object. |
| napi\_value source | PixelMap object or ImageSource object at the JavaScript native layer. |
| [ImagePacker\_Opts](../../structs/imagepacker-opts/document.md)\* opts | Pointer to the packing options. |
| int fd | File descriptor of the output file. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**ERR\_IMAGE\_DATA\_ABNORMAL**: The output buffer is abnormal.

**ERR\_IMAGE\_MISMATCHED\_FORMAT**: The format is incorrect.

**ERR\_IMAGE\_MALLOC\_ABNORMAL**: An error occurs in the malloc internal buffer.

**ERR\_IMAGE\_DECODE\_ABNORMAL**: An internal error occurs during codec initialization.

**ERR\_IMAGE\_ENCODE\_FAILED**: An error occurs during encoding.

 |

**See also**

[OH\_ImagePacker\_PackToData](#oh_imagepacker_packtodata)

#### \[h2\]OH\_ImagePacker\_Release()

int32\_t OH\_ImagePacker\_Release(ImagePacker\_Native\* native)

**Description**

Releases an [ImagePacker\_Native](../../structs/imagepacker-native/document.md) object.

It is not used to release the ImagePacker object at the JavaScript native layer.

It is parsed by calling [OH\_ImagePacker\_InitNative](#oh_imagepacker_initnative).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [ImagePacker\_Native](../../structs/imagepacker-native/document.md)\* native | Pointer to an ImagePacker\_Native object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

 |

**See also**

[OH\_ImagePacker\_InitNative](#oh_imagepacker_initnative)
