# Running

The following table lists the types of running records.

| 
**Subtype Constant**

 | 

**Description**

 | 

Data Source

 |
| :-- | :-- | :-- |
| 

[exerciseSequenceHelper.running.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section1326024118404)

 | 

Outdoor running.

 | 

Mobile phones, watches, and bands

 |
| 

[exerciseSequenceHelper.indoorRunning.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section52972450370)

 | 

Indoor running/On a treadmill

 | 

Mobile phones, watches, and bands

 |
| 

[exerciseSequenceHelper.trailRunning.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section1075820157426)

 | 

Trail running.

 | 

Mobile phones, watches, and bands

 |

#### Associated Statistical Data

-   Field definition: [exerciseSequenceHelper.running.SummaryFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section526104111405)

| 
**Field**

 | 

Description

 | 

**Type**

 | 

Mandatory

 |
| :-- | :-- | :-- | :-- |
| 

distance

 | 

Distance statistics.

 | 

[DistanceSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1931022758)

 | 

Yes

 |
| 

calorie

 | 

Calories statistics.

 | 

[CalorieSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section10820034172215)

 | 

Yes

 |
| 

speed

 | 

Speed statistics.

 | 

[SpeedSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section4460144920180)

 | 

Yes

 |
| 

exerciseHeartRate

 | 

Exercise heart rate statistics.

 | 

[ExerciseHeartRateSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section61131157564)

 | 

No

 |
| 

step

 | 

Step count statistics.

 | 

[StepSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1531683122019)

 | 

No

 |
| 

cadence

 | 

Step cadence statistics.

 | 

[CadenceSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section517018141201)

 | 

No

 |
| 

altitude

 | 

Altitude statistics.

 | 

[AltitudeSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section5999164151119)

 | 

No

 |
| 

location

 | 

Location statistics.

 | 

[LocationSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section20701154013341)

 | 

No

 |
| 

runningForm

 | 

Running form statistics.

 | 

[RunningFormSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section09431418413)

 | 

No

 |
| 

runningFeature

 | 

Running feature data.

 | 

[RunningFeature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section543218206545)

 | 

No

 |

#### Associated Detailed Data

-   Field definition: [exerciseSequenceHelper.running.DetailFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section9261114111400)

| 
**Field**

 | 

Description

 | 

**Type**

 | 

Mandatory

 |
| :-- | :-- | :-- | :-- |
| 

exerciseHeartRate

 | 

Exercise heart rate details.

 | 

[ExerciseHeartRate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1011218571967)\[\]

 | 

No

 |
| 

speed

 | 

Speed details.

 | 

[Speed](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section10458134951817)\[\]

 | 

No

 |
| 

cadence

 | 

Step cadence details.

 | 

[Cadence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section625153911153)\[\]

 | 

No

 |
| 

runningForm

 | 

Running form details.

 | 

[RunningForm](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1668116459594)\[\]

 | 

No

 |
| 

location

 | 

Location details.

 | 

[Location](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1970034063415)\[\]

 | 

No

 |
| 

altitude

 | 

Altitude details.

 | 

[Altitude](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section271517115816)\[\]

 | 

No

 |
