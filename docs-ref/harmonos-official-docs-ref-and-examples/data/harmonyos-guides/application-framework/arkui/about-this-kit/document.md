# About This Kit

ArkUI provides a comprehensive infrastructure for application UI development, including simple UI syntax, a diverse array of UI features (components, layouts, animations, and interaction events), and powerful preview tools.

#### Basic Concepts

-   **UI**: user interface. You can design the application's UI into multiple functional pages using [NavDestination](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navdestination). These pages are managed in a stack structure, and transitions between them, such as navigating to a new page or going back to the previous one, are handled by the navigation container [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation), enabling functional decoupling within the application.
    
-   **Component**: the smallest unit for UI building and display, for example, a list, grid, button, radio button, progress indicator, and text. You build a UI that meets your needs through flexible combinations of components.
    

#### Two Development Paradigms

ArkUI comes with two development paradigms: [ArkTS-based declarative development paradigm](../ui-development-arkts-based-declarative-development-paradigm/ui-development-arkts-based-declarative-development-paradigm-overview/document.md) (declarative development paradigm for short) and [JavaScript-compatible web-like development paradigm](../ui-development-javascript-compatible-web-like-development-paradigm/ui-development-javascript-compatible-web-like-development-paradigm-overview/document.md) (web-like development paradigm for short). You can choose whichever development paradigm that aligns with your practice.

-   **Declarative development paradigm**: uses the [ArkTS language](../../../getting-started/learning-arkts/getting-started-with-arkts/document.md), which extends TypeScript with declarative UI syntax, to provide UI drawing capabilities from three dimensions: components, animations, and state management.
    
-   **Web-like development paradigm**: uses the classical three-stage programming model, in which HML is used for building layouts, CSS for defining styles, and JavaScript for adding processing logic. This development paradigm has a low learning curve for frontend web developers, allowing them to quickly transform existing web applications into ArkUI applications.
    

The declarative development paradigm is a better choice for building new application UIs for the following reasons:

-   **Higher development efficiency**: In the declarative development paradigm, the programming mode used is closer to natural semantics. You can intuitively describe the UI without caring about how the framework implements UI drawing and rendering, leading to simplified and efficient development.
    
-   **Higher application performance**: As shown below, the two development paradigms share the UI backend engine and language runtime. However, the declarative development paradigm does not require the JavaScript framework for managing the page DOM. As such, it has more streamlined rendering and update links and less memory usage.
    
-   **Future proof**: The declarative development paradigm will continue to develop as the preferred development paradigm, providing increasingly diverse and powerful capabilities.
    
    **Figure 1** ArkUI framework
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/5tYRmlZgSuqi7IeZQ_phGg/en-us_image_0000002537924338.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061926Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C969493A946D104A06F47C691243324EA2B20E5198BB07C11AFB4E6C5359896F)
    

#### Development Paradigm Support by Application Type

The supported development paradigm varies according to the [application model](../../ability-kit/application-models/document.md) and page form. For details, see the following table.

**Table 1** Supported development paradigms

| Application Model | Page Form | Supported Development Paradigm |
| :-- | :-- | :-- |
| Stage model (recommended) | Application or service page | Declarative development paradigm (recommended) |
| Stage model (recommended) | Widget | 
Declarative development paradigm (recommended)

Web-like development paradigm

 |
| FA model | Application or service page | 

Declarative development paradigm

Web-like development paradigm

 |
| FA model | Widget | Web-like development paradigm |

#### Layered API Architecture and Selection Guidelines

-   **Declarative development paradigm**: Built on ArkTS, this paradigm automatically renders UIs by declaring UI structure and state. You define "what the UI should be" rather than managing updates manually. This paradigm is suitable for complex applications and team collaboration scenarios.
    
    **Recommended for**: new projects and applications requiring rapid development with sustained maintainability.
    
-   **Customization capabilities**: ArkUI supports multi-layer customization capabilities, including custom composition, custom extensions through [modifiers](../ui-development-arkts-based-declarative-development-paradigm/using-customization-capabilities/modifier/custom-extension-capability-overview/document.md)), custom node types ([FrameNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-framenode), [RenderNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-rendernode), and [BuilderNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-buildernode)), and custom rendering. You can choose different levels of customization based on your service requirements.
    
    Recommended for: specialized UI requirements, low-level rendering control, and deep system integration.
    
-   **NDK development**: The ArkUI framework offers NDK APIs for building UIs with C/C++, including component creation, UI tree control, attribute configuration, and event handling. For details, see [NDK API Overview](../using-ndk-apis-to-build-uis/ndk-based-ui-development-overview/document.md).
    
    **Recommended for**: performance-critical applications, fine-grained UI control, and integration with existing C/C++ libraries.
