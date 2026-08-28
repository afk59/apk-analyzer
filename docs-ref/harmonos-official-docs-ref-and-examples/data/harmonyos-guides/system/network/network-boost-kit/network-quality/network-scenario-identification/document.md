# Network Scenario Identification

#### Use Case

Your app can subscribe to network scenario updates. When the real-time or predicted scenario changes, the device will send information to your app, including link type, network scenario type, data transmission policy suggestions, and weak signal information.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-netquality#section132431252185419).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void

 | 

Subscribes to network scenario changes.

 |
| 

off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void

 | 

Unsubscribes from network scenario changes.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netQuality } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Subscribe to network scenario identification data.
    
    try {
      netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
        if (list.length > 0) {
          list.forEach((sceneInfo) => {
            // Process the network scenario identification callback information.
            if (sceneInfo.scene == 'congestion') {
              // Process the network congestion.
            }
            if (sceneInfo.weakSignalPrediction) {
              // Process the predicted weak signal information.
            }
          });
        }
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Unsubscribe from network scenario identification data after your app process ends.
    
    try {
      netQuality.off('netSceneChange'); 
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
