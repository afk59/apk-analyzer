# Sending NearLink Advertising Packets

#### Use Cases

A device can send NearLink advertising packets to get scanned by a central device with NearLink capabilities.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[startAdvertising](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-advertising#section87401754163116)(advertisingParams: AdvertisingParams): Promise<number>

 | 

Starts NearLink advertising.

 |
| 

[stopAdvertising](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-advertising#section1238104011424)(advertisingId: number): Promise<void>

 | 

Stops NearLink advertising.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-advertising#section13106021163)(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void

 | 

Subscribes to the NearLink advertising status change event.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-advertising#section1552411314504)(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void

 | 

Unsubscribes from the NearLink advertising status change event.

 |

#### Development Procedure

1.  Import required modules.
    
    import { advertising } from '@kit.NearLinkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Subscribe to the NearLink advertising status change event.
    
    let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void = (data: advertising.AdvertisingStateChangeInfo) => {
      console.info('advertisingId:'+ data.advertisingId);
      console.info('advertisingState:'+ data.state);
    }
    try {
      advertising.on('advertisingStateChange', onReceiveEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Construct desired advertising parameters and data.
    
    let manufactureValueBuffer = new Uint8Array(4);
    manufactureValueBuffer\[0\] = 1;
    manufactureValueBuffer\[1\] = 2;
    manufactureValueBuffer\[2\] = 3;
    manufactureValueBuffer\[3\] = 4;
    let serviceValueBuffer = new Uint8Array(4);
    serviceValueBuffer\[0\] = 4;
    serviceValueBuffer\[1\] = 6;
    serviceValueBuffer\[2\] = 7;
    serviceValueBuffer\[3\] = 8;
    console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
    console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
    let setting: advertising.AdvertisingSettings = {
      interval:5000,
      power:advertising.TxPowerMode.ADV\_TX\_POWER\_LOW
    };
    let manufactureDataUnit: advertising.ManufacturerData = {
      manufacturerId:4567,
      manufacturerData:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: advertising.ServiceData = {
      serviceUuid:"37bea880-fc70-11ea-b720-000000001234",
      serviceData:serviceValueBuffer.buffer
    };
    let advData: advertising.AdvertisingData = {
      serviceUuids:\["37bea880-fc70-11ea-b720-000000001234"\],
      manufacturerData:\[manufactureDataUnit\],
      serviceData:\[serviceDataUnit\]
    };
    let advertisingParams: advertising.AdvertisingParams = {
      advertisingSettings: setting,
      advertisingData: advData
    };
    
4.  Start NearLink advertising. The returned **advertisingId** indicates the current advertising index.
    
    let advId = -1;
    try {
      advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
        advId = advertisingId;
        console.info('advertising id:'+ JSON.stringify(advId));
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
5.  Stop NearLink advertising. The value of **advId** is that of **advertisingId** returned after advertising is started in [step 4](#li18315388294).
    
    try {
      advertising.stopAdvertising(advId).then(() => {
          console.info("stop advertising success");
        }).catch ((err: BusinessError) => {
          console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
        });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
6.  Unsubscribe from the NearLink advertising status change event.
    
    try {
      advertising.off('advertisingStateChang_e_', onReceiveEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    

#### Sample Code

For details about the sample code for the NearLink advertising scenario, see the implementation method in **entry/src/main/ets/pages/MainPage.ets** of the [NearLink Kit Sample Code](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code).
