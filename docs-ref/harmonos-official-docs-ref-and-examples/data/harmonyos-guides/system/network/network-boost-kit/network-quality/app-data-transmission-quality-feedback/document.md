# App Data Transmission Quality Feedback

#### Use Case

When the data transmission performance of your app changes, your app can send the transmission quality and service type data to the network service module of the device via the real-time feedback API. If the performance deteriorates, the module can refine resource scheduling to implement network acceleration.

If frame freezing occurs during video streaming in your app, Network Boost Kit will receive this issue and report it to the network service module. The module will then optimize resource scheduling to accelerate the network.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-netquality#section16821202143413).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

reportQoe(appQoe: AppQoe): void

 | 

Sends transmission quality data to the device.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netQuality } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the **reportQoe** API to notify the device of your app's data transmission quality.
    
    try{
      let serviceType: netQuality.ServiceType = 'shortVideo';
      let qoeType: netQuality.BadQoeCause = 'serverErr';
      let appQoE: netQuality.AppQoe = {
        serviceType,
        qoeType
      };
      netQuality.reportQoe(appQoE);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
