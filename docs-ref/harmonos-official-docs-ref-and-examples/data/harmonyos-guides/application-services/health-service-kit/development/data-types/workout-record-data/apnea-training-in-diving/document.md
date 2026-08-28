# Apnea Training in Diving

The following table lists the type of apnea training records.

| 
**Subtype Constant**

 | 

**Description**

 | 

Data Source

 |
| :-- | :-- | :-- |
| 

[exerciseSequenceHelper.breathHoldingTrain.EXERCISE\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section1310632742)

 | 

Diving apnea training.

 | 

Selected professional watches and bands

 |

#### Associated Statistical Data

-   Field definition: [exerciseSequenceHelper.breathHoldingTrain.SummaryFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section6107525417)

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

breathHoldingTrainFeature

 | 

Diving apnea training feature.

 | 

[BreathHoldingTrainFeature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthfields#section1359857181417)

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

-   Field definition: [exerciseSequenceHelper.breathHoldingTrain.DetailFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section41086213414)

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
