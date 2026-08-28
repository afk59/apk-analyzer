# @ohos.net.connection (Network Connection Management)

The network connection management module provides basic network management capabilities. You can obtain the default active network, the list of all active networks, and network capability information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Vg7-MxjRSX6F_eVM89L3eA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=173DB2840902270F810A0B487FC9FB915F5500D3BB2F436C761BDC8B95B83117)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Unless otherwise specified, the APIs of this module do not support concurrent calls.

#### Modules to Import

import { connection } from '@kit.NetworkKit';

#### connection.createNetConnection

createNetConnection(netSpecifier?: NetSpecifier, timeout?: number): NetConnection

Creates a **NetConnection** object, which can be used to listen for the network status. [netSpecifier](#netspecifier) specifies the network to be listened for, and **timeout** indicates the timeout duration (ms). **netSpecifier** is a mandatory parameter for **timeout**. If neither of them is present, the default network is used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/VOgyoWmaS6SJRzgboAjpSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9D3471158DEA2CC3CDB5F9B90AAFC79FC01E81999069E1DDB427FB63CB15AC8)

To listen for the network status, after creating a **NetConnection** object, you need to call [register](#register) to register the notification of the specified network status change.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netSpecifier | [NetSpecifier](#netspecifier) | No | Specification of the network to be listened for. If this parameter is not specified, the default network is listened for. |
| timeout | number | No | 
Timeout interval for obtaining the network specified by **netSpecifier**. The input value must be an uint32\_t integer. This parameter is valid only when **netSpecifier** is present. The default value is **0**.

**Note**: If the network to be listened for does not exist, the system attempts to activate the network. If the timeout interval is exceeded and the network status listener is registered, the **netUnavailable** event is triggered.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NetConnection](#netconnection) | Type of the network connection object to be listened for. |

**Example**

import { connection } from '@kit.NetworkKit';

// Example 1: Only the default network is concerned. You do not need to specify the netSpecifier parameter. If the timeout parameter is not passed, the timeout interval is not used. In this case, the value of timeout is 0.
let netConnection = connection.createNetConnection();

// Example 2: Only the cellular network is concerned. You need to specify the network type to cellular.
let timeout = 1000;
let netConnectionCellular = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: \[connection.NetBearType.BEARER\_CELLULAR\]
  }
}, timeout);

// Example 3: Both the cellular and Wi-Fi networks are concerned. You need to specify the network type to cellular and Wi-Fi.
let netConnectionCellularAndWifi = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: \[connection.NetBearType.BEARER\_CELLULAR,
      connection.NetBearType.BEARER\_WIFI\]
  }
});

#### connection.getDefaultNet

getDefaultNet(callback: AsyncCallback<NetHandle>): void

Obtains the network handle used by the system by default, including the network ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/BCDxNApZTLy0PH9eo4u0Lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31975681F33017C7B77B6179CE483B283A7773CF9E707EB0331A94BD4BC5C8F9)

-   Default network used by the system. The network must have the [NET\_CAPABILITY\_INTERNET](#netcap) capability and is not a VPN network.
    
-   The return value of this interface is determined by the system and is irrelevant to whether the application specifies a network.
    
-   Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch) > Wi-Fi > Cellular. In special cases, the actual return result prevails.
    
