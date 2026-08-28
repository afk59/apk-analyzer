# cloudDatabase (Cloud DB Module)

This module provides the capabilities of writing, querying, and deleting data through the Cloud DB service.

**Start version**: 5.0.0(12)

#### Modules to Import

import { cloudDatabase } from '@kit.CloudFoundationKit';

#### zone

zone(zone: string): DatabaseZone

Initializes a Cloud DB instance using a zone name.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

zone

 | 

string

 | 

Yes

 | 

Zone name.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseZone](#section18912210182513)

 | 

Cloud DB instance that processes data.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';

let databaseZone = cloudDatabase.zone("storageArea");

#### DatabaseZone

Cloud DB instance that processes data.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

#### \[h2\]query

query<T extends DatabaseObject>(condition: DatabaseQuery<T>): Promise<T\[\]>

Queries data based on specified criteria. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

condition

 | 

[DatabaseQuery](#section76501736191415)<T>

 | 

Yes

 | 

Query criteria.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<T\[\]>

 | 

Query result returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

// Create the **BookInfo.ets** file in the code project.
import { cloudDatabase } from '@kit.CloudFoundationKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**.
class BookInfo extends cloudDatabase.DatabaseObject{
  public naturalbase\_ClassName(): string {
    return 'BookInfo';
  }
  public key\_string: string | undefined;
  public key\_boolean: boolean | undefined;
  public key\_byte: number | undefined;
  public key\_short: number | undefined;
  public key\_integer: number | undefined;
  public key\_long: number | undefined;
  public key\_float: number | undefined;
  public key\_double: number | undefined;
  public key\_text: string | undefined;
  public key\_date: Date | undefined;
  public key\_byte\_array: Uint8Array | undefined;
}

export { BookInfo };

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // Import the **BookInfo.ets** file to the Cloud DB code project. _xx_ indicates the file path.

try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let condition = new cloudDatabase.DatabaseQuery(BookInfo);
  condition.equalTo('key\_string', 'string\_123');
  let bookInfoArray = await databaseZone.query(condition);
  hilog.info(0x0000, 'testTag', \`Succeeded in querying data, result: ${JSON.stringify(bookInfoArray)}\`);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query data, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]query

query<T extends DatabaseObject>(condition: DatabaseQuery<T>, callback: AsyncCallback<T\[\]>): void

Queries data based on specified criteria. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

condition

 | 

[DatabaseQuery](#section76501736191415)<T>

 | 

Yes

 | 

Query criteria.

 |
| 

callback

 | 

AsyncCallback<T\[\]>

 | 

Yes

 | 

Callback function. If data is queried successfully, **err** is **undefined** and **data** is the result array obtained; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('key\_string', 'string\_123');
databaseZone.query(condition, (err: BusinessError, bookInfoArray) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to query data, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in querying data, result: ${JSON.stringify(bookInfoArray)}\`);
  }
});

#### \[h2\]calculateQuery

calculateQuery<T extends DatabaseObject>(condition: DatabaseQuery<T>, fieldName: string, calculate: QueryCalculate): Promise<number>

Queries data that meets the search criteria from the database and performs arithmetic calculation on the specified field. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

condition

 | 

[DatabaseQuery](#section76501736191415)<T>

 | 

Yes

 | 

Query criteria.

 |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of the field on which the arithmetic calculation is performed in the query object.

 |
| 

calculate

 | 

[QueryCalculate](#section530095545712)

 | 

Yes

 | 

Calculation type.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Calculation result of the specified field, returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let condition = new cloudDatabase.DatabaseQuery(BookInfo);
  condition.lessThan('key\_integer', 100);
  let count = await databaseZone.calculateQuery(condition, 'key\_integer', cloudDatabase.QueryCalculate.AVERAGE);
  hilog.info(0x0000, 'testTag', \`Succeeded in calculating queried data, result: ${count}\`);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to calculate queried data, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]calculateQuery

calculateQuery<T extends DatabaseObject>(condition: DatabaseQuery<T>, fieldName: string, calculate: QueryCalculate, callback: AsyncCallback<number>): void

Queries data that meets the search criteria from the database and performs arithmetic calculation on the specified field. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

condition

 | 

[DatabaseQuery](#section76501736191415)<T>

 | 

Yes

 | 

Query criteria.

 |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of the field on which the arithmetic calculation is performed in the query object.

 |
| 

calculate

 | 

[QueryCalculate](#section530095545712)

 | 

Yes

 | 

Calculation type.

 |
| 

callback

 | 

AsyncCallback<number>

 | 

Yes

 | 

Callback function that returns the calculation result of the specified field.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key\_integer', 100);
databaseZone.calculateQuery(condition, 'key\_integer', cloudDatabase.QueryCalculate.AVERAGE,
  (err: BusinessError, num) => {
    if (err) {
      hilog.error(0x0000, 'testTag', \`Failed to calculate queried data, code: ${err.code}, message: ${err.message}\`);
    } else {
      hilog.info(0x0000, 'testTag', \`Succeeded in calculating queried data, result: ${num}\`);
    }
  });

#### \[h2\]upsert

upsert<T extends DatabaseObject>(objectList: T\[\] | T): Promise<number>

Updates data in the database. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

objectList

 | 

T\[\] | T

 | 

Yes

 | 

One or more objects.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Number of data records that are successfully updated, returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let book = new BookInfo();
  book.key\_string = 'string\_12';
  book.key\_integer = 90;
  let book1 = new BookInfo();
  book1.key\_string = 'string\_1234';
  book1.key\_integer = 101;
  let num = await databaseZone.upsert(\[book, book1\]);
  hilog.info(0x0000, 'testTag', \`Succeeded in upserting data, result: ${num}\`);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to upsert data, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]upsert

upsert<T extends DatabaseObject>(objectList: T\[\] | T, callback: AsyncCallback<number>): void

Updates data in the database. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

objectList

 | 

T\[\] | T

 | 

Yes

 | 

One or more objects.

 |
| 

callback

 | 

AsyncCallback<number>

 | 

Yes

 | 

Callback function that returns the number of data records that are successfully updated.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let book = new BookInfo();
book.key\_string = 'string\_12';
book.key\_integer = 90;
let book1 = new BookInfo();
book1.key\_string = 'string\_1234';
book1.key\_integer = 101;
databaseZone.upsert(\[book, book1\], (err: BusinessError, num) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to upsert data, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in upserting data, result: ${num}\`);
  }
});

#### \[h2\]delete

delete<T extends DatabaseObject>(objectList: T\[\] | T): Promise<number>

Deletes one or more data records from the database. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

objectList

 | 

T\[\] | T

 | 

Yes

 | 

One or more objects.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Number of data records that are successfully deleted, returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
try {
  let databaseZone = cloudDatabase.zone('storageArea');
  let condition = new cloudDatabase.DatabaseQuery(BookInfo);
  condition.lessThan('key\_integer', 100);
  let bookArray = await databaseZone.query(condition);
  let deleteNum = await databaseZone.delete(bookArray);
  hilog.info(0x0000, 'testTag', \`Succeeded in deleting a book, result: ${deleteNum}\`);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete a book, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]delete

delete<T extends DatabaseObject>(objectList: T\[\] | T, callback: AsyncCallback<number>): void

Deletes one or more data records from the database. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

objectList

 | 

T\[\] | T

 | 

Yes

 | 

One or more objects.

 |
| 

callback

 | 

AsyncCallback<number>

 | 

Yes

 | 

Callback function that returns the number of data records that are successfully deleted.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1008230001

 | 

Network connection error.

 |
| 

1008230002

 | 

Schema config error.

 |
| 

1008230003

 | 

Natural object error.

 |
| 

1008230009

 | 

Client internal error.

 |
| 

1008231001

 | 

Server error.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key\_integer', 100);
try {
  let bookArray = await databaseZone.query(condition);
  databaseZone.delete(bookArray, (err: BusinessError, num) => {
    if (err) {
      hilog.error(0x0000, 'testTag', \`Failed to delete a book, code: ${err.code}, message: ${err.message}\`);
    } else {
      hilog.info(0x0000, 'testTag', \`Succeeded in deleting a book, result: ${num}\`);
    }
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### DatabaseObject

Base class for database data types, which is extended during table structure generation on the cloud.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

#### \[h2\]naturalbase\_ClassName

naturalbase\_ClassName(): string

Base class name for data types.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Base class name for a data type, which must be the same as the name of the created object type.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
class BookInfo extends cloudDatabase.DatabaseObject{
  public naturalbase\_ClassName(): string {
    return "BookInfo";
  }
}

export { BookInfo };

#### FieldType

type FieldType = string | number | boolean | Uint8Array | Date

Data types supported by Cloud DB. The value types are the union or intersection of the types listed in the table below.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

The value can be any string.

 |
| 

number

 | 

The value can be any number.

 |
| 

boolean

 | 

The value is of the Boolean type and can be set to **true** or **false**.

 |
| 

Uint8Array

 | 

The value is an array of 8-bit unsigned integers and can be set to any value.

 |
| 

Date

 | 

The value is a date in format _YYYY-MM-DD_.

 |

#### QueryCalculate

Enumerated calculation types.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

AVERAGE

 | 

0

 | 

Calculate the average value.

 |
| 

SUM

 | 

1

 | 

Calculate the sum.

 |
| 

MAXIMUM

 | 

2

 | 

Calculate the maximum value.

 |
| 

MINIMUM

 | 

3

 | 

Calculate the minimum value.

 |
| 

COUNT

 | 

4

 | 

Calculate the total number of records.

 |

#### DatabaseQuery

DatabaseQuery<T extends DatabaseObject>

Provides various predicate queries to construct query conditions. You can create your own **DatabaseQuery** object using these predicate query methods.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

#### \[h2\]constructor

constructor(entityClass: new () => T)

Constructs the query entity class information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

entityClass

 | 

new () => T

 | 

Yes

 | 

Entity class of a data object.

 |

#### \[h2\]equalTo

equalTo(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is equal to a specified value.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('key\_string', 'string\_123');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]notEqualTo

notEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is not equal to a specified value.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.notEqualTo('key\_string', 'string\_123');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]beginsWith

beginsWith(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a string-type field in an entity class starts with a specified substring.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.beginsWith('key\_string', 'key');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]endsWith

endsWith(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a string-type field in an entity class ends with a specified substring.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.endsWith('key\_string', 'string');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]contains

contains(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a string-type field in an entity class contains the specified substring.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.contains('key\_string', 'string');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]greaterThan

greaterThan(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is greater than a specified value.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.greaterThan('key\_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]greaterThanOrEqualTo

greaterThanOrEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is greater than or equal to a specified value.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.greaterThanOrEqualTo('key\_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]lessThan

lessThan(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is less than a specified value.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key\_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]lessThanOrEqualTo

lessThanOrEqualTo(fieldName: string, value: FieldType): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is less than or equal to a specified value.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

value

 | 

[FieldType](#section15219172491013)

 | 

Yes

 | 

Value of a data type supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThanOrEqualTo('key\_integer', 100);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]in

in(fieldName: string, values: FieldType\[\]): DatabaseQuery<T>

Adds a query condition where the value of a field in an entity class is contained in a specified array.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |
| 

values

 | 

[FieldType](#section15219172491013)\[\]

 | 

Yes

 | 

Array of values of data types supported by Cloud DB.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.in('key\_integer', \[100, 200\]);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]isNull

isNull(fieldName: string): DatabaseQuery<T>

Adds a query condition where a field in an entity class is **null**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.isNull('key\_date');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]isNotNull

isNotNull(fieldName: string): DatabaseQuery<T>

Adds a query condition where a field in an entity class is not **null**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.isNotNull('key\_date');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]orderByAsc

orderByAsc(fieldName: string): DatabaseQuery<T>

Sorts query results by specified field in ascending order.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.orderByAsc('key\_integer');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]orderByDesc

orderByDesc(fieldName: string): DatabaseQuery<T>

Sorts query results by specified field in descending order.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fieldName

 | 

string

 | 

Yes

 | 

Name of a field in an entity class.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.orderByDesc('key\_integer');
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]orderByRandom

orderByRandom(): DatabaseQuery<T>

Sorts query results in random order.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/dqaCRcj1TpuXlmgAMxUO_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AE2CF0AA9FA467C58BA1CE7697BE7FD1152B17E1E7DE60F155256D06BDA2DB2)

You are advised to use **orderByRandom()** together with **limit()** to sort data. Otherwise, if the number of data records of the object type is too large, the query efficiency may be affected, causing query timeout or failure.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 6.0.1(21)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.orderByRandom().limit(10);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]limit

limit(count: number, offset?: number): DatabaseQuery<T>

Specifies the number of data records in the returned query result set. If you do not set **offset**, the first _count_ objects will be obtained by default.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

count

 | 

number

 | 

Yes

 | 

Number of data records that can be obtained.

 |
| 

offset

 | 

number

 | 

No

 | 

Start position of data records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.lessThan('key\_integer', 100);
condition.limit(4, 1);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]beginGroup

beginGroup(): DatabaseQuery<T>

Adds a left parenthesis "(" to any query condition and pairs it with a right parenthesis ")" to group the conditions together within the same query.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/7apFCjYHQ0iP3350jqFkDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C6A5BC64723C241995DB30ECE024E907EA6F9A7AF3BB4E57E2B654AA172AF69)

-   **beginGroup()** and **endGroup()** must be used together and combined with other query conditions.
-   One or more of the following query conditions must exist between **beginGroup()** and **endGroup()**:
    
    **equalTo()**, **notEqualTo()**, **greaterThan()**, **greaterThanOrEqualTo()**, **lessThan()**, **lessThanOrEqualTo()**, **in()**, **beginsWith()**, **endsWith()**, **isNull()**, **isNotNull()**, and **contains()**
    
-   **beginGroup()** cannot be directly used before **and()** or **or()**. That is, **beginGroup().and()**, **beginGroup().and().endGroup()**, **beginGroup().or()**, and **beginGroup().or().endGroup()** are not supported.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.beginGroup().equalTo('string\_string', 'string\_123').endGroup();
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]endGroup

endGroup(): DatabaseQuery<T>

Adds a right parenthesis ")" to any query condition and pairs it with a left parenthesis "(" to group the conditions together within the same query.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/GoHmYZT5SJqnoaWmUzlsmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C9CA2E541D3D67C8846509592921A0DD8596A9C753A3F2F693092B98DC93AEB)

-   **beginGroup()** and **endGroup()** must be used together and combined with other query conditions.
-   One or more of the following query conditions must exist between **beginGroup()** and **endGroup()**:
    
    **equalTo()**, **notEqualTo()**, **greaterThan()**, **greaterThanOrEqualTo()**, **lessThan()**, **lessThanOrEqualTo()**, **in()**, **beginsWith()**, **endsWith()**, **isNull()**, **isNotNull()**, and **contains()**
    
-   **endGroup()** cannot be directly used before **and()** or **or()**. That is, **and().endGroup()**, **beginGroup().and().endGroup()**, **or().endGroup()**, and **beginGroup().or().endGroup()** are not supported.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.beginGroup().equalTo('string\_string', 'string\_123').endGroup();
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]or

or(): DatabaseQuery<T>

Combines two conditions using the OR operator and returns the union of the two query results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/s9PJI2PzSyGbg1KENRSk5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D12F48D2DB98B12AE334CD83C39873A7AE4445A1CBB88E09C82B6B28B05674F)

-   **or()** can be used only with other query conditions.
-   When it is used together with **equalTo()**, **notEqualTo()**, **greaterThan()**, **greaterThanOrEqualTo()**, **lessThan()**, **lessThanOrEqualTo()**, **in()**, **beginsWith()**, **endsWith()**, **isNull()**, **isNotNull()**, or **contains()**, the intersection of the two query results is returned.
-   When **or()** is used together with **and()**, **or()** cannot directly follow **and()**. That is, **and().or()** is not supported.
-   When it is used together with **beginGroup()** or **endGroup()**:
    -   Multi-layer nesting is supported, and **beginGroup()** and **endGroup()** must appear in pairs.
    -   **beginGroup()** cannot be used before **or()**, and **endGroup()** cannot be used after **or()**.
    -   That is, **beginGroup().or()**, **beginGroup().or().endGroup()**, and **or().endGroup()** are not supported.
    -   It cannot be used with **orderByAsc()**, **orderByDesc()**, or **limit()**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('string\_string', 'string\_123').or().lessThan('key\_integer', 50);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]and

and(): DatabaseQuery<T>

Combines two conditions using the AND operator and returns the intersection of the two query results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/DatFeXJdRduwjNfY5XnFXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90666AE16752594277018F9D8F07A3AD3B588BCFF7E9E3BC9CB59639F1E652F0)

-   **and()** can be used only with other query conditions.
-   When it is used together with **equalTo()**, **notEqualTo()**, **greaterThan()**, **greaterThanOrEqualTo()**, **lessThan()**, **lessThanOrEqualTo()**, **in()**, **beginsWith()**, **endsWith()**, **isNull()**, **isNotNull()**, or **contains()**, the intersection of the two query results is returned.
-   When **and()** is used together with **or()**, **and()** cannot be directly followed by **or()**. That is, **and().or()** is not supported.
-   When it is used together with **beginGroup()** or **endGroup()**:
    -   Multi-layer nesting is supported, and **beginGroup()** and **endGroup()** must appear in pairs.
    -   **beginGroup()** cannot be used before **and()**, and **endGroup()** cannot be used after **and()**.
    -   That is, **beginGroup().and()**, **beginGroup().and().endGroup()**, and **and().endGroup()** are not supported.
    -   It cannot be used with **orderByAsc()**, **orderByDesc()**, or **limit()**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DatabaseQuery](#section76501736191415)<T>

 | 

**DatabaseQuery** object.

 |

**Example**:

import { cloudDatabase } from '@kit.CloudFoundationKit';
import { BookInfo } from 'xx/BookInfo'; // _xx_ is the path to the **BookInfo** file.
import { hilog } from '@kit.PerformanceAnalysisKit';

// Create a **BookInfo** class that extends **cloudDatabase.DatabaseObject**. Its implementation is the same as the sample code of the **query** API which returns the result asynchronously through a promise.
let databaseZone = cloudDatabase.zone('storageArea');
let condition = new cloudDatabase.DatabaseQuery(BookInfo);
condition.equalTo('string\_string', 'string\_123').and().lessThan('key\_integer', 50);
try {
  let bookInfoArray = await databaseZone.query(condition);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to query books, code: ${err.code}, message: ${err.message}\`);
}
