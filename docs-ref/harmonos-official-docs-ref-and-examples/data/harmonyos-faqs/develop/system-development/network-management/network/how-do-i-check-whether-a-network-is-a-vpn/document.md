# How do I check whether a network is a VPN?

You can use **getNetCapabilities** to obtain the network capability information. If the value of [bearerTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#netbeartype) is **4**, the network is a VPN. Before using this method, you must have the **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO** permissions.

The code snippet is as follows:

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct JudeNetType {
  getNetType() {
    connection.getAllNets((error: BusinessError, allNets: connection.NetHandle\[\]) => {
      if (error) {
        console.error(\`Failed to get getAllNets. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      for (let netHandle of allNets) {
        connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
          if (error) {
            console.error(\`Failed to get capabilities. Code: ${error.code}, message: ${error.message}\`);
            return;
          }
          if (data.bearerTypes\[0\] == connection.NetBearType.BEARER\_VPN) {
            console.info('The VPN network is connected');
          }
        })
      }
    });
  }

  build() {
    Column({ space: 10 }) {
      Button('Obtain the type of network connection').onClick(() => {
        this.getNetType()
      })
    }.alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}

For details, see [Network Connection Management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#netbeartype).
