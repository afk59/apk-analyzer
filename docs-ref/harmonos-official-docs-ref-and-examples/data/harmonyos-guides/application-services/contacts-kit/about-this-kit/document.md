# About This Kit

The Contacts Kit allows users to add, delete, modify, and query contacts easily. It provides a series of APIs for you to quickly integrate contact management functions into your applications.

For details, see [@ohos.contact (Contacts)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-contact).

#### Available Capabilities

Using the Contacts Kit, you can manage contacts, including adding, deleting, modifying, and querying contact information. You can also use the Picker function to open the contact list.

The following capabilities are opened to all applications:

-   [Contact Selection with Picker](#contact-selection-with-picker)

The following capabilities are restrictedly opened to third-party applications:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/lLtxsau2TMCXfx_JC5sykw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B5AE43DC459D481CE68C5F50281F8CCE7D8C03B63692327C2F313358FB5541E)

The capability is subject to use in the [specified scenarios](../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionwrite_contacts) and is generally not provided for third-party applications. You need to declare the ohos.permission.WRITE\_CONTACTS permission to use this capability. For details, see [Requesting Restricted Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).

-   [Contact Management](#contact-management-restricted-permission)

#### Contact Selection with Picker

Generally, an app must have permission to access the system **Contacts**. When the user selects a contact, the Picker displays the contact list, directing the user to complete the operation. The app does not need to apply for the permission.

1.  Import the related modules.
    
    import { contact } from '@kit.ContactsKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the contact API to display the contact list, and click the desired contact.
    
    contact.selectContacts({
      isMultiSelect:false
    },(err: BusinessError, data) => {
        if (err) {
          console.error('selectContact callback, errCode:' + err.code + ', errMessage:' + err.message);
            return;
        }
        console.info(\`selectContact callback: success data->${JSON.stringify(data)}\`);
    });
    
3.  View the returned contact data.
    

#### Contact Management (Restricted Permission)

To implement contact management for an application, use the **permissions** API to request for the contact editing permission.

1.  Declare the required permission:
    
    The capability is subject to use in the [specified scenarios](../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionwrite_contacts) and is generally not provided for third-party applications. You need to declare the ohos.permission.WRITE\_CONTACTS permission to use this capability. For details, see [Requesting Restricted Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
    
2.  Include an array of required permissions in **Permissions**.
    
3.  Perform the corresponding operation on the contact.
    

// Sample code
import { common, abilityAccessCtrl, Permissions, PermissionRequestResult } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Contact {
  addContactByPermissions() {
    // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const permissions: Array<Permissions> = \['ohos.permission.WRITE\_CONTACTS'\];
    const contactInfo: contact.Contact = {
      name: { fullName: 'Wang Xiaoming' },
      phoneNumbers: \[{ phoneNumber: '13912345678' }\]
    }
    abilityAccessCtrl.createAtManager().requestPermissionsFromUser(context, permissions).then((result: PermissionRequestResult) => {
      if (result.authResults\[0\] !== 0) { // 0 if the permission request is successful; a non-0 value otherwise.
        console.error('request contact permissions failed');
        return;
      }
      contact.addContact(context, contactInfo).then((data) => {
        console.info(\`Succeeded in adding Contact. data: ${JSON.stringify(data)}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to add Contact. Code: ${err.code}, message: ${err.message}\`);
      });
    })
  }

  build() {
    Row() {
      Column() {
        Button ('Add Contact')
          .onClick(() => {
            this.addContactByPermissions();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
