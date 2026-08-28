# Vibrator Overview

The **vibrator** module extends the vibrator service via maximizing utilization of vibrator hardware capabilities. By innovatively integrating vibration and interaction, the module takes user interaction efficiency and usability to the next level.

#### Working Principles

The vibrator is a Misc device that consists of four modules: Vibrator API, Vibrator Framework, Vibrator Service, and HDF layer.

**Figure 1** Vibrator in Misc devices

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/sa5ogoRLSfO_-sfzXCPzRA/en-us_image_0000002537765112.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=502131831766BCA4AB4D92C43C598848132C48E2783F51A8599095AECFE58F24)

-   Vibrator API: provides basic vibrator APIs, including the APIs for obtaining the vibrator list, querying the vibrator by effect, and triggering and stopping vibration.
    
-   Vibrator framework: manages the framework layer of the vibrator and communicates with the Misc Device Service.
    
-   Misc device service: manages services of controllers.
    
-   HDF layer: adapts to different devices.
    

#### Constraints

When using a vibrator, you must declare the **ohos.permission.VIBRATE** permission before you can control the vibration effect.
