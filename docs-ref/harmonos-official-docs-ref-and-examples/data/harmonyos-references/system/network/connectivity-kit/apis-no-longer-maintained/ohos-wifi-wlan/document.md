# @ohos.wifi (WLAN)

The **WLAN** module provides basic wireless local area network (WLAN) functions, peer-to-peer (P2P) functions, and WLAN message notification services. It allows applications to communicate with other devices over WLAN.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wv_Op8KQQJCSlJtni4V9pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86D0BBC966C36004C72A89CF7E01B81DD37F0822A48C44A71BFF11BE0F2704B5)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module are no longer maintained since API version 9. You are advised to use [@ohos.wifiManager (WLAN)](../../arkts-apis/ohos-wifimanager-wlan/document.md).

#### Modules to Import

import wifi from '@ohos.wifi';

#### wifi.isWifiActive(deprecated)

isWifiActive(): boolean

Checks whether WLAN is enabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/1tHHXrP7Tr299TQxq8JfHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5AC418236A890504CD18E8DC83B0BB575726CCD986988F32306C2401EFE2CC5)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.isWifiActive](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageriswifiactive) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if WLAN is enabled; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    let isWifiActive = wifi.isWifiActive();
    console.info("isWifiActive:" + isWifiActive);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.scan(deprecated)

scan(): boolean

Starts a scan for WLAN.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/N6dWrxdoRQqbmyny-j2p5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DDD8EFFBE2A3CF5955FD8B56C0D0DFC3784264EF308F417967971EB27159705)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.scan](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerscandeprecated) instead.

**Required permissions**: **ohos.permission.SET\_WIFI\_INFO** and **ohos.permission.LOCATION**

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    wifi.scan();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.getScanInfos(deprecated)

getScanInfos(): Promise<Array<WifiScanInfo>>

Obtains the scan result. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/9Zgb6D1ZQHSnjScXQfGGlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33C2FA6301DB47D12792F4F466AC8CD1C6CF8A8563B8A3FE12ACAEB950910EFC)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.getScanInfos](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetscaninfolist10) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION or ohos.permission.GET\_WIFI\_PEERS\_MAC (

available only for system applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Promise< Array<[WifiScanInfo](#wifiscaninfodeprecated)\> > | Promise used to return the detected hotspots. |

#### wifi.getScanInfos(deprecated)

getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void

Obtains the scan result. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/9Ls319J6TaCr1lmuvqmRjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=906E34BE66D72B21CB2DCF739D8587A92D92514C6AC26C06A164D7A900C9AA85)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.getScanInfos](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetscaninfolist10) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION or ohos.permission.GET\_WIFI\_PEERS\_MAC (

available only for system applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback< Array<[WifiScanInfo](#wifiscaninfodeprecated)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the detected hotspots. Otherwise, **err** is a non-zero value and **data** is empty. |

**Example**

import wifi from '@ohos.wifi';

wifi.getScanInfos().then(result => {
    let len = result.length;
    console.info("wifi received scan info: " + len);
    for (let i = 0; i < len; ++i) {
        console.info("ssid: " + result\[i\].ssid);
        console.info("bssid: " + result\[i\].bssid);
        console.info("capabilities: " + result\[i\].capabilities);
        console.info("securityType: " + result\[i\].securityType);
        console.info("rssi: " + result\[i\].rssi);
        console.info("band: " + result\[i\].band);
        console.info("frequency: " + result\[i\].frequency);
        console.info("channelWidth: " + result\[i\].channelWidth);
        console.info("timestamp: " + result\[i\].timestamp);
    }
});

#### WifiScanInfo(deprecated)

Represents WLAN hotspot information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/pCS2dj86Qn2qjo9kr6msSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4A3A63F22BFB2D513AF272B39D7344E727D52A7774CB82449FCFF269BB50BB4)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [WifiScanInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifiscaninfo) instead.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | Service set identifier (SSID) of the hotspot, in UTF-8 format. The maximum length is 32 bytes. |
| bssid | string | No | No | Basic service set identifier (BSSID) of the hotspot, for example, **00:11:22:33:44:55**. |
| capabilities | string | No | No | Hotspot capabilities. |
| securityType | [WifiSecurityType](#wifisecuritytypedeprecated) | No | No | WLAN security type. |
| rssi | number | No | No | Received signal strength indicator (RSSI) of the hotspot, in dBm. |
| band | number | No | No | Frequency band of the WLAN access point (AP). The value **1** indicates 2.4 GHz, and the value **2** indicates 5 GHz. |
| frequency | number | No | No | Frequency of the WLAN AP. |
| channelWidth | number | No | No | Channel width of the WLAN AP. |
| timestamp | number | No | No | Timestamp. |

#### WifiSecurityType(deprecated)

Enumerates the WLAN security types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/z0ZAfsiiR2uUEv-jD0rh5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE94B96D032015D12DE4F3D2D46745CF82EC59E87E2C1D7DDB0855C5172D4FAF)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [WifiSecurityType](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifisecuritytype) instead.

**System capability**: SystemCapability.Communication.WiFi.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| WIFI\_SEC\_TYPE\_INVALID | 0 | Invalid security type. |
| WIFI\_SEC\_TYPE\_OPEN | 1 | Open security type. |
| WIFI\_SEC\_TYPE\_WEP | 2 | Wired Equivalent Privacy (WEP). |
| WIFI\_SEC\_TYPE\_PSK | 3 | Pre-shared key (PSK). |
| WIFI\_SEC\_TYPE\_SAE | 4 | Simultaneous Authentication of Equals (SAE). |

#### WifiDeviceConfig(deprecated)

Represents the WLAN configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/2euel-s8Tjqict6MPe3nIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BB11DD5C05A235A211D091222E7E520B0B678348635902B1F4688233D85B6A2)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [WifiDeviceConfig](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifideviceconfig) instead.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | Service set identifier (SSID) of the hotspot, in UTF-8 format. The maximum length is 32 bytes. |
| bssid | string | No | No | BSSID of the hotspot, for example, **00:11:22:33:44:55**. |
| preSharedKey | string | No | No | PSK of the hotspot. The maximum length is 64 bytes. |
| isHiddenSsid | boolean | No | No | Whether the network is hidden. The value **true** indicates that the network is hidden, and the value **false** indicates the opposite. |
| securityType | [WifiSecurityType](#wifisecuritytypedeprecated) | No | No | Security type. |

#### wifi.addUntrustedConfig(deprecated)

addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

Adds the configuration of an untrusted network. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/6as0vAH8Twe7wzxExA38eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08EFAA53D34101FC020A12A116545052967CCE3C79FC4FBA11671E649245F534)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.addCandidateConfig](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageraddcandidateconfig) instead.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | Yes | WLAN configuration to add. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the operation is successful; the value **false** means the opposite. |

