# Preparations

#### Applying for Permissions

Before using capabilities of Ads Kit, check whether your app has obtained corresponding permissions. If not, you need to declare these permissions.

Specifically, Ads Kit requires the following permissions:

-   **ohos.permission.INTERNET**: used to request and display an ad, and post back the bidding result.
-   **ohos.permission.APP\_TRACKING\_CONSENT**: used to obtain the Open Anonymous Device Identifier (OAID).

Configure the required permissions in the **module.json5** file of the module. The activity tracking permission [ohos.permission.APP\_TRACKING\_CONSENT](../../../system/security/application-access-control/application-permission-management/application-permissions/open-user-grant-permissions/document.md#ohospermissionapp_tracking_consent) is a **user\_grant** permission, and **reason** and **abilities** are mandatory. For details about the configuration method, please refer to the [requestPermissions description](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).

The sample code is as follows:

{
  "module": {
    "requestPermissions": \[
      {
        "name": "ohos.permission.APP\_TRACKING\_CONSENT",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": \[
            "EntryAbility"
          \],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.INTERNET"
      }
    \]
  }
}
