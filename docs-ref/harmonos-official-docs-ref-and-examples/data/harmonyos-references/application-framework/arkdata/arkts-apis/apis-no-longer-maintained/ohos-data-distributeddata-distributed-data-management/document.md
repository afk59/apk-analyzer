# @ohos.data.distributedData (Distributed Data Management)

The distributed data management module implements collaboration between databases of different devices for applications. The APIs provided by distributed data management can be used to save data to distributed databases and perform operations such as adding, deleting, modifying, querying, and synchronizing data in distributed databases.

This module provides the following functions:

-   [KVManager](#kvmanager): provides a **KVManager** instance to manage key-value (KV) stores.
-   [KvStoreResultSet8+](#kvstoreresultset8): provides APIs to obtain the KV store result set and query or move the data read position.
-   [Query8+](#query8): provides APIs to query data from the database through a **Query** instance by using predicates.
-   [KVStore](#kvstore): provides APIs to add data, delete data, and observe data changes and data sync through a **KVStore** instance.
-   [SingleKVStore](#singlekvstore): provides APIs to query and synchronize data in a single KV store. This class inherits from [KVStore](#kvstore), and data is not distinguished by device.
-   [DeviceKVStore8+](#devicekvstore8): provides APIs to query and synchronize data in a device KV store. This class inherits from [KVStore](#kvstore), and data is distinguished by device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/r3YhQvXaRpOdydJJ-A7soA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC051A9B52AE9A6B6EA1F7EF18C86359AF64E3A7C96169C4F0EE5B2920DE4559)

-   The APIs provided by this module are no longer maintained since API version 9. You are advised to use [@ohos.data.distributedKVStore](../../ohos-data-distributedkvstore-distributed-kv-store/document.md).
    
-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   All the APIs that need to obtain **deviceId** in this module are available only to system applications.
    

#### Modules to Import

import distributedData from '@ohos.data.distributedData';

#### distributedData.createKVManager

createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void

Creates a **KVManager** instance to manage KV stores. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [KVManagerConfig](#kvmanagerconfig) | Yes | Configuration of the **KVManager** instance, including the bundle name and user information of the caller. |
| callback | AsyncCallback<[KVManager](#kvmanager)\> | Yes | Callback used to return the **KVManager** instance created. |

**Example**

let kvManager;
try {
    const kvManagerConfig = {
        bundleName : 'com.example.datamanagertest',
        userInfo : {
            userId : '0',
            userType : distributedData.UserType.SAME\_USER\_ID
        }
    }
    distributedData.createKVManager(kvManagerConfig, function (err, manager) {
        if (err) {
            console.log("Failed to create KVManager: "  + JSON.stringify(err));
            return;
        }
        console.log("Succeeded in creating KVManager");
        kvManager = manager;
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### distributedData.createKVManager

createKVManager(config: KVManagerConfig): Promise<KVManager>

Creates a **KVManager** instance to manage KV stores. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [KVManagerConfig](#kvmanager) | Yes | Configuration of the **KVManager** instance, including the bundle name and user information of the caller. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVManager](#kvmanager)\> | Promise used to return the **KVManager** instance created. |

**Example**

try {
  const kvManagerConfig = {
    bundleName: 'com.example.datamanagertest',
    userInfo: {
      userId: '0',
      userType: distributedData.UserType.SAME\_USER\_ID
    }
  }
  distributedData.createKVManager(kvManagerConfig).then((manager) => {
    console.log("Succeeded in creating KVManager");
    kvManager = manager;
  }).catch((err) => {
    console.error("Failed to create KVManager: " + JSON.stringify(err));
  });
} catch (e) {
  console.log("An unexpected error occurred. Error:" + e);
}

#### KVManagerConfig

Represents the configuration of a **KVManager** instance, including the bundle name and user information of the caller.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userInfo | [UserInfo](#userinfo) | Yes | User information. |
| bundleName | string | Yes | Bundle name of the caller. |

#### UserInfo

Defines user information.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userId | string | No | User ID. The default value is **0**. |
| userType | [UserType](#usertype) | No | User type. The default value is **0**. |

#### UserType

Enumerates the user types.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SAME\_USER\_ID | 0 | User who logs in to different devices using the same account. |

#### KVManager

Creates a **KVManager** object to obtain KV store information. Before calling any method in **KVManager**, you must use [createKVManager](#distributeddatacreatekvmanager) to create a **KVManager** object.

#### \[h2\]getKVStore

getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>): void

Creates and obtains a KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| storeId | string | Yes | Unique identifier of the KV store. The length cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants). |
| options | [Options](#options) | Yes | Configuration of the KV store. |
| callback | AsyncCallback<T> | Yes | Callback used to return the KV store instance created. |

**Example**

let kvStore;
let kvManager;
try {
    const options = {
        createIfMissing : true,
        encrypt : false,
        backup : false,
        autoSync : true,
        kvStoreType : distributedData.KVStoreType.SINGLE\_VERSION,
        securityLevel : distributedData.SecurityLevel.S3,
    };
    kvManager.getKVStore('storeId', options, function (err, store) {
        if (err) {
            console.log("getKVStore err: "  + JSON.stringify(err));
            return;
        }
        console.log("getKVStore success");
        kvStore = store;
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]getKVStore

getKVStore<T extends KVStore>(storeId: string, options: Options): Promise<T>

Creates and obtains a KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| storeId | string | Yes | Unique identifier of the KV store. The length cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants). |
| options | [Options](#options) | Yes | Configuration of the KV store. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<T>, <T extends [KVStore](#kvstore)\> | Promise used to return the KV store instance created. |

**Example**

let kvStore;
let kvManager;
try {
    const options = {
        createIfMissing : true,
        encrypt : false,
        backup : false,
        autoSync : true,
        kvStoreType : distributedData.KVStoreType.SINGLE\_VERSION,
        securityLevel : distributedData.SecurityLevel.S3,
    };
    kvManager.getKVStore('storeId', options).then((store) => {
        console.log("getKVStore success");
        kvStore = store;
    }).catch((err) => {
        console.log("getKVStore err: "  + JSON.stringify(err));
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]closeKVStore8+

closeKVStore(appId: string, storeId: string, kvStore: KVStore, callback: AsyncCallback<void>): void

Closes a KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the app that invokes the KV store. |
| storeId | string | Yes | Unique identifier of the KV store to close. The length cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants). |
| kvStore | [KVStore](#kvstore) | Yes | KV store to close. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
let kvManager;
const options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedData.KVStoreType.SINGLE\_VERSION,
    schema: undefined,
    securityLevel: distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options, async function (err, store) {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.closeKVStore('appId', 'storeId', kvStore, function (err, data) {
            console.log('closeKVStore success');
        });
    });
} catch (e) {
    console.log('closeKVStore e ' + e);
}

#### \[h2\]closeKVStore8+

closeKVStore(appId: string, storeId: string, kvStore: KVStore): Promise<void>

Closes a KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the app that invokes the KV store. |
| storeId | string | Yes | Unique identifier of the KV store to close. The length cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants). |
| kvStore | [KVStore](#kvstore) | Yes | KV store to close. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvManager;
let kvStore;
const options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedData.KVStoreType.SINGLE\_VERSION,
    schema: undefined,
    securityLevel: distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options).then(async (store) => {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.closeKVStore('appId', 'storeId', kvStore).then(() => {
            console.log('closeKVStore success');
        }).catch((err) => {
            console.log('closeKVStore err ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('CloseKVStore getKVStore err ' + JSON.stringify(err));
    });
} catch (e) {
    console.log('closeKVStore e ' + e);
}

#### \[h2\]deleteKVStore8+

deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

Deletes a KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the app that invokes the KV store. |
| storeId | string | Yes | Unique identifier of the KV store to delete. The length cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvManager;
let kvStore;
const options = {
    createIfMissing : true,
    encrypt : false,
    backup : false,
    autoSync : true,
    kvStoreType : distributedData.KVStoreType.SINGLE\_VERSION,
    schema : undefined,
    securityLevel : distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('store', options, async function (err, store) {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.deleteKVStore('appId', 'storeId', function (err, data) {
            console.log('deleteKVStore success');
        });
    });
} catch (e) {
    console.log('DeleteKVStore e ' + e);
}

#### \[h2\]deleteKVStore8+

deleteKVStore(appId: string, storeId: string): Promise<void>

Deletes a KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the app that invokes the KV store. |
| storeId | string | Yes | Unique identifier of the KV store to delete. The length cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvManager;
let kvStore;
const options = {
    createIfMissing : true,
    encrypt : false,
    backup : false,
    autoSync : true,
    kvStoreType : distributedData.KVStoreType.SINGLE\_VERSION,
    schema : undefined,
    securityLevel : distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options).then(async (store) => {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.deleteKVStore('appId', 'storeId').then(() => {
            console.log('deleteKVStore success');
        }).catch((err) => {
            console.log('deleteKVStore err ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('getKVStore err ' + JSON.stringify(err));
    });
} catch (e) {
    console.log('deleteKVStore e ' + e);
}

#### \[h2\]getAllKVStoreId8+

getAllKVStoreId(appId: string, callback: AsyncCallback<string\[\]>): void

Obtains the IDs of all KV stores that are created by [getKVStore()](#getkvstore) and have not been deleted by [deleteKVStore()](#deletekvstore8). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the app that invokes the KV store. |
| callback | AsyncCallback<string\[\]> | Yes | Callback used to return the IDs of all created KV stores. |

**Example**

let kvManager;
try {
    kvManager.getAllKVStoreId('appId', function (err, data) {
        console.log('GetAllKVStoreId success');
        console.log('GetAllKVStoreId size = ' + data.length);
    });
} catch (e) {
    console.log('GetAllKVStoreId e ' + e);
}

#### \[h2\]getAllKVStoreId8+

getAllKVStoreId(appId: string): Promise<string\[\]>

Obtains the IDs of all KV stores that are created by [getKVStore()](#getkvstore) and have not been deleted by [deleteKVStore()](#deletekvstore8). This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the app that invokes the KV store. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string\[\]> | Promise used to return the IDs of all created KV stores. |

**Example**

let kvManager;
try {
    console.log('GetAllKVStoreId');
    kvManager.getAllKVStoreId('appId').then((data) => {
        console.log('getAllKVStoreId success');
        console.log('size = ' + data.length);
    }).catch((err) => {
        console.log('getAllKVStoreId err ' + JSON.stringify(err));
    });
} catch(e) {
    console.log('getAllKVStoreId e ' + e);
}

#### \[h2\]on('distributedDataServiceDie')8+

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

Subscribes to service status changes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **distributedDataServiceDie**, which indicates service status changes. |
| deathCallback | Callback<void> | Yes | Callback used to return the result. |

**Example**

let kvManager;
try {
    console.log('KVManagerOn');
    const deathCallback = function () {
        console.log('death callback call');
    }
    kvManager.on('distributedDataServiceDie', deathCallback);
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]off('distributedDataServiceDie')8+

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

Unsubscribes from service status changes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **distributedDataServiceDie**, which indicates service status changes. |
| deathCallback | Callback<void> | No | Callback to unregister. If this parameter is not specified, all callbacks for service status changes will be unregistered. |

**Example**

let kvManager;
try {
    console.log('KVManagerOff');
    const deathCallback = function () {
        console.log('death callback call');
    }
    kvManager.off('distributedDataServiceDie', deathCallback);
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
    

#### Options

Provides KV store configuration.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| createIfMissing | boolean | No | 
Whether to create a KV store if the database file does not exist. The default value is **true**, which means to create a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| encrypt | boolean | No | 

Whether to encrypt the KV store. The default value is **false**, which means the KV store is not encrypted.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| backup | boolean | No | 

Whether to back up the KV store. The default value is **true**, which means to back up the KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| autoSync | boolean | No | 

Whether to automatically synchronize database files. The default value is **false**, which means the database files are manually synchronized.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

 |
| kvStoreType | [KVStoreType](#kvstoretype) | No | 

Type of the KV store to create. The default value is **DEVICE\_COLLABORATION**, which indicates a device KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| securityLevel | [SecurityLevel](#securitylevel) | No | 

Security level (S1 to S4) of the KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| schema8+ | [Schema](#schema8) | No | 

Schema that defines the values stored in the KV store. The default value is **undefined**, which means no schema is used.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

 |

#### KVStoreType

Enumerates the KV store types.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_COLLABORATION | 0 | 
Device KV store.

The device KV store manages data by device, which eliminates conflicts. Data can be queried by device.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

 |
| SINGLE\_VERSION | 1 | 

Single KV store.

The single KV store does not differentiate data by device. If the same key is modified by different devices, the data will be overwritten.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| MULTI\_VERSION | 2 | 

Multi-version KV store. This type is not supported currently.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

 |

#### SecurityLevel

Enumerates the KV store security levels.

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_LEVEL | 0 | 
No security level is set for the KV store (deprecated).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

 |
| S0 | 1 | 

The KV store security level is public (deprecated).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| S1 | 2 | 

Low security level. If data leakage occurs, minor impact will be caused. For example, a KV store that contains system data such as wallpapers.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| S2 | 3 | 

Medium security level. If data leakage occurs, moderate impact will be caused. For example, a KV store that contains information created by users or call records, such as audio or video clips.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| S3 | 5 | 

High security level. If data leakage occurs, major impact will be caused. For example, a KV store that contains information such as user fitness, health, and location data.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| S4 | 6 | 

Critical security level. If data leakage occurs, severe impact will be caused. For example, a KV store that contains information such as authentication credentials and financial data.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |

#### Constants

Defines the KV store constants.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MAX\_KEY\_LENGTH | 1024 | Maximum length of a key in the KV store, in bytes. |
| MAX\_VALUE\_LENGTH | 4194303 | Maximum length of a value in the KV store, in bytes. |
| MAX\_KEY\_LENGTH\_DEVICE | 896 | Maximum length of a device key, in bytes. |
| MAX\_STORE\_ID\_LENGTH | 128 | Maximum length of a KV store ID, in bytes. |
| MAX\_QUERY\_LENGTH | 512000 | Maximum query length, in bytes. |
| MAX\_BATCH\_SIZE | 128 | Maximum number of batch operations. |

#### Schema8+

Defines the schema of a KV store. You can create a **Schema** object and place it in [Options](#options) when creating or opening a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| root8+ | [FieldNode](#fieldnode8) | Yes | Yes | JSON root object. |
| indexes8+ | Array<string> | Yes | Yes | String array in JSON format. |
| mode8+ | number | Yes | Yes | Schema mode. |
| skip8+ | number | Yes | Yes | Size of a skip of the schema. |

#### \[h2\]constructor8+

constructor()

A constructor used to create a **Schema** instance.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

#### FieldNode8+

Represents a **Schema** instance, which provides the APIs for defining the values stored in a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| nullable8+ | boolean | Yes | Yes | Whether the database field can be null. |
| default8+ | string | Yes | Yes | Default value of a **FieldNode**. |
| type8+ | number | Yes | Yes | Value of the data type corresponding to the specified node. |

#### \[h2\]constructor8+

constructor(name: string)

A constructor used to create a **FieldNode** instance with a string field.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Value of **FieldNode**. |

#### \[h2\]appendChild8+

appendChild(child: FieldNode): boolean

Appends a child node to this **FieldNode**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| child | [FieldNode](#fieldnode8) | Yes | Child node to append. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import ddm from '@ohos.data.distributedData';
try {
    let node = new ddm.FieldNode("root");
    let child1 = new ddm.FieldNode("child1");
    let child2 = new ddm.FieldNode("child2");
    let child3 = new ddm.FieldNode("child3");
    node.appendChild(child1);
    node.appendChild(child2);
    node.appendChild(child3);
    console.log("appendNode " + JSON.stringify(node));
    child1 = null;
    child2 = null;
    child3 = null;
    node = null;
} catch (e) {
    console.log("AppendChild " + e);
}

#### KvStoreResultSet8+

Provides APIs to obtain the KV store result sets, and query and move the data read position.

Before calling any method in **KvStoreResultSet**, you must use [getKVStore](#getkvstore) to obtain a **KVStore** object.

#### \[h2\]getCount8+

getCount(): number

Obtains the total number of rows in the result set.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total number of rows obtained. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const count = resultSet.getCount();
    console.log("getCount succeed:" + count);
} catch (e) {
    console.log("getCount failed: " + e);
}

#### \[h2\]getPosition8+

getPosition(): number

Obtains the current data read position (position from which data is read) in the result set.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Current data read position obtained. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeeded.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const position = resultSet.getPosition();
    console.log("getPosition succeed:" + position);
} catch (e) {
    console.log("getPosition failed: " + e);
}

#### \[h2\]moveToFirst8+

moveToFirst(): boolean

Moves the data read position to the first row. If the result set is empty, **false** will be returned.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved1 = resultSet.moveToFirst();
    console.log("moveToFirst succeed: " + moved1);
} catch (e) {
    console.log("moveToFirst failed " + e);
}

#### \[h2\]moveToLast8+

moveToLast(): boolean

Moves the data read position to the last row. If the result set is empty, **false** will be returned.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved2 = resultSet.moveToLast();
    console.log("moveToLast succeed:" + moved2);
} catch (e) {
    console.log("moveToLast failed: " + e);
}

#### \[h2\]moveToNext8+

moveToNext(): boolean

Moves the data read position to the next row. If the result set is empty, **false** will be returned.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved3 = resultSet.moveToNext();
    console.log("moveToNext succeed: " + moved3);
} catch (e) {
    console.log("moveToNext failed: " + e);
}

#### \[h2\]moveToPrevious8+

moveToPrevious(): boolean

Moves the data read position to the previous row. If the result set is empty, **false** will be returned.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved4 = resultSet.moveToPrevious();
    console.log("moveToPrevious succeed:" + moved4);
} catch (e) {
    console.log("moveToPrevious failed: " + e);
}

#### \[h2\]move8+

move(offset: number): boolean

Moves the data read position with the specified offset from the current position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Offset to move the data read position. A negative value means to move backward, and a positive value means to move forward. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved5 = resultSet.move(1);
    console.log("move succeed:" + moved5);
} catch (e) {
    console.log("move failed: " + e);
}

#### \[h2\]moveToPosition8+

moveToPosition(position: number): boolean

Moves the data read position from 0 to an absolute position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | number | Yes | Absolute position to move to. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved6 = resultSet.moveToPosition(1);
    console.log("moveToPosition succeed: " + moved6);
} catch (e) {
    console.log("moveToPosition failed: " + e);
}

#### \[h2\]isFirst8+

isFirst(): boolean

Checks whether the data read position is the first row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the first row is being read; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const isfirst = resultSet.isFirst();
    console.log("Check isFirst succeed:" + isfirst);
} catch (e) {
    console.log("Check isFirst failed: " + e);
}

#### \[h2\]isLast8+

isLast(): boolean

Checks whether the data read position is the last row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the last row is being read; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const islast = resultSet.isLast();
    console.log("Check isLast succeed: " + islast);
} catch (e) {
    console.log("Check isLast failed: " + e);
}

#### \[h2\]isBeforeFirst8+

isBeforeFirst(): boolean

Checks whether the data read position is before the first row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data read position is before the first row; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const isbeforefirst = resultSet.isBeforeFirst();
    console.log("Check isBeforeFirst succeed: " + isbeforefirst);
} catch (e) {
    console.log("Check isBeforeFirst failed: " + e);
}

#### \[h2\]isAfterLast8+

isAfterLast(): boolean

Checks whether the data read position is after the last row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data read position is after the last row; returns **false** otherwise. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const isafterlast = resultSet.isAfterLast();
    console.log("Check isAfterLast succeed:" + isafterlast);
} catch (e) {
    console.log("Check isAfterLast failed: " + e);
}

#### \[h2\]getEntry8+

getEntry(): Entry

Obtains the KV pair from the current position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Entry](#entry) | KV pair obtained. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const entry  = resultSet.getEntry();
    console.log("getEntry succeed:" + JSON.stringify(entry));
} catch (e) {
    console.log("getEntry failed: " + e);
}

#### Query8+

Provides APIs to create a **Query** object, which defines different data query criteria.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

#### \[h2\]constructor8+

constructor()

Defines a constructor used to create a **Query** instance.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

#### \[h2\]reset8+

reset(): Query

Resets the **Query** object.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object reset. |

**Example**

try {
    let query = new distributedData.Query();
    query.equalTo("key", "value");
    console.log("query is " + query.getSqlLike());
    query.reset();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("simply calls should be ok :" + e);
}

#### \[h2\]equalTo8+

equalTo(field: string, value: number|string|boolean): Query

Creates a **Query** object to search for the records with the specified field that are equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | number|string|boolean | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.equalTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]notEqualTo8+

notEqualTo(field: string, value: number|string|boolean): Query

Creates a **Query** object to search for the records with the specified field that are not equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | number|string|boolean | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]greaterThan8+

greaterThan(field: string, value: number|string|boolean): Query

Creates a **Query** object to search for the records with the specified field that are greater than the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | number|string|boolean | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.greaterThan("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]lessThan8+

lessThan(field: string, value: number|string): Query

Creates a **Query** object to search for the records with the specified field that are less than the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | number|string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.lessThan("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]greaterThanOrEqualTo8+

greaterThanOrEqualTo(field: string, value: number|string): Query

Creates a **Query** object to search for the records with the specified field that are greater than or equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | number|string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.greaterThanOrEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]lessThanOrEqualTo8+

lessThanOrEqualTo(field: string, value: number|string): Query

Creates a **Query** object to search for the records with the specified field that are less than or equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | number|string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.lessThanOrEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]isNull8+

isNull(field: string): Query

Creates a **Query** object to search for the records with the specified field that are **null**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.isNull("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]inNumber8+

inNumber(field: string, valueList: number\[\]): Query

Creates a **Query** object to search for the records with the specified field that are within the given number list.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| valueList | number\[\] | Yes | List of numbers to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.inNumber("field", \[0, 1\]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]inString8+

inString(field: string, valueList: string\[\]): Query

Creates a **Query** object to search for the records with the specified field that are within the given string list.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| valueList | string\[\] | Yes | List of strings to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.inString("field", \['test1', 'test2'\]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]notInNumber8+

notInNumber(field: string, valueList: number\[\]): Query

Creates a **Query** object to search for the records with the specified field that are not within the given number list.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| valueList | number\[\] | Yes | List of numbers to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notInNumber("field", \[0, 1\]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]notInString8+

notInString(field: string, valueList: string\[\]): Query

Creates a **Query** object to search for the records with the specified field that are not within the given string list.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| valueList | string\[\] | Yes | List of strings to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notInString("field", \['test1', 'test2'\]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]like8+

like(field: string, value: string): Query

Creates a **Query** object to search for the records with the specified field that are similar to the given string.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | string | Yes | String to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.like("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]unlike8+

unlike(field: string, value: string): Query

Creates a **Query** object to search for the records with the specified field that are not similar to the given string.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |
| value | string | Yes | String to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.unlike("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]and8+

and(): Query

Creates a **Query** object with the AND condition.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.and();
    query.notEqualTo("field", "value2");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]or8+

or(): Query

Creates a **Query** object with the OR condition.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.or();
    query.notEqualTo("field", "value2");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]orderByAsc8+

orderByAsc(field: string): Query

Creates a **Query** object to sort the query results in ascending order.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByAsc("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]orderByDesc8+

orderByDesc(field: string): Query

Creates a **Query** object to sort the query results in descending order.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByDesc("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]limit8+

limit(total: number, offset: number): Query

Creates a **Query** object to specify the number of records in the query result and the start position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| total | number | Yes | Number of records in the query result. |
| offset | number | Yes | Start position. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

let total = 10;
let offset = 1;
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.limit(total, offset);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]isNotNull8+

isNotNull(field: string): Query

Creates a **Query** object to search for the records whose value is not **null**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to query. It cannot contain '^'. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.isNotNull("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]beginGroup8+

beginGroup(): Query

Creates a **Query** object for a query condition group with a left parenthesis.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]endGroup8+

endGroup(): Query

Creates a **Query** object for a query condition group with a right parenthesis.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]prefixKey8+

prefixKey(prefix: string): Query

Creates a **Query** object with a specified key prefix.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | Key prefix. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.prefixKey("$.name");
    query.prefixKey("0");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]setSuggestIndex8+

setSuggestIndex(index: string): Query

Creates a **Query** object with an index preferentially used for query.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | string | Yes | Index preferentially used for query. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.setSuggestIndex("$.name");
    query.setSuggestIndex("0");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
   console.log("duplicated calls should be ok :" + e);
}

#### \[h2\]deviceId8+

deviceId(deviceId:string):Query

Creates a **Query** object with the device ID as the key prefix.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/z0-gU-fhSZeCB6m05F1-vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1BFB8E8099452B7C8F1B09E1A0B59FDA1A0A5ABDB9E8B653B8BFE192F574830)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Device ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query8) | **Query** object created. |

**Example**

try {
    let query = new distributedData.Query();
    query.deviceId("deviceId");
    console.log("query is " + query.getSqlLike());
} catch (e) {
    console.log("should be ok on Method Chaining : " + e);
}

#### \[h2\]getSqlLike8+

getSqlLike():string

Obtains the query statement of the **Query** object.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Query statement obtained. |

**Example**

try {
    let query = new distributedData.Query();
    let sql1 = query.getSqlLike();
    console.log("GetSqlLike sql=" + sql1);
} catch (e) {
    console.log("duplicated calls should be ok : " + e);
}

#### KVStore

Provides APIs to manage data in a KV store, for example, adding or deleting data and subscribing to data changes or completion of data sync.

Before calling any method in **KVStore**, you must use [getKVStore](#getkvstore) to obtain a **KVStore** object.

#### \[h2\]put

put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void

Adds a KV pair of the specified type to this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair to add. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| value | Uint8Array | string | number | boolean | Yes | Value of the KV pair to add. The value type can be Uint8Array, number, string, or boolean. A value of the Uint8Array or string type cannot exceed [MAX\_VALUE\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.log("put err: " + JSON.stringify(err));
            return;
        }
        console.log("put success");
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]put

put(key: string, value: Uint8Array | string | number | boolean): Promise<void>

Adds a KV pair of the specified type to this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair to add. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| value | Uint8Array | string | number | boolean | Yes | Value of the KV pair to add. The value type can be Uint8Array, number, string, or boolean. A value of the Uint8Array or string type cannot exceed [MAX\_VALUE\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then((data) => {
        console.log("put success: " + JSON.stringify(data));
    }).catch((err) => {
        console.log("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]delete

delete(key: string, callback: AsyncCallback<void>): void

Deletes a KV pair from this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair to delete. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.log("put err: " + JSON.stringify(err));
            return;
        }
        console.log("put success");
        kvStore.delete(KEY\_TEST\_STRING\_ELEMENT, function (err,data) {
            if (err != undefined) {
                console.log("delete err: " + JSON.stringify(err));
                return;
            }
            console.log("delete success");
        });
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]delete

delete(key: string): Promise<void>

Deletes a KV pair from this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair to delete. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then((data) => {
        console.log("put success: " + JSON.stringify(data));
        kvStore.delete(KEY\_TEST\_STRING\_ELEMENT).then((data) => {
            console.log("delete success");
        }).catch((err) => {
            console.log("delete err: " + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]on('dataChange')

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

Subscribes to data changes of the specified type.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates data changes. |
| type | [SubscribeType](#subscribetype) | Yes | Type of data change. |
| listener | Callback<[ChangeNotification](#changenotification)\> | Yes | Callback used to return the result. |

**Example**

let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_LOCAL, function (data) {
    console.log("dataChange callback call data: " + JSON.stringify(data));
});

#### \[h2\]on('syncComplete')

on(event: 'syncComplete', syncCallback: Callback<Array<\[string, number\]>>): void

Subscribes to sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | Yes | Callback used to return a sync completion event. |

**Example**

let kvStore;
kvStore.on('syncComplete', function (data) {
    console.log("callback call data: " + data);
});

#### \[h2\]off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

Unsubscribes from data changes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates data changes. |
| listener | Callback<[ChangeNotification](#changenotification)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for data changes will be unregistered. |

**Example**

let kvStore;
class KvstoreModel {
    call(data) {
        console.log("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}

#### \[h2\]off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<\[string, number\]>>): void

Unsubscribes from sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | No | Callback to unregister. If this parameter is not specified, all callbacks for data changes will be unregistered. |

**Example**

let kvStore;
class KvstoreModel {
    call(data) {
        console.log("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}

#### \[h2\]putBatch8+

putBatch(entries: Entry\[\], callback: AsyncCallback<void>): void

Inserts KV pairs in batches to this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| entries | [Entry](#entry)\[\] | Yes | KV pairs to insert in batches. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.getEntries('batch\_test\_string\_key', function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
        });
    });
}catch(e) {
    console.log('PutBatch e ' + JSON.stringify(e));
}

#### \[h2\]putBatch8+

putBatch(entries: Entry\[\]): Promise<void>

Inserts KV pairs in batches to this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| entries | [Entry](#entry)\[\] | Yes | KV pairs to insert in batches. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.getEntries('batch\_test\_string\_key').then((entries) => {
            console.log('getEntries success');
            console.log('PutBatch ' + JSON.stringify(entries));
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('PutBatch e ' + JSON.stringify(e));
}

#### \[h2\]deleteBatch8+

deleteBatch(keys: string\[\], callback: AsyncCallback<void>): void

Deletes KV pairs in batches from this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | string\[\] | Yes | KV pairs to delete in batches. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    let entries = \[\];
    let keys = \[\];
    for (var i = 0; i < 5; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
        keys.push(key + i);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.deleteBatch(keys, async function (err,data) {
            console.log('deleteBatch success');
        });
    });
}catch(e) {
    console.log('DeleteBatch e ' + e);
}

#### \[h2\]deleteBatch8+

deleteBatch(keys: string\[\]): Promise<void>

Deletes KV pairs in batches from this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | string\[\] | Yes | KV pairs to delete in batches. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    let entries = \[\];
    let keys = \[\];
    for (var i = 0; i < 5; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
        keys.push(key + i);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.deleteBatch(keys).then((err) => {
            console.log('deleteBatch success');
        }).catch((err) => {
            console.log('deleteBatch fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('DeleteBatch e ' + e);
}

#### \[h2\]startTransaction8+

startTransaction(callback: AsyncCallback<void>): void

Starts the transaction in this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
function putBatchString(len, prefix) {
    let entries = \[\];
    for (var i = 0; i < len; i++) {
        var entry = {
            key : prefix + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    return entries;
}
try {
    var count = 0;
    kvStore.on('dataChange', 0, function (data) {
        console.log('startTransaction 0' + data)
        count++;
    });
    kvStore.startTransaction(async function (err,data) {
        console.log('startTransaction success');
        let entries = putBatchString(10, 'batch\_test\_string\_key');
        console.log('entries: ' + JSON.stringify(entries));
        kvStore.putBatch(entries, async function (err,data) {
            console.log('putBatch success');
        });
    });
}catch(e) {
    console.log('startTransaction e ' + e);
}

#### \[h2\]startTransaction8+

startTransaction(): Promise<void>

Starts the transaction in this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    var count = 0;
    kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_ALL, function (data) {
        console.log('startTransaction ' + JSON.stringify(data));
        count++;
    });
    kvStore.startTransaction().then(async (err) => {
        console.log('startTransaction success');
    }).catch((err) => {
        console.log('startTransaction fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('startTransaction e ' + e);
}

#### \[h2\]commit8+

commit(callback: AsyncCallback<void>): void

Commits the transaction in this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    kvStore.commit(function (err,data) {
        if (err == undefined) {
            console.log('commit success');
        } else {
            console.log('commit fail');
        }
    });
}catch(e) {
    console.log('Commit e ' + e);
}

#### \[h2\]commit8+

commit(): Promise<void>

Commits the transaction in this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    kvStore.commit().then(async (err) => {
        console.log('commit success');
    }).catch((err) => {
        console.log('commit fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('Commit e ' + e);
}

#### \[h2\]rollback8+

rollback(callback: AsyncCallback<void>): void

Rolls back the transaction in this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    kvStore.rollback(function (err,data) {
        if (err == undefined) {
            console.log('commit success');
        } else {
            console.log('commit fail');
        }
    });
}catch(e) {
    console.log('Rollback e ' + e);
}

#### \[h2\]rollback8+

rollback(): Promise<void>

Rolls back the transaction in this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    kvStore.rollback().then(async (err) => {
        console.log('rollback success');
    }).catch((err) => {
        console.log('rollback fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('Rollback e ' + e);
}

#### \[h2\]enableSync8+

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

Sets data sync, which can be enabled or disabled. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable data sync. The value **true** means to enable data sync, and **false** means the opposite. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    kvStore.enableSync(true, function (err,data) {
        if (err == undefined) {
            console.log('enableSync success');
        } else {
            console.log('enableSync fail');
        }
    });
}catch(e) {
    console.log('EnableSync e ' + e);
}

#### \[h2\]enableSync8+

enableSync(enabled: boolean): Promise<void>

Sets data sync, which can be enabled or disabled. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable data sync. The value **true** means to enable data sync, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    kvStore.enableSync(true).then((err) => {
        console.log('enableSync success');
    }).catch((err) => {
        console.log('enableSync fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('EnableSync e ' + e);
}

#### \[h2\]setSyncRange8+

setSyncRange(localLabels: string\[\], remoteSupportLabels: string\[\], callback: AsyncCallback<void>): void

Sets the data sync range. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localLabels | string\[\] | Yes | Sync labels set for the local device. |
| remoteSupportLabels | string\[\] | Yes | Sync labels set for remote devices. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    const localLabels = \['A', 'B'\];
    const remoteSupportLabels = \['C', 'D'\];
    kvStore.setSyncRange(localLabels, remoteSupportLabels, function (err,data) {
        console.log('SetSyncRange put success');
    });
}catch(e) {
    console.log('SetSyncRange e ' + e);
}

#### \[h2\]setSyncRange8+

setSyncRange(localLabels: string\[\], remoteSupportLabels: string\[\]): Promise<void>

Sets the data sync range. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localLabels | string\[\] | Yes | Sync labels set for the local device. |
| remoteSupportLabels | string\[\] | Yes | Sync labels set for remote devices. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    const localLabels = \['A', 'B'\];
    const remoteSupportLabels = \['C', 'D'\];
    kvStore.setSyncRange(localLabels, remoteSupportLabels).then((err) => {
        console.log('setSyncRange success');
    }).catch((err) => {
        console.log('delete fail ' + err);
    });
}catch(e) {
    console.log('SetSyncRange e ' + e);
}

#### SubscribeType

Enumerates the subscription types.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SUBSCRIBE\_TYPE\_LOCAL | 0 | Local data changes. |
| SUBSCRIBE\_TYPE\_REMOTE | 1 | Remote data changes. |
| SUBSCRIBE\_TYPE\_ALL | 2 | Local and remote data changes. |

#### ChangeNotification

Defines the content of data change notifications, including inserted data, updated data, deleted data, and device ID.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| insertEntries | [Entry](#entry)\[\] | Yes | Data inserted. |
| updateEntries | [Entry](#entry)\[\] | Yes | Data updated. |
| deleteEntries | [Entry](#entry)\[\] | Yes | Data deleted. |
| deviceId | string | Yes | UUID of the device. |

#### Entry

Defines the KV pairs stored in the KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair stored in the KV store. |
| value | [Value](#value) | Yes | Value of the KV pair stored in the KV store. |

#### Value

Defines the **value** object in a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [ValueType](#value) | Yes | Type of the value. |
| value | Uint8Array | string | number | boolean | Yes | Value of the KV pair stored in the KV store. |

#### ValueType

Enumerates the data types.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STRING | 0 | String. |
| INTEGER | 1 | Integer. |
| FLOAT | 2 | Float (single-precision floating point). |
| BYTE\_ARRAY | 3 | Byte array. |
| BOOLEAN | 4 | Boolean. |
| DOUBLE | 5 | Double (double-precision floating point). |

#### SingleKVStore

Provides APIs to query and synchronize data in a single KV store. This class inherits from [KVStore](#kvstore).

Data is not distinguished by device in a single KV store. The data written to different devices using the same key will be overwritten. For example, a single KV store can be used to synchronize a user's calendar and contact data between different devices.

Before calling any method in **SingleKVStore**, you must use [getKVStore](#getkvstore) to obtain a **SingleKVStore** instance.

#### \[h2\]get

get(key: string, callback: AsyncCallback<Uint8Array | string | boolean | number>): void

Obtains the value of the specified key. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the value to obtain. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<Uint8Array | string | boolean | number> | Yes | Callback used to return the value obtained. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.log("put err: " + JSON.stringify(err));
            return;
        }
        console.log("put success");
        kvStore.get(KEY\_TEST\_STRING\_ELEMENT, function (err,data) {
            console.log("get success data: " + data);
        });
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]get

get(key: string): Promise<Uint8Array | string | boolean | number>

Obtains the value of the specified key. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the value to obtain. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array | string | boolean | number> | Promise used to return the value obtained. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then((data) => {
        console.log("put success: " + JSON.stringify(data));
        kvStore.get(KEY\_TEST\_STRING\_ELEMENT).then((data) => {
            console.log("get success data: " + data);
        }).catch((err) => {
            console.log("get err: " + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

#### \[h2\]getEntries8+

getEntries(keyPrefix: string, callback: AsyncCallback<Entry\[\]>): void

Obtains all KV pairs that match the specified key prefix. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified prefix. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_number\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.INTEGER,
                value : 222
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.getEntries('batch\_test\_number\_key', function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
        });
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}

#### \[h2\]getEntries8+

getEntries(keyPrefix: string): Promise<Entry\[\]>

Obtains all KV pairs that match the specified key prefix. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified prefix. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + entries);
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.getEntries('batch\_test\_string\_key').then((entries) => {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
            console.log('entries\[0\].value: ' + JSON.stringify(entries\[0\].value));
            console.log('entries\[0\].value.value: ' + entries\[0\].value.value);
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}

#### \[h2\]getEntries8+

getEntries(query: Query, callback: AsyncCallback<Entry\[\]>): void

Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | Key prefix to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified **Query** object. |

**Example**

let kvStore;
try {
    var arr = new Uint8Array(\[21,31\]);
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_bool\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE\_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getEntries(query, function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
        });
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}

#### \[h2\]getEntries8+

getEntries(query: Query): Promise<Entry\[\]>

Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified **Query** object. |

**Example**

let kvStore;
try {
    var arr = new Uint8Array(\[21,31\]);
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_bool\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE\_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getEntries(query).then((entries) => {
            console.log('getEntries success');
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('GetEntries putBatch fail ' + JSON.stringify(err))
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

Obtains the result set with the specified prefix. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. |
| callback | AsyncCallback<[KvStoreResultSet](#kvstoreresultset8)\> | Yes | Callback used to return the result set with the specified prefix. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('GetResultSet putBatch success');
        kvStore.getResultSet('batch\_test\_string\_key', async function (err, result) {
            console.log('GetResultSet getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.log('GetResultSet closeResultSet success');
            })
        });
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(keyPrefix: string): Promise<KvStoreResultSet>

Obtains the result set with the specified prefix. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KvStoreResultSet](#kvstoreresultset8)\> | Promise used to return the result set with the specified prefix. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('PutBatch putBatch fail ' + JSON.stringify(err));
    });
    kvStore.getResultSet('batch\_test\_string\_key').then((result) => {
        console.log('GetResult getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('GetResult closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResult e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | Query | Yes | **Query** object to match. |
| callback | AsyncCallback<[KvStoreResultSet](#kvstoreresultset8)\> | Yes | Callback used to return the **KvStoreResultSet** object obtained. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getResultSet(query, async function (err, result) {
            console.log('getResultSet succeed.');
            resultSet = result;
        });
    });
} catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(query: Query): Promise<KvStoreResultSet>

Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KvStoreResultSet](#kvstoreresultset8)\> | Promise used to return the **KvStoreResultSet** object obtained. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch\_test");
    kvStore.getResultSet(query).then((result) => {
        console.log(' getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

Closes the **KvStoreResultSet** object obtained by [SingleKVStore.getResultSet](#getresultset8). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resultSet | [KvStoreResultSet](#kvstoreresultset8) | Yes | **KvStoreResultSet** object to close. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    let resultSet = null;
    kvStore.closeResultSet(resultSet, function (err, data) {
        if (err == undefined) {
            console.log('closeResultSet success');
        } else {
            console.log('closeResultSet fail');
        }
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}

#### \[h2\]closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet): Promise<void>

Closes the **KvStoreResultSet** object obtained by [SingleKVStore.getResultSet](#getresultset8). This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resultSet | [KvStoreResultSet](#kvstoreresultset8) | Yes | **KvStoreResultSet** object to close. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    let resultSet = null;
    kvStore.closeResultSet(resultSet).then(() => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}

#### \[h2\]getResultSize8+

getResultSize(query: Query, callback: AsyncCallback<number>): void

Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of results that match the specified **Query** object. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getResultSize(query, async function (err, resultSize) {
            console.log('getResultSet succeed.');
        });
    });
} catch(e) {
    console.log('GetResultSize e ' + e);
}

#### \[h2\]getResultSize8+

getResultSize(query: Query): Promise<number>

Obtains the number of results that match the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of results obtained. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch\_test");
    kvStore.getResultSize(query).then((resultSize) => {
        console.log('getResultSet succeed.');
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSize e ' + e);
}

#### \[h2\]removeDeviceData8+

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

Deletes data of a device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/m0QNIifzT8mujXpoCXxoqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBBACCE918C0A9A6DC7B13305565F3C7833E6D6DC443C75A1A21857DD6F04056)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-002';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, async function (err,data) {
        console.log('put success');
        const deviceid = 'no\_exist\_device\_id';
        kvStore.removeDeviceData(deviceid, async function (err,data) {
            if (err == undefined) {
                console.log('removeDeviceData success');
            } else {
                console.log('removeDeviceData fail');
                kvStore.get(KEY\_TEST\_STRING\_ELEMENT, async function (err,data) {
                    console.log('RemoveDeviceData get success');
                });
            }
        });
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}

#### \[h2\]removeDeviceData8+

removeDeviceData(deviceId: string): Promise<void>

Deletes data of a device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Y4UCWsVCRCaA4u8KxwMpEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CE13E7343C5326A3E009461816226A914B98ED10D64EE0085F09C88D8C51551)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then((err) => {
        console.log('removeDeviceData put success');
    }).catch((err) => {
        console.log('put fail ' + JSON.stringify(err));
    });
    const deviceid = 'no\_exist\_device\_id';
    kvStore.removeDeviceData(deviceid).then((err) => {
        console.log('removeDeviceData success');
    }).catch((err) => {
        console.log('removeDeviceData fail ' + JSON.stringify(err));
    });
    kvStore.get(KEY\_TEST\_STRING\_ELEMENT).then((data) => {
        console.log('get success data:' + data);
    }).catch((err) => {
        console.log('RemoveDeviceData get fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}

#### \[h2\]sync

sync(deviceIds: string\[\], mode: SyncMode, delayMs?: number): void

Synchronizes the KV store manually.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/vcOb3fonRCuehVFOV5PLlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8572BCB046AB51E2986A0B08D9D33699AB6F7E64A45A4C354A64FE14AC2A1A7)

**deviceIds** is **networkId** in DeviceInfo, which can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceIds | string\[\] | Yes | List of **networkId**s of the devices in the same networking environment to be synchronized. |
| mode | [SyncMode](#syncmode) | Yes | Sync mode. |
| delayMs | number | No | Delay time allowed, in milliseconds. The default value is **0**. |

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let devManager;
let kvStore;
const KEY\_TEST\_SYNC\_ELEMENT = 'key\_test\_sync';
const VALUE\_TEST\_SYNC\_ELEMENT = 'value-string-001';
// create deviceManager
deviceManager.createDeviceManager('bundleName', (err, value) => {
  if (!err) {
    devManager = value;
    let deviceIds = \[\];
    if (devManager != null) {
      var devices = devManager.getTrustedDeviceListSync();
      for (var i = 0; i < devices.length; i++) {
        deviceIds\[i\] = devices\[i\].networkId;
      }
    }
    try {
      kvStore.on('syncComplete', function (data) {
        console.log('Sync dataChange');
      });
      kvStore.put(KEY\_TEST\_SYNC\_ELEMENT + 'testSync101', VALUE\_TEST\_SYNC\_ELEMENT, function (err, data) {
        if (err != undefined) {
          console.log("put err: " + JSON.stringify(err));
          return;
        }
        console.log('Succeeded in putting data');
        const mode = distributedData.SyncMode.PULL\_ONLY;
        kvStore.sync(deviceIds, mode, 1000);
      });
    } catch (e) {
      console.log('Sync e' + e);
    }
  }
});

#### \[h2\]on('dataChange')8+

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

Subscribes to data changes of the specified type.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates data changes. |
| type | [SubscribeType](#subscribetype) | Yes | Type of data change. |
| listener | Callback<[ChangeNotification](#changenotification)\> | Yes | Callback used to return the result. |

**Example**

let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_LOCAL, function (data) {
    console.log("dataChange callback call data: " + JSON.stringify(data));
});

#### \[h2\]on('syncComplete')8+

on(event: 'syncComplete', syncCallback: Callback<Array<\[string, number\]>>): void

Subscribes to sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | Yes | Callback used to return a sync completion event. |

**Example**

let kvStore;
const KEY\_TEST\_FLOAT\_ELEMENT = 'key\_test\_float';
const VALUE\_TEST\_FLOAT\_ELEMENT = 321.12;
try {
    kvStore.on('syncComplete', function (data) {
        console.log('syncComplete ' + data)
    });
    kvStore.put(KEY\_TEST\_FLOAT\_ELEMENT, VALUE\_TEST\_FLOAT\_ELEMENT).then((data) => {
        console.log('syncComplete put success');
    }).catch((error) => {
        console.log('syncComplete put fail ' + error);
    });
}catch(e) {
    console.log('syncComplete put e ' + e);
}

#### \[h2\]off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

Unsubscribes from data changes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates data changes. |
| listener | Callback<[ChangeNotification](#changenotification)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for data changes will be unregistered. |

**Example**

let kvStore;
class KvstoreModel {
    call(data) {
        console.log("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}

#### \[h2\]off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<\[string, number\]>>): void

Unsubscribes from sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | No | Callback to unregister. If this parameter is not specified, all callbacks for data changes will be unregistered. |

**Example**

let kvStore;
class KvstoreModel {
    call(data) {
        console.log("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}

#### \[h2\]setSyncParam8+

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

Sets the default delay allowed for KV store sync. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| defaultAllowedDelayMs | number | Yes | Default delay allowed for database sync, in ms. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    const defaultAllowedDelayMs = 500;
    kvStore.setSyncParam(defaultAllowedDelayMs, function (err,data) {
        console.log('SetSyncParam put success');
    });
}catch(e) {
    console.log('testSingleKvStoreSetSyncParam e ' + e);
}

#### \[h2\]setSyncParam8+

setSyncParam(defaultAllowedDelayMs: number): Promise<void>

Sets the default delay allowed for KV store sync. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| defaultAllowedDelayMs | number | Yes | Default delay allowed for database sync, in ms. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    const defaultAllowedDelayMs = 500;
    kvStore.setSyncParam(defaultAllowedDelayMs).then((err) => {
        console.log('SetSyncParam put success');
    }).catch((err) => {
        console.log('SetSyncParam put fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('SetSyncParam e ' + e);
}

#### \[h2\]getSecurityLevel8+

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

Obtains the security level of this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SecurityLevel](#securitylevel)\> | Yes | Callback used to return the security level of the KV store. |

**Example**

let kvStore;
try {
    kvStore.getSecurityLevel(function (err,data) {
        console.log('getSecurityLevel success');
    });
}catch(e) {
    console.log('GetSecurityLevel e ' + e);
}

#### \[h2\]getSecurityLevel8+

getSecurityLevel(): Promise<SecurityLevel>

Obtains the security level of this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SecurityLevel](#securitylevel)\> | Promise used to return the security level of the KV store. |

**Example**

let kvStore;
try {
    kvStore.getSecurityLevel().then((data) => {
        console.log(' getSecurityLevel success');
    }).catch((err) => {
        console.log('getSecurityLevel fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetSecurityLevel e ' + e);
}

#### DeviceKVStore8+

Provides APIs to query and synchronize data in a device KV store. This class inherits from [KVStore](#kvstore).

Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of other devices is read-only and cannot be modified.

For example, a device KV store can be used to implement image sharing between devices. The images of other devices can be viewed, but not be modified or deleted.

Before calling any method in **DeviceKVStore**, you must use [getKVStore](#getkvstore) to obtain a **DeviceKVStore** object.

#### \[h2\]get8+

get(deviceId: string, key: string, callback: AsyncCallback<boolean|string|number|Uint8Array>): void

Obtains a string value that matches the specified device ID and key. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/q-fQep0VTYaZt2KLtkMKjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED3D603B457E465CB561FEED3286CEE0C6D6755C0346D6B9487A9A9C28228A53)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| key | string | Yes | Key to match. |
| callback | AsyncCallback<boolean|string|number|Uint8Array> | Yes | Callback used to return the value obtained. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-002';
try{
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, async function (err,data) {
        console.log('put success');
        kvStore.get('localDeviceId', KEY\_TEST\_STRING\_ELEMENT, function (err,data) {
            console.log('get success');
        });
    })
}catch(e) {
    console.log('get e' + e);
}

#### \[h2\]get8+

get(deviceId: string, key: string): Promise<boolean|string|number|Uint8Array>

Obtains a string value that matches the specified device ID and key. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/4NpCO8NiR4OptkV100poVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5B78A22F0F939595B777F1A563CF2909915D3AC81222082976B451F46739B11)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| key | string | Yes | Key to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean|string|number|Uint8Array> | Promise used to return the string value that matches the given condition. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-002';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(async (data) => {
        console.log(' put success');
        kvStore.get('localDeviceId', KEY\_TEST\_STRING\_ELEMENT).then((data) => {
            console.log('get success');
        }).catch((err) => {
            console.log('get fail ' + JSON.stringify(err));
        });
    }).catch((error) => {
        console.log('put error' + error);
    });
} catch (e) {
    console.log('Get e ' + e);
}

#### \[h2\]getEntries8+

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry\[\]>): void

Obtains all KV pairs that match the specified device ID and key prefix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/A_WwfU-dQHef50LjuRi3bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=510AD2EB7FF794C5311A6DE481860613BC375FF71BCA2C5116A7CA6EB8BC65B3)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs obtained. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + entries);
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.getEntries('localDeviceId', 'batch\_test\_string\_key', function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
        });
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}

#### \[h2\]getEntries8+

getEntries(deviceId: string, keyPrefix: string): Promise<Entry\[\]>

Obtains all KV pairs that match the specified device ID and key prefix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Pr6ePkNxQSy87EoG-3w45g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BE4215BC805D467E3F7AB68EB6C015F334494D2982BFC00861BC27DE7E2A77E)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return all the KV pairs that match the given condition. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + entries);
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.getEntries('localDeviceId', 'batch\_test\_string\_key').then((entries) => {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
            console.log('entries\[0\].value: ' + JSON.stringify(entries\[0\].value));
            console.log('entries\[0\].value.value: ' + entries\[0\].value.value);
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}

#### \[h2\]getEntries8+

getEntries(query: Query, callback: AsyncCallback<Entry\[\]>): void

Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs obtained. |

**Example**

let kvStore;
try {
    var arr = new Uint8Array(\[21,31\]);
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_bool\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE\_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        query.deviceId('localDeviceId');
        kvStore.getEntries(query, function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
        });
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}

#### \[h2\]getEntries8+

getEntries(query: Query): Promise<Entry\[\]>

Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified **Query** object. |

**Example**

let kvStore;
try {
    var arr = new Uint8Array(\[21,31\]);
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_bool\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE\_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getEntries(query).then((entries) => {
            console.log('getEntries success');
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('GetEntries putBatch fail ' + JSON.stringify(err))
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}

#### \[h2\]getEntries8+

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry\[\]>): void

Obtains the KV pairs that match the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/hlhG-9HQQM6oaXwHtRUc1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D50896EB5602A148781C79180684B26F742F7058C356B4F3531EEAD7B96002B)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified device ID and **Query** object. |

**Example**

let kvStore;
try {
    var arr = new Uint8Array(\[21,31\]);
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_bool\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE\_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        var query = new distributedData.Query();
        query.deviceId('localDeviceId');
        query.prefixKey("batch\_test");
        kvStore.getEntries('localDeviceId', query, function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries\[0\]: ' + JSON.stringify(entries\[0\]));
        })
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}

#### \[h2\]getEntries8+

getEntries(deviceId: string, query: Query): Promise<Entry\[\]>

Obtains the KV pairs that match the specified device ID and **Query** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/_lAAYYORSVuQrxouBDYYNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFC8A51AAC4930AD64881FB74FA05CB1B48B5BFCD30C052416784464DE347B75)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified device ID and **Query** object. |

**Example**

let kvStore;
try {
    var arr = new Uint8Array(\[21,31\]);
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_bool\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE\_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        var query = new distributedData.Query();
        query.deviceId('localDeviceId');
        query.prefixKey("batch\_test");
        kvStore.getEntries('localDeviceId', query).then((entries) => {
            console.log('getEntries success');
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

Obtains a **KvStoreResultSet** object that matches the specified device ID and key prefix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/wlIuldRKQjKHz2TQ2DAkHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2A3A5CBAF2F8FD904C488CD1F26F2492154BCE27E0C2B8EF156EAFA0D63A1FF)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. |
| callback | AsyncCallback<[KvStoreResultSet](#kvstoreresultset8)\> | Yes | Callback used to return the **KvStoreResultSet** object that matches the specified device ID and key prefix. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('localDeviceId', 'batch\_test\_string\_key', async function (err, result) {
        console.log('getResultSet succeed.');
        resultSet = result;
        kvStore.closeResultSet(resultSet, function (err, data) {
            console.log('closeResultSet success');
        })
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(deviceId: string, keyPrefix: string): Promise<KvStoreResultSet>

Obtains a **KvStoreResultSet** object that matches the specified device ID and key prefix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/w-TtV_blTgikvTyVDsSJ4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97F5047068411BB9420311C7F843E36D90F621BEFBDD22329903CAF271E142D7)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KvStoreResultSet](#kvstoreresultset8)\> | Promise used to return the **KvStoreResultSet** object that matches the specified device ID and key prefix. |

**Example**

let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('localDeviceId', 'batch\_test\_string\_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<[KvStoreResultSet](#kvstoreresultset8)\> | Yes | Callback used to return the **KvStoreResultSet** object obtained. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        query.deviceId('localDeviceId');
        kvStore.getResultSet(query, async function (err, result) {
            console.log('getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.log('closeResultSet success');
            })
        });
    });
} catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(query: Query): Promise<KvStoreResultSet>

Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KvStoreResultSet](#kvstoreresultset8)\> | Promise used to return the **KvStoreResultSet** object that matches the specified **Query** object. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + err);
    });
    const query = new distributedData.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch\_test");
    console.log("GetResultSet " + query.getSqlLike());
    kvStore.getResultSet(query).then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>): void

Obtains a **KvStoreResultSet** object that matches the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/tFrXZ_lFRLGJ6kJXUyDEwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39B9CDC99CC3E9A327923EE9A8E84193B4A550120037011347C6CA3F4BD8F244)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<[KvStoreResultSet](#kvstoreresultset8)\> | Yes | Callback used to return the **KvStoreResultSet** object that matches the specified device ID and **Query** object. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getResultSet('localDeviceId', query, async function (err, result) {
            console.log('getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.log('closeResultSet success');
            })
        });
    });
} catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]getResultSet8+

getResultSet(deviceId: string, query: Query): Promise<KvStoreResultSet>

Obtains a **KvStoreResultSet** object that matches the specified device ID and **Query** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/hZ2Y1F3XTsSIqy9u25OgxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0A8C30F81CE7E2A355C6D97EAC3D68F33ED5A13EBEEF2FCE05478A6A214A728)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KvStoreResultSet](#kvstoreresultset8)\> | Promise used to return the **KvStoreResultSet** object that matches the specified device ID and **Query** object. |

**Example**

let kvStore;
try {
    let resultSet;
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('GetResultSet putBatch success');
    }).catch((err) => {
        console.log('PutBatch putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch\_test");
    kvStore.getResultSet('localDeviceId', query).then((result) => {
        console.log('GetResultSet getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('GetResultSet getResultSet failed: ' + JSON.stringify(err));
    });
    query.deviceId('localDeviceId');
    console.log("GetResultSet " + query.getSqlLike());
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('GetResultSet closeResultSet success');
    }).catch((err) => {
        console.log('GetResultSet closeResultSet fail ' + JSON.stringify(err));
    });

}catch(e) {
    console.log('GetResultSet e ' + e);
}

#### \[h2\]closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

Closes the **KvStoreResultSet** object obtained by [DeviceKVStore.getResultSet](#getresultset8-4). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resultSet | [KvStoreResultSet](#kvstoreresultset8) | Yes | **KvStoreResultSet** object to close. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
try {
    console.log('CloseResultSet success');
    let resultSet = null;
    kvStore.closeResultSet(resultSet, function (err, data) {
        if (err == undefined) {
            console.log('closeResultSet success');
        } else {
            console.log('closeResultSet fail');
        }
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}

#### \[h2\]closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet): Promise<void>

Closes the **KvStoreResultSet** object obtained by [DeviceKVStore.getResultSet](#getresultset8-4). This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resultSet | [KvStoreResultSet](#kvstoreresultset8) | Yes | **KvStoreResultSet** object to close. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
try {
    console.log('CloseResultSet success');
    let resultSet = null;
    kvStore.closeResultSet(resultSet).then(() => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}

#### \[h2\]getResultSize8+

getResultSize(query: Query, callback: AsyncCallback<number>): void

Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of results obtained. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        query.deviceId('localDeviceId');
        kvStore.getResultSize(query, async function (err, resultSize) {
            console.log('getResultSet succeed.');
        });
    });
} catch(e) {
    console.log('GetResultSize e ' + e);
}

#### \[h2\]getResultSize8+

getResultSize(query: Query): Promise<number>

Obtains the number of results that match the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of results obtained. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch\_test");
    query.deviceId('localDeviceId');
    kvStore.getResultSize(query).then((resultSize) => {
        console.log('getResultSet succeed.');
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSize e ' + e);
}

#### \[h2\]getResultSize8+

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

Obtains the number of results that match the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/tvO7ZpFWTbuIebjuli69-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09B3773DD9AB0BE8B725C889829132A84586F4402332A4B2ED17E62F7767EBFA)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query8) | Yes | **Query** object to match. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of results obtained. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch\_test");
        kvStore.getResultSize('localDeviceId', query, async function (err, resultSize) {
            console.log('getResultSet succeed.');
        });
    });
} catch(e) {
    console.log('GetResultSize e ' + e);
}

#### \[h2\]getResultSize8+

getResultSize(deviceId: string, query: Query): Promise<number>

Obtains the number of results that match the specified device ID and **Query** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/e2nr_A3KSRqGqV_VKnRldA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B92DD9D104797B27ECC0EAC992DB1EE420FFC6A161366926872A1F3444E97D74)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query8) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of results obtained. |

**Example**

let kvStore;
try {
    let entries = \[\];
    for (var i = 0; i < 10; i++) {
        var key = 'batch\_test\_string\_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch\_test\_string\_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    var query = new distributedData.Query();
    query.prefixKey("batch\_test");
    kvStore.getResultSize('localDeviceId', query).then((resultSize) => {
        console.log('getResultSet succeed.');
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSize e ' + e);
}

#### \[h2\]removeDeviceData8+

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

Deletes data of the specified device from this KV store. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/5XIyHZOYTSSeos9VPJC4-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97E03E49512875170E85D1F30B7D97D096CA48AB1ECDAF2943981C821170686E)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, async function (err,data) {
        console.log('RemoveDeviceData  put success');
        const deviceid = 'no\_exist\_device\_id';
        kvStore.removeDeviceData(deviceid, async function (err,data) {
            if (err == undefined) {
                console.log('removeDeviceData success');
            } else {
                console.log('removeDeviceData fail');
                kvStore.get('localDeviceId', KEY\_TEST\_STRING\_ELEMENT, async function (err,data) {
                    console.log('RemoveDeviceData get success');
                });
            }
        });
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}

#### \[h2\]removeDeviceData8+

removeDeviceData(deviceId: string): Promise<void>

Deletes data of the specified device from this KV store. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/CqBDWoBURSy2v6doRGyn3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=761010BA6F57AC3E623FB65F5482BBF9FCB3BADC37CFBB90657A8BF35E773AEA)

The value of **deviceId** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let kvStore;
const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then((err) => {
        console.log('RemoveDeviceData put success');
    }).catch((err) => {
        console.log('RemoveDeviceData put fail ' + JSON.stringify(err));
    });
    const deviceid = 'no\_exist\_device\_id';
    kvStore.removeDeviceData(deviceid).then((err) => {
        console.log('removeDeviceData success');
    }).catch((err) => {
        console.log('removeDeviceData fail ' + JSON.stringify(err));
    });
    kvStore.get('localDeviceId', KEY\_TEST\_STRING\_ELEMENT).then((data) => {
        console.log('RemoveDeviceData get success data:' + data);
    }).catch((err) => {
        console.log('RemoveDeviceData get fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}

#### \[h2\]sync8+

sync(deviceIds: string\[\], mode: SyncMode, delayMs?: number): void

Synchronizes the KV store manually.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/nD6Scb6ESGaaDRFkt82yhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B26A37F91220B9F6609F86EADF238ECE157E80006DC4DE2CC53E501D78235541)

**deviceIds** is **networkId** in DeviceInfo, which can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceIds | string\[\] | Yes | **networkId**s of the devices to be synchronized. |
| mode | [SyncMode](#syncmode) | Yes | Sync mode. |
| delayMs | number | No | Delay time allowed, in milliseconds. The default value is **0**. |

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let devManager;
let kvStore;
const KEY\_TEST\_SYNC\_ELEMENT = 'key\_test\_sync';
const VALUE\_TEST\_SYNC\_ELEMENT = 'value-string-001';
// create deviceManager
deviceManager.createDeviceManager('bundleName', (err, value) => {
  if (!err) {
    devManager = value;
    let deviceIds = \[\];
    if (devManager != null) {
      var devices = devManager.getTrustedDeviceListSync();
      for (var i = 0; i < devices.length; i++) {
        deviceIds\[i\] = devices\[i\].networkId;
      }
    }
    try {
      kvStore.on('syncComplete', function (data) {
        console.log('Sync dataChange');
      });
      kvStore.put(KEY\_TEST\_SYNC\_ELEMENT + 'testSync101', VALUE\_TEST\_SYNC\_ELEMENT, function (err, data) {
        if (err != undefined) {
          console.log("put err: " + JSON.stringify(err));
          return;
        }
        console.log('Succeeded in putting data');
        const mode = distributedData.SyncMode.PULL\_ONLY;
        kvStore.sync(deviceIds, mode, 1000);
      });
    } catch (e) {
      console.log('Sync e' + e);
    }
  }
});

#### \[h2\]on('dataChange')8+

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

Subscribes to data changes of the specified type.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates data changes. |
| type | [SubscribeType](#subscribetype) | Yes | Type of data change. |
| listener | Callback<[ChangeNotification](#changenotification)\> | Yes | Callback used to return the result. |

**Example**

let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_LOCAL, function (data) {
    console.log("dataChange callback call data: " + JSON.stringify(data));
});

#### \[h2\]on('syncComplete')8+

on(event: 'syncComplete', syncCallback: Callback<Array<\[string, number\]>>): void

Subscribes to sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | Yes | Callback used to return a sync completion event. |

**Example**

let kvStore;
const KEY\_TEST\_FLOAT\_ELEMENT = 'key\_test\_float';
const VALUE\_TEST\_FLOAT\_ELEMENT = 321.12;
try {
    kvStore.on('syncComplete', function (data) {
        console.log('syncComplete ' + data)
    });
    kvStore.put(KEY\_TEST\_FLOAT\_ELEMENT, VALUE\_TEST\_FLOAT\_ELEMENT).then((data) => {
        console.log('syncComplete put success');
    }).catch((error) => {
        console.log('syncComplete put fail ' + error);
    });
}catch(e) {
    console.log('syncComplete put e ' + e);
}

#### \[h2\]off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

Unsubscribes from data changes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates data changes. |
| listener | Callback<[ChangeNotification](#changenotification)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for data changes will be unregistered. |

**Example**

let kvStore;
class KvstoreModel {
    call(data) {
        console.log("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}

#### \[h2\]off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<\[string, number\]>>): void

Unsubscribes from sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | No | Callback to unregister. If this parameter is not specified, all callbacks for data changes will be unregistered. |

**Example**

let kvStore;
class KvstoreModel {
    call(data) {
        console.log("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}

#### SyncMode

Enumerates the sync modes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PULL\_ONLY | 0 | Pull data from the peer end to the local end only. |
| PUSH\_ONLY | 1 | Push data from the local end to the peer end only. |
| PUSH\_PULL | 2 | Push data from the local end to the peer end and then pull data from the peer end to the local end. |
