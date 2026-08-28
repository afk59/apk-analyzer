# oh\_display\_info.h

#### Overview

The file declares the common enums and definitions of the display.

**File to include**: <window\_manager/oh\_display\_info.h>

**Library**: libnative\_display\_manager.so

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Since**: 12

**Related module**: [OH\_DisplayManager](../../modules/oh-displaymanager/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativeDisplayManager\_Rect](../../structs/nativedisplaymanager-rect/document.md) | NativeDisplayManager\_Rect | Describes a rectangle. |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](../../structs/nativedisplaymanager-waterfalldisplayarearects/document.md) | NativeDisplayManager\_WaterfallDisplayAreaRects | Describes the curved area on a waterfall display. |
| [NativeDisplayManager\_CutoutInfo](../../structs/nativedisplaymanager-cutoutinfo/document.md) | NativeDisplayManager\_CutoutInfo | Describes the unusable area of a display, including punch hole, notch, and curved area of a waterfall display. |
| [NativeDisplayManager\_DisplayHdrFormat](../../structs/nativedisplaymanager-displayhdrformat/document.md) | NativeDisplayManager\_DisplayHdrFormat | Describes all the HDR formats supported by a display. |
| [NativeDisplayManager\_DisplayColorSpace](../../structs/nativedisplaymanager-displaycolorspace/document.md) | NativeDisplayManager\_DisplayColorSpace | Describes all the color spaces supported by a display. |
| [NativeDisplayManager\_DisplayInfo](../../structs/nativedisplaymanager-displayinfo/document.md) | NativeDisplayManager\_DisplayInfo | Describes the information about a display. |
| [NativeDisplayManager\_DisplaysInfo](../../structs/nativedisplaymanager-displaysinfo/document.md) | NativeDisplayManager\_DisplaysInfo | Describes the information about displays of a device with multiple screens. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [OH\_DISPLAY\_NAME\_LENGTH](#oh_display_name_length) 32 | Maximum length of a display name. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativeDisplayManager\_Rotation](#nativedisplaymanager_rotation) | NativeDisplayManager\_Rotation | Enumerates the clockwise rotation angles of a display. |
| [NativeDisplayManager\_Orientation](#nativedisplaymanager_orientation) | NativeDisplayManager\_Orientation | Enumerates the orientations of a display. |
| [NativeDisplayManager\_ErrorCode](#nativedisplaymanager_errorcode) | NativeDisplayManager\_ErrorCode | Enumerates the status codes returned by the display manager interface. |
| [NativeDisplayManager\_FoldDisplayMode](#nativedisplaymanager_folddisplaymode) | NativeDisplayManager\_FoldDisplayMode | Enumerates the display modes of a foldable device. |
| [NativeDisplayManager\_DisplayState](#nativedisplaymanager_displaystate) | NativeDisplayManager\_DisplayState | Enumerates the states of a display. |
| [NativeDisplayManager\_SourceMode](#nativedisplaymanager_sourcemode) | NativeDisplayManager\_SourceMode | Enumerates the source modes of a device. |

#### Macro Description

#### \[h2\]OH\_DISPLAY\_NAME\_LENGTH

#define OH\_DISPLAY\_NAME\_LENGTH 32

**Description**

Maximum length of a display name.

**Since**: 14

#### Enum Description

#### \[h2\]NativeDisplayManager\_Rotation

enum NativeDisplayManager\_Rotation

**Description**

Enumerates the clockwise rotation angles of a display.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DISPLAY\_MANAGER\_ROTATION\_0 = 0 | The display is rotated clockwise by 0 degrees. |
| DISPLAY\_MANAGER\_ROTATION\_90 = 1 | The display is rotated clockwise by 90 degrees. |
| DISPLAY\_MANAGER\_ROTATION\_180 = 2 | The display is rotated clockwise by 180 degrees. |
| DISPLAY\_MANAGER\_ROTATION\_270 = 3 | The display is rotated clockwise by 270 degrees. |

#### \[h2\]NativeDisplayManager\_Orientation

enum NativeDisplayManager\_Orientation

**Description**

Enumerates the orientations of a display.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DISPLAY\_MANAGER\_PORTRAIT = 0 | The display is in portrait mode. |
| DISPLAY\_MANAGER\_LANDSCAPE = 1 | The display is in landscape mode. |
| DISPLAY\_MANAGER\_PORTRAIT\_INVERTED = 2 | The display is in reverse portrait mode. |
| DISPLAY\_MANAGER\_LANDSCAPE\_INVERTED = 3 | The display is in reverse landscape mode. |
| DISPLAY\_MANAGER\_UNKNOWN | The screen orientation is unknown. |

#### \[h2\]NativeDisplayManager\_ErrorCode

enum NativeDisplayManager\_ErrorCode

**Description**

Enumerates the status codes returned by the display manager interface.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DISPLAY\_MANAGER\_OK = 0 | Success. |
| DISPLAY\_MANAGER\_ERROR\_NO\_PERMISSION = 201 | Permission verification fails. The application does not have the permission to use the API. |
| DISPLAY\_MANAGER\_ERROR\_NOT\_SYSTEM\_APP = 202 | Permission verification fails. A non-system application attempts to call a system API. |
| DISPLAY\_MANAGER\_ERROR\_INVALID\_PARAM = 401 | Parameter check fails. |
| DISPLAY\_MANAGER\_ERROR\_DEVICE\_NOT\_SUPPORTED = 801 | The device does not support the API. |
| DISPLAY\_MANAGER\_ERROR\_INVALID\_SCREEN = 1400001 | The display is invalid. |
| DISPLAY\_MANAGER\_ERROR\_INVALID\_CALL = 1400002 | The current operation object does not have the operation permission. |
| DISPLAY\_MANAGER\_ERROR\_SYSTEM\_ABNORMAL = 1400003 | The system service is abnormal. |
| DISPLAY\_MANAGER\_ERROR\_ILLEGAL\_PARAM = 1400004 | 
Invalid parameter.

**Since**: 20

 |

#### \[h2\]NativeDisplayManager\_FoldDisplayMode

enum NativeDisplayManager\_FoldDisplayMode

**Description**

Enumerates the display modes of a foldable device.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_UNKNOWN = 0 | The display mode of the device is unknown. |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_FULL = 1 | The device is displayed in full screen. |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_MAIN = 2 | The main screen of the device is displayed. |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_SUB = 3 | The subscreen of the device is displayed. |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_COORDINATION = 4 | Both screens of the device are displayed in collaborative mode. |

#### \[h2\]NativeDisplayManager\_DisplayState

enum NativeDisplayManager\_DisplayState

**Description**

Enumerates the states of a display.

**Since**: 14

| Enum Item | Description |
| :-- | :-- |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_UNKNOWN = 0 | Unknown. |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_OFF = 1 | The display is shut down. |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_ON = 2 | The display is powered on. |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_DOZE = 3 | The display is in sleep mode. |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_DOZE\_SUSPEND = 4 | The display is in sleep mode, and the CPU is suspended. |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_VR = 5 | The display is in VR mode. |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_ON\_SUSPEND = 6 | The display is powered on, and the CPU is suspended. |

#### \[h2\]NativeDisplayManager\_SourceMode

enum NativeDisplayManager\_SourceMode

**Description**

Enumerates the source modes of a device.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| DISPLAY\_SOURCE\_MODE\_NONE = 0 | The device is currently not in use. |
| DISPLAY\_SOURCE\_MODE\_MAIN = 1 | The primary screen of the device is currently in use. |
| DISPLAY\_SOURCE\_MODE\_MIRROR = 2 | The device is currently in mirror display mode. |
| DISPLAY\_SOURCE\_MODE\_EXTEND = 3 | The device is currently in extended display mode. |
| DISPLAY\_SOURCE\_MODE\_ALONE = 4 | The device is currently in independent display mode. |
