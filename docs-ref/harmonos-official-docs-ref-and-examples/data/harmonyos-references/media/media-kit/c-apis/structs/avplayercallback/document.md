# AVPlayerCallback

typedef struct AVPlayerCallback {...} AVPlayerCallback

#### Overview

The struct contains the set of the **OH\_AVPlayerOnInfo** and **OH\_AVPlayerOnError** callback function pointers. To ensure the normal running of OH\_AVPlayer, you must register the instance of this struct with the OH\_AVPlayer instance and process the information reported by the callback functions.

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_AVPlayerOnInfoCallback](../../header-files/avplayer-base-h/document.md#oh_avplayeroninfocallback) and [OH\_AVPlayerOnErrorCallback](../../header-files/avplayer-base-h/document.md#oh_avplayeronerrorcallback)

**Related module**: [AVPlayer](../../modules/avplayer/document.md)

**Header file**: [avplayer\_base.h](../../header-files/avplayer-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| OH\_AVPlayerOnInfo onInfo | 
Callback for AVPlayer process information. For details about the available options, see [OH\_AVPlayerOnInfo](../../header-files/avplayer-base-h/document.md#oh_avplayeroninfo).

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_AVPlayerOnInfoCallback](../../header-files/avplayer-base-h/document.md#oh_avplayeroninfocallback)

 |
| OH\_AVPlayerOnError onError | 

Callback for AVPlayer error information. For details about the available options, see [OH\_AVPlayerOnError](../../header-files/avplayer-base-h/document.md#oh_avplayeronerror).

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_AVPlayerOnErrorCallback](../../header-files/avplayer-base-h/document.md#oh_avplayeronerrorcallback)

 |
