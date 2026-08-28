# Network Handover Notification

#### Use Case

When the network signal is weak and the device initiates a network handover (such as from Wi-Fi to cellular or between primary and secondary SIM cards), the device will notify your app upon the start and end of the handover. Then your app can re-establish the link accordingly and swiftly restore services, providing users with a smooth, fast, and low-latency network experience.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-nethandover#section13106021163).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'handoverChange', callback: Callback<HandoverInfo>): void

 | 

Subscribes to network handover information.

 |
| 

off(type: 'handoverChange', callback?: Callback<HandoverInfo>): void

 | 

Unsubscribes from network handover information.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netHandover } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Subscribe to network handover information.
    
    try {
      netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
        if (info.handoverStart) {
          // Callback for the start of network handover. Adjust the data transmission policy based on the suggestion in HandoverStart.
          console.info('handover start');
        } else if (info.handoverComplete) {
          // Callback for the end of network handover. Adjust the network speed and re-establish the link based on the suggestion in HandoverComplete.
          console.info('handover complete');
        }
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Unsubscribe from network handover information after your app process ends.
    
    try {
      netHandover.off('handoverChange');
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
