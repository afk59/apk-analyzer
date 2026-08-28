# About This Kit

Ability Kit provides an application model for application development and running. The application model is the abstraction of capabilities required by an application. It provides components and mechanisms required for running the application. You can develop applications based on a unified set of models, which makes your development simpler and more efficient.

#### Use Scenarios

-   Multi-module development: You can use different types of modules ([HAP](../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md), [HAR](../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/har/document.md), and [HSP](../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hsp/document.md)) to develop an application. The HAP is used to implement application features, and the HAR and HSP are used to share code and resources.
-   Intra-application interaction: Redirection is allowed between components of an application. For example, in a mobile office application, you may need to start a video meeting UIAbility from the entry UIAbility. For details, see [Starting UIAbility Within the Same Application](../stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md).
-   Inter-application interaction: An application can start another application to complete a task or operation. For example, when making a purchase in an e-commerce application, you can be redirected to a payment application to complete the transaction. For details, see [Application Redirection](../stage-model-development/inter-application-redirection/overview-of-application-redirection/document.md).
-   Cross-device hopping: Your application delivers a better user experience through cross-device migration and multi-device collaboration. For example, you migrate a video playback task from a tablet to a smart TV. For details, see [Hopping](../../../hopping/hopping-overview/document.md).

#### Capability Scope

-   Provides APIs to create or destroy an application process, and schedule the application lifecycle.
-   Provides an entry to run application components, schedule the application component lifecycle, and enable interaction between components.
-   Provides APIs to listen for application context changes, system environment changes, and component lifecycle changes.
-   Provides the capabilities of AppStartup. For details, see [AppStartup](../stage-model-development/stage-model-application-components/appstartup/document.md).
-   Provides the capabilities of the InsightIntent framework. For details, see [InsightIntent Framework Overview](../stage-model-development/insightintent-framework-development/insightintent-framework-overview/document.md).
-   Provides APIs to continue an application on another device.
-   Provides capabilities such as multi-package, shared package, and application information configuration. For details, see [Application Package Overview](../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-overview/document.md).
-   Provides APIs related to shortcuts. For details, see [Shortcuts](../../../getting-started/development-fundamentals/typical-scenarios-development/creating-a-static-shortcut-of-the-application/document.md).
-   Provides access control capabilities. For details, see [Access Control Overview](../../../system/security/application-access-control/access-control-overview/document.md).
-   Provide the security password autofill function. For details, see [Overview of Password Autofill](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/passwordvault-overview-V5).

#### Highlights

1.  **Separation of UI and service logic**
    
    This architecture enforces a development paradigm where service logic and UI interactions are clearly separated.
    
    -   From service logic to UI: Developers implement core service logic within the ability. Data is then passed to the UI framework through binding mechanisms. Based on declarative syntax, ArkUI automatically renders the view and triggers UI updates when the state changes.
    -   From UI to service logic: User inputs captured from UI interactions are synchronized back to the ability framework through event callbacks or state binding mechanisms, reflecting the user's actions in the service logic layer.
2.  **Support for cross-device migration and multi-device collaboration at the application component level**
    
    The [stage model](../ability-kit-terminology/document.md#stage-model) decouples application components from UI.
    
    -   The declarative feature of ArkUI allows the UI to be restored based on the data or status saved in application components, which facilitates cross-device migration.
    -   Application components support cross-device interaction over Remote Procedure Calls (RPCs).
3.  **Support for multiple device types and window forms**
    
    Application component management and window management are decoupled at the architecture level. This decoupling makes it easy to:
    
    -   Tailor application components. For example, windows can be tailored for devices without screens.
    -   Extend the window forms.
    -   Use the same application component lifecycle on multiple devices (such as desktop devices and mobile devices).
4.  **Well balanced application capabilities and system management costs**
    
    The stage model redefines the boundary of application capabilities to well balance application capabilities and system management costs.
    
    -   Diverse application components (such as service widgets and input methods) for specific scenarios.
    -   Standardized background process management. To deliver a better user experience, the stage model manages background application processes in a more orderly manner. Applications cannot reside in the background randomly, and their background behavior is strictly managed to minimize malicious behavior.

#### Relationship with Related Kits

ArkUI: The UIAbility component of Ability Kit can use the components, events, animations, and status management capabilities provided by ArkUI.

ArkTS: provides language runtime capabilities for Ability Kit.

#### Emulator Support

This kit supports development using the Emulator. However, there are some functional differences compared to real devices, as detailed below:

-   Launching vertical application panels is not supported.
-   Launching atomic services in installation-free mode is not supported.
-   Using App Linking for cross-application redirection is not supported.
-   Using Deep Linking to trigger the application selection dialog box is not supported. Since the Emulator lacks an application selection dialog box, when multiple applications match a Deep Link, the dialog box cannot be displayed.
