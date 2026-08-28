# Fault Log

When an app process is terminated due to an error, the app throws a fault log to report the cause of the crash. You can analyze the fault log to locate the cause and the code that causes the crash.

Fault logs are automatically collected by the system from devices. They are classified as follows:

-   App Freeze
-   CPP Crash
-   JS Crash
-   System Freeze
-   [ASan](../asan-detecting-memory-errors/document.md)
-   [HWASan](../hwasan-detecting-memory-errors/document.md)
-   [TSan](../tsan-detecting-thread-errors/document.md)
-   [UBSan](../ubsan-detecting-undefined-behaviors/document.md)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Xzj8_xRpSk-KoccK7hs_EA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9E57E80BF688197AD161DEC3AEF33E522244DD4C4E3C855A9E021C86EDE571D)

In debugging mode (debug or attach), DevEco Studio shields the timeout detections such as App Freeze and System Freeze of the project to prevent the debugging from being affected by timeout detections.

Currently, the following types of App Freeze faults can be shielded:

-   **THREAD\_BLOCK\_3S**/**THREAD\_BLOCK\_6S**: The main thread of an app is suspended for 3s or 6s.
-   **APP\_INPUT\_BLOCK**: The input response times out.

The following types of App Freeze faults can be shielded:

-   **LIFECYCLE\_TIMEOUT**: The lifecycle switchover of an app or ability times out.

#### Viewing Fault Logs

## Viewing Historical Fault Logs of a Device

Open the **FaultLog** window. All the fault logs thrown by the selected device are displayed.

The fault logs displayed in the left pane are organized in the app/atomic service bundle name > fault type > fault occurrence time structure. After you select a fault occurrence time, the detailed fault information is displayed in the right pane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Tba00zRNSBC7MVuNc8k3YQ/en-us_image_0000002532670263.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DAFE0AC6C77AD824F24FA565D8D38E4447C7FB86DB3837D52E9F77F02EDA582)

## Viewing Real-Time Fault Logs of a Device

When a fault is thrown by a device, DevEco Studio displays a message. You can click **Jump to Log** to view the log information in the **FaultLog** window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/w_5M9fbPSJCq6U3_svyqqg/en-us_image_0000002532750231.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BABF51808DB8BF5E209985AAFC109EDE87C092805C4407B5A633EFE227378BD8)

## Locating the Error Code

If the link or offset address in the stack trace information in the thrown fault log points to a line of code of the current project, a hyperlink is provided. You can click the hyperlink to go to the code line.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/U-lwUVnnRhGb7eNgcS-L5g/en-us_image_0000002500910356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79FB5D7CBDAEB8BC16348861A0A838309B23ABDE20B19982819F74D03862012A)

#### Exporting Fault Logs

You can export fault logs locally for further analysis. You can export logs of a fault type or all fault logs as required.

-   To export logs of a fault type:
    -   Right-click the selected node and choose **Export FaultLog** from the shortcut menu.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/S9OLfsn7QBieiXSpTKyRkQ/en-us_image_0000002532670287.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF686829DBA5AD8C2DF269D25C48639A4B3C9042384009135D3902312CED02C4)
        
    -   Click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Ppdoya3TTCOv6sxPg5ndIg/en-us_image_0000002501070210.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3832CE1E94167EB8FA076CEFB5BD48C6FF97506479F1E03DE533C2D9188A7D19) **Export FaultLog** button and select **Export Selected FaultLog**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/XmdD-OcZRum4jl8RRLHdKA/en-us_image_0000002532670273.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD9FB63F7719063E99BFBBD1E7F6B322DCA08F27AEBAFFC5218E3272C64E5AA8)
        
-   To export all fault logs, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/n8WAGmKJRtmWuf47SRCdnQ/en-us_image_0000002532670269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7444FF335CC2CFCEFD43B77305DAD60BA88C47F50E0288F259772181B94FE5D3) **Export FaultLog** and select **Export All FaultLog**.

#### Viewing cppcrash Structured Logs

Since DevEco Studio 6.0.0 Beta1, Cpp Crash fault logs can be displayed in a structured manner and filtered.

1.  Double-click the cppcrash log. The **Fault Analysis** tab is displayed on the right of the **Fault Info** tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/C18LKtlvTLaF_A0kEI_jAw/en-us_image_0000002501070192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BD368DE45E36DE5200838ED02FE57407BF6036A5A0131603E5CC08F8052C6D4 "Click to enlarge")
    
2.  Click the **Fault Analysis** tab to view structured log information.
    
    -   The fields in the upper part of the page map to the fields in the fault log. For details on their mapping relationships, see [Fields](#section1983219211210).
    -   In the lower part of the page, there are:
        -   **Stacks** tab: displays thread stack information. For details, see [Viewing Stack Information](#section459581010138).
        -   **Logs** tab: displays HiLogs in the fault log. For details, see [Viewing HiLogs](#section13361239195113).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/FWDEJZg7SFyYIUGPQGmxUg/en-us_image_0000002501070190.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0D42F3AD8EA79C966E579B58575C13C769DDDBF2470DC3D5545CF11841A4D3D "Click to enlarge")
    

## Fields

The following table describes the fields on the **Fault Analysis** tab and their mapping with fields in the fault log.

**Table 1**
| 
Fields on Fault Analysis

 | 

Description

 |
| :-- | :-- |
| 

Occurrence time

 | 

Time when the fault log is generated, which corresponds to the **Timestamp** field in the fault log.

 |
| 

Analysis time

 | 

Time when the log is displayed in structured format, that is, the time when the log file is double-clicked.

 |
| 

Frontend

 | 

Whether the app is a foreground app, which corresponds to the **Foreground** field in the fault log.

 |
| 

Bundle name

 | 

Bundle name, which corresponds to the **Module name** field in the fault log.

 |
| 

Device type

 | 

Device type.

 |
| 

App build number

 | 

App build number, which corresponds to the **VersionCode** field in the fault log.

 |
| 

App version

 | 

App version, which corresponds to the **Version** field in the fault log.

 |
| 

Device model

 | 

Device information, which corresponds to the **Device info** field in the fault log.

 |
| 

System version

 | 

System image version, which corresponds to the **Build info** field in the fault log.

 |
| 

Abnormal signal

 | 

Exception signal, which corresponds to the **Reason** field in the fault log.

 |

## Viewing Stack Information

The **Stacks** tab contains the stack information in the fault log and is folded by thread. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/8HfyovJATI-5QVnqQ1NBfg/en-us_image_0000002532670265.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=569D90B52F958A9585E5FFD1AF68513CBDE0C2428EF10BB53D66D62D8DB30380) to expand the corresponding thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/9PcK_4RfRU2o8QuT0B4v5Q/en-us_image_0000002532750233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F19E12CC48D61A532624D06B79B0792C601251B71D6A2B61B55DFB9701EBC598 "Click to enlarge")

In the figure, the checkbox marked with **1** is for expanding application stacks, and the checkbox marked with **2** is for expanding system stacks. These two checkboxes together form four states, as detailed in the following table.

**Table 2**
| 
Checkbox State

 | 

Description

 |
| :-- | :-- |
| 

Neither 1 nor 2 is checked

 | 

All threads are displayed, in a collapsed state.

 |
| 

Both 1 and 2 are checked

 | 

All threads are displayed, in an expanded state.

 |
| 

Only 1 is checked

 | 

Only application threads are displayed, in an expanded state.

 |
| 

Only 2 is checked

 | 

Only system threads are displayed, in an expanded state.

 |

## Viewing HiLogs

The **Logs** tab displays the HiLogs in the fault log. You can filter and search for logs by log level.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/CGoXxEgQStK3IKQXrwjWdA/en-us_image_0000002532670267.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=746292E7F6CA4C358EACD156E0B143AB5A1EAC6629D89E3739C726722E6AF326)

#### Viewing appfreeze Structured Logs

Since DevEco Studio 6.0.0 Beta2, AppFreeze fault logs can be displayed in a structured manner and filtered.

1.  Double-click the appfreeze log. The **Fault Analysis** tab is displayed on the right of the **Fault Info** tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/IoEZ_NA6Tn68FW89Z2yAKA/en-us_image_0000002532750229.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B1D9C0F529A419D53663A5E54384D5731124A5D9EA2375B4BC29FA9E0CCFCE4)
    
2.  Click the **Fault Analysis** tab to view structured log information.
    
    -   The fields in the upper part of the page map to the fields in the fault log. For details on their mapping relationships, see [Fields](#section15864144624712).
    -   In the lower part of the page, there are:
        -   **Stacks** tab: displays thread stack information. The usage is the same as that of cppcrash logs. For details, see [Viewing Stack Information](#section459581010138).
        -   **Logs** tab: displays HiLogs in the fault log. The usage is the same as that of cppcrash logs. For details, see [Viewing HiLogs](#section13361239195113).
        -   **System** tab: displays device CPU/memory logs in high-load scenarios. For details, see [Viewing High-Load CPU/Memory Logs](#section179717814915). This tab is available since DevEco Studio 6.0.0 Beta3.
        -   **3s/6s Compare** (added since DevEco Studio 6.0.2 Beta1): displays the main thread stack logs at the 3s and 6s time points for AppFreeze issues of the [THREAD\_BLOCK\_6S](../../../../system/debugging-tools/performance-analysis-kit/fault-detection/application-freeze-detection/document.md#thread_block_6s-application-main-thread-timeout) type. For details, see [Viewing 3s/6s Stack Logs](#section76467955514).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/pyu03Y0JRYO_5qnMjhkQlg/en-us_image_0000002500910352.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8809C1A4040E0518FA9ED28010DFB3F587D6DB172F5BE26D0DE4425152D768BB)
    

## Fields

The following table describes the fields on the **Fault Analysis** tab and their mapping with fields in the fault log.

**Table 3**
| 
Fields on Fault Analysis

 | 

Description

 |
| :-- | :-- |
| 

Occurrence time

 | 

Time when the fault log is generated, which corresponds to the **Timestamp** field in the fault log.

 |
| 

Analysis time

 | 

Time when the log is displayed in structured format, that is, the time when the log file is double-clicked.

 |
| 

Frontend

 | 

Whether the app is a foreground app, which corresponds to the **Foreground** field in the fault log.

 |
| 

Bundle name

 | 

Bundle name, which corresponds to the **Module name** field in the fault log.

 |
| 

Device type

 | 

Device type.

 |
| 

App build number

 | 

App build number, which corresponds to the **VersionCode** field in the fault log.

 |
| 

App version

 | 

App version, which corresponds to the **Version** field in the fault log.

 |
| 

Device model

 | 

Device information, which corresponds to the **Device info** field in the fault log.

 |
| 

System version

 | 

System image version, which corresponds to the **Build info** field in the fault log.

 |
| 

Freeze type

 | 

Freeze type, which corresponds to the **Reason** field in the fault log.

 |

## Viewing Stack Information

The **Stacks** tab displays stack information in appfreeze logs. The usage is the same as that of cppcrash logs. For details, see [Viewing Stack Information](#section459581010138).

## Viewing HiLogs

The **Logs** tab displays HiLogs in appfreeze logs. The usage is the same as that of cppcrash logs. For details, see [Viewing HiLogs](#section13361239195113).

## Viewing High-Load CPU/Memory Logs

The **System** tab is available since DevEco Studio 6.0.0 Beta3. It displays device CPU/memory logs in high-load scenarios, helping analyze the association between high load and appfreeze.

The following figure shows CPU-related logs.

①: The bar chart indicates CPU usage (as a percentage) at corresponding time points.

②: Hovering the mouse over the bar chart displays the total CPU usage, the top 5 process IDs (PIDs) by CPU usage, and their respective CPU usage.

③: Selecting a bar in the chart displays the relevant logs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/yvJ52zukSkumkWNhKX9_IA/en-us_image_0000002500910344.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=016A3A2475E921A26287D798CFEAC805060A6ECF1523BA0C6E5065764E3352B1)

The following figure shows memory-related logs.

①: The bar chart indicates memory usage (as a percentage) at corresponding time points.

②: Hovering the mouse over the bar chart displays the total memory usage, the top 5 PIDs by memory usage, and their respective memory usage.

③: Selecting a bar in the chart displays the relevant logs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/C7fQ59MLTb6dLGwVvFTIXg/en-us_image_0000002501070212.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9463467374149D53430C542293BCCDF4D36DD806B3CE8E6E891DA850FC39DB21)

## Viewing 3s/6s Stack Logs

Since DevEco Studio 6.0.2 Beta1, the **3s/6s Compare** tab has been added. For AppFreeze issues of the [THREAD\_BLOCK\_6S](../../../../system/debugging-tools/performance-analysis-kit/fault-detection/application-freeze-detection/document.md#thread_block_6s-application-main-thread-timeout) type, this tab displays the main thread stack logs captured at the 3s and 6s time points and highlights potential problematic stack frames.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/DohEYlmyR3WBsXfuj-RoIA/en-us_image_0000002532670261.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3150D48F528C8857B49C984F8FB52874CFBAB077CB29B7838C8868B1A46C3EB)

If the AppFreeze issue is not of the THREAD\_BLOCK\_6S type, the **3s/6s Compare** tab will not be displayed.
