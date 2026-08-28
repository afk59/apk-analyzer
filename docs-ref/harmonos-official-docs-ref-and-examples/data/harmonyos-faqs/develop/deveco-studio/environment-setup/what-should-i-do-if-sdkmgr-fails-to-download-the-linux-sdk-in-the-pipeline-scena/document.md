# What should I do if sdkmgr fails to download the Linux SDK in the pipeline scenario?

**Symptom**

When sdkmgr is used on Linux, the following error is displayed: "Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Pgm6Oc44RYCX7CWO9f8MDQ/en-us_image_0000002194158336.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28B85EA6835E714B3EBFA239A739FF60B457B2235FDE56393AA5F046CF141FAF)

**Solution**

This issue occurs when the country code for Linux is not set to China.

1.  Open the CLI and go to the directory where sdkmgr is located.
    
    cd ${root directory of sdkmgr}/sdkmanager/bin
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Pn4s2P1lSqWPafnY0M4NiA/en-us_image_0000002229603729.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00DCA997C92C03D0AF5444119350F4593DF7BF97F40535DCD542A82FDCB23E2D)
    
2.  Open the sdkmgr file.
    
    vim sdkmgr
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/tpsGdQ3QRC2OdCdBuEVZDg/en-us_image_0000002229758205.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1EDCDDD584697904E57148F0FEE061B12486C0E41C25F3A3E2D1D456247C20E)
    
3.  Append the country code **\-Duser.country=CN** to **\-Dfile.encoding=UTF-8** on the last line.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/RAHK-n6YRsGqzpiQQBrUIQ/en-us_image_0000002194317952.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062614Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5D2461A753E6B6EA6BDBE07892128DB3CB41516881790E05BB74AC44F5ECF2F)
    
4.  Save the changes and run the sdkmgr-related commands again to download the Linux SDK.
