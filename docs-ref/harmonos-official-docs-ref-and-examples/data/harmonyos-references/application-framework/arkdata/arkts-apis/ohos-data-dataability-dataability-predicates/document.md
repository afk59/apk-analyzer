# @ohos.data.dataAbility (DataAbility Predicates)

The **DataAbility** module provides APIs to create predicates for querying data from relational database (RDB) stores.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/GFvsb-5DSY-3O4d4Y0AxLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D7C2751F21E210B77A54E4025BF841C7891F759026216DD8D9B5D718BB3A269)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { dataAbility } from '@kit.ArkData';

#### dataAbility.createRdbPredicates

createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates

Creates an **RdbPredicates** object with a table name and **DataAbilityPredicates** object.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of a database table. |
| dataAbilityPredicates | [DataAbilityPredicates](#dataabilitypredicates) | Yes | **DataAbilityPredicates** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| rdb.[RdbPredicates](../apis-no-longer-maintained/ohos-data-rdb-rdb-store/document.md#rdbpredicates) | **RdbPredicates** object created. |

**Example**

let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
dataAbilityPredicates.equalTo("NAME", "Rose")
// EMPLOYEE is a table created in an RDB store.
let predicates = dataAbility.createRdbPredicates("EMPLOYEE", dataAbilityPredicates)

#### DataAbilityPredicates

Provides APIs for creating diverse query conditions.

**Initialization**

let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()

#### \[h2\]equalTo

equalTo(field: string, value: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are equal to the given value.

This API is similar to the SQL equal to (=) operator.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.equalTo("NAME", "lisi")

#### \[h2\]notEqualTo

notEqualTo(field: string, value: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are not equal to the given value.

This API is similar to the SQL not equal (!=) operator.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.notEqualTo("NAME", "lisi")

#### \[h2\]beginWrap

beginWrap(): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to add a left parenthesis. This API is similar to "(" in an SQL statement and must be used with **endWrap**.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object with a left parenthesis. |

**Example**

dataAbilityPredicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap()

#### \[h2\]endWrap

endWrap(): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to add a right parenthesis. This API is similar to ")" in an SQL statement and must be used with **beginWrap**.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object with a right parenthesis. |

**Example**

dataAbilityPredicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap()

#### \[h2\]or

or(): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to add the OR condition.

This API is similar to the SQL **or** operator.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object with the OR condition. |

**Example**

dataAbilityPredicates.equalTo("NAME", "Lisa")
    .or()
    .equalTo("NAME", "Rose")

#### \[h2\]and

and(): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to add the AND condition.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object with the AND condition. |

**Example**

dataAbilityPredicates.equalTo("NAME", "Lisa")
    .and()
    .equalTo("SALARY", 200.5)

#### \[h2\]contains

contains(field: string, value: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that contain the given value.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.contains("NAME", "os")

#### \[h2\]beginsWith

beginsWith(field: string, value: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that begin with the given value.

This API is similar to the percent sign (%) in SQL statements.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.beginsWith("NAME", "os")

#### \[h2\]endsWith

endsWith(field: string, value: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that end with the given value.

This API is similar to the percent sign (%) in SQL statements.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.endsWith("NAME", "se")

#### \[h2\]isNull

isNull(field: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are **null**.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.isNull("NAME")

#### \[h2\]isNotNull

isNotNull(field: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are not **null**.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.isNotNull("NAME")

#### \[h2\]like

like(field: string, value: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are similar to the given value.

This API is similar to the SQL **like** statement.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.like("NAME", "%os%")

#### \[h2\]glob

glob(field: string, value: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that match the given string. Different from **like**, the input parameters of this API are case-sensitive.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.glob("NAME", "?h\*g")

// Only the records whose value is "Lisa" in the "name" column are matched.
dataAbilityPredicates.glob("NAME", "Lisa")

// Only the records whose value is "lisa" in the "name" column are matched.
dataAbilityPredicates.glob("NAME", "lisa")

#### \[h2\]between

between(field: string, low: ValueType, high: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are within the given range.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| low | [ValueType](#valuetype) | Yes | Minimum value to match. |
| high | [ValueType](#valuetype) | Yes | Maximum value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.between("AGE", 10, 50)

#### \[h2\]notBetween

notBetween(field: string, low: ValueType, high: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are out of the given range.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| low | [ValueType](#valuetype) | Yes | Minimum value to match. |
| high | [ValueType](#valuetype) | Yes | Maximum value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.notBetween("AGE", 10, 50)

#### \[h2\]greaterThan

greaterThan(field: string, value: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are greater than the given value.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.greaterThan("AGE", 18)

#### \[h2\]lessThan

lessThan(field: string, value: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are less than the given value.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.lessThan("AGE", 20)

#### \[h2\]greaterThanOrEqualTo

greaterThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are greater than or equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.greaterThanOrEqualTo("AGE", 18)

#### \[h2\]lessThanOrEqualTo

lessThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are less than or equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | [ValueType](#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.lessThanOrEqualTo("AGE", 20)

#### \[h2\]orderByAsc

orderByAsc(field: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to sort the records in the specified column in ascending order. When there are multiple **orderByAsc**s, the first **orderByAsc** used has the highest priority.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

// Sort data by name first; for the records with the same name, sort them by age; for the records with the same name and age, sort them by salary in ascending order.
dataAbilityPredicates.orderByAsc("NAME").orderByAsc("AGE").orderByAsc("SALARY")

#### \[h2\]orderByDesc

orderByDesc(field: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to sort the records in the specified column in descending order. When there are multiple **orderByDesc**s, the first **orderByDesc** used has the highest priority.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

// Sort the data by age first. For the data records with the same age, sort them by salary.
dataAbilityPredicates.orderByDesc("AGE").orderByDesc("SALARY")

#### \[h2\]distinct

distinct(): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to filter out duplicate records.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.equalTo("NAME", "Rose").distinct()

#### \[h2\]limitAs

limitAs(value: number): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to limit the number of records.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Maximum number of records. The value should be a positive integer. If a value less than or equal to **0** is specified, the number of records is not limited. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.equalTo("NAME", "Rose").limitAs(3)

#### \[h2\]offsetAs

offsetAs(rowOffset: number): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to set the start position of the query result. This API must be used together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in **\-1** in **limitAs**.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rowOffset | number | Yes | Start position. The value should be a positive integer. If a value less than or equal to **0** is specified, the query result is returned from the first element. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

// Display the three data records following the first three records.
dataAbilityPredicates.equalTo("NAME", "Rose").offsetAs(3).limitAs(3)

#### \[h2\]groupBy

groupBy(fields: Array<string>): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to group the query results based on the specified columns.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fields | Array<string> | Yes | Names of columns to group. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.groupBy(\["AGE", "NAME"\])

#### \[h2\]indexedBy

indexedBy(field: string): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to specify the index column. Before calling this API, you need to create an index column.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Name of the index. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { dataAbility, relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate(): Promise<void> {
    let store: relationalStore.RdbStore | undefined = undefined;
    let context = this.context;

    try {
      const STORE\_CONFIG: relationalStore.StoreConfig = {
        name: 'RdbTest.db', // Database file name.
        securityLevel: relationalStore.SecurityLevel.S3,
      };
      // Table structure: EMPLOYEE (NAME, AGE, SALARY, CODES)
      const SQL\_CREATE\_TABLE =
        'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)'; // SQL statement for creating a data table.
      store = await relationalStore.getRdbStore(context, STORE\_CONFIG);
      console.info('Succeeded in getting RdbStore.');
      await store.executeSql(SQL\_CREATE\_TABLE); // Create a data table.
    } catch (e) {
      const err = e as BusinessError;
      console.error(\`Failed to get RdbStore. Code:${err.code}, message:${err.message}\`);
    }

    if (!store) {
      return;
    }

    // Create an index.
    const SQL\_CREATE\_INDEX = 'CREATE INDEX SALARY\_INDEX ON EMPLOYEE(SALARY)'
    await store.executeSql(SQL\_CREATE\_INDEX);
    // ...

    let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
    dataAbilityPredicates.indexedBy("SALARY\_INDEX")

    //  ...
  }
}

#### \[h2\]in

in(field: string, value: Array<ValueType>): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are in the given range.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | Array<[ValueType](#valuetype)\> | Yes | Array of **ValueType**s to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.in("AGE", \[18, 20\])

#### \[h2\]notIn

notIn(field: string, value: Array<ValueType>): DataAbilityPredicates

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are out of the given range.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the table. |
| value | Array<[ValueType](#valuetype)\> | Yes | Array of **ValueType**s to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityPredicates](#dataabilitypredicates) | **DataAbilityPredicates** object created. |

**Example**

dataAbilityPredicates.notIn("NAME", \["Lisa", "Rose"\])

#### ValueType

type ValueType = number | string | boolean

Defines the value types.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

| Type | Description |
| :-- | :-- |
| number | The value is a number. |
| string | The value is a string. |
| boolean | The value is of Boolean type. |
