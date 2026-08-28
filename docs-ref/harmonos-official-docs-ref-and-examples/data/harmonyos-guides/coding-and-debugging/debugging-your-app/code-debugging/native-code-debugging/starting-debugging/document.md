# Starting Debugging

Native code debugging depends on the LLDB. For details about this debugger, see [LLDB](../../../../../ndk-development/debugging-and-profiling/lldb-debugger/document.md).

Before starting debugging, choose **Run** > **Edit Configurations** to open the **Debug Configurations** page. On the **Debugger** tab, set **Debug type** to **Dual (ArkTS/JS + Native)**, **Native**, or **Detect Automatically**. Set the code type for debugging to C/C++.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/KdHKrtEkS5aFG4ZEQMdkdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E72C3C31FDF2D80D694B2D4CFD99ABC66FC93F35CBBFA1D34BCABCC94DBA78B)

-   If **Debug type** is **Detect Automatically**, the debugger determines the debugging type based on the code type detected.

-   During debugging, enabling compiler optimization – by adding optimization options – or using the [release build mode](../../../../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916) – can lead to more efficient code execution, as the compiler modifies the assembly instructions. However, this optimization can complicate the mapping back to the original source code, potentially causing debugging issues such as unexpected deletion of local variable information or incorrect line breakpoints. To prevent such optimization-related exceptions during debugging, you are advised to disable optimization or use the debug build mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/TxWGpD85Tt-iy67IUrJIWA/en-us_image_0000002501070182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3761E6850ECC5881655834F909F476C5F845CFC6C8D6296B53F4CC908DC70B0B)

On the **Debugger** tab, you can customize the following configurations:

-   **Whether to display static/global variables in the Variables pane during debugging**: Check or uncheck **Show static/global variables in the Variables Pane**.
-   **Symbol directories**: On the **Symbol Directories** tab, click **+** to add a symbol directory (.so file with debugging information). For example, you can generate a .so library with debugging information, run the library without debugging information on the device, and debug the .so library by adding the path of the .so library with debugging information here.
-   **LLDB commands**: You can set LLDB commands on the **LLDB Startup Commands** and **LLDB Post Attach Commands** tabs. The commands set on the **LLDB Startup Commands** tab are executed immediately after the LLDB is started, and the commands set on the **LLDB Post Attach Commands** tab are executed after the LLDB is successfully attached to a process.
    

After the configuration is complete, you can start native code debugging in debug or attach mode. For details, see [Starting Debugging in debug Mode](../../arkts-code-debugging/starting-and-debugging-an-app-atomic-service/document.md) or [Starting Debugging in attach Mode](../../arkts-code-debugging/debugging-an-app-atomic-service-in-running/document.md).
