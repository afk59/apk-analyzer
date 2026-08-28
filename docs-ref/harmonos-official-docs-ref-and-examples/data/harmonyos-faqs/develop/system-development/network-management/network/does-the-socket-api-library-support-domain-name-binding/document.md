# Does the Socket API library support domain name binding?

Socket supports only IP address access, but not domain name access. A domain name can be resolved to the corresponding IP address through DNS.

The code snippet is as follows:

import { connection } from '@kit.NetworkKit';
import { BusinessError } from "@kit.BasicServicesKit"

connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress\[\]) => {
  console.log(JSON.stringify(error));
  console.log(JSON.stringify(data));
})

**Reference**

[connection.getAddressesByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetaddressesbyname)
