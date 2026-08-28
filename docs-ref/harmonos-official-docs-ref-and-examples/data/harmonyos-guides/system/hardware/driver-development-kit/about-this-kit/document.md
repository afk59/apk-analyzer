# About This Kit

Empowered by the C-API solution, Driver Development Kit (DDK) provides easy-to-use, secure, and diversified ArkTs-API and C APIs to elevate your experience in developing peripheral drivers, which bring ultimate plug-and-play experience to users.

#### When to Use

With DDK, you can develop dedicated or extended peripheral drivers in an efficient and secure manner.

1.  Develop drivers of dedicated
    
    peripherals for bank counters, enterprise office, and medical detection, such as high-speed document scanners, ID card scanners, fingerprint scanners, and blood oxygen and blood glucose meters.
    
2.  Develop enhanced functions of non-standard peripherals,
    
    such as customizing handwriting pad shortcut keys, setting the pressure sensing/drawing area, setting extended enhancement capabilities, setting the mouse lighting effect, customizing mouse extended buttons, and setting DPI and X and Y axes.
    

#### Typical Use Cases

-   You can develop advanced peripheral functions to meet user requirements.
    
-   The extended driver framework supports lifecycle management of peripheral drivers and provides APIs for querying and binding peripheral devices.
    

#### Basic Concepts

-   Peripheral driver client: [basic UI-based driver](../basic-peripheral-driver-development/ui-based-driver-development/document.md), which is used to query and bind drivers, and customize the communication mode and data processing mode.
-   Peripheral driver: [basic UI-free driver](../basic-peripheral-driver-development/ui-free-driver-development/document.md), which is the dedicated peripheral driver or enhanced peripheral driver developed based on DDK.
-   External Device Manager: performs lifecycle management of peripheral devices and driver packages.
-   Bundle Manager Service (BMS): manages application installation, uninstallation, and data on the system.
-   Ability Manager Service (AMS): used to start and stop **DriverExtensionAbility**.
-   System Ability (SA): a system service that provides basic system capabilities for devices. For example, the driver extension SA is a system service that provides extended drivers for non-standard peripherals.
-   Non-standard peripheral: a peripheral that uses non-standard protocols (also called vendor-defined protocols) for communication.

#### Implementation Principles

The HDF extended driver framework provides unified APIs for you to leverage the DDK capabilities for user-mode peripheral driver development.

External Device Manager, the core service of user-mode peripheral management, performs lifecycle management of peripherals and peripheral drivers. In addition, standard ArkTS APIs are provided to query, bind, and unbind peripherals.

## Peripheral Driver Architecture

**Figure 1** Peripheral driver working mechanism

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/ZTjyquPlQD2TD6SYmMASrw/en-us_image_0000002537765106.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69E87A6A8210CCDA7B2111717D3DBEF9B1B441270A066E7681A4A404ED16DD0E)

## Operation Process

Figure 2 shows the process for matching a peripheral driver client with a peripheral driver when a peripheral is connected.

**Figure 2** Process for matching a peripheral driver client with a peripheral driver

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/PF7NNt6EQ2CSTRpatl5L6Q/en-us_image_0000002537925046.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD1835E10B35C9AEFEFAE0CA1D5FAB2EADF9D5E25062A2942139B6CC8D5F954C)

Figure 3 shows the process for binding the peripheral driver client with a peripheral driver.

**Figure 3** Process of binding the peripheral driver client with a peripheral driver

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/T-GhwDIoT7SeB2JmufJdYQ/en-us_image_0000002568684823.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A15E99F782C1668CEFCA37005DC2573C6BC726C7B2D4E3038A8B5E7F3148E99E)

#### Notes and Constraints

To call the ArkTs or C APIs provided by DDK, you need to apply for specified permissions.

The following table lists the required permissions.

| API Type | DDK Type | Permission |
| :-- | :-- | :-- |
| ArkTs-API | NA | ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER |
| C-API | USB DDK | ohos.permission.ACCESS\_DDK\_USB |
| C-API | HID DDK | ohos.permission.ACCESS\_DDK\_HID |
| C-API | USB Serial DDK | ohos.permission.ACCESS\_DDK\_USB\_SERIAL |
| C-API | SCSI Peripheral DDK | ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL |

#### Associated Modules

The following table lists the associated modules you may use during development of peripheral drivers.

| Name | Description |
| :-- | :-- |
| PerformanceAnalysisKit | Introduces {[hilog](../../../debugging-tools/performance-analysis-kit/command-line-tools/hilog/document.md)} for log printing. |
| BasicServicesKit | Introduces {[BusinessError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#businesserror)} to capture error information. |
| IPCKit | Introduces {[rpc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc)} to implement inter-process communication between the driver and the client. |
| AbilityKit | Introduces {[want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-application-want)} for lifecycle management. |

#### Driver Application Specifications

1.  Driver application definition

-   A driver application is a user-mode driver developed based on DDK for non-standard peripherals.
-   Since driver applications are based on **DriverExtensionAbility**, you need to override its lifecycle callback APIs.

1.  Driver application installation and uninstallation

-   Installation policy
    -   When a user installs a driver application, the system installs the application in all existing user spaces.
    -   When a user is created, the system installs the installed driver application in the respective user space.
-   Uninstallation policy: When a user uninstalls a driver application in any user space, the system uninstalls the driver application in all user spaces.

1.  DriverExtensionAbility-based lifecycle management

-   ExtensionAbility is a general term of scenario-based service extension abilities, such as user-mode peripheral drivers, service widgets, and input methods.
-   The lifecycle of each ExtensionAbility is managed by its SA. The SA calls **connectAbility** to start the ExtensionAbility and drive the execution of the defined service APIs. When the service is complete, the SA calls **disconnectAbility** to disconnect the ExtensionAbility. The AMS then determines whether to destroy the ExtensionAbility and its associated process based on whether the ExtensionAbility has any active SA connections. In the user-mode driver development scenario, the system SA that manages the DriverExtensionAbility lifecycle is the driver extension SA.

1.  API access security control in DriverExtensionAbility

-   The system supports scenario-based extension abilities built on ExtensionAbility. DriverExtensionAbility is a type of ability designed to support the development of user-mode drivers.
-   DriverExtensionAbility can use only the APIs in ([Driver Development Kit (DDK)](https://gitcode.com/openharmony/docs/tree/master/en/application-dev/reference/apis-driverdevelopment-kit)) to control access to non-standard peripherals and implement data communication.
-   Based on the security constraints and service scenarios in driver development, access to other ArkTS APIs is not allowed within DriverExtensionAbility, which is intended to prevent malicious behavior and data leakage.
-   Restricted access to ArkTS APIs in DriverExtensionAbility is implemented as follows:
    -   During the initialization and creation of DriverExtensionAbility, system modules are loaded based on the list of ArkTS APIs that can be accessed by DriverExtensionAbility. If a restricted ArkTS API is called in DriverExtensionAbility during the operation process, the API call fails because the corresponding system module is not loaded during the initialization and creation process.
-   For the list of restricted ArkTS APIs, see the DriverExtension configuration in [Restricted ArkTS APIs](https://gitcode.com/openharmony/ability_ability_runtime/blob/master/frameworks/native/ability/native/etc/extension_blocklist_config.json).
