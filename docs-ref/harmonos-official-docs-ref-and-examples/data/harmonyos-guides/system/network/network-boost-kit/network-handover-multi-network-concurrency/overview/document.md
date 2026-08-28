# Overview

Multi-network concurrency refers to the system capability to establish multiple network paths through provided APIs. When an app initiates a multi-network concurrency request, the device determines the concurrency strategy based on the service scenario, applies corresponding concurrency controls, and evaluates the performance benefits accordingly. The principles for using multi-network concurrency are: app-initiated requests (with restricted permissions), system-level governance, and minimal usage.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/yAuBC3GHSXCuefFlwacYLw/en-us_image_0000002496694669.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062017Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A0F3FC0528C8E24CDE9EDE8B1A9ED3F99D5F3C430FFB0BBB97B8C2A5637218F)

The functions involved in the process are as follows:

Concurrency listening: An app listens for any changes of the multi-network concurrency status. Meanwhile, the network subsystem of the device provides suggestions such as initiating or releasing multi-network concurrency.

Quota query: The app obtains the quota information of multi-network concurrency (including the used and remaining session count and duration) to proactively manage and optimize usage of multi-network concurrency.

Concurrency initiation: Before initiating multi-network concurrency, the app can proactively call the service scenario setting API to notify the device of entering a specific service scenario, and trigger multi-network concurrency through an explicit initiation API.

NIC binding: In the API for listening on the multi-network concurrency status, a newly acquired NIC is bound either by socket or by app.

Concurrency termination: When the app's network performance becomes normal, it must proactively release multi-network concurrency and call the service scenario setting API to notify the device of exiting the specific service scenario. The device may also proactively release multi-network concurrency to prevent misuse.

Benefit measurement: The consistency between app-reported transmission experience and device-calculated results is evaluated based on app feedback and system QoE algorithms.

Note: Multi-network concurrency is governed by factors such as the network acceleration switch setting, permission scope, quotas, and power consumption. Non-compliant behavior may trigger penalties, including but not limited to concurrency termination, quota reduction, and revocation of restricted permissions.
