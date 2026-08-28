# @ohos.data.rdb (RDB Store)

The relational database (RDB) manages data based on relational models. With the underlying SQLite database, the RDB provides a complete mechanism for managing local databases. To satisfy different needs in complicated scenarios, the RDB offers a series of methods for performing operations such as adding, deleting, modifying, and querying data, and supports direct execution of SQL statements. The worker threads are not supported.

This module provides the following RDB-related functions:

-   [RdbPredicates](#rdbpredicates): provides APIs for creating predicates. The predicates represent the properties, characteristics, or relationships between data entities in an RDB store and are used to define data operation conditions.
-   [RdbStore](#rdbstore): provides APIs for managing data in an RDB store.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/kNsCqgOkT_iSLeTtG0Ejpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0AF2224A825E3EB699C9755234919FFA96902DB5880FDAB6BBC7CD5BBBED2BC)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module are no longer maintained since API version 9. You are advised to use [@ohos.data.relationalStore](../../ohos-data-relationalstore-rdb-store/module-description/document.md).
    

#### Modules to Import

import data\_rdb from '@ohos.data.rdb';

#### data\_rdb.getRdbStore

getRdbStore(context: Context, config: StoreConfig, version: number, callback: AsyncCallback<RdbStore>): void

Obtains an RDB store. This API uses an asynchronous callback to return the result. You can set parameters for the RDB store based on service requirements and call APIs to perform data operations.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

 |
| config | [StoreConfig](#storeconfig) | Yes | Configuration of the RDB store. |
| version | number | Yes | 

RDB store version.

Currently, automatic RDB upgrades and downgrades performed based on **version** is not supported.

 |
| callback | AsyncCallback<[RdbStore](#rdbstore)\> | Yes | Callback used to return the RDB store obtained. |

**Example**

FA model:

import featureAbility from '@ohos.ability.featureAbility';
import relationalStore from '@ohos.data.relationalStore';
import window from '@ohos.window';
import { BusinessError } from '@ohos.base';

const STORE\_CONFIG: data\_rdb.StoreConfig = { name: "RdbTest.db"}
data\_rdb.getRdbStore(this.context, STORE\_CONFIG, 1, (err, rdbStore) => {
  if (err) {
    console.info("Get RdbStore failed, err: " + err)
    return
  }
  console.log("Get RdbStore successfully.")
})

Stage model:

import UIAbility from '@ohos.app.ability.UIAbility';
import { BusinessError } from "@ohos.base";
import window from '@ohos.window';

const STORE\_CONFIG: data\_rdb.StoreConfig = { name: "RdbTest.db"}
class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage){
    data\_rdb.getRdbStore(this.context, STORE\_CONFIG, 1, (err: BusinessError, rdbStore: data\_rdb.RdbStore) => {
      if (err) {
        console.info("Get RdbStore failed, err: " + err)
        return
      }
      console.log("Get RdbStore successfully.")
    })
  }
}

#### data\_rdb.getRdbStore

getRdbStore(context: Context, config: StoreConfig, version: number): Promise<RdbStore>

Obtains an RDB store. This API uses a promise to return the result. You can set parameters for the RDB store based on service requirements and call APIs to perform data operations.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

 |
| config | [StoreConfig](#storeconfig) | Yes | Configuration of the RDB store. |
| version | number | Yes | 

RDB store version.

Currently, automatic RDB upgrades and downgrades performed based on **version** is not supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RdbStore](#rdbstore)\> | Promise used to return the **RdbStore** object. |

**Example**

FA model:

import featureAbility from '@ohos.ability.featureAbility';

const STORE\_CONFIG: data\_rdb.StoreConfig = { name: "RdbTest.db"}
let promise = data\_rdb.getRdbStore(this.context, STORE\_CONFIG, 1);
promise.then(async (rdbStore) => {
  console.log("Get RdbStore successfully.")
}).catch((err: BusinessError) => {
  console.log("Get RdbStore failed, err: " + err)
})

Stage model:

import UIAbility from '@ohos.app.ability.UIAbility';
import { BusinessError } from "@ohos.base";
import window from '@ohos.window';

const STORE\_CONFIG: data\_rdb.StoreConfig = { name: "RdbTest.db"}
class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage){
    context = this.context
  }
}

// Call getRdbStore.
let promise = data\_rdb.getRdbStore(this.context, STORE\_CONFIG, 1);
promise.then(async (rdbStore: data\_rdb.RdbStore) => {
  console.log("Get RdbStore successfully.")
}).catch((err: BusinessError) => {
  console.log("Get RdbStore failed, err: " + err)
})

#### data\_rdb.deleteRdbStore

deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void

Deletes an RDB store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

 |
| name | string | Yes | Name of the RDB store to delete. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

FA model:

import featureAbility from '@ohos.ability.featureAbility';

data\_rdb.deleteRdbStore(this.context, "RdbTest.db", (err) => {
  if (err) {
    console.info("Delete RdbStore failed, err: " + err)
    return
  }
  console.log("Delete RdbStore successfully.")
})

Stage model:

import UIAbility from '@ohos.app.ability.UIAbility';
import window from '@ohos.window';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage){
    context = this.context
  }
}

