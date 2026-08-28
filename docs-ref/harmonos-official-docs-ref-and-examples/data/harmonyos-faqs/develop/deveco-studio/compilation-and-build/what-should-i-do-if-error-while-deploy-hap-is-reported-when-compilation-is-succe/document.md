# What should I do if "Error while Deploy Hap" is reported when compilation is successful but installation fails?

**Symptom**

The packed HAR is successfully compiled in the project, but fails to be installed.

04/10 14:01:54: Install Failed: error: failed to install bundle. 
code:9568278 
error: install version code not same. 
$ hdc shell rm -rf data/local/tmp/f47e1222b8c64dbe92f86bc3b55cc3d2 
Error while Deploy Hap

**Possible Causes**

The **versionCode** field in the **app.json** file of the application to be installed is different from that of the installed one in the system.

**Solution**

Solution 1: You may have installed the application by using the **debug** button in DevEco Studio. Then, you install the application by running the **hdc install** command. You can run the following command to view the **debug** field information of the installed application:

bm dump -n application bundleName | grep debug

Uninstall and install a common application using the following command:

\>hdc uninstall application bundleName

Clear application data using the following command:

hdc shell bm clean -d -n application bundleName

Solution 2: The saved data of the application version is inconsistent with that of the newly installed version. Go to **Run** > **Edit Configurations** > **Run/Debug Configuration** and deselect **Keep Application Data**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ZmqnY70ZQceKOIlQFJtNqg/en-us_image_0000002194159004.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03CC1E16BE4959BECB96E465D3BF5EFC6374C4194387EA56392D08D312E147EC)
