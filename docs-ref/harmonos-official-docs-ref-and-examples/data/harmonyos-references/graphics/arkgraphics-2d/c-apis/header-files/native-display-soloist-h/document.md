# native\_display\_soloist.h

#### Overview

This file declares the functions for obtaining and using native display soloist.

**File to include**: <native\_display\_soloist/native\_display\_soloist.h>

**Library**: libnative\_display\_soloist.so

**System capability**: SystemCapability.Graphic.Graphic2D.HyperGraphicManager

**Since**: 12

**Related module**: [NativeDisplaySoloist](../../modules/nativedisplaysoloist/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DisplaySoloist\_ExpectedRateRange](../../structs/displaysoloist-expectedraterange/document.md) | DisplaySoloist\_ExpectedRateRange | Describes the expected frame rate range. |
| [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md) | OH\_DisplaySoloist | Provides the declaration of an **OH\_DisplaySoloist** struct. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_DisplaySoloist\_FrameCallback)(long long timestamp, long long targetTimestamp, void\* data)](#oh_displaysoloist_framecallback) | OH\_DisplaySoloist\_FrameCallback | Defines the pointer to an OH\_DisplaySoloist callback function. |
| [OH\_DisplaySoloist\* OH\_DisplaySoloist\_Create(bool useExclusiveThread)](#oh_displaysoloist_create) | \- | Creates an **OH\_DisplaySoloist** instance. A new **OH\_DisplaySoloist** instance is created each time this API is called. |
| [int32\_t OH\_DisplaySoloist\_Destroy(OH\_DisplaySoloist\* displaySoloist)](#oh_displaysoloist_destroy) | \- | Destroys an **OH\_DisplaySoloist** object and reclaims the memory occupied. |
| [int32\_t OH\_DisplaySoloist\_Start(OH\_DisplaySoloist\* displaySoloist, OH\_DisplaySoloist\_FrameCallback callback, void\* data)](#oh_displaysoloist_start) | \- | Sets a callback function for each frame. The callback function is triggered each time a VSync signal arrives. |
| [int32\_t OH\_DisplaySoloist\_Stop(OH\_DisplaySoloist\* displaySoloist)](#oh_displaysoloist_stop) | \- | Stops requesting the next VSync signal and triggering the callback function. |
| [int32\_t OH\_DisplaySoloist\_SetExpectedFrameRateRange(OH\_DisplaySoloist\* displaySoloist, DisplaySoloist\_ExpectedRateRange\* range)](#oh_displaysoloist_setexpectedframeraterange) | \- | Sets the expected frame rate range. |

#### Function Description

#### \[h2\]OH\_DisplaySoloist\_FrameCallback()

typedef void (\*OH\_DisplaySoloist\_FrameCallback)(long long timestamp, long long targetTimestamp, void\* data)

**Description**

Defines the pointer to an OH\_DisplaySoloist callback function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| long long timestamp | Current frame VSync timestamp. |
| long long targetTimestamp | Expected VSync timestamp of the next frame. |
| void\* data | Pointer to user-defined data. |

#### \[h2\]OH\_DisplaySoloist\_Create()

OH\_DisplaySoloist\* OH\_DisplaySoloist\_Create(bool useExclusiveThread)

**Description**

Creates an **OH\_DisplaySoloist** instance. A new **OH\_DisplaySoloist** instance is created each time this API is called.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| bool useExclusiveThread | Whether the **OH\_DisplaySoloist** instance is an exclusive thread. **true** means yes; **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_DisplaySoloist\* | Returns the pointer to the [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md) instance created if the operation is successful; returns a null pointer otherwise. The failure cause may be out of memory. |

#### \[h2\]OH\_DisplaySoloist\_Destroy()

int32\_t OH\_DisplaySoloist\_Destroy(OH\_DisplaySoloist\* displaySoloist)

**Description**

Destroys an **OH\_DisplaySoloist** object and reclaims the memory occupied.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md)\* displaySoloist | Pointer to the [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns **\-1** otherwise. |

#### \[h2\]OH\_DisplaySoloist\_Start()

int32\_t OH\_DisplaySoloist\_Start(OH\_DisplaySoloist\* displaySoloist, OH\_DisplaySoloist\_FrameCallback callback, void\* data)

**Description**

Sets a callback function for each frame. The callback function is triggered each time a VSync signal arrives.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md)\* displaySoloist | Pointer to the [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md) instance. |
| [OH\_DisplaySoloist\_FrameCallback](#oh_displaysoloist_framecallback) callback | Callback function to be triggered when the next VSync signal arrives. |
| void\* data | Pointer to the user-defined data struct. The type is void. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns **\-1** otherwise. |

#### \[h2\]OH\_DisplaySoloist\_Stop()

int32\_t OH\_DisplaySoloist\_Stop(OH\_DisplaySoloist\* displaySoloist)

**Description**

Stops requesting the next VSync signal and triggering the callback function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md)\* displaySoloist | Pointer to the [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns **\-1** otherwise. |

#### \[h2\]OH\_DisplaySoloist\_SetExpectedFrameRateRange()

int32\_t OH\_DisplaySoloist\_SetExpectedFrameRateRange(OH\_DisplaySoloist\* displaySoloist, DisplaySoloist\_ExpectedRateRange\* range)

**Description**

Sets the expected frame rate range.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md)\* displaySoloist | Pointer to the [OH\_DisplaySoloist](../../structs/oh-displaysoloist/document.md) instance. |
| [DisplaySoloist\_ExpectedRateRange](../../structs/displaysoloist-expectedraterange/document.md)\* range | Pointer to the [DisplaySoloist\_ExpectedRateRange](../../structs/displaysoloist-expectedraterange/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns **\-1** otherwise. |
