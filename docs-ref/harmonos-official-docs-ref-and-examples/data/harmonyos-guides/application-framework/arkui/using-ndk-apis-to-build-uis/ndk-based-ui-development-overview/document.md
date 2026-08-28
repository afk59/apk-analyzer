# NDK-Based UI Development Overview

The ArkUI framework offers [NDK APIs](../../../../ndk-development/about-this-kit/document.md) for building UIs with C/C++, including component creation, UI tree control, attribute configuration, and event listening. While ArkTS and the ArkUI declarative framework are recommended for most UI development, use the ArkUI NDK APIs when:

-   You need to dynamically create and mount UI components for bridging to your own UI framework.
    
-   You aim to reuse C or C++ UI libraries developed by yourself or others.
    

The ArkUI NDK APIs provide the following capabilities:

-   **Layout**
    
    Layout defines the size and position of components on the UI. The ArkUI NDK APIs offer linear, stacking, flexbox, relative layouts, and scrollable and carousel containers.
    
-   **Component**
    
    Components are essential for UI, shaping the appearance on the screen. They include both built-in components and custom components with user-defined layout and drawing behaviors. Built-in components, such as buttons, radio buttons, images, and text, can be quickly created and have their attributes and events set using the ArkUI NDK APIs. Customization capabilities for UI components encompass layout measurement and drawing, enabling the construction of distinctive UI components.
    
-   **Dialog box**
    
    Dialog boxes are vital for UI interactions. ArkUI NDK APIs enable the creation and display of custom dialog boxes with user-defined content.
    
-   **Animation**
    
    Animations are one of the key elements of UI. The ArkUI NDK provides explicit animation APIs for crafting property animations that enhance user experience with efficient and sophisticated effects.
    
-   **Interaction event**
    
    Interaction events are important for interactions between the UI and users. The ArkUI NDK allows users to interact with your application UI, with support for various universal events and gesture events. Universal events include touch events, mouse events, and focus events. Gesture events accept single gestures (tap, long press, pan, pinch, rotation, and swipe), and a combination of gestures.
    

#### Overall Architecture

**Figure 1** Relationship between NDK APIs and the ArkTS declarative UI

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/DhqmDUwmT4ivljf7_tapHw/en-us_image_0000002568764609.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93BD016881842A5EB8B1EB3314AB87D0E6216F6BA1E1788F663E887CE1806762)

**Figure 2** Schematic diagram of component mounting through NDK APIs

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/MaDCRf9USEumqfXyMWMiKw/en-us_image_0000002537764884.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=002799000A37D6B186CF6281E2EFB81FDC951907FE5B4C0BAC2E1F948D2B07DA)

-   The ArkTS declarative UI frontend and the NDK APIs both expose ArkUI's underlying capabilities. Compared to the ArkTS declarative UI frontend, NDK APIs not only strip away the declarative UI syntax such as state management but also streamline component capabilities, encapsulating the core functions of ArkUI components through C APIs.
    
-   NDK-created UI components must be mounted through ArkTS placeholder components. Once mounted, they coexist with ArkTS components on the same UI tree, following uniform layout and event-handling rules.
    

#### How to Develop

Using the NDK for UI development involves the following tasks.

| Task | Description |
| :-- | :-- |
| [Getting Started with the NDK](../../../../ndk-development/about-this-kit/document.md) | Introduces the use scenarios and essential knowledge of the NDK. |
| [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md) | Explains how to mount the NDK-developed UI onto ArkTS pages for rendering and display. |
| [Adding Interaction Events](../adding-interaction-events/listening-for-component-events/document.md) | Describes how to add interaction events for components. |
| [Using Animations](../using-animations/document.md) | Introduces how to add animations on the native side. |
| [Building Layouts](../building-a-layout/implementing-a-list-layout/document.md) | Describes how to use container components to build layouts on the native side. |
| [Building Dialog Boxes](../building-a-dialog-box/document.md) | Introduces how to build dialog boxes. |
| [Building Custom Components](../building-custom-components/document.md) | Describes how to build custom components with the NDK to achieve unique UI elements. |
| [Embedding ArkTS Components](../embedding-arkts-components/document.md) | Explains how to build pages on the native side that include ArkTS components. |
| [Building a Rendering Node](../building-a-rendering-node/document.md) | Explains how to build a rendering node on the native side. |
| [Integrating Accessibility Through XComponent](../integrating-accessibility-through-xcomponent/document.md) | Describes how to connect third-party systems to the UI platform through **XComponent**. |
| [Implementing Custom Drawing](../custom-drawing/document.md) | Describes how to use custom drawing capabilities to render custom content. |
| [Querying and Operating Custom Nodes](../querying-and-operating-custom-nodes/document.md) | Introduces how to query and operate custom nodes. |
| [Launching EmbeddedUIExtensionAbility with EmbeddedComponent](../launching-embeddeduiextensionability-with-embeddedcomponent/document.md) | Introduces how to launch **EmbeddedUIExtensionAbility** with **EmbeddedComponent** on the native side. This is mainly used in modular development scenarios with process isolation requirements. |
| [Using Text](../using-text/drawing-and-displaying-text-in-text-components/document.md) | Introduces how to use the **Text** component and font engine. |
| [Ensuring Multi-Instance Functionality in the NDK](../ensuring-multi-instance-functionality-in-the-ndk/document.md) | Introduces how to ensure the normal functionality of API calls in NDK multi-threaded scenarios. |
| [Parallelizing UI Page Building Using Multi-threaded NDK APIs](../parallelizing-ui-page-building-using-multi-threaded-ndk-apis/document.md) | Introduces how to create multi-threaded UI components using NDK. |

#### Precautions

When using NDK APIs to develop UIs, ensure that all UI API calls are made on the application's main thread to prevent multi-threading issues, which can lead to crashes.
