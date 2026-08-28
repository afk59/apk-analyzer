# healthStore (Health and Fitness Data Services)

This module provides health and fitness data services.

**Start version**: 5.0.0(12)

#### Module Import

import { healthStore } from '@kit.HealthServiceKit';

#### AggregateMetrics

type AggregateMetrics = Partial<Record<[AggregateMetricScope](#section246315450395), number>>

Aggregation metric.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

max

 | 

number

 | 

No

 | 

Yes

 | 

Maximum aggregation. If this parameter is not set, this type of aggregation is not supported.

 |
| 

min

 | 

number

 | 

No

 | 

Yes

 | 

Minimum aggregation. If this parameter is not set, this type of aggregation is not supported.

 |
| 

avg

 | 

number

 | 

No

 | 

Yes

 | 

Average aggregation. If this parameter is not set, this type of aggregation is not supported.

 |
| 

sum

 | 

number

 | 

No

 | 

Yes

 | 

Sum aggregation. If this parameter is not set, this type of aggregation is not supported.

 |
| 

last

 | 

number

 | 

No

 | 

Yes

 | 

Latest aggregation. If this parameter is not set, this type of aggregation is not supported.

 |
| 

count

 | 

number

 | 

No

 | 

Yes

 | 

Count aggregation. If this parameter is not set, this type of aggregation is not supported.

 |

#### AggregateMetricScope

type AggregateMetricScope = 'max' | 'min' | 'avg' | 'sum' | 'last' | 'count'

Aggregation metric type.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'max'

 | 

Calculates the maximum value.

 |
| 

'min'

 | 

Calculates the minimum value.

 |
| 

'avg'

 | 

Calculates the average value.

 |
| 

'sum'

 | 

Calculates the sum value.

 |
| 

'last'

 | 

Calculates the latest value.

 |
| 

'count'

 | 

Calculates the count.

 |

#### AggregateRequest

AggregateRequest<T extends Record<string, [AggregateMetrics](#section023015433412)\> = Record<string, [AggregateMetrics](#section023015433412)\>>

Aggregation query request class, which inherits from Omit<[DataReadRequest](#en-us_topic_0000001768344397_section15461104913472), 'startTime' | 'endTime'>.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)

 | 

No

 | 

No

 | 

Type of the data to be queried.

 |
| 

metrics

 | 

Partial<Record<keyof T, [AggregateMetricScope](#section246315450395)\[\]>>

 | 

No

 | 

No

 | 

Aggregation metric.

 |
| 

groupBy

 | 

[GroupOption](#section17334182555912)

 | 

No

 | 

No

 | 

Aggregation group options.

 |

#### AggregateResult

AggregateResult<T extends Record<string, [AggregateMetrics](#section023015433412)\> = Record<string, [AggregateMetrics](#section023015433412)\>>

Aggregation query result class, which inherits from Omit<[SampleDataBase](#section1327119123313), 'dataSourceId'>.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fields

 | 

Pick<T, keyof T>

 | 

No

 | 

No

 | 

Aggregation query field.

 |

#### AppInfo

App information class.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bundleName

 | 

string

 | 

Yes

 | 

Yes

 | 

App bundle name. If this parameter is not set, the bundle name of your app will be used by default.

 |
| 

appId

 | 

string

 | 

Yes

 | 

Yes

 | 

OAuth 2.0 client ID (**client\_id**). If this parameter is not set, the **client\_id** of your app is used by default.

 |
| 

appName

 | 

string

 | 

Yes

 | 

Yes

 | 

App name. The length is less than 256 bytes. If this parameter is not set in the beginning, the default value **CoreServiceExtAbility** is used. You can call [updateDataSource](#en-us_topic_0000001768344397_section7156914939) to update the app name.

 |
| 

version

 | 

string

 | 

Yes

 | 

Yes

 | 

App version. The length is less than 256 bytes. If this parameter is not set in the beginning, the default value is empty. You can call [updateDataSource](#en-us_topic_0000001768344397_section7156914939) to update the app version.

 |

#### AuthorizationBase

Authorization information base class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

readDataTypes

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data type to be read.

 |
| 

writeDataTypes

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data type to be written.

 |

#### AuthorizationRequest

Authorization request parameter type, which inherits from [AuthorizationBase](#en-us_topic_0000001768344397_section16391736104620).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

readDataTypes

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data type to be read.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

writeDataTypes

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data type to be written.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

scopes

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Non-data type scope. For details, see [OAuth Scope](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-cloudsync#section1451346172216). The value is left empty by default.

**Start version**: 5.1.0(18)

**Atomic service API**: This API can be used in atomic services since API version 5.1.0(18).

 |

#### AuthorizationResponse

Authorization response return type, which inherits from [AuthorizationBase](#en-us_topic_0000001768344397_section16391736104620).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

readDataTypes

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data types that are authorized to be read. Their scopes are the intersection of the [scopes you have applied for](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-apply) and those granted by users.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

writeDataTypes

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data types that are authorized to be written. Their scopes are the intersection of the [scopes you have applied for](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-apply) and those granted by users.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

scopes

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Non-data type scope. For details, see [OAuth Scope](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-cloudsync#section1451346172216). The value is left empty by default.

**Start version**: 5.1.0(18)

**Atomic service API**: This API can be used in atomic services since API version 5.1.0(18).

 |

#### DataReadRequest

Base class of parameters for data reading requests, which inherits from [DataRequest](#en-us_topic_0000001768344397_section142361026204113).

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

count

 | 

number

 | 

No

 | 

Yes

 | 

Number of data records to be read. If this parameter is not set, there is no restriction on the number of data records by default.

Value range: \[1, ∞)

 |
| 

offset

 | 

number

 | 

No

 | 

Yes

 | 

Offset relative to the current position. If this parameter is not set, the default value **0** is used, indicating no offset.

 |
| 

sortOrder

 | 

[SortOrder](#section1063613217259)

 | 

No

 | 

Yes

 | 

Sort order. If this parameter is not set, the ascending order is used by default.

 |

#### DataRequest

Request parameter base class.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startLocalDate

 | 

string

 | 

No

 | 

No

 | 

Local start date of data, in MM/DD/YYYY format.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

endLocalDate

 | 

string

 | 

No

 | 

No

 | 

Local end date of data, in MM/DD/YYYY format.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

startTime

 | 

number

 | 

No

 | 

No

 | 

Request start time. The value is a Unix timestamp in milliseconds.

This parameter does not take effect on wearable devices. Only the latest data record can be returned.

Value range: (0, ∞)

 |
| 

endTime

 | 

number

 | 

No

 | 

No

 | 

Request end time. The value is a Unix timestamp in milliseconds.

This parameter does not take effect on wearable devices. Only the latest data record can be returned.

Value range: (0, ∞)

 |
| 

dataSourceOptions

 | 

[DataSourceOptions](#section2546745691)

 | 

No

 | 

Yes

 | 

Data sources associated with the request. If this parameter is not set, there is no restriction on the data source by default.

 |

#### DataSource

Data source.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataSourceId

 | 

string

 | 

Yes

 | 

No

 | 

ID of a data source, which is generated by the platform and cannot be changed. The length is less than 256 bytes.

 |
| 

deviceInfo

 | 

[DeviceInfo](#section9562162482112)

 | 

Yes

 | 

Yes

 | 

Device information. The value is left empty by default.

 |
| 

appInfo

 | 

[AppInfo](#en-us_topic_0000001768344397_section19505904120)

 | 

Yes

 | 

Yes

 | 

App information. If this parameter is not set, your app information is used by default.

 |

#### DataSourceBase

type DataSourceBase = Omit<DataSource, 'dataSourceId'>

Data source base class, which is used to insert data sources.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

deviceInfo

 | 

[DeviceInfo](#section9562162482112)

 | 

Yes

 | 

Yes

 | 

Device information. The value is left empty by default.

 |
| 

appInfo

 | 

[AppInfo](#en-us_topic_0000001768344397_section19505904120)

 | 

Yes

 | 

Yes

 | 

App information. If this parameter is not set, your app information is used by default.

 |

#### DataSourceOptions

Data source option class, which is used to query and delete data sources.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataSourceId

 | 

string

 | 

No

 | 

Yes

 | 

ID of a data source, which is generated by the platform and cannot be changed. The value is left empty by default.

 |
| 

deviceUniqueId

 | 

string

 | 

No

 | 

Yes

 | 

Unique device ID. The value is left empty by default.

 |
| 

appBundleName

 | 

string

 | 

No

 | 

Yes

 | 

App bundle name. The value is left empty by default.

 |
| 

appId

 | 

string

 | 

No

 | 

Yes

 | 

OAuth 2.0 client ID (**client\_id**) of your app. The value is left empty by default.

 |

#### DataSourceReadRequest

Request for reading the data source.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataSourceId

 | 

string

 | 

No

 | 

Yes

 | 

Unique ID of a data source. (Do not set **dataSourceId** when you have set **bundleName** and **deviceUniqueId**).

 |
| 

bundleName

 | 

string

 | 

No

 | 

Yes

 | 

App bundle name. (Set this parameter only when **dataSourceId** is not set.)

 |
| 

deviceUniqueId

 | 

string

 | 

No

 | 

Yes

 | 

Unique device ID. (Set this parameter only when **dataSourceId** is not set.)

 |

#### DataType

Data type class. Each data type field is identified by a unique ID.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

Yes

 | 

No

 | 

Unique ID of a data type.

 |
| 

name

 | 

string

 | 

Yes

 | 

Yes

 | 

Name of a data type. If this parameter is not set, the name matching the data type ID is used by default.

 |

#### DeviceCategory

Device type enum object.

**System capability**: SystemCapability.Health.HealthStore

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

MANUAL\_INPUT

 | 

'000'

 | 

Manually entered.

 |
| 

SMART\_PHONE

 | 

'00E'

 | 

Phone.

 |
| 

WEARABLE\_WATCH

 | 

'06D'

 | 

Watch.

 |
| 

WEARABLE\_BAND

 | 

'06E'

 | 

Band.

 |
| 

SMART\_HEADPHONES

 | 

'082'

 | 

Smart earphones.

 |
| 

HDK\_WEIGHT\_SCALE

 | 

'0CB'

 | 

Body fat scale.

 |
| 

HDK\_BLOOD\_SUGAR\_MONITOR

 | 

'086'

 | 

Blood glucose monitor.

 |
| 

HDK\_BLOOD\_PRESSURE\_MONITOR

 | 

'02B'

 | 

Blood pressure monitor.

 |
| 

HDK\_HEART\_RATE\_MONITOR

 | 

'088'

 | 

Heart rate monitor.

 |
| 

HDK\_THERMOMETER

 | 

'0B3'

 | 

Thermometer.

 |
| 

HDK\_BLOOD\_OXYGEN\_MONITOR

 | 

'0B4'

 | 

Oximeter.

 |
| 

HDK\_ROPE\_SKIPPING

 | 

'095'

 | 

Jump rope.

 |
| 

HDK\_TREADMILL

 | 

'08F'

 | 

Treadmill.

 |
| 

HDK\_EXERCISE\_BIKE

 | 

'0BF'

 | 

Spinning bike.

 |
| 

HDK\_ROWING\_MACHINE

 | 

'0C1'

 | 

Rower.

 |
| 

HDK\_ELLIPTICAL\_MACHINE

 | 

'0C0'

 | 

Elliptical machine.

 |
| 

HDK\_WALKING\_MACHINE

 | 

'092'

 | 

Air walker.

 |
| 

SPORTS\_GENIE

 | 

'A12'

 | 

Running form monitoring device.

 |

#### DeviceInfo

Device information class.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

uniqueId

 | 

string

 | 

Yes

 | 

No

 | 

Unique device ID. The length is less than 256 bytes.

 |
| 

udid

 | 

string

 | 

Yes

 | 

Yes

 | 

Device UDID. The value is left empty by default.

 |
| 

name

 | 

string

 | 

Yes

 | 

Yes

 | 

Device name. The length is less than 256 bytes. (This parameter is mandatory when a data source is inserted.)

 |
| 

category

 | 

[DeviceCategory](#en-us_topic_0000001768344397_section178320191510)

 | 

Yes

 | 

Yes

 | 

Device type, which must match the value of **productId**. (This parameter is mandatory when a data source is inserted.)

 |
| 

productId

 | 

string

 | 

Yes

 | 

Yes

 | 

Huawei ecosystem product ID. This must align with the category. The length is less than 256 bytes. (This parameter is mandatory when a data source is inserted.)

For example, in a manual input scenario:

category: [DeviceCategory](#en-us_topic_0000001768344397_section178320191510).MANUAL\_INPUT

productId: '0062'

 |
| 

model

 | 

string

 | 

Yes

 | 

Yes

 | 

Device model name. The value is left empty by default.

 |
| 

manufacturer

 | 

string

 | 

Yes

 | 

Yes

 | 

Device manufacturer. The value is left empty by default.

 |
| 

mac

 | 

string

 | 

Yes

 | 

Yes

 | 

Device MAC address. The value is left empty by default.

 |
| 

sn

 | 

string

 | 

Yes

 | 

Yes

 | 

Device SN. The value is left empty by default.

 |
| 

hardwareVersion

 | 

string

 | 

Yes

 | 

Yes

 | 

Device hardware version. The value is left empty by default.

 |
| 

softwareVersion

 | 

string

 | 

Yes

 | 

Yes

 | 

Device software version. The value is left empty by default.

 |
| 

firmwareVersion

 | 

string

 | 

Yes

 | 

Yes

 | 

Device firmware version. The value is left empty by default.

 |

#### ExerciseSequence

ExerciseSequence<K extends Record<string, [ExerciseSummary](#section5452655143320)\> = Record<string, [ExerciseSummary](#section5452655143320)\>,DK extends Record<string, [SequencePoint](#section244154911570)\[\]> = Record<string, [SequencePoint](#section244154911570)\[\]>>

Workout record data class, which inherits from [SampleDataBase](#section1327119123313).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

exerciseType

 | 

[SubDataType](#en-us_topic_0000001768344397_section1928718141247)

 | 

No

 | 

No

 | 

Subdata type of workout records.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Workout duration, in milliseconds. If this parameter is not set, the default value is the end time minus the start time.

Value range: (0, ∞)

 |
| 

summaries

 | 

Pick<K, keyof K>

 | 

No

 | 

No

 | 

Statistical data. For details about the statistical data types associated with workout records, please refer to the model defined in [exerciseSequenceHelper](../fitness-and-health-data-type-constants-and-model-definitions/exercisesequencehelper-exercise-record-type-constant/document.md).

 |
| 

details

 | 

Pick<DK, keyof DK>

 | 

No

 | 

Yes

 | 

Detailed data. For details about the detailed data types associated with workout records, please refer to the model defined in [exerciseSequenceHelper](../fitness-and-health-data-type-constants-and-model-definitions/exercisesequencehelper-exercise-record-type-constant/document.md). If this parameter is not set, it defaults to an empty value.

 |

#### ExerciseSequenceDeleteRequest

Workout record deletion request class, which inherits from Omit<[DataRequest](#en-us_topic_0000001768344397_section142361026204113), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

exerciseType

 | 

[SubDataType](#en-us_topic_0000001768344397_section1928718141247) | [SubDataType](#en-us_topic_0000001768344397_section1928718141247)\[\] | null

 | 

No

 | 

No

 | 

Subdata type of workout records. If this parameter is not set, all data types are deleted.

 |

#### ExerciseSequenceReadRequest

ExerciseSequenceReadRequest<DK extends Record<string, [SequencePoint](#section244154911570)\[\]> = Record<string, [SequencePoint](#section244154911570)\[\]>>

Workout record reading request class, which inherits from Omit<[DataReadRequest](#en-us_topic_0000001768344397_section15461104913472), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

exerciseType

 | 

[SubDataType](#en-us_topic_0000001768344397_section1928718141247) | [SubDataType](#en-us_topic_0000001768344397_section1928718141247)\[\] | null

 | 

No

 | 

No

 | 

Subdata type of workout records. If this parameter is not set, all data types are read.

 |
| 

readOptions

 | 

[SequenceReadOptions](#section83641141804)<DK>

 | 

No

 | 

Yes

 | 

Details data option. If this parameter is not set, details data is not read by default.

 |

#### ExerciseSummary

Workout record statistics class.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

\[P: string\]

 | 

[HealthValueType](#en-us_topic_0000001768344397_section14966196131311) | [PaceValueType](#section1842384565915)

 | 

No

 | 

No

 | 

Statistical data field.

 |

#### GroupOption

Aggregation group options.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

unitType

 | 

[GroupUnitType](#section6754124511337)

 | 

No

 | 

No

 | 

Aggregation metric (group unit).

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Number of units in each group. If this parameter is not set, the default value is **1**, indicating one unit in each group. The **duration** can only be **1** if aggregation is performed by day.

 |

#### GroupUnitType

Aggregation metric (group unit) enum object.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

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

DAY

 | 

3

 | 

Data aggregation by day.

 |

#### HealthSequence

HealthSequence<K extends Record<string, [HealthValueType](#en-us_topic_0000001768344397_section14966196131311)\> = Record<string, [HealthValueType](#en-us_topic_0000001768344397_section14966196131311)\>,DK extends Record<string, [SequencePoint](#section244154911570)\[\]> = Record<string, [SequencePoint](#section244154911570)\[\]>>

Health record data class, which inherits from [SampleDataBase](#section1327119123313).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

summaries

 | 

Pick<K, keyof K>

 | 

No

 | 

No

 | 

Statistical data. For details about the statistical data types associated with health records, please refer to the model defined in [healthSequenceHelper](../fitness-and-health-data-type-constants-and-model-definitions/healthsequencehelper-health-record-type-constant/document.md).

 |
| 

details

 | 

Pick<DK, keyof DK>

 | 

No

 | 

Yes

 | 

Detailed data. For details about the detailed data types associated with health records, please refer to the model defined in [healthSequenceHelper](../fitness-and-health-data-type-constants-and-model-definitions/healthsequencehelper-health-record-type-constant/document.md). If this parameter is not set, it defaults to an empty value.

 |

#### HealthSequenceDeleteRequest

Health record deletion request class, which inherits from Omit<[DataRequest](#en-us_topic_0000001768344397_section142361026204113), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

healthSequenceDataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298) | [DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Health data type.

 |

#### HealthSequenceReadRequest

HealthSequenceReadRequest<DK extends Record<string, [SequencePoint](#section244154911570)\[\]> = Record<string, [SequencePoint](#section244154911570)\[\]>>

Health record reading request class, which inherits from Omit<[DataReadRequest](#en-us_topic_0000001768344397_section15461104913472), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

healthSequenceDataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298) | [DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Health data type.

 |
| 

readOptions

 | 

[SequenceReadOptions](#section83641141804)<DK>

 | 

No

 | 

Yes

 | 

Details data option. If this parameter is not set, details data is not read by default.

 |

#### HealthValueType

type HealthValueType = number | string | boolean | undefined

Health and fitness data value type.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

The value can be any number.

 |
| 

string

 | 

The value can be any character string.

 |
| 

boolean

 | 

The value can be **true** or **false**. The specific meaning varies depending on the actual situation.

 |
| 

undefined

 | 

The value is empty.

**Start version**: 6.0.1(21)

 |

#### PaceValueType

type PaceValueType = Record<string, number>

Pace data type.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<string, number>

 | 

Pace data field.

 |

#### SampleDataBase

Health data base class.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)

 | 

No

 | 

No

 | 

Data type.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

dataSourceId

 | 

string

 | 

No

 | 

No

 | 

Unique ID of a data source.

 |
| 

localDate

 | 

string

 | 

No

 | 

No

 | 

Local date of data, in MM/DD/YYYY format.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

startTime

 | 

number

 | 

No

 | 

No

 | 

Data start time. The value is a Unix timestamp in milliseconds.

Value range: (0, ∞)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

endTime

 | 

number

 | 

No

 | 

No

 | 

Data end time. The value is a Unix timestamp in milliseconds.

Value range: (0, ∞)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

timeZone

 | 

string

 | 

No

 | 

No

 | 

Time zone where the data is located, in the format '+0800'.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

modifiedTime

 | 

number

 | 

No

 | 

No

 | 

Creation or modification time. The value is a Unix timestamp in milliseconds.

Value range: (0, ∞)

 |

#### SamplePoint

SamplePoint<K extends Record<string, [HealthValueType](#en-us_topic_0000001768344397_section14966196131311)\> = Record<string, [HealthValueType](#en-us_topic_0000001768344397_section14966196131311)\>>

Data sampling point, which inherits from [SampleDataBase](#section1327119123313).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fields

 | 

Pick<K, keyof K>

 | 

No

 | 

No

 | 

Data field. For details about the field matching each data type, please refer to the model defined in [samplePointHelper](../fitness-and-health-data-type-constants-and-model-definitions/samplepointhelper-sampling-data-type-constants/document.md).

 |

#### SamplePointDeleteRequest

type SamplePointDeleteRequest = UnixTimeBasedDataDeleteRequest

Data sampling point deletion request, which inherits from Omit<[DataRequest](#en-us_topic_0000001768344397_section142361026204113), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298) | [DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data type to be deleted.

 |

#### SamplePointReadRequest

SamplePointReadRequest<FK extends Record<string, [HealthValueType](#en-us_topic_0000001768344397_section14966196131311)\> = Record<string, [HealthValueType](#en-us_topic_0000001768344397_section14966196131311)\>>

Data sampling point reading request, which inherits from Omit<[DataReadRequest](#en-us_topic_0000001768344397_section15461104913472), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

samplePointDataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298)| [DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Type of the data to be queried.

 |
| 

fields

 | 

Partial<Pick<FK, keyof FK>>

 | 

No

 | 

Yes

 | 

List of fields to be read. If **samplePointDataType** is set to an array, **fields** cannot be set. For details about the field matching each data type, please refer to the model defined in [samplePointHelper](../fitness-and-health-data-type-constants-and-model-definitions/samplepointhelper-sampling-data-type-constants/document.md). If this parameter is not set, all fields are read.

 |

#### SequencePoint

Detailed health and fitness data points.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startTime

 | 

number

 | 

No

 | 

No

 | 

Data start time. The value is a Unix timestamp in milliseconds.

Value range: (0, ∞)

 |
| 

\[P: string\]

 | 

[HealthValueType](#en-us_topic_0000001768344397_section14966196131311)

 | 

No

 | 

No

 | 

Detailed data point field.

 |

#### SequenceReadOptions

SequenceReadOptions<DK extends Record<string, [SequencePoint](#section244154911570)\[\]> = Record<string, [SequencePoint](#section244154911570)\[\]>>

Option class for reading health and fitness record details.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

withDetails

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to read all details. Value **true** indicates to read all details, and value **false** indicates not to read any details. If this parameter is not set, the **withPartialDetails** parameter takes effect.

 |
| 

withPartialDetails

 | 

(keyof DK)\[\]

 | 

No

 | 

Yes

 | 

Indicates to read details of certain data types. (Set this parameter only when **withDetails** is not set.) For details about the details data types associated with workout records and health records, please refer to the models defined in [exerciseSequenceHelper](../fitness-and-health-data-type-constants-and-model-definitions/exercisesequencehelper-exercise-record-type-constant/document.md) and [healthSequenceHelper](../fitness-and-health-data-type-constants-and-model-definitions/healthsequencehelper-health-record-type-constant/document.md), respectively.

 |

#### SequenceValueType

type SequenceValueType = number | string | boolean | object

Health and fitness data value type.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

The value can be any number.

 |
| 

string

 | 

The value can be any character string.

 |
| 

boolean

 | 

The value can be **true** or **false**. The specific meaning varies depending on the actual situation.

 |
| 

object

 | 

The value can be any object.

 |

#### SortOrder

Sort order enum object.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

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

ASC

 | 

0

 | 

Ascending order.

 |
| 

DESC

 | 

1

 | 

Descending order.

 |

#### SubDataType

type SubDataType = DataType

Subdata type.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

Yes

 | 

No

 | 

Unique ID of a subdata type.

 |
| 

name

 | 

string

 | 

Yes

 | 

Yes

 | 

Name of a subdata type. If this parameter is not set, the name matching the subdata type ID is used by default.

 |

#### UnixTimeBasedDataDeleteRequest

Base class of the request for deleting data by Unix timestamp, which inherits from Omit<[DataRequest](#en-us_topic_0000001768344397_section142361026204113), 'startLocalDate' | 'endLocalDate'>.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataType

 | 

[DataType](#en-us_topic_0000001768344397_section136147472298) | [DataType](#en-us_topic_0000001768344397_section136147472298)\[\]

 | 

No

 | 

No

 | 

Data type to be deleted.

 |

#### healthStore.init

init(context: common.Context): Promise<void>

This API is used to initialize Health Service Kit. It returns the result asynchronously through a promise. Call this API before calling other APIs when you call the kit for the first time.

This API can be used to develop wearable apps since API 19 Release.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Currently, the options are [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V14/js-apis-app-ability-uiability-V14) and [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types.

 |

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthStore.init(this.getUIContext().getHostContext());
  hilog.info(0x0000, 'testTag', 'Succeeded in initing.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to init. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.insertDataSource

insertDataSource(dataSource: DataSourceBase): Promise<string>

Inserts a specific data source. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

dataSource

 | 

[DataSourceBase](#section137003251628)

 | 

Yes

 | 

Constructed data source.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise object, which returns the unique ID (**dataSourceId**) of the data source.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/-g0IPGJ8SFCTqbSbbZxjgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3AB73050D838A05C109259992D47BD8D666E3611660FB6C56CD9A0B468E517E)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let dataSource: healthStore.DataSourceBase = {
  deviceInfo: {
    uniqueId: 'test',
    name: 'test', // This field is mandatory when a data source is inserted.
    category: healthStore.DeviceCategory.WEARABLE\_BAND, // This field is mandatory when a data source is inserted.
    productId: '0554', // This field is mandatory when a data source is inserted.
    model: 'lotana',
    manufacturer: 'HUAWEI',
    mac: 'testDeviceMac',
    sn: 'testDeviceSn',
    hardwareVersion: '1',
    softwareVersion: '2',
    firmwareVersion: '3',
    udid: ''
  }
}

try {
  const dataSourceId = await healthStore.insertDataSource(dataSource);
  hilog.info(0x0000, 'testTag', \`Succeeded in inserting dataSource, the dataSourceId is ${dataSourceId}.\`);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to insert dataSource. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.readDataSource

readDataSource(request: DataSourceReadRequest): Promise<DataSource\[\]>

Reads the data source. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[DataSourceReadRequest](#section13571101918281)

 | 

Yes

 | 

Request for reading the data source.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[DataSource](#en-us_topic_0000001768344397_section197195291918)\[\]>

 | 

Promise object, which returns the [DataSource](#en-us_topic_0000001768344397_section197195291918) array.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7clAe1o4SF-g_0LHw-9lFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44CD4C705AB42A83581A4309DF22713B38EB3CA4398DC3D770C660F4B89B5B65)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let readSourceRequest: healthStore.DataSourceReadRequest = {
  deviceUniqueId: 'testudidupdate'
}

try {
  let dataSources = await healthStore.readDataSource(readSourceRequest);
  dataSources.forEach((dataSource) => {
    hilog.info(0x0000, 'testTag', \`Succeeded in reading dataSource, the dataSourceId is ${dataSource.dataSourceId}.\`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to read dataSource. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.updateDataSource

updateDataSource(dataSource: DataSource): Promise<void>

Updates the data source. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

dataSource

 | 

[DataSource](#en-us_topic_0000001768344397_section197195291918)

 | 

Yes

 | 

Data source to be updated.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/l6uqBkkTQUK2VqnWB1iFIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BC395C308C196774CE8D60E22ABB4FB23CEB8A61FE24D061C98EC0E1D51EE45)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let newDataSource: healthStore.DataSource = {
  deviceInfo: {
    uniqueId: 'test',
    name: 'test',
    category: healthStore.DeviceCategory.WEARABLE\_BAND,
    productId: '0554',
    model: 'lotana',
    manufacturer: 'HUAWEI',
    mac: 'testDeviceMac',
    sn: 'testDeviceSn',
    hardwareVersion: '1',
    softwareVersion: '2',
    firmwareVersion: '3',
    // Update the UDID.
    udid: 'updateudid'
  },
  // Pass the value of **dataSourceId** returned when you insert the data source during the development.
  dataSourceId: 'xxx'
}

try {
  await healthStore.updateDataSource(newDataSource);
  hilog.info(0x0000, 'testTag', 'Succeeded in updating dataSource.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to update dataSource. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.saveData

saveData(sampleData: SamplePoint\[\] | SamplePoint): Promise<void>

Saves data sampling points. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

sampleData

 | 

[SamplePoint](#section341712418323)\[\] | [SamplePoint](#section341712418323)

 | 

Yes

 | 

A single data sampling point or an array of data sampling points.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/cbUf0MmvRHi_h4BUn4o0yA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03A8E4C36E2BAD05B24AEC5113FBAFB64E4A7029E6DCE0470B865ECBCAA83E66)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let samplePoint: healthStore.SamplePoint = {
  dataType: healthStore.samplePointHelper.bodyTemperature.DATA\_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000,
  localDate: '10/30/2023',
  timeZone: '+0800',
  modifiedTime: 1698633801000,
  // Pass the value of **DataSourceId** returned when you call **insertDataSource** to insert the data source.
  dataSourceId: 'xxx',
  fields: {
    bodyTemperature: 39
  }
}

try {
  await healthStore.saveData(samplePoint);
  hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to save data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.saveData

saveData(exerciseSequence: ExerciseSequence\[\] | ExerciseSequence): Promise<void>

Saves workout records. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

exerciseSequence

 | 

[ExerciseSequence](#section17704373316)\[\] | [ExerciseSequence](#section17704373316)

 | 

Yes

 | 

A single workout record or an array of workout records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/xS-sXs42Qzmw-7Gznlb5GA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCB2BE6E20ACF5DA31E781F464663F7C94FEE6C3509ABFC6752D51C033D47C0B)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Construct a running record.
const startTime = 1698040800000; // 2023-10-23 14:00:00
const endTime = 1698042600000; // 2023-10-23 14:30:00

const runningSequence: healthStore.exerciseSequenceHelper.running.Model = {
  dataType: healthStore.exerciseSequenceHelper.DATA\_TYPE,
  // Pass the value of **DataSourceId** returned when you call **insertDataSource** to insert the data source.
  dataSourceId: 'xxx',
  startTime: startTime, // 2023-10-23 14:00:00
  endTime: endTime, // 2023-10-23 14:30:00
  localDate: '10/23/2023',
  timeZone: '+0800',
  modifiedTime: new Date().getTime(),
  exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE,
  duration: 1800000,
  summaries: {
    distance: {
      totalDistance: 2000
    },
    calorie: {
      totalCalories: 20
    },
    speed: {
      avg: 5,
      max: 6
    }
  },
  details: {
    exerciseHeartRate: \[
      {
        startTime: startTime,
        bpm: 88
      },
      {
        startTime: startTime + 5000,
        bpm: 89
      }
    \],
    speed: \[
      {
        startTime: startTime,
        speed: 2.5
      }, 
      {
        startTime: startTime + 5000,
        speed: 2.3
      }
    \],
    altitude: \[
      {
        startTime: startTime,
        altitude: 100
      }, 
      {
        startTime: startTime + 5000,
        altitude: 101
      }
    \]
  }
};
try {
  await healthStore.saveData(runningSequence);
  hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to save data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.saveData

saveData(healthSequence: HealthSequence\[\] | HealthSequence): Promise<void>

Saves health records. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

healthSequence

 | 

[HealthSequence](#section1038711561532)\[\] | [HealthSequence](#section1038711561532)

 | 

Yes

 | 

A single health record or an array of health records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Cj7iP3cnRcaDlIj5CPomiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D06230EF8DAAE19B58F13422204B1B215985A8A7A2D0DCC2177E3F11B3482F)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let healthSequence: healthStore.healthSequenceHelper.sleepRecord.Model = {
  summaries: {
    fallAsleepTime: 1695740400000, // 2023-09-26 23:00:00
    wakeupTime: 1695769200000, // 2023-09-27 7:00:00
    sleepScore: 80,
    wakeCount: 2,
    sleepType: 1,
    shallowDuration: 14400,
    deepDuration: 7200,
    dreamDuration: 7200,
    wakeDuration: 0,
    duration: 28800
  },
  dataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
  // Pass the value of **DataSourceId** returned when you call **insertDataSource** to insert the data source.
  dataSourceId: 'xxx',
  localDate: '09/26/2023',
  startTime: 1695740400000,
  endTime: 1695769200000,
  timeZone: '+0800',
  modifiedTime: 1695769200000,
  details: {
    sleepSegment: \[
      {
        startTime: 1695740400000, // 2023-09-26 23:00:00
        endTime: 1695747600000, // 2023-09-27 01:00:00
        sleepStatus: 2
      },
      {
        startTime: 1695747600000, // 2023-09-27 01:00:00
        endTime: 1695754800000, // 2023-09-27 03:00:00
        sleepStatus: 1
      },
      {
        startTime: 1695754800000, // 2023-09-27 03:00:00
        endTime: 1695762000000, // 2023-09-27 05:00:00
        sleepStatus: 3
      },
      {
        startTime: 1695762000000, // 2023-09-27 05:00:00
        endTime: 1695769200000, // 2023-09-27 07:00:00
        sleepStatus: 2
      }
    \]
  }
}
try {
  await healthStore.saveData(healthSequence);
  hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to save data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.readData

readData<T extends SamplePoint>(request: SamplePointReadRequest): Promise<T\[\]>

Reads data sampling points. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[SamplePointReadRequest](#section1419811172920)

 | 

Yes

 | 

Request for reading data sampling points. The time span is 31 days.

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

Promise object, with **T** inheriting from [SamplePoint](#section341712418323). Returns an array of data sampling points.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/SIPFCYKuSmSswrW3BLFH7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=393EB57E0EA71DDFF6E3C7A27FA8DC888046DC0ACAB9500FE468660366F253FB)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let samplePointReadRequest: healthStore.SamplePointReadRequest = {
  samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA\_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000,
  fields: {
    bodyTemperature: 39
  }
}

try {
  let samplePoints = await healthStore.readData(samplePointReadRequest);
  samplePoints.forEach((samplePoint) => {
    hilog.info(0x0000, 'testTag', \`Succeeded in reading data, the bodyTemperature is ${samplePoint.fields.bodyTemperature}.\`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to read data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.readData

readData<T extends ExerciseSequence>(request: ExerciseSequenceReadRequest): Promise<T\[\]>

Reads workout records. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[ExerciseSequenceReadRequest](#section17500162113363)

 | 

Yes

 | 

Request for reading workout records. The time span is 31 days.

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

Promise object, with **T** inheriting from [ExerciseSequence](#section17704373316). Returns an array of workout records.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/HJ0bYwhdQy64xAzY_lRKlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EE0EB5BFB3677CABB8B4DE8FF20CB9154CABA1D206A018EA9C4B9721482E38B)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Query running records.
const startTime = 1698040800000; // 2023-10-23 14:00:00
const endTime = 1698042600000; // 2023-10-23 14:30:00

const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
  startTime: startTime,
  endTime: endTime,
  exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE,
  count: 1,
  sortOrder: 1,
  readOptions: {
    withPartialDetails: \['exerciseHeartRate', 'altitude'\] 
 }
};
try {
  const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
  runningSequences.forEach((runningSequence) => {
    hilog.info(0x0000, 'testTag', \`the start time is ${runningSequence.startTime}.\`);
    hilog.info(0x0000, 'testTag', \`the end time is ${runningSequence.endTime}.\`);
    Object.keys(runningSequence.summaries).forEach((key) => {
      Object.keys(runningSequence.summaries\[key\]).forEach((fieldName) => {
        hilog.info(0x0000, 'testTag', \`the summaries of ${key} field ${fieldName} is ${runningSequence.summaries\[key\]\[fieldName\]}.\`);
      });
    });
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to read data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.readData

readData<T extends HealthSequence>(request: HealthSequenceReadRequest): Promise<T\[\]>

Reads health records. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[HealthSequenceReadRequest](#section11615192919718)

 | 

Yes

 | 

Request for reading health records. The time span is 31 days.

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

Promise object, with **T** inheriting from [HealthSequence](#section1038711561532). Returns an array of health records.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/FU1Hi6cnTImR0PEHA6_4jQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D3164DBF4FA76C45A14B1B7E4B48D5C94EDF38945CB5152E231A23AE1CC756F)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
  healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
  startTime: 1695740400000,
  endTime: 1695769200000,
  readOptions: {
    withDetails: true
  }
}
try {
  const healthSequences = await healthStore.readData(healthSequenceReadRequest);
  
  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.'); 
  healthSequences.forEach((healthSequence) => {
    hilog.info(0x0000, 'testTag', \`the start time is ${healthSequence.startTime}.\`);
    hilog.info(0x0000, 'testTag', \`the end time is ${healthSequence.endTime}.\`);
    Object.keys(healthSequence.summaries).forEach((key) => {
      hilog.info(0x0000, 'testTag', \`the summaries of ${key} is ${healthSequence.summaries\[key\]}.\`);
    });
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to read data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.deleteData

deleteData(request: SamplePointDeleteRequest | SamplePointDeleteRequest\[\]): Promise<void>

Deletes data sampling points. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[SamplePointDeleteRequest](#section1680218365918) | [SamplePointDeleteRequest](#section1680218365918)\[\]

 | 

Yes

 | 

Request for deleting data sampling points.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/y7BK-yDJQTOp4CdiO_4GVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=184B48032579F7BFB17AF2F6B3A502EFCCD6B45E314D00ED52A9C98845879D71)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let samplePointDeleteRequest: healthStore.SamplePointDeleteRequest = {
  dataType: healthStore.samplePointHelper.bodyTemperature.DATA\_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000
}

try {
  await healthStore.deleteData(samplePointDeleteRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.deleteData

deleteData(request: ExerciseSequenceDeleteRequest | ExerciseSequenceDeleteRequest\[\]): Promise<void>

Deletes workout records. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[ExerciseSequenceDeleteRequest](#section207708111867) | [ExerciseSequenceDeleteRequest](#section207708111867)\[\]

 | 

Yes

 | 

Request for deleting workout records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/7aAH85ySTFq8Xp-RRBFqYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A7DE85C8D4FB799A2CEB7F41213CE86C30BEDA39C9E1ADFA9FB2EF3B3340D8C)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let exerciseSequenceDeleteRequest: healthStore.ExerciseSequenceDeleteRequest= {
  exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000
}
try {
  await healthStore.deleteData(exerciseSequenceDeleteRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.deleteData

deleteData(request: HealthSequenceDeleteRequest | HealthSequenceDeleteRequest\[\]): Promise<void>

Deletes health records. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[HealthSequenceDeleteRequest](#section1779165141119) | [HealthSequenceDeleteRequest](#section1779165141119)\[\]

 | 

Yes

 | 

Request for deleting health records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/3PwJbq0-TC61JJJafzz2pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7324B592D5AE5D93ECE0D07E40C3931D460D385B1B38A6916A23927276FCC00)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const healthSequenceDeleteRequest: healthStore.HealthSequenceDeleteRequest = {
  healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
  startTime: 1695740400000,
  endTime: 1695769200000
}
try {
  await healthStore.deleteData(healthSequenceDeleteRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.deleteData

deleteData(samplePoint: SamplePoint | SamplePoint\[\]): Promise<void>

Deletes specific data sampling points. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

samplePoint

 | 

[SamplePoint](#section341712418323) | [SamplePoint](#section341712418323)\[\]

 | 

Yes

 | 

A single data sampling point or an array of data sampling points.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/kC_GA2lYQJmjs4aVmTkzuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3395A67726016D9A72413A36EC659F31240BEC5260FDD6F8529343168BCE3F16)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let samplePointReadRequest: healthStore.SamplePointReadRequest = {
    samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA\_TYPE,
    startTime: 1698633801000,
    endTime: 1698633801000
  }
  let samplePoints: healthStore.SamplePoint\[\] = await healthStore.readData(samplePointReadRequest);
  for (let index = 0; index < samplePoints.length; index++) {
    const samplePoint = samplePoints\[index\];
    await healthStore.deleteData(samplePoint);
  }
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.deleteData

deleteData(exerciseSequence: ExerciseSequence | ExerciseSequence\[\]): Promise<void>

Deletes specific workout records. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

exerciseSequence

 | 

[ExerciseSequence](#section17704373316) | [ExerciseSequence](#section17704373316)\[\]

 | 

Yes

 | 

A single workout record or an array of workout records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Blui5ACOT6aDr8x21xlKKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E13AA049AED968C0CC7D6293BE178DE197BA92A15C4515FAD58F0EE80A2B5C5)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Delete running records.
try {
  const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
    startTime: 1698040800000,
    endTime: 1698042600000,
    exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE
  };
  const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
  for (let index = 0; index < runningSequences.length; index++) {
    const runningSequence = runningSequences\[index\];
    await healthStore.deleteData(runningSequence);
  }
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.deleteData

deleteData(healthSequence: HealthSequence | HealthSequence\[\]): Promise<void>

Deletes specific health records. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

healthSequence

 | 

[HealthSequence](#section1038711561532) | [HealthSequence](#section1038711561532)\[\]

 | 

Yes

 | 

A single health record or an array of health records.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Y0YYyN6eS3uCAsjmPY9QyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CEB6CD2CD8F781ED653086A2347C16E028501F42BC9EEC240462B6D58086866)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
    healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
    startTime: 1695740400000,
    endTime: 1695769200000
  }
  const healthSequences = await healthStore.readData(healthSequenceReadRequest);
  for (let index = 0; index < healthSequences.length; index++) {
    const healthSequence = healthSequences\[index\];
    await healthStore.deleteData(healthSequence);
  }
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.aggregateData

aggregateData<T extends AggregateResult>(request: AggregateRequest | AggregateRequest\[\]): Promise<T\[\]>

Performs aggregation queries. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 1002700001.

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[AggregateRequest](#section599483722019) | [AggregateRequest](#section599483722019)\[\]

 | 

Yes

 | 

Request for performing an aggregation query.

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

Promise object, with **T** inheriting from [AggregateResult](#section19656142151412). Returns an array of aggregation query results.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/7ZuvCx39TiymBfYYdJQkAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F386D3F4C47254698FFC788AB66EB3FBE8BB21097820B48DFE92FA5C6395271D)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let aggregateRequest: healthStore.AggregateRequest<healthStore.samplePointHelper.dailyActivities.AggregateFields> = {
  dataType: healthStore.samplePointHelper.dailyActivities.DATA\_TYPE,
  metrics: {
    step: \['sum'\],
    calorie: \['sum'\],
    distance: \['sum'\],
    climbHighAltitude:\['sum'\],
    isIntensity: \['sum'\],
    isStand: \['sum'\]
 },
  groupBy: {
    unitType: 3,
    duration: 0
  },
  startLocalDate: '10/30/2023',
  endLocalDate: '10/30/2023'
}

try {
  const aggregateResults = await healthStore.aggregateData<healthStore.samplePointHelper.dailyActivities.AggregateResult>(aggregateRequest);
  
  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
  aggregateResults.forEach((aggregateResult) => {
    hilog.info(0x0000, 'testTag', \`the start time is ${aggregateResult.startTime}.\`);
    hilog.info(0x0000, 'testTag', \`the end time is ${aggregateResult.endTime}.\`);
    Object.keys(aggregateResult.fields).forEach((fieldName) => {
      hilog.info(0x0000, 'testTag', \`the sum of ${fieldName} is ${aggregateResult.fields\[fieldName\].sum}.\`);
    });
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to read data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.requestAuthorizations

requestAuthorizations(context: common.UIAbilityContext, request: AuthorizationRequest): Promise<AuthorizationResponse>

Requests user authorization. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)

 | 

Yes

 | 

UIAbility context.

 |
| 

request

 | 

[AuthorizationRequest](#en-us_topic_0000001768344397_section1956619544498)

 | 

Yes

 | 

Authorization request. Make sure you have applied for the scopes specified in the authorization parameters during your Health Service Kit application.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthorizationResponse](#en-us_topic_0000001768344397_section963483625117)\>

 | 

Promise object, which returns the authorization response result.

 |

**Result codes**:

For details about the following error codes, please refer to [Health Service Kit ArkTS API Error Codes](../../arkts-api-error-codes/document.md). For details about other error codes, please refer to [Account Kit ArkTS Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V13/account-api-error-code-V13).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Lslb4axRTsa0a9iGx5WrKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E103E713D2D5C65809DA0000A7D7B70938BBBF8CCB4C04DE1D18C7A3B27949FD)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

let authorizationParameter: healthStore.AuthorizationRequest = {
  readDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\],
  writeDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\]
}

try {
  let authorizationResponse = await healthStore.requestAuthorizations(this.getUIContext().getHostContext() as common.UIAbilityContext, authorizationParameter);
  
  hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
  authorizationResponse.writeDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', \`grantedWriteDataType is : ${dataType.name}\`);
  });
  authorizationResponse.readDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', \`grantedReadDataTypes is : ${dataType.name}\`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to request authorization. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.getAuthorizations

getAuthorizations(request: AuthorizationRequest): Promise<AuthorizationResponse>

Queries the authorization. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[AuthorizationRequest](#en-us_topic_0000001768344397_section1956619544498)

 | 

Yes

 | 

Authorization querying request.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthorizationResponse](#en-us_topic_0000001768344397_section963483625117)\>

 | 

Promise object, which returns the authorization query result.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[401](../../arkts-api-error-codes/document.md#section1598111146271)

 | 

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/FcdwNx6zSeSUqLWasq6BQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DBA058D81C3C368A9C17161B06F6330E4649D7B8BC9A785396EF5EDC359F6D9)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let queryAuthorizationRequest: healthStore.AuthorizationRequest = {
  readDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\],
  writeDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\]
}

try {
  let queryAuthorizationResponse = await healthStore.getAuthorizations(queryAuthorizationRequest);
  
  hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
  queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', \`grantedWriteDataType is : ${dataType.name}\`);
  });
  queryAuthorizationResponse.readDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', \`grantedReadDataTypes is : ${dataType.name}\`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to get authorization. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.cancelAuthorizations

cancelAuthorizations(): Promise<void>

Cancels user authorization. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the following error codes, please refer to [Health Service Kit ArkTS API Error Codes](../../arkts-api-error-codes/document.md). For details about other error codes, please refer to [Account Kit ArkTS Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V13/account-api-error-code-V13).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/x4Elmn0qTneaYCA6pwQJkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C31C591A6A0311DA79B6A2E4FEA5ADC79882F9692E9D530D047C7893D0C1F1C9)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthStore.cancelAuthorizations();
  hilog.info(0x0000, 'testTag', 'Succeeded in canceling authorization.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to cancel authorization. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.syncAll

syncAll(): Promise<void>

Proactively triggers data syncing. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthStore

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 801.

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Result codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[201](../../arkts-api-error-codes/document.md#section383228112410)

 | 

Permission verification failed.

 |
| 

[801](../../arkts-api-error-codes/document.md#section14722630151713)

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |
| 

[1002700001](../../arkts-api-error-codes/document.md#section153755119333)

 | 

System internal error.

 |
| 

[1002700002](../../arkts-api-error-codes/document.md#section1210612513414)

 | 

Database processing error.

 |
| 

[1002701001](../../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error. The network is unavailable.

 |
| 

[1002702001](../../arkts-api-error-codes/document.md#section673773124213)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1002702002](../../arkts-api-error-codes/document.md#section1283610451436)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1002703001](../../arkts-api-error-codes/document.md#section9390213122310)

 | 

User privacy is not agreed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ucBQdYLERUGoE2VqxOPCqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FE876E4C292C860272F9695DEEC01725722A2FF543722168928C8CAB5ED5A2A)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthStore.syncAll();
  hilog.info(0x0000, 'testTag', 'Succeeded in synchronizing data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to synchronize data. Code: ${err.code}, message: ${err.message}\`);
}

#### healthStore.on('serviceDie')

on(type: 'serviceDie', callback: Callback<void>): void

Subscribes to Health Service Kit process destruction notifications. This API returns the result asynchronously through a callback.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.1.0(18)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Health Service Kit process status type. This field has a fixed value of **serviceDie**. This event is triggered when the Health Service Kit process is destroyed.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no value.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/89-5qk9TTMeNzPj5ZV3-lQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51EC4E0B33A3CFEA7064DB49C6B791CB90A80633A680667525268A83C19BFDD1)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

healthStore.on('serviceDie', () => {
  hilog.info(0x0000, 'testTag', 'Succeeded in monitoring the process death.');
});

#### healthStore.off('serviceDie')

off(type: 'serviceDie', callback?: Callback<void>): void

Unsubscribe from Health Service Kit process destruction notifications. This API returns the result asynchronously through a callback.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthStore

**Start version**: 5.1.0(18)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Health Service Kit process status type. This field has a fixed value of **serviceDie**. This event is triggered when the Health Service Kit process is destroyed.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no value.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/uoAPrgc8SoykcgHxr9rxNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDDD4D829A41E1EAAF3DFAC56C29C0962441361C50F4C077B823E044FB307579)

Before calling these APIs, call [init](#section1571935817328) to perform initialization.

**Example:**

import { healthStore } from '@kit.HealthServiceKit';

healthStore.off('serviceDie');
