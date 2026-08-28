# Performance Detection

#### Time-Consuming Launch Event Detection

#### Overview

Time-consuming launch events are used to measure the time consumed in the application launch process that can be perceived by the system and users. The measurement can be implemented in various scenarios, including launch from the home screen, status bar, and recent task list. You can subscribe to this event to obtain the time consumed in key phases of the launch process.

## Principles

The start time of the launch event statistics is when the user taps the screen, and the default end time is when the launch animation is complete. You can call the [reportDrawCompleted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#reportdrawncompleted10) API to pass the custom end time as required.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/jf0yClHnR4KqSMAGyKh0Kg/en-us_image_0000002529715091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72326C13A674EAD9D51B57CE8A35CA65145E430B06BBA01211E95D070D3532C5 "Click to enlarge")

**icon\_input\_time**: time when the user taps the screen

**animation\_finish\_time**: launch duration defined by the system from when the finger leaves the screen to when the launch animation ends. This duration cannot be customized.

**extend\_time**: custom launch duration from when the finger leaves the screen to when the [reportDrawnCompleted](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/js-apis-inner-application-uiextensioncontext-V5#uiextensioncontextreportdrawncompleted12) API is called. You can call the **reportDrawnCompleted** API at a proper time as required. If the API is not called or is not called within 5 seconds after the finger leaves the screen, the value of this indicator is **0**.

## Constraints

1\. The launch event indicates that the application is started by users, excluding the automatic process restart.

2\. The launch duration is a behavior event, which is reported immediately after being triggered and is not restricted by the threshold.

## How to Obtain Events

You can use HiAppEvent to subscribe to the time-consuming launch event and related information. For details, see [Introduction to HiAppEvent](../event-subscription/introduction-to-hiappevent/document.md) and [Event Subscription (ArkTS)](../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/time-consuming-launch-events/event-subscription-arkts/document.md).

#### Scrolling Event Detection

#### Overview

Scrolling frame loss events are used to detect frame freezes during list scrolling. If this event is subscribed, it is reported when frame freezes last for more than 50 ms during list scrolling.

## Principles

1\. Calculation method

Scrolling frame loss events are reported when frame freezes occur in the application main thread or the RenderService process during list scrolling.

The scrolling process starts when the scrolling gesture is recognized and ends when the page stops scrolling. The frame freeze duration is calculated separately from the application main thread and RenderService.

2\. Reporting threshold

If the duration of a single frame exceeds 50 ms, a scrolling frame loss event occurs. Specifically, this event is reported when the value of **max\_render\_frametime** or **max\_app\_frametime** exceeds 50 ms.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/BOtVvv9cQpeA35lJGYjQmA/en-us_image_0000002529595105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=698A0F45F3C6A56410029D4ACD6939F3811D93A78085A1BF123F8F4F7625C9AD)

## Constraints

If the duration of a single frame does not exceed 50 ms, this event is not reported.

#### Logging Mechanism

Scrolling frame loss events trigger the call stack collection of the main thread.

1\. Start time

The sampling stack functionality for scrolling frame loss events is enabled only during scrolling.

2\. Stack sampling time

The stack sampling is triggered when the freeze duration of the application main thread reaches the reporting threshold during scrolling.

#### Log Specifications

1\. Log aging

In most cases, the size of a stack file is 7 KB to 10 KB. The **watchdog** directory in the app sandbox can store a maximum of 10 MB files. If the total file size exceeds 10 MB, you need to manually delete files. The path to **watchdog** is **/data/storage/el2/log/watchdog/**.

If you do not manually delete the files, the system will delete them.

2\. Obtaining logs in events

You can obtain the log path from **external\_logs**.

3\. Sampling stack format

Currently, stack capturing supports only the ARM64 architecture. The stack capture result contains both native frames and JS frames parsed. To avoid excessive consumption of system resources, a process can be collected only once a day.

An example of the stack capture result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Odc3UhzvSveYtCwUU8Nb4Q/en-us_image_0000002497755126.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B2C2F414759DFC396461C505A90DAE574FABECB8E086AEC2BAE754C8AC0D512)

## How to Obtain Logs

HiAppEvent provides APIs for subscribing to faults. For details, see [Introduction to HiAppEvent](../event-subscription/introduction-to-hiappevent/document.md). To subscribe to the scrolling frame loss event, see [Event Subscription (ArkTS)](../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/scrolling-frame-loss-events/event-subscription-arkts/document.md).
