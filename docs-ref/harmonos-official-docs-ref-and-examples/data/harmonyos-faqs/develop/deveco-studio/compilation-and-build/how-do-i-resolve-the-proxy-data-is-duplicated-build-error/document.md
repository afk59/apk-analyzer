# How do I resolve the "proxy data is duplicated" build error?

**Symptom**

When an App Pack is packaged, the message "uri datashareproxy://bundleName/\*\* in proxy data is duplicated" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Uu-qkGOCQxiDao9qmjm0BQ/en-us_image_0000002229758777.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97D600E3802633846180225C0D779868837B4CE13BFDE02977C56C4BDBD8E4A2)

**Solution**

The **proxyData** field lists the data proxies provided by the module and is only allowed to be configured in **entry** and **feature** modules. The URIs configured in different **proxyData** configurations must be unique. In light of this, if the preceding issue occurs, make sure there are no duplicate URIs across different modules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/MshXlSg0TvulFRhw3zGfZQ/en-us_image_0000002194158904.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D836BFF8E3B89194D0BE1DDC5213D8C3F1F1FFDECC6AF3F829C63FDF02FFD941)
