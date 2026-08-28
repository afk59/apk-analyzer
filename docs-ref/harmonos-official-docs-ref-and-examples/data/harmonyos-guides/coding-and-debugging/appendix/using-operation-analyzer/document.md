# Using Operation Analyzer

DevEco Studio can locate crashes and analyze exceptions such as crashes, frame freezing, frame loss, and power consumption.

#### Constraints

Currently, this feature is available only in the Chinese mainland.

#### Page Layout

Choose **View** > **Tool Windows** > **Operation Analyzer** to access Operation Analyzer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ofPj5QNyTO2DnraQLzVcZw/en-us_image_0000002532670615.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44ED558FF24F28EBDE18350EFB7E68DAF92D95C7561772636BE57F7EA26428EE)

Click **Add account**, log in with your HUAWEI ID, and grant the required permissions to view the anomaly status of apps under your account.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/6Wx7uTnDQr6wR6C2wGxJOw/en-us_image_0000002501070548.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B21484EDA4547FA2A47AA24E48B4EAF170107114A8A7FF87150E70E77986A0BA)

The Operation Analyzer UI is divided into two sections. The left side is the menu bar, and the right side is the data display area.

1.  Menu bar:
    1.  Area 1: drop-down list from which you can select an app under the current account.
    2.  Area 2: Reports area that displays data details for locating specific issues.
    3.  Area 3: Metrics area that shows the trend of abnormal data changes for Crash, Frame Loss, Launch, and Battery Usage.
2.  At the top of the data display area, the following filters are available:
    1.  Time: from the current day to the last three months by time.
    2.  App version: version of the app that has abnormal data.
    3.  System version: version of the system that has abnormal data.
    4.  Device type (modal): device types supported by the current app.
    5.  Phone modal (version): model of the phone that has abnormal data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/w-NEyf6rTCinExIRmzoBww/en-us_image_0000002501070546.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7266EE07919E303D36C202F647238ED77DCC4458770CCCB993EFE30802BBAEB1)

#### Reports

Displays crash details. The **Stack** tab allows deobfuscating code and navigating to specific code lines to identify issues. The **System load** tab shows CPU and memory information at the time of the crash. The **FaultLog** tab displays crash logs. After symbol tables are uploaded, deobfuscation of the log's stack trace is supported.

-   Area 1: displays the crash issue list.
-   Area 2: allows you to switch between detailed information for the stack trace, system load, and fault logs via different tabs.
-   Area 3: allows you to locate specific exception points via pagination if the currently selected issue has multiple distinct exception points.
-   Area 4: provides a symbol table configuration button. Click the button to de-obfuscate the selected stack trace into the original code. Select a code line with a path, then click the **Open in project** button on the far right to jump to the issue location within the app.
-   Area 5: displays the current device information.
-   Area 6: allows you to switch between different device models and time periods to view the distribution of crash occurrences.
-   Area 7: displays CPU and memory information from the crash log. This feature is supported since DevEco Studio 5.1.0 Release.
-   Area 8: displays all information from the fault log and allows you to de-obfuscate the stack trace after [the symbol table is uploaded](../../../app-release/release/document.md#section97874500234). This feature is supported since DevEco Studio 5.1.0 Release.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/gJBn8iKAR8e1OGxDv9M-sQ/en-us_image_0000002532750567.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B116D9B2AFD2F86381A8B8AAC6678E699CCC01EB83CC35A256EA3A9D5081EC7)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/o8obsxRFQGOQuh9pgpbnXw/en-us_image_0000002500910704.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFB301210698A256FE2DEB0256C90B4157F2BED4C19E9C033B2EF2DED843FE2F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/uMKZpewdT9ev9LxgaEM2xg/en-us_image_0000002500910706.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26C090C3F26263261DE702E543914C53F5633544939722BF202664A679962331)

#### Metrics

## Crash

Displays the number of app crashes and crash rate.

Area 1: You can switch between the following tabs to analyze the number of crashes and crash rates from different dimensions: **All**, **JsError** (JavaScript crash), **CppCrash** (C++ crash), **OOM** (crashes caused by memory), **ProcessKill** (system forced termination).

Area 2: A bar chart is used to show the proportion of different dimensions in all crash exceptions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/OjrO3Q2kRxOK9AC6D74Gcg/en-us_image_0000002501070544.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2762024CF6F86D6E67D9BBC6387D16C34006F327A8A45F2D16E967206467A089)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/pHb-7ROXQ-20NS2ijfGZEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=638908DDD7A71142836312A9B9E81F2EAD617AC98F87BFA80E9C70FBD05B637B)

ProcessKill analysis data is presented through an interactive combination of bar and pie charts. Click the bar chart, and the pie chart will display the distribution of ProcessKill types for a specific time period.

## Frame Loss

Presents statistics on continuous frame loss from multiple dimensions to quickly locate faults.

Area 1: The frame loss overview is used to collect statistics on the continuous frame loss rate in the maximum dimension.

-   < 6: frame with minor stuttering (fewer than 6 consecutive frame drops)
-   6-15: frame with moderate stuttering (6 to 15 consecutive frame drops)
-   \> 15: frame with severe stuttering (more than 15 consecutive frame drops)

Area 2: displays the top N pages or scenes with the highest frame loss rate by page or scene. You can click an area in the pie chart to view the continuous frame loss rate of a specific page or scene.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/0UiKPWbtSXKYvCqHVacM1w/en-us_image_0000002532750573.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5002B696A6CD10E808BB740B649548AF45349840D074AD8E9B2B4837178324F0)

## Launch

Presents statistics on device startup in different dimensions, helping analyze the distribution of exceptions.

Area 1: features tabs for **All** (overall launch duration), **Cold Launch**, and **Hot Launch**, allowing you to switch between them and view their respective launch durations.

Area 2: displays the trend of overall duration in a line chart. The following figure is an example.

-   **AVG** indicates the average duration of all launch stages at the current time point.
-   **P50** indicates that 50% of launch stages at the current time point complete within 579 ms.
-   **P75** indicates that 75% of launch stages at the current time point complete within 582 ms.
-   **P90** indicates that 90% of launch stages at the current time point complete within 585 ms.
-   **P99** indicates that 99% of launch stages at the current time point complete within 585 ms.

A bar chart alongside shows the reported quantity of anomalous duration instances.

Area 3: displays the duration of each launch stage. Clicking a stage name reveals its detailed duration metrics across different time periods.

Area 4: shows the duration trend of the currently selected launch stage over time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/OkJ2IvqfS5mFwlIW-3axLg/en-us_image_0000002501070550.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC3B90E009BE5843C0CF418D41A2FEB70D88893F0DF2E0E4F3089709F9A60BFD)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/FqWiMbVlTqeeyLcq8lK_sg/en-us_image_0000002532670619.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C67D3FE96E789BC20C5E02FC72612BF6D4BF5F5CE5316874FC9A71249695112E)

## Battery Usage

Presents statistics on the total battery usage of devices, as well as the battery usage and usage duration in the foreground and background.

Area 1: energy consumption overview. A line chart is used to display total battery usage, foreground battery usage, and background battery usage.

Area 2: shows the distribution of foreground battery usage and usage duration across the top 5 device components.

Area 3: shows the distribution of background battery usage and usage duration across the top 5 device components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/mmvVujV6Qg-ZaDC8NYGDdg/en-us_image_0000002532670617.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE7E3FA99861B563844FAB176532B413AB92EED25B4DC959258AA4A325894BDB)
