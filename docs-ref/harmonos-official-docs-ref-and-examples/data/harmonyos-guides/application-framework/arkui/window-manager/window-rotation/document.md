# Window Rotation

#### Overview

Users can hold their mobile devices in various orientations. To ensure an optimal experience, applications sometimes need to adapt their layout to the device's orientation or lock the display to a specific one. For example, games operated with both hands are more suitable for landscape display, whereas video applications often need to switch freely between full-screen and Picture-in-Picture (PiP) playback.

The system provides screen rotation features, allowing you to define how your application responds to orientation changes.

A device has four display orientations. When a user holds the device upright, if the screen width is greater than its height, it is in LANDSCAPE mode, and the opposite orientation is LANDSCAPE\_INVERTED. Conversely, if the screen height is greater than its width, it is in PORTRAIT mode, and the opposite is PORTRAIT\_INVERTED.

The final display orientation is determined by multiple factors: the rotation strategy set by the application, the current holding direction of the device (gravity sensor angle), the system rotation lock switch status (viewable/setting via the pull-down control panel), and the application's scenario (such as split-screen, floating window, or running in the background). Rotation strategies set via the system are effective for the main window, and settings for other windows are ignored.

The general principle of how the "application's scenario" affect the display orientation is as follows:

-   If the application's main window is displayed in full screen, changes in rotation strategies take effect immediately.
    
-   If the application's main window is not displayed in full screen, changes in rotation strategies take effect only when the main window enters full-screen mode.
    

