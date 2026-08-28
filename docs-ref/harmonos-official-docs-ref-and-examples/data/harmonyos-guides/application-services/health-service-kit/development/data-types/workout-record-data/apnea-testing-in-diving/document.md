# Apnea Testing in Diving

The following table lists the type of apnea testing records.

| 
**Subtype Constant**

 | 

**Description**

 | 

Data Source

 |
| :-- | :-- | :-- |
| 

[exerciseSequenceHelper.breathHoldingTest.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section4370709410)

 | 

Diving apnea test.

 | 

Selected professional watches and bands

 |

#### Associated Statistical Data

Field definition: [exerciseSequenceHelper.breathHoldingTest.SummaryFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section43718017416)

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

breathHoldingTestFeature

 | 

Diving apnea test feature.

 | 

[BreathHoldingTestFeature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section236115121419)

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

#### Associated Detailed Data

Field definition: [exerciseSequenceHelper.breathHoldingTest.DetailFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section637211017416)

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
