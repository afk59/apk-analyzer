# Case: Analyzing the First Frame Completion Delay During Cold Start

The first frame completion delay of an app during cold start is the period from the time when a user touches the app icon on the home screen to the time when the first frame of the app process is drawn. This case describes how to find the start and end points of the first frame completion delay of an app during cold start, and how to analyze the app runtime logic based on the call stack and trace information to locate the cause of the unexpected first frame completion delay.

For details about the basic operations related to app cold start analysis, see [Basic Operations with Launch Analysis](../basic-operations-with-launch-analysis/document.md).

#### Analysis Steps

To analyze the first frame completion delay during cold start, perform the following steps:

1.  Determine the start and end points of the first frame completion delay during cold start.
2.  Select the start and end points of the first frame completion delay during cold start, and check whether the delay exceeds the expected value.
3.  If the delay exceeds the expected value, troubleshoot based on the call stack and trace information.

#### Recording Launch Data

1.  Connect the device and click the app selection box to select the target app. Select the **Launch** template, and click **Create Session** or double-click the **Launch** icon to create a launch session.
2.  After the template is created, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/fpwL0WgdQP6RgjDnx9Cedg/en-us_image_0000002501070102.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=981D48C23B5952B6D798D198D0003007EACF3ECAC4596053FDF016392CB9D6CF "Click to enlarge") to switch the launch mode to ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/X0jLLeKiQ7yuBRpEv1zkuQ/en-us_image_0000002532750107.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1680D287EC64852D8324D91D5B3C2D02F3B266CBC60FE08DF57A1869D3F02FF "Click to enlarge") manual launch.
3.  On the toolbar, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/D2d9dgGnSsi8IMcousnLeg/en-us_image_0000002500910244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=809A704FA81B2B6C24C1E94B8E5CEC23E724A9BCE61C47F41DECF9621E8015BF "Click to enlarge") and select **HiTrace** > **multimodalinput** to collect trace information of the multimodal subsystem. The information includes the finger-off signal transferred by the hardware, that is, the touch release event received by the multimodal subsystem.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/DSRoOtgEQZuBkAuZSVoqAg/en-us_image_0000002532750125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=160173EFDCDCB2042836AD4B7BCA4C7F3AC56B55D82074036624A4CA8E306F30 "Click to enlarge")
    
4.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/PA8n5WmVSyq3VbTgxzzfqA/en-us_image_0000002500910250.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B87CD516FA636D1EBCA3E93A125097A2D39CC03A5F8031DA32483AE061D5C36 "Click to enlarge") to start recording. After the dialog box is displayed, click the app icon on the device to launch the app.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/FREj6xbPQ4aZrT20_bC0Mw/en-us_image_0000002532750117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4DF57B31757864659E029568C9D7F816569C5BE043FB881C5B84E757597E2E5 "Click to enlarge")
    
5.  Once all the lanes on the right side show "recording," it indicates that the recording is in progress. After the cold start is complete, you can end the recording by clicking the square button shown in the figure or the pause button on the left.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/QUdTZBjlSYik4bic_VJyfw/en-us_image_0000002532670161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A426ECCE3B4520706E5E03B9F492CAB2C9264FBF07B6E43563EA06C34F0BAF43 "Click to enlarge")
    

#### Analyzing Launch Data

## Determining the Start and End Points of the First Frame Completion Delay

**Determining the start point of the first frame completion delay during cold start**

The start point of the first frame completion delay is the moment when the user releases the touch on the app icon on the home screen, that is, the moment when the multimodal subsystem receives the finger-off signal from the hardware.

The trace point corresponding to the finger-off signal takes a short time and is inconvenient to memorize. Therefore, you need to find the trace point (**H:DispatchTouchEvent**) where the launcher process receives the touch release event to locate the start point of the first frame completion delay. The procedure is as follows:

1.  Locate the **H:DispatchTouchEvent** trace point where the launcher process receives the touch release event. Specifically, in the Profiler panel, select **Search Unit Data** from the search box options to search for lane data. Enter **H:DispatchTouchEvent** in the search box and press Enter. Navigate through results using the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/tsjFvH6WQhm9zyba9sEVJA/en-us_image_0000002532750121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CAEAE902683D429E9F61DDA0F4969C116F0B16D9CB40A4444254BCBB82D11C9 "Click to enlarge") or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/UV1vSt6zSnS_64IUJLj3AA/en-us_image_0000002500910252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A84520145B1976894CCB06742F37A538581C08BF8188B0D66D9B73625E57A7DD "Click to enlarge") button to find the **H:DispatchTouchEvent** point within the launcher process lane (**ohos.sceneboard**) where **type** is **1** (**0**: finger down; **1**: finger up; **2**: move). Add a marker to this point. Double-click the marker and edit its description to "Touch release event" in the property dialog for future reference. This trace point marks the moment the launcher process receives the touch release event.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/zkeoqdF0TVC71zW8gYeD4A/en-us_image_0000002532750113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24E3BF74A9AD172F7B3CEEDC54B36ABAF089831D87D2626473ED7728430AD13A "Click to enlarge")
    
