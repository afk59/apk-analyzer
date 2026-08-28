# MDM Kit Development

#### Introduction

MDM Kit provides capabilities for the device administrator application, including enterprise device management and event listening, application management, feature restriction management, security management, device settings, device control, device information acquisition, hardware peripheral management, system management, and network management. For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/mdm-arkts).

A device administrator application is an application with the [EnterpriseAdminExtensionAbility](../enterpriseadminextensionability-development/document.md).

#### How to Develop

To develop a device administrator application, perform the following steps:

1.  Apply for qualification.
    
2.  Create an EnterpriseAdminExtensionAbility.
    
3.  Declare the permissions required by the application for calling the APIs.
    
4.  Develop and debug MDM functionalities.
    
5.  Distribute and deploy MDM applications.
    

## Applying for Qualification

Before developing an application, configure the project and application information in AppGallery Connect (AGC), including:

-   [Register as an enterprise developer](https://developer.huawei.com/consumer/en/doc/start/registration-and-verification-0000001053628148).
-   [Create a project](https://developer.huawei.com/consumer/en/doc/app/agc-help-createproject-0000001100334664) and [create an application](https://developer.huawei.com/consumer/en/doc/app/agc-help-createapp-0000001146718717).
-   Apply for the certificate and profile of the MDM application.

## Creating an **EnterpriseAdminExtensionAbility** Instance

For details, see [EnterpriseAdminExtensionAbility Development](../enterpriseadminextensionability-development/document.md).

## Declaring Required Permissions

Before declaring the required permissions, ensure that the [basic principles for using permissions](../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Then, declare the permissions required by the application under **requestPermissions** in the [module.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file of the module of the project. Example:

"requestPermissions": \[
// ···
  {
    "name": "ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS"
  },
// ···
\],

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/QUoe0aZlSquK1am8SCKpog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4D09C4E8E99FB5C24D5FC1D5BDDC3AF0DA8976B8CF4586CBAC5AE38AB078E72)

The required permissions vary with the API to call. For details, see [Enterprise Device Management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterprise-adminmanager) and other related APIs.

Apply for the declared MDM permission when applying for the certificate and profile of the MDM application. Otherwise, the application cannot obtain the permission.

## Developing MDM Functionalities

1.  Import modules. MDM Kit provides a wide variety of APIs for application management, communication management, security management, feature restriction management, system management, device settings and query, device control, and more. Import related modules based on service requirements. In this example, **adminManager** and **restrictions** are imported.
    
    import { adminManager, restrictions } from '@kit.MDMKit';
    
2.  Call APIs to implement related functionalities. For example, disable Wi-Fi for devices.
    
    import { adminManager, restrictions } from '@kit.MDMKit';
    // ...
    import { Want } from '@kit.AbilityKit';
    // ...
      private wantTemp: Want = {
        bundleName: 'com.example.mdmsample',
        abilityName: 'EnterpriseAdminAbility',
      };
      // ...
        try {
          restrictions.setDisallowedPolicy(this.wantTemp, 'wifi', isDisallow);
          console.info(isDisallow ? 'disable wifi success.' : 'enable wifi success.');
          // ...
        } catch (err) {
          console.error('setDisallowedPolicy fail.');
          // ...
        }
    

## Debugging

The MDM APIs can be called only after the **EnterpriseAdminExtensionAbility** is enabled. During the debugging process, you can use the following hdc commands to enable and disable an **EnterpriseAdminExtensionAbility**:

\# Enable a super administrator application.
hdc shell edm enable-admin -n Bundle\_name -a EnterpriseAdminExtensionAbility\_class\_name
# Enable a BYOD device administrator application.
hdc shell edm enable-admin -n Bundle\_name -a EnterpriseAdminExtensionAbility\_class\_name -t byod
# Disable an EnterpriseAdminExtensionAbility.
hdc shell edm disable-admin -n Bundle\_name

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Ev4rkRkzSjOg1ATcjiJkTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D226F4C427A9C09BC40B8B6E737CA98697F02478898998943BC30C4EC9896BC)

Only one super device administrator application can be enabled on a device.

BYOD, or Bring Your Own Device, allows enterprise employees to use their own mobile devices, such as laptops, tablets, and smartphones, on premises to obtain internal information and operate authorized enterprise applications.

The qualification application must be complete before the debugging.

## Distributing and Deploying MDM Applications

This function is not supported and will be released soon.
