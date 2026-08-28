# @ohos.app.ability.wantConstant (Want Constants)

The wantConstant provides predefined enums and constants related to [Want](../ohos-app-ability-want-want/document.md) operations, such as the **flags** and **params** fields used during ability startup.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/bcsSelgSSzWXSqzvV571Zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20FDCF215B511EE670A0AF8C2034555C35048BE877926BB4C15FB252132DCDC7)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { wantConstant } from '@kit.AbilityKit';

#### Params

Enumerates the common system-defined keywords for the [Want.parameters](../ohos-app-ability-want-want/document.md#want) field. You can use these predefined keywords to set or retrieve additional parameter information carried in application transitions. For example, during the launch phase of a [UIAbility](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md), if the value of **ABILITY\_RECOVERY\_RESTART** obtained from the **want** field in the **onCreate** callback is **true**, the current UIAbility has restarted due to a fault.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Value | Description |
| :-- | :-- | :-- |
| ABILITY\_BACK\_TO\_OTHER\_MISSION\_STACK | ability.params.backToOtherMissionStack | 
Whether redirection back across mission stacks is supported.

This parameter controls the redirection-back logic across applications, altering the application transition behavior when the user presses the back button. For example, if UIAbility A is currently displayed and UIAbility B is launched with this parameter set to **true**, exiting UIAbility B will return to UIAbility A. If this parameter is not set, the system defaults to returning to the home screen. Note that this parameter is only supported for system applications and does not take effect for third-party applications.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ABILITY\_RECOVERY\_RESTART10+ | ohos.ability.params.abilityRecoveryRestart | 

Whether the ability has been restarted due to a fault.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CONTENT\_TITLE\_KEY10+ | ohos.extra.param.key.contentTitle | 

Title for sharing in an atomic service.

You can set the sharing title using this field in the [onShare](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onshare10) callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SHARE\_ABSTRACT\_KEY10+ | ohos.extra.param.key.shareAbstract | 

Content abstract for sharing in an atomic service.

You can set the sharing abstract using this field in the [onShare](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onshare10) callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SHARE\_URL\_KEY10+ | ohos.extra.param.key.shareUrl | 

URL link for sharing in an atomic service.

You can set the URL link using this field in the [onShare](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onshare10) callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SUPPORT\_CONTINUE\_PAGE\_STACK\_KEY10+ | ohos.extra.param.key.supportContinuePageStack | 

Whether to migrate the page stack information during cross-device migration. The default value is **true**, indicating that the page stack information is automatically migrated during cross-device migration.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SUPPORT\_CONTINUE\_SOURCE\_EXIT\_KEY10+ | ohos.extra.param.key.supportContinueSourceExit | 

Whether the source application exits during cross-device migration. The default value is\*\* true\*\*, indicating that the source application automatically exits during cross-device migration.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SHOW\_MODE\_KEY12+ | ohos.extra.param.key.showMode | 

Display mode of the [EmbeddableUIAbility](../../stage-model/ohos-app-ability-embeddableuiability-embeddable-uiability/document.md). The value is an enumerated value of [ShowMode](#showmode12).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PARAMS\_STREAM12+ | ability.params.stream | 

List of file URIs authorized to the target. The value must be an array of file URIs of the string type. For details about how to obtain the file URI, see [fileUri](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#fileurigeturifrompath). This field must be used in conjunction with file URI [read/write flag](#flags).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| APP\_CLONE\_INDEX\_KEY12+ | ohos.extra.param.key.appCloneIndex | 

Index of an application clone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CALLER\_REQUEST\_CODE12+ | ohos.extra.param.key.callerRequestCode | 

Request code

that uniquely identifies the caller of [startAbilityForResult](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startabilityforresult) or [openLink](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#openlink12). When either of the APIs is called to start an ability, the target ability returns the result to the caller based on the request code.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PAGE\_PATH12+ | ohos.param.atomicservice.pagePath | 

Page path for an atomic service.

If page redirection in an atomic service is implemented using [router](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing), you can use this parameter to specify the target page, for example, **library/ets/pages/menu**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ROUTER\_NAME12+ | ohos.param.atomicservice.routerName | 

Router name for page redirection in an atomic service.

If page redirection in an atomic service is implemented using [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation), you can use **ROUTER\_NAME**, **PAGE\_SOURCE\_FILE**, and **BUILD\_FUNCTION** together to specify the target page.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PAGE\_SOURCE\_FILE12+ | ohos.param.atomicservice.pageSourceFile | 

Source file for the page in an atomic service.

If page redirection in an atomic service is implemented using [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation), you can use **ROUTER\_NAME**, **PAGE\_SOURCE\_FILE**, and **BUILD\_FUNCTION** together to specify the target page.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BUILD\_FUNCTION12+ | ohos.param.atomicservice.buildFunction | 

Build function for the page in an atomic service.

If page redirection in an atomic service is implemented using [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation), you can use **ROUTER\_NAME**, **PAGE\_SOURCE\_FILE**, and **BUILD\_FUNCTION** together to specify the target page.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SUB\_PACKAGE\_NAME12+ | ohos.param.atomicservice.subpackageName | 

Sub-package name for an atomic service. Application packages can be developed with multiple modules, and each package may include one or multiple HAPs or HSPs. To enhance the launch speed, atomic services restrict the size of HAP and HSP files and optimize the startup process. This modular development approach is known as sub-packaging.

When you open an atomic service, you can use this parameter to activate the specific sub-package.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| APP\_INSTANCE\_KEY14+ | ohos.extra.param.key.appInstance | 

Specific application instance.

When you create [multiple instances](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/multiinstance) of an application, the system assigns a unique ID to each instance. During application transitions, you can use this parameter to specify which created application instance you want to transition to.

 |
| CREATE\_APP\_INSTANCE\_KEY14+ | ohos.extra.param.key.createAppInstance | 

Whether to create an application instance. The default value is **false**, indicating that no new application instance is created.

You can set this parameter to **true** to launch a new application instance. Note that the application to be launched must support multiple instances. For details, see [Creating an Application Multi-Instance](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/multiinstance).

 |
| CALLER\_APP\_CLONE\_INDEX14+ | ohos.param.callerAppCloneIndex | Clone index of the caller. |
| APP\_LAUNCH\_TRUSTLIST17+ | ohos.params.appLaunchTrustList | 

Filter list of applications for implicit launch.

Only applications in the list are matched during implicit launch. The value is an array of [AppIdentifiers](../../dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo) of the string type. The filter list supports a maximum of 50 applications. Passing an empty array will have no effect.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| LAUNCH\_REASON\_MESSAGE18+ | ohos.params.launchReasonMessage | 

Reason for launching the application.

The caller must be a system application and must request the ohos.permission.SET\_LAUNCH\_REASON\_MESSAGE permission. The following values are supported:

**ReasonMessage\_SystemShare**: The application is launched through system sharing.

**ReasonMessage\_DesktopShortcut**: The application is launched through a home screen shortcut.

**ReasonMessage\_Notification**: The application is launched through a notification.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| DESTINATION\_PLUGIN\_ABILITY19+ | ohos.params.pluginAbility | The target ability is a plugin ability. |
| ATOMIC\_SERVICE\_SHARE\_ROUTER20+ | ohos.params.atomicservice.shareRouter | 

Page stack information of the atomic service being launched. This parameter takes effect only when the caller is a UIAbilityContext and the callee is an atomic service.

For example, if an atomic service contains a home page and a second page, and you want to directly launch the second page, you can pass the page stack information of the second page through this field when launching the atomic service.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| ABILITY\_UNIFIED\_DATA\_KEY20+ | ohos.param.ability.udKey | 

Unique identifier for file sharing based on [UDMF](../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md). This field can only be set by system applications, but third-party applications can read it.

If the Want contains a URI authorization flag (for example, [FLAG\_AUTH\_READ\_URI\_PERMISSION](#flags) or [FLAG\_AUTH\_WRITE\_URI\_PERMISSION](#flags)) and the **PARAMS\_STREAM** field is also present, this field does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### Flags

Enumerates the common preset keywords of the [Want.flags](../ohos-app-ability-want-want/document.md#want) field. You can use these predefined keywords to set or retrieve additional flag information carried in application transitions.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Value | Description |
| :-- | :-- | :-- |
| FLAG\_AUTH\_READ\_URI\_PERMISSION | 0x00000001 | 
Temporarily grants the receiver read permission for the URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FLAG\_AUTH\_WRITE\_URI\_PERMISSION | 0x00000002 | 

Temporarily grants the receiver write permission for the URI.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FLAG\_AUTH\_PERSISTABLE\_URI\_PERMISSION12+ | 0x00000040 | The URI can be persisted by the receiver. It takes effect only on 2-in-1 devices and tablets. |
| FLAG\_INSTALL\_ON\_DEMAND | 0x00000800 | 

Enables on-demand installation when launching an atomic service.

\- If enabled, the system automatically installs the atomic service if it is not already installed before proceeding with the launch.

\- If disabled, the launch fails if the atomic service is not installed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FLAG\_START\_WITHOUT\_TIPS11+ | 0x40000000 | 

Disables the "No available applications" prompt during implicit application launches.

When [launching an application implicitly](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-startup-overview), a prompt saying "No available applications" will appear if no matching application is found. You can use this flag to prevent this prompt from appearing.

 |
| FLAG\_ABILITY\_ON\_COLLABORATE18+ | 0x00002000 | In multi-device collaboration scenario, the caller application must initiate a request through the DMS, with this flag included in the **Flags** field, in order to invoke the lifecycle callback [onCollaborate()](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#oncollaborate18) of the target application. |

#### ShowMode12+

Enumerates the display modes of an [EmbeddableUIAbility](../../stage-model/ohos-app-ability-embeddableuiability-embeddable-uiability/document.md) when it is launched.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW | 0 | An independent window is used to show the ability startup. |
| EMBEDDED\_FULL | 1 | An embedded full-screen is used to show the ability startup. |
