# Animation Overview

The UI is an interface for users to interact with devices, containing various visual components (such as buttons and lists). Attributes serve as APIs to control the behavior of components. The change of attribute values will cause the UI to update. Animation adds smooth transition effects when the UI changes, allowing attribute values to gradually change from the start state to the end state, avoiding abruptness caused by instantaneous changes and maintaining the user's visual focus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/5Qyr_ngHSECb38XFZyZMaw/en-us_image_0000002537924740.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061937Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31E7C5D89FC3C1FD49139673C51D4274424FB8D34BCC70C1678C620FFA832EE6)

Animations enable you to:

-   Create smooth transitions between states.
-   Provide visual feedback to give users a sense of control.
-   Inform users of the system status, for example, the loading progress, to make them less stressed while waiting.
-   Show users how to interact with the UI.

Smart use of animations can breathe life into the process of interaction. The frequently seen animations include those that play under device startup, application startup or exit, and pull-down-to-access-the-control-panel scenarios. These animations provide effective user feedback and direct the user attention to where it should be focused.

ArkUI provides a wide range of animation APIs (such as [property animation](../property-animation/property-animation-overview/document.md) and [transition animation](../transition-animation/transition-animation-overview/document.md)), which you can leverage to cause attributes to gradually change from the start value to the end value based on the specified settings. Although attribute values change discretely rather than continuously, the human eye's persistence of vision creates the illusion of smooth animation. Each UI change represents an animation frame, corresponding to a screen refresh. The frame rate, which indicates frames per second (fps), critically affects animation smoothness. Higher frame rates create smoother animations. In ArkUI, animation parameters include animation duration, animation curve, and more. [Traditional curves](../animation-curve/traditional-curve/document.md) in particular influence how attribute values change over time. For example, with a linear animation curve, the attribute changes from the start value to the end value at a constant speed over the given duration. If the attribute changes too fast or too slow, the visual experience may suffer. Therefore, animation parameters, especially animation curves, must be well designed and adjusted to suit specific use cases.

Animation APIs drive attribute values to continuously transit from one state to another according to the rule determined by the animation parameters, and thereby generate a continuous visual effect on the UI. This walkthrough demonstrates the steps and considerations for creating a compelling animation experience.

-   [Property animation](../property-animation/property-animation-overview/document.md): It is the most basic animation type. It drives property changes frame by frame based on animation parameters to create an animation on a frame-by-frame basis. Except for custom property animations, the system handles the animation process with no application-side awareness of the intermediate states.
    
-   [Transition animation](../transition-animation/transition-animation-overview/document.md): It handles component appearance and disappearance transitions. To maintain animation consistency, some animation curves have been built in and cannot be customized.
    
    -   Whenever possible, avoid [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) redirection in your application. A UIAbility is a task in effect and is individually displayed on the recent tasks screen. Redirection between UIAbilities is redirection between tasks. In the typical scenario of viewing large images in an application, if you call the gallery UIAbility from the application to open large images, then the gallery UIAbility will appear on the recent tasks screen. This is not recommended. A more recommended practice is as follows: Build a large image component in the application and invoke that component through modal transition. In this way, the entire animation can be completed in one UIAbility.
    -   To implement navigation, use the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation) component instead of the page+[router](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-router) mode. The latter causes page separation, which complicates transition effect synchronization. and hinders one-time development for multi-device deployment.
-   [Particle animation](../particle-animation/document.md): Enhance visual effects with a multitude of particles based on certain principles.
    
-   [Component animation](../component-animation/document.md): Components provide default animations (such as the scroll animation of the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component) with some supporting customization.
    
-   [Animation curve](../animation-curve/traditional-curve/document.md): You can use traditional and spring curves to control property value changes, creating engaging animation effects.
    
-   [Animation smoothing](../animation-smoothing/document.md): Ensure natural transitions between animations and between gestures and animations.
    
-   [Animation effect](../animation-effects/blur-effect/document.md): Enhance animations with blur, shadow, color gradient, and other sophisticated effects.
    
-   [Frame animation](../frame-animation-ohos-animator/document.md): The system provides interpolated values during the animation process, requiring you to manually update property values each frame to generate animation effects. Compared with the property animation, this type of animation offers the advantage of pause/resume animation control, but with inferior performance.
