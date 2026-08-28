# image\_receiver\_native.h

#### Overview

The file declares the APIs used to obtain image data from the native layer.

**File to include**: <multimedia/image\_framework/image/image\_receiver\_native.h>

**Library**: libimage\_receiver.so

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md) | OH\_ImageReceiverNative | Describes the image receiver, which is encapsulated at the native layer. The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct. |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md) | OH\_ImageReceiverOptions | Describes the data type name of the image receiver options. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_ImageReceiver\_OnCallback)(OH\_ImageReceiverNative \*receiver)](#oh_imagereceiver_oncallback) | OH\_ImageReceiver\_OnCallback | Defines the callbacks for the image receiver at the native layer. |
| [typedef void (\*OH\_ImageReceiver\_ImageArriveCallback)(OH\_ImageReceiverNative \*receiver, void \*userData)](#oh_imagereceiver_imagearrivecallback) | OH\_ImageReceiver\_ImageArriveCallback | Defines the callback for the ImageArrive event. |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_Create(OH\_ImageReceiverOptions \*\*options)](#oh_imagereceiveroptions_create) | \- | Creates an OH\_ImageReceiverOptions object at the application layer. |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_GetSize(OH\_ImageReceiverOptions\* options, Image\_Size\* size)](#oh_imagereceiveroptions_getsize) | \- | Obtains the image size of an OH\_ImageReceiverOptions object. |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_SetSize(OH\_ImageReceiverOptions\* options, Image\_Size size)](#oh_imagereceiveroptions_setsize) | \- | Sets the image size of an OH\_ImageReceiverOptions object. |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_GetCapacity(OH\_ImageReceiverOptions\* options, int32\_t\* capacity)](#oh_imagereceiveroptions_getcapacity) | \- | Obtains the image cache capacity of an OH\_ImageReceiverOptions object. |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_SetCapacity(OH\_ImageReceiverOptions\* options, int32\_t capacity)](#oh_imagereceiveroptions_setcapacity) | \- | Sets the image cache capacity of an OH\_ImageReceiverOptions object. |
| [Image\_ErrorCode OH\_ImageReceiverOptions\_Release(OH\_ImageReceiverOptions\* options)](#oh_imagereceiveroptions_release) | \- | Releases an OH\_ImageReceiverOptions object. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_Create(OH\_ImageReceiverOptions\* options, OH\_ImageReceiverNative\*\* receiver)](#oh_imagereceivernative_create) | \- | Creates an OH\_ImageReceiverNative object at the application layer. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_GetReceivingSurfaceId(OH\_ImageReceiverNative\* receiver, uint64\_t\* surfaceId)](#oh_imagereceivernative_getreceivingsurfaceid) | \- | Obtains the surface ID through an OH\_ImageReceiverNative object. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_ReadLatestImage(OH\_ImageReceiverNative\* receiver, OH\_ImageNative\*\* image)](#oh_imagereceivernative_readlatestimage) | \- | Obtains the latest image through an OH\_ImageReceiverNative object. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_ReadNextImage(OH\_ImageReceiverNative\* receiver, OH\_ImageNative\*\* image)](#oh_imagereceivernative_readnextimage) | \- | Obtains the next image through an OH\_ImageReceiverNative object. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_On(OH\_ImageReceiverNative\* receiver, OH\_ImageReceiver\_OnCallback callback)](#oh_imagereceivernative_on) | \- | 
Registers the [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback.

This callback is triggered whenever a new image is received.

 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_Off(OH\_ImageReceiverNative\* receiver)](#oh_imagereceivernative_off) | \- | 

Unregisters the [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback.

The callback is registered by calling [OH\_ImageReceiverNative\_On](#oh_imagereceivernative_on).

 |
| [Image\_ErrorCode OH\_ImageReceiverNative\_GetSize(OH\_ImageReceiverNative\* receiver, Image\_Size\* size)](#oh_imagereceivernative_getsize) | \- | Obtains the size of an **OH\_ImageReceiverNative**. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_GetCapacity(OH\_ImageReceiverNative\* receiver, int32\_t\* capacity)](#oh_imagereceivernative_getcapacity) | \- | Obtains the capacity of an **OH\_ImageReceiverNative**. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_Release(OH\_ImageReceiverNative\* receiver)](#oh_imagereceivernative_release) | \- | Releases an OH\_ImageReceiverNative object. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_OnImageArrive(OH\_ImageReceiverNative \*receiver, OH\_ImageReceiver\_ImageArriveCallback callback, void \*userData)](#oh_imagereceivernative_onimagearrive) | \- | Registers the [OH\_ImageReceiver\_ImageArriveCallback](#oh_imagereceiver_imagearrivecallback) callback. |
| [Image\_ErrorCode OH\_ImageReceiverNative\_OffImageArrive(OH\_ImageReceiverNative \*receiver, OH\_ImageReceiver\_ImageArriveCallback callback)](#oh_imagereceivernative_offimagearrive) | \- | Unregisters the [OH\_ImageReceiver\_ImageArriveCallback](#oh_imagereceiver_imagearrivecallback) callback. |

#### Function Description

#### \[h2\]OH\_ImageReceiver\_OnCallback()

typedef void (\*OH\_ImageReceiver\_OnCallback)(OH\_ImageReceiverNative \*receiver)

**Description**

Defines the callbacks for the image receiver at the native layer.

**Since**: 12

#### \[h2\]OH\_ImageReceiver\_ImageArriveCallback()

typedef void (\*OH\_ImageReceiver\_ImageArriveCallback)(OH\_ImageReceiverNative \*receiver, void \*userData)

**Description**

Defines the callback for the ImageArrive event.

**Since**: 20

#### \[h2\]OH\_ImageReceiverOptions\_Create()

Image\_ErrorCode OH\_ImageReceiverOptions\_Create(OH\_ImageReceiverOptions \*\*options)

**Description**

Creates an OH\_ImageReceiverOptions object at the application layer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md) \*\*options | Double pointer to the OH\_ImageReceiverOptions object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageReceiverOptions\_GetSize()

Image\_ErrorCode OH\_ImageReceiverOptions\_GetSize(OH\_ImageReceiverOptions\* options, Image\_Size\* size)

**Description**

Obtains the image size of an OH\_ImageReceiverOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md)\* options | Pointer to an OH\_ImageReceiverOptions object. |
| [Image\_Size](../../structs/image-size/document.md)\* size | Pointer to the Image\_Size object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverOptions\_SetSize()

Image\_ErrorCode OH\_ImageReceiverOptions\_SetSize(OH\_ImageReceiverOptions\* options, Image\_Size size)

**Description**

Sets the image size of an OH\_ImageReceiverOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md)\* options | Pointer to an OH\_ImageReceiverOptions object. |
| [Image\_Size](../../structs/image-size/document.md) size | Image\_Size object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverOptions\_GetCapacity()

Image\_ErrorCode OH\_ImageReceiverOptions\_GetCapacity(OH\_ImageReceiverOptions\* options, int32\_t\* capacity)

**Description**

Obtains the image cache capacity of an OH\_ImageReceiverOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md)\* options | Pointer to an OH\_ImageReceiverOptions object. |
| int32\_t\* capacity | Pointer to the capacity obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverOptions\_SetCapacity()

Image\_ErrorCode OH\_ImageReceiverOptions\_SetCapacity(OH\_ImageReceiverOptions\* options, int32\_t capacity)

**Description**

Sets the image cache capacity of an OH\_ImageReceiverOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md)\* options | Pointer to an OH\_ImageReceiverOptions object. |
| int32\_t capacity | Capacity. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverOptions\_Release()

Image\_ErrorCode OH\_ImageReceiverOptions\_Release(OH\_ImageReceiverOptions\* options)

**Description**

Releases an OH\_ImageReceiverOptions object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md)\* options | Pointer to an OH\_ImageReceiverOptions object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_Create()

Image\_ErrorCode OH\_ImageReceiverNative\_Create(OH\_ImageReceiverOptions\* options, OH\_ImageReceiverNative\*\* receiver)

**Description**

Creates an OH\_ImageReceiverNative object at the application layer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverOptions](../../structs/oh-imagereceiveroptions/document.md)\* options | Pointer to an OH\_ImageReceiverOptions object. |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\*\* receiver | Double pointer to the OH\_ImageReceiverNative object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageReceiverNative\_GetReceivingSurfaceId()

Image\_ErrorCode OH\_ImageReceiverNative\_GetReceivingSurfaceId(OH\_ImageReceiverNative\* receiver, uint64\_t\* surfaceId)

**Description**

Obtains the surface ID through an OH\_ImageReceiverNative object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |
| uint64\_t\* surfaceId | Pointer to the surface ID obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImageReceiverNative\_ReadLatestImage()

Image\_ErrorCode OH\_ImageReceiverNative\_ReadLatestImage(OH\_ImageReceiverNative\* receiver, OH\_ImageNative\*\* image)

**Description**

Obtains the latest image through an OH\_ImageReceiverNative object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/HHpCenuqSR65kcWMMjNa6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062433Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2684ABA1F52A015955038827E3D051C7ABEEB433D07F254A8B4392D55B745EE8)

