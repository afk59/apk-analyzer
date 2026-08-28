# What should I do if the website cannot be reached after I click Allow?

**Symptom**

After you log in with a HUAWEI ID on the browser and click **Allow**, the browser redirects to **http://localhost:10101/xxx**, and the error message "This site can't be reached" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/tFv-zpK3RaCEKMC4_bN3Ug/en-us_image_0000002194318008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19E20BB00662A5E73C52B9FE404CC0F4B6F20F423A6D9DC9B391F9F959DADCB8)

**Solution**

There may be an issue with the login channel between DevEco Studio and HUAWEI ID during login authorization. This may occur if you click Cancel or if DevEco Studio is closed unexpectedly during login.

Try to log in again. Do not perform other operations during the process. If the issue persists, check and configure the HTTP proxy of DevEco Studio. For details, see [What should I do if login failed after clicking the Allow button on the browser?](../what-should-i-do-if-login-failed-after-clicking-the-allow-button-on-the-browser/document.md)
