# How do I obtain the Wi-Fi list?

You can call **wifiManager.getScanInfoList** to obtain the Wi-Fi list. The **ohos.permission.GET\_WIFI\_INFO** permission is required for using this API. The sample code is as follows:

import { wifiManager } from '@kit.ConnectivityKit';

try {
  let scanInfoList = wifiManager.getScanInfoList();
  console.info('scanInfoList:' + JSON.stringify(scanInfoList));
  let len = scanInfoList.length;
  console.log('wifi received scan info: ' + len);
  if (len > 0) {
    for (let i = 0; i < len; ++i) {
      console.info('ssid: ' + scanInfoList\[i\].ssid);
      console.info('bssid: ' + scanInfoList\[i\].bssid);
      console.info('capabilities: ' + scanInfoList\[i\].capabilities);
      console.info('securityType: ' + scanInfoList\[i\].securityType);
      console.info('rssi: ' + scanInfoList\[i\].rssi);
      console.info('band: ' + scanInfoList\[i\].band);
      console.info('frequency: ' + scanInfoList\[i\].frequency);
      console.info('channelWidth: ' + scanInfoList\[i\].channelWidth);
      console.info('timestamp: ' + scanInfoList\[i\].timestamp);
    }
  }
} catch (error) {
  console.error('failed:' + JSON.stringify(error));
}

**Reference**

[wifiManager.getScanInfoList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetscaninfolist10)
