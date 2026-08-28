# Debugging an App/Atomic Service in Running

You can also attach the debugger to an app that is already running for debugging.

The difference between **Debug** and **Attach Debugger to Process** is that the latter allows you to debug an app/atomic service in running or start an app/atomic service installed on the device for debugging. **Debug** allows you to start and debug an app/atomic service in sequence.

#### Prerequisites

The attached app on the device is running code that matches the local source, with source maps pre-built for debugging.

#### Constraints

The attach operation does not support the following cases:

-   There is no source code locally.
-   The local bundle name does not match the bundle name of the app to be attached to. If this occurs, the message "The selected process does not match the bundle name of the current project!" will be displayed, but the debugging process will not be blocked.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/vLgKkevORqSZB9oolJb5oQ/en-us_image_0000002500910360.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28B902562A890A8C6C442AEA1210254D540561DF33CFF934501D4973380AE36D)
    

#### Procedure

1.  On the toolbar, select the device to be debugged and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/itDVZcv1T6KtgqhtL-odvA/en-us_image_0000002500910364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41D14D5A48285F1647913F9AF39584ADAB0EB18B45DE3B1C2F05AD76A66A70CF) **Attach Debugger to Process**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/lNuJjdJ4Q5SNcWncIst3FA/en-us_image_0000002500910362.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E94D4114344EC72029CF7B2947619707A2B2F01B20B163382D9D333F358384A)
    
2.  Select the app to be debugged. If the bundle name of the app is different from that of the current project, select **Show all processes**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/DJVxh5n2RNenYBJBRgqfIg/en-us_image_0000002500910366.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1BE3ED0339250EFC230A925FA712D00424567D2AEAB1BF72E67A6EFAA15C9A2)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/QEkn3S6xRq-UJe7yjI0qYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAFFF75E665271E72BA7FE4DE501EDB3EE671F8E045C6D6A6A85FB08441AB0FB)
    
    In general, attach debugging only supports apps signed with a debug certificate. Since DevEco Studio 6.0.2 Beta1, apps on PCs and 2-in-1 devices can also be attached and debugged if they are signed with a release certificate and have been granted the **ohos.permission.kernel.ALLOW\_DEBUG** permission.
    
3.  Select the debugger settings to be used, or use the default settings.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/mxeYPta3R46_3KZt3KjFcA/en-us_image_0000002500910354.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D2E693D55780FB44062A2E7359F15A643C545C3ECD70CA7DF31B5A41B8A39EC)
    
4.  Select the debug type. The debug type can be changed only on the **Run/Debug Configurations** page. If you select configured debugger settings, the debug type cannot be changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/57sNYY_QTsuOCMgKzbsa6w/en-us_image_0000002532670271.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D83AF0E3D5A6153A8ECECA25D5C27DDA89D9BD2121412CA6518345ED75DEFD3)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/B0VdVVquQguNYdTPhfme7w/en-us_image_0000002532670275.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7485248A18B45DBC51C4D1E493001791246FD395A588FDDCDFB31896B3E7BA1B)
    
5.  Click **OK** to start debugging.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/307RKWrjT-S1rR0oohLc7g/en-us_image_0000002500910358.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17A186E5A691545AF81AF970EE44D979A4DD9FD8A72581064E6F1DFBE496B5E1)
