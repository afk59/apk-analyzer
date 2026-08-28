# Data Area

DevEco Profiler visualizes performance data in the data area. The visualization capabilities vary with the template you use. This topic describes the common capabilities available for all the templates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jbzaaAzNSl6pjAygXKqw8g/en-us_image_0000002532670547.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E2DC8997605F5665656E5765B91BFE2A3C4E65F02646EAAD348E4505C3424DF "Click to enlarge")

The data area can be divided into five parts.

① Toolbar: manages auxiliary features such as marking, favoriting, and importing symbols offline, and controls the session status and timeline.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/qmVjCBVMS4eF-NGH8b0XhA/en-us_image_0000002532670525.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E5B54B6783810C6FC57E01AA793300F573F217AF3E76741540D583375B54C4B): Click this button to view all markers that have been placed. You can view or redirect to the marker description and time, and change the marker color.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/q_0s9HR0SjOkTmvw1nPAJw/en-us_image_0000002501070478.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83400E5AE9E2E50554DE71D68FB185D1A8DB7DE9AA0C647A8EC66930B7137C91): Click this button to show or hide a lane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/lp5SkfGDSoubt948sJXsjg/en-us_image_0000002500910644.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AAD414DEC673C8587EED903A7E311FA66DCD2D6BEA1BD82F985FB93DDF68821): Click this button to import a .so file that contains debug symbols, allowing you to restore native function stack symbols. This feature is only supported for Callstack and Native Allocation lanes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/fwjUFCdfSNuY4tzL1JVqiQ/en-us_image_0000002532670563.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E916DF609797F1038AB63FBDF4DBC3F72D1F85D0FE3783BD092990406D0C9008): Click this button to filter lanes. Filtering out the lanes that do not have data captured can reduce the overhead of data collection. However, it also reduces the number of data analysis dimensions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/hLGTPj-TSDGqmPrUn0nYFA/en-us_image_0000002532750481.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FDAAFB2A6104A8936D1FFC3F3A9CF53268F56F0FD285AA3A8FBF9CF09DF2B02): Click this button to view and manage the plug-in startup settings for different lanes. You can save these settings to a configuration file, and they will automatically be applied when you use this template type in the future.

② Timeline: provides a horizontal timeline to display the timestamps of data.

③ Marker bar: places markers to mark critical time points or periods.

④ Lane panel: displays lanes. A series of lanes is preset for each scenario-specific template. For example, **Frame** shown in the figure is a lane. A lane is the minimum unit of data to be analyzed in a specific dimension in DevEco Profiler. A lane presents performance data of a dimension. You can view the data changes over time, find the period during which data is abnormal, and rectangle select the period to view the data details on the details panel.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Lx9_5CzvSxqWNUKa9qhLKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15E72E57DF440AAE72FE34765340D4ACC06076BA5A6C4F120DDB75AACA8CFB2F)

-   The lanes of each scenario-specific template comply with the top-down analysis approach. A lane close to the top indicates an abstract performance dimension, whereas a lane at the bottom indicates the performance dimension of the underlying layer of the system. Therefore, you are advised to analyze the data displayed by the lanes from top down.
-   The panel in a lane displays performance changes over time, helping you locate the abnormal time period. Then you can view the detailed data of each dimension in this period on the details panel and analyze the parameters or attributes that affect the performance.

⑤ Details panel: displays data details. After you select data in a lane, detailed data in the selected period is displayed in different graphs. The **More** panel provides supplementary description for the selected data on the details panel on the left.

#### Basic Operations

## Session Control

In the data area, you can start or stop a session by clicking the first button on the toolbar. The following figure shows the state transition of the first button with the data collecting status. If the first button is dimmed, data collecting is complete. The buttons provide the same effect as data collecting in the session area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/kQ3kOlcoTDOg2j-hzJqi3w/en-us_image_0000002500910618.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B8275834DB13E0D1BD9945C1E91200B5198334C1C9F8A9663C69B292F9D1200)

## Timeline Control

DevEco Profiler provides various timeline operations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/F9DYtb48TxezgJ1SgspF2w/en-us_image_0000002532670541.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90DDFF184FC3AFAB4B7FD5E1EF858E0B6F86CD127F7C6EDDD4FC2C1F60153128 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/mll5Ww2gS_m4HxKiiuyawQ/en-us_image_0000002500910638.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2508C326181E7CB83A8DFA8AFBF5395949E7E23BAAF933D3450D1EF5B58B8003): displays all the data. After you click this button, the timeline is automatically adjusted and data within the session duration is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/WWDx0NbIRP2i7l6cjPLsfg/en-us_image_0000002532670553.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D39D2B16B8C003A13FCA7E851A716725C78C88B08591183B783CDD12D33C78DF) (shortcut key: **W** or **Ctrl**+mouse wheel): zooms in to the timeline. After you click this button, the total duration displayed on the timeline decreases and more data details are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/SgWiojNQQS6hk31kAjn1AQ/en-us_image_0000002500910612.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F5AFFE0BF6297E542E7362D984B22D229591BADCC8E53AB59580290911671B7) (shortcut key: **S** or **Ctrl**+mouse wheel): zooms out of the timeline. After you click this button, the total duration displayed on the timeline increases, so you can better view the overall data trend.