-   [NetHandle](#nethandle) is the unique identifier of the network. If no network is available, **0** is returned. It can be used by [getNetCapabilities](#connectiongetnetcapabilities) to query more network information.
    

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetHandle](#nethandle)\> | Yes | Callback used to return the result. When the network handle of the default activated network is successfully obtained, **error** is **undefined** and **data** is the network handle of the default network; otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, data: connection.NetHandle) => {
  if (error) {
    console.error(\`Failed to get default net. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

#### connection.getDefaultNet

getDefaultNet(): Promise<NetHandle>

Obtains the network handle used by the system by default, including the network ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/wuyV17LiSgWAYke428Lxww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F66C0D722B86953DD97B45E4968080353DC74C2B2072D3CF8454F2B3E5D5F25D)

-   Default network used by the system. The network must have the [NET\_CAPABILITY\_INTERNET](#netcap) capability and is not a VPN network.
    
-   The return value of this interface is determined by the system and is irrelevant to whether the application specifies a network.
    
-   Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch) > Wi-Fi > Cellular. In special cases, the actual returned result prevails.
    
-   [NetHandle](#nethandle) is the unique identifier of the network. If no network is available, **0** is returned. It can be used by [getNetCapabilities](#connectiongetnetcapabilities) to query more network information.
    

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetHandle](#nethandle)\> | Promise used to return the network handle of the default network. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

#### connection.getDefaultNetSync9+

getDefaultNetSync(): NetHandle

Obtains the network handle used by the system by default, including the network ID. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/aw-odzvUSbyVv009GV4lPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD61DEB4C91FDF75E85E7968857D97088AC2EB97C3BE1AEAD4D9E24DA7788931)

-   Default network used by the system. The network must have the [NET\_CAPABILITY\_INTERNET](#netcap) capability and is not a VPN network.
    
-   The return value of this interface is determined by the system and is irrelevant to whether the application specifies a network.
    
-   Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch) > Wi-Fi > Cellular. In special cases, the actual returned result prevails.
    
-   [NetHandle](#nethandle) is the unique identifier of the network. If no network is available, **0** is returned. It can be used by [getNetCapabilities](#connectiongetnetcapabilities) to query more network information.
    

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [NetHandle](#nethandle) | Network handle of the default network. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let netHandle = connection.getDefaultNetSync();

#### connection.setAppHttpProxy11+

setAppHttpProxy(httpProxy: HttpProxy): void

Sets the application-level HTTP proxy configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/SMNrxZUSRw6dzyirGRssfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E7575567162B22CF2989285ADC6D99549B6294BE247F904B3FBCBEEE29FCC3D)

If you want to use the proxy information configured by this API, set **usingProxy** in [HttpRequestOptions](../ohos-net-http-data-request/document.md#httprequestoptions) to **true** to enable proxy forwarding. This API is used only for configuring proxy rules. It does not verify the validity of the proxy service.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| httpProxy | [HttpProxy](#httpproxy10) | Yes | Application-level HTTP proxy configuration. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100001 | Invalid http proxy. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';

let exclusionStr = "192.168,baidu.com";
let exclusionArray = exclusionStr.split(',');
connection.setAppHttpProxy({
  host: "192.168.xx.xxx",
  port: 8080,
  exclusionList: exclusionArray
} as connection.HttpProxy);
let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
  usingProxy: true, // This field specifies whether to use the network proxy. It is supported since API version 10.
};
// Initiate an HTTP request.
httpRequest.request("EXAMPLE\_URL", options, (err: Error, data: http.HttpResponse) => {
  if (!err) {
   console.info(\`Result: ${data.result}\`);
   console.info(\`code: ${data.responseCode}\`);
   console.info(\`type: ${JSON.stringify(data.resultType)}\`);
   console.info(\`header: ${JSON.stringify(data.header)}\`);
   console.info(\`cookies: ${data.cookies}\`); // Cookies are supported since API version 8.
  } else {
   console.error(\`error: ${JSON.stringify(err)}\`);
  }
});

#### connection.getDefaultHttpProxy10+

getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void

Obtains the default HTTP proxy configuration of the network. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/D8J5omraRKCg7aScMtzyXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=585E94537F13C2F181A1A6FF909E8E94545881A2793F9DCADD9D6BF7D1A255B8)

-   If the global proxy is set, the global proxy configuration is returned.
-   If [setAppNet](#connectionsetappnet9) is used to bind the application to the network specified by [NetHandle](#nethandle), the HTTP proxy configuration of this network is returned. In other cases, the HTTP proxy configuration of the default network is returned.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[HttpProxy](#httpproxy10)\> | Yes | Callback used to return the result. If the global HTTP proxy configuration of the network is obtained successfully, **error** is **undefined** and **data** is the global HTTP proxy configuration. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy((error: BusinessError, data: connection.HttpProxy) => {
  if (error) {
    console.error(\`Failed to get default http proxy. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data" + JSON.stringify(data));
});

#### connection.getDefaultHttpProxy10+

getDefaultHttpProxy(): Promise<HttpProxy>

Obtains the default HTTP proxy configuration of the network. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/AKVwgh9oTleXVDxZZFTaCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC08B0E59F3F71CD372B045B6F2094A23B55A9226759591D6F869CC5BD89529C)

-   If the global proxy is set, the global proxy configuration is returned.
-   If [setAppNet](#connectionsetappnet9) is used to bind the application to the network specified by [NetHandle](#nethandle), the HTTP proxy configuration of this network is returned. In other cases, the HTTP proxy configuration of the default network is returned.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[HttpProxy](#httpproxy10)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
  console.info(JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.info(JSON.stringify(error));
});

#### connection.getAppNet9+

getAppNet(callback: AsyncCallback<NetHandle>): void

Obtains the network handle bound to an application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetHandle](#nethandle)\> | Yes | Callback used to return the result. If information about the network bound to the application is successfully obtained, **error** is **undefined** and **data** is the obtained network information. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAppNet((error: BusinessError, data: connection.NetHandle) => {
  if (error) {
    console.error(\`Failed to get App net. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})

#### connection.getAppNet9+

getAppNet(): Promise<NetHandle>

Obtains the network information bound to an application. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetHandle](#nethandle)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAppNet().then((data: connection.NetHandle) => {
  console.info(JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.info(JSON.stringify(error));
});

#### connection.getAppNetSync10+

getAppNetSync(): NetHandle

Obtains the network information bound to an application. This API returns the result synchronously.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [NetHandle](#nethandle) | Data network bound to the application. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAppNetSync();

#### connection.setAppNet9+

setAppNet(netHandle: NetHandle, callback: AsyncCallback<void>): void

Binds an application to the network specified by **netHandle**, so that the application can access the external network only through this network. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the application is successfully bound to the specified network, **error** is **undefined**. Otherwise, **error** is an error object. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/cGv_DZgKQtGXHvLbRskxmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDBBB1AF9F9EFCC6941B8BBB362F7156B89A6C9819040E304580E65440C1158C)

To unbind the application from the specified network, call [setAppNet](#connectionsetappnet9) and pass a **NetHandle** object with **netId** set to **0**. For details, see the following example.

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  netHandle.netId = 0;
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(\`Failed to get default net. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  // The application accesses the network using the default network.
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(\`Failed to get default net. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

#### connection.setAppNet9+

setAppNet(netHandle: NetHandle): Promise<void>

Binds an application to the network specified by **netHandle**, so that the application can access the external network only through this network. This API uses a promise to return the result. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/DaJrGs8BQ464V1dUYGj30Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E39B64C1778B3B3445B181913AD679259E9F15D587E7B1D8F70734E24BFFCADB)

To unbind the application from the specified network, call [setAppNet](#connectionsetappnet9) and pass a **NetHandle** object with **netId** set to **0**. For details, see the following example.

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  netHandle.netId = 0;
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(\`Failed to get default net. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }

  connection.setAppNet(netHandle).then(() => {
    console.info("success");
  }).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  })
});

#### connection.getAllNets

getAllNets(callback: AsyncCallback<Array<NetHandle>>): void

Obtains the list of all connected networks. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[NetHandle](#nethandle)\>> | Yes | 
Callback used to return the result. If the list of all connected networks is obtained successfully, **error** is **undefined** and **data** is the list of activated networks. Otherwise, **error** is an error object.

Note: If Wi-Fi and cellular data are both enabled, and no application specifies the use of cellular data, only Wi-Fi is activated. In this case, only the **NetHandle** of Wi-Fi is returned. The NetHandle of Wi-Fi and cellular data can be obtained at the same time only when a specific application enables the cellular network.

 |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAllNets((error: BusinessError, data: connection.NetHandle\[\]) => {
  if (error) {
    console.error(\`Failed to get all nets. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

#### connection.getAllNets

getAllNets(): Promise<Array<NetHandle>>

Obtains the list of all connected networks. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NetHandle](#nethandle)\>> | Promise used to return the list of activated networks. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getAllNets().then((data: connection.NetHandle\[\]) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

#### connection.getAllNetsSync10+

getAllNetsSync(): Array<NetHandle>

Obtains the list of all connected networks. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[NetHandle](#nethandle)\> | List of all connected networks. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAllNetsSync();

#### connection.getConnectionProperties

getConnectionProperties(netHandle: NetHandle, callback: AsyncCallback<ConnectionProperties>): void

Obtains the connection information of the data network specified by **NetHandle**, including the NIC name, domain name, link information, route information, network address, and maximum transmission unit. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |
| callback | AsyncCallback<[ConnectionProperties](#connectionproperties)\> | Yes | Callback used to return the result. If the connection properties of the network specified by **netHandle** is obtained successfully, **error** is **undefined** and **data** is the obtained network connection information. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Example: Obtain the connection information of the default network.
connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
    if (error) {
      console.error(\`Failed to get connection properties. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
});

#### connection.getConnectionProperties

getConnectionProperties(netHandle: NetHandle): Promise<ConnectionProperties>

Obtains the connection information of the data network specified by **NetHandle**, including the NIC name, domain name, link information, route information, network address, and maximum transmission unit. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Handle of the data network. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ConnectionProperties](#connectionproperties)\> | Promise used to return the network connection information. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }

  connection.getConnectionProperties(netHandle).then((data: connection.ConnectionProperties) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
});

#### connection.getConnectionPropertiesSync10+

getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties

Obtains the connection information of the data network specified by **NetHandle**, including the NIC name, domain name, link information, route information, network address, and maximum transmission unit. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ConnectionProperties](#connectionproperties) | Network connection information. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle: connection.NetHandle;
let connectionproperties: connection.ConnectionProperties;

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  netHandle = connection.getDefaultNetSync();
  connectionproperties = connection.getConnectionPropertiesSync(netHandle);
  console.info("Succeeded to get connectionproperties: " + JSON.stringify(connectionproperties));
});

#### connection.getNetCapabilities

getNetCapabilities(netHandle: NetHandle, callback: AsyncCallback<NetCapabilities>): void

Obtains the network capability set of the data network specified by **NetHandle**, including the uplink and downlink bandwidth, specific network capabilities, and network type. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |
| callback | AsyncCallback<[NetCapabilities](#netcapabilities)\> | Yes | Callback used to return the result. If the capability set of the network specified by **NetHandle** is successfully obtained, **error** is **undefined**, and **data** is the obtained network capability set. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
    if (error) {
      console.error(\`Failed to get net capabilities. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
});

#### connection.getNetCapabilities

getNetCapabilities(netHandle: NetHandle): Promise<NetCapabilities>

Obtains the network capability set of the data network specified by **NetHandle**, including the uplink and downlink bandwidth, specific network capabilities, and network type. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetCapabilities](#netcapabilities)\> | Promise used to return the network capability set. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getNetCapabilities(netHandle).then((data: connection.NetCapabilities) => {
      console.info("Succeeded to get data: " + JSON.stringify(data));
  })
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
});

#### connection.getNetCapabilitiesSync10+

getNetCapabilitiesSync(netHandle: NetHandle): NetCapabilities

Obtains the network capability information of the data network specified by **NetHandle**, including the uplink and downlink bandwidth, specific network capabilities, and network type. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NetCapabilities](#netcapabilities) | Network capability set. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle: connection.NetHandle;
let getNetCapabilitiesSync: connection.NetCapabilities;

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }

  getNetCapabilitiesSync = connection.getNetCapabilitiesSync(netHandle);
  console.info("Succeeded to get net capabilities sync: " + JSON.stringify(getNetCapabilitiesSync));
});

#### connection.isDefaultNetMetered9+

isDefaultNetMetered(callback: AsyncCallback<boolean>): void

Checks whether the data traffic over the current default network is metered. For example, data traffic over Wi-Fi is not metered, whereas that over cellular networks is. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the data traffic over the current network is metered, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.isDefaultNetMetered((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info('data: ' + data);
});

#### connection.isDefaultNetMetered9+

isDefaultNetMetered(): Promise<boolean>

Checks whether the data traffic over the current default network is metered. For example, data traffic over Wi-Fi is not metered, whereas that over cellular networks is. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the data traffic over the current network is metered, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.isDefaultNetMetered().then((data: boolean) => {
  console.info('data: ' + data);
});

#### connection.isDefaultNetMeteredSync10+

isDefaultNetMeteredSync(): boolean

Checks whether the data traffic over the current network is metered. For example, data traffic over Wi-Fi is not metered, whereas that over cellular networks is. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value indicating whether data traffic over the current network is metered. The value **true** indicates that the data traffic is metered, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let isMetered = connection.isDefaultNetMeteredSync();

#### connection.hasDefaultNet

hasDefaultNet(callback: AsyncCallback<boolean>): void

Checks whether there is an available network. This API uses an asynchronous callback to return the result. If there is an available network, [getDefaultNet](#connectiongetdefaultnet) can be used to obtain the default network handle.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return whether there is an available network. The value **true** indicates that a network is available, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.hasDefaultNet((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info('data: ' + data);
});

#### connection.hasDefaultNet

hasDefaultNet(): Promise<boolean>

Checks whether there is an available network. This API uses a promise to return the result. If there is an available network, [getDefaultNet](#connectiongetdefaultnet) can be used to obtain the default network handle.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether there is an available network. The value **true** indicates that a network is available, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.hasDefaultNet().then((data: boolean) => {
  console.info('data: ' + data);
});

#### connection.hasDefaultNetSync10+

hasDefaultNetSync(): boolean

Checks whether there is an available network. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether there is an available network. The value **true** indicates that a network is available, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let hasDefaultNet = connection.hasDefaultNetSync();

#### connection.reportNetConnected

reportNetConnected(netHandle: NetHandle, callback: AsyncCallback<void>): void

Reports the network availability to the network management module. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/-yRfPtMnTTezSoS5n2PKsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=327122504EE369D6A631AF0EFF46566CB5540B265B810452573C581EAA89AC92)

This API is used by the browser to connect to the portal network. After the network authentication is successful, the browser reports the network connection success to the network management module. The network management module then triggers network detection and updates the network status.

**Permission required**: ohos.permission.GET\_NETWORK\_INFO and ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. For details, see [NetHandle](#nethandle). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the network status is reported successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  connection.reportNetConnected(netHandle, (error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
});

#### connection.reportNetConnected

reportNetConnected(netHandle: NetHandle): Promise<void>

Reports that the network is available to the network management module. This API uses a promise to return the result.

**Permission required**: ohos.permission.GET\_NETWORK\_INFO and ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. For details, see [NetHandle](#nethandle). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  connection.reportNetConnected(netHandle).then(() => {
    console.info(\`report success\`);
  });
});

#### connection.reportNetDisconnected

reportNetDisconnected(netHandle: NetHandle, callback: AsyncCallback<void>): void

Reports the network unavailability to the network management module. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.GET\_NETWORK\_INFO and ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. For details, see [NetHandle](#nethandle). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the network status is reported successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.reportNetDisconnected(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(\`Failed to get default net. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("report success");
  });
});

#### connection.reportNetDisconnected

reportNetDisconnected(netHandle: NetHandle): Promise<void>

Reports the network unavailability to the network management module. This API uses a promise to return the result.

**Permission required**: ohos.permission.GET\_NETWORK\_INFO and ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  connection.reportNetDisconnected(netHandle).then( () => {
    console.info(\`report success\`);
  });
});

#### connection.getAddressesByName

getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void

Obtains all IP addresses of the default network by resolving the host name. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Host name to resolve. |
| callback | AsyncCallback<Array<[NetAddress](#netaddress)\>> | Yes | Callback used to return the result. If all IP addresses are successfully obtained, **error** is **undefined**, and **data** is the list of all obtained IP addresses. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress\[\]) => {
  if (error) {
    console.error(\`Failed to get addresses. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

#### connection.getAddressesByName

getAddressesByName(host: string): Promise<Array<NetAddress>>

Obtains all IP addresses of the default network by resolving the host name. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Host name to resolve. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NetAddress](#netaddress)\>> | Promise used to return all IP addresses. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getAddressesByName("xxxx").then((data: connection.NetAddress\[\]) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

#### connection.addCustomDnsRule11+

addCustomDnsRule(host: string, ip: Array<string>, callback: AsyncCallback<void>): void

Adds custom DNS rules for the specified host of the current application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/yKFxtq_RTniMy_sk8C0nbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FE95D2FADC49E01BD9F51F915770F57BBFED6C941A5F67FAE6645591E037C77)

You can call [removeCustomDnsRule](#connectionremovecustomdnsrule11) to delete a custom DNS rule or call [clearCustomDnsRules](#connectionclearcustomdnsrules11) to delete all custom DNS rules of the current application.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Name of the custom host. |
| ip | Array<string> | Yes | List of IP addresses mapped to the host name. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the mapping is added successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.addCustomDnsRule("xxxx", \["xx.xx.xx.xx","xx.xx.xx.xx"\], (error: BusinessError, data: void) => {
  if (error) {
    console.error(\`Failed to get add custom dns rule. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})

#### connection.addCustomDnsRule11+

addCustomDnsRule(host: string, ip: Array<string>): Promise<void>

Adds custom DNS rules for the specified host of the current application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Rzu-V9oFSH2zSOrqs8UgfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23246C7BA1F94F6296AE3536E110A03D42DFE18177E00E8D56A23D68407F9557)

You can call [removeCustomDnsRule](#connectionremovecustomdnsrule11) to delete a custom DNS rule or call [clearCustomDnsRules](#connectionclearcustomdnsrules11) to delete all custom DNS rules of the current application.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Name of the custom host. |
| ip | Array<string> | Yes | List of IP addresses mapped to the host name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.addCustomDnsRule("xxxx", \["xx.xx.xx.xx","xx.xx.xx.xx"\]).then(() => {
    console.info("success");
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
})

#### connection.removeCustomDnsRule11+

removeCustomDnsRule(host: string, callback: AsyncCallback<void>): void

Removes the custom DNS rules of the specified host from the current application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/g1ATWEHmQwCyax7XmN84Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB6EEDA23F488BA3AC7DF18F0CB62C70191F42D737D48CD6044375FABB2D4B4B)

You can call [addCustomDnsRule](#connectionaddcustomdnsrule11) to add a custom rule.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Name of the host for which DNS rules are to be deleted. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the DNS rules are removed successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.removeCustomDnsRule("xxxx", (error: BusinessError, data: void) => {
  if (error) {
    console.error(\`Failed to remove custom dns rule. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})

#### connection.removeCustomDnsRule11+

removeCustomDnsRule(host: string): Promise<void>

Removes the custom DNS rules of the specified host from the current application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Y1So6BYXRMKM5v3i4EYYDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA4B4F4F7BE9571875C8C21844D3DF948201C312F39F5581160BA6A97D5B287B)

You can call [addCustomDnsRule](#connectionaddcustomdnsrule11) to add a custom rule.

**Required permissions**: ohos.permission.INTERNET

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Name of the host for which DNS rules are to be deleted. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.removeCustomDnsRule("xxxx").then(() => {
    console.info("success");
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
})

#### connection.clearCustomDnsRules11+

clearCustomDnsRules(callback: AsyncCallback<void>): void

Removes all custom DNS rules of the current application. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If all the DNS rules are removed successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.clearCustomDnsRules((error: BusinessError, data: void) => {
  if (error) {
    console.error(\`Failed to clear custom dns rules. Code:${error.code}, message:${error.message}\`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})

#### connection.clearCustomDnsRules11+

clearCustomDnsRules(): Promise<void>

Removes all custom DNS rules of the current application. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.clearCustomDnsRules().then(() => {
    console.info("success");
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
})

#### connection.setPacFileUrl20+

setPacFileUrl(pacFileUrl: string): void

Sets the URL of the Proxy Auto-Configuration Script (PAC) and enables the PAC proxy capability, for example, [http://127.0.0.1:21998/PacProxyScript.pac](http://127.0.0.1:21998/PacProxyScript.pac). You can call [findProxyForUrl](#connectionfindproxyforurl20) to parse the URL and obtain the proxy information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ZDPGngrJSZyBPC0Jkdbigw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98BBE50A2CAF405C77A2BC7102EA23B44733AEAF06AAA674CE7E8392536BD943)

1.  Currently, this API can be used to parse scripts and enable the PAC proxy capability only on PCs. For other device types, only the script address is saved and the PAC proxy capability is not enabled.
    
2.  This API does not verify the URL authenticity. After the URL is set on the PC, the PAC proxy is started. If the URL is incorrect, the proxy fails to be started and the error code 2100002 is returned.

**Required permissions**: ohos.permission.SET\_PAC\_URL

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pacFileUrl | string | Yes | URL of the current PAC script. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |

**Example**

import { connection } from '@kit.NetworkKit';

let pacFileUrl = "http://example.com/proxy.pac";
connection.setPacFileUrl(pacFileUrl);

#### connection.getPacFileUrl20+

getPacFileUrl(): string

Obtains the URL of the current PAC script.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the current PAC script. If no PAC script is available, an empty string is returned. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2100002 | Failed to connect to the service. |

**Example**

import { connection } from '@kit.NetworkKit';

let pacFileUrl = connection.getPacFileUrl();
console.info(pacFileUrl);

#### connection.findProxyForUrl20+

findProxyForUrl(url: string): string

Parses the specified URL proxy address based on the configured PAC script and returns the corresponding PAC proxy information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/fw79Ep-SSTatqSh-RyX11Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61F9A1E0722B7C242EB488A93B92790A0D4785D6A2D251BF39E978B4F585EBB2)

1.  You can use [setPacFileUrl](#connectionsetpacfileurl20) or [setPacUrl](#connectionsetpacurl15) to set the PAC script.
    
2.  If no PAC script is set before this interface is called, an empty string is returned.
3.  Currently, the [setPacFileUrl](#connectionsetpacfileurl20) interface can be used to parse scripts and enable the PAC proxy capability only for PCs. Therefore, this interface can be used to obtain PAC proxy information only for PCs. If other devices call this API, the function does not take effect and an empty string is returned.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | URL used to search for the proxy information. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Proxy information. |

**Example**

import { connection } from '@kit.NetworkKit';

let proxyInfo = connection.findProxyForUrl("http://example.com");
console.info(proxyInfo);

#### connection.setPacUrl15+

setPacUrl(pacUrl: string): void

Sets the URL of the system-level Proxy Auto Config (PAC) script.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/jOnlTTyHTEyWpeWaX3y7uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D7C61BD8EA5FE06384AFBAB0D2C9D5F306D950E8463AE81ACD565801B4449C3)

Only the script address can be set. The proxy function cannot be parsed or enabled. To set the script and enable the proxy, call the [setPacFileUrl](#connectionsetpacfileurl20) API.

**Required permissions**: ohos.permission.SET\_PAC\_URL

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pacUrl | string | Yes | URL of the PAC script. Note that this URL will not be verified by the API. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let pacUrl = "xxx";
connection.setPacUrl(pacUrl);

#### connection.getPacUrl15+

getPacUrl(): string

Obtains the URL of the system-level PAC script.

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URL of the PAC script. If the PAC script does not exist, error code 2100003 is reported. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

let pacUrl = connection.getPacUrl();

#### connection.setNetExtAttribute20+

setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise<void>

Sets extended attributes of the network specified by **netHandle** to indicate its security level. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/5ccFfkFlSian_5SvOXwipg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B4D5B91AAA1A75604AD1367F94916B1150C6BC6F633E4001EF2FC4951E22FF6)

Currently, this API is available only for PCs.

**Required permissions**: ohos.permission.SET\_NET\_EXT\_ATTRIBUTE

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |
| netExtAttribute | string | Yes | Extended network attributes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  let netExtAttribute: string = "xxx";
  connection.setNetExtAttribute(netHandle, netExtAttribute).then(() => {
    console.info("setNetExtAttribute success");
  }).catch((error: BusinessError) => {
    console.error("setNetExtAttribute failed, err: " + error.code);
  })
});

#### connection.setNetExtAttributeSync20+

setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void

Sets extended attributes of the network specified by **netHandle** to indicate its security level. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/CZBRbRZTS0Wn50DGo-PAQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CED15E6B9F33EAE02354C05B12FB324078E353621AB933F6925061ABBAD5B9A2)

Currently, this API is available only for PCs.

**Required permissions**: ohos.permission.SET\_NET\_EXT\_ATTRIBUTE

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |
| netExtAttribute | string | Yes | Extended network attributes. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netExtAttribute: string = "xxx";
let netHandle = connection.getDefaultNetSync();
if (netHandle.netId != 0) {
  connection.setNetExtAttributeSync(netHandle, netExtAttribute);
}

#### connection.getNetExtAttribute20+

getNetExtAttribute(netHandle: NetHandle): Promise<string>

Obtains the extended attributes of the network specified by **netHandle** to determine its security level. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the network extension attributes. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getNetExtAttribute(netHandle).then((netExtAttribute: string) => {
    console.info("getNetExtAttribute: " + netExtAttribute);
  }).catch((error: BusinessError) => {
    console.error("getNetExtAttribute failed, err: " + error.code);
  })
});

#### connection.getNetExtAttributeSync20+

getNetExtAttributeSync(netHandle: NetHandle): string

Obtains the extended attributes of the network specified by **netHandle** to determine its security level. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | Yes | Network handle. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Extended network attributes. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle = connection.getDefaultNetSync();
if (netHandle.netId != 0) {
  let netExtAttribute: string = connection.getNetExtAttributeSync(netHandle);
  console.info("getNetExtAttribute: " + netExtAttribute);
}

#### connection.getIpNeighTable22+

getIpNeighTable(): Promise<Array<NetIpMacInfo>>

Obtains information about entries in the IP neighbor table of the local device, including IPv4 and IPv6 entries. Each entry contains an IP address, a MAC address, and a network adapter name. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/O3WpW75zQ4ykgiG1MxGciA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8CB2749FEFC1D157F4007AAEF9F48B2FC8CFC673CD372C45D2778BE5F6C5498)

This interface is used to obtain the cached data of the IP neighbor table, not the data of all connections on the LAN.

This API is used to check network exceptions and parse the mapping between IP addresses and MAC addresses.

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO and ohos.permission.GET\_IP\_MAC\_INFO

**System capability**: SystemCapability.Communication.NetManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NetIpMacInfo](#netipmacinfo22)\>> | Promise used to return information about entries in the IP neighbor table. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getIpNeighTable().then((data: connection.NetIpMacInfo\[\]) => {
  if (data.length !== 0) {
    console.info(\`ipAddress:${data\[0\].ipAddress}\`);
    console.info(\`ifaceName:${data\[0\].iface}\`);
    console.info(\`macAddress:${data\[0\].macAddress}\`);
  }
}).catch((error: BusinessError) => {
  console.error(\`error fetching ip neigh table. Code:${error.code}, message:${error.message}\`);
});

#### NetConnection

Represents the network connection object type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/14ykxQOKQv6CqXRbK5gRxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5951C2B475A29BF8AF4C61D938B5BA1B9A597AAE06C57E3EAFFEA0A38841F8FF)

(1) When the network transitions from unavailable to available, the **netAvailable**, **netCapabilitiesChange**, and **netConnectionPropertiesChange** events are triggered.

(2) If the network transitions from available to unavailable after a **netAvailable** event is received, a **netLost** event is triggered.

(3) If no **netAvailable** event is received, a **netUnavailable** event is directly triggered.

(4) When the network transitions from Wi-Fi to cellular, a **netLost** event is first triggered to indicate that the Wi-Fi network is lost and then a **netAvailable** event is triggered to indicate that the cellular network is available.

#### \[h2\]register

register(callback: AsyncCallback<void>): void

Registers a listener for network status changes. To listen for a specific type of events, call **on** to enable listening and then call **register** to register an event listener.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/NILHdAC7S6C1Neik7Q3Hvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B08F4502CECDC259E5D623C1CE69F6E37274F10C664CF22C2E2AC874F4959A95)

After using the **register** API, you need to call **unregister** to deregister the listener.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If a listener for network status changes is registered successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2101008 | The callback already exists. |
| 2101022 | The number of requests exceeded the maximum allowed. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]unregister

unregister(callback: AsyncCallback<void>): void

Unregisters the listener for network status changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If a listener for network status changes is unregistered successfully, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2101007 | The callback does not exist. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]on('netAvailable')

on(type: 'netAvailable', callback: Callback<NetHandle>): void

Registers a listener for **netAvailable** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **netAvailable**.

**netAvailable**: event indicating that the data network is available.

 |
| callback | Callback<[NetHandle](#nethandle)\> | Yes | Callback used to return the network handle. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netAvailable events.
netCon.on('netAvailable', (data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to unsubscribe from netAvailable events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]on('netBlockStatusChange')

on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void

Registers a listener for **netBlockStatusChange** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **netBlockStatusChange**.

**netBlockStatusChange**: event indicating a change in the network blocking status.

 |
| callback | Callback<[NetBlockStatusInfo](#netblockstatusinfo11)\> | Yes | Callback used to return the result. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netBlockStatusChange events.
netCon.on('netBlockStatusChange', (data: connection.NetBlockStatusInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netBlockStatusChange events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]on('netCapabilitiesChange')

on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void

Registers a listener for **netCapabilitiesChange** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **netCapabilitiesChange**.

**netCapabilitiesChange**: event indicating that the network capabilities have changed.

 |
| callback | Callback<[NetCapabilityInfo](#netcapabilityinfo10)\> | Yes | Callback used to return the network handle (**netHandle**) and capability information (**netCap**). |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netCapChange events.
netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Unsubscribe from netCapabilitiesChange events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]on('netConnectionPropertiesChange')

on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void

Registers a listener for **netConnectionPropertiesChange** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **netConnectionPropertiesChange**.

**netConnectionPropertiesChange**: event indicating that network connection properties have changed.

 |
| callback | Callback<[NetConnectionPropertyInfo](#netconnectionpropertyinfo11)\> | Yes | Callback used to return the result. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netConnectionChange events.
netCon.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netConnectionPropertiesChange events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]on('netLost')

on(type: 'netLost', callback: Callback<NetHandle>): void

Registers a listener for **netLost** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **netLost**.

**netLost**: event indicating that the network is interrupted or normally disconnected.

 |
| callback | Callback<[NetHandle](#nethandle)\> | Yes | Callback used to return the result, which is a **netHandle** object. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netLost events.
netCon.on('netLost', (data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netLost events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### \[h2\]on('netUnavailable')

on(type: 'netUnavailable', callback: Callback<void>): void

Registers a listener for **netUnavailable** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **netUnavailable**.

**netUnavailable**: event indicating that the network is unavailable.

 |
| callback | Callback<void> | Yes | Callback used to return the result, which is empty. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netUnavailable events.
netCon.on('netUnavailable', () => {
  console.info("Succeeded to get unavailable net event");
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netUnavailable events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

#### NetHandle

Represents the network handle.

Before invoking **NetHandle** APIs, call **getNetHandle** to obtain a **NetHandle** object. For example, you can call [getDefaultNet](#connectiongetdefaultnet) to obtain the network handle of the default network.

**System capability**: SystemCapability.Communication.NetManager.Core

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| netId | number | No | No | 
Network ID. The value **0** indicates that there is no default network. The other valid values must be greater than or equal to **100**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### \[h2\]bindSocket9+

bindSocket(socketParam: TCPSocket | UDPSocket, callback: AsyncCallback<void>): void

Binds the TCPSocket or UDPSocket to the network specified by **NetHandle**. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socketParam | [TCPSocket](../ohos-net-socket-socket-connection/document.md#tcpsocket) | [UDPSocket](../ohos-net-socket-socket-connection/document.md#udpsocket) | Yes | **TCPSocket** or **UDPSocket** object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the **TCPSocket** or **UDPSocket** object is successfully bound to the current network, **error** is **undefined**. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection, socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface Data {
  message: ArrayBuffer,
  remoteInfo: socket.SocketRemoteInfo
}

  connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
  }
  let tcp : socket.TCPSocket = socket.constructTCPSocketInstance();
  let udp : socket.UDPSocket = socket.constructUDPSocketInstance();
  let socketType = "TCPSocket";
  if (socketType == "TCPSocket") {
    tcp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: Error) => {
      if (error) {
        console.error('bind fail');
        return;
      }
      netHandle.bindSocket(tcp, (error: BusinessError, data: void) => {
        if (error) {
          console.error(\`Failed to bind socket. Code:${error.code}, message:${error.message}\`);
          return;
        } else {
          console.info(JSON.stringify(data));
        }
      });
    });
  } else {
    let callback: (value: Data) => void = (value: Data) => {
      console.info("on message, message:" + value.message + ", remoteInfo:" + value.remoteInfo);
    };
    udp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: BusinessError) => {
      if (error) {
        console.error(\`Failed to bind. Code:${error.code}, message:${error.message}\`);
        return;
      }
      udp.on('message', (data: Data) => {
        console.info("Succeeded to get data: " + JSON.stringify(data));
      });
      netHandle.bindSocket(udp, (error: BusinessError, data: void) => {
        if (error) {
          console.error(\`Failed to bind socket. Code:${error.code}, message:${error.message}\`);
          return;
        } else {
          console.info(JSON.stringify(data));
        }
      });
    });
  }
})

#### \[h2\]bindSocket9+

bindSocket(socketParam: TCPSocket | UDPSocket): Promise<void>

Binds the TCPSocket or UDPSocket to the network specified by **NetHandle**. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socketParam | [TCPSocket](../ohos-net-socket-socket-connection/document.md#tcpsocket) | [UDPSocket](../ohos-net-socket-socket-connection/document.md#udpsocket) | Yes | **TCPSocket** or **UDPSocket** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection, socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface Data {
  message: ArrayBuffer,
  remoteInfo: socket.SocketRemoteInfo
}

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  let tcp : socket.TCPSocket = socket.constructTCPSocketInstance();
  let udp : socket.UDPSocket = socket.constructUDPSocketInstance();
  let socketType = "TCPSocket";
  if (socketType == "TCPSocket") {
    tcp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: Error) => {
      if (error) {
        console.error('bind fail');
        return;
      }
      netHandle.bindSocket(tcp).then(() => {
        console.info("bind socket success");
      }).catch((error: BusinessError) => {
        console.error(\`Failed to bind socket. Code:${error.code}, message:${error.message}\`);
      });
    });
  } else {
    let callback: (value: Data) => void = (value: Data) => {
      console.info("on message, message:" + value.message + ", remoteInfo:" + value.remoteInfo);
    }
    udp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: BusinessError) => {
      if (error) {
        console.error(\`Failed to bind. Code:${error.code}, message:${error.message}\`);
        return;
      }
      udp.on('message', (data: Data) => {
        console.info("Succeeded to get data: " + JSON.stringify(data));
      });
      netHandle.bindSocket(udp).then(() => {
        console.info("bind socket success");
      }).catch((error: BusinessError) => {
        console.error(\`Failed to bind socket. Code:${error.code}, message:${error.message}\`);
      });
    });
  }
});

#### \[h2\]getAddressesByName

getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void

Obtains all IP addresses by using the network specified by **NetHandle** to resolve the host name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 15.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Host name to resolve. For example, [www.example.com](http://www.example.com). |
| callback | AsyncCallback<Array<[NetAddress](#netaddress)\>> | Yes | Callback used to return the result. If all IP addresses are successfully obtained, **error** is **undefined**, and **data** is the list of all obtained IP addresses. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressesByName(host, (error: BusinessError, data: connection.NetAddress\[\]) => {
    if (error) {
      console.error(\`Failed to get addresses. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

#### \[h2\]getAddressesByName

getAddressesByName(host: string): Promise<Array<NetAddress>>

Obtains all IP addresses by using the network specified by **NetHandle** to resolve the host name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 15.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Host name to resolve. For example, [www.example.com](http://www.example.com). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[NetAddress](#netaddress)\>> | Promise used to return all IP addresses. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressesByName(host).then((data: connection.NetAddress\[\]) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

#### \[h2\]getAddressByName

getAddressByName(host: string, callback: AsyncCallback<NetAddress>): void

Obtains the first IP address by using the network specified by **NetHandle** to resolve the host name. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Host name to resolve. For example, [www.example.com](http://www.example.com). |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | Yes | Callback used to return the result. If the first IP address is obtained successfully, **error** is **undefined**, and **data** is the first obtained IP address. Otherwise, **error** is an error object. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressByName(host, (error: BusinessError, data: connection.NetAddress) => {
    if (error) {
      console.error(\`Failed to get address. Code:${error.code}, message:${error.message}\`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

#### \[h2\]getAddressByName

getAddressByName(host: string): Promise<NetAddress>

Obtains the first IP address by using the network specified by **NetHandle** to resolve the host name. This API uses a promise to return the result.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| host | string | Yes | Host name to resolve. For example, [www.example.com](http://www.example.com). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | Promise used to return the first IP address. |

**Error codes**

For details about the error codes, see [Network Connection Management Error Codes](../../error-codes/network-connection-management-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**Example**

import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressByName(host).then((data: connection.NetAddress) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
});

#### NetCap

Defines the network capability.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NET\_CAPABILITY\_MMS | 0 | 
The network can connect to the carrier's Multimedia Messaging Service Center (MMSC) to send and receive multimedia messages.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NET\_CAPABILITY\_NOT\_METERED | 11 | 

The network traffic is not metered.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NET\_CAPABILITY\_INTERNET | 12 | 

The network is capable of Internet access but the network connectivity is not successfully verified by the network management module. This capability is configured by the network provider. Your application can determine the network connectivity by **NET\_CAPABILITY\_VALIDATED** and **NET\_CAPABILITY\_CHECKING\_CONNECTIVITY**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NET\_CAPABILITY\_NOT\_VPN | 15 | 

The network does not use a virtual private network (VPN).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NET\_CAPABILITY\_VALIDATED | 16 | 

The network management module successfully connects to the Huawei Cloud address through this network. This capability is configured by the network management module.

Note: If the network management module fails to connect to the Huawei Cloud address, this flag is not available in the network capability, but this does not mean a complete loss in Internet access. Note that for a newly connected network, this value may not reflect the actual verification result as network connectivity verification is in progress. Your application can use **NET\_CAPABILITY\_CHECKING\_CONNECTIVITY**12+ to check whether network connectivity verification is in progress.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NET\_CAPABILITY\_PORTAL12+ | 17 | 

The network is found to have a captive portal and user login authentication is required. This capability is set by the connection management module.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NET\_CAPABILITY\_CHECKING\_CONNECTIVITY12+ | 31 | 

The network management module is verifying the network connectivity. This flag remains valid until the network connectivity check is complete. During this period, the value of **NET\_CAPABILITY\_VALIDATED** may be incorrect. After the network connectivity check is complete, this flag is cleared and your application can determine the network connectivity by checking **NET\_CAPABILITY\_VALIDATED**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### NetBearType

Enumerates network types.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BEARER\_CELLULAR | 0 | 
Cellular network.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BEARER\_WIFI | 1 | 

Wi-Fi network.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BEARER\_BLUETOOTH12+ | 2 | 

Bluetooth network.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BEARER\_ETHERNET | 3 | 

Ethernet network.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BEARER\_VPN12+ | 4 | VPN. |

#### HttpProxy10+

Represents the HTTP proxy configuration.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| host | string | No | No | 
Host name of the proxy server.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| port | number | No | No | 

Host port. The value range is \[0, 65535\].

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| exclusionList | Array<string> | No | No | 

List of the names of hosts that do not use a proxy. Host names can be domain names, IP addresses, or wildcards. The detailed matching rules are as follows:

\- Domain name matching:

\- Exact match: The host name of the proxy server exactly matches any host name in the list.

\- Partial match: The host name of the proxy server contains any host name in the list.

For example, if **ample.com** is set in the host name list, **ample.com**, **[www.ample.com](http://www.ample.com)**, and **ample.com:80** are matched, and **[www.example.com](http://www.example.com)** and **ample.com.org** are not matched.

\- IP address matching: The host name of the proxy server exactly matches any IP address in the list.

\- Both the domain name and IP address are added to the list for matching.

\- A single asterisk (\*) is the only valid wildcard. If the list contains only wildcards, the wildcards match all host names; that is, the HTTP proxy is disabled. A wildcard can only be added independently. It cannot be added to the list together with other domain names or IP addresses. Otherwise, the wildcard does not take effect.

\- Host names are case insensitive.

\- Protocol prefixes such as **http** and **https** are ignored during matching.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| username12+ | string | No | Yes | 

Name of the user who uses the proxy.

Note: This parameter takes effect only when the password parameter is set.

 |
| password12+ | string | No | Yes | 

Password of the user who uses the proxy.

Note: The setting takes effect only when the username parameter is set.

 |

#### NetSpecifier

Provides an instance that bears data network capabilities.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| netCapabilities | [NetCapabilities](#netcapabilities) | No | No | Network transmission capabilities and bearer types of the data network. |
| bearerPrivateIdentifier | string | No | Yes | Network identifier. The identifier of the cellular network is **slot0** for SIM card 1 and **slot1** for SIM card 2. Since API version 12, you can pass the registered WLAN hotspot to the API to specify the WLAN network to be activated. |

**Example**

import { connection } from '@kit.NetworkKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let config: wifiManager.WifiDeviceConfig = {
  ssid: "TEST",
  preSharedKey: "\*\*\*\*\*\*\*\*\*\*",
  securityType: wifiManager.WifiSecurityType.WIFI\_SEC\_TYPE\_PSK
};
// Obtain the network ID of the registered WLAN through wifiManager.addCandidateConfig.
wifiManager.addCandidateConfig(config,(error,networkId) => {
 let netConnectionWlan = connection.createNetConnection({
   netCapabilities: {
     bearerTypes: \[connection.NetBearType.BEARER\_WIFI\]
   },
   bearerPrivateIdentifier: \`${networkId}\`
 });
 netConnectionWlan.register((error: BusinessError) => {
   console.error(JSON.stringify(error));
 });
});

#### NetCapabilityInfo10+

Provides an instance that bears data network capabilities.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | No | No | Network handle. |
| netCap | [NetCapabilities](#netcapabilities) | No | No | Network transmission capabilities and bearer types of the data network. |

#### NetCapabilities

Defines the network capability set.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| linkUpBandwidthKbps | number | No | Yes | Uplink (device-to-network) bandwidth, in kbit/s. The value **0** indicates that the current network bandwidth cannot be evaluated. |
| linkDownBandwidthKbps | number | No | Yes | Downlink (network-to-device) bandwidth, in kbit/s. The value **0** indicates that the current network bandwidth cannot be evaluated. |
| networkCap | Array<[NetCap](#netcap)\> | No | Yes | 
Network capability.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bearerTypes | Array<[NetBearType](#netbeartype)\> | No | No | 

Network type. The array contains only one network type.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### NetConnectionPropertyInfo11+

Defines the network connection properties.

**System capability**: SystemCapability.Communication.NetManager.Core

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | No | No | Network handle. |
| connectionProperties | [ConnectionProperties](#connectionproperties) | No | No | Defines the network connection properties. |

#### NetBlockStatusInfo11+

Obtains the network block status information.

**System capability**: SystemCapability.Communication.NetManager.Core

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| netHandle | [NetHandle](#nethandle) | No | No | Network handle. |
| blocked | boolean | No | No | Whether the current network is blocked. The value **true** indicates that the network is congested, and the value **false** indicates the opposite. |

#### ConnectionProperties

Defines the network connection properties.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/bPSjGQk7SsqI3gYZRxtiKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D64A59DB933A369546B89D73B6D4C5A6BEF02E0F7ACF16E410CD5ADE181D3D95)

The values of **linkAddresses**, **routes**, and **dnses** may be empty. You need to protect the empty values. You are advised to check whether the objects exist before using the values.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interfaceName | string | No | No | Network interface card (NIC) name. |
| domains | string | No | No | Domain name. |
| linkAddresses | Array<[LinkAddress](#linkaddress)\> | No | No | Network link information. |
| routes | Array<[RouteInfo](#routeinfo)\> | No | No | Network route information. |
| dnses | Array<[NetAddress](#netaddress)\> | No | No | Network address. For details, see [NetAddress](#netaddress). |
| mtu | number | No | No | Maximum transmission unit (MTU). |

#### RouteInfo

Defines network route information.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interface | string | No | No | NIC name. |
| destination | [LinkAddress](#linkaddress) | No | No | Destination address. |
| gateway | [NetAddress](#netaddress) | No | No | Gateway address. |
| hasGateway | boolean | No | No | Whether a gateway is present. Whether a gateway is available. The value **true** indicates that a gateway is available, and the value **false** indicates the opposite. |
| isDefaultRoute | boolean | No | No | 
Whether the route is the default one. Whether the route is the default route. The value **true** indicates that the route is the default route, and the value **false** indicates the opposite.

Note: The IPv4 default route refers to the route whose destination address is **0.0.0.0/0**. The IPv6 default route refers to the route whose destination address is **::/0**.

 |
| isExcludedRoute20+ | boolean | No | Yes | Whether the route is excluded. The value **true** indicates that the route is excluded, and the value **false** indicates the opposite. |

#### LinkAddress

Defines network link information.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | No | No | Link address. |
| prefixLength | number | No | No | Length of the link address prefix. |

#### NetAddress

Defines a network address.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | string | No | No | Network address. |
| family | number | No | Yes | Address family identifier. The value is **1** for IPv4 and **2** for IPv6. The default value is **1**. |
| port | number | No | Yes | Port number. The value range is \[0, 65535\]. The default value is **0**. |

#### HttpRequest

type HttpRequest = http.HttpRequest

Defines an HTTP request, which can be created using [http.createHttp](../ohos-net-http-data-request/document.md#httpcreatehttp).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| http.HttpRequest | HTTP request task. You need to obtain an HTTP request task before calling **HttpRequest** APIs . |

#### TCPSocket

type TCPSocket = socket.TCPSocket

Defines a TCPSocket object, which can be created using [socket.constructTCPSocketInstance](../ohos-net-socket-socket-connection/document.md#socketconstructtcpsocketinstance).

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| socket.TCPSocket | **TCPSocket** object. |

#### UDPSocket

type UDPSocket = socket.UDPSocket

Defines a **UDPSocket** object, which can be created using [socket.constructUDPSocketInstance](../ohos-net-socket-socket-connection/document.md#socketconstructudpsocketinstance).

**System capability**: SystemCapability.Communication.NetStack

| Type | Description |
| :-- | :-- |
| socket.UDPSocket | **UDPSocket** object. |

#### NetIpMacInfo22+

Defines information about entries in the IP neighbor table.

**System capability**: SystemCapability.Communication.NetManager.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ipAddress | [NetAddress](#netaddress) | No | No | IP address information. |
| iface | string | No | No | NIC name. |
| macAddress | string | No | No | MAC address. |
