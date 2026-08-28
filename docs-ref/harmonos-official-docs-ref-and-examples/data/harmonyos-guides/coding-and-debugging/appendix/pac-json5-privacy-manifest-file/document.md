# pac.json5 Privacy Manifest File

#### Introduction

During app development, you need to provide the app's privacy label when releasing the app via AppGallery Connect. It is recommended that you create a **pac.json5** configuration file in your project, where you declare the types of personal data processed, purposes of use, and other information. During the build process, if the **pac.json5** file in the integrated HSPs/HARs also declares privacy protection information, such information will be automatically aggregated into this file and packaged with the software. During app release, AppGallery Connect can automatically generate the privacy label based on the content of this file.

If you develop an HSP or a HAR, to help downstream developers who integrate and use the HSP or HAR quickly and accurately understand how it processes personal data, it is recommended that you create a **pac.json5** configuration file in your project, where you declare the types of personal data processed, purposes of use, and other relevant information. The file will be incorporated into the software package during the build process, and the privacy protection information will be synchronously passed to downstream developers along with the software package.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/kAv18y2IRrWuI1ElsllJlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C5D27244EA31E21E30ECCCE6392FD3D487BA45B6745ADF31B065A54DEBA54C7)

Supported version: DevEco Studio 6.0.0 Beta2 or later.

#### Creating a pac.json5 File

-   For app development, select the **AppScope** directory and create a **pac.json5** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/w3kX4ILWQ5qP4RZpzPYx5A/en-us_image_0000002532670025.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55F103F49DDE19778774E77DB27C1A7334B020CC915BE7C197319AAA017B0171)
    

-   For HSP or HAR development, select the HSP or HAR module directory and create a **pac.json5** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/hwXcErvjQXic-um6PtAI1A/en-us_image_0000002532670027.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3C5DF856D0649DE576F9885251594DCE483ACB153BEEB64AA7357B9663A10C2)
    

#### Configuration File Structure

The structure of the **pac.json5** privacy manifest file is as follows:

dataProcess
└── dataType
└── dataLabels
    └── label
    └── purposes
specialAPIs
└── apiType
└── reasons

#### Fields in the Configuration File

The **pac.json5** privacy manifest file contains the following fields.

**Table 1** Fields in the pac.json5 file
| 
Name

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

