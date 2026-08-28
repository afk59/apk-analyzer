# Overview

#### Use Case

The sharing panel is displayed in modal mode on a phone, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/i7hAAQozQbGmdEev-XieQQ/en-us_image_0000002513409487.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E30FB04A02209D1D6D8C64B39B032713D9129439971FE617ED92AB076CD6D6AF "Click to enlarge")

The sharing panel is displayed in a pop-up window on a 2-in-1 device, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/xH7gRw3JTRO96w52RzG6wQ/en-us_image_0000002513289523.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8636D951B040F50080C156300171175757DFD91EA6C467DA02B2FAC84A5AD35E "Click to enlarge")

1.  The host app can share a piece of text, a file, or a memo to other apps.
2.  The host app can also share multiple items, such as texts and images, to other apps.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/L4Ec9_w5T5iWq8e4n9g-ZQ/en-us_image_0000002513289517.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2EC20C742732D6A1536BCAC5C11890FCA7977DD1C6139BB6DB61E18B64EF468 "Click to enlarge")

The process is as follows:

1\. The host app constructs the data to be shared and **ShareController**, and registers the sharing panel status listener. The listener registration is optional.

2\. The host app starts the sharing panel.

3\. The user selects a target device or app.

4\. The target app processes the shared data and closes the sharing panel.

#### Design Specifications

When integrating your host app with Share Kit, you need to choose proper display modes for different types of shared content. For details, please refer to [System Sharing Design Guide](https://developer.huawei.com/consumer/en/doc/design-guides/share-0000001957076313).