2.  Search for the multimode subsystem lane (**mmi\_service**). Specifically, click **Search Units** from the search box options. Enter **mmi\_service** in the search box and press Enter. If multiple lanes match, navigate through results using the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/oOOZKFw5SwuUq9Oz0xbjQw/en-us_image_0000002500910254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6734666FDF7120D046533800F92DE64E80C177B52D2180A067B62CF498D49168 "Click to enlarge") or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/JcFaME6kSIqquBNuw33RlQ/en-us_image_0000002532670171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23068CFD40A2DFB122367AAA37ED7B631C52EBFF8A0E784F09499855AEDEE169 "Click to enlarge") button to identify the **mmi\_service** lane containing the target trace segment.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/lGO3rSHUQZSWyySvlBZL0Q/en-us_image_0000002532670175.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70DE7F2E8875B5AE7F7B8199157ECE13040E1DBB9B4EF183882505C2CC603DB5 "Click to enlarge")
    
3.  By using the previously marked touch release event trace point in the launcher process, locate the corresponding trace point in the multimodal subsystem.
    
    Specifically, within the **mmi\_service** lane, identify the **CPU Running** slice positioned prior to the touch release marker (indicating subsystem activity during this period). Below this slice, find the trace point labeled **H:service report touchId:{id}, type: up** or **H:service report pointerId:{id}, type: button-up**. Add a marker to this trace point. Modify the marker's description to "Start point of first frame completion latency." This trace point marks the multimodal subsystem receiving the touch release event, that is, the start point of the first frame completion latency during cold start.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fob2Ay9AQkqpORFCUymYyg/en-us_image_0000002501070086.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91A4D2108582A0808D929C68BC39C57DD041209481EF8F6748A97BF939DDE5AC "Click to enlarge")
    

**Determining the end point of the first frame completion delay during cold start**

The end point of the first frame completion delay is the time when the first hardware vertical sync signal is received after the application process starts, that is, the end point when the Render Service (unified rendering service process) displays the rendering result of the application's first frame on the screen. To locate the end point of the first frame completion delay, perform the following steps:

1.  Identify the first vertical sync signal trace point **H:ReceiveVsync** after the application process starts. This trace point indicates the beginning of the first frame rendering for the application. Select the application process sub-lane, and select **Search Unit Data** from the search box options to search for lane data. Enter **H:ReceiveVsync** and press Enter to locate the first **H:ReceiveVsync** point. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/v0KS9u2DQ72D00-yctH1Mw/en-us_image_0000002500910256.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC1C2E85EEBE08B68727AD3E3DC1015B5954F40DDACE3F06656F2E12D0483D8D "Click to enlarge") 
2.  After the application process starts, upon receiving the first vertical sync signal, it notifies the Render Service process to perform graphics rendering. Therefore, the first step is to locate the following three traces related to this notification: **H:FlushMessages** > **H:SendCommands** > **H:MarshRSTransactionData**. Since these three traces have short durations and are difficult to visually identify, use the search function to locate them: (1) Select the **H:ReceiveVsync** trace point. (2) Select **Search Unit Data** from the search box options to search for lane data. (3) Enter **FlushMessages** and press Enter.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/_dgyg1lZRbqbrX3F99Oisg/en-us_image_0000002532750123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F15F6799D2AE2F353ED25C1661918D449FB2B32068AC5D34E6AD667894416F9 "Click to enlarge")
    
3.  After locating the trace point **H:FlushMessages** (indicating the flushing of drawing messages), continue analyzing the layers below this trace point. First, find **H:SendCommands** (indicating the transmission of drawing commands to the Render Service process for graphic rendering). Then, locate **H:MarshRSTransactionData** (indicating the transmission of drawing commands). These three trace points together represent the workflow of the application process notifying the Render Service process to perform graphic rendering.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/WAi3bp2dQbGUWSYfzGIe0A/en-us_image_0000002501070098.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=254CEAEF3B9C19C35F77EEAAE5C6C3C260128E02C48E3367B30662DFBA78158A "Click to enlarge")
    
4.  Locate the trace point where the Render Service process receives the first frame rendering notification from the application process. Specifically, click on the **H:MarshRSTransactionData** slice. In the **Slice Detail** panel, you can view details of this trace, including the trace name and the process it belongs to. Click the jump button ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/rXiUZGKoTlWI5uohX4Nneg/en-us_image_0000002500910246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=658D79B5A9091D50ECBD3A43756C617E8572B6A6285B551F9A4E7A08EF76BA0F) next to **Name** in the **Slice Detail** panel to navigate to the **H:RSMainThread::ProcessCommandUni** trace point in the **render\_service** lane. Add a marker to this point and modify its description to "Rendering callback received." This trace point indicates that the Render Service process has received the first frame rendering notification from the application process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/7gPRO8lMTqGeo7vukVyg3w/en-us_image_0000002500910248.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30778F5E25B17C7EC00B0B14B0A23B4E635C4BD886C36BEBBAAB1CBB5AF4AD03 "Click to enlarge")
    
