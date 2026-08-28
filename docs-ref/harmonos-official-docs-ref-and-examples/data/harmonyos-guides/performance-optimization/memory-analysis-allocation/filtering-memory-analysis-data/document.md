# Filtering Memory Analysis Data

Multiple data filtering methods are provided during allocation task analysis, helping you narrow down the analysis scope and accurately locate performance problems.

Since DevEco Studio 6.0.2 Beta1, Allocation analysis tasks support filtering of the memory status information.

#### Filtering by Memory Status

During allocation task analysis, you can filter the memory status information of the Native Allocation or Graphic Memory lane.

In the drop-down list box in the lower-left corner of the details panel of the Native Allocation or Graphic Memory lane, you can select the memory status to be filtered.

-   **All Allocations**: The details panel displays all the memory allocation information in the selected period.
-   **Created & Existing**: The details panel displays the memory that is allocated but not released in the selected period.
-   **Created & Released**: The details panel displays the memory that has been released in the selected period.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/MG0LayJRSJiTp5aXhcXvsg/en-us_image_0000002501070372.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28F7EF77859A0EE2CA194FFCCF4ACFCF1257580C40B5CE20CEC2E7FD6ED3E915 "Click to enlarge")

#### Filtering by Statistics Mode

On the **Statistics** tab page of the Native Allocation or Graphic Memory lane, you can click **Native Size** to select a statistics mode.

-   **Native Size**: The details are displayed based on the object memory.
-   **Native Library**: The details are displayed based on the .so library of the object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/LdUaI6KgSb6xVvvYO-hIqQ/en-us_image_0000002500910530.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1971450FB0241ED97BCA397973A6C9F8F695D1AF4D7F2D28FF0AAF3394F3BE33 "Click to enlarge")

#### Filtering by .so Library

In non-sampling mode, on the **Allocations List** tab page of the Native Allocation or Graphic Memory lane, you can click **Click to choose** and select a .so library to filter data related to the target library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/km9qtXHZR4yIxbO4mS43yg/en-us_image_0000002532750393.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF32AE68F9824EBA06A5B96098E76697D16E66C4BA2939B4390535692EC1DA3B "Click to enlarge")

#### Filtering by Search

On any tab page of the Native Allocation or Graphic Memory lane, enter the item to search to locate the related content. You can click **<** or **\>** in the search box to view the details of the search result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vF1y7AVjRii2TL5gBoxwPA/en-us_image_0000002532670441.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCED810BBE911B290950D7F2445D0DBF9BF99A3725302ED8C1EDA5A2679DE2E8 "Click to enlarge")

#### Filtering by Stack

On the **Call Trees** tab page of the Native Allocation or Graphic Memory lane, you can click **Call Trees** and **Constraints** at the bottom to filter stacks used for memory allocation.

The **Call Trees** selection box provides the following filter criteria:

-   **Separate by Allocated Size**: separates the stacks based on the allocated memory size when the stacks are the same.
-   **Hide System Libraries**: hides system stacks in memory allocation stacks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/JsH8eFbtRkSbVgjXc1lsNQ/en-us_image_0000002500910534.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9361A9C23F0BF7F9536F9740B1BBFE81F07D6B2A8CB7B3EF3EE4381FB5F27F0D "Click to enlarge")

The **Constraints** selection box provides the following filter criteria:

-   **Count**: filters the stack information based on the number of memory allocation times.
-   **Bytes**: filters the stack information based on the specified memory size requested.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/MCMEEglxQLS5kSPhD1C2BA/en-us_image_0000002532670439.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01612B6CAC6606F1BC5DC8D08717F80DB8B5C1BA28BF5CBB19AB7D83500313F4 "Click to enlarge")

In the **More** area on the **Call Trees** tab page, you can click the hidden button next to **Heaviest Stack** to determine whether to display the system stack in the maximum stack in the **More** area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/4f0yBnO0SfK8viRjZTAr0A/en-us_image_0000002500910536.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89B50A503F13C08294AB7BA2B303036F9D1D5B4D0D506C1597DC2485119DC301 "Click to enlarge")

On the **Call Trees** tab, you can click **Flame Chart** at the bottom to switch to the flame chart view.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/UI57ZfyYTk6miCaJyBY1dg/en-us_image_0000002500910532.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB194E2FA3CC1BC33D5F92C3A404E0E390CCF432F9FFBEEC6634873E11C1420A "Click to enlarge")
