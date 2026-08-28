# How do I determine the IP address version of the current network?

You can use the [NetAddress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#netaddress) class to obtain the address information of the current network. The **family** attribute of the **NetAddress** class is used to specify the IP address version. The value **1** of the **family** attribute indicates **IPv4**, and the value **2** indicates **IPv6**.

The sample code is as follows:

import { connection } from '@kit.NetworkKit';

@Entry
@Component
struct Index {
  getNetworkFamily() {
    try {
      let netHandle = connection.getDefaultNetSync();
      let connectionProperties = connection.getConnectionPropertiesSync(netHandle);
      if (connectionProperties !== undefined) {
        let linkAddressesArray = connectionProperties.linkAddresses;
        if (linkAddressesArray !== undefined && linkAddressesArray instanceof Array && linkAddressesArray.length > 0) {
          for (let i = 0; i < linkAddressesArray.length; i++) {
            let address: connection.NetAddress = linkAddressesArray\[i\].address;
            if (address !== undefined) {
              console.info("Succeeded to get address: " + JSON.stringify(address))
              if (address.family === 1) {
                console.info('Current network IP address version is ipv4')
              } else if (address.family === 2) {
                console.info('Current network IP address version is ipv6')
              }
            }
          }
        }
      }
    } catch (e) {
      console.error(\`Get exception: ${e}\`);
    }
  }

  build() {
    Column({ space: 10 }) {
      Button('Obtain the current network IP address version')
        .onClick(() => {
          this.getNetworkFamily();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
