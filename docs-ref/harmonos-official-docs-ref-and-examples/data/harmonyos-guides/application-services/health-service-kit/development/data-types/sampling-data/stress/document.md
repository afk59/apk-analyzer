# Stress

Stress data of a user at a certain moment. Each data record indicates the stress data at a certain time point.

-   Constant in the HarmonyOS SDK: [samplePointHelper.stress.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section299320372296)

#### OAuth Scope

To apply for the required scopes, go to **Health data** > **Stress** on the Console of HUAWEI Developers.

#### Sampling Details

## Fields

-   Field definition: [samplePointHelper.stress.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1599483720293)

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

stressScore

 | 

Stress score.

 | 

number

 | 

Yes

 | 

\-

 | 

\[1, 99\]

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

#### Sampling Statistics

**Aggregation metrics**

-   Field definition: [samplePointHelper.stress.AggregateFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section119551246145013)

| 
**Field**

 | 

Description

 | 

Aggregation Metric

 | 

**Type**

 | 

Unit

 |
| :-- | :-- | :-- | :-- | :-- |
| 

stressScore

 | 

Stress score.

 | 

avg | max | min | last | count

 | 

number

 | 

\-

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

[healthStore.aggregateData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section4878142184216)

 | 

In hours

 | 

Watches, bands, and so on

 |
