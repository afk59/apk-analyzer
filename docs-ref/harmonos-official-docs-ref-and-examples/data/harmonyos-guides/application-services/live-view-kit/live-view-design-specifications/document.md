# Live View Design Specifications

Live view messages sent by your app must comply with the live view design specifications. Solutions that do not comply with the design specifications will not be granted formal permission on Live View Kit. After the live view function goes live in your app, any action that violates the specifications will be regarded as a [violation](../about-this-kit/document.md#section61131311488).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/bYLgKXjXSD-i4a85kxBk-g/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A524E07FB1064E35C751B20FD26EA5E6951F7CB9A86DCE8128F701AAB6D5A9B)

-   The lifecycle of a live view cannot exceed 8 hours. After 8 hours, the system considers that the live view ends.
-   To ensure the timeliness of the live view content, you need to update the live view promptly. The system automatically adjusts the live view display in the following scenarios:
    -   If a live view hasn't been updated for over 2 hours, the system will hide it from the status bar capsule and lock screen capsule, but it will remain visible in the notification panel.
    -   If a live view hasn't been updated for over 4 hours, the system will consider it ended and remove it from all display entries.

#### Design Principles

A live view aims to provide users with simple, convenient, and clear notification content, interaction, and visual effect. Its design must comply with [Live View Design Principles](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section1181711415233).

#### Template Rules

A live view can display messages in both widget and capsule modes for more visualized and simplified effect, helping users focus on important information. When designing a live view widget and capsule, you must comply with the specified rules. You are advised to use the following templates for different scenarios. If these templates cannot meet your service requirements, you may customize your own template.

-   [General Widget Templates](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section1598402815257)
-   [General Capsule Templates](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section198971755122812)
-   [Lock Screen Templates](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section168294023217)
-   [Ultra-Long Text Display Rules](https://developer.huawei.com/consumer/en/doc/design-guides/system-features-live-view-0000001955186861#section938445193413)

#### Node Design Requirements for Different Application Scenarios

When designing live view nodes for a specific scenario, ensure that the following requirements are met. If certain nodes are not listed here, you can add them based on your service needs, but please use the provided node design templates as a reference.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/uIgcMKzlTViXvJtdz3nkmQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4671A37AE3EAF79C5041BDAD0F9C1EE4AB256CAAA9E332BE9031713103080E1)

-   Important live view updates should use strong alerts such as ringtone or vibration, which can be set through the **mute** parameter for cloud-side updates and through the **isMute** parameter for device-side updates. In addition, you can configure the dynamic effect for capsules on the status bar to notify the user, through the **remind** parameter of capsules (only supported for cloud-side updates).

## Instant Delivery

You are advised to integrate user orders that can be completed within 8 hours. The node design requirements are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Node Constraints**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- | :-- |
| 

Pending payment

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/n1EMMJ-jTHCC_67nXmUktQ/en-us_image_0000002511871770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28865B1F0322785042BA933038ED87862ABE8A174A25EC02759E793A64C1C92F "Click to enlarge")

 | 

The **Pending payment** status should be displayed for no more than 5 minutes.

 | 

-   When a user successfully cancels an order, end the live view immediately.
-   When a merchant cancels an order, notify the user of the order information change in a timely manner.

 |
| 

To be accepted by merchant

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Ha1FPBmzQDKBKneGhOpZ_g/en-us_image_0000002512031740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CFD9D1B4326E2A06226552A5B940A859BE358A9FEE6B475B03173444CB6A3A7 "Click to enlarge")

 | 

/

 |
| 

Accepted by merchant

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/G1z83sTxRQqUfv2oYd2NOg/en-us_image_0000002512031712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=003BAC51FED525B208D476CC87E4A2B3E3CAE4C21EA8C8B4AFA13071CFABEA0F "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of preempting the capsule position.

 |
| 

Rider picking up the order

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/QMWVH3a8Sge6XyxN42OVGg/en-us_image_0000002511871774.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D93B347C40026F203B3D270200E9BA071262F0359F404568D73C3FB96968FED4 "Click to enlarge")

 | 

/

 |
| 

Rider arrived at store

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/wsP0Nb7YQk2EPQLhxemeKw/en-us_image_0000002511871778.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA5F76DA188C0D23B95438CF1FEA97D2D10EE10E912E2F36A91668313604F091 "Click to enlarge")

 | 

/

 |
| 

Delivery in progress

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/u8PF5atOSMaCvvuZJJ2vYw/en-us_image_0000002512031736.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A474513B5CF707A975D51AE278A9EA135C011A9D14D5F1DC28D141851CA98584 "Click to enlarge")

 | 

/

 |
| 

