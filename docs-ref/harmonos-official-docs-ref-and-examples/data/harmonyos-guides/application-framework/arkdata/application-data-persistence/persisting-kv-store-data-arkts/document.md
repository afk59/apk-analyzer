# Persisting KV Store Data (ArkTS)

#### When to Use

The key-value (KV) database stores data in the form of KV pairs. You can use KV stores to store data organized in a simple model, for example, product names and prices or employee IDs and daily attendance. The simple data structure allows higher compatibility with different database versions and device types.

#### Constraints

-   For each record in a device KV store, the key cannot exceed 896 bytes and the value cannot exceed 4 MB.
    
-   For each record in a single KV store, the key cannot exceed 1 KB and the value cannot exceed 4 MB.
    
-   A maximum of 16 distributed KV stores can be opened simultaneously for an application.
    
-   Blocking operations, for example, modifying UI components, are not allowed in the KV store event callbacks.
    

#### Available APIs

The following table lists the APIs used for KV data persistence. Most of the APIs are executed asynchronously, using a callback or promise to return the result. The following table uses the callback-based APIs as an example. For more information about the APIs, see [Distributed KV Store](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedkvstore).

| API | Description |
| :-- | :-- |
| createKVManager(config: KVManagerConfig): KVManager | Creates a **KvManager** instance to manage database objects. |
| getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void | Obtains a KV store of the specified type. |
| put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void | Adds a KV pair of the specified type to this KV store. |
| get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void | Obtains the value of the specified key. |
| delete(key: string, callback: AsyncCallback<void>): void | Deletes a KV pair based on the specified key. |
| closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void | Closes the distributed KV store of the given **storeId**. |
| deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void | Deletes the distributed KV store of the given **storeId**. |

#### How to Develop

1.  Use the **createKVManager()** method to create a **KVManager** instance for managing database objects.
    
    Example:
    
    // Import the module.
    // Create a KvStoreInterface.ets file in the pages directory.
    import { distributedKVStore } from '@kit.ArkData';
    import { BusinessError } from '@kit.BasicServicesKit';
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
    
2.  Use the **getKVStore()** method to create and obtain a KV store.
    
    Example:
    
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
    
3.  Use the **on()** method to subscribe to distributed data changes. To unsubscribe from the data changes, call [off('dataChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedkvstore#offdatachange).
    
    Example:
    
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
    
4.  Use **put()** to add data to the KV store.
    
    Example:
    
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/C3nhp1TdR-GFY7kvdyKClQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E14E7C3C8A8210D810C5D0AA4DBD7185AB5A357B1E7A3B6AED8882B69D7181A)
    
    The **put()** method adds a KV pair if the specified key does not exist and changes the value if the specified key already exists.
    
5.  Use **get()** to obtain the value of a key.
    
    Example:
    
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
    
6.  Use **delete()** to delete the data of the specified key.
    
    Example:
    
    public Delete = (() => {
      Logger.info('DeleteData start');
      if (kvStore === undefined) {
        Logger.info('DeleteData: kvStore not initialized');
        return;
      }
      const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
      try {
        kvStore.delete(KEY\_TEST\_STRING\_ELEMENT, (err) => {
          if (err !== undefined) {
            Logger.error(\`Failed to delete data. Code:${err.code},message:${err.message}\`);
            return;
          }
          Logger.info('Succeeded in deleting data.');
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
    
7.  Use **closeKVStore()** to close the specified distributed KV store by **storeId**.
    
    Example:
    
    public CloseKVStore = (()=>{
      Logger.info('CloseKVStore start');
      if (kvManager === undefined) {
        Logger.info('KvManager not initialized');
        return;
      }
      try {
        // appId is the bundle name of the application.
        kvStore = undefined;
        kvManager.closeKVStore(appId, storeId, (err: BusinessError)=> {
          if (err) {
            Logger.error(\`Failed to close KVStore.code is ${err.code},message is ${err.message}\`);
            return;
          }
          Logger.info('Succeeded in closing KVStore');
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
    
8.  Use **deleteKVStore()** to delete the specified distributed KV store by **storeId**.
    
    Example:
    
    public DeleteKvStore = (()=>{
      Logger.info('DeleteKvStore start');
      if (kvManager === undefined) {
        Logger.info('KvManager not initialized');
        return;
      }
      try {
        // appId is the bundle name of the application.
        kvStore = undefined;
        kvManager.deleteKVStore(appId, storeId, (err: BusinessError)=> {
          if (err) {
            Logger.error(\`Failed to delete KVStore.code is ${err.code},message is ${err.message}\`);
            return;
          }
          Logger.info('Succeeded in deleting KVStore');
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