**Example**

import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "\*\*\*\*",
        bssid:  "\*\*\*\*",
        preSharedKey: "\*\*\*\*",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "\*\*\*\*",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: \[\],
            domains: \[\]
        }
    }
    wifi.addUntrustedConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.addUntrustedConfig(deprecated)

addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

Adds the configuration of an untrusted network. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/LMGouRZvS-WBVcppYzia1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8128B04ADB45E03C98595CAA19E8B0977DF026FEF7E01E5265B7B8CC3323604)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.addCandidateConfig](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageraddcandidateconfig-1) instead.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | Yes | WLAN configuration to add. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is **true**. If the operation fails, **data** is **false**. If **err** is not **0**, an error has occurred. |

**Example**

import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "\*\*\*\*",
        bssid:  "\*\*\*\*",
        preSharedKey: "\*\*\*\*",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "\*\*\*\*",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: \[\],
            domains: \[\]
        }
    }
    wifi.addUntrustedConfig(config,(error,result) => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.removeUntrustedConfig(deprecated)

removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

Removes the configuration of an untrusted network. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/fqkUCIUsSHCv7ro1CtA5qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E119C6E48AD6C8CD523B8900AB14302E6123A9950AB3B0E5092F564448428E2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.removeCandidateConfig](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerremovecandidateconfig) instead.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | Yes | WLAN configuration to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the operation is successful; the value **false** means the opposite. |

**Example**

import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "\*\*\*\*",
        bssid:  "\*\*\*\*",
        preSharedKey: "\*\*\*\*",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "\*\*\*\*",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: \[\],
            domains: \[\]
        }
    }
    wifi.removeUntrustedConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.removeUntrustedConfig(deprecated)

removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

Removes the configuration of an untrusted network. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/6EszUhavRaW5hT6AzswSiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA3C68807F8A3CA9AB692BBE917BD47CF2372062B901CF7C260E1F7B5BB1A040)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.removeCandidateConfig](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerremovecandidateconfig-1) instead.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | Yes | WLAN configuration to remove. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is **true**. If the operation fails, **data** is **false**. If **err** is not **0**, an error has occurred. |

**Example**

import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "\*\*\*\*",
        bssid:  "\*\*\*\*",
        preSharedKey: "\*\*\*\*",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "\*\*\*\*",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: \[\],
            domains: \[\]
        }
    }
    wifi.removeUntrustedConfig(config,(error,result) => {
    console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.getSignalLevel(deprecated)

getSignalLevel(rssi: number, band: number): number

Obtains the WLAN signal level.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/DBnLSxxtRvCz0I_mIRBU6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E730E208004A3CB1C33469D223DC5F0CC238518C2BF5190036209311DC6B7513)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.getSignalLevel](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetsignallevel) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rssi | number | Yes | RSSI of the hotspot, in dBm. |
| band | number | Yes | Frequency band of the WLAN AP. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Signal level obtained. The value range is \[0, 4\]. |

**Example**

import wifi from '@ohos.wifi';