Delivered/Ready for pickup

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/mzD-pzMKR2yUP-UhqRh4fA/en-us_image_0000002512031758.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51C0426CF0C2D94E0E31A970B63181C8F3CFD405B497D49C487C6AD2E064C2AB "Click to enlarge")

 | 

-   Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.
-   Status removal: The **Delivered** or **Ready for pickup** status is displayed for up to 5 minutes. Upon direct handover, the status is removed immediately.

 |

## Ride Hailing

Ride hailing can be classified into two categories based on whether a user departs immediately: immediate ride-hailing and scheduled ride-hailing.

In the ride hailing scenario, messages of a single live view can be updated for up to 30 times every 5 minutes and up to 180 times per hour on each device. The node design requirements are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Node Constraints**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- | :-- |
| 

Requesting a car

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/H4ac--S0SNOMhL-cIrM_7A/en-us_image_0000002543471681.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ECD27D89631081AD99BE93B14052D524C4F17EAC95754EE1351BB2823A1DB14 "Click to enlarge")

 | 

/

 | 

-   When a user successfully cancels an order, end the live view immediately.
-   In the case of order cancellation by the driver or driver reassignment, update the live view, set the reminder mode to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget to promptly remind the user.
-   In the case of scheduled ride-hailing, create a live view through the Push Kit server 20 minutes before the scheduled departure to remind the user.

 |
| 

Queuing

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/WuvM_5ZkQlaFwLsNIMwXYg/en-us_image_0000002543471665.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5B893231092C831FA7EBA4C209D59AFA5BD5E1EF303A1844E23CA3A19C78EDE "Click to enlarge")

 | 

/

 |
| 

Driver completing previous trip

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/NFVg3tUaSLmEO9m7ly0OZg/en-us_image_0000002512031742.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=479AA508FEC95FCF5679F932703E528C8F043A2981B10CF73CCB481233053E74 "Click to enlarge")

 | 

/

 |
| 

Driver on the way

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Vu_TE1fSQ4K7w7HpZHlHpw/en-us_image_0000002543471699.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7992796E641ECB374E66E6C29D3B1035C514A7317A480E5B7DDF87DED56CE479 "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of preempting the capsule position.

 |
| 

Arriving soon

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/tjehE15PTgiWVoNoaOAWhA/en-us_image_0000002543551699.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8797428E2BB203BDF5738A053F2FAB37AD31539077F8656DB5049085FC8D6784 "Click to enlarge")

 | 

/

 |
| 

Driver arrived

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/7HdszllkR_u4Q9B1271Gqg/en-us_image_0000002543551673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A18437A0E4A56EDF017D3D58E2170546E52C4ADA51EC7166A02E553AED03E47 "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.

 |
| 

Heading to destination

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/1BCAe1i6QHis5W-Cug6zCw/en-us_image_0000002511871754.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=208734D36E1EB20F56BB2124BAE234362CD72513E3FB93BF78B0AF25205A7F24 "Click to enlarge")

 | 

/

 |
| 

Trip completed

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/PlF63wapSL2-Y70Q7e2ttA/en-us_image_0000002543471649.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75053B2D72EB398606F97C14E0A784A090B5D9069DB51B0E4C551B11005A1BA8 "Click to enlarge")

 | 

-   Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of preempting the capsule position.
-   Status removal: The **Pending payment** status is displayed for up to 5 minutes, and is removed immediately upon successful payment.

 |

## Meal Pickup

The node design requirements are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Node Constraints**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- | :-- |
| 

Order placed

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Gz2Avk5bShmHhHJZcQ8E2A/en-us_image_0000002543551705.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A23B3884C85B8F8253BC73583EE489C4DE93492F256CDBD0559BFE275EE37D12 "Click to enlarge")

 | 

/

 | 

When a user successfully cancels an order, end the live view immediately.

 |
| 

Meal in preparation

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/koO4dCOHRUCqCe9uzxpoXA/en-us_image_0000002511871776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC45F35BD2F34275C9D4D5B33286A7C95B39211457F1AD3E974F71E7356B31DB "Click to enlarge")

 | 

/

 |
| 

Meal ready

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/-YuHo-1gQ0C9a06Pl6FvEg/en-us_image_0000002512031752.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB71E3798271211F9739DADEE58F0A0CA606EB3F28349ACCDA728B656EC1AF6B "Click to enlarge")

 | 

-   Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.
-   Status removal: The **Ready for pickup** status is displayed for up to 15 minutes, and is removed immediately when a user picks up the meal.

 |

## Queuing

**Queuing for a meal:**

The node design requirements in the scenario of queuing for a meal are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Node Constraints**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- | :-- |
| 

Queuing

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/9Wuf3LCcR2qSjemSnh77zQ/en-us_image_0000002512031760.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A73DA139C3D4F691E873909B2829669AFDAE35B3968E79F0949B1900B4D4A03 "Click to enlarge")

 | 

