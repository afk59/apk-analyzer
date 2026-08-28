# Handover Mode Setting

#### Use Case

Your app can call the relevant API to change the network handover mode between delegation mode and proactive mode.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-nethandover#section82308124011).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

setHandoverMode(mode: HandoverMode): void

 | 

Sets the network handover mode for your app. The delegation mode is used by default.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netHandover} from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the **setHandoverMode** API to set the mode to proactive mode, forbidding the device to initiate handovers by itself.
    
    try{
      let mode: netHandover.HandoverMode = netHandover.HandoverMode.DISCRETION;
      netHandover.setHandoverMode(mode);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
