# Interface (RdbStore)

Provides APIs for managing data in an RDB store.

Before using the following APIs, you should obtain an **RdbStore** instance by calling the [getRdbStore](../functions/document.md#relationalstoregetrdbstore-1) method and then call the corresponding method through the instance.

In addition, use [execute](#execute12) to initialize the database table structure and related data first, ensuring that the prerequisites for related API calls are met.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/sn0eeAnZQAOIGg8uCfh4BQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=639FBE85F0A9654F5B3052C7F3DEFFA3298F652D9D216218FEF568FBCE27BD3F)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { relationalStore } from '@kit.ArkData';

#### Properties

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| version10+ | number | No | No | 
RDB store version, which is an integer greater than 0.

Reading and setting this property will occupy the database connection. Do not frequently perform operations on this property.

Use a temporary variable to store the value obtained and assign the value to the **version** property of the **RdbStore** instance after the database change is complete. For details, see [Persisting RDB Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-rdb-store#how-to-develop).

 |
| rebuilt12+ | [RebuildType](../enums/document.md#rebuildtype12) | Yes | No | Whether the RDB store has been rebuilt or repaired. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**Example:**

For details about the definition of **this.context** in the sample code, see the application [context](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) of the stage model.

// Set the RDB store version.
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    const SQL\_CREATE\_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT, ASSETDATA ASSET, ASSETSDATA ASSETS, FLOATARRAY floatvector(128))';
    relationalStore.getRdbStore(this.context, STORE\_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      await (store as relationalStore.RdbStore).executeSql(SQL\_CREATE\_TABLE);
      console.info('Get RdbStore successfully.');

      // Set the RDB store version.
      if (store != undefined) {
        (store as relationalStore.RdbStore).version = 3;
        // Obtain the RDB store version.
        console.info(\`RdbStore version is ${store.version}\`);
        // Whether the RDB store has been rebuilt.
        console.info(\`RdbStore rebuilt is ${store.rebuilt}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`Get RdbStore failed, code is ${err.code}, message is ${err.message}\`);
    });
  }
}

#### insert

insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>):void

Inserts a row of data into a table. This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Row of data to insert. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, (err: BusinessError, rowId: number) => {
    if (err) {
      console.error(\`Insert is failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`Insert is successful, rowId = ${rowId}\`);
  });
}

#### insert10+

insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>):void

Inserts a row of data into a table. You can use the **conflict** parameter to specify [ConflictResolution](../enums/document.md#conflictresolution10). This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Row of data to insert. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | Yes | Resolution used to resolve the conflict. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE,
    (err: BusinessError, rowId: number) => {
      if (err) {
        console.error(\`Insert is failed, code is ${err.code},message is ${err.message}\`);
        return;
      }
      console.info(\`Insert is successful, rowId = ${rowId}\`);
    });
}

#### insert

insert(table: string, values: ValuesBucket):Promise<number>

Inserts a row of data into a table. This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Row of data to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1).then((rowId: number) => {
    console.info(\`Insert is successful, rowId = ${rowId}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Insert is failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### insert10+

insert(table: string, values: ValuesBucket, conflict: ConflictResolution):Promise<number>

Inserts a row of data into a table. You can use the **conflict** parameter to specify [ConflictResolution](../enums/document.md#conflictresolution10). This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Row of data to insert. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | Yes | Resolution used to resolve the conflict. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE).then((rowId: number) => {
    console.info(\`Insert is successful, rowId = ${rowId}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Insert is failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### insertSync12+

insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution):number

Inserts a row of data into a table. This API returns the result synchronously. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Row of data to insert. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | No | 
Resolution used to resolve the conflict.

Default value: **relationalStore.ConflictResolution.ON\_CONFLICT\_NONE**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  try {
    let rowId: number = (store as relationalStore.RdbStore).insertSync("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE);
    console.info(\`Insert is successful, rowId = ${rowId}\`);
  } catch (error) {
    console.error(\`Insert is failed, code is ${error.code},message is ${error.message}\`);
  }
}

#### insertSync12+

insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution):number

Inserts a row of Sendable data into a table. This API returns the result synchronously. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [sendableRelationalStore.ValuesBucket](../../ohos-data-sendablerelationalstore-shared-rdb-store/document.md#valuesbucket) | Yes | Sendable data to insert. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | No | 
Resolution used to resolve the conflict.

Default value: **relationalStore.ConflictResolution.ON\_CONFLICT\_NONE**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { sendableRelationalStore } from '@kit.ArkData';

const valuesBucket: relationalStore.ValuesBucket = {
  "NAME": 'hangman',
  "AGE": 18,
  "SALARY": 100.5,
  "CODES": new Uint8Array(\[1, 2, 3\])
};
const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);

if (store != undefined) {
  try {
    let rowId: number = (store as relationalStore.RdbStore).insertSync("EMPLOYEE", sendableValuesBucket, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE);
    console.info(\`Insert is successful, rowId = ${rowId}\`);
  } catch (error) {
    console.error(\`Insert is failed, code is ${error.code},message is ${error.message}\`);
  }
}

#### batchInsert

batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>):void

Inserts data into a table in batches. This API uses an asynchronous callback to return the result.

The data insertion fails if the API returns an error, or if it returns \*\* -1\*\* without throwing an error.

[Vector store](../interfaces-others/document.md#storeconfig) is supported since API version 20.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](../types/document.md#valuesbucket)\> | Yes | An array of data to insert. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array(\[6, 7, 8, 9, 10\]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array(\[11, 12, 13, 14, 15\]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  (store as relationalStore.RdbStore).batchInsert("EMPLOYEE", valueBuckets, (err, insertNum) => {
    if (err || insertNum == -1) {
      console.error(\`batchInsert is failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`batchInsert is successful, the number of values that were inserted = ${insertNum}\`);
  })
}

#### batchInsert

batchInsert(table: string, values: Array<ValuesBucket>):Promise<number>

Inserts data into a table in batches. This API uses a promise to return the result.

The data insertion fails if the API returns an error, or if it returns **\-1** without throwing an error.

[Vector store](../interfaces-others/document.md#storeconfig) is supported since API version 20.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](../types/document.md#valuesbucket)\> | Yes | An array of data to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

RDB store:

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array(\[6, 7, 8, 9, 10\]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array(\[11, 12, 13, 14, 15\]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  (store as relationalStore.RdbStore).batchInsert("EMPLOYEE", valueBuckets).then((insertNum: number) => {
    if (insertNum == -1) {
      console.error(\`batchInsert is failed\`);
      return;
    }
    console.info(\`batchInsert is successful, the number of values that were inserted = ${insertNum}\`);
  }).catch((err: BusinessError) => {
    console.error(\`batchInsert is failed, code is ${err.code},message is ${err.message}\`);
  })
}

Vector store:

let createSql = "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 floatvector(2));";
await store!.execute(createSql, 0, undefined);  // Create a relational table. The second parameter 0 indicates that explicit transactions are not enabled, and the third parameter undefined indicates that the SQL statement does not use parameter binding.
let floatVector = Float32Array.from(\[1.2, 2.3\]);
let valueBucketArray = new Array<relationalStore.ValuesBucket>();
for (let i = 0; i < 100; i++) { // Construct a BucketArray for writing.
  const row : relationalStore.ValuesBucket = {
    "id" : i,
    "data1" : floatVector,
  }
  valueBucketArray.push(row);
}
await store!.batchInsert("test", valueBucketArray); // Execute batched writes.

#### batchInsertSync12+

batchInsertSync(table: string, values: Array<ValuesBucket>):number

Inserts data into a table with conflict resolutions in batches. This API returns the result synchronously.

The data insertion fails if the API returns an error, or if it returns **\-1** without throwing an error.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](../types/document.md#valuesbucket)\> | Yes | An array of data to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array(\[6, 7, 8, 9, 10\]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array(\[11, 12, 13, 14, 15\]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  try {
    let insertNum: number = (store as relationalStore.RdbStore).batchInsertSync("EMPLOYEE", valueBuckets);
    if (insertNum == -1) {
      console.error(\`batchInsertSync is failed\`);
      return;
    }
    console.info(\`batchInsert is successful, the number of values that were inserted = ${insertNum}\`);
  } catch (err) {
    console.error(\`batchInsert is failed, code is ${err.code},message is ${err.message}\`);
  }
}

#### batchInsertWithConflictResolution18+

batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>

Inserts data into a table in batches. You can use the **conflict** parameter to specify [ConflictResolution](../enums/document.md#conflictresolution10). This API uses a promise to return the result.

A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit, the error code 14800000 is returned. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters.

For example, if the size of the union is 10, a maximum of 3276 data records can be inserted (3276 × 10 = 32760).

Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](../types/document.md#valuesbucket)\> | Yes | An array of data to insert. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | Yes | Resolution used to resolve the conflict. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array(\[6, 7, 8, 9, 10\]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array(\[11, 12, 13, 14, 15\]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  (store as relationalStore.RdbStore).batchInsertWithConflictResolution("EMPLOYEE", valueBuckets, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE).then((insertNum: number) => {
    console.info(\`batchInsert is successful, insertNum = ${insertNum}\`);
  }).catch((err: BusinessError) => {
    console.error(\`batchInsert is failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### batchInsertWithConflictResolutionSync18+

batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number

Inserts data into a table in batches. You can use the **conflict** parameter to specify [ConflictResolution](../enums/document.md#conflictresolution10).

A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit, the error code 14800000 is returned. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters.

For example, if the size of the union is 10, a maximum of 3276 data records can be inserted (3276 × 10 = 32760).

Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](../types/document.md#valuesbucket)\> | Yes | An array of data to insert. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | Yes | Resolution used to resolve the conflict. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array(\[6, 7, 8, 9, 10\]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array(\[11, 12, 13, 14, 15\]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  try {
    let insertNum: number = (store as relationalStore.RdbStore).batchInsertWithConflictResolutionSync("EMPLOYEE", valueBuckets, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE);
    console.info(\`batchInsert is successful, the number of values that were inserted = ${insertNum}\`);
  } catch (err) {
    console.error(\`batchInsert is failed, code is ${err.code},message is ${err.message}\`);
  }
}

#### update

update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>):void

Updates data in the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Update conditions specified by the **RdbPredicates** object. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of rows updated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates, (err, rows) => {
    if (err) {
      console.error(\`Updated failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`Updated row count: ${rows}\`);
  });
}

#### update10+

update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution, callback: AsyncCallback<number>):void

Updates data based on the specified **RdbPredicates** object. You can use the **conflict** parameter to specify [ConflictResolution](../enums/document.md#conflictresolution10). This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Update conditions specified by the **RdbPredicates** object. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | Yes | Resolution used to resolve the conflict. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of rows updated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE, (err, rows) => {
    if (err) {
      console.error(\`Updated failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`Updated row count: ${rows}\`);
  });
}

#### update

update(values: ValuesBucket, predicates: RdbPredicates):Promise<number>

Updates data based on the specified **RdbPredicates** object. This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Update conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of rows updated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates).then(async (rows: number) => {
    console.info(\`Updated row count: ${rows}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Updated failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### update10+

update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution):Promise<number>

Updates data based on the specified **RdbPredicates** object. You can use the **conflict** parameter to specify [ConflictResolution](../enums/document.md#conflictresolution10). This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Update conditions specified by the **RdbPredicates** object. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | Yes | Resolution used to resolve the conflict. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of rows updated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE).then(async (rows: number) => {
    console.info(\`Updated row count: ${rows}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Updated failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### updateSync12+

updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution):number

Updates data in the RDB store based on the specified **RdbPredicates** object. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained through the [query](#query) or [querySql](#querysql) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Update conditions specified by the **RdbPredicates** object. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | No | 
Resolution used to resolve the conflict.

Default value: **relationalStore.ConflictResolution.ON\_CONFLICT\_NONE**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of rows updated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

// You can use either of the following:
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  try {
    let rows: number = (store as relationalStore.RdbStore).updateSync(valueBucket1, predicates, relationalStore.ConflictResolution.ON\_CONFLICT\_REPLACE);
    console.info(\`Updated row count: ${rows}\`);
  } catch (error) {
    console.error(\`Updated failed, code is ${error.code},message is ${error.message}\`);
  }
}

#### delete

delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Deletion conditions specified by the **RdbPredicates** object. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of rows deleted. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).delete(predicates, (err, rows) => {
    if (err) {
      console.error(\`Delete failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`Delete rows: ${rows}\`);
  });
}

#### delete

delete(predicates: RdbPredicates):Promise<number>

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Deletion conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of rows deleted. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).delete(predicates).then((rows: number) => {
    console.info(\`Delete rows: ${rows}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Delete failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### deleteSync12+

deleteSync(predicates: RdbPredicates):number

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API returns the result synchronously.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Deletion conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of rows deleted. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  try {
    let rows: number = (store as relationalStore.RdbStore).deleteSync(predicates);
    console.info(\`Delete rows: ${rows}\`);
  } catch (err) {
    console.error(\`Delete failed, code is ${err.code},message is ${err.message}\`);
  }
}

#### query10+

query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>):void

Queries data from the RDB store based on specified conditions. This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| callback | AsyncCallback<[ResultSet](../interface-resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).query(predicates, async (err, resultSet) => {
    if (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  });
}

#### query

query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void

Queries data from the RDB store based on specified conditions (for example, column). This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | Yes | Columns to query. If this parameter is not specified, the query applies to all columns. |
| callback | AsyncCallback<[ResultSet](../interface-resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).query(predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\], async (err, resultSet) => {
    if (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  });
}

#### query

query(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

Queries data from the RDB store based on specified conditions. This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained. As a result, the operation may fail or an exception may be thrown.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | No | Columns to query. If this parameter is not specified, the query applies to all columns. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResultSet](../interface-resultset/document.md)\> | Promise used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).query(predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### querySync12+

querySync(predicates: RdbPredicates, columns?: Array<string>):ResultSet

Queries data in a database based on specified conditions. This API returns the result synchronously. If complex logic and a large number of loops are involved in the operations on the **resultSet** obtained by **querySync**, the freeze problem may occur. You are advised to perform this operation in the [taskpool](../../../../arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md) thread.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | No | Columns to query. If this parameter is not specified, the query applies to all columns. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ResultSet](../interface-resultset/document.md) | If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  let resultSet: relationalStore.ResultSet | undefined;
  try {
    resultSet = store.querySync(predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\]);
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    while (resultSet.goToNextRow()) {
      const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
      const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
      const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
      const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
      console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
    }
  } catch (err) {
    console.error(\`Query failed, code is ${err.code}, message is ${err.message}\`);
  } finally {
    // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
    if (resultSet) {
      resultSet.close();
    }
  }
}

#### remoteQuery

remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string> , callback: AsyncCallback<ResultSet>): void

Queries data from the RDB store of a remote device based on specified conditions. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/dpMlKjZYSjihO0_S-J6lJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0206B1CE5801BDCAAF16214A8B8DF81DB9E63F853837FFA34848B0E9BBFB7E29)

**device** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | ID of the remote device. |
| table | string | Yes | Name of the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | Yes | Columns to query. If this parameter is not specified, the query applies to all columns. |
| callback | AsyncCallback<[ResultSet](../interface-resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices = dmInstance.getAvailableDeviceListSync();
  if (devices != undefined) {
    deviceId = devices\[0\].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.greaterThan("id", 0);
if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).remoteQuery(deviceId, "EMPLOYEE", predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to remoteQuery, code is ${err.code},message is ${err.message}\`);
  });
}

#### remoteQuery

remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>

Queries data from the RDB store of a remote device based on specified conditions. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/tGdx7jZaQgKMMH_xtdg5CA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A060843E5B5A78609714AD09D7A0E493D9B267E4B128D8550BBB58E01BA8772)

**device** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | ID of the remote device. |
| table | string | Yes | Name of the target table. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | Yes | Columns to query. If this parameter is not specified, the query applies to all columns. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResultSet](../interface-resultset/document.md)\> | Promise used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  if (devices != undefined) {
    deviceId = devices\[0\].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.greaterThan("id", 0);
if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).remoteQuery(deviceId, "EMPLOYEE", predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to remoteQuery, code is ${err.code},message is ${err.message}\`);
  });
}

#### querySql10+

querySql(sql: string, callback: AsyncCallback<ResultSet>):void

Queries data in the RDB store using the specified SQL statement. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1000. This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained. As a result, the operation may fail or an exception may be thrown.

[Vector store](../interfaces-others/document.md#storeconfig) is supported. For details about the supported syntax, see [Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-vector-store#specifications).

Aggregate functions cannot be nested.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| callback | AsyncCallback<[ResultSet](../interface-resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

RDB store:

if (store != undefined) {
  (store as relationalStore.RdbStore).querySql("SELECT \* FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'", async (err, resultSet) => {
    if (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  });
}

Vector store:

// <-> means to calculate vector similarity, and <=> means to calculate the cosine distance.
const querySql = "select id, repr <-> '\[1.5,5.6\]' as distance from test ORDER BY repr <-> '\[1.5,5.6\]' limit 10 offset 1;";
let resultSet = await store.querySql(querySql);

// Aggregate query. GROUP BY supports multiple columns.
const querySql1 = "select id, repr from test group by id, repr having max(repr<=>'\[1.5,5.6\]');";
let resultSet1 = await store.querySql(querySql1);

// Subquery. A maximum of 32 nested layers are supported.
const querySql2 = "select \* from test where id in (select id from test1)";
let resultSet2 = await store.querySql(querySql2);

#### querySql

querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>):void

Queries data using the specified SQL statements. The number of relational operators in the SQL statements cannot exceed 1000. The parameter values in the SQL statement can be passed in. This API uses an asynchronous callback to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained. As a result, the operation may fail or an exception may be thrown.

[Vector store](../interfaces-others/document.md#storeconfig) is supported. For details about the supported syntax, see [Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-vector-store#specifications).

Aggregate functions cannot be nested.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](../types/document.md#valuetype)\> | Yes | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, the value of this parameter must be an empty array. |
| callback | AsyncCallback<[ResultSet](../interface-resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).querySql("SELECT \* FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = ?", \['sanguo'\], async (err, resultSet) => {
    if (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  });
}

#### querySql

querySql(sql: string, bindArgs?: Array<ValueType>):Promise<ResultSet>

Queries data in the RDB store using the specified SQL statement. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1000. This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](../interface-resultset/document.md#getvalue12) and [getString](../interface-resultset/document.md#getstring) after **ResultSet** is obtained. As a result, the operation may fail or an exception may be thrown.

[Vector store](../interfaces-others/document.md#storeconfig) is supported. For details about the supported syntax, see [Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-vector-store#specifications).

Aggregate functions cannot be nested.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](../types/document.md#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResultSet](../interface-resultset/document.md)\> | Promise used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

RDB store:

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).querySql("SELECT \* FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'").then(async (resultSet: relationalStore.ResultSet) => {
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
  });
}

Vector store:

// Query the top 10 records with ID of 1 and the similarity to \[1.5, 2.5\] is less than 0.5, and sort them in ascending order by similarity.
const querySql = "select id, repr <-> ? as distance from test where id = ? and repr <-> ? < 0.5 ORDER BY repr <-> ? limit 10;";
const vectorValue: Float32Array = new Float32Array(\[1.5, 2.5\]);
let resultSet = await store.querySql(querySql, \[vectorValue, 1, vectorValue, vectorValue\]);

#### querySqlSync12+

querySqlSync(sql: string, bindArgs?: Array<ValueType>):ResultSet

Queries data in the RDB store using the specified SQL statement. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1000. If complex logic and a large number of loops are involved in the operations on the **resultSet** obtained by **querySqlSync**, the freeze problem may occur. You are advised to perform this operation in the [taskpool](../../../../arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md) thread.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](../types/document.md#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ResultSet](../interface-resultset/document.md) | If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |

**Example:**

if (store != undefined) {
  let resultSet: relationalStore.ResultSet | undefined;
  try {
    resultSet = store.querySqlSync("SELECT \* FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    while (resultSet.goToNextRow()) {
      const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
      const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
      const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
      const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
      console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
    }
  } catch (err) {
    console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
  } finally {
    // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
    if (resultSet) {
      resultSet.close();
    }
  }
}

#### executeSql10+

executeSql(sql: string, callback: AsyncCallback<void>):void

Executes an SQL statement. The number of relational operators between expressions and operators in the statement cannot exceed 1000. This API uses an asynchronous callback to return the result.

This API does not support query, attach, or transaction operations. To perform these operations, use [querySql](#querysql10), [query](#query10), [attach](#attach12), [beginTransaction](#begintransaction), and [commit](#commit).

Statements separated by semicolons (;) are not supported.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

const SQL\_DELETE\_TABLE = "DELETE FROM test WHERE name = 'zhangsan'";
if (store != undefined) {
  (store as relationalStore.RdbStore).executeSql(SQL\_DELETE\_TABLE, (err) => {
    if (err) {
      console.error(\`ExecuteSql failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Delete table done.');
  });
}

#### executeSql

executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>):void

Executes an SQL statement. The parameter values in the SQL statement can be passed in. The number of relational operators in the SQL statements cannot exceed 1000. This API uses an asynchronous callback to return the result.

This API does not support query, attach, or transaction operations. To perform these operations, use [querySql](#querysql10), [query](#query10), [attach](#attach12), [beginTransaction](#begintransaction), and [commit](#commit).

Statements separated by semicolons (;) are not supported.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](../types/document.md#valuetype)\> | Yes | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, the value of this parameter must be an empty array. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

const SQL\_DELETE\_TABLE = "DELETE FROM test WHERE name = ?";
if (store != undefined) {
  (store as relationalStore.RdbStore).executeSql(SQL\_DELETE\_TABLE, \['zhangsan'\], (err) => {
    if (err) {
      console.error(\`ExecuteSql failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Delete table done.');
  });
}

#### executeSql

executeSql(sql: string, bindArgs?: Array<ValueType>):Promise<void>

Executes an SQL statement. The number of relational operators between expressions and operators in the statement cannot exceed 1000. This API uses a promise to return the result.

This API does not support query, attach, or transaction operations. To perform these operations, use [querySql](#querysql10), [query](#query10), [attach](#attach12), [beginTransaction](#begintransaction), and [commit](#commit).

Statements separated by semicolons (;) are not supported.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](../types/document.md#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

const SQL\_DELETE\_TABLE = "DELETE FROM test WHERE name = 'zhangsan'";
if (store != undefined) {
  (store as relationalStore.RdbStore).executeSql(SQL\_DELETE\_TABLE).then(() => {
    console.info('Delete table done.');
  }).catch((err: BusinessError) => {
    console.error(\`ExecuteSql failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### execute12+

execute(sql: string, args?: Array<ValueType>):Promise<ValueType>

Executes an SQL statement that contains specified arguments. The number of relational operators between expressions and operators in the statement cannot exceed 1000. This API uses a promise to return a value of the ValueType type.

This API can be used to add, delete, and modify data, run SQL statements of the PRAGMA syntax, and create, delete, and modify a table. The type of the return value varies, depending on the execution result.

This API does not support query, attach, or transaction operations. To perform these operations, use [querySql](#querysql10), [query](#query10), [attach](#attach12), [beginTransaction](#begintransaction), and [commit](#commit).

When this API is used to insert data originating from a subquery to a vector store, full-field insertion is supported, but partial-field insertion is not yet supported.

Statements separated by semicolons (;) are not supported.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| args | Array<[ValueType](../types/document.md#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ValueType](../types/document.md#valuetype)\> | Promise used to return the SQL execution result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

RDB store:

import { BusinessError } from '@kit.BasicServicesKit';

// Check the RDB store integrity.
if (store != undefined) {
  const SQL\_CHECK\_INTEGRITY = 'PRAGMA integrity\_check';
  (store as relationalStore.RdbStore).execute(SQL\_CHECK\_INTEGRITY).then((data) => {
    console.info(\`check result: ${data}\`);
  }).catch((err: BusinessError) => {
    console.error(\`check failed, code is ${err.code}, message is ${err.message}\`);
  });
}

// Delete all data from the table.
if (store != undefined) {
  const SQL\_DELETE\_TABLE = 'DELETE FROM test';
  (store as relationalStore.RdbStore).execute(SQL\_DELETE\_TABLE).then((data) => {
    console.info(\`delete result: ${data}\`);
  }).catch((err: BusinessError) => {
    console.error(\`delete failed, code is ${err.code}, message is ${err.message}\`);
  });
}

// Delete a table.
if (store != undefined) {
  const SQL\_DROP\_TABLE = 'DROP TABLE test';
  (store as relationalStore.RdbStore).execute(SQL\_DROP\_TABLE).then((data) => {
    console.info(\`drop result: ${data}\`);
  }).catch((err: BusinessError) => {
    console.error(\`drop failed, code is ${err.code}, message is ${err.message}\`);
  });
}

Vector store:

// FLOATVECTOR(2) is a vector property with a dimension of 2. The subsequent repr operation should be performed based on this dimension.
let createSql = "CREATE TABLE test (ID INTEGER PRIMARY KEY,REPR FLOATVECTOR(2));";
// Create a table.
await store!.execute(createSql);
// Insert data with parameter binding.
let insertSql = "insert into test VALUES(?, ?);";
const vectorValue: Float32Array = Float32Array.from(\[1.5, 6.6\]);
await store!.execute(insertSql, \[0, vectorValue\]);
// Execute without using bound parameters.
await store!.execute("insert into test values(1, '\[3.5, 1.8\]');");

#### execute12+

execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>

Executes an SQL statement that contains specified arguments. The number of relational operators between expressions and operators in the statement cannot exceed 1000. This API uses a promise to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig). When this API is used to insert data originating from a subquery, full-field insertion is supported, but partial-field insertion is not yet supported.

This API does not support data query. To query data, use [querySql](#querysql10).

Statements separated by semicolons (;) are not supported.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| txId | number | Yes | Transaction ID obtained via [beginTrans](#begintrans12). If the value is **0**, the SQL statement is executed in a separate transaction by default. |
| args | Array<[ValueType](../types/document.md#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If this parameter is left blank or set to **null** or **undefined**, the SQL parameter statement is considered complete. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ValueType](../types/document.md#valuetype)\> | Promise that returns **null**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, \["18", "20"\])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(\`execute sql failed, code is ${err.code},message is ${err.message}\`);
      });
  });
}

#### executeSync12+

executeSync(sql: string, args?: Array<ValueType>): ValueType

Executes an SQL statement that contains specified arguments. The number of relational operators between expressions and operators in the statement cannot exceed 1000. This API returns a value of theValueType type.

This API can be used to add, delete, and modify data, run SQL statements of the PRAGMA syntax, and create, delete, and modify a table. The type of the return value varies, depending on the execution result.

This API does not support query, attach, or transaction operations. To perform these operations, use [querySql](#querysql10), [query](#query10), [attach](#attach12), [beginTransaction](#begintransaction), and [commit](#commit).

Statements separated by semicolons (;) are not supported.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| args | Array<[ValueType](../types/document.md#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If this parameter is left blank or set to **null** or **undefined**, the SQL statement is complete. The default value is null. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ValueType](../types/document.md#valuetype) | SQL execution result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

// Check the RDB store integrity.
if (store != undefined) {
  const SQL\_CHECK\_INTEGRITY = 'PRAGMA integrity\_check';
  try {
    let data = (store as relationalStore.RdbStore).executeSync(SQL\_CHECK\_INTEGRITY);
    console.info(\`check result: ${data}\`);
  } catch (err) {
    console.error(\`check failed, code is ${err.code}, message is ${err.message}\`);
  }
}

// Delete all data from the table.
if (store != undefined) {
  const SQL\_DELETE\_TABLE = 'DELETE FROM test';
  try {
    let data = (store as relationalStore.RdbStore).executeSync(SQL\_DELETE\_TABLE);
    console.info(\`delete result: ${data}\`);
  } catch (err) {
    console.error(\`delete failed, code is ${err.code}, message is ${err.message}\`);
  }
}

// Delete a table.
if (store != undefined) {
  const SQL\_DROP\_TABLE = 'DROP TABLE test';
  try {
    let data = (store as relationalStore.RdbStore).executeSync(SQL\_DROP\_TABLE);
    console.info(\`drop result: ${data}\`);
  } catch (err) {
    console.error(\`drop failed, code is ${err.code}, message is ${err.message}\`);
  }
}

#### getModifyTime10+

getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType\[\], callback: AsyncCallback<ModifyTime>): void

Obtains the last modification time of the data in a table. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the database table to query. |
| columnName | string | Yes | Pointer to the column name of the database table to query. |
| primaryKeys | [PRIKeyType](../types/document.md#prikeytype10)\[\] | Yes | 
Pointer to the primary keys of the rows to query.

If the database table has no primary key, **rowid** must be passed in through **columnName**. In this case, **primaryKeys** specifies the row numbers of the database table to query.

If the database table has no primary key and no **rowid** is passed in through **columnName**, an error code will be returned.

 |
| callback | AsyncCallback<[ModifyTime](../types/document.md#modifytime10)\> | Yes | Callback used to return the result. If the operation is successful, the **ModifyTime** object is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 3 - 4 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

let PRIKey = \[1, 4, 2, 3\];
if (store != undefined) {
  (store as relationalStore.RdbStore).getModifyTime("EMPLOYEE", "NAME", PRIKey, (err, modifyTime: relationalStore.ModifyTime) => {
    if (err) {
      console.error(\`getModifyTime failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    let size = modifyTime.size;
  });
}

#### getModifyTime10+

getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType\[\]): Promise<ModifyTime>

Obtains the last modification time of the data in a table. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the database table to query. |
| columnName | string | Yes | Pointer to the column name of the database table to query. |
| primaryKeys | [PRIKeyType](../types/document.md#prikeytype10)\[\] | Yes | 
Pointer to the primary keys of the rows to query.

If the database table has no primary key, **rowid** must be passed in through **columnName**. In this case, **primaryKeys** specifies the row numbers of the database table to query.

If the database table has no primary key and no **rowid** is passed in through **columnName**, an error code will be returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ModifyTime](../types/document.md#modifytime10)\> | Promise used to return the **ModifyTime** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 3 - 4 parameter(s)! 2. The RdbStore must be not nullptr.3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let PRIKey = \[1, 2, 3\];
if (store != undefined) {
  (store as relationalStore.RdbStore).getModifyTime("EMPLOYEE", "NAME", PRIKey)
    .then((modifyTime: relationalStore.ModifyTime) => {
      let size = modifyTime.size;
    })
    .catch((err: BusinessError) => {
      console.error(\`getModifyTime failed, code is ${err.code},message is ${err.message}\`);
    });
}

#### beginTransaction

beginTransaction():void

Begins a transaction before executing the SQL statements.

This API does not allow nested transactions and cannot be used across processes or threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

if (store != undefined) {
  (store as relationalStore.RdbStore).beginTransaction();
  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  (store as relationalStore.RdbStore).insert("test", valueBucket);
  (store as relationalStore.RdbStore).commit();
}

#### beginTrans12+

beginTrans(): Promise<number>

Begins a transaction before executing the SQL statement. This API uses a promise to return the result.

Different from [beginTransaction](#begintransaction), this API returns a transaction ID. [execute](#execute12-1) can specify the transaction ID to isolate different transactions.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the transaction ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, \["18", "20"\])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(\`execute sql failed, code is ${err.code},message is ${err.message}\`);
      });
  });
}

#### createTransaction14+

createTransaction(options?: TransactionOptions): Promise<Transaction>

Creates a transaction object and starts a transaction. This API uses a promise to return the result.

Different from [beginTransaction](#begintransaction), **createTransaction()** returns a transaction object, which is isolated from other transaction objects. When a transaction object is used to insert, delete, or update data, these changes cannot be detected by [on('dataChange')](#ondatachange).

A store supports a maximum of four transaction objects at a time. If the number of transaction objects exceeds the upper limit, error 14800015 is returned. In this case, check whether transaction objects are being held too long or whether there are too many concurrent transactions. If the problem cannot be solved through these optimizations, you are advised to create transaction objects after existing transactions are released.

You are advised to use **createTransaction** instead of **beginTransaction**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TransactionOptions](../interfaces-others/document.md#transactionoptions14) | No | Configuration of the transaction object to create. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Transaction](../interface-transaction/document.md)\> | Promise used to return the transaction object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database is busy. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).createTransaction().then(async (transaction: relationalStore.Transaction) => {
    transaction.execute("DELETE FROM test WHERE age = ? OR age = ?", \[21, 20\]).then(() => {
      transaction.commit();
    }).catch((e: BusinessError) => {
      transaction.rollback();
      console.error(\`execute sql failed, code is ${e.code},message is ${e.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`createTransaction failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### commit

commit():void

Commits this executed SQL statement. This API must be used with [beginTransaction](#begintransaction).

This API does not allow nested transactions and cannot be used across processes or threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

if (store != undefined) {
  (store as relationalStore.RdbStore).beginTransaction();
  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  (store as relationalStore.RdbStore).insert("test", valueBucket);
  (store as relationalStore.RdbStore).commit();
}

#### commit12+

commit(txId : number):Promise<void>

Commits an executed SQL statement. This API is used together with [beginTrans](#begintrans12) and uses a promise to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| txId | number | Yes | Transaction ID obtained via [beginTrans](#begintrans12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, \["18", "20"\])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(\`execute sql failed, code is ${err.code},message is ${err.message}\`);
      });
  });
}

#### rollBack

rollBack():void

Rolls back the SQL statements that have been executed.

This API does not allow nested transactions and cannot be used across processes or threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

if (store != undefined) {
  try {
    (store as relationalStore.RdbStore).beginTransaction();
    const valueBucket: relationalStore.ValuesBucket = {
      'NAME': value1,
      'AGE': value2,
      'SALARY': value3,
      'CODES': value4
    };
    (store as relationalStore.RdbStore).insert("test", valueBucket);
    (store as relationalStore.RdbStore).commit();
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(\`Transaction failed, code is ${code},message is ${message}\`);
    (store as relationalStore.RdbStore).rollBack();
  }
}

#### rollback12+

rollback(txId : number):Promise<void>

Rolls back an executed SQL statement. This API is used together with [beginTrans](#begintrans12) and uses a promise to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| txId | number | Yes | Transaction ID obtained via [beginTrans](#begintrans12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, \["18", "20"\])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(\`execute sql failed, code is ${err.code},message is ${err.message}\`);
      });
  });
}

#### backup

backup(destName:string, callback: AsyncCallback<void>):void

Backs up an RDB store. This API uses an asynchronous callback to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| destName | string | Yes | Name of the RDB store backup file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).backup("dbBackup.db", (err) => {
    if (err) {
      console.error(\`Backup failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Backup success.');
  });
}

#### backup

backup(destName:string): Promise<void>

Backs up an RDB store. This API uses a promise to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| destName | string | Yes | Name of the RDB store backup file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  let promiseBackup = (store as relationalStore.RdbStore).backup("dbBackup.db");
  promiseBackup.then(() => {
    console.info('Backup success.');
  }).catch((err: BusinessError) => {
    console.error(\`Backup failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### restore

restore(srcName:string, callback: AsyncCallback<void>):void

Restores an RDB store from a backup file. This API uses an asynchronous callback to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcName | string | Yes | Name of the RDB store backup file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).restore("dbBackup.db", (err) => {
    if (err) {
      console.error(\`Restore failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Restore success.');
  });
}

#### restore

restore(srcName:string): Promise<void>

Restores an RDB store from a backup file. This API uses a promise to return the result.

This API is available only to [vector stores](../interfaces-others/document.md#storeconfig).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcName | string | Yes | Name of the RDB store backup file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  let promiseRestore = (store as relationalStore.RdbStore).restore("dbBackup.db");
  promiseRestore.then(() => {
    console.info('Restore success.');
  }).catch((err: BusinessError) => {
    console.error(\`Restore failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### setDistributedTables

setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void

Sets distributed tables. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tables | Array<string> | Yes | Names of the distributed tables to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(\["EMPLOYEE"\], (err) => {
    if (err) {
      console.error(\`SetDistributedTables failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('SetDistributedTables successfully.');
  });
}

#### setDistributedTables

setDistributedTables(tables: Array<string>): Promise<void>

Sets distributed tables. This API uses a promise to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tables | Array<string> | Yes | Names of the distributed tables to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(\["EMPLOYEE"\]).then(() => {
    console.info('SetDistributedTables successfully.');
  }).catch((err: BusinessError) => {
    console.error(\`SetDistributedTables failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### setDistributedTables10+

setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void

Sets distributed tables. The distributed type of the table can be specified. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tables | Array<string> | Yes | Names of the distributed tables to set. |
| type | [DistributedType](../enums/document.md#distributedtype10) | Yes | Distributed type of the tables. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800051 | The type of the distributed table does not match. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(\["EMPLOYEE"\], relationalStore.DistributedType.DISTRIBUTED\_CLOUD, (err) => {
    if (err) {
      console.error(\`SetDistributedTables failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('SetDistributedTables successfully.');
  });
}

#### setDistributedTables10+

setDistributedTables(tables: Array<string>, type: DistributedType, config: DistributedConfig, callback: AsyncCallback<void>): void

Sets distributed tables. The distributed type and configuration of the table can be specified. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tables | Array<string> | Yes | Names of the distributed tables to set. |
| type | [DistributedType](../enums/document.md#distributedtype10) | Yes | Distributed type of the tables. |
| config | [DistributedConfig](../interfaces-others/document.md#distributedconfig10) | Yes | Configuration of the distributed mode. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800051 | The type of the distributed table does not match. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(\["EMPLOYEE"\], relationalStore.DistributedType.DISTRIBUTED\_CLOUD, {
    autoSync: true
  }, (err) => {
    if (err) {
      console.error(\`SetDistributedTables failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('SetDistributedTables successfully.');
  });
}

#### setDistributedTables10+

setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>

Sets distributed tables. The distributed type and configuration of the table can be specified. This API uses a promise to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tables | Array<string> | Yes | Names of the distributed tables to set. |
| type | [DistributedType](../enums/document.md#distributedtype10) | No | 
Distributed type of the tables.

Default value: **relationalStore.DistributedType.DISTRIBUTED\_DEVICE**.

 |
| config | [DistributedConfig](../interfaces-others/document.md#distributedconfig10) | No | Configuration of the distributed mode. If this parameter is not specified, the value of **autoSync** is **false** by default, which means only manual sync is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800051 | The type of the distributed table does not match. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(\["EMPLOYEE"\], relationalStore.DistributedType.DISTRIBUTED\_CLOUD, {
    autoSync: true
  }).then(() => {
    console.info('SetDistributedTables successfully.');
  }).catch((err: BusinessError) => {
    console.error(\`SetDistributedTables failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### obtainDistributedTableName

obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void

Obtains the distributed table name of a remote device based on the local table name of the device. The distributed table name is required when the RDB store of a remote device is queried. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Bzk5qF32TPeaXdnZDDY1hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5036F17B443B5239D35B410A42D24BFA714115ADA11B64B266B39A1B997A2FCC)

**device** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | ID of the remote device. |
| table | string | Yes | Local table name of the remote device. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation succeeds, the distributed table name of the remote device is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices = dmInstance.getAvailableDeviceListSync();
  deviceId = devices\[0\].networkId;
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).obtainDistributedTableName(deviceId, "EMPLOYEE", (err, tableName) => {
    if (err) {
      console.error(\`ObtainDistributedTableName failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info(\`ObtainDistributedTableName successfully, tableName= ${tableName}\`);
  });
}

#### obtainDistributedTableName

obtainDistributedTableName(device: string, table: string): Promise<string>

Obtains the distributed table name of a remote device based on the local table name of the device. The distributed table name is required when the RDB store of a remote device is queried. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/OnfSjeooQWKI1VjFaqfYIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15375C20DB95B26886C95B0561277F0BC9288E0E9C4552CBAEC4F00B2E9675FD)

**device** can be obtained by [deviceManager.getAvailableDeviceListSync](../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | ID of the remote device. |
| table | string | Yes | Local table name of the remote device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. If the operation succeeds, the distributed table name of the remote device is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices = dmInstance.getAvailableDeviceListSync();
  if (!devices || devices.length === 0) {
    console.error("No available devices found");
  } else {
    deviceId = devices\[0\].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).obtainDistributedTableName(deviceId, "EMPLOYEE").then((tableName: string) => {
    console.info(\`ObtainDistributedTableName successfully, tableName= ${tableName}\`);
  }).catch((err: BusinessError) => {
    console.error(\`ObtainDistributedTableName failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### sync

sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<\[string, number\]>>): void

Synchronizes data across devices. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](../enums/document.md#syncmode) | Yes | Data sync mode. The value can be **relationalStore.SyncMode.SYNC\_MODE\_PUSH** or **relationalStore.SyncMode.SYNC\_MODE\_PULL**. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | **RdbPredicates** object that specifies the data and devices to sync. |
| callback | AsyncCallback<Array<\[string, number\]>> | Yes | Callback used to return the sync result to the caller. **string** indicates the device ID. **number** indicates the sync status of that device. The value **0** indicates a successful sync; **1** indicates a sync failure. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceIds: Array<string> = \[\];

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds\[i\] = devices\[i\].networkId!;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.inDevices(deviceIds);
if (store != undefined) {
  (store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC\_MODE\_PUSH, predicates, (err, result) => {
    if (err) {
      console.error(\`Sync failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Sync done.');
    for (let i = 0; i < result.length; i++) {
      console.info(\`device= ${result\[i\]\[0\]}, status= ${result\[i\]\[1\]}\`);
    }
  });
}

#### sync

sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<\[string, number\]>>

Synchronizes data across devices. This API uses a promise to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](../enums/document.md#syncmode) | Yes | Data sync mode. The value can be **relationalStore.SyncMode.SYNC\_MODE\_PUSH** or **relationalStore.SyncMode.SYNC\_MODE\_PULL**. |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | **RdbPredicates** object that specifies the data and devices to sync. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<\[string, number\]>> | Promise used to send the sync result to the caller. **string** indicates the device ID. **number** indicates the sync status of that device. The value **0** indicates a successful sync; **1** indicates a sync failure. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceIds: Array<string> = \[\];

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds\[i\] = devices\[i\].networkId!;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.inDevices(deviceIds);
if (store != undefined) {
  (store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC\_MODE\_PUSH, predicates).then((result: Object\[\]\[\]) => {
    console.info('Sync done.');
    for (let i = 0; i < result.length; i++) {
      console.info(\`device= ${result\[i\]\[0\]}, status= ${result\[i\]\[1\]}\`);
    }
  }).catch((err: BusinessError) => {
    console.error(\`Sync failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### cloudSync10+

cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void

Manually starts device-cloud sync for all distributed tables. This API uses an asynchronous callback to return the result. Before using this API, ensure that the cloud service is available.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](../enums/document.md#syncmode) | Yes | Sync mode of the database. |
| progress | Callback<[ProgressDetails](../interfaces-others/document.md#progressdetails10)\> | Yes | Callback used to process database sync details. |
| callback | AsyncCallback<void> | Yes | Callback used to return the sync result to the caller. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type. 5. The callback must be a function. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC\_MODE\_CLOUD\_FIRST, (progressDetails) => {
    console.info(\`Progress: ${progressDetails}\`);
  }, (err) => {
    if (err) {
      console.error(\`Cloud sync failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Cloud sync succeeded');
  });
}

#### cloudSync10+

cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>

Manually starts device-cloud sync for all distributed tables. This API uses a promise to return the result. Before using this API, ensure that the cloud service is available.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](../enums/document.md#syncmode) | Yes | Sync mode of the database. |
| progress | Callback<[ProgressDetails](../interfaces-others/document.md#progressdetails10)\> | Yes | Callback used to process database sync details. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to send the sync result to the caller. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC\_MODE\_CLOUD\_FIRST, (progressDetail: relationalStore.ProgressDetails) => {
    console.info(\`progress: ${progressDetail}\`);
  }).then(() => {
    console.info('Cloud sync succeeded');
  }).catch((err: BusinessError) => {
    console.error(\`cloudSync failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### cloudSync10+

cloudSync(mode: SyncMode, tables: string\[\], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void

Manually starts device-cloud sync of the specified table. This API uses an asynchronous callback to return the result. Before using this API, ensure that the cloud service is available.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](../enums/document.md#syncmode) | Yes | Sync mode of the database. |
| tables | string\[\] | Yes | Name of the table to sync. |
| progress | Callback<[ProgressDetails](../interfaces-others/document.md#progressdetails10)\> | Yes | Callback used to process database sync details. |
| callback | AsyncCallback<void> | Yes | Callback used to return the sync result to the caller. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type. 6.The callback must be a function. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

const tables = \["table1", "table2"\];

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC\_MODE\_CLOUD\_FIRST, tables, (progressDetail: relationalStore.ProgressDetails) => {
    console.info(\`Progress: ${progressDetail}\`);
  }, (err) => {
    if (err) {
      console.error(\`Cloud sync failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('Cloud sync succeeded');
  });
};

#### cloudSync10+

cloudSync(mode: SyncMode, tables: string\[\], progress: Callback<ProgressDetails>): Promise<void>

Manually starts device-cloud sync of the specified table. This API uses a promise to return the result. Before using this API, ensure that the cloud service is available.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](../enums/document.md#syncmode) | Yes | Sync mode of the database. |
| tables | string\[\] | Yes | Name of the table to sync. |
| progress | Callback<[ProgressDetails](../interfaces-others/document.md#progressdetails10)\> | Yes | Callback used to process database sync details. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to send the sync result to the caller. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

const tables = \["table1", "table2"\];

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC\_MODE\_CLOUD\_FIRST, tables, (progressDetail: relationalStore.ProgressDetails) => {
    console.info(\`progress: ${progressDetail}\`);
  }).then(() => {
    console.info('Cloud sync succeeded');
  }).catch((err: BusinessError) => {
    console.error(\`cloudSync failed, code is ${err.code},message is ${err.message}\`);
  });
};

#### on('dataChange')

on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

Subscribes to data changes of this RDB store. The registered callback will be called when data in a distributed RDB store changes.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| type | [SubscribeType](../enums/document.md#subscribetype) | Yes | Type of data change to observe. |
| observer | Callback<Array<string>> | Yes | Callback used to return the data change. **Array<string>** holds the IDs of the peer devices whose data is changed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(\`device= ${devices\[i\]} data changed\`);
    }
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

#### on('dataChange')10+

on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void

Subscribes to data changes of this RDB store. The registered callback will be called when data in a distributed or local RDB store changes.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| type | [SubscribeType](../enums/document.md#subscribetype) | Yes | Type of data change to observe. |
| observer | Callback<Array<string>> | Callback<Array<[ChangeInfo](../interfaces-others/document.md#changeinfo10)\>> | Yes | 
Callback used to return the result.

\- If **type** is **SUBSCRIBE\_TYPE\_REMOTE**, **observer** must be **Callback<Array<string>>**, where **Array<string>** holds the IDs of the peer devices with data changes.

\- If **type** is **SUBSCRIBE\_TYPE\_CLOUD**, **observer** must be **Callback<Array<string>>**, where **Array<string>** holds the cloud accounts with data changes.

\- If **type** is **SUBSCRIBE\_TYPE\_CLOUD\_DETAILS**, **observer** must be **Callback<Array<ChangeInfo>>**, where **Array<ChangeInfo>** holds the details about the device-cloud sync.

\- If **type** is **SUBSCRIBE\_TYPE\_LOCAL\_DETAILS**, **observer** must be **Callback<Array<ChangeInfo>>**, where **Array<ChangeInfo>** holds the data change details in the local RDB store.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

Example 1: **type** is **SUBSCRIBE\_TYPE\_REMOTE**.

import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(\`device= ${devices\[i\]} data changed\`);
    }
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

Example 2: **type** is **SUBSCRIBE\_TYPE\_LOCAL\_DETAILS**.

import { BusinessError } from '@kit.BasicServicesKit';

let changeInfos = (changeInfos: Array<relationalStore.ChangeInfo>) => {
  for (let i = 0; i < changeInfos.length; i++) {
    console.info(\`changeInfos = ${JSON.stringify(changeInfos\[i\])}\`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_LOCAL\_DETAILS, changeInfos);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`on dataChange fail, code is ${code},message is ${message}\`);
}

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

try {
  const valueBucket: relationalStore.ValuesBucket = {
    'name': value1,
    'age': value2,
    'salary': value3,
    'blobType': value4
  };

  if (store != undefined) {
    (store as relationalStore.RdbStore).insert('test', valueBucket);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`insert fail, code is ${code},message is ${message}\`);
}

#### on10+

on(event: string, interProcess: boolean, observer: Callback<void>): void

Subscribes to the intra-process or inter-process events of this RDB store. The registered callback will be called when [emit](#emit10) is invoked.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name, which must match the event name in **emit**. |
| interProcess | boolean | Yes | 
Type of the data to observe.

**true**: inter-process.

**false**: intra-process.

 |
| observer | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = () => {
  console.info(\`storeObserver\`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('storeObserver', false, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

#### on('autoSyncProgress')11+

on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void

Subscribes to the auto sync progress. This API can be called only when device-cloud sync is enabled and the network connection is normal. When auto sync is performed, a callback will be invoked to send a notification of the sync progress.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'autoSyncProgress'**, which indicates the auto sync progress. |
| progress | Callback<[ProgressDetails](../interfaces-others/document.md#progressdetails10)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let progressDetail = (progressDetail: relationalStore.ProgressDetails) => {
  console.info(\`progress: ${progressDetail}\`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('autoSyncProgress', progressDetail);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

#### on('statistics')12+

on(event: 'statistics', observer: Callback<SqlExecutionInfo>): void

Subscribes to SQL statistics.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. The value is **'statistics'**, which indicates the statistics of the SQL execution time. |
| observer | Callback<[SqlExecutionInfo](../interfaces-others/document.md#sqlexecutioninfo12)\> | Yes | Callback used to return the statistics about the SQL execution time in the database. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let sqlExecutionInfo = (sqlExecutionInfo: relationalStore.SqlExecutionInfo) => {
  console.info(\`sql: ${sqlExecutionInfo.sql\[0\]}\`);
  console.info(\`totalTime: ${sqlExecutionInfo.totalTime}\`);
  console.info(\`waitTime: ${sqlExecutionInfo.waitTime}\`);
  console.info(\`prepareTime: ${sqlExecutionInfo.prepareTime}\`);
  console.info(\`executeTime: ${sqlExecutionInfo.executeTime}\`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('statistics', sqlExecutionInfo);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

try {
  let value1 = "Lisa";
  let value2 = 18;
  let value3 = 100.5;
  let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  if (store != undefined) {
    (store as relationalStore.RdbStore).insert('test', valueBucket);
  }
} catch (err) {
  console.error(\`insert fail, code:${err.code}, message: ${err.message}\`);
}

#### on('sqliteErrorOccurred')20+

on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void

Subscribes to the error logs generated when SQL statements are executed.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. The value is **sqliteErrorOccurred**, which indicates the error logs generated when SQL statements are executed. |
| observer | Callback<[ExceptionMessage](../interfaces-others/document.md#exceptionmessage20)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    store.on('sqliteErrorOccurred', exceptionMessage => {
      let sqliteCode = exceptionMessage.code;
      let sqliteMessage = exceptionMessage.message;
      let errSQL = exceptionMessage.sql;
      console.error(\`error log is ${sqliteCode}, errMessage is ${sqliteMessage}, errSQL is ${errSQL}\`);
    })
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}
const CREATE\_TABLE\_TEST = "CREATE TABLE IF NOT EXISTS test (" + "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
  "name TEXT NOT NULL, " + "age INTEGER, " + "salary REAL)";
try {
  let value = new Uint8Array(\[1, 2, 3, 4, 5\]);
  const valueBucket: relationalStore.ValuesBucket = {
    'name': "Lisa",
    'age': 18,
    'salary': 100.5,
    'codes': value,
  };
  await store.executeSql(CREATE\_TABLE\_TEST);
  if (store != undefined) {
    (store as relationalStore.RdbStore).insert('test', valueBucket);
  }
} catch (err) {
  console.error(\`Insert fail, code:${err.code}, message: ${err.message}\`);
}

#### on('perfStat')20+

on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void

Subscribes to SQL statistics. Operations performed on the [transaction](../interface-transaction/document.md) created by [createTransaction](#createtransaction14) notify the statistics only once when the transaction is committed or rolled back.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. The value is **'perfStat'**, which indicates the SQL execution time. |
| observer | Callback<[SqlExecutionInfo](../interfaces-others/document.md#sqlexecutioninfo12)\> | Yes | Callback used to return the SQL execution time in the database. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let sqlExecutionInfo = (sqlExecutionInfo: relationalStore.SqlExecutionInfo) => {
  console.info(\`sql: ${sqlExecutionInfo.sql\[0\]}\`);
  console.info(\`totalTime: ${sqlExecutionInfo.totalTime}\`);
  console.info(\`waitTime: ${sqlExecutionInfo.waitTime}\`);
  console.info(\`prepareTime: ${sqlExecutionInfo.prepareTime}\`);
  console.info(\`executeTime: ${sqlExecutionInfo.executeTime}\`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('perfStat', sqlExecutionInfo);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

try {
  let value1 = "Lisa";
  let value2 = 18;
  let value3 = 100.5;
  let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  if (store != undefined) {
    const rowId = await store.insert('EMPLOYEE', valueBucket);
    console.info(\`Insert success, rowId is: ${rowId}\`);
  }
} catch (err) {
  console.error(\`insert fail, code:${err.code}, message: ${err.message}\`);
}

#### off('dataChange')

off(event:'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

Unsubscribes from process events.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| type | [SubscribeType](../enums/document.md#subscribetype) | Yes | Type of data change to observe. |
| observer | Callback<Array<string>> | Yes | Callback to unregister. **Array<string>** holds the IDs of the peer devices whose data is changed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(\`device= ${devices\[i\]} data changed\`);
    }
  }
};

try {
  if (store != undefined) {
    // The Lambda expression cannot be used here.
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister observer failed, code is ${code},message is ${message}\`);
}

#### off('dataChange')10+

off(event:'dataChange', type: SubscribeType, observer?: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void

Unsubscribes from process events.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| type | [SubscribeType](../enums/document.md#subscribetype) | Yes | Type of data change to observe. |
| observer | Callback<Array<string>>| Callback<Array<[ChangeInfo](../interfaces-others/document.md#changeinfo10)\>> | No | 
Callback used to return the result.

\- If **type** is **SUBSCRIBE\_TYPE\_REMOTE**, **observer** must be **Callback<Array<string>>**, where **Array<string>** holds the IDs of the peer devices with data changes.

\- If **type** is **SUBSCRIBE\_TYPE\_CLOUD**, **observer** must be **Callback<Array<string>>**, where **Array<string>** holds the cloud accounts with data changes.

\- If **type** is **SUBSCRIBE\_TYPE\_CLOUD\_DETAILS**, **observer** must be **Callback<Array<ChangeInfo>>**, where **Array<ChangeInfo>** holds the details about the device-cloud sync.

\- If **type** is **SUBSCRIBE\_TYPE\_LOCAL\_DETAILS**, **observer** must be **Callback<Array<ChangeInfo>>**, where **Array<ChangeInfo>** holds the data change details in the local RDB store.

\- If **observer** is not specified, this API unregisters all callbacks for data changes of the specified **type**.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(\`device= ${devices\[i\]} data changed\`);
    }
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister observer failed, code is ${code},message is ${message}\`);
}

#### off10+

off(event: string, interProcess: boolean, observer?: Callback<void>): void

Unsubscribes from process events.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name, which matches the event name in **on()**. |
| interProcess | boolean | Yes | 
Type of the data to observe.

**true**: inter-process.

**false**: intra-process.

 |
| observer | Callback<void> | No | If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = () => {
  console.info(\`storeObserver\`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('storeObserver', false, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('storeObserver', false, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister observer failed, code is ${code},message is ${message}\`);
}

#### off('autoSyncProgress')11+

off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void

Unsubscribes from the auto sync progress.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event type. The value is **'autoSyncProgress'**, which indicates the auto sync progress. |
| progress | Callback<[ProgressDetails](../interfaces-others/document.md#progressdetails10)\> | No | Callback to unregister. If this parameter is **null** or **undefined** or not specified, this API unregisters all callbacks for the auto sync progress. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be valid. 3. The event must be a not empty string. 4. The progress must be function. |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let progressDetail = (progressDetail: relationalStore.ProgressDetails) => {
  console.info(\`progress: ${progressDetail}\`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('autoSyncProgress', progressDetail);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Register observer failed, code is ${code},message is ${message}\`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('autoSyncProgress', progressDetail);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister failed, code is ${code},message is ${message}\`);
}

#### off('statistics')12+

off(event: 'statistics', observer?: Callback<SqlExecutionInfo>): void

Unsubscribes from SQL statistics.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. The value is **'statistics'**, which indicates the statistics of the SQL execution time. |
| observer | Callback<[SqlExecutionInfo](../interfaces-others/document.md#sqlexecutioninfo12)\> | No | Callback used to return the result. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |

import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('statistics');
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister observer failed, code is ${code},message is ${message}\`);
}

#### off('sqliteErrorOccurred')20+

off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void

Unsubscribes from error logs generated during SQL statement execution.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. The value is **sqliteErrorOccurred**, which indicates the error logs generated when SQL statements are executed. |
| observer | Callback<[ExceptionMessage](../interfaces-others/document.md#exceptionmessage20)\> | No | Callback used to return the result. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('sqliteErrorOccurred');
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister observer failed, code is ${code},message is ${message}\`);
}

#### off('perfStat')20+

off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void

Unsubscribes from SQL statistics.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. The value is **'perfStat'**, which indicates the SQL execution time. |
| observer | Callback<[SqlExecutionInfo](../interfaces-others/document.md#sqlexecutioninfo12)\> | No | Callback used to return the result. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800014 | The RdbStore or ResultSet is already closed. |

import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('perfStat');
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(\`Unregister observer failed, code is ${code},message is ${message}\`);
}

#### emit10+

emit(event: string): void

Triggers the inter-process or intra-process event listener registered in [on](#on10).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event name. Custom event names are allowed. However, the customized event name cannot be duplicate with the existing event names [dataChange](#ondatachange), [autoSyncProgress](#onautosyncprogress11), and [statistics](#onstatistics12). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).emit('storeObserver');
}

#### cleanDirtyData11+

cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void

Clears the dirty data whose cursor is smaller than the specified cursor from the local device. The dirty data is the data that has been deleted from the cloud.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the table in the RDB store. |
| cursor | number | Yes | Cursor of the data, which is an integer. All the dirty data with the cursor smaller than the specified value will be cleared. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).cleanDirtyData('test\_table', 100, (err) => {
    if (err) {
      console.error(\`clean dirty data failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('clean dirty data succeeded');
  });
}

#### cleanDirtyData11+

cleanDirtyData(table: string, callback: AsyncCallback<void>): void

Clears all dirty data from the local device. The dirty data is the data that has been deleted from the cloud.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the table in the RDB store. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s). 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

if (store != undefined) {
  (store as relationalStore.RdbStore).cleanDirtyData('test\_table', (err) => {
    if (err) {
      console.error(\`clean dirty data failed, code is ${err.code},message is ${err.message}\`);
      return;
    }
    console.info('clean dirty data succeeded');
  });
}

#### cleanDirtyData11+

cleanDirtyData(table: string, cursor?: number): Promise<void>

Cleans the dirty data whose cursor is smaller than the specified cursor from the local device. The dirty data is the data that has been deleted from the cloud. This API uses a promise to return the result. If **cursor** is not specified, all the dirty data will be cleared.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the table in the RDB store. |
| cursor | number | No | Cursor of the data, which is an integer. All the dirty data with the cursor smaller than the specified value will be cleared. If this parameter is not specified, all dirty data in the current table will be cleared. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).cleanDirtyData('test\_table', 100).then(() => {
    console.info('clean dirty data  succeeded');
  }).catch((err: BusinessError) => {
    console.error(\`clean dirty data failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### attach12+

attach(fullPath: string, attachName: string, waitTime?: number) : Promise<number>

Attaches an RDB store to this RDB store so that the data in the attached RDB store can be directly accessed using the SQL statement. This API uses a promise to return the result.

The RDB store is attached via a database file. This API cannot be used for encrypted RDB stores. After the **attach** API is called, the RDB store is switched to the non-WAL mode, which may affect the performance.

Before the RDB store is switched to non-WAL mode, ensure that all **ResultSet**s are closed and all write operations are complete. Otherwise, error 14800015 will be reported.

The **attach** API cannot be called concurrently. Concurrent calls may cause the system to become unresponsive and trigger 14800015. If this occurs, try to call **attach()** again later.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fullPath | string | Yes | Path of the database file to attach. |
| attachName | string | Yes | Alias of the RDB store formed after the attach operation. |
| waitTime | number | No | 
Maximum time period (in seconds) allowed for attaching the database file.

Value range: 1 to 300

Default value: **2**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of attached RDB stores. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800016 | The database alias already exists. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

// Attach a non-encrypted RDB store to a non-encrypted RDB store.
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).attach("/path/rdbstore1.db", "attachDB").then((number: number) => {
    console.info('attach succeeded');
  }).catch((err: BusinessError) => {
    console.error(\`attach failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### attach12+

attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number) : Promise<number>

Attaches an RDB store of the current application to this RDB store so that the data in the attached RDB store can be directly accessed using the SQL statement. This API uses a promise to return the result.

This API cannot be used to attach a non-encrypted RDB store to an encrypted RDB store. After the **attach** API is called, the RDB store is switched to the non-WAL mode, which may affect the performance.

Before the RDB store is switched to non-WAL mode, ensure that all **ResultSet**s are closed and all write operations are complete. Otherwise, error 14800015 will be reported.

The **attach** API cannot be called concurrently. Concurrent calls may cause the system to become unresponsive and trigger 14800015. If this occurs, try to call **attach()** again later. In addition, when an encrypted database is attached, the database may fail to be decrypted due to concurrency and error 14800011 is reported. In this case, explicitly specify encryption parameters and try again.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| config | [StoreConfig](../interfaces-others/document.md#storeconfig) | Yes | Configuration of the RDB store. |
| attachName | string | Yes | Alias of the RDB store formed after the attach operation. |
| waitTime | number | No | 

Maximum time period (in seconds) allowed for attaching the database file.

Value range: 1 to 300

Default value: **2**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of attached RDB stores. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800016 | The database alias already exists. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

Example 1: Attach a non-encrypted RDB store to a non-encrypted RDB store.

import { BusinessError } from '@kit.BasicServicesKit';

let attachStore: relationalStore.RdbStore | undefined = undefined;

const STORE\_CONFIG1: relationalStore.StoreConfig = {
  name: "rdbstore1.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(this.context, STORE\_CONFIG1).then(async (rdbStore: relationalStore.RdbStore) => {
  attachStore = rdbStore;
  console.info('Get RdbStore successfully.');
  if (store != undefined) {
    (store as relationalStore.RdbStore).attach(this.context, STORE\_CONFIG1, "attachDB").then((number: number) => {
      console.info(\`attach succeeded, number is ${number}\`);
    }).catch((err: BusinessError) => {
      console.error(\`attach failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}).catch((err: BusinessError) => {
  console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
});

Example 2: Attach an encrypted RDB store to a non-encrypted RDB store.

import { BusinessError } from '@kit.BasicServicesKit';

let attachStore: relationalStore.RdbStore | undefined = undefined;

const STORE\_CONFIG2: relationalStore.StoreConfig = {
  name: "rdbstore2.db",
  encrypt: true,
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(this.context, STORE\_CONFIG2).then(async (rdbStore: relationalStore.RdbStore) => {
  attachStore = rdbStore;
  console.info('Get RdbStore successfully.');
  if (store != undefined) {
    (store as relationalStore.RdbStore).attach(this.context, STORE\_CONFIG2, "attachDB2", 10).then((number: number) => {
      console.info(\`attach succeeded, number is ${number}\`);
    }).catch((err: BusinessError) => {
      console.error(\`attach failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}).catch((err: BusinessError) => {
  console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
});

#### detach12+

detach(attachName: string, waitTime?: number) : Promise<number>

Detaches an RDB store from this RDB store. This API uses a promise to return the result.

After all attached RDB stores are detached, the RDB is switched to the WAL mode.

Before calling **detach()**, ensure that all database operations are complete and all **ResultSet**s are closed. In addition, **detach()** cannot be called concurrently. Concurrent calls may cause the system to become unresponsive. If this occurs, try to call **detach()** again later.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attachName | string | Yes | Alias of the RDB store formed after the attach operation. |
| waitTime | number | No | 
Maximum time period (in seconds) allowed for detaching the RDB store.

Value range: 1 to 300

Default value: **2**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of remaining attached RDB stores. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).detach("attachDB").then((number: number) => {
    console.info(\`detach succeeded, number is ${number}\`);
  }).catch((err: BusinessError) => {
    console.error(\`detach failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### lockRow12+

lockRow(predicates: RdbPredicates):Promise<void>

Locks data in this RDB store. This API uses a promise to return the result. The locked data is blocked from device-cloud sync.

This API supports only the tables with the primary keys of the basic types. It is not available to shared tables, tables without primary keys, or tables with primary keys of composite types.

This API does not support lock transfer between tables with dependencies. If this table has dependent tables, you need to call this API for the related tables based on the dependency relationships.

This API cannot be used for deleted data.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Locking conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800018 | No data meets the condition. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).lockRow(predicates).then(() => {
    console.info(\`Lock success\`);
  }).catch((err: BusinessError) => {
    console.error(\`Lock failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### unlockRow12+

unlockRow(predicates: RdbPredicates):Promise<void>

Unlocks data in this RDB store. This API uses a promise to return the result.

This API supports only the tables with the primary keys of the basic types. It is not available to shared tables, tables without primary keys, or tables with primary keys of composite types.

This API does not support lock transfer between tables with dependencies. If this table has dependent tables, you need to call this API for the related tables based on the dependency relationships.

This API cannot be used for deleted data.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Locking conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800018 | No data meets the condition. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).unlockRow(predicates).then(() => {
    console.info(\`Unlock success\`);
  }).catch((err: BusinessError) => {
    console.error(\`Unlock failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### queryLockedRow12+

queryLockedRow(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

Queries the locked data in this RDB store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | No | Columns to query. If this parameter is not specified, the query applies to all columns. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResultSet](../interface-resultset/document.md)\> | Promise used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). For details about how to handle error 14800011, see [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).queryLockedRow(predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(\`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}\`);
    // resultSet is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(\`id=${id}, name=${name}, age=${age}, salary=${salary}\`);
      }
    } catch (err) {
      console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
    } finally {
      // Release the memory of resultSet. If the memory is not released, FD or memory leaks may occur.
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(\`Query failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### close12+

close(): Promise<void>

Closes this RDB store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).close().then(() => {
    console.info(\`close succeeded\`);
  }).catch((err: BusinessError) => {
    console.error(\`close failed, code is ${err.code},message is ${err.message}\`);
  });
}

#### rekey20+

rekey(cryptoParam?: CryptoParam): Promise<void>

Updates the key of an encrypted database. This API uses a promise to return the result.

Key update is not supported for databases in non-WAL mode.

Manual update requires exclusive access to the database. If any result set, transaction, or database opened by another process is not released, the update will fail.

Only encrypted databases can be updated. Non-encrypted databases cannot be changed to encrypted databases, and vice versa. The encryption parameters and key generation mode must be the same as those used during database creation.

The larger the database, the longer the key update takes.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cryptoParam | [CryptoParam](../interfaces-others/document.md#cryptoparam14) | No | 
Custom encryption parameters.

If this parameter is not set, the default encryption parameters are used. For details, see CryptoParam.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**Example:**

For details about the definition of **this.context** in the sample code, see the application [context](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) of the stage model.

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// Example 1: Use default encryption parameters.
export default class EntryAbility extends UIAbility {
  onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const STORE\_CONFIG1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true
    };

    relationalStore.getRdbStore(this.context, STORE\_CONFIG1).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array()
      };

      if (store != undefined) {
        try {
          (store as relationalStore.RdbStore).rekey(cryptoParam1);
          console.info('rekey is successful');
        } catch (err) {
          console.error(\`rekey is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
    }).catch((err: BusinessError) => {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// Example 2: Use custom encryption parameters.
export default class EntryAbility extends UIAbility {
  onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      encryptionKey: new Uint8Array(\[1, 2, 3, 4, 5, 6\]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
      cryptoPageSize: 1024
    };

    const STORE\_CONFIG2: relationalStore.StoreConfig = {
      name: 'rdbstore2.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    relationalStore.getRdbStore(this.context, STORE\_CONFIG2).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');
      let cryptoParam2: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(\[6, 5, 4, 3, 2, 1\]),
        iterationCount: 1000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_GCM,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
        cryptoPageSize: 1024
      };

      if (store != undefined) {
        try {
          (store as relationalStore.RdbStore).rekey(cryptoParam2);
          console.info('rekey is successful');
        } catch (err) {
          console.error(\`rekey is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
    }).catch((err: BusinessError) => {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}

#### setLocale20+

setLocale(locale: string) : Promise<void>

Sets locale. This API uses a promise to return the result.

The value complies with the ISO 639 standard and supports some languages in ICU. For languages not supported, error code 14800001 is reported when the locale is set.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | Locale to set. The value complies with the ISO 639 standard, for example, **zh**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800034 | SQLite: Library used incorrectly. |

**Example:**

try {
  if (store != undefined) {
    await store.setLocale("zh");
    store.querySql("SELECT \* FROM EMPLOYEE ORDER BY NAME COLLATE LOCALES", async (err, resultSet) => {
      if (err) {
        console.error(\`Query failed, code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info(\`ResultSet rowCount ${resultSet.rowCount}\`);
    });
  }
} catch (err) {
  console.error(\`SetLocale failed, code: ${err.code}, message: ${err.message}\`);
}

#### rekeyEx22+

rekeyEx(cryptoParam: CryptoParam): Promise<void>

Manually updates the database key or encryption parameters. This API uses a promise to return the result.

Key update is not supported for databases in non-WAL mode.

Manual update requires exclusive access to the database. If any result set, transaction, or database opened by another process is not released, the update will fail.

Parameter update for an encrypted database and conversion between an encrypted database and a non-encrypted database are supported.

The larger the database, the longer the update takes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/5SF0Lee9SISrwdjcsL_zlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8F0B6DDFEB060E194459A1B647DB40393A213D2819CE8E6C8A5F27F3BB352D0)

Exercise caution when changing encryption parameters. After **rekeyEx** is executed, you must use the new parameters to open the database when calling **getRdbStore**. Otherwise, the database may fail to be opened.

If the rekey process is interrupted due to device power-off or other reasons, the operation may succeed or fail. Therefore, it is recommended that the service party perform a redundancy retry based on the parameters modified before and after **RekeyEx** is used to ensure the database status is correctly determined and the database can be opened.

If the encryption parameters are changed, do not use the **AllowedRebuild** parameter when calling **getRdbStore** to prevent the database from being rebuilt due to incorrect encryption parameters.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cryptoParam | [CryptoParam](../interfaces-others/document.md#cryptoparam14) | Yes | Custom encryption parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14800014 | The RdbStore or ResultSet is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**Example 1: The original database is encrypted using default parameters. Change the key and encryption parameters.**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(),
        encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
        iterationCount: 1000,
        cryptoPageSize: 2048,
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(\`rekeyEx is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
      // After rekeyEx is used, use new parameters for getRdbStore to reopen the database.
    } catch (err) {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    };
  }
}

**Example 2: The original database is encrypted using custom parameters. Change the custom key and encryption parameters.**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      // Security reminder: 1. An empty array encryptionKey indicates that the key generated by the system is used (applicable only to some scenarios). 2. In the production environment, use the application sandbox key or secure storage service management key. Do not use hard-coded key in the code.
      encryptionKey: new Uint8Array(\[1, 2, 3, 4, 5, 6\]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
      cryptoPageSize: 1024
    };
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(\[6, 5, 4, 3, 2, 1\]),
        iterationCount: 5000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA512,
        kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA512,
        cryptoPageSize: 2048
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(\`rekeyEx is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
      // After rekeyEx is used, use new parameters for getRdbStore to reopen the database.
    } catch (err) {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    };
  }
}

**Example 3: The original database is encrypted using default parameters. Change the default key and parameters to the custom key and encryption parameters.**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam: relationalStore.CryptoParam = {
        // Security reminder: 1. An empty array encryptionKey indicates that the key generated by the system is used (applicable only to some scenarios). 2. In the production environment, use the application sandbox key or secure storage service management key. Do not use hard-coded key in the code.
        encryptionKey: new Uint8Array(\[6, 5, 4, 3, 2, 1\]),
        encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
        iterationCount: 1000,
        cryptoPageSize: 2048,
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(\`rekeyEx is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
      // After rekeyEx is used, use new parameters for getRdbStore to reopen the database.
    } catch (err) {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    };
  }
}

**Example 4: The original database is encrypted using custom parameters. Change the key generated by database and custom encryption parameters.**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      // Security reminder: 1. An empty array encryptionKey indicates that the key generated by the system is used (applicable only to some scenarios). 2. In the production environment, use the application sandbox key or secure storage service management key. Do not use hard-coded key in the code.
      encryptionKey: new Uint8Array(\[1, 2, 3, 4, 5, 6\]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
      cryptoPageSize: 1024
    };
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore2.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(),
        iterationCount: 5000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA512,
        kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA512,
        cryptoPageSize: 2048
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(\`rekeyEx is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
      // After rekeyEx is used, use new parameters for getRdbStore to reopen the database.
    } catch (err) {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    };
  }
}

**Example 5: The original database is an encrypted database. Change it to a non-encrypted database.**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      // Security reminder: 1. An empty array encryptionKey indicates that the key generated by the system is used (applicable only to some scenarios). 2. In the production environment, use the application sandbox key or secure storage service management key. Do not use hard-coded key in the code.
      encryptionKey: new Uint8Array(\[1, 2, 3, 4, 5, 6\]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
      cryptoPageSize: 1024
    };
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(),
        encryptionAlgo: relationalStore.EncryptionAlgo.PLAIN\_TEXT
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(\`rekeyEx is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
      // After rekeyEx is used, use new parameters for getRdbStore to reopen the database.
    } catch (err) {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    };
  }
}

**Example 6: The original database is a non-encrypted database. Change it to a database encrypted using custom parameters.**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: false,
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam: relationalStore.CryptoParam = {
        // Security reminder: 1. An empty array encryptionKey indicates that the key generated by the system is used (applicable only to some scenarios). 2. In the production environment, use the application sandbox key or secure storage service management key. Do not use hard-coded key in the code.
        encryptionKey: new Uint8Array(\[1, 2, 3, 4, 5, 6\]),
        iterationCount: 1000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES\_256\_GCM,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF\_SHA256,
        cryptoPageSize: 1024
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(\`rekeyEx is failed, code is ${err.code},message is ${err.message}\`);
        }
      }
      // After rekeyEx is used, use new parameters for getRdbStore to reopen the database.
    } catch (err) {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    };
  }
}
