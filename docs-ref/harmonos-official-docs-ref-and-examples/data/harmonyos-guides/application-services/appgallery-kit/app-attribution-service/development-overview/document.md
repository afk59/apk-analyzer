# Development Overview

The app attribution service is a device-side attribution capability provided by Huawei. It operates independently of user identifiers.

After a user installs an app or generates in-app conversions, this service analyzes the user's behavioral data generated before app installation to identify the user's source and the reasons for conversions. It then posts back the attribution result to the distribution platform, developer, and attribution monitoring platform. Developers can use the attribution result to analyze the effectiveness of ad delivery, assess the quality of channels, and optimize ad strategies. Similarly, distribution platforms can use this information to evaluate the commercial value of channels and enhance marketing performance.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/q-tSJzUxT9ebq-zyJEWdlw/en-us_image_0000002337894552.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AF189E605AD6417817D78974B87455E8AA79A180A3784F93B9FDAF52784F00A "Click to enlarge")

The following table describes tasks in the service process.

| 
No.

 | 

Task

 | 

Description

 |
| :-- | :-- | :-- |
| 

1

 | 

[Register an attribution role](../preparations/managing-attribution-roles/document.md#section11218192952612)

 | 

An app ecosystem partner registers an attribution role and configures necessary information on the cloud platform of the app attribution service, including the name, postback URL (URL for receiving the attribution result), and public key. The app attribution service platform generates an attribution role ID after the registration succeeds. App ecosystem partners comprise developers, distribution platforms, and attribution monitoring platforms.

 |
| 

2

 | 

[Register an attribution source](../registering-attribution-sources-and-conversion-events/document.md#section1753254172910)

 | 

A media app or distribution platform calls [registerSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager#section359424018307) to register an attribution source (impression or click).

 |
| 

3

 | 

[Register a conversion event](../registering-attribution-sources-and-conversion-events/document.md#section191112563619)

 | 

A developer's app or an attribution monitoring platform calls [registerTrigger](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager#section13414543616) to register a conversion event.

 |
| 

4

 | 

[Post back the attribution result](../posting-back-the-attribution-result/document.md)

 | 

The app attribution service posts the attribution result back to the app ecosystem partner through the postback URL.

 |
| 

5

 | 

[Perform debugging](../performing-debugging/document.md)

 | 

The app attribution service provides the debugging function. Call the debugging API to ensure a smooth interworking process and verify the basic capabilities including attribution postback.

 |

#### Restrictions

-   Relevant apps must have been released on AppGallery.
-   All developers who access the app attribution service must strictly adhere to laws, regulations, terms of signed agreements, and requirements outlined in developer documentation when handling users' personal information.
-   It is prohibited to report or transparently transmit personal information through the app attribution service.
-   The debugging API of the app attribution service currently supports the Emulator running on Arm and x86 architectures.
