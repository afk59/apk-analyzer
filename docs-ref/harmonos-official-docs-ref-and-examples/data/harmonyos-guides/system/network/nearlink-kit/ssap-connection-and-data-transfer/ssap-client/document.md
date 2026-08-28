# SSAP Client

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/L9iModxgSt2allkpR1mgFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062015Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BFC8B3796B0F234183ADF0CDC7DE90E72A5F4182407E6EA434505D7748F315C)

You can use SSAP client-related capabilities such as connection to the client, data transfer with the client, and service operations.

#### Use Cases

These capabilities provide client devices with the capability to connect to the server for data transfer.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[createClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section1855815061418)(address: string): Client

 | 

Creates an SSAP client instance.

 |
| 

[connect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section0465155481619)(): Promise<void>

 | 

Initiates a connection to the server.

 |
| 

[getServices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section10154105183620)(): Promise<Array<Service>>

 | 

Obtains a list of services supported by the server.

 |
| 

[readProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section447518180514)(property: Property): Promise<Property>

 | 

Reads a property from the server.

 |
| 

[writeProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section12565420144911)(property: Property, writeType: PropertyWriteType): Promise<void>

 | 

Writes a property to the server.

 |
| 

[setPropertyNotification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section579174605120)(property: Property, enable: boolean): Promise<void>

 | 

Enables or disables a property change notification.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section75631811278)(type: 'propertyChange', callback: Callback<Property>): void

 | 

Subscribes to the property change event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section145567317291)(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void

 | 

Subscribes to the connection status change event.

 |

#### Development Procedure

1.  Import required modules.
    
    import { ssap } from '@kit.NearLinkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create an SSAP client instance. **addr** indicates the remote device address obtained through [scanning](../../initiating-nearlink-scanning/document.md).
    
    let addr: string = '00:11:22:33:AA:FF'; // Remote device address obtained through scanning.
    let client: ssap.Client;
    try {
      client = ssap.createClient(addr);
      console.info('client: ' + JSON.stringify(client));
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Subscribe to the connection status change event. The **client** object is created in [Step 2](#li8347174101218). The object will be used in the following steps.
    
    let onReceiveConnectionChangeEvent:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
      console.info('data:'+ JSON.stringify(data));
    }
    try {
      client.on('connectionStateChange', onReceiveConnectionChangeEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
4.  Subscribe to the property change event.
    
    let onReceivePropertyChangeEvent:(data: ssap.Property) => void = (data: ssap.Property) => {
      console.info('data:'+ JSON.stringify(data));
    }
    try {
      client.on('propertyChange', onReceivePropertyChangeEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
5.  Initiate a connection to the server. After the connection is successful, you will receive the callback for connection status changes subscribed to in [Step 3](#li1990714891216). Then, you can perform data transfer.
    
    try {
      client.connect().then(() => {
        console.info("connect success");
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
6.  Obtain a list of services supported by the server.
    
    try {
      client.getServices().then((result: Array<ssap.Service>) => {
        console.info('getServices successfully:' + JSON.stringify(result));
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
7.  Read the property value of a specified service. The values of [serviceUuid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section9708731141914) and [propertyUuid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section9708731141914) in **property** are obtained in [Step 6](#li167991110128).
    
    try {
      // Create a property. During actual development, the property needs to be obtained from the server through the **getServices** API.
      let arrayBufferC = new ArrayBuffer(1);
      let properV = new Uint8Array(arrayBufferC);
      properV\[0\] = 1;
      let property: ssap.Property = {
        serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
        propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
        value: arrayBufferC
      };
      client.readProperty(property).then((result: ssap.Property) => {
        console.info('readProperty successfully:' + JSON.stringify(result));
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
8.  Write the property value of a specified service. The values of [serviceUuid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section9708731141914) and [propertyUuid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section9708731141914) in **property** are obtained in [Step 6](#li167991110128).
    
    try {
      let arrayBufferC = new ArrayBuffer(1);
      // Value of the property expected to be written.
      let properV = new Uint8Array(arrayBufferC);
      properV\[0\] = 1;
      let property: ssap.Property = {
        serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
        propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
        value: arrayBufferC
      };
      client.writeProperty(property, ssap.PropertyWriteType.WRITE\_NO\_RESPONSE).then(() => {
        console.info('writeProperty success');
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
9.  Enable the property change notification. The values of [serviceUuid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section9708731141914) and [propertyUuid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section9708731141914) in **property** are obtained in [Step 6](#li167991110128).
    
    If a property value changes on the server, the client will receive updated data through the event subscribed to in [Step 4](#li139331061219).
    
    try {
      let arrayBufferC = new ArrayBuffer(1);
      let properV = new Uint8Array(arrayBufferC);
      properV\[0\] = 1;
      let property: ssap.Property = {
        serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
        propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
        value: arrayBufferC
      };
      client.setPropertyNotification(property, true).then(() => {
        console.info('setPropertyNotification success');
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    

#### Sample Code

For details about the sample code for the SSAP client function, see the implementation method in **entry/src/main/ets/pages/SsapClientPage.ets** of the [NearLink Kit Sample Code](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code).
