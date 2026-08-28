# SSAP Server

You can use SparkLink Service Access Protocol (SSAP) server-related capabilities such as connection to the server, data transfer with the server, and service management.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/1MaSaIgtTj20r4BlBS9UXg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062015Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2426E12765FEB6BF0A1F100CD9B2306E949A011E07ADD2D648FBE3575A87BD38)

After an SSAP connection is established, the SSAP server stops advertising automatically. If the server expects to be discovered by clients, you can re-initiate advertising by referring to [Sending NearLink Advertising Packets](../../sending-nearlink-advertising-packets/document.md).

#### Use Cases

These capabilities allow your app to transfer data using NearLink. You can connect client devices to the server for data transfer.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[createServer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section383817192117)(): Server

 | 

Creates an SSAP server instance.

 |
| 

[addService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section169891248173012)(service: Service): void

 | 

Adds a service to the server.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section168082298487)(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void

 | 

Subscribes to the connection status change event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section16823110115120)(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void

 | 

Subscribes to the client read request event.

 |
| 

[sendResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section299716275465)(response: ServerResponse): void

 | 

Responds to read or write requests from the client.

 |
| 

[notifyPropertyChanged](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-ssap#section19961193482813)(address: string, property: Property): Promise<void>

 | 

Notifies the client of property value updates.

 |

#### Development Procedure

1.  Import required modules.
    
    import { ssap } from '@kit.NearLinkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create an SSAP server instance.
    
    let server: ssap.Server;
    try {
      server = ssap.createServer();
      console.info('server: ' + JSON.stringify(server));
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Add a service supported by the server. The **server** object is created in [Step 2](#li155814147593). The object will be used in the following steps.
    
    // Construct a descriptor.
    let descriptorsArray: Array<ssap.PropertyDescriptor> = \[\];
    let arrayBuffer = new ArrayBuffer(2);
    let descValue = new Uint8Array(arrayBuffer);
    descValue\[0\] = 11;
    descValue\[1\] = 22;
    let descriptor: ssap.PropertyDescriptor = {
      serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
      propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
      value: arrayBuffer,
      descriptorType:ssap.PropertyDescriptorType.PROPERTY,
      isWriteable:true
    };
    descriptorsArray\[0\] = descriptor;
    // Construct properties.
    let propertiesArray: Array<ssap.Property> = \[\];
    let arrayBufferProperty = new ArrayBuffer(1);
    let properValue = new Uint8Array(arrayBufferProperty);
    properValue\[0\] = 1;
    let property1: ssap.Property = {
      serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
      propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
      value: arrayBufferProperty,
      descriptors:descriptorsArray,
      operation:3 // The property is readable and writable.
    };
    let property2: ssap.Property = {
      serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
      propertyUuid: '37bea880-fc70-11ea-b720-000000003421',
      value: arrayBufferProperty,
      descriptors:descriptorsArray,
      operation:3 // The property is readable and writable.
    };
    propertiesArray\[0\] = property1;
    propertiesArray\[1\] = property2;
    // Construct a service.
    let Service: ssap.Service = {
      serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
      properties:propertiesArray
    };
    try {
      server.addService(Service);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
4.  Subscribe to the connection status change event.
    
    let onReceiveConnectionChangeEvent:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
      console.info('data:'+ JSON.stringify(data));
    }
    try {
      server.on('connectionStateChange', onReceiveConnectionChangeEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
5.  Subscribe to the client read request event.
    
    let onReceivePropertyReadEvent:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
      console.info('data:'+ JSON.stringify(data));
    }
    try {
      server.on('propertyRead', onReceivePropertyReadEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
6.  Respond to the client read request after it is received. A read request is subscribed to according to [Step 5](#li1776019142546).
    
    // After receiving a read or write request, respond to the request through this API.
    let arrayBuffer = new ArrayBuffer(2);
    let descValue = new Uint8Array(arrayBuffer);
    descValue\[0\] = 11;
    descValue\[1\] = 22;
    let resp: ssap.ServerResponse = {
      address: '00:11:22:33:AA:FF', // Address of a requester client.
      requestId: 1, // Request ID.
      value: arrayBuffer // Response data.
    };
    try {
      // This address is that of the connected client device and is cached on the server.
      server.sendResponse(resp);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
7.  Notify the client of property value updates. **address** indicates the address of the connected client device obtained in [Step 4](#li629472212549).
    
    // Construct properties.
    let arrayBufferProperty = new ArrayBuffer(8);
    let properValue = new Uint8Array(arrayBufferProperty);
    properValue\[0\] = 123; // Value after the update.
    let property: ssap.Property = {
      serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
      propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
      value: arrayBufferProperty,
    };
    try {
      let address = '00:11:22:33:AA:FF'; // Address of the connected device.
      server.notifyPropertyChanged(address, property).then(() => {
        console.info('notifyPropertyChanged success');
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    

#### Sample Code

For details about the sample code for the SSAP server function, see the implementation method in **entry/src/main/ets/pages/SsapServerPage.ets** of the [NearLink Kit Sample Code](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code).
