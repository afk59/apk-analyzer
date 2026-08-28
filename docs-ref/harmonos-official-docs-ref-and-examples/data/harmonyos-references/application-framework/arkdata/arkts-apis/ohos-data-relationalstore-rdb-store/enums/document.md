# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Ue17J4NgS3yD48JPG9i87Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=649FF71D6E3B51C92EFF028AD085B4135AD2CE32DF66E57BE1E11B7E393891CC)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### SecurityLevel

Enumerates the KV store security levels. Use the enum name rather than the enum value. You cannot change the security level of an RDB store from a higher level to a lower one.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/gYh8gB4_RYeUiMcPKyY79A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9C303CC0D399C2DE60CD78ECD3B6BCBDB9D0E91BA39FBDCE85F614C3E06E455)

To perform data sync operations, the RDB store security level must be lower than or equal to that of the peer device. For details, see [Access Control Mechanism in Cross-Device Sync](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sync-app-data-across-devices-overview#access-control-mechanism-in-cross-device-sync).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| S1 | 1 | The RDB store security level is low. If data leakage occurs, minor impact will be caused on the database. An example would be a graph store containing non-sensitive system data such as wallpapers. |
| S2 | 2 | The RDB store security level is medium. If data leakage occurs, moderate impact will be caused on the database. An example would be a graph store containing audio and video data created by users or call logs. |
| S3 | 3 | The RDB store security level is high. If data leakage occurs, major impact will be caused on the database. An example would be a graph store containing user fitness, health, and location data. |
| S4 | 4 | The RDB store security level is critical. If data leakage occurs, severe impact will be caused on the database. An example would be a graph store containing authentication credentials and financial data. |

#### EncryptionAlgo14+

Enumerates the encryption algorithms of the database. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AES\_256\_GCM | 0 | AES\_256\_GCM. |
| AES\_256\_CBC | 1 | AES\_256\_CBC. |
| PLAIN\_TEXT22+ | 2 | No encryption is required. |

#### HmacAlgo14+

Enumerates the HMAC algorithms for the database. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SHA1 | 0 | HMAC\_SHA1. |
| SHA256 | 1 | HMAC\_SHA256. |
| SHA512 | 2 | HMAC\_SHA512. |

#### KdfAlgo14+

Enumerates the PBKDF2 algorithms for the database. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| KDF\_SHA1 | 0 | PBKDF2\_HMAC\_SHA1. |
| KDF\_SHA256 | 1 | PBKDF2\_HMAC\_SHA256. |
| KDF\_SHA512 | 2 | PBKDF2\_HMAC\_SHA512. |

#### Tokenizer17+

Enumerates tokenizers that can be used for FTS. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE\_TOKENIZER | 0 | No tokenizer is used. |
| ICU\_TOKENIZER | 1 | The ICU tokenizer is used, which supports Chinese and multiple languages. If the ICU tokenizer is used, you can set the language to use, for example, **zh\_CN** for Chinese and **tr\_TR** for Turkish. For details about the supported languages, see [ICU tokenizer](https://gitcode.com/openharmony/third_party_icu/blob/master/icu4c/source/data/lang/en.txt). For details about the language abbreviations, see [locales](https://gitcode.com/openharmony/third_party_icu/tree/master/icu4c/source/data/locales). |
| CUSTOM\_TOKENIZER18+ | 2 | A custom tokenizer is used. Chinese (simplified and traditional), English, and Arabic numerals are supported. Compared with **ICU\_TOKENIZER**, **CUSTOM\_TOKENIZER** has advantages in tokenization accuracy and resident memory usage. The self-developed tokenizer supports two modes: default tokenization mode and short word tokenization mode (short\_words). You can use the cut\_mode parameter to specify the mode. If no mode is specified, the default mode is used. |

The table creation statement varies with the tokenizer in use.

**Example**:

For details about the definition of **this.context** in the sample code, see the application [context](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) of the stage model.

The following is an example of the table creation statement when **ICU\_TOKENIZER** is used:

import { relationalStore } from '@kit.ArkData'; // Import the relationalStore module.
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

// In this example, Ability is used to obtain an RdbStore instance in the stage model. You can use other implementations as required.
class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let store: relationalStore.RdbStore | undefined = undefined;
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "MyStore.db",
      securityLevel: relationalStore.SecurityLevel.S3,
      tokenizer: relationalStore.Tokenizer.ICU\_TOKENIZER
    };
    store = await relationalStore.getRdbStore(this.context, STORE\_CONFIG);

    const SQL\_CREATE\_TABLE = "CREATE VIRTUAL TABLE example USING fts4(name, content, tokenize=icu zh\_CN)";
    if (store != undefined) {
      (store as relationalStore.RdbStore).executeSql(SQL\_CREATE\_TABLE, (err) => {
        if (err) {
          console.error(\`ExecuteSql failed, code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('create virtual table done.');
      });
    }
  }
}

The following is an example of the table creation statement when **CUSTOM\_TOKENIZER** is used:

import { relationalStore } from '@kit.ArkData'; // Import the relationalStore module.
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

// In this example, Ability is used to obtain an RdbStore instance in the stage model. You can use other implementations as required.
class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let store: relationalStore.RdbStore | undefined = undefined;
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "MyStore.db",
      securityLevel: relationalStore.SecurityLevel.S3,
      tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER
    };
    store = await relationalStore.getRdbStore(this.context, STORE\_CONFIG);

    const SQL\_CREATE\_TABLE = "CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize='customtokenizer')";
    if (store != undefined) {
      (store as relationalStore.RdbStore).executeSql(SQL\_CREATE\_TABLE, (err) => {
        if (err) {
          console.error(\`ExecuteSql failed, code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('create virtual table done.');
      });
    }
  }
}

The following is an example of the table creation statement when **CUSTOM\_TOKENIZER** is used:

import { relationalStore } from '@kit.ArkData'; // Import the relationalStore module.
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('custom tokenizer example: window stage create begin.');
    let store: relationalStore.RdbStore | undefined = undefined;
    const storeConfig: relationalStore.StoreConfig = {
      name: "MyStore.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    let customType = relationalStore.Tokenizer.CUSTOM\_TOKENIZER;
    let customTypeSupported = relationalStore.isTokenizerSupported(customType);
    if (customTypeSupported) {
      storeConfig.tokenizer = customType;
    } else {
      console.info('custom tokenizer example: not support custom tokenizer.');
      return;
    }
    store = await relationalStore.getRdbStore(this.context, storeConfig);

    const sqlCreateTable =
      "CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize='customtokenizer cut\_mode short\_words')";
    if (store != undefined) {
      (store as relationalStore.RdbStore).executeSql(sqlCreateTable, (err) => {
        if (err) {
          console.error(\`custom tokenizer example: ExecuteSql failed, code is ${err.code},message is ${err.message}\`);
          return;
        }
        console.info('custom tokenizer example: create virtual table done.');
      });
    }
  }
}

#### AssetStatus10+

Enumerates the asset statuses. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ASSET\_NORMAL | 1 | The asset is in normal status. |
| ASSET\_INSERT | 2 | The asset is to be inserted to the cloud. |
| ASSET\_UPDATE | 3 | The asset is to be updated to the cloud. |
| ASSET\_DELETE | 4 | The asset is to be deleted from the cloud. |
| ASSET\_ABNORMAL | 5 | The asset is in abnormal status. |
| ASSET\_DOWNLOADING | 6 | The asset is being downloaded to a local device. |

#### SyncMode

Defines the database synchronization mode. Use the enum name rather than the enum value.

| Name | Value | Description |
| :-- | :-- | :-- |
| SYNC\_MODE\_PUSH | 0 | 
Data is pushed from a local device to a remote device.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| SYNC\_MODE\_PULL | 1 | 

Data is pulled from a remote device to a local device.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| SYNC\_MODE\_TIME\_FIRST10+ | 4 | 

Synchronize with the data with the latest modification time.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |
| SYNC\_MODE\_NATIVE\_FIRST10+ | 5 | 

Synchronize data from a local device to the cloud.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |
| SYNC\_MODE\_CLOUD\_FIRST10+ | 6 | 

Synchronize data from the cloud to a local device.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |

#### Origin11+

Enumerates the data sources. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

| Name | Value | Description |
| :-- | :-- | :-- |
| LOCAL | 0 | Local data. |
| CLOUD | 1 | Cloud data. |
| REMOTE | 2 | Remote device data. |

#### Field11+

Enumerates predicates used as query conditions. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

| Name | Value | Description |
| :-- | :-- | :-- |
| CURSOR\_FIELD | '#\_cursor' | Field name used for cursor-based search. |
| ORIGIN\_FIELD | '#\_origin' | Field name used to specify the data source in cursor-based search. |
| DELETED\_FLAG\_FIELD | '#\_deleted\_flag' | 
Whether the dirty data (data deleted from the cloud) is cleared from the local device. It fills in the result set returned upon the cursor-based search.

The value **true** means the dirty data is cleared; the value **false** means the opposite.

 |
| DATA\_STATUS\_FIELD12+ | '#\_data\_status' | Data status in the cursor-based search result set. The value **0** indicates normal data status; **1** indicates that data is retained after the account is logged out; **2** indicates that data is deleted from the cloud; **3** indicates that data is deleted after the account is logged out. |
| OWNER\_FIELD | '#\_cloud\_owner' | Party who shares the data. It fills in the result set returned when the owner of the shared data is searched. |
| PRIVILEGE\_FIELD | '#\_cloud\_privilege' | Operation permission on the shared data. It fills in the result set returned when the permission on the shared data is searched. |
| SHARING\_RESOURCE\_FIELD | '#\_sharing\_resource\_field' | Resource shared. It fills in the result set returned when the shared resource is searched. |

#### SubscribeType

Enumerates the subscription types. Use the enum name rather than the enum value.

| Name | Value | Description |
| :-- | :-- | :-- |
| SUBSCRIBE\_TYPE\_REMOTE | 0 | 
Subscribe to remote data changes.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| SUBSCRIBE\_TYPE\_CLOUD10+ | 1 | 

Subscribe to cloud data changes.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |
| SUBSCRIBE\_TYPE\_CLOUD\_DETAILS10+ | 2 | 

Subscribe to details of the cloud data change.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |
| SUBSCRIBE\_TYPE\_LOCAL\_DETAILS12+ | 3 | 

Subscribe to details of the local data change.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |

#### RebuildType12+

Enumerates the RDB store rebuild types. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The RDB store is not rebuilt. |
| REBUILT | 1 | The RDB store is rebuilt and creates an empty database. You need to create tables and restore data. |
| REPAIRED | 2 | The database is repaired and the undamaged data is restored. Currently, only the [vector store](../interfaces-others/document.md#storeconfig) supports this capability. |

#### ChangeType10+

Enumerates data change types. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DATA\_CHANGE | 0 | Data change. |
| ASSET\_CHANGE | 1 | Asset change. |

#### DistributedType10+

Enumerates the distributed database table types. Use the enum name rather than the enum value.

| Name | Value | Description |
| :-- | :-- | :-- |
| DISTRIBUTED\_DEVICE | 0 | 
Distributed database table synced between devices.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| DISTRIBUTED\_CLOUD | 1 | 

Distributed database table synced between a device and the cloud.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |

#### ConflictResolution10+

Enumerates the resolutions used when a conflict occurs during data insertion or modification. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ON\_CONFLICT\_NONE | 0 | No operation is performed. |
| ON\_CONFLICT\_ROLLBACK | 1 | Abort the SQL statement and roll back the current transaction. |
| ON\_CONFLICT\_ABORT | 2 | Abort the current SQL statement and revert any changes made by the current SQL statement. However, the changes made by the previous SQL statement in the same transaction are retained and the transaction remains active. |
| ON\_CONFLICT\_FAIL | 3 | Abort the current SQL statement. The **FAIL** resolution does not revert previous changes made by the failed SQL statement or end the transaction. |
| ON\_CONFLICT\_IGNORE | 4 | Skip the rows that contain constraint violations and continue to process the subsequent rows of the SQL statement. |
| ON\_CONFLICT\_REPLACE | 5 | Delete pre-existing rows that cause the constraint violation before inserting or updating the current row, and continue to execute the command normally. |

#### Progress10+

Enumerates the stages in the device-cloud sync progress. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SYNC\_BEGIN | 0 | The device-cloud sync starts. |
| SYNC\_IN\_PROGRESS | 1 | The device-cloud sync is in progress. |
| SYNC\_FINISH | 2 | The device-cloud sync is finished. |

#### ProgressCode10+

Enumerates the device-cloud sync states. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 0 | The device-cloud sync is successful. |
| UNKNOWN\_ERROR | 1 | An unknown error occurs during the device-cloud sync. |
| NETWORK\_ERROR | 2 | A network error occurs during the device-cloud sync. |
| CLOUD\_DISABLED | 3 | The cloud is unavailable. |
| LOCKED\_BY\_OTHERS | 4 | 
The device-cloud sync of another device is being performed.

The sync of the local device can be performed only when the cloud resources are available.

 |
| RECORD\_LIMIT\_EXCEEDED | 5 | The number of records or size of the data to be synced exceeds the maximum. The maximum value is configured on the cloud. |
| NO\_SPACE\_FOR\_ASSET | 6 | The remaining cloud space is less than the size of the data to be synced. |
| BLOCKED\_BY\_NETWORK\_STRATEGY12+ | 7 | The device-cloud sync is blocked due to the network strategy. |

#### TransactionType14+

Enumerates the types of transaction objects that can be created. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFERRED | 0 | Deferred transaction object. When a deferred transaction object is created, automatic commit is disabled and no transaction will start. A read or write transaction starts only when the first read or write operation is performed. |
| IMMEDIATE | 1 | Immediate transaction object. When an immediate transaction object is created, a write transaction starts. If there is any uncommitted write transaction, the transaction object cannot be created and error 14800024 is returned. |
| EXCLUSIVE | 2 | Exclusive transaction object. In WAL mode, the exclusive transaction object is the same as the immediate transaction object. In other log modes, this type of transaction can prevent the database from being read by other connections during the transaction. |

#### ColumnType18+

Enumerates the types of the column data. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NULL | 0 | NULL. |
| INTEGER | 1 | 
64-bit integer.

The column can hold 8-bit (including Boolean values), 16-bit, 32-bit, and 64-bit integers. If the 64-bit integer is greater than 2^53 or less than -2^53, use [getString](../interface-resultset/document.md#getstring) to convert the 64-bit integer to a string.

 |
| REAL | 2 | Floating-point number. |
| TEXT | 3 | String. |
| BLOB | 4 | Uint8Array. |
| ASSET | 5 | [Asset](../interfaces-others/document.md#asset10). |
| ASSETS | 6 | [Assets](../types/document.md#assets10). |
| FLOAT\_VECTOR | 7 | Float32Array. |
| UNLIMITED\_INT | 8 | BigInt. |
