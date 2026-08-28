# Setting the Service Scenario

#### Use Case

You can set the service scenario for your app before requesting multi-network concurrency, so the device can manage multi-network concurrency and perform service duration analysis accordingly.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-netboost#section13106021163).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

setSceneDesc(sceneDesc : SceneDesc): void

 | 

Sets the service scenario.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netBoost } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Set the service scenario.
    
    try {
      let sceneDesc : netBoost.SceneDesc = {
        scene : 'realtimeVoice',
        sceneEvent : netBoost.SceneEvent.SCENE\_EVENT\_ENTER
      }
      netBoost.setSceneDesc(sceneDesc);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
