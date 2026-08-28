# Development Procedure (ArkTS)

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/CGU-SZduSxScp5GuHU3qUg/en-us_image_0000002474311102.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07620D81CA3C2F9E89E735BC73E011B68767CAB81575713EB04950AD0CACDF07)

1.  The sender and receiver call [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section131971556806) to create a nearby transfer service for the game.
2.  After creation, the game calls the following APIs to register listeners:
    -   [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section17453143012584)('connectNotify'): Registers a listener for connection notification.
    -   [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section766518402463)('discovery'): Registers the discovery result event, required when the sender selects a receiver to bind to.
    -   [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section1959517425315)('receivePackageInfo'): Registers a listener for package information reception.
    -   [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section05583466314)('transferNotify'): Registers a listener for transfer notification.
    -   [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section122432503314)('error'): Registers a listener for errors.
3.  The receiver calls the [publishNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section225333655719) API to publish its own nearby transfer service.
4.  The sender can bind to the receiver in the following methods:
    -   Automatic binding:
        
        The sender calls [autoBindNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section52391745713) to automatically bind to a nearby device. That is, the sender will search for and bind to the first nearby transfer service found within 10 meters.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/dsQyWpS-Slqzc3RfPglTnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=099D953A6449845D3DF08AAB989B2546E2F4480D76E2AEEF7E27FA6F8570FE5C)
        
        The automatic binding API takes effect within 2 minutes after being called. If the operation times out, you need to call the relevant API again.
        
    -   Selected binding:
        
        The sender calls [discoveryNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section16687197125918) to search for nearby devices and will receive the callback for the **discovery** event when a device is discovered. From the callback, the sender can obtain a list of discovered devices and select one to bind to. Then, the sender calls [bindNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section13279659901) to bind to the selected device.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/OPT0Sku0Ra6dpSj4AKxwXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF515011CEA187BF371A9ACA356F81B55720FD4BD5CDEE75E93EFCB7B18FD20A)
        
        This discovery API takes effect within 2 minutes after being called. If the operation times out, you need to call the relevant API again.
        
5.  After receiving the [onCollaborate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncollaborate18) callback of **UIAbility**, the receiver calls [acceptCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section106164517195) to accept the collaboration request.
6.  The receiver receives the callback for the link connection event (**connectNotify**).
7.  The receiver calls [sendPackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section12490112992612) to send its own file information, such as the version information and package information.
8.  The sender receives the callback for the **receivePackageInfo** event.
9.  The sender compares the versions and calls [replyPackageInfoResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section78288285293) to report the comparison result.
10.  After checking the comparison result and determining that the resource packages need to be sent, the sender calls [transferPackageData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section1227711101118) to send the packages to the receiver.
11.  The receiver will then obtain information such as the transferred package size, total package size, transfer rate, and remaining transfer time from the callback for the **transferNotify** event. After the transfer is complete, the receiver can obtain the storage directory of the received resource packages and process the transferred resource files.
12.  After processing the transferred resource files, the receiver can call [destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section13373155416) to destroy the service.
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/bp_Ops_mRvKKR94Oqvs0Cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DFB0CBD8B019B274EACE01529966BB7C10FAC35C427BDD34D85EC5E9FB399D2)
     
     -   The **destroy** API will then clear received data. Ensure that the received data has been processed or transferred before you call this API.
     -   The historical data will be automatically cleared upon each call to the [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section131971556806) API.
     

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer).

| 
**API Name**

 | 

**Description**

 |
| :-- | :-- |
| 

[create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section131971556806)(createParameters: CreateParameters): Promise<CreateResult>

 | 

Creates a nearby transfer service for the game.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section17453143012584)(type: 'connectNotify', callback: Callback<ConnectNotification>): void

 | 

Subscribes to the connection notification event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section3614173614593)(type: 'connectNotify', callback?: Callback<ConnectNotification>): void

 | 

Unsubscribes from the connection notification event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section766518402463)(type: 'discovery', callback: Callback<DiscoveryResult>): void

 | 

Subscribes to the discovery result event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section10671640104614)(type: 'discovery', callback?: Callback<DiscoveryResult>): void

 | 

Unsubscribes from the discovery result event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section1959517425315)(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void

 | 

Subscribes to the package information reception event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section1359944210319)(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void

 | 

Unsubscribes from the package information reception event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section05583466314)(type: 'transferNotify', callback: Callback<TransferNotification>): void

 | 

