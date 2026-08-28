# Subscribing to State Changes of a Remote Object

IPC/RPC allows you to subscribe to the state changes of a remote stub object. When the remote stub object dies, a death notification will be sent to your local proxy. To subscribe to death notifications, you need to call the [registerDeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#registerdeathrecipient9-1) API. To unsubscribe from death notifications, call the [unregisterDeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#unregisterdeathrecipient9-1) API.

To be specific, you need to inherit the death notification class [DeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#deathrecipient) and implement the [onRemoteDied](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#onremotedied) method to clear resources. This callback is invoked when the process accommodating the remote stub object exits or the DSoftBus connection on which RPC depends is disabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/aN7PmgrxQDSKNnLG2AZhaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061955Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E43C8704726D41258150DA1723FEE86DCBFC094DC23511B461159446655F185)

-   The proxy object must first subscribe to death notifications of the stub object. If the stub object is in the normal state, the proxy object can cancel the subscription as required.
-   If the process of the stub object exits or the DSoftBus connection on which RPC depends is disabled, the [onRemoteDied](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#onremotedied) method customized by the proxy object will be automatically triggered.

#### When to Use

IPC/RPC subscription is applicable to the following scenarios:

1.  In IPC, the proxy object needs to detect the status of the process hosting the remote stub object.
    
2.  In RPC, the proxy object needs to detect the status of the process hosting the remote stub object, or the DSoftBus connection status on which RPC depends.
    
    When the proxy detects the death of the remote stub object, proxy objects and clear local resources should be cleared.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/jqenrF1kRnS8O-fOtn7wpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061955Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=542B7FE342D8F7A830C1A799C2023BAFC763E17155C29EEFC0F908149E04259D)

Subscription to death notifications of anonymous stub objects (not registered with SAMgr) is supported in IPC, but not in RPC.

#### **Development Using ArkTS APIs**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/0mjp_BsyQi6N9kuUsW56Xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061955Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D81E071D631D91D659043F52565153A37D1BD226DC24CFC59295D361033DACF)

-   The sample code in this topic implements communication between system applications across processes.
    
-   Application scenario constraints: The client is a third-party or system application, and the server is a system application or service.
    

| API | Return Value Type | Description |
| :-- | :-- | :-- |
| [registerDeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#registerdeathrecipient9-1) | void | Registers a callback for receiving death notifications of the remote object. This method should be called on the proxy side. |
| [unregisterDeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#unregisterdeathrecipient9-1) | void | Unregisters from the callback used to receive death notifications of the remote object. |
| [onRemoteDied](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#onremotedied) | void | Called when the process accommodating the remote stub object dies after the proxy successfully registers the death notification. |

## Sample Code

In IPC, create the variables **want** and **connect**.

import { Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;

let want: Want = {
  // Enter the bundle name and ability name.
  bundleName: "ohos.rpc.test.server",
  abilityName: "ohos.rpc.test.server.ServiceAbility",
};
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'RpcClient: js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'RpcClient: onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'RpcClient: onFailed');
  }
};

In RPC, create the variables **want** and **connect**.

import { Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager | undefined;
let proxy: rpc.IRemoteObject | undefined;
let deviceList: Array<distributedDeviceManager.DeviceBasicInfo> | undefined;
let networkId: string | undefined;
let want: Want | undefined;
let connect: common.ConnectOptions | undefined;

try{
  dmInstance = distributedDeviceManager.createDeviceManager("ohos.rpc.test");
} catch (error) {
  let err: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'createDeviceManager errCode:' + err.code + ', errMessage:' + err.message);
}

// Use distributedDeviceManager to obtain the network ID of the target device.
if (dmInstance != undefined) {
  try {
    deviceList = dmInstance.getAvailableDeviceListSync();
    if (deviceList.length !== 0) {
      networkId = deviceList\[0\].networkId;
      want = {
        bundleName: "ohos.rpc.test.server",
        abilityName: "ohos.rpc.test.service.ServiceAbility",
        deviceId: networkId,
      };
      connect = {
        onConnect: (elementName, remoteProxy) => {
          hilog.info(0x0000, 'testTag', 'RpcClient: js onConnect called');
          proxy = remoteProxy;
        },
        onDisconnect: (elementName) => {
          hilog.info(0x0000, 'testTag', 'RpcClient: onDisconnect');
        },
        onFailed: () => {
          hilog.info(0x0000, 'testTag', 'RpcClient: onFailed');
        }
      };
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'createDeviceManager err:' + err);
  }
}

In the FA model, the [connectAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-ability-featureability#featureabilityconnectability7) API is used to connect to an ability.

import { featureAbility } from '@kit.AbilityKit';

// Save the connection ID, which will be used for the subsequent service disconnection.
let connectId = featureAbility.connectAbility(want, connect);

In the stage model, the [connectServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#connectserviceextensionability) API of **common.UIAbilityContext** is used to connect to an ability.

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](../../ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).

let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectId = context.connectServiceExtensionAbility(want, connect);

After the service is successfully connected, the proxy object in the **onConnect** callback can be assigned a value You can call the [registerDeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#registerdeathrecipient9-1) method of the proxy object to register the death callback. When the proxy object is no longer used, you can call the [unregisterDeathRecipient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#unregisterdeathrecipient9-1) method to deregister the death callback.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;

class MyDeathRecipient implements rpc.DeathRecipient{
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
let deathRecipient = new MyDeathRecipient();
if (proxy != undefined) {
  // The value 0 is a reserved flag for the death notification of the death listener and has no actual meaning. The removal of the listener provided here is only an example. The actual removal time is determined by the service.
  proxy.registerDeathRecipient(deathRecipient, 0);
  proxy.unregisterDeathRecipient(deathRecipient, 0);
}

#### Reverse Death Notification (Anonymous Stub)

Forward dead notification is a mechanism that allows the proxy to detect death notifications of the stub. To achieve reverse dead notification, you can leverage the forward dead notification mechanism. Suppose there are two processes, A (the process hosting the original stub) and B (the process hosting the original proxy). After obtaining the proxy object of process A, process B creates an anonymous stub object (that is, a stub object not registered with SAMgr), which can be called a callback stub. Then, process B calls [sendMessageRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#sendmessagerequest9-2) to send the callback stub to the original stub of process A. Then, process A obtains the callback proxy of process B. As long as the death notification is registered with the callback proxy, when process B (callback stub) dies or the DSoftBus connection on which RPC depends is disabled, the callback proxy can detect the death and notify process A (original stub). In this way, the reverse death notification is implemented.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/USEfThmUTMON3Hk9kXHqkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061955Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FAA7BAC7FCE7CB9353B0CFCEDBB121BF355E353EB0626A51DC2ABE8E19BB170)

-   Reverse death notification can only be used for cross-process communication within a device.
-   When an anonymous stub object is not referenced by any proxy, the object is automatically released.
