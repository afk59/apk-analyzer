# OH\_OnFrameAvailableListener

typedef struct {...} OH\_OnFrameAvailableListener

#### Overview

Defines an **OH\_NativeImage** listener, which is registered through [OH\_NativeImage\_SetOnFrameAvailableListener](../../header-files/native-image-h/document.md#oh_nativeimage_setonframeavailablelistener). The listener triggers a callback when a frame is available.

**Since**: 11

**Related module**: [OH\_NativeImage](../../modules/oh-nativeimage/document.md)

**Header file**: [native\_image.h](../../header-files/native-image-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| void\* context | User-defined context information, which is returned when the callback is triggered. |
| [OH\_OnFrameAvailable](../../header-files/native-image-h/document.md#oh_onframeavailable) onFrameAvailable | Callback function triggered when a frame is available. |

#### \[h2\]Member Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_OnFrameAvailable)(void \*context)](#oh_onframeavailable) | OH\_OnFrameAvailable() | 
Callback function triggered when a frame is available.

**Since**: 11

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

 |

#### Member Function Description

#### \[h2\]OH\_OnFrameAvailable()

typedef void (\*OH\_OnFrameAvailable)(void \*context)

**Item**

Callback function triggered when a frame is available.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*context | User-defined context information, which is returned when the callback is triggered. |
