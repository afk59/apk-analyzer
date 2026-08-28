# Using Breakpoints

DevEco Studio for ArkTS debugging supports line breakpoints and log breakpoints, which trigger different operations.

#### Setting a Line Breakpoint

A link breakpoint, as the most common type of breakpoints, pauses the execution of an app at a specified line of code for debugging purposes. During the pause, you can check variables, evaluate expressions, and execute the code line by line to identify runtime errors.

To add a line breakpoint, perform the following steps:

1.  Locate the line of code that you want to pause the execution.
2.  Click the left sideline of the code line, or move the cursor to the line and press **Ctrl**+**F8** (**Command**+**F8** for macOS).
    
    After a breakpoint is set, a red dot is displayed next to the code line, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/qzNMN1nBSjarQ93wjv6aIQ/en-us_image_0000002532750095.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F69674EC453EAD79CED7455E33F769FC566D1F9DB209ECBD96EA37E14A4F150)
    
    You can right-click the red dot and choose **Condition** from the shortcut menu to set a conditional breakpoint. Then, the app will be paused only when the specified condition is met.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/pagZTdhcQ8iXFBoa6ZLFag/en-us_image_0000002500910230.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A0FDE90295B33083F574308E4E89ED23D8FBDDF64EBE1880FFC072F5F0BBAAF)
    
3.  Start debugging. You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Th0Eh21cSy6igUSS6H3_ww/en-us_image_0000002500910224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3A62979588B986039E71DB6FA4117CBBFA4517C1C6C668BEBE731D84C70B0AE) **Debug** to debug an app that has not started or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/c2TywiIKRPyyjUaatZmIEw/en-us_image_0000002532670143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2862784B579BF94E3A6C4CC417DEECFECA1081C7059C8B419589EDC7F12B0AA3) **Attach Debugger to Process** to debug an app that is already running.
    
    When the app runs to the breakpoint, it pauses at the code, which is highlighted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/VXn7GzkuTMm5uV32WoOPYQ/en-us_image_0000002500910228.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A9C27D0FF1E112526B25F3DEBC3E84A3527995AB9F8F3FC3728F36C8CDC59CF)
    

#### Setting a Log Breakpoint

To print log information in **Console** when a breakpoint is hit, configure the following for the breakpoint on the [Breakpoints](#section168791742202819) page:

-   Select **"Breakpoint hit" message** to print "Breakpoint reached" when the breakpoint is hit.
-   Select **Stack trace** to print the stack of the thread when the breakpoint is hit.
-   Select **Evaluate and log** and add an expression to print the value of the expression when the breakpoint is hit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/5kvqLwO1R8iqxzokjiVZNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21208377D94B43EF197F7128B9E1E483273F3928DC8B9AF97220BC0CD3D35F09)

If **Enabled** is not selected, log information will not be printed for that breakpoint. If **Enabled** is selected and **Suspend execution** is not selected, log information will be printed. If **Enabled** is selected and **Condition** is set, log information will not be printed if the specified condition is not met.

#### Setting a Temporary Breakpoint

To set a one-time breakpoint, select **Remove once hit** for the breakpoint on the [Breakpoints](#section168791742202819) page. Then, the breakpoint will be removed after it is hit.

#### Setting a Function Breakpoint

Since DevEco Studio 6.0.0 Beta2, function breakpoints can be set in ArkTS code.

A function breakpoint, also called a method breakpoint or a symbolic breakpoint, pauses the execution when a function is called. A function name is set as the condition for hitting the breakpoint.

On the [Breakpoints](#section168791742202819) page, click **+** and select **ArkTS Symbolic Breakpoints**. In the dialog box displayed, enter the function name, and click **OK** to set a function breakpoint.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/eki20unSTB2Dfr5ZiEAC5w/en-us_image_0000002501070066.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38E48792BDBDA5B8F117E7618CB55FF871D661090CF833D7649C0B9C8DD2E31D)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/0-GNUC-AROSe8zRQWziKjw/en-us_image_0000002532670139.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FA2CFEFD69B144100170168A45B3F5128E1C2DA6B5458B6CF52DC7D0FF91E05)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/SvoleLSkSxCC7qYTrLLXDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B05E8AF8DEE8EB732B9449B58EF502AD99E4F18C9DDF8B14C53BCDE2246F17C)

If a C++ breakpoint is hit during debugging in DevEco Studio 6.0.1 Release or earlier, ArkTS function breakpoints cannot be added or removed. In DevEco Studio 6.0.2 Beta1 or later, ArkTS function breakpoints can be added or removed.

#### Setting an Exception Breakpoint

An exception breakpoint pauses the execution of an app when an exception is thrown.

On the [Breakpoints](#section168791742202819) page, select **ArkTS/Js Exception Breakpoints** to enable exception breakpoints.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/dOmnCpupRKSmfdIuwlUaag/en-us_image_0000002501070062.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9227B9D220DCA030390F63D4A1A3F65F62F8AEA8BB2E10E51156682D2E96752)

When an exception is thrown during the debugging process, the exception is highlighted and ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/hUGRZYDJSr2SZ8LmUlLypQ/en-us_image_0000002532750099.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B453515FC65E5BA5B72AFFC30583648565605A30AB15F31731DC2AAEB0C07F30) is displayed on the left of the code. You can see the current frames, variables, and error information on the page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/a0x_IU6pQ4-LGw_pwTFyyA/en-us_image_0000002501070064.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7735EB9FB41DE7A198593E4F58958769B3C9A90ACD5F928CB37D42224F74F69)

#### Managing Breakpoints

Right-click the red dot of a breakpoint and choose **More**, or press **Ctrl+Shift+F8** (**Shift+Command+F8** for macOS) to manage breakpoints.

Alternatively, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/MC4uS_sISNam3fXAIPJrOg/en-us_image_0000002532670141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B6569F47BAA09252A2478669D8450C95FDEFD9F81CA87EA3E5504E6DD2050B4) **View Breakpoints** in the **Debug** window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/x8uJAWBJS2Gqmp5hsrA9aA/en-us_image_0000002532750097.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=000F4820684D072582DBF168B4EBF3A6AE4D06E1005F22FA923526DC45A47BFB)
