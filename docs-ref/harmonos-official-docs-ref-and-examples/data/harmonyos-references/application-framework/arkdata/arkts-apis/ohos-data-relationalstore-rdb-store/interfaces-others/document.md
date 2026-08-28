# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/QD9JMYSgRgqX8F8OpH6q_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36F4AB106E89FBFB7C63CF5ECB536F2EA795F57DC542EA77E83A823776F07762)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### StoreConfig

Defines the RDB store configuration.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | 
Database file name, which is the unique identifier of the RDB store. Creating two databases with the same name in the same process is prohibited; otherwise, functions such as device-device sync, device-cloud sync, silent access, and key backup may malfunction.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| securityLevel | [SecurityLevel](../enums/document.md#securitylevel) | No | No | 

Security level of the RDB store.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| encrypt | boolean | No | Yes | 

Whether to encrypt the RDB store.

**true**: encrypt the RDB store.

**false** (default): not encrypt the RDB store.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| dataGroupId10+ | string | No | Yes | 

Application group ID. You should obtain it from AppGallery. Based on dataGroupId, data sharing between different processes of the same application is supported only in the input method and extension scenarios of third-party applications and that between different applications is supported only by system applications.

**Model restriction**: This parameter can be used only in the stage model.

This parameter is supported since API version 10. If **dataGroupId** is specified, the **RdbStore** instance will be created in the sandbox directory of the specified **dataGroupId**. However, the encrypted RDB store in this sandbox directory does not support multi-process access. If this parameter is left blank, the **RdbStore** instance will be created in the sandbox directory of the application by default.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| customDir11+ | string | No | Yes | 

Custom database path.

**Constraints**: The maximum length of the database path is 128 bytes. If the database path exceeds 128 bytes, the RDB store fails to be opened and an error is returned.

This parameter is supported since API version 11. The database is created in the following directory structure: **context.databaseDir** + **"/rdb/"** + **customDir**, where **context.databaseDir** indicates the path of the application sandbox, **"/rdb/"** indicates the RDB store created, and **customDir** indicates a user-defined path. If this parameter is left blank, the **RdbStore** instance will be created in the sandbox directory of the application by default. Since API version 18, if the **rootDir** parameter is also configured, the RDB store in the following directory will be opened or deleted: **rootDir** + "/" + **customDir** + "/" + **name**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| rootDir18+ | string | No | Yes | 

Root path of the database.

This parameter is supported since API version 18. The database in the **rootDir** + "/" + **customDir** directory will be opened or deleted. The database opened is read-only. Writing data to a read-only database will trigger error 801. If this parameter is set when you want to open or delete an RDB store, ensure that the database file exists in the corresponding path and the caller has the read permission. Otherwise, error 14800010 will be returned.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| autoCleanDirtyData11+ | boolean | No | Yes | 

Whether to automatically clear the dirty data (data that has been deleted from the cloud) from the local device. The value **true** means to clear the dirty data automatically; **false** means to clear the data manually.

Default value: **true**.

For a database with device-cloud synergy, this parameter can be used to set whether to automatically clear the data deleted from the cloud on the device. You can manually clear the data by calling [cleanDirtyData11+](../interface-rdbstore/document.md#cleandirtydata11).

This parameter is supported since API version 11.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

 |
| allowRebuild12+ | boolean | No | Yes | 

Whether to automatically delete the RDB store and create an empty table in the case of an exception.

**true**: delete the RDB store and create an empty table in the case of an exception.

**false** (default): not delete the RDB store in the case of an exception.

This parameter is supported since API version 12.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| isReadOnly12+ | boolean | No | Yes | 

Whether the RDB store is read-only.

**true**: The RDB store is read-only. Writing data to the RDB store will result in error code 801.

**false** (default): The RDB store is readable and writeable.

This parameter is supported since API version 12.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| pluginLibs12+ | Array<string> | No | Yes | 

Loads custom dynamic libraries. Multiple dynamic library names can be passed in the array. For details, see [Constraints and Examples of pluginLibs](#constraints-and-examples-of-pluginlibs).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| cryptoParam14+ | [CryptoParam](#cryptoparam14) | No | Yes | 

Custom encryption parameters.

If this parameter is left empty, the default encryption parameters are used. For details, see default values of [CryptoParam](#cryptoparam14).

This parameter is valid only when **encrypt** is set to **true** or the key is not empty.

This parameter is supported since API version 14.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| vector18+ | boolean | No | Yes | 

Whether the RDB store is a vector store. The value **true** means the RDB store is a vector store, and the value **false** means the opposite.

Default value: **false**.

The vector store is ideal for storing and managing high-dimensional vector data, while the RDB store is optimal for storing and processing structured data.

Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been closed.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| tokenizer17+ | [Tokenizer](../enums/document.md#tokenizer17) | No | Yes | 

Type of the tokenizer to be used for FTS.

If this parameter is left blank, English tokenization is supported if FTS does not support Chinese or multi-language tokenization.

If you want to use a custom tokenizer, you can configure it through the **pluginLibs** parameter. For details, see [Restrictions and Examples of pluginLibs](#constraints-and-examples-of-pluginlibs).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| persist18+ | boolean | No | Yes | 

Whether to persist an RDB store. The value **true** means to persist the RDB store; **false** means the opposite (using an in-memory database). The default value is **true**.

An in-memory database does not support encryption, backup, restore, cross-process access, and distributed capabilities, with the **securityLevel** property ignored.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |
| enableSemanticIndex20+ | boolean | No | Yes | 

Whether to enable the semantic index processing feature for the database. The value **true** means to enable the semantic index processing feature; **false** means the opposite. The default value is **false**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

 |

#### CryptoParam14+

Represents the configuration of database encryption parameters. This configuration is valid only when **encrypt** of **StoreConfig** is set to **true** or the key is not empty.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| encryptionKey | Uint8Array | No | No | 
Key used for database encryption and decryption.

If this parameter is not specified, the RDB store generates a key, saves the key, and uses the key to open the database file.

If the key is not required, you need to set the key to **0**.

 |
| iterationCount | number | No | Yes | 

Number of iterations of the PBKDF2 algorithm used in the RDB store. The value is an integer.

Default value: **10000**.

The value must be an integer greater than 0. If it is not an integer, the value is rounded down.

If this parameter is not specified or is set to **0**, the default value **10000** and the default encryption algorithm **AES\_256\_GCM** are used.

 |
| encryptionAlgo | [EncryptionAlgo](../enums/document.md#encryptionalgo14) | No | Yes | 

Algorithm used for database encryption and decryption.

Default value: **AES\_256\_GCM**.

 |
| hmacAlgo | [HmacAlgo](../enums/document.md#hmacalgo14) | No | Yes | 

HMAC algorithm used for database encryption and decryption.

Default value: **SHA256**.

 |
| kdfAlgo | [KdfAlgo](../enums/document.md#kdfalgo14) | No | Yes | 

PBKDF2 algorithm used for database encryption and decryption.

Default value: the same as the HMAC algorithm used.

 |
| cryptoPageSize | number | No | Yes | 

Page size used for database encryption and decryption, in bytes.

Default value: **1024**.

The value must be an integer within the range of 1,024 to 65,536 and must be 2n. If the specified value is not an integer, the value is rounded down.

 |

#### Asset10+

Represents the asset (such as a document, image, or video).

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Asset name. |
| uri | string | No | No | Asset URI, which is an absolute path in the system. |
| path | string | No | No | Path of an asset in the application sandbox. |
| createTime | string | No | No | Time when an asset is created. |
| modifyTime | string | No | No | Time when an asset is last modified. |
| size | string | No | No | Asset size. In the device-cloud sync mechanism, this field is one of the key bases for determining whether an asset is changed. Ensure that the storage format and value logic are consistent across the end-to-end link. It is recommended that all system nodes use the standard processing format (unit: byte; value: a non-negative integer) to avoid sync exceptions or misjudgment caused by format differences. |
| status | [AssetStatus](../enums/document.md#assetstatus10) | No | Yes | 
Asset status.

Default value: **ASSET\_NORMAL**.

 |

#### ChangeInfo10+

Defines a struct for the details about the device-cloud sync process.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| table | string | No | No | Name of the table with data changes. |
| type | [ChangeType](../enums/document.md#changetype10) | No | No | Type of the data changed, which can be data or asset. |
| inserted | Array<string> | Array<number> | No | No | Location where data is inserted. If the primary key of the table is of the string type, it is the value of the primary key. Otherwise, it is the row number of the inserted data. |
| updated | Array<string> | Array<number> | No | No | Location where data is updated. If the primary key of the table is of the string type, it is the value of the primary key. Otherwise, it is the row number of the updated data. |
| deleted | Array<string> | Array<number> | No | No | Location where data is deleted. If the primary key of the table is of the string type, it is the value of the primary key. Otherwise, it is the row number of the deleted data. |

#### DistributedConfig10+

Defines a struct for distributed configuration of a table.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| autoSync | boolean | No | No | The value **true** means both auto sync and manual sync are supported for the table; **false** means only manual sync is supported for the table. |
| asyncDownloadAsset18+ | boolean | No | Yes | 
Whether to download assets synchronously or asynchronously when device-cloud sync is being performed for the current RDB store. The value **true** means to use an asynchronous task to download assets after all data is downloaded; **false** means to download assets synchronously.

Default value: **false**.

 |
| enableCloud18+ | boolean | No | Yes | Whether to enable device-cloud sync for this RDB store. The value **true** means to enable device-cloud sync; **false** means the opposite. The default value is **true**. |

#### Statistic10+

Defines a struct for the device-cloud sync statistics of a database table.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| total | number | No | No | Total number of rows to be synced between the device and cloud in the database table. |
| successful | number | No | No | Number of rows that are successfully synced between the device and cloud in the database table. |
| failed | number | No | No | Number of rows that failed to be synced between the device and cloud in the database table. |
| remained | number | No | No | Number of rows that are not executed for device-cloud sync in the database table. |

#### TableDetails10+

Defines a struct for statistics of device-cloud upload and download tasks of a database table.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| upload | [Statistic](#statistic10) | No | No | Statistics of the device-cloud upload tasks. |
| download | [Statistic](#statistic10) | No | No | Statistics of the device-cloud download tasks. |

#### ProgressDetails10+

Defines a struct for statistics of the overall device-cloud sync (upload and download) tasks of an RDB store.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| schedule | [Progress](../enums/document.md#progress10) | No | No | Device-cloud sync process. |
| code | [ProgressCode](../enums/document.md#progresscode10) | No | No | Device-cloud sync state. |
| details | Record<string, [TableDetails](#tabledetails10)\> | No | No | 
Statistics of each table.

The key indicates the table name, and the value indicates the device-cloud sync statistics of the table.

 |

#### SqlExecutionInfo12+

Represents statistics about SQL statements executed by the database.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sql | Array<string> | No | No | SQL statements executed. If the value of [batchInsert](../interface-rdbstore/document.md#batchinsert) is too large, multiple SQL statements may be executed. |
| totalTime | number | No | No | Total time used to execute the SQL statements, in μs. |
| waitTime | number | No | No | Time used to obtain the handle, in μs. |
| prepareTime | number | No | No | Time used to get the SQL statements ready and bind parameters, in μs. |
| executeTime | number | No | No | Time used to execute the SQL statements, in μs. |

#### SqlInfo20+

Represents details about the SQL statement executed by the database.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sql | string | No | No | SQL statements to be executed. |
| args | Array<[ValueType](../types/document.md#valuetype)\> | No | No | Parameters in the SQL statements to be executed. |

#### ExceptionMessage20+

Represents an exception message about the SQL statement executed by the database.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | No | Error code returned by the executed SQL statement. For details about the values and meanings, see [SQLite Error Codes](https://www.sqlite.org/rescode.html). |
| message | string | No | No | Exception message returned by the executed SQL statement. |
| sql | string | No | No | SQL statement that reports the error. |

#### TransactionOptions14+

Represents the configuration of a transaction object.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| transactionType | [TransactionType](../enums/document.md#transactiontype14) | No | Yes | 
Transaction object type.

Default value: **DEFERRED**.

 |

#### Constraints and Examples of pluginLibs

**Constraints**

1\. The maximum number of dynamic library names is 16. If the number exceeds 16, the library fails to be opened and the error code 14800000 is returned.

2\. The dynamic libraries must be those in the sandbox directory or system directory of the application. If a dynamic library fails to be loaded, the RDB store cannot be opened and the error code 14800010 is returned.

3\. The dynamic library name must be a complete path that can be loaded by SQLite. The path is in the format of \[context.bundleCodeDir + "/libs/arm64/" + name of the .so file"\], in which **context.bundleCodeDir** is the application sandbox path, **libs** is a fixed directory, and **arm64** is the subdirectory determined by the system architecture. For example, if the system architecture is arm64-v8a, the subdirectory is arm64.

Example: \[context.bundleCodeDir+ "/libs/arm64/" + libtokenizer.so\]. If this parameter is left blank, dynamic libraries are not loaded by default.

4\. The dynamic library must contain all its dependencies to prevent the failure caused by the lack of dependencies.

Example: In an NDK project, **libtokenizer.so** is built using the default compilation parameters and depends on the C++ standard library. When the dynamic library is loaded, **libc++\_shared.so** is linked by mistake because the namespace is different from that during compilation. As a result, the **\_\_emutls\_get\_address** symbol cannot be found. To solve this problem, you need to statically link the C++ standard library during compilation. For details, see [NDK Project Building Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/build-with-ndk-overview).

The following is an example of using **pluginLibs** to load a custom tokenizer:

1\. Implement an FTS5 loadable tokenizer extension and compile it into a .so file. For details about the compilation, see [Building an NDK Project with CMake](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/build-with-ndk-cmake).

2\. Copy the generated .so file to the corresponding subdirectory in the **entry/libs/** directory of the project. If the subdirectory does not exist, create one. The subdirectory is determined by the system architecture. For example, put the file in the **entry/libs/arm64-v8a** or **entry/libs/armeabi-v7a** directory, respectively, if the system architecture is arm64-v8a or armeabi-v7a.

3\. Load the custom tokenizer.

import { relationalStore } from '@kit.ArkData'
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { fileIo as fs } from '@kit.CoreFileKit'

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let rdbStore: relationalStore.RdbStore | undefined = undefined;
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: "testTokenize.db",
      securityLevel: relationalStore.SecurityLevel.S1,
    };
    let bundleCodeDir = this.context.bundleCodeDir;
    // libdistributeddb\_extension.so is the name of the .so file compiled by the FTS5 loadable tokenizer extension.
    let soPath = bundleCodeDir + "/libs/arm64/libdistributeddb\_extension.so";
    let res = await fs.access(soPath);
    if (!res) {
      console.error("Dynamic library not accessible");
      return;
    }
    console.info("Dynamic library found and accessible");

    // Set pluginLibs to the path of the dynamic library extension to be loaded.
    STORE\_CONFIG.pluginLibs = \[soPath\];
    try {
      rdbStore = await relationalStore.getRdbStore(this.context, STORE\_CONFIG);
      // Use the custom tokenizer to create an FTS5 virtual table. Set the tokenize parameter to the actual tokenizer name.
      await rdbStore.executeSql("CREATE VIRTUAL TABLE IF NOT EXISTS pages USING fts5(title, keywords, body, tokenize=koowork\_tokenizer);");
      console.info("CREATE VIRTUAL TABLE OK");
      await rdbStore.executeSql("INSERT INTO pages(keywords, title, body) VALUES('Song', 'xxx', 'Today is Sunday');");
      console.info("INSERT VIRTUAL TABLE OK, body is 'Today is Sunday'");
      await rdbStore.executeSql("INSERT INTO pages(keywords, title, body) VALUES('Song', 'xxx', 'Tomorrow is Monday');");
      console.info("INSERT VIRTUAL TABLE OK, body is 'Tomorrow is Monday'");
      let resultSet = await rdbStore.querySql("select \* from pages where body match 'Monday';");
      while (resultSet.goToNextRow()) {
        console.info(\`query result success, match body:${resultSet.getString(resultSet.getColumnIndex("body"))}\`);
      }
      resultSet.close();
      await rdbStore.close();
    } catch (err) {
      console.error("RdbStore failed, err: code=" + err.code + " message=" + err.message);
    }
  }
}
