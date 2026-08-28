# Requirements and Restrictions on IAP Integration

To guarantee a seamless payment process for users, Huawei has outlined specific design guidelines for app integration. To guarantee a smooth app launch, make sure to follow these guidelines. Check the UI design guidelines and integration restrictions described below.

#### UI Design Guidelines

1.  The purchase screen should not show any payment method–related information, including the payment method logo or name (such as Huawei Pay, HarmonyOS Pay, and IAP). The general-purpose button names such as **Buy** and **Subscribe** are recommended. Once a user taps the **Buy** or **Subscribe** button, the app will show the checkout screen of IAP Kit for the user to complete the purchase.
2.  It is recommended that the loading animation effect appear when the IAP Kit checkout screen is shown upon a product purchase request to ensure a smooth purchase process, improving user experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Xs8PlgFkSViMmyFVUtv1zg/en-us_image_0000002413014396.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062108Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9985483687FA9801B7B15D278BCFA00D094D4D5763916F366F47436343D0B11D "Click to enlarge")

#### Restrictions

Apps with virtual products sold must integrate IAP Kit instead of third-party payment methods such as Alipay and WeChat Pay; otherwise, the apps may fail to be launched.