[dataProcess](#section82051543115414)

 | 

Optional

 | 

Array

 | 

Personal data collected by the app.

 |
| 

[specialAPIs](#section26881432131216)

 | 

Optional

 | 

Array

 | 

APIs that can be called by the app to generate device fingerprints.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/PXEBlOlGQfK7675iilUrZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=025EE579877A4DF1FA01D2BFB772B68CDF68BDC6DC24A92A17756640AF092621)

**dataProcess** and **specialAPIs** cannot be both empty.

#### dataProcess

**dataProcess** declares the personal data collected by the app, including the data type, data item, and data usage purpose.

**Table 2** dataProcess
| 
Field

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

[dataType](#table176277269236)

 | 

Mandatory

 | 

String

 | 

Type of personal data collected by the app.

 |
| 

[dataLabels](#section13345163017127)

 | 

Mandatory

 | 

Array

 | 

Item and usage purpose of personal data collected by the app.

 |

**Table 3** dataType
| 
Data Type

 | 

Description

 |
| :-- | :-- |
| 

Identifiers

 | 

Identifier

 |
| 

Financial information

 | 

Financial information

 |
| 

Basic information

 | 

Basic information

 |
| 

Transaction information

 | 

Transaction information

 |
| 

Contact information

 | 

Contacts information

 |
| 

Special category data

 | 

Special category data

 |
| 

Device information

 | 

Device information

 |
| 

Location information

 | 

Location information

 |
| 

App information

 | 

App information

 |
| 

User content

 | 

User content

 |
| 

Fitness and health information

 | 

Fitness and health information

 |
| 

Other personal data

 | 

Other personal data

 |

## dataLabels

**dataLabels** declares the personal data items collected by the app and the purpose of collecting the data.

**Table 4** dataLabels
| 
Field

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

[label](#table202051420105216)

 | 

Mandatory

 | 

String

 | 

Item of personal data collected by the app.

 |
| 

[purposes](#table1292433153213)

 | 

Mandatory

 | 

Array

 | 

Purpose for which the app collects personal data.

 |

**Table 5** label
| 
Personal Data Item

 | 

Description

 | 

Data Type

 |
| :-- | :-- | :-- |
| 

MAC

 | 

Media access control address

 | 

Identifiers

 |
| 

OAID

 | 

Open anonymous device identifier

 |
| 

ODID

 | 

Open device identifier

 |
| 

SSID

 | 

Service set identifier

 |
| 

BSSID

 | 

Basic service set identifier

 |
| 

Other device identifiers

 | 

Other device identifiers

 |
| 

ID card

 | 

ID card

 |
| 

Other identity information

 | 

Other identity information

 |
| 

User identifiers

 | 

User identifiers

 |
| 

Bank account information

 | 

Bank account information

 | 

Financial information

 |
| 

Other financial account information

 | 

Other financial account information

 |
| 

Asset information

 | 

Asset information

 |
| 

Other financial information

 | 

Other financial information

 |
| 

Name

 | 

Name

 | 

Basic information

 |
| 

Gender

 | 

Gender

 |
| 

Age

 | 

Age

 |
| 

Date of birth

 | 

Date of birth

 |
| 

Account information

 | 

Account information

 |
| 

Education information

 | 

Education information

 |
| 

Work information

 | 

Work information

 |
| 

Home information

 | 

Family information

 |
| 

Address

 | 

Address

 |
| 

Phone number

 | 

Phone number

 |
| 

Email address

 | 

Email address

 |
| 

Calendar and schedule

 | 

Calendar

 |
| 

Other personal information

 | 

Other personal information

 |
| 

Order information

 | 

Order information

 | 

Transaction information

 |
| 

Transaction records

 | 

Transaction records

 |
| 

Package delivery information

 | 

Package delivery information

 |
| 

Other transaction information

 | 

Other transaction information

 |
| 

Contact list

 | 

Contact list

 | 

Contact information

 |
| 

Social media accounts

 | 

Social media accounts

 |
| 

Other contact information

 | 

Other contact information

 |
| 

Facial recognition features

 | 

Facial recognition features

 | 

Special category data

 |
| 

Voiceprint information

 | 

Voiceprint information

 |
| 

Other biometric features

 | 

Other biometric features

 |
| 

Other special category data

 | 

Other special category data

 |
| 

Magnetometer

 | 

Magnetometer data

 | 

Device information

 |
| 

Light sensor

 | 

Light sensor data

 |
| 

Acceleration sensor

 | 

Acceleration sensor data

 |
| 

Screen orientation sensor

 | 

Screen orientation sensor data

 |
| 

Barometer

 | 

Barometer data

 |
| 

Gyroscope

 | 

Gyroscope data

 |
| 

Rotation vector sensor

 | 

Rotation vector sensor data

 |
| 

Gravity sensor

 | 

Gravity sensor data

 |
| 

OS information

 | 

Operating system information

 |
| 

Other hardware and software parameters/System settings

 | 

Other hardware and software parameters/System settings

 |
| 

Device status

 | 

Device status

 |
| 

IP address

 | 

IP address

 |
| 

Wi-Fi parameters

 | 

Wi-Fi parameters

 |
| 

Wi-Fi status

 | 

Wi-Fi status

 |
| 

Network type

 | 

Network type

 |
| 

Carrier

 | 

Carrier

 |
| 

Other device information

 | 

Other device information

 |
| 

Network location

 | 

Network location

 | 

Location information

 |
| 

Other approximate location information

 | 

Other approximate location information

 |
| 

GPS location

 | 

GPS location

 |
| 

Other precise location information

 | 

Other precise location information

 |
| 

Browsing history

 | 

Browsing history

 | 

App information

 |
| 

Favorites

 | 

Favorites

 |
| 

Basic app information

 | 

Basic app information

 |
| 

App settings

 | 

App settings

 |
| 

App running status

 | 

App running status

 |
| 

App run logs

 | 

App run logs

 |
| 

App usage information

 | 

Other app usage information

 |
| 

Other communication content

 | 

Other communication content

 | 

User content

 |
| 

Image or video

 | 

Image or video

 |
| 

Audio recording

 | 

Audio recording

 |
| 

Audio

 | 

Audio

 |
| 

Text information

 | 

Text information

 |
| 

Search keywords

 | 

Search keywords

 |
| 

Social interactions

 | 

Social interactions

 |
| 

Game statistics

 | 

Game statistics

 |
| 

Customer service records

 | 

Customer service records

 |
| 

Pasteboard

 | 

Pasteboard

 |
| 

Other user content

 | 

Other user content

 |
| 

Heart rate

 | 

Heart rate

 | 

Fitness and health information

 |
| 

Blood pressure

 | 

Blood pressure

 |
| 

Other health information

 | 

Other health information

 |
| 

Fitness information

 | 

Fitness information

 |
| 

Other personal data

 | 

Other personal data

 | 

Other personal data

 |

**Table 6** purposes
| 
Purpose of Personal Data Collection

 | 

Description

 |
| :-- | :-- |
| 

App functionality

 | 

Provides basic app features, security protection, app operations, and customer service.

 |
| 

Product personalization

 | 

Tailors app experience for different users.

 |
| 

Analytics

 | 

Analyzes user behavior to understand whether the current version can meet user needs and improve later versions accordingly.

 |
| 

Advertising and marketing

 | 

Displays ads or other marketing information in your app.

 |
| 

Disclosure to third parties

 | 

Shares data with third-party operating entities for purposes including but not limited to: sharing data with logistics service providers for shipping, and sharing data with third-party institutions for advertising effect evaluation, data display, evaluation, research, reconciliation, provision of operations and O&M services, and data disclosure in forums or social media.

 |
| 

Cross-border transfer

 | 

Serves for cross-border data transmission.

 |
| 

Others

 | 

For other purposes not listed.

 |

#### specialAPIs

**specialAPIs** declares the information about APIs that can be called by the app to generate device fingerprints, including API types and purposes of API calling.

**Table 7** specialAPIs
| 
Field

 | 

Mandatory/Optional

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

[apiType](#table53349541435)

 | 

Mandatory

 | 

String

 | 

API type.

 |
| 

[reasons](#table178321910193719)

 | 

Mandatory

 | 

Array

 | 

Purposes of API calling.

 |

**Table 8** apiType
| 
API Type

 | 

Description

 | 

API

 |
| :-- | :-- | :-- |
| 

File timestamp APIs

 | 

Obtains the creation, modification, or access timestamp of a file, which is helpful for file management and data synchronization.

 | 

ctime

mtime

fs.getxattr

fs.getxattrSync

fs.stat

file.get

fs.lstat

cloudStorage.bucket().getMetadata

 |
| 

System boot time APIs

 | 

Provides the system start time, which is often used to calculate the system running duration or retain the application status after the system is restarted.

 | 

systemDateTime.getUptime

 |
| 

Disk space APIs

 | 

Detects disk space, which helps manage storage resources, for example, alerting on insufficient space or optimizing data storage.

 | 

statvfs.getFreeSize

statvfs.getTotalSize

 |
| 

Active keyboard APIs

 | 

Detects the currently active keyboard to enable context-aware input or multi-language input.

 | 

inputDevice.getKeyboardType

 |
| 

User preferences APIs

 | 

Stores and retrieves user preferences, such as app configurations or recently used items, to improve user experience and app-level personalization.

 | 

preferences.getPreferences

sendablePreferences.getPreferences

 |

**Table 9** reasons
| 
Purpose of API Calling

 | 

Description

 | 

API Type

 |
| :-- | :-- | :-- |
| 

Display to user on-device

 | 

Displays file timestamps, such as the creation, modification, and access time.

 | 

File timestamp APIs

 |
| 

Access file metadata in-app

 | 

Accesses the timestamps, sizes, or other metadata of files in the app container or Cloud Foundation Kit.

 |
| 

Files provided to app by user

 | 

Accesses the timestamps, sizes, or other metadata of files or directories with user authorization.

 |
| 

3rd-party SDK wrapper on-device

 | 

Enables apps to call encapsulated file timestamp functions provided by a third-party SDK.

 |
| 

Measure time on-device

 | 

Calculates the elapsed time between events in an app, or implements a timer through time calculations.

 | 

System boot time APIs

 |
| 

Calculate timestamp for in-app event

 | 

Calculates the absolute timestamps of events in an app.

 |
| 

User-initiated bug report

 | 

Records the system start time in the diagnosis report submitted by the user.

 |
| 

Display to user on-device

 | 

Displays disk space information to users.

 | 

Disk space APIs

 |
| 

Write or delete file on-device

 | 

Checks for disk space before file writing, or triggers junk file cleanup when disk space is insufficient.

 |
| 

User-initiated bug report

 | 

Records the disk space information in the diagnosis report submitted by the user.

 |
| 

Health research app

 | 

Checks whether there is sufficient disk space to store the health data collected by the app.

 |
| 

Custom keyboard app on-device

 | 

Enables custom keyboard apps to check the keyboard activated on the current device.

 | 

Active keyboard APIs

 |
| 

Customized UI on-device

 | 

Presents the correct customized UI based on the state of the currently activated keyboard.

 |
| 

Access preferences data in-app

 | 

Accesses user preferences configuration that can only be read and written by this app.

 | 

User preferences APIs

 |
| 

3rd-party SDK wrapper on-device

 | 

Enables apps to call encapsulated user preferences functions (preference APIs) provided by a third-party SDK.

 |

#### pac.json5 File Example

{
  "dataProcess": \[
    {
      "dataType": "Identifiers",
      "dataLabels": \[
        {
          "label": "MAC",
          "purposes": \["App functionality"\]
        }
      \]
    }
  \],
  "specialAPIs": \[
    {
      "apiType": "File timestamp APIs",
      "reasons": \["Display to user on-device","Access file metadata in-app"\]
    }
  \]
}
