# Listening to the Multi-Network Concurrency Status

#### Use Case

Your app can listen to the multi-network concurrency status to detect any changes on available network paths and select an appropriate strategy for transmitting data through them.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-nethandover#section7919111205211).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void

 | 

Subscribes to multi-network concurrency status changes.

 |
| 

off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void

 | 

Unsubscribes from multi-network concurrency status changes.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netHandover } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Subscribe to multi-network concurrency status changes.
    
    try {
      netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
        // Callback information processing.
        console.info("on multiPathStateChange: " + JSON.stringify(data));
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Unsubscribe from multi-network concurrency status changes after your app process ends or your app exits.
    
    try {
      netHandover.off('multiPathStateChange');
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
