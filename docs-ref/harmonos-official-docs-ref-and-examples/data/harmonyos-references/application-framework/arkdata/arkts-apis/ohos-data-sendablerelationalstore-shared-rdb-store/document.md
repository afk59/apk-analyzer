# @ohos.data.sendableRelationalStore (Shared RDB Store)

The **sendableRelationalStore** module provides APIs for obtaining **ValuesBucket** of the sendable type from the query result set and transferring it between concurrent instances.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/MtNEwQ-SQYiqj7F9vhC70Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78870E957CCED22D144A0663031BE4730E92F8D332476DCCF46E1C34A9ECA379)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### When to Use

When [taskpool](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/taskpool-introduction) is used for multi-thread computing, data storage containers such as **ValuesBucket**, **Asset**, and **Assets** of the RDB store cannot be used for cross-thread transfer due to the restriction on data types.

This module provides conversion functions for converting the types between common data storage containers and data storage containers that can be passed across threads.

#### Modules to Import

import { sendableRelationalStore } from '@kit.ArkData';

#### sendableRelationalStore.toSendableValuesBucket

toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket

Converts a key-value (KV) pair that cannot be passed across threads into the data that can be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| valuesBucket | [NonSendableBucket](#nonsendablebucket) | Yes | Data that cannot be passed across threads. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ValuesBucket](#valuesbucket) | Data that can be passed across threads. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**Example**

const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const asset2: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const u8 = new Uint8Array(\[1, 2, 3\]);
const valuesBucket: sendableRelationalStore.NonSendableBucket = {
  age: 18,
  name: "hangman",
  salary: 100.5,
  passed: true,
  data1: asset1,
  blobType: u8,
  bigValue: BigInt("15822401018187971961171"),
  data2: \[asset1, asset2\]
};

const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);

#### sendableRelationalStore.fromSendableValuesBucket

fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket

