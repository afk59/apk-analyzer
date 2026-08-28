# Initiating NearLink Scanning

#### Use Cases

A central device can initiate NearLink scanning to discover peripheral devices that are sending NearLink advertising packets.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[startScan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-scan#section87401754163116)(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void>

 | 

Starts NearLink scanning.

 |
| 

[stopScan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-scan#section11322144811298)(): Promise<void>

 | 

Stops NearLink scanning.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-scan#section13106021163)(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void

 | 

Subscribes to scanning results.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-scan#section1552411314504)(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void

 | 

Unsubscribes from scanning results.

 |

#### Development Procedure

1.  Import required modules.
    
    import { scan } from '@kit.NearLinkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { util } from '@kit.ArkTS';
    
2.  Define the scanning result callback and parse the scanning result.
    
    const SLE\_ADV\_DATA\_TYPE\_DISCOVERY\_LEVEL = 0x01;
    const SLE\_ADV\_DATA\_TYPE\_SERVICE\_DATA\_16BIT\_UUID = 0x03;
    const SLE\_ADV\_DATA\_TYPE\_SERVICE\_DATA\_128BIT\_UUID = 0x04;
    const SLE\_ADV\_DATA\_TYPE\_COMPLETE\_LIST\_OF\_16BIT\_SERVICE\_UUIDS = 0x05;
    const SLE\_ADV\_DATA\_TYPE\_COMPLETE\_LIST\_OF\_128BIT\_SERVICE\_UUIDS = 0x06;
    const SLE\_ADV\_DATA\_TYPE\_INCOMPLETE\_LIST\_OF\_16BIT\_SERVICE\_UUIDS = 0x07;
    const SLE\_ADV\_DATA\_TYPE\_INCOMPLETE\_LIST\_OF\_128BIT\_SERVICE\_UUIDS = 0x08;
    const SLE\_ADV\_DATA\_TYPE\_SHORTENED\_LOCAL\_NAME = 0x0A;
    const SLE\_ADV\_DATA\_TYPE\_COMPLETE\_LOCAL\_NAME = 0x0B;
    const SLE\_ADV\_DATA\_TYPE\_MANUFACTURER\_SPECIFIC\_DATA = 0xFF;
    
    const NEARLINK\_UUID\_16\_BIT\_LENGTH = 2;
    const NEARLINK\_UUID\_128\_BIT\_LENGTH = 16;
    
    const NEARLINK\_MANUFACTURE\_ID\_LENGTH = 2;
    
    // Define the scanning result callback.
    let onReceiveEvent:(data: Array<scan.ScanResults>) => void = (data: Array<scan.ScanResults>) => {
      console.info('scan result addr:'+ data\[0\].address + 'name:' + data\[0\].deviceName);
      parseScanResult(data\[0\].data);
    }
    
    // Parse the scanning result based on the data type.
    function parseScanResult(data: ArrayBuffer) {
      let advData = new Uint8Array(data);
      if (advData.byteLength == 0) {
        console.warn('nothing, adv data length is 0');
        return;
      }
      console.info('advData: ' + JSON.stringify(advData));
    
      let discoveryLevel: number = -1;
      let serviceData: Record<string, Uint8Array> = {};
      let standardUuids: string\[\] = \[\];
      let specificUuids: string\[\] = \[\];
      let localName: string = "";
      let manufactureSpecificData: Record<number, Uint8Array> = {};
    
      let curPos: number= 0;
      while (curPos < advData.byteLength) {
        let advDataType: number = advData\[curPos++\];
        let advDataLength: number = advData\[curPos++\];
        if (advDataLength == 0) {
          break;
        }
        switch (advDataType) {
          case SLE\_ADV\_DATA\_TYPE\_DISCOVERY\_LEVEL: // Discovery level.
            discoveryLevel = advData\[curPos\];
            break;
          case SLE\_ADV\_DATA\_TYPE\_SERVICE\_DATA\_16BIT\_UUID: // Standard service data information.
            parseServiceData(NEARLINK\_UUID\_16\_BIT\_LENGTH, curPos, advDataLength, advData, serviceData);
            break;
          case SLE\_ADV\_DATA\_TYPE\_SERVICE\_DATA\_128BIT\_UUID: // Custom service data information.
            parseServiceData(NEARLINK\_UUID\_128\_BIT\_LENGTH, curPos, advDataLength, advData, serviceData);
            break;
          case SLE\_ADV\_DATA\_TYPE\_COMPLETE\_LIST\_OF\_16BIT\_SERVICE\_UUIDS: // Complete standard service identifier list.
          case SLE\_ADV\_DATA\_TYPE\_INCOMPLETE\_LIST\_OF\_16BIT\_SERVICE\_UUIDS: // Partial standard service identifier list.
            parseServiceUuid(NEARLINK\_UUID\_16\_BIT\_LENGTH, curPos, advDataLength, advData, standardUuids);
            break;
          case SLE\_ADV\_DATA\_TYPE\_COMPLETE\_LIST\_OF\_128BIT\_SERVICE\_UUIDS: // Complete custom service identifier list.
          case SLE\_ADV\_DATA\_TYPE\_INCOMPLETE\_LIST\_OF\_128BIT\_SERVICE\_UUIDS: // Partial custom service identifier list.
            parseServiceUuid(NEARLINK\_UUID\_128\_BIT\_LENGTH, curPos, advDataLength, advData, specificUuids);
            break;
          case SLE\_ADV\_DATA\_TYPE\_SHORTENED\_LOCAL\_NAME: // Abbreviated local name of the device.
          case SLE\_ADV\_DATA\_TYPE\_COMPLETE\_LOCAL\_NAME: // Full local name of the device.
            let tmpName: Uint8Array = advData.slice(curPos, curPos + advDataLength);
            let decoder = util.TextDecoder.create('utf-8');
            localName = decoder.decodeToString(new Uint8Array(tmpName));
            break;
          case SLE\_ADV\_DATA\_TYPE\_MANUFACTURER\_SPECIFIC\_DATA: // Manufacturer-defined information.
            parseManufactureData(curPos, advDataLength, advData, manufactureSpecificData);
            break;
          default:
            break;
        }
        curPos += advDataLength;
      }
    }
    
    // Parse the service data information.
    function parseServiceData (uuidLength: number, curPos: number, advDataLength: number,
      advData: Uint8Array, serviceData: Record<string, Uint8Array>) {
      let tmpUuid: Uint8Array = advData.slice(curPos, curPos + uuidLength);
      getUuidFromUint8Array(uuidLength, tmpUuid); 
      let tmpValue: Uint8Array = advData.slice(curPos + uuidLength, curPos + advDataLength);
      serviceData\[tmpUuid.toString()\] = tmpValue;
    }
    
    // Parse the service identifier list.
    function parseServiceUuid (uuidLength: number, curPos: number, advDataLength: number,
      advData: Uint8Array, serviceUuids: string\[\]) {
      while (advDataLength > 0) {
        let tmpData: Uint8Array = advData.slice(curPos, curPos + uuidLength);
        serviceUuids.push(getUuidFromUint8Array(uuidLength, tmpData));
        advDataLength -= uuidLength;
        curPos += uuidLength;
      }
    }
    
    // Parse the manufacturer-defined information.
    function parseManufactureData(curPos: number, advDataLength: number,
      advData: Uint8Array, manufactureSpecificData: Record<number, Uint8Array>) {
        let manufactureId: number = (advData\[curPos + 1\] << 8) + advData\[curPos\];
        let tmpValue: Uint8Array = advData.slice(curPos + NEARLINK\_MANUFACTURE\_ID\_LENGTH, curPos + advDataLength);
        manufactureSpecificData\[manufactureId\] = tmpValue;
    }
    
    // Parse UUIDs.
    function getUuidFromUint8Array(uuidLength: number, uuidData: Uint8Array): string {
      let uuid: string = '';
      let temp: string = '';
      for (let i = uuidLength - 1; i > -1; i--) {
        temp += uuidData\[i\].toString(16).padStart(2, '0');
      }
      switch (uuidLength) {
        case NEARLINK\_UUID\_16\_BIT\_LENGTH:
          uuid = \`37BEA880-FC70-11EA-B720-00000000${temp}\`;
          break;
        case NEARLINK\_UUID\_128\_BIT\_LENGTH:
          uuid = \`${temp.substring(0, 8)}-${temp.substring(8, 12)}-${temp.substring(12, 16)}-${temp.substring(16,
              20)}-${temp.substring(20, 32)}\`;
          break;
        default:
          break;
      }
      return uuid;
    }
    
3.  Subscribe to scanning results.
    
    try {
      scan.on("deviceFound", onReceiveEvent);
      // Subscribe to NearLink scanning results. The address carried in the scanning result is a random address of the remote device.
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
4.  Configure scanning parameters, such as a desired device name and address for a scan filter.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/I3N4ZsSWSP6VYOOIzbko4Q/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062015Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4A6ED9117E5DCF943BB6E88927F89AA189B37712179DAEF11564D0B307B5525)
    
    1.  A scan filter must contain at least one condition. Otherwise, the filter is invalid.
    2.  You can configure multiple filter groups, and the conditions between the groups are in an "OR" relationship (which means that only one group's conditions need to be met), as described in [Step 5](#li1359217817358).
    3.  Within a group, the conditions are in an "AND" relationship (which means that all conditions need to be met). For example, a scanning result can be reported only when both **address** and **deviceName** are met.
    
    let scanFilter1: scan.ScanFilters = {
      address:"11:22:33:44:AA:BB", // Address of the peripheral device 1 that is expected to be scanned.
      deviceName:"deviceName1" // Name of the peripheral device 1 that is expected to be scanned.
    };
    let scanFilter2: scan.ScanFilters = {
      address:"22:33:44:AB:CD:EF", // Address of the peripheral device 2 that is expected to be scanned.
      deviceName:"deviceName2" // Name of the peripheral device 2 that is expected to be scanned.
    };
    let scanOptions: scan.ScanOptions = {
      scanMode: scan.ScanMode.SCAN\_MODE\_LOW\_POWER
    }
    
5.  Start NearLink scanning. For details about parameter settings, see [Step 4](#li429915715350).
    
    try {
      scan.startScan(\[scanFilter1, scanFilter2\], scanOptions).then(() => {
        console.info("start scan success");
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
6.  Stop NearLink scanning.
    
    try {
      scan.stopScan().then(() => {
        console.info("stop scan success");
      }).catch ((err: BusinessError) => {
        console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      });
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
7.  Unsubscribe from scanning results. **onReceiveEvent** is the callback registered in [Step 2](#li2668635103812).
    
    try {
      scan.off("deviceFound", onReceiveEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    

#### Sample Code

For details about the sample code for the NearLink scanning scenario, see the implementation method in **entry/src/main/ets/pages/ScanConfigPage.ets** of the [NearLink Kit Sample Code](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code).
