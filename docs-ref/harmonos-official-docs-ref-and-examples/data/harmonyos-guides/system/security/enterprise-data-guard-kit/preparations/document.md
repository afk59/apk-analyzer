# Preparations

#### Preparing the Environment

-   HarmonyOS: HarmonyOS NEXT Developer Beta1 or later
-   DevEco Studio: DevEco Studio NEXT Developer Beta1 or later
-   HarmonyOS SDK: HarmonyOS NEXT Developer Beta1 SDK or later

#### Applying for Qualification

Before you start developing an app, configure your project and app information in AppGallery Connect, including:

-   [Register an account](https://developer.huawei.com/consumer/en/doc/start/registration-and-verification-0000001053628148) and [perform identity verification as an enterprise developer](https://developer.huawei.com/consumer/en/doc/start/edrna-0000001062678489).
-   [Create a project](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-project-0000002242804048) and [create a HarmonyOS app](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506).

#### Applying for Permissions

Ensure that your permission application purposes comply with the [basic principles for using permissions](../../application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions). Then, apply for the development permissions required by the app under **requestPermissions** in the [module.json5 configuration file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of the module of the project.

| 
App Capability

 | 

Required Permissions

 |
| :-- | :-- |
| 

Hierarchical file management

 | 

ohos.permission.FILE\_GUARD\_MANAGER

 |
| 

ohos.permission.SET\_FILE\_GUARD\_POLICY

 |
| 

Enterprise recovery key

 | 

ohos.permission.ENTERPRISE\_RECOVERY\_KEY

 |

Example:

"requestPermissions": \[
  {
	"name": "ohos.permission.FILE\_GUARD\_MANAGER"
  },
  {
	"name": "ohos.permission.SET\_FILE\_GUARD\_POLICY"
  },
  {
	"name": "ohos.permission.ENTERPRISE\_RECOVERY\_KEY" 
  }
\]
