# Cross-Device Sync of KV Stores (ArkTS)

#### When to Use

KV Stores are suitable for storing service data with simple relationships. It provides higher read and write performance than the SQL database. KV stores are widely used because the simplicity of the KV data model poses fewer database version compatibility issues in distributed scenarios and simplifies conflict handling in cross-device data sync.

#### Basic Concepts

Before implementing cross-device data sync of KV stores, understand the following concepts:

## Single KV Store

In a single KV store, data is stored locally as individual entries. When data is modified, the change is applied directly to the entry. After sync, only one global copy of the data is retained across multiple devices. If multiple devices have the same record (with the same primary key), the latest version is preserved irrespective of the device. If data with the same key is modified on multiple devices, the latest change will overwrite the previous ones. For the data written or modified locally, the data with the latest time is synced to other devices. Single KV store is used to store information, such as the contacts and weather application data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/eO8NBOcaRI-i8SNRg6Nn4w/en-us_image_0000002537764372.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EDB36415D2989A5BA06588A265A53B33650EF7B483CABA7A70A62BB86660597)

## Device KV Store

In a device KV store, the local device ID is added before the key of the KV pair stored by an application. In this way, the data of different devices is isolated. Data is managed by device and can be queried by device.

The underlying devices manage the data by device. The device KV stores support distributed data query by device, but do not support modification of the data synced from peer devices. Device KV stores are used to store the data that needs to be accessed by device, such as the Gallery thumbnails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/9hQVCXjwQgqmDTBcnQWYRg/en-us_image_0000002537924312.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CE17CB305004D491E6CC75A6B8D40861A0499AD9E131538DC083243FE21E042)

#### Sync Types

The data management service provides two sync types: manual sync and auto sync. You can use either mode to sync the data of an application across devices:

## Manual Sync

The application calls **sync()** with the devices to be synced and the sync mode specified to trigger the sync. The sync mode can be **PULL\_ONLY** (pulling remote data to the local end), **PUSH\_ONLY** (pushing local data to the remote end), or **PUSH\_PULL** (pushing local data to the remote end and pulling remote data to the local end). You can use the [**sync()** with the **query** parameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedkvstore#sync-1) to sync the data that meets the specified conditions.

## Auto Sync

In multi-device collaboration via cross-device calls, after an application updates data, the distributed database automatically pushes the local data to the peer ends and pulls the peer data to the local device for data sync. In this case, the application does not need to call sync().

#### Working Principles

After completing device discovery and authentication, the underlying communication component notifies the application that the device goes online. The **DatamgrService** then establishes an encrypted transmission channel to sync data between the two devices.

## Cross-Device Data Sync Mechanism

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/aMY4jgEkTOmRAHlFF76cPQ/en-us_image_0000002568684089.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=787BED73A4B6E2A7356050A7576E151B376793C752BC106B89532A9E31309D3F)

When **put()** or **delete()** is called successfully, an auto sync is triggered. The distributed data is sent to the peer device through the communication adaptation layer for sync.

If **sync()** is called successfully, a manual sync is triggered to send distributed data to the peer device through the communication adaptation layer.

## Data Change Notification Mechanism

When data is added, deleted, or modified, a notification is sent to the subscriber. The notifications can be classified into the following types:

-   Local data change notification: subscription of the application data changes on the local device. When the data in the local KV store is added, deleted, or modified in the database, a notification is received.
    
-   Distributed data change notification: subscription of the application data changes of other devices in the network. When the data in the local KV store changes after being synced with data from another device in the same network, a notification is received.
    

#### Constraints

-   For each record in a device KV store, the key cannot exceed 896 bytes and the value cannot exceed 4 MB.
    
-   For each record in a single KV store, the key cannot exceed 1 KB and the value cannot exceed 4 MB.
    
-   The KV stores do not support custom conflict resolution policies for applications.
    
-   An application can open a maximum of 16 distributed KV stores at a time.
    
-   A single KV store supports a maximum of eight listener callbacks for data changes.
    

#### Available APIs

The following table lists the APIs for cross-device data sync of the single KV store. Most of the APIs are executed asynchronously, using a callback or promise to return the result. The following table uses the callback-based APIs as an example. For more information about the APIs, see [Distributed KV Store](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedkvstore).

