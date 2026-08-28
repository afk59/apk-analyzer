# Checking Variables

During debugging, you can view global/static variables, register variables, and local variables in **Variables**.

#### Displaying Global/Static Variables

To display global/static variables in the **Variables** pane during the debugging process, choose **Edit Configurations** and check **Show static/global variables in the Variables Pane**.

#### Simplify STL

On the menu bar, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Debugger** > **C++ Debugger**. Select **Display STL variables as visualization in the Variables Pane** to display simplified STL variable values. To display variables in their original structure, leave **Display STL variables as visualization in the Variables Pane** unselected.

#### Observing a Variable

Enter an expression in the **Watches** list and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4KC11UtuQOydRoo48ufnKQ/en-us_image_0000002532670651.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7484D0CDE464FD92CA467EFFD721F6767E403405D44DBEC590F323B7C9D24E9D) **Add to Watches**, or right-click a variable and choose **Add to Watches** from the shortcut menu and add an expression. Then, the value of the expression will be calculated each time the app is paused.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/oZCmHpoPSAOZ-nZXkFtOBA/en-us_image_0000002501070582.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E765A5003F703ADCE80A8188B3231ED0CFA2CEBC6ADF7029BF530D4395D9EB39)

#### Evaluating an Expression

Click the **Evaluate Expression** button or enter an expression in **Expression** on the **Evaluate** dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/r3WoOWF0SPehdRvPWfF6mg/en-us_image_0000002532750601.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C050C4BE4270E9692A197FEE10443EE2B72C060C305BAE377A7C5C49837E00CC)

#### Viewing the Hexadecimal View

On the **Variables** tab, right-click anywhere and choose **Show As Hex Values** from the shortcut menu. The integer variables on the page will be displayed in hexadecimal format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/HYh7b5WpQk-K2YDAysMexw/en-us_image_0000002500910738.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=645DF5C93EE72EC52537C3C93EA3ABD7DF314CFAEB5CBA117CE034EFD2599E37)

#### Viewing Function Return Values

After you use **Step Out** to step out of a function, the **ReturnValues** section in the variable list displays the return value of the stepped-out function.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/uyi02W8rSgySa-q6LSMCRg/en-us_image_0000002501070580.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F953ACB6AD8FD8D66D8FB5715EF8E75BF5109B3D8F3DE8083FCD9B1EAAC65D79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/669Ihw_9QUKx7Ws3y85d3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DAD71EA8EDEB0A77D5A5746C1E18DD0760316048B325EC5A643FEAA064FEC76)

-   Data structures longer than 64 bits cannot be viewed.
-   Return values of the reference type cannot be viewed.
-   When a breakpoint exists at the location where the Step Out feature returns, the function return value cannot be viewed.

#### More Information

For variables of the specific type, there is also support for features such as bitmap preview and viewing long strings.

-   **View Bitmap**: Click to preview bitmaps during debugging.

-   **View**: Click to expand a long string to view it in full.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/M-hwbmB9R6OeTQOYAd7B_A/en-us_image_0000002532750603.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68D46B99E44FF9A8880D58942807ABB2052ACA3A4BC25DBD7AA0C1C3A3460783)
