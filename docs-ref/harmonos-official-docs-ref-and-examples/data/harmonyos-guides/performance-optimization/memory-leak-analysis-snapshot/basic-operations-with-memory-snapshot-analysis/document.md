# Basic Operations with Memory Snapshot Analysis

#### Viewing Snapshot Details

1.  Create a snapshot analysis task. For details, see [In-depth Capture for Problem Locating](../../using-deveco-profiler/in-depth-capture-for-problem-locating/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/m2On33I6ThWzew9P3fmWkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8232FE29E42C3502C7F1E085EF50C6F6CEF5D01D0799ACFE17335153705099E3)
    
    -   In the task analysis window, you can hold **Ctrl** and scroll the mouse wheel to zoom in to or out of the timeline, and hold **Shift** and scroll the mouse wheel to move the timeline leftwards or rightwards. Alternatively, you can press **W** or **S** to zoom in to or zoom out of the timeline, and press **A** or **D** to move the timeline leftwards or rightwards.
    -   You can hover the pointer over any position in the lane and press **M** to add a single-point marker.
    -   You can rectangle select a time period and press **Shift+M** to add a time period marker.
    -   In the task analysis window, you can press **Ctrl+,** to select a single-point marker forward, and press **Ctrl+.** to select a single-point marker backward.
    -   In the task analysis window, you can press **Ctrl+\[** to select a time period marker forward, and press **Ctrl+\]** to select a time period marker backward.
    
2.  Set an ArkTS Snapshot lane.
    
    Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/qQybodOBQZ2rl7IKdWdP9A/en-us_image_0000002501070272.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAB008C1EAE12A7581AC5C06B6205F6E302151506433F3CE94C694721867AD53 "Click to enlarge") in the upper left corner of the task to filter lanes. Click this button again to close the setting and make the setting take effect.
    
3.  Click the **options** drop-down menu for the ArkTS Snapshot lane to set whether to capture data of the number type. By default, such data is not captured.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/gPHJt25PSQKwrUdHcvdedw/en-us_image_0000002501070264.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B0DE1C0698780F6A552B739AA0EB44A868BCFB1639A071AEA53E6D144409F7B)
    
4.  After the capture starts, you can view the memory usage of the Memory lane and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/j1XwzRP5Tri_lQmDycfb-g/en-us_image_0000002532670347.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C091AD32AA1F514AD1043EEFE6F9BA587FA6D95561C72EC9AA8E75307178A94 "Click to enlarge") in the upper left corner of the task to start a snapshot.
    
    The purple block in the ArkTS Snapshot lane indicates that the snapshot is complete.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ufmEDJ7OS8iNIYj_KkNVhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D6233F6CFFDB56FF356DD35FB16ACD67D1F405604EE2038E5D186861D2EC5E8)
    
    -   During capture, you can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/6GU9-bZtQze5PhH0EToFKQ/en-us_image_0000002501070270.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D985268551460BA4C95BB76C2D7C20858EBD491DAD104A92A47E5DA445F6E1A4 "Click to enlarge") in the upper left corner of the analysis task window to start memory reclamation.
    -   If a memory space occupied by a process of an ARK VM object is no longer accessed by the object in subsequent operations, the space is automatically returned to the system, reducing possible program errors and unnecessary memory loss.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/lpuQB6GTTD6eVKSIR-bvTA/en-us_image_0000002500910408.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A889DD6CB8EEFB5058DD3F5CBED8A828CC3D998FE375D64424F66FB4EE89BF00 "Click to enlarge")
    
    On the **Statistics** tab, detailed information of the current snapshot is displayed:
    
    -   **Constructor**: constructor.
    -   **Count**: number of objects.
    -   **Distance**: distance from the Garbage Collection (GC) root to this object.
    -   **Shallow Size**: actual size of the object itself.
    -   **Retained Size**: total amount of memory that can be freed when the current object is released.
    -   **Native Size**: size of the native memory that is referenced by this object.
    -   **Retained Native Size**: total amount of native memory that can be freed when the current object is released.
    -   Objects marked with ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ZmUsCx2GSPS6REejNCPSYQ/en-us_image_0000002500910410.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF6BE900200DEE04BCB83B4F81E15B6F0B204469066AF490A344C3519232874A "Click to enlarge") are global objects, which can be accessed through the global window object.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/veUFONq1R_aCqahuEzgwkw/en-us_image_0000002532750273.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7806DAE2EE356EC88DB17EE95447FA09986893EF57E66B17D233E552DD40F904 "Click to enlarge")
    

