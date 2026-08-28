# VideoProcessing\_Callback

typedef struct VideoProcessing\_Callback VideoProcessing\_Callback

#### Overview

The struct describes a callback object for handling video processing events.

You should define a null pointer for **VideoProcessing\_Callback** and use [OH\_VideoProcessingCallback\_Create](../../header-files/video-processing-h/document.md#oh_videoprocessingcallback_create) to create a callback object. Before creation, ensure that the pointer is null. After creating the callback object, call [OH\_VideoProcessing\_RegisterCallback](../../header-files/video-processing-h/document.md#oh_videoprocessing_registercallback) to register it with the video processing instance.

**Since**: 12

**Related module**: [VideoProcessing](../../modules/videoprocessing/document.md)

**Header file**: [video\_processing\_types.h](../../header-files/video-processing-types-h/document.md)
