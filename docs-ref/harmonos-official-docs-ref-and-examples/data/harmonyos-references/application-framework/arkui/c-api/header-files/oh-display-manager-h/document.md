# oh\_display\_manager.h

#### Overview

The file declares the functions for basic display management. You can call the functions to obtain various information about the default display and listen for display status changes, such as rotation, folding, and unfolding.

**File to include**: <window\_manager/oh\_display\_manager.h>

**Library**: libnative\_display\_manager.so

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Since**: 12

**Related module**: [OH\_DisplayManager](../../modules/oh-displaymanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayId(uint64\_t \*displayId)](#oh_nativedisplaymanager_getdefaultdisplayid) | \- | Obtains the ID of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayWidth(int32\_t \*displayWidth)](#oh_nativedisplaymanager_getdefaultdisplaywidth) | \- | Obtains the width of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayHeight(int32\_t \*displayHeight)](#oh_nativedisplaymanager_getdefaultdisplayheight) | \- | Obtains the height of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayRotation(NativeDisplayManager\_Rotation \*displayRotation)](#oh_nativedisplaymanager_getdefaultdisplayrotation) | \- | Obtains the clockwise rotation angle of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayOrientation(NativeDisplayManager\_Orientation \*displayOrientation)](#oh_nativedisplaymanager_getdefaultdisplayorientation) | \- | Obtains the orientation of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayVirtualPixelRatio(float \*virtualPixels)](#oh_nativedisplaymanager_getdefaultdisplayvirtualpixelratio) | \- | Obtains the virtual pixel ratio of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayRefreshRate(uint32\_t \*refreshRate)](#oh_nativedisplaymanager_getdefaultdisplayrefreshrate) | \- | Obtains the refresh rate of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityDpi(int32\_t \*densityDpi)](#oh_nativedisplaymanager_getdefaultdisplaydensitydpi) | \- | Obtains the physical pixel density of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityPixels(float \*densityPixels)](#oh_nativedisplaymanager_getdefaultdisplaydensitypixels) | \- | Obtains the logical pixel density of the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayScaledDensity(float \*scaledDensity)](#oh_nativedisplaymanager_getdefaultdisplayscaleddensity) | \- | Obtains the scale factor of fonts displayed on the default display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityXdpi(float \*xDpi)](#oh_nativedisplaymanager_getdefaultdisplaydensityxdpi) | \- | Obtains the number of physical pixels per inch on the default display in the X dimension. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityYdpi(float \*yDpi)](#oh_nativedisplaymanager_getdefaultdisplaydensityydpi) | \- | Obtains the number of physical pixels per inch on the default display in the Y dimension. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*\*cutoutInfo)](#oh_nativedisplaymanager_createdefaultdisplaycutoutinfo) | \- | Obtains the unusable area of the default display, including punch hole, notch, and curved area of a waterfall display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*cutoutInfo)](#oh_nativedisplaymanager_destroydefaultdisplaycutoutinfo) | \- | Destroys the unusable area of the default display, including punch hole, notch, and curved area of a waterfall display. |
| [bool OH\_NativeDisplayManager\_IsFoldable()](#oh_nativedisplaymanager_isfoldable) | \- | Checks whether the current device is foldable. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetFoldDisplayMode(NativeDisplayManager\_FoldDisplayMode \*displayMode)](#oh_nativedisplaymanager_getfolddisplaymode) | \- | Obtains the display mode of the foldable device. |
| [typedef void (\*OH\_NativeDisplayManager\_DisplayChangeCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_displaychangecallback) | OH\_NativeDisplayManager\_DisplayChangeCallback | Defines a callback function to listen for display status changes. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayChangeListener(OH\_NativeDisplayManager\_DisplayChangeCallback displayChangeCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerdisplaychangelistener) | \- | Registers a listener for display status changes (such as rotation, refresh rate, DPI, and resolution changes). |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterdisplaychangelistener) | \- | Unregisters a listener for display status changes. |
| [typedef void (\*OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback)(NativeDisplayManager\_FoldDisplayMode displayMode)](#oh_nativedisplaymanager_folddisplaymodechangecallback) | OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback | Defines a callback function to listen for folded/unfolded state changes of the display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener(OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerfolddisplaymodechangelistener) | \- | Registers a listener for folded/unfolded state changes of the display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterfolddisplaymodechangelistener) | \- | Unregisters a listener for folded/unfolded state changes of the display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateAllDisplays(NativeDisplayManager\_DisplaysInfo \*\*allDisplays)](#oh_nativedisplaymanager_createalldisplays) | \- | Obtains the object that contains the information about all displays. |
| [void OH\_NativeDisplayManager\_DestroyAllDisplays(NativeDisplayManager\_DisplaysInfo \*allDisplays)](#oh_nativedisplaymanager_destroyalldisplays) | \- | Destroys the object that contains the information about all displays. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateDisplayById(uint32\_t displayId,NativeDisplayManager\_DisplayInfo \*\*displayInfo)](#oh_nativedisplaymanager_createdisplaybyid) | \- | Obtains the object that contains the information about a display. |
| [void OH\_NativeDisplayManager\_DestroyDisplay(NativeDisplayManager\_DisplayInfo \*displayInfo)](#oh_nativedisplaymanager_destroydisplay) | \- | Destroys the object that contains the information about a display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreatePrimaryDisplay(NativeDisplayManager\_DisplayInfo \*\*displayInfo)](#oh_nativedisplaymanager_createprimarydisplay) | \- | Obtains the object that contains the information about the primary display. For devices other than 2-in-1 devices, the displayInfo object obtained contains information about the built-in screen. For 2-in-1 devices with an external screen, the displayInfo object obtained contains information about the current primary screen. For 2-in-1 devices without an external screen, the displayInfo object obtained contains information about the built-in screen. |
| [typedef void (\*OH\_NativeDisplayManager\_AvailableAreaChangeCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_availableareachangecallback) | OH\_NativeDisplayManager\_AvailableAreaChangeCallback | Defines a callback function to listen for available area changes of a display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener(OH\_NativeDisplayManager\_AvailableAreaChangeCallback availableAreaChangeCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registeravailableareachangelistener) | \- | Registers a listener for available area changes of the display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisteravailableareachangelistener) | \- | Unregisters a listener for available area changes of the display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateAvailableArea(uint64\_t displayId, NativeDisplayManager\_Rect \*\*availableArea)](#oh_nativedisplaymanager_createavailablearea) | \- | Obtains the available area of a display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_DestroyAvailableArea(NativeDisplayManager\_Rect \*availableArea)](#oh_nativedisplaymanager_destroyavailablearea) | \- | Destroys the available area of a display. |
| [typedef void (\*OH\_NativeDisplayManager\_DisplayAddCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_displayaddcallback) | OH\_NativeDisplayManager\_DisplayAddCallback | Defines a callback function to listen for display addition events. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayAddListener(OH\_NativeDisplayManager\_DisplayAddCallback displayAddCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerdisplayaddlistener) | \- | Registers a listener for display addition events (for example, monitor inserted). |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayAddListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterdisplayaddlistener) | \- | Unregisters a listener for display addition events. |
| [typedef void (\*OH\_NativeDisplayManager\_DisplayRemoveCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_displayremovecallback) | OH\_NativeDisplayManager\_DisplayRemoveCallback | Defines a callback function to listen for display removal events. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayRemoveListener(OH\_NativeDisplayManager\_DisplayRemoveCallback displayRemoveCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerdisplayremovelistener) | \- | Registers a listener for display removal events (for example, monitor removed). |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterdisplayremovelistener) | \- | Unregisters the listener for display removal events. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDisplaySourceMode(uint64\_t displayId, NativeDisplayManager\_SourceMode \*sourceMode)](#oh_nativedisplaymanager_getdisplaysourcemode) | \- | Obtains the source mode of a display. |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDisplayPosition(uint64\_t displayId, int32\_t \*x, int32\_t \*y)](#oh_nativedisplaymanager_getdisplayposition) | \- | Obtains the position of a display. |

#### Function Description

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayId()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayId(uint64\_t \*displayId)

**Description**

Obtains the ID of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t \*displayId | Pointer to the display ID. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayWidth()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayWidth(int32\_t \*displayWidth)

**Description**

Obtains the width of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t \*displayWidth | Pointer to the width, in px. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayHeight()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayHeight(int32\_t \*displayHeight)

**Description**

Obtains the height of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t \*displayHeight | Pointer to the height, in px. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayRotation()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayRotation(NativeDisplayManager\_Rotation \*displayRotation)

**Description**

Obtains the clockwise rotation angle of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_Rotation](../oh-display-info-h/document.md#nativedisplaymanager_rotation) \*displayRotation | Pointer to the clockwise rotation angle. For details about the available options, see [NativeDisplayManager\_Rotation](../oh-display-info-h/document.md#nativedisplaymanager_rotation). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayOrientation()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayOrientation(NativeDisplayManager\_Orientation \*displayOrientation)

**Description**

Obtains the orientation of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_Orientation](../oh-display-info-h/document.md#nativedisplaymanager_orientation) \*displayOrientation | Pointer to the orientation. For details about the available options, see [NativeDisplayManager\_Orientation](../oh-display-info-h/document.md#nativedisplaymanager_orientation). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayVirtualPixelRatio()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayVirtualPixelRatio(float \*virtualPixels)

**Description**

Obtains the virtual pixel ratio of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| float \*virtualPixels | Pointer to the virtual pixel ratio. The value is a floating-point number, and it is usually the same as that of **densityPixels**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayRefreshRate()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayRefreshRate(uint32\_t \*refreshRate)

**Description**

Obtains the refresh rate of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t \*refreshRate | Pointer to the refresh rate. The value is an integer, in Hz. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityDpi()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityDpi(int32\_t \*densityDpi)

**Description**

Obtains the physical pixel density of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t \*densityDpi | Pointer to the physical pixel density, that is, the number of pixels per inch. The value is an integer, in px. The actual value depends on the options provided in device settings. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityPixels()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityPixels(float \*densityPixels)

**Description**

Obtains the logical pixel density of the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| float \*densityPixels | Pointer to the logical pixel density, which indicates the scaling coefficient of the physical pixels and logical pixels. The value is a floating-point number in the range \[0.5, 4.0\]. Generally, the value is **1.0** or **3.0**. The actual value depends on the density DPI provided by the device in use. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayScaledDensity()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayScaledDensity(float \*scaledDensity)

**Description**

Obtains the scale factor of fonts displayed on the default display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| float \*scaledDensity | Pointer to the scale factor. The value is a floating-point number, and it is usually the same as that of **densityPixels**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityXdpi()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityXdpi(float \*xDpi)

**Description**

Obtains the number of physical pixels per inch on the default display in the X dimension.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| float \*xDpi | Pointer to the number of physical pixels per inch in the X dimension. The value is a floating-point number. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityYdpi()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityYdpi(float \*yDpi)

**Description**

Obtains the number of physical pixels per inch on the default display in the Y dimension.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| float \*yDpi | Pointer to the number of physical pixels per inch in the Y dimension. The value is a floating-point number. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*\*cutoutInfo)

**Description**

Obtains the unusable area of the default display, including punch hole, notch, and curved area of a waterfall display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_CutoutInfo](../../structs/nativedisplaymanager-cutoutinfo/document.md) \*\*cutoutInfo | Double pointer to the unusable area information, which is encapsulated in [NativeDisplayManager\_CutoutInfo](../../structs/nativedisplaymanager-cutoutinfo/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*cutoutInfo)

**Description**

Destroys the unusable area of the default display, including punch hole, notch, and curved area of a waterfall display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_CutoutInfo](../../structs/nativedisplaymanager-cutoutinfo/document.md) \*cutoutInfo | Pointer to the unusable area information object, which is obtained by calling [OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo](#oh_nativedisplaymanager_createdefaultdisplaycutoutinfo). For details, see [NativeDisplayManager\_CutoutInfo](../../structs/nativedisplaymanager-cutoutinfo/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_IsFoldable()

bool OH\_NativeDisplayManager\_IsFoldable()

**Description**

Checks whether the current device is foldable.

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Check result for whether the device is foldable. **true** if foldable, **false** otherwise. |

#### \[h2\]OH\_NativeDisplayManager\_GetFoldDisplayMode()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetFoldDisplayMode(NativeDisplayManager\_FoldDisplayMode \*displayMode)

**Description**

Obtains the display mode of the foldable device.

**Since**: 12

**Device behavior differences**: This API returns **0** for 2-in-1 devices and non-foldable devices. For other devices, this API can be called properly.

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_FoldDisplayMode](../oh-display-info-h/document.md#nativedisplaymanager_folddisplaymode) \*displayMode | Pointer to the display mode. For details about the available options, see [NativeDisplayManager\_FoldDisplayMode](../oh-display-info-h/document.md#nativedisplaymanager_folddisplaymode). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DisplayChangeCallback()

typedef void (\*OH\_NativeDisplayManager\_DisplayChangeCallback)(uint64\_t displayId)

**Description**

Defines a callback function to listen for display status changes.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | ID of the display. |

#### \[h2\]OH\_NativeDisplayManager\_RegisterDisplayChangeListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayChangeListener(OH\_NativeDisplayManager\_DisplayChangeCallback displayChangeCallback, uint32\_t \*listenerIndex)

**Description**

Registers a listener for display status changes (such as rotation, refresh rate, DPI, and resolution changes).

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_NativeDisplayManager\_DisplayChangeCallback](#oh_nativedisplaymanager_displaychangecallback) displayChangeCallback | Callback function triggered when the display status is changed. For details, see [OH\_NativeDisplayManager\_DisplayChangeCallback](#oh_nativedisplaymanager_displaychangecallback). |
| uint32\_t \*listenerIndex | Pointer to the index of the listener registered. It can be used as an input parameter of [OH\_NativeDisplayManager\_UnregisterDisplayChangeListener](#oh_nativedisplaymanager_unregisterdisplaychangelistener). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterDisplayChangeListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(uint32\_t listenerIndex)

**Description**

Unregisters a listener for display status changes.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t listenerIndex | Index of the listener returned when [OH\_NativeDisplayManager\_RegisterDisplayChangeListener](#oh_nativedisplaymanager_registerdisplaychangelistener) is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback()

typedef void (\*OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback)(NativeDisplayManager\_FoldDisplayMode displayMode)

**Description**

Defines a callback function to listen for folded/unfolded state changes of the display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_FoldDisplayMode](../oh-display-info-h/document.md#nativedisplaymanager_folddisplaymode) displayMode | Folded or unfolded state of the display. For details about the available options, see [NativeDisplayManager\_FoldDisplayMode](../oh-display-info-h/document.md#nativedisplaymanager_folddisplaymode). |

#### \[h2\]OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener(OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32\_t \*listenerIndex)

**Description**

Registers a listener for folded/unfolded state changes of the display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback](#oh_nativedisplaymanager_folddisplaymodechangecallback) displayModeChangeCallback | Callback function triggered when the folded/unfolded state of the display is changed. For details, see [OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback](#oh_nativedisplaymanager_folddisplaymodechangecallback). |
| uint32\_t \*listenerIndex | Pointer to the index of the listener registered. It can be used as an input parameter of [OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener](#oh_nativedisplaymanager_unregisterfolddisplaymodechangelistener). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(uint32\_t listenerIndex)

**Description**

Unregisters a listener for folded/unfolded state changes of the display.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t listenerIndex | Index of the listener returned when [OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener](#oh_nativedisplaymanager_registerfolddisplaymodechangelistener) is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_CreateAllDisplays()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateAllDisplays(NativeDisplayManager\_DisplaysInfo \*\*allDisplays)

**Description**

Obtains the object that contains the information about all displays.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_DisplaysInfo](../../structs/nativedisplaymanager-displaysinfo/document.md) \*\*allDisplays | Double pointer to the display information, which is encapsulated in [NativeDisplayManager\_DisplaysInfo](../../structs/nativedisplaymanager-displaysinfo/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DestroyAllDisplays()

void OH\_NativeDisplayManager\_DestroyAllDisplays(NativeDisplayManager\_DisplaysInfo \*allDisplays)

**Description**

Destroys the object that contains the information about all displays.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_DisplaysInfo](../../structs/nativedisplaymanager-displaysinfo/document.md) \*allDisplays | Pointer to the display information object, which is obtained by calling [OH\_NativeDisplayManager\_CreateAllDisplays](#oh_nativedisplaymanager_createalldisplays). For details, see [NativeDisplayManager\_DisplaysInfo](../../structs/nativedisplaymanager-displaysinfo/document.md). |

#### \[h2\]OH\_NativeDisplayManager\_CreateDisplayById()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateDisplayById(uint32\_t displayId,NativeDisplayManager\_DisplayInfo \*\*displayInfo)

**Description**

Obtains the object that contains the information about a display.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t displayId | ID of the display. The value must be a non-negative integer. |
| [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md) \*\*displayInfo | Double pointer to the display information, which is encapsulated in [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DestroyDisplay()

void OH\_NativeDisplayManager\_DestroyDisplay(NativeDisplayManager\_DisplayInfo \*displayInfo)

**Description**

Destroys the object that contains the information about a display.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md) \*displayInfo | Pointer to the display information object, which is obtained by calling [OH\_NativeDisplayManager\_CreateDisplayById](#oh_nativedisplaymanager_createdisplaybyid) or [OH\_NativeDisplayManager\_CreatePrimaryDisplay](#oh_nativedisplaymanager_createprimarydisplay). For details, see [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md). |

#### \[h2\]OH\_NativeDisplayManager\_CreatePrimaryDisplay()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreatePrimaryDisplay(NativeDisplayManager\_DisplayInfo \*\*displayInfo)

**Description**

Obtains the object that contains the information about the primary display. For devices other than 2-in-1 devices, the displayInfo object obtained contains information about the built-in screen. For 2-in-1 devices with an external screen, the displayInfo object obtained contains information about the current primary screen. For 2-in-1 devices without an external screen, the displayInfo object obtained contains information about the built-in screen.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md) \*\*displayInfo | Double pointer to the display information, which is encapsulated in [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_AvailableAreaChangeCallback()

typedef void (\*OH\_NativeDisplayManager\_AvailableAreaChangeCallback)(uint64\_t displayId)

**Description**

Defines a callback function to listen for available area changes of a display.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | Display ID, which is a non-negative integer. |

#### \[h2\]OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener(OH\_NativeDisplayManager\_AvailableAreaChangeCallback availableAreaChangeCallback, uint32\_t \*listenerIndex)

**Description**

Registers a listener for available area changes of the display.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_NativeDisplayManager\_AvailableAreaChangeCallback](#oh_nativedisplaymanager_availableareachangecallback) availableAreaChangeCallback | 
Callback function triggered when the available area of the display changes.

For details, see [OH\_NativeDisplayManager\_AvailableAreaChangeCallback](#oh_nativedisplaymanager_availableareachangecallback).

 |
| uint32\_t \*listenerIndex | 

Pointer to the index of the listener registered.

It can be used as an input parameter of [OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener](#oh_nativedisplaymanager_unregisteravailableareachangelistener).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener(uint32\_t listenerIndex)

**Description**

Unregisters a listener for available area changes of the display.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t listenerIndex | 
Index of the listener returned

when [OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener](#oh_nativedisplaymanager_registeravailableareachangelistener) is called.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_CreateAvailableArea()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateAvailableArea(uint64\_t displayId, NativeDisplayManager\_Rect \*\*availableArea)

**Description**

Obtains the available area of a display.

**Since**: 20

**Device behavior differences**: This API can be properly called on 2-in-1 devices and tablets. It does not work for other device types. To obtain the available screen area on the current device, call [OH\_NativeDisplayManager\_GetDefaultDisplayWidth()](#oh_nativedisplaymanager_getdefaultdisplaywidth) and [OH\_NativeDisplayManager\_GetDefaultDisplayHeight()](#oh_nativedisplaymanager_getdefaultdisplayheight).

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | Display ID, which is a non-negative integer. |
| [NativeDisplayManager\_Rect](../../structs/nativedisplaymanager-rect/document.md) \*\*availableArea | Double pointer to the available area of the display. For details, see [NativeDisplayManager\_Rect](../../structs/nativedisplaymanager-rect/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DestroyAvailableArea()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_DestroyAvailableArea(NativeDisplayManager\_Rect \*availableArea)

**Description**

Destroys the available area of a display.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [NativeDisplayManager\_Rect](../../structs/nativedisplaymanager-rect/document.md) \*availableArea | 
Pointer to the available area, which is obtained by calling [OH\_NativeDisplayManager\_CreateAvailableArea](#oh_nativedisplaymanager_createavailablearea).

For details about the available area, see [NativeDisplayManager\_Rect](../../structs/nativedisplaymanager-rect/document.md).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DisplayAddCallback()

typedef void (\*OH\_NativeDisplayManager\_DisplayAddCallback)(uint64\_t displayId)

**Description**

Defines a callback function to listen for display addition events.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | Display ID, which is a non-negative integer. |

#### \[h2\]OH\_NativeDisplayManager\_RegisterDisplayAddListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayAddListener(OH\_NativeDisplayManager\_DisplayAddCallback displayAddCallback, uint32\_t \*listenerIndex)

**Description**

Registers a listener for display addition events (for example, monitor inserted).

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_NativeDisplayManager\_DisplayAddCallback](#oh_nativedisplaymanager_displayaddcallback) displayAddCallback | Callback function triggered when a display is added. For details, see [OH\_NativeDisplayManager\_DisplayAddCallback](#oh_nativedisplaymanager_displayaddcallback). |
| uint32\_t \*listenerIndex | 
Pointer to the index of the listener registered.

It can be used as an input parameter of [OH\_NativeDisplayManager\_UnregisterDisplayAddListener](#oh_nativedisplaymanager_unregisterdisplayaddlistener).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterDisplayAddListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayAddListener(uint32\_t listenerIndex)

**Description**

Unregisters a listener for display addition events.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t listenerIndex | Index of the listener returned when [OH\_NativeDisplayManager\_RegisterDisplayAddListener](#oh_nativedisplaymanager_registerdisplayaddlistener) is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_DisplayRemoveCallback()

typedef void (\*OH\_NativeDisplayManager\_DisplayRemoveCallback)(uint64\_t displayId)

**Description**

Defines a callback function to listen for display removal events.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | Display ID, which is a non-negative integer. |

#### \[h2\]OH\_NativeDisplayManager\_RegisterDisplayRemoveListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayRemoveListener(OH\_NativeDisplayManager\_DisplayRemoveCallback displayRemoveCallback, uint32\_t \*listenerIndex)

**Description**

Registers a listener for display removal events (for example, monitor removed).

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_NativeDisplayManager\_DisplayRemoveCallback](#oh_nativedisplaymanager_displayremovecallback) displayRemoveCallback | Callback function triggered when a display is removed. For details, see [OH\_NativeDisplayManager\_DisplayRemoveCallback](#oh_nativedisplaymanager_displayremovecallback). |
| uint32\_t \*listenerIndex | 
Pointer to the index of the listener registered.

It can be used as an input parameter of [OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener](#oh_nativedisplaymanager_unregisterdisplayremovelistener).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener(uint32\_t listenerIndex)

**Description**

Unregisters the listener for display removal events.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t listenerIndex | Index of the listener returned when [OH\_NativeDisplayManager\_RegisterDisplayRemoveListener](#oh_nativedisplaymanager_registerdisplayremovelistener) is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDisplaySourceMode()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDisplaySourceMode(uint64\_t displayId, NativeDisplayManager\_SourceMode \*sourceMode)

**Description**

Obtains the source mode of a display.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | Display ID, which is a non-negative integer. |
| [NativeDisplayManager\_SourceMode](../oh-display-info-h/document.md#nativedisplaymanager_sourcemode) \*sourceMode | Pointer to the source mode. For details about the available options, see [NativeDisplayManager\_SourceMode](../oh-display-info-h/document.md#nativedisplaymanager_sourcemode). |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |

#### \[h2\]OH\_NativeDisplayManager\_GetDisplayPosition()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDisplayPosition(uint64\_t displayId, int32\_t \*x, int32\_t \*y)

**Description**

Obtains the position of a display.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint64\_t displayId | Display ID, which is a non-negative integer. |
| int32\_t \*x | Pointer to the X coordinate of the top-left corner of the primary screen. |
| int32\_t \*y | Pointer to the Y coordinate of the top-left corner of the primary screen. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | 
Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode).

Currently, only the primary screen and extended screen support position information query. Queries for other screens return **DISPLAY\_MANAGER\_ERROR\_ILLEGAL\_PARAM**.

 |