You can drag the slider under the lane panel (shortcut key: **A**, **D**, or **Shift**+mouse wheel) to adjust the time range shown in the timeline. You can drag the slider on the right of the lane (or slide the mouse wheel) to scroll up and down the lanes. For details about how to use the shortcut keys, see [Shortcut Keys](../../appendixes/shortcut-keys/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/-oKPWZqrRZew-vjXkFP_rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5A4A2EC84205FC43AE996E185ED4AC5F87E84455151E7B305F6EE0879F92FC8)

Shortcut keys such as **W**, **A**, **S**, and **D** take effect only in activated lanes. A lane is activated if a bright blue border exists on the lane panel.

## Viewing the Details Panel

If you find suspicious data on the lane panel, you can use rectangle selection or click selection to select the data to be displayed on the details panel. You can click data in a lane to trigger click selection, or click, hold, and drag the mouse on the lane panel to trigger rectangle selection. You can hold down **Alt** during rectangle selection. In this case, the lane in the selected time period fills the entire lane panel when you finish selection.

Different lanes display data in different dimensions. Therefore, the data displayed on the details panel corresponds to the lane selected on the lane panel. The selected lane is displayed in blue. If you select a lane without performing rectangle selection or click selection, the details panel displays the complete and detailed data of the lane, as if you used rectangle selection to select the entire lane.

## Adding or Editing Markers

DevEco Profiler provides markers to help you mark key time points or periods.

It provides two types of markers:

-   Single-point marker: Click a time point, and mark it (shortcut key: **M**). The icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/JWPMPINhSB-lPZ-kocTmrQ/en-us_image_0000002532750517.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD08799774809BE501AFDDEC460D17F48094D2D1E6E9AFFCB2AF5B87D66C3DA0) (the color is customizable) is displayed.
-   Time period marker: Rectangle select a time period and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/XsC8-afSTlyRU5e-e5wNqw/en-us_image_0000002532670535.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=145A932B217B200E888ED11CB0BD005873BB59D71AF37F9EEFB3E27EC6911976) in the upper right corner to add the start mark (shortcut key: **Shift+M**).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/p6gPnZyjQ2ePwLmApn3-yw/en-us_image_0000002501070472.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81D28CF82293D1497BD68B0E7529357BEA0D4C60911185BA3B91485FA04178DE)
    

You can click any position in the marker area under the timeline to place a marker. Alternatively, after rectangle selecting a time period, click the flag icon to mark the time period, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/h3mHSFImTPCtyatjh1wWUw/en-us_image_0000002501070470.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3185B7745CB7AEE77038386114C82384EAA2EFC87903C16BD7DA105E55211513 "Click to enlarge")

You can press **Ctrl+,** to select a single-point marker forward; press **Ctrl+.** to select a single-point marker backward; press **Ctrl+\[** to select a time period marker forward; press **Ctrl+\]** to select a time period marker backward.

After a marker is placed, you can double-click the marker and modify its description and color in the displayed dialog box, or delete the marker.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/wWu7aqCoR4-OJyOB59YfrA/en-us_image_0000002532750519.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=012B7B0689EA588AE22FF3A88A93BEA5421B3DE7FD6C12BDFF1832CEDE75A67D "Click to enlarge")

In addition, DevEco Profiler shows the time difference between markers. By selecting a marker and moving the mouse pointer to another marker, you can view the time difference between them in the lower right corner ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/C3lG-ulpTj63sbcP6OpWEw/en-us_image_0000002501070476.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAFCE28BD53B066EE53A0DFB8EF88ED98A31CEE7C44DF1286B37CF8A0F32FEF6) of the panel. This feature is especially useful for analyzing time-sensitive performance problems.

## Favoriting Lanes

If there are too many lanes, your concerned lanes may be far away from each other, leading to low analysis efficiency. To address this issue, DevEco Profiler enables you to favorite lanes. Specifically, hover the mouse pointer over a lane, and click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/EdBBXOLvQkikareXXyv9Ww/en-us_image_0000002532670543.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=330704D09A840E46B522E3F0B58A38D7CFC91EF0AE25BCBB4768ABD6FD4B5316) icon displayed to add the lane to favorites.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/0tkLqQPkRcqHaj39JGZFqw/en-us_image_0000002532670549.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB814881E7757B6F697532484D82FE622359E5CFF0E72677C40CFA7C8C0EC767)

You can click the icon again to remove the lane from favorites. DevEco Profiler also supports lane collapse. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/GffXV0TIS2K7quswBdOrEg/en-us_image_0000002532670531.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA309151C48D4DB0B1B75CFE603297DC56B6CFFD100E54B541C5B3242DB5689F) to fold the favorite lanes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/qZjxXgegR6S0ItEDqiKYXg/en-us_image_0000002501070468.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39EFD26A4FF4F0736C301CCB1AEB1CF82BC12BC5B9516ACBF39C8E729BFDA036 "Click to enlarge")

