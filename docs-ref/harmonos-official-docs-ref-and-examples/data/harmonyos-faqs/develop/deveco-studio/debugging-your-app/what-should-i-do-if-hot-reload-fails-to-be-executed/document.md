# What should I do if hot reload fails to be executed?

**Symptom**

Hot reload fails, and the console displays "Reloaded 1 files failed. Please reinstall and restart."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/qQnbvQbiQImdrlin-sL3eg/en-us_image_0000002194318548.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D81EBB7388810080ACB78FEEFE85105B3310A76F1C4FDD66F8B86172923A22D0 "Click to enlarge")

**Solution**

The patch package is installed on the device in the last step of hot reload. Hot reload fails if the **quickfix** command fails to be executed.

If the patch package fails to be installed, do the following checks:

-   Check whether the project is using a debug signature (not release signature). An incorrect signature would lead to a hot reload failure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/GGWkhf7eTtm1c8c0HmONbA/en-us_image_0000002229604317.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5A5BEF00C0513760DB18B267789FF689D695B54FC54F45A786156F3B03D785C "Click to enlarge")
    
-   Check **Build Mode** of the project. Hot reload supports **debug** and **<None>** instead of **release**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/JSFzMCPyQsKvgYfVQ196bw/en-us_image_0000002487886068.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E00529E3169332B68FD3A47E7E11F14CECE24452C6126F16F89674C2A19E722)
