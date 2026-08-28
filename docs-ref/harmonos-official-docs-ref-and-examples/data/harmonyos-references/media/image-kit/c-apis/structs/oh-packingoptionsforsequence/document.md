# OH\_PackingOptionsForSequence

typedef struct OH\_PackingOptionsForSequence OH\_PackingOptionsForSequence

#### Overview

OH\_PackingOptionsForSequence is an image sequence encoding option struct encapsulated at the native layer. It cannot be manipulated directly; instead, functions shall be called to create and release the struct, and operate on its specific fields.

The [OH\_PackingOptionsForSequence\_Create](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_create) function is used to create the OH\_PackingOptionsForSequence struct.

The [OH\_PackingOptionsForSequence\_Release](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_release) function is used to release the OH\_PackingOptionsForSequence struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| uint32\_t | frameCount | Number of frames. | [OH\_PackingOptionsForSequence\_GetFrameCount](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_getframecount) | Obtains the number of frames specified for encoding. |
| uint32\_t | frameCount | Number of frames. | [OH\_PackingOptionsForSequence\_SetFrameCount](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_setframecount) | Sets the number of frames specified for encoding. |
| int32\_t \* | delayTimeList | Delay time array. | [OH\_PackingOptionsForSequence\_GetDelayTimeList](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_getdelaytimelist) | Obtains the delay time array of images during encoding. |
| int32\_t \* | delayTimeList | Delay time array. | [OH\_PackingOptionsForSequence\_SetDelayTimeList](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_setdelaytimelist) | Sets the delay time array of images during encoding. |
| uint32\_t \* | disposalTypes | Number of frames. | [OH\_PackingOptionsForSequence\_GetDisposalTypes](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_getdisposaltypes) | Obtains the disposal type array for image sequence encoding. |
| uint32\_t \* | disposalTypes | Number of frames. | [OH\_PackingOptionsForSequence\_SetDisposalTypes](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_setdisposaltypes) | Sets the disposal type array of images during encoding. |
| uint32\_t | loopCount | Number of frames. | [OH\_PackingOptionsForSequence\_GetLoopCount](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_getloopcount) | Obtains the number of image loops during encoding. |
| uint32\_t | loopCount | Number of frames. | [OH\_PackingOptionsForSequence\_SetLoopCount](../../header-files/image-packer-native-h/document.md#oh_packingoptionsforsequence_setloopcount) | Sets the number of image loops during encoding. The value range is \[0, 65535\]. The value **0** indicates infinite looping. If this field is not set, the playback does not loop. |

**Since**: 18

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_packer\_native.h](../../header-files/image-packer-native-h/document.md)