-   Call this API after the [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback is triggered to ensure that it can receive data properly.
-   When **OH\_ImageNative** returned by this API is no longer needed, call [OH\_ImageNative\_Release](../image-native-h/document.md#oh_imagenative_release) to release it. Then new data can be received properly.
-   This API requires a lock to ensure that the **OH\_ImageReceiverNative** object is not released during use. For details, see [Using Image\_NativeModule to Receive Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-receiver-c).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md)\*\* image | Double pointer to the image obtained, which is an OH\_ImageNative object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageReceiverNative\_ReadNextImage()

Image\_ErrorCode OH\_ImageReceiverNative\_ReadNextImage(OH\_ImageReceiverNative\* receiver, OH\_ImageNative\*\* image)

**Description**

Obtains the next image through an OH\_ImageReceiverNative object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/M4Sn7nIxSRid1TAnHOqFGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062433Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CFBA677BD2CCB278CC06842C44F30B8E8DAC00A7E54D4396F09E077C34D5D23)

-   Call this API after the [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback is triggered to ensure that it can receive data properly.
-   When **OH\_ImageNative** returned by this API is no longer needed, call [OH\_ImageNative\_Release](../image-native-h/document.md#oh_imagenative_release) to release it. Then new data can be received properly.
-   This API requires a lock to ensure that the **OH\_ImageReceiverNative** object is not released during use. For details, see [Using Image\_NativeModule to Receive Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-receiver-c).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md)\*\* image | Double pointer to the image obtained, which is an OH\_ImageNative object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageReceiverNative\_On()

Image\_ErrorCode OH\_ImageReceiverNative\_On(OH\_ImageReceiverNative\* receiver, OH\_ImageReceiver\_OnCallback callback)

**Description**

Registers the [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback.

This callback is triggered whenever a new image is received.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |
| [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback | Callback to register. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_Off()

Image\_ErrorCode OH\_ImageReceiverNative\_Off(OH\_ImageReceiverNative\* receiver)

**Description**

Unregisters the [OH\_ImageReceiver\_OnCallback](#oh_imagereceiver_oncallback) callback.

The callback is registered by calling [OH\_ImageReceiverNative\_On](#oh_imagereceivernative_on).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_GetSize()

Image\_ErrorCode OH\_ImageReceiverNative\_GetSize(OH\_ImageReceiverNative\* receiver, Image\_Size\* size)

**Description**

Obtains the size of an **OH\_ImageReceiverNative**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |
| [Image\_Size](../../structs/image-size/document.md)\* size | Pointer to the Image\_Size object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_GetCapacity()

Image\_ErrorCode OH\_ImageReceiverNative\_GetCapacity(OH\_ImageReceiverNative\* receiver, int32\_t\* capacity)

**Description**

Obtains the capacity of an **OH\_ImageReceiverNative**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |
| int32\_t\* capacity | Pointer to the capacity obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_Release()

Image\_ErrorCode OH\_ImageReceiverNative\_Release(OH\_ImageReceiverNative\* receiver)

**Description**

Releases an OH\_ImageReceiverNative object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/VjL8El1kSRW-TfP0UkFs4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062433Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=318DC724F1AD97AFD6E3CEBCE8CDAD10831C3B49EDE19438F2DF086C7D91D052)

This API requires a lock to ensure that the released **OH\_ImageReceiverNative** object will not be used by other APIs. For details, see [Using Image\_NativeModule to Receive Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-receiver-c).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md)\* receiver | Pointer to an OH\_ImageReceiverNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_OnImageArrive()

Image\_ErrorCode OH\_ImageReceiverNative\_OnImageArrive(OH\_ImageReceiverNative \*receiver,OH\_ImageReceiver\_ImageArriveCallback callback, void \*userData)

**Description**

Registers the [OH\_ImageReceiver\_ImageArriveCallback](#oh_imagereceiver_imagearrivecallback) callback.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md) \*receiver | Pointer to an OH\_ImageReceiverNative object that processes the callback. |
| [OH\_ImageReceiver\_ImageArriveCallback](#oh_imagereceiver_imagearrivecallback) callback | Callback to register. |
| void \*userData | Pointer to user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_RECEIVER\_INVALID\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageReceiverNative\_OffImageArrive()

Image\_ErrorCode OH\_ImageReceiverNative\_OffImageArrive(OH\_ImageReceiverNative \*receiver,OH\_ImageReceiver\_ImageArriveCallback callback)

**Description**

Unregisters the [OH\_ImageReceiver\_ImageArriveCallback](#oh_imagereceiver_imagearrivecallback) callback.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageReceiverNative](../../structs/oh-imagereceivernative/document.md) \*receiver | Pointer to an OH\_ImageReceiverNative object that processes the callback. |
| [OH\_ImageReceiver\_ImageArriveCallback](#oh_imagereceiver_imagearrivecallback) callback | Callback to unregister. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_RECEIVER\_INVALID\_PARAMETER**: The **receiver** or **callback** parameter is not registered.

 |
