# Preparations

Before you start integration, make [necessary preparations](../../../getting-prepared/application-development-preparations/document.md).

#### Enabling Push Kit

As stated in [Relationship with Other Kits](../about-this-kit/document.md#section194981821202916), you need to enable Push Kit before enabling Call Service Kit. For details, please refer to [Enabling Push Kit](../../push-kit/preparations/enabling-push-kit/document.md).

#### Applying for Permissions

You need to [request required permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) according to your actual needs.

| 
Permission

 | 

Scenario

 | 

Remarks

 |
| :-- | :-- | :-- |
| 

[ohos.permission.MICROPHONE](../../../system/security/application-access-control/application-permission-management/application-permissions/open-user-grant-permissions/document.md#ohospermissionmicrophone)

 | 

Using the microphone during a voice call.

 | 

Mandatory.

 |
| 

[ohos.permission.CAMERA](../../../system/security/application-access-control/application-permission-management/application-permissions/open-user-grant-permissions/document.md#ohospermissioncamera)

 | 

Using the camera during a video call.

 | 

Needed when the app supports video calls.

 |

#### Sample Code

This guide provides only code snippets. For the complete sample code, please refer to the [sample code](https://gitee.com/harmonyos_samples/callkit-samplecode-voipdemo-arkts).
