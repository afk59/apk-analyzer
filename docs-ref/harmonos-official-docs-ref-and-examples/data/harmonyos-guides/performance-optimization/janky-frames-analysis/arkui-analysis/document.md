# ArkUI Analysis

ArkUI analysis is intended to identify frame freezing and frame loss issues caused by page layout, component time consumption, and state variable update. Common scenarios include:

Scenario 1: Performance issues caused by excessive layout nesting.

Scenario 2: Improper data structure design, where an app uses a large object and updates only certain properties, leading to redundant update for properties that have not changed.

Scenario 3: Repeated binding of child components within a parent component to the same state variable for updates.

Scenario 4: Incorrect use of decorators, such as using @Prop to pass a large object for deep copying.

#### Inspecting Component Drawing Duration

You can obtain statistics such as the component drawing frequency and duration from the ArkUI Component lane.

1.  Drag the mouse on the timeline to select a time period.
2.  On the details panel, view the drawing statistics of custom components and system components in the selected period, including the number of drawing times, total duration, minimum duration, average duration, maximum duration, and standard duration deviation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/eHmVS5G0QvWt1cLwax9j-w/en-us_image_0000002532669845.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A4BEE85D23668B828374FB8643DCE4C72CF440544614E358D3B843AA9D4E6B8 "Click to enlarge")
    
3.  On the **Details** tab page, you can view component details by timeline. In addition, the **More** area displays information about the component tree where the component is used as the root node.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/PHoJfvDmRPC2TYSCFyGpWA/en-us_image_0000002501069774.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F293195FC003FB7C1B67B0EF7F9D7F5BE9E9193BB99B87F89DAAD29A8997EECA "Click to enlarge")
    
4.  Click a bar in the ArkUI Component lane to display the **Slice Detail** area. You can click **Name** in the **Slice Detail** area to redirect to the corresponding Process sub-lane, with the trace information selected. In addition, the **More** area displays information about the component tree where the component is used as the root node.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Qs0UArKLSPWe3JFh45RDcA/en-us_image_0000002532749799.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F291A778A5BCEDA5D8CAFE4D9F5C210A7F908962E0D9266FD7A0850E677E7CD8 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/gGjjjs02S9G-S7J91ntYTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4541382904B8214CB5C49A5991DF89A53124109B256F0BD5E9908452B92015B8)
    
    Due to privacy and security policies, the ArkUI Component lane is not available for apps that have been released on AppGallery.
    

#### Inspecting State Information

1.  Select the **ArkUI** template, create a session, and start recording. Trigger component updates during the recording process.
2.  After recording ends, wait for data processing to complete. Click the ArkUI State lane. Inspect changes in state variables that occurred during the recording in the data area below the lane. The **Summary** tab page displays the names, the number of changes, types, owning components, and owning classes of state variables.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/PsqpddDHRFiGX5y6ZM3gSg/en-us_image_0000002532749793.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DC87C9F9E3D04914F053D7D8A40760D06C658B3A2AE37AC1CD7E45E34A0042C "Click to enlarge")
    
    The **Current Value** tab page displays the changes in state variables in chronological order. The **Current Values** column shows the value after the change.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/g20WxPYvS8GCRUe1BtioyA/en-us_image_0000002501069776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1B685DBE5A6F94173EC20EC456DF085FC03DF57C21834027670E99DB8D46C40 "Click to enlarge")
    
3.  Select a data point on the **Current Value** tab page. The lane will display its temporal position with a dashed line. At the same time, the **More** panel on the right will show the components affected by this state variable. Turn on the **Delivery Chain** switch at the bottom of the page to view a diagram of the components affected by the state variable.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/onHV9Qp4TR-8-bH8ha7bdg/en-us_image_0000002500909926.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B4B1171AB9829272A2D48F12AB2E2BD3A095F3384660D893D69A27A282DCD1A "Click to enlarge")
    
4.  Locate the time point of state variable change that may cause jank, select the corresponding time segment, and choose the ArkUI Component lane to view the update time of the corresponding component.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/K0CXn6BvRuCSVzN3sgA7Ew/en-us_image_0000002501069778.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A52D2884936A36AF8593361D7580B476D89CB386BBDE2F8FDAE6951C917D5FA2 "Click to enlarge")
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/YsKA_nzaTK-deFE_dw4Xgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E4E9FB7604509A9D3F52311E1523456BB7B37D0C7AF66FF0A0962208568FCA2)

-   For details about other lanes, see [Frame Analysis](../frame-analysis/document.md).
-   Due to privacy and security policies, the ArkUI State lane is not available for apps that have been released on AppGallery.