Subscribes to the transfer notification event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section65611146153113)(type: 'transferNotify', callback?: Callback<TransferNotification>): void

 | 

Unsubscribes from the transfer notification event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section122432503314)(type: 'error', callback: Callback<ReturnResult>): void

 | 

Subscribes to the error event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section20246850163115)(type: 'error', callback?: Callback<ReturnResult>): void

 | 

Unsubscribes from the error event.

 |
| 

[publishNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section225333655719)(): Promise<void>

 | 

Publishes the nearby transfer service.

 |
| 

[autoBindNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section52391745713)(): Promise<void>

 | 

Automatically binds to the nearby transfer service.

 |
| 

[discoveryNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section16687197125918)(): Promise<void>

 | 

Discovers the nearby transfer service.

 |
| 

[bindNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section13279659901)(bindParameters: BindParameters): Promise<void>

 | 

Binds to the specified nearby transfer service.

 |
| 

[acceptCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section106164517195)(acceptParameters: Record<string, object>): Promise<void>

 | 

Accepts the collaboration.

 |
| 

[sendPackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section12490112992612)(packageInfo: PackageInfo): Promise<void>

 | 

Sends the receiver's own file information (performed by the receiver).

 |
| 

[replyPackageInfoResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section78288285293)(packageInfoResult: PackageInfoResult): Promise<void>

 | 

Reports the package information comparison result.

 |
| 

[transferPackageData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section1227711101118)(packageData: PackageData): Promise<void>

 | 

Transfers package data.

 |
| 

[destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section13373155416)(): Promise<void>

 | 

Destroys the nearby transfer service created for the game.

 |

#### Integration Procedure

## Importing Modules

Import Game Service Kit and common modules.

import { abilityAccessCtrl, AbilityConstant, UIAbility, common } from "@kit.AbilityKit";
import { hilog } from '@kit.PerformanceAnalysisKit';
import { gameNearbyTransfer } from '@kit.GameServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Requesting Permissions

Request the **ohos.permission.DISTRIBUTED\_DATASYNC** permission for device discovery. For details, please refer to [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

let atManager = abilityAccessCtrl.createAtManager();
let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
try {
  atManager.requestPermissionsFromUser(uiAbilityContext, \['ohos.permission.DISTRIBUTED\_DATASYNC'\]).then((data) => {
    hilog.info(0x0000, 'nearby', '%{public}s', 'data: ' + JSON.stringify(data));
  }).catch((err: object) => {
    hilog.error(0x0000, 'nearby', '%{public}s', 'err: ' + JSON.stringify(err));
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

## Creating a Nearby Transfer Service and Registering Relevant Callbacks

After importing required modules, call the [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section131971556806) API to create a nearby transfer service and register relevant callbacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/ITh4J5l-QIezwWJK05-0vQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9520B840C7CCA0009E7AB4B6A16A1D876BAFEC4478B1E48EC185D5352C2CB620)

The [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section131971556806) API is the prerequisite for calling other APIs. Not creating a nearby transfer service or failing to do so will result in the failure of other API calls.

public create() {
  let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
  let initParam: gameNearbyTransfer.CreateParameters = {
    abilityName: uiAbilityContext.abilityInfo.name,
    context: uiAbilityContext,
    moduleName: uiAbilityContext.abilityInfo.moduleName,
    needShowSystemUI: false // Indicates whether to display the system UI. **true**: yes; **false** (default): no.
  };
  try {
    gameNearbyTransfer.create(initParam).then((createResult) => {
      hilog.info(0x0000, '\[nearby\]', '%{public}s', 'create success' + createResult.localDeviceName);
      this.registerCallback();
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'create error' + (err as Error).message);
    })
  } catch (err) {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
  }
}

// Register a listener.
public registerCallback() {
  try {
    gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
    gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
    gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
    gameNearbyTransfer.on('error', errorCallBack);
  } catch (err) {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
  }
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // Connection status callback. After receiving the link setup success callback, the receiver calls the **sendPackageInfo** API to send its own file information, such as the version information and package information.
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // Package information reception callback. After receiving the version information from the receiver, the sender compares the received version information with its local version information, and then determines whether to transfer the resource package data based on the comparison result.
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // Transfer callback used to process the transfer progress information.
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  // Exception callback used to process the exception information.
}

## Accepting Collaboration Request

The receiver implements the [onCollaborate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncollaborate18) callback and calls the [acceptCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section106164517195) API in the callback to accept the collaboration request.

export default class EntryAbility extends UIAbility { 
  // Collaboration callback.
  onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
    try {
      gameNearbyTransfer.acceptCollaboration(wantParam);
    } catch (err) {
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
    }
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'onCollaborate: accept collaborate');
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}

## Publishing the Receiver's Own Nearby Transfer Service (Performed by the Receiver)

The receiver calls the [publishNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section225333655719) API to publish its own nearby transfer service.

try {
  gameNearbyTransfer.publishNearbyGame().then(() => {
    hilog.info(0x0000, '\[nearby\]', '%{public}s', 'publishNearbyGame success');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'publishNearbyGame error' + (err as Error).message);
  })
} catch (err) {
  hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
}

