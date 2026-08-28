# Pushing a Live View Message

#### Use Cases

Live view notifications can help users focus on ongoing tasks, facilitating quick viewing and instant processing of these tasks. For details about what a live view is, how to apply for the required permissions, supported scenarios, and design specifications, please refer to [Live View Kit](../../../live-view-kit/about-this-kit/document.md).

Live view messages initiated through Push Kit support three types of operations, as described in the following table.

| 
Live View Message Operation

 | 

Application Scenario

 | 

Description

 |
| :-- | :-- | :-- |
| 

Create a live view

 | 

FLIGHT, TAXI, and TRAIN

 | 

A live view can be created through Push Kit only for apps relevant to flight, ride hailing, and high-speed rail/common train scenarios. For other scenarios, create a live view through Live View Kit.

 |
| 

Update a live view

 | 

All

 | 

A live view can be updated through Push Kit for all scenarios.

 |
| 

End a live view

 | 

All

 | 

A live view can be ended through Push Kit for all scenarios.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Go9ekalCQK2IEPSJ77WZPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13853529E73031E77FFFD232EEAFE38171FF3C6010E949FE6D2DB9657CCD8618)

The function of sending live view messages supports phones and tablets.

You can refer to the [applicable scope and scenarios](../../../live-view-kit/about-this-kit/document.md#section1539812274717) for details.

The process of sending live view messages through Push Kit varies depending on the method of creating the live view.

**Creating a live view through Live View Kit, and updating and ending the live view through Push Kit**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/grxeM-O_TlqG-jG0Vdg15w/en-us_image_0000002402305801.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B387CB657F90AC118E608B4D12BE70476560E34A9AB4EEF7AF4B0F26E108D65 "Click to enlarge")

1.  Request a push token from Push Kit.
2.  Create a live view using Live View Kit. Then you need to save the live view ID, push token, live view scenario events, and business service status attributes to your app server.
3.  When the order status on the app server changes, Push Kit pushes update messages to update or end the live view.

**Creating, updating, and ending a live view through Push Kit**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/N5brAYNlRS-DfBYhfXGnew/en-us_image_0000002402225657.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DAC9EFE201D9671C727C04B0E5F16A2FDF1662C48952A5225E27F61DBAEF73A "Click to enlarge")

1.  Request a push token from Push Kit.
2.  Save the push token to your app server.
3.  Use Push Kit to create/update/end a live view.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/joUM0ac9QVaejDL6nEnWpQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43FECCC09BF988AAAC2AF0870E98181FA33B054C4DF9D369A6F814E0FA5EDEB8)

-   The lifecycle of a live view cannot exceed 8 hours. After 8 hours, the system considers that the live view ends.
-   To ensure the timeliness of live view messages, be sure to update the live view content promptly. If a live view is not updated for more than 2 hours, the system will hide the live view display on the status bar and lock screen, but retain its display in the notification panel. If a live view is not updated for more than 4 hours, the system considers that the live view ends and clears the live view from all display entrances.

#### Applying for Required Permissions

To push live view messages, you need to [apply for the live view permission in the specific scenario](../../../live-view-kit/preparations/applying-for-the-formal-permission-on-live-view-kit/document.md) first.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/TWFuzmPsTcKenyjuYC4d9w/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=095521E797636376F6A1384A4D9DE52A5D71A3535E532930468B2E26676A295E)

To push live view messages using Push Kit, you need to apply for the live view message permission first. Relevant functions cannot be commissioned merely by trustlist configuration.

#### Frequency Control

**During the debugging phase**, the maximum number of test messages that can be pushed for each project every day is 1000. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

**After formal release**, the total number of messages that each app can push to a single device is subject to the limits specified in the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section993063213715). The total number of scenario-specific messages that can be pushed on a daily basis to each device cannot exceed 3000.

The messages of a single live view can be updated for up to 30 times every 5 minutes and 180 times every hour on each device in the ride hailing and live score scenarios. In other scenarios, the messages of a single live view can be updated for up to 10 times every 5 minutes and 60 times every hour on each device. The excess messages will be discarded.

#### Development Procedure

