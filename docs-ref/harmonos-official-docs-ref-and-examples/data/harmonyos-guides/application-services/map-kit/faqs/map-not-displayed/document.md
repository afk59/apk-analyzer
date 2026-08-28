# Map Not Displayed

**Symptom**

The map cannot be loaded.

**Possible causes**

1.  No network.
2.  The app identity verification failed or the Map Kit permission is not enabled.
3.  Basic preparations are not completed.

**Solution**

1.  Check whether the "get network status error, code: 201, message:Permission denied" log entry exists. If the log exists, the app does not have the permission for obtaining the network status.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/bd3ntPopQoGIODzoGF2tow/en-us_image_0000002517280073.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3B266243DF9411021D4DA17230EEC895C6A3E69B436C82E9521A7343F6C740)
    
    Add the permission for obtaining the network status to the **module.json5** file of your app.
    
    {
      "module" : {
        // ...
        "requestPermissions": \[
          {
            "name": "ohos.permission.INTERNET",
            "usedScene": {
              "when": "always"
            }
          },
          {
            "name": "ohos.permission.GET\_NETWORK\_INFO",
            "usedScene": {
              "when": "always"
            }
          }
        \]
      }
    }
    
    Search your app logs for "The network is unavailable". If this log entry exists, the device network is faulty. Check the network status.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/QfQUVfpRQxuH6Wh74eV0Rw/en-us_image_0000002485000168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ADDBDA9641A2360C91C00850F63841BFE5002ABD1039769D402CFB1F6492C20)
    
2.  Search your app logs for "The app does not have map permission". If this log entry exists, the app identity verification failed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/dCJckiLDQeSj_cuULI3u-Q/en-us_image_0000002517280077.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=320D925768457FABE87950E8FFF83696DC51FC0441BE9BD4CB2C9A2194E47489)
    
    Search the logs of the **com.huawei.hms.mapservice** process for "App authentication failed. code: 1002600003". If this log entry exists, refer to [1002600003](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-errorcode#section104439246447) to complete app identity verification.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/gm53v6iiSAK34Yc5cG6GJA/en-us_image_0000002517280075.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73B85B34CE3514C9B9E828B55C16E9EA043D2301E76027C7BA9E64BDB23EFBB6)
    
3.  Complete the basic preparations by referring to [Preparing for Application Development](../../../../getting-prepared/application-development-preparations/document.md).
