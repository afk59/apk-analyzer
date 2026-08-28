# Debugging on the Emulator

Before starting debugging on the Emulator, register a debug credential with AppGallery Connect to secure the access of your app or atomic service to Cloud Foundation Kit. When you start your app or atomic service on the Emulator and trigger an API of Cloud Functions, Cloud DB, or Cloud Storage, the Emulator will generate a debug credential and output it to the log. Register the debug credential with AppGallery Connect, and you can debug your app or atomic service on the Emulator.

The procedure is as follows:

1.  Obtain the debug credential.
    1.  Create and start an Emulator. For details, please refer to [Managing the Emulator](../../../coding-and-debugging/running-your-app-on-the-emulator/managing-the-emulator/document.md).
    2.  Start your app or atomic service on the Emulator and trigger an API of Cloud Functions, Cloud DB, or Cloud Storage (an API of Cloud Functions is recommended). The API call will fail because the debug credential has not been registered. Ignore the failure and go to the next step.
    3.  Select **No filters** and use the keyword **clouddevelopproxy.debugToken** to find the debug credential in the log, and copy the debug credential.
        
        Format: \[clouddevelopproxy.debugToken=_xxx_\], where _xxx_ indicates the debug credential.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Dw-veYl2RZqeDgsoKPVqnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12C73F3464186290F5A2DA8D2C991683204DEFD4A977C9B6ECDD207DA9B93189)
        
        If the debug credential cannot be found in the log, check whether the app uses an incorrect signing mode. Currently, Cloud Foundation Kit supports two signing modes: [automatically signing an app associated with a registered app](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section20943184413328) or [manual signing](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233). Change the signing mode and try again.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/XwDBXHSXSFGTHBs9eZVIQQ/en-us_image_0000002440934308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=027D31B1B23F500905FAB70079354EDA1A7A7E7E58658BEC2D0B51D07440979C)
        
2.  Register the obtained debug credential with AppGallery Connect. For details, please refer to [Registering an Emulator Debug Credential](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-credential-0000002415343501).
3.  After the debug credential is registered, you can use the Emulator to debug your app or atomic service. For details about how to use the Emulator, please refer to the [instructions](../../../coding-and-debugging/running-your-app-on-the-emulator/document.md).
    
    If the error message returned when an API is called indicates that the signature verification fails (error code 401) or the authentication fails (error code 403), the possible causes are as follows:
    
    -   The debug credential is not registered. In this case, [register an Emulator debug credential](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-credential-0000002415343501).
    -   The registered debug credential is bound to an incorrect app or atomic service. In this case, delete the debug credential, bind the correct app or atomic service, and wait for 30 minutes before debugging.