1.  Complete operations in [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md).
2.  Select a method for creating a live view based on your needs.
    
    -   If you need to create a live view locally using Live View Kit, please refer to [Creating a Local Live View](../../../live-view-kit/app-development/creating-a-local-live-view/document.md).
    -   If you need to create a live view remotely using Push Kit, ensure that you comply with the [requirements](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section441214411235). The following is a request example of the ride hailing scenario:
        
        // Request URL 
        POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
         
        // Request Header 
        Content-Type: application/json 
        Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*  
        push-type: 7
        
        // Request Body
        {
          "payload": {
            "activityId": 1,
            "operation": 0,
            "event": "TAXI",
            "status": "DRIVER\_ON\_THE\_WAY", // Driver on the way
            "activityData": {
              "notificationData": {
                "type": 3,       
                "contentTitle": "{{status}}", // Driver on the way
                "contentText": \[
                  {
                    "text": "1.2 km"
                  },
                  {
                    "text": "away",
                    "foregroundColor": "#FF317AF7"
                  },
                  {
                    "text": " | "
                  },
                  {
                    "text": "5 minutes",
                    "foregroundColor": "#FF317AF7"
                  }
                \],
                "clickAction": {
                  "actionType": 1, // Open a custom app page.
                  "action": "xxxxxx" // Action corresponding to the ability of the in-app page.
                },
                "richProgress": {
                  "type": 0,
                  "nodeIcons": \["icon1.png", "icon2.png", "icon3.png"\], // The value is file names in **resources/rawfile**.
                  "indicatorIcon": "taxi.png", // The value is a file name in **/resources/rawfile**.
                  "progress": 40,
                  "indicatorType": 1,
                  "color": "#FF317AF7",
                  "bgColor": "#19000000"
                },
                "extend": {
                  "type": 3,
                  "pic": "phone.png", // The value is a file name in **/resources/rawfile**.
                  "clickAction": {
                    "actionType": 0 // Tapping the auxiliary area opens the app home page.
                  }
                }
              },
              "capsuleData": {
                "type": 1,
                "status": 1,
                "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
                "bgColor": "#FF317AF7",
                "remind": "EXPAND",
                "title": "Picking up",
                "content": "About 5 minutes"
              }
            }
          },
          "pushOptions": {
            "ttl": 1000,
            "biTag": "biTag"
          },
          "target": {
            "token": \[
              "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
            \]
          }
        }
        
        -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
        -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313).
        -   **push-type**: The value **7** indicates live view message.
        -   **activityId**: live view activity ID. For details, please refer to [activityId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306).
        -   **operation**: live view message operation type. The value **0** indicates creating a live view. For details, please refer to [operation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306).
        -   **event**: scenario of the live view message, which must be the same as that you have applied for, for example, **TAXI** (ride hailing) and **FLIGHT** (flight). Only the TAXI, FLIGHT, and TRAIN scenarios support creating a live view through Push Kit. For details, please refer to [Restrictions on Live View Creation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section441214411235).
        -   **status**: status of a live view message. This parameter is mandatory when **operation** is set to **0**. The value range varies depending on the scenario type. For details, please refer to [Value Range of Status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section1251014198565). Also, you need to enter the placeholder _{{status}}_ at least once in the [Parameters That Support Placeholders](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section111894703518). Push Kit will replace the placeholder _{{status}}_ with the matching value in [Value Range of Status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section1251014198565).
        -   **activityData**: live view data in your project. For details, please refer to [activityData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section93901138192612).
        -   **type**: live view layout type, including progress visualization and emphasized text. During live view creation, each event can use only the specified layout type. For details, please refer to [Restrictions on Live View Creation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section441214411235).
        -   **token**: push token. Obtain the token by referring to [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md).
    
3.  Call the REST API provided by Push Kit when the status of a user's service order changes to update or end the live view.
    
    For details about the request message, please refer to [Scenario-Specific Message API Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-intro). (If the live view to be updated is remotely created using Push Kit, be sure to meet the [requirements](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section441214411235) during the update.)
    
    // Request URL 
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
     
    // Request Header 
    Content-Type: application/json 
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*  
    push-type: 7 
     
    // Request Body
    {
      "payload": {
        "activityId": 1,
        "operation": 1,
        "event": "TAXI",
        "status": "HEADING\_TO\_DESTINATION", // Heading to the destination
        "version": 1,
        "activityData": {
          "notificationData": {
            "type": 3,
            "contentTitle": "{{status}}", // Heading to the destination
            "contentText": \[
              {
                "text": "Remaining distance:"
              },
              {
                "text": "7.2 km",
                "foregroundColor": "#FF317AF7"
              },
              {
                "text": " | About"
              },
              {
                "text": "27 minutes",
                "foregroundColor": "#FF317AF7"
              }
            \],
            "clickAction": {
              "actionType": 1, // Open a custom app page.
              "action": "xxxxxx" // Action corresponding to the ability of the in-app page.
            },
            "richProgress": {
              "type": 0,
              "nodeIcons": \["icon1.png", "icon2.png", "icon3.png"\], // The value is file names in **resources/rawfile**.
              "indicatorIcon": "taxi.png", // The value is a file name in **/resources/rawfile**.
              "progress": 70,
              "indicatorType": 1,
              "color": "#FF317AF7",
              "bgColor": "#19000000"
            },
            "extend": {
              "type": 0
            }
          },
          "capsuleData": {
            "type": 1,
            "status": 1,
            "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
            "bgColor": "#FF317AF7",
            "title": "27 minutes",
            "content": "Remaining distance: 7.2 km"
          }
        }
      },
      "pushOptions": {
        "ttl": 1000,
        "biTag": "biTag"
      },
      "target": {
        "token": \[
          "MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"
        \]
      }
    }
    
    -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313).
    -   **push-type**: The value **7** indicates live view message.
    -   **activityId**: live view activity ID. For details, please refer to [activityId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306).
    -   **operation**: live view notification operation type. The options are **0** (create a live view), **1** (update the live view), and **2** (end the live view). For details, please refer to [operation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306).
    -   **event**: scenario of the live view message, which must be the same as that you have applied for, for example, **TAXI** (ride hailing) and **FLIGHT** (flight). For details, please refer to [event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306).
    -   **status**: status of a live view message. This parameter is mandatory when **operation** is set to **1** and the live view is created through Push Kit remotely. The value range varies depending on the scenario type. For details, please refer to [Value Range of Status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section1251014198565). Also, you need to enter the placeholder _{{status}}_ at least once in the [Parameters That Support Placeholders](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section111894703518). Push Kit will replace the placeholder _{{status}}_ with the matching value in [Value Range of Status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section1251014198565).
    -   **version**: version number of the live view update notification. For details, please refer to [version](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306).
    -   **activityData**: live view data in your project. For details, please refer to [activityData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section93901138192612).
    -   **type**: live view layout type, including progress visualization and emphasized text. For details, please refer to [type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section7742121916279).
    -   **token**: push token. Obtain the token by referring to [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/5lIyDyUeTjm83justSoSvQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2CB88BC52F9B9A310B5EDE514DFE0BD81434D8B4C6983357CC7AAF7AB41C21F)
        
        If the live view corresponding to a specific **activityId** does not exist in the scenario of updating or ending a live view, the use of this **activityId** to send live view messages will be banned for 24 hours.
