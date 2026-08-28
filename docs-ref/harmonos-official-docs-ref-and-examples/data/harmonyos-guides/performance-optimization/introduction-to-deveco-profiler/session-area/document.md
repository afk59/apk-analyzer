# Session Area

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/tGF7NeT4TtOgr548ZuIJ2A/en-us_image_0000002500910714.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=069A3736B94CF5C051171D0F570D9D53433E5A205D9086C8CE7792C76481E413 "Click to enlarge")

Located on the left of DevEco Profiler, the session area can be divided into three parts.

(1) Target selection, where you can select a device, app, and process as the analysis target.

In this part, you can select the device, app, and process from the drop-down boxes in sequence.

(2) Session list, where the created profiling sessions are displayed.

You can click a session in the list to display the session data in the data area on the right. After you select the device, app, and process, a Realtime Monitor task is displayed by default in this list.

The session list records all running sessions. Each session contains the following information: session name, session status, and session duration, which are shown as **Launch**, **Recorded**, and **7s 605ms** in the figure, respectively. You can reorder sessions by dragging and dropping them.

In the session list, you can perform the following operations:

**Starting or deleting a session**: When you hover the mouse pointer over ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/mHMAsS61S7OpRa1Ak13ZHA/en-us_image_0000002532670621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A40FBA94739115E8FE5D248745EB5788F609009C65FF051205818CBED7CD8FD) next to the session name, the basic information about the analysis target is displayed in a tooltip. When you click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/DxXDgFNeT3CtNKxMhUz_AQ/en-us_image_0000002532670631.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FCCAB53B835B9106900006DF4946FE806BB1D9C577BA4E87B251A15AEE06EB2) on the right of the session, the tool starts to capture performance data, and you can operate the app to reproduce the performance deterioration scenario. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0hA2xluaQdCo_UbvssD0gA/en-us_image_0000002501070562.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0D90FE4CAE2D473F14E4D2F77F9E2BC04EAC1B35C3E96EBB06A23D37D1A0403) to stop session capture or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/y5mjIg95RxSempKAfJfYYg/en-us_image_0000002501070560.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21DA08A07767B696C5BA4BCDEDFD97F3D411FEC452FA372C67D35C52AE11D29C) to delete the session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/xG8xPMPZTqS-r-PDtCSK2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF6AEDEDC015B6D969DFE6A41FF68003836B02209C14EF507B760450A7DFCF04)

-   There are two types of sessions in the session list: active sessions and historical sessions. Active sessions are directly displayed. To view historical sessions, click **View Successful Sessions** in the lower part of the UI. After you select a new analysis target, the active session is turned into a historical session.
-   Historical sessions support session deletion and data export.
-   Only sessions that are successfully imported or have data successfully captured can be put in the session list. Sessions that fail to start or fail to have data captured are automatically deleted from the list after you change the device or app for analysis.
-   After the performance data is captured for a session, ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/kDLmuD3_QLGagilWw9fllg/en-us_image_0000002500910718.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C2E179F8ACCF528D29B57D7D212C5D71A723C4EC49985B7D94D25923D0C1B4A) is displayed, indicating that the data is being parsed. Wait until the parsing is complete.
-   The maximum number of sessions (that is, the sum of active session count and historical session count, with duplicates not included) is 15.

**Exporting data**: After data parsing is complete, the session enters the data display state and data is displayed in the data area on the right. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/EChIq3W_QxazdmoYhASpuQ/en-us_image_0000002500910716.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB40251823654866727D30CC3606AF1DA5778E7596A4DE08ABE181DEA35BC996) on the session panel to export the data to the local host. Data export facilitates data sharing and prevents the loss of collected performance data.

