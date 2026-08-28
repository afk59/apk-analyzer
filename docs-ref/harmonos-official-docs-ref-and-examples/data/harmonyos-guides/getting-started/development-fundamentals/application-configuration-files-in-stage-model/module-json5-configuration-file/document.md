# module.json5 Configuration File

A module-level configuration file provides the basic configuration of the module, information about the **UIAbility** and **ExtensionAbility** components, and permissions required during application running for the compilation tool, OS, and AppGallery. Each module must contain a **module.json5** configuration file, which is stored in the **project or module name/src/main/module.json5** directory, for example, **entry/src/main/module.json5**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/jHpq4sbbT6i3Tkqyk14aBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED13AF65BB89C8AE2B2B3FA57465683AAFA31D092FF47C2A2C279CFB155C64EB)

Using the sample code in the actual project may cause a compilation failure. You need to configure the code as required. For example, if the resource file referenced by the **$** symbol does not exist in the project, you need to manually add the resource file or replace it with the actual one.

In the configuration file, fields can be repeated. The last field is used.

#### Configuration File Example

This topic gives an overview of the **module.json5** configuration file. To start with, let's go through an example of what this file contains.

{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module\_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": \[
      "tv",
      "tablet"
    \],
    "deliveryWithInstall": true,
    "pages": "$profile:main\_pages", // Resource configuration, pointing to the main\_pages.json configuration file defined in the profile.
    "appStartup": "$profile:app\_startup\_config",
    "metadata": \[
      {
        "name": "string",
        "value": "string",
        "resource": "$profile:distributionFilter\_config"
      },
      // ...
    \],
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility\_desc",
        "icon": "$media:layered\_image",
        "label": "$string:EntryAbility\_label",
        "startWindow": "$profile:start\_window",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          // ...
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              "ohos.want.action.home"
            \]
          }
        \],
        // ...
        "continueType": \[
          "continueType1"
        \],
        "continueBundleName": \[
          "com.example.myapplication1",
          "com.example.myapplication2"
        \],
      }
    \],
    "requestPermissions": \[
      {
        "name": "ohos.permission.ACCESS\_BLUETOOTH",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": \[
            "EntryAbility"
          \],
          "when": "inuse"
        }
      }
    \],
    "querySchemes": \[
      "app1Scheme",
      "app2Scheme"
    \],
    "routerMap": "$profile:router\_map",
    "appEnvironments": \[
      {
        "name": "name1",
        "value": "value1"
      }
    \],
    "fileContextMenu": "$profile:menu", // Resource configuration, which points to the menu.json configuration file defined in the profile.
    "crossAppSharedConfig": "$profile:shared\_config",
    // ...
  }
}

#### Tags in the Configuration File

As shown above, the **module.json5** file contains several tags.

**Table 1** Tags in the module.json5 file

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | 
Name of the module. This name must be unique in the entire application. The value must comply with the following rules:

\- Starts with a letter and consists of letters, digits, underscores (\_).

\- The maximum length is 128 bytes.

This name can be changed during application updates. However, if it is changed, directories related to the module must be migrated. For details, see [@ohos.file.fs (File Management)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs).

**NOTE**

The module name cannot exceed 31 characters when you create a module on DevEco Studio. If the length cannot meet your requirements, you can modify this tag in the configuration file.

 | String | No |
| type | 

Type of the module. The options are as follows:

\- **entry**: main module of the application.

\- **feature**: feature module of the application.

\- **har**: static shared module.

\- **shared**: dynamic shared module.

 | String | No |
| srcEntry | Code path of the AbilityStage component. The value is a string with a maximum of 127 bytes. For details, see [AbilityStage Component Container](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/abilitystage-component-manager/document.md). | String | Yes (initial value: left empty) |
| description | Description of the module, used to describe the module functions. The value is a string with a maximum of 255 bytes. It can be a resource reference. | String | Yes (initial value: left empty) |
| mainElement | 

Name of the entry **UIAbility** of the module. The value is a string with a maximum of 255 bytes.

**NOTE**

