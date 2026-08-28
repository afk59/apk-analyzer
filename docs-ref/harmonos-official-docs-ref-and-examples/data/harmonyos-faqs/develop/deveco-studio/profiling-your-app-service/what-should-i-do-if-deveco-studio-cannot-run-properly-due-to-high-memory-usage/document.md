# What should I do if DevEco Studio cannot run properly due to high memory usage?

**Symptom 1**

During Profiler data analysis, DevEco Studio freezes or stops responding, and "Low Memory" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/PKlVIVoWQkmFdTZm_Wdzvw/en-us_image_0000002229758565.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAD470A398962425FEED1B441EDDC14A5A626D0D5BE26D1F31926C6455B57C79)

**Symptom 2**

During Profiler data analysis, Profiler cannot be used, and "The IDE is running low on memory" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/5_ZtM_SvTuWheGjhNYPzPg/en-us_image_0000002418335854.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E44AD3C02844358F17B00E540457A19304A69796B2F7BB06DBF44E662B65567F)

**Solution**

Modify the maximum memory that can be used by the VM in the DevEco Studio configuration file.

1.  On the DevEco Studio toolbar, choose **Help** > **Edit Custom VM Options** to open the configuration file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/yNlyBBx-TrCWPl0dDWYegg/en-us_image_0000002229604085.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84F0D9DF40D622F70E3FB4BAF657B80D6D0B710A14E17673B3A550A4DED99B97)
    
2.  Adjust the value after the **\-Xmx** parameter according to your actual needs. If the **\-Xmx** parameter is not present in the configuration file, add it manually. For example: **\-Xmx2048m**. **2048m** represents the amount of memory the virtual machine can use. You can increase this value as needed.
