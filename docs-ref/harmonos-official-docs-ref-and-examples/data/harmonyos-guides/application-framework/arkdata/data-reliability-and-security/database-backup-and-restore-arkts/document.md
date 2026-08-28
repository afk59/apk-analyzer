# Database Backup and Restore (ArkTS)

#### When to Use

If an error occurs during the operation or storage, you can restore the database to the previous state and continue the operation.

If a database is tampered with, deleted, or powered off, the database may be unavailable due to data loss, data corruption, or dirty data. In this case, you can use the backup and restore capability to restore the database to the available state.

Both KV stores and RDB stores support database backup and restore. You can also delete KV store backups to release local storage space.

#### Backing Up, Restoring, and Deleting a KV Store

You can use **backup()** to back up a KV store, use **restore()** to restore a KV store, and use **deletebackup()** to delete a KV store backup file. For details about the APIs, see [Distributed KV Store](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-distributedkvstore).

1.  Create a KV store.
    
    (1) Create a **kvManager** instance.
    
    (2) Set database parameters.
    
    (3) Create a **kvStore** instance.
    
    // Import modules.
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
    const context = EntryAbility.getContext();
    
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
          // kvStoreType is distributedKVStore.KVStoreType.DEVICE\_COLLABORATION for a device KV store.
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
    
2.  Call **put()** to insert data to the KV store.
    
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
    
