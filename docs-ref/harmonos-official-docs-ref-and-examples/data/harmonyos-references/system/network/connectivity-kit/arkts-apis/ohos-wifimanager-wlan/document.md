# @ohos.wifiManager (WLAN)

The **wifiManager** module provides basic WLAN functionalities (such as wireless access, wireless encryption, and wireless roaming), basic peer-to-peer (P2P) services, and WLAN notification services. It allows applications to interact with other devices through WLAN.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/McUPeOAwT2esPel8dcw46A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF7BD209284D240FDEDD49B3A619E0B268AA9F27F7B7674EB0390E471AA8026B)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { wifiManager } from '@kit.ConnectivityKit';

#### wifiManager.isWifiActive

isWifiActive(): boolean

Checks whether WLAN is enabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if WLAN is enabled; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let isWifiActive = wifiManager.isWifiActive();
    console.info("isWifiActive:" + isWifiActive);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.enableWifi15+

enableWifi(): void

Enables the WLAN.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO and ohos.permission.MANAGE\_WIFI\_CONNECTION (available only to system applications) or ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION (available only to enterprise applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501003 | Operation failed because the service is being closed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    wifiManager.enableWifi();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.disableWifi20+

disableWifi(): void

Disables WLAN.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO and ohos.permission.MANAGE\_WIFI\_CONNECTION (available only to system applications) or ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION (available only to enterprise applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501004 | Operation failed because the service is being opened. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.disableWifi();
  }catch(error){
    console.error(\`disableWifi failed. ${error.message}\`);
  }

#### wifiManager.scan(deprecated)

scan(): void

Starts WLAN scanning. Note that WLAN must have been enabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/yahKiRyFTU6z9Y7NbS9a1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5C24F904D4323E5D890EBD0706A46782DCD2BB16E1E15ECB1AAF1E35D7586F8)

This API is supported since API version 9 and deprecated since API version 10. Use [wifiManager.startScan](#wifimanagerstartscan21) instead.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO, ohos.permission.LOCATION, and ohos.permission.APPROXIMATELY\_LOCATION

**System capability**: SystemCapability.Communication.WiFi.STA

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.scan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.startScan21+

startScan(): void

Starts a WLAN scan.

-   At most four scans can be initiated within 2 minutes while the application is running in the foreground.
-   At most one scan can be initiated within 30 minutes while the application is running in the background.
-   You can subscribe to the scan status change event by calling [on('wifiScanStateChange')](#wifimanageronwifiscanstatechange) to listen for scan completion notifications.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startScan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.getScanResults(deprecated)

getScanResults(): Promise<Array<WifiScanInfo>>

Obtains the scan result. This API uses a promise to return the result.

-   Returns a promise. The resolved value is an array containing multiple WifiScanInfo objects, each of which indicates the scanning information about a WLAN.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/r5TrA5SDREKFNhdm5ccNLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F2F9E1F76DC593F34878707B8F0CC7F56AF242142A0E2ABC0B2B0A644ACF540)

This API is supported since API version 9 and deprecated since API version 10. Use [wifiManager.getScanInfoList](#wifimanagergetscaninfolist10) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION))

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Promise< Array<[WifiScanInfo](#wifiscaninfo)\> > | Promise used to return the hotspots detected. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

#### wifiManager.getScanResults(deprecated)

getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void

Obtains the scan result. This API uses an asynchronous callback to return the result.

-   Returns an array containing multiple WifiScanInfo objects through the callback function. Each object indicates the scanning information about a WLAN network.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/jhRaRhlrSx2hON_1gRQvNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D3FE75722E44E29375A165E46BA7C71BA968C7ED20DFFF4892EC1149D97368E)

This API is supported since API version 9 and deprecated since API version 10. Use [wifiManager.getScanInfoList](#wifimanagergetscaninfolist10) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION))

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback< Array<[WifiScanInfo](#wifiscaninfo)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the detected hotspots. Otherwise, **err** is a non-zero value and **data** is empty. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  wifiManager.getScanResults((err, result) => {
      if (err) {
          console.error("get scan info error");
          return;
      }
  
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
  
  wifiManager.getScanResults().then(result => {
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
  }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
  });

#### wifiManager.getScanResultsSync(deprecated)

getScanResultsSync(): Array<[WifiScanInfo](#wifiscaninfo)\>

Obtains the scanning result. This API returns an array containing multiple WifiScanInfo objects in synchronous mode. Each object indicates the scanning information about a WLAN network.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/XDMyzNRzTbS8h4hWltSkDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC670E57FF7C791DF81E89ACBC0EC8CBA283CD4A7A5DEED10C31D568231AF00B)

This API is supported since API version 9 and deprecated since API version 10. Use [wifiManager.getScanInfoList](#wifimanagergetscaninfolist10) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION))

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiScanInfo](#wifiscaninfo)\> | Scan result obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let scanInfoList = wifiManager.getScanResultsSync();
    console.info("scanInfoList:" + JSON.stringify(scanInfoList));
    let len = scanInfoList.length;
        console.info("wifi received scan info: " + len);
    if(len > 0){
      for (let i = 0; i < len; ++i) {
        console.info("ssid: " + scanInfoList\[i\].ssid);
        console.info("bssid: " + scanInfoList\[i\].bssid);
        console.info("capabilities: " + scanInfoList\[i\].capabilities);
        console.info("securityType: " + scanInfoList\[i\].securityType);
        console.info("rssi: " + scanInfoList\[i\].rssi);
        console.info("band: " + scanInfoList\[i\].band);
        console.info("frequency: " + scanInfoList\[i\].frequency);
        console.info("channelWidth: " + scanInfoList\[i\].channelWidth);
        console.info("timestamp: " + scanInfoList\[i\].timestamp);
      }
    }
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
  

#### wifiManager.getScanInfoList10+

getScanInfoList(): Array<WifiScanInfo>

Obtains the cached scan results within 30s before the current time point.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiScanInfo](#wifiscaninfo)\> | Hotspots detected. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **bssid** in the return value is a real device address; otherwise, **bssid** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let scanInfoList = wifiManager.getScanInfoList();
    console.info("scanInfoList:" + JSON.stringify(scanInfoList));
    let len = scanInfoList.length;
        console.info("wifi received scan info: " + len);
    if(len > 0){
      for (let i = 0; i < len; ++i) {
        console.info("ssid: " + scanInfoList\[i\].ssid);
        console.info("bssid: " + scanInfoList\[i\].bssid);
        console.info("capabilities: " + scanInfoList\[i\].capabilities);
        console.info("securityType: " + scanInfoList\[i\].securityType);
        console.info("rssi: " + scanInfoList\[i\].rssi);
        console.info("band: " + scanInfoList\[i\].band);
        console.info("frequency: " + scanInfoList\[i\].frequency);
        console.info("channelWidth: " + scanInfoList\[i\].channelWidth);
        console.info("timestamp: " + scanInfoList\[i\].timestamp);
        console.info("supportedWifiCategory: " + scanInfoList\[i\].supportedWifiCategory);
        console.info("isHiLinkNetwork: " + scanInfoList\[i\].isHiLinkNetwork);
      }
    }
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
  

#### WifiScanInfo

Represents WLAN hotspot information.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | 
Service set identifier (SSID) of the hotspot, in UTF-8 format. The maximum length is 32 bytes.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bssid | string | No | No | 

Basic service set identifier (BSSID) of the hotspot, for example, **00:11:22:33:44:55**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bssidType10+ | [DeviceAddressType](#deviceaddresstype10) | No | No | 

BSSID type of the hotspot.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| capabilities | string | No | No | Hotspot capabilities. |
| securityType | [WifiSecurityType](#wifisecuritytype) | No | No | 

WLAN security type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| rssi | number | No | No | 

Received signal strength indicator (RSSI) of the hotspot, in dBm.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| band | number | No | No | Frequency band of the WLAN access point (AP). The value **1** indicates 2.4 GHz, and the value **2** indicates 5 GHz. |
| frequency | number | No | No | 

Frequency of the WLAN AP.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| channelWidth | number | No | No | Channel width of the WLAN AP. For details, see [WifiChannelWidth](#wifichannelwidth). |
| centerFrequency0 | number | No | No | Center frequency of the hotspot. |
| centerFrequency1 | number | No | No | Center frequency of the hotspot. If the hotspot uses two non-overlapping WLAN channels, two center frequencies, namely **centerFrequency0** and **centerFrequency1**, are returned. |
| infoElems | Array<[WifiInfoElem](#wifiinfoelem)\> | No | No | Information elements. |
| timestamp | number | No | No | Timestamp. |
| supportedWifiCategory12+ | [WifiCategory](#wificategory12) | No | No | Highest Wi-Fi category supported by the hotspot. |
| isHiLinkNetwork12+ | boolean | No | No | Whether HiLink is supported by the hotspot. The value **true** indicates that HiLink is supported, and the value **false** indicates the opposite. |

#### DeviceAddressType10+

Enumerates the WLAN device address (MAC/BSSID) types. It is the unique address of a WLAN device or access point.

Parameters of the DeviceAddressType type are required for WLAN-related operations, such as connecting to a specified WLAN network and obtaining device information.

**System capability**: SystemCapability.Communication.WiFi.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| RANDOM\_DEVICE\_ADDRESS | 0 | Random device address. |
| REAL\_DEVICE\_ADDRESS | 1 | Real device address. |

#### WifiSecurityType

Enumerates the WLAN security types.

**System capability**: SystemCapability.Communication.WiFi.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| WIFI\_SEC\_TYPE\_INVALID | 0 | Invalid security type. |
| WIFI\_SEC\_TYPE\_OPEN | 1 | 
Open security type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| WIFI\_SEC\_TYPE\_WEP | 2 | Wired Equivalent Privacy (WEP). This type is not supported for the candidate network configuration added by **addCandidateConfig**. |
| WIFI\_SEC\_TYPE\_PSK | 3 | Pre-shared key (PSK). |
| WIFI\_SEC\_TYPE\_SAE | 4 | Simultaneous Authentication of Equals (SAE). |
| WIFI\_SEC\_TYPE\_EAP | 5 | Extensible Authentication Protocol (EAP). |
| WIFI\_SEC\_TYPE\_EAP\_SUITE\_B | 6 | Suite B 192-bit encryption. |
| WIFI\_SEC\_TYPE\_OWE | 7 | Opportunistic Wireless Encryption (OWE). |
| WIFI\_SEC\_TYPE\_WAPI\_CERT | 8 | WLAN Authentication and Privacy Infrastructure (WAPI) in certificate-based mode (WAPI-CERT). |
| WIFI\_SEC\_TYPE\_WAPI\_PSK | 9 | WAPI-PSK. |

#### WifiBandType10+

Enumerates the Wi-Fi band types.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| WIFI\_BAND\_NONE | 0 | Invalid band type |
| WIFI\_BAND\_2G | 1 | 2.4 GHz |
| WIFI\_BAND\_5G | 2 | 5 GHz |
| WIFI\_BAND\_6G | 3 | 6 GHz |
| WIFI\_BAND\_60G | 4 | 60 GHz |

#### WifiStandard10+

Enumerates the Wi-Fi standards.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| WIFI\_STANDARD\_UNDEFINED | 0 | Invalid Wi-Fi standard |
| WIFI\_STANDARD\_11A | 1 | 802.11a |
| WIFI\_STANDARD\_11B | 2 | 802.11b |
| WIFI\_STANDARD\_11G | 3 | 802.11g |
| WIFI\_STANDARD\_11N | 4 | 802.11n |
| WIFI\_STANDARD\_11AC | 5 | 802.11ac |
| WIFI\_STANDARD\_11AX | 6 | 802.11ax |
| WIFI\_STANDARD\_11AD | 7 | 802.11ad |

#### WifiInfoElem

Represents WLAN hotspot information.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eid | number | No | No | ID of the information element. |
| content | Uint8Array | No | No | Content of the information element. |

#### WifiChannelWidth

Enumerates the WLAN channel widths.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| WIDTH\_20MHZ | 0 | 20 MHz |
| WIDTH\_40MHZ | 1 | 40 MHz |
| WIDTH\_80MHZ | 2 | 80 MHz |
| WIDTH\_160MHZ | 3 | 160 MHz |
| WIDTH\_80MHZ\_PLUS | 4 | 80 MHz+ |
| WIDTH\_INVALID | 5 | Invalid value |

#### WifiDeviceConfig

Represents WLAN configuration.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | 
Service set identifier (SSID) of the hotspot, in UTF-8 format. The maximum length is 32 bytes.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bssid | string | No | Yes | 

Basic service set identifier (BSSID) of the hotspot, for example, **00:11:22:33:44:55**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bssidType10+ | [DeviceAddressType](#deviceaddresstype10) | No | Yes | 

BSSID type of the hotspot.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| preSharedKey | string | No | No | 

PSK of the hotspot, which cannot exceed 64 bytes.

When **securityType** is **WIFI\_SEC\_TYPE\_OPEN**, this parameter must be an empty string. When **securityType** is any other value, this parameter cannot be empty.

When **securityType** is **WIFI\_SEC\_TYPE\_WEP**, the PSK must be of 5, 10, 13, 26, 16, or 32 bytes. If the PSK length is 10, 26, 16, or 32 bytes, the PSK must be a hexadecimal number.

When **securityType** is **WIFI\_SEC\_TYPE\_SAE**, the minimum PSK length is 1 byte.

When **securityType** is **WIFI\_SEC\_TYPE\_PSK**, the minimum PSK length is 8 bytes.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isHiddenSsid | boolean | No | Yes | Whether the network is hidden. The value **true** indicates that the network is hidden; the value **false** indicates the opposite. |
| netId22+ | number | No | Yes | Network ID allocated. |
| securityType | [WifiSecurityType](#wifisecuritytype) | No | No | 

Security type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| eapConfig10+ | [WifiEapConfig](#wifieapconfig10) | No | Yes | EAP configuration. This parameter is mandatory only when **securityType** is **WIFI\_SEC\_TYPE\_EAP**. |
| wapiConfig12+ | [WifiWapiConfig](#wifiwapiconfig12) | No | Yes | WAPI configuration. This parameter is mandatory only when **securityType** is **WIFI\_SEC\_TYPE\_WAPI\_CERT** or\*\* WIFI\_SEC\_TYPE\_WAPI\_PSK\*\*. |

#### WifiEapConfig10+

Represents EAP configuration information.

-   WifiEapConfig is a class used to configure the EAP authentication type of the WLAN network.
-   Includes the EAP authentication mode, second-phase authentication mode, identity information, password, and certificate.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eapMethod | [EapMethod](#eapmethod10) | No | No | EAP authentication method. |
| phase2Method | [Phase2Method](#phase2method10) | No | No | Phase 2 authentication method. This parameter is mandatory only when **eapMethod** is **EAP\_PEAP** or **EAP\_TTLS**. |
| identity | string | No | No | Identity Information. When **eapMethod** is **EAP\_PEAP**, **EAP\_TLS**, or **EAP\_PWD**, this parameter cannot be empty. |
| anonymousIdentity | string | No | No | Anonymous identity. This parameter is not used currently. |
| password | string | No | No | Password. When **eapMethod** is **EAP\_PEAP** or **EAP\_PWD**, this parameter cannot be empty. The value contains a maximum of 128 bytes. |
| caCertAlias | string | No | No | CA certificate alias. |
| caPath | string | No | No | CA certificate path. |
| clientCertAlias | string | No | No | Client certificate alias. |
| certEntry | Uint8Array | No | No | CA certificate content. If **eapMethod** is **EAP\_TLS** and this parameter is not specified, **clientCertAlias** cannot be empty. |
| certPassword | string | No | No | CA certificate password. The value contains a maximum of 128 bytes. |
| altSubjectMatch | string | No | No | A string to match the alternate subject. |
| domainSuffixMatch | string | No | No | A string to match the domain suffix. |
| realm | string | No | No | Realm for the passpoint credential. |
| plmn | string | No | No | Public land mobile network (PLMN) of the passpoint credential provider. |
| eapSubId | number | No | No | Sub-ID of the SIM card. |

#### WifiWapiConfig12+

Configuration of the WAPI(Wireless LAN Authentication and Privacy Infrastructure) authentication protocol.

When a user connects to the WLAN through the WAPI authentication protocol, the user can configure parameters or certificates in the following ways:

-   Method 1: Configure a certificate for connection. The key fields in WifiDeviceConfig are configured as follows:
    -   **preSharedKey** does not need to be transferred.
    -   Set **securityType** to **WIFI\_SEC\_TYPE\_WAPI\_CERT**.
    -   In wapiConfig:
        -   wapiAsCert transfers the text content of the AS certificate.
        -   wapiUserCert transfers the text content of the user certificate.
-   Method 2: Configure preSharedKey for connection. The key fields in WifiDeviceConfig are configured as follows:
    -   **preSharedKey** transfers the password set on the router.
    -   Set **securityType** to **WIFI\_SEC\_TYPE\_WAPI\_PSK**.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| wapiPskType | [WapiPskType](#wapipsktype12) | No | No | Security type. |
| wapiAsCert | string | No | No | Authentication server certificate (AS certificate). |
| wapiUserCert | string | No | No | User Certificate. |

#### WapiPskType12+

Enumerates the WAPI authentication types.

**System capability**: SystemCapability.Communication.WiFi.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| WAPI\_PSK\_ASCII | 0 | ASCII. |
| WAPI\_PSK\_HEX | 1 | HEX. |

#### EapMethod10+

Enumerates the EAP authentication methods.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| EAP\_NONE | 0 | Not specified. |
| EAP\_PEAP | 1 | PEAP. |
| EAP\_TLS | 2 | TLS. |
| EAP\_TTLS | 3 | TTLS. |
| EAP\_PWD | 4 | Password. |
| EAP\_SIM | 5 | SIM. |
| EAP\_AKA | 6 | AKA. |
| EAP\_AKA\_PRIME | 7 | AKA Prime. |
| EAP\_UNAUTH\_TLS | 8 | UNAUTH TLS. |

#### Phase2Method10+

Enumerates the Phase 2 authentication methods.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| PHASE2\_NONE | 0 | Not specified. |
| PHASE2\_PAP | 1 | PAP. |
| PHASE2\_MSCHAP | 2 | MS-CHAP. |
| PHASE2\_MSCHAPV2 | 3 | MS-CHAPv2. |
| PHASE2\_GTC | 4 | GTC. |
| PHASE2\_SIM | 5 | SIM. |
| PHASE2\_AKA | 6 | AKA. |
| PHASE2\_AKA\_PRIME | 7 | AKA Prime. |

#### WifiCategory12+

Represents the highest WLAN category supported by a hotspot. Identifies and distinguishes hotspots of different WLAN technology standards.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 1 | Default, that is, Wi-Fi types lower than Wi-Fi 6. |
| WIFI6 | 2 | Wi-Fi 6 |
| WIFI6\_PLUS | 3 | Wi-Fi 6+ |
| WIFI715+ | 4 | Wi-Fi 7 |
| WIFI7\_PLUS15+ | 5 | Wi-Fi 7+ |

#### wifiManager.addCandidateConfig

addCandidateConfig(config: WifiDeviceConfig): Promise<number>

Adds the candidate network configuration. This API uses a promise to return the result. Before using this API, ensure that WLAN is enabled.

-   Configures the WLAN network details, such as the SSID, password, and security type, by passing a [WifiDeviceConfig](#wifideviceconfig) object.
-   Returns a promise object. After the promise is resolved, a number is returned, indicating the configuration ID (used to distinguish and manage different WLAN configurations, and perform other related API operations, error handling, and debugging).

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfig) | Yes | WLAN configuration. If **bssidType** is left unspecified, its value is a random device address by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the network configuration ID. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    let config:wifiManager.WifiDeviceConfig = {
      ssid : "\*\*\*\*",
      preSharedKey : "\*\*\*\*",
      securityType : 0
    }
    wifiManager.addCandidateConfig(config).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.addCandidateConfig

addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void

Adds the configuration of a candidate network. This API uses an asynchronous callback to return the result.

-   Adds the configuration of a specified WLAN device as a candidate network. The candidate network cannot trigger automatic reconnection if no connection record is recorded. You can call **connectToCandidateConfig** or **connectToCandidateConfigWithUserAction** to connect to the candidate network. After the connection is confirmed on the page, automatic reconnection can be implemented.
-   Candidate networks are added in the application dimension and are isolated from system network configurations. They are invisible on the System WLAN page.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfig) | Yes | WLAN configuration. If **bssidType** is left unspecified, its value is a random device address by default. |
| callback | AsyncCallback<number> | Yes | 
Callback used to return the result. If **err** is **0**, the operation is successful. **data** indicates the ID of the network configuration to add. If **data** is **\-1**, the network configuration fails to be added.

If the value of **err** is not **0**, an error has occurred during the operation.

 |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiDeviceConfig = {
      ssid : "\*\*\*\*",
      preSharedKey : "\*\*\*\*",
      securityType : 0
    }
    wifiManager.addCandidateConfig(config,(error,result) => {
      console.info("result:" + JSON.stringify(result));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.removeCandidateConfig

removeCandidateConfig(networkId: number): Promise<void>

Removes the configuration of a candidate network. This API uses a promise to return the result.

-   Deletes the candidate WLAN configuration of a specified network ID from the system, clears the candidate WLAN configuration that is no longer needed, and releases system resources.
-   Only the candidate configuration added by calling [addCandidateConfig](#wifimanageraddcandidateconfig) can be removed. After the candidate configuration is removed, the candidate network will not be automatically connected.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | number | Yes | ID of the network configuration to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    wifiManager.removeCandidateConfig(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.removeCandidateConfig

removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void

Removes the candidate network configuration of a specified network. This API uses an asynchronous callback to return the result.

-   Deletes the candidate WLAN configuration of a specified network ID from the system, clears the candidate WLAN configuration that is no longer needed, and releases system resources.
-   Only the candidate configuration added by calling [addCandidateConfig](#wifimanageraddcandidateconfig) can be removed. After the candidate configuration is removed, the candidate network will not be automatically connected.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | number | Yes | ID of the network configuration to remove. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **0**. If the operation fails, **error** is not **0**. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    wifiManager.removeCandidateConfig(networkId,(error,result) => {
    console.info("result:" + JSON.stringify(result));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.removeDevice15+

removeDevice(id: number): void

Removes the network configuration.

-   Deletes the saved WLAN network configuration information according to the network configuration ID.
-   After the removal, the corresponding network configuration is no longer available, and the device does not automatically connect to the network.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO and ohos.permission.MANAGE\_WIFI\_CONNECTION (available only to system applications) or ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION (available only to enterprise applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | ID of the network configuration to remove. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
    try {
      let id = 0;
      wifiManager.removeDevice(id);
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }

#### wifiManager.getCandidateConfigs

getCandidateConfigs(): Array<WifiDeviceConfig>

Obtains candidate network configuration.

-   Candidate networks are the networks that have been connected to or manually added.
-   Obtains the configurations of all WLAN networks that have been saved but are not connected to in the system.
-   Displays the list of networks that can be connected to or performs network management operations.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiDeviceConfig](#wifideviceconfig)\> | Candidate network configuration obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let configs = wifiManager.getCandidateConfigs();
    console.info("configs:" + JSON.stringify(configs));
    let len = configs.length;
        console.info("result len: " + len);
    if(len > 0){
      for (let i = 0; i < len; ++i) {
        console.info("ssid: " + configs\[i\].ssid);
        console.info("bssid: " + configs\[i\].bssid);
      }
    }
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
  

#### wifiManager.connectToCandidateConfig

connectToCandidateConfig(networkId: number): void

Connects to a candidate network.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | number | Yes | ID of the candidate network configuration. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0; // Candidate network ID, which is generated when a candidate network is added.
    wifiManager.connectToCandidateConfig(networkId);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
  

#### wifiManager.connectToCandidateConfigWithUserAction20+

connectToCandidateConfigWithUserAction(networkId: number): Promise<void>

This API is used to connect an application to a candidate network added by a user and prompt the user to confirm the trust during the connection. This API uses a promise to return the result.

-   When this API is called, the system prompts the user to confirm whether to trust and connect to the specified candidate network.
-   User confirmation is a necessary step in the connection process. The connection operation is not performed before the user confirms the trust.
-   You are advised to trigger a WLAN scan by calling the **startScan** API before initiating a connection, and then connect to the candidate network after the updating of the scan result is detected by using the [wifiManager.on('wifiScanStateChange')](#wifimanageronwifiscanstatechange) method. This improves the connection success rate.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/KsGqgtmATPm9WEmohBbfGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E98CF80869566A72A1A367DFA4AFABDEE715F8BC8AC1292F90B777F59DE3673)

If [wifiManager.connectToCandidateConfig](#wifimanagerconnecttocandidateconfig) is used to connect to a candidate network, no user response is returned.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | number | Yes | Candidate network ID. The value cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |
| 2501005 | The user does not respond. |
| 2501006 | The user refused the action. |
| 2501007 | Parameter validation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    let networkId = 0; // Candidate network ID, which is generated when a candidate network is added.
    wifiManager.connectToCandidateConfigWithUserAction(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.addDeviceConfig15+

addDeviceConfig(config: WifiDeviceConfig): Promise<number>

Adds network configuration. This API uses a promise to return the result.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO and ohos.permission.SET\_WIFI\_CONFIG

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfig) | Yes | WLAN configuration. The value of **bssidType** is a random device address by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the network configuration ID. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    let config:wifiManager.WifiDeviceConfig = {
      ssid : "\*\*\*\*",
      preSharedKey : "\*\*\*\*",
      securityType : 0
    }
    wifiManager.addDeviceConfig(config).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.addDeviceConfig15+

addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void

Adds network configuration. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO and ohos.permission.SET\_WIFI\_CONFIG

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfig) | Yes | WLAN configuration. The value of **bssidType** is a random device address by default. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the network configuration ID. If **data** is **\-1**, the operation has failed. If **err** is not **0**, an error has occurred. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
    try {
      let config:wifiManager.WifiDeviceConfig = {
        ssid : "\*\*\*\*",
        preSharedKey : "\*\*\*\*",
        securityType : 0
      }
      wifiManager.addDeviceConfig(config,(error,result) => {
        console.info("result:" + JSON.stringify(result));
      });
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }

#### wifiManager.getDeviceConfigs15+

getDeviceConfigs(): Array<WifiDeviceConfig>

Obtains network configuration.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.GET\_WIFI\_CONFIG

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiDeviceConfig](#wifideviceconfig)\> | Network configuration array. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
    try {
      let configs = wifiManager.getDeviceConfigs();
      console.info("configs:" + JSON.stringify(configs));
    }catch(error){
      console.error("failed:", error.code, error.message);
    }
  

#### wifiManager.connectToNetwork15+

connectToNetwork(networkId: number): void

Connects to a hotspot.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_CONNECTION (available only to system applications) or ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION (available only to enterprise applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| networkId | number | Yes | ID of the candidate network configuration. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types. 3. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
    try {
      let networkId = 0;
      wifiManager.connectToNetwork(networkId);
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }
  

#### wifiManager.getSignalLevel

getSignalLevel(rssi: number, band: number): number

Obtains the WLAN signal level.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rssi | number | Yes | RSSI of the hotspot, in dBm. |
| band | number | Yes | Frequency band of the WLAN AP. The value **1** indicates 2.4 GHz, and the value **2** indicates 5 GHz. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Signal level obtained. The value range is \[0, 4\]. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let rssi = 0;
    let band = 0;
    let level = wifiManager.getSignalLevel(rssi,band);
    console.info("level:" + JSON.stringify(level));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.getLinkedInfo

getLinkedInfo(): Promise<WifiLinkedInfo>

Obtains information about the WLAN connection. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

If **macType** is set to **1** (device MAC address), you also need to apply for the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission to obtain the value of **macAddress**. (For API version 8 to 15, this permission is available only to system applications. For API version 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.) If the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission is not granted, a random MAC address is returned for **macAddress**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiLinkedInfo](#wifilinkedinfo)\> | Promise used to return the WLAN connection information. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

#### wifiManager.getLinkedInfo

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

Obtains information about the WLAN connection. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/SKJjUC_OR1mJ6QkGdvicOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D33D543E3344353FC492D655B7B68E49E45FA16B64A8831019080C172E1C8E4)

-   If **macType** is set to **1** (device MAC address), you also need to apply for the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission to obtain the value of **macAddress**. (For API version 8 to 15, this permission is available only to system applications. For API version 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.) If the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission is not granted, no value is returned for **macAddress**.
-   If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **bssid** in the return value is a real BSSID; otherwise, **bssid** is a random device address.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiLinkedInfo](#wifilinkedinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the WLAN connection information obtained. If the operation fails, **err** is not **0**. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

import { wifiManager } from '@kit.ConnectivityKit';

wifiManager.getLinkedInfo().then((data: wifiManager.WifiLinkedInfo) => {
    console.info("get wifi linked info: " + JSON.stringify(data));
}).catch((error: Error) => {
    console.error("get linked info error: ", error);
});

#### wifiManager.getLinkedInfoSync18+

getLinkedInfoSync(): WifiLinkedInfo;

Obtains the WLAN connection information. This API returns the result synchronously.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/1hxwRxrFQvCO4fzPpGXEjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF8C50F360A37D26332951F3664C484E7329360DDD23C243891C9EA885C09BE5)

-   If **macType** is set to **1** (device MAC address), you also need to apply for the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission to obtain the value of **macAddress**. (For API version 8 to 15, this permission is available only to system applications. For API version 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.) If the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission is not granted, no value is returned for **macAddress**.
-   If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **bssid** in the return value is a real BSSID; otherwise, **bssid** is a random device address.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| [WifiLinkedInfo](#wifilinkedinfo) | WLAN connection information. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  try {
    let linkInfo = wifiManager.getLinkedInfoSync();
    console.info("get linked info:" + JSON.stringify(linkInfo));
  } catch(error) {
    console.error("get linked info failed:" + JSON.stringify(error));
  }

#### WifiLinkedInfo

Represents WLAN connection information.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | No | No | 
Service set identifier (SSID) of the hotspot, which is used to obtain the public name (name of the wireless network) of the Wi-Fi hotspot connected to the current device. The encoding format is UTF-8.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| bssid | string | No | No | 

Basic service set identifier (BSSID) of the hotspot, which is the MAC address of the wireless network.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| rssi | number | No | No | 

Received signal strength indicator (RSSI) of the hotspot, in dBm.

Received signal strength indicator (RSSI), in dBm. The standard value range ranges from –127 dBm to 0 dBm. In normal usage scenarios, the RSSI value ranges from –100 dBm (weak signal) to –30 dBm (strong signal). A value close to 0 dBm indicates an extremely strong signal.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| band | number | No | No | Frequency band of the WLAN AP. The value **1** indicates 2.4 GHz, and the value **2** indicates 5 GHz. |
| linkSpeed | number | No | No | Uplink speed of the WLAN AP, in Mbps. |
| rxLinkSpeed10+ | number | No | No | Downlink speed of the WLAN AP, in Mbps. |
| maxSupportedTxLinkSpeed10+ | number | No | No | Maximum uplink speed supported, in Mbps. |
| maxSupportedRxLinkSpeed10+ | number | No | No | Maximum downlink speed supported, in Mbps. |
| frequency | number | No | No | 

Frequency of the WLAN AP.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isHidden | boolean | No | No | Whether the WLAN AP is hidden. The value **true** indicates that the WLAN AP is hidden; the value **false** indicates the opposite. |
| isRestricted | boolean | No | No | Whether data volume is restricted at the WLAN AP. The value **true** indicates that data volume is restricted, and the value **false** indicates the opposite. |
| macType | number | No | No | 

MAC address type.

The value **0** indicates a random MAC address, and the value **1** indicates device MAC address.

 |
| macAddress | string | No | No | MAC address of the device. |
| ipAddress | number | No | No | 

IP address of the device that sets up the WLAN connection.

1\. You can view the IP address in Wi-Fi connection information and in **Settings** > **About phone** > **Status**.

2\. The **ipAddress** value is of the number type and needs to be converted to the common IP address format. For details, see [IP Address Format Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-connectivity-4).

 |
| connState | [ConnState](#connstate) | No | No | WLAN connection state. |
| channelWidth10+ | [WifiChannelWidth](#wifichannelwidth) | No | No | Channel bandwidth of the connected hotspot. |
| wifiStandard10+ | [WifiStandard](#wifistandard10) | No | No | Wi-Fi standard used by the connected hotspot. |
| supportedWifiCategory12+ | [WifiCategory](#wificategory12) | No | No | Highest Wi-Fi category supported by the hotspot. |
| isHiLinkNetwork12+ | boolean | No | No | Whether HiLink is supported by the hotspot. The value **true** indicates that HiLink is supported, and the value **false** indicates the opposite. |
| wifiLinkType18+ | [WifiLinkType](#wifilinktype18) | No | Yes | Wi-Fi 7 connection type. |

#### WifiLinkType18+

Enumerates Wi-Fi 7 connection types.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT\_LINK | 0 | Default connection type. |
| WIFI7\_SINGLE\_LINK | 1 | Wi-Fi 7 single-link connection. |
| WIFI7\_MLSR | 2 | Wi-Fi 7 multi-link single-radio (MLSR) connection. |
| WIFI7\_EMLSR | 3 | Wi-Fi 7 enhanced multi-link single-radio (EMLSR) connection. |
| WIFI7\_STR | 4 | Wi-Fi 7 simultaneous transmit and receive (STR) connection. |

#### ConnState

Enumerates the WLAN connection states.

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

#### wifiManager.isConnected

isConnected(): boolean

Checks whether WLAN is connected.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if WLAN is connected; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.isConnected();
    console.info("isConnected:" + ret);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.disconnect15+

disconnect(): void

Disconnects from a WLAN.

**Required permissions**: ohos.permission.SET\_WIFI\_INFO and ohos.permission.MANAGE\_WIFI\_CONNECTION (available only to system applications) or

ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION (available only to enterprise applications)

**System capability**: SystemCapability.Communication.WiFi.STA

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.disconnect();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.isFeatureSupported

isFeatureSupported(featureId: number): boolean

Checks whether the device supports the specified WLAN feature.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| featureId | number | Yes | Feature ID. |

**Feature IDs**

| Value | Description |
| :-- | :-- |
| 0x0001 | WLAN infrastructure mode |
| 0x0002 | 5 GHz feature |
| 0x0004 | Generic Advertisement Service (GAS)/Access Network Query Protocol (ANQP) feature |
| 0x0008 | Wi-Fi Direct |
| 0x0010 | SoftAP |
| 0x0040 | Wi-Fi Aware |
| 0x8000 | WLAN AP/STA concurrency |
| 0x8000000 | WPA3 Personal (WPA-3 SAE) |
| 0x10000000 | WPA3-Enterprise Suite B |
| 0x20000000 | Enhanced open feature |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the feature is supported; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

 |
| 801 | Capability not supported. |
| 2401000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let featureId = 0;
    let ret = wifiManager.isFeatureSupported(featureId);
    console.info("isFeatureSupported:" + ret);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.getDeviceMacAddress15+

getDeviceMacAddress(): string\[\]

Obtains the device MAC address.

**Required permissions**: ohos.permission.GET\_WIFI\_LOCAL\_MAC and ohos.permission.GET\_WIFI\_INFO

This permission is available only to system applications in API versions 8 to 15. From API version 16, it is also available to normal applications on PCs/2-in-1 devices while remaining exclusive to system applications on other devices.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | MAC address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.getDeviceMacAddress();
    console.info("deviceMacAddress:" + JSON.stringify(ret));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.getIpInfo

getIpInfo(): IpInfo

Obtains IPv4 information.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| [IpInfo](#ipinfo) | IP information obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let info = wifiManager.getIpInfo();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### IpInfo

Represents IPv4 information.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ipAddress | number | No | No | IP address. The **ipAddress** value is of the number type and needs to be converted to the common IP address format. For details, see [IP Address Format Conversion](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-connectivity-4). |
| gateway | number | No | No | Gateway. |
| netmask | number | No | No | Subnet mask. |
| primaryDns | number | No | No | IP address of the preferred DNS server. |
| secondDns | number | No | No | IP address of the alternate DNS server. |
| serverIp | number | No | No | IP address of the DHCP server. |
| leaseDuration | number | No | No | Lease duration of the IP address, in seconds. |

#### wifiManager.getIpv6Info10+

getIpv6Info(): Ipv6Info

Obtains IPv6 information.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| [Ipv6Info](#ipv6info10) | IPv6 information obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let info = wifiManager.getIpv6Info();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### Ipv6Info10+

Represents the IPv6 information.

**System capability**: SystemCapability.Communication.WiFi.STA

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| linkIpv6Address | string | No | No | IPv6 address of the link. |
| globalIpv6Address | string | No | No | Global IPv6 address. |
| randomGlobalIpv6Address | string | No | No | Random global IPv6 address. This parameter is reserved. |
| uniqueIpv6Address12+ | string | No | Yes | Unique local address (ULA) in IPv6 format. |
| randomUniqueIpv6Address12+ | string | No | Yes | Random unique local address (RULA) in IPv6 format. |
| gateway | string | No | No | Gateway. |
| netmask | string | No | No | Subnet mask. |
| primaryDNS | string | No | No | IPv6 address of the preferred DNS server. |
| secondDNS | string | No | No | IPv6 address of the alternate DNS server. |

#### wifiManager.getCountryCode

getCountryCode(): string

Obtains the country code.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Country code obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2401000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let code = wifiManager.getCountryCode();
    console.info("code:" + code);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.isBandTypeSupported10+

isBandTypeSupported(bandType: WifiBandType): boolean

Checks whether the current frequency band is supported.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bandType | [WifiBandType](#wifibandtype10) | Yes | Wi-Fi band type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the feature is supported; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let type = 0;
    let isBandTypeSupported = wifiManager.isBandTypeSupported(type);
    console.info("isBandTypeSupported:" + isBandTypeSupported);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.isMeteredHotspot11+

isMeteredHotspot(): boolean

Checks whether the Wi-Fi network connected to the device is a smartphone hotspot.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the Wi-Fi network connected is a smartphone hotspot; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let isMeteredHotspot = wifiManager.isMeteredHotspot();
    console.info("isMeteredHotspot:" + isMeteredHotspot);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.isHotspotActive15+

isHotspotActive(): boolean

Checks whether this hotspot is active.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if WLAN is enabled; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2601000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.isHotspotActive();
    console.info("result:" + ret);
  } catch(error) {
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.getP2pLinkedInfo

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

Obtains P2P connection information. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

To obtain the value of **groupOwnerAddr**, you also need to apply for the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission. (For API version 8 to 15, this permission is available only to system applications. For API version 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.) If the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission is not granted, an all-zero address is returned for **groupOwnerAddr**.

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pLinkedInfo](#wifip2plinkedinfo)\> | Promise used to return the P2P connection information obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.getP2pLinkedInfo

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

Obtains P2P connection information. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

To obtain the value of **groupOwnerAddr**, you also need to apply for the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission. (For API version 8 to 15, this permission is available only to system applications. For API version 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.) If the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission is not granted, an all-zero address is returned for **groupOwnerAddr**.

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pLinkedInfo](#wifip2plinkedinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the P2P link information. If the operation fails, **err** is not **0**. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  wifiManager.getP2pLinkedInfo((err, data:wifiManager.WifiP2pLinkedInfo) => {
    if (err) {
        console.error("get p2p linked info error");
        return;
    }
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
  });

  wifiManager.getP2pLinkedInfo().then(data => {
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
  });

#### WifiP2pLinkedInfo

Represents the P2P link information.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| connectState | [P2pConnectState](#p2pconnectstate) | No | No | P2P connection state. |
| isGroupOwner | boolean | No | No | Whether the device is the group owner. The value **true** indicates that the device is the group owner, and the value **false** indicates the opposite. |
| groupOwnerAddr | string | No | No | IP address of the group. |

#### P2pConnectState

Enumerates the P2P connection states.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Value | Description |
| :-- | :-- | :-- |
| DISCONNECTED | 0 | Disconnected. |
| CONNECTED | 1 | Connected. |

#### wifiManager.getCurrentGroup

getCurrentGroup(): Promise<WifiP2pGroupInfo>

Obtains the current P2P group information. This API uses a promise to return the result.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pGroupInfo](#wifip2pgroupinfo)\> | Promise used to return the P2P group information obtained. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **deviceAddress** in the return value is a real device address; otherwise, **deviceAddress** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.getCurrentGroup

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

Obtains the current P2P group information. This API uses an asynchronous callback to return the result.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pGroupInfo](#wifip2pgroupinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the group information obtained. If the operation fails, **error** is not **0**. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **deviceAddress** in the return value is a real device address; otherwise, **deviceAddress** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  // The current group information can be obtained only after the P2P group is created or the connection is successful.
  wifiManager.getCurrentGroup((err, data:wifiManager.WifiP2pGroupInfo) => {
    if (err) {
        console.error("get current P2P group error");
        return;
    }
    console.info("get current P2P group: " + JSON.stringify(data));
  });

  wifiManager.getCurrentGroup().then(data => {
    console.info("get current P2P group: " + JSON.stringify(data));
  });

#### wifiManager.getP2pPeerDevices

getP2pPeerDevices(): Promise<WifiP2pDevice\[\]>

Obtains the P2P peer device list. This API uses a promise to return the result.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pDevice\[\]](#wifip2pdevice)\> | Promise used to return the peer device list. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **deviceAddress** in the return value is a real device address; otherwise, **deviceAddress** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.getP2pPeerDevices

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice\[\]>): void

Obtains the P2P peer device list. This API uses an asynchronous callback to return the result.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pDevice\[\]](#wifip2pdevice)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the peer device list obtained. If the operation fails, **err** is not **0**. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **deviceAddress** in the return value is a real device address; otherwise, **deviceAddress** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  // The peer device list can be obtained only after the P2P discovery is complete.
  wifiManager.getP2pPeerDevices((err, data:wifiManager.WifiP2pDevice\[\]) => {
    if (err) {
        console.error("get P2P peer devices error");
        return;
    }
    console.info("get P2P peer devices: " + JSON.stringify(data));
  });

  wifiManager.getP2pPeerDevices().then(data => {
    console.info("get P2P peer devices: " + JSON.stringify(data));
  });

#### WifiP2pDevice

Represents the P2P device information.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceName | string | No | No | Device name. |
| deviceAddress | string | No | No | MAC address of the device. |
| deviceAddressType10+ | [DeviceAddressType](#deviceaddresstype10) | No | Yes | MAC address type of the device. |
| primaryDeviceType | string | No | No | Type of the primary device. |
| deviceStatus | [P2pDeviceStatus](#p2pdevicestatus) | No | No | Device state. |
| groupCapabilities | number | No | No | Group capabilities. |

#### P2pDeviceStatus

Enumerates the P2P device states.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Value | Description |
| :-- | :-- | :-- |
| CONNECTED | 0 | Connected. |
| INVITED | 1 | Invited. |
| FAILED | 2 | Failed. |
| AVAILABLE | 3 | Available. |
| UNAVAILABLE | 4 | Unavailable. |

#### wifiManager.getP2pLocalDevice

getP2pLocalDevice(): Promise<WifiP2pDevice>

Obtains the local device information in the P2P connection. This API uses a promise to return the result.

**Required permissions**:

API version 11 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WifiP2pDevice](#wifip2pdevice)\> | Promise used to return the local device information obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.getP2pLocalDevice

getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void

Obtains the local device information in the P2P connection. This API uses an asynchronous callback to return the result.

**Required permissions**:

API version 11 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pDevice](#wifip2pdevice)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the local device information obtained. If the operation fails, **error** is not **0**. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  // The local device information can be obtained only after a P2P group is created or the connection is successful.
  wifiManager.getP2pLocalDevice((err, data:wifiManager.WifiP2pDevice) => {
    if (err) {
        console.error("get P2P local device error");
        return;
    }
    console.info("get P2P local device: " + JSON.stringify(data));
  });

  wifiManager.getP2pLocalDevice().then(data => {
    console.info("get P2P local device: " + JSON.stringify(data));
  });

#### wifiManager.createGroup

createGroup(config: WifiP2PConfig): void

Creates a P2P group.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiP2PConfig](#wifip2pconfig) | Yes | Group configuration. The value of **DeviceAddressType** is a random device address by default. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiP2PConfig = {
      deviceAddress: "\*\*\*\*",
      netId: 0,
      passphrase: "\*\*\*\*\*",
      groupName: "\*\*\*\*",
      goBand: 0
    }
    wifiManager.createGroup(config);
    
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### WifiP2PConfig

Represents P2P group configuration.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceAddress | string | No | No | Device address. |
| deviceAddressType10+ | [DeviceAddressType](#deviceaddresstype10) | No | Yes | Device address type. |
| netId | number | No | No | Network ID. The value **\-1** indicates a temporary group, and the value **\-2** indicates a persistent group. |
| passphrase | string | No | No | Passphrase of the group. |
| groupName | string | No | No | Group name. |
| goBand | [GroupOwnerBand](#groupownerband) | No | No | Frequency band of the group. |

#### GroupOwnerBand

Enumerates the P2P group frequency bands.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Value | Description |
| :-- | :-- | :-- |
| GO\_BAND\_AUTO | 0 | Auto. |
| GO\_BAND\_2GHZ | 1 | 2.4 GHz. |
| GO\_BAND\_5GHZ | 2 | 5 GHz. |

#### wifiManager.removeGroup

removeGroup(): void

Removes this P2P group.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.removeGroup();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.p2pConnect

p2pConnect(config: WifiP2PConfig): void

Sets up a P2P connection.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [WifiP2PConfig](#wifip2pconfig) | Yes | P2P group configuration. The value of **DeviceAddressType** is a random device address by default. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Invalid parameters. Possible causes: 1. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pConnectionChangeFunc = (result:wifiManager.WifiP2pLinkedInfo) => {
      console.info("p2p connection change receive event: " + JSON.stringify(result));
      wifiManager.getP2pLinkedInfo((err, data:wifiManager.WifiP2pLinkedInfo) => {
          if (err) {
              console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
              return;
          }
          console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
      });
  }
  wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);
  
  let recvP2pDeviceChangeFunc = (result:wifiManager.WifiP2pDevice) => {
      console.info("p2p device change receive event: " + JSON.stringify(result));
  }
  wifiManager.on("p2pDeviceChange", recvP2pDeviceChangeFunc);
  
  let recvP2pPeerDeviceChangeFunc = (result:wifiManager.WifiP2pDevice\[\]) => {
      console.info("p2p peer device change receive event: " + JSON.stringify(result));
      wifiManager.getP2pPeerDevices((err, data:wifiManager.WifiP2pDevice\[\]) => {
          if (err) {
              console.error('failed to get peer devices: ' + JSON.stringify(err));
              return;
          }
          console.info("get peer devices: " + JSON.stringify(data));
          let len = data.length;
          for (let i = 0; i < len; ++i) {
              if (data\[i\].deviceName === "my\_test\_device") {
                  console.info("p2p connect to test device: " + data\[i\].deviceAddress);
                  let config:wifiManager.WifiP2PConfig = {
                      deviceAddress:data\[i\].deviceAddress,
                      netId:-2,
                      passphrase:"",
                      groupName:"",
                      goBand:0,
                  }
                  wifiManager.p2pConnect(config);
              }
          }
      });
  }
  wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
  
  let recvP2pPersistentGroupChangeFunc = () => {
      console.info("p2p persistent group change receive event");
  
      wifiManager.getCurrentGroup((err, data:wifiManager.WifiP2pGroupInfo) => {
          if (err) {
              console.error('failed to get current group: ' + JSON.stringify(err));
              return;
          }
          console.info("get current group: " + JSON.stringify(data));
      });
  }
  wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
  
  setTimeout(() => {wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 \* 1000);
  setTimeout(() =>  {wifiManager.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 \* 1000);
  setTimeout(() =>  {wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 \* 1000);
  setTimeout(() =>  {wifiManager.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 \* 1000);
  console.info("start discover devices -> " + wifiManager.startDiscoverDevices());

#### wifiManager.p2pCancelConnect

p2pCancelConnect(): void

Cancels the P2P connection being set up.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.p2pCancelConnect();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.startDiscoverDevices

startDiscoverDevices(): void

Starts to discover devices.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startDiscoverDevices();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.stopDiscoverDevices

stopDiscoverDevices(): void

Stops discovering devices.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.stopDiscoverDevices();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### wifiManager.getMultiLinkedInfo18+

getMultiLinkedInfo(): Array<WifiLinkedInfo>

Obtains WLAN connection information for multi-link operation (MLO).

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/wLUSN7jzRvK0cJHRNT2wQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5450F7FD876864FC8A85CB2D4A9A47499018FD8B4BF615264C3DB02E238AB647)

-   If **macType** is set to **1** (device MAC address), you also need to apply for the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission to obtain the value of **macAddress**. (For API version 8 to 15, this permission is available only to system applications. For API version 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.) If the ohos.permission.GET\_WIFI\_LOCAL\_MAC permission is not granted, no value is returned for **macAddress**.
-   If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **bssid** in the return value is a real BSSID; otherwise, **bssid** is a random device address.

**System capability**: SystemCapability.Communication.WiFi.STA

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[WifiLinkedInfo](#wifilinkedinfo)\> | Wi-Fi connection information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |
| 2501001 | Wi-Fi STA disabled. |

**Example**

import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let linkedInfo = wifiManager.getMultiLinkedInfo();
    console.info("linkedInfo:" + JSON.stringify(linkedInfo));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

#### WifiP2pGroupInfo

Represents the P2P group information.

**System capability**: SystemCapability.Communication.WiFi.P2P

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isP2pGo | boolean | No | No | Whether the device is the group owner. The value **true** indicates that the device is the group owner, and the value **false** indicates the opposite. |
| ownerInfo | [WifiP2pDevice](#wifip2pdevice) | No | No | Device information of the group. |
| passphrase | string | No | No | Passphrase of the group. |
| interface | string | No | No | Interface name. |
| groupName | string | No | No | Group name. |
| networkId | number | No | No | Network ID. |
| frequency | number | No | No | Frequency of the group. |
| clientDevices | [WifiP2pDevice\[\]](#wifip2pdevice) | No | No | List of connected devices. |
| goIpAddress | string | No | No | IP address of the group. |

#### wifiManager.on('wifiStateChange')

on(type: 'wifiStateChange', callback: Callback<number>): void

Subscribes to WLAN state changes. When the service exits, call off(type: 'wifiStateChange', callback?: Callback<number>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiStateChange**. |
| callback | Callback<number> | Yes | Callback used to return the WLAN state. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**WLAN states**

| Value | Description |
| :-- | :-- |
| 0 | Deactivated |
| 1 | Activated |
| 2 | Activating |
| 3 | Deactivating |

#### wifiManager.off('wifiStateChange')

off(type: 'wifiStateChange', callback?: Callback<number>): void

Unsubscribes from WLAN state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvPowerNotifyFunc = (result:number) => {
      console.info("Receive power state change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("wifiStateChange", recvPowerNotifyFunc);
  
  // Unregister an event.
  wifiManager.off("wifiStateChange", recvPowerNotifyFunc);

#### wifiManager.on('wifiConnectionChange')

on(type: 'wifiConnectionChange', callback: Callback<number>): void

Subscribes to WLAN connection state changes. When the service exits, call off(type: 'wifiConnectionChange', callback?: Callback<number>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

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

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

#### wifiManager.off('wifiConnectionChange')

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

Unsubscribes from WLAN connection state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiConnectionChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvWifiConnectionChangeFunc = (result:number) => {
      console.info("Receive wifi connection change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("wifiConnectionChange", recvWifiConnectionChangeFunc);
  
  // Unregister an event.
  wifiManager.off("wifiConnectionChange", recvWifiConnectionChangeFunc);

#### wifiManager.on('wifiScanStateChange')

on(type: 'wifiScanStateChange', callback: Callback<number>): void

Subscribes to WLAN scan state changes. When the service exits, call off(type: 'wifiScanStateChange', callback?: Callback<number>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

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

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

#### wifiManager.off('wifiScanStateChange')

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

Unsubscribes from WLAN scan state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiScanStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvWifiScanStateChangeFunc = (result:number) => {
      console.info("Receive Wifi scan state change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("wifiScanStateChange", recvWifiScanStateChangeFunc);
  
  // Unregister an event.
  wifiManager.off("wifiScanStateChange", recvWifiScanStateChangeFunc);

#### wifiManager.on('wifiRssiChange')

on(type: 'wifiRssiChange', callback: Callback<number>): void

Subscribes to WLAN received signal strength indicator (RSSI) changes. When the service exits, you need to call off(type: 'wifiRssiChange', callback?: Callback<number>) to remove the registered callback. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiRssiChange**. |
| callback | Callback<number> | Yes | Callback used to return the RSSI, in dBm. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

#### wifiManager.off('wifiRssiChange')

off(type: 'wifiRssiChange', callback?: Callback<number>): void

Unsubscribes from WLAN RSSI changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.STA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **wifiRssiChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2501000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvWifiRssiChangeFunc = (result:number) => {
      console.info("Receive wifi rssi change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("wifiRssiChange", recvWifiRssiChangeFunc);
  
  // Unregister an event.
  wifiManager.off("wifiRssiChange", recvWifiRssiChangeFunc);

#### wifiManager.on('hotspotStateChange')

on(type: 'hotspotStateChange', callback: Callback<number>): void

Subscribes to hotspot state changes. When the service exits, call off(type: 'hotspotStateChange', callback?: Callback<number>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

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

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2601000 | Operation failed. |

#### wifiManager.off('hotspotStateChange')

off(type: 'hotspotStateChange', callback?: Callback<number>): void

Unsubscribes from hotspot state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **hotspotStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2601000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvHotspotStateChangeFunc = (result:number) => {
      console.info("Receive hotspot state change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("hotspotStateChange", recvHotspotStateChangeFunc);
  
  // Unregister an event.
  wifiManager.off("hotspotStateChange", recvHotspotStateChangeFunc);

#### wifiManager.on('p2pStateChange')

on(type: 'p2pStateChange', callback: Callback<number>): void

Subscribes to P2P state changes. When the service exits, call off(type: 'p2pStateChange', callback?: Callback<number>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

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

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.off('p2pStateChange')

off(type: 'p2pStateChange', callback?: Callback<number>): void

Unsubscribes from P2P state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pStateChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pStateChangeFunc = (result:number) => {
      console.info("Receive p2p state change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("p2pStateChange", recvP2pStateChangeFunc);
  
  // Unregister an event.
  wifiManager.off("p2pStateChange", recvP2pStateChangeFunc);

#### wifiManager.on('p2pConnectionChange')

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

Subscribes to P2P connection state changes. When the service exits, call off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pConnectionChange**. |
| callback | Callback<[WifiP2pLinkedInfo](#wifip2plinkedinfo)\> | Yes | Callback used to return the WLAN state. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.off('p2pConnectionChange')

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

Unsubscribes from P2P connection state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pConnectionChange**. |
| callback | Callback<[WifiP2pLinkedInfo](#wifip2plinkedinfo)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pConnectionChangeFunc = (result:wifiManager.WifiP2pLinkedInfo) => {
      console.info("Receive p2p connection change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);
  
  // Unregister an event.
  wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);

#### wifiManager.on('p2pDeviceChange')

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

Subscribes to P2P device state changes. When the service exits, call off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDeviceChange**. |
| callback | Callback<[WifiP2pDevice](#wifip2pdevice)\> | Yes | Callback used to return the WLAN state. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.off('p2pDeviceChange')

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

Unsubscribes from P2P device state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDeviceChange**. |
| callback | Callback<[WifiP2pDevice](#wifip2pdevice)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pDeviceChangeFunc = (result:wifiManager.WifiP2pDevice) => {
      console.info("Receive p2p device change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("p2pDeviceChange", recvP2pDeviceChangeFunc);
  
  // Unregister an event.
  wifiManager.off("p2pDeviceChange", recvP2pDeviceChangeFunc);

#### wifiManager.on('p2pPeerDeviceChange')

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice\[\]>): void

Subscribes to P2P peer device state changes. When the service exits, call off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice\[\]>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**:

API version 10 and later: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPeerDeviceChange**. |
| callback | Callback<[WifiP2pDevice\[\]](#wifip2pdevice)\> | Yes | Callback used to return the P2P peer device state. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **deviceAddress** in the return value is a real device address; otherwise, **deviceAddress** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.off('p2pPeerDeviceChange')

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice\[\]>): void

Unsubscribes from P2P peer device state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPeerDeviceChange**. |
| callback | Callback<[WifiP2pDevice\[\]](#wifip2pdevice)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. If the application has the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission, **deviceAddress** in the return value is a real device address; otherwise, **deviceAddress** is a random device address. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pPeerDeviceChangeFunc = (result:wifiManager.WifiP2pDevice\[\]) => {
      console.info("Receive p2p peer device change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
  
  // Unregister an event.
  wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

#### wifiManager.on('p2pPersistentGroupChange')

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

Subscribes to P2P persistent group changes. When the service exits, call off(type: 'p2pPersistentGroupChange', callback?: Callback<void>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPersistentGroupChange**. |
| callback | Callback<void> | Yes | Callback used to return the WLAN state. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.off('p2pPersistentGroupChange')

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

Unsubscribes from P2P persistent group state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pPersistentGroupChange**. |
| callback | Callback<void> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pPersistentGroupChangeFunc = (result:void) => {
      console.info("Receive p2p persistent group change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
  
  // Unregister an event.
  wifiManager.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

#### wifiManager.on('p2pDiscoveryChange')

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

Subscribes to P2P device discovery changes. When the service exits, call off(type: 'p2pDiscoveryChange', callback?: Callback<number>) to unregister the callback registered. This API uses an asynchronous callback to return the result.

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

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

#### wifiManager.off('p2pDiscoveryChange')

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

Unsubscribes from P2P device discovery state changes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.P2P

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which has a fixed value of **p2pDiscoveryChange**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |

**Example**

  import { wifiManager } from '@kit.ConnectivityKit';
  
  let recvP2pDiscoveryChangeFunc = (result:number) => {
      console.info("Receive p2p discovery change event: " + result);
  }
  
  // Register an event.
  wifiManager.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
  
  // Unregister an event.
  wifiManager.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