try {
    let rssi = 0;
    let band = 0;
    let level = wifi.getSignalLevel(rssi,band);
    console.info("level:" + JSON.stringify(level));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.getLinkedInfo(deprecated)

getLinkedInfo(): Promise<WifiLinkedInfo>

Obtains information about the WLAN connection. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/uUdmOGY4R2uDDJS7SrtaSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F329492C647437BEC111D0334FB75F2910450E51A666E6E5211A735C7F0E485F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.getLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetlinkedinfo) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiLinkedInfo](#wifilinkedinfodeprecated)\> | Promise used to return the WLAN connection information. |

#### wifi.getLinkedInfo(deprecated)

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

Obtains information about the WLAN connection. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/t7DTYL68RiWGKP1siYJFyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B75874DCD34B5B5AE05C8780870596210AEFB9EC6FDAB641A6B243509E064FD)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [wifiManager.getLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetlinkedinfo-1) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiLinkedInfo](#wifilinkedinfodeprecated)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the WLAN connection information obtained. If **err** is not **0**, an error has occurred. |

**Example**

import wifi from '@ohos.wifi';

wifi.getLinkedInfo((err, data:wifi.WifiLinkedInfo) => {
    if (err) {
        console.error("get linked info error");
        return;
    }
    console.info("get wifi linked info: " + JSON.stringify(data));
});

wifi.getLinkedInfo().then(data => {
    console.info("get wifi linked info: " + JSON.stringify(data));
}).catch((error:number) => {
    console.info("get linked info error");
});

#### WifiLinkedInfo(deprecated)

Represents the WLAN connection information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/TdPBDrjzQ1WLtpqk9Rx9RQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB1FBF51D96F1A5A9B8F3374A7BC84C1843C1D4C8AF4494C1EBC50F1D51DF423)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [WifiLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifilinkedinfo) instead.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | Service set identifier (SSID) of the hotspot, in UTF-8 format. The maximum length is 32 bytes. |
| bssid | string | No | No | BSSID of the hotspot, for example, **00:11:22:33:44:55**. |
| rssi | number | No | No | Received signal strength indicator (RSSI) of the hotspot, in dBm. |
| band | number | No | No | Frequency band of the WLAN access point (AP). The value **1** indicates 2.4 GHz, and the value **2** indicates 5 GHz. |
| linkSpeed | number | No | No | Speed of the WLAN AP, in Mbit/s. |
| frequency | number | No | No | Frequency of the WLAN AP. |
| isHidden | boolean | No | No | Whether to hide the WLAN AP. The value **true** indicates that the network is hidden, and the value **false** indicates the opposite. |
| isRestricted | boolean | No | No | Whether to restrict data volume at the WLAN AP. The value **true** means to restrict data volume at the WLAN AP, and the value **false** indicates the opposite. |
| macAddress | string | No | No | MAC address of the device. |
| ipAddress | number | No | No | IP address of the device that sets up the WLAN connection. |
| connState | [ConnState](#connstatedeprecated) | No | No | WLAN connection state. |

#### ConnState(deprecated)

Enumerates the WLAN connection states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/MPFKMIikRtiNnYbwM3rmwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A2CE8B567340733BBAD2504DF2ABAB2D78E6AD0A2026A4AE0C2DCA2F7F70FB6)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [WifiLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#connstate) instead.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| SCANNING | 0 | The device is scanning for available APs. |
| CONNECTING | 1 | A WLAN connection is being established. |
| AUTHENTICATING | 2 | An authentication is being performed for a WLAN connection. |
| OBTAINING\_IPADDR | 3 | The IP address of the WLAN connection is being acquired. |
| CONNECTED | 4 | A WLAN connection is established. |
| DISCONNECTING | 5 | The WLAN connection is being disconnected. |
| DISCONNECTED | 6 | The WLAN connection is disconnected. |
| UNKNOWN | 7 | Failed to set up the WLAN connection. |

#### wifi.isConnected(deprecated)

isConnected(): boolean

Checks whether the WLAN is connected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/QmBOGRDjQqGQyKhYbsufWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EB750CF099869C7F095B45956CC2CF2DA43876556B3BCF82D433D78DE250D25)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.isConnected](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerisconnected) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the WLAN is connected; returns **false** otherwise. |

#### wifi.isFeatureSupported(deprecated)

isFeatureSupported(featureId: number): boolean

Checks whether the device supports the specified WLAN feature.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/ujIDtHNbQMK2XUxs1I9AkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8449C8CD88CC7BB474635A2B8EE20F1509E98B2B922B9F5CCF7D68712C7B88D4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.isFeatureSupported](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerisfeaturesupported) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| featureId | number | Yes | Feature ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the feature is supported; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    let featureId = 0;
    let ret = wifi.isFeatureSupported(featureId);
    console.info("isFeatureSupported:" + ret);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.getIpInfo(deprecated)

getIpInfo(): IpInfo

