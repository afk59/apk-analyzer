# Network Quality Assessment

#### Use Case

Your app can subscribe to network quality QoS assessment data. The device will periodically send updates or notify you when QoS changes. The returned QoS data includes the link type, real-time bandwidth and rate of the uplink and downlink air interface, and RTT delay.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-netquality#section13106021163).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void

 | 

Subscribes to QoS state changes.

 |
| 

off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void

 | 

Unsubscribes from QoS state changes.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netQuality } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Subscribe to network quality assessment information.
    
    try {
      netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
        if (list.length > 0) {
          list.forEach((qos) => {
            // Callback information processing.
            console.info(\`Data link type: ${JSON.stringify(qos.pathType )}.\` );
            console.info(\`Uplink bandwidth of the data link type: ${JSON.stringify(qos.linkUpBandwidth)}.\` );
            console.info(\`Downlink bandwidth of the data link type: ${JSON.stringify(qos.linkDownBandwidth)}.\` );
            // The unit is bit/s. You can divide the value by 8 to convert it to byte/s.
            console.info(\`Uplink rate of the data link type: ${JSON.stringify(qos.linkUpRate)}.\` );
            // The unit is bit/s. You can divide the value by 8 to convert it to byte/s.
            console.info(\`Downlink rate of the data link type: ${JSON.stringify(qos.linkDownRate)}.\` );
            // The real-time rate is the sum of the uplink and downlink rates.
            console.info(\`Real-time rate of the data link type (in byte/s): ${JSON.stringify((qos.linkUpRate + qos.linkDownRate)/8)}.\`);
            console.info(\`RTT delay of the data link type: ${JSON.stringify(qos.rttMs)}.\` );
            console.info(\`Uplink transmission air-interface buffer delay of the data link type: ${JSON.stringify(qos.linkUpBufferDelayMs )}.\`);
          });
        }
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Unsubscribe from the network quality assessment information after your app process ends.
    
    try {
      netQuality.off('netQosChange'); 
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
