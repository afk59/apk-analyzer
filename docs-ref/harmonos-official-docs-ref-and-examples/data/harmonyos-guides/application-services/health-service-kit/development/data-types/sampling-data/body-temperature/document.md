# Body Temperature

#### Body Temperature

Body temperature data of a user within a short period of time.

Constant in the HarmonyOS SDK: [samplePointHelper.bodyTemperature.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section8499929111914)

## OAuth Scope

To apply for the required scopes, go to **Health data** > **Body temperature** on the Console of HUAWEI Developers.

## Sampling Details

**Fields**

-   Field definition: [samplePointHelper.bodyTemperature.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section125001429171917)

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

bodyTemperature

 | 

Body temperature.

 | 

number

 | 

Yes

 | 

Celsius (°C)

 | 

\[34, 42\]

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

In minutes

 | 

Selected watches

 |

## Sampling Statistics

**Aggregation metrics**

Field definition: [samplePointHelper.bodyTemperature.AggregateFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section170613199291)

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

bodyTemperature

 | 

Body temperature.

 | 

avg | max | min | count

 | 

number

 | 

Celsius (°C)

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

In minutes

 | 

Selected watches

 |

#### Skin Temperature

Skin temperature data of a user within a short period of time.

-   Constant in the HarmonyOS SDK: [samplePointHelper.skinTemperature.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section88802164482)

## OAuth Scope

To apply for the required scopes, go to **Health data** > **Body temperature** on the Console of HUAWEI Developers.

## Sampling Details

**Fields**

-   Field definition: [samplePointHelper.skinTemperature.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1188171616489)

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

skinTemperature

 | 

Skin temperature.

 | 

number

 | 

Yes

 | 

Celsius (°C)

 | 

\[20, 42\]

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

In minutes

 | 

Selected watches

 |

## Sampling Statistics

**Aggregation metrics**

Field definition: [samplePointHelper.skinTemperature.AggregateFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section088331611483)

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

skinTemperature

 | 

Skin temperature.

 | 

avg | max | min | count

 | 

number

 | 

Celsius (°C)

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

In minutes

 | 

Selected watches

 |
