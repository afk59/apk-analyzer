# 1001500001 Fingerprint Certificate Verification Failure

**Symptom**

Error code 1001500001 is reported upon an API call, indicating a failed fingerprint certificate verification.

**Possible causes**

1.  **client\_id** has an incorrect value. (For example, it is set to the project's client ID.)
2.  The certificate fingerprint of the app is not configured or is incorrectly configured.
3.  You have not configured a new certificate fingerprint after replacing the certificate.
4.  The public key fingerprint does not take effect after you have added the fingerprint certificate.
5.  The app package signed with a debug certificate is installed, followed by the installation of the same version signed with a release certificate, or vice versa.
6.  Automatic signing is used instead of manual signing.

**Solution**

1.  Make sure that the client ID in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](../../getting-started/configuring-the-client-id/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/6IeoWOXFTC2txr9nZnGTKA/en-us_image_0000002497063312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1DC14092A7B898DBB18FBA00E4493AEBC72C8A27173955412668A9FC085C585)
    
2.  Ensure the fingerprint certificate of the app is correctly configured in AppGallery Connect. For details, please refer to [Adding a Public Key Fingerprint](../../../../getting-prepared/application-development-preparations/document.md#section1726913517284).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/ywf82yq9QgO9aiVGyZmNaQ/en-us_image_0000002528823289.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=113C36BF697185A39CD34DE3F542A9D2A7716F13CC10226A80B9348216782308 "Click to enlarge")
    
3.  After the certificate is replaced, reconfigure the new certificate fingerprint.
4.  Ten minutes after configuring the public key fingerprint, you can change the value of **versionCode** in the project's **app.json5** file to validate the fingerprint. The following figures show how to change the value of **versionCode**.
5.  After the debug certificate is replaced with the release certificate or vice versa, the app version number needs to be updated (by changing the value of **versionCode** in the project's **app.json5** file). The following figures show how to change the value of **versionCode**.
    
    **Figure 1** Before  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/rKejPFohTeyepybBkHaHTw/en-us_image_0000002528943265.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5E7A565045A087CE2BD5458CE74115AFA2758E4FF7145A8EA757DB36E21AA07)
    
    **Figure 2** After  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/BiVuF-tjSdKZaXav3xqyxw/en-us_image_0000002528823291.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B982BE2FCEB6E1C84FA435D9AF80B5C0A1F7AE9840F44ADEBB4E7CEDB6D1DB52)
    
6.  Use manual signing. For details, please refer to [Configuring Signing Information and Fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md).
