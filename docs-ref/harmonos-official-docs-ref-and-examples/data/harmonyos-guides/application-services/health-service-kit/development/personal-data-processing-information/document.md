# Personal Data Processing Information

Last modified: May 16, 2024

Huawei is a data processor, but not a data controller. The purpose and method of using data are determined by users.

In personal data processing, Huawei serves as the end user data processor, and you (the developer) serve as the end user data controller. For appropriate and legal processing of personal data, the following are provided:

-   List of personal data processed by Huawei
-   Guidance for you to help the end user control personal data

#### List of Personal Data Processed by Huawei

| 
Personal Data

 | 

Purpose

 | 

Retention Period

 |
| :-- | :-- | :-- |
| 

Personal information: height and weight

 | 

Health Service Kit provides a platform for users to store and share their data. It does not proactively process any user data. All data display and health and fitness services are provided by developers for users. The data comes from the Huawei Health app and third-party services. The data is stored in the local database of the Health Service Kit and will be synced to the cloud.

 | 

After a user deletes their HUAWEI ID, their personal data will be deleted.

 |
| 

Fitness data: daily activities (steps, calories, distance, medium- and high-intensity activities, ascent, and hours active) and workout records

 |
| 

Health data: sleep, heart rate, stress, SpO2, body temperature, and blood pressure data

 |
| 

Device ID of the data source (MAC address or other device identifiers, which are provided by the third-party service)

 | 

The device ID is used to identify the data source.

 |
| 

HUAWEI ID

 | 

To identify the end user when their HUAWEI ID is bound to a third-party service

 |

#### Guidance for You to Help the End User Control Personal Data

**How to Clear the End User's Personal Data**

1.  After an end user logs in to and authorizes an app through Health Service Kit APIs, the developer can delete the user data written by their app to Health Service Kit through the [healthStore.deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1502957143419) API.
2.  The end user can delete their personal data by deleting their HUAWEI ID. All personal data under their HUAWEI ID will be deleted.

**How to Export the End User's Personal Data**

The developer can call Health Service Kit APIs to obtain user data and provide data export services for users by referring to [healthStore.readData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section193411928192218). For details, please refer to [Health and Fitness Sampling Data](../developing-phone-tablet-apps/managing-health-and-fitness-data/health-and-fitness-sampling-data/document.md).
