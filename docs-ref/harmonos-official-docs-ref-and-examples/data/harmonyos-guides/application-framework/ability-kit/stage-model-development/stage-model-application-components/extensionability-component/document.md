# ExtensionAbility Component

[ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-extensionability) components are application components for specific scenarios. Each ExtensionAbility component corresponds to a specific real-world scenario. For example, [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) is used for widget scenarios, [InputMethodExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-ability) is used for input method scenarios, and [WorkSchedulerExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-workschedulerextensionability) is used for deferred task scenarios. You can use ExtensionAbility components of different types in your application to add new capabilities and interact more deeply with the system or other applications.

All types of ExtensionAbility components are defined by the system and are usually managed by the corresponding system services in a unified manner. For example, the [InputMethodExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-ability) component is managed by the input method management service. You cannot directly inherit from ExtensionAbility components. Instead, you can only implement or access the provided [ExtensionAbility types](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#extensionabilitytype).

#### ExtensionAbility Types

The table below lists the ExtensionAbility types defined in the system.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/iC11XDeuRiCmOymLDsXigQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5EA6496CF8CB286C52A242B7C0F14C14F2984881A97267393B8742E13D2B4F2)

-   The column **Allow Third-Party Apps to Implement** specifies whether third-party applications can inherit from this ExtensionAbility to implement their own service logic.
-   The column **Allow Independent ExtensionAbility Sandbox** specifies whether this ExtensionAbility runs in a sandbox separate from the main application's, preventing direct access between them.

| ExtensionAbility Type | Description | 
Allow Third-Party Apps

to Implement

 | 

Allow Independent

ExtensionAbility Sandbox

 |
| :-- | :-- | :-- | :-- |
| [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) | Provides extended capabilities related to [service widgets](../../../../form-kit/about-this-kit/document.md). | Yes | No |
| [WorkSchedulerExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-workschedulerextensionability) | Provides extended capabilities related to [deferred tasks](../../../../background-tasks-kit/deferred-task-arkts/document.md). | Yes | No |
| [InputMethodExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-ability) | Provides extended capabilities related to [input method applications](../../../../ime-kit/about-this-kit/document.md). | Yes | Yes |
| ServiceExtensionAbility | 

Provides extended capabilities related to background services.

Third-party applications can connect to this ExtensionAbility and communicate with it.

 | No | No |
| [AccessibilityExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-application-accessibilityextensionability) | Provides extended capabilities related to accessibility services, supporting access and operation of the foreground UI. | Yes | No |
| DataShareExtensionAbility | 

Provides extended capabilities related to data sharing, providing data reading and writing services.

Third-party applications can connect to this ExtensionAbility for data reading and writing.

 | No | No |
| [BackupExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-application-backupextensionability) | Provides extended capabilities for [data backup and restore](../../../../core-file-kit/application-files/application-data-backup-and-restore/application-data-backup-and-restore-overview/document.md). | Yes | No |
| [EnterpriseAdminExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterpriseadminextensionability) | 

Provides extended capabilities to handle management events during [enterprise management](../../../../../system/basic-functions/mdm-kit/enterpriseadminextensionability-development/document.md).

Example events are application installation events on the device and excessive incorrect lock screen password input events.

 | Yes | No |
