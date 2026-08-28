# @ohos.net.ethernet (Ethernet Connection Management)

The **ethernet** module provides Ethernet management functions such as configuring a network proxy and obtaining the network IP address.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/hBwu58D-Rb2-Y8SZdzkMVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB32A84F066D5FC0B68242D0C0121CC184B69C854BBB3227241EA9E46D09D6DF)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ethernet } from '@kit.NetworkKit';

#### HttpProxy10+

type HttpProxy = connection.HttpProxy

Defines the network proxy configuration.

**System capability**: SystemCapability.Communication.NetManager.Ethernet

| Type | Description |
| :-- | :-- |
| connection.HttpProxy | Network proxy configuration. |

#### ethernet.getMacAddress14+

getMacAddress(): Promise<Array<MacAddressInfo>>

Obtains the names and MAC addresses of all Ethernet NICs. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_ETHERNET\_LOCAL\_MAC

**System capability**: SystemCapability.Communication.NetManager.Ethernet

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array[<MacAddressInfo>](#macaddressinfo14)\> | Promise used to return the result. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2201005 | Device information does not exist. |

**Example**

import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.getMacAddress().then((data: Array<ethernet.MacAddressInfo>) => {
  console.info("getMacAddress promise data = " + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error("getMacAddress promise error = " + JSON.stringify(error));
});

#### MacAddressInfo14+

Defines the name and MAC address of an Ethernet NIC.

**System capability**: SystemCapability.Communication.NetManager.Ethernet

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iface | string | No | No | Name of the Ethernet NIC. |
| macAddress | string | No | No | MAC address of the Ethernet NIC. |
