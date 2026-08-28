# Push Notification Violation Penalty Criteria

#### Violation Types, Violation Actions, and Penalty Criteria

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/9aDa1oqJSFyVa8KEuVCChA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFA30B685F280C2123153501EAB7D65B02315169A06D41411605A1E3C899336D)

If your app is found to be in violation of our policies, your developer account will receive a notification email or SMS message from Push Kit. Please follow the instructions provided in the notification to check the specific violations and corresponding penalties.

| 
**Violations by Type**

 | 

**Penalty**

 |
| :-- | :-- |
| 

**Type I: poor user experience caused by violations of notification layout, redirection action, notification content, notification classification, and notification switch authorization**

**[Notification Layout](../../preparations/integration-specifications/document.md#section66741239491)** **Violation**

-   Forging push messages of other apps, including app names, app icons, and message content.
-   Hiding your app name or icon in a notification.
-   Sending notifications that violate layout design guidelines.
-   Misusing notification styles, such as setting notification background images or changing push text font colors.
-   Forcibly pinning a notification to the top without authorization.
-   Pushing a notification that cannot be directly deleted.
-   Forging banner notifications or lock screen notifications.

**[Notification Redirection](../../preparations/integration-specifications/document.md#section1792717184810)** **Violation**

-   Launching an app process in the background via push messages.
-   Waking up another app via push messages.
-   Tricking users into downloading a third-party app via push messages.
-   Linking to an illegal website when a user taps the notification.

**[Notification Content Principles](../notification-content-management-rules/document.md#section146985016916)** **Violation**

-   Pushing a notification that violates the consistency, accuracy, readability, or compliance principle.

**Notification Classification Violation**

-   The notification classification does not comply with [Message Classification Standards and Notification Modes](../../preparations/applying-for-scenario-specific-message-permissions/document.md#section1924971516101).

**[Notification Switch Authorization](../../preparations/integration-specifications/document.md#section02319296486)** **Violation**

-   Not asking a user whether to allow notifications in a pop-up when your app is launched for the first time.
-   Enabling notifications without user consent.
-   Combining multiple event notifications into a single authorization to trick users into enabling all notifications with a single tap.

**Others**

-   Malicious mutual keeping alive among apps.
-   Other actions that affect the experience of Huawei device users.

NOTE:

Maliciously keeping an app alive refers to the act of bringing an app's process back to life without a user's consent and beyond what is necessary for normal app functionality.

 | 

Penalties for violations within the last 12 months:

-   **Penalty for the first violation**: You will receive an email of warning. If the rectification is not completed within 7 natural days, it will be treated as a second violation and punished accordingly.
-   **Penalty for the second violation**: The app will be suspended from sending news and marketing push notifications for 7 days. If the rectification is not completed within 7 natural days, it will be treated as a third violation and punished accordingly.
-   **Penalty for the third and more violations**: All messages will be silenced within 90 natural days, and your app can send up to 2 messages each day to a device.

NOTICE:

-   Non-compliant apps must be rectified within 7 natural days of the warning and the rectification results must be reported, or Huawei will impose stricter penalties.
-   When submitting your rectification feedback, please refer to the [Rectification Commitment Letter](#section19877944201013).

 |
| 

**Type 2: violation of laws and regulations**

 | 

Push Kit will not be available until the penalty order issued by the administrative regulatory authority is lifted.

 |
| 

**Type 3: poor user experience caused by violations of live view design specifications and scenario-specific rules**

**Violations of design specifications**

-   The live view message does not comply with the design specifications.

**[Scenario](../../../live-view-kit/about-this-kit/document.md) violations**

-   A live view message is not initiated by the user and the user has no definite expectations regarding the content.
-   Live view notifications are employed in marketing, advertising, and other unapproved scenarios.
-   There is a discrepancy between the actual use case of a live view message and that approved in the application.

 | 

The app must complete the rectification within 3 natural days of receiving the violation notification and provide feedback on the rectification results. Failure to do so will result in the revocation of the live view message permission of the corresponding scenario.

NOTICE:

When submitting your rectification feedback, please refer to the [Rectification Commitment Letter](#section19877944201013).

 |

#### Rectification Commitment Letter

When submitting the rectification feedback, you must provide a _Rectification Commitment Letter_ bearing the official seal of the company that released the app, with the following specific content:

To: Huawei Software Technologies Co., Ltd.

Our company's app (app name: \*\*\*; app ID/app package name: \*\*\*; version: \*\*\*), was penalized on \_\_\_\_\_\_ (MM/DD/YY) during the use of Push Kit due to \_\_\_\_\_\_\_ (violation).

Our company hereby confirms that the following corrective measures have been taken in response to the violation:

Problem 1: \*\*\*

Rectification measure:

Problem 2: \*\*\*

Rectification measure:

Rectification completion date: \_\_\_\_\_\_ (MM/DD/YY)

Our company commits to complying with applicable laws and regulations. During the use of Push Kit, we have carefully read and agreed to the _HUAWEI Push Service Agreement_, _Push Kit Integration Specifications_, and other applicable agreements. If our company violates any applicable laws, regulations, or the aforementioned agreements again, we agree to accept Huawei's handling of the app and/or our company. We will independently assume all responsibilities regarding the app. If any loss is caused to Huawei, its affiliates, partners, or other third parties, our company will assume full responsibility and compensate for all resulting losses.

Hereby declared and guaranteed.

#### Violation Penalty Appeal

According to the violation handling rules, if an app has any violations, its corresponding push permissions may be affected.

If you disagree with the violation penalty imposed on your app, you can view the details of the penalty and issue an appeal within three working days of receiving the penalty notification (only three appeals are allowed for the same violation).

To view the violation penalty details, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, find and click your project, go to **Grow** > **Push Kit** > **Settings**, and click the button following **Project status** for details.

Your appeal will be assessed based on its justification, the authenticity of the supporting documents, and the impact of the violation. We will communicate the outcome to you. If the appeal is upheld, the penalty may be mitigated at the discretion of the reviewing body.

For any doubt, send emails to [hwpush@huawei.com](mailto:hwpush@huawei.com).
