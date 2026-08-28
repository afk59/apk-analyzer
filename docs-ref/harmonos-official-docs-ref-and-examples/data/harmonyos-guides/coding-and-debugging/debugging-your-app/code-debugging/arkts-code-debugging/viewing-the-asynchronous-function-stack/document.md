# Viewing the Asynchronous Function Stack

Since DevEco Studio 5.1.1 Beta1, you can enable the asynchronous stack tracing feature and set the asynchronous call chain depth to trace the sequence of asynchronous function calls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/PP7Gk0D7S9-z5nx9XlwZaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FACBD83EDA6876E7911BAEF9C40A14D22043F1249E2841DB4382562FA24FEF20)

-   The **Async Stack Traces** feature is a global setting. Once enabled, it takes effect for all projects.
-   After modifying **Async Stack Traces** or **Async call chain depth**, you need to restart debugging or start a new debugging session for the changes to take effect.
-   The asynchronous stack of the **setTimeout** function does not take effect.
-   The asynchronous stack does not display the variable list.

1.  Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Debugger** > **Async Stack Traces**.
    
    -   Check **Enable async stack traces**.
    -   Set **Async call chain depth** to a value greater than 0 to display the corresponding call chain layers during stack debugging.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/zVKKs0rHQgWmZDUELOB2qg/en-us_image_0000002532750389.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E296BCCC383B434F8F2134F095F14CEFC4CB82E3D50E7EB7099ACD327CAE7525)
    
2.  Set breakpoints in the asynchronous call chain and start debugging. After a breakpoint is hit, the stack list will display the corresponding call layers. If the actual number of call layers is less than the configured **Async call chain depth**, only the actual layers will be shown. Each asynchronous call in the chain is delimited by **Async call from**, followed by the calling function.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/DY2ziNinT8iG1B4hpT0qtw/en-us_image_0000002501070366.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E19A25940A579F0D5072BA51B2AF6E5F9131174DBBB6D8A40E21DDC4262C390F)