5.  Locate the trace point where the Render Service commits the application's first frame to hardware display, which is completed in the Render Service's hardware display thread (**RSHardwareThrea**). Specifically, click **Search Units** from the search box options. Enter **RSHardwareThrea** in the search box and press Enter. Find the first **H:CommitLayers** trace point after the "Rendering callback received" marker, and add a marker to it. Modify the marker description to "FrameBuffer submission to display hardware." This trace point indicates that the Render Service has committed the application's first frame to hardware display.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/uqHfdLxjSZWouKha0qA6sA/en-us_image_0000002500910238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAA7D08A2B471031CAC003522DD58CF48A938466E054ED0BA049368AFC28E529 "Click to enlarge")
    
6.  Locate the trace point where the Render Service presents the application's first frame rendering result on the screen, which is completed in the **Present Fence**. Specifically, click **Search Units** from the search box options. Enter **Present Fence** in the search box and press Enter. Find the first **H:Waiting for Present Fence** trace point after the "FrameBuffer submission to display hardware" marker. This trace point indicates that the Render Service has presented the first frame to the screen. The end position of this trace point is the end point of the first frame completion delay. Add a marker here and modify its description to "End point of first frame completion latency."
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/pWg0J7p-Rp2D85ZsFl8hGA/en-us_image_0000002532750115.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10E77B9E69035036BBAA39F06282EED30F809059F5FCC248E1748F2747D6E1E6 "Click to enlarge")
    

## Case: First Frame Completion Delay During Cold Start Exceeds the Expected Value Due to Prolonged App Home Page Loading

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Bbmiq2JvTKaFvuX3XkC0PQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8148831B823B5A7D4FAE39FE099ABE6E192AECBAF3BE5D0604E8280EA338791)

-   This case is based on the assumption that time-consuming operations are performed in the lifecycle callback function of the ability during application process startup.
-   The expected first frame completion delay during cold start is less than or equal to 600 ms.

Select the start and end points of the first frame completion delay during cold start of the application. The duration within the selected range reveals that the actual delay exceeds 800 ms, surpassing the expected 600 ms.

Switch to the Process lane and view the trace of the main thread (whose thread ID is the same as the process ID).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/3JIaO4PKSvefvARrEFHyog/en-us_image_0000002526402710.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB912D5965772A3CD2D6E9597C82E5B3C9BFD214CDB302A98CBC9E89EB8A2D66 "Click to enlarge")

The **Details** area displays the trace name, start time, and duration. Sort the durations in descending order to identify that the main time consumption occurs in **H:void OHOS::AbilityRuntime::UIAbilityThread::HandleAbilityTransaction**. This phase primarily involves the execution of callback functions during the launch lifecycle of AbilityStage/Ability. From this, it can be inferred that the prolonged execution of AbilityStage/Ability launch lifecycle callbacks is the root cause. Next, analyze the call stack to determine why these callbacks take excessive time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/-0qldLpIQ02dDstHKlLWzQ/en-us_image_0000002500910236.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E856730D74F569FA56517BBE2BB82436CCE34C7078771E0BD222A9896CBDFD5C "Click to enlarge")

Switch to the **ArkTS Callstack** lane to analyze the time-consuming functions on the ArkTS side. First, check the **ArkVM** sub-lane whose thread ID matches the process ID (this sub-lane represents the main thread call stack) to view the execution time of ArkTS methods. As shown in the figure below, no ArkTS functions are executed, so you need to switch to the **Callstack** lane to view the mixed ArkTS-Native function call stack.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/_Iw3F-JWTFG1uAfYturzJQ/en-us_image_0000002501070084.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D402232D00EA10292707E62653F6EF663070C7A13A282CA84A31A2D049B493F9 "Click to enlarge")

Finally, switch to the **Callstack** lane, check the main thread sub-lane (whose thread ID matches the process ID), and view the **Heaviest Stack** section below. Scroll to observe the function call stack with the highest weight percentage, and identify that the main time consumption is caused by the code on line 79 of the **EntryAbility.ets** file. Double-clicking this stack frame will directly navigate to the corresponding position in the source code file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/Goe9jOSgSf6p6BqL3q4aXQ/en-us_image_0000002532750105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EED62B6BF2DD471A7AF974115135D310EB76DD4E1731948BF6A23D2C9E9AECA7 "Click to enlarge")

By examining the service code, it is found that time-consuming operations are performed in the **onCreate()** method in the **EntryAbility.ets** file. You are advised to handle time-consuming operations through asynchronous tasks with delayed processing or execute them on separate threads to reduce main thread load and shorten the first frame completion delay during cold start.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/3gXCTMmvS1CNO5IlNnNY_A/en-us_image_0000002532750119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64232D51D822FCA44554924628C3B4D6B60079B229E73E23B3A8C0449811C3D4)

For more cold start optimization solutions, see [Reducing Application Cold Start Latency](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-application-cold-start-optimization).
