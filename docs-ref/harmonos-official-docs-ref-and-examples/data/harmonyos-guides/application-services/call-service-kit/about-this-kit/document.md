# About This Kit

Call Service Kit is an in-app call management service provided by HarmonyOS.

By integrating Call Service Kit, you can enable features such as one-tap answering, banner notifications, and muting and unmuting, enhancing user experience.

#### Use Cases

In-app calls include incoming and outgoing calls.

-   Incoming call
    
    The app receives a voice or video call through the network.
    
    The app needs to report incoming call information to Call Service Kit, and the system will then display a notification banner to the user. The user can answer or reject the call, mute or unmute it, or hang up through the banner.
    
    Additionally, Call Service Kit supports lock screen notifications and multi-call notifications.
    
-   Outgoing call
    
    The app initiates a voice or video call. Services for outgoing calls are similar to those for incoming calls, with the following differences:
    
    -   When an outgoing call is made, the call capsule appears in the upper left corner of the screen since the app is in the foreground and no notification banner is needed.
    -   Multiple outgoing calls cannot occur simultaneously. That is, only one outgoing call can be made at a time.

#### Relationship with Other Kits

When the app is running in the background and an incoming call is received, [Push Kit](../../push-kit/document.md) needs to be used to launch the app's main process before the app can report the call to Call Service Kit.

Service process:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/mDcTNgnyRouMSsQffm7gQQ/en-us_image_0000002444622308.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E91DBBC981EB88B83500764265EA58A91FE66AEF3A8470C3A3EF6E81153BAA9F "Click to enlarge")

#### Restrictions

## Device Restrictions

Sample code provided in this guide is supported only on standard systems and is not compatible with emulators.

| 
Capability

 | 

Supported Device

 |
| :-- | :-- |
| 

Incoming call

 | 

Phones, tablets, and wearables

 |
| 

Outgoing call

 | 

Phones, tablets, and wearables

 |
| 

Displaying enterprise contact information on the incoming or outgoing call screen

 | 

Phones, tablets, PCs/2-in-1 devices, and wearables

 |

## Number of Calls

-   A maximum of three in-app incoming calls are supported at the same time.
-   A maximum of one in-app outgoing call is supported at the same time.

## Supported Countries/Regions

Call Service Kit is now available only in the Chinese mainland.

## Restrictions of Relevant Kits

Since Call Service Kit relies on Push Kit, it is also necessary to refer to the [restrictions for Push Kit](../../push-kit/about-this-kit/document.md#section15315537123318).