| API | Description |
| :-- | :-- |
| createKVManager(config: KVManagerConfig): KVManager | Creates a **KvManager** instance to manage database objects. |
| getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void | Obtains a KV store of the specified type. |
| put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void | Inserts and updates data. |
| on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void | Subscribes to data changes in the KV store. |
| get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void | Queries the value of the specified key. |
| sync(deviceIds: string\[\], mode: SyncMode, delayMs?: number): void | Triggers a manual sync of the KV store. |

#### How to Develop

The following uses a single KV store as an example to describe how to implement cross-device data sync. The development process is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/B81rJnwoQX6CoAX8WZfQ7A/en-us_image_0000002568764099.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F04094D51791FA27469B68A597414038CCF354120F7E3DAA14CFA871D9873B5C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/4yajaYVYRC22iIrpJ7QP4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87D7A5235E9EBC60654E7A95A5EA82E5F5CCE35127BE3B139793FD146B7F82F2)

The security level of the destination device (to which data is synced) cannot be higher than that of the source device. For details, see [Access Control Mechanism in Cross-Device Sync](../../data-reliability-and-security/access-control-by-device-and-data-level-arkts/document.md#access-control-mechanism-in-cross-device-sync).

1.  Import module to obtain the context.
    
    // Import modules.
    // Create a KvStoreInterface.ets file in the pages directory.
    import { distributedKVStore } from '@kit.ArkData';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { distributedDeviceManager } from '@kit.DistributedServiceKit';
    import EntryAbility from '../entryability/EntryAbility';
    // Logger implements the print feature after Hilog is encapsulated.
    import Logger from '../common/Logger';
    
    let kvManager: distributedKVStore.KVManager | undefined = undefined;
    let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
    let appId: string = 'com.example.kvstoresamples';
    let storeId: string = 'storeId';
    // Obtain the context of the stage model from EntryAbility.ets.
    const context = EntryAbility.getContext();
    
    // Obtain the context of the FA model.
    import { featureAbility } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let context = featureAbility.getContext();
    
    // The code of all the following APIs is implemented in KvInterface.
    export class KvInterface {
    }
    
2.  Request permissions.
    
    1.  Declare the **ohos.permission.DISTRIBUTED\_DATASYNC** permission. For details, see [Declaring Permissions](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
    2.  Display a dialog box to ask for authorization from the user when the application is started for the first time. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
3.  Call the **createKVManager()** method to create a **KvManager** instance.
    
    1.  Create a **kvManagerConfig** object based on the application context.
    2.  Create a **KvManager** instance.
    
    public CreateKvManager = (() => {
      Logger.info('CreateKvManager start');
      if (typeof (kvManager) === 'undefined') {
        const kvManagerConfig: distributedKVStore.KVManagerConfig = {
          bundleName: appId,
          context: context
        };
        try {
          // Create a KVManager instance.
          kvManager = distributedKVStore.createKVManager(kvManagerConfig);
          Logger.info('Succeeded in creating KVManager.');
        } catch (err) {
          Logger.error(\`Failed to create KVManager. Code:${err.code},message:${err.message}\`);
        }
      } else {
        Logger.info ('KVManager has created');
      }
    })
    
4.  Call the **getKVStore()** method to obtain the KV store of the specified type.
    
    1.  Declare the ID of the distributed KV store to create, for example, **'storeId'** in the sample code.
    2.  Disable the auto sync function (**autoSync:false**) to facilitate subsequent verification of the sync feature. If sync is required, call the **sync()** API.
    
    public GetKvStore = (() => {
      Logger.info('GetKvStore start');
      if (kvManager === undefined) {
        Logger.info('KvManager not initialized');
        return;
      }
      try {
        let child1 = new distributedKVStore.FieldNode('id');
        child1.type = distributedKVStore.ValueType.INTEGER;
        child1.nullable = false;
        child1.default = '1';
        let child2 = new distributedKVStore.FieldNode('name');
        child2.type = distributedKVStore.ValueType.STRING;
        child2.nullable = false;
        child2.default = 'zhangsan';
    
        let schema = new distributedKVStore.Schema();
        schema.root.appendChild(child1);
        schema.root.appendChild(child2);
        schema.indexes = \['$.id', '$.name'\];
        // The value 0 indicates the compatible mode, and 1 indicates the strict mode.
        schema.mode = 1;
        // Set the number of bytes to be skipped during the value check. The value range is \[0, 4M-2\].
        schema.skip = 0;
    
        const options: distributedKVStore.Options = {
          createIfMissing: true,
          // Whether to encrypt the KV store.
          encrypt: true,
          backup: false,
          autoSync: false,
          // If kvStoreType is left empty, a device KV store is created by default.
          kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
          // Device KV store: kvStoreType: distributedKVStore.KVStoreType.DEVICE\_COLLABORATION,
          schema: schema,
          // If the schema is not defined, you can leave it empty. For details about how to define the schema, see the example above.
          securityLevel: distributedKVStore.SecurityLevel.S3
        };
        kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeId, options,
          (err, store: distributedKVStore.SingleKVStore) => {
            if (err) {
              Logger.error(\`Failed to get KVStore: Code:${err.code},message:${err.message}\`);
              return;
            }
            Logger.info('Succeeded in getting KVStore.');
            kvStore = store;
            // Before performing related data operations, obtain a KV store instance.
          });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
    
5.  Call the **on()** method to subscribe to distributed data changes. To unsubscribe from the data changes, call [off('dataChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedkvstore#offdatachange).
    
    public On = (() =>{
      Logger.info('On start');
      if(kvStore === undefined) {
        Logger.info('On: kvStore not initialized');
        return;
      }
      try {
        kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE\_TYPE\_ALL, (data) => {
          Logger.info(\`dataChange callback call data: ${data}\`);
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. code:${error.code},message:${error.message}\`);
      }
    })
    
6.  Call the **put()** method to write data to the distributed KV store.
    
    1.  Construct the key and value to be written to the single KV store.
    2.  Write KV pairs to the single KV store.
    
    public Put = (() => {
      Logger.info('Put start');
      if (kvStore === undefined) {
        Logger.info('Put: kvStore not initialized');
        return;
      }
      const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
      // If schema is not defined, pass in other values that meet the requirements.
      const VALUE\_TEST\_STRING\_ELEMENT = '{"id":0, "name":"lisi"}';
      try {
        kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err) => {
          if (err !== undefined) {
            Logger.error(\`Failed to put data. Code:${err.code},message:${err.message}\`);
            return;
          }
          Logger.info('Succeeded in putting data.');
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
    
7.  Query data from the distributed KV store.
    
    1.  Construct the key to be queried from the single KV store.
    2.  Query data from the single KV store.
    
    public Get = (() => {
      Logger.info('Get start');
      if (kvStore === undefined) {
        Logger.info('Get: kvStore not initialized');
        return;
      }
      const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
      try {
        kvStore.get(KEY\_TEST\_STRING\_ELEMENT, (err, data) => {
          if (err != undefined) {
            Logger.error(\`Failed to get data. Code:${err.code},message:${err.message}\`);
            return;
          }
          Logger.info(\`Succeeded in getting data. Data:${data}\`);
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`Failed to get data. Code:${error.code},message:${error.message}\`);
      }
    })
    
8.  Call the **sync()** method to sync data to other devices.
    
    Select the devices to be synced with data and the sync mode. The user needs to confirm the sync mode when the application is started for the first time.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/goiIar5ORGC_EfJE-ueNgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0963E13268368AB13BF79FAC6550FF728803F31268C8504BD621D62FD6FE36B)
    
    In manual sync mode, **deviceIds** can be obtained by using [devManager.getAvailableDeviceListSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributeddevicemanager#getavailabledevicelistsync).
    
    public Sync = (() =>{
      Logger.info('Sync start');
      if(kvStore === undefined) {
        Logger.info('Sync: kvStore not initialized');
        return;
      }
      let devManager: distributedDeviceManager.DeviceManager;
      try {
        // Create deviceManager.
        devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
        // deviceIds is obtained by devManager.getAvailableDeviceListSync.
        let deviceIds: string\[\] = \[\];
        if (devManager != null) {
          let devices = devManager.getAvailableDeviceListSync();
          for (let i = 0; i < devices.length; i++) {
            deviceIds\[i\] = devices\[i\].networkId as string;
          }
        }
        if (deviceIds.length === 0) {
          Logger.info('Sync failed networkId is empty.');
          return;
        }
        try {
          // 1000 indicates the maximum delay, in ms.
          kvStore.sync(deviceIds, distributedKVStore.SyncMode.PUSH\_PULL, 1000);
        } catch (e) {
          let error = e as BusinessError;
          Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
        }
      } catch (err) {
        let error = err as BusinessError;
        Logger.error('createDeviceManager errCode:' + error.code + ',errMessage:' + error.message);
      }
    })