Obtains IP information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/BWs2E1tqQG2EqgxF_hyc5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AB88DF77641D55C58936450EF415F9BD4CA01437F678A5EBC8EB3B8FF7C6EF8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.getIpInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetipinfo) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| [IpInfo](#ipinfodeprecated) | IP information obtained. |

**Example**

import wifi from '@ohos.wifi';

try {
    let info = wifi.getIpInfo();
    console.info("info:" + JSON.stringify(info));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### IpInfo(deprecated)

IP information obtained.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Xm50dxUnTUq-rN1VQBthGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10870ECD5568A4E4110E5D060993D4C315BD08A46E61B402EF8CAFCB8A232B5D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.getIpInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetipinfo) instead.

**System capability**: SystemCapability.Communication.WiFi.AP.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ipAddress | number | No | No | IP address. |
| gateway | number | No | No | Gateway. |
| netmask | number | No | No | Subnet mask. |
| primaryDns | number | No | No | IP address of the preferred DNS server. |
| secondDns | number | No | No | IP address of the alternate DNS server. |
| serverIp | number | No | No | IP address of the DHCP server. |
| leaseDuration | number | No | No | Lease duration of the IP address. |

#### wifi.getCountryCode(deprecated)

getCountryCode(): string

Obtains the country code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3xzNXkf0ReGConvYTF0HiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11DA0628DECDAE07FEBB8E9338E2E121D4BC8917E875BE03244CB1F9874F8B27)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.getCountryCode](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetcountrycode) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Country code obtained. |

**Example**

import wifi from '@ohos.wifi';

try {
    let code = wifi.getCountryCode();
    console.info("code:" + code);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.getP2pLinkedInfo(deprecated)

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

Obtains P2P connection information. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/jHuhj4SLS_qALzw6lEu1iQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90C696994CF1408FC7D10C9B62DAFA42BDAD7F3DE5A61517E776DE94BF857943)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.getP2pLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetp2plinkedinfo) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | Promise used to return the P2P link information. |

#### WifiP2pLinkedInfo(deprecated)

Represents the WLAN connection information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/OuB1oEWRSZyE_pG2NRokbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3F26D1062E7A87F2B51B609C235DC0E55A0ABFE737FDEA43A9BBB231202BD4F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [WifiP2pLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifip2plinkedinfo) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| connectState | [P2pConnectState](#p2pconnectstatedeprecated) | No | No | P2P connection state. |
| isGroupOwner | boolean | No | No | Whether the device is the group owner. The value **true** indicates that the device is the group owner, and the value **false** indicates the opposite. |
| groupOwnerAddr | string | No | No | MAC address of the group. |

#### P2pConnectState(deprecated)

Enumerates the P2P connection states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/gXi0l5IiSTeMHj4-86vadg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7D0336D18C003226FD67A58F1510BFDFC7C7E3D75B2831D0C7AFC11F0B7F9F4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [P2pConnectState](../../arkts-apis/ohos-wifimanager-wlan/document.md#p2pconnectstate) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Value | Description |
| :-- | :-- | :-- |
| DISCONNECTED | 0 | Disconnected. |
| CONNECTED | 1 | Connected. |

#### wifi.getP2pLinkedInfo(deprecated)

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

Obtains P2P connection information. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/LLAm2lpbQHSAML_s7tznLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A80D189E25618610C2B73CA4276EB30F16DC1F5F6D16CD7DF2AE9F1640AC26F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.getP2pLinkedInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetp2plinkedinfo-1) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the P2P link information. If **err** is not **0**, an error has occurred. |

**Example**

import wifi from '@ohos.wifi';

wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
   if (err) {
       console.error("get p2p linked info error");
       return;
   }
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
});

wifi.getP2pLinkedInfo().then(data => {
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
});

#### wifi.getCurrentGroup(deprecated)

getCurrentGroup(): Promise<WifiP2pGroupInfo>

Obtains the current P2P group information. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/p9CLMfqSRlGK9DoaZTpx0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8501C4C09CD4956D9929A184277C7A6E3B7B4BDB550951061C945A58958E013)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.getCurrentGroup](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetcurrentgroup) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pGroupInfo](#wifip2pgroupinfodeprecated)\> | Promise used to return the P2P group information obtained. |

#### wifi.getCurrentGroup(deprecated)

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

Obtains the current P2P group information. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/zW0oOaLtRpmCa9EyyEGv4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB68AA5EFD0EACE53C55A2E68E6A1EDBD69E16F4A5C0668B6B203F5745A54301)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.getCurrentGroup](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetcurrentgroup-1) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pGroupInfo](#wifip2pgroupinfodeprecated)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the group information obtained. If **err** is not **0**, an error has occurred. |

**Example**

import wifi from '@ohos.wifi';

wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
   if (err) {
       console.error("get current P2P group error");
       return;
   }
    console.info("get current P2P group: " + JSON.stringify(data));
});

wifi.getCurrentGroup().then(data => {
    console.info("get current P2P group: " + JSON.stringify(data));
});

#### wifi.getP2pPeerDevices(deprecated)

getP2pPeerDevices(): Promise<WifiP2pDevice\[\]>

Obtains the P2P peer device list. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/BzYv8_StR82ODULxeb3p7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A12BC8007BAE63BD2746B2A03E82D02A265F53BBB0B29605F62EBBF8C5C6F14)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.getP2pPeerDevices](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetp2ppeerdevices) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | Promise used to return the peer device list. |

#### wifi.getP2pPeerDevices(deprecated)

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice\[\]>): void

Obtains the P2P peer device list. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Mv5kG0XnSECX_ckRDX5fog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAAF0283548BAE7D5F659C5DDC7486062CBE73B36669D556F7E7C9D1A405A927)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.getP2pPeerDevices](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagergetp2ppeerdevices-1) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the peer device list obtained. If **err** is not **0**, an error has occurred. |

