# Debug Tool Window

There are three tab pages on the **Debug** page: **entry**, **entry(PandaDebugger)**, and **entry(Native)**.

The **entry** tab page displays the HAP push and installation process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/5AbyRyo6ShyK-SP2yWJMUg/en-us_image_0000002501070344.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48293DF293347C1FB0C8C1ED4D778E72D55517F1D9088F1DC190B8BEE1C7F862)

The second tab **entry(PandaDebugger)** and the third tab **entry(Native)** are debuggers. The **entry(Native)** is started only when native debugging is involved. The debugger contains two pages, **[Debugger](#section1437520119316)** and **[Console](#section327153017314)**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/TaUaBn8SQD68eUzAWJgRUQ/en-us_image_0000002501070350.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB7A66451944AD9A40AD5FF9A777F183ACC2D7BA2568D2D08631AD85C4AB9D7C)

#### Debugger Page

The **Debugger** page provides two panes:

-   Left **Frames** pane: displays the location of the code referenced by the current code when a breakpoint is hit during app debugging.
-   Right **Variables** pane: displays the current variables.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/DkOCne1fT8yyihcANH8-VA/en-us_image_0000002501070314.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD7407CFC8074EE88D7C0F02B47DB0DC1F91C03A4137AF41A6F0E241164B1422)

The following describes the buttons on the **Debugger** page.

**Table 1** Debugger buttons
| 
Button

 | 

Name

 | 

Shortcut Keys

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/RJ-kLmsFQ8uAsi_CntMtJg/en-us_image_0000002501070358.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17AA90236AF207A3238F952CD0EA422621EF2525423D3E55C5672A7430E9EF4E)

 | 

Resume Program

 | 

**F9** (**Option+Command+R** for macOS)

 | 

Resumes execution.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/QxDk6PAWTZaIjXGjGny-1w/en-us_image_0000002500910496.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F84FFBB1961D036F7D943F13FA7C4E0432FB9813265FD4D7642F318F7571ED2F)

 | 

Step Over

 | 

**F8**

 | 

Proceeds to the next line of code without entering any function on that line. If the line contains a function, the debugger will execute the entire function as a step.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/mYDMDWm4SXeBKfrK4q5CqA/en-us_image_0000002532670401.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49EACAC097FB2C9897CA1A3FB40A0F1DD88DADD3D9887D86B2141989D382CB50)

 | 

Step Into

 | 

**F7**

 | 

Executes code one line at a time. If the current line contains a function, the debugger will enter that function and continue single-stepping within it.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XOfSKxXlTyys85B7nYWjgQ/en-us_image_0000002532670431.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F58C66D7993E11F4A8762F63321CB2D273E13B478549FBD3A1868CDD8CA5693A)

 | 

Force Step Into

 | 

**Alt+Shift+F7** (**Option+Shift+F7** for macOS)

 | 

Forcibly steps into functions during step-by-step debugging.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jwBJiH38RnObuTLDlT-eCw/en-us_image_0000002501070324.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD978668A9F13BBB82BA8F84AD4976BC52649EA53F4D3290D720273913FA785A)

 | 

Step Out

 | 

**Shift+F8**

 | 

Executes the rest of the current function and then returns to the calling function.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/1UlqD87NRU6FkCerIJHUkw/en-us_image_0000002500910478.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D3E9382E5B332651BAFEC5300DB3977F161A6DA99CE4EE873D069EFE2A4771F)

 | 

Stop

 | 

**Ctrl+F2** (**Command+F2** for macOS)

 | 

Stops debugging.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/OgKcDDkiTqKhtCmTeGo5vg/en-us_image_0000002532670391.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19144C2CB1E76BABCA565CA2B49B1BE9B92E1FB83858C0CB0B3E4E27C150A612)

 | 

Run To Cursor

 | 

**Alt+F9** (**Option+F9** for macOS)

 | 

Continues the execution until it reaches the location of the cursor.

 |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/BSlKHy_OR_Wlnda_NyyQOw/en-us_image_0000002532670417.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=430CA976FA9393A2760B13903C5EE46381D69C653479B959B91D2BD5D491C7DE)

 | 

JSVM Debug Port

 | 

None

 | 

Forwards JSVM debugging requests. After the forwarding, you can perform [JSVM-API Debugging](../../../../ndk-development/code-development/using-jsvm-api/typical-jsvm-api-use-cases/jsvm-api-debugging/document.md) in DevTools via the browser.

NOTE:

This button is available only in the Native debugger.

 |

## Resume Program

