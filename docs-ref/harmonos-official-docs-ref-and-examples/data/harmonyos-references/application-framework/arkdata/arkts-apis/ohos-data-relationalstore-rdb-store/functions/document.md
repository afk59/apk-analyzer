# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/OGy0sICPSjSNgZYj0WFqUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF7875C2FBCEE68A0115C75CF826F923BE133F462AD11E1C9B91617EF320C00B)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Module to Import

import { relationalStore } from '@kit.ArkData';

#### relationalStore.getRdbStore

getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void

Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform data operations. This API uses an asynchronous callback to return the result.

If no database file exists in the corresponding sandbox directory, a database file is created. For details, see [StoreConfig](../interfaces-others/document.md#storeconfig). If a database file exists in the corresponding directory, the existing database file is opened.

When creating a database, you should consider whether to configure the [encrypt](../interfaces-others/document.md#storeconfig) parameter. Once the database is created, you are not allowed to change this parameter.

| Encryption Type When the RDB Store Is Opened | Encryption Type When the RDB Store Is Created | Result |
| :-- | :-- | :-- |
| Non-encryption | Encryption | The RDB store is opened in encrypted mode. |
| Encryption | Non-encryption | The RDB store is opened in non-encrypted mode. |

Currently, **getRdbStore()** does not support multi-thread concurrent operations.

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
| callback | AsyncCallback<[RdbStore](../interface-rdbstore/document.md)\> | Yes | Callback invoked to return the RDB store obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). To handle error 14800011, you can refer to [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800017 | StoreConfig is changed. |
| 14800020 | The secret key is corrupted or lost. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**Example**:

FA model:

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;
let context = featureAbility.getContext();

const STORE\_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(context, STORE\_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
  if (err) {
    console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    return;
  }
  console.info('Get RdbStore successfully.');
  store = rdbStore;
  // Perform subsequent operations after the rdbStore instance is successfully obtained.
});

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };

    relationalStore.getRdbStore(this.context, STORE\_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
      if (err) {
        console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
        return;
      }
      console.info('Get RdbStore successfully.');
      store = rdbStore;
      // Perform subsequent operations after the rdbStore instance is successfully obtained.
    });
  }
}

#### relationalStore.getRdbStore

getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>

Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform data operations. This API uses a promise to return the result.

If no database file exists in the corresponding sandbox directory, a database file is created. For details, see [StoreConfig](../interfaces-others/document.md#storeconfig). If a database file exists in the corresponding directory, the existing database file is opened.

When creating a database, you should consider whether to configure the [encrypt](../interfaces-others/document.md#storeconfig) parameter. Once the database is created, you are not allowed to change this parameter.

| Encryption Type When the RDB Store Is Opened | Encryption Type When the RDB Store Is Created | Result |
| :-- | :-- | :-- |
| Non-encryption | Encryption | The RDB store is opened in encrypted mode. |
| Encryption | Non-encryption | The RDB store is opened in non-encrypted mode. |

Currently, **getRdbStore()** does not support multi-thread concurrent operations.

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

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RdbStore](../interface-rdbstore/document.md)\> | Promise used to return the **RdbStore** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md). To handle error 14800011, you can refer to [Database Backup and Restore](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-backup-and-restore).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | Failed to open the database because it is corrupted. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800017 | StoreConfig is changed. |
| 14800020 | The secret key is corrupted or lost. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**Example**:

FA model:

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;
let context = featureAbility.getContext();

const STORE\_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(context, STORE\_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
  store = rdbStore;
  console.info('Get RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
});

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };

    relationalStore.getRdbStore(this.context, STORE\_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}

#### relationalStore.deleteRdbStore

deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void

Deletes an RDB store. This API uses an asynchronous callback to return the result.

After the deletion, you are advised to set the database object to null. If a custom path is set in [StoreConfig](../interfaces-others/document.md#storeconfig) when an RDB store is created, using this API cannot delete the RDB store. Use [deleteRdbStore](#relationalstoredeleterdbstore10) instead.

Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been closed.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | Name of the RDB store to delete. |
| callback | AsyncCallback<void> | Yes | Callback invoked to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |

**Example**:

FA model:

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

relationalStore.deleteRdbStore(context, "RdbTest.db", (err: BusinessError) => {
  if (err) {
    console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
    return;
  }
  // After the database is deleted, the initialized RdbStore instance cannot be used.
  // Clear the related variables to release resources in time.
  console.info('Delete RdbStore successfully.');
});

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    relationalStore.deleteRdbStore(this.context, "RdbTest.db", (err: BusinessError) => {
      if (err) {
        console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
        return;
      }
      // After the database is deleted, the initialized RdbStore instance cannot be used.
      // Clear the related variables to release resources in time.
      console.info('Delete RdbStore successfully.');
    });
  }
}

