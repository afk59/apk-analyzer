# oh\_window\_pip.h

#### Overview

The file declares the APIs related to the Picture in Picture (PiP) feature, including creating and deleting a PiP controller, and starting and stopping PiP. PiP is mainly used in video playback, live streaming, video calls, or video meetings.

**File to include**: <window\_manager/oh\_window\_pip.h>

**Library**: libnative\_window\_manager.so

**System capability**: SystemCapability.Window.SessionManager

**Since**: 20

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

#### Summary

#### \[h2\]Structs

| Name | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) | Describes the PiP configuration. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [PictureInPicture\_PipTemplateType](#pictureinpicture_piptemplatetype) | PictureInPicture\_PipTemplateType | Enumerates the types of PiP templates. |
| [PictureInPicture\_PipControlGroup](#pictureinpicture_pipcontrolgroup) | PictureInPicture\_PipControlGroup | Enumerates the types of component groups displayed on the PiP controller. |
| [PictureInPicture\_PipControlType](#pictureinpicture_pipcontroltype) | PictureInPicture\_PipControlType | Enumerates the types of components displayed on the PiP controller. |
| [PictureInPicture\_PipControlStatus](#pictureinpicture_pipcontrolstatus) | PictureInPicture\_PipControlStatus | Enumerates the statuses of components displayed on the PiP controller. |
| [PictureInPicture\_PipState](#pictureinpicture_pipstate) | PictureInPicture\_PipState | Enumerates the PiP lifecycle states. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*WebPipStartPipCallback)(uint32\_t controllerId, uint8\_t requestId, uint64\_t surfaceId)](#webpipstartpipcallback) | WebPipStartPipCallback | Defines a callback function for PiP window creation. |
| [typedef void (\*WebPipLifecycleCallback)(uint32\_t controllerId, PictureInPicture\_PipState state, int32\_t errcode)](#webpiplifecyclecallback) | WebPipLifecycleCallback | Defines a callback function for PiP window lifecycle changes. |
| [typedef void (\*WebPipControlEventCallback)(uint32\_t controllerId, PictureInPicture\_PipControlType controlType,PictureInPicture\_PipControlStatus status)](#webpipcontroleventcallback) | WebPipControlEventCallback | Defines a callback function for the component click event of the PiP window. |
| [typedef void (\*WebPipResizeCallback)(uint32\_t controllerId, uint32\_t width, uint32\_t height, double scale)](#webpipresizecallback) | WebPipResizeCallback | Defines a callback function for PiP window size changes. |
| [int32\_t OH\_PictureInPicture\_CreatePipConfig(PictureInPicture\_PipConfig\* pipConfig)](#oh_pictureinpicture_createpipconfig) | \- | Creates a PiP configuration. |
| [int32\_t OH\_PictureInPicture\_DestroyPipConfig(PictureInPicture\_PipConfig\* pipConfig)](#oh_pictureinpicture_destroypipconfig) | \- | Destroys a PiP configuration. |
| [int32\_t OH\_PictureInPicture\_SetPipMainWindowId(PictureInPicture\_PipConfig pipConfig, uint32\_t mainWindowId)](#oh_pictureinpicture_setpipmainwindowid) | \- | Sets the ID of the main window that launches PiP. |
| [int32\_t OH\_PictureInPicture\_SetPipTemplateType(PictureInPicture\_PipConfig pipConfig,PictureInPicture\_PipTemplateType pipTemplateType)](#oh_pictureinpicture_setpiptemplatetype) | \- | Sets the PiP template type. The default value is video playback. |
| [int32\_t OH\_PictureInPicture\_SetPipRect(PictureInPicture\_PipConfig pipConfig, uint32\_t width, uint32\_t height)](#oh_pictureinpicture_setpiprect) | \- | Sets the size of the PiP window for calculating the aspect ratio. |
| [int32\_t OH\_PictureInPicture\_SetPipControlGroup(PictureInPicture\_PipConfig pipConfig,PictureInPicture\_PipControlGroup\* controlGroup, uint8\_t controlGroupLength)](#oh_pictureinpicture_setpipcontrolgroup) | \- | Sets a PiP component group, which must match the template type. |
| [int32\_t OH\_PictureInPicture\_SetPipNapiEnv(PictureInPicture\_PipConfig pipConfig, void\* env)](#oh_pictureinpicture_setpipnapienv) | \- | Sets the runtime environment for launching PiP. |
| [int32\_t OH\_PictureInPicture\_CreatePip(PictureInPicture\_PipConfig pipConfig, uint32\_t\* controllerId)](#oh_pictureinpicture_createpip) | \- | Creates a PiP controller. |
| [int32\_t OH\_PictureInPicture\_DeletePip(uint32\_t controllerId)](#oh_pictureinpicture_deletepip) | \- | Deletes a PiP controller. |
| [int32\_t OH\_PictureInPicture\_StartPip(uint32\_t controllerId)](#oh_pictureinpicture_startpip) | \- | Starts PiP. |
| [int32\_t OH\_PictureInPicture\_StopPip(uint32\_t controllerId)](#oh_pictureinpicture_stoppip) | \- | Stops PiP. |
| [int32\_t OH\_PictureInPicture\_UpdatePipContentSize(uint32\_t controllerId, uint32\_t width, uint32\_t height)](#oh_pictureinpicture_updatepipcontentsize) | \- | Updates the media content size when the media content changes. |
| [int32\_t OH\_PictureInPicture\_UpdatePipControlStatus(uint32\_t controllerId, PictureInPicture\_PipControlType controlType,PictureInPicture\_PipControlStatus status)](#oh_pictureinpicture_updatepipcontrolstatus) | \- | Updates the PiP component status. |
| [int32\_t OH\_PictureInPicture\_SetPipControlEnabled(uint32\_t controllerId, PictureInPicture\_PipControlType controlType,bool enabled)](#oh_pictureinpicture_setpipcontrolenabled) | \- | Sets the PiP component enabled status. |
| [int32\_t OH\_PictureInPicture\_RegisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)](#oh_pictureinpicture_registerstartpipcallback) | \- | Registers a callback to listen for the completion of PiP surface creation. |
| [int32\_t OH\_PictureInPicture\_UnregisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)](#oh_pictureinpicture_unregisterstartpipcallback) | \- | Unregisters the callback used to listen for the completion of PiP surface creation. |
| [int32\_t OH\_PictureInPicture\_UnregisterAllStartPipCallbacks(uint32\_t controllerId)](#oh_pictureinpicture_unregisterallstartpipcallbacks) | \- | Unregisters all the callbacks used to listen for the completion of PiP surface creation. |
| [int32\_t OH\_PictureInPicture\_RegisterLifecycleListener(uint32\_t controllerId, WebPipLifecycleCallback callback)](#oh_pictureinpicture_registerlifecyclelistener) | \- | Registers a callback to listen for PiP lifecycle state changes. |
| [int32\_t OH\_PictureInPicture\_UnregisterLifecycleListener(uint32\_t controllerId, WebPipLifecycleCallback callback)](#oh_pictureinpicture_unregisterlifecyclelistener) | \- | Unregisters the callback used to listen for PiP lifecycle state changes. |
| [int32\_t OH\_PictureInPicture\_UnregisterAllLifecycleListeners(uint32\_t controllerId)](#oh_pictureinpicture_unregisteralllifecyclelisteners) | \- | Unregisters all the callbacks used to listen for PiP lifecycle state changes. |
| [int32\_t OH\_PictureInPicture\_RegisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)](#oh_pictureinpicture_registercontroleventlistener) | \- | Registers a callback to listen for control panel action events in PiP mode. |
| [int32\_t OH\_PictureInPicture\_UnregisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)](#oh_pictureinpicture_unregistercontroleventlistener) | \- | Unregisters the callback used to listen for control panel action events in PiP mode. |
| [int32\_t OH\_PictureInPicture\_UnregisterAllControlEventListeners(uint32\_t controllerId)](#oh_pictureinpicture_unregisterallcontroleventlisteners) | \- | Unregisters all the callbacks used to listen for control panel action events in PiP mode. |
| [int32\_t OH\_PictureInPicture\_RegisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)](#oh_pictureinpicture_registerresizelistener) | \- | Registers a callback to listen for PiP window size changes. |
| [int32\_t OH\_PictureInPicture\_UnregisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)](#oh_pictureinpicture_unregisterresizelistener) | \- | Unregisters the callback used to listen for PiP window size changes. |
| [int32\_t OH\_PictureInPicture\_UnregisterAllResizeListeners(uint32\_t controllerId)](#oh_pictureinpicture_unregisterallresizelisteners) | \- | Unregisters all the callbacks used to listen for PiP window size changes. |
| [int32\_t OH\_PictureInPicture\_SetPipInitialSurfaceRect(uint32\_t controllerId, int32\_t positionX, int32\_t positionY,uint32\_t width, uint32\_t height)](#oh_pictureinpicture_setpipinitialsurfacerect) | \- | Sets the initial position and size of the PiP surface when the PiP launch animation starts. It can be used to achieve a seamless transition effect. |
| [int32\_t OH\_PictureInPicture\_UnsetPipInitialSurfaceRect(uint32\_t controllerId)](#oh_pictureinpicture_unsetpipinitialsurfacerect) | \- | Cancels the previously set initial position and size for the PiP surface. |
| [int32\_t OH\_PictureInPicture\_SetParentWindowId(uint32\_t controllerId, uint32\_t windowId)](#oh_pictureinpicture_setparentwindowid) | \- | Sets the main window ID for PiP. |

#### Enum Description

#### \[h2\]PictureInPicture\_PipTemplateType

enum PictureInPicture\_PipTemplateType

**Description**

Enumerates the types of PiP templates.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_PLAY = 0 | Video playback template. A PiP window will be started during video playback, and the video playback template is loaded. |
| VIDEO\_CALL = 1 | Video call template. A PiP window will be started during a video call, and the video call template will be loaded. |
| VIDEO\_MEETING = 2 | Video meeting template. A PiP window will be started during a video meeting, and the video meeting template will be loaded. |
| VIDEO\_LIVE = 3 | Live template. A PiP window will be started during a live, and the live template is loaded. |

#### \[h2\]PictureInPicture\_PipControlGroup

enum PictureInPicture\_PipControlGroup

**Description**

Enumerates the types of component groups displayed on the PiP controller.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_PLAY\_VIDEO\_PREVIOUS\_NEXT = 101 | Previous/Next component group for video playback. This component group is mutually exclusive with the fast-forward/rewind component group. It cannot be added if the fast-forward/rewind component group is added. |
| VIDEO\_PLAY\_FAST\_FORWARD\_BACKWARD = 102 | Fast-forward/Rewind component group for video playback. This component group is mutually exclusive with the previous/next component group. It cannot be added if the previous/next component group is added. |
| VIDEO\_CALL\_MICROPHONE\_SWITCH = 201 | Microphone on/off component group for video calls. |
| VIDEO\_CALL\_HANG\_UP\_BUTTON = 202 | Hang-up component group for video calls. |
| VIDEO\_CALL\_CAMERA\_SWITCH = 203 | Camera on/off component group for video calls. |
| VIDEO\_CALL\_MUTE\_SWITCH = 204 | Mute component group for video calls. |
| VIDEO\_MEETING\_HANG\_UP\_BUTTON = 301 | Hang-up component group for video meetings. |
| VIDEO\_MEETING\_CAMERA\_SWITCH = 302 | Camera on/off component group for video meetings. |
| VIDEO\_MEETING\_MUTE\_SWITCH = 303 | Mute component group for video meetings. |
| VIDEO\_MEETING\_MICROPHONE\_SWITCH = 304 | Microphone on/off component group for video meetings. |
| VIDEO\_LIVE\_VIDEO\_PLAY\_PAUSE = 401 | Play/Pause component group for live streaming. |
| VIDEO\_LIVE\_MUTE\_SWITCH = 402 | Mute component group for live streaming. |

#### \[h2\]PictureInPicture\_PipControlType

enum PictureInPicture\_PipControlType

**Description**

Enumerates the types of components displayed on the PiP controller.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_PLAY\_PAUSE = 0 | Play/Pause component. |
| VIDEO\_PREVIOUS = 1 | Previous component in video scenarios. |
| VIDEO\_NEXT = 2 | Next component in video scenarios. |
| FAST\_FORWARD = 3 | Fast-forward component in video scenarios. |
| FAST\_BACKWARD = 4 | Rewind component in video scenarios. |
| HANG\_UP\_BUTTON = 5 | Hang-up component. |
| MICROPHONE\_SWITCH = 6 | Microphone on/off component. |
| CAMERA\_SWITCH = 7 | Camera on/off component. |
| MUTE\_SWITCH = 8 | Mute/Unmute component. |

#### \[h2\]PictureInPicture\_PipControlStatus

enum PictureInPicture\_PipControlStatus

**Description**

Enumerates the statuses of components displayed on the PiP controller.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| PLAY = 1 | A video is playing. |
| PAUSE = 0 | A video is paused. |
| OPEN = 1 | The camera, microphone, and mute components are enabled. |
| CLOSE = 0 | The camera, microphone, and mute components are disabled. |

#### \[h2\]PictureInPicture\_PipState

enum PictureInPicture\_PipState

**Description**

Enumerates the PiP lifecycle states.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| ABOUT\_TO\_START = 1 | PiP is about to start. |
| STARTED = 2 | PiP is started. |
| ABOUT\_TO\_STOP = 3 | PiP is about to stop. |
| STOPPED = 4 | PiP is stopped. |
| ABOUT\_TO\_RESTORE = 5 | The original page is about to restore. |
| ERROR = 6 | An error occurs during the execution of the PiP lifecycle. |

#### Function Description

#### \[h2\]WebPipStartPipCallback()

typedef void (\*WebPipStartPipCallback)(uint32\_t controllerId, uint8\_t requestId, uint64\_t surfaceId)

**Description**

Defines a callback function for PiP window creation.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| uint8\_t requestId | Request ID, which indicates the number of times the PiP window has been requested to be pulled up. |
| uint64\_t surfaceId | Surface ID of the **XComponent** in PiP. It is used for application rendering. |

#### \[h2\]WebPipLifecycleCallback()

typedef void (\*WebPipLifecycleCallback)(uint32\_t controllerId, PictureInPicture\_PipState state, int32\_t errcode)

**Description**

Defines a callback function for PiP window lifecycle changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| PictureInPicture\_PipState state | PiP lifecycle state. |
| int32\_t errcode | Common status codes of PiP APIs. For details, see [WindowManager\_ErrorCode](../oh-window-comm-h/document.md#windowmanager_errorcode). |

#### \[h2\]WebPipControlEventCallback()

typedef void (\*WebPipControlEventCallback)(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, PictureInPicture\_PipControlStatus status)

**Description**

Defines a callback function for the component click event of the PiP window.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| PictureInPicture\_PipControlType controlType | Type of component displayed on the PiP controller. |
| [PictureInPicture\_PipControlStatus](#pictureinpicture_pipcontrolstatus) status | Status of the component displayed on the PiP controller. |

#### \[h2\]WebPipResizeCallback()

typedef void (\*WebPipResizeCallback)(uint32\_t controllerId, uint32\_t width, uint32\_t height, double scale)

**Description**

Defines a callback function for PiP window size changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| uint32\_t width | PiP window width, in px. The value is a positive integer and cannot be greater than the screen width. |
| uint32\_t height | PiP window height, in px. The value is a positive integer and cannot be greater than the screen height. |
| double scale | Scale factor of the PiP window, representing the display size relative to the width and height. The value is a floating-point number in the range (0.0, 1.0\]. The value **1** means that the PiP window matches the specified width and height. |

#### \[h2\]OH\_PictureInPicture\_CreatePipConfig()

int32\_t OH\_PictureInPicture\_CreatePipConfig(PictureInPicture\_PipConfig\* pipConfig)

**Description**

Creates a PiP configuration.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md)\* pipConfig | Pointer to the PiP parameter configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureInPicture\_DestroyPipConfig()

int32\_t OH\_PictureInPicture\_DestroyPipConfig(PictureInPicture\_PipConfig\* pipConfig)

**Description**

Destroys a PiP configuration.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md)\* pipConfig | Pointer to the PiP configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipMainWindowId()

int32\_t OH\_PictureInPicture\_SetPipMainWindowId(PictureInPicture\_PipConfig pipConfig, uint32\_t mainWindowId)

**Description**

Sets the ID of the main window that launches PiP.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) pipConfig | PiP configuration. |
| uint32\_t mainWindowId | ID of the main window that launches PiP. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipTemplateType()

int32\_t OH\_PictureInPicture\_SetPipTemplateType(PictureInPicture\_PipConfig pipConfig, PictureInPicture\_PipTemplateType pipTemplateType)

**Description**

Sets the PiP template type. The default value is video playback.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) pipConfig | PiP configuration. |
| [PictureInPicture\_PipTemplateType](#pictureinpicture_piptemplatetype) pipTemplateType | Type of the PiP template. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipRect()

int32\_t OH\_PictureInPicture\_SetPipRect(PictureInPicture\_PipConfig pipConfig, uint32\_t width, uint32\_t height)

**Description**

Sets the size of the PiP window for calculating the aspect ratio.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) pipConfig | PiP configuration. |
| uint32\_t width | Width of the original content, in px. The value must be a positive integer. It is used to determine the aspect ratio of the PiP window. |
| uint32\_t height | Height of the original content, in px. The value must be a positive integer. It is used to determine the aspect ratio of the PiP window. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipControlGroup()

int32\_t OH\_PictureInPicture\_SetPipControlGroup(PictureInPicture\_PipConfig pipConfig, PictureInPicture\_PipControlGroup\* controlGroup, uint8\_t controlGroupLength)

**Description**

Sets a PiP component group, which must match the template type.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) pipConfig | PiP configuration. |
| [PictureInPicture\_PipControlGroup](#pictureinpicture_pipcontrolgroup)\* controlGroup | Pointer to an optional component group of the PiP controller. An application can configure whether to display these optional components. If this parameter is not set for an application, the basic components (for example, play/pause of the video playback component group) are displayed. A maximum of three components can be configured. |
| uint8\_t controlGroupLength | Number of components in the PiP component group. The value ranges from 0 to 3. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipNapiEnv()

int32\_t OH\_PictureInPicture\_SetPipNapiEnv(PictureInPicture\_PipConfig pipConfig, void\* env)

**Description**

Sets the runtime environment for launching PiP.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) pipConfig | PiP configuration. |
| void\* env | Pointer to the NAPI environment. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

 |

#### \[h2\]OH\_PictureInPicture\_CreatePip()

int32\_t OH\_PictureInPicture\_CreatePip(PictureInPicture\_PipConfig pipConfig, uint32\_t\* controllerId)

**Description**

Creates a PiP controller.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [PictureInPicture\_PipConfig](../../structs/pictureinpicture-pipconfig/document.md) pipConfig | PiP configuration. |
| uint32\_t\* controllerId | Pointer to the ID of the PiP controller created. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_DeletePip()

int32\_t OH\_PictureInPicture\_DeletePip(uint32\_t controllerId)

**Description**

Deletes a PiP controller.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureInPicture\_StartPip()

int32\_t OH\_PictureInPicture\_StartPip(uint32\_t controllerId)

**Description**

Starts PiP.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_STATE\_ABNORMAL**: The PiP window is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_CREATE\_FAILED**: Creating the PiP window fails.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_REPEATED\_OPERATION**: The PiP window is manipulated repeatedly.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureInPicture\_StopPip()

int32\_t OH\_PictureInPicture\_StopPip(uint32\_t controllerId)

**Description**

Stops PiP.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_DESTROY\_FAILED**: Destroying the PiP window fails.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_STATE\_ABNORMAL**: The PiP window is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_REPEATED\_OPERATION**: The PiP window is manipulated repeatedly.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureInPicture\_UpdatePipContentSize()

int32\_t OH\_PictureInPicture\_UpdatePipContentSize(uint32\_t controllerId, uint32\_t width, uint32\_t height)

**Description**

Updates the media content size when the media content changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| uint32\_t width | Width of the media content, in px. The value must be a positive integer. It is used to update the aspect ratio of the PiP window. |
| uint32\_t height | Height of the media content, in px. The value must be a positive integer. It is used to update the aspect ratio of the PiP window. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UpdatePipControlStatus()

int32\_t OH\_PictureInPicture\_UpdatePipControlStatus(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, PictureInPicture\_PipControlStatus status)

**Description**

Updates the PiP component status.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [PictureInPicture\_PipControlType](#pictureinpicture_pipcontroltype) controlType | Type of the component displayed on the PiP controller. Currently, only **VIDEO\_PLAY\_PAUSE**, **MICROPHONE\_SWITCH**, **CAMERA\_SWITCH**, and **MUTE\_SWITCH** are supported. |
| [PictureInPicture\_PipControlStatus](#pictureinpicture_pipcontrolstatus) status | Status of the component displayed on the PiP controller. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipControlEnabled()

int32\_t OH\_PictureInPicture\_SetPipControlEnabled(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, bool enabled)

**Description**

Sets the PiP component enabled status.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [PictureInPicture\_PipControlType](#pictureinpicture_pipcontroltype) controlType | Type of the component displayed on the PiP controller. |
| bool enabled | Enabled status of the component displayed on the PiP controller. **true** if enabled, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_RegisterStartPipCallback()

int32\_t OH\_PictureInPicture\_RegisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)

**Description**

Registers a callback to listen for the completion of PiP surface creation.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipStartPipCallback](#webpipstartpipcallback) callback | Callback function for PiP window creation. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterStartPipCallback()

int32\_t OH\_PictureInPicture\_UnregisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)

**Description**

Unregisters the callback used to listen for the completion of PiP surface creation.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipStartPipCallback](#webpipstartpipcallback) callback | Callback function for PiP window creation. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterAllStartPipCallbacks()

int32\_t OH\_PictureInPicture\_UnregisterAllStartPipCallbacks(uint32\_t controllerId)

**Description**

Unregisters all the callbacks used to listen for the completion of PiP surface creation.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_RegisterLifecycleListener()

int32\_t OH\_PictureInPicture\_RegisterLifecycleListener(uint32\_t controllerId, WebPipLifecycleCallback callback)

**Description**

Registers a callback to listen for PiP lifecycle state changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipLifecycleCallback](#webpiplifecyclecallback) callback | Callback function for PiP window lifecycle changes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterLifecycleListener()

int32\_t OH\_PictureInPicture\_UnregisterLifecycleListener(uint32\_t controllerId, WebPipLifecycleCallback callback)

**Description**

Unregisters the callback used to listen for PiP lifecycle state changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipLifecycleCallback](#webpiplifecyclecallback) callback | Callback function for PiP window lifecycle changes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterAllLifecycleListeners()

int32\_t OH\_PictureInPicture\_UnregisterAllLifecycleListeners(uint32\_t controllerId)

**Description**

Unregisters all the callbacks used to listen for PiP lifecycle state changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_RegisterControlEventListener()

int32\_t OH\_PictureInPicture\_RegisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)

**Description**

Registers a callback to listen for control panel action events in PiP mode.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipControlEventCallback](#webpipcontroleventcallback) callback | Callback function for the component click event of the PiP window. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterControlEventListener()

int32\_t OH\_PictureInPicture\_UnregisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)

**Description**

Unregisters the callback used to listen for control panel action events in PiP mode.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipControlEventCallback](#webpipcontroleventcallback) callback | Callback function for the component click event of the PiP window. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterAllControlEventListeners()

int32\_t OH\_PictureInPicture\_UnregisterAllControlEventListeners(uint32\_t controllerId)

**Description**

Unregisters all the callbacks used to listen for control panel action events in PiP mode.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_RegisterResizeListener()

int32\_t OH\_PictureInPicture\_RegisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)

**Description**

Registers a callback to listen for PiP window size changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipResizeCallback](#webpipresizecallback) callback | Callback function for PiP window size changes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterResizeListener()

int32\_t OH\_PictureInPicture\_UnregisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)

**Description**

Unregisters the callback used to listen for PiP window size changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| [WebPipResizeCallback](#webpipresizecallback) callback | Callback function for PiP window size changes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnregisterAllResizeListeners()

int32\_t OH\_PictureInPicture\_UnregisterAllResizeListeners(uint32\_t controllerId)

**Description**

Unregisters all the callbacks used to listen for PiP window size changes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetPipInitialSurfaceRect()

int32\_t OH\_PictureInPicture\_SetPipInitialSurfaceRect(uint32\_t controllerId, int32\_t positionX, int32\_t positionY,uint32\_t width, uint32\_t height)

**Description**

Sets the initial position and size of the PiP surface when the PiP launch animation starts. It can be used to achieve a seamless transition effect.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| int32\_t positionX | X coordinate of the PiP window relative to the top-left corner of the screen when the PiP window is started, in px. |
| int32\_t positionY | Y coordinate of the PiP window relative to the top-left corner of the screen when the PiP window is started, in px. |
| uint32\_t width | Width of the PiP window when the PiP window is started. The value is greater than 0, measured in px. |
| uint32\_t height | Height of the PiP window when the PiP window is started. The value is greater than 0, measured in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_UnsetPipInitialSurfaceRect()

int32\_t OH\_PictureInPicture\_UnsetPipInitialSurfaceRect(uint32\_t controllerId)

**Description**

Cancels the previously set initial position and size for the PiP surface.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |

#### \[h2\]OH\_PictureInPicture\_SetParentWindowId()

int32\_t OH\_PictureInPicture\_SetParentWindowId(uint32\_t controllerId, uint32\_t windowId)

**Description**

Sets the main window ID for PiP.

Before launching PiP, call [OH\_PictureInPicture\_SetPipMainWindowId()](#oh_pictureinpicture_setpipmainwindowid) to set the main window ID.

If the main window of PiP changes (for example, if you launch PiP in one tab of a browser and then drag that tab out to create a new window), you must call this API to update the main window ID to the new window ID. This ensures that PiP can be restored to the correct main window.

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t controllerId | ID of the PiP controller. The value is a non-negative integer. |
| uint32\_t windowId | ID of the main window. The value is a non-negative integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device does not support PiP.

**WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR**: An internal error occurs in PiP.

 |