/

 | 

When a user successfully cancels queuing, end the live view immediately.

 |
| 

Coming up

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/wdjJrkZ-Sa-b58kyJpTjzQ/en-us_image_0000002511871726.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5674072D3C36546D2B725C66F815F0EA8F87A42645E4CE4A5309EC0979B271D "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.

 |
| 

Number being called

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/zo6i4h-USJuJiognfPrAbA/en-us_image_0000002511871764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AEA34FF969A788978BDCAC3D01CA98BDAD7862C3194856540B81EF2B4DF1F16 "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of preempting the capsule position.

 |
| 

Missed turn

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/11iSvr4pRC-900nbGTpcZQ/en-us_image_0000002543551713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53F1D165EB21F240BDB09984919457151312D7FED43D9726FBDB71AB0A041383 "Click to enlarge")

 | 

Status removal: The **Missed turn** status is displayed for 5 minutes.

 |

**Queuing in the bank:**

The node design requirements in the scenario of queuing in the bank are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Node Constraints**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- | :-- |
| 

Queuing

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/lZGFzk1bRUa9u6OVcbbZTA/en-us_image_0000002511871772.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F08B7886B6F6EC17F7B3C3806362D026F1800DA4083EA00484BB4000DB7B368E "Click to enlarge")

 | 

/

 | 

-   When a user successfully cancels queuing, end the live view immediately.
-   In the case of appointment queuing, display a live view message to remind the user 30 minutes in advance.

 |
| 

Number being called

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/ks2sKVrpQaC4C74b1jEOKQ/en-us_image_0000002543471689.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C81BF5127419BC6CDAA014FE68204BE016043D0D6E0F99301362BEA4FA8DA00C "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.

 |
| 

Missed turn

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Dy52O-XMRUiS8KDV5JoLaA/en-us_image_0000002512031762.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24A005F3B21F50FA155B26AFB0BA23A7B4FE58205DE4560F4D1412948C04D078 "Click to enlarge")

 | 

Status removal: The **Missed turn** status is displayed for 5 minutes.

 |

## Timing

You are advised to integrate timing that lasts for no more than 8 hours. The live view can only be created and updated on devices. The node design requirements are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- |
| 

Timing in progress

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/lrWn_b0_RnmOTl9S55BHSw/en-us_image_0000002543471673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFDBACDAB7AF4625227B5BD5926708214ED3D3092210FF3EB2EFDD371BF8EBC6 "Click to enlarge")

 | 

When a user actively or passively stops timing, end the live view immediately.

 |
| 

Paused

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/DilaEzUdQ1CwJSfaeBTGTQ/en-us_image_0000002511871744.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDC577CCF5E5025638EC9C8A74028B8121E4155685E19253A3137DDA559483D0 "Click to enlarge")

 |

## Air Travel

Display live view messages 3 hours before the scheduled departure in the air travel scenario. The node design requirements are as follows.

| 
**Node**

 | 

**Design Template**

 | 

**Node Constraints**

 | 

**Special Consideration**

 |
| :-- | :-- | :-- | :-- |
| 

Not checked in

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/TxpwixnPRRCxGJaTHpIRuQ/en-us_image_0000002543551711.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2680A6DA6EF3165E510D38315464A2E6C3AF27A3D5A3108160C8C7F511BD338 "Click to enlarge")

 | 

If online check-in and seat selection are not supported, remind the user to check in at the airport.

 | 

-   In the case of seat number changes, update the live view message promptly to display the new seat number information.
-   In the case of boarding gate changes, update the live view message promptly and set a message reminder to notify the user of the new boarding gate information.
-   In the case of delays, update the information in the extension area and notify the user of the delay and estimated departure time.
-   In the case of flight cancellation or change initiated by a user, end the current live view and create a new live view based on the user's new flight schedule.
-   Provide also live view notification solutions for the following special cases: a flight's cancellation, connection, return, unscheduled landing, loss of contact, and accident.
-   If a user only follows a flight, display live view messages to notify the user of key updates about the flight, such as boarding, departure, arrival, delay, and cancellation.

 |
| 

Checked in

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/H1E4MklTTqicYDXf5oFjIg/en-us_image_0000002543551697.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C37071D5085DE3E96A50B01BFDE9F92958212DBCC3ED74ED6E61E9100DBF89FF "Click to enlarge")

 | 

/

 |
| 

Boarding started

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/u4qjwH0hQF6WFOyNUDg49A/en-us_image_0000002543471671.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1360CDAD3223EE8D731E06F1515598651AEB2C1773EB9158DFDB964C15DC818 "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.

 |
| 

Last boarding call

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Z0Z8orYaSiKvzeGkco0M5g/en-us_image_0000002543471661.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A19EFC70B59F27D3BB57DC37C41BC692C6101B30020C06B30F51F9AD62E3F841 "Click to enlarge")

 | 

