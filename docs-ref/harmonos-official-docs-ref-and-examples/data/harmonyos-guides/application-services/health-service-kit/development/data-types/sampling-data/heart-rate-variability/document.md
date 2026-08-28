# Heart Rate Variability

Heart rate variability data of a user at a certain time point.

Constant in the HarmonyOS SDK: [samplePointHelper.heartRateVariability.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section62317226815)

#### OAuth Scope

To apply for the required scopes, go to **Health data** > **Heart rate** on the Console of HUAWEI Developers.

#### Sampling Details

## Fields

Field definition: [samplePointHelper.heartRateVariability.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section132322221288)

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

heartRateVariabilityRMSSD

 | 

Heart rate variability

 | 

number

 | 

Yes

 | 

Millisecond

 | 

(0, 200\]

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
