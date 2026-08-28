# Using Breakpoints

To view or modify breakpoints, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/J5tNK3ooTIi9Nl5Nfsj93Q/en-us_image_0000002532749945.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0C7ADA1CBFA4604AFE084F129A50E0A339FB3FAB5EE5F4748BBB4C7E974EC06) **View Breakpoints**. On the page displayed, you can:

-   Check **Enabled** to enable the breakpoint.
-   Check **Suspend execution** to pause the app execution at the breakpoint.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/6w_LrYkUSdOByrehILxSDg/en-us_image_0000002532749937.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87D0910FFF3F6F775AA86370C161EE25410AD922DA53C8436E2A7D891378F1F3)

#### Setting a Conditional Breakpoint

To set a conditional breakpoint, select **Condition** for the breakpoint and set the condition. Then, the app will be paused at the breakpoint when the specified condition is met.

#### Setting a Log Breakpoint

To print log information in **Console** when a breakpoint is hit:

-   Select **"Breakpoint hit" message** to print "Breakpoint reached " when the breakpoint is hit.
-   Select **Stack trace** to print the stack of the thread when the breakpoint is hit.
-   Select **Evaluate and log** and add an expression to print the value of the expression when the breakpoint is hit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/IreIeAw0R2GSSAmEpCpYmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40C4D7C4317391C26C55EB96AB9D4530E0849A325DD786224C108AEDBC473EDF)

If **Enabled** is not selected, log information will not be printed for that breakpoint. If **Enabled** is selected and **Suspend execution** is not selected, log information will be printed. If **Enabled** is selected and **Condition** is set, log information will not be printed if the specified condition is not met.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/e-i5RPzbQReOsjkGkToEMg/en-us_image_0000002500910072.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D10ED20856F8F2F8C0ACA482B7A1B145671C13FE869E1A9D774D7AA18E7CFC4)

#### Setting a Temporary Breakpoint

To set a one-time breakpoint, select **Remove once hit** for the breakpoint. Then, the breakpoint will be removed after it is hit.

#### Setting a Function breakpoint

A function breakpoint, also called a method breakpoint or a symbolic breakpoint, pauses execution when a function is called. A function name is set as the condition for hitting the breakpoint.

To set a function breakpoint, click **+** and select **Cpp Symbolic Breakpoints**. In the dialog box displayed, enter the function name and module name (the module name is optional), and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/4N_Y4q_vSnKvu7rUKjiwJQ/en-us_image_0000002532669991.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDC1992CF1C11EF7C18331D5E0EB78029B123E4A230E7656AC2B9EC6678D7975)

#### Setting an Exception Breakpoint

An exception breakpoint pauses the execution at the code when an exception is thrown or captured.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kQeEI92xQrynvpKYjMGXzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=324E42693A80765A99A13FCDB03E4D12E209099850BF11AF998D3919E402CED6)

System exceptions, such as SIGSEGV, will be captured and terminate the process by default.

To set an exception breakpoint, select **Any exception** under **Cpp Exception Breakpoints**, and check **Enabled** for the breakpoint.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/EjktX05gQ_2BRP_A-IUCeA/en-us_image_0000002532669989.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2B6848D200A366D262AB885BECC3FEC16EE4E48C8095161DD28F910BBDCB3D6)

#### Setting a Data breakpoint

Three types of data breakpoints are supported: break on read, break on write, or break on read/write.

To set a data breakpoint, right-click a variable in **Variables** and choose **Break on Read Access**, **Break on Write Access**, or **Break on Any Access** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/dRM9HydhRoGBVkbYXfvNZg/en-us_image_0000002500910070.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42174B9AB17AC8AD779DE42465ACE9720DC3C6385B78BB376C8FEDBD092DDEC2)

You can view and modify breakpoints on the **Breakpoints** page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/yr9TgDKDToGPyZgwf7pfgw/en-us_image_0000002532669987.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37E88DBBB9E14A0D507B0CCCFDDF57D44464B7422E42606CD3D89FA2279C1C7F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/-xVrhprzSLepjo_xbBQ-rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD90501AC1CCAA9CDB9F3C7B4BB35A441EF8AACB9B266E301CEBC21111B607AC)

1.  The specific types of data breakpoints that can be set vary depending on the hardware in use. The size of the variable is also restricted by the hardware.
2.  Due to hardware limits, a maximum of two data breakpoints can be set.
3.  Data breakpoints set for local variables must be manually deleted when they get out of scope. Otherwise, the process will be interrupted when the variable address is reused.