For details about the differences between rotation strategies and device-related differences, see [Rotation Strategies and Device Differences](#rotation-strategies-and-device-differences). For details about the rotation strategies and restrictions in different scenarios, see [Behavior Restrictions of the Rotation API](#behavior-restrictions-of-the-rotation-api).

#### Relationship Between Window Rotation and Screen Orientation

Typically, "window rotation" refers to an application calling the [setPreferredOrientation()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9-1) API to set a rotation strategy, thereby changing the display orientation of the application on the screen. More precisely, this strategy influences the entire screen's orientation, which in turn affects the layout of all on-screen elements, including system components (such as home screen, status bar, pull-down control panel, and pull-down notification center) and other applications. The key point is that changing an application's rotation strategy affects not only the application itself but also all visible elements on the screen, including elements that are invisible in the background. These elements ultimately transition from one direction to another through a rotation animation.

The system provides the screen property [@ohos.display](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display) to obtain basic screen information, where [Orientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#orientation10) represents the current display direction of the device screen. This value updates after a window rotation. It is important to note that [Orientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-e#orientation9) used in the rotation strategy is a different concept from [Orientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#orientation10) used in the screen property, though they share the same names for the four base directions. For details, see [Window Orientation](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-window-direction).

The aspect ratio of the application window has no direct relationship with **Orientation** of the screen property. Use **Orientation** primarily to assist with sensor and camera direction calibration, not for window layout adaptation.

#### Behavior Restrictions of the Rotation API

When a foreground application calls [setPreferredOrientation()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9-1) to set a rotation strategy, the system immediately checks whether the current screen display orientation meets the new strategy.

-   If not, in most cases, the system immediately triggers a rotation animation to comply. For example:
    
    Scenario 1: An application switches from **PORTRAIT** to **LANDSCAPE** while the user holds the phone upright. The application immediately rotates to landscape.
    
    Scenario 2: An application switches from **PORTRAIT** to **AUTO\_ROTATION** while the user holds the phone sideways. The application immediately rotates from portrait to landscape.
    
-   Under special circumstances, such as floating windows, split-screen, multitasking, application background, and free windows, the system ignores the rotation strategy setting. The API call is successful, but the application's display orientation does not change until the application exits these scenarios.
    
    Scenario 1: In special scenarios such as split-screen and floating windows, the system locks the application to portrait for consistency. Setting the rotation strategy to **LANDSCAPE** has no immediate effect.
    
    Scenario 2: In free windows mode, all applications are forced to display in a small window, and rotation strategies are ignored.
    

Additionally, the application's display orientation is strongly related to the sensor. On devices without a sensor, setting the rotation strategy also does not take effect. For example, devices like TVs do not have sensors and can normally call [setPreferredOrientation()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9-1), but the actual orientation does not change.

#### Rotation Strategies and Device Differences

Applications can set their display orientation by configuring the **orientation** field in the [model.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file or by calling the [setPreferredOrientation()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9-1) API to set the **orientation** field at runtime. The meaning of the **orientation** field is the same in both cases, representing the rotation strategy. For details, see [Setting the Window Rotation Policy](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-landscape-and-portrait-development#section58861731201715).

The system provides 18 orientation types to meet the needs of different scenarios. Depending on the usage scenario, these orientation types can be divided into fixed, automatic rotation, temporary, and others.

## Fixed Orientation Types

| Name | Value | Description |
| :-- | :-- | :-- |
| PORTRAIT | 1 | Portrait. |
| LANDSCAPE | 2 | Landscape. |
| PORTRAIT\_INVERTED | 3 | Reverse portrait. |
| LANDSCAPE\_INVERTED | 4 | Reverse landscape. |

These four types lock the application to a specific orientation, regardless of how the user holds the device. They are commonly used in games.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Hy6ANxiEQ_yggoCe9jqkKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13FF5BB65FA7A542B30515CC6343C21A64967825CBCB9DD8534ACEF18CA2C8FD)

[Orientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-e#orientation9) used in the rotation strategy is a different concept from [Orientation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#orientation10) used in the screen property, though they share the same names for the four base directions. For details, see [Window Orientation](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-window-direction).

## Automatic Rotation Orientation Types

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO\_ROTATION | 5 | Automatically rotates with the sensor. The orientation can be portrait, landscape, reverse portrait, or reverse landscape. |
| AUTO\_ROTATION\_PORTRAIT | 6 | Automatically rotates with the sensor in the vertical direction. The orientation can be portrait or reverse portrait. |
| AUTO\_ROTATION\_LANDSCAPE | 7 | Automatically rotates with the sensor in the horizontal direction. The orientation can be landscape or reverse landscape. |
| AUTO\_ROTATION\_RESTRICTED | 8 | Automatically rotates with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation can be portrait, landscape, reverse portrait, or reverse landscape. |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 9 | Automatically rotates with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation can be portrait or reverse portrait. |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | Automatically rotates with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation can be landscape or reverse landscape. |
| AUTO\_ROTATION\_UNSPECIFIED | 12 | Automatically rotates with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation that can be rotated to is determined by the system. For example, the window can rotate to portrait, landscape, or reverse landscape, but not reverse portrait, on a certain device. |

These seven types are commonly used to set the application to adjust its orientation according to the gravity sensor so that the application always displays the page correctly when the user holds the device.

There are some differences in these seven types depending on the usage scenario. For example:

-   Types with **RESTRICTED** (such as **AUTO\_ROTATION\_RESTRICTED**, **AUTO\_ROTATION\_PORTRAIT\_RESTRICTED**, and **AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED**) are controlled by the rotation switch in the control panel. When the rotation lock is enabled, applications set to these types are fixed in the locked direction and no longer adjust the page according to the gravity sensor.
    
-   Types with **PORTRAIT** or **LANDSCAPE** restrict the application to rotate between portrait/inverted portrait and landscape/inverted landscape.
    
-   **AUTO\_ROTATION\_UNSPECIFIED** is a special type that supports auto-rotation and is controlled by the rotation lock switch in the control panel, similar to **AUTO\_ROTATION\_RESTRICTED**.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/1zCFSURfRm6LIkB-dJl4cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEDAA029354CCBB9B621CA898C810527090E1F6AAA26A6228B0B87F5168F7BD6)

**AUTO\_ROTATION\_RESTRICTED** and **AUTO\_ROTATION\_UNSPECIFIED** are very similar in functionality, both supporting automatic rotation controlled by the rotation lock switch. However, there are still some differences between these two rotation strategies on different devices.

-   **System rotation lock switch is off**
    
    **AUTO\_ROTATION\_RESTRICTED** supports rotation to all four directions of the device. However, the rotation orientation supported by **AUTO\_ROTATION\_UNSPECIFIED** is affected by the product form of the system. On a straight-board phone or when the device is in a straight-board-like form factor, applications with this orientation type support rotation to portrait, landscape, and inverted landscape, but not to inverted portrait. On a tablet or when the device is in a tablet-like form factor, applications support rotation to all four directions of the device.
    
-   **System rotation lock switch is on**
    
    On a straight-board phone or when the device is in a straight-board-like form factor, neither **AUTO\_ROTATION\_RESTRICTED** nor **AUTO\_ROTATION\_UNSPECIFIED** supports locking in landscape mode. If an application is set to either of these rotation strategies and rotates to landscape, and then the user pulls down the control panel to enable rotation lock, the application is forced to rotate to portrait and remains in the locked state. On a tablet or when the device is in a tablet-like form factor, both rotation strategies support locking in landscape mode. If an application wants to support automatic rotation on a straight-board phone and can lock to the current direction, **USER\_ROTATION** is recommended.
    

## Temporary Orientation Types

| Name | Value | Description |
| :-- | :-- | :-- |
| USER\_ROTATION\_PORTRAIT | 13 | Temporarily rotates to portrait mode, and then automatically rotates with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation that can be rotated to is determined by the system. |
| USER\_ROTATION\_LANDSCAPE | 14 | Temporarily rotating to landscape mode, and then automatically rotating with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation that can be rotated to is determined by the system. |
| USER\_ROTATION\_PORTRAIT\_INVERTED | 15 | Temporarily rotating to reverse portrait mode, and then automatically rotating with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation that can be rotated to is determined by the system. |
| USER\_ROTATION\_LANDSCAPE\_INVERTED | 16 | Temporarily rotating to reverse landscape mode, and then automatically rotating with the sensor, under the restriction of the rotation switch in the Control Panel. The orientation that can be rotated to is determined by the system. |

These four types support automatic rotation based on the gravity sensor while also being controlled by the rotation lock switch in the control panel. Different from **AUTO\_ROTATION\_RESTRICTED**, these four types immediately temporarily rotate the application to the specified orientation when set. For example, if the user is holding the phone in portrait mode and the application is displayed in portrait, when the application sets the rotation strategy to **USER\_ROTATION\_LANDSCAPE**, the application immediately rotates to landscape display. These four types are commonly used by video applications when switching from PiP playback to full-screen playback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/VWln7BSgT_y_LOfZu1Qh5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A259A7E1B820F8E03435E146D5FEEF27DD0C85150998466209E8D31C63D955DD)

**USER\_ROTATION\_PORTRAIT\_INVERTED** behaves differently across devices.

-   On a straight-board phone or when the device is in a straight-board-like form factor, applications set to the **USER\_ROTATION\_PORTRAIT\_INVERTED** rotation strategy cannot temporarily rotate to inverted portrait. Instead, they still display in portrait mode, and when rotating automatically, they can rotate only to portrait, landscape, and inverted landscape, but not to inverted portrait.
    
-   On a tablet or when the device is in a tablet-like form factor, when the rotation lock switch is off, it supports automatic rotation to portrait, inverted portrait, landscape, and inverted landscape.
    

## Other Orientation Types

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | Unspecified. The orientation is determined by the system. |
| LOCKED | 11 | Locked. |
| FOLLOW\_DESKTOP | 17 | Following the orientation of the home screen. |

These three types are used in the following specific scenarios:

-   **UNSPECIFIED** is the default type used by the system when the application has neither set it in the **model.json5** file nor called **setPreferredOrientation()** at runtime. In this case, the application's display orientation is determined by the system. Typically, on a straight-board phone, the application defaults to portrait display and does not support rotation; on a tablet, it supports rotation to all four directions and is controlled by the system rotation lock switch in the control panel.
    
-   **LOCKED** is commonly used in application launch scenarios. Applications set to this strategy maintain the same orientation as the previous application when launched by another application. The orientation of the application may also change due to application switching and other reasons when this strategy is effective.
    
-   **FOLLOW\_DESKTOP** is a mode that follows the home screen. Typically, the home screen on a straight-board phone is fixed in portrait mode and cannot rotate, while the home screen on a tablet can rotate. Foldable devices are special in that the home screen cannot rotate when the device is folded, similar to a straight-board phone, but it can rotate like a tablet when the device is unfolded.
