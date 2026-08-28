# @ohos.data.distributedKVStore (Distributed KV Store)

The **distributedKVStore** module implements collaboration between databases for different devices that form a Super Device. You can use the APIs provided by this module to save application data to a distributed key-value (KV) store and perform operations, such as adding, deleting, modifying, and querying data, and synchronizing data across devices.

The **distributedKVStore** module provides the following functionalities:

-   [KVManager](#kvmanager): provides a **KVManager** instance to obtain KV store information.
-   [KVStoreResultSet](#kvstoreresultset): provides APIs for accessing the results obtained from a KV store.
-   [Query](#query): provides APIs for setting predicates for data query.
-   [SingleKVStore](#singlekvstore): provides APIs for querying data in single KV stores and synchronizing data across devices. The single KV stores manage data without distinguishing devices.
-   [DeviceKVStore](#devicekvstore): provides APIs for querying data in device KV stores and synchronizing data across devices. This class inherits from [SingleKVStore](#singlekvstore). The device KV stores manage data by device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/8MDAAGNXTNa7EvbOc3fPvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDADEA1E99E7657AACBD9DC17E06577412C84B6D0F14E45294397A6E799E053C)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { distributedKVStore } from '@kit.ArkData';

#### KVManagerConfig

Provides the **KVManager** instance configuration, including the bundle name of the invoker and the application context.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | BaseContext | No | No | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

Since API version 10, the parameter type of context is [BaseContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md).

 |
| bundleName | string | No | No | Bundle name. |

#### Constants

Provides constants of the distributed KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| MAX\_KEY\_LENGTH | number | Yes | No | Maximum length of a key in the database, which is 1024 bytes. |
| MAX\_VALUE\_LENGTH | number | Yes | No | Maximum length of a value in the database, which is 4194303 bytes. |
| MAX\_KEY\_LENGTH\_DEVICE | number | Yes | No | Maximum length of a key in a device KV store, which is 896 bytes. |
| MAX\_STORE\_ID\_LENGTH | number | Yes | No | Maximum length of a KV store ID, which is 128 bytes. |
| MAX\_QUERY\_LENGTH | number | Yes | No | Maximum query length, which is 512000 bytes. |
| MAX\_BATCH\_SIZE | number | Yes | No | Maximum number of batch operations allowed, which is 128. |

#### ValueType

Enumerates the types of the value in a KV pair.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STRING | 0 | String. |
| INTEGER | 1 | Integer. |
| FLOAT | 2 | Float (single-precision floating point). |
| BYTE\_ARRAY | 3 | Byte array. |
| BOOLEAN | 4 | Boolean. |
| DOUBLE | 5 | Double (double-precision floating point). |

#### Value

Defines the **value** object in a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ValueType](#valuetype) | No | No | Type of the value. |
| value | Uint8Array | string | number | boolean | No | No | Value of the KV pair. |

#### Entry

Defines the KV pairs stored in a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| key | string | No | No | Key of the KV pair. |
| value | [Value](#value) | No | No | Value object of the KV pair. |

#### ChangeNotification

Defines the content of a data change notification, including inserted data, updated data, deleted data, and device ID.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| insertEntries | [Entry](#entry)\[\] | No | No | Data inserted. |
| updateEntries | [Entry](#entry)\[\] | No | No | Data updated. |
| deleteEntries | [Entry](#entry)\[\] | No | No | Data deleted. |
| deviceId | string | No | No | UUID of the device. |

#### SyncMode

Enumerates the sync modes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PULL\_ONLY | 0 | Pull data from the peer end to the local end only. |
| PUSH\_ONLY | 1 | Push data from the local end to the peer end only. |
| PUSH\_PULL | 2 | Push data from the local end to the peer end and then pull data from the peer end to the local end. |

#### SubscribeType

Enumerates the subscription types.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SUBSCRIBE\_TYPE\_LOCAL | 0 | Local data changes. |
| SUBSCRIBE\_TYPE\_REMOTE | 1 | Remote data changes. |
| SUBSCRIBE\_TYPE\_ALL | 2 | Local and remote data changes. |

#### KVStoreType

Enumerates the distributed KV store types.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_COLLABORATION | 0 | 
Device KV store.

The device KV store manages data by device, which eliminates conflicts. Data can be queried by device.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

 |
| SINGLE\_VERSION | 1 | 

Single KV store.

The single KV store does not differentiate data by device. If entries with the same key are modified on different devices, the value will be overwritten.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |

#### SecurityLevel

Enumerates the KV store security levels.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/L4hjE0-LRMasZ12HfyhIMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBC2E991C09B7A4D9D06DC366A1F3BAB1209B244D7DC97C7498C3989133C42B7)

For the scenarios involving a single device, you can upgrade the security level of a KV store by modifying the **securityLevel** parameter. When upgrading the database security level, observe the following:

-   This operation does not apply to the databases that require cross-device sync. Data cannot be synced between databases of different security levels. If you want to upgrade the security level of a database, you are advised to create a database of a higher security level.
-   You need to close the database before modifying the **securityLevel** parameter, and open it after the security level is upgraded.
-   You cannot downgrade the database security level. For example, you can change the database security level from S2 to S3, but cannot change it from S3 to S2.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| S1 | 2 | 
Low security level. Disclosure, tampering, corruption, or loss of the data may cause minor impact on an individual or group.

Examples: gender and nationality information, and user application records

 |
| S2 | 3 | 

Medium security level. Disclosure, tampering, corruption, or loss of the data may cause major impact on an individual or group.

Examples: individual mailing addresses and nicknames

 |
| S3 | 5 | 

High security level. Disclosure, tampering, corruption, or loss of the data may cause critical impact on an individual or group.

Examples: real-time precise positioning information and movement trajectory

 |
| S4 | 6 | 

Critical security level. Disclosure, tampering, corruption, or loss of the data may cause significant adverse impact on an individual or group.

Examples: political opinions, religious and philosophical belief, trade union membership, genetic data, biological information, health and sexual life status, sexual orientation, device authentication, and personal credit card information

 |

#### Options

Provides KV store configuration.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| createIfMissing | boolean | No | Yes | 
Whether to create a database when database files do not exist. The value **true** means to create a database, and the value **false** means the opposite. The default value is **true**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| encrypt | boolean | No | Yes | 

Whether to encrypt the database files. The value **true** means to encrypt the database files, and the value **false** means the opposite. The default value is **false**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| backup | boolean | No | Yes | 

Whether to back up the database files. The value **true** means to back up the database files, and the value **false** means the opposite. The default value is **true**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| autoSync | boolean | No | Yes | 

Whether to enable auto sync across devices. The default value is **false**, indicating that only manual sync is supported. If this parameter is set to **true**, it takes effect only in device collaboration using cross-device calls.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

 |
| kvStoreType | [KVStoreType](#kvstoretype) | No | Yes | 

Type of the KV store to create. The default value is **DEVICE\_COLLABORATION**, which indicates a device KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| securityLevel | [SecurityLevel](#securitylevel) | No | No | 

Security level of the KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

 |
| schema | [Schema](#schema) | No | Yes | 

Schema that defines the values stored in the KV store. The default value is **undefined**, which means no schema is used.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

 |

#### Schema

Defines the schema of a KV store. You can create a **Schema** object and pass it in [Options](#options) when creating or opening a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| root | [FieldNode](#fieldnode) | No | No | Definitions of all the fields in **Value**. |
| indexes | Array<string> | No | No | Indexes of the fields in **Value**. Indexes are created only for **FieldNode** with this parameter specified. The format is **'$.field1'**, **'$.field2'**. |
| mode | number | No | No | Schema mode, which can be **0** (compatible mode) or **1** (strict mode). |
| skip | number | No | No | Number of bytes to be skipped during the value check. The value range is \[0, 4 x 1024 x 1024 - 2\]. |

Strict mode: In this mode, the value to be inserted must strictly match the schema defined, and the number and format of fields must be consistent with that defined in the schema. Otherwise, an error will be returned.

Compatible mode: In this mode, the value check is successful as long as the value has the characteristics defined in the schema. Extra fields are allowed. For example, if **id** and **name** are defined, more fields such as **id**, **name**, and **age** can be inserted.

#### \[h2\]constructor

constructor()

Defines a constructor used to create a **Schema** instance.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Example**

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
schema.mode = 1;
schema.skip = 0;

#### FieldNode

Represents a **Schema** instance, which provides the methods for defining the values stored in a KV store.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| nullable | boolean | No | No | Whether the field can be null. The value **true** means the node field can be null; the value **false** means the opposite. |
| default | string | No | No | Default value of **FieldNode**. The value of **default** must be a string literal that can be parsed by the type. Ensure that the value type is the same as **type**. |
| type | number | No | No | **FieldNode** data type, which is a value of [ValueType](#valuetype). Currently, the BYTE\_ARRAY type is not supported. Using this type may cause a failure in calling [getKVStore](#getkvstore). |

#### \[h2\]constructor

constructor(name: string)

Defines a constructor used to create a **FieldNode** instance with a string field.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Value of **FieldNode**, with a maximum of 64 characters. This parameter cannot be left blank. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

#### \[h2\]appendChild

appendChild(child: FieldNode): boolean

Appends a child node to this **FieldNode**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| child | [FieldNode](#fieldnode) | Yes | Child node to append. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

try {
  let node: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("root");
  let child1: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child1");
  let child2: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child2");
  let child3: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child3");
  node.appendChild(child1);
  node.appendChild(child2);
  node.appendChild(child3);
  console.info("appendNode " + JSON.stringify(node));
  child1 = null;
  child2 = null;
  child3 = null;
  node = null;
} catch (e) {
  console.error("AppendChild " + e);
}

#### distributedKVStore.createKVManager

createKVManager(config: KVManagerConfig): KVManager

Creates a **KVManager** instance for KV store management.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [KVManagerConfig](#kvmanagerconfig) | Yes | Configuration of the **KVManager** instance, including the bundle name (cannot be empty) of the caller and user information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [KVManager](#kvmanager) | **KVManager** instance created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let kvManager: distributedKVStore.KVManager;
let appId: string = 'com.example.datamanagertest';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info("MyAbilityStage onCreate");
    let context = this.context;
    const kvManagerConfig: distributedKVStore.KVManagerConfig = {
      context: context,
      bundleName: appId
    }
    try {
      kvManager = distributedKVStore.createKVManager(kvManagerConfig);
      console.info("Succeeded in creating KVManager");
    } catch (e) {
      let error = e as BusinessError;
      console.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
    if (kvManager !== undefined) {
      // Perform subsequent operations such as creating a KV store.
      // ...
    }
  }
}

FA model:

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let kvManager: distributedKVStore.KVManager;
let appId: string = 'com.example.datamanagertest';
let context = featureAbility.getContext();
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
  context: context,
  bundleName: appId
}
try {
  kvManager = distributedKVStore.createKVManager(kvManagerConfig);
  console.info("Succeeded in creating KVManager");
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
}
if (kvManager !== undefined) {
  kvManager = kvManager as distributedKVStore.KVManager;
  // Perform subsequent operations such as creating a KV store.
  // ...
}

#### KVManager

Provides an instance to obtain information about a distributed KV store. Before calling any API in **KVManager**, you must use [createKVManager](#distributedkvstorecreatekvmanager) to create a **KVManager** instance.

#### \[h2\]getKVStore

getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void

Creates and obtains a distributed KV store based on the specified **options** and **storeId**. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/S22nXSIOR-Wt192aKRaUsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D89868BF50DC8563E585649E9A3857C79C8CFD181306FDBBD4CBDBD000E8156)

If the database file cannot be opened (for example, the file header is damaged) when an existing distributed KV store is obtained, the automatic rebuild logic will be triggered to return a newly created distributed KV store instance. For important data that cannot be regenerated, you are advised to use the backup and restore feature to prevent data loss. For details, see [Database Backup and Restoration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| storeId | string | Yes | Unique identifier of the KV store. The KV store ID allows only letters, digits, and underscores (\_), and cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants) in length. |
| options | [Options](#options) | Yes | Configuration of the KV store to create. |
| callback | AsyncCallback<T> | Yes | Callback used to return the **SingleKVStore** or **DeviceKVStore** instance created. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100002 | Open existed database with changed options. |
| 15100003 | Database corrupted. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
try {
  const options: distributedKVStore.Options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S3
  };
  kvManager.getKVStore('storeId', options, (err: BusinessError, store: distributedKVStore.SingleKVStore) => {
    if (err) {
      console.error(\`Failed to get KVStore.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info("Succeeded in getting KVStore");
    kvStore = store;
    if (kvStore !== null) {
       // Perform subsequent data operations, such as adding, deleting, modifying, and querying data, and subscribing to data changes.
       // ...
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getKVStore

getKVStore<T>(storeId: string, options: Options): Promise<T>

Creates and obtains a distributed KV store based on the specified **options** and **storeId**. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/723Mzj18RiuJXWh_jmYFIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7444B0C851D07EF6874CFFE84A02692530781CE2CC5F49E5C187BB7B7E349DE8)

If the database file cannot be opened (for example, the file header is damaged) when an existing distributed KV store is obtained, the automatic rebuild logic will be triggered to return a newly created distributed KV store instance. For important data that cannot be regenerated, you are advised to use the backup and restore feature to prevent data loss. For details, see [Database Backup and Restoration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| storeId | string | Yes | Unique identifier of the KV store. The KV store ID allows only letters, digits, and underscores (\_), and cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants) in length. |
| options | [Options](#options) | Yes | Configuration of the KV store to create. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<T> | Promise used to return the **SingleKVStore** or **DeviceKVStore** instance created. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100002 | Open existed database with changed options. |
| 15100003 | Database corrupted. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
try {
  const options: distributedKVStore.Options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S3
  };
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then((store: distributedKVStore.SingleKVStore) => {
    console.info("Succeeded in getting KVStore");
    kvStore = store;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get KVStore.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]closeKVStore

closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

Closes a distributed KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the application. It cannot be empty and its length cannot exceed 256 characters. |
| storeId | string | Yes | Unique identifier of the KV store to close. The KV store ID allows only letters, digits, and underscores (\_), and cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants) in length. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
    if (err != undefined) {
      console.error(\`Failed to get KVStore.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId is the one in createKVManager.
      kvManager.closeKVStore(appId, 'storeId', (err: BusinessError)=> {
        if (err != undefined) {
          console.error(\`Failed to close KVStore.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in closing KVStore');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]closeKVStore

closeKVStore(appId: string, storeId: string): Promise<void>

Closes a distributed KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the application. It cannot be empty and its length cannot exceed 256 characters. |
| storeId | string | Yes | Unique identifier of the KV store to close. The KV store ID allows only letters, digits, and underscores (\_), and cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants) in length. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then(async (store: distributedKVStore.SingleKVStore | null) => {
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId is the one in createKVManager.
      kvManager.closeKVStore(appId, 'storeId').then(() => {
        console.info('Succeeded in closing KVStore');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to close KVStore.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get KVStore.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to close KVStore.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deleteKVStore

deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

Deletes a distributed KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the application. It cannot be empty and its length cannot exceed 256 characters. |
| storeId | string | Yes | Unique identifier of the KV store to delete. The KV store ID allows only letters, digits, and underscores (\_), and cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants) in length. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100004 | Not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
    if (err != undefined) {
      console.error(\`Failed to get KVStore.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId is the one in createKVManager.
      kvManager.deleteKVStore(appId, 'storeId', (err: BusinessError) => {
        if (err != undefined) {
          console.error(\`Failed to delete KVStore.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info(\`Succeeded in deleting KVStore\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to delete KVStore.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deleteKVStore

deleteKVStore(appId: string, storeId: string): Promise<void>

Deletes a distributed KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the application. It cannot be empty and its length cannot exceed 256 characters. |
| storeId | string | Yes | Unique identifier of the KV store to delete. The KV store ID allows only letters, digits, and underscores (\_), and cannot exceed [MAX\_STORE\_ID\_LENGTH](#constants) in length. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100004 | Not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then(async (store: distributedKVStore.SingleKVStore | null) => {
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId is the one in createKVManager.
      kvManager.deleteKVStore(appId, 'storeId').then(() => {
        console.info('Succeeded in deleting KVStore');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to delete KVStore.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get KVStore.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to delete KVStore.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getAllKVStoreId

getAllKVStoreId(appId: string, callback: AsyncCallback<string\[\]>): void

Obtains the IDs of all distributed KV stores that are created by [getKVStore](#getkvstore) and have not been deleted by [deleteKVStore](#deletekvstore). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the application. It cannot be empty and its length cannot exceed 256 characters. |
| callback | AsyncCallback<string\[\]> | Yes | Callback used to return the IDs of all the distributed KV stores created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  // appId is the one in createKVManager.
  kvManager.getAllKVStoreId(appId, (err: BusinessError, data: string\[\]) => {
    if (err != undefined) {
      console.error(\`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting AllKVStoreId');
    console.info(\`GetAllKVStoreId size = ${data.length}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getAllKVStoreId

getAllKVStoreId(appId: string): Promise<string\[\]>

Obtains the IDs of all distributed KV stores that are created by [getKVStore](#getkvstore) and have not been deleted by [deleteKVStore](#deletekvstore). This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Bundle name of the application. It cannot be empty and its length cannot exceed 256 characters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string\[\]> | Promise used to return the IDs of all the distributed KV stores created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  // appId is the one in createKVManager.
  console.info('GetAllKVStoreId');
  kvManager.getAllKVStoreId(appId).then((data: string\[\]) => {
    console.info('Succeeded in getting AllKVStoreId');
    console.info(\`GetAllKVStoreId size = ${data.length}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]on('distributedDataServiceDie')

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

Subscribes to the termination (death) of the distributed data service. If the service is terminated, you need to register the callbacks for data change notifications and cross-device sync completion notifications again. In addition, an error will be returned for a sync operation.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **distributedDataServiceDie**, which indicates the termination of the distributed data service. |
| deathCallback | Callback<void> | Yes | Callback function. If the subscription is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info('KVManagerOn');
  const deathCallback = () => {
    console.info('death callback call');
  }
  kvManager.on('distributedDataServiceDie', deathCallback);
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]off('distributedDataServiceDie')

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

Unsubscribes from the termination (death) of the distributed data service. The **deathCallback** parameter must be a callback registered for subscribing to the termination of the distributed data service. Otherwise, the unsubscription will fail.

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **distributedDataServiceDie**, which indicates the termination of the distributed data service. |
| deathCallback | Callback<void> | No | Callback function. If this parameter is not specified, this API unregisters all callbacks for the **distributedDataServiceDie** event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info('KVManagerOff');
  const deathCallback = () => {
    console.info('death callback call');
  }
  kvManager.off('distributedDataServiceDie', deathCallback);
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### KVStoreResultSet

Provides APIs for obtaining the distributed KV store result sets. A maximum of eight result sets can be opened at a time.

The **KVStoreResultSet** instance is not refreshed in real time. After using the result set, if the data in the database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest data.

Before calling any API in **KVStoreResultSet**, you must use **[getKVStore](#getkvstore)** to construct a **SingleKVStore** or **DeviceKVStore** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/lrRwzeR1RwaIDWSDaypkAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D520294725E09D748DAD249959731FD23ECC4FA8B551D82DFEA244B506CBC79A)

The cursor start position of **KVStoreResultSet** is **\-1**.

#### \[h2\]getCount

getCount(): number

Obtains the total number of rows in the result set.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total number of rows obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let count: number;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    count = resultSet.getCount();
    console.info("getCount succeed:" + count);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("getCount failed: " + e);
}

#### \[h2\]getPosition

getPosition(): number

Obtains the current data read position (position from which data is read) in the result set. The read position changes with the operations, such as [moveToFirst](#movetofirst) and [moveToLast](#movetolast).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Current data read position obtained. The value must be greater than or equal to **\-1**. The value **\-1** means no data is read; the value **0** indicates the first row. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let position: number;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeeded.');
    resultSet = result;
    position = resultSet.getPosition();
    console.info("getPosition succeed:" + position);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("getPosition failed: " + e);
}

#### \[h2\]moveToFirst

moveToFirst(): boolean

Moves the data read position to the first row. If the result set is empty, **false** will be returned.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    moved = resultSet.moveToFirst();
    console.info("moveToFirst succeed: " + moved);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToFirst failed " + e);
}

#### \[h2\]moveToLast

moveToLast(): boolean

Moves the data read position to the last row. If the result set is empty, **false** will be returned.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    moved = resultSet.moveToLast();
    console.info("moveToLast succeed:" + moved);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToLast failed: " + e);
}

#### \[h2\]moveToNext

moveToNext(): boolean

Moves the data read position to the next row. If the result set is empty, **false** will be returned. This API applies when the whole result set is obtained.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    do {
      moved = resultSet.moveToNext();
      console.info("moveToNext succeed: " + moved);
    } while (moved)
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToNext failed: " + e);
}

#### \[h2\]moveToPrevious

moveToPrevious(): boolean

Moves the data read position to the previous row. If the result set is empty, **false** will be returned. This API applies when the whole result set is obtained.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    moved = resultSet.moveToLast();
    moved = resultSet.moveToPrevious();
    console.info("moveToPrevious succeed:" + moved);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToPrevious failed: " + e);
}

#### \[h2\]move

move(offset: number): boolean

Moves the data read position with the specified offset from the current position. That is, moves the number of rows specified by **offset** from the current position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Offset to move the data read position. A positive value means to move forward; a negative value means to move backward. If the cursor is beyond the start or end position of the result set, **false** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    moved = resultSet.move(2); // If the current position is 0, move the read position forward by two rows, that is, move to row 3.
    console.info(\`Succeeded in moving.moved = ${moved}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to move.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]moveToPosition

moveToPosition(position: number): boolean

Moves the data read position from 0 to an absolute position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | number | Yes | Absolute position to move to. If the absolute position exceeds the start or end position of the result set, **false** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    moved = resultSet.moveToPosition(1);
    console.info(\`Succeeded in moving to position.moved=${moved}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to move to position.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]isFirst

isFirst(): boolean

Checks whether the data read position is the first row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the first row is being read; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let isFirst: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    isFirst = resultSet.isFirst();
    console.info("Check isFirst succeed:" + isFirst);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isFirst failed: " + e);
}

#### \[h2\]isLast

isLast(): boolean

Checks whether the data read position is the last row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the last row is being read; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let isLast: boolean;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    isLast = resultSet.isLast();
    console.info("Check isLast succeed: " + isLast);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isLast failed: " + e);
}

#### \[h2\]isBeforeFirst

isBeforeFirst(): boolean

Checks whether the data read position is before the first row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data read position is before the first row; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    let isBeforeFirst = resultSet.isBeforeFirst();
    console.info("Check isBeforeFirst succeed: " + isBeforeFirst);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isBeforeFirst failed: " + e);
}

#### \[h2\]isAfterLast

isAfterLast(): boolean

Checks whether the data read position is after the last row.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data read position is after the last row; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    let isAfterLast = resultSet.isAfterLast();
    console.info("Check isAfterLast succeed:" + isAfterLast);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isAfterLast failed: " + e);
}

#### \[h2\]getEntry

getEntry(): Entry

Obtains the KV pair from the current position.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Entry](#entry) | KV pair obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    let entry = resultSet.getEntry();
    console.info("getEntry succeed:" + JSON.stringify(entry));
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("getEntry failed: " + e);
}

#### Query

Provides methods to create a **Query** object, which defines different data query criteria. A **Query** object supports a maximum of 256 predicates.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

#### \[h2\]constructor

constructor()

Defines a constructor used to create a **Query** instance.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

#### \[h2\]reset

reset(): Query

Resets the **Query** object.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object reset. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo("key", "value");
    console.info("query is " + query.getSqlLike());
    query.reset();
    console.info("query is " + query.getSqlLike());
  }
  query = null;
} catch (e) {
  console.error("simply calls should be ok :" + e);
}

#### \[h2\]equalTo

equalTo(field: string, value: number|string|boolean): Query

Creates a **Query** object to match the specified field whose value is equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/YWIeIfCdRuSc7m4_PT113w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B2B6DEF6F024E9D9D9835081E43BD58646409386F6F0383D8ED5861F3EC2DCD)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | number|string|boolean | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo("field", "value");
    console.info(\`query is ${query.getSqlLike()}\`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]notEqualTo

notEqualTo(field: string, value: number|string|boolean): Query

Creates a **Query** object to match the specified field whose value is not equal to the specified value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Ji0kAAALQ06ImsctV6bBKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2AE048D044B7CE4304AA9E4BA06ACA9ADA5372311CA1267E977639A01BC4DD9)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | number|string|boolean | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo("field", "value");
    console.info(\`query is ${query.getSqlLike()}\`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]greaterThan

greaterThan(field: string, value: number|string|boolean): Query

Creates a **Query** object to match the specified field whose value is greater than the specified value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/QHG2Obu0S8qf3D0pxVeQRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8CE527DE413B0167AF37B24E7A83331EF42B0D13C595CAE55E6B7A0EEB358E3)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | number|string|boolean | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.greaterThan("field", "value");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]lessThan

lessThan(field: string, value: number|string): Query

Creates a **Query** object to match the specified field whose value is less than the specified value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/FhXg35T4RdiFwW71EwjrpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CFF856333DB353D557EFA038784AEFC652585D71306B89AD2746EA6AD6131DB)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | number|string | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.lessThan("field", "value");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]greaterThanOrEqualTo

greaterThanOrEqualTo(field: string, value: number|string): Query

Creates a **Query** object to match the specified field whose value is greater than or equal to the specified value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/p-q-SPtGSh2WIWdR8nW5UA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=843EA4B868EC4765C9FFF0956471BAFE4A47C9D50E0E1548B2F48DB52D8140ED)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | number|string | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.greaterThanOrEqualTo("field", "value");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]lessThanOrEqualTo

lessThanOrEqualTo(field: string, value: number|string): Query

Creates a **Query** object to match the specified field whose value is less than or equal to the specified value.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/hZbJE_fTQCmRJEmSKKZTKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A11D265C38BC53F446D51EE4696B687CE567AB4676859476961BCAFCFA356409)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | number|string | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.lessThanOrEqualTo("field", "value");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]isNull

isNull(field: string): Query

Creates a **Query** object to match the specified field whose value is **null**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/FO4ScYJYQSiqWpaMa72o5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07328528DD2BA3B8C7FAC748FCEB3FA7D1AB9BD2C37D4B1011F8FB597F4ADFFF)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.isNull("field");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]inNumber

inNumber(field: string, valueList: number\[\]): Query

Creates a **Query** object to match the specified field whose value is within the specified list of numbers.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/LBiXUqxMTGak-otHKle-xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00FC7F9746C33BE695B7CE928BC64AFA08E015BD50482E5C470A9D014FC97EF4)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| valueList | number\[\] | Yes | List of numbers. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inNumber("field", \[0, 1\]);
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]inString

inString(field: string, valueList: string\[\]): Query

Creates a **Query** object to match the specified field whose value is within the specified list of strings.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/63ISpnVpRd6783LHgEHKfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24941119CAB274E1252BB82943F79828AEA361F03E2F45F7198EF47CCE7D2544)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| valueList | string\[\] | Yes | List of strings. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inString("field", \['test1', 'test2'\]);
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]notInNumber

notInNumber(field: string, valueList: number\[\]): Query

Creates a **Query** object to match the specified field whose value is not within the specified list of numbers.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/cGsvhv-LSB6Nni-BLTrTnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BE1A5FAB2AFA56B37590AC9E9E8FE7B48D22272BF81E41B2337FDBB5626395C)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| valueList | number\[\] | Yes | List of numbers. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInNumber("field", \[0, 1\]);
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]notInString

notInString(field: string, valueList: string\[\]): Query

Creates a **Query** object to match the specified field whose value is not within the specified list of strings.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/WPl8XUUwQWmPoUnaugFNAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA75B29B8C2CE0228D2DCF82DCED136DE716B602120E29F0BBD38F2A110964D3)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| valueList | string\[\] | Yes | List of strings. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInString("field", \['test1', 'test2'\]);
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]like

like(field: string, value: string): Query

Creates a **Query** object to match the specified field whose value is similar to the specified string.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/ESuZ5HT7RWSHB_VpFhpI4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EAD159F367E53CEBCAAE4E3ED088D5F4DADE509EEC1CD60507F087D75C895DE)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | string | Yes | String specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.like("field", "value");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]unlike

unlike(field: string, value: string): Query

Creates a **Query** object to match the specified field whose value is not similar to the specified string.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/YzfQuMZ3TSG0x-9H6vzVkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BFA20F10BE42C3AFA7A64E023D72DAF49C1E1AC8C86603CD94C983055F15C59)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |
| value | string | Yes | String specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.unlike("field", "value");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]and

and(): Query

Creates a **Query** object with the AND condition.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value1");
      query.and();
      query.notEqualTo("field", "value2");
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}

#### \[h2\]or

or(): Query

Creates a **Query** object with the OR condition.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value1");
      query.or();
      query.notEqualTo("field", "value2");
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}

#### \[h2\]orderByAsc

orderByAsc(field: string): Query

Creates a **Query** object to sort the query results in ascending order.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/uSCPBUlKSb6MhllLpKZcTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7B186A549C082605678E9341C2EDF78CF0745DD02A6CB2C93019955ACDAC8F2)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value");
      query.orderByAsc("field");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]orderByDesc

orderByDesc(field: string): Query

Creates a **Query** object to sort the query results in descending order.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/NQeqSOUfTLqdigPatBlE_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41A84CFECA8C69443924CDFCA1F560B5EAE61E514ECEA01CFB486DE7891160B4)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value");
      query.orderByDesc("field");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]limit

limit(total: number, offset: number): Query

Creates a **Query** object to specify the number of records of the query result and where to start. This API must be called after the invocation of the **orderByAsc()**, **orderByDesc()**, and the query APIs of the **Query** object.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| total | number | Yes | 
Maximum number of results to query. The value must be a non-negative integer.

If the value is a negative number, the entire result set is queried.

 |
| offset | number | Yes | 

Start position of the query result. The value must be a non-negative integer.

If the value is a negative number, the entire result set is queried.

If **offset** exceeds the end of the result set, the query result is empty.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let total = 10;
let offset = 1;
try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo("field", "value");
    query.limit(total, offset);
    console.info(\`query is ${query.getSqlLike()}\`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]isNotNull

isNotNull(field: string): Query

Creates a **Query** object to match the specified field whose value is not **null**.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/KQlcQQ57Q7KeGVwJVdNMrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D40BD9D71E8C7A202762508E36589AA20D271A29CE192E5D573B7333461BB37)

This API should be used together with [Schema](#schema).

For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV store using the **getKVStore()** method in [Persisting KV Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-kv-store#how-to-develop).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.isNotNull("field");
    console.info(\`query is ${query.getSqlLike()}\`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]beginGroup

beginGroup(): Query

Creates a **Query** object for a query condition group with a left parenthesis.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull("field");
      query.endGroup();
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}

#### \[h2\]endGroup

endGroup(): Query

Creates a **Query** object for a query condition group with a right parenthesis.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull("field");
      query.endGroup();
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}

#### \[h2\]prefixKey

prefixKey(prefix: string): Query

Creates a **Query** object with a specified key prefix.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | Key prefix, which cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.prefixKey("$.name");
      query.prefixKey("0");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]setSuggestIndex

setSuggestIndex(index: string): Query

Creates a **Query** object with an index preferentially used for query.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | string | Yes | Index to set, which cannot contain '^'. If the value contains '^', the predicate becomes invalid and all data in the KV store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.setSuggestIndex("$.name");
      query.setSuggestIndex("0");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deviceId

deviceId(deviceId:string):Query

Creates a **Query** object with the device ID as the key prefix.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/YbYLUyLwRQee0DyLfJVT-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81FB2C42C629EC49C57D43D70C4CB04FC998BB9BB5CAB9C33FE62411668E95C1)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device to be queried. This parameter cannot be left empty. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Query](#query) | **Query** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.deviceId("deviceId");
      console.info(\`query is ${query.getSqlLike()}\`);
    }
} catch (e) {
    let error = e as BusinessError;
    console.error(\`duplicated calls should be ok.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getSqlLike

getSqlLike():string

Obtains the query statement of the **Query** object.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Returns the query statement obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      let sql1 = query.getSqlLike();
      console.info(\`GetSqlLike sql= ${sql1}\`);
    }
} catch (e) {
    console.error("duplicated calls should be ok : " + e);
}

#### SingleKVStore

Provides APIs for data management in a single KV store, such as adding data, deleting data, and subscribing to data changes or across-device data sync completion events.

Before calling any method in **SingleKVStore**, you must use [getKVStore](#getkvstore) to obtain a **SingleKVStore** instance.

#### \[h2\]put

put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void

Adds a KV pair of the specified type to this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair to add. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| value | Uint8Array | string | number | boolean | Yes | Value of the KV pair to add. The value type can be Uint8Array, number, string, or boolean. A value of the Uint8Array or string type cannot exceed [MAX\_VALUE\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info("Succeeded in putting");
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
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

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(() => {
    console.info(\`Succeeded in putting data\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]putBatch

putBatch(entries: Entry\[\], callback: AsyncCallback<void>): void

Batch inserts KV pairs to this single KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| entries | [Entry](#entry)\[\] | Yes | KV pairs to insert, which cannot exceed 512 MB. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch\_test\_string\_key', (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
        }
        console.info('Succeeded in getting Entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      });
    } else {
      console.error('KvStore is null'); // The subsequent sample code is the same as the code here.
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message} \`);
}

#### \[h2\]putBatch

putBatch(entries: Entry\[\]): Promise<void>

Batch inserts KV pairs to this single KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| entries | [Entry](#entry)\[\] | Yes | KV pairs to insert, which cannot exceed 512 MB. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch\_test\_string\_key').then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting Entries');
        console.info(\`PutBatch ${entries}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message} \`);
}

#### \[h2\]delete

delete(key: string, callback: AsyncCallback<void>): void

Deletes a KV pair from this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the KV pair to delete. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.delete(KEY\_TEST\_STRING\_ELEMENT, (err: BusinessError) => {
        if (err != undefined) {
          console.error(\`Failed to delete.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in deleting');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
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

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(() => {
    console.info(\`Succeeded in putting data\`);
    if (kvStore != null) {
      kvStore.delete(KEY\_TEST\_STRING\_ELEMENT).then(() => {
        console.info('Succeeded in deleting');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to delete.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deleteBatch

deleteBatch(keys: string\[\], callback: AsyncCallback<void>): void

Batch deletes KV pairs from this single KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | string\[\] | Yes | KV pairs to delete. This parameter cannot be empty. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  let keys: string\[\] = \[\];
  for (let i = 0; i < 5; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
    keys.push(key + i);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.deleteBatch(keys, async (err: BusinessError) => {
        if (err != undefined) {
          console.error(\`Failed to delete Batch.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in deleting Batch');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deleteBatch

deleteBatch(keys: string\[\]): Promise<void>

Batch deletes KV pairs from this single KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keys | string\[\] | Yes | KV pairs to delete. This parameter cannot be empty. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  let keys: string\[\] = \[\];
  for (let i = 0; i < 5; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
    keys.push(key + i);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.deleteBatch(keys).then(() => {
        console.info('Succeeded in deleting Batch');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to delete Batch.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]removeDeviceData

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

Deletes data of a device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/EG3F_9fQSn-NxK_Rh1kqow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78F00D8DA4958637D497CF7A41C97EBF00A2D9EFD5551136E7DD724479234851)

**deviceId** is **networkId** in [DeviceBasicInfo](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo), which can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Network ID of the target device. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-002';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, async (err: BusinessError) => {
    console.info('Succeeded in putting data');
    const deviceid = 'no\_exist\_device\_id';
    if (kvStore != null) {
      kvStore.removeDeviceData(deviceid, async (err: BusinessError) => {
        if (err == undefined) {
          console.info('succeeded in removing device data');
        } else {
          console.error(\`Failed to remove device data.code is ${err.code},message is ${err.message} \`);
          if (kvStore != null) {
            kvStore.get(KEY\_TEST\_STRING\_ELEMENT, async (err: BusinessError, data: boolean | string | number | Uint8Array) => {
              console.info('Succeeded in getting data');
            });
          }
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`)
}

#### \[h2\]removeDeviceData

removeDeviceData(deviceId: string): Promise<void>

Deletes data of a device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/3Gb-R7LBQS-wjTvKSFrEIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0F4838D7FC783990E2394F3B39C37967B639E638D459DBC5A6829A0BFEC393E)

**deviceId** is **networkId** in [DeviceBasicInfo](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo), which can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | Network ID of the target device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-001';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(() => {
    console.info('Succeeded in putting data');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put data.code is ${err.code},message is ${err.message} \`);
  });
  const deviceid = 'no\_exist\_device\_id';
  kvStore.removeDeviceData(deviceid).then(() => {
    console.info('succeeded in removing device data');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to remove device data.code is ${err.code},message is ${err.message} \`);
  });
  kvStore.get(KEY\_TEST\_STRING\_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
    console.info('Succeeded in getting data');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get data.code is ${err.code},message is ${err.message} \`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`)
}

#### \[h2\]get

get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

Obtains the value of the specified key. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the value to obtain. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<boolean | string | number | Uint8Array> | Yes | Callback used to return the value obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info("Succeeded in putting");
    if (kvStore != null) {
      kvStore.get(KEY\_TEST\_STRING\_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
        if (err != undefined) {
          console.error(\`Failed to get.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info(\`Succeeded in getting data.data=${data}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]get

get(key: string): Promise<boolean | string | number | Uint8Array>

Obtains the value of the specified key. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the value to obtain. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean | string | number | Uint8Array> | Promise used to return the value obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(() => {
    console.info(\`Succeeded in putting data\`);
    if (kvStore != null) {
      kvStore.get(KEY\_TEST\_STRING\_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
        console.info(\`Succeeded in getting data.data=${data}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(keyPrefix: string, callback: AsyncCallback<Entry\[\]>): void

Obtains all KV pairs that match the specified key prefix. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch\_test\_string\_key', (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message} \`);
}

#### \[h2\]getEntries

getEntries(keyPrefix: string): Promise<Entry\[\]>

Obtains all KV pairs that match the specified key prefix. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch\_test\_string\_key').then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting Entries');
        console.info(\`PutBatch ${entries}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message} \`);
}

#### \[h2\]getEntries

getEntries(query: Query, callback: AsyncCallback<Entry\[\]>): void

Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | Key prefix to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified **Query** object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array(\[21, 31\]);
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_bool\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE\_ARRAY,
        value: arr
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: {entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getEntries(query, (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get Entries.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(query: Query): Promise<Entry\[\]>

Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified **Query** object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array(\[21, 31\]);
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_bool\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE\_ARRAY,
        value: arr
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: {entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getEntries(query).then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting Entries');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`)
  });
  console.info('Succeeded in getting Entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get Entries.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

Obtains a result set with the specified prefix from this single KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |
| callback | AsyncCallback<[KVStoreResultSet](#kvstoreresultset)\> | Yes | Callback used to return the result set with the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getResultSet('batch\_test\_string\_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting result set');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err :BusinessError) => {
            if (err != undefined) {
              console.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
              return;
            }
            console.info('Succeeded in closing result set');
          });
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(keyPrefix: string): Promise<KVStoreResultSet>

Obtains a result set with the specified prefix from this single KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVStoreResultSet](#kvstoreresultset)\> | Promise used to return the result set with the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void

Obtains a **KVStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | Query | Yes | **Query** object to match. |
| callback | AsyncCallback<[KVStoreResultSet](#kvstoreresultset)\> | Yes | Callback used to return the **KVStoreResultSet** object obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting result set');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(query: Query): Promise<KVStoreResultSet>

Obtains a **KVStoreResultSet** object that matches the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVStoreResultSet](#kvstoreresultset)\> | Promise used to return the **KVStoreResultSet** object obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch\_test");
  kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]closeResultSet

closeResultSet(resultSet: KVStoreResultSet, callback: AsyncCallback<void>): void

Closes the **KVStoreResultSet** object returned by [SingleKvStore.getResultSet](#getresultset-1). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resultSet | [KVStoreResultSet](#kvstoreresultset) | Yes | **KVStoreResultSet** object to close. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let resultSet: distributedKVStore.KVStoreResultSet;
try {
  kvStore.getResultSet('batch\_test\_string\_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
    if (err != undefined) {
      console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet, (err: BusinessError) => {
        if (err != undefined) {
          console.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in closing result set');
      })
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]closeResultSet

closeResultSet(resultSet: KVStoreResultSet): Promise<void>

Closes the **KVStoreResultSet** object returned by [SingleKvStore.getResultSet](#getresultset-1). This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resultSet | [KVStoreResultSet](#kvstoreresultset) | Yes | **KVStoreResultSet** object to close. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let resultSet: distributedKVStore.KVStoreResultSet;
try {
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
  });

} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSize

getResultSize(query: Query, callback: AsyncCallback<number>): void

Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of results obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, (err: BusinessError) => {
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getResultSize(query, (err: BusinessError, resultSize: number) => {
        if (err != undefined) {
          console.error(\`Failed to get result size.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting result set size');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSize

getResultSize(query: Query): Promise<number>

Obtains the number of results that match the specified **Query** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of results obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch\_test");
  kvStore.getResultSize(query).then((resultSize: number) => {
    console.info('Succeeded in getting result set size');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get result size.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]backup

backup(file:string, callback: AsyncCallback<void>):void

Backs up a distributed KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | Yes | Name of the KV store. The value cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.backup(backupFile, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to backup.code is ${err.code},message is ${err.message} \`);
    } else {
      console.info(\`Succeeded in backupping data\`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]backup

backup(file:string): Promise<void>

Backs up an RDB store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | Yes | Name of the KV store. The value cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.backup(backupFile).then(() => {
    console.info(\`Succeeded in backupping data\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to backup.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]restore

restore(file:string, callback: AsyncCallback<void>):void

Restores a distributed KV store from a database file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | Yes | Name of the database file. The value cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.restore(backupFile, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to restore.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info(\`Succeeded in restoring data\`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]restore

restore(file:string): Promise<void>

Restores a distributed KV store from a database file. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| file | string | Yes | Name of the database file. The value cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.restore(backupFile).then(() => {
    console.info(\`Succeeded in restoring data\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to restore.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deleteBackup

deleteBackup(files:Array<string>, callback: AsyncCallback<Array<\[string, number\]>>):void

Deletes a backup file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| files | Array<string> | Yes | Name of the backup file to delete. The value cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<Array<\[string, number\]>> | Yes | Callback used to return the name of the backup file deleted and the operation result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let files = \["BK001", "BK002"\];
try {
  kvStore.deleteBackup(files, (err: BusinessError, data: \[string, number\]\[\]) => {
    if (err) {
      console.error(\`Failed to delete Backup.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info(\`Succeed in deleting Backup.data=${data}\`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]deleteBackup

deleteBackup(files:Array<string>): Promise<Array<\[string, number\]>>

Deletes a backup file. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| files | Array<string> | Yes | Name of the backup file to delete. The value cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<\[string, number\]>> | Promise used to return the name of the backup file deleted and the operation result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let files = \["BK001", "BK002"\];
try {
  kvStore.deleteBackup(files).then((data: \[string, number\]\[\]) => {
    console.info(\`Succeed in deleting Backup.data=${data}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to delete Backup.code is ${err.code},message is ${err.message}\`);
  })
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]startTransaction

startTransaction(callback: AsyncCallback<void>): void

Starts the transaction in this single KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function putBatchString(len: number, prefix: string) {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < len; i++) {
    let entry: distributedKVStore.Entry = {
      key: prefix + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  return entries;
} // Custom function used outside the scope to prevent syntax check errors.

try {
  let count = 0;
  kvStore.on('dataChange', 0, (data: distributedKVStore.ChangeNotification) => {
    console.info(\`startTransaction 0 ${data}\`);
    count++;
  });
  kvStore.startTransaction(async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to start Transaction.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in starting Transaction');
    let entries = putBatchString(10, 'batch\_test\_string\_key');
    console.info(\`entries: ${entries}\`);
    if (kvStore != null) {
      kvStore.putBatch(entries, async (err: BusinessError) => {
        if (err != undefined) {
          console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in putting Batch');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to start Transaction.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]startTransaction

startTransaction(): Promise<void>

Starts the transaction in this single KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 14800047 | The WAL file size exceeds the default limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let count = 0;
  kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE\_TYPE\_ALL, (data: distributedKVStore.ChangeNotification) => {
    console.info(\`startTransaction 0 ${data}\`);
    count++;
  });
  kvStore.startTransaction().then(async () => {
    console.info('Succeeded in starting Transaction');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to start Transaction.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to start Transaction.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]commit

commit(callback: AsyncCallback<void>): void

Commits the transaction in this single KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.commit((err: BusinessError) => {
    if (err == undefined) {
      console.info('Succeeded in committing');
    } else {
      console.error(\`Failed to commit.code is ${err.code},message is ${err.message}\`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]commit

commit(): Promise<void>

Commits the transaction in this single KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.commit().then(async () => {
    console.info('Succeeded in committing');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to commit.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]rollback

rollback(callback: AsyncCallback<void>): void

Rolls back the transaction in this single KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.rollback((err: BusinessError) => {
    if (err == undefined) {
      console.info('Succeeded in rolling back');
    } else {
      console.error(\`Failed to rollback.code is ${err.code},message is ${err.message}\`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]rollback

rollback(): Promise<void>

Rolls back the transaction in this single KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.rollback().then(async () => {
    console.info('Succeeded in rolling back');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to rollback.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]enableSync

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

Sets cross-device data sync, which can be enabled or disabled. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable data sync across devices. The value **true** means to enable data sync across devices, and the value **false** means the opposite. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.enableSync(true, (err: BusinessError) => {
    if (err == undefined) {
      console.info('Succeeded in enabling sync');
    } else {
      console.error(\`Failed to enable sync.code is ${err.code},message is ${err.message}\`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]enableSync

enableSync(enabled: boolean): Promise<void>

Sets cross-device data sync, which can be enabled or disabled. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable data sync across devices. The value **true** means to enable data sync across devices, and the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.enableSync(true).then(() => {
    console.info('Succeeded in enabling sync');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to enable sync.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]setSyncRange

setSyncRange(localLabels: string\[\], remoteSupportLabels: string\[\], callback: AsyncCallback<void>): void

Sets the data sync range. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localLabels | string\[\] | Yes | Sync labels set for the local device. |
| remoteSupportLabels | string\[\] | Yes | Sync labels set for remote devices. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  const localLabels = \['A', 'B'\];
  const remoteSupportLabels = \['C', 'D'\];
  kvStore.setSyncRange(localLabels, remoteSupportLabels, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to set syncRange.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting syncRange');
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]setSyncRange

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

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  const localLabels = \['A', 'B'\];
  const remoteSupportLabels = \['C', 'D'\];
  kvStore.setSyncRange(localLabels, remoteSupportLabels).then(() => {
    console.info('Succeeded in setting syncRange');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set syncRange.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]setSyncParam

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

Sets the default delay for cross-device data sync. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/hfLx4E9NRr-I-93g8QQOeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A14F9A446D05F365434D8098E85D4DB0263609416F7A111450A5C849832DFC67)

After the default delay is set, calling [sync](#sync) will not trigger the cross-device data sync immediately. Instead, the data sync will be executed only after the specified delay duration.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| defaultAllowedDelayMs | number | Yes | Delay time to set, in ms. The value can be **0** or ranges from 100 to 86400000. |
| callback | AsyncCallback<void> | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  const defaultAllowedDelayMs = 500;
  kvStore.setSyncParam(defaultAllowedDelayMs, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to set syncParam.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting syncParam');
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]setSyncParam

setSyncParam(defaultAllowedDelayMs: number): Promise<void>

Sets the default delay for cross-device data sync. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/gliB17XHR0GIIg508KeYMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76DA51018A0F72BE183A3215FAFE27890177611AD85C3CE8FF2C80BBA738966C)

After the default delay is set, calling [sync](#sync) will not trigger the cross-device data sync immediately. Instead, the data sync will be executed only after the specified delay duration.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| defaultAllowedDelayMs | number | Yes | Delay time to set, in ms. The value can be **0** or ranges from 100 to 86400000. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  const defaultAllowedDelayMs = 500;
  kvStore.setSyncParam(defaultAllowedDelayMs).then(() => {
    console.info('Succeeded in setting syncParam');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set syncParam.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]sync

sync(deviceIds: string\[\], mode: SyncMode, delayMs?: number): void

Starts cross-device data sync manually. For details about the sync modes of KV stores, see [Cross-Device Synchronization of KV Stores](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-sync-of-kv-store).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/eZC4ob02SGCqsslE61n-8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16E3637AAC50EE057131BF988049650EB519C604FA62161AF1C7D27A2544BAC4)

**deviceIds** is **networkId** in [DeviceBasicInfo](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo), which can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceIds | string\[\] | Yes | List of **networkId**s of the devices in the same networking environment to be synchronized. |
| mode | [SyncMode](#syncmode) | Yes | Sync mode. |
| delayMs | number | No | Delay time allowed, in ms. The default value is **0**. If **delayMs** is set, data sync will be executed **delayMs** after **sync()** is called. If **delayMs** is not set, the delay set in [setSyncParam](#setsyncparam) is used. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |

**Example**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let devManager: distributedDeviceManager.DeviceManager;
const KEY\_TEST\_SYNC\_ELEMENT = 'key\_test\_sync';
const VALUE\_TEST\_SYNC\_ELEMENT = 'value-string-001';
// create deviceManager
export default class EntryAbility extends UIAbility {
  onCreate() {
    let context = this.context;
    try {
      devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
      let deviceIds: string\[\] = \[\];
      if (devManager != null) {
        let devices = devManager.getAvailableDeviceListSync();
        for (let i = 0; i < devices.length; i++) {
          deviceIds\[i\] = devices\[i\].networkId as string;
        }
      }
      try {
        if (kvStore != null) {
          kvStore.on('syncComplete', (data: \[string, number\]\[\]) => {
            console.info('Sync dataChange');
          });
          if (kvStore != null) {
            kvStore.put(KEY\_TEST\_SYNC\_ELEMENT + 'testSync101', VALUE\_TEST\_SYNC\_ELEMENT, (err: BusinessError) => {
              if (err != undefined) {
                console.error(\`Failed to sync.code is ${err.code},message is ${err.message}\`);
                return;
              }
              console.info('Succeeded in putting data');
              const mode = distributedKVStore.SyncMode.PULL\_ONLY;
              if (kvStore != null) {
                kvStore.sync(deviceIds, mode, 1000);
              }
            });
          }
        }
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`Failed to sync.code is ${error.code},message is ${error.message}\`);
      }

    } catch (err) {
      let error = err as BusinessError;
      console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
    }
  }
}

#### \[h2\]sync

sync(deviceIds: string\[\], query: Query, mode: SyncMode, delayMs?: number): void

Starts cross-device data sync manually. This API returns the result synchronously. For details about the sync modes of KV stores, see [Cross-Device Synchronization of KV Stores](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-sync-of-kv-store).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/0oDfxTMBTU-fmGyowey9hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A84BF92A53F2A41ADA8FB25E63CF4A03385893388BFB239746A5D2076868390A)

**deviceIds** is **networkId** in [DeviceBasicInfo](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo), which can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceIds | string\[\] | Yes | List of **networkId**s of the devices in the same networking environment to be synchronized. |
| query | [Query](#query) | Yes | **Query** object to match. |
| mode | [SyncMode](#syncmode) | Yes | Sync mode. |
| delayMs | number | No | Delay time allowed, in ms. The default value is **0**. If **delayMs** is set, data sync will be executed **delayMs** after **sync()** is called. If **delayMs** is not set, the delay set in [setSyncParam](#setsyncparam) is used. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |

**Example**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_SYNC\_ELEMENT = 'key\_test\_sync';
const VALUE\_TEST\_SYNC\_ELEMENT = 'value-string-001';
// create deviceManager
export default class EntryAbility extends UIAbility {
  onCreate() {
    let context = this.context;
    try {
      let devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
      let deviceIds: string\[\] = \[\];
      if (devManager != null) {
        let devices = devManager.getAvailableDeviceListSync();
        for (let i = 0; i < devices.length; i++) {
          deviceIds\[i\] = devices\[i\].networkId as string;
        }
      }
      try {
        if (kvStore != null) {
          kvStore.on('syncComplete', (data: \[string, number\]\[\]) => {
            console.info('Sync dataChange');
          });
          if (kvStore != null) {
            kvStore.put(KEY\_TEST\_SYNC\_ELEMENT + 'testSync101', VALUE\_TEST\_SYNC\_ELEMENT, (err: BusinessError) => {
              if (err != undefined) {
                console.error(\`Failed to sync.code is ${err.code},message is ${err.message}\`);
                return;
              }
              console.info('Succeeded in putting data');
              const mode = distributedKVStore.SyncMode.PULL\_ONLY;
              const query = new distributedKVStore.Query();
              query.prefixKey("batch\_test");
              query.deviceId(devManager.getLocalDeviceNetworkId());
              if (kvStore != null) {
                kvStore.sync(deviceIds, query, mode, 1000);
              }
            });
          }
        }
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`Failed to sync.code is ${error.code},message is ${error.message}\`);
      }

    } catch (err) {
      let error = err as BusinessError;
      console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
    }
  }
}

#### \[h2\]on('dataChange')

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

Subscribes to data changes of the specified type.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates a data change event. |
| type | [SubscribeType](#subscribetype) | Yes | Type of data change. |
| listener | Callback<[ChangeNotification](#changenotification)\> | Yes | Callback used to return the object to be notified when the data changes. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE\_TYPE\_LOCAL, (data: distributedKVStore.ChangeNotification) => {
    console.info(\`dataChange callback call data: ${data}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]on('syncComplete')

on(event: 'syncComplete', syncCallback: Callback<Array<\[string, number\]>>): void

Subscribes to the cross-device data sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates the sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | Yes | Callback used to return the sync completion event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_FLOAT\_ELEMENT = 'key\_test\_float';
const VALUE\_TEST\_FLOAT\_ELEMENT = 321.12;
try {
  kvStore.on('syncComplete', (data: \[string, number\]\[\]) => {
    console.info(\`syncComplete ${data}\`);
  });
  kvStore.put(KEY\_TEST\_FLOAT\_ELEMENT, VALUE\_TEST\_FLOAT\_ELEMENT).then(() => {
    console.info('succeeded in putting');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to subscribe syncComplete.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]off('dataChange')

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

Unsubscribes from data changes.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **dataChange**, which indicates a data change event. |
| listener | Callback<[ChangeNotification](#changenotification)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for data changes. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class KvstoreModel {
  call(data: distributedKVStore.ChangeNotification) {
    console.info(\`dataChange : ${data}\`);
  }

  subscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to subscribeDataChange.code is ${error.code},message is ${error.message}\`);
    }
  }

  unsubscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.off('dataChange', this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to unsubscribeDataChange.code is ${error.code},message is ${error.message}\`);
    }
  }
}

#### \[h2\]off('syncComplete')

off(event: 'syncComplete', syncCallback?: Callback<Array<\[string, number\]>>): void

Unsubscribes from the cross-device data sync completion events.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **syncComplete**, which indicates a sync completion event. |
| syncCallback | Callback<Array<\[string, number\]>> | No | Callback to unregister. If this parameter is not set, all callbacks used to listen for the data sync completion event are unregistered. When multiple ArkTS instances (obtained through the [getKVStore](#getkvstore) API) of the same database all register the callback used to listen for the sync completion event, if all these callbacks are unregistered by one of the ArkTS instances, then the callbacks of the others are also unregistered. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class KvstoreModel {
  call(data: \[string, number\]\[\]) {
    console.info(\`syncComplete : ${data}\`);
  }

  subscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.on('syncComplete', this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to subscribeDataChange.code is ${error.code},message is ${error.message}\`);
    }
  }

  unsubscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.off('syncComplete', this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(\`Failed to unsubscribeDataChange.code is ${error.code},message is ${error.message}\`);
    }
  }
}

#### \[h2\]getSecurityLevel

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

Obtains the security level of this KV store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SecurityLevel](#securitylevel)\> | Yes | Callback used to return the security level of the KV store. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.getSecurityLevel((err: BusinessError, data: distributedKVStore.SecurityLevel) => {
    if (err != undefined) {
      console.error(\`Failed to get SecurityLevel.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting securityLevel');
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getSecurityLevel

getSecurityLevel(): Promise<SecurityLevel>

Obtains the security level of this KV store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SecurityLevel](#securitylevel)\> | Promise used to return the security level of the KV store. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.getSecurityLevel().then((data: distributedKVStore.SecurityLevel) => {
    console.info('Succeeded in getting securityLevel');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get SecurityLevel.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### DeviceKVStore

Provides APIs for querying data in a device KV store and performing cross-device data sync. This class inherits from **SingleKVStore**. The **SingleKVStore** APIs such as **put** and **putBatch** can be used.

Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of other devices is read-only and cannot be modified.

For example, a device KV store can be used to implement image sharing between devices. The images of other devices can be viewed, but not be modified or deleted.

Before calling any method in **DeviceKVStore**, you must use [getKVStore](#getkvstore) to obtain a **DeviceKVStore** object.

#### \[h2\]get

get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

Obtains the value of the specified key for this device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the value to obtain. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<boolean | string | number | Uint8Array> | Yes | Callback used to return the value obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info("Succeeded in putting");
    if (kvStore != null) {
      kvStore.get(KEY\_TEST\_STRING\_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
        if (err != undefined) {
          console.error(\`Failed to get.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info(\`Succeeded in getting data.data=${data}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]get

get(key: string): Promise<boolean | string | number | Uint8Array>

Obtains the value of the specified key for this device. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key of the value to obtain. It cannot be empty, and the length cannot exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean | string | number | Uint8Array> | Promise used to return the value obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(() => {
    console.info(\`Succeeded in putting data\`);
    if (kvStore != null) {
      kvStore.get(KEY\_TEST\_STRING\_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
        console.info(\`Succeeded in getting data.data=${data}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]get

get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

Obtains a string value that matches the specified device ID and key. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/SUhiNYxBTkaenDTnF8gaNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D5EF18AEB0532B55A768551E48C1A244FC482D778B9F21495DDA13E1B1BF7B8)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| key | string | Yes | Key of the value to obtain. It cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |
| callback | AsyncCallback<boolean|string|number|Uint8Array> | Yes | Callback used to return the value obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-002';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.get('localDeviceId', KEY\_TEST\_STRING\_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
        if (err != undefined) {
          console.error(\`Failed to get.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting');
      });
    }
  })
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]get

get(deviceId: string, key: string): Promise<boolean | string | number | Uint8Array>

Obtains a string value that matches the specified device ID and key. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/c9RZxrkvTQ-8XLeACcxxeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60EB5F8E9EB87E301A4E34D5CDC86F218B7D8F290E6892C9F824B218895DC820)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| key | string | Yes | Key of the value to obtain. It cannot be empty or exceed [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean|string|number|Uint8Array> | Promise used to return the string value that matches the given condition. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string\_2';
const VALUE\_TEST\_STRING\_ELEMENT = 'value-string-002';
try {
  kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT).then(async () => {
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.get('localDeviceId', KEY\_TEST\_STRING\_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
        console.info('Succeeded in getting');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((error: BusinessError) => {
    console.error(\`Failed to put.code is ${error.code},message is ${error.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(keyPrefix: string, callback: AsyncCallback<Entry\[\]>): void

Obtains all KV pairs that match the specified key prefix for this device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch\_test\_string\_key', (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message} \`);
}

#### \[h2\]getEntries

getEntries(keyPrefix: string): Promise<Entry\[\]>

Obtains all KV pairs that match the specified key prefix for this device. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch\_test\_string\_key').then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting Entries');
        console.info(\`PutBatch ${entries}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put Batch.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message} \`);
}

#### \[h2\]getEntries

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry\[\]>): void

Obtains all KV pairs that match the specified device ID and key prefix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/kZ5nf-xgTAexYx_UwQaNJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E86227EE03ECE7225FBB206084FABBB2AA6F9E7DE5E9D8389DE9F783EE96E6EB)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries : ${entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', 'batch\_test\_string\_key', (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to put batch.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(deviceId: string, keyPrefix: string): Promise<Entry\[\]>

Obtains all KV pairs that match the specified device ID and key prefix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/repHA0hZStuNsH3UdztU8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67AC5CC1BCE46A66F2FDDFB64FE74FA91C3C1F34E8601DF01980FB9A8B586D0E)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return all the KV pairs that match the given condition. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', 'batch\_test\_string\_key').then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
        console.info(\`entries\[0\].value: ${entries\[0\].value}\`);
        console.info(\`entries\[0\].value.value: ${entries\[0\].value.value}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to put batch.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(query: Query, callback: AsyncCallback<Entry\[\]>): void

Obtains all KV pairs that match the specified **Query** object for this device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | Key prefix to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified **Query** object on the local device. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array(\[21, 31\]);
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_bool\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE\_ARRAY,
        value: arr
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: {entries}\`);
  kvStore.putBatch(entries, (err: BusinessError) => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getEntries(query, (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get Entries.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(query: Query): Promise<Entry\[\]>

Obtains all KV pairs that match the specified **Query** object for this device. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified **Query** object on the local device. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array(\[21, 31\]);
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_bool\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE\_ARRAY,
        value: arr
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: {entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getEntries(query).then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting Entries');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`)
  });
  console.info('Succeeded in getting Entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get Entries.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry\[\]>): void

Obtains the KV pairs that match the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/rCz_Re6PQoKfdzUkYsTW9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=727FB7AB8AFEF80A8A9688970385EB2BF17BAB99BB80DA137919EA794922BC81)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query) | Yes | **Query** object to match. |
| callback | AsyncCallback<[Entry](#entry)\[\]> | Yes | Callback used to return the KV pairs that match the specified device ID and **Query** object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array(\[21, 31\]);
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_bool\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE\_ARRAY,
        value: arr
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    let query = new distributedKVStore.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', query, (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          console.error(\`Failed to get entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting entries');
        console.info(\`entries.length: ${entries.length}\`);
        console.info(\`entries\[0\]: ${entries\[0\]}\`);
      })
    }
  });
  console.info('Succeeded in getting entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get entries.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getEntries

getEntries(deviceId: string, query: Query): Promise<Entry\[\]>

Obtains the KV pairs that match the specified device ID and **Query** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/JaAyFKYrR0u2kSYh7CEuNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C9B190EC700AD9F5F4728376C3F5276D9EB389289841F2CB7D23278AC0EE153)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Entry](#entry)\[\]> | Promise used to return the KV pairs that match the specified device ID and **Query** object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array(\[21, 31\]);
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_bool\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE\_ARRAY,
        value: arr
      }
    }
    entries.push(entry);
  }
  console.info(\`entries: ${entries}\`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
    let query = new distributedKVStore.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', query).then((entries: distributedKVStore.Entry\[\]) => {
        console.info('Succeeded in getting entries');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get entries.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  console.info('Succeeded in getting entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get entries.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

Obtains a result set with the specified prefix for this device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |
| callback | AsyncCallback<[KVStoreResultSet](#kvstoreresultset)\> | Yes | Callback used to return the result set with the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getResultSet('batch\_test\_string\_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting result set');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
              return;
            }
            console.info('Succeeded in closing result set');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(keyPrefix: string): Promise<KVStoreResultSet>

Obtains a result set with the specified prefix for this device. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVStoreResultSet](#kvstoreresultset)\> | Promise used to return the result set with the specified prefix. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  kvStore.getResultSet('batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

Obtains a **KVStoreResultSet** object that matches the specified device ID and key prefix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/7sT61j8hT4O0yhpSq4vYHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65E4630A3372C6549A4ADE9874B3DDD5A1CBFAA62E4DDFB291C1D19FA6AFB544)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |
| callback | AsyncCallback<[KVStoreResultSet](#kvstoreresultset)\> | Yes | Callback used to return the **KVStoreResultSet** object obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('localDeviceId', 'batch\_test\_string\_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
    if (err != undefined) {
      console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet, (err: BusinessError) => {
        if (err != undefined) {
          console.error(\`Failed to close resultSet.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in closing resultSet');
      })
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSet.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>

Obtains a **KVStoreResultSet** object that matches the specified device ID and key prefix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/RmBp8jEZS4C8iIagBCFSiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EECC0F1F1AFD798C418EE8E97C017BBF57F38A26D0E89287A10F582FAD7933B)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the target device. |
| keyPrefix | string | Yes | Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and all data in the RDB store will be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVStoreResultSet](#kvstoreresultset)\> | Promise used to return the **KVStoreResultSet** object obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('localDeviceId', 'batch\_test\_string\_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing resultSet');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to close resultSet.code is ${err.code},message is ${err.message}\`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSet.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void

Obtains a **KVStoreResultSet** object that matches the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ci1nvQ3FQcGtGF2rEYvVTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F89F8CC0EBA18C5CF170A2DA020C0302D96279A00C4291EDAAD3B035D0C2863D)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device to which the **KVStoreResultSet** object belongs. |
| query | [Query](#query) | Yes | **Query** object to match. |
| callback | AsyncCallback<[KVStoreResultSet](#kvstoreresultset)\> | Yes | Callback used to return the **KVStoreResultSet** object that matches the specified device ID and **Query** object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getResultSet('localDeviceId', query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting resultSet');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(\`Failed to close resultSet.code is ${err.code},message is ${err.message}\`);
              return;
            }
            console.info('Succeeded in closing resultSet');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSet.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>

Obtains a **KVStoreResultSet** object that matches the specified device ID and **Query** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/WHEID9y-Qxabb_Wq_TrIUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED736CEF26C2B5166170763F5CB180399C3C57F4343E2D7C3AAF14D677CEBD55)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device to which the **KVStoreResultSet** object belongs. |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVStoreResultSet](#kvstoreresultset)\> | Promise used to return the **KVStoreResultSet** object that matches the specified device ID and **Query** object. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch\_test");
  if (kvStore != null) {
    kvStore.getResultSet('localDeviceId', query).then((result: distributedKVStore.KVStoreResultSet) => {
      console.info('Succeeded in getting resultSet');
      resultSet = result;
      if (kvStore != null) {
        kvStore.closeResultSet(resultSet).then(() => {
          console.info('Succeeded in closing resultSet');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to close resultSet.code is ${err.code},message is ${err.message}\`);
        });
      }
    }).catch((err: BusinessError) => {
      console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
    });
  }
  query.deviceId('localDeviceId');
  console.info("GetResultSet " + query.getSqlLike());

} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSet.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(query: Query): Promise<KVStoreResultSet>

Obtains a **KVStoreResultSet** object that matches the specified **Query** object for this device. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KVStoreResultSet](#kvstoreresultset)\> | Promise used to return the **KVStoreResultSet** object obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch\_test");
  kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSet

getResultSet(query: Query, callback:AsyncCallback<KVStoreResultSet>): void

Obtains a **KVStoreResultSet** object that matches the specified **Query** object for this device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/DBYzxgVlRCaJ1k_i-B1TAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC3D73B62E75F91E1B8E99163556EC4DAA146BAFABF131CD540B5EAF56F7B230)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |
| callback | AsyncCallback<[KVStoreResultSet](#kvstoreresultset)\> | Yes | Callback used to return the **KVStoreResultSet** object obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(\`Failed to get resultSet.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting resultSet');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(\`Failed to close resultSet.code is ${err.code},message is ${err.message}\`);
              return;
            }
            console.info('Succeeded in closing resultSet');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSet\`);
}

#### \[h2\]getResultSize

getResultSize(query: Query, callback: AsyncCallback<number>): void

Obtains the number of results that match the specified **Query** object for this device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of results obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, (err: BusinessError) => {
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getResultSize(query, (err: BusinessError, resultSize: number) => {
        if (err != undefined) {
          console.error(\`Failed to get result size.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting result set size');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSize

getResultSize(query: Query): Promise<number>

Obtains the number of results that match the specified **Query** object for this device. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.KVStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of results obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch\_test");
  kvStore.getResultSize(query).then((resultSize: number) => {
    console.info('Succeeded in getting result set size');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get result size.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSize

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

Obtains the number of results that match the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/apn1YL04SGa7TaP4t4KIxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F39B8AB7163C71982AC3721B5ED45660E03EB5CFD367C9B9435D9E4E78EE1A44)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device to which the **KVStoreResultSet** object belongs. |
| query | [Query](#query) | Yes | **Query** object to match. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of results obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, (err: BusinessError) => {
    if (err != undefined) {
      console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch\_test");
    if (kvStore != null) {
      kvStore.getResultSize('localDeviceId', query, (err: BusinessError, resultSize: number) => {
        if (err != undefined) {
          console.error(\`Failed to get resultSize.code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('Succeeded in getting resultSize');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSize.code is ${error.code},message is ${error.message}\`);
}

#### \[h2\]getResultSize

getResultSize(deviceId: string, query: Query): Promise<number>

Obtains the number of results that match the specified device ID and **Query** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/9c7Q9VX0SG6Cs6xlQZxl0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7939CEC44A3FCF58F35D98CBBCC4371E5AEC3B006A81CA0CE6674571EC5A87D0)

**deviceId** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

For details about how to obtain **deviceId**, see [sync()](#sync).

**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device to which the **KVStoreResultSet** object belongs. |
| query | [Query](#query) | Yes | **Query** object to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of results obtained. |

**Error codes**

For details about the error codes, see [Distributed KV Store Error Codes](../../error-codes/distributed-kv-store-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry\[\] = \[\];
  for (let i = 0; i < 10; i++) {
    let key = 'batch\_test\_string\_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch\_test\_string\_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to put batch.code is ${err.code},message is ${err.message}\`);
  });
  let query = new distributedKVStore.Query();
  query.prefixKey("batch\_test");
  kvStore.getResultSize('localDeviceId', query).then((resultSize: number) => {
    console.info('Succeeded in getting resultSize');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get resultSize.code is ${err.code},message is ${err.message}\`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(\`Failed to get resultSize.code is ${error.code},message is ${error.message}\`);
}