**Example**

import wifi from '@ohos.wifi';

wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice) => {
   if (err) {
       console.error("get P2P peer devices error");
       return;
   }
    console.info("get P2P peer devices: " + JSON.stringify(data));
});

wifi.getP2pPeerDevices().then(data => {
    console.info("get P2P peer devices: " + JSON.stringify(data));
});

#### WifiP2pDevice(deprecated)

Represents the P2P device information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/eKEOhxVhSkusegHPmM_cWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F73018D2D83D38B65A58296900736D7EB2F26685B0E81E050156DE570AF211A9)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [WifiP2pDevice](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifip2pdevice) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceName | string | No | No | Device name. |
| deviceAddress | string | No | No | MAC address of the device. |
| primaryDeviceType | string | No | No | Type of the primary device. |
| deviceStatus | [P2pDeviceStatus](#p2pdevicestatusdeprecated) | No | No | Device status. |
| groupCapabilitys | number | No | No | Group capabilities. |

#### P2pDeviceStatus(deprecated)

Enumerates the P2P device states.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/HqoQub7aR0Gx7tXpM09bsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8218021C932BB0EE2C819447FB45291C863D329F7E40074667FF9C2CD61CB738)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [P2pDeviceStatus](../../arkts-apis/ohos-wifimanager-wlan/document.md#p2pdevicestatus) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Value | Description |
| :-- | :-- | :-- |
| CONNECTED | 0 | Connected. |
| INVITED | 1 | Invited. |
| FAILED | 2 | Failed. |
| AVAILABLE | 3 | Available. |
| UNAVAILABLE | 4 | Unavailable. |

#### wifi.createGroup(deprecated)

createGroup(config: WifiP2PConfig): boolean

Creates a P2P group.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/DmSv7OnyTnS5FuhT0ddTvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDF1A68668E4EDD1F2E7EE8CACC6D5EF34818FB2C022D66CAA411201986AEA8D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.createGroup](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagercreategroup) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiP2PConfig](#wifip2pconfigdeprecated) | Yes | Group configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiP2PConfig = {
        deviceAddress: "\*\*\*\*",
        netId: 0,
        passphrase: "\*\*\*\*\*",
        groupName: "\*\*\*\*",
        goBand: 0
    }
    wifi.createGroup(config);
    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### WifiP2PConfig(deprecated)

Represents P2P group configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/t3GK7LUDSGaLsVDXVzOFiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D74C0296BD1781C8FE637B81E0781EF87436FE2487E5089E56017B26DC6FB7D3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [WifiP2PConfig](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifip2pconfig) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceAddress | string | No | No | Device address. |
| netId | number | No | No | Network ID. The value **\-1** indicates a temporary group, and **\-2** indicates a persistent group. |
| passphrase | string | No | No | Passphrase of the group. |
| groupName | string | No | No | Group name. |
| goBand | [GroupOwnerBand](#groupownerbanddeprecated) | No | No | Frequency band of the group. |

#### GroupOwnerBand(deprecated)

Enumerates the P2P group frequency bands.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ldKOnGnlTqCvkucdAG8Rsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B9E57BA80B8C2E17B611B55577BCB217AA1F90EFE00765CFFEFF8B972521BFE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [GroupOwnerBand](../../arkts-apis/ohos-wifimanager-wlan/document.md#groupownerband) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Value | Description |
| :-- | :-- | :-- |
| GO\_BAND\_AUTO | 0 | Auto. |
| GO\_BAND\_2GHZ | 1 | 2 GHz. |
| GO\_BAND\_5GHZ | 2 | 5 GHz. |

#### wifi.removeGroup(deprecated)

removeGroup(): boolean

Removes this P2P group.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/i3tCl0SIQQKokHqGa7q4sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BB2A244E5E31653313AD92F87564CB8AC05D25BF59777416349A5950BB50517)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.removeGroup](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerremovegroup) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    wifi.removeGroup();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.p2pConnect(deprecated)

p2pConnect(config: WifiP2PConfig): boolean

Sets up a P2P connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/nL-MAqMXSMmUw1Kaet5FSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A94D6A14D6162337C5B72EA7EB6DB840047EDCBBC9FC176806C5E0489F9BBE56)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.p2pConnect](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerp2pconnect) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiP2PConfig](#wifip2pconfigdeprecated) | Yes | P2P group configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("p2p connection change receive event: " + JSON.stringify(result));
    wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
        if (err) {
            console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
            return;
        }
        console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
    });
}
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
    console.info("p2p device change receive event: " + JSON.stringify(result));
}
wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice\[\]) => {
    console.info("p2p peer device change receive event: " + JSON.stringify(result));
    wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice\[\]) => {
        if (err) {
            console.error('failed to get peer devices: ' + JSON.stringify(err));
            return;
        }
        console.info("get peer devices: " + JSON.stringify(data));
        let len = data.length;
        for (let i = 0; i < len; ++i) {
            if (data\[i\].deviceName === "my\_test\_device") {
                console.info("p2p connect to test device: " + data\[i\].deviceAddress);
                let config:wifi.WifiP2PConfig = {
                    deviceAddress:data\[i\].deviceAddress,
                    netId:-2,
                    passphrase:"",
                    groupName:"",
                    goBand:0,
                }
                wifi.p2pConnect(config);
            }
        }
    });
}
wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

