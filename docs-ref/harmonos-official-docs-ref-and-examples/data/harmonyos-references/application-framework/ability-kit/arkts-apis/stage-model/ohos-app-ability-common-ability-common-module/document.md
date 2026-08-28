# @ohos.app.ability.common (Ability Common Module)

The module provides pure type definitions for common capabilities within Ability Kit, including various context objects, callback interfaces, and data structures. It exports type declarations only and does not include any implementation logic or executable code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/mxXoopA4Q4WqMxtOEnTurg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D52AAFBE8D5885210CC30F4D77FADB789CED2BD8CC3C3452981EA182FED55905)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### UIAbilityContext

type UIAbilityContext = \_UIAbilityContext.default

Defines the context environment for the [UIAbility](../ohos-app-ability-uiability-ability-with-ui/document.md). It inherits from Context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_UIAbilityContext.default](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Default context of the UIAbility. |

#### AbilityStageContext

type AbilityStageContext = \_AbilityStageContext.default

Defines the context environment for the [AbilityStage](../ohos-app-ability-abilitystage-abilitystage-component-manager/document.md). It inherits from Context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_AbilityStageContext.default](../../dependent-elements-and-definitions/application/abilitystagecontext/document.md) | Default context of the AbilityStage. |

#### ApplicationContext

type ApplicationContext = \_ApplicationContext.default

Defines the application context. It inherits from Context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_ApplicationContext.default](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md) | Application context. |

#### BaseContext

type BaseContext = \_BaseContext.default

Defines the parent class of all context types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_BaseContext.default](../../dependent-elements-and-definitions/application/basecontext/document.md) | Parent class of all context types. |

#### Context

type Context = \_Context.default

Defines the context base class for the [stage model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#stage-model).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_Context.default](../../dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Base class of the context in the stage model. |

#### ExtensionContext

type ExtensionContext = \_ExtensionContext.default

Defines the context environment for the [ExtensionAbility](../ohos-app-ability-extensionability-extensionability-base-class/document.md). It inherits from Context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_ExtensionContext.default](../../dependent-elements-and-definitions/application/extensioncontext/document.md) | Default context of the ExtensionAbility. |

#### FormExtensionContext

type FormExtensionContext = \_FormExtensionContext.default

Defines the context environment for the [FormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md). It inherits from [ExtensionContext](../../dependent-elements-and-definitions/application/extensioncontext/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_FormExtensionContext.default](../../../../form-kit/arkts-apis/application/formextensioncontext/document.md) | Default context of the FormExtensionAbility. |

#### VpnExtensionContext11+

type VpnExtensionContext = \_VpnExtensionContext.default

Defines the context environment for the [VpnExtensionAbility](../../../../../system/network/network-kit/arkts-apis/ohos-app-ability-vpnextensionability-enhanced-vpn-management/document.md). It inherits from Context.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_VpnExtensionContext.default](../../../../../system/network/network-kit/arkts-apis/vpnextensioncontext/document.md) | Default context of the VpnExtensionAbility. |

#### EventHub

type EventHub = \_EventHub.default

Defines EventHub, which is an event communication mechanism based on the publish-subscribe pattern.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_EventHub.default](../../dependent-elements-and-definitions/application/eventhub/document.md) | Event communication mechanism based on the publish-subscribe pattern. |

#### PacMap

type PacMap = \_PacMap

Defines the container of basic data types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_PacMap](../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md#pacmap) | Container of basic data types. |

#### AbilityResult

type AbilityResult = \_AbilityResult

Defines the result code and data returned when a started ability is terminated.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_AbilityResult](../../dependent-elements-and-definitions/ability/abilityresult/document.md) | Result code and data returned when a started ability is terminated. |

#### AbilityStartCallback11+

type AbilityStartCallback = \_AbilityStartCallback

Defines the callback invoked to return the UIExtensionAbility startup result. It is usually used as an input parameter in [UIAbilityContext.startAbilityByType](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startabilitybytype11) or [UIExtensionContext.startAbilityByType](../ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#startabilitybytype11).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_AbilityStartCallback](../../dependent-elements-and-definitions/application/abilitystartcallback/document.md) | Callback invoked to return the UIExtensionAbility startup result. |

#### ConnectOptions

type ConnectOptions = \_ConnectOptions

Defines the connection options. It is used as an input parameter for connection to a background service, to receive the connection status with the background service.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_ConnectOptions](../../dependent-elements-and-definitions/ability/connectoptions/document.md) | Input parameter used to receive the connection status with the background service. |

#### UIExtensionContext10+

type UIExtensionContext = \_UIExtensionContext.default

