# Heart Rate

#### Dynamic Heart Rate

Dynamic heart rates of a user within a period of time.

-   Constant in the HarmonyOS SDK: [samplePointHelper.heartRate.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section8922144319272)

## OAuth Scope

To apply for the required scopes, go to **Health data** > **Heart rate** on the Console of HUAWEI Developers.

## Sampling Details

**Fields**

Field definition: [samplePointHelper.heartRate.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section69231443182712)

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

bpm

 | 

Heart rate.

 | 

number

 | 

Yes

 | 

Beats/min

 | 

\[0, ∞)

 |

**Data Openness**

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

## Sampling Statistics

**Aggregation metrics**

-   Field definition: [samplePointHelper.heartRate.AggregateFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1191392414619)

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

bpm

 | 

Heart rate.

 | 

max | min | last

 | 

number

 | 

Beats/min

 |

**Data Openness**

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

#### Resting Heart Rate

This data type refers to the resting heart rate of a user at a certain time point when the user is awake and resting.

Constant in the HarmonyOS SDK: [samplePointHelper.restingHeartRate.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section142451938435)

## OAuth Scope

To apply for the required scopes, go to **Health data** > **Heart rate** on the Console of HUAWEI Developers.

## Sampling Details

**Fields**

Field definition: [samplePointHelper.restingHeartRate.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section12246532433)

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

restBpm

 | 

Resting Heart Rate

 | 

number

 | 

Yes

 | 

Beats/min

 | 

\[0, ∞)

 |

**Data Openness**

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

## Sampling Statistics

**Aggregation metrics**

Field definition: [samplePointHelper.restingHeartRate.AggregateFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section12206132184518)

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

restBpm

 | 

Resting heart rate.

 | 

last

 | 

number

 | 

Beats/min

 |

**Data Openness**

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
