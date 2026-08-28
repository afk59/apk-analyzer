# OH\_ImageReceiverOptions

typedef struct OH\_ImageReceiverOptions OH\_ImageReceiverOptions

#### Overview

The struct describes the data type name of the image receiver options.

OH\_ImageReceiverOptions is the image receiver option setter struct encapsulated at the native layer. It is used to pass parameters during the creation of an OH\_ImageReceiverNative object. The struct cannot be directly operated. Instead, functions must be called to create and release the struct and operate the fields in the struct.

To create an OH\_ImageReceiverOptions object, call [OH\_ImageReceiverOptions\_Create](../../header-files/image-receiver-native-h/document.md#oh_imagereceiveroptions_create).

To release an OH\_ImageReceiverOptions object, call [OH\_ImageReceiverOptions\_Release](../../header-files/image-receiver-native-h/document.md#oh_imagereceiveroptions_release).

The table below describes the content and operation mode of the OH\_ImageReceiverOptions struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| Image\_Size | size | Image size. | [OH\_ImageReceiverOptions\_GetSize](../../header-files/image-receiver-native-h/document.md#oh_imagereceiveroptions_getsize) | Obtains the image size of an OH\_ImageReceiverOptions object. |
| Image\_Size | size | Image size. | [OH\_ImageReceiverOptions\_SetSize](../../header-files/image-receiver-native-h/document.md#oh_imagereceiveroptions_setsize) | Sets the image size of an OH\_ImageReceiverOptions object. |
| int32\_t | capacity | Capacity of the image buffer. | [OH\_ImageReceiverOptions\_GetCapacity](../../header-files/image-receiver-native-h/document.md#oh_imagereceiveroptions_getcapacity) | Obtains the image cache capacity of an OH\_ImageReceiverOptions object. |
| int32\_t | capacity | Capacity of the image buffer. | [OH\_ImageReceiverOptions\_SetCapacity](../../header-files/image-receiver-native-h/document.md#oh_imagereceiveroptions_setcapacity) | Sets the image cache capacity of an OH\_ImageReceiverOptions object. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_receiver\_native.h](../../header-files/image-receiver-native-h/document.md)
