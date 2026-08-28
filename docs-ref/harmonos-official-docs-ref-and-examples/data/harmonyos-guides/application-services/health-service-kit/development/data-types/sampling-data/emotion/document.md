# Emotion

Emotion data of a user at a certain time point.

Constant in the HarmonyOS SDK: [samplePointHelper.emotion.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section633320312412)

#### OAuth Scope

To apply for the required scopes, go to **Health data** > **Emotion** on the Console of HUAWEI Developers.

#### Sampling Details

## Fields

Field definition: [samplePointHelper.emotion.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section733463444)

| 
**Field**

 | 

Description

 | 

**Type**

 | 

Mandatory

 | 

Unit

 | 

Value Range

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

emotionStatus

 | 

Emotional state

 | 

number

 | 

Yes

 | 

\-

 | 

\[0, 100)

Currently, the Huawei Health app only displays the following values:

1: unpleasant

2: neutral

3: pleasant

 |

## Data Openness

| 
Open API

 | 

Query Timeliness

 | 

Data Source

 |
| :-- | :-- | :-- |
| 

[healthStore.readData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section193411928192218)

 | 

In hours

 | 

Watches, bands, and so on

 |
