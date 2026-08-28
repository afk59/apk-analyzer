# IPC and RPC Development (ArkTS)

#### When to Use

IPC/RPC is used to implement object communication across processes (one-to-one mapping between the client proxy and the server stub).

#### How to Develop

## Connecting to the Service and Obtaining the Service Proxy

**Creating want and connect**

1.  Create a **want** variable, and specify the bundle name and component name of the application where the ability is located. If cross-device communication is involved, also specify the network ID of the target device, which can be obtained through distributedDeviceManager.
    
2.  Create a **connect** variable, and specify the callback that is called when the binding is successful, the binding fails, or the ability is disconnected.
    
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
    

**Connection Service**

In the FA model, the [connectAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-ability-featureability#featureabilityconnectability7) API is used to connect to an ability.

import { featureAbility } from '@kit.AbilityKit';

// Save the connection ID, which will be used when the ability is disconnected.
let connectId = featureAbility.connectAbility(want, connect);

In the stage model, the [connectServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#connectserviceextensionability) API of **common.UIAbilityContext** is used to connect to an ability.

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](../../ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).

let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used when the ability is disconnected.
let connectId = context.connectServiceExtensionAbility(want, connect);

## Sending Information from Client to Server

After the service is successfully connected, you can use the **onConnect** callback to obtain the proxy object of the server. Then, use the proxy to call the [sendMessageRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#sendmessagerequest9-2) method to initiate a request. When the server processes the request and returns data, you can receive the result returned by a promise contract (used to indicate the success or failure result value of an asynchronous operation).

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// The proxy in this code snippet is obtained from the onConnect callback after the service is successfully connected.
let proxy: rpc.IRemoteObject | undefined;

// Use the promise contract.
let option = new rpc.MessageOption();
let data = rpc.MessageSequence.create();
let reply = rpc.MessageSequence.create();
// Write parameters in data. The following uses the string as an example.
data.writeString("hello world");

if (proxy != undefined) {
  proxy.sendMessageRequest(1, data, reply, option)
    .then((result: rpc.RequestResult) => {
      if (result.errCode != 0) {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
        return;
      }
      // Read the result from result.reply.
      // The following is an example of creating a ServiceExtensionAbility on the server.
      result.reply.readString();
    })
    .catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendMessageRequest got exception: ' + e);
    })
    .finally(() => {
      data.reclaim();
      reply.reclaim();
    })
}

## Server Handling of Client Requests

Call **onConnect()** to return a stub object inherited from [rpc.RemoteObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#remoteobject), and implement [onRemoteMessageRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc#onremotemessagerequest9) for the object to process requests sent from the client.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // The server stub executes the corresponding processing based on the request code.
    if (code == 1) {
      let str = data.readString();
      hilog.info(0x0000, 'testTag', 'stub receive str : ' + str);
      // The server sends the request processing result to the client.
      reply.writeString("hello rpc");
      return true;
    } else {
        hilog.info(0x0000, 'testTag', 'stub unknown code: ' + code);
        return false;
    }
  }
}

## Terminating the Connection

After IPC is complete, the FA model calls [disconnectAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-ability-featureability#featureabilitydisconnectability7) to disable the connection. The **connectId** is saved when the service is connected.

import { featureAbility } from "@kit.AbilityKit";
import { hilog } from '@kit.PerformanceAnalysisKit';

function disconnectCallback() {
  hilog.info(0x0000, 'testTag', 'disconnect ability done');
}
// Use the connectId saved when the service is successfully connected to disable the connection.
featureAbility.disconnectAbility(connectId, disconnectCallback);

The **common.UIAbilityContext** provides the [disconnectServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#disconnectserviceextensionability-1) API to disconnect from the service. The **connectId** is saved when the service is connected.

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](../../ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).

let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
 
// Use the connectId saved when the service is successfully connected to disable the connection.
context.disconnectServiceExtensionAbility(connectId);

#### Sample

For the end-to-end complete example of IPC and RPC development, see the following:

-   [Complete IPC Example - Using Parcelable/ArrayBuffer](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/SystemFeature/IPC/ObjectTransfer)
