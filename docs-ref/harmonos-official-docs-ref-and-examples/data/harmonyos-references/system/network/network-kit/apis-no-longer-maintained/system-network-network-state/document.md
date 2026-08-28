# @system.network (Network State)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/joaRkvR0Q2um0uBWr0NogQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062348Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EEB9AE630A8CE281AC30D78896F55C3A6F04F0519E44A0DD8B8A66589345911)

-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module are no longer maintained since API version 8. You are advised to use ['@ohos.net.connection'](../../arkts-apis/ohos-net-connection-network-connection-management/document.md).
    

#### Modules to Import

import network from '@system.network';

#### Required Permissions

ohos.permission.GET\_WIFI\_INFO

ohos.permission.GET\_NETWORK\_INFO

#### network.getType3+

getType(options?: {

success?: (data: NetworkResponse) => void;

fail?: (data: any, code: number) => void;

complete?: () => void;

}): void

Obtains the network type of this device.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | Function | No | Called when the API call is successful. The return value is defined by [NetworkResponse](#networkresponse3). |
| fail | Function | No | Called when an API call fails. |
| complete | Function | No | Called when an API call is complete. |

Error codes:

| Error Code | Description |
| :-- | :-- |
| 602 | The current permission is not declared. |

**Example**

export default class Network {
  getType() {
    network.getType({
      success: (data) => {
        console.info('success get network type:' + data.type);
      }
    });
  }
}

#### network.subscribe3+

subscribe(options?:{

success?: (data: NetworkResponse) => void;

fail?: (data: any, code: number) => void;

}): void

Listens to the network connection state of this device. If this API is called multiple times, the last call takes effect.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | Function | No | Called when the network connection state changes The return value is defined by [NetworkResponse](#networkresponse3). |
| fail | Function | No | Called when an API call fails. |

Error codes:

| Error Code | Description |
| :-- | :-- |
| 602 | The current permission is not declared. |
| 200 | Subscription failed. |

**Example**

export default class Network {
  subscribe() {
    network.subscribe({
      success: (data) => {
        console.info('success get network type:' + data.type);
      }
    });
  }
}

#### network.unsubscribe3+

unsubscribe(): void

Cancels listening to the network connection state of this device.

**System capability**: SystemCapability.Communication.NetManager.Core

**Example**

import network from '@system.network';

network.unsubscribe();

#### NetworkResponse3+

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| metered | boolean | No | Yes | Whether to charge by traffic. The value **true** means to charge by traffic, and the value **false** means the opposite. |
| type | string | No | No | Network type. The value can be **2G**, **3G**, **4G**, **5G**, **WiFi**, or **none**. |
