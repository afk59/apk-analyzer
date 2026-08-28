# What should I do if breakpoints cannot be added during debugging?

**Symptom**

A breakpoint cannot be added during debugging, and the error message "Can't set breakpoint to remote debug server" is displayed, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/cRbhuFRkQh6glMRIh3WXOQ/en-us_image_0000002250578541.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F376B0B919891465E7F02FB653664F9738C10F076B20F8D5B40694C00ACFFB2E)

**Solution**

Perform the following steps:

1.  Check for the _xx_**.map** file. If it is not found, compile and build the project again to generate the map file, and then try adding the breakpoint again.
    
    -   For a stage model project, check whether the **sourceMaps.map** file exists. This file is generated during the build process and is stored under **entry\\build\\default\\intermediates\\loader\_out\\default**, as shown in the following figure.
        
        **Figure 1** Directory of the sourceMaps.map file in the stage model project  
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/-AsKgaZvTkmZtSQhsO7gBA/en-us_image_0000002250498437.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA6B334D9333C1A9F2DC987FCB3E37D0A905081726D2FB597EA3270075C0A056)
        
    -   For an FA model project, check whether the .map file corresponding to the file with the breakpoint issue exists. This file is generated during the build process and is stored under **entry\\build\\default\\intermediates\\loader\_out\\default**, as shown in the following figure.
        
        **Figure 2** Directory of the .map file in the FA model project  
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/cNOFBiOoTvmWFRbLnrb3LQ/en-us_image_0000002215658548.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7D65BD90E3487385E168F3278A0A2A85E61C0ED16B817FDBF575BC5D11A8853)
        

2.  Make sure the code file where the breakpoint is placed has been loaded. After the debugging session starts, if the code file has not been loaded (it will appear in the **Console** when loaded), the breakpoint cannot be added. The code file might not be loaded because it was not directly or indirectly referenced by the entry module. Once the code file is loaded, you should be able to add the breakpoint.
    
    **Figure 3** Code file with the breakpoint issue not loaded  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ZZm-brWgQJq0UdRuXNM8Zw/en-us_image_0000002215498752.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44057CA6410A61B31B28D91C23C52724C1F63774FC1376A9BD1C4C9C9879D3EF "Click to enlarge")
    
3.  Make sure the breakpoint is not placed at an invalid position. ArkTS does not support adding a breakpoint on the line containing only the closing parenthesis ()) of a method.
    
    **Figure 4** Invalid breakpoint position  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/PrdRgboVT_mFVuc-9srOxw/en-us_image_0000002250578549.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E900A10179674552B99196D197CA09B81F554D062BBB4B1AE8CF50ACF4F47E40 "Click to enlarge")