For a favorited parent lane whose title is not fully displayed, hovering over the title area of the parent lane will show its title information.

For a favorited sub-lane whose title is not fully displayed, hovering over the title area of the sub-lane will show the title information of its parent lane and itself.

For a favorited sub-lane whose title is fully displayed, hovering over the title area of the sub-lane will show its title information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/cB40yq6rSlGXlZ8gHDHkVg/en-us_image_0000002532750515.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=132AD5BBC31350EB1DE690C069CD9AE74C29727A63D6EF4DA9EF0A5D8FD6FEBA "Click to enlarge")

## Expanding or Collapsing Sub-lanes

Use either of the following methods to expand or collapse sub-lanes:

1\. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/pPenvUNsTVycC3XcigD_yA/en-us_image_0000002500910640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D6B3981E24EAC3B976C3CD84136ADA6FA0C745CF4BA03076C6A2CF8FBD07838) on the left of the parent lane.

2\. Double-click the header area of the parent lane.

## Global Search

To help you quickly search for concerned performance data, DevEco Profiler provides global search.

1.  Specify the search type in the search box. Select **Search Units** if you are looking to find specific lanes or **Search Unit Data** to search lane data. By default, the system searches lane data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ydoOrPbvQ_GM28i59E7JPg/en-us_image_0000002501070462.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31E78E47B771E26017EAF91D29BE736BC6FB88DBB9C903286B2B56685166F9D4 "Click to enlarge")
    
2.  Search for lane data. You can specify whether to search across the entire time range or within a selected time range both before you enter the search keywords and after the search results are displayed. In addition, you can select a particular lane to search within.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/4-dkiGBVTPeDwk_BFfKgSw/en-us_image_0000002501070480.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9769D72466100FD8CDEC5842AA5A8C153A2C4224911F785AB5AAD8077BAD167 "Click to enlarge")
    
3.  To make your search more inclusive, you can click the **Cc** button to toggle case sensitivity for your keywords. By default, searches are not case-sensitive. Once you click **Cc**, the search is reinitiated automatically, and the count of search results is shown on the right side of the search bar. Keywords that yield matches are logged in the search history. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/p57DLzEuQJ2fnGTte9F1sw/en-us_image_0000002532670555.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1196A6011AB0E9830B22B4F94F4BAF027F2EC600918CC9431DA5364D37D145DC) or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/TQZ5AF1zRR2MDYjquG222Q/en-us_image_0000002500910652.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A320546DDC251479D46B4859EA65AA06261CA66EE92EA325AC890844032A27B) to navigate through the results. As you click through the results, the lane panel automatically jumps to the corresponding location, highlighting the selected result, and the details panel automatically refreshes to display the detailed data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/uICMWyVsQuimoZZaW2iHXw/en-us_image_0000002532670539.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75B94D5244286A1C5500AE2555FA9499F229AFDC8C41556096A2CEBCA5B4F852 "Click to enlarge")
    

## Offline Symbol Parsing

To help you analyze native function hotspots, DevEco Profiler provides symbol import. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/IIx3RveAS02a0-rv-sTnnA/en-us_image_0000002501070474.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90CA25269A136F209A9236458ADB224191124BB98A542A9933454404A9E79E6A) on the toolbar and select the .so library with debugging information to import. The tool uses the information to convert the collected function offset information into source code symbols (including system .so libraries, user-compiled .so libraries, and third-party libraries).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/N2PSeKOUQu2RjEPYDTbjvQ/en-us_image_0000002532750487.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A0C88BACC50A53E5F12862E8F7A93C1A307A32635FDCC6E80F159796433D2B8 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/oS6nKwchSkm8tq3vT1k7Wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=077CBCFCA0D370D23EA7A5A31F20FAD7D61FAD10422759AF09764D2626F52478)

-   When importing the .so library that carries symbols, ensure that the optimization level (such as -O1, -O2, -O3) is the same as that of the .so library of the release version. You can view or configure the optimization level in the **CMakeLists.txt** file.
-   When importing the .so library that carries symbols, ensure that the compilation options are the same as those of the .so library of the release version. This helps prevent inconsistent start addresses of the .so library from affecting parsing correctness.

## Code Navigation

Finding the source code of the problem is the most important part in profiling. For the function stack frame information displayed on the details panel (as shown in the figure below), you can double-click a stack frame node. The tool opens the related source code file in the editor and locates the code line. The prerequisite for using this feature is that the app being debugged is compiled in the current project of DevEco Studio and the source file is not moved.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/drlYkZMGQhqce_OnPYD7Iw/en-us_image_0000002501070482.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF7A4B71F57C870D086763C43B7309313C6F0F8F7D1DE18D2CBBC259256938BD)