// Call deleteRdbStore.
data\_rdb.deleteRdbStore(this.context, "RdbTest.db", (err) => {
  if (err) {
    console.info("Delete RdbStore failed, err: " + err)
    return
  }
  console.log("Delete RdbStore successfully.")
})

#### data\_rdb.deleteRdbStore

deleteRdbStore(context: Context, name: string): Promise<void>

Deletes an RDB store. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

 |
| name | string | Yes | Name of the RDB store to delete. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

FA model:

import featureAbility from '@ohos.ability.featureAbility';

let promise = data\_rdb.deleteRdbStore(this.context, "RdbTest.db")
promise.then(() => {
  console.log("Delete RdbStore successfully.")
}).catch((err: BusinessError) => {
  console.info("Delete RdbStore failed, err: " + err)
})

Stage model:

import UIAbility from '@ohos.app.ability.UIAbility';
import { BusinessError } from "@ohos.base";
import window from '@ohos.window';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage){
    context = this.context
  }
}

// Call deleteRdbStore.
let promise = data\_rdb.deleteRdbStore(this.context, "RdbTest.db")
promise.then(()=>{
  console.log("Delete RdbStore successfully.")
}).catch((err: BusinessError) => {
  console.info("Delete RdbStore failed, err: " + err)
})

#### ValueType

type ValueType = number | string | boolean

Defines the data types allowed.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| number | Number. |
| string | String. |
| boolean | Boolean. |

#### ValuesBucket

type ValuesBucket = { \[key: string\]: ValueType | Uint8Array | null }

Defines the types of the key and value in a KV pair.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Key Type | Value Type |
| :-- | :-- |
| string | [ValueType](#valuetype)| Uint8Array | null |

#### SyncMode8+

Defines the database sync mode.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SYNC\_MODE\_PUSH | 0 | Data is pushed from a local device to a remote device. |
| SYNC\_MODE\_PULL | 1 | Data is pulled from a remote device to a local device. |

#### SubscribeType8+

Defines the subscription type.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SUBSCRIBE\_TYPE\_REMOTE | 0 | Subscribe to remote data changes. |

#### StoreConfig

Defines the RDB store configuration.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Database file name. |

#### RdbPredicates

Defines predicates for an RDB store. This class determines whether the conditional expression for the RDB store is true or false.

#### \[h2\]constructor

constructor(name: string)

A constructor used to create an **RdbPredicates** object.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Database table name. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")

#### \[h2\]inDevices8+

inDevices(devices: Array<string>): RdbPredicates

Creates an **RdbPredicates** object to specify the remote devices to connect on the network during distributed database sync.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/-yluPlUvTbKKEqVaSpjIwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC11CB00501BFF777AEFDE288C43E11E8C88EB99D3823D191BF5A1FC13D8A934)

The value of **devices** can be obtained by using deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| devices | Array<string> | Yes | IDs of the remote devices in the same network. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: deviceManager.DeviceManager;
let deviceIds: Array<string> = \[\];
let devices: Array<string> = \[\];

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  devices = dmInstance.getTrustedDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds\[i\] = devices\[i\].deviceId;
  }
})

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE");
predicates.inDevices(deviceIds);
                                  