Defines the context environment for the [UIExtensionAbility](../ohos-app-ability-uiextensionability-extensionability-with-ui/document.md). It inherits from Context.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_UIExtensionContext.default](../../dependent-elements-and-definitions/application/uiextensioncontext/document.md) | Default context of the UIExtensionAbility. |

#### EmbeddableUIAbilityContext12+

type EmbeddableUIAbilityContext = \_EmbeddableUIAbilityContext.default

Defines the context environment for the [EmbeddableUIAbility](../ohos-app-ability-embeddableuiability-embeddable-uiability/document.md). It inherits from Context.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_EmbeddableUIAbilityContext.default](../../dependent-elements-and-definitions/application/embeddableuiabilitycontext/document.md) | Default context of the EmbeddableUIAbility. |

#### PhotoEditorExtensionContext12+

type PhotoEditorExtensionContext = \_PhotoEditorExtensionContext.default

Defines the context environment for the [PhotoEditorExtensionAbility](../ohos-app-ability-photoeditorextensionability-extensionability-for-image-editing/document.md). It inherits from Context.

**System capability**: SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_PhotoEditorExtensionContext.default](../../dependent-elements-and-definitions/application/photoeditorextensioncontext/document.md) | Default context of the PhotoEditorExtensionAbility. |

#### UIServiceProxy14+

type UIServiceProxy = \_UIServiceProxy.default

Defines the capability for data communication with the UIServiceExtensionAbility. UIServiceExtensionAbility is a special type of ExtensionAbility provided by the system and is used to provide extended capabilities related to floating windows.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_UIServiceProxy.default](../../dependent-elements-and-definitions/application/uiserviceproxy/document.md) | Capability for data communication with the UIServiceExtensionAbility. |

#### UIServiceExtensionConnectCallback14+

type UIServiceExtensionConnectCallback = \_UIServiceExtensionConnectCallback.default

Defines the connection callback. It is used as an input parameter for connection to a UIServiceExtensionAbility, to provide the callback for the connection.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_UIServiceExtensionConnectCallback.default](../../dependent-elements-and-definitions/application/uiserviceextensionconnectcallback/document.md) | Callback for connection to a UIServiceExtensionAbility. |

#### AppServiceExtensionContext20+

type AppServiceExtensionContext = \_AppServiceExtensionContext.default

Defines the context environment for the [AppServiceExtensionAbility](../ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md). It inherits from Context.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_AppServiceExtensionContext.default](../../dependent-elements-and-definitions/application/appserviceextensioncontext-extensionability-context-for-application-background-s/document.md) | Default context of the AppServiceExtensionAbility. |

#### FormEditExtensionContext22+

type FormEditExtensionContext = \_FormEditExtensionContext.default

Defines the context environment for the [FormEditExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formeditextensionability-formeditextensionability/document.md). It inherits from [UIExtensionContext](../../dependent-elements-and-definitions/application/uiextensioncontext/document.md).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Ability.Form

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_FormEditExtensionContext.default](../../../../form-kit/arkts-apis/application/formeditextensioncontext/document.md) | Default context of the FormEditExtensionAbility. |

#### LiveFormExtensionContext22+

type LiveFormExtensionContext = \_LiveFormExtensionContext.default

Defines the context environment for the [LiveFormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-liveformextensionability-liveformextensionability/document.md). It inherits from [ExtensionContext](../../dependent-elements-and-definitions/application/extensioncontext/document.md).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Ability.Form

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [\_LiveFormExtensionContext.default](../../../../form-kit/arkts-apis/application/liveformextensioncontext/document.md) | Default context of the LiveFormExtensionAbility. |

**Example**

import { common } from '@kit.AbilityKit';

let uiAbilityContext: common.UIAbilityContext;
let abilityStageContext: common.AbilityStageContext;
let applicationContext: common.ApplicationContext;
let baseContext: common.BaseContext;
let context: common.Context;
let uiExtensionContext: common.UIExtensionContext;
let extensionContext: common.ExtensionContext;
let formExtensionContext: common.FormExtensionContext;
let vpnExtensionContext: common.VpnExtensionContext;
let eventHub: common.EventHub;
let pacMap: common.PacMap;
let abilityResult: common.AbilityResult;
let abilityStartCallback: common.AbilityStartCallback;
let connectOptions: common.ConnectOptions;
let embeddableUIAbilityContext: common.EmbeddableUIAbilityContext;
let photoEditorExtensionContext: common.PhotoEditorExtensionContext;
let uiServiceProxy : common.UIServiceProxy;
let uiServiceExtensionConnectCallback : common.UIServiceExtensionConnectCallback;
let appServiceExtensionContext : common.AppServiceExtensionContext;
let formEditExtensionContext : common.FormEditExtensionContext;
let liveFormExtensionContext : common.LiveFormExtensionContext;
