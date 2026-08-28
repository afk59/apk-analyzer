# How do I find out if a cellular network is used?

You can use the **connection.getNetCapabilities** API provided by the **@kit.NetworkKit** module to obtain the network capability information. If the value of **bearerTypes** is **0**, the network is a cellular network. Before using the API, you must declare the **ohos.permission.GET\_NETWORK\_INFO** permission.

The code snippet is as follows:

import { connection } from '@kit.NetworkKit';

// Check if the network is connected
connection.hasDefaultNet((error, data) => {
  console.log('data: ' + data);
})
// Obtain network capability information
connection.getDefaultNet().then((netHandle) => {
  connection.getNetCapabilities(netHandle, (error, data) => {
    console.log(JSON.stringify(error));
    console.log(JSON.stringify(data));
  })
})

**Reference**

[connection.getNetCapabilities](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilities)

[NetBeartype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#netbeartype)
