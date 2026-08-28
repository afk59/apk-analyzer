# What should I do if a cppcrash is reported during the test run because the ohosTest file references the method of the entry module?

**Symptom**

If the **ohosTest** file references the method of the **entry** module, which contains worker loading in common mode (for example, **"entry/ets/workers/Worker.ets"**), cppcrash is reported during the test run.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/OsFVb9OVQJK0gMhL9nqYPA/en-us_image_0000002194318400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09893E3673FB584934491F72C4B93D155AFFB3749317C0373BA744BABF985961)

**Solution**

Change the path mode of the instantiated worker in **entry** to the path loading mode with @ or relative path loading mode. Then, run the test again.

-   Path loading mode with @ (**"@entry/ets/workers/Worker.ets"**):
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/FfqYCUo3QBeCczUCPD4m5w/en-us_image_0000002194158792.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8C212683B087C25304A4C444337C4C06B3A87532FDF664D509009A80F1BA96B)
    
-   Relative path loading mode (**"../workers/Worker.ets"**):
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/_9ve53HQQGSke3gVM8iePw/en-us_image_0000002229758665.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B4C2EEE25BAAD63B05DD6E08E903ECD1FDA71D8441E13FD667A82DCB026E847)
