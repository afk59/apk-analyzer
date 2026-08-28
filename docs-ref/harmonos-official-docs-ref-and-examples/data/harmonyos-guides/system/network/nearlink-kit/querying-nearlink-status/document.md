# Querying NearLink Status

#### Use Cases

Before using NearLink, you need to manually enable the NearLink service in the device settings. You can obtain the NearLink status either by querying or subscribing, and start the service processes when the status changes to **STATE\_ON**.

#### API Description

You can obtain the NearLink status through proactive queries or subscription notifications.

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[getState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-manager#section87401754163116)(): NearlinkState

 | 

Obtains the NearLink status through proactive queries.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-manager#section13106021163)(type: 'stateChange', callback: Callback<NearlinkState>): void

 | 

Subscribes to the NearLink status change event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-manager#section1552411314504)(type: 'stateChange', callback?: Callback<NearlinkState>): void

 | 

Unsubscribes from the NearLink status change event.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/4fFILGk-Q8aDsAxbaIA6aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062015Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E518D1D6FA083DD3FCE2638B4CDBD74AEBD6E41A01491DFA1D0D9DCEA1FB16BD)

Turning on or off NearLink under **Settings** > **More connectivity options** > **NearLink** on a device (or **Settings** > **NearLink & Bluetooth** > **NearLink** for different products or OS versions) will trigger NearLink status changes.

1.  Import required modules.
    
    import { manager } from '@kit.NearLinkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Query the NearLink status.
    
    try {
      let state : manager.NearlinkState = manager.getState();
      console.info('state = '+ JSON.stringify(state));
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Alternatively, subscribe to NearLink status changes by registering a callback.
    
    let onReceiveEvent:(data: manager.NearlinkState) => void = (data: manager.NearlinkState) => {
      console.info('nearlink state = '+ JSON.stringify(data));
    }
    try {
      manager.on('stateChange', onReceiveEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
4.  Unsubscribe from NearLink status changes. **onReceiveEvent** is the callback defined in [Step 3](#li7116175463320).
    
    try {
      manager.off('stateChange', onReceiveEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
