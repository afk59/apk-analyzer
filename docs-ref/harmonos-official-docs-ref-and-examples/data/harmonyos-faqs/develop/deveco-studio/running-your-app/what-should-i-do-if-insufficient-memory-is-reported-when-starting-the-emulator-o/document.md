# What should I do if "insufficient memory" is reported when starting the Emulator on a Windows computer?

**Symptom**

When the Emulator is started, the system displays a message indicating that the memory of the Windows computer is insufficient.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Zyt4nFBdTgi4vjnFWr7wgw/en-us_image_0000002427651109.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB61482DDF9BAEAC98AB02F1930EAA96F310570FAC643CE167845DFE07538102)

**Solution**

1.  Open **Task Manager** and choose the **Details** tab, right-click the table header and choose **Select columns** and select **Commit size**. Click the **Commit size** column to sort the processes, and close some processes with high commit size.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/fo7G0bIRQFOdUaHx0iVpkg/en-us_image_0000002394051450.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54C48DA627061F0DC6369250B8BE691B9FD6B2DB044D12E743E84FE624DA11E4)
    
2.  Choose **Task Manager** > **Performance** > **Memory** and ensure that the remaining committed memory size is greater than the RAM size set for the Emulator.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/UF4EiZ89Rp2jHKmGTMIIvA/en-us_image_0000002394211314.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4141796EBAE8E57D8DB3DE8ED2F89E182860AA716E226634987D7DF1B0ABB845 "Click to enlarge")
