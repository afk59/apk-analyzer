# Weight

Weight data of a user at a certain time point.

Constant in the HarmonyOS SDK: [samplePointHelper.weight.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section7705611125214)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/z9Ny2xAJSRuI9MXdVd38Og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062107Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B18B54B056F7B068A558FB66CD7EB84C0B1060749F90C84C49624CF2330FD774)

This data type is not supported on wearables.

#### OAuth Scope

To apply for the required scopes, go to **Health data** > **Body fat** on the Console of HUAWEI Developers.

#### Sampling Details

## Fields

Field definition: [samplePointHelper.weight.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section16706111155215)

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

bodyWeight

 | 

Weight.

 | 

number

 | 

Yes

 | 

kg

 | 

\[0.1, 500\]

 |
| 

bmi

 | 

Body mass index.

 | 

number

 | 

No

 | 

kg/m2

 | 

\[1, 200\]

 |
| 

bodyFat

 | 

Body fat.

 | 

number

 | 

No

 | 

kg

 | 

\[0, 500\]

 |
| 

bodyFatRate

 | 

Body fat percentage.

 | 

number

 | 

No

 | 

%

 | 

\[0, 100\]

 |
| 

muscleMass

 | 

Muscle mass.

 | 

number

 | 

No

 | 

kg

 | 

\[0.1, 150\]

 |
| 

basalMetabolism

 | 

Basal metabolic rate.

 | 

number

 | 

No

 | 

Kcal/day

 | 

\[0, ∞)

 |
| 

moisture

 | 

Body water.

 | 

number

 | 

No

 | 

kg

 | 

\[0, 500\]

 |
| 

moistureRate

 | 

Body water percentage.

 | 

number

 | 

No

 | 

%

 | 

\[0, 100\]

 |
| 

visceralFatLevel

 | 

Visceral fat level.

 | 

number

 | 

No

 | 

\-

 | 

\[1, 59\]

 |
| 

boneSalt

 | 

Bone mineral content.

 | 

number

 | 

No

 | 

kg

 | 

\[0.5, 5\]

 |
| 

proteinRate

 | 

Protein rate.

 | 

number

 | 

No

 | 

%

 | 

\[0, 100\]

 |
| 

bodyScore

 | 

Body score.

 | 

number

 | 

No

 | 

%

 | 

\[0, 100\]

 |
| 

bodyAge

 | 

Body age.

 | 

number

 | 

No

 | 

\-

 | 

\[5, 99\]

 |
| 

skeletalMuscleMass

 | 

Skeletal muscle mass

 | 

number

 | 

No

 | 

kg

 | 

\[1, 150\]

 |
| 

impedance

 | 

Impedance.

 | 

number

 | 

No

 | 

Ohm

 | 

\[0.1, 100000\]

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

In minutes

 | 

Huawei and other compatible body fat scales (ecosystem devices)

 |
