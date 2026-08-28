# @ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)

WebNativeMessagingExtensionAbility provides the web native messaging capability and is inherited from ExtensionAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Xaia1pQTRwGaFj2s4goNdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062314Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1894432FC9CD658E6862E67CF21BBC2DE2FEC06C6988E30B315023B672E80E4D)

The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { WebNativeMessagingExtensionAbility } from '@kit.ArkWeb';

#### WebNativeMessagingExtensionAbility

Provides the web native messaging capability and is inherited from ExtensionAbility.

#### \[h2\]Attributes

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [WebNativeMessagingExtensionContext](../ohos-web-webnativemessagingextensioncontext-web-native-messaging-extension-conte/document.md) | No | No | Context of web native messaging. |

#### \[h2\]onConnectNative

onConnectNative(info: ConnectionInfo): void

Called when a web native messaging connection is established.

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [ConnectionInfo](#connectioninfo) | Yes | Connection information. |

**Example**

import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    console.info('Web Native connection established!');
    console.info(\`Connection ID: ${info.connectionId}\`);
    console.info(\`Caller bundle: ${info.bundleName}\`);
    // Process the service logic after the connection is established.
  }
}

#### \[h2\]onDisconnectNative

onDisconnectNative(info: ConnectionInfo): void

Called when a web native messaging connection is disconnected.

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [ConnectionInfo](#connectioninfo) | Yes | Connection information. |

**Example**

import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onDisconnectNative(info: ConnectionInfo): void {
    console.info('Web Native connection closed!');
    console.info(\`Connection ID: ${info.connectionId}\`);
    // Process the cleanup after the connection is disconnected.
  }
}

#### \[h2\]onDestroy

onDestroy(): void

Called when the WebNativeMessagingExtensionAbility is destroyed.

**System capability**: SystemCapability.Web.Webview.Core

**Model restriction**: This API can be used only in the stage model.

**Example**

import { WebNativeMessagingExtensionAbility } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onDestroy(): void {
    console.info('WebNativeMessagingExtensionAbility is about to be destroyed!');
    // Release resources or perform cleanup operations.
  }
}

#### ConnectionInfo

Represents the information object of the web native messaging connection.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| connectionId | number | No | No | Connection ID. |
| bundleName | string | No | No | Application bundle name of the caller. |
| extensionOrigin | string | No | No | Original URL of the caller extension. |
| fdRead | number | No | No | Pipe file descriptor used to read data. |
| fdWrite | number | No | No | Pipe file descriptor used to write data. |