let recvP2pPersistentGroupChangeFunc = () => {
    console.info("p2p persistent group change receive event");

    wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
        if (err) {
            console.error('failed to get current group: ' + JSON.stringify(err));
            return;
        }
        console.info("get current group: " + JSON.stringify(data));
    });
}
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

setTimeout(() => {wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 \* 1000);
setTimeout(() => {wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 \* 1000);
setTimeout(() => {wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 \* 1000);
setTimeout(() => {wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 \* 1000);
console.info("start discover devices -> " + wifi.startDiscoverDevices());

#### wifi.p2pCancelConnect(deprecated)

p2pCancelConnect(): boolean

Cancels this P2P connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/eyacwZmMQBu-rsLoVLxsmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F996BE9ADBA7B2EB1DBAFEA6907E3DBE330EEF81077FA2B8C6F781FAD76AE07)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.p2pCancelConnect](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerp2pcancelconnect) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    wifi.p2pCancelConnect();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.startDiscoverDevices(deprecated)

startDiscoverDevices(): boolean

Starts to discover devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/KT8X6asaS12ci8OKvSv8oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9957008A30B47FCF2DFBE8BBB778DAA00346AEC02DBD915E78A6E708DCD78F99)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.startDiscoverDevices](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerstartdiscoverdevices) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    wifi.startDiscoverDevices();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### wifi.stopDiscoverDevices(deprecated)

stopDiscoverDevices(): boolean

Stops discovering devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/XHkIEQC1TlGGiwdtG6Febw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DBA05EE9FF4282A9B3328ECA565588F83BB87524BD97A17CCA78BDA810C76DF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.stopDiscoverDevices](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanagerstopdiscoverdevices) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the operation is successful; **false** otherwise. |

**Example**

import wifi from '@ohos.wifi';

try {
    wifi.stopDiscoverDevices();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}

#### WifiP2pGroupInfo(deprecated)

Represents the P2P group information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/V4bGPJ-TShq6-OKbxJN1ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79331AF1AE8EAF2067E4F2CF53FB4D2415EC70EC798510777393FC8CDDCD2990)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [WifiP2pGroupInfo](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifip2pgroupinfo) instead.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isP2pGo | boolean | No | No | Whether the device is the group owner. The value **true** indicates that the device is the group owner, and the value **false** indicates the opposite. |
| ownerInfo | [WifiP2pDevice](#wifip2pdevicedeprecated) | No | No | Device information of the group. |
| passphrase | string | No | No | Passphrase of the group. |
| interface | string | No | No | Interface name. |
| groupName | string | No | No | Group name. |
| networkId | number | No | No | Network ID. |
| frequency | number | No | No | Frequency of the group. |
| clientDevices | [WifiP2pDevice\[\]](#wifip2pdevicedeprecated) | No | No | List of connected devices. |
| goIpAddress | string | No | No | IP address of the group. |

#### wifi.on('wifiStateChange')(deprecated)

on(type: 'wifiStateChange', callback: Callback<number>): void

Subscribes to WLAN state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/mW-bP0hpQzCXtcRuLmZO9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19D5CB74A9BB5BCE1F98FD4EC3175427FA9AB09CD6845341C4A7B8902E377C50)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronwifistatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiStateChange**. |
| callback | Callback<number> | Yes | Callback used to return the WLAN state. |

**WLAN states**

| Value | Description |
| :-- | :-- |
| 0 | Deactivated |
| 1 | Activated |
| 2 | Activating |
| 3 | Deactivating |

#### wifi.off('wifiStateChange')(deprecated)

off(type: 'wifiStateChange', callback?: Callback<number>): void

Unsubscribes from WLAN state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/-7XHXioZTBymJbke4rM19g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=639420EBEF0D1DC7F58F3EAB02CF192440025EFFE2D35B04D13C51FFA073CBED)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffwifistatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvPowerNotifyFunc = (result:number) => {
    console.info("Receive power state change event: " + result);
}

// Register an event.
wifi.on("wifiStateChange", recvPowerNotifyFunc);

// Unregister an event.
wifi.off("wifiStateChange", recvPowerNotifyFunc);

#### wifi.on('wifiConnectionChange')(deprecated)

on(type: 'wifiConnectionChange', callback: Callback<number>): void

Subscribes to WLAN connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/ifwd5cuYQB2B_PbPV32gzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=717EF356503697C736BC60D572F3F1D78491D7A958801498350E49B5C1E84DDC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronwificonnectionchange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiConnectionChange**. |
| callback | Callback<number> | Yes | Callback used to return the WLAN connection state. |

**WLAN connection states**

| Value | Description |
| :-- | :-- |
| 0 | Disconnected. |
| 1 | Connected. |

#### wifi.off('wifiConnectionChange')(deprecated)

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

Unsubscribes from WLAN connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_Eeqf8VbRN2imsNIerZdBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC5CCCBD6328D435E14A34221ED63B76D34A1B01F07C287CB49DFF6D09C447BD)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffwificonnectionchange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiConnectionChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvWifiConnectionChangeFunc = (result:number) => {
    console.info("Receive wifi connection change event: " + result);
}

