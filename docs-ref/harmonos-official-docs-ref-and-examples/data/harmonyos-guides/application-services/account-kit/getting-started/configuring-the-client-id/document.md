# Configuring the Client ID

#### Obtaining the Client ID and App ID

In AppGallery Connect, go to [Development and services](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/myProject), select the relevant project and app, and find the app ID and client ID under **General information** > **App information**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/mNUhZRnuQduKtDpMXDWJrQ/en-us_image_0000002497223270.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=694E8821C195CDF769A9C453923502E1B4644B2CB2D5CBCCB44F381567BBA376 "Click to enlarge")

#### Checking the Necessity of Client ID Configuration

If the client ID and app ID obtained in the previous section are the same, it is unnecessary to configure the client ID. Otherwise, you need to configure the client ID as instructed in the next section.

#### Configuring the Client ID

In the **module.json5** file of the **entry** module in the project, add the **metadata** section. Set **name** to **client\_id** and **value** to the client ID obtained in the previous section.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/HkSNrOYqTtmWGLYaVLBTSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B60EB86F5742E8D47AFBC1FD601DD27082A14D0A2ABAD26C70F7925A86760935)

1\. If the project has multiple modules, configure the client ID of your app in the **module.json5** file in the module whose **type** is **entry**.

2\. Ensure that the obtained client ID is the client ID of your **app**. Using the project's client ID by mistake will result in API call errors.

"module": {
  "name": "_<name>_",
  **"type": "entry",**
  "description": "_<description>_",
  "mainElement": "_<mainElement>_",
  "deviceTypes": \[\],
  "pages": "_<pages>_",
  "abilities": \[\],
  **"metadata"****: \[** // Set as follows:
    **{**
      **"name": "client\_id",**
      **"value": "xxxxx"** // Assign the previously obtained client ID to the value field. Make sure not to set value using any other method.
    **}**
  **\]**
 }
