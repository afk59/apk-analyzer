# Setting Execution Points

With the **Set Execution Point to Cursor** feature, you can jump to any line of code in the editor during a debugging session and set an execution point at that location, bypassing all the code between the current location and the target location.

This feature applies to linear and non-linear execution paths, used for interrupting and skipping loops, or for selecting another branch in if-else statements or switch-case statements. For example, if you want to check another branch without restarting the debugging session, you can use this feature.

#### Procedure

1.  Drag the current execution pointer (the orange arrow representing the current running position) to the desired line of code.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/v61Td6dWRrmjuqfxIU-BWg/en-us_image_0000002501069766.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEF51402A5AB8C8F016D4418D735FA38878A06A78A04A857DD270896F6ACBAF5)
    
2.  Right-click the line where you want to set the execution point, and select **Set Execution Point to Cursor** from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/2Nn8gAxuQ-2ixRrXXPsY_w/en-us_image_0000002500909918.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16B8A7649777E7090E1658D9FDBAB7688DC8D4BDBFCC1905B0532C7A10175D50)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/qiAsWoY7SAuipWTUiXNCoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFF297DBCA82370CB7DD95C83FECC38A8D7F4F219C623B511313D4CC39FE6BDF)

With **Set Execution Point to Cursor**, only the value of the program counter is changed, and the values of other registers are not modified, which may lead to unpredictable errors, such as:

-   If the line where a variable is initialized is skipped, the app will fetch the value from the stack/register, which may cause a segmentation fault.
-   If the executable code has been optimized by the compiler, you may get an unpredictable result, or it may not be possible to move the execution point.

There may be other unexpected issues, such as variable value confusion and abnormal stack information.
