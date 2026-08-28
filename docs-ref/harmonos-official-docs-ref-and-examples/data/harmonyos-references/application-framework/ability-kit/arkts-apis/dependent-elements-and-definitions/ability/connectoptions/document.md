# ConnectOptions

**ConnectOptions** can be used as an input parameter to receive status changes during the connection to a background service. For example, it is used as an input parameter of [connectServiceExtensionAbility](../../application/uiabilitycontext/document.md#connectserviceextensionability) to connect to a ServiceExtensionAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/SwweLo52RyC3Ie8kfvaDgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB2E432A04FAFB51003BD883F8673AC1A718F6131CCCB501A4E6CA1454956931)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### ConnectOptions

#### \[h2\]onConnect

onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void

Callback invoked when a connection is set up.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../bundlemanager/elementname/document.md) | Yes | Element name of the target ability. |
| remote | [rpc.IRemoteObject](../../../../../ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#iremoteobject) | Yes | IRemoteObject instance used for IPC with the target ability. |

**Example**

import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect(elementName: bundleManager.ElementName, remote: rpc.IRemoteObject) {
    console.info(\`onConnect elementName: ${elementName}\`);
  },
  onDisconnect(elementName: bundleManager.ElementName) {
    console.info(\`onDisconnect elementName: ${elementName}\`);
  },
  onFailed(code: number) {
    console.error(\`onFailed code: ${code}\`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection: number = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}

#### \[h2\]onDisconnect

onDisconnect(elementName: ElementName): void

Callback invoked when a connection is interrupted.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../bundlemanager/elementname/document.md) | Yes | Element name of the target ability. |

**Example**

import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect(elementName: bundleManager.ElementName, remote: rpc.IRemoteObject) {
    console.info(\`onConnect elementName: ${elementName}\`);
  },
  onDisconnect(elementName: bundleManager.ElementName) {
    console.info(\`onDisconnect elementName: ${elementName}\`);
  },
  onFailed(code: number) {
    console.error(\`onFailed code: ${code}\`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection: number = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}

#### \[h2\]onFailed

onFailed(code: number): void

Callback invoked when a connection fails.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | 
Error code returned when connection to the specified ability fails.

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

201 - The application does not have permission to call the interface.

16000001 - The specified ability does not exist.

16000002 - Incorrect ability type.

16000004 - Cannot start an invisible component.

16000005 - The specified process does not have the permission.

16000006 - Cross-user operations are not allowed.

16000008 - The crowdtesting application expires.

16000053 - The ability is not on the top of the UI.

16000055 - Installation-free timed out.

16000050 - Internal error.

 |

**Example**

import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect(elementName: bundleManager.ElementName, remote: rpc.IRemoteObject) {
    console.info(\`onConnect elementName: ${elementName}\`);
  },
  onDisconnect(elementName: bundleManager.ElementName) {
    console.info(\`onDisconnect elementName: ${elementName}\`);
  },
  onFailed(code: number) {
    console.error(\`onFailed code: ${code}\`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection: number = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}