#### Parsing App Object Name

The Ark System currently includes three types of objects: Ark app objects, system internal framework objects, and other JS objects. Since DevEco Studio 6.0.0 Beta1, it supports parsing the names of app object classes, helping you quickly locate the source code where errors occur, thus improving problem localization efficiency.

1.  System internal framework objects: core objects used to describe the HarmonyOS underlying framework, providing basic system capabilities. To facilitate viewing, such objects are currently classified under the constructor node (framework) in **Statistics**. All such objects start with **\_GLOBAL**.
2.  Ark app objects: objects used to represent specific components, modules, or resources in HarmonyOS applications. These objects must be named in the following format:
    
    com.example.app/MainModule@1.0.0/src/main/ets/MainPage.ets#MainPage(line: 10)\[MainModule\] // The format is BundleName/SelfModule@Version/FilePath/File#Class(line: xx)\[RefModule\].
    
3.  Other JS objects: objects used to describe those related to the JavaScript engine in Ark Runtime, providing basic capabilities at the JavaScript language level. For example, JSArray and JSSharedObject.

In the Snapshot template, you can click the name of an Ark App Object on the **Attributes** tab to view its parsing result, helping you locate the problem. The parameters are described as follows:

-   **Module**: module information
-   **Class**: attribute name
-   **Path**: path of the compiled source code You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/O9sjSTy1TFu3CBeeZ4ROFw/en-us_image_0000002501070246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14ABFD3B1FAB37610F17328EE1D3FBAC0E2CE287CB4A99DD9DBF4094F608DD44) next to the attribute name to navigate to the corresponding code in the project, facilitating debugging.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/uJNyC3PCQASMr9Z9B8gkMQ/en-us_image_0000002500910400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=832C5F1E67F713E19BD19E60E3C48A4FCF8F3689F12E4DBA184E94FEA6B3B77B "Click to enlarge")

If the app is built in release mode with source code obfuscation enabled, the Ark app objects will display obfuscated data. You can view the source code information of the selected app object on the **Attributes** tab.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-bOTjc2oRLCCo5gpBcnjjg/en-us_image_0000002532750285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B47112058A816EB0375B936F345A3079816FF28494211F91036B3020162E787A "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/NdtK5jN3QaWois0wRnfL3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=587C893ACCA1D76D81CF455BBC43DB69BEFA4DAFA59A0E4C6E7E34EBEF727D45)

-   Ensure that the project code path matches the parsing information. Otherwise, the navigation may fail.
-   System internal framework objects (framework) provide only basic information and do not support navigation.
-   **line=0** after an object name indicates an invalid line number and cannot be used for navigation.

#### Node Attributes and Reference Chains

On the **Statistics** and **Comparison** tab pages, when you expand any instance object node, you will see <fields> and <references>. These two nodes represent the attributes (or fields) of the instance object and the reference chain of the instance object, respectively.

In the **More** area, the **Fields** and **References** tabs display the attributes of the object selected in the **Detail** area and the reference chain of the object, respectively. They provide a convenient way to view the information about the selected object without navigating away.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/9BCaLCCLQASYuWjkaj1dnw/en-us_image_0000002500910418.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C438B22C82C1E6ADB413F148605FB4A75E18A1E4F8530589E216E9E4C5B54EF "Click to enlarge")

#### Redirecting to a Node

