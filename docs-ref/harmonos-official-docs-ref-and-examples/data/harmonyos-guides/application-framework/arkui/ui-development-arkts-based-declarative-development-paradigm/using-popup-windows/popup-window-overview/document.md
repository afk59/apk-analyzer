# Popup Window Overview

A popup window is a UI element that automatically appears when an application is launched or when a user performs a specific action. It is designed to present important information or actions that require the user's attention within a short timeframe.

In the ArkUI component tree, regular overlays, popup windows, modals, and ordered overlays are all mounted under the root node Popup windows, modals, and ordered overlays are displayed in layers based on their assigned z-order values, appearing above all regular overlays. The figure below illustrates the structure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/cL9JcxVjQLCu7CDPSdETJg/en-us_image_0000002537764720.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A9A430AACC619D7F3B3EA39833A50F9EB0A093506C812A71789518B6EEC9EED)

For a multi-page application, the basic tree structure is as shown below. Multiple Page-level pages are navigated using the [Router](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-router) APIs. Pages composed of [NavBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#navbar12) and [Navdestination](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navdestination) are navigated via the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation) component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/k3-FQSLlTQuBuPlO3gUSbg/en-us_image_0000002537924660.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAFA3CF5C4F933D6DB03CD25177BB2174FE0DE44F273C2DB2BA7D01FD780948B)

When used together with routing and navigation, components created using [Dialog](../dialog-boxes-dialog/dialog-box-overview/document.md), [Popup](../using-popups/popup-overview/document.md), [Menu](../using-menus/menu-overview/document.md), [OverlayManager](../managing-overlays-overlaymanager/document.md), [Toast](../using-toasts-toast/document.md), [bindSheet](../binding-modal-pages/binding-a-modal-sheet-bindsheet/document.md), or [bindContentCover](../binding-modal-pages/binding-a-full-modal-page-bindcontentcover/document.md) can appear in the following display modes:

-   The dialog box is displayed at the topmost layer of the application window, above all pages in the main window (default behavior).
    
    As shown below, when a dialog box is displayed, it sits above both **Page** pages and **Navigation** pages. If the dialog box is not closed, it will remain visible during page switching, and the new routing or navigation page will not overlay it.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/QotYwW82Rvm_ooJ9pG6AzA/en-us_image_0000002568684437.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4682427A74EF390201EB00242651247EBA37D7BB6AB10A9824486DD89E1B6F03)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/1aj3Dl1FQ7C_-iXwhYpS6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA84D1EDCACB75A39ECFDFE86772FD4E4307ADF7F0D8C2581761EF1E42DAEC46)
    
    If a dialog box component (such as **Popup** or **Menu**) is bound to a component that is no longer displayed after a page jump, the system will automatically close that dialog box. However, because the dialog box's visibility is also controlled by developer-set parameters (such as the **show** parameter of [Popup](../using-popups/popup-overview/document.md)), the dialog box may still appear overlaying the next page.
    
-   The dialog box is displayed within the current page, below the next page.
    
    To restrict a dialog box to a single page (ensuring the dialog box is covered by the new page during routing/navigation-based page switching, and reappears normally when the user returns to the original page), the component hierarchy should be structured as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/7EizrtOAQjaWsICTQ6IVkw/en-us_image_0000002568764447.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C7BE7CCCEADCE0FAD4333ECCF597B2A49638F2883B3742B4C1E258EB5B45AAD)
    
    Page-level dialog box capabilities must be used in conjunction with the page-level support feature of the dialog box component. Currently, [Dialog](../dialog-boxes-dialog/dialog-box-overview/document.md) and [bindSheet](../binding-modal-pages/binding-a-modal-sheet-bindsheet/document.md) support page-level behavior.
    
