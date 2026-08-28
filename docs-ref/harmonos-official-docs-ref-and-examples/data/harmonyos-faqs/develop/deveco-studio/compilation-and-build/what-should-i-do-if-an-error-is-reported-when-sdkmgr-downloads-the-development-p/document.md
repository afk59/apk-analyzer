# What should I do if an error is reported when sdkmgr downloads the development package in commandline-tools-linux during pipeline setup?

**Symptom**

When the **commandline-tools** tool is used on Linux, the message "Failed to request URL https://devecostudio-dre.op.hicloud.com/sdkmanager/v5/hos/getSdkList" is displayed. Check whether the network connection is normal and ensure that the URL can be accessed. If the network is normal, update the **commandline-tools** tool to the latest version.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/q24DZkTATdWlXItTYu7kfA/en-us_image_0000002229603881.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D8507CA96F0D3BEAA653CA451D2AA524035043188C6314EA4075A6A7ACD3D55 "Click to enlarge")

**Solution**

This issue occurs when the Linux country code is not set to China.

You can perform the following steps to resolve this issue.

1.  Go to the folder where the **sdkmgr** script is located: **_${Root directory of the command line tool}_/sdkmanager/bin**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/DvAKeLLETVGhf_Ga2pLNGQ/en-us_image_0000002194158460.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66434DC8B94FCA558998654D98118BC0A3FCDD10B6C729858CF3FD640A76ECD3 "Click to enlarge")
    
2.  Open the sdkmgr file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/9earl1KgR_yzOH5GIYyBLA/en-us_image_0000002229603849.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC4A880FE3F4B326BA7AA7EB991F5A801963A717A94092C3BA11F681D6BDDE72 "Click to enlarge")
    
3.  Add **\-Duser.country=CN** after **\-Dfile.encoding=UTF-8** in the last line of the file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/ymccCbGxQMiVGwZdO70lcQ/en-us_image_0000002194318088.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66BC7B3C5F776AE425BCBF3533A66144545758D45C4B8E375810DC046A5AD535 "Click to enlarge")
    
4.  Save the modification and run the **sdkmgr** command again.
