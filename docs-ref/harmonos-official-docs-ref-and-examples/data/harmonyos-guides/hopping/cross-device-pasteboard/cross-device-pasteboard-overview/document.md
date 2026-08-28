# Cross-Device Pasteboard Overview

Pasteboards are classified into local pasteboards and cross-device pasteboards. Local pasteboards allow users to copy and paste content within a device, and cross-device pasteboards allow users to copy and paste content across devices.

In multi-device scenarios, cross-device pasteboard enables the user to copy a piece of text in the application of device A and paste it to the application of device B, achieving efficient content sharing among multiple devices.

During development of a browser application or a rich-text editing application such as memo, notes, and email, cross-device pasteboard is accessible, improving user experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/kVCYgmQzT42mS4kbz1M6QQ/en-us_image_0000002220910166.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91F12DB8CAD32A3A04E0567375F8BCD9AE9CF89E438071F81F3106A834B94DCD "Click to enlarge")

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/MJNV5oZ9RfO_p0RsSI6dsQ/en-us_image_0000002255989853.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7206625834E70FC1116C2A0F04831CDDD4C11A939CC277B83EBAAC6831D81A9 "Click to enlarge")

1\. A user copies data on device A.

2\. The system pasteboard service processes the related data and synchronizes the data, during which the developer is unaware of such actions.

3\. The user pastes data from device A on device B.