③ Scenario-specific template selection: entry for creating a session. DevEco Profiler provides the following scenario-specific templates: [Frame](../../janky-frames-analysis/frame-analysis/document.md), [Launch](../../cold-start-analysis-launch/document.md), [Snapshot](../../memory-leak-analysis-snapshot/document.md), [Allocation](../../memory-analysis-allocation/document.md), [ArkUI](../../janky-frames-analysis/arkui-analysis/document.md), [Energy](../../energy-consumption-diagnosis-energy-analysis/document.md), [ArkWeb](../../loading-and-frame-loss-analysis-arkweb/document.md), [Network](../../network-diagnosis-network/document.md), [Concurrency](../../parallelism-and-concurrency-analysis-concurrency/document.md), [Time](../../basic-time-analysis-time/document.md), and [CPU](../../cpu-activity-analysis/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/iVi5qXrPQ52h_gPo7SKHDQ/en-us_image_0000002532670623.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88F75DB7475CA6483AA01C38F2392FB90D47A33C0482187CB2B0CCE3E213B032 "Click to enlarge"): Frame template, a template for the janky frame scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/cUDF1MbRRwqnA4xLUnY0ow/en-us_image_0000002532750577.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72FE18E2F99695685EC1E3433EDCFE9E9669B8963366B1D96994887C307F97AD): Launch template, a template for the cold start scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ix-TNtiSRuuBWy6hu2mPFQ/en-us_image_0000002532750583.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC601381F3FEAED54A7F4EFD23BDB671A6198B83AF17E7E1BCF98596796B1C2B "Click to enlarge"): Snapshot template, a template for the ArkTS memory leak scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ZpkezANfRdmKMnHEG1sIsQ/en-us_image_0000002532670627.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=931718D862375D4F94A026BC7BF4D59F455F9CFF9B77797D715BA4AF44C93980): Allocation template, a template for the native memory leak scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/9ywvf2_sRAee1kKonD1JMA/en-us_image_0000002532750581.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5FE849E2974F42F9E34F9D8E0CF633FD55422FBAD0A0ADFAFD06524E82DC143): ArkUI template, a template for the ArkUI janky frame scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/YO3kCG2EQqesVDZTZGtuKw/en-us_image_0000002500910710.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BEB5C91E4EEE06B9752529DA2862967ECCA8AF732F94F6F7420C466AD42FE56): Energy template, a template for the energy consumption diagnosis scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/knlLy00OTVS3DWzv1O2ANg/en-us_image_0000002532670633.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1FA727E2918229A02A30B19A4F35AA1375726E0BFDA9B475B14871BB31F490D): ArkWeb template, a template for the ArkWeb frame loss scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/v7BiBWv1SQi0f1BX5SaFug/en-us_image_0000002501070552.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87E10CEBABB548564F0C2BD21037F620669368AB96820943045F4FD9A56C6466): Network template, a template for the network diagnosis scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/oFZp4GqCQbWkyWadL5NzWQ/en-us_image_0000002500910722.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3195C466B9AA1DADCA8A4D8B5EA1D7339E53AA192CEA1CF0CEE5FF4D7FFAE9E): Concurrency template, a template for the scenario where multiple processes or threads are executing simultaneously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Be4TsNE_THexPZ7HuHqUGA/en-us_image_0000002532750579.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC1D870B9D40FC36CBA37F84173D171A53225947AB5919FD80F4FE0CE0E0E2C5): Time template, a template for the function execution time scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/XDvnE-H3SS68cChVoqH14Q/en-us_image_0000002532670635.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9C08585B490E5D964D88AACC6AE9E8CDBBAB92F3A9355CAA855FDD32310F563): CPU template, a template for the CPU scheduling scenario.

To create a session, select a template and click **Create Session**.

You can also click **Open File** to import data. Currently, .insight, .htrace, .ftrace, .heapsnapshot, .rawheap, .sys, .perfdata, .data, .nas (files containing native allocation data), and .txt (files containing native allocation data) files can be imported.

To configure the cache path for DevEco Profiler, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/I6EeBI1VR2WMnUY-WcbZ8Q/en-us_image_0000002500910712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=044D03B1E3AB0DA64870D671CAC0582B577BE38662407292820044F1D934BA12 "Click to enlarge") in the upper left corner and follow the onscreen instructions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/M8so4lZYSlqtOLsdhwOMjw/en-us_image_0000002532750585.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062157Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E94CD92DB034D9F7F83759B0E84C60F460D2B5105AC818549A29F0A922F6BC3)
