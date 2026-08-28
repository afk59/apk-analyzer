# oh\_window\_comm.h

#### Overview

The file declares the common enums and definitions of the window manager.

**File to include**: <window\_manager/oh\_window\_comm.h>

**Library**: libnative\_window\_manager.so

**System capability**: SystemCapability.Window.SessionManager

**Since**: 12

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [WindowManager\_Rect](../../structs/windowmanager-rect/document.md) | WindowManager\_Rect | Describes the window rectangle, including the window position, width, and height. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative--00020177/document.md) | OH\_PixelmapNative | Describes the pixel image information. |
| [WindowManager\_WindowProperties](../../structs/windowmanager-windowproperties/document.md) | WindowManager\_WindowProperties | Describes the window properties. |
| [WindowManager\_AvoidArea](../../structs/windowmanager-avoidarea/document.md) | WindowManager\_AvoidArea | Describes the avoid area. |
| [WindowManager\_MainWindowInfo](../../structs/windowmanager-mainwindowinfo/document.md) | WindowManager\_MainWindowInfo | Describes the main window information. |
| [WindowManager\_WindowSnapshotConfig](../../structs/windowmanager-windowsnapshotconfig/document.md) | WindowManager\_WindowSnapshotConfig | Describes the configuration of the main window screenshot. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [WindowManager\_ErrorCode](#windowmanager_errorcode) | WindowManager\_ErrorCode | Enumerates the status codes returned by the window manager interface. |
| [WindowManager\_AvoidAreaType](#windowmanager_avoidareatype) | WindowManager\_AvoidAreaType | Enumerates the avoid area types. |
| [WindowManager\_WindowType](#windowmanager_windowtype) | WindowManager\_WindowType | Enumerates the window types. |

#### Enum Description

#### \[h2\]WindowManager\_ErrorCode

enum WindowManager\_ErrorCode

**Description**

Enumerates the status codes returned by the window manager interface.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OK = 0 | Operation successful. |
| WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION = 201 | 
No permission.

**Since**: 15

 |
| WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM = 401 | 

Invalid parameter.

**Since**: 15

 |
| WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED = 801 | 

Not supported by the device.

**Since**: 15

 |
| INVAILD\_WINDOW\_ID = 1000 | Invalid window ID. |
| SERVICE\_ERROR = 2000 | Service error. |
| WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL = 1300002 | 

Abnormal window status.

**Since**: 15

 |
| WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL = 1300003 | 

Abnormal window manager service.

**Since**: 15

 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_DESTROY\_FAILED = 1300011 | 

Failed to destroy the PiP window.

**Since**: 20

 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_STATE\_ABNORMAL = 1300012 | 

Abnormal PiP status.

**Since**: 20

 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_CREATE\_FAILED = 1300013 | 

Failed to create the PiP window.

**Since**: 20

 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR = 1300014 | 

An internal error occurs in PiP. Possible causes:

1\. The window on which the PiP feature depends is abnormal. For example, the window is empty. 2. The PiP controller is abnormal.

**Since**: 20

 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_REPEATED\_OPERATION = 1300015 | 

Repeated PiP operation.

**Since**: 20

 |
| WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM = 1300016 | 

Incorrect parameter. Possible causes:

1\. The parameter value range is invalid. 2. The number of parameters is invalid. 3. The parameter type is invalid.

**Since**: 20

 |

#### \[h2\]WindowManager\_AvoidAreaType

enum WindowManager\_AvoidAreaType

**Description**

Enumerates the avoid area types.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_SYSTEM = 0 | System avoid area. |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_CUTOUT = 1 | Cutout area. |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_SYSTEM\_GESTURE = 2 | System gesture area. |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_KEYBOARD = 3 | Keyboard area. |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_NAVIGATION\_INDICATOR = 4 | Navigation bar area. |

#### \[h2\]WindowManager\_WindowType

enum WindowManager\_WindowType

**Description**

Enumerates the window types.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_APP = 0 | Child window. |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_MAIN = 1 | Main window. |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_FLOAT = 8 | Floating window. |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_DIALOG = 16 | Modal window. |