To resume execution of the app, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/sBGb-qIuTMO9QJpEWR7QXQ/en-us_image_0000002500910500.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B60FAD839231477ED7D48813F3ED1D04432C9C72BF70096BC5583E15C82AB5E9) **Resume Program**. If a subsequent breakpoint is encountered, the debugger pauses and displays the corresponding **Frames** and **Variables**. If no breakpoints remain, the app runs normally and the debug information disappears.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/NpKdoiAfTUSuQWJnnadqkw/en-us_image_0000002532670383.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06C967FFBC44EC5EDF29CACDB142AE642215D0A9305A17C858E842D9DBF2D8EF)

## Pause Program

To pause the execution of the app, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/SRcjNQ6VQUqBTTnf-lnzig/en-us_image_0000002532750361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D389761DE2222EB83463EC94EDC1454559936DB7AD613230A9FD0B4165960E8E) **Pause Program**.

## Step Over

To go to the next line of code, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/xnna4HGKR4u75RsRxBcJ9g/en-us_image_0000002532670409.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07DD21600B31EDB8B9559DDD3D9ED3D28EA25F9DBB7F8D2A4E8A40AD56D2D561) **Step Over**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/lkGYjZuiRQiIHTtMAomqVw/en-us_image_0000002532670413.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0635E0F40F928AD4811C9EB6DF2E9878EACDD15970C7667879B379427AFD924)

## Step Into

To step into a function from the current code, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/i0g6MbbSQguX861UHC8uBQ/en-us_image_0000002501070356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21D5353F70A4B3CEACCAC9AF2052FC35EF165AD68B0BBDF8247B8CC610F90B3E) **Step Into**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/pbH4S0SjQSafcQSpV6B9uA/en-us_image_0000002501070320.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CF22AFC8CD8DD7EFB817CDF4580AD794BF926185187AF158C87CF36ED22E315)

For example, step into **add()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/WYuuriLsReCfPUYkSBicog/en-us_image_0000002501070332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F9E256AF640CA17F49ACE5494AB14F30F2ACBB993F49C38BD383498ADA3257F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/2GxbahAGR4y3XsY3_FYC0w/en-us_image_0000002532670389.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B32C2506AB1330B90079D03E15A862A441FE955AC0EAB4BB4D3E29E226BBFDAC)

## Step Out

To step out of the current function to the calling function, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/hKYgqFR1QTS6L1nu0cklag/en-us_image_0000002532670395.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=614831CB535371EEB6B4E15A1B8E3B3DEE1DAD4A50EDF73840986E5E7A116812) **Step Out**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/RsByV4QMTqyd2kO15GhkWw/en-us_image_0000002501070334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB41069598BE5FC4AEF2AB1F80FE215D2D42629A94C9047216CE3B415166148D)

## Run to Cursor

To stop execution at the cursor, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/VADAMytgT3ehPeMKB8DbZg/en-us_image_0000002532750353.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8D0E375546A56B3F4090C1BB1734803C41ACD59302DCB6A08136FC57E6D9010) **Run to Cursor**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/CkvDeARtRXKiLHORFwy7Mw/en-us_image_0000002500910482.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4604556ECF12776EE51068E25B48FC0864C41E4612860D8C731F06B591E8216)

## JSVM Debug Port

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/cjHk0N1lQbeGNaOvsIjU7w/en-us_image_0000002532670423.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB5CBB9AE70A86ACC9F7C5797EEC85CA2CE9D4E12B53D5978F0AD9CFA225ABBF) **JSVM Debug Port**. The page for entering the forwarding port is displayed. Enter the port number and click **OK**. After the forwarding is successful, a dialog box is displayed. Open the corresponding URL to debug the JS code. For details about how to debug the JS code started by C++, see [JSVM-API Debugging](../../../../ndk-development/code-development/using-jsvm-api/typical-jsvm-api-use-cases/jsvm-api-debugging/document.md).

This feature is supported since DevEco Studio 5.1.0 Release.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/6pmQ-k2dQJi_ozJeK-QbzQ/en-us_image_0000002532670419.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1ADD189A7DAD1A89E1F5F18435F3A3A164D1B7B7B652A3E530A9CF0A284A71D5)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/kLUnJ1hJRaK7dAEim02pCA/en-us_image_0000002532670385.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=787C9C0A9FBE017EF7C04F8FFED8346421AFBA1EB783E4EADFDD4DAB64CD8EE3)

#### Console Page

The **Console** page displays loaded .ets or .js files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/VPCv8jZCSueBwxjmdmnpCg/en-us_image_0000002532670403.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03C2A6586E7CBE9003F1D6BA35EC2F1CBC5A3D93FF4F750526138593A11F4F23)
