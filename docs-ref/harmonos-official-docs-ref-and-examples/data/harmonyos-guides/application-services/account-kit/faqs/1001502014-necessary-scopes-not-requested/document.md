# 1001502014 Necessary Scopes Not Requested

**Symptom**

Error code 1001502014 is reported upon an API call, indicating that the app does not have the required scope.

**Possible causes**

1.  You have not requested the necessary scope.
2.  Once your requested scope is approved, it will take effect within 25 hours.
3.  Your app tries calling the API for [obtaining a user's risk level](../../access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/document.md) before being granted the relevant scope.

**Solution**

1.  [Request the necessary scope](../../getting-started/requesting-scopes/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/z7wAEyHETa-BEnHJ6DvPRQ/en-us_image_0000002497223272.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60EE7DA922D021E182BEDF1900B68B76398002A54C8BD57E4F9B8E181D9C2826 "Click to enlarge")
    
2.  After the scope request is approved, you can change the value of **versionCode** in **app.json5** of your app project to validate the scope.
    
    **Figure 1** Before  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Eq9jicMERJSaGIQaSQAqIQ/en-us_image_0000002528823271.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A173A9D17532A1F8653DE575B509428B97343C0D1467675D0AEF99804196B41)
    
    **Figure 2** After  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/TqwoAyRnSx270PXiwryJtw/en-us_image_0000002528943239.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D129BB9D336E8EFE2EB826CEFA17CDC377D0F302AC375525D74BA1005857F38)
    
3.  Check whether the capability of obtaining a user's risk level is required. If so, request the corresponding scope by referring to [Obtaining the Risk Level](../../access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/document.md).