When viewing memory objects, object attributes, and reference chains on the **Comparison** tab page, you can click the redirection icon at the end of the row of an object. The tool redirects you to the object on the **Statistics** tab page, where you can view the detailed object information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/6re501Y8Sn2_cb-9_MfwbA/en-us_image_0000002500910402.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF62BB7BB1D0A3745F76EAE5E2FF79D265944E0CF2B769EE33F172D3DE6E2B36 "Click to enlarge")

#### Switching Between Historical Nodes

After you perform node redirection between **Comparison** and **Statistics**, you can click the left or right arrow in the lower left corner of the **Details** panel to move forward or backward to the next or previous historical node. This feature is available only when the left or right arrow is not dimmed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/XC9XODx_QbuJ7tivZBT9SQ/en-us_image_0000002500910414.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F71670BBBEB6FAA7823818EE64879C4CF68C9BB199F96E64EE096C2746D3EF33 "Click to enlarge")

#### Comparing Snapshots

On the **Comparison** tab page, select the names of the snapshots to be compared from the **Base** and Target lists. The comparison results are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/TMD7NXcISFqFjnzk6eV0jQ/en-us_image_0000002501070260.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3315BE1BC6B52EF9911006BA687F08E1C8685BC7ECE2C30253820705FF448DB "Click to enlarge")

On the **Comparison** tab page, you can compare snapshots, including the number of added snapshots, number of deleted snapshots, number increment, allocated memory size, released memory size, and memory size increment. Through continuous comparison, you can analyze and locate memory problems.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/LrLQaAdjTy6H2Gek5PEs2A/en-us_image_0000002532670321.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19AB9728976E12F7A02A7AA2309F4687D72152764076DC4B5393FF7DFB3D5212 "Click to enlarge")

#### Expanding a Reference Chain Towards Minimum Reference Distance

Snapshot analysis supports one-click expansion of reference chains towards the minimum reference distance. The minimum reference distance refers to the shortest path from GC Roots to the selected instance object. Each step along this path decrements the **Distance** value by 1, ultimately reaching a node with Distance = 1. This provides clear visibility of which objects hold references to the target instance, enabling rapid root cause analysis.

For further analysis, select a problematic instance node. When the **Path to GC Root** button in the bottom search bar becomes available, click it to enable the system to calculate the shortest reference path from the GC Roots to the selected node in the right pane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/_iS6jmeyQ1O8rV-HSblvBA/en-us_image_0000002501070266.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C8B60491DACD9413D1A691A5D102497B5824B8CCDB3699485C129EDDA38173B "Click to enlarge")

Currently, the single-root path search (default), search with a specified number of root paths, and all-root path search are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Zl2CdnDLSemjnOBWyqAKwQ/en-us_image_0000002532750277.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6D18530941198B29796DFBA692C67955A38A80964EAF5EE4884A4EF7FF51589 "Click to enlarge")

Once you set the search mode and click **OK**, the **More** area on the right automatically switches to the **Shortest Paths** tab to display the search results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/HornuraPQq-WjizCHrUIiw/en-us_image_0000002532750283.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F78B2AF91C468C61EA1F55C7D0E06BC550F10DBF75A35EDBD078D180B56C7DB0 "Click to enlarge")

#### Visualizing Reference Chains

Since DevEco Studio 6.0.0 Beta1, the Snapshot template can display all reference chains in graph form. The system calculates the reference nodes around the target node and clearly presents the object's reference relationship in a relationship graph, making it easy to locate the root cause of issues.

Select an instance node or a reference node. When the **Visualization** button in the bottom search bar becomes available, click it and configure the search mode to enable the system to calculate the reference nodes around the selected node and display the reference relationship on the **Graph** tab.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/MRXlmv1JSkmSciiSvSEeAg/en-us_image_0000002500910424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CD2CD41F26758B3B1015491C75BA03311CB08D04BABD603B4711C41765CF803 "Click to enlarge")

A maximum of 30 reference nodes can be displayed. By default, 20 reference nodes are displayed. Currently, the following two reference chain expansion modes are supported:

-   **Retained Size**: displays reference nodes by retained size in descending order.
-   **Distance**: displays reference nodes by distance in ascending order.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/oNmjAoUYTqqFHgUDABoBDg/en-us_image_0000002500910404.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6597324763DBCE2B58C188BD88A41A9998D9ED4BA128DCCC04967620EBA67F22 "Click to enlarge")

