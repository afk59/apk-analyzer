# Cycling

The following table lists the types of cycling records.

| 
**Subtype Constant**

 | 

**Description**

 | 

Data Source

 |
| :-- | :-- | :-- |
| 

[exerciseSequenceHelper.cycling.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section299320372296)

 | 

Outdoor cycling.

 | 

Mobile phones, watches, and bands

 |
| 

[exerciseSequenceHelper.indoorCycling.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section14762493361)

 | 

Indoor cycling.

 | 

Indoor bicycles and bike trainers.

 |
| 

[exerciseSequenceHelper.spinning.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section13529152615411)

 | 

Spinning.

 | 

Spinning bike

 |
| 

[exerciseSequenceHelper.bmx.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section171409112597)

 | 

BMX cycling.

 | 

Mountain bikes.

 |

#### Associated Statistical Data

-   Field definition: [exerciseSequenceHelper.cycling.SummaryFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section1599483720293)

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

#### Associated Detailed Data

-   Field definition: [exerciseSequenceHelper.cycling.DetailFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section988513311325)

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
| 

resistance

 | 

Resistance details.

 | 

[Resistance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section17695193744217)\[\]

 | 

No

 |
