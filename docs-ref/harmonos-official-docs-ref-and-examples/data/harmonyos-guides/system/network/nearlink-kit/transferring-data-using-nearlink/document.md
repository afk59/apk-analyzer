# Transferring Data Using NearLink

You can establish ports for data transfer and execute data transfer. A device can be both the sending port and receiving port.

#### Use Cases

NearLink-based data transfer is supported since version 5.1.0(18), including port registration, connection establishment, and data read/write.

Your app can transfer data between devices through Nearlink, based on the logical link established between the devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/KiPC8qidTjWe6RYewqdzoQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062015Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=699CD921E9B4A817F31A40422D5D73353AF2E766CB560A6A2BAC00059A4A930F)

1\. Data transfer links are not encrypted by default. You need to call the [startPairing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-remote-device#section65252361113) API to start the pairing process before performing encrypted data transfer.

2\. Call the [getAcbState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-remote-device#section945162120309) API to check if a data transfer link is encrypted. **ENCRYPTED** indicates the data link is encrypted.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[createPort](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-data-transfer-api#section19932155019)(uuid: string): void

 | 

Registers a port.

 |
| 

[connect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-data-transfer-api#section1047122612211)(params: ConnectionParams): Promise<void>

 | 

Connects to a remote device and establishes a port.

 |
| 

[writeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-data-transfer-api#section5484100194119)(params: DataParams): Promise<void>

 | 

Sends data to a remote device using the device address and UUID.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-data-transfer-api#section1259823863112)(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void

 | 

Subscribes to the port connection status change event.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-data-transfer-api#section5547151720408)(type: 'readData', callback: Callback<DataParams>): void

 | 

Subscribes to the port data receiving event.

 |

#### Development Procedure

1.  Import required modules.
    
    import { dataTransfer } from '@kit.NearLinkKit';
    import { remoteDevice } from '@kit.NearLinkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  (Optional) Encrypt the pairing between the local device and the remote device. (This step is required for encrypted data transfer.) After this step is performed, different types of dialog boxes will be displayed based on the input and output capability flags of both the local and remote devices. The user will need to confirm the pairing. Currently, the following dialog boxes are supported: dialog box for pairing without input, dialog box for comparing numbers, and dialog box for passcode authentication.
    
    let addr: string = '00:11:22:33:AA:FF'; // Remote device address obtained through scanning.
    let device: remoteDevice.RemoteDevice;
    try {
      device = remoteDevice.createRemoteDevice(addr);
      device.startPairing().then(()=>{
        console.info('start pairing success');
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  Register ports, including data sending and receiving ports. The UUID of the sending port must be the same as that of the receiving port.
    
    let serviceUuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // NearLink service UUID. Here uses a custom service UUID as an example.
    try {
      dataTransfer.createPort(serviceUuid);
      console.info('create port success');
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
4.  Subscribe to the port connection status change event.
    
    let onReceiveConnectionStateEvent:(data: dataTransfer.ConnectionResult) => void = (data: dataTransfer.ConnectionResult) => {
      console.info('data: ' + JSON.stringify(data));
    }
    try {
      dataTransfer.on('connectionStateChanged', onReceiveConnectionStateEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
5.  Subscribe to the port data receiving event.
    
    let onReceiveReadDataEvent:(data: dataTransfer.DataParams) => void = (data: dataTransfer.DataParams) => {
      console.info('data: ' + JSON.stringify(data));
    }
    try {
      dataTransfer.on('readData', onReceiveReadDataEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
6.  Connect to a remote device and establish a port. The UUID must be the same as that of the ports registered in [Step 3](#li1311118434818).
    
      // Construct parameters for establishing a port.
    let connectionParams:dataTransfer.ConnectionParams = {
      address: addr, // Remote device address obtained through scanning.
      uuid: serviceUuid, // NearLink service UUID.
        mtu: 1024, // Size of the data packet expected to be sent, in bytes. This parameter is optional.
    };
    try {
      dataTransfer.connect(connectionParams).then(()=>{
        console.info('connect success');
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
7.  Send data to the remote device using the device address and UUID. The UUID must be the same as that of the ports registered in [Step 3](#li1311118434818).
    
      // Construct parameters for data sending.
    let transferValueBuffer: Uint8Array = new Uint8Array(4);
    transferValueBuffer\[0\] = 1;
    transferValueBuffer\[1\] = 2;
    transferValueBuffer\[2\] = 3;
    transferValueBuffer\[3\] = 4;
    let dataParams: dataTransfer.DataParams = {
      address: addr, // Address of the remote NearLink device.
      uuid: serviceUuid, // NearLink service UUID.
      data: transferValueBuffer.buffer, // Data to be transferred between NearLink devices.
    };
    try {
      dataTransfer.writeData(dataParams).then(() => {
        console.info('writeData success');
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
