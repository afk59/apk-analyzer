# Intents Kit Integration Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/zAzHtliSRnCj0VUtPquB_Q/en-us_image_0000002402161841.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50EEC1CC5637AC8E0F45A640345B89CCAC0B0459FB83DD020A297E0B9E25F510 "Click to enlarge")

| 
**Phase**

 | 

**Task**

 | 

**Description**

 | 

**Example**

 | 

**Reference Document**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

**Purpose**

 | 

Select features and determine intents.

 | 

Select features from the available feature list based on the desired user experience, and determine the intents to be implemented based on these features.

 | 

If you want to implement the feature of recommending a song to be resumed, you need to implement the **PlayMusic** intent based on the description of the smart distribution feature.

 | 

/

 |
| 

**Development**

 | 

Apply to be added to the debugging trustlist.

 | 

Send an email to **hagservice@huawei.com** or contact Huawei Intents Kit staff, and provide information about your app to be tested, to apply to Huawei for adding your app to the debugging trustlist.

 | 

1.  App name: HUAWEI Music
2.  App package name: com.xxxx
3.  Intent name: PlayMusic
4.  App icon format: JPG, PNG, and others
5.  App ID: 1234567
6.  Client ID: 1234567
7.  HUAWEI ID (UID): 1234567, 7654321, and others

 | 

For details, please refer to the following links:

Habit-based recommendation: [Testing Solution](../habit-based-recommendation-solution/testing-solution/document.md)

Event-based notification: [Testing Solution](../event-based-notification-solution/testing-solution/document.md)

 |
| 

Register an intent in the intent declaration file.

 | 

Register your intent during development in DevEco Studio.

 | 

Register the **PlayMusic** intent.

 | 

For details, please refer to [Registering an Intent](../habit-based-recommendation-solution/integration-solution/document.md#section12621163216260).

 |
| 

Implement intent calls/intent sharing.

 | 

Develop a HarmonyOS API for intent sharing, so that the intent data in your app or atomic service can be shared with the system.

 | 

Develop an intent sharing API for the **PlayMusic** intent.

 | 

For details, please refer to [Sharing a Device-Side Intent](../habit-based-recommendation-solution/integration-solution/document.md#section14210125472916).

 |
| 

Develop a HarmonyOS API for intent calls, so that the intent in your app or atomic service can be called.

 | 

Develop an intent call API for the **PlayMusic** intent.

 | 

For details, please refer to [Calling a Device-Side Intent](../habit-based-recommendation-solution/integration-solution/document.md#section9408948143016).

 |
| 

**Verification**

 | 

Perform end-to-end feature verification.

 | 

Use the test capability provided by Huawei to perform end-to-end debugging of the target feature. After completing the debugging, submit the smart distribution configuration for review.

 | 

Perform an end-to-end test on the feature of recommending a song to be resumed in HUAWEI Music. After the test is complete, submit the smart distribution configuration.

 | 

/

 |
| 

**Release**

 | 

Release your app or atomic service on AppGallery.

 | 

After completing the development and packaging, upload your package to AppGallery.

 | 

Package HUAWEI Music and release it on AppGallery.

 | 

For details, please refer to the [process for releasing an app](https://developer.huawei.com/consumer/en/doc/app/agc-help-releaseharmony-0000001933963166).

 |
| 

Register with Intents Kit.

 | 

Configure intent registration on Celia Open Platform and submit it for review. The request will be reviewed by Huawei technical support within three working days.

 | 

Register the **PlayMusic** intent.

 | 

/

 |
