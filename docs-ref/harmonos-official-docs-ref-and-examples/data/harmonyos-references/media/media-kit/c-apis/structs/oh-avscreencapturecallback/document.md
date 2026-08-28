# OH\_AVScreenCaptureCallback

typedef struct OH\_AVScreenCaptureCallback {...} OH\_AVScreenCaptureCallback

#### Overview

The struct describes all the asynchronous callback function pointers of an OH\_AVScreenCapture instance. To ensure the normal running of OH\_AVScreenCapture, you must register the instance of this struct with the OH\_AVScreenCapture instance and process the information reported by the callback functions.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnError](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencapture_onerror) and [OH\_AVScreenCapture\_OnBufferAvailable](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_AVScreenCaptureOnError](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencaptureonerror) onError | 
Callback function invoked when an error occurs during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnError](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencapture_onerror) instead.

 |
| [OH\_AVScreenCaptureOnAudioBufferAvailable](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencaptureonaudiobufferavailable) onAudioBufferAvailable | 

Callback function invoked when an audio buffer is available during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

 |
| [OH\_AVScreenCaptureOnVideoBufferAvailable](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencaptureonvideobufferavailable) onVideoBufferAvailable | 

Callback function invoked when a video buffer is available during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../../header-files/native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

 |
