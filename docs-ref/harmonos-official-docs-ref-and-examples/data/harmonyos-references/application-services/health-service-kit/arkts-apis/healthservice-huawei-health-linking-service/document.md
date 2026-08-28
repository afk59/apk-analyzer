# healthService (Huawei Health Linking Service)

This module provides the Huawei Health linking service.

**Start version**: 5.0.0(12)

#### Module Import

import { healthService } from '@kit.HealthServiceKit';

#### SampleEvent

Linkage control event.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

eventId

 | 

number

 | 

No

 | 

No

 | 

Event ID.

 |
| 

eventLevel

 | 

number

 | 

No

 | 

No

 | 

Event level.

Value range: \[0, 255\].

 |
| 

eventData

 | 

string

 | 

No

 | 

No

 | 

Information carried in an event.

 |
| 

srcPkgName

 | 

string

 | 

No

 | 

Yes

 | 

Package name of the event source. The value is left empty by default.

 |
| 

destPkgName

 | 

string

 | 

No

 | 

Yes

 | 

Package name of the event target. The value is left empty by default.

 |

#### SampleReal

SampleReal<K extends Record<string, [healthStore.HealthValueType](../healthstore-health-and-fitness-data-services/document.md#en-us_topic_0000001768344397_section14966196131311)\> = Record<string, [healthStore.HealthValueType](../healthstore-health-and-fitness-data-services/document.md#en-us_topic_0000001768344397_section14966196131311)\>>

Linkage real-time workout data.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

dataType

 | 

[healthStore.DataType](../healthstore-health-and-fitness-data-services/document.md#en-us_topic_0000001768344397_section136147472298)

 | 

No

 | 

No

 | 

Real-time fused data type.

 |
| 

time

 | 

number

 | 

No

 | 

No

 | 

Generation time of real-time fused data. The value is a Unix timestamp in milliseconds.

 |
| 

fields

 | 

Pick<K, keyof K>

 | 

No

 | 

No

 | 

Real-time fused data field.

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

Real-time fused data source. The value is left empty by default.

 |

#### workout

Provides real-time health and fitness data.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.0.0(12)

#### \[h2\]ActivityReport

Provides real-time Activity rings data.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthService

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

steps

 | 

number

 | 

No

 | 

No

 | 

Step count.

 |
| 

stepsGoal

 | 

number

 | 

No

 | 

Yes

 | 

Step count goal (If this parameter is not set, the default goal displayed in the Huawei Health app cannot be read.)

 |
| 

activeCalories

 | 

number

 | 

No

 | 

No

 | 

Active calories.

Unit: cal

 |
| 

activeCaloriesGoal

 | 

number

 | 

No

 | 

Yes

 | 

Active calories goal.

Unit: cal

 |
| 

exercise

 | 

number

 | 

No

 | 

No

 | 

Workout duration.

Unit: minute

 |
| 

exerciseGoal

 | 

number

 | 

No

 | 

Yes

 | 

Time goal.

Unit: minute

 |
| 

activeHours

 | 

number

 | 

No

 | 

No

 | 

Hours active.

 |
| 

activeHoursGoal

 | 

number

 | 

No

 | 

Yes

 | 

Hours active goal.

 |

#### \[h2\]ConfigType

type ConfigType = number | string | boolean

Linkage configuration item type.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
Type

 | 

**Description**

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

#### \[h2\]DeviceState

Linkage device status.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

deviceId

 | 

string

 | 

No

 | 

No

 | 

Device ID.

 |
| 

state

 | 

number

 | 

No

 | 

No

 | 

Device status.

 |
| 

deviceName

 | 

string

 | 

No

 | 

Yes

 | 

Device name. The value is left empty by default.

 |

#### \[h2\]Goal

Linkage workout goal.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

number

 | 

No

 | 

No

 | 

Target type. For details about the value, see [TargetType](#section7230195122817).

 |
| 

value

 | 

number

 | 

No

 | 

No

 | 

Target value.

 |

#### \[h2\]LinkageType

Linkage type.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

COURSE\_LINK

 | 

0

 | 

Course data linking.

 |
| 

ACTIVITY\_LINK

 | 

1

 | 

Workout data linking.

 |

#### \[h2\]StartCode

Result code when the linking service is enabled.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SUCCESS

 | 

0

 | 

The linking service is enabled successfully.

 |
| 

WORKOUT\_WORKING

 | 

1

 | 

The linking service is started.

 |
| 

NO\_SUPPORTED\_DEVICE

 | 

2

 | 

No device supports the linking service.

 |
| 

DEVICE\_BUSY

 | 

3

 | 

The linkage device is busy.

 |

#### \[h2\]StartResult

Result of enabling the linking service.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startCode

 | 

[StartCode](#section16819124442317)

 | 

No

 | 

No

 | 

Result code when the linking service is enabled.

 |
| 

deviceState

 | 

[DeviceState](#section1466304421712)\[\]

 | 

No

 | 

No

 | 

Linkage device status.

 |

#### \[h2\]TargetType

Linkage target type.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

No goal.

 |
| 

DISTANCE

 | 

1

 | 

Distance.

 |
| 

CALORIE

 | 

2

 | 

Calories burned.

 |
| 

TIME

 | 

3

 | 

Duration.

 |
| 

SKIPPING\_TIMES

 | 

4

 | 

Jump times.

 |

#### \[h2\]WorkoutConfig

Linkage configuration item.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

linkageType

 | 

[LinkageType](#section15978631122119)

 | 

No

 | 

No

 | 

Linkage type.

 |
| 

sportType

 | 

number

 | 

No

 | 

No

 | 

Workout type. For details, please refer to the subdata type IDs in [Exercise Record Type Constant](../fitness-and-health-data-type-constants-and-model-definitions/exercisesequencehelper-exercise-record-type-constant/document.md).

 |
| 

activityGoals

 | 

[Goal](#section1847017072015)\[\]

 | 

No

 | 

Yes

 | 

Linkage workout goal. The value is left empty by default.

 |
| 

extensionConfig

 | 

Record<string, [ConfigType](#section895913201519)\>

 | 

No

 | 

Yes

 | 

Extended configuration item. The value is left empty by default.

 |

#### \[h2\]workout.config

config(workoutConfig: WorkoutConfig): Promise<void>

Configures the linking service. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

workoutConfig

 | 

[WorkoutConfig](#section77282239296)

 | 

Yes

 | 

Linkage configuration item.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified.

 |
| 

[1009104003](../../arkts-api-error-codes/document.md#section2796145134414)

 | 

Illegal command. Called when workout not in stoped or idle state.

 |
| 

[1009104999](../../arkts-api-error-codes/document.md#section358195916206)

 | 

System internal error.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6oNY4UL3SbO5cr6gFqEguQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D65CA99950AD5A944AB1D8C12E2481A74EB363942B2F2F91175400AE9BA4FAFC)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let workoutOptions: healthService.workout.WorkoutConfig = {
    linkageType: healthService.workout.LinkageType.COURSE\_LINK,
    sportType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE.id
  };
  await healthService.workout.config(workoutOptions);
  hilog.info(0x0000, 'testTag', 'Succeed in configuring workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to configure workout. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.start

start(): Promise<StartResult>

Enables the linking service. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[StartResult](#section103341756122412)\>

 | 

Promise that returns the result of enabling the linking service.

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

[1009104001](../../arkts-api-error-codes/document.md#section9399145163817)

 | 

Sport service busy. Workout is already started by other application.

 |
| 

[1009104002](../../arkts-api-error-codes/document.md#section1492831113409)

 | 

Unsupported sport type.

 |
| 

[1009104003](../../arkts-api-error-codes/document.md#section2796145134414)

 | 

Illegal command. Called when workout in sporting, paused or stoped state.

 |
| 

[1009104004](../../arkts-api-error-codes/document.md#section5369132174419)

 | 

Permission verification error. Application has no permission, such as Motion Permission.

 |
| 

[1009104999](../../arkts-api-error-codes/document.md#section358195916206)

 | 

System internal error.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mCFiv0EvS5y07UiuISQXXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F654B91383D3891811CF2510DD238796E28F881B9DC22EE046FA1A4497D8CE8E)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.start();
  hilog.info(0x0000, 'testTag', 'Succeed in starting workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to start workout. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.pause

pause(): Promise<void>

Pauses the linking service. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

[1009104003](../../arkts-api-error-codes/document.md#section2796145134414)

 | 

Illegal command. Called when workout in ready, paused or stoped state.

 |
| 

[1009104999](../../arkts-api-error-codes/document.md#section358195916206)

 | 

System internal error.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/yw6vuNNoT0C0J2o2O_0L_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92B46970683178A634772D905F0839268EC19D46FC63F93B1E760AE17C74B4C1)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.pause();
  hilog.info(0x0000, 'testTag', 'Succeed in pausing workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to pause workout. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.resume

resume(): Promise<void>

Resumes the linking service. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

[1009104003](../../arkts-api-error-codes/document.md#section2796145134414)

 | 

Illegal command. Called when workout in ready, sporting or stoped state.

 |
| 

[1009104999](../../arkts-api-error-codes/document.md#section358195916206)

 | 

System internal error.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/nU2ZWwCOQJu_v12mkYtVZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C23808C7AC2D572228C815C8D19F5951E3A3EEE4929393405E2C408A0729B694)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.resume();
  hilog.info(0x0000, 'testTag', 'Succeed in resuming workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to resume workout. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.stop

stop(): Promise<void>

Stops the linking service. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

[1009104003](../../arkts-api-error-codes/document.md#section2796145134414)

 | 

Illegal command. Called when workout is not started.

 |
| 

[1009104999](../../arkts-api-error-codes/document.md#section358195916206)

 | 

System internal error.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/kl91brWsTJamPL-g8OwlaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A70D30AF057D4F8C7FCB2850D10EB8C90B58DCD4EC12BCCDC01AA244C483A97)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.stop();
  hilog.info(0x0000, 'testTag', 'Succeed in stopping workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to stop workout. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.onData

onData(dataType: healthStore.DataType, listener: Callback<SampleReal\[\]>): Promise<void>

Registers a listener for the specified linkage workout data. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

dataType

 | 

[healthStore.DataType](../healthstore-health-and-fitness-data-services/document.md#en-us_topic_0000001768344397_section136147472298)

 | 

Yes

 | 

Linkage workout data type.

 |
| 

listener

 | 

Callback<[SampleReal](#section133382582612)\[\]>

 | 

Yes

 | 

Linkage workout data listener callback.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Iy2bRlCjTHa26cNlb4a7qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DE459A9E6F9C79D6E747B21C2E13465A63EE17EF612F0332FE962647150287A)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal\[\]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', \`Workout onData receive data. The sampleReals size is ${sampleReals.length}\`);
  };
  const realTimeMotionDataType: healthStore.DataType = {
    id: 50004
  };
  await healthService.workout.onData(realTimeMotionDataType, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to onData. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.onData

onData(dataType: undefined, listener: Callback<SampleReal\[\]>): Promise<void>

Registers a listener for all linkage workout data. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

dataType

 | 

undefined

 | 

Yes

 | 

All linkage workout data types for which the listener is registered.

 |
| 

listener

 | 

Callback<[SampleReal](#section133382582612)\[\]>

 | 

Yes

 | 

Linkage workout data listener callback.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/jKHizBWwRr6tVV7gnnEnWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18C0D58B634C767D217091AB4D0F3F761C292F0B2B41A1CA33DCCEB083DFE9B0)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal\[\]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', \`Workout onData receive data. The sampleReals size is ${sampleReals.length}\`);
  };
  await healthService.workout.onData(undefined, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to onData. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.offData

offData(dataType: healthStore.DataType, listener: Callback<SampleReal\[\]>): Promise<void>

Cancels the listener for the specified linkage workout data. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

dataType

 | 

[healthStore.DataType](../healthstore-health-and-fitness-data-services/document.md#en-us_topic_0000001768344397_section136147472298)

 | 

Yes

 | 

Linkage workout data type.

 |
| 

listener

 | 

Callback<[SampleReal](#section133382582612)\[\]>

 | 

Yes

 | 

Linkage workout data listener callback.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/qR6742mSQES9ApQD8EHwfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=013C6B309A05FA2B83AB20DCF51980DE29103FC7B3A8B7FD0115F65DFC1FA933)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal\[\]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', \`Workout offData receive data. The sampleReals size is ${sampleReals.length}\`);
  };
  await healthService.workout.offData(healthStore.healthDataTypes.WORKOUT, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to offData. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.offData

offData(dataType: undefined, listener: Callback<SampleReal\[\]>): Promise<void>

Cancels the listener for all linkage workout data. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**System capability**: SystemCapability.Health.HealthService

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

dataType

 | 

undefined

 | 

Yes

 | 

All linkage workout data types for which the listener is registered.

 |
| 

listener

 | 

Callback<[SampleReal](#section133382582612)\[\]>

 | 

Yes

 | 

Linkage workout data listener callback.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/kVewN3-_QDqj8aPw4bvwsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21D1BC784AFFF2A4B0E008BFFEBBCE7E285DACD9153E432BE1D6BCBD6BA11037)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal\[\]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', \`Workout offData receive data. The sampleReals size is ${sampleReals.length}\`);
  };
  await healthService.workout.offData(undefined, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to offData. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.onEvent("\*")

onEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

Registers a listener for linkage device events. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthService

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 401.

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

event

 | 

string

 | 

Yes

 | 

Linkage device event type. This field has a fixed value of **\***. This event is triggered when the motion status of the linkage device is changed.

 |
| 

listener

 | 

Callback<[SampleEvent](#section599483722019)\>

 | 

Yes

 | 

Linkage device event listener callback.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/qhV8cN5HRQSMgRxKTJqZag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5790E46F1BC1BA8080BEF21471FCCD355C33CD8BFB7ADFA601A1EF9317791E4)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleEvent> = (event) => {
    hilog.info(0x0000, 'testTag', \`Workout onEvent receive event. Event data: ${event.eventData}, event id: ${event.eventId}\`);
  };
  await healthService.workout.onEvent('\*', callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to onEvent. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.offEvent("\*")

offEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

Cancels the listener for linkage device events. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthService

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 401.

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

event

 | 

string

 | 

Yes

 | 

Linkage device event type. This field has a fixed value of **\***. This event is triggered when the motion status of the linkage device is changed.

 |
| 

listener

 | 

Callback<[SampleEvent](#section599483722019)\>

 | 

Yes

 | 

Linkage device event listener callback.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/Ual0uggRTaqICTk4W904Zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F7BDE532F0D3C5EBAE947164D0289AAE55EBD44953EB3F00D8AD89301A435C4)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleEvent> = (event) => {
    hilog.info(0x0000, 'testTag', \`Workout offEvent receive event. Event data: ${event.eventData}, event id: ${event.eventId}\`);
  };
  await healthService.workout.offEvent('\*', callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to offEvent. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.readActivityReport

readActivityReport(): Promise<ActivityReport>

Reads real-time Activity rings data. This API returns the result asynchronously through a promise.

This API can be used to develop wearable apps since API 19 Release.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Health.HealthService

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ActivityReport](#section17562157135210)\>

 | 

Promise object, which returns real-time Activity rings data.

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

Permission denied.

 |
| 

[14500101](../../arkts-api-error-codes/document.md#section6671152405412)

 | 

Service exception.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/mNVLL2cPTzib37iOPgT12A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=898A732C915895EBF2C71B0E80314665A6899EB923DE69F41082ADC5A91E8FCF)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();
  
  hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
  Object.keys(result).forEach(key => {
    hilog.info(0x0000, 'testTag', \`the ${key} is ${result\[key\]}\`);
  });
} catch(err) {
  hilog.error(0x0000, 'testTag', \`Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.sendData

sendData(sampleReal: SampleReal\[\]): Promise<void>

Sends the fused workout data to the linkage device. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthService

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 401.

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

sampleReal

 | 

[SampleReal](#section133382582612)\[\]

 | 

Yes

 | 

Fused workout data.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/IOUILAXVS5OmmF8FF2LYUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79AA1E6C8D86E82E8C34764719A180E777F409F8228E8DD5FE46515434F2785C)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const sampleReal: healthService.SampleReal = {
    dataType: { id: 50004 },
    time: 1695740400000, // 2023-09-26 23:00:00,
    fields: {
      hr: 90
    }
  };
  await healthService.workout.sendData(\[sampleReal\]);
  hilog.info(0x0000, 'testTag', 'Succeed in sending data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to send data. Code: ${err.code}, message: ${err.message}\`);
}

#### \[h2\]workout.sendEvent

sendEvent(event: SampleEvent): Promise<void>

Sends the control event to the linkage device. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.HealthService

**Device behavior differences**: This API is supported on phones and tablets. On wearables, it returns error code 401.

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

event

 | 

[SampleEvent](#section599483722019)

 | 

Yes

 | 

Linkage control event.

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

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/wvnMgASjRCie-YOCmlBjUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062507Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FFFAD214B91F9E82DEE3DF52503374A1B76909F80BC38670D7A2AF380AEC8E5)

Before calling these APIs, call [init](../healthstore-health-and-fitness-data-services/document.md#section1571935817328) to perform initialization.

**Example:**

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const sampleEvent: healthService.SampleEvent = {
    eventId: 800400002,
    eventLevel: 0,
    eventData: 'start'
  };
  await healthService.workout.sendEvent(sampleEvent);
  hilog.info(0x0000, 'testTag', 'Succeed in sending event.');
} catch (err) {
  hilog.error(0x0000, 'testTag', \`Failed to send event. Code: ${err.code}, message: ${err.message}\`);
}
