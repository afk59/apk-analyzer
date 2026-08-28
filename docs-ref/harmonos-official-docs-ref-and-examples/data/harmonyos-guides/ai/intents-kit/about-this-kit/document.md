# About This Kit

Intents Kit for HarmonyOS defines standards for intents, linking functions of apps or atomic services.

It helps you intelligently distribute functions of apps or atomic services to system entry points. This process is called smart distribution. The system entry points include Celia Chat, Celia Search, and Celia Suggestions.

The following figure shows the relationships among system entry points, Intents Kit, and the HarmonyOS ecosystem.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/_yb9-62iT-qEg0rfVMcvkA/en-us_image_0000002402161829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8959C87EFDB392665D60F3E61A2875D0F632270301095F7FE054DBBA657EE1A4 "Click to enlarge")

#### Intents Kit Advantages

Intents Kit can use AI capabilities such as foundation models and multi-dimensional device awareness in HarmonyOS to accurately and promptly obtain users' explicit or implicit intents, implementing personalized, multi-modal, accurate, and smart distribution of functions.

#### Smart Distribution

To facilitate integration of Intents Kit, various smart distribution feature categories are available. Currently, habit-based recommendation, event-based notification, skill calls (through voice input), and local search have been open, while other features will be available in the future. The following table lists the typical system entry point and distribution logic of each feature category.

| 
**Feature Category**

 | 

**System Entry Point**

 | 

**Distribution Logic**

 |
| :-- | :-- | :-- |
| 

Habit-based recommendation

 | 

Celia Suggestions

 | 

Apps or atomic services share intents with the system. Then the system learns the intent patterns and recommends services at the proper time. For example, after your app or atomic service shares intent data with the system about user browsing news, Celia Suggestions can learn habitual patterns and recommend suitable browsing services and content to the user at the right time.

 |
| 

Event-based notification

 | 

Celia Suggestions

 | 

Apps or atomic services share intents with the system. Then the system extracts events from the intents and recommends services to users based on information such as the time and location. For instance, after your app or atomic service shares a user's movie ticket order data with the system, the system can extract key information such as time and location. Celia Suggestions will then inform the user of the movie at the appropriate time.

 |
| 

Skill call (through voice input)

 | 

Celia Chat

 | 

The system tries to understand users' explicit or implicit intents based on their input by using the AI foundation model and helps users access appropriate functions of apps or atomic services. For instance, if a user asks "How much is a flight from Shenzhen to Beijing?" in a conversation with Celia, it can understand the user's intent to search for flight tickets, call the flight ticket search intent provided by your app or atomic service, obtain relevant data, and present the data to the user.

 |
| 

Local search

 | 

Celia Search

 | 

Apps or atomic services share intents with the system. Then the system builds local indexes for the entities contained in the intents to satisfy users' search requirements. For example, after your app or atomic service shares news related to HUAWEI DEVELOPER CONFERENCE with the system, a user can enter keywords through the entry point to search for relevant news in your app or atomic service.

 |

#### Intent Execution Logic

In the interaction between HarmonyOS and apps or atomic services, there are two intent execution modes: intent call and intent sharing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/LQ_WR9QNT_e7kjpaDtNzMg/en-us_image_0000002402161833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=744DDD926476109222FE5FB121C7CDAF2CFCC6BCF5488E83C7D8D382CBE2872D "Click to enlarge")

| 
Intent Execution Mode

 | 

**Initiated By**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

**Intent sharing**

 | 

Apps or atomic services

 | 

Apps or atomic services proactively share intents with HarmonyOS. The intents can be used by HarmonyOS to build local content indexes and learn user behavior patterns to support local search and provide proactive suggestions.

Intent sharing involves two aspects: actions and entities. Actions contain two statuses: executed and expected.

-   Executed: User intents have been executed, and shared data can be used for local search and system recommendations.
-   Expected: Intents are predicted based on user behavior, and shared data can be used for local search.

Intents Kit also allows you to share auxiliary entities, such as location information, with the system, to enhance scenario-based recommendation and other smart distribution functions.

 |
| 

**Intent call**

 | 

HarmonyOS

 | 

HarmonyOS proactively calls functions of apps or atomic services.

After a user inputs information at a system entry point or the system proactively recommends content, the system can call functions of apps or atomic services, such as playing music, viewing travel tips, or searching for videos.

 |

#### Restrictions

-   Devices

This kit is applicable only to phones, tablets, and PCs/2-in-1 devices. It is not supported on the Emulator.

-   Regions

This kit is available only in the Chinese mainland.

-   Operating systems

This kit is supported by HarmonyOS 5.0 or later.
