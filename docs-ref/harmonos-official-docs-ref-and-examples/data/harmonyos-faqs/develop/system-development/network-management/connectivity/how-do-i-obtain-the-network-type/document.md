# How do I obtain the network type?

You can use [getNetCapabilities](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilities) to check whether the default network is Wi-Fi or cellular.

**WIFI** indicates a Wi-Fi network, and **CELLULAR** indicates a cellular network. For a cellular network, you can call [radio.getSignalInformation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-radio#radiogetsignalinformation7) to obtain a list of signal strengths of the network with which the SIM card in the specified slot is registered. In the returned array of [SignalInformation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-radio#signalinformation) objects, **signalType** indicates the [network type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-radio#networktype). The value can be:

-   GSM: 2G
-   CDMA: 2G
-   WCDMA: 3G
-   TDSCDMA: 3G
-   LTE: 4G

Refer to the code snippet below:

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { radio } from '@kit.TelephonyKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Obtain Network Type')
        .type(ButtonType.Normal)
        .width(200)
        .height(200)
        .onClick(() => {
          connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
            if (netHandle.netId == 0) {
              // When there is currently no connected network, the obtained netHandler's netid is 0, which belongs to an abnormal scenario.
              // Here, some processing mechanisms can be added according to the actual situation.
              return;
            }
            // Obtain the capability information of the network corresponding to netHandle
            connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
              if (error) {
                console.error(\`Failed to get net capabilities. Code:${error.code}, message:${error.message}\`);
                return;
              }
              console.info("Succeeded to get data: " + JSON.stringify(data));
              if (data.bearerTypes\[0\] == 1) {
                // console.info("Wi Fi network");
              } else if (data.bearerTypes\[0\] == 0) {
                // console.info("Cellular Network");
                let slotId: number = 0; // Slot ID, -0: Slot 1, -1: Slot 2
                radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
                  if (err) {
                    console.error(\`getSignalInformation failed, callback: err->${JSON.stringify(err)}\`);
                    return;
                  }
                  console.info(\`getSignalInformation success, callback: data->${JSON.stringify(data)}\`);
                  // Return an array of SignalInformation objects, where the returned signalType represents the network type NetworkType
                });
              }
            })
          }).catch((error: BusinessError) => {
            console.error('error: ' + JSON.stringify(error));
          });
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
