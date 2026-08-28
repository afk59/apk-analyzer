# image\_receiver\_mdk.h

#### Overview

The file declares the APIs used to obtain image data from the native layer.

**Library**: libimage\_receiver\_ndk.z.so

**File to include**: <multimedia/image\_framework/image\_receiver\_mdk.h>

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OhosImageReceiverInfo](../../structs/ohosimagereceiverinfo/document.md) | \- | Describes the information about an image receiver. |
| [ImageReceiverNative\_](../../structs/imagereceivernative/document.md) | ImageReceiverNative | Defines the data type name of the image receiver at the native layer. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_Image\_Receiver\_On\_Callback)()](#oh_image_receiver_on_callback) | OH\_Image\_Receiver\_On\_Callback | Defines the callbacks for the image receiver at the native layer. |
| [int32\_t OH\_Image\_Receiver\_CreateImageReceiver(napi\_env env, struct OhosImageReceiverInfo info, napi\_value\* res)](#oh_image_receiver_createimagereceiver) | \- | Creates an ImageReceiver object at the application layer. |
| [ImageReceiverNative\* OH\_Image\_Receiver\_InitImageReceiverNative(napi\_env env, napi\_value source)](#oh_image_receiver_initimagereceivernative) | \- | Initializes an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object through an ImageReceiver object. |
| [int32\_t OH\_Image\_Receiver\_GetReceivingSurfaceId(const ImageReceiverNative\* native, char\* id, size\_t len)](#oh_image_receiver_getreceivingsurfaceid) | \- | Obtains the receiver ID through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object. |
| [int32\_t OH\_Image\_Receiver\_ReadLatestImage(const ImageReceiverNative\* native, napi\_value\* image)](#oh_image_receiver_readlatestimage) | \- | Obtains the latest image through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object. |
| [int32\_t OH\_Image\_Receiver\_ReadNextImage(const ImageReceiverNative\* native, napi\_value\* image)](#oh_image_receiver_readnextimage) | \- | Obtains the next image through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object. |
| [int32\_t OH\_Image\_Receiver\_On(const ImageReceiverNative\* native, OH\_Image\_Receiver\_On\_Callback callback)](#oh_image_receiver_on) | \- | Registers an [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback. This callback is triggered whenever a new image is received. |
| [int32\_t OH\_Image\_Receiver\_GetSize(const ImageReceiverNative\* native, struct OhosImageSize\* size)](#oh_image_receiver_getsize) | \- | Obtains the size of the image receiver through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object. |
| [int32\_t OH\_Image\_Receiver\_GetCapacity(const ImageReceiverNative\* native, int32\_t\* capacity)](#oh_image_receiver_getcapacity) | \- | Obtains the capacity of the image receiver through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object. |
| [int32\_t OH\_Image\_Receiver\_GetFormat(const ImageReceiverNative\* native, int32\_t\* format)](#oh_image_receiver_getformat) | \- | Obtains the format of the image receiver through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object. |
| [int32\_t OH\_Image\_Receiver\_Release(ImageReceiverNative\* native)](#oh_image_receiver_release) | \- | 
Releases an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

This function is not used to release an ImageReceiver object.

 |

#### Function Description

#### \[h2\]OH\_Image\_Receiver\_On\_Callback()

typedef void (\*OH\_Image\_Receiver\_On\_Callback)(void)

**Description**

Defines the callbacks for the image receiver at the native layer.

**Since**: 10

#### \[h2\]OH\_Image\_Receiver\_CreateImageReceiver()

int32\_t OH\_Image\_Receiver\_CreateImageReceiver(napi\_env env, struct OhosImageReceiverInfo info, napi\_value\* res)

**Description**

Creates an ImageReceiver object at the application layer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| struct [OhosImageReceiverInfo](../../structs/ohosimagereceiverinfo/document.md) info | Options for setting the ImageReceiver object. |
| napi\_value\* res | Pointer to the ImageReceiver object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED**: The surface fails to be created.

**IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED**: The buffer fails to be allocated to the surface.

**IMAGE\_RESULT\_GET\_SURFACE\_FAILED**: The surface fails to be obtained.

**IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT**: The media RTSP surface is not supported.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

**IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT**: The media type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_InitImageReceiverNative()

ImageReceiverNative\* OH\_Image\_Receiver\_InitImageReceiverNative(napi\_env env, napi\_value source)

**Description**

Initializes an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object through an ImageReceiver object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value source | ImageReceiver object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* | Pointer to the ImageReceiverNative object obtained. If the operation fails, nullptr is returned. |

**See also**

[OH\_Image\_Receiver\_Release](#oh_image_receiver_release)

#### \[h2\]OH\_Image\_Receiver\_GetReceivingSurfaceId()

int32\_t OH\_Image\_Receiver\_GetReceivingSurfaceId(const ImageReceiverNative\* native, char\* id, size\_t len)

**Description**

Obtains the receiver ID through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| char\* id | Pointer to the buffer that stores the ID string obtained. |
| size\_t len | Size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_GET\_SURFACE\_FAILED**: The surface fails to be obtained.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

**IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT**: The media type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_ReadLatestImage()

int32\_t OH\_Image\_Receiver\_ReadLatestImage(const ImageReceiverNative\* native, napi\_value\* image)

**Description**

Obtains the latest image through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

This function can be called to receive data only after the [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback is triggered. When the [ImageNative](../../structs/imagenative/document.md) object created by the Image object returned by this function is no longer needed, call [OH\_Image\_Release](../image-mdk-h/document.md#oh_image_release) to release the object. New data can be received only after the release.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| napi\_value\* image | Pointer to an Image object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED**: The surface fails to be created.

**IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED**: The buffer fails to be allocated to the surface.

**IMAGE\_RESULT\_GET\_SURFACE\_FAILED**: The surface fails to be obtained.

**IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT**: The media RTSP surface is not supported.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

**IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT**: The media type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_ReadNextImage()

int32\_t OH\_Image\_Receiver\_ReadNextImage(const ImageReceiverNative\* native, napi\_value\* image)

**Description**

Obtains the next image through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

This function can be called to receive data only after the [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback is triggered. When the [ImageNative](../../structs/imagenative/document.md) object created by the Image object returned by this function is no longer needed, call [OH\_Image\_Release](../image-mdk-h/document.md#oh_image_release) to release the object. New data can be received only after the release.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| napi\_value\* image | Pointer to an Image object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED**: The surface fails to be created.

**IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED**: The buffer fails to be allocated to the surface.

**IMAGE\_RESULT\_GET\_SURFACE\_FAILED**: The surface fails to be obtained.

**IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT**: The media RTSP surface is not supported.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

**IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT**: The media type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_On()

int32\_t OH\_Image\_Receiver\_On(const ImageReceiverNative\* native, OH\_Image\_Receiver\_On\_Callback callback)

**Description**

Registers an [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback. This callback is triggered whenever a new image is received.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback | [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback to register. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_GET\_SURFACE\_FAILED**: The surface fails to be obtained.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

**IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT**: The media type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_GetSize()

int32\_t OH\_Image\_Receiver\_GetSize(const ImageReceiverNative\* native, struct OhosImageSize\* size)

**Description**

Obtains the size of the image receiver through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| struct [OhosImageSize](../../structs/ohosimagesize/document.md)\* size | Pointer to the OhosImageSize object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_GetCapacity()

int32\_t OH\_Image\_Receiver\_GetCapacity(const ImageReceiverNative\* native, int32\_t\* capacity)

**Description**

Obtains the capacity of the image receiver through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| int32\_t\* capacity | Pointer to the capacity obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_GetFormat()

int32\_t OH\_Image\_Receiver\_GetFormat(const ImageReceiverNative\* native, int32\_t\* format)

**Description**

Obtains the format of the image receiver through an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |
| int32\_t\* format | Pointer to the format obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

 |

#### \[h2\]OH\_Image\_Receiver\_Release()

int32\_t OH\_Image\_Receiver\_Release(ImageReceiverNative\* native)

**Description**

Releases an [ImageReceiverNative](../../structs/imagereceivernative/document.md) object.

This function is not used to release an ImageReceiver object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ImageReceiverNative](../../structs/imagereceivernative/document.md)\* native | Pointer to an ImageReceiverNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image type is not supported.

 |
