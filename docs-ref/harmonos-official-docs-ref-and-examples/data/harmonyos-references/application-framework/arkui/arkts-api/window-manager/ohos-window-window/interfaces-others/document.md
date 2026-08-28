# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/4uHRF84tT9mqdFU4QTIS3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33ADB46ACD97436BFD40D3F7B3EE5C9379CF2DD6E62F260290F8FC8F8D53A604)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For the system capability SystemCapability.Window.SessionManager, use [canIUse()](../../../../../../common-capabilities/arkts-api/syscap/document.md#caniuse) to check whether the device supports this system capability and the corresponding APIs.
    

#### Configuration9+

Describes the parameters for creating a child window or system window.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | 
Window name.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| windowType | [WindowType](../enums/document.md#windowtype7) | No | No | 

Window type.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | No | Yes | 

Current application context. If no value is passed, no context is used.

In the FA model, do not pass in this parameter when creating a child window. Otherwise, an error is reported.

In the stage model, you must pass in this parameter when creating a floating window, modal window, or system window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| displayId | number | No | Yes | 

Screen ID of the current window. If it is not set, the screen ID of the parent window is used by default.

The value is a non-negative integer and must correspond to an existing screen.

In scenarios involving extended screens or heterogeneous virtual screens, a global floating window can be displayed on a specified screen by setting the screen ID.

For modal windows and system windows, this parameter takes no effect, and the parent window's screen ID is used by default.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| parentId | number | No | Yes | 

ID of the parent window. If this parameter is not set, the default value **\-1** is used. The default parent window is the main window corresponding to the current application context.

In the FA model, the parameter value must be a non-negative integer and must correspond to an existing parent window.

This parameter is invalid in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| decorEnabled12+ | boolean | No | Yes | 

Whether the window decoration is enabled. This parameter is valid only when **windowType** is set to **TYPE\_DIALOG**. **true** if enabled, **false** otherwise. The default value is **false**.

**System capability**: SystemCapability.Window.SessionManager

 |
| title12+ | string | No | Yes | 

Title of the window when **decorEnabled** is set to **true**. The title display area should not go past the left side of the three-button area of the system. Any part that goes beyond will show as an ellipsis. If this parameter is not set, an empty string is used.

**System capability**: SystemCapability.Window.SessionManager

 |

#### SystemBarProperties

Describes the properties of the status bar.

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| statusBarColor | string | No | Yes | 
Background color of the status bar. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**. The default value is **'#66000000'**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isStatusBarLightIcon7+ | boolean | No | Yes | 

Whether any icon on the status bar is highlighted. **true** if highlighted, **false** otherwise. The default value is **false**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| statusBarContentColor8+ | string | No | Yes | 

Color of the text on the status bar. After this property is set, the setting of **isStatusBarLightIcon** is invalid. The default value is **'#E5FFFFFF'**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| navigationBarColor | string | No | Yes | 

Background color of the three-button navigation bar. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**. The default value is **'#66000000'**.

This enum is not supported by HarmonyOS devices.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isNavigationBarLightIcon7+ | boolean | No | Yes | 

Whether any icon on the three-button navigation bar is highlighted. **true** if highlighted, **false** otherwise. The default value is **false**.

This enum is not supported by HarmonyOS devices.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| navigationBarContentColor8+ | string | No | Yes | 

Color of the text on the three-button navigation bar. After this property is set, the setting of **isNavigationBarLightIcon** is invalid. The default value is **'#E5FFFFFF'**.

This enum is not supported by HarmonyOS devices.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| enableStatusBarAnimation12+ | boolean | No | Yes | 

Whether to enable animation for a status bar property change. **true** to enable, **false** otherwise. The default value is **false**.

**System capability**: SystemCapability.Window.SessionManager

 |
| enableNavigationBarAnimation12+ | boolean | No | Yes | 

Whether to enable animation for a three-button navigation bar property change. **true** to enable, **false** otherwise. The default value is **false**.

This enum is not supported by HarmonyOS devices.

**System capability**: SystemCapability.Window.SessionManager

 |

#### StatusBarProperty18+

Describes the properties of the status bar. These properties are returned when you query the status bar's configuration details.

**Atomic service API**: This API can be used in atomic services since API version 18.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| contentColor | string | No | No | 
Color of the text on the status bar. The value is in ARGB format, for example, **#E5FFFFFF**.

**System capability**: SystemCapability.Window.SessionManager

 |

#### SystemBarStyle12+

Describes the properties of the status bar. These properties are valid for the page-level status bar.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| statusBarContentColor | string | No | Yes | Color of the text on the status bar. The default value is **'#E5FFFFFF'**. |

#### FrameMetrics22+

Enumerates the metrics for frame performance.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| firstDrawFrame | boolean | No | No | Whether the frame is the first frame. **true** for first frame, **false** otherwise. |
| inputHandlingDuration | number | No | No | Duration of gesture handling in a frame, in nanoseconds. |
| layoutMeasureDuration | number | No | No | Duration of layout measurement in a frame, in nanoseconds. |
| vsyncTimestamp | number | No | No | Timestamp marking the start of the current frame, in nanoseconds. |

#### Rect7+

Describes the rectangular area of the window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | Left boundary of the rectangle, in px. The value must be an integer. |
| top | number | No | No | Top boundary of the rectangle, in px. The value must be an integer. |
| width | number | No | No | Width of the rectangle, in px. The value must be an integer. |
| height | number | No | No | Height of the rectangle, in px. The value must be an integer. |

#### AvoidArea7+

Describes the area to avoid for window content.

When adapting window content for an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout), you should adjust the content based on the corresponding **AvoidArea** specified by [AvoidAreaType](../enums/document.md#avoidareatype7).

In the avoid area, the application window content is obscured and does not respond to user click events.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| visible9+ | boolean | No | No | Whether the avoid area is visible. **true** if visible, **false** otherwise. |
| leftRect | [Rect](#rect7) | No | No | Rectangle centered to the left of the window's two diagonals. |
| topRect | [Rect](#rect7) | No | No | Rectangle centered at the top of the window's two diagonals. |
| rightRect | [Rect](#rect7) | No | No | Rectangle centered to the right of the window's two diagonals. |
| bottomRect | [Rect](#rect7) | No | No | Rectangle centered at the bottom of the window's two diagonals. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fuMaB4X6S5au9KlySYThxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=061D15F29F36604EE730ABFCD52F92411AA6CE6E87EBC8A5902EB444F6245F65)

The figure below shows the meanings of **leftRect**, **topRect**, **rightRect**, and **bottomRect**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Zg1AQ3IMTlqDyb10HAo_uA/en-us_image_0000002537925312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF0E6CA021833D000730141C6C21D3933B03D9929D754003A0AD72BD00B3462D)

#### Size7+

Describes the window size.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | No | Window width, in px. The value must be an integer. |
| height | number | No | No | Window height, in px. The value must be an integer. |

#### Position20+

Describes the position of the window or component.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X coordinate, in px. The value must be an integer. |
| y | number | No | No | Y coordinate, in px. The value must be an integer. |

#### RectChangeOptions12+

Describes the value and reason returned upon a window rectangle (position and size) change.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rect | [Rect](#rect7) | No | No | New value of the window rectangle. |
| reason | [RectChangeReason](../enums/document.md#rectchangereason12) | No | No | Reason for the window rectangle change. |

#### AvoidAreaOptions12+

Returns the new avoid area and its type after the system avoid area changes.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [AvoidAreaType](../enums/document.md#avoidareatype7) | No | No | Type of the new avoid area returned after the system avoid area changes. |
| area | [AvoidArea](#avoidarea7) | No | No | New avoid area returned after the system avoid area changes. |

#### WindowProperties

Describes the window properties.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| windowRect7+ | [Rect](#rect7) | No | No | 
Window size, which can be obtained via [onPageShow](../../../../arkts-components/custom-components/custom-component-lifecycle/document.md#onpageshow) or [onForeground](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onforeground). Note that the left and top boundaries of the window are calculated relative to the top-left corner of the screen where the window is located.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| drawableRect11+ | [Rect](#rect7) | No | No | 

Size of the rectangle that can be drawn in the window. The upper boundary and left boundary are calculated relative to the top-left vertex of the window. In the stage model, this property should be obtained after [loadContent()](../interface-window/document.md#loadcontent9) or [setUIContent()](../interface-window/document.md#setuicontent9) is called to load the page content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| type7+ | [WindowType](../enums/document.md#windowtype7) | No | No | 

Window type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isFullScreen | boolean | No | No | 

Whether the status bar is hidden when **isLayoutFullScreen** is set to **true**. If the status bar is hidden, the return value is **true**. In other cases, the return value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isLayoutFullScreen7+ | boolean | No | No | 

Whether an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout) is set for a child window. If an immersive-layout is set for the child window, the return value is **true**.

Whether an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout) is set for the main window and the main window is in full-screen mode. If an immersive-layout is set for the main window and the main window is in full-screen mode, the return value is **true**.

In other cases, the return value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| focusable7+ | boolean | No | No | 

Whether the window is focusable. **true** if focusable, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| touchable7+ | boolean | No | No | 

Whether the window is touchable. **true** if touchable, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| brightness | number | No | No | 

Screen brightness of the window. The brightness can be set by calling [setWindowBrightness()](../interface-window/document.md#setwindowbrightness9). The value is a floating-point number. Valid values are in the range \[0.0, 1.0\] (where **1.0** means the brightest) or the special value **\-1.0** (which means that the brightness follows the system). If no value is passed, the brightness follows the system. In this case, the obtained brightness value is **\-1.0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| dimBehindValue(deprecated) | number | No | No | 

Dimness of the window that is not on top. The value is a floating-point number in the range \[0.0, 1.0\], and the value **1.0** means the dimmest.

Note: This property is supported since API version 7 and deprecated since API version 9. Currently, no substitute is available.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isKeepScreenOn | boolean | No | No | 

Whether the screen is always on. **true** if always on, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isPrivacyMode7+ | boolean | No | No | 

Whether the window is in privacy mode. **true** if the window is in privacy mode, **false** otherwise. You can call [setWindowPrivacyMode()](../interface-window/document.md#setwindowprivacymode9) to set the privacy mode of the window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isRoundCorner(deprecated) | boolean | No | No | 

Whether the window has rounded corners. **true** if the window has rounded corners; **false** otherwise.

Note: This property is supported since API version 7 and deprecated since API version 9. Currently, no substitute is available.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| isTransparent7+ | boolean | No | No | 

Whether the window background is transparent. **true** if transparent, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| id9+ | number | No | No | 

Window ID. The value is an integer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| displayId12+ | number | No | Yes | 

ID of the screen where the window is located. By default, the ID of the main screen is returned. The value is an integer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| name18+ | string | No | Yes | 

Window name. The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

 |
| globalDisplayRect20+ | [Rect](#rect7) | No | Yes | 

Window size in the global coordinate system. In extended screen scenarios, the top-left corner of the primary screen is used as the coordinate origin. In virtual screen scenarios, the top-left corner of the virtual screen is used as the coordinate origin. The default value is \[0, 0, 0, 0\].

**System capability**: SystemCapability.Window.SessionManager

 |

#### DecorButtonStyle14+

Describes the button style of the system decoration bar.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colorMode | [ConfigurationConstant.ColorMode](../../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-configurationconstant-constants-related-to-environment-variable/document.md#colormode) | No | Yes | 
Color mode. Buttons automatically adapt to light colors in dark mode and to dark colors in light mode. If this parameter is not set, they will automatically match the system color mode.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| buttonBackgroundSize | number | No | Yes | 

Size of the button when it is highlighted. The value ranges from 20 vp to 40 vp. The default value is 28 vp.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| spacingBetweenButtons | number | No | Yes | 

Spacing between buttons. The value ranges from 8 vp to 24 vp. The default value is 12 vp.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| closeButtonRightMargin | number | No | Yes | 

Margin between the rightmost edge of the close button and the window. The value ranges from 6 vp to 22 vp. The default value is 20 vp.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| buttonIconSize20+ | number | No | Yes | 

Size of the button icon. The value ranges from 16 vp to 24 vp. The default value is 20 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| buttonBackgroundCornerRadius20+ | number | No | Yes | 

Radius of the button background rounded corner. The value ranges from 4 vp to 8 vp. The default value is 4 vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### WindowLimits11+

Describes the parameters for window size limits. Applications can obtain the current window size limits (in px) via [getWindowLimits](../interface-window/document.md#getwindowlimits11). Starting from API version 22, they can also be obtained via [getWindowLimitsVP](../interface-window/document.md#getwindowlimitsvp22) (in vp).

The actual window size limits applied are determined by the intersection of the default system limits, application configurations, and runtime settings, with the priority (from highest to lowest) as follows:

1.  Window size limits configured by the application via [setWindowLimits](../interface-window/document.md#setwindowlimits11).
2.  Window size limits specified by the application via [StartOptions](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md#startoptions) when the application starts the window through [startAbility](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-2). (This approach is supported since API version 17.)
3.  Window size limits configured by the application in [abilities in the module.json5 file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities).
4.  Default system limits (which vary depending on the product and window type).

**System capability**: SystemCapability.Window.SessionManager

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/mMPrp0L5TfKQTI84tHQm2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D26D223079F3B484F686DFDDB9FD22051882E21443BCD03318B0DE29D594204)

For the **maxWidth**, **maxHeight**, **minWidth**, and **minHeight** properties:

-   The default unit is px. Starting from API version 22, the unit can be px or vp, depending on the setting of **pixelUnit**.
-   The value is an integer. Floating-point values will be rounded down.
-   The default value is **0**, indicating that the property does not change.
-   The lower bound of the effective range is the minimum height/width limited by the system.
-   The upper bound of the effective range is the maximum height/width limited by the system.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| maxWidth | number | No | Yes | 
Maximum window width.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maxHeight | number | No | Yes | 

Maximum window height.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| minWidth | number | No | Yes | 

Minimum window width.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| minHeight | number | No | Yes | 

Minimum window height.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| pixelUnit22+ | [PixelUnit](../enums/document.md#pixelunit22) | No | Yes | Unit of the window size limits. The default value is **px**. The value can be **px** or **vp**. |

#### TitleButtonRect11+

Describes the rectangle used to hold the minimize, maximize, and close buttons on the title bar. This rectangle is located in the top-right corner of the window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| right | number | No | No | Right boundary of the rectangle, in vp. The value must be an integer. |
| top | number | No | No | Top boundary of the rectangle, in vp. The value must be an integer. |
| width | number | No | No | Width of the rectangle, in vp. The value must be an integer. |
| height | number | No | No | Height of the rectangle, in vp. The value must be an integer. |

#### MoveConfiguration15+

Describes the window movement configuration.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| displayId | number | No | Yes | Target display ID. The value must be an integer. If a non-integer is passed in, the value is rounded down. The default value is **undefined**. If this parameter is passed in, the window is positioned relative to the top-left corner of the target display. If this parameter is left empty or set to **undefined**, or the target display ID does not exist, the window is positioned relative to the top-left corner of the current display. |

#### WindowDensityInfo15+

Describes the information about the display density of the screen where the window is located and the window's custom display density. It is a scale factor independent of pixel units, that is, a factor for scaling display size.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| systemDensity | number | No | No | System's display size scale factor for the screen where the window is located. The value ranges from 0.5 to 4.0 and varies according to user settings. |
| defaultDensity | number | No | No | Default display size scale factor for the screen where the window is located. The value ranges from 0.5 to 4.0 and varies with the screen. |
| customDensity | number | No | No | Custom display size scale factor of the window. The value ranges from 0.5 to 4.0. If this parameter is left unspecified, the system's display size scale factor is used. This parameter takes effect only for the main window. For the child window or system window, it is equivalent to the system's display size scale factor (**systemDensity**). |

#### WindowLayoutInfo15+

Describes the information about the window layout.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| windowRect | [Rect](#rect7) | No | No | Window rectangle, that is, the position and size of the window on the display. |

#### KeyboardInfo18+

Describes the information about the soft keyboard window.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| beginRect | [Rect](#rect7) | No | No | 
Position and size of the soft keyboard before the animation starts.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| endRect | [Rect](#rect7) | No | No | 

Position and size of the soft keyboard after the animation ends.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| animated20+ | boolean | No | Yes | 

Whether there is a show/hide animation. **true** if there is a show/hide animation, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| config20+ | [WindowAnimationConfig](#windowanimationconfig20) | No | Yes | 

Animation configuration.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ShowWindowOptions20+

Describes the parameters for displaying a child window or system window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 20.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| focusOnShow | boolean | No | Yes | Whether the window automatically gains focus when [showWindow()](../interface-window/document.md#showwindow20) is called. The default value is **true**. This parameter does not take effect for the main window, modal window, and dialog boxes. |

#### WindowAnimationConfig20+

Describes the configuration for window animation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| curve | [WindowAnimationCurve](../enums/document.md#windowanimationcurve20) | No | No | Type of animation curve. |
| duration | number | No | Yes | 
Duration for playing the animation, in milliseconds (ms).

The default value is 0, and the maximum value is 3000.

Whether it is required depends on the animation curve type.

 |
| param | [WindowAnimationCurveParam](../types/document.md#windowanimationcurveparam20) | No | Yes | Parameters for the animation curve. Whether it is required depends on the animation curve type. |

#### WindowInfo18+

Describes the window information.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rect | [Rect](#rect7) | No | No | Window size. |
| bundleName | string | No | No | Bundle name of the application. |
| abilityName | string | No | No | Ability name. |
| windowId | number | No | No | Window ID. |
| windowStatusType | [WindowStatusType](../enums/document.md#windowstatustype11) | No | No | Window mode. |
| isFocused | boolean | No | Yes | Whether the window gains focus. **true** if the window gains focus, **false** otherwise. The return value is the same as that of the [isFocused()](../interface-window/document.md#isfocused12) API. |
| globalDisplayRect20+ | [Rect](#rect7) | No | Yes | Window size in the global coordinate system. In extended screen scenarios, the top-left corner of the primary screen is used as the coordinate origin. In virtual screen scenarios, the top-left corner of the virtual screen is used as the coordinate origin. The default value is \[0, 0, 0, 0\]. |

#### TransitionAnimation20+

Describes the window transition animation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| config | [WindowAnimationConfig](#windowanimationconfig20) | No | No | Transition animation configuration. |
| opacity | number | No | Yes | Opacity of the window during the transition animation. If this parameter is set to **0**, the window is completely transparent. The default value is **1.0**. When the animation type is **WindowTransitionType.DESTROY**, this represents the opacity at the end of the animation. The value ranges from 0 to 1.0. The value is reset to **1.0** when the animation ends. |

#### StartAnimationParams20+

Describes the parameters for the startup animation.

The configuration is valid only for transitions between different abilities within the same application.

The configuration is valid only full-screen applications.

**Device behavior differences**: The API can be called properly on phones that are not working in [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode and tablets that are working in neither freeform window nor desktop mode. On phones and tablets in freeform window or desktop mode and other devices, calls to this API do not take effect or return an error.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [AnimationType](../enums/document.md#animationtype20) | No | No | Type of the window animation. |

#### WindowCreateParams20+

Describes the window parameters during application startup.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| animationParams | [StartAnimationParams](#startanimationparams20) | No | Yes | Parameters for the startup animation. The default value is **undefined**. If this parameter is not set, the default animation of the system is used. |

#### Callback15+

#### \[h2\](data: T)15+

(data: T): V

Describes a generic callback function.

You can set **data** to customize the parameter type of the information returned by the callback.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | T | Yes | Parameter of type T that needs to be passed when the callback function is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value of type V. |

#### RotationChangeInfo19+

Describes the window information obtained during window rotation changes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [RotationChangeType](../enums/document.md#rotationchangetype19) | No | No | Type of window rotation event. |
| orientation | number | No | No | 
Display orientation of the window.

\- **0**: portrait.

\- **1**: reverse landscape.

\- **2**: reverse portrait.

\- **3**: landscape.

Note that the orientation here is different from the orientation property of the display object.

 |
| displayId | number | No | No | ID of the screen where the window is located. |
| displayRect | [Rect](#rect7) | No | No | Size of the rectangle after the screen where the window is located is rotated. |

#### RotationChangeResult19+

Describes the information returned by the application during window rotation changes. The system uses the information to adjust the size of the current window rectangle. If the returned information is about the rotation change of the main window, the system does not change the size of the main window.

There are limitations on the size of application windows and system windows. For details about specific restrictions and rules, see [resize](../interface-window/document.md#resize9).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rectType | [RectType](../enums/document.md#recttype19) | No | No | Type of window rectangle coordinate system. |
| windowRect | [Rect](#rect7) | No | No | Information about the window's rectangle relative to the screen or parent window coordinate system. |

#### RotationChangeCallback19+

#### \[h2\](info: T)19+

(info: T): U

Describes a generic callback function for rotation event notifications.

In this callback function, the parameter type is [RotationChangeInfo](#rotationchangeinfo19), and the return value type is [RotationChangeResult](#rotationchangeresult19) | void.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | T | Yes | Parameter of type [RotationChangeInfo](#rotationchangeinfo19) passed by the system when the callback is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| U | Return value of the [RotationChangeResult](#rotationchangeresult19) or void type returned by the callback. |

#### SubWindowOptions11+

Describes the parameters used for creating a child window.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title11+ | string | No | No | 
Title of the child window. The title display area should not go past the left side of the three-button area of the system. Any part that goes beyond will show as an ellipsis.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| decorEnabled11+ | boolean | No | No | 

Whether decorations are displayed in the child window. **true** if displayed, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isModal12+ | boolean | No | Yes | 

Whether the modal property is enabled for the child window. **true** if enabled, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| modalityType14+ | [ModalityType](../enums/document.md#modalitytype14) | No | Yes | 

Modality type of the child window. This parameter takes effect only when the modal property is enabled for the child window. The default value is **WINDOW\_MODALITY**.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| windowRect18+ | [Rect](#rect7) | No | Yes | 

Rectangle of the child window, and the size of the child window is limited. For details, see [resize()](../interface-window/document.md#resize9). If this parameter is not set and [showWindow()](../interface-window/document.md#showwindow9) is not called, the default value {left: 0, top: 0, width: 0, height: 0} is used. For details, see [Setting a Child Window of an Application](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-stage#setting-a-child-window-of-an-application).

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| zLevel18+ | number | No | Yes | 

Z-level of the child window. This parameter is valid only when the modal property is not enabled for the child window, that is, **isModal** is not set. The value is an integer in the range \[-10000, 10000\]. Floating-point numbers will be rounded down. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| maximizeSupported19+ | boolean | No | Yes | 

Whether the child window supports maximization. **true** if supported, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**Device behavior differences**: This parameter can be used properly on devices that support the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode and are currently in that mode. On devices that do not support the freeform window mode, the API call will neither take effect nor report an error when this parameter is used as an input. On devices that support the freeform window mode but are not currently in that mode, the API call will neither take effect nor report an error when this parameter is used as an input. The setting will take effect after the devices switch to that mode.

 |
| outlineEnabled20+ | boolean | No | Yes | 

Whether the child window displays an outline. **true** if displayed, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**Device behavior differences**: This parameter works properly on 2-in-1 devices, and on other devices in desktop mode. If it is used as an input parameter in other scenarios, the corresponding API neither takes effect nor reports an error.

 |

#### KeyFramePolicy20+

Describes the configuration for keyframe policies.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enable | boolean | No | No | Whether to enable keyframes. **true** to enable, **false** otherwise. |
| interval | number | No | Yes | Time interval for triggering keyframe layout changes via dragging, in ms. The default value is **1000**. The value is a positive integer. Floating-point values are rounded down. It works with **distance** using an OR condition. If either of them is met, the layout change starts. |
| distance | number | No | Yes | Distance interval for triggering keyframe layout changes via dragging, in px. The default value is **1000**. The value is **0** or a positive integer. Floating-point values are rounded down. If the value is 0, the drag distance is ignored. It works with **interval** using an OR condition. If either of them is met, the layout change starts. |
| animationDuration | number | No | Yes | Duration of the animation for keyframe layout changes, in ms. The default value is **100**. The value is **0** or a positive integer. Floating-point values are rounded down. |
| animationDelay | number | No | Yes | Delay before the animation for keyframe layout changes starts, in ms. The default value is **100**. The value is **0** or a positive integer. Floating-point values are rounded down. |

#### MainWindowInfo21+

Describes the main window information.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| displayId | number | No | No | ID of the display to which the main window belongs. |
| windowId | number | No | No | ID of the main window. |
| showing | boolean | No | No | Foreground/Background status of the main window. **true** if the main window is in the foreground, **false** otherwise. |
| label | string | No | No | Task name of the main window. |

#### WindowSnapshotConfiguration21+

Describes the configuration of the main window screenshot.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| useCache | boolean | No | Yes | Whether the existing screenshot of the main window should be used. The default value is **true**. When it is set to **true**, the system uses the existing screenshot of the main window, or captures the latest screenshot if no existing screenshot is saved. When it is set to **false**, the system captures the latest screenshot of the main window. |
