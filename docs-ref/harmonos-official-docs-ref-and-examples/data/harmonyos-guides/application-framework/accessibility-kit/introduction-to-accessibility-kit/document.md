# Introduction to Accessibility Kit

#### Overview

Accessibility is the ability to ensure that anyone can access and use information in an equal and convenient manner under any circumstances. It aims to narrow the digital divide in information understanding, interaction, and utilization among different social strata, regions, age groups, and people with different health conditions, so that they can integrate into social life more conveniently and fully enjoy the convenience brought by digital development.

Therefore, whether developing a new application or updating an existing one, accessibility needs should be considered to make the application usable by more people. Accessibility Kit opens up necessary capabilities to help applications better adapt to accessibility needs, such as adding accessibility focus for components and reading text aloud.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/czeF-FAiThC4ELcxFq4Gxg/en-us_image_0000002495356460.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061919Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCE8901686E05931FCCAFF72EE0462772064B60A4A7ADECBFE4EE20702C447EC "Click to enlarge")

-   **System services**: The system provides various accessibility capabilities for different groups of people with disabilities and different scenarios with obstacles, such as screen reading, large font, high-contrast text, color correction, color inversion, mono audio, volume balance, and screen touch.
-   **Open capabilities**: Based on system services, the system provides open accessibility capabilities for applications, such as querying whether Screen Reader is enabled, setting text to be read, and proactively reading text.
-   **Applications**: Applications are designed to ensure accessibility in information acquisition and usage in terms of layout, color matching, font, interaction, broadcast, and feedback. The open capabilities provided by Accessibility Kit can be used to better adapt to accessibility.

#### Capability Scope

-   **Accessibility status query**: provides APIs for querying the accessibility status and touch exploration status of applications, so that applications can better serve people with impairments and scenarios with obstacles based on the accessibility status.
-   **Accessibility event sending**: provides APIs for sending accessibility events such as proactive focus and proactive reading, so that applications can provide better accessibility experience based on service scenarios.

#### Relationship with Other Kits

ArkUI Kit provides Accessibility with the capabilities of defining accessibility component attributes, such as accessibility text and description, and sending accessibility events.