// Register an event.
wifi.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

// Unregister an event.
wifi.off("wifiConnectionChange", recvWifiConnectionChangeFunc);

#### wifi.on('wifiScanStateChange')(deprecated)

on(type: 'wifiScanStateChange', callback: Callback<number>): void

Subscribes to WLAN scan state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/LIWvrhvDTVyKV6V_RGVsdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC52291C840140469C44B24A2748EE4D2A5FED98E76F0964BF990352AF20460E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronwifiscanstatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiScanStateChange**. |
| callback | Callback<number> | Yes | Callback used to return the WLAN scan state. |

**WLAN scan states**

| Value | Description |
| :-- | :-- |
| 0 | Scan failed. |
| 1 | Scan successful. |

#### wifi.off('wifiScanStateChange')(deprecated)

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

Unsubscribes from WLAN scan state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/QTpzobeURD2Q5WbTntnCRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17D8257B77314BC24328204543B816669BFE025471CAF375D55E0FDDF671EAFE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffwifiscanstatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiScanStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvWifiScanStateChangeFunc = (result:number) => {
    console.info("Receive Wifi scan state change event: " + result);
}

// Register an event.
wifi.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

// Unregister an event.
wifi.off("wifiScanStateChange", recvWifiScanStateChangeFunc);

#### wifi.on('wifiRssiChange')(deprecated)

on(type: 'wifiRssiChange', callback: Callback<number>): void

Subscribes to RSSI changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/QWyfjN9EQEyTRffBhbUlQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19A47679A99D2447EDDEE0AF307275002BA37178BC02D664B6B7DB4C72384C9B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronwifirssichange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiRssiChange**. |
| callback | Callback<number> | Yes | Callback used to return the RSSI, in dBm. |

#### wifi.off('wifiRssiChange')(deprecated)

off(type: 'wifiRssiChange', callback?: Callback<number>): void

Unsubscribes from RSSI changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/NxN9h9GwQV-bm5mRm09nZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5CA24EB2EF66813B2DD14120865F83CA939363D9DD7E3350DEAA1CB45B3DA3B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffwifirssichange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiRssiChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvWifiRssiChangeFunc = (result:number) => {
    console.info("Receive wifi rssi change event: " + result);
}

// Register an event.
wifi.on("wifiRssiChange", recvWifiRssiChangeFunc);

// Unregister an event.
wifi.off("wifiRssiChange", recvWifiRssiChangeFunc);

#### wifi.on('hotspotStateChange')(deprecated)

on(type: 'hotspotStateChange', callback: Callback<number>): void

Subscribes to hotspot state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/xDyYb7WYQr2VmGJWf1Jgrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2938FB7784265806B026F8110F59420009CAB75DBB90873D56FA33553FB1951)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronhotspotstatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **hotspotStateChange**. |
| callback | Callback<number> | Yes | Callback used to return the hotspot state. |

**Hotspot states**

| Value | Description |
| :-- | :-- |
| 0 | Deactivated |
| 1 | Activated |
| 2 | Activating |
| 3 | Deactivating |

**Example**

import wifi from '@ohos.wifi';

let recvHotspotStateChangeFunc = (result:number) => {
    console.info("Receive hotspot state change event: " + result);
}

// Register an event.
wifi.on("hotspotStateChange", recvHotspotStateChangeFunc);

// Unregister an event.
wifi.off("hotspotStateChange", recvHotspotStateChangeFunc);

#### wifi.off('hotspotStateChange')(deprecated)

off(type: 'hotspotStateChange', callback?: Callback<number>): void

Unsubscribes from hotspot state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Gh7jRuirRmK-_LQThutW0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=549CD7429BB2D96813D4B6E17C0C9CE61B65465C015297E86DAE8FA7A17CE72B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffhotspotstatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **hotspotStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

#### wifi.on('p2pStateChange')(deprecated)

on(type: 'p2pStateChange', callback: Callback<number>): void

Subscribes to P2P state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Dbn0mcxSQjqXmp80m20tlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F377D8C636A8417E45086603CD2548965588E8F7B7ED53B6D719FE5B351D1221)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronp2pstatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pStateChange**. |
| callback | Callback<number> | Yes | Callback used to return the P2P state. |

**P2P states**

| Value | Description |
| :-- | :-- |
| 1 | Available |
| 2 | Opening |
| 3 | Opened |
| 4 | Closing |
| 5 | Closed |

#### wifi.off('p2pStateChange')(deprecated)

off(type: 'p2pStateChange', callback?: Callback<number>): void

Unsubscribes from P2P state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/WerZTj6wTSSyhTGK9RfAVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFAFEBDB4F93272AB0E3FDF91142669DE9951FD0CCAA994975C812D726EF7CB8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffp2pstatechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pStateChangeFunc = (result:number) => {
    console.info("Receive p2p state change event: " + result);
}

// Register an event.
wifi.on("p2pStateChange", recvP2pStateChangeFunc);