3.  Call **backup()** to back up the KV store.
    
    public Backup = (() => {
      Logger.info('Backup start');
      if (kvStore === undefined) {
        Logger.info('Backup: kvStore not initialized');
        return;
      }
      let backupFile = 'BK001';
      try {
        kvStore.backup(backupFile, (err) => {
          if (err) {
            Logger.error(\`Fail to backup data.code:${err.code},message:${err.message}\`);
          } else {
            Logger.info('Succeeded in backing up data.');
          }
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
    
4.  Call **delete()** to delete data to simulate unexpected deletion or data tampering.
    
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
    
5.  Call **restore()** to restore the KV store.
    
    public Restore = (() => {
      Logger.info('Restore start');
      if (kvStore === undefined) {
        Logger.info('Restore: kvStore not initialized');
        return;
      }
      let backupFile = 'BK001';
      try {
        kvStore.restore(backupFile, (err) => {
          if (err) {
            Logger.error(\`Fail to restore data. Code:${err.code},message:${err.message}\`);
          } else {
            Logger.info('Succeeded in restoring data.');
          }
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    })
    
6.  Call **deleteBackup()** to delete the backup file to release storage space.
    
    public DeleteBackup = (() => {
      Logger.info('DeleteBackup start');
      if (kvStore === undefined) {
        Logger.info('DeleteBackup: kvStore not initialized');
        return;
      }
      let backupFile = 'BK001';
      let files = \[backupFile\];
      try {
        kvStore.deleteBackup(files, (err: BusinessError, data: \[string, number\]\[\]) => {
          if (err) {
            Logger.error(\`Failed to delete Backup.code is ${err.code},message is ${err.message}\`);
          } else {
            Logger.info(\`Succeed in deleting Backup.data=${data}\`);
          }
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
      }
    })
    

#### Backing Up an RDB Store

A database backup can be used to quickly restore an RDB store in abnormal state.

Two backup modes are available: manual backup and automatic backup. Automatic backup is available only for system applications.

## Manual Backup

Call the [backup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore#backup) API to manually back up an RDB store.

Example:

import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit'
import { UIContext } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

/\* context indicates the application's context information, which is obtained by the caller. The following is for demonstration purposes only. \*/
const context = new UIContext().getHostContext() as common.UIAbilityContext;
let store: relationalStore.RdbStore | undefined = undefined;
const STORE\_CONFIG: relationalStore.StoreConfig = {
  name: 'RdbTest.db',
  securityLevel: relationalStore.SecurityLevel.S3
};
try {
  store = await relationalStore.getRdbStore(context, STORE\_CONFIG);
  await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)');
  hilog.info(DOMAIN, 'BackupAndRestore', 'Succeeded in getting RdbStore.');
} catch (e) {
  const err = e as BusinessError;
  hilog.error(DOMAIN, 'BackupAndRestore', \`Failed to get RdbStore. Code:${err.code},message:${err.message}\`);
}

if (!store) {
  return;
}

try {
  /\*\*
   \* Backup.db specifies the database backup file. By default, it is in the same directory as the RDB store.
   \* You can also specify an absolute path, for example, /data/storage/el2/database/Backup.db. The file path must exist and will not be automatically created.
   \*/
  await store.backup('Backup.db');
  hilog.info(DOMAIN, 'BackupAndRestore', \`Succeeded in backing up RdbStore.\`);
} catch (e) {
  const err = e as BusinessError;
  hilog.error(DOMAIN, 'BackupAndRestore', \`Failed to backup RdbStore. Code:${err.code}, message:${err.message}\`);
}

#### Rebuilding an RDB Store

If error 14800011 is displayed when an RDB store is created or used, an exception occurs in the database. You can delete the database and restore data.

You can set **allowRebuild** in [StoreConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore-i#storeconfig) to **true**, which allows the database to be automatically deleted when an exception occurs. The newly rebuilt RDB store is empty. You need to create tables and restore data from the database backup. For details about how to back up RDB store data, see [Backing Up an RDB Store](#backing-up-an-rdb-store). For details about how to restore RDB store data, see [Restoring RDB Store Data](#restoring-rdb-store-data).

If **allowRebuild** in **StoreConfig** is set to **true** before the database is abnormal, the database will be automatically deleted when an exception occurs.

If **allowRebuild** in **StoreConfig** is not set or is set to **false**, set **allowRebuild** to **true** and open the rebuilt RDB store.

Example:

let store: relationalStore.RdbStore | undefined = undefined;
/\* context indicates the application's context information, which is obtained by the caller. The following is for demonstration purposes only. \*/
const context = new UIContext().getHostContext() as common.UIAbilityContext;
try {
  const STORE\_CONFIG: relationalStore.StoreConfig = {
    name: 'RdbTest.db',
    securityLevel: relationalStore.SecurityLevel.S3,
    allowRebuild: true
  };
  store = await relationalStore.getRdbStore(context, STORE\_CONFIG);
  await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)');
  hilog.info(DOMAIN, 'BackupAndRestore', 'Succeeded in getting RdbStore.');
} catch (e) {
  const err = e as BusinessError;
  hilog.error(DOMAIN, 'BackupAndRestore', \`Failed to get RdbStore. Code:${err.code}, message:${err.message}\`);
}

#### Restoring RDB Store Data

If an RDB store is abnormal, you can restore it by using the database backup.

You can restore data from either the manual backup data or automatic backup data. The latter is available only for system applications.

## Restoring from Manual Backup Data

You can use **backup()** to [perform manual backup](#manual-backup) and use **restore()** to restore data from the manual backup data.

The following example contains only the code snippet for the restore process. The complete code must also contain the code for backing up data and rebuilding an RDB store.

1.  An error code is thrown to indicate a database exception.
    
    let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
    if (store != undefined) {
      (store as relationalStore.RdbStore).query(predicates, \['ID', 'NAME', 'AGE', 'SALARY', 'CODES'\])
        .then((result: relationalStore.ResultSet) => {
          let resultSet = result;
          try {
            /\* ...
               Logic for adding, deleting, and modifying data.
               ...
             \*/
            // Throw an exception.
            if (resultSet?.rowCount == -1) {
              resultSet?.isColumnNull(0);
            }
            // Calling other APIs such as resultSet.goToFirstRow() also throws exceptions.
            while (resultSet.goToNextRow()) {
              hilog.info(DOMAIN, 'BackupAndRestore', JSON.stringify(resultSet.getRow()));
            }
            resultSet.close();
          } catch (err) {
            if (err.code === 14800011) {
              // Perform step 2 (close result sets and then restore data).
            }
            hilog.info(DOMAIN, 'BackupAndRestore', JSON.stringify(err));
          }
        })
    }
    
2.  Close all opened result sets.
    
    let resultSets: relationalStore.ResultSet\[\] = \[\]
    // Call resultSet.close() to close all opened result sets.
    for (let resultSet of resultSets) {
      try {
        resultSet.close();
      } catch (e) {
        if (e.code !== 14800014) {
          hilog.info(DOMAIN, 'BackupAndRestore', \`Code:${e.code}, message:${e.message}\`);
        }
      }
    }
    
3.  Call **restore()** to restore data.
    
    let store: relationalStore.RdbStore | undefined = undefined;
    /\* context indicates the application's context information, which is obtained by the caller. The following is for demonstration purposes only. \*/
    const context = new UIContext().getHostContext() as common.UIAbilityContext;
    let STORE\_CONFIG: relationalStore.StoreConfig = {
      name: 'RdbTest.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      allowRebuild: true
    }
    try {
      /\*\*
       \* Backup.db specifies the database backup file. By default, it is in the same directory as the current database.
       \* If an absolute path is specified for the database backup file, for example, /data/storage/el2/database/Backup.db, pass in the absolute path.
       \*/
      let backupFilePath = context.databaseDir + '/rdb/Backup.db';
      const backupExist: boolean = await fileIo.access(backupFilePath);
      if (!backupExist) {
        hilog.info(DOMAIN, 'BackupAndRestore', 'Backup is not exist.');
        // Open the rebuilt RDB store and create tables.
        // Generate data.
        return;
      }
    } catch (e) {
      hilog.info(DOMAIN, 'BackupAndRestore', \`Code:${e.code}, message:${e.message}\`);
    }
    
    try {
      store = await relationalStore.getRdbStore(context, STORE\_CONFIG);
      // Call restore() to restore data.
      await store.restore('Backup.db');
      hilog.info(DOMAIN, 'BackupAndRestore', 'Restore from backup success.');
    } catch (e) {
      const err = e as BusinessError;
      hilog.error(DOMAIN, 'BackupAndRestore', \`Failed to get RdbStore. Code:${err.code}, message:${err.message}\`);
    }
