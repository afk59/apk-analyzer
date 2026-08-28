# Personal Data Processing Information

In personal data processing of Device Security Kit, Huawei serves as the end user data processor, and you serve as the end user data controller. For appropriate and legal processing of personal data, the following are provided:

-   List of personal data processed by Huawei
-   Guidance for you to help the end user control personal data

#### List of Personal Data Processed by Huawei

Last modified: May 20, 2024

| 
Personal Data

 | 

Purpose of Use

 | 

Retention Period

 |
| :-- | :-- | :-- |
| 

Device identifier

 | 

Device identifier, based on which the app usage status on the device is recorded.

 | 

The DeviceVerify server stores data for a maximum of two years, and automatically deletes the expired data.

 |
| 

App usage information

 | 

App usage status (for example, whether a coupon is claimed) on a device.

 |
| 

Device identifier

 | 

Device identifier, based on which risky device usage information is recorded.

 | 

The BusinessRiskIntelligentDetection server stores data for a maximum of 180 days, and automatically deletes the expired data.

 |
| 

Device usage information

 | 

Risk information (for example, whether a user answers a fraudulent call or shares the screen) during device use, which is used for business risk detection.

 |
| 

ODID

 | 

ODID, based on which risky device usage information is recorded.

 |
| 

Call log information

 | 

Includes the calling number, timestamp when a call is answered, call log type, calling party name, and call duration. The information will be sent to your app to implement the function of reporting fraudulent call logs.

 | 

The data is not retained.

 |
| 

Message information

 | 

Includes the mobile number of a message sender, timestamp when a message is received, message content, sender name, home area of the mobile number of a message sender, message type, MMS subject, MMS attachment type, and attachment URI. The information will be sent to your app to implement the function of reporting fraudulent messages.

 | 

The data is not retained.

 |

#### Guidance for You to Help the End User Control Personal Data

-   How to Clear the End User's Personal Data
    -   You can call the [delDeviceStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-deletedevicestatus) API of the DeviceVerify server to delete the end user's personal data.
-   How to Export the End User's Personal Data
    
    -   You can call the [getDeviceStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-deviceverify-getdevicestatus) API of the DeviceVerify server to export the end user's personal data.