If a user has boarded the plane, this node is unnecessary.

 |
| 

Boarded

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/NuZikIPiS8mATTwPR6jbVA/en-us_image_0000002511871766.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80AE078B625AF935A2ABAE095DFE579B155980EB7A10480BF4590A188C1F9538 "Click to enlarge")

 | 

/

 |
| 

Departed

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/gMuaHlToTOuKn9jRsT0qmQ/en-us_image_0000002543551703.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9921B32471AEF9AB00036F967607656923C6DE4AC359F97E1D135D2378DF23C "Click to enlarge")

 | 

/

 |
| 

Arrived

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/zsoQBmObRgeLjgbreVtepA/en-us_image_0000002543471651.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0686536315622ADD64C505B3AD61D09E5487814451DB8988AF2A2E9902E4BFA3 "Click to enlarge")

 | 

Status removal: The status is removed immediately for baggage-free trips. If a user checked baggage, the status will be displayed for 30 to 60 minutes.

 |
| 

Delayed

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/O7yZ-XqpSFOP6bSBEg6z0w/en-us_image_0000002543471687.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF6DA0C18E8D734A5D25FC275F69A68B08E56CB8CFF9FE723B7F518051327D63 "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.

 |
| 

Canceled

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/lUS_PDn2RPC7feCsmxVCwg/en-us_image_0000002512031738.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE8B0BEC8E345A67DE08983DE0E06F365C1A9CC0984D2F7494D895E7C6CF7603 "Click to enlarge")

 | 

-   Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.
-   Status removal: The status is displayed for up to 30 minutes.

 |
| 

Boarding gate changed

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Fhyg7XqUTOCNFJnQlwo3kQ/en-us_image_0000002543551707.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=753DBCEB1A80AC81B72258725ECFFFEEF7D4582851FB5B93CD7AB16EC00A20B4 "Click to enlarge")

 | 

Reminder mode: Set it to ringtone or vibration, and configure the dynamic effect of automatically expanding the capsule into a floating widget.

 |

## Rail Travel

Display live view messages 1 hour before the scheduled departure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ksVlCIBFTrS2e36QPS2BYg/en-us_image_0000002543551695.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B095DE864FFA53345B5F774BCD788385D1A024A001386B9854556731ECA478D)

| 
**Key Information to Be Displayed**

 | 

**Special Consideration**

 | 

**Key Node Requiring Notification**

 |
| :-- | :-- | :-- |
| 

-   Train number
-   Seat number
-   Boarding gate
-   Departure station
-   Departure time
-   Arrival station
-   Arrival time

 | 

-   In the case of high-speed train delays, update the live view message to notify the user of the delay and estimated departure time.
-   In the case of temporary train stops, update the live view message to notify the user of the stop and related key information such as the reason for the stop and the estimated departure time.
-   In the case of high-speed train cancellation, update the live view message to notify the user of the cancellation and related key information.
-   After a user reschedules their trip, display the latest itinerary in the live view and remove the outdated trip.
-   After a user cancels their trip, end the currently displayed live view.

 | 

-   Scheduled departure
-   Arrived

 |

## Shared Leasing

You are advised to integrate shared leasing that lasts for no more than 8 hours.

The key nodes in shared leasing can be sorted out based on the following process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/t9rMkPy1SjKBLewEHri_RA/en-us_image_0000002512031764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10C1042870EEBB47A96B6BB5D7BB73011AC6435C9D66BDCBCB658276E98279B2)

| 
**Key Information to Be Displayed**

 | 

**Special Consideration**

 | 

**Key Node Requiring Notification**

 |
| :-- | :-- | :-- |
| 

-   Lease duration
-   Lease fee

 | 

-   When a user temporarily pauses a rental, notify the user of the rental status change in a timely manner.
-   In cases where an item cannot be rented due to a malfunction or other reasons, notify the user promptly.

 | 

-   Lease ends
-   Pending payment

 |

## Workout

| 
**Key Information to Be Displayed**

 | 

**Special Consideration**

 | 

**Key Node Requiring Notification**

 |
| :-- | :-- | :-- |
| 

-   Workout duration
-   Remaining distance

 | 

-   When the workout is interrupted or paused, notify the user in a timely manner.
-   When an anomaly is detected during the workout, notify the user promptly.

 | 

-   Workout in progress
-   Workout complete

 |

## Navigation

| 
**Key Information to Be Displayed**

 | 

**Special Consideration**

 | 

**Key Node Requiring Notification**

 |
| :-- | :-- | :-- |
| 

-   Route change
-   Remaining distance and time required

 | 

-   Upon route changes, notify the user of the latest route promptly.

 | 

-   Navigation in progress
-   Navigation ends

 |
