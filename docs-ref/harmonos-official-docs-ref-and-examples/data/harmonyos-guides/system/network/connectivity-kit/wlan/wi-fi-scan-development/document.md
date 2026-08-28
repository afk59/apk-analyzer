# Wi-Fi Scan Development

#### Introduction

Wi-Fi scan is the process where devices (such as smartphones, PCs, and routers) search for available Wi-Fi networks in their surrounding environment. Through this scan process, devices can gather fundamental information about nearby networks—such as network name, signal strength, and encryption type—thereby enabling connection to, management of, or analysis of these networks.

#### Use Cases

-   [Wi-Fi Scan](#wi-fi-scan)
-   [PNO Scan](#pno-scan)
-   [Periodic Scan](#periodic-scan)
-   [Scan Control](#scan-control)

#### Available APIs

For details about the JavaScript APIs and sample code, see the [SCAN API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-wifimanager).

The following table describes the related APIs.

| API | Description |
| :-- | :-- |
| getScanInfoList() | Obtains the scan result. |
| on(type: 'wifiScanStateChange') | Subscribes to Wi-Fi scan state changes. |
| off(type: 'wifiScanStateChange') | Unsubscribes from Wi-Fi scan state changes. |

#### How to Develop

## Wi-Fi Scan

1.  Import the required Wi-Fi module.
    
2.  Check that the **SystemCapability.Communication.WiFi.STA** capability is available.
    
3.  Apply for the **ohos.permission.GET\_WIFI\_INFO** permission.
    
4.  Enable Wi-Fi on the device.
    
5.  Sample code:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Ppscg-RoQp2VS_XbBM1cyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062015Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9F79BFEB823038543DB569E2A872DB2B63BA25AC7DE956BCB0EF5B813BF0990)
    
    The Wi-Fi scan API is deprecated since API version 10. The substitute API is available only for system applications.
    
    import { wifiManager } from '@kit.ConnectivityKit';
    
    try {
      let recvWifiScanStateChangeFunc = (result:number) => {
          console.info("Receive Wifi scan state change event: " + result);
      }
    
      // Obtain the scan status. The value 1 indicates that the scan is successful, and the value 0 indicates the opposite.
      wifiManager.on("wifiScanStateChange", recvWifiScanStateChangeFunc);
    
      let isWifiActive = wifiManager.isWifiActive();
      if (!isWifiActive) {
        console.error("wifi not enable"); // Enable Wi-Fi manually.
        return;
      }
    
      let scanInfoList = wifiManager.getScanInfoList();
    
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
    
      // Unsubscribe from Wi-Fi scan state changes.
      wifiManager.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
    } catch (error) {
      console.error(\`WiFi scan fail. ${error.message}\`);
    }
    
6.  For details about error codes, see [Wi-Fi Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-wifi).
    

## PNO Scan

Preferred Network Offload (PNO) scan is a Wi-Fi scan technology that reduces power consumption of mobile devices.

PNO scan is triggered when a device is not connected to any Wi-Fi network and the screen is off. The device then searches for and connects to the preferred Wi-Fi network in the background.

## Periodic Scan

Periodic scan is the process where a wireless device (such as a smartphone, tablet, or laptop) automatically searches for available Wi-Fi networks at the specified interval.

This function can be used in the following scenarios:

1.  When the screen is on and the device is connected to Wi-Fi, the device checks whether the current link supports Internet access. If Internet access is supported, perform scan at an interval of 1 hour. If Internet access is not supported, check the device's mobility status:
    
    \- Stationary scenario: Scan cycle starts at 20 seconds and doubles exponentially, with a maximum of 300 seconds.
    
    \- Non-stationary scenario: Scan cycle starts at 20 seconds and caps at 160 seconds.
    
2.  When the screen is on and the device is not connected to Wi-Fi:
    
    \- Stationary scenario: Scan cycle starts at 20 seconds and doubles exponentially, with a maximum of 300 seconds.
    
    \- Non-stationary scenario: Scan cycle starts at 20 seconds and caps at 160 seconds.
    

## Scan Control

Scan control allows management and control of Wi-Fi network scan by wireless devices.

Typical scenarios include:

1.  Prohibiting periodic scan and PNO scan when Wi-Fi is disabled
    
2.  Prohibiting scan during Wi-Fi connection
    
3.  Initiating no more than four scans within 2 minutes
    
4.  Prohibiting scan when the device temperature reaches the specified threshold
    
5.  Using the substitute of the scan API only for system applications (The scan API is supported since API version 9 and deprecated since API version 10.)
    
6.  Requesting the **ohos.permission.GET\_WIFI\_PEERS\_MAC** permission to obtain the actual BSSID in the scan result
