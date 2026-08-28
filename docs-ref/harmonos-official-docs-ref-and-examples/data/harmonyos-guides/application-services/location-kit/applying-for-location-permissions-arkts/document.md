# Applying for Location Permissions (ArkTS)

#### Scenario

Before using the capabilities provided by [Location Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager), check whether your application has been granted the permission to access the device location information. If not, your application needs to obtain the permission from the user.

The system provides the following location permission:

-   **ohos.permission.LOCATION**: used to obtain location accurate to meters.
    
-   **ohos.permission.APPROXIMATELY\_LOCATION**: used to obtain location accurate to 5 kilometers.
    
-   **ohos.permission.LOCATION\_IN\_BACKGROUND**: used to obtain location while the application is running at the background.
    

For details about the permissions required for each API of Location Kit, see [Location Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager).

#### How to Develop

1.  Declare the required permission in your application's configuration file. For details, see [Requesting User Authorization](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
    
2.  If your application needs to access the device location when running in the foreground, declare the location permission as described in the following table.
    

| Permission | Declarable or Not | Location Accuracy |
| :-- | :-- | :-- |
| ohos.permission.APPROXIMATELY\_LOCATION | Yes | Location accurate to 5 kilometers. |
| ohos.permission.APPROXIMATELY\_LOCATION and ohos.permission.LOCATION | Yes | Location accurate to meters. |

1.  If your application needs to access the device location when running in the background, declare the location permission as follows:

If your application needs to access the device location when running in the background, also request for a continuous task of the LOCATION type in addition to the permission declared in step 2.

For details about how to request for a continuous task, see [Continuous Task](../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).