If multiple entry [UIAbilities](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-overview/document.md) are configured in the [abilities](#abilities) tag, the home screen icon, name, and entry are subject to the configuration of this tag. If this tag is left empty or no matching is found, the **UIAbility** **name** tag is sorted in ascending order based on the ASCII, and the first **UIAbility**'s icon, name, and entry are used.

 | String | Yes (initial value: left empty) |
| [deviceTypes](#devicetypes) | 

Types of the devices on which the module can run.

**NOTE**

When there are multiple modules, the configuration of each module can be different, but the required device type must be included to ensure the proper running.

 | String array | No |
| deliveryWithInstall | 

Whether the current module is installed during active installation, that is, whether the HAP or HSP corresponding to the module is installed together with the application.

\- **true**: The HAP or HSP of the module is installed together with the application.

\- **false**: The HAP or HSP of the module is not installed together with the application. They are installed through [on-demand feature distribution](../../../../application-services/appgallery-kit/on-demand-feature-distribution/on-demand-feature-distribution-arkts/document.md).

 | Boolean | 

No

This tag is mandatory when the current module is a HAP or an HSP.

 |
| installationFree | 

Whether the module supports the installation-free feature.

\- **true**: The module supports the installation-free feature and meets installation-free constraints.

\- **false**: The module does not support the installation-free feature.

 | Boolean | 

Yes

This tag is automatically generated during compilation and build. Manual configuration does not take effect.

**NOTE**

If [bundleType](../app-json5-configuration-file/document.md#tags-in-the-configuration-file) is set to **atomicService**, this tag is automatically set to **true**; otherwise, this tag is automatically set to **false**.

 |
| virtualMachine | Type of the target virtual machine (VM) where the module can run. It is used for cloud distribution, such as distribution by the application market and distribution center. If the target VM type is ArkTS engine, the value is **ark**+version number. | String | 

Yes

This tag is automatically generated during compilation and build. Manual configuration does not take effect.

 |
| [pages](#pages) | Profile that represents information about each page in the module. The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| [metadata](#metadata) | Custom metadata of the module. You can configure [distributionFilter](#distributionfilter) and [shortcuts](#shortcuts) by referencing resources. The setting is effective only for the current module, **UIAbility**, and **ExtensionAbility**. | Object array | Yes (initial value: left empty) |
| [abilities](#abilities) | **UIAbility** configuration of the module. The setting is effective only for the current **UIAbility**. | Object array | Yes (initial value: left empty) |
| [extensionAbilities](#extensionabilities) | **ExtensionAbility** configuration of the module. The setting is effective only for the current **ExtensionAbility**. | Object array | Yes (initial value: left empty) |
| [requestPermissions](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file) | A set of permissions that the application needs to request from the system for running correctly. | Object array | Yes (initial value: left empty) |
| [testRunner](#testrunner) | Test runner of the module. For details, see the [test](../../../../system/debugging-tools/debugging-commands/ability-assistant/document.md#test) command. | Object | Yes (initial value: left empty) |
| [atomicService](#atomicservice) | Atomic service configuration. | Object | Yes (initial value: left empty) |
| [dependencies](#dependencies) | List of shared libraries on which the module depends during running. | Object array | 

Yes (initial value: left empty)

This tag is automatically generated during compilation and build. Manual configuration does not take effect.

 |
| targetModuleName | Target module name. The value is a string with a maximum of 128 bytes. The module that has this tag set provides the overlay feature. This tag is applicable only to HSPs. | String | Yes (initial value: left empty) |
| targetPriority | Priority of the module. The value ranges from 1 to 100. This tag can be configured only after the **targetModuleName** tag is configured. This tag is applicable only to HSPs. | Integer | Yes (initial value: **1**) |
| [proxyData](#proxydata) | List of data proxies provided by the module. | Object array | Yes (initial value: left empty) |
| isolationMode | 

Multi-process configuration of the module. The options are as follows:

\- **nonisolationFirst**: The module preferentially runs in a non-isolated process.

\- **isolationFirst**: The module preferentially runs in an isolated process.

\- **isolationOnly**: The module runs only in an isolated process.

\- **nonisolationOnly**: The module runs only in a non-isolated process.

**NOTE**

1\. The current module can serve as an isolated process on 2-in-1 devices and tablets.

2\. This tag takes effect only for HAPs.

 | String | Yes (initial value: **nonisolationFirst**) |
| generateBuildHash | 

Whether the hash value of the HAP or HSP is generated by the packing tool. If the value is set to **true**, the hash value (if any) is used to determine whether the application needs to be updated when the system is updated in OTA mode but the **versionCode** value of the application remains unchanged.

This tag takes effect only when **generateBuildHash** in the [app.json5](../app-json5-configuration-file/document.md) file is set to **false**.

**NOTE**

This tag takes effect only for pre-installed applications.

 | Boolean | Yes (initial value: **false**) |
| compressNativeLibs | 

During HAP packaging, whether libraries are packaged to HAP after being compressed.

\- **true**: Libraries are stored in the HAP file after being compressed.

\- **false**: Libraries are stored without being compressed.

 | Boolean | Yes (initial value: **false**) |
| extractNativeLibs | 

During application installation, whether libraries are decompressed to the application installation directory. If both **compressNativeLibs** and **extractNativeLibs** are set to **false**, the application is installed without decompressing libraries. In other scenarios, the application is installed with libraries decompressed.

**NOTE**

This tag is supported since API version 20.

 | Boolean | Yes (initial value: **true**) |
| libIsolation | 

Whether to save the .so files of the current HAP to a separate folder. This is intended to avoid .so file conflicts between HAPs.

\- **true**: The .so files of the current HAP are stored in a separate folder (named after the module) in the **libs** directory.

\- **false**: The .so files of the current HAP are directly stored in the **libs** directory.

 | Boolean | Yes (initial value: **false**) |
| [fileContextMenu](#filecontextmenu) | 

Context menu of the current HAP. It is a profile resource. The value is a string with a maximum of 255 bytes.

**NOTE**

This tag takes effect only on PCs/2-in-1 devices.

It can be configured only in entry modules.

 | String | Yes (initial value: left empty) |
| querySchemes | 

URL schemes that the current application can query for redirection. This tag is only available for the entry modules. The value is a string with a maximum of 128 bytes.

**NOTE**

Since API version 21, a maximum of 200 URL schemes can be configured. In API version 20 and earlier versions, a maximum of 50 URL schemes can be configured.

 | String array | Yes (initial value: left empty) |
| [routerMap](#routermap) | Path of the routing table for the current module. The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| [appEnvironments](#appenvironments) | Application environments for the current module. This tag is only available for the entry and feature modules. | Object array | Yes (initial value: left empty) |
| appStartup | 

Configuration path of the current [AppStartup](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/appstartup/document.md). This tag can be configured only in the entry module.

Since API version 18, this tag can be configured in HSPs and HARs.

Since API version 20, this tag can be configured in feature modules.

 | String | Yes (initial value: left empty) |
| [hnpPackages](#hnppackages) | Native software package information of the current application. This tag is only available for the entry modules. | Object array | Yes (initial value: left empty) |
| [systemTheme](#systemtheme) | 

System theme that is being used. This tag is only available for the entry modules. The value is a string with a maximum of 255 bytes.

**NOTE**

This tag is supported since API version 20.

 | String | Yes (initial value: left empty) |
| abilitySrcEntryDelegator | 

Name of the **UIAbility** to which the current module redirects. It is used together with the **abilityStageSrcEntryDelegator** tag to specify the target object for redirection.

**NOTE**

1\. This tag is supported since API version 17.

2\. This tag does not take effect when the **UIAbility** is started through the [startAbilityByCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilitybycall) API.

3\. Configuration in the HAR and redirection to the **UIAbility** of the HAR are not supported.

 | String | Yes (initial value: left empty) |
| abilityStageSrcEntryDelegator | 

Name of the target module corresponding to the **UIAbility** that the current module redirects to (different from the current module name). It is used together with the **abilitySrcEntryDelegator** tag to specify the target object for redirection.

**NOTE**

1\. This tag is supported since API version 17.

2\. This tag does not take effect when the **UIAbility** is started through the [startAbilityByCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilitybycall) API.

3\. Configuration in the HAR and redirection to the **UIAbility** of the HAR are not supported.

 | String | Yes (initial value: left empty) |
| crossAppSharedConfig | 

Name of the configuration file for inter-application sharing. The value is a string with a maximum of 255 bytes. It is used to release configurations for other applications to read. The configurations take effect when the application is installed and become invalid when the application is uninstalled. For details, see [Sharing Configurations Between Applications (ArkTS)](../../../../application-framework/arkdata/cross-application-data-sharing/one-to-many-data-sharing/sharing-configurations-between-applications-arkts/document.md#configuring-the-publisher).

**NOTE**

This tag is supported since API version 20.

 | String | Yes (initial value: left empty) |
| formWidgetModule | 

In [standalone widget package](../../../../application-framework/form-kit/arkts-widget-development-recommended/creating-an-arkts-widget/document.md#method-2-creating-a-standalone-package), this tag needs to be configured for the application package to associate with the widget package. The value is the module name of the widget package, corresponding to the **name** tag in the **module.json5** file of the widget package. For details, see [FormExtensionAbility Configuration](../../../../application-framework/form-kit/arkts-widget-development-recommended/configuring-arkts-widget-configuration-files/document.md#formextensionability-configuration).

**NOTE**

1\. This tag is supported since API version 20.

2\. This tag takes effect only in the application package of a standalone widget package. The **formExtensionModule** tag must be configured for the corresponding widget package module.

 | String | Yes (initial value: left empty) |
| formExtensionModule | 

In [standalone widget package](../../../../application-framework/form-kit/arkts-widget-development-recommended/creating-an-arkts-widget/document.md#method-2-creating-a-standalone-package), this tag needs to be configured for the widget package to associate with the application package. The value is the module name of the application package, corresponding to the **name** tag in the **module.json5** file of the application package. For details, see [Standalone Widget Package Configuration](../../../../application-framework/form-kit/arkts-widget-development-recommended/configuring-arkts-widget-configuration-files/document.md#standalone-widget-package-configuration).

**NOTE**

1\. This tag is supported since API version 20.

2\. This tag takes effect only in the widget package of a standalone widget package. The **formWidgetModule** tag must be configured for the corresponding application package module.

 | String | Yes (initial value: left empty) |
| [requiredDeviceFeatures](#requireddevicefeatures) | 

Specific device features required for running the current module. AGC can distribute the application to devices that support the features based on the configuration. **NOTE**

1\. This tag is supported since API version 19.

2\. This tag is not supported for plugin applications.

 | Object | Yes (initial value: left empty) |

#### deviceTypes

**Table 2** deviceTypes

| Device Type | Enumerated Value | Description |
| :-- | :-- | :-- |
| Mobile phone | phone | \- |
| Tablet | tablet | \- |
| PCs/2-in-1 Devices | 2in1 | PC whose productivity is fully leveraged through interaction modes including multi-window, multitasking, and keyboard-mouse operations. In the HarmonyOS topics, "2-in-1" indicates PC/2-in-1 device. |
| Smart screen | tv | \- |
| Smart watch | wearable | A watch with rich system capabilities and phone call features. |
| Telematics device | car | \- |
| Default device | default | A default device on which applications can be built but not released. Change the device type to phone. |

Example of the **deviceTypes** structure:

{
  "module": {
    "name": "myHapName",
    "type": "feature",
    "deviceTypes": \[
      "tv",
      "tablet"
    \],
    // ...
  }
}

#### pages

The **pages** tag is a profile that represents information about specified pages.

{
  "module": {
    // ...
    "pages": "$profile:main\_pages", // Resource configuration, pointing to the main\_pages.json configuration file defined in the profile.
    // ...
  }
}

Define the **main\_pages.json** file under **resources/base/profile** in the development view. The file name (**main\_pages** in this example) can be customized, but must be consistent with the information specified by the **pages** tag. The file lists the page information of the current application, including the route information and the window-related configuration.

**Table 3** pages

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| src | Route information about all pages in the module, including the page path and page name. The page path is relative to the **src/main/ets** directory of the current module. The value is a string array, each element of which represents a page. | String array | No |
| window | Window-related configuration. | Object | Yes (initial value: left empty) |

**Table 4** window

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| designWidth | Baseline width for page design. The size of an element is scaled by the actual device width. | Number | Yes (initial value: **720px**) |
| autoDesignWidth | Whether to automatically calculate the baseline width for page design. If it is set to **true**, the **designWidth** attribute becomes invalid. The baseline width is calculated based on the device width and screen density. If it is set to **false**, the baseline width uses the value of **designWidth**. | Boolean | Yes (initial value: **false**) |

{
  "src": \[
    "pages/Index"
  \],
  "window": {
    "designWidth": 720,
    "autoDesignWidth": false
  }
}

#### metadata

The **metadata** tag represents the custom metadata of the HAP. The tag value is an array and contains three subtags: **name**, **value**, and **resource**.

**Table 5** metadata

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | Name of the data item. The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| value | Value of the data item. The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| resource | Custom data, which is a resource index. The value is a string with a maximum of 255 bytes. For example, **$profile:shortcuts\_config** indicates that the data points to the **/resources/base/profile/shortcuts\_config.json** configuration file. | String | Yes (initial value: left empty) |

{
  "module": {
    // ...
    "metadata": \[
      // ...
      {
        "name": "pageConfig",
        "value": "main page config of application",
        "resource": "$profile:main\_pages" // Resource configuration, pointing to the main\_pages.json configuration file defined in the profile.
      }
    \],
    // ...
  }
}

#### abilities

The **abilities** tag represents the **UIAbility** configuration of the module, which is valid only for the current **UIAbility** component.

**Table 6** abilities

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | Name of the **UIAbility**, which must be unique in the entire application. The value is a string with a maximum of 127 bytes. It must start with a letter and can contain letters, digits, underscores (\_), and periods (.). | String | No |
| srcEntry | Code path of the **UIAbility**. The value is a string with a maximum of 127 bytes. | String | No |
| [launchType](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-launch-type/document.md) | 
Launch type of the **UIAbility**. The options are as follows:

\- **multiton**: A **UIAbility** instance is created each time the **UIAbility** is started.

\- **singleton**: A **UIAbility** instance is created only when the **UIAbility** is started for the first time.

\- **specified**: You can determine whether to create a **UIAbility** instance when the application is running.

\- **standard**: original name of **multiton**. The effect is the same as that multiton mode.

 | String | Yes (initial value: **"singleton"**) |
| description | Description of the **UIAbility** component, used to describe the component functions. The value is a string with a maximum of 255 bytes. It is advised to use a resource index to support multiple languages. | String | Yes (initial value: left empty) |
| icon | [Icon](../../typical-scenarios-development/configuring-an-application-icon-and-label/document.md) of the **UIAbility**. The value is the index of the icon resource file. | String | Yes (initial value: left empty) |
| label | [Name](../../typical-scenarios-development/configuring-an-application-icon-and-label/document.md) of the **UIAbility** displayed to users. The value is an index of a string with a maximum of 255 bytes to support multiple languages. | String | Yes (initial value: left empty) |
| permissions | 

Permissions required for another application to access the **UIAbility** component. When other applications access the **UIAbility**, they need to apply for the corresponding permissions.

Each array element is a permission name with a maximum of 255 bytes. For details about the value, see [Application Permissions](../../../../system/security/application-access-control/application-permission-management/application-permissions/document.md).

 | String array | Yes (initial value: left empty) |
| [metadata](#metadata) | Metadata information of the **UIAbility**. For details about the typical use scenarios, see [metadata](../../../../application-framework/arkui/window-manager/window-metadata-configuration/document.md#metadata). | Object array | Yes (initial value: left empty) |
| exported | 

Whether the **UIAbility** component can be started by other applications.

\- **true**: The **UIAbility** component can be started by other applications. (It is recommended that this tag be set to **true** for the entry **UIAbility**.)

\- **false**: The **UIAbility** component can be started only by the same application or an application with the ohos.permission.START\_INVISIBLE\_ABILITY permission (only system applications can request this permission).

For example, if this attribute is set to **false**, the **UIAbility** component can be started through the application icon, shortcut, or push notification on the home screen which has the permission. However, it cannot be started by the Ability Assistant, which does not have this permission.

 | Boolean | Yes (initial value: **false**) |
| continuable | 

Whether the **UIAbility** can be continued on another device.

\- **true**: The **UIAbility** can be continued on another device.

\- **false**: The **UIAbility** cannot be continued on another device.

 | Boolean | Yes (initial value: **false**) |
| [skills](#skills) | 

A set of [wants](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/want-overview/document.md) that can be received by the **UIAbility**.

Configuration rules:

\- For HAPs of the entry type, you can configure multiple **skills** tags with the entry capability for an application. (A **skills** tag with the entry capability is the one that has **ohos.want.action.home** and **entity.system.home** configured.)

\- For HAPs of the feature type, you can configure the **skills** tag with the entry capability for an application, but not for a service.

 | Object array | Yes (initial value: left empty) |
| backgroundModes | 

Continuous tasks of the **UIAbility**.

For details about the continuous task types, see [Continuous Task (ArkTS)](../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).

 | String array | Yes (initial value: left empty) |
| [startWindow](#startwindow) | 

Profile resource of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes. If this tag is set, the **startWindowIcon** and **startWindowBackground** tags do not take effect.

**NOTE**

Starting from API version 19, this field can be used to configure enhanced starting windows.

 | String | Yes (initial value: left empty) |
| startWindowIcon | Index to the icon file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes. | String | No |
| startWindowBackground | 

Index to the background color resource file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes.

Example: **$color:red**.

 | String | No |
| removeMissionAfterTerminate | 

Whether to remove the relevant mission from the mission list after the **UIAbility** is destroyed.

\- **true**: Remove the relevant mission from the mission list after the **UIAbility** is destroyed.

\- **false**: Do not remove the relevant mission from the task mission list after the **UIAbility** is destroyed.

**NOTE**

This attribute is invalid in freeform window mode on 2-in-1 devices and tablets, and tasks are removed by default.

 | Boolean | Yes (initial value: **false**) |
| orientation | 

Startup direction of the **UIAbility** component. The enum and startup direction resource index can be configured.

The enum values are as follows:

\- **unspecified**: automatically determined by the system.

\- **landscape**: landscape mode.

\- **portrait**: portrait mode.

\- **follow\_recent**: rotation mode following the background window.

\- **landscape\_inverted**: inverted landscape mode.

\- **portrait\_inverted**: inverted portrait mode.

\- **auto\_rotation**: determined by the sensor.

\- **auto\_rotation\_landscape**: determined by the sensor in the horizontal direction, including landscape and inverted landscape modes.

\- **auto\_rotation\_portrait**: determined by the sensor in the vertical direction, including portrait and inverted portrait modes.

\- **auto\_rotation\_restricted**: determined by the sensor when the sensor switch is enabled.

\- **auto\_rotation\_landscape\_restricted**: determined by the sensor in the horizontal direction, including landscape and inverted landscape modes, when the sensor switch is enabled.

\- **auto\_rotation\_portrait\_restricted**: determined by the sensor in the vertical direction, including portrait and inverted portrait modes, when the sensor switch is enabled.

\- **locked**: auto-rotation disabled.

\- **auto\_rotation\_unspecified**: auto-rotation controlled by the switch and determined by the system.

\- **follow\_desktop**: following the orientation of the home screen.

To configure the startup direction resource index, the value should be a string with a maximum of 255 bytes, for example, **$string:orientation**.

**NOTE**

\- The startup direction resource index is supported since API version 14.

 | String | Yes (initial value: **"unspecified"**) |
| supportWindowMode | 

Window mode supported by the **UIAbility**. The options are as follows:

\- **fullscreen**: full-screen mode.

\- **split**: split-screen mode.

\- **floating**: floating window mode.

When **fullscreen** and **split** are both configured for a [freeform window](../../../../application-framework/arkui/window-manager/window-development-terminology/document.md#freeform-window), the window will be started in floating window mode if the value of [targetAPIVersion](../app-json5-configuration-file/document.md#tags-in-the-configuration-file) is less than 15, and in full-screen mode if the value is greater than or equal to 15.

In addition, you can configure the window mode through **metadata**. For details about the configuration rules and priorities, see [metadata](#metadata).

 | String array | 

Yes (initial value:

**\["fullscreen", "split", "floating"\]**)

 |
| maxWindowRatio | Maximum aspect ratio supported by the **UIAbility** component. The minimum value is **0**. | Number | Yes (initial value: maximum aspect ratio supported by the platform) |
| minWindowRatio | Minimum aspect ratio supported by the **UIAbility** component. The minimum value is **0**. | Number | Yes (initial value: minimum aspect ratio supported by the platform) |
| maxWindowWidth | 

Maximum window width supported by the **UIAbility**, in vp.

The value cannot be less than the value of **minWindowWidth** or greater than the maximum window width allowed by the platform. For details about the window size, see [Constraints](../../../../application-framework/arkui/window-manager/window-overview/document.md#constraints).

 | Number | Yes (initial value: maximum window width supported by the platform) |
| minWindowWidth | 

Minimum window width supported by the **UIAbility**, in vp.

The value cannot be less than the minimum window width allowed by the platform or greater than the value of **maxWindowWidth**. For details about the window size, see [Constraints](../../../../application-framework/arkui/window-manager/window-overview/document.md#constraints).

 | Number | Yes (initial value: minimum window width supported by the platform) |
| maxWindowHeight | 

Maximum window height supported by the **UIAbility**, in vp.

The value cannot be less than the value of **minWindowHeight** or greater than the maximum window height allowed by the platform. For details about the window size, see [Constraints](../../../../application-framework/arkui/window-manager/window-overview/document.md#constraints).

 | Number | Yes (initial value: maximum window height supported by the platform) |
| minWindowHeight | 

Minimum window height supported by the **UIAbility**, in vp.

The value cannot be less than the minimum window height allowed by the platform or greater than the value of **maxWindowHeight**. For details about the window size, see [Constraints](../../../../application-framework/arkui/window-manager/window-overview/document.md#constraints).

 | Number | Yes (initial value: minimum window height supported by the platform) |
| excludeFromMissions | 

Whether the **UIAbility** component is displayed in Recents.

\- **true**: displayed in Recents.

\- **false**: not displayed in Recents.

**NOTE**

Configurations of third-party applications do not take effect; the current configurations are only valid for system applications. To make system application configurations take effect, you need to apply for the application privilege. Privilege application is not open to third-party applications.

 | Boolean | Yes (initial value: **false**) |
| recoverable | 

Whether the application can be recovered to its previous state in case of faults.

\- **true**: The application can be recovered to its previous state in case of faults.

\- **false**: The application cannot be recovered to its previous state in case of faults.

 | Boolean | Yes (initial value: **false**) |
| isolationProcess | 

Whether the component can run in an isolated process.

\- **true**: The component can run in an isolated process.

\- **false**: The component cannot run in an isolated process.

**NOTE**

The **UIAbility** can serve as an isolated process on 2-in-1 devices and tablets.

 | Boolean | Yes (initial value: **false**) |
| excludeFromDock | 

Whether the **UIAbility** can be hidden from the dock.

\- **true**: The **UIAbility** can be hidden from the dock.

\- **false**: The **UIAbility** cannot be hidden from the dock.

**NOTE**

The configuration of this tag does not take effect.

 | Boolean | Yes (initial value: **false**) |
| preferMultiWindowOrientation | 

Multi-window orientation of the **UIAbility**.

\- **default**: default value. Do not set this parameter to the default value. You are advised to set this parameter for other applications.

\- **portrait**: portrait. This option is recommended for games in portrait mode.

\- **landscape**: landscape. This option is recommended for games in landscape mode. With this option, the floating window and upper and lower split screens are supported in landscape mode.

\- **landscape\_auto**: automatically landscape. This option is recommended for video applications. It must be used together with the **enableLandScapeMultiWindow/disableLandScapeMultiWindow** API.

 | String | Yes (initial value: **default**) |
| continueType | Continuation type of the **UIAbility**. | String array | Yes (initial value: name of the **UIAbility**) |
| continueBundleName | 

List of other applications that support cross-device migration.

**NOTE**

This parameter cannot be set to the application bundle name. It is used only for migration with different bundle names.

This tag is supported since API version 13.

 | String array | Yes (initial value: left empty) |
| process | 

Name of the process where the component runs. For details, see "Statically specified process" in [Process Model (Stage Model)](../../../../application-framework/ability-kit/stage-model-development/process-model/document.md#other-process-types).

**NOTE**

1\. This tag takes effect only on [PCs/2-in-1 devices](#devicetypes) and [tablets](#devicetypes).

2\. The **UIAbility** component and the **ExtensionAbility** component whose type is **embeddedUI** run in the same process when their tags are the same.

3\. This tag is supported since API version 14.

 | String | Yes (initial value: left empty) |

Example of the **abilities** structure:

{
  // ...
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "launchType": "singleton",
        "description": "$string:description\_main\_ability",
        "icon": "$media:layered\_image",
        "label": "$string:EntryAbility\_label",
        "permissions": \[\],
        "metadata": \[\],
        "exported": true,
        "continuable": true,
        "skills": \[
          {
            "actions": \[
              "ohos.want.action.home"
            \],
            "entities": \[
              "entity.system.home"
            \],
            "uris": \[\]
          }
        \],
        "backgroundModes": \[
          "dataTransfer"
        \],
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:red",
        "removeMissionAfterTerminate": true,
        "orientation": "$string:orientation",
        "supportWindowMode": \[
          "fullscreen",
          "split",
          "floating"
        \],
        "maxWindowRatio": 3.5,
        "minWindowRatio": 0.5,
        "maxWindowWidth": 2560,
        "minWindowWidth": 1400,
        "maxWindowHeight": 300,
        "minWindowHeight": 200,
        "excludeFromMissions": false,
        "preferMultiWindowOrientation": "default",
        "isolationProcess": false,
        "continueType": \[
          "continueType1",
          "continueType2"
        \],
        "continueBundleName": \[
          "com.example.myapplication1",
          "com.example.myapplication2"
        \],
        "process": ":processTag"
      }
    \],
    // ...
}

#### skills

The **skills** tag represents the feature set of [wants](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/want-overview/document.md) that can be received by the **UIAbility** or **ExtensionAbility** component.

For example, when downloading a PDF file in a browser, you can configure the **skills** tag to open the specified PDF file. For details, see [Using startAbility to Start a File Application](../../../../application-framework/ability-kit/stage-model-development/inter-application-redirection/starting-an-application-of-the-specified-type/using-startability-to-start-a-file-application/document.md).

**Table 7** skills

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| actions | 
Actions of wants that can be received, which can be predefined or customized.

You are advised not to configure multiple **actions** for a **skill**. Otherwise, the expected scenario may not be matched. For details, see [Common action and entities Values](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/common-action-and-entities-values-not-recommended/document.md).

 | String array | Yes (initial value: left empty) |
| entities | 

Entities of wants that can be received.

You are advised not to configure multiple **entities** for a **skill**. Otherwise, the expected scenario may not be matched. For details, see [Common action and entities Values](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/common-action-and-entities-values-not-recommended/document.md).

 | String array | Yes (initial value: left empty) |
| uris | URIs that match the wants. | Object array | Yes (initial value: left empty) |
| permissions | 

Permissions required for another application to access the **UIAbility** or **ExtensionAbility** component.

Each array element is a permission name with a maximum of 255 bytes. For details about the value, see [Application Permissions](../../../../system/security/application-access-control/application-permission-management/application-permissions/document.md).

 | String array | Yes (initial value: left empty) |
| domainVerify | 

Whether to enable [domain name verification](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section4452103365213).

\- **true**: Domain name verification is enabled.

\- **false**: Domain name verification is disabled.

 | Boolean | Yes (initial value: **false**) |

**Table 8** uris

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/tzfyYhDjSKmJJci6BlRoog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62ACA2E136935AE84ED50A54558476E2341A29619B8EC546E25BD3904614C551)

The following tags of the string type cannot be configured using resource indexes (**$string**).

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| scheme | 
Scheme of the URI, such as HTTP, HTTPS, file, and FTP.

**NOTE**

This tag is case-insensitive when it is used for implicit Want matching since API version 18.

 | String | Yes when only **type** is set in **uris** (initial value: left empty) |
| host | 

Host address of the URI. This tag is valid only when **scheme** is set. Common methods:

\- domain name, for example, **example.com**.

\- IP address, for example, **10.10.10.1**.

**NOTE**

This tag is case-insensitive when it is used for implicit Want matching since API version 18.

 | String | Yes (initial value: left empty) |
| port | Port number of the URI. For example, the default HTTP port number is 80, the default HTTPS port number is 443, and the default FTP port number is 21. This tag takes effect only when both **scheme** and **host** are configured. | String | Yes (initial value: left empty) |
| path | pathStartWith | pathRegex | Path of the URI. **path**, **pathStartWith**, and **pathRegex** represent different matching modes between the paths in the URI and the want. Set any one of them as needed. **path** indicates full matching, **pathStartWith** indicates prefix matching, and **pathRegex** indicates regular expression matching. This tag takes effect only when both **scheme** and **host** are configured. | String | Yes (initial value: left empty) |
| type | Data type that matches the want. The value complies with the Multipurpose Internet Mail Extensions (MIME) and [UniformDataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-uniformtypedescriptor#uniformdatatype) specifications. This tag can be configured together with **scheme** or configured separately. | String | Yes (initial value: left empty) |
| utd | [Uniform data types](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-uniformtypedescriptor) that match the wants. This tag is applicable to scenarios such as sharing. | String | Yes (initial value: left empty) |
| maxFileSupported | Maximum number of files of a specified type that can be received or opened at a time. This tag is applicable to scenarios such as sharing and must be used together with **utd**. | Integer | Yes (initial value: **0**) |
| linkFeature | Feature type provided by the URI. It is used to implement redirection between applications. The value is a string with a maximum of 127 bytes. The number of **linkFeature** declared in a bundle cannot exceed 150. For details, see [Description of linkFeature](../../../../application-framework/ability-kit/stage-model-development/inter-application-redirection/starting-a-specified-application/application-link-description/document.md#description-of-linkfeature) | String | Yes (initial value: left empty) |

Example of the **skills** structure:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/S9liWOq6S5-g-yNwE3CQlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F4F3508C2586AF937D9A3F7A8D5776C42ABED5D29E04453B526CDCEF48BDAC0)

The following example is a common configuration. Some components and modules are different in actual configuration. For details, see the corresponding document.

{
  // ...
    "abilities": \[
      {
        // ...
        "skills": \[
          {
            "actions": \[
              "ohos.want.action.home"
            \],
            "entities": \[
              "entity.system.home"
            \],
            "uris": \[
              {
                "scheme":"http",
                "host":"example.com",
                "port":"80",
                "path":"path",
                "type": "text/\*",
                "linkFeature": "Login"
              }
            \],
            "permissions": \[\],
            "domainVerify": false
          },
          // ...
        \],
        // ...
    \],
    // ...
}

#### extensionAbilities

The **extensionAbilities** tag represents the configuration of **ExtensionAbilities**, which is valid only for the current **ExtensionAbility**.

**Table 9** extensionAbilities

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | Name of the **ExtensionAbility**. This name must be unique in the entire application. The value is a string with a maximum of 127 bytes. | String | No |
| srcEntry | Code path of the **ExtensionAbility**. The value is a string with a maximum of 127 bytes. | String | No |
| description | Description of the **ExtensionAbility** component, used to describe the component functions. The value is a string with a maximum of 255 bytes. It can be a resource index to support multiple languages. | String | Yes (initial value: left empty) |
| icon | Icon of the **ExtensionAbility**. The value is the index of the icon resource file. | String | Yes (initial value: left empty) |
| label | Name of the **ExtensionAbility** displayed to users. The value must be a resource index to support multiple languages. It contains a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| type | 
Type of the **ExtensionAbility**. The options are as follows:

\- **form**: **ExtensionAbility** of a widget.

\- **workScheduler**: **ExtensionAbility** of a deferred task.

\- **inputMethod**: **ExtensionAbility** of an input method.

\- **share**: [ShareExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-shareextensionability) for content sharing.

\- **service**: In scenarios where **service** components run in the background, application installation will fail via third-party configurations. You need to apply for the application privilege. Privilege application is not open to third-party applications.

\- **accessibility**: **ExtensionAbility** of an accessibility feature.

\- **fileAccess**: **ExtensionAbility** for public data access. It allows applications to provide files and folders for file management applications to display. This configuration takes effect only for system applications but not for third-party applications.

\- **dataShare**: **ExtensionAbility** for data sharing. Application installation will fail via third-party configurations. You need to apply for the application privilege. Privilege application is not open to third-party applications.

\- **staticSubscriber**: **ExtensionAbility** for static broadcast. This configuration takes effect only for system applications but not for third-party applications.

\- **fileShare**: **ExtensionAbility** for file sharing.

\- **vpn**: **ExtensionAbility** of the [VPN](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-vpnextensionability) capability.

\- **wallpaper**: **ExtensionAbility** of the wallpaper.

\- **backup**: **ExtensionAbility** for data backup.

\- **enterpriseAdmin**: **ExtensionAbility** for [enterprise device management](../../../../system/basic-functions/mdm-kit/enterpriseadminextensionability-development/document.md). An enterprise device management application must have such **ExtensionAbility**.

\- **window**: **ExtensionAbility** of a window. This type of **ExtensionAbility** creates a window during startup for which you can develop the GUI. The GUI developed by you will be combined into windows of other applications through the **UIExtensionComponent** control. This configuration takes effect only for system applications but not for third-party applications.

\- **thumbnail**: **ExtensionAbility** for obtaining file thumbnails. You can provide thumbnails for files of customized file types.

\- **preview**: **ExtensionAbility** for preview. This type of **ExtensionAbility** can parse the file and display it in a window. You can combine the window with other application windows.

\- **print**: **ExtensionAbility** for the print framework.

\- **push**: **ExtensionAbility** for the push service.

\- **driver**: **ExtensionAbility** for the driver framework. When an application configures an **ExtensionAbility** of the driver type, it is recognized as a driver application. Driver applications do not differentiate between users during installation, uninstall, and recovery. Moreover, when a new user account is created, the existing driver applications on the device are installed for that user. For example, when a sub-user is created, the driver applications already installed by the primary user is automatically installed for the sub-user. If a driver application is uninstalled for a sub-user, it is also removed for the primary user.

\- **remoteNotification**: **ExtensionAbility** for remote notifications.

\- **remoteLocation**: **ExtensionAbility** for remote location.

\- **voip**: **ExtensionAbility** for VoIP calls.

\- **action**: **ExtensionAbility** for custom service operations, which provides custom service operation templates based on UIExtension.

\- **adsService**: **ExtensionAbility** for the advertisement service, which provides the advertisement service framework. This configuration takes effect only for system applications but not for third-party applications.

\- **embeddedUI**: **ExtensionAbility** for embedded UI, which allows for UI embedding across processes.

\- **insightIntentUI**: **ExtensionAbility** that enables applications to be called by Celia intents so as to be displayed in windows.

\- **ads**: **ExtensionAbility** for the ad service, which is used with the AdComponent to display the ad page in other applications. This option is only available for device manufacturers.

\- **photoEditor**: **ExtensionAbility** for the image editing service, which provides an image editing service template based on UIExtension.

\- **appAccountAuthorization**: **ExtensionAbility** for application account authorization extension, which is used to process account authorization requests, for example, account login authorization.

\- **autoFill/password**: **ExtensionAbility** for automatically filling in usernames and passwords.

\- **hms/account**: **ExtensionAbility** for application account management.

\- **sysDialog/atomicServicePanel**: **ExtensionAbility** for building the atomic service panel. This ability is implemented based on **UIExtensionAbility**. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/userAuth**: **ExtensionAbility** for local user authentication. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/common**: **ExtensionAbility** for common pop-up windows. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/power**: **ExtensionAbility** for the restart pop-up window. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/print**: **ExtensionAbility** for the modal pop-up window. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/meetimeCall**: **ExtensionAbility** for MeeTime calls. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/meetimeContact**: **ExtensionAbility** for MeeTime contacts. This configuration takes effect only for system applications but not for third-party applications.

\- **sysDialog/meetimeMessage**: **ExtensionAbility** for MeeTime messages. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/meetimeContact**: **ExtensionAbility** for MeeTime contact lists. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/meetimeCallLog**: **ExtensionAbility** for MeeTime call records. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/share**: **ExtensionAbility** for system sharing. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/mediaControl**: **ExtensionAbility** for the casting component. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/photoPicker**: Third-party applications launch the gallery picker interface via the corresponding **UIExtensionType**. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/filePicker**: **ExtensionAbility** for the file download pop-up window. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/audioPicker**: **ExtensionAbility** for the audio management pop-up window. This configuration takes effect only for system applications but not for third-party applications.

\- **sysPicker/photoEditor**: **ExtensionAbility** for the image editing pop-up window. This configuration takes effect only for system applications but not for third-party applications.

\- **sys/commonUI**: **ExtensionAbility** for embedded display or pop-up windows that are closely related to service attributes. This configuration takes effect only for system applications but not for third-party applications.

\- **autoFill/smart**: **ExtensionAbility** for scenario-specific autofill services.

\- **uiService**: Pop-up service component that creates a window during startup and supports two-way communication. This configuration takes effect only for system applications but not for third-party applications.

\- **statusBarView**: ExtensionAbility for [Status Bar Extension Kit](../../../../system/basic-functions/desktop-extension-kit/about-this-kit/document.md).

\- **recentPhoto**: **ExtensionAbility** for recommended recent photos.

\- **fence**: **ExtensionAbility** for geofencing.

\- **callerInfoQuery**: **ExtensionAbility** for enterprise contacts.

\- **assetAcceleration**: **ExtensionAbility** for resource pre-download.

\- **formEdit**: **ExtensionAbility** for widget editing.

\- **distributed**: **ExtensionAbility** for distributed extension.

\- **liveForm**: [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-liveformextensionability) for interactive widgets. This tag is supported since API version 20.

\- **appService**: [AppServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability) for background services, which provides lifecycle callbacks to manage background services, including creation, destruction, connection, and disconnection. This tag is supported since API version 20.

\- **webNativeMessaging**: [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability) for web native message communication. This tag is supported since API version 21.

\- **faultLog**: [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability) for delayed fault notification. This tag is supported since API version 21.

\- **notificationSubscriber**: [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationsubscriberextensionability) for notification subscription. This tag is supported since API version 22.

\- **crypto**: [ExtensionAbility](../../../../system/security/universal-keystore-kit/external-key-management-extension/driver-hap-extensionability-adaptation-guide/cryptoextensionability-adaptation-development-guide/document.md) for external key management. This tag is supported since API version 22.

\- **selection**: **ExtensionAbility** for word selection extension. Starting from API version 20, this configuration takes effect only for system applications but not for third-party applications.

\- **awc/webpage**: **ExtensionAbility** for common web browsing.

\- **awc/newsfeed**: **ExtensionAbility** for news feed.

 | String | No |
| permissions | 

Permissions required for another application to access the **ExtensionAbility** component.

Each permission name is an array element, with a maximum of 255 bytes. For details about the value, see [Application Permissions](../../../../system/security/application-access-control/application-permission-management/application-permissions/document.md).

 | String array | Yes (initial value: left empty) |
| appIdentifierAllowList | 

List of applications that are allowed to start the **ExtensionAbility**.

Each **appIdentifier** is an array element. For details about **appIdentifier**, see [What is appIdentifier](../../faqs-about-application-packages/document.md#what-is-appidentifier).

**NOTE**

This tag is available only when the type of the **ExtensionAbility** is set to **appService**.

This tag is supported since API version 20.

 | String array | Yes (initial value: left empty) |
| readPermission | Permission required for reading data in the **ExtensionAbility**. The value is a string with a maximum of 255 bytes. This tag takes effect only when **type** of the preset **ExtensionAbility** of the system application is set to **dataShare**. The **dataShare** type is invalid for third-party applications. | String | Yes (initial value: left empty) |
| writePermission | Permission required for writing data to the **ExtensionAbility**. The value is a string with a maximum of 255 bytes. This tag takes effect only when **type** of the preset **ExtensionAbility** of the system application is set to **dataShare**. The **dataShare** type is invalid for third-party applications. | String | Yes (initial value: left empty) |
| uri | 

Data URI provided by the **ExtensionAbility**. The value is a string with a maximum of 255 bytes, in the reverse domain name notation.

**NOTE**

This tag is mandatory when the type of the **ExtensionAbility** is set to **dataShare**.

 | String | Yes (initial value: left empty) |
| skills | 

A set of [wants](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/want/want-overview/document.md) that can be received by the **ExtensionAbility**.

Configuration rule: In an entry package, you can configure multiple **skills** attributes with the entry capability. (A **skills** attribute with the entry capability is the one that has **ohos.want.action.home** and **entity.system.home** configured.) The label and icon of the first **ExtensionAbility** that has **skills** configured are used as the label and icon of the entire service/application.

**NOTE**

The feature package of a service does not support the **skills** tag with the entry capability.

The feature package of an application supports the **skills** tag with entry capability.

 | Array | Yes (initial value: left empty) |
| [metadata](#metadata) | 

Metadata of the **ExtensionAbility** component.

**NOTE**

When **type** is set to **form**, this tag cannot be left empty. In addition, an object value **ohos.extension.form** must exist. Its corresponding resource value cannot be left empty and is the level-2 resource reference of the service widgets.

 | Object array | Yes (initial value: left empty) |
| exported | 

Whether the **ExtensionAbility** can be called by other applications.

\- **true**: The **ExtensionAbility** can be called by other applications.

\- **false**: The **UIAbility** cannot be called by other applications, not even by Ability Assistant.

 | Boolean | Yes (initial value: **false**) |
| extensionProcessMode | 

Multi-process instance model of the **ExtensionAbility**. Currently, this tag is effective only for **UIExtensionAbilities** and **ExtensionAbilities** extended from **UIExtensionAbilities**.

\- **instance**: Each instance of the **ExtensionAbility** has a process.

\- **type**: All instances of the **ExtensionAbility** run in the same process, separated from other **ExtensionAbility** instances.

\- **bundle**: All instances of the **ExtensionAbility** run in the same process as instances of other **ExtensionAbilities** using the **bundle** model.

\- **runWithMainProcess**: The ExtensionAbility and the application main process share the same process. Only the ExtensionAbility for [Status Bar Extension Kit](../../../../system/basic-functions/desktop-extension-kit/about-this-kit/document.md) can be set to **runWithMainProcess**.

 | String | Yes (initial value: left empty) |
| dataGroupIds | Data group IDs of the **ExtensionAbility**. If the application where the current **ExtensionAbility** component is located also applies for a **dataGroupId** in the **groupIds** of the certificate applied by the AppGallery, the current **ExtensionAbility** component can share the directory generated by the **dataGroupId** with the application, therefore, the **dataGroupId** of the **ExtensionAbility** component takes effect only when it is configured in the **groupIds** tag in the signing certificate. This tag takes effect only when the **ExtensionAbility** component has an independent sandbox directory.For details, see [dataGroupId Application Process](../../../../application-framework/ime-kit/security-mode-of-the-input-method/document.md#section4219152220459). | String array | Yes (initial value: left empty) |
| process | 

Name of the process where the component runs. This tag can be configured only when **type** is set to **embeddedUI**. For details, see "Statically specified process" in [Process Model (Stage Model)](../../../../application-framework/ability-kit/stage-model-development/process-model/document.md#other-process-types).

**NOTE**

1\. This tag takes effect only on [PCs/2-in-1 devices](#devicetypes) and [tablets](#devicetypes).

2\. The **UIAbility** and **ExtensionAbility** components run in the same process when their tags are the same.

3\. This tag is supported since API version 14.

 | String | Yes (initial value: left empty) |
| isolationProcess | 

Whether the **ExtensionAbility** component can run in an isolated process.

\- **true**: The component can run in an isolated process.

\- **false**: The component cannot run in an isolated process.

**NOTE**

This tag takes effect only when **type** of **ExtensionAbility** is set to **sys/commonUI** (for system applications only).

This tag is supported since API version 20.

 | Boolean | Yes (initial value: **false**) |

Example of the **extensionAbilities** structure:

{
  // ...
    "extensionAbilities": \[
      {
        "name": "FormName",
        "srcEntry": "./ets/form/MyForm.ets",
        "icon": "$media:icon",
        "label" : "$string:extension\_name",
        "description": "$string:form\_description",
        "type": "form",
        "permissions": \["ohos.permission.ACCESS\_BLUETOOTH"\],
        "exported": true,
        "uri":"scheme://authority/path/query",
        "skills": \[{
          "actions": \[\],
          "entities": \[\],
          "uris": \[\],
          "permissions": \[\]
        }\],
        "metadata": \[
          {
            "name": "ohos.extension.form",
            "resource": "$profile:form\_config",
          }
        \],
        "extensionProcessMode": "instance",
        "dataGroupIds": \[
          "testGroupId1"
        \]
      }
    \],
    // ...
}

#### shortcuts

The **shortcuts** tag provides the shortcut information of an application. The value is an array and consists of four sub-attributes: **shortcutId**, **label**, **icon**, and **wants**.

The **shortcut** information is specified in [metadata](#metadata), where:

-   **name** indicates the name of the shortcut, identified by **ohos.ability.shortcuts**.
    
-   **resource** indicates where the resources of the shortcut are stored.
    

**Table 10** Shortcuts

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| shortcutId | ID of the shortcut. The value is a string with a maximum of 63 bytes. **This tag cannot be configured using the resource index ($string).** | String | No |
| label | Label of the shortcut, that is, the text description displayed for the shortcut. The value is a string with a maximum of 255 bytes. It can be descriptive content or a resource index. | String | Yes (initial value: left empty) |
| icon | 
Icon of the shortcut. The value is the index of the icon resource file.

**NOTE**

Icons are classified into single-layer icons and layered icons. A single-layer icon contains only one image, and a layered icon contains a foreground image and a background image. The following configurations are recommended:

1\. Foreground image: a transparent layer whose icon size is 450 × 450 px and resource size is 1024 × 1024 px.

2\. Background image: The size is 1024 × 1024 px.

 | String | Yes (initial value: left empty) |
| visible | 

Whether the shortcut is visible. The value **true** indicates that the shortcut is visible; **false** indicates the opposite.

**NOTE**

This tag is supported since API version 20.

 | Boolean | Yes (initial value: **true**) |
| [wants](#wants) | Wants to which the shortcut points. If the **startShortcut** API of **launcherBundleManager** is called, the first target component in the wants is started. As such, you are advised to configure only one element for **wants**. | Object | Yes (initial value: left empty) |

1.  Configure the **shortcuts\_config.json** file in **/resources/base/profile/**.
    
    {
      "shortcuts": \[
        {
          "shortcutId": "id\_test1",
          "label": "$string:shortcut",
          "icon": "$media:aa\_icon",
          "visible": true,
          "wants": \[
            {
              "bundleName": "com.ohos.hello",
              "moduleName": "entry",
              "abilityName": "EntryAbility",
              "parameters": {
                "testKey": "testValue"
              }
            }
          \]
        }
      \]
    }
    
2.  In the **abilities** tag of the **module.json5** file, configure the **metadata** tag for the **UIAbility** component to which a shortcut needs to be added so that the shortcut configuration file takes effect for the **UIAbility**.
    
    {
      "module": {
        // ...
        "abilities": \[
          {
            "name": "EntryAbility",
            "srcEntry": "./ets/entryability/EntryAbility.ets",
            // ...
            "skills": \[
              // ...
              {
                "entities": \[
                  "entity.system.home"
                \],
                "actions": \[
                  "ohos.want.action.home"
                \]
              }
            \],
            "metadata": \[
              {
                "name": "ohos.ability.shortcuts",
                "resource": "$profile:shortcuts\_config"
              }
            \],
            // ...
          }
        \],
        // ...
      }
    }
    

## wants

The **wants** tag provides wants information for a shortcut.

**Table 11** wants

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| bundleName | Target bundle name of the shortcut. | String | Yes |
| moduleName | Target module name of the shortcut. | String | Yes |
| abilityName | Target ability name of the shortcut. | String | Yes |
| parameters | Custom data when the shortcut is started. The data must be strings. A key can contain a maximum of 1024 characters. | Object | Yes |

Example of the **wants** tag:

{
  "wants": \[
    {
      "bundleName": "com.ohos.hello",
      "moduleName": "entry",
      "abilityName": "EntryAbility",
      "parameters": {
        "testKey": "testValue"
      }
    }
  \]
}

#### distributionFilter

The **distributionFilter** tag defines the rules for distributing HAP files based on different device specifications, so that precise matching can be performed when the application market distributes applications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/H1PanvHPRnecjZvbgKHhQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED7930BC1B630183C9225CCACC6564B6661FA3680261C05C04F3846656DA50D2)

This tag is supported since API version 10. For API version 9 and earlier, the **distroFilter** tag is used.

-   **Application scenario**: If a project has multiple entry-type modules and the values of **deviceType** configured for these modules overlap, you need to use this tag to distinguish the modules. In the following example, both entry-type modules support the tablet type, and therefore the **distributionFilter** tag is required.
    
    // Device types supported by entry1
    {
      "module": {
        "name": "entry1",
        "type": "entry",
        "deviceTypes": \[
          "tv",
          "tablet"
        \],
        // ...
    }
    
    // Device types supported by entry2
    {
      "module": {
        "name": "entry2",
        "type": "entry",
        "deviceTypes": \[
          "tv",
          "tablet"
        \],
        // ...
    }
    
-   **Configuration rule**: This tag consists of four attributes, including [screenShape](#screenshape), [screenWindow](#screenwindow), [screenDensity](#screendensity), and [countryCode](#countrycode). For details, see the following table.
    
    During distribution, a unique HAP is determined based on the mapping between **deviceTypes** and the preceding attributes.
    
    -   When configuring this tag, include at least one of the attributes.
    -   If any one or more attributes are set for one entry-type module, the same attributes must be set for all other entry-type modules.
    -   The **screenShape** and **screenWindow** attributes are available only for lite wearables.
-   **Configuration**: This tag must be configured in the **/resources/base/profile** directory and be referenced in the **resource** tag of **metadata**.
    

**Table 12** distributionFilter

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| [screenShape](#screenshape) | Supported screen shapes. | Object array | Yes (initial value: left empty) |
| [screenWindow](#screenwindow) | Supported application window resolutions. | Object array | Yes (initial value: left empty) |
| [screenDensity](#screendensity) | Pixel density of the screen, in dots per inch (DPI). | Object array | Yes (initial value: left empty) |
| [countryCode](#countrycode) | Code of the country or region to which the application is to be distributed. The value is subject to the ISO-3166-1 standard. Enumerated definitions of multiple countries and regions are supported. | Object array | Yes (initial value: left empty) |

## screenShape

**Table 13** screenShape

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| policy | 
Rule for the sub-attribute value.

\- **exclude**: Exclude the matches of the sub-attribute value.

\- **include**: Include the matches of the sub-attribute value.

 | String | No |
| value | Screen shapes. The value can be **circle**, **rect**, or both. For example, different HAPs can be provided for a smart watch with a circular face and that with a rectangular face. | String array | No |

## screenWindow

**Table 14** screenWindow

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| policy | 
Rule for the sub-attribute value. Currently, the value can only be **include**.

\- **include**: Include the matches of the sub-attribute value.

 | String | No |
| value | Screen width and height, in pixels. The value is an array of supported width and height pairs, each in the "width \* height" format, for example, **"454 \* 454"**. | String array | No |

## screenDensity

**Table 15** screenDensity

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| policy | 
Rule for the sub-attribute value.

\- **exclude**: Exclude the matches of the sub-attribute value.

\- **include**: Include the matches of the sub-attribute value.

 | String | No |
| value | 

Pixel density of the screen, in DPI. The options are as follows:

\- **sdpi**: small-scale DPI. This value is applicable to devices with a DPI range of (0, 120\].

\- **mdpi**: medium-scale DPI. This value is applicable to devices with a DPI range of (120, 160\].

\- **ldpi**: large-scale DPI. This value is applicable to devices with a DPI range of (160, 240\].

\- **xldpi**: extra-large-scale DPI. This value is applicable to devices with a DPI range of (240, 320\].

\- **xxldpi**: extra-extra-large-scale DPI. This value is applicable to devices with a DPI range of (320, 480\].

\- **xxxldpi**: extra-extra-extra-large-scale DPI. This value is applicable to devices with a DPI range of (480, 640\].

 | String array | No |

## countryCode

**Table 16** countryCode

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| policy | 
Rule for the sub-attribute value.

\- **exclude**: Exclude the matches of the sub-attribute value.

\- **include**: Include the matches of the sub-attribute value.

 | String | No |
| value | Code of the country or region to which the application is to be distributed. | String array | No |

Example:

1.  Configure the **distributionFilter\_config.json** file (this file name is customizable) in **resources/base/profile** under the development view.
    
    {
      "distributionFilter": {
        "screenShape": {
          "policy": "include",
          "value": \[
            "circle",
            "rect"
          \]
        },
        "screenWindow": {
          "policy": "include",
          "value": \[
            "454\*454",
            "466\*466"
          \]
        },
        "screenDensity": {
          "policy": "exclude",
          "value": \[
            "ldpi",
            "xldpi"
          \]
        },
        "countryCode": {
          "policy": "include",
          "value": \[
            "CN"
          \]
        }
      }
    }
    
2.  Configure **metadata** in the **module** tag in the **module.json5** file.
    

{
  "module": {
    // ...
    "metadata": \[
      {
        "name": "ohos.module.distribution",
        "resource": "$profile:distributionFilter\_config",
      }
    \],
    // ...
}

#### testRunner

The **testRunner** tag represents the supported test runner.

**Table 17** testRunner

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | Name of the test runner object. The value is a string with a maximum of 255 bytes. | String | No |
| srcPath | Code path of the test runner. The value is a string with a maximum of 255 bytes. | String | No |

Example of the **testRunner** structure:

{
  "module": {
    // ...
    "testRunner": {
      "name": "myTestRunnerName",
      "srcPath": "etc/test/TestRunner.ts"
    },
    // ...
  }
}

#### atomicService

The **atomicService** tag represents the atomic service configuration. It takes effect only when **bundleType** is set to **atomicService** in the **app.json5** file.

**Table 18** atomicService

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| preloads | List of modules to preload. | Object array | Yes (initial value: left empty) |
| resizeable | 
Whether an atomic service supports adaptive window. If this tag is set to **true**, the width and height of the window automatically adapt to the screen when the tablet is switched from landscape mode to portrait mode or the foldable screen is folded.

**NOTE**

1\. This tag is supported since API version 20.

2\. If the window has adapted to the tablet (landscape) and foldable screen (unfolded), you are advised to set this tag to **true**.

\- **true**: The atomic service supports adaptive window.

\- **false**: The atomic service does not support adaptive window.

 | Boolean | Yes (initial value: **false**) |

**Table 19** preloads

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| moduleName | Name of the module to be preloaded when the current module is loaded in the atomic service. The value must match an existing module other than the current one. It contains a maximum of 31 bytes. | String | No |

Example of the **atomicService** structure:

{
  "module": {
    // ...
    "atomicService": {
      "preloads":\[
        {
          "moduleName":"feature"
        }
      \],
      "resizeable": true
    },
    // ...
}

#### dependencies

The **dependencies** tag identifies the list of shared libraries that the module depends on when it is running.

**Table 20** dependencies

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| bundleName | Name of the shared bundle on which the current module depends. The value is a string of 7 to 128 bytes. | String | Yes (initial value: left empty) |
| moduleName | Module name of the shared bundle on which the current module depends. The value is a string with a maximum of 31 bytes. | String | No |
| versionCode | Version number of the shared bundle on which the current module depends. The value ranges from 0 to 2147483647. | Number | Yes (initial value: left empty) |

Example of the **dependencies** structure:

{
  "module": {
    // ...
    "dependencies": \[
      {
        "bundleName":"com.share.library",
        "moduleName": "library",
        "versionCode": 10001
      }
    \],
    // ...
  }
}

#### proxyData

The **proxyDatas** tag provides the list of data proxies provided by the module. It can be configured only for entry and feature modules.

**Table 21** proxyData

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| uri | URI of the data proxy. The URIs configured for different data proxies must be unique and must be in the datashareproxy://Current application bundle name/xxx format. The value is a string with a maximum of 255 bytes. | String | No |
| requiredReadPermission | Permission required for reading data from the data proxy. If it is not specified, other applications will not be able to use the data proxy. For non-system applications, the level of the set permission must be **system\_basic** or **system\_core**. For system applications, the permission level is not limited. For details about the permission levels, see [Application Permissions](../../../../system/security/application-access-control/application-permission-management/application-permissions/document.md). The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| requiredWritePermission | Permission required for writing data to the data proxy. If it is not specified, other applications will not be able to use the data proxy. For non-system applications, the level of the set permission must be **system\_basic** or **system\_core**. For system applications, the permission level is not limited. For details about the permission levels, see [Application Permissions](../../../../system/security/application-access-control/application-permission-management/application-permissions/document.md). The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
| [metadata](#metadata) | Metadata of the data proxy. Only the **name** and **resource** tags can be configured. | Object | Yes (initial value: left empty) |

Example of the **proxyData** structure:

{
  "module": {
    // ...
    "proxyData": \[
      {
        "uri":"datashareproxy://ohos.app.hap.myapplication/event/Meeting",
        "requiredReadPermission": "ohos.permission.SYSTEM\_FLOAT\_WINDOW",
        "requiredWritePermission": "ohos.permission.SYSTEM\_FLOAT\_WINDOW",
        "metadata": {
          "name": "datashare\_metadata",
          "resource": "$profile:datashare"
        }
      }
    \],
    // ...
  }
}

#### routerMap

The **routerMap** tag represents the path to the routing table for the module.

The **routerMap** configuration file provides the routing table information of the module. The value of the **routerMap** tag is an array.

**Table 22** routerMap

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | Name of the page to be redirected to. The value is a string with a maximum of 1023 bytes. | String | No |
| pageSourceFile | Path of the page in the module. The value is a string with a maximum of 255 bytes. | String | No |
| buildFunction | Function decorated by @Builder. The function describes the UI of the page. The value is a string with a maximum of 1023 bytes. | String | No |
| [data](#data) | Custom data of the string type. You can extend capabilities and obtain the content from the **data** field in **routerMap** of the [HapModuleInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo) object. This tag has been parsed by the system. Each piece of custom data cannot exceed 128 bytes. | Object | Yes (initial value: left empty) |
| [customData](#customdata) | Custom data of any type. You can extend capabilities and obtain the content from the **customData** field in **routerMap** of the [HapModuleInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo) object. You have to call the **JSON.parse** function to parse this tag. The total length of the value cannot exceed 4096 bytes. | Object | Yes (initial value: left empty) |

Example:

1.  Define a routing table configuration file under **resources/base/profile** in the development view. The file name can be customized, for example, **router\_map.json**.
    
    {
      "routerMap": \[
        {
          "name": "DynamicPage1",
          "pageSourceFile": "src/main/ets/pages/pageOne.ets",
          "buildFunction": "myFunction",
          "customData": {
            "stringKey": "data1",
            "numberKey": 123,
            "booleanKey": true,
            "objectKey": {
              "name": "test"
            },
            "arrayKey": \[
              {
                "id": 123
              }
            \]
          }
        },
        {
          "name": "DynamicPage2",
          "pageSourceFile": "src/main/ets/pages/pageTwo.ets",
          "buildFunction": "myBuilder",
          "data": {
            "key1": "data1",
            "key2": "data2"
          }
        }
      \]
    }
    
2.  Define the **routerMap** tag under **module** of the **module.json5** file, set it to point to the defined routing table configuration file, for example, set it to **"routerMap": "$profile:router\_map"**.
    

## data

The **data** tag is used to configure custom string data in the routing table.

Example of the **data** structure:

{
  "routerMap": \[
    {
      "name": "DynamicPage",
      "pageSourceFile": "src/main/ets/pages/pageOne.ets",
      "buildFunction": "myBuilder",
      "data": {
        "key1": "data1",
        "key2": "data2"
      }
    }
  \]
}

## customData

The **data** tag represents custom data in the routing table.

The **customData** tag is used to configure custom data of any type.

Example of the **customData** structure:

{
  "routerMap": \[
    {
      "name": "DynamicPage",
      "pageSourceFile": "src/main/ets/pages/pageOne.ets",
      "buildFunction": "myBuilder",
      "customData": {
        "stringKey": "data1",
        "numberKey": 123,
        "booleanKey": true,
        "objectKey": {
          "name": "test"
        },
        "arrayKey": \[
          {
            "id": 123
          }
        \]
      }
    }
  \]
}

#### appEnvironments

The **appEnvironments** tag represents the application environment variables configured for the module.

**Table 23** appEnvironments

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| name | Name of the environment variable. The value is a string with a maximum of 4,096 bytes. | String | Yes (initial value: left empty) |
| value | Value of the environment variable. The value is a string with a maximum of 4,096 bytes. | String | Yes (initial value: left empty) |

Example of the **appEnvironments** structure:

{
  "module": {
    // ...
    "appEnvironments": \[
      {
        "name": "name1",
        "value": "value1"
      }
    \],
    // ...
  }
}

#### hnpPackages

The **hnpPackages** tag provides information about the native software package contained in the application.

**Table 24** hnpPackages

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| package | Name of the native software package. | String | No |
| type | 
Type of the native software package. The options are as follows:

\- **public**: public type.

\- **private**: private type.

 | String | No |

Example of the **hnpPackages** structure:

{
  "module": {
    // ...
    "hnpPackages": \[
      {
        "package": "hnpsample.hnp",
        "type": "public"
      }
    \],
    // ...
  },
}

#### fileContextMenu

The **fileContextMenu** tag provides configuration options for the context menu (displayed upon right-clicking) of the current HAP. It is a profile that contains the context menu configuration registered by the application. This tag takes effect only on PCs/2-in-1 devices and can be configured only in entry modules.

Example of the **fileContextMenu** structure:

{
  "module": {
    // ...
    "fileContextMenu": "$profile:menu", // Resource configuration, which points to the menu.json configuration file defined in the profile.
    // ...
  }
}

Define the **menu.json** file under **resources/base/profile** in the development view. The file name (**menu.json** in this example) can be customized, but must be consistent with the information specified by the **fileContextMenu** tag. The file describes the items and response behavior of the context menu registered by the application.

The root node of the file is **fileContextMenu**, which is an object array and indicates the number of context menus registered by the current module. (The number must not exceed 5 per module and per application. If the number exceeds 5, only five random menus are parsed.)

**Table 25** fileContextMenu

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| abilityName | Name of the ability to be started for the context menu. | String | No |
| menuItem | 
Information displayed on the context menu. Naming rules:

Rule 1: \[Action\] + \[Application name\]. Example: **Open with {application}**, or **Open with {application} ({plugin})**.

Rule 2: \[Action\] + \[Purpose\]. Example: **Compress to {file name}**, **Compress to {path}**, or **Convert to {format} with {application}**.

 | Resource ID | No |
| menuHandler | Context menu handler. An ability can be used to create multiple shortcut menus. Each tag corresponds to one shortcut menu item, so you can customize the value of this tag to ensure that each tag is unique in the ability. When a user right-clicks a context menu to start an application, this tag is passed to the application as a parameter. | String | No |
| menuContext | Context required for displaying the context menu. Multiple contexts are supported. | Object array | No |

**Table 26** menuContext

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| menuKind | 
Condition in which the context menu is displayed. The options are as follows:

\- **0**: blank area

\- **1**: file

\- **2**: folder

\- **3**: file and folder

 | Number | No |
| menuRule | 

Operations that can trigger context menu. The options are as follows:

\- **single**: Single file or folder is selected.

\- **multi**: Multiple files or folders are selected.

\- **both**: Both.

 | String | No (This tag is read when **menuKind** is set to **1** or **2**.) |
| fileSupportType | 

Supported types of files. The context menu is displayed when the selected file list contains files of these types.

If the value of this tag is set to **\["\*"\]**, the **fileNotSupportType** tag is read.

When the value is left empty, no processing is performed.

 | String array | No (This tag is read when **menuKind** is set to **1**.) |
| fileNotSupportType | 

Types of files not supported. The context menu is not displayed when the selected file list contains files of these types.

This tag is read only when **menuKind** is set to **1** and **fileSupportType** is set to **\["\*"\]**.

 | String array | Yes (initial value: left empty) |

Example of the **menu.json** file in the **resources/base/profile** directory:

{
  "fileContextMenu": \[
    {
      "abilityName": "EntryAbility",
      "menuItem": "$string:module\_desc",
      "menuHandler": "openCompress",
      "menuContext": \[
        {
          "menuKind": 0
        },
        {
          "menuKind": 1,
          "menuRule": "both",
          "fileSupportType": \[
            ".rar",
            ".zip"
          \],
          "fileNotSupportType": \[
            ""
          \]
        },
        {
          "menuKind": 2,
          "menuRule": "single"
        },
        {
          "menuKind": 3
        }
      \]
    }
  \]
}

**Response Behavior**

After a context menu is registered, the **More** option of the menu, when clicked, displays a sublist of menu items specified in **menuItem**. After you click any of the items, the file manager starts the third-party application using **startAbility** by default. In addition to the bundle name and ability name of the third-party application, the following tags are also passed in **parameter** of **want**:

**Table 27** parameter field in want

| Name | Value | Data Type |
| :-- | :-- | :-- |
| menuHandler | Value of **menuHandler** in the registration configuration file. | String |
| uriList | URIs for redirection when the user right-clicks files. If the context menu is displayed by right-clicking a blank area, the value is null. If the context menu is displayed by right-clicking a single file, the array length is 1. If the context menu is displayed by right-clicking multiple files, the URIs of all files should be passed in. | String array |

#### startWindow

This tag points to a profile resource and is used to define the configuration file **start\_window.json** of the **UIAbility** startup page in **resources/base/profile**. If this tag is set, the **startWindowIcon** and **startWindowBackground** tags do not take effect.

**NOTE**

Starting from API version 19, this field can be used to configure enhanced starting windows.

**Table 28** startWindow

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| startWindowType | 
Visibility type of the **UIAbility** startup page.

This tag is supported only on 2-in-1 devices or tablets in freeform mode.

The options are as follows:

\- **REQUIRED\_SHOW**: The starting window is displayed. This setting is not affected by the setting of the **hideStartWindow** tag in [StartOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions#startoptions).

\- **REQUIRED\_HIDE**: The starting window is hidden. This setting is not affected by the setting of the **hideStartWindow** tag in [StartOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions#startoptions).

\- **OPTIONAL\_SHOW**: The starting window is displayed by default, but it can be hidden if the **hideStartWindow** tag in [StartOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-startoptions#startoptions) is set to hide it.

\- The default value is **REQUIRED\_SHOW**.

This tag is supported since API version 20.

 | String | Yes (initial value: **REQUIRED\_SHOW**) |
| startWindowAppIcon | 

Index to the icon file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes.

This field is supported since API version 19.

 | String | Yes (initial value: left empty) |
| startWindowIllustration | 

Index to the illustration file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes.

This field is supported since API version 19.

 | String | Yes (initial value: left empty) |
| startWindowBrandingImage | 

Index to the brand logo file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes.

This field is supported since API version 19.

 | String | Yes (initial value: left empty) |
| startWindowBackgroundColor | 

Index to the background color resource file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes.

This field is supported since API version 19.

 | String | No |
| startWindowBackgroundImage | 

Index to the background image file of the **UIAbility** startup page. The value is a string with a maximum of 255 bytes.

This field is supported since API version 19.

 | String | Yes (initial value: left empty) |
| startWindowBackgroundImageFit | 

Background image adaptation mode of the **UIAbility** startup page. The options are as follows:

\- **Contain**: Proportionally scaled based on the aspect ratio, the image is fully contained within the display area.

\- **Cover**: Proportionally scaled based on the aspect ratio, both width and height of the image are greater than or equal to that of the display area.

\- **Auto**: adaptive display.

\- **Fill**: The image fills the display area without any aspect ratio scaling applied.

\- **ScaleDown**: The image is displayed in accordance with its aspect ratio, either scaled down or kept unchanged.

\- **None**: The image is displayed in its original size.

This field is supported since API version 19.

 | String | Yes (initial value: **Cover**) |
| startWindowColorModeType | 

Dark and light mode of the starting window of the current UIAbility. It applies only for launching within the same process.

The options are as follows:

\- FOLLOW\_SYSTEM: The dark and light color mode of the starting window follows the system's color scheme.

\- FOLLOW\_APPLICATION: The dark and light mode of the starting window follows the application's color scheme.

\- The default value is FOLLOW\_SYSTEM.

This field is supported since API version 20.

 | String | Yes (initial value: FOLLOW\_SYSTEM) |

Example of the **start\_window.json** file in the **resources/base/profile** directory:

{
  "startWindowType": "REQUIRED\_SHOW",
  "startWindowColorModeType": "FOLLOW\_SYSTEM",
  "startWindowAppIcon": "$media:start\_window\_app\_icon",
  "startWindowIllustration": "$media:start\_window\_illustration",
  "startWindowBrandingImage": "$media:start\_window\_branding\_image",
  "startWindowBackgroundColor": "$color:start\_window\_back\_ground\_color",
  "startWindowBackgroundImage": "$media:start\_window\_back\_ground\_image",
  "startWindowBackgroundImageFit": "Cover"
}

#### systemTheme

The **systemTheme** tag points to a profile resource, which is used to specify the system theme configuration file used by the current application. This tag is supported since API version 20.

Example:

{
  "module": {
    // ...
    "systemTheme": "$profile:theme\_config", // Resource configuration, which points to the theme\_config.json configuration file defined in the profile.
  }
}

Define the **theme\_config.json** configuration file in **resources/base/profile**. The file's base name can be customized but must be either **theme\_config** or a name that starts with **theme\_config** (e.g. **theme\_config\_1**). The configuration file specifies the system theme used by the current application, corresponding to the information specified by the **systemTheme** tag.

**Table 29** theme\_config.json

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| systemTheme | 
System theme used by the current application. The value is an enum of the system theme name. The options are as follows:

\- **$ohos:theme:ohos\_theme**: default system theme

 | String | No |

Example of the **theme\_config.json** file in the **resources/base/profile** directory:

{
  "systemTheme": "$ohos:theme:ohos\_theme"
}

#### requiredDeviceFeatures

**Table 30** requiredDeviceFeatures

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| phone | 
Device features required by smartphones. The options are as follows:

\- **large\_screen**: [large screen in landscape mode](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-screen-layout#section6493354468)

 | String array | Yes (initial value: left empty) |

Example:

{
  "module": {
    "requiredDeviceFeatures": {
      "phone": \[
        "large\_screen"
      \]
    },
  }
}