let predicates = new data\_rdb.RdbPredicates("EMPLOYEE");
predicates.inDevices(deviceIds);

#### \[h2\]inAllDevices8+

inAllDevices(): RdbPredicates

Creates an **RdbPredicates** object to specify all remote devices on the network to connect during distributed database sync.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.inAllDevices()

#### \[h2\]equalTo

equalTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "lisi")

#### \[h2\]notEqualTo

notEqualTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are not equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.notEqualTo("NAME", "lisi")

#### \[h2\]beginWrap

beginWrap(): RdbPredicates

Creates an **RdbPredicates** object to add a left parenthesis.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap()

#### \[h2\]endWrap

endWrap(): RdbPredicates

Creates an **RdbPredicates** object to add a right parenthesis.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap()

#### \[h2\]or

or(): RdbPredicates

Creates an **RdbPredicates** object to add the OR condition.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
    .or()
    .equalTo("NAME", "Rose")

#### \[h2\]and

and(): RdbPredicates

Creates an **RdbPredicates** object to add the AND condition.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
    .and()
    .equalTo("SALARY", 200.5)

#### \[h2\]contains

contains(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that contain the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.contains("NAME", "os")

#### \[h2\]beginsWith

beginsWith(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that start with the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.beginsWith("NAME", "os")

#### \[h2\]endsWith

endsWith(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that end with the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.endsWith("NAME", "se")

#### \[h2\]isNull

isNull(field: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are **null**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.isNull("NAME")

#### \[h2\]isNotNull

isNotNull(field: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are not **null**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **Error Code** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.isNotNull("NAME")

#### \[h2\]like

like(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are similar to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.like("NAME", "%os%")

#### \[h2\]glob

glob(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that match the given string.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | 
Value to match.

Wildcards are supported. An asterisk (\*) indicates zero, one, or multiple digits or characters, and a question mark (?) indicates a single digit or character.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.glob("NAME", "?h\*g")

#### \[h2\]between

between(field: string, low: ValueType, high: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are within the specified range.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| low | [ValueType](#valuetype) | Yes | Minimum value of the range to set. |
| high | [ValueType](#valuetype) | Yes | Maximum value of the range to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.between("AGE", 10, 50)

#### \[h2\]notBetween

notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are out of the specified range.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| low | [ValueType](#valuetype) | Yes | Minimum value of the range to set. |
| high | [ValueType](#valuetype) | Yes | Maximum value of the range to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.notBetween("AGE", 10, 50)

#### \[h2\]greaterThan

greaterThan(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are greater than the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.greaterThan("AGE", 18)

#### \[h2\]lessThan

lessThan(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are less than the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.lessThan("AGE", 20)

#### \[h2\]greaterThanOrEqualTo

greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are greater than or equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.greaterThanOrEqualTo("AGE", 18)

#### \[h2\]lessThanOrEqualTo

lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are less than or equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.lessThanOrEqualTo("AGE", 20)

#### \[h2\]orderByAsc

orderByAsc(field: string): RdbPredicates

Creates an **RdbPredicates** object to sort the records in the specified column in ascending order.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.orderByAsc("NAME")

#### \[h2\]orderByDesc

orderByDesc(field: string): RdbPredicates

Creates an **RdbPredicates** object to sort the records in the specified column in descending order.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.orderByDesc("AGE")

#### \[h2\]distinct

distinct(): RdbPredicates

Creates an **RdbPredicates** object to filter out duplicate records.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose").distinct()

#### \[h2\]limitAs

limitAs(value: number): RdbPredicates

Creates an **RdbPredicates** object to limit the number of records.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Maximum number of records. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose").limitAs(3)

#### \[h2\]offsetAs

offsetAs(rowOffset: number): RdbPredicates

Creates an **RdbPredicates** object to specify the start position of the returned result. This API must be used together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in **\-1** in **limitAs**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rowOffset | number | Yes | Start position, which is a positive integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose").limitAs(-1).offsetAs(3)

#### \[h2\]groupBy

groupBy(fields: Array<string>): RdbPredicates

Creates an **RdbPredicates** object to group the query results based on the specified columns.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fields | Array<string> | Yes | Names of columns to group. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.groupBy(\["AGE", "NAME"\])

#### \[h2\]indexedBy

indexedBy(field: string): RdbPredicates

Creates an **RdbPredicates** object to specify the index column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Name of the index column. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.indexedBy("SALARY\_INDEX")

#### \[h2\]in

in(field: string, value: Array<ValueType>): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are within the specified range.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | Array<[ValueType](#valuetype)\> | Yes | Array of **ValueType**s to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.in("AGE", \[18, 20\])

#### \[h2\]notIn

notIn(field: string, value: Array<ValueType>): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are out of the specified range.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | Array<[ValueType](#valuetype)\> | Yes | Array of **ValueType**s to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.notIn("NAME", \["Lisa", "Rose"\])

#### RdbStore

Provides APIs for managing data in an RDB store.

Before using the APIs of this class, use [executeSql](#executesql8) to initialize the database table structure and related data.

#### \[h2\]insert

insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>):void

Inserts a row of data into a table. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](#valuesbucket) | Yes | Row of data to insert. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisi";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

rdbStore.insert("EMPLOYEE", valueBucket, (status: number, rowId: number) => {
  if (status) {
    console.log("Insert is failed");
    return;
  }
  console.log("Insert is successful, rowId = " + rowId);
})

#### \[h2\]insert

insert(table: string, values: ValuesBucket):Promise<number>

Inserts a row of data into a table. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | [ValuesBucket](#valuesbucket) | Yes | Row of data to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the row ID will be returned. Otherwise, **\-1** will be returned. |

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisi";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);
const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

let promise: void = rdbStore.insert("EMPLOYEE", valueBucket)
promise.then((rowId: BusinessError) => {
  console.log("Insert is successful, rowId = " + rowId);
}).catch((status: number) => {
  console.log("Insert is failed");
})

#### \[h2\]batchInsert

batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>):void

Inserts a batch of data into a table. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](#valuesbucket)\> | Yes | An array of data to insert. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
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
const valueBucket1: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
const valueBucket2: ValuesBucket = {
  key1: value5,
  key2: value6,
  key3: value7,
  key4: value8,
};
const valueBucket3: ValuesBucket = {
  key1: value9,
  key2: value10,
  key3: value11,
  key4: value12,
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
rdbStore.batchInsert("EMPLOYEE", valueBuckets, (status: number, insertNum: number) => {
  if (status) {
    console.log("batchInsert is failed, status = " + status);
    return;
  }
  console.log("batchInsert is successful, the number of values that were inserted = " + insertNum);
})

#### \[h2\]batchInsert

batchInsert(table: string, values: Array<ValuesBucket>):Promise<number>

Inserts a batch of data into a table. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| table | string | Yes | Name of the target table. |
| values | Array<[ValuesBucket](#valuesbucket)\> | Yes | An array of data to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the number of inserted data records is returned. Otherwise, **\-1** is returned. |

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
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
const valueBucket1: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
const valueBucket2: ValuesBucket = {
  key1: value5,
  key2: value6,
  key3: value7,
  key4: value8,
};
const valueBucket3: ValuesBucket = {
  key1: value9,
  key2: value10,
  key3: value11,
  key4: value12,
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
let promise: void = rdbStore.batchInsert("EMPLOYEE", valueBuckets);
promise.then((insertNum: number) => {
  console.log("batchInsert is successful, the number of values that were inserted = " + insertNum);
}).catch((status: number) => {
  console.log("batchInsert is failed, status = " + status);
})

#### \[h2\]update

update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>):void

Updates data in the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | Update conditions specified by the **RdbPredicates** object. |
| callback | AsyncCallback<number> | Yes | Callback invoked to return the number of rows updated. |

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
rdbStore.update(valueBucket, predicates, (err: BusinessError, rows: number) => {
  if (err) {
    console.info("Updated failed, err: " + err)
    return
  }
  console.log("Updated row count: " + rows)
})

#### \[h2\]update

update(values: ValuesBucket, predicates: RdbPredicates):Promise<number>

Updates data based on the specified **RdbPredicates** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | [ValuesBucket](#valuesbucket) | Yes | Rows of data to update in the RDB store. The key-value pair is associated with the column name in the target table. |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | Update conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of rows updated. |

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3, 4, 5\]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
let promise: void = rdbStore.update(valueBucket, predicates)
promise.then(async (rows: number) => {
  console.log("Updated row count: " + rows)
}).catch((err: BusinessError) => {
  console.info("Updated failed, err: " + err)
})

#### \[h2\]delete

delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | Deletion conditions specified by the **RdbPredicates** object. |
| callback | AsyncCallback<number> | Yes | Callback used to return the number of rows deleted. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
rdbStore.delete(predicates, (err: BusinessError, rows: number) => {
  if (err) {
    console.info("Delete failed, err: " + err)
    return
  }
  console.log("Delete rows: " + rows)
})

#### \[h2\]delete

delete(predicates: RdbPredicates):Promise<number>

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | Deletion conditions specified by the **RdbPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of rows deleted. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
let promise: void = rdbStore.delete(predicates)
promise.then((rows: number) => {
  console.log("Delete rows: " + rows)
}).catch((err: BusinessError) => {
  console.info("Delete failed, err: " + err)
})

#### \[h2\]query

query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void

Queries data from the RDB store based on specified conditions. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | Yes | Columns to query. If this parameter is not specified, the query applies to all columns. |
| callback | AsyncCallback<[ResultSet](../data-rdb/resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose")
rdbStore.query(predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\], (err: BusinessError, resultSet: void) => {
  if (err) {
    console.info("Query failed, err: " + err)
    return
  }
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
})

#### \[h2\]query

query(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

Queries data from the RDB store based on specified conditions. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | Query conditions specified by the **RdbPredicates** object. |
| columns | Array<string> | No | Columns to query. If this parameter is not specified, the query applies to all columns. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResultSet](../data-rdb/resultset/document.md)\> | Promise used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Example**

let predicates = new data\_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose")
let promise: void = rdbStore.query(predicates, \["ID", "NAME", "AGE", "SALARY", "CODES"\])
promise.then((resultSet: void) => {
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
}).catch((err: BusinessError) => {
  console.info("Query failed, err: " + err)
})

#### \[h2\]querySql8+

querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>):void

Queries data using the specified SQL statement. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](#valuetype)\> | Yes | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, the value of this parameter must be an empty array. |
| callback | AsyncCallback<[ResultSet](../data-rdb/resultset/document.md)\> | Yes | Callback used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Example**

rdbStore.querySql("SELECT \* FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = ?", \['sanguo'\], (err: BusinessError, resultSet: void) => {
  if (err) {
    console.info("Query failed, err: " + err)
    return
  }
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
})

#### \[h2\]querySql8+

querySql(sql: string, bindArgs?: Array<ValueType>):Promise<ResultSet>

Queries data using the specified SQL statement. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResultSet](../data-rdb/resultset/document.md)\> | Promise used to return the result. If the operation is successful, a **ResultSet** object will be returned. |

**Example**

let promise: void = rdbStore.querySql("SELECT \* FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'")
promise.then((resultSet: void) => {
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
}).catch((err: BusinessError) => {
  console.info("Query failed, err: " + err)
})

#### \[h2\]executeSql8+

executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>):void

Executes an SQL statement that contains specified arguments but returns no value. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](#valuetype)\> | Yes | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, the value of this parameter must be an empty array. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

const SQL\_DELETE\_TABLE = "DELETE FROM test WHERE name = ?"
rdbStore.executeSql(SQL\_DELETE\_TABLE, \['zhangsan'\], (err: BusinessError) => {
  if (err) {
    console.info("ExecuteSql failed, err: " + err)
    return
  }
  console.info('Delete table done.')
})

#### \[h2\]executeSql8+

executeSql(sql: string, bindArgs?: Array<ValueType>):Promise<void>

Executes an SQL statement that contains specified arguments but returns no value. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sql | string | Yes | SQL statement to run. |
| bindArgs | Array<[ValueType](#valuetype)\> | No | Arguments in the SQL statement. The value corresponds to the placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

const SQL\_DELETE\_TABLE = "DELETE FROM test WHERE name = 'zhangsan'"
let promise = rdbStore.executeSql(SQL\_DELETE\_TABLE)
promise.then(() => {
  console.info('Delete table done.')
}).catch((err: BusinessError) => {
  console.info("ExecuteSql failed, err: " + err)
})

#### \[h2\]beginTransaction8+

beginTransaction():void

Starts the transaction before executing an SQL statement.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Example**

import featureAbility from '@ohos.ability.featureAbility';
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "blobType";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

data\_rdb.getRdbStore(this.context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
  rdbStore.beginTransaction()
  await rdbStore.insert("test", valueBucket)
  rdbStore.commit()
})

#### \[h2\]commit8+

commit():void

Commits the executed SQL statements.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';
import featureAbility from '@ohos.ability.featureAbility';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "blobType";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

data\_rdb.getRdbStore(this.context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
  rdbStore.beginTransaction()
  await rdbStore.insert("test", valueBucket)
  rdbStore.commit()
})

#### \[h2\]rollBack8+

rollBack():void

Rolls back the SQL statements that have been executed.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Example**

import { ValuesBucket } from '@ohos.data.ValuesBucket';
import featureAbility from '@ohos.ability.featureAbility';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "blobType";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array(\[1, 2, 3\]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

const STORE\_CONFIG = { name: "RdbTest.db"}
data\_rdb.getRdbStore(this,context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
  try {
    rdbStore.beginTransaction()
    await rdbStore.insert("test", valueBucket)
    rdbStore.commit()
  } catch (e) {
    rdbStore.rollBack()
  }
})

#### \[h2\]setDistributedTables8+

setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void

Sets distributed tables. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tables | Array<string> | Yes | Names of the distributed tables to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

rdbStore.setDistributedTables(\["EMPLOYEE"\], (err: BusinessError) => {
  if (err) {
    console.info('SetDistributedTables failed, err: ' + err)
    return
  }
  console.info('SetDistributedTables successfully.')
})

#### \[h2\]setDistributedTables8+

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

**Example**

let promise: void = rdbStore.setDistributedTables(\["EMPLOYEE"\])
promise.then(() => {
  console.info("SetDistributedTables successfully.")
}).catch((err: BusinessError) => {
  console.info("SetDistributedTables failed, err: " + err)
})

#### \[h2\]obtainDistributedTableName8+

obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void

Obtains the distributed table name of a remote device based on the local table name of the device. The distributed table name is required when the RDB store of a remote device is queried. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/oZtm1NRvS1OVDvzuHCha6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F72BF0BED32145E7276A0512AAB5842F68F47BCA23D6D4BC44104C06B170A52E)

The value of **device** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| device | string | Yes | ID of the remote device. |
| table | string | Yes | Local table name of the remote device. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation succeeds, the distributed table name of the remote device is returned. |

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  let deviceId: Array<string> = devices\[0\].deviceId;
})

rdbStore.obtainDistributedTableName(deviceId, "EMPLOYEE", (err: BusinessError, tableName: String) {
  if (err) {
    console.info('ObtainDistributedTableName failed, err: ' + err)
    return
  }
  console.info('ObtainDistributedTableName successfully, tableName=.' + tableName)
})

#### \[h2\]obtainDistributedTableName8+

obtainDistributedTableName(device: string, table: string): Promise<string>

Obtains the distributed table name of a remote device based on the local table name of the device. The distributed table name is required when the RDB store of a remote device is queried. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/NnbKAUa3Q66r3dmqAij3BA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDB1FFBB8F80A8AB3144A530E216728396193DDD88DD0D3B93AEDDCD77CE6845)

The value of **device** can be obtained by deviceManager.getTrustedDeviceListSync. The APIs of the **deviceManager** module are system interfaces and available only to system applications.

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

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  let deviceId: Array<string> = devices\[0\].deviceId;
})

let promise: void = rdbStore.obtainDistributedTableName(deviceId, "EMPLOYEE")
promise.then((tableName: String) => {
  console.info('ObtainDistributedTableName successfully, tableName= ' + tableName)
}).catch((err: BusinessError) => {
  console.info('ObtainDistributedTableName failed, err: ' + err)
})

#### \[h2\]sync8+

sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<\[string, number\]>>): void

Synchronizes data across devices. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](#syncmode8) | Yes | Data sync mode. The value can be **push** or **pull**. |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | **RdbPredicates** object that specifies the data and devices to synchronize. |
| callback | AsyncCallback<Array<\[string, number\]>> | Yes | 
Callback invoked to send the sync result to the caller.

**string** indicates the device ID.

**number** indicates the sync status of that device. The value **0** indicates a successful sync. Other values indicate a sync failure.

 |

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    let deviceIds: Array<string> = devices\[i\].deviceId;
  }
})

let predicates = new data\_rdb.RdbPredicates('EMPLOYEE')
predicates.inDevices(deviceIds)
rdbStore.sync(data\_rdb.SyncMode.SYNC\_MODE\_PUSH, predicates, (err: BusinessError, result: void) {
  if (err) {
    console.log('Sync failed, err: ' + err)
    return
  }
  console.log('Sync done.')
  for (let i = 0; i < result.length; i++) {
    console.log('device=' + result\[i\]\[0\] + ' status=' + result\[i\]\[1\])
  }
})

#### \[h2\]sync8+

sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<\[string, number\]>>

Synchronizes data across devices. This API uses a promise to return the result.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SyncMode](#syncmode8) | Yes | Data sync mode. The value can be **push** or **pull**. |
| predicates | [RdbPredicates](#rdbpredicates) | Yes | **RdbPredicates** object that specifies the data and devices to synchronize. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<\[string, number\]>> | 
Promise used to send the sync result.

**string** indicates the device ID.

**number** indicates the sync status of that device. The value **0** indicates a successful sync. Other values indicate a sync failure.

 |

**Example**

import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    let deviceIds: Array<string> = devices\[i\].deviceId;
  }
})

let predicates = new data\_rdb.RdbPredicates('EMPLOYEE')
predicates.inDevices(deviceIds)
let promise: void = rdbStore.sync(data\_rdb.SyncMode.SYNC\_MODE\_PUSH, predicates)
promise.then((result: void) =>{
  console.log('Sync done.')
  for (let i = 0; i < result.length; i++) {
    console.log('device=' + result\[i\]\[0\] + ' status=' + result\[i\]\[1\])
  }
}).catch((err: BusinessError) => {
  console.log('Sync failed')
})

#### \[h2\]on('dataChange')8+

on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

Registers an observer for this RDB store. When the data in the RDB store changes, a callback is invoked to return the data changes.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event to observe. The value is **dataChange**, which indicates a data change event. |
| type | [SubscribeType](#subscribetype8) | Yes | Subscription type to register. |
| observer | Callback<Array<string>> | Yes | Observer that listens for the data changes in the RDB store. **Array<string>** indicates the ID of the peer device whose data in the database is changed. |

**Example**

let devices: Array<string>;

try {
  rdbStore.on('dataChange', data\_rdb.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, (storeObserver: Array<string>) => {
    for (let i = 0; i < devices.length; i++) {
      console.log('device=' + devices\[i\] + ' data changed')
    }
  })
} catch (err) {
  console.log('Register observer failed')
}

#### \[h2\]off('dataChange')8+

off(event:'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

Unregisters the observer of the specified type from the RDB store. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | string | Yes | Event to observe. The value is **dataChange**, which indicates a data change event. |
| type | [SubscribeType](#subscribetype8) | Yes | Subscription type to register. |
| observer | Callback<Array<string>> | Yes | Data change observer registered. **Array<string>** indicates the ID of the peer device whose data in the database is changed. |

**Example**

let devices: Array<string>;

try {
  rdbStore.off('dataChange', data\_rdb.SubscribeType.SUBSCRIBE\_TYPE\_REMOTE, (storeObserver: Array<string>) => {
    for (let i = 0; i < devices.length; i++) {
      console.log('device=' + devices\[i\] + ' data changed')
    }
  })
} catch (err) {
  console.log('Unregister observer failed')
}
