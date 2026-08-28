# Black Screen Occurred on the Custom Scanning UI

**Problem**

The camera was launched from the custom scanning UI, but a black screen was displayed.

**Solution**

-   The camera permission has not been requested and the permission verification error code 201 is returned. In this case, [apply for the permission from the user](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   For details, please refer to the description of the ArkTS API error code [1000500001](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-error-code#section13010304159).
    1.  Ensure that you have called customScan.[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section447114223245).
    2.  Ensure that the aspect ratio defined in customScan.[ViewControl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section8604949165313) matches the camera stream aspect ratio, which is usually 1:1, 4:3, or 16:9.
    3.  Verify the logic executed when the app is switched between the foreground and background:
        
        When the app is switched to the background, stop the camera stream by calling customScan.[stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section6949611114915) and then release the camera stream by calling customScan.[release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1109456134917) in the page lifecycle function **onPageHide**. When the app is switched back to the foreground, restart the camera stream by calling customScan.[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section747366165913) in the page lifecycle function **onPageShow**.
