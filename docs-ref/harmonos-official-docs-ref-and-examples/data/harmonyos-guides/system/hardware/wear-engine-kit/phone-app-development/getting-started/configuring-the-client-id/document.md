# Configuring the Client ID

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, find your desired app, and click it to access the **Project settings** page. On the **routine** tab page, find the client ID under **apply**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Vd84zZwLRpG583FRaVxdsQ/en-us_image_0000002190453281.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02BAA4B8FB3467291A45FAF8BCD6A9BF019EC5F94F946DA1CA495729051A6F0E "Click to enlarge")
    
2.  In the _module.json5_ file of the **entry** module in the project, add the **metadata** section, in which you should set **name** to **client\_id** and **value** to the client ID obtained in the previous step.
    
    {
      "module": {
        "name": "xxxx",
        "type": "entry",
        "description": "xxxx",
        "mainElement": "xxxx",
        "deviceTypes": \[\],
        "pages": "xxxx",
        "abilities": \[\],
        "metadata": \[
          // Configure the following information:
          {
            "name": "client\_id",
            "value": "xxxxxx"
          }
        \]
      }
    }