## Binding to the Receiver's Nearby Transfer Service (Performed by the Sender)

The sender can bind to the nearby transfer service of the receiver in the following ways:

-   Method 1: automatic binding
    
    The sender calls the [autoBindNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section52391745713) API to automatically bind to the nearby transfer service of the receiver.
    
    try {
      gameNearbyTransfer.autoBindNearbyGame().then(() => {
        hilog.info(0x0000, '\[nearby\]', '%{public}s', 'autoBindNearbyGame success');
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, '\[nearby\]', '%{public}s', 'autoBindNearbyGame error' + (err as Error).message);
      })
    } catch (err) {
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
    }
    

-   Method 2: selected binding
    1.  The sender calls the [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section766518402463)('discovery') API to listen to the discovery result event.
        
        try {
          gameNearbyTransfer.on('discovery', discoveryCallBack);
        } catch (err) {
          hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message)
        }
        
        function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
          // Obtain the discovered devices and display the device list.
          callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {    
          });
        }
        
    2.  The sender calls [discoveryNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section16687197125918) to discover a nearby device.
        
        try {
          gameNearbyTransfer.discoveryNearbyGame().then(() => {
            hilog.info(0x0000, '\[nearby\]', '%{public}s', 'discoveryNearbyGame success');
          }).catch((err: BusinessError) => {
            hilog.error(0x0000, '\[nearby\]', '%{public}s', 'discoveryNearbyGame error' + (err as Error).message);
          })
        } catch (err) {
          hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
        }
        
    3.  After the discovering operation, a callback that listens to the **discovery** event will be received. From the callback, the sender can obtain a list of discovered devices and select one to bind to. Then, the sender calls [bindNearbyGame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section13279659901) to bind to the selected device.
        
        public bindNearbyGame(deviceInfo: gameNearbyTransfer.NearbyGameDevice) {
          try {
            let bindInfo: gameNearbyTransfer.BindParameters = {
              deviceId: deviceInfo.deviceId,
              networkId: deviceInfo.networkId
            };
            gameNearbyTransfer.bindNearbyGame(bindInfo).then(() => {
              hilog.info(0x0000, '\[nearby\]', '%{public}s', 'bindNearbyGame success');
            }).catch((err: BusinessError) => {
              hilog.error(0x0000, '\[nearby\]', '%{public}s', 'bindNearbyGame error' + (err as Error).message);
            })
          } catch (err) {
            hilog.error(0x0000, '\[nearby\]', '%{public}s', 'bindNearbyGame error' + (err as Error).message);
          }
        }
        

## Sending the Receiver's Own File Information (Performed by the Receiver)

After receiving the link setup success callback, the receiver calls the [sendPackageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section12490112992612) API to send its own file information, such as the version information and package information.

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  if (callback.connectState == gameNearbyTransfer.ConnectState.CONNECTED) {
    // Callback for successful connection, which is used to indicate whether the current device is the receiver. If so, set the relevant parameter to **true**. Otherwise, set it to **false**.
    let isReceive = true;
    if (!isReceive) {
      return;
    }
    // After receiving the link setup success callback, the receiver sends the resource package information to the sender.
    let packageInfo: gameNearbyTransfer.PackageInfo = {
      name: 'com.huawei.xxxx',
      files: \[\],
      version: '1.1.0',
      extraData: 'extraData'
    };
    let fileInfo: gameNearbyTransfer.FileInfo = {
      path: "/xxx/xxxx/files/data.zip",  // Use a sandbox path. For details, please refer to [Application Sandbox](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
      hash: 'fileHash' // Optional.
    };
    packageInfo.files?.push(fileInfo);
    try {
      gameNearbyTransfer.sendPackageInfo(packageInfo).then(() => {
        hilog.info(0x0000, '\[nearby\]', '%{public}s', 'sendPackageInfo success');
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, '\[nearby\]', '%{public}s', 'sendPackageInfo error' + (err as Error).message);
      });
    } catch (err) {
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
    }
  }
}

