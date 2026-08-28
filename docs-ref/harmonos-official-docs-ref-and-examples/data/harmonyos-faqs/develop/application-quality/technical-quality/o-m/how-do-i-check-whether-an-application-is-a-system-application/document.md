# How do I check whether an application is a system application?

1.  Connect the device.
2.  Run the following command to print logs (for details about how to obtain the bundle name, see [bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)):
    
    hdc shell bm dump -n <Bundle Name>
    
3.  If the value of **isSystemApp** is **true**, the current application is a system application.
    
    The following figures show part of the log:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/bzKIImMlTquzEk_BhvFUVw/en-us_image_0000002244305208.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062534Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D66BD4DD8E9BD7CF3F9EB9F70A3AAECA6B04EEA25283294A18F2848D8C6D711D "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/rRAv5uy8Sr2OGLky7HubCA/en-us_image_0000002279264169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062534Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C45210DD27260D1F3F20082A0CD83DD4B61512E6336CA2645FE775920C4B211 "Click to enlarge")