Once you set the search mode and click **OK**, the bottom tab will automatically navigate to the **Graph** tab to display the search results. The central node is marked in red, and the line segments indicate the reference relationship between the two connected nodes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/sLPENzvCRymkCDLgWPoFKw/en-us_image_0000002532670345.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=668472520C7153E737287EB93D937E98E2C40742063BA5171058482138BE71D9 "Click to enlarge")

You can select a node to display its details on the **More** pane on the right, which includes the **Fields**, **References**, and **Shortest Paths** tabs. When you hover the pointer over a node or line segment in the graph, a tooltip will display the corresponding detailed information. The graph area supports dragging to pan and zooming via Ctrl + mouse wheel.

When you right-click a node, the displayed context menu includes the following options:

-   **Show More References**: displays more reference chains of the current node. After this search mode is configured, the reference chain graph centered on the node is regenerated.
-   **Show Path to GC Root**: displays the path from the current node to the GC root. After this search mode is selected, the reference chain graph centered on the node to the GC root is regenerated.
-   **Redraw with this node**: redraws the reference chain graph centered on the node.
-   **Reveal in Statistics**: displays the node on the **Statistics** tab.
-   **Clear Diagram**: clears all content in the current graph and the activation status in the bottom bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/OB9jz1T7T6mNKmBCuZndBw/en-us_image_0000002532750287.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F75A6F52C8FA4C7D95E7F438247DB672F0B1350D65905AC578E03F92F16DD781 "Click to enlarge")

After selecting **Show More References**, **Show Path to GC Root**, or **Redraw with this node**, you can click the left or right arrow in the lower left corner of the details area to navigate back to the previous graph or forward to the next graph, respectively. In this way, you can switch between multiple (a maximum of three) graphs. This feature is available only when the left or right arrow is not dimmed.![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/_HMyVH4VQxe0p2-BJn5gNA/en-us_image_0000002501070256.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CF6F676A096D87759C4F07538137C77F3B7A10FA9027EA4524B92FC6CAF04C1 "Click to enlarge")

#### Importing Memory Snapshots Offline

DevEco Profiler supports offline import of memory snapshots. You can import one or more .heapsnapshot and .rawheap files.

You can click **Open File** in the **Create Session** area on the DevEco Profiler main page to import .heapsnapshot or .rawheap files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/uUMMiExGRtitUxOjklm2Kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B40C4DFF1EA183D2FEEF4BDEE88383DF4DDF7A8E78F50526E184ED67C5080DA2)

-   The size of a single file to import cannot exceed 1.5 GB.
-   A maximum of 10 files can be imported in batches.
-   The .rawheap file is a memory dump generated when an Out of Memory error occurs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Kn8AGl_-SfSzxOqF4i8Jzg/en-us_image_0000002500910406.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2CB75ACC7D27A78689FD172AF26845491E77EC77EA67E1427AE036EC0DD4FCF "Click to enlarge")

After the offline import, you can import a .jsleaklist file that matches the .heapsnapshot or .rawheap file to display the memory leak objects collected by the jsleakwatcher.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/Hfs00YyoQcyqefiMATzMjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E05BC6E066833AAEEF9CD2DD4C4D634C53E315AD1EA59AF2B3DF68AFA6C80344)

-   The size of a single .jsleaklist file to import cannot exceed 30 MB.
-   The .jsleaklist file to import must match the imported .heapsnapshot file based on the hash value in the file.
-   You can import different .jsleaklist files multiple times, or import multiple different .jsleaklist files at once. Repeated imports will not overwrite the previously imported matching .jsleaklist files. The total number of successfully imported files must not exceed the number of imported heap snapshot files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/EoEcZxZgQBOp1Xv_TeESEA/en-us_image_0000002500910416.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7427D05196E53BE2AA7D25AA892C162D21866C8405714981A2F6E160DF18ECE3 "Click to enlarge")