## Transferring the Resource Packages After Comparing Versions (Performed by the Sender)

After receiving the version information from the receiver, the sender compares the version information, calls the [replyPackageInfoResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section78288285293) API to report the comparison result, and determines whether to call the [transferPackageData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section1227711101118) API to send the resource package data based on the comparison result.

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // Compare versions or file hashes to determine whether to send the resource packages.
  let packageInfoResult: gameNearbyTransfer.PackageInfoResult = {
    packageInfoResultCode: gameNearbyTransfer.PackageInfoResultCode.PACKAGE\_AVAILABLE\_COMPARED
  };
  try {
  // Report the comparison result.
    gameNearbyTransfer.replyPackageInfoResult(packageInfoResult).then(() => {
      let packageData: gameNearbyTransfer.PackageData = {
        name: 'com.huawei.gamenearbydemo',
        version: '1.0.0',
        files: \[{
          srcPath: '/data/xxxx/a.zip', // Sandbox path of the file to be sent. For details, please refer to [Application Sandbox](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
          destPath: 'xxxx/a.zip'       // Custom path for receiving files. The complete sandbox path is _[fileStoragePath](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section116223815415) + destPath_. For details, please refer to [Application Sandbox](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
        }\] 
      }
      try {
        // Send the resource packages.
        gameNearbyTransfer.transferPackageData(packageData).then(() => {
          // Successfully sent.
        }).catch((err: BusinessError) => {
          // Catch errors.
          hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);          
        });
      } catch (err) {
        hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
      }
    }).catch((err: BusinessError) => {
      // Report the errors.
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
    });
  } catch (err) {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
  }
}

## Processing the Resource Package Transfer Progress Information

The sender and receiver process the transfer progress information in the callback for transfer notification.

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  if (callback.transferState == gameNearbyTransfer.TransferState.SEND\_PROCESS) {
    // Process the sending progress, for example, displaying the progress bar and rate.
  }
  if (callback.transferState == gameNearbyTransfer.TransferState.SEND\_FINISH) {
    // Sending complete.
  }
  if (callback.transferState == gameNearbyTransfer.TransferState.RECEIVE\_PROCESS) {
    // Process the receiving progress, for example, displaying the progress bar and rate.
  }
  if (callback.transferState == gameNearbyTransfer.TransferState.RECEIVE\_FINISH) {
    // After reception, the sandbox path for the resource packages will be obtained.
    let fileStoragePath = callback.fileStoragePath;
    // Process files in **fileStoragePath**.
  }
}

## Destroying the Service After Processing the Received Resource Packages

After processing or transferring the received data, call the [destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-nearbytransfer#section13373155416) API to destroy the service. To use the nearby transfer service after it is destroyed, you need to [create a nearby transfer service and register relevant callbacks](#section8810153223912) again.

public destroy() {
  // Unregister the callback.
  this.unregisterCallback();
  // Destroy the service.
  try {
    gameNearbyTransfer.destroy().then(() => {
      hilog.info(0x0000, '\[nearby\]', '%{public}s', 'destroy success');
    }).catch((err: Error) => {
      hilog.error(0x0000, '\[nearby\]', '%{public}s', 'destroy error' + (err as Error).message);
    });
  } catch (err) {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
  }
}

public unregisterCallback() {
  try {
    gameNearbyTransfer.off('connectNotify', connectNotifyCallBack);
    gameNearbyTransfer.off('receivePackageInfo', receivePackageInfoCallBack);
    gameNearbyTransfer.off('transferNotify', transferNotifyCallBack);
    gameNearbyTransfer.off('error', errorCallBack);
    // The sender selects to manually bind the receiver. Before this operation, the sender must have subscribed to the **discovery** event.
    gameNearbyTransfer.off('discovery', discoveryCallBack);
  } catch (err) {
    hilog.error(0x0000, '\[nearby\]', '%{public}s', 'error' + (err as Error).message);
  }
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // Connection status callback. After receiving the link setup success callback, the receiver calls the **sendPackageInfo** API to send its own file information, such as the version information and package information.
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // Package information reception callback. After receiving the version information from the receiver, the sender compares the received version information with its local version information, and then determines whether to transfer the resource package data based on the comparison result.
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // Transfer callback used to process the transfer progress information.
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  // Exception callback used to process the exception information.
}

function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
  // Obtain the discovered devices and display the device list.
  callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
  });
}
