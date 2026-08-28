# Blood Pressure

Blood pressure of a user at a certain time point.

Constant in the HarmonyOS SDK: [samplePointHelper.bloodPressure.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1144555923610)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/xfMoI5c1Q-SD580_nl7_sw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062106Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDE4DB35D4FD38DF5BD98C4BBC580FD197578E21B593A1281752D12F957A619E)

This data type is not supported on wearables.

#### OAuth Scope

To apply for the required scopes, go to **Health data** > **Blood pressure** on the Console of HUAWEI Developers.

#### Sampling Details

## Fields

Field definition: [samplePointHelper.bloodPressure.Fields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1044675919367)

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

bloodPressureSystolic

 | 

Systolic (top) pressure.

 | 

number

 | 

Yes

 | 

mmHg

 | 

(0, ∞)

 |
| 

bloodPressureDiastolic

 | 

Diastolic (bottom) pressure.

 | 

number

 | 

Yes

 | 

mmHg

 | 

(0, ∞)

 |
| 

sphygmus

 | 

Pulse.

 | 

number

 | 

No

 | 

Beats/min

 | 

(0, ∞)

 |
| 

measurementAnomalyFlag

 | 

Measurement exception event.

 | 

number

 | 

No

 | 

\-

 | 

(0, ∞)

The options are:

**1**: normal

**2**: The device is not level with the user's heart.

**3**: The user shakes slightly during the measurement.

**4**: The user does not rest for 5 minutes or more before the measurement.

 |
| 

beforeMeasureActivity

 | 

Activity before measurement.

 | 

number

 | 

No

 | 

\-

 | 

(0, ∞)

The options are:

**1**: intense exercise

**2**: smoking

**3**: eating

**4**: drinking alcohol

**5**: drinking coffee

**6**: no activity

**7**: after getting up

**8**: prepared for bed

**100**: custom

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

Blood pressure monitors or more

 |
