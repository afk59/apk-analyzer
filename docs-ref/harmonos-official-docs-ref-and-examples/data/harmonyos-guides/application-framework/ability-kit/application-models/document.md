# Application Models

#### Elements of the Application Model

An application model is the abstraction of capabilities required by an application. It provides components and mechanisms required for running the application. You can develop applications based on a unified set of models, which makes your development simpler and more efficient.

The application model consists of the following elements:

-   Application component
    
    An application component is the basic unit and entry for the running of an application. When a user starts, uses, or exits an application, the application component transits in different states. This is called the [application component lifecycle](../stage-model-development/stage-model-application-components/uiability-component/uiability-lifecycle/document.md). The application component provides lifecycle callbacks, through which you can detect application status changes. When writing an application, you need to compile application components and their lifecycle callbacks, and configure related information in the application configuration file. In this way, the operating system creates an application component instance based on the configuration file during running, and schedules the lifecycle callbacks to execute your code.
    
-   Process model
    
    The process model defines how application processes are created, destroyed, and communicate with each other.
    
-   Thread model
    
    The thread model defines how a thread in an application process is created and destroyed, how the main thread and UI thread are created, and how the threads communicate with each other.
    
-   Mission Management Model (for System Applications Only)
    
    The mission management model defines how a mission is created and destroyed, and the relationship between missions and application components. A mission is a record about the use of an application component instance. Each time a user starts an application component instance, a mission is generated. For example, when a user starts a video application, the video application mission is displayed on the recent task page. When the user clicks the mission, the system switches the mission to the foreground. If the video editing feature in the video application is coded based on an application component, an application component instance for video editing is created when the user starts video editing. In this case, both the video application mission and video editing mission are displayed on the recent task page.
    
-   Configuration file
    
    The configuration file contains information about the application's configuration, components, and permissions, as well as custom information. The information will be provided for the compiler, application market, and operating system in the build, distribution, and running phases.
    

#### Application Model Overview

Along its evolution, the system has provided two application models:

-   [Feature Ability (FA) model](../ability-kit-terminology/document.md#fa-model): This model has been supported since API version 7, and is no longer recommended.
    
-   [Stage model](../ability-kit-terminology/document.md#stage-model): This model is supported since API version 9. It is the mainstream model with a long evolution plan. In this model, classes such as **AbilityStage** and **WindowStage** are provided as the stage of application components and windows. That's why it is named stage model.
    

#### Differences Between the FA Model and Stage Model

In the FA model, each application component exclusively uses an ArkTS engine instance. However, in the stage model, multiple application components share the same ArkTS engine instance. This allows application components to share objects and statuses with less memory required. With the stage model, you can easily develop complex applications in distributed scenarios.

The table below describes their differences in detail.

**Table 1** Differences between the FA model and stage model

| Item | FA model | Stage model |
| :-- | :-- | :-- |
| **Application component** | 
1\. Component classification

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/AEKmqFFFSL25ARMurJz6CA/en-us_image_0000002537924282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=724C24E68F32F0E4B06351308D00836DAD3085486FBA4FFD5579840D7515BE23)

\- PageAbility: supports user interaction via the UI. For details, see [PageAbility Component Overview](../fa-model-development/fa-model-application-components/pageability-component-development/pageability-overview/document.md).

\- ServiceAbility: provides background services without the UI. For details, see [ServiceAbility Component Overview](../fa-model-development/fa-model-application-components/serviceability-component-development/serviceability-overview/document.md).

\- DataAbility: provides the data sharing capability without the UI. For details, see [DataAbility Component Overview](../fa-model-development/fa-model-application-components/dataability-component-development/dataability-overview/document.md).

2\. Development mode

Application components are specified by exporting anonymous objects and fixed entry files. You cannot perform derivation. It is inconvenient for capability expansion.

 | 

1\. Component classification

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/t_yIPfMrQuG_ftG_cuqtnA/en-us_image_0000002568684059.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C1164087B189056331E6AA7D5F21FBBBCC6D8B3E51FF5661A33FC68E8A64A37)

\- UIAbility: supports user interaction with the UI. For details, see [UIAbility Component Overview](../stage-model-development/stage-model-application-components/uiability-component/uiability-overview/document.md).

\- ExtensionAbility: provides scenario-specific extension capabilities (such as widget and input methods). For details, see [ExtensionAbility Component Overview](../stage-model-development/stage-model-application-components/extensionability-component/document.md).

2\. Development mode

The object-oriented mode is used to provide open application components as classes. You can derive application components for capability expansion.

 |
| **Process model** | 

There are two types of processes:

1\. Main process

2\. Render process

For details, see [Process Model](../fa-model-development/process-model-fa-model/document.md).

 | 

There are three types of processes:

1\. Main process

2\. ExtensionAbility process

3\. Render process

For details, see [Process Model](../stage-model-development/process-model/document.md).

 |
| **Thread model** | 

1\. ArkTS engine instance creation

A process can run multiple instances of application components, and each instance runs in an independent ArkTS engine instance.

2\. Thread model

Each ArkTS engine instance is created on an independent thread (non-main thread). The main thread does not have an ArkTS engine instance.

3\. Intra-process object sharing: not supported.

For details, see [Thread Model](../fa-model-development/thread-model-fa-model/document.md).

 | 

1\. ArkTS engine instance creation

A process can run multiple application component instances, and all application component instances share one ArkTS engine instance.

2\. Thread model

The ArkTS engine instance is created on the main thread.

3\. Intra-process object sharing: supported.

For details, see [Thread Model](../stage-model-development/thread-model-stage-model/document.md).

 |
| **Configuration file** | 

The **config.json** file contains the application, HAP, and application component information.

For details, see [Application Configuration File Overview (FA Model)](../../../getting-started/development-fundamentals/application-configuration-files-in-fa-model/application-configuration-files-fa-model/document.md).

 | 

The **app.json5** file contains the application information, and the **module.json5** file contains the HAP and application component information.

For details, see [Application Configuration File Overview (Stage Model)](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/application-configuration-files-stage-model/document.md).

 |