#### relationalStore.deleteRdbStore

deleteRdbStore(context: Context, name: string): Promise<void>

Deletes an RDB store. This API uses a promise to return the result.

After the deletion, you are advised to set the database object to null. If a custom path is set in [StoreConfig](../interfaces-others/document.md#storeconfig) when an RDB store is created, using this API cannot delete the RDB store. Use [deleteRdbStore](#relationalstoredeleterdbstore10-1) instead.

Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been closed.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | Name of the RDB store to delete. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |

**Example**:

FA model:

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

relationalStore.deleteRdbStore(context, "RdbTest.db").then(() => {
  // After the database is deleted, the initialized RdbStore instance cannot be used.
  // Clear the related variables to release resources in time.
  console.info('Delete RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
});

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    relationalStore.deleteRdbStore(this.context, "RdbTest.db").then(() => {
      // After the database is deleted, the initialized RdbStore instance cannot be used.
      // Clear the related variables to release resources in time.
      console.info('Delete RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}

#### relationalStore.deleteRdbStore10+

deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void

Deletes an RDB store. This API uses an asynchronous callback to return the result.

After the deletion, you are advised to set the database object to null. If the database file is stored in the sandbox directory, use this API to delete the database. If multiple processes operate the same database, other processes should be notified about the database deletion so that they can detect and process the deletion. If a custom path is set in [StoreConfig](../interfaces-others/document.md#storeconfig) during RDB store creation, using this API to delete the RDB store.

Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been closed.

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
| callback | AsyncCallback<void> | Yes | Callback invoked to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |

**Example**:

FA model:

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

const STORE\_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.deleteRdbStore(context, STORE\_CONFIG, (err: BusinessError) => {
  if (err) {
    console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
    return;
  }
  // After the database is deleted, the initialized RdbStore instance cannot be used.
  // Clear the related variables to release resources in time.
  console.info('Delete RdbStore successfully.');
});

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    relationalStore.deleteRdbStore(this.context, STORE\_CONFIG, (err: BusinessError) => {
      if (err) {
        console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
        return;
      }
      // After the database is deleted, the initialized RdbStore instance cannot be used.
      // Clear the related variables to release resources in time.
      console.info('Delete RdbStore successfully.');
    });
  }
}

#### relationalStore.deleteRdbStore10+

deleteRdbStore(context: Context, config: StoreConfig): Promise<void>

Deletes an RDB store. This API uses a promise to return the result.

After the deletion, you are advised to set the database object to null. If the database file is stored in the sandbox directory, use this API to delete the database. If multiple processes operate the same database, other processes should be notified about the database deletion so that they can detect and process the deletion. If a custom path is set in [StoreConfig](../interfaces-others/document.md#storeconfig) during RDB store creation, using this API to delete the RDB store.

Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been closed.

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

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |

**Example**:

FA model:

import { featureAbility } from "@kit.AbilityKit";
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

const STORE\_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.deleteRdbStore(context, STORE\_CONFIG).then(() => {
  // After the database is deleted, the initialized RdbStore instance cannot be used.
  // Clear the related variables to release resources in time.
  console.info('Delete RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
});

Stage model:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    relationalStore.deleteRdbStore(this.context, STORE\_CONFIG).then(() => {
      // After the database is deleted, the initialized RdbStore instance cannot be used.
      // Clear the related variables to release resources in time.
      console.info('Delete RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(\`Delete RdbStore failed, code is ${err.code},message is ${err.message}\`);
    });
  }
}

#### relationalStore.isVectorSupported18+

isVectorSupported(): boolean

Checks whether the system supports vector stores.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the system supports vector stores; returns **false** otherwise. |

**Example**:

import { contextConstant, UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { relationalStore } from '@kit.ArkData';

let store: relationalStore.RdbStore | undefined = undefined;
export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let supported = relationalStore.isVectorSupported();
    if (supported) {
      // Vector stores are supported.
      console.info("Vector database supported on current platform.");
      const STORE\_CONFIG: relationalStore.StoreConfig = {
        name: "VectorTest.db",
        securityLevel: relationalStore.SecurityLevel.S3,
        vector: true
      };
      try {
        const context = this.context.getApplicationContext().createAreaModeContext(contextConstant.AreaMode.EL3);
        const rdbStore = await relationalStore.getRdbStore(context, STORE\_CONFIG);
        console.info('Get RdbStore successfully.');
        store = rdbStore;
        // Perform subsequent operations after the rdbStore instance is successfully obtained.
      } catch (error) {
        const err = error as BusinessError;
        console.error(\`Get RdbStore failed, code is ${err.code},message is ${err.message}\`);
      }
    } else {
      console.info("Vector database not supported on current platform.");
    }
  }
}

#### relationalStore.isTokenizerSupported18+

isTokenizerSupported(tokenizer: Tokenizer): boolean

Checks whether the specified tokenizer is supported. This API returns the result synchronously.

This API returns **true** if the specified tokenizer is supported; returns **false** otherwise.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tokenizer | [Tokenizer](../enums/document.md#tokenizer17) | Yes | Tokenizer to check. |

**Return Value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the specified tokenizer is supported; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let customType = relationalStore.Tokenizer.CUSTOM\_TOKENIZER;
let customTypeSupported = relationalStore.isTokenizerSupported(customType);
console.info("custom tokenizer supported on current platform: " + customTypeSupported);

#### relationalStore.getInsertSqlInfo20+

getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo

Obtains the SQL statement used to insert data. This API returns the result synchronously.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the database table to which data is to be written. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Field information and corresponding values of the data to be written to the database. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | No | 
Resolution used to resolve the conflict.

Default value: **relationalStore.ConflictResolution.ON\_CONFLICT\_NONE**.

 |

**Return Value**

| Type | Description |
| :-- | :-- |
| [SqlInfo](../interfaces-others/document.md#sqlinfo20) | **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the parameters in the executed SQL statement. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**Example**:

const bucket: relationalStore.ValuesBucket = {
  name: "Logitech",
  age: 18,
  sex: "man",
  desc: "asserter"
};
const sqlInfo: relationalStore.SqlInfo = relationalStore.getInsertSqlInfo(
  "USER",
  bucket,
  relationalStore.ConflictResolution.ON\_CONFLICT\_NONE
);

#### relationalStore.getUpdateSqlInfo20+

getUpdateSqlInfo(predicates: RdbPredicates, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo

Obtains the SQL statement used to update data. This API returns the result synchronously.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | **RdbPredicates** object that matches the specified field. |
| values | [ValuesBucket](../types/document.md#valuesbucket) | Yes | Field information and corresponding values of the data to be written to the database. |
| conflict | [ConflictResolution](../enums/document.md#conflictresolution10) | No | 
Resolution used to resolve the conflict.

Default value: **relationalStore.ConflictResolution.ON\_CONFLICT\_NONE**.

 |

**Return Value**

| Type | Description |
| :-- | :-- |
| [SqlInfo](../interfaces-others/document.md#sqlinfo20) | **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the parameters in the executed SQL statement. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**Example**:

const bucket: relationalStore.ValuesBucket = {
  name: "Logitech",
  age: 18,
  sex: "man",
  desc: "asserter"
};
const predicates = new relationalStore.RdbPredicates("users");
const sqlInfo: relationalStore.SqlInfo = relationalStore.getUpdateSqlInfo(
  predicates,
  bucket,
  relationalStore.ConflictResolution.ON\_CONFLICT\_NONE
);

#### relationalStore.getDeleteSqlInfo20+

getDeleteSqlInfo(predicates: RdbPredicates): SqlInfo

Obtains the SQL statement used to delete data. This API returns the result synchronously.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | **RdbPredicates** object that matches the specified field. |

**Return Value**

| Type | Description |
| :-- | :-- |
| [SqlInfo](../interfaces-others/document.md#sqlinfo20) | **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the parameters in the executed SQL statement. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**Example**:

const predicates = new relationalStore.RdbPredicates("users");
predicates.equalTo("tableName", "a");
predicates.notEqualTo("age", 18);
const sqlInfo: relationalStore.SqlInfo = relationalStore.getDeleteSqlInfo(predicates);

#### relationalStore.getQuerySqlInfo20+

getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>): SqlInfo

Obtains the SQL statement used to query data. This API returns the result synchronously.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](../class-rdbpredicates/document.md) | Yes | **RdbPredicates** object that matches the specified field. |
| columns | Array<string> | No | Columns to be queried. If this parameter is not specified, all columns are queried. |

**Return Value**

| Type | Description |
| :-- | :-- |
| [SqlInfo](../interfaces-others/document.md#sqlinfo20) | **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the parameters in the executed SQL statement. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**Example**:

const predicates = new relationalStore.RdbPredicates("users");
predicates.notEqualTo("age", 18);
predicates.equalTo("name", "zhangsan");
const sqlInfo: relationalStore.SqlInfo = relationalStore.getQuerySqlInfo(predicates);