Converts a KV pair that can be passed across threads into the data that cannot be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| valuesBucket | [ValuesBucket](#valuesbucket) | Yes | Data that can be passed across threads. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NonSendableBucket](#nonsendablebucket) | Data that cannot be passed across threads. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**Example**

const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const asset2: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const u8 = new Uint8Array(\[1, 2, 3\]);

const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket({
  age: 18,
  name: "hangman",
  salary: 100.5,
  passed: true,
  data1: asset1,
  blobType: u8,
  bigValue: BigInt("15822401018187971961171"),
  data2: \[asset1, asset2\]
});
const nonSendableBucket = sendableRelationalStore.fromSendableValuesBucket(sendableValuesBucket);

#### sendableRelationalStore.toSendableAsset

toSendableAsset(asset: NonSendableAsset): Asset

Converts the asset data that cannot be passed across threads into the data that can be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| asset | [NonSendableAsset](#nonsendableasset) | Yes | Asset data that cannot be passed across threads. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Asset](#asset) | Asset data that can be passed across threads. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**Example**

const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);

#### sendableRelationalStore.fromSendableAsset

fromSendableAsset(asset: Asset): NonSendableAsset

Converts the asset data that can be passed across threads into the data that cannot be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| asset | [Asset](#asset) | Yes | Asset data that can be passed across threads. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NonSendableAsset](#nonsendableasset) | Asset data that cannot be passed across threads. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [RDB Store Error Codes](../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**Example**

const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
const normalAsset = sendableRelationalStore.fromSendableAsset(sendableAsset);

#### sendableRelationalStore.fromSendableValues20+

fromSendableValues(values: collections.Array<ValueType>): NonSendableValues

Converts the array data that can be passed across threads into the data that cannot be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | collections.Array<[ValueType](../ohos-data-relationalstore-rdb-store/types/document.md#valuetype)\> | Yes | Array data that can be passed across threads. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NonSendableValues](#nonsendablevalues20) | Array data that cannot be passed across threads. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800000 | Inner error. |

**Example**

import { sendableRelationalStore } from '@kit.ArkData';
import { collections } from '@kit.ArkTS';
const array = new collections.Array<sendableRelationalStore.ValueType>();
array.push("a");
array.push("b");
array.push(1);
array.push(2);
const values = sendableRelationalStore.fromSendableValues(array);

#### sendableRelationalStore.toSendableValues20+

toSendableValues(values: NonSendableValues): collections.Array<ValueType>

Converts the array data that cannot be passed across threads into the data that can be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [NonSendableValues](#nonsendablevalues20) | Yes | Array data that cannot be passed across threads. |

**Return value**

| Type | Description |
| :-- | :-- |
| collections.Array<[ValueType](../ohos-data-relationalstore-rdb-store/types/document.md#valuetype)\> | Array data that can be passed across threads. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800000 | Inner error. |

**Example**

import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
const array: relationalStore.ValueType\[\] = \[\];
array.push(1);
array.push(2);
array.push("aaaaaa")
const values = sendableRelationalStore.toSendableValues(array);

#### Asset

Represents the asset (such as a document, image, or video). **Asset** inherits from [lang.ISendable](../../../arkts/arkts-apis/arkts-lang-arkts-base-capability/document.md#langisendable) and is used to implement cross-thread transfer of asset data. The asset data does not support **Datashare** APIs. Use [sendableRelationalStore.toSendableAsset](#sendablerelationalstoretosendableasset) to create an **Asset** instance.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Asset name. |
| uri | string | No | No | Asset URI, which is an absolute path in the system. |
| path | string | No | No | Application sandbox path of the asset. |
| createTime | string | No | No | Time when the asset was created. |
| modifyTime | string | No | No | Time when the asset was last modified. |
| size | string | No | No | Size of the asset. |
| status | number | No | Yes | Asset status. For details, see [relationalStore.AssetStatus](../ohos-data-relationalstore-rdb-store/enums/document.md#assetstatus10). The default value is **relationalStore.AssetStatus.ASSET\_NORMAL**. |

#### Assets

type Assets = collections.Array<Asset>

Represent an array of [Assets](#asset), which allows assets to be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| [collections.Array](../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-array/document.md)<[Asset](#asset)\> | Array of assets. |

#### ValueType

type ValueType = null | number | string | boolean | collections.Uint8Array | Asset | Assets | collections.Float32Array | bigint

Defines the types of the value in a KV pair. The type varies with the parameter function.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| null | The value is null. |
| number | The value is a number. |
| string | The value is a string. |
| boolean | The value is **true** or **false**. |
| [collections.Uint8Array](../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8array/document.md) | The value is a Uint8 array. |
| [Asset](#asset) | 
The value is an asset.

If the value type is **Asset**, the type in the SQL statement for creating a table must be **ASSET**.

 |
| [Assets](#assets) | 

The value is an array of assets.

If the value type is **Assets**, the type in the SQL statement for creating a table must be **ASSETS**.

 |
| [collections.Float32Array](../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-float32array/document.md) | 

The value is an array of 32-bit floating-point numbers.

If the field type is **collections.Float32Array**, the type in the SQL statement for creating a table must be **floatvector(128)**.

 |
| bigint | 

The value is an integer of any length.

If the value type is bigint, the type in the SQL statement for creating a table must be **UNLIMITED INT**. For details, see [Persisting RDB Store Data](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-persistence-by-rdb-store).

**NOTE**

The bigint type does not support value comparison and cannot be used with the following predicates: **between**, **notBetween**, **greaterThan**, **lessThan**, **greaterThanOrEqualTo**, **lessThanOrEqualTo**, **orderByAsc**, and **orderByDesc**

To write a value of bigint type, use **BigInt()** or add **n** to the end of the value, for example,'let data = BigInt(1234)' or 'let data = 1234n'.

If data of the number type is written to a bigint field, the type of the return value obtained (queried) is number but not bigint.

 |

#### ValuesBucket

type ValuesBucket = collections.Map<string, ValueType>

Represents the KV pair of the [ValueType](#valuetype) data that can be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| [collections.Map](../../../arkts/arkts-apis/arkts-collections-arkts-collections/class-map/document.md)<string, [ValueType](#valuetype)\> | KV pair that can be passed across threads. The key must be a string, and the value is of the **ValueType** type. |

#### NonSendableBucket

type NonSendableBucket = relationalStore.ValuesBucket

Represents the KV pair that cannot be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| [relationalStore.ValuesBucket](../ohos-data-relationalstore-rdb-store/types/document.md#valuesbucket) | KV pair that cannot be passed across threads. |

#### NonSendableValues20+

type NonSendableValues = Array<relationalStore.ValueType>

Represents the [ValueType](../ohos-data-relationalstore-rdb-store/types/document.md#valuetype) array that cannot be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| Array<[relationalStore.ValueType](../ohos-data-relationalstore-rdb-store/types/document.md#valuetype)\> | Array that cannot be passed across threads. The value type is **ValueType**. |

#### NonSendableAsset

type NonSendableAsset = relationalStore.Asset

Represents the asset (such as a document, image, or video) that cannot be passed across threads.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| [relationalStore.Asset](../ohos-data-relationalstore-rdb-store/interfaces-others/document.md#asset10) | Asset that cannot be passed across threads. |

#### Example of Cross-Thread Data Passing

When invoking TaskPool for data insertion, the main thread calls the **toSendableValuesBucket** method to convert data into a cross-thread transferable type, which is then passed to TaskPool for processing.

When invoking TaskPool for data query operations, call the **getSendableRow** method of **ResultSet** to obtain cross-thread transferable data rows, which are then returned to the main thread. In the main thread, invoke the **fromSendableValuesBucket** method to convert these rows into the standard **ValuesBucket** format for subsequent processing.

// Index.ets
import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
import { taskpool } from '@kit.ArkTS';

@Concurrent
async function insert(context: Context, dataItem: sendableRelationalStore.ValuesBucket) {
  const CONFIG: relationalStore.StoreConfig = {
    name: "Store.db",
    securityLevel: relationalStore.SecurityLevel.S3,
  };

  let store = await relationalStore.getRdbStore(context, CONFIG);
  console.info(\`Get store successfully!\`);

  const CREATE\_TABLE\_SQL = "CREATE TABLE IF NOT EXISTS test (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "name TEXT NOT NULL, " +
    "age INTEGER, " +
    "salary REAL, " +
    "blobType BLOB)";
  await store.executeSql(CREATE\_TABLE\_SQL);
  console.info(\`Create table test successfully!\`);

  // Insert data.
  const rowId = await store.insertSync("test", dataItem);
  await store.close();
  return rowId;
}

@Concurrent
async function queryByName(context: Context, name: string) {
  const CONFIG: relationalStore.StoreConfig = {
    name: "Store.db",
    securityLevel: relationalStore.SecurityLevel.S3,
  };

  let store = await relationalStore.getRdbStore(context, CONFIG);
  console.info(\`Get store successfully!\`);

  const predicates = new relationalStore.RdbPredicates("test");
  predicates.equalTo("name", name);

  const resultSet = await store.query(predicates);
  if (resultSet.rowCount > 0 && resultSet.goToFirstRow()) {
    // Obtain the cross-thread transferable ValuesBucket to return the query result.
    return resultSet.getSendableRow();
  }
  return null;
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(async () => {
          let context: Context = this.getUIContext().getHostContext() as Context;

          const item: relationalStore.ValuesBucket = {
            name: "zhangsan",
            age: 20,
            salary: 5000
          }
          // Call toSendableValuesBucket to convert the data type for cross-thread passing.
          const sendableItem = sendableRelationalStore.toSendableValuesBucket(item);
          const insertRowId = await taskpool.execute(insert, context, sendableItem) as number;
          console.info(\`Insert data success, row id is: ${insertRowId}\`);

          const rowData = await taskpool.execute(queryByName, context, "zhangsan");
          if (rowData) {
            const row =
              sendableRelationalStore.fromSendableValuesBucket(rowData as sendableRelationalStore.ValuesBucket);
            console.info(\`Query success, name is ${row\['name'\]}, age is ${row\['age'\]}.\`);
          } else {
            console.error(\`Query failed.\`)
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
