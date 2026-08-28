# Getting Started

#### Preparing the Environment

-   HarmonyOS: HarmonyOS 6.0.0 Release or later
-   DevEco Studio: DevEco Studio 6.0.0 Release or later
-   HarmonyOS SDK: HarmonyOS 6.0.0 Release SDK or later

#### Applying for Qualification

Before you start developing an app, configure your project and app information in AppGallery Connect, including:

-   [Register an account](https://developer.huawei.com/consumer/en/doc/start/registration-and-verification-0000001053628148) and [perform identity verification as an enterprise developer](https://developer.huawei.com/consumer/en/doc/start/edrna-0000001062678489).
-   [Create a project](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-project-0000002242804048) and [create a HarmonyOS app](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506).

#### Applying for Required Permissions

Ensure that your permission application purposes comply with the [basic principles for using permissions](../../../system/security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions). Then, declare the permissions required by the app under **requestPermissions** in the [module.json5](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file of the module of the project.

| 
Capability

 | 

Use Case

 | 

Required Permission

 |
| :-- | :-- | :-- |
| 

Inter-workspace data transfer

 | 

Set and obtain audit information using the inter-workspace data transfer APIs.

 | 

ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT

 |
| 

Workspace management

 | 

Deliver the workspace lifecycle management policy.

 | 

ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES

 |
| 

Query workspace information.

 | 

ohos.permission.QUERY\_LOCAL\_WORKSPACES

 |
| 

Subscribe to workspace events.

 | 

ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE

 |

Example:

"requestPermissions": \[
  {
    "name": "ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT"
  },
  {
    "name": "ohos.permission.ENTERPRISE\_MANAGE\_LOCAL\_PUBLICSPACES"
  },
  {
    "name": "ohos.permission.QUERY\_LOCAL\_WORKSPACES"
  },
  {
    "name": "ohos.permission.ENTERPRISE\_WORKSPACES\_EVENT\_SUBSCRIBE"
  }
\]
