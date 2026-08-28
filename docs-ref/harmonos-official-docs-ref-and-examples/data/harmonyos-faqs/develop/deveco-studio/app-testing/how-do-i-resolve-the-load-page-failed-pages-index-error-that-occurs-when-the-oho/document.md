# How do I resolve the "Load Page Failed: pages/Index" error that occurs when the ohosTest file references the exported method of the startup page?

**Symptom**

When the ohosTest file references the exported method from the launch page and an attempt is made to launch the ability that contains the startup page, a JS crash occurs with the "Load Page Failed: pages/Index" error message during the test execution.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/qXCuaVPNR5-ys-oKYo6e9Q/en-us_image_0000002229604273.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E5D9BD26D2D712A7807F44DD301DBEDE6603F531738BEF2335E12670306BB00)**Solution**

When launching the ability that contains the startup page, explicitly specify the name of the current module. Run the test again.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/IYkL6z04TuuOHuA4Z78F7g/en-us_image_0000002194158896.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D5D5A6229115678407F93581D9892A756D75BB780F7CDD34AD3A4A38052BA1A)
