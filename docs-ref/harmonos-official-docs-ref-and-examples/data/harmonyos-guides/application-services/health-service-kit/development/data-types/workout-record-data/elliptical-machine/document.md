# Elliptical Machine

The following table lists the types of workout records on an elliptical machine.

| 
**Subtype Constant**

 | 

**Description**

 | 

Data Source

 |
| :-- | :-- | :-- |
| 

[exerciseSequenceHelper.elliptical.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section17797111421017)

 | 

Elliptical machine.

 | 

Bands and watches

 |

#### Associated Statistical Data

Field definition: [exerciseSequenceHelper.elliptical.SummaryFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section2079861411018)

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

calorie

 | 

Calories statistics.

 | 

[CalorieSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section10820034172215)

 | 

Yes

 |
| 

distance

 | 

Distance statistics.

 | 

[DistanceSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1931022758)

 | 

No

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

speed

 | 

Speed statistics.

 | 

[SpeedSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section4460144920180)

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

resistance

 | 

Resistance statistics.

 | 

[ResistanceSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section969783754212)

 | 

No

 |
| 

pedalingCadence

 | 

Pedaling cadence statistics.

 | 

[PedalingCadenceSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section17379171873917)

 | 

No

 |
| 

power

 | 

Power statistics.

 | 

[PowerSummary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section6460410194012)

 | 

No

 |

#### Associated Detailed Data

Field definition: [exerciseSequenceHelper.elliptical.DetailFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section279918149104)

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

pedalingCadence

 | 

Pedaling cadence details.

 | 

[PedalingCadence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section15378151813915)\[\]

 | 

No

 |
| 

power

 | 

Power details.

 | 

[Power](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section154582103406)\[\]

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
