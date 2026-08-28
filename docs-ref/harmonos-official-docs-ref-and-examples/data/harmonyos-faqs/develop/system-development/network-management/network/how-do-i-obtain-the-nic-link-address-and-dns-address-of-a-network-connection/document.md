# How do I obtain the NIC link address and DNS address of a network connection?

Use [connection.getConnectionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetconnectionproperties) to obtain the connection information of the network corresponding to **netHandle**, such as the NIC link address and DNS address. Before using this API, you must have the **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO** permissions. The code snippet is as follows:

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetConnectionProperties {
  getConnectionProperties() {
    connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
      connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
        if (error) {
          console.error(\`Failed to get connection properties. Code:${error.code}, message:${error.message}\`);
          return;
        }
        console.info('Succeeded to get data: ' + JSON.stringify(data));
      })
    });
  }

  build() {
    Column({ space: 10 }) {
      Button('Obtain Network Connection Info')
        .onClick(() => {
          this.getConnectionProperties();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
