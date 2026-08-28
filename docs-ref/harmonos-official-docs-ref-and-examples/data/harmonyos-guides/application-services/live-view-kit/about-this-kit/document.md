# About This Kit

Live View Kit enables apps to display the real-time status of orders or services on key device screens, and manages the lifecycle and UI effect of the displayed information.

#### Use Cases

Live view is a notification form that helps users focus on ongoing tasks and quickly view and process the notified events in a timely manner. Live view messages feature a specific period, timeliness, and updates.

Live view messages can be displayed in capsule or widget mode on the notification panel, status bar, and lock screen.

| 
Notification Panel

 | 

Status Bar

 | 

Lock Screen

 |
| :-- | :-- | :-- |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/l7Fdu00aTIi5HkB__rGtdA/en-us_image_0000002511871742.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FF8AE15457DA5B6F758D5AA05581B0999357CA0F0EEBE75684E9897520A53D5 "Click to enlarge")

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/do-wuJBfS3-venVHm3Gmjw/en-us_image_0000002543551671.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD2ED3277CB383943F3833D170411DCF9F7E80AF751AB8AF73EEC3D14B0B6C13 "Click to enlarge")

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/KYvFMzJkTwCg1tSdwAEkOA/en-us_image_0000002543471659.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D53B6894456B771499FBB073DD8D9DB6208AC31B1F237C262BE8C71690E6D97 "Click to enlarge")

 |

## Specific Period

An event or service needs to last for a period of time with the definite start time and end time, rather than a one-off reminder or message.

For example, ride hailing and food delivery last for a certain period from the start to the end, so they are applicable scenarios of live view messages. On the contrary, notifications about weather and movie tickets are one-off and do not belong to live view messages.

## Timeliness

The live view content is a notification of an ongoing event or service. The information is valuable to users in a specific period.

For example, ride hailing and food delivery are ongoing activities. When a user buys an air ticket for a flight in two days, no notification is sent when the user buys it. Instead, a live view message will be sent to the user a certain period (determined based on the actual business requirements) before departure. System status notifications such as required permissions and function standby are not live view messages.

## Updates

Live view content needs to be dynamically updated to present users with the latest status.

#### Highlights

-   **Compatibility with all phones and tablets running HarmonyOS 5 or later**
    
    Completely decoupled from device hardware, Live View Kit is compatible with all phones and tablets running HarmonyOS 5 or later.
    

-   **Multiple touchpoints**
    
    Once you've integrated Live View Kit into your app, live view messages can be displayed through multiple touchpoints such as the lock screen, notification panel, and status bar.
    

-   **Uninterrupted operations**
    
    Users can view a live view capsule on any touchpoint or tap the live view capsule to view detailed event progress.
    
    After tapping the live view capsule, users will be redirected to the landing page to quickly view the detailed information in the app.
    

-   **Timely service progress update**
    
    Users can follow the latest service progress through multiple touchpoints in a timely manner. This helps businesses achieve quick and efficient closed-loop management of services.
    

#### Applicable Scope and Scenarios

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/P_DEo1zbQseRo-TsUDucxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D61A3D6EF155C71D49AA6BED316868BACB4FEAB0369CC5DB37DDCDD34DD4ABA)

-   Live View Kit is preferentially available to apps that meet the requirements on applicable scope and application scenarios.

-   Live View Kit is compatible with **HarmonyOS 5 or later**.
-   Live View Kit is currently supported only on **phones** and **tablets**.
-   Currently, Live View Kit is available only in the Chinese mainland.

## Application Scenario Requirements

-   The activity must be of great concern to users and requires repeated viewing or shortcut operations.
-   The activity must have a start time and an end time, and lasts for no more than 8 hours.
-   Users have a clear expectation on receiving live view messages of the activity. And generally the live view messages are triggered by user operations.
-   The live view messages must be valuable to users, and cannot be used for marketing or advertising purposes.

## Applicable Scenarios

| 
**Scenario**

 | 

**Event Value**

 | 

**Description**

 | 

**Applicable Scope**

 |
| :-- | :-- | :-- | :-- |
| 

Ride hailing

 | 

TAXI

 | 

After a user books a ride through a ride-hailing app, the live view displays information such as the estimated pickup time and remaining distance and time to the user.

 | 

Applicable to scenarios such as online ride hailing, taxi hailing, carpooling, and hitchhiking.

 |
| 

Instant delivery

 | 

DELIVERY

 | 

The delivery personnel deliver meals and products to users at the specified location, generally within a short period of time.

 | 

Applicable to scenarios such as take-out, fresh food delivery, and intra-city delivery.

 |
| 

Flight

 | 

FLIGHT

 | 

After a user follows a flight, the live view displays key updates of the flight, such as boarding, departure, delay, cancellation, and arrival.

 | 

Applicable to scenarios where the user travels through a flight or follows the progress of a flight.

 |
| 

High-speed train/Common train

 | 

TRAIN

 | 

When a user travels by high-speed train or common train, the live view displays information such as the boarding gate, seat number, train number, and train running status to the user.

 | 

Applicable to scenarios where the user travels by high-speed train or common train.

 |
| 

Queuing

 | 

QUEUE

 | 

A user needs to queue to enjoy relevant services in order.

 | 

