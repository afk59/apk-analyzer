# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/x5B6E1OfQM2Hr5hjAP-qEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19485E9062FF7C57687AF5A28E0D966313B24B20EC2668C6AAD8FF2241559F18)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For the system capability SystemCapability.Window.SessionManager, use [canIUse()](../../../../../../common-capabilities/arkts-api/syscap/document.md#caniuse) to check whether the device supports this system capability and the corresponding APIs.
    

#### WindowType7+

Enumerates the window types.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_APP | 0 | 
Child window of an application.

**Model restriction**: This API can be used only in the FA model.

 |
| TYPE\_SYSTEM\_ALERT(deprecated) | 1 | 

System alert window.

**Note**: This API has been deprecated since API version 11,

and was supported since API version 7.

 |
| TYPE\_FLOAT9+ | 8 | 

Global floating window.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TYPE\_DIALOG10+ | 16 | 

Modal window.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| TYPE\_MAIN18+ | 32 | 

Main window of an application.

This window type cannot be used during window creation.

 |

#### AvoidAreaType7+

Enumerates the types of areas to avoid for window content.

When adapting window content for an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout), you should adjust the content based on the corresponding [AvoidArea](../interfaces-others/document.md#avoidarea7) specified by **AvoidAreaType**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_SYSTEM | 0 | Default area of the system. It usually indicates the status bar area. In a floating window, it indicates the three-dot control bar area of the main window of the application. |
| TYPE\_CUTOUT | 1 | Cutout area. |
| TYPE\_SYSTEM\_GESTURE9+ | 2 | Side return gesture area. Currently, no devices support this type of avoid area. |
| TYPE\_KEYBOARD9+ | 3 | Fixed soft keyboard area. |
| TYPE\_NAVIGATION\_INDICATOR11+ | 4 | Bottom navigation bar. It may appear as a navigation bar or a three-button navigation bar depending on user settings. |

#### Orientation9+

Enumerates the window orientations.

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | 
Unspecified. The orientation is determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| PORTRAIT | 1 | 

Portrait.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LANDSCAPE | 2 | 

Landscape.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| PORTRAIT\_INVERTED | 3 | 

Reverse portrait.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| LANDSCAPE\_INVERTED | 4 | 

Reverse landscape.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AUTO\_ROTATION | 5 | 

Automatically rotates with the sensor to four orientations: portrait, landscape, reverse portrait, and reverse landscape. This rotation is not controlled by the rotation switch in Control Panel.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_ROTATION\_PORTRAIT | 6 | 

Automatically rotates with the sensor to two orientations: portrait and reverse portrait. This rotation is not controlled by the rotation switch in Control Panel.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| AUTO\_ROTATION\_LANDSCAPE | 7 | 

Automatically rotates with the sensor to two orientations: landscape and reverse landscape. This rotation is not controlled by the rotation switch in Control Panel.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AUTO\_ROTATION\_RESTRICTED | 8 | 

Automatically rotates with the sensor to four orientations: portrait, landscape, reverse portrait, and reverse landscape. This rotation is controlled by the rotation switch in Control Panel.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 9 | 

Automatically rotates with the sensor to two orientations: portrait and reverse portrait. This rotation is controlled by the rotation switch in Control Panel.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | 

Automatically rotates with the sensor to two orientations: landscape and reverse landscape. This rotation is controlled by the rotation switch in Control Panel.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| LOCKED | 11 | 

Locked mode, where the window orientation is consistent with the current screen orientation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| AUTO\_ROTATION\_UNSPECIFIED12+ | 12 | 

Automatically rotates with the sensor, under the restriction of the rotation switch in Control Panel. The orientation that can be rotated to is determined by the system. For example, the window can rotate to portrait, landscape, or reverse landscape, but not reverse portrait, on a certain device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

 |
| USER\_ROTATION\_PORTRAIT12+ | 13 | 

Temporarily rotates to portrait mode, and then automatically rotates with the sensor, under the restriction of the rotation switch in Control Panel. The orientation that can be rotated to is determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

 |
| USER\_ROTATION\_LANDSCAPE12+ | 14 | 

Temporarily rotates to landscape mode, and then automatically rotates with the sensor, under the restriction of the rotation switch in Control Panel. The orientation that can be rotated to is determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

 |
| USER\_ROTATION\_PORTRAIT\_INVERTED12+ | 15 | 

Temporarily rotates to reverse portrait mode, and then automatically rotates with the sensor, under the restriction of the rotation switch in Control Panel. The orientation that can be rotated to is determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

 |
| USER\_ROTATION\_LANDSCAPE\_INVERTED12+ | 16 | 

Temporarily rotates to reverse landscape mode, and then automatically rotates with the sensor, under the restriction of the rotation switch in Control Panel. The orientation that can be rotated to is determined by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

 |
| FOLLOW\_DESKTOP12+ | 17 | 

Follows the orientation of the home screen, where the window will rotate if the home screen rotates and will not rotate if the home screen does not.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

 |

#### RectChangeReason12+

Enumerates the reasons for window rectangle (position and size) changes.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| UNDEFINED | 0 | Default value. |
| MAXIMIZE | 1 | The window is maximized. |
| RECOVER | 2 | The window is restored to the previous state. |
| MOVE | 3 | The window is moved. |
| DRAG | 4 | The window is zoomed in or out by dragging. |
| DRAG\_START | 5 | The window starts zooming in or out. |
| DRAG\_END | 6 | The window finishes zooming in or out. |

#### ColorSpace8+

Enumerates the color spaces.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Default SRGB gamut. |
| WIDE\_GAMUT | 1 | Wide-gamut. |

#### WindowEventType10+

Enumerates the window lifecycle states.

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_SHOWN | 1 | 
The window is running in the foreground.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| WINDOW\_ACTIVE | 2 | 

The window gains focus.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| WINDOW\_INACTIVE | 3 | 

The window loses focus.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| WINDOW\_HIDDEN | 4 | 

The window is running in the background.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| WINDOW\_DESTROYED11+ | 7 | 

The window is destroyed.

**System capability**: SystemCapability.Window.SessionManager

 |

#### WindowStatusType11+

Enumerates the window modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| UNDEFINED | 0 | The window mode is not defined by the application. |
| FULL\_SCREEN | 1 | 
The application is displayed in full screen.

In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state, the window occupies the entire screen with no dock, title bar, or status bar displayed by default.

You can use [maximize()](../interface-window/document.md#maximize12) and [setTitleAndDockHoverShown()](../interface-window/document.md#settitleanddockhovershown14) to configure whether to display the title bar and dock upon hovering over the hot zone.

The last call takes precedence when both the **maximize()** and **setTitleAndDockHoverShown()** APIs are called.

In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state, the window occupies the entire screen with no title bar or dock displayed. You can use [setSpecificSystemBarEnabled()](../interface-window/document.md#setspecificsystembarenabled11) to configure whether to display the status bar.

 |
| MAXIMIZE | 2 | The application window is maximized. In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state, the window occupies the entire screen, and the dock, status bar, and title bar are displayed without requiring a hover. This state is unavailable in non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state. |
| MINIMIZE | 3 | The application window is minimized. |
| FLOATING | 4 | The application is displayed in a floating window. |
| SPLIT\_SCREEN | 5 | The application is displayed in split-screen mode. |

#### PixelUnit22+

Enumerates the pixel units.

You can use [px2vp](../../../ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2vp12) and [vp2px](../../../ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert between physical pixels and virtual pixels.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| PX | 0 | Physical pixel unit (px). |
| VP | 1 | Virtual pixel unit (vp). |

#### MaximizePresentation12+

Enumerates the layout when the window is maximized.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| FOLLOW\_APP\_IMMERSIVE\_SETTING | 0 | 
The window, when maximized, follows the application's full-screen mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| EXIT\_IMMERSIVE | 1 | 

The window, when maximized, exits full-screen mode if it is set to full-screen.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ENTER\_IMMERSIVE | 2 | 

The window, when maximized, transitions into the full-screen mode, and the window title bar and dock bar are displayed when the cursor hovers over the hot zone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ENTER\_IMMERSIVE\_DISABLE\_TITLE\_AND\_DOCK\_HOVER14+ | 3 | 

The window, when maximized, transitions into the full-screen mode, and the window title bar and dock bar are not displayed when the cursor hovers over the hot zone.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### WindowAnimationCurve20+

Enumerates the types of window animation curves.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| LINEAR | 0 | 
The animation speed is constant from start to finish.

When this curve type is used, **duration** in [WindowAnimationConfig](../interfaces-others/document.md#windowanimationconfig20) is mandatory.

When this curve type is used, **param** in [WindowAnimationConfig](../interfaces-others/document.md#windowanimationconfig20) is optional and does not take effect.

 |
| INTERPOLATION\_SPRING | 1 | 

Interpolator spring curve, an animation curve from 0 to 1, where the actual animation values are interpolated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in [WindowAnimationConfig](../interfaces-others/document.md#windowanimationconfig20).

When this curve type is used, **duration** in [WindowAnimationConfig](../interfaces-others/document.md#windowanimationconfig20) is optional and does not take effect.

When this curve type is used, **param** in [WindowAnimationConfig](../interfaces-others/document.md#windowanimationconfig20) is mandatory.

 |
| CUBIC\_BEZIER | 2 | 

Cubic Bézier curve.

When this curve type is used, **param** and **duration** in [WindowAnimationConfig](../interfaces-others/document.md#windowanimationconfig20) are mandatory.

 |

#### WindowTransitionType20+

Enumerates the types of window transition animations.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| DESTROY | 0 | Transition animation when the window is destroyed. |

#### AnimationType20+

Enumerates the types of window animations.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| FADE\_IN\_OUT | 0 | Fade-in/fade-out animation. The fade-in animation takes effect during window display, and the fade-out animation takes effect during window hiding. |

#### WindowAnchor20+

Enumerates the window anchor points.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP\_START | 0 | Top-left corner of the window. |
| TOP | 1 | Horizontal center point along the top edge of the window. |
| TOP\_END | 2 | Top-right corner of the window. |
| START | 3 | Vertical center point along the left edge of the window. |
| CENTER | 4 | Center point of the window, both horizontally and vertically. |
| END | 5 | Vertical center point along the right edge of the window. |
| BOTTOM\_START | 6 | Bottom-left corner of the window. |
| BOTTOM | 7 | Horizontal center point along the bottom edge of the window. |
| BOTTOM\_END | 8 | Bottom-right corner of the window. |

#### RotationChangeType19+

Enumerates the types of window rotation events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_WILL\_ROTATE | 0 | The window is about to rotate. |
| WINDOW\_DID\_ROTATE | 1 | The window has finished rotating. |

#### RectType19+

Enumerates the types of window rectangle coordinate systems.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| RELATIVE\_TO\_SCREEN | 0 | The window rectangle is relative to the screen coordinate system. |
| RELATIVE\_TO\_PARENT\_WINDOW | 1 | The window rectangle is relative to the parent window coordinate system. |

#### GlobalWindowMode20+

Enumerates the window modes.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| FULLSCREEN | 1 | Full-screen window. The first binary bit from right to left is 1. |
| SPLIT | 1 << 1 | Split-screen window. The second binary bit from right to left is 1. |
| FLOAT | 1 << 2 | Floating window. The third binary bit from right to left is 1. |
| PIP | 1 << 3 | PiP window. The fourth binary bit from right to left is 1. |

#### OcclusionState22+

Enumerates the window visibility states.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_OCCLUSION | 0 | The window is entirely visible, with no parts obscured by other non-transparent windows. |
| PARTIAL\_OCCLUSION | 1 | The window is partially visible, with some parts obscured by other non-transparent windows. |
| FULL\_OCCLUSION | 2 | The window is completely invisible, either fully obscured by other non-transparent windows, minimized, or hidden. |

#### WindowStageEventType9+

Enumerates the lifecycle event types of a WindowStage.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Value | Description |
| :-- | :-- | :-- |
| SHOWN | 1 | The WindowStage is shown in the foreground, for example, when launching from the application icon, triggered whether it is the first launch or resuming from the background. |
| ACTIVE | 2 | The WindowStage gains focus, for example, the state of the application window after handling a click event, or the state after the application is launched. |
| INACTIVE | 3 | The WindowStage loses focus, for example, the state of the window that was in focus when a new application is opened or another window is clicked. |
| HIDDEN | 4 | The WindowStage is running in the background, for example, when the application exists after swiping up or the application window is closed. |
| RESUMED11+ | 5 | The WindowStage is in the foreground and interactive, for example, when the application is open and can interact with the user. |
| PAUSED11+ | 6 | The WindowStage is in the foreground but not interactive, for example, when the application is in the foreground and is entering the multitasking screen. |

#### WindowStageLifecycleEventType20+

Enumerates the lifecycle state types of a WindowStage.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| SHOWN | 1 | The WindowStage is shown in the foreground, for example, when launching from the application icon, triggered whether it is the first launch or resuming from the background. |
| RESUMED | 2 | The WindowStage is in the foreground and interactive, for example, when the application is open and can interact with the user. |
| PAUSED | 3 | The WindowStage is in the foreground but not interactive, for example, when the application is in the foreground and is entering the multitasking screen. |
| HIDDEN | 4 | The WindowStage is running in the background, for example, when the application exists after swiping up or the application window is closed. |

#### ModalityType14+

Enumerates the modality types of the child window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 14.

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_MODALITY | 0 | Select this value when only the parent window should not respond to user operations. |
| APPLICATION\_MODALITY | 1 | 
Select this value when other instances of the application should also not respond to user operations.

**Device behavior differences**: This enumeration can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, error code 801 is returned.

 |

#### ScreenshotEventType20+

Enumerates the screenshot event types.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SYSTEM\_SCREENSHOT | 0 | System screenshot succeeds. |
| SYSTEM\_SCREENSHOT\_ABORT | 1 | System screenshot aborted. |
| SCROLL\_SHOT\_START | 2 | Scroll screenshot starts. |
| SCROLL\_SHOT\_END | 3 | Scroll screenshot ends. |
| SCROLL\_SHOT\_ABORT | 4 | Scroll screenshot aborted. |
