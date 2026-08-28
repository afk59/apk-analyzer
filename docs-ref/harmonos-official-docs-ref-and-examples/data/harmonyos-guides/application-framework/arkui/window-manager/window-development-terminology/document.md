# Window Development Terminology

#### Window Type

Windows are classified into system windows and application windows.

## System Window

System windows are designed to carry out specific system functions. Examples include volume bars, wallpapers, notification panels, status bars, and navigation bars.

System windows are available only for system applications.

## Application Window

Application windows, which are different from system windows, are related to the display of application content. Depending on how they are managed and their purpose, application windows can be further divided into main windows and auxiliary windows.

-   Main window
    
    Main windows are created by default when a UIAbility is created and are displayed as an independent mission card on the mission management screen. They are used to show the main interface of the application's UIAbility.
    
-   Auxiliary window
    
    Auxiliary windows are managed, created, and destroyed by the application itself and are not displayed as an independent mission card on the mission management screen. They can be used to show auxiliary content of the application, such as pop-up windows.
    
    Auxiliary windows include child windows, global floating windows, modal windows, picture-in-picture, and floating ball windows.
    

#### Floating Window

Floating windows are divided into multi-window floating windows and global floating windows.

-   Multi-window floating windows are non-full-screen application windows that float on the device screen.
    
    They are typically used to temporarily handle another task while a full-screen task is running or for short-term parallel use of multiple tasks, such as replying to messages while browsing the web.
    
    For details, see [Introduction to Multi-Window](../adapting-your-app-to-multi-window/introduction-to-multi-window/document.md) and [Multi-Window](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-window-practice).
    
-   Global floating windows are a special type of application auxiliary window that can remain displayed on the foreground even after the application's main window and corresponding ability are moved to the background.
    
    Global floating windows can be used to continue displaying the UI in a small window after the application is moved to the background, such as displaying lyrics on the home screen for a music application.
    
    Before creating a global floating window, the application needs to request the corresponding permission.
    

For details, see [Setting a Global Floating Window](../application-window-development-stage-model/document.md#setting-a-global-floating-window-restricted-permission).

#### Freeform Window

Freeform windows are a type of window that can be displayed on the same screen with flexible size and position. These windows support multitasking features such as dragging, resizing, and split-screen combinations.

Freeform windows are stacked on the Z-axis in the order they are opened or gain focus. When a freeform window is clicked or touched, it is brought to the front and gains focus.

When a new freeform window is launched, it appears with a certain gap in the bottom-right corner of the previous window by default.

Each freeform window includes a window title bar at the top by default. The title bar displays the application icon on the left and three control buttons on the right: maximize/restore, minimize, and close. The window title bar also supports [immersive configurations](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-window-immersive#section359241062916).

You can resize a freeform window by dragging its edges and move its position by dragging the title bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/RLSFzyfZRLq8yGxpuLDH6A/en-us_image_0000002568684707.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2D73B8420BFDAA65B6278A42DD12A16ED628A68BD5FB9866DCFD16FC731381E)

**Device Support**

-   **2-in-1 devices**: Windows on 2-in-1 devices are freeform window by default.
-   **Tablets**: Some tablets support enabling [free windows](#free-windows) mode by pulling down Control Panel and tapping the **Free windows** button. Once this mode is enabled, application windows default to freeform windows.
-   **Phones**: Some phones support enabling [free windows](#free-windows) mode by pulling down Control Panel and tapping the **Free windows** button. Once this mode is enabled, application windows default to freeform windows.

## Free Windows

Free windows mode is an interaction method that enables multitasking on mobile devices.

It allows multiple application windows to be displayed on a single screen simultaneously. These windows are known as [freeform window](#freeform-window).

On some tablets, you can enable free windows mode by pulling down Control Panel and tapping the **Free windows** button.

On some phones, you can enable free windows mode by pulling down Control Panel and tapping the **Free windows** button.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/er2lEAwYRnGtnUhgXysGig/en-us_image_0000002568764717.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1018225154A8F01528A286ADED3C97FC6012689811AA8DA2CE768E26502900C)

#### Immersive Layout

An immersive layout is a window state that helps an application UI focus on content by reducing distractions from irrelevant elements.

Non-[freeform windows](#freeform-window) can enter immersive layout by calling [setWindowLayoutFullScreen](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowlayoutfullscreen9).

| Non-immersive layout of a non-freeform window | Immersive layout of a non-freeform window |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/oVd_KPySTamX8gs8r31jAw/en-us_image_0000002537764992.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07133B1125D270F0C8B6B105B10FD6D6C51CE41510B7EC302A6F55EEDB4DEA5C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/HG45WvoqTqOKWdUntwFbyA/en-us_image_0000002537924932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAB8931D24CFB275D182A5584147E90E0D5AF608B9B2888BF072F502A3EA0C88) |

Freeform windows can enter immersive layout by hiding the decoration bar.

| Non-immersive layout of a freeform window | Immersive layout of a freeform window |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/an-4cMdWRcOB1D9h7VTygA/en-us_image_0000002568684709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEC4F2D744B7407858888E1CB36332440AE98AD4748CA94C486FCAF30FA47137) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/BAAWly7jSVS-G6qFdWb6RA/en-us_image_0000002568764719.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB56B5B606510FD8AFFF510A77C77115190CC2A989668587F99AC96798D51A27) |

In immersive layout, an application window's component layout expands from the safe area to the entire window. You can use [isImmersiveLayout](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#isimmersivelayout20) to check whether the window is in immersive layout.

For details about immersive development and implementation in different window forms in multi-device scenarios, see [Immersive Window](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-window-immersive).

#### Global Coordinate System

The global coordinate system refers to a coordinate system that uniformly describes the positions of objects such as windows and pointers in scenarios where a device is connected to an [extended screen](../../display-management/display-management-development-terminology/document.md#extended-screen) (multiple physical screens). It takes the upper-left corner of the main screen as the origin (0, 0), with the right side of the screen as the positive direction of the x-axis and the bottom side of the screen as the positive direction of the y-axis.

In this coordinate system, all physical screens are mapped to the same continuous virtual coordinate space. Various window operations, coordinate conversions, and window rectangle change events are calculated and callback based on this coordinate space.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/JOMpbthjSMe_Mcj7AO2q6g/en-us_image_0000002537764994.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061946Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=719D7CAC786FC1754BD2B16934BFE53AB52396CEC97800BA03590A85B1686D0D)

Usage scenarios:

-   Cross-screen window movement: Call the API based on the global coordinate system to move a window. There is no need to pass specific screen ID parameters to move the window between multiple screens.
-   Window position change monitoring: Monitor window rectangle change events based on the global coordinate system to uniformly obtain information about changes in the position and size of the window in a multi-screen environment.