Applicable to scenarios where queuing and number calling are required, such as service halls, hospitals, banks, and restaurants.

 |
| 

Meal pickup

 | 

PICK\_UP

 | 

A user places an order for a meal or product, and picks up the meal or product by themselves.

 | 

Applicable to the onsite meal pickup scenario, including reminders on the queuing information, meal preparation progress, and meal pickup.

 |
| 

Live scores

 | 

SCORE

 | 

The live view displays live score updates of both parties in a competition.

 | 

Applicable to scenarios with live score updates, such as gaming events and sporting events.

 |
| 

Shared leasing

 | 

RENT

 | 

When a user uses the temporary leasing service, the live view displays the leasing information such as the real-time leasing duration and fee to the user.

 | 

Applicable to scenarios such as bicycle sharing, mobile power pack sharing, temporary parking in parking lots, and electric vehicle fast charging.

 |
| 

Timing

 | 

TIMER

 | 

A user uses a timer or countdown to track the duration of a short period of time or the time remaining until a task begins.

 | 

Applicable to scenarios like focused work sessions, Pomodoro timers, and ticket purchase countdowns. These scenarios are only accessible for tools apps (the timer scenario can only be created and updated on devices).

 |
| 

Subscription timing

 | 

SUBSCRIBE\_TIMER

 | 

After a user subscribes to a product launch reminder, the system will send countdown notifications prior to the sale.

 | 

Applicable to scenarios where a user actively subscribes to a countdown reminder for a single product and a single sales session.

 |
| 

Workout

 | 

WORKOUT

 | 

The live view displays information such as the workout duration and progress to users in real time.

 | 

Applicable to outdoor or indoor workouts, such as running and cycling.

 |
| 

Navigation

 | 

NAVIGATION

 | 

The live view displays the next upcoming change in the route when a user is utilizing the navigation service.

 | 

Applicable to walking, cycling, and vehicle navigation.

 |

#### Restrictions

-   When integrating Live View Kit into your app, you must [enable Live View Kit](../preparations/document.md).
-   A local live view can be created only when the matching app is running. After the creation, the live view can be updated either locally or through Push Kit.
-   A live view can be updated through Push Kit, regardless of whether the matching app is running or not. With Push Kit, live views can be properly updated and ended within their lifecycle.
-   The lifecycle of a live view cannot exceed 8 hours. After 8 hours, the system considers that the live view ends.
-   For live view update through Push Kit, the messages of a single live view can be updated for up to 30 times every 5 minutes and 180 times every hour on each device in the ride hailing and live score scenarios. In other scenarios, the messages of a single live view can be updated for up to 10 times every 5 minutes and 60 times every hour per device. The excess messages will be discarded.
-   To ensure the timeliness of the live view content, you need to update the live view promptly. The system automatically adjusts the live view display in the following scenarios:
    -   If a live view hasn't been updated for over 2 hours, the system will hide it from the status bar capsule and lock screen capsule, but it will remain visible in the notification panel.
    -   If a live view hasn't been updated for over 4 hours, the system will consider it ended and remove it from all display entries.
-   Users can delete a live view message at any time when it is displayed. After the deletion, the message updates will not be displayed any more.
-   Currently, [live view creation through Push Kit](../../push-kit/pushing-scenario-specific-messages/pushing-a-live-view-message/document.md) only supports the **FLIGHT**, **TAXI**, and **TRAIN** scenarios.
-   The flow control mechanism for live view creation and update is as follows:
    -   System-level flow control (for all apps): A maximum of 15 live view creation requests and 30 live view update requests can be processed per second. The excess requests are discarded.
    -   App-level flow control (for a single app): A maximum of 10 live view creation requests and 20 live view update requests can be processed per second. The excess requests are discarded.

#### Development Process

Follow the steps in the following process when you integrate Live View Kit.

| 
Step

 | 

Description

 |
| :-- | :-- |
| 

Following [Live View Design Specifications](../live-view-design-specifications/document.md) to design the live view message style

 | 

Design your live view message style based on the available style templates.

 |
| 

[Preparations](../preparations/document.md)

 | 

Enable Live View Kit in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

 |
| 

[Creating a Local Live View](../app-development/creating-a-local-live-view/document.md)

 | 

Develop a local live view based on [Live View Design Specifications](../live-view-design-specifications/document.md).

 |
| 

[Creating a Live View Through Push Kit](../../push-kit/pushing-scenario-specific-messages/pushing-a-live-view-message/document.md)

 | 

Use Push Kit to create a live view.

 |
| 

[Updating a Live View Through Push Kit](../app-development/updating-a-live-view-through-push-kit/document.md)

 | 

Use Push Kit to update a live view.

 |

#### Penalties for Violations

Live view messages sent by your app must comply with both [Live View Design Specifications](../live-view-design-specifications/document.md) and Push Kit's [Notification Content Management Rules](../../push-kit/appendixes/notification-content-management-rules/document.md). Any action that violates the specifications and requirements will be regarded as a violation.

For details about the violations and penalties, please refer to [Violation Types, Violation Actions, and Penalty Criteria](../../push-kit/appendixes/push-notification-violation-penalty-criteria/document.md#section1385731811412).
