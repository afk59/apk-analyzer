# Scope Description

Scopes are required for reading and writing fitness and health data. For details about how to apply for the scopes, please refer to [Applying for Health Service Kit](../../getting-started/applying-for-health-service-kit/document.md). The following lists the scopes for each data type:

| 
Data Type

 | 

Constant in the HarmonyOS SDK

 | 

Read

 | 

Write

 |
| :-- | :-- | :-- | :-- |
| 

Daily activities

 | 

[samplePointHelper.dailyActivities.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section122559932419)

 | 

Daily activity data (read)

 | 

Daily activity data (write)

 |
| 

Dynamic heart rate

 | 

[samplePointHelper.heartRate.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section8922144319272)

 | 

Heart rate data (read)

 | 

Heart rate data (write)

 |
| 

Resting heart rate

 | 

[samplePointHelper.restingHeartRate.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section142451938435)

 | 

Heart rate data (read)

 | 

Heart rate data (write)

 |
| 

SpO2

 | 

[samplePointHelper.bloodOxygenSaturation.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1518925691412)

 | 

SpO2 data (read)

 | 

SpO2 data (write)

 |
| 

Stress

 | 

[samplePointHelper.stress.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section299320372296)

 | 

Stress data (read)

 | 

Stress data (write)

 |
| 

Body temperature

 | 

[samplePointHelper.bodyTemperature.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section8499929111914)

 | 

Body temperature data (read)

 | 

Body temperature data (write)

 |
| 

Skin temperature

 | 

[samplePointHelper.skinTemperature.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section88802164482)

 | 

Body temperature data (read)

 | 

Body temperature data (write)

 |
| 

Blood pressure

 | 

[samplePointHelper.bloodPressure.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section1144555923610)

 | 

Blood pressure data (read)

 | 

Blood pressure data (write)

 |
| 

Height

 | 

[samplePointHelper.height.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section691019541405)

 | 

Body fat data (read)

 | 

Body fat data (write)

 |
| 

Weight

 | 

[samplePointHelper.weight.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section7705611125214)

 | 

Body fat data (read)

 | 

Body fat data (write)

 |
| 

Emotion

 | 

[samplePointHelper.emotion.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section633320312412)

 | 

Emotion data (read)

 | 

Emotion data (write)

 |
| 

Heart rate variability

 | 

[samplePointHelper.heartRateVariability.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-samplepointhelper#section62317226815)

 | 

Heart rate data (read)

 | 

Heart rate data (write)

 |
| 

Sleep

 | 

[healthSequenceHelper.sleepRecord.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthsequencehelper#section299320372296)

 | 

Sleep data (read)

 | 

Sleep data (write)

 |
| 

[healthSequenceHelper.sleepNapRecord.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthsequencehelper#section84091227104612)

 |
| 

Workout records

 | 

[exerciseSequenceHelper.DATA\_TYPE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-exercisedequencehelper#section171402050378)

 | 

Workout record summary (read)

Workout record details (read)

Workout record location details (read)

 | 

Workout record summary (write)

Workout record details (write)

Workout record location details (write)

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/slpsh9zyQZ2e3wfownGIFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062106Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E850D67029DEBAA868F4C540010790648D4DD95D09E84EDABDC41D14924F3A9)

-   To read/write workout records, apply for the scope for reading/writing the workout record summary.
-   If you need to read/write workout records and associate them with detailed data, you need to apply for both the scopes for reading/writing the workout record summary and for reading/writing workout record details.
-   If you want to read/write workout records and associate them with detailed data (including the location), you need to apply for the scopes for reading/writing the workout record summary, workout record details, and workout record location details.
