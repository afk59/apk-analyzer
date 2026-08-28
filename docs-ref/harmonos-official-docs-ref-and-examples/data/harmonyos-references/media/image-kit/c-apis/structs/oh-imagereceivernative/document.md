# OH\_ImageReceiverNative

struct OH\_ImageReceiverNative

#### Overview

The OH\_ImageReceiverNative struct describes the image receiver, which is encapsulated at the native layer. The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct.

To create an OH\_ImageReceiverNative object, call [OH\_ImageReceiverNative\_Create](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_create).

To release an OH\_ImageReceiverNative object, call [OH\_ImageReceiverNative\_Release](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_release).

The table below describes the content and operation mode of the OH\_ImageReceiverNative struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| uint64\_t | surfaceId | Surface ID of the receiver. | [OH\_ImageReceiverNative\_GetReceivingSurfaceId](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_getreceivingsurfaceid) | Obtains the surface ID through an OH\_ImageReceiverNative object. |
| OH\_ImageNative | image | Image at the native layer. | [OH\_ImageReceiverNative\_ReadLatestImage](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_readlatestimage) | Obtains the latest image through an OH\_ImageReceiverNative object. |
| OH\_ImageNative | image | Image at the native layer. | [OH\_ImageReceiverNative\_ReadNextImage](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_readnextimage) | Obtains the next image through an OH\_ImageReceiverNative object. |
| OH\_ImageReceiver\_OnCallback | callback | Callback function of the image receiver. | [OH\_ImageReceiverNative\_On](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_on) | Registers an OH\_ImageReceiver\_OnCallback. |
| OH\_ImageReceiver\_OnCallback | callback | Callback function of the image receiver. | [OH\_ImageReceiverNative\_Off](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_off) | Unregisters an OH\_ImageReceiver\_OnCallback. |
| Image\_Size | size | Size of an image receiver. | [OH\_ImageReceiverNative\_GetSize](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_getsize) | Obtains the size of an OH\_ImageReceiverNative. |
| int32\_t | capacity | Capacity of an image receiver. | [OH\_ImageReceiverNative\_GetCapacity](../../header-files/image-receiver-native-h/document.md#oh_imagereceivernative_getcapacity) | Obtains the capacity of an OH\_ImageReceiverNative. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_receiver\_native.h](../../header-files/image-receiver-native-h/document.md)
