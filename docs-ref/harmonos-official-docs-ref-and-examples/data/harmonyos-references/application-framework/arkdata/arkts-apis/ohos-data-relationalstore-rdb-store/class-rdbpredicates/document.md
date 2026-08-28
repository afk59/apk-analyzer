# Class (RdbPredicates)

Defines the predicates for an RDB store. This class determines whether the conditional expression for the RDB store is true or false. Multiple predicates statements can be concatenated by using **and()** by default. **RdbPredicates** cannot be passed across threads using Sendable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/hV7lrtYlRFyuiC_XRL2yVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=569FDEC992DFDEB45DF36D8D43E0EB8E8CC3AE9D3DDF1B995A0BBF0B2E4EF111)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Module to Import

import { relationalStore } from '@kit.ArkData';

#### constructor

constructor(name: string)

Defines a constructor used to create an **RdbPredicates** object.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Database table name. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");

#### inDevices

inDevices(devices: Array<string>): RdbPredicates

Creates an **RdbPredicates** object to specify the remote devices to connect on the network during distributed database sync.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/HHWtwHLrRjeJUgXZ1u1C9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2340E5755182647FF0324C31170F5F21801D6E9CFB1D631A6FBB19225DA53AEF)

**devices** can be obtained by using [deviceManager.getAvailableDeviceListSync](../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#getavailabledevicelistsync).

When calling **sync()**, you need to call **inDevices** to specify the devices. If **inDevices** is not used, data will be synced to all devices on the network by default.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| devices | Array<string> | Yes | IDs of the remote devices to connect. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

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

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.inDevices(deviceIds);

#### inAllDevices

inAllDevices(): RdbPredicates

Creates an **RdbPredicates** object to specify all remote devices on the network to connect during distributed database sync.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.inAllDevices();

#### equalTo

equalTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](../types/document.md#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records in the NAME column where the value is Lisa.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");

#### notEqualTo

notEqualTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are not equal to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](../types/document.md#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records in the NAME column where the value is not Lisa.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notEqualTo("NAME", "Lisa");

#### beginWrap

beginWrap(): RdbPredicates

Creates an **RdbPredicates** object to add a left parenthesis.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .beginWrap()
  .equalTo("AGE", 18)
  .or()
  .equalTo("SALARY", 200.5)
  .endWrap();

#### endWrap

endWrap(): RdbPredicates

Creates an **RdbPredicates** object to add a right parenthesis.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .beginWrap()
  .equalTo("AGE", 18)
  .or()
  .equalTo("SALARY", 200.5)
  .endWrap();

#### or

or(): RdbPredicates

Creates an **RdbPredicates** object to add the OR condition.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Example**:

// Find all records in the NAME column where the value is Lisa or Rose.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .or()
  .equalTo("NAME", "Rose");

#### and

and(): RdbPredicates

Creates an **RdbPredicates** object to add the AND condition.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Example**:

// Find the records in the EMPLOYEE table where the NAME column is Lisa and the SALARY column is 200.5.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa")
  .and()
  .equalTo("SALARY", 200.5);

#### contains

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that contain the string 'os' in the NAME column, for example, Rose.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.contains("NAME", "os");

#### beginsWith

beginsWith(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that begin with the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that start with "Li" in the NAME column, for example, Lisa.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.beginsWith("NAME", "Li");

#### endsWith

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that end with "se" in the NAME column, for example, Rose.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.endsWith("NAME", "se");

#### isNull

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.isNull("NAME");

#### isNotNull

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.isNotNull("NAME");

#### like

like(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are similar to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Condition for fuzzy match. Generally, this parameter is used together with a wildcard. A percent sign (%) represents any character of any length, and an underscore (\_) represents a single character. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that are similar to "os" in the NAME column, for example, Rose.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.like("NAME", "%os%");

#### glob

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find the strings that match "?h\*g" in the NAME column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.glob("NAME", "?h\*g");

#### between

between(field: string, low: ValueType, high: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are within the given range (including the min. and max. values) in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| low | [ValueType](../types/document.md#valuetype) | Yes | Minimum value of the range to set. |
| high | [ValueType](../types/document.md#valuetype) | Yes | Maximum value of the range to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find the records that are greater than or equal to 10 and less than or equal to 50 in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.between("AGE", 10, 50);

#### notBetween

notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are out of the given range (excluding the min. and max. values) in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| low | [ValueType](../types/document.md#valuetype) | Yes | Minimum value of the range to set. |
| high | [ValueType](../types/document.md#valuetype) | Yes | Maximum value of the range to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find the records that are less than 10 or greater than 50 in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notBetween("AGE", 10, 50);

#### greaterThan

greaterThan(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are greater than the given value in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](../types/document.md#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that are greater than 18 in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.greaterThan("AGE", 18);

#### lessThan

lessThan(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are less than the given value in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](../types/document.md#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that are less than 20 in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.lessThan("AGE", 20);

#### greaterThanOrEqualTo

greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are greater than or equal to the given value in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](../types/document.md#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that are greater than or equal to 18 in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.greaterThanOrEqualTo("AGE", 18);

#### lessThanOrEqualTo

lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are less than or equal to the given value in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | [ValueType](../types/document.md#valuetype) | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that are less than or equal to 20 in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.lessThanOrEqualTo("AGE", 20);

#### orderByAsc

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.orderByAsc("NAME");

#### orderByDesc

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
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.orderByDesc("AGE");

#### distinct

distinct(): RdbPredicates

Creates an **RdbPredicates** object to filter out duplicate records.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object that can filter out duplicate records. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose").distinct(); // Deduplicate result sets whose NAME is Rose.

#### limitAs

limitAs(value: number): RdbPredicates

Creates a **RdbPredicates** object to limit the number of records.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Maximum number of data records. The value should be a positive integer. If a value less than or equal to **0** is specified, the number of records is not limited. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | Predicates that specify the maximum number of records. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose").limitAs(3);

#### offsetAs

offsetAs(rowOffset: number): RdbPredicates

Creates an **RdbPredicates** object to set the start position of the query result. This API must be used together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in a parameter less than or equal to **0** in **limitAs**.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rowOffset | number | Yes | Start position of the query result. By default, the start position is the beginning of the result set. If **rowOffset** is a negative number, the start position is the beginning of the result set. If **rowOffset** exceeds the end of the result set, the query result is empty. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | Predicates that specify the start position of the returned result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose").limitAs(-1).offsetAs(3);

#### groupBy

groupBy(fields: Array<string>): RdbPredicates

Creates a **RdbPredicates** object to group the query results based on the specified columns.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fields | Array<string> | Yes | Names of columns to group. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | Predicates that group rows with the same value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.groupBy(\["AGE", "NAME"\]);

#### indexedBy

indexedBy(field: string): RdbPredicates

Creates a **RdbPredicates** object to specify the index column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Name of the index column. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.indexedBy("SALARY");

#### in

in(field: string, value: Array<ValueType>): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are in the given range in the specified column.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/H10OB2VOSP2E-iq9oJxXvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3CC07D874E56C01EDE2F3076B8DD9EB1B39D2C3866419A0A8146AE07A4DCBF6)

The **value** array cannot be empty; otherwise, this condition becomes invalid. As a result, the operation (such as full query, update, or deletion) is performed on all data. Before calling this API, check whether the **value** array is empty to avoid misoperations.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | Array<[ValueType](../types/document.md#valuetype)\> | Yes | Array of **ValueType**s to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find records that are within \[18, 20\] in the AGE column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.in("AGE", \[18, 20\]);

#### notIn

notIn(field: string, value: Array<ValueType>): RdbPredicates

Creates an **RdbPredicates** object to search for the records that are out of the given range in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | Array<[ValueType](../types/document.md#valuetype)\> | Yes | Array of **ValueType**s to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find the records that are not within \[Lisa, Rose\] in the NAME column.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notIn("NAME", \["Lisa", "Rose"\]);

#### notContains12+

notContains(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records that do not contain the given value in the specified column.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find the records that do not contain the string "os" in the NAME column, for example, Lisa.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notContains("NAME", "os");

#### notLike12+

notLike(field: string, value: string): RdbPredicates

Creates an **RdbPredicates** object to search for the records in the specified column that are not similar to the given value.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Condition for fuzzy match. Generally, this parameter is used together with a wildcard. A percent sign (%) represents any character of any length, and an underscore (\_) represents a single character. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**:

// Find all the records that are not similar to "os" in the NAME column, for example, Lisa.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.notLike("NAME", "%os%");

#### having20+

having(conditions:string, args?: Array<ValueType>): RdbPredicates

Filters for group data that meets the conditions.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| conditions | string | Yes | Condition used to filter the data obtained using [groupBy](#groupby). This parameter cannot be empty and must be used with [groupBy](#groupby). |
| args | Array<[ValueType](../types/document.md#valuetype)\> | No | Parameters used in **conditions**, which replace the placeholder in the conditional statement. If this parameter is not specified, the default value is an empty array. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RdbPredicates](#) | **RdbPredicates** object created. |

**Error codes**

For details about the error codes, see [RDB Error Codes](../../../error-codes/rdb-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range; 2. Missing GROUP BY clause. |

**Example 1**:

// Pass a complete condition.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.groupBy(\["AGE"\]);
predicates.having("NAME = zhangsan");

**Example 2**:

// Use placeholders in the condition and pass values to args to replace the placeholders.
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.groupBy(\["AGE"\]);
predicates.having("NAME = ?", \["zhangsan"\]);
