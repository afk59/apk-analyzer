# Using Multi-Process Debugging

On some devices, a UIAbility can run and be debugged as an independent process. For details, see [Process Model](../../../../../application-framework/ability-kit/stage-model-development/process-model/document.md#other-process-types). The following describes how to debug a UIAbility.

#### Configuration Before Building Your App

1.  Create an ability that inherits **AbilityStage**, which will serve as the entry point for the independent process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/R5wpLfvGRoCj-dT-BuwTog/en-us_image_0000002532749903.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2498A3DF0EC786662DE11CEEFDDEEE19DCEA25DEF51A6CFFE2D212B3324A0B1)
    
2.  Right-click the **ets** directory and create any additional UIAbilities that need to be started as independent processes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/HzjJgX5WRfK7kS7QcXse5w/en-us_image_0000002532669947.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9868562D07873ED275EB465257B06CEED6F24A31C6F99E52920844DCE4382EF "Click to enlarge")
    
3.  Modify the **module.json5** configuration file and add the independent process entry and the **isolationProcess** configuration item.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/f5cijDBTSFun1ER19lx67g/en-us_image_0000002532749893.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9ACF61FDEDF76366A5E9AF9D31E320EC92A52E3B9D2E1AF39565225ADD2B287)
    

#### Debugging Code

1.  Write the code for redirecting to the UIAbility.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/jEacvuFNQH-nG4nnjG3-PA/en-us_image_0000002532749897.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F4A0B4C42C1FB094EAAE41681B71C5763BFF1C07C2C870F7BC9904D91852B6F)
    
2.  Set a breakpoint in the UIAbility or at the entry of the independent process, and start debugging.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/YxR_u_QcSrmAhby0ZlemHQ/en-us_image_0000002500910032.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77C7A3DBBD4F8D59CE52773F3F5AC7946B1BEF3D24C2FE8ABB5E1A867590BB96)
    
    When you navigate to a UIAbility that is started as an independent process, a new debugging session window will be launched.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/o-a9YOKQR3KR1S1VUr5rAA/en-us_image_0000002532749891.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E384B489B45A3C98DB793E3D00D7C03DFFA0C3F195D8D01DCA1D84BFC346BF3)
