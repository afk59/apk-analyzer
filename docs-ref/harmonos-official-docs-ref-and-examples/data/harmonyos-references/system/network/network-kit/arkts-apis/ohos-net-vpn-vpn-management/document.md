# @ohos.net.vpn (VPN Management)

This module is the built-in VPN function provided by the OS. It allows users to set up VPN connections through the network settings of the OS. Generally, this module provides only limited functions and is subject to strict restrictions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/0-SN_WTcSfCE5J5cwxaqRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A849DD421C23DE6877FF2FC247C9FF8CF64083312B689397A7BEDA60C37117AF)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { vpn } from '@kit.NetworkKit';

#### LinkAddress

type LinkAddress = connection.LinkAddress

Defines the network link address information.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| [connection.LinkAddress](../ohos-net-connection-network-connection-management/document.md#linkaddress) | Network link address information. |

#### RouteInfo

type RouteInfo = connection.RouteInfo

Defines the network route information.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| [connection.RouteInfo](../ohos-net-connection-network-connection-management/document.md#routeinfo) | Network route information. |

#### AbilityContext

type AbilityContext = \_AbilityContext

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_AbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Context of the target **UIAbility**. It is inherited from [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) and provides the **UIAbility** configuration and methods for operating **UIAbility** and **ServiceExtensionAbility**. |