// Unregister an event.
wifi.off("p2pStateChange", recvP2pStateChangeFunc);

#### wifi.on('p2pConnectionChange')(deprecated)

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

Subscribes to P2P connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/vtrTO-pmRdyyUXsdhrlG_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0335B41D516E2960E36DD92EB26927D8A66F2042B0B66F3EFAC63C45E32F1ACD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronp2pconnectionchange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pConnectionChange**. |
| callback | Callback<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | Yes | Callback used to return the P2P connection state. |

#### wifi.off('p2pConnectionChange')(deprecated)

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

Unsubscribes from P2P connection state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/x4vg6uyxSp-ZSN6zbEFKUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E67FB5213A1379C430CAED79598D77831256A80DE36B6FE217923DDD7E4256A4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffp2pconnectionchange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pConnectionChange**. |
| callback | Callback<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("Receive p2p connection change event: " + result);
}

// Register an event.
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

// Unregister an event.
wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);

#### wifi.on('p2pDeviceChange')(deprecated)

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

Subscribes to P2P device state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/yreiXtvTSlCYBNGAiCX9JA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBF61165C5374C0405A8F842004646D7CE6F532F1C59A21CAF70F2287BEB77EC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronp2pdevicechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDeviceChange**. |
| callback | Callback<[WifiP2pDevice](#wifip2pdevicedeprecated)\> | Yes | Callback used to return the P2P device state. |

#### wifi.off('p2pDeviceChange')(deprecated)

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

Unsubscribes from P2P device state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/zW_JtqjZTuqfIxG0eBUbhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83EBB96735BF83840ADF9CDD63B26DBFC3505C7C688428F0329F076485F36352)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffp2pdevicechange) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDeviceChange**. |
| callback | Callback<[WifiP2pDevice](#wifip2pdevicedeprecated)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
    console.info("Receive p2p device change event: " + result);
}

// Register an event.
wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

// Unregister an event.
wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);

#### wifi.on('p2pPeerDeviceChange')(deprecated)

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice\[\]>): void

Subscribes to P2P peer device state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/9pCB3rzQS92A9nqz1KsxcA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10156D6F06B4E1A35A905459F0754FFD1A772862CF6CA62079D9CE4B5F3B2BB7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronp2ppeerdevicechange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPeerDeviceChange**. |
| callback | Callback<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | Yes | Callback used to return the P2P peer device state. |

#### wifi.off('p2pPeerDeviceChange')(deprecated)

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice\[\]>): void

Unsubscribes from P2P peer device state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/SWfb_ASkS6quNAuBofO3Xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49F2080A4118992B4F03C29C1BD4A85D037F21B6C8808F1783B630BC8297A575)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffp2ppeerdevicechange) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPeerDeviceChange**. |
| callback | Callback<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice\[\]) => {
    console.info("Receive p2p peer device change event: " + result);
}

// Register an event.
wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

// Unregister an event.
wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

#### wifi.on('p2pPersistentGroupChange')(deprecated)

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

Subscribes to P2P persistent group state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/o72oVgduR7Olc8-2bSIw0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87FBBDA84CB68691275037BE2C6AF79DC018E5FD9C8889C88AB89AC734CE3658)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronp2ppersistentgroupchange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPersistentGroupChange**. |
| callback | Callback<void> | Yes | Callback used to return the P2P persistent group state. |

#### wifi.off('p2pPersistentGroupChange')(deprecated)

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

Unsubscribes from P2P persistent group state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/glD6GNNkQgSHuKl1ot3qXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04026D13F060086DC0400A9EE3E54EF2A85183E73DC91FAA551BAC302C25A9E3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffp2ppersistentgroupchange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPersistentGroupChange**. |
| callback | Callback<void> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pPersistentGroupChangeFunc = (result:void) => {
    console.info("Receive p2p persistent group change event: " + result);
}

// Register an event.
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

// Unregister an event.
wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

#### wifi.on('p2pDiscoveryChange')(deprecated)

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

Subscribes to P2P device discovery state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Qu91jKQITOinOEwc6hNlFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06490B3733707ED7DAB753659AB044CA7B760DAB219C4FC0F0479002D8C4B538)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.on](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageronp2pdiscoverychange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDiscoveryChange**. |
| callback | Callback<number> | Yes | Callback used to return the P2P device discovery state. |

**P2P discovered device states**

| Value | Description |
| :-- | :-- |
| 0 | Initial state. |
| 1 | Discovered. |

#### wifi.off('p2pDiscoveryChange')(deprecated)

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

Unsubscribes from P2P device discovery state changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/IE3K5GrKS3ySiMOHMUcXxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75289305D8ADC46B3E0BC79CB834C6FA57E972AE54043BACD61A7D7BCF9F637C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManager.off](../../arkts-apis/ohos-wifimanager-wlan/document.md#wifimanageroffp2pdiscoverychange) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDiscoveryChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified event will be unregistered. |

**Example**

import wifi from '@ohos.wifi';

let recvP2pDiscoveryChangeFunc = (result:number) => {
    console.info("Receive p2p discovery change event: " + result);
}

// Register an event.
wifi.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

// Unregister an event.
wifi.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
