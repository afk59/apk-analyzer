# oh\_window.h

#### Overview

The file declares the window management APIs. You can use the APIs to set and obtain the properties of a window, and set its status bar style and navigation bar style.

**File to include**: <window\_manager/oh\_window.h>

**Library**: libnative\_window\_manager.so

**System capability**: SystemCapability.Window.SessionManager

**Since**: 15

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [int32\_t OH\_WindowManager\_SetWindowStatusBarEnabled(int32\_t windowId, bool enabled, bool enableAnimation)](#oh_windowmanager_setwindowstatusbarenabled) | \- | Sets whether to display the status bar in a window. |
| [int32\_t OH\_WindowManager\_SetWindowStatusBarColor(int32\_t windowId, int32\_t color)](#oh_windowmanager_setwindowstatusbarcolor) | \- | Sets the color of the status bar in a window. |
| [int32\_t OH\_WindowManager\_SetWindowNavigationBarEnabled(int32\_t windowId, bool enabled, bool enableAnimation)](#oh_windowmanager_setwindownavigationbarenabled) | \- | Sets whether to display the navigation bar in a window. |
| [int32\_t OH\_WindowManager\_GetWindowAvoidArea(int32\_t windowId, WindowManager\_AvoidAreaType type, WindowManager\_AvoidArea\* avoidArea)](#oh_windowmanager_getwindowavoidarea) | \- | Obtains the avoid area of a window. |
| [int32\_t OH\_WindowManager\_IsWindowShown(int32\_t windowId, bool\* isShow)](#oh_windowmanager_iswindowshown) | \- | Checks whether a window is displayed. |
| [int32\_t OH\_WindowManager\_ShowWindow(int32\_t windowId)](#oh_windowmanager_showwindow) | \- | Shows a window. |
| [int32\_t OH\_WindowManager\_SetWindowTouchable(int32\_t windowId, bool isTouchable)](#oh_windowmanager_setwindowtouchable) | \- | Sets whether a window is touchable. |
| [int32\_t OH\_WindowManager\_SetWindowFocusable(int32\_t windowId, bool isFocusable)](#oh_windowmanager_setwindowfocusable) | \- | Sets whether a window is focusable. |
| [int32\_t OH\_WindowManager\_SetWindowBackgroundColor(int32\_t windowId, const char\* color)](#oh_windowmanager_setwindowbackgroundcolor) | \- | Sets the background color of a window. |
| [int32\_t OH\_WindowManager\_SetWindowBrightness(int32\_t windowId, float brightness)](#oh_windowmanager_setwindowbrightness) | \- | Sets the screen brightness of a window. |
| [int32\_t OH\_WindowManager\_SetWindowKeepScreenOn(int32\_t windowId, bool isKeepScreenOn)](#oh_windowmanager_setwindowkeepscreenon) | \- | Sets whether to always keep the screen on for a window. |
| [int32\_t OH\_WindowManager\_SetWindowPrivacyMode(int32\_t windowId, bool isPrivacy)](#oh_windowmanager_setwindowprivacymode) | \- | Sets whether to enable privacy mode for a window. |
| [int32\_t OH\_WindowManager\_GetWindowProperties(int32\_t windowId, WindowManager\_WindowProperties\* windowProperties)](#oh_windowmanager_getwindowproperties) | \- | Obtains the properties of a window. |
| [int32\_t OH\_WindowManager\_Snapshot(int32\_t windowId, OH\_PixelmapNative\* pixelMap)](#oh_windowmanager_snapshot) | \- | Obtains the snapshot of a window. |
| [int32\_t OH\_WindowManager\_GetAllWindowLayoutInfoList(int64\_t displayId,WindowManager\_Rect\*\* windowLayoutInfoList, size\_t\* windowLayoutInfoSize)](#oh_windowmanager_getallwindowlayoutinfolist) | \- | Obtains the layout information array of all windows visible on a display. The layout information is arranged based on the current window stacking order, and the topmost window in the hierarchy is at index 0 of the array. |
| [void OH\_WindowManager\_ReleaseAllWindowLayoutInfoList(WindowManager\_Rect\* windowLayoutInfoList)](#oh_windowmanager_releaseallwindowlayoutinfolist) | \- | Releases the memory occupied by a window layout information array. |
| [int32\_t OH\_WindowManager\_InjectTouchEvent(int32\_t windowId, Input\_TouchEvent\* touchEvent, int32\_t windowX, int32\_t windowY)](#oh_windowmanager_injecttouchevent) | \- | Injects a multimodal touch event into the target window. This function is limited to injecting events into windows that belong to the same process. The injection does not affect window focus or stacking order, nor does it start window dragging. The event is forwarded directly to ArkUI. This function must be called after the target window has completed its UI loading. |
| [int32\_t OH\_WindowManager\_GetAllMainWindowInfo(WindowManager\_MainWindowInfo\*\* infoList, size\_t\* mainWindowInfoSize)](#oh_windowmanager_getallmainwindowinfo) | \- | Obtains the information about all main windows. |
| [void OH\_WindowManager\_ReleaseAllMainWindowInfo(WindowManager\_MainWindowInfo\* infoList)](#oh_windowmanager_releaseallmainwindowinfo) | \- | Releases the memory used by the main window information list. |
| [typedef void (\*OH\_WindowManager\_WindowSnapshotCallback)(const OH\_PixelmapNative\*\* snapshotPixelMapList, size\_t snapshotListSize)](#oh_windowmanager_windowsnapshotcallback) | OH\_WindowManager\_WindowSnapshotCallback | Defines the callback used for receiving the main window screenshot list. |
| [int32\_t OH\_WindowManager\_GetMainWindowSnapshot(int32\_t\* windowIdList, size\_t windowIdListSize, WindowManager\_WindowSnapshotConfig config, OH\_WindowManager\_WindowSnapshotCallback callback)](#oh_windowmanager_getmainwindowsnapshot) | \- | Obtains the screenshots of one or more main windows specified by **windowId**. |
| [void OH\_WindowManager\_ReleaseMainWindowSnapshot(const OH\_PixelmapNative\* snapshotPixelMapList)](#oh_windowmanager_releasemainwindowsnapshot) | \- | Releases the memory used by the main window screenshot list. |
| [int32\_t OH\_WindowManager\_LockCursor(int32\_t windowId, bool isCursorFollowMovement)](#oh_windowmanager_lockcursor) | \- | Locks the mouse cursor within the specified window area and controls whether the cursor follows mouse movements. It is only supported by the window that currently has focus, and the lock is automatically released when the window loses focus. |
| [int32\_t OH\_WindowManager\_UnlockCursor(int32\_t windowId)](#oh_windowmanager_unlockcursor) | \- | Clears the mouse cursor mode previously set for the window. |

#### Function Description

#### \[h2\]OH\_WindowManager\_SetWindowStatusBarEnabled()

int32\_t OH\_WindowManager\_SetWindowStatusBarEnabled(int32\_t windowId, bool enabled, bool enableAnimation)

**Description**

Sets whether to display the status bar in a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool enabled | Whether to display the status bar. **true** to display, **false** otherwise. |
| bool enableAnimation | Whether to enable the show/hide animation of the status bar. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The feature is not supported by the device.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowStatusBarColor()

int32\_t OH\_WindowManager\_SetWindowStatusBarColor(int32\_t windowId, int32\_t color)

**Description**

Sets the color of the status bar in a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| int32\_t color | Color to set, in ARGB format. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The feature is not supported by the device.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowNavigationBarEnabled()

int32\_t OH\_WindowManager\_SetWindowNavigationBarEnabled(int32\_t windowId, bool enabled, bool enableAnimation)

**Description**

Sets whether to display the navigation bar in a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool enabled | Whether to display the navigation bar. **true** to display, **false** otherwise. |
| bool enableAnimation | Whether to enable the show/hide animation of the navigation bar. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The feature is not supported by the device.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_GetWindowAvoidArea()

int32\_t OH\_WindowManager\_GetWindowAvoidArea(int32\_t windowId, WindowManager\_AvoidAreaType type, WindowManager\_AvoidArea\* avoidArea)

**Description**

Obtains the avoid area of a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| [WindowManager\_AvoidAreaType](../oh-window-comm-h/document.md#windowmanager_avoidareatype) type | Type of the avoid area. |
| [WindowManager\_AvoidArea](../../structs/windowmanager-avoidarea/document.md)\* avoidArea | Pointer to the avoid area. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called, and the pointer to the avoid area is returned.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_IsWindowShown()

int32\_t OH\_WindowManager\_IsWindowShown(int32\_t windowId, bool\* isShow)

**Description**

Checks whether a window is displayed.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool\* isShow | Pointer to the check result for whether the window is displayed. **true** if displayed, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

 |

#### \[h2\]OH\_WindowManager\_ShowWindow()

int32\_t OH\_WindowManager\_ShowWindow(int32\_t windowId)

**Description**

Shows a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowTouchable()

int32\_t OH\_WindowManager\_SetWindowTouchable(int32\_t windowId, bool isTouchable)

**Description**

Sets whether a window is touchable.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool isTouchable | Whether the window is touchable. **true** if touchable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowFocusable()

int32\_t OH\_WindowManager\_SetWindowFocusable(int32\_t windowId, bool isFocusable)

**Description**

Sets whether a window is focusable.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool isFocusable | Whether the window is focusable. **true** if focusable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowBackgroundColor()

int32\_t OH\_WindowManager\_SetWindowBackgroundColor(int32\_t windowId, const char\* color)

**Description**

Sets the background color of a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| const char\* color | Pointer to the background color. The value is a string in hexadecimal RGB or ARGB color format. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowBrightness()

int32\_t OH\_WindowManager\_SetWindowBrightness(int32\_t windowId, float brightness)

**Description**

Sets the window brightness for the main window. The window brightness takes effect only when the window is in the foreground and has focus.

When the setting is valid, it affects only the physical screen where the window is displayed. It does not apply to virtual displays (for example, casting/mirroring screens).

If the input parameter is **\-1**, the window brightness reverts to the system brightness (which can be adjusted through Control Panel or shortcut keys).

When the window moves to the background, the setting becomes invalid, and brightness can be adjusted through Control Panel or shortcut keys. You are not advised to call this API when the window is in the background, as it may cause timing issues.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/AQl6zCngT5KX-ImaxfHPZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7BF4FF759ACAD830C40520D3BF6FF39BE10FD446550762B6717D29A8D5687AE)

-   For non-2-in-1 devices: if a window has custom brightness, Control Panel cannot change the system brightness.
-   For 2-in-1 devices:
    -   Before HarmonyOS 5.0.2, if a window has custom brightness, system brightness controls (Control Panel or shortcut keys) are disabled.
    -   Starting from HarmonyOS 5.0.2, window brightness is always synchronized with system brightness. Brightness can be adjusted through this API, Control Panel, or shortcut keys.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| float brightness | Screen brightness. The value is a floating-point number in the range \[0.0, 1.0\] or is set to **\-1.0**. The value **1.0** means the brightest, and **\-1.0** means that the window brightness resets to the original brightness set through Control Panel. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowKeepScreenOn()

int32\_t OH\_WindowManager\_SetWindowKeepScreenOn(int32\_t windowId, bool isKeepScreenOn)

**Description**

Sets whether to always keep the screen on for a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool isKeepScreenOn | Whether to always keep the screen on. **true** to always keep the screen on, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_SetWindowPrivacyMode()

int32\_t OH\_WindowManager\_SetWindowPrivacyMode(int32\_t windowId, bool isPrivacy)

**Description**

Sets whether to enable privacy mode for a window.

**Required permissions**: ohos.permission.PRIVACY\_WINDOW

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| bool isPrivacy | Whether to enable privacy mode. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION**: The permission verification fails.

 |

#### \[h2\]OH\_WindowManager\_GetWindowProperties()

int32\_t OH\_WindowManager\_GetWindowProperties(int32\_t windowId, WindowManager\_WindowProperties\* windowProperties)

**Description**

Obtains the properties of a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| [WindowManager\_WindowProperties](../../structs/windowmanager-windowproperties/document.md)\* windowProperties | Pointer to the properties. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called, and the pointer to the window properties is returned.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

 |

#### \[h2\]OH\_WindowManager\_Snapshot()

int32\_t OH\_WindowManager\_Snapshot(int32\_t windowId, OH\_PixelmapNative\* pixelMap)

**Description**

Obtains the snapshot of a window.

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | 
Window ID. The default value is **0**. The value is an integer.

If the window ID is invalid or the window has been destroyed, you cannot obtain the window snapshot. To successfully obtain a snapshot, a valid window ID is required.

You can obtain a valid window ID by calling the ArkTS API [getWindowProperties()](../../../arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9) on the window object

 |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative--00020177/document.md)\* pixelMap | Pointer to the snapshot. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called, and the pointer to the pixelMap is returned.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_GetAllWindowLayoutInfoList()

int32\_t OH\_WindowManager\_GetAllWindowLayoutInfoList(int64\_t displayId,WindowManager\_Rect\*\* windowLayoutInfoList, size\_t\* windowLayoutInfoSize)

**Description**

Obtains the layout information array of all windows visible on a display. The layout information is arranged based on the current window stacking order, and the topmost window in the hierarchy is at index 0 of the array.

**Since**: 17

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int64\_t displayId | ID of the display. You can obtain a valid display ID by calling the ArkTS API [getWindowProperties()](../../../arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9) on the window object |
| [WindowManager\_Rect](../../structs/windowmanager-rect/document.md)\*\* windowLayoutInfoList | Double pointer to the layout information array of all windows visible. |
| size\_t\* windowLayoutInfoSize | Pointer to the length of the layout information array. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called, and the double pointer to the array and the pointer to the array length are returned.

**WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM**: A parameter is incorrect.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The feature is not supported by the device.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_ReleaseAllWindowLayoutInfoList()

void OH\_WindowManager\_ReleaseAllWindowLayoutInfoList(WindowManager\_Rect\* windowLayoutInfoList)

**Description**

Releases the memory occupied by a window layout information array.

**Since**: 17

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [WindowManager\_Rect](../../structs/windowmanager-rect/document.md)\* windowLayoutInfoList | Pointer to the layout information array of all windows visible on the display. You can obtain the array pointer by calling [OH\_WindowManager\_GetAllWindowLayoutInfoList](#oh_windowmanager_getallwindowlayoutinfolist). |

#### \[h2\]OH\_WindowManager\_InjectTouchEvent()

int32\_t OH\_WindowManager\_InjectTouchEvent(int32\_t windowId, Input\_TouchEvent\* touchEvent, int32\_t windowX, int32\_t windowY)

**Description**

Injects a multimodal touch event into the target window. This function is limited to injecting events into windows that belong to the same process. The injection does not affect window focus or stacking order, nor does it start window dragging. The event is forwarded directly to ArkUI. This function must be called after the target window has completed its UI loading.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The default value is **0**. The value is an integer. |
| [Input\_TouchEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-touchevent/document.md)\* touchEvent | Pointer to the multimodal touch event. For details, see [Input\_TouchEvent](../../../../../system/basic-functions/input-kit/c-apis/structs/input-touchevent/document.md). The event is defined in **oh\_input\_manager.h**. Certain fields in this parameter have specific constraints. Specifically, **action** should be an integer in the range \[0, 3\]; **id**, **displayX**, **displayY**, and **actionTime** should be an integer greater than or equal to 0. If these constraints are not met, the function returns **WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**, indicating that the window manager service is abnormal. |
| int32\_t windowX | X coordinate of the event relative to the target window. The value is an integer. |
| int32\_t windowY | Y coordinate of the event relative to the target window. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_GetAllMainWindowInfo()

int32\_t OH\_WindowManager\_GetAllMainWindowInfo(WindowManager\_MainWindowInfo\*\* infoList, size\_t\* mainWindowInfoSize)

**Description**

Obtains the information about all main windows.

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Required permissions**: ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [WindowManager\_MainWindowInfo](../../structs/windowmanager-mainwindowinfo/document.md)\*\* infoList | Double pointer to the main window information list. |
| size\_t\* mainWindowInfoSize | Pointer to the size of the main window information list. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION**: The permission verification fails.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The feature is not supported by the device.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_ReleaseAllMainWindowInfo()

void OH\_WindowManager\_ReleaseAllMainWindowInfo(WindowManager\_MainWindowInfo\* infoList)

**Description**

Releases the memory used by the main window information list.

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [WindowManager\_MainWindowInfo](../../structs/windowmanager-mainwindowinfo/document.md)\* infoList | Pointer to the main window information list. |

#### \[h2\]OH\_WindowManager\_WindowSnapshotCallback()

typedef void (\*OH\_WindowManager\_WindowSnapshotCallback)(const OH\_PixelmapNative\*\* snapshotPixelMapList, size\_t snapshotListSize)

**Description**

Defines the callback used for receiving the main window screenshot list.

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_PixelmapNative](../../structs/oh-pixelmapnative--00020177/document.md)\*\* snapshotPixelMapList | Double pointer to the window screenshot list. |
| size\_t snapshotListSize | Size of the window screenshot list. |

#### \[h2\]OH\_WindowManager\_GetMainWindowSnapshot()

int32\_t OH\_WindowManager\_GetMainWindowSnapshot(int32\_t\* windowIdList, size\_t windowIdListSize, WindowManager\_WindowSnapshotConfig config, OH\_WindowManager\_WindowSnapshotCallback callback)

**Description**

Obtains the screenshots of one or more main windows specified by **windowId**.

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Required permissions**: ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t\* windowIdList | Pointer to the main window ID list. |
| size\_t windowIdListSize | Size of the main window ID list. |
| [WindowManager\_WindowSnapshotConfig](../../structs/windowmanager-windowsnapshotconfig/document.md) config | Configuration for obtaining the window screenshot. |
| [OH\_WindowManager\_WindowSnapshotCallback](#oh_windowmanager_windowsnapshotcallback) callback | Callback used to return the lists of window screenshots, in the order of the provided window ID array. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION**: The permission verification fails.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The feature is not supported by the device.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_ReleaseMainWindowSnapshot()

void OH\_WindowManager\_ReleaseMainWindowSnapshot(const OH\_PixelmapNative\* snapshotPixelMapList)

**Description**

Releases the memory used by the main window screenshot list.

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_PixelmapNative](../../structs/oh-pixelmapnative--00020177/document.md)\* snapshotPixelMapList | Pointer to the list of window screenshots. |

#### \[h2\]OH\_WindowManager\_LockCursor()

int32\_t OH\_WindowManager\_LockCursor(int32\_t windowId, bool isCursorFollowMovement)

**Description**

Locks the mouse cursor within the specified window area and controls whether the cursor follows mouse movements. It is only supported by the window that currently has focus, and the lock is automatically released when the window loses focus.

**Required permissions**: ohos.permission.LOCK\_WINDOW\_CURSOR

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The value is an integer. |
| bool isCursorFollowMovement | Behavior of the mouse cursor when locked. If it is set to **true**, the cursor moves along with the mouse. If it is set to **false**, the cursor remains stationary and does not follow mouse movements. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION**: You do not have the permission to call the API.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device is not supported.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |

#### \[h2\]OH\_WindowManager\_UnlockCursor()

int32\_t OH\_WindowManager\_UnlockCursor(int32\_t windowId)

**Description**

Clears the mouse cursor mode previously set for the window.

**Required permissions**: ohos.permission.LOCK\_WINDOW\_CURSOR

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t windowId | Window ID. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following result codes:

**OK**: The function is successfully called.

**WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION**: You do not have the permission to call the API.

**WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED**: The device is not supported.

**WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL**: The window status is abnormal.

**WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL**: The window manager service is abnormal.

 |
