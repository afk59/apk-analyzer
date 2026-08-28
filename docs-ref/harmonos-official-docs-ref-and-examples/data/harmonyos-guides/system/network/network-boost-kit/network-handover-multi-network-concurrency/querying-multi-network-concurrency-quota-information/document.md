# Querying Multi-Network Concurrency Quota Information

#### Use Case

Since multi-network concurrency for network acceleration is governed by quotas, your app can obtain the remaining quota information and allocate the number of acceleration sessions and acceleration duration accordingly. The quota information is updated every 24 hours. If the quota (number of sessions or duration) is used up, access to multi-network concurrency will be restricted, and an error code will be returned. The quota will be re-allocated 24 hours later.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-nethandover#section47829529513).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

getMultiPathQuotaStats(): MultiPathQuota

 | 

Obtains multi-network concurrency quota information.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netHandover } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Obtain multi-network concurrency quota information.
    
    try {
      let multiquota : netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
      // Number of quota sessions already used.
      console.info('getMultiPathQuotaStats multiPathQuota.used.count is:' + multiquota.used.count)
      // Quota duration already used, in seconds.
      console.info('getMultiPathQuotaStats multiPathQuota.used.duration is:' + multiquota.used.duration)
      // Number of quota sessions remaining.
      console.info('getMultiPathQuotaStats multiPathQuota.remaining.count is:' + multiquota.remaining.count)
      // Remaining quota duration, in seconds.
      console.info('getMultiPathQuotaStats multiPathQuota.remaining.durationis:' + multiquota.remaining.duration)
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
