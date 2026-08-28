# drawing\_record\_cmd.h

#### Overview

This file declares the functions related to a recording command object.

**File to include**: <native\_drawing/drawing\_record\_cmd.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RecordCmdUtils\* OH\_Drawing\_RecordCmdUtilsCreate(void)](#oh_drawing_recordcmdutilscreate) | Creates an **OH\_Drawing\_RecordCmdUtils** object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsDestroy(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils)](#oh_drawing_recordcmdutilsdestroy) | Destroys an **OH\_Drawing\_RecordCmdUtils** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsBeginRecording(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils,int32\_t width, int32\_t height, OH\_Drawing\_Canvas\*\* canvas)](#oh_drawing_recordcmdutilsbeginrecording) | 
Starts recording. This API must be used together with [OH\_Drawing\_RecordCmdUtilsFinishRecording](#oh_drawing_recordcmdutilsfinishrecording).

The **OH\_Drawing\_RecordCmdUtils** object generates a canvas object of the recording type and calls the interface of the drawing object to record all drawing commands.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsFinishRecording(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils,OH\_Drawing\_RecordCmd\*\* recordCmd)](#oh_drawing_recordcmdutilsfinishrecording) | 

Stops video recording. This function must be called after [OH\_Drawing\_RecordCmdUtilsBeginRecording](#oh_drawing_recordcmdutilsbeginrecording).

The **OH\_Drawing\_RecordCmdUtils** object ends recording and stores the drawing commands recorded by the canvas object of the recording type into the generated [OH\_Drawing\_RecordCmdUtilsBeginRecording](#oh_drawing_recordcmdutilsbeginrecording) object.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdDestroy(OH\_Drawing\_RecordCmd\* recordCmd)](#oh_drawing_recordcmddestroy) | Destroys an **OH\_Drawing\_RecordCmd** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_RecordCmdUtilsCreate()

OH\_Drawing\_RecordCmdUtils\* OH\_Drawing\_RecordCmdUtilsCreate(void)

**Description**

Creates an **OH\_Drawing\_RecordCmdUtils** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md)\* | Returns the pointer to the **OH\_Drawing\_RecordCmdUtils** object created. |

#### \[h2\]OH\_Drawing\_RecordCmdUtilsDestroy()

OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsDestroy(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils)

**Description**

Destroys an **OH\_Drawing\_RecordCmdUtils** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md)\* recordCmdUtils | Pointer to an [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **recordCmdUtils** is NULL.

 |

#### \[h2\]OH\_Drawing\_RecordCmdUtilsBeginRecording()

OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsBeginRecording(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils,int32\_t width, int32\_t height, OH\_Drawing\_Canvas\*\* canvas)

**Description**

Starts recording. This API must be used together with [OH\_Drawing\_RecordCmdUtilsFinishRecording](#oh_drawing_recordcmdutilsfinishrecording).

The **OH\_Drawing\_RecordCmdUtils** object generates a canvas object of the recording type and calls the interface of the drawing object to record all drawing commands.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md)\* recordCmdUtils | Pointer to an [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md) object. |
| int32\_t width | Width of the canvas. |
| int32\_t height | Height of the canvas. |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\*\* canvas | 
Double pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. You do not need to release this pointer.

This object does not support nested calling of [OH\_Drawing\_CanvasDrawRecordCmd](../drawing-canvas-h/document.md#oh_drawing_canvasdrawrecordcmd).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **recordCmdUtils** or **canvas** is NULL.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **width** or **height** is less than 0.

**OH\_DRAWING\_ERROR\_ALLOCATION\_FAILED** if the system memory is insufficient.

 |

#### \[h2\]OH\_Drawing\_RecordCmdUtilsFinishRecording()

OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsFinishRecording(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils,OH\_Drawing\_RecordCmd\*\* recordCmd)

**Description**

Stops video recording. This function must be called after [OH\_Drawing\_RecordCmdUtilsBeginRecording](#oh_drawing_recordcmdutilsbeginrecording).

The **OH\_Drawing\_RecordCmdUtils** object ends recording and stores the drawing commands recorded by the canvas object of the recording type into the generated [OH\_Drawing\_RecordCmdUtilsBeginRecording](#oh_drawing_recordcmdutilsbeginrecording) object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md)\* recordCmdUtils | Pointer to an [OH\_Drawing\_RecordCmdUtils](../../structs/oh-drawing-recordcmdutils/document.md) object. |
| [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md)\*\* recordCmd | Double pointer to the [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md) object. You need to call [OH\_Drawing\_CanvasDrawRecordCmd](../drawing-canvas-h/document.md#oh_drawing_canvasdrawrecordcmd) to draw the object, and call [OH\_Drawing\_RecordCmdDestroy](#oh_drawing_recordcmddestroy) to release it. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **recordCmdUtils** or **recordCmd** is NULL.

**OH\_DRAWING\_ERROR\_ALLOCATION\_FAILED** if the system memory is insufficient.

 |

#### \[h2\]OH\_Drawing\_RecordCmdDestroy()

OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdDestroy(OH\_Drawing\_RecordCmd\* recordCmd)

**Description**

Destroys an **OH\_Drawing\_RecordCmd** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md)\* recordCmd | Pointer to an [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **recordCmd** is NULL.

 |
