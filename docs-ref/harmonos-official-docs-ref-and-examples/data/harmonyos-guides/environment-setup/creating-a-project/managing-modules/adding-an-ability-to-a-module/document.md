# Adding an Ability to a Module

An ability is an abstraction of the capabilities of an app/atomic service. A module of an app can contain one or more abilities, while a module of an atomic service can contain only one ability. To understand the ability, first familiarize yourself with the two application models:

-   Feature Ability (FA) model: This model is supported since API version 7, and no longer recommended.
-   Stage model: This model is supported since HarmonyOS 3.1 Developer Preview. It is the mainstream model with a long evolution plan. In this model, classes such as **AbilityStage** and **WindowStage** are provided as the stage of app components and windows. That's why it is named stage model.
    
    The stage model comes with two types of abilities:
    
    -   UIAbility: has the UI and supports user interaction. For details, see [UIAbility Overview](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-overview/document.md).
    -   ExtensionAbility: provides scenario-specific extension capabilities. For details, see [ExtensionAbility Component](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md). Currently, an atomic service does not support the **ExtensionAbility** component.

#### Adding an Ability in the Stage Model

## Adding a UIAbility to a Module

1.  Right-click a module and choose **New** > **Ability** from the shortcut menu.
2.  Set the ability name and other fields, and click **Finish**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/3YQoMy7-SGuav9gJoV5Yuw/en-us_image_0000002532750429.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D632E6A5FC33395DF585F69321007546EB57A91CE538089F61552377E5CA9BA8)
    

## Adding an ExtensionAbility to a Module

1.  Right-click a module, choose **New** > **Extension Ability** from the shortcut menu, and select a scenario. Adding an ExtensionAbility is only available for **Application** projects.
    
    -   If the type of the created module is entry or feature, the following extension abilities are supported:
        -   **EmbeddedUIExtensionAbility**: provides the capability of [embedded UIs across processes](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/embeddeduiextensionability/document.md).
        -   **Backup****Ability**: provides the capability of [app data backup and restoration](../../../../application-framework/core-file-kit/application-files/application-data-backup-and-restore/application-data-backup-and-restore-overview/document.md).
        -   **WorkScheduler**: provides [deferred task](../../../../application-framework/background-tasks-kit/deferred-task-arkts/document.md) capabilities.
        -   **RemoteNotificationAbility**: provides callbacks for obtaining scenario-specific message data and destroying the lifecycle.
        -   **Driver**: provides the [driver-related extension framework](../../../../system/hardware/driver-development-kit/basic-peripheral-driver-development/ui-free-driver-development/document.md). This type can be created only when the project contains only 2-in-1 devices.
    -   If the type of the created module is HAR or HSP, the following extension abilities are supported:
        -   **EmbeddedUIExtensionAbility**: provides the capability of [embedded UIs across processes](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/embeddeduiextensionability/document.md).
        -   **WorkScheduler**: provides [deferred task](../../../../application-framework/background-tasks-kit/deferred-task-arkts/document.md) capabilities.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/_tBHdiejS0W6kOMgKTNuXg/en-us_image_0000002501070404.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B897830FF7F839DB9EE6CD411781D475B3DBA09F77B56D1EA46726CDDEA359D)
    
2.  Set the ability name and click **Finish**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/EwBRVuWUSqeKWoNr6MyoEQ/en-us_image_0000002532670469.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2D1C80A9438BA25928A440DE779F0BDF9E34D33BBFEA654B104C48AC5D1BE52)
    

#### Adding an Ability in the FA Model

The method of adding an ability to a module is the same for ArkTS and JS projects. In this example, an ability is being added to a module for an ArkTS project.

## Creating a Particle Ability

1.  Right-click a module and choose **New** > **Ability** > an ability template from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/vUIv5Ac5R-aPxRWmXmKHXA/en-us_image_0000002532670477.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7C89476B108A73025A6FD55CD268ADE1EFAAF0E62E8DFF1596A7F848716C096)
    
2.  Set the basic information about the ability based on the ability template you have selected.
    
    -   **Ability name**: name of the ability, which consists of uppercase letters, lowercase letters, digits, and underscores (\_).
    -   **Language**: programming language of the ability.
    
3.  When you have finished, click **Finish**. You can then view and edit the new ability in the corresponding module of the project directory.

## Creating a Feature Ability

1.  Right-click a module and choose **New** > **Ability** > an ability template from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/ecXjJR0iQPW1ucZeO4VLOw/en-us_image_0000002501070398.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7780C41F13B24CB0AF7AE95434B6D5AF553AC102A149BA5825B04C3A92E61D94)
    
2.  Set the basic information about the ability based on the ability template you have selected.
    
    -   **Ability name**: name of the ability, which consists of uppercase letters, lowercase letters, digits, and underscores (\_).
    -   **Launcher ability**: whether the ability launcher icon is displayed on the home screen. A HAP can have multiple launcher icons to start different feature abilities.
    -   **Language**: programming language of the ability.
    
3.  When you have finished, click **Finish**. You can then view and edit the ability in the corresponding module of the project directory.
