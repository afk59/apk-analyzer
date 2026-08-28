# Using Reverse Debugging

In addition to basic debugging capabilities, DevEco Studio provides reverse debugging to help you better understand code and quickly locate faults in C/C++ development.

Reverse debugging, also called time travel debugging, allows you to roll back to historical lines and breakpoints during debugging to view historical debugging information of threads, stacks, and variables. DevEco Studio supports the following debugging operations:

-   Enter/Exit the reverse debugging mode.
-   Reversely step over to a historical line.
-   Reversely resume execution to a historical breakpoint.
-   View the values of global, static, and local variables at the record points of the app execution history.

#### Prerequisites

Before you start reverse debugging, ensure that reverse debugging is enabled as follows: choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build,Execution,Deployment** > **Debugger** > **C++ Debugger**, and select **Enable time travel debug**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/1bh4biRuTLGcUzOyoq-KBg/en-us_image_0000002500909914.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CBE9FC8822403233E5790539237E9125861E3AF9918B12BF203372E2127548D "Click to enlarge")

#### Procedure

1.  Set breakpoints and enter the debugging mode.
2.  Click the reverse debugging buttons in **Debugger** to perform reverse debugging.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/yU_f7InfTsewLs8-UTqjWg/en-us_image_0000002501069762.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=027C6413E7894F8B195B93C5D2E36E386774D21132E0EA081D1961FF299E25EF)
    
    To view historical debugging information, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Xkc76d0eR7WqlSr2OL87cg/en-us_image_0000002532749785.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D315B5A0C0AD326F101EB91C4240A2F74F41C8ECE0F5095898ECC2626C668337) **Open Time Travel Debug** to enter the reverse debugging mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/zq26bXBPRc-DN72XyT0ecg/en-us_image_0000002501069768.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57553CCB2B380AB7D43CD5680A31168A47896EE78CF04E20397E525DAA721E87)
    
    You can use:
    
    -   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/1qvxApYkSUuI_aK2GAwVrw/en-us_image_0000002532749791.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=685A6B24A6A27D7C9134C0A834C9ECD0F3FBF1F99F5C23E88A80B271B7BC6D14) to exit the reverse debugging mode.
    -   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/l59PrEm-QTy5q6qyYk4E8Q/en-us_image_0000002532669833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83A36415F7811235C35DB7FE8FCBAAB24F93FC15276FAF565F36056D27F71DD1) to go to the next historical breakpoint from the current highlighted line and display the breakpoint information.
    -   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/zMK0lZzkQJacjGoGxiSLAw/en-us_image_0000002532669829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6369F3776AA18B392973E4F595674D37528E5EC555753912A2A834DAA70E752B) to go to the previous historical breakpoint from the current highlighted line and display the breakpoint information.
    -   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/YGsAkdNwQuycw1ZEt6KntQ/en-us_image_0000002501069764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19DB5D4C3E666D4647F4D4AAE8E75F36F0F6E0AFA91B5F98C3FD0F1BCDEB611F) to go to the next historical line from the current highlighted line and display the code information.
    -   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/IX8nO7pYRgayfmcD-dJMBQ/en-us_image_0000002532669837.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=878DF7D49EECE10E92ED63B81B97DC76DD238081C5E0E8B05E2334D6A7F6B59E) to go to the previous historical line from the current highlighted line and display the code information.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/2J1K8JlyShinL75qVsx2SQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B992646693A4EDBB3A4902858A0C17052973E370D5383AAA2EBE7DDD3C3A079E)

For the features that cannot be used in reverse debugging mode, a message will be displayed based on your behavior.