| [PrintExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-printextensionability) | Provides extended capabilities for printing photos and documents in office scenarios. For details, see [PrintExtensionAbility](../../../../../system/basic-functions/basic-services-kit/print/printextensionability/document.md). | Yes | No |
| [ShareExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-shareextensionability) | Provides extended capabilities related to the share template service. | Yes | No |
| [DriverExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-driverextensionability) | Provides extended capabilities for [driver development](../../../../../system/hardware/driver-development-kit/basic-peripheral-driver-development/ui-free-driver-development/document.md). | Yes | No |
| [ActionExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-actionextensionability) | Provides extended capabilities for custom operation service templates. | Yes | No |
| [AdsServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-adsserviceextensionability) | Provides extended capabilities related to background custom ad services. | Yes | No |
| [EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability) | Provides extended capabilities for [UI embedding across processes](embeddeduiextensionability/document.md). | Yes | No |
| [FenceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-fenceextensionability) | Provides extended capabilities for the [Geofence](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/fenceextensionability). | Yes | No |
| [DistributedExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedextensionability) | Provides extended capabilities and lifecycle callbacks for distributed ability creation, destruction, and connection. | Yes | No |
| [AppServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability) | Provides extended capabilities for the application background service, which provides lifecycle callbacks for creating, destroying, connecting to, and disconnecting from the application background service. | Yes | No |
| [FaultLogExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability) | Provides extended capabilities for delayed fault notification. | Yes | No |
| [WebNativeMessagingExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability) | Provides extended capabilities for web plugins to interface with native applications. | Yes | No |
| [NotificationSubscriberExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationsubscriberextensionability) | Provides extended capabilities for sending notifications to third-party wearable devices. | Yes | No |
| [PhotoEditorExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-photoeditorextensionability) | Provides extended capabilities for applications to implement image editing functions. | Yes | No |
| [VpnExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-vpnextensionability) | Provides extended capabilities for third-party VPNs, including lifecycle callbacks such as creation and destruction. | Yes | No |
| [FormEditExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formeditextensionability) | Provides extended editing capabilities for widgets, allowing users to customize widget content, for example, editing a contact widget, modifying contacts displayed in a widget, and editing a weather widget. | Yes | No |
| [LiveFormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-liveformextensionability) | Provides extended animation capabilities for widgets, including overflow animations, rich information notifications, and shallow interactions, greatly enhancing user experience. | Yes | No |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/JVAetFewQVSRTxjyUPctUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A12063057DAD994091339E8274972F6FDEE2C37EF7EE3F8F158E819B865247A1)

Unless otherwise configured, all ExtensionAbility instances of the same type within an application (with the same bundle name) share a single process. Exceptions:

-   ServiceExtensionAbility (only for system applications), DataShareExtensionAbility (only for system applications), and all UIAbility instances run in the same independent process (main process).
-   The UIExtensionAbility and its child classes ExtensionAbility can specify a separate process via the [extensionProcessMode](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#extensionabilities) field in the **module.json5** file.

#### Accessing ExtensionAbility of the Specified Type

Each type of [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-extensionability) component is started by the corresponding system management service, rather than applications, so that its lifecycle is under system control. The caller of the ExtensionAbility component does not need to care about its lifecycle.

The following uses [InputMethodExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-ability) as an example. As shown in the figure below, when an application calls the InputMethodExtensionAbility component, the input method management service is called first. The input method management service starts the InputMethodExtensionAbility component, returns the component to the application, and starts to manage its lifecycle.

**Figure 1** Using the InputMethodExtensionAbility component

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/dMFiAV6mT0yEikz1iMlFyg/en-us_image_0000002537924288.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DE5E07821839C0FC7E5AD6149FEA10F83D56EF13D601ADC8067C91F17A7BA61)

#### Implementing ExtensionAbility of the Specified Type

The following uses [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) as an example. The widget framework provides the base class **FormExtensionAbility**. You can derive this base class to create your own class (for example, **MyFormExtensionAbility**) and implement the callbacks, such as **onCreate()** and [onUpdateForm()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability#formextensionabilityonupdateform), to provide specific widget features. For details, see [Service Widget](../../../../form-kit/about-this-kit/document.md).

You do not need to care when to add or delete a widget. The lifecycle of the FormExtensionAbility instance and the lifecycle of the [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-extensionability) process where the FormExtensionAbility instance is located are scheduled and managed by FormManagerService.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/HoDjCcjuTCCC5q9N67tVZw/en-us_image_0000002568684065.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E846CB38F389F46F01C3569F8364B0BA8D316D5438AE0A10BF0C362EAED3F165)

-   **[EmbeddedUIExtensionAbility](embeddeduiextensionability/document.md)**  
    
-   **[Using AppServiceExtensionAbility for Background Services](using-appserviceextensionability-for-background-services/document.md)**
