# SpO2

SpO2 level of a user at a certain moment. Each data record indicates the SpO2 level at a certain time point. Data records cannot overlap. The start time of the next data record must be later than or equal to the end time of the previous data record.

-   Constant in the HarmonyOS SDK: [samplePointHelper.bloodOxygenSaturation.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1518925691412)

#### OAuth Scope

To apply for the required scopes, go to **Health data** > **SpO2** on the Console of HUAWEI Developers.

#### Sampling Details

## Fields

-   Field definition: [samplePointHelper.bloodOxygenSaturation.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section175921611817)

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

spo2

 | 

SpO2.

 | 

number

 | 

Yes

 | 

%

 | 

(0, 100\]

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

Selected watches, bands, and so on

 |

#### Sampling Statistics

**Aggregation metrics**

Field definition: [samplePointHelper.bloodOxygenSaturation.AggregateFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1972045182915)

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

spo2

 | 

SpO2.

 | 

avg | max | min | last

 | 

number

 | 

%

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

Selected watches, bands, and so on

 |
