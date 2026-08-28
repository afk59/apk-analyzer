# What should I do if "Failed to get the device apiVersion" is reported when a project is run on the local Emulator?

**Symptom**

The error "Failed to get the device apiVersion" is reported when a project is run on the local Emulator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/uqrby3EqQri2s-YXGyfgig/en-us_image_0000002194317932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A55B8FBAF70AB5D057B3E7813E6DD7C1D826B65665166493EE3E40CFE1A2FA7)

**Solution**

Run the project again in either of the following ways:

-   In the **Local Emulator** window, click **Wipe User Data** to clear the Emulator data, restart the Emulator, and run the project again.
-   Open the command line tool, go to the **default/base/toolchains** directory under the HarmonyOS SDK installation directory, and run the following command to restart the hdc server:
    
    ./hdc kill -r
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/nsQekr6oSiGi1JiTHmL4Mg/en-us_image_0000002229758185.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A890333835A82A2EAA8A79B92880EF559169729AA631CDAC65F55330AA331DF6)