-   The dialog box is displayed in an independent window, which is above the application window.
    
    On devices such as PCs/2-in-1 devices, you may need to display dialog boxes outside the application window. This requires the subwindow capability, which can be enabled for custom dialog boxes via the **showInSubWindow** property in [CustomDialogControllerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontrolleroptions). An example of a dialog box displayed in a subwindow is shown below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/o4iX14h2SWa_i7tyrX62rA/en-us_image_0000002537764722.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB9FFF1D223AA0EFC26CB39A61B14D30D64B8178C4FFAB1C62101FF5597290EC)
    
    In this case, the dialog box's display order is managed by the window stack manager, placing it above the current application window but below system windows (for example, system input methods and system dialog boxes).
    

#### Types of Popup Windows

Popup windows can be categorized based on the level of user interaction required. There are two main types: modal and non-modal popup windows. The key difference between them lies in whether the user must interact with the popup window.

-   **Modal popup window**: This type of popup window is a strong interaction element. It interrupts the user's current task and requires a response before the user can proceed with other actions. It is typically used when important information needs to be conveyed to the user.
-   **Non-modal popup window**: This is a weaker form of interaction and does not interfere with the user's current tasks. The user is not required to respond to the popup window, which usually has a time limit and disappears automatically after a set period. This type is generally used when users need to perform additional actions while being notified of certain information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Dq25CJY3Qyupuk2-xFcosA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06958D2AFB5323301BF89A4BA77948918E446A398999CC87B615719EE57F5603)

A modal popup window can be converted to a non-modal one through specific attributes. For example, setting the **isModal** attribute of [AlertDialogParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-alert-dialog-box#alertdialogparam) to **false** for **AlertDialog** will change it from modal to non-modal. For more details on other popup windows, see the respective API references.

Avoid calling popup window display APIs when the application runs in the background.

System popup windows are managed by the system and do not support style customization for security reasons.

When a system popup window displays, call non-system popup window display APIs (such as [openCustomDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-promptaction#promptactionopencustomdialogdeprecated) of [promptAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-promptaction) and [open](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-custom-dialog-box#open) of [CustomDialogController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontroller)) to disable the popup window display.

#### Use Cases

Choose the appropriate component based on your specific requirements.

| Popup Window Name | Use Case |
| :-- | :-- |
| [Dialog](../dialog-boxes-dialog/dialog-box-overview/document.md) | Use this popup window when you need to display information or actions that require the user's attention, such as when exiting the application for the second time. |
| [Menu (Menu/openMenu)](../using-menus/menu-overview/document.md) | Use this popup window to bind actions to specified components, such as displaying operation options when an icon is long-pressed. |
| [Popup (Popup/openPopup)](../using-popups/popup-overview/document.md) | Use this popup window to display a hint for a specific component, for example, a tooltip when a question mark is clicked. |
| [Modal page (bindContentCover/bindSheet)](../binding-modal-pages/modal-page-overview/document.md) | Choose this popup window when a new page needs to overlay the old one without making the old page disappear, such as viewing a large image by clicking a thumbnail. |
| [Toast](../using-toasts-toast/document.md) | Use this popup window to provide simple feedback on the user's current action in a small window, like displaying a message that a file has been saved successfully. |
| [Overlay (OverlayManager)](../managing-overlays-overlaymanager/document.md) | Use this popup window when you need to customize the content, behavior, and style, and want to display a floating layer on top of the page, such as a music or voice playback floating bubble. |

#### Specifications Constraints

-   When multiple popup window components are displayed in sequence, the layer of the later displayed component is higher than that of the earlier one, and they exit in the reverse order of their display.
    
-   On mobile devices, a popup window in subwindow mode cannot exceed the main window. On a 2-in-1 device, a modal popup window may need to be displayed beyond the main window. In this case, you can set **showInSubWindow** to **true** to achieve this effect. The following figure shows the effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/MjkZerMRT12yZWtfx8NDVw/en-us_image_0000002537924662.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB9CA710A271C4ED919DBD7A95F2B1AAD18D63A374AA1B3B4AFB5AF7ACA8985E)
