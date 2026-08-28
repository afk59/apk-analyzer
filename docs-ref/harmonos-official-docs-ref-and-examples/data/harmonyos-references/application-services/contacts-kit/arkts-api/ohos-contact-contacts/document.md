# @ohos.contact (Contacts)

The **contact** module provides contact management functions, such as adding, deleting, and updating contacts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/J5KbquRNQS-9ZjFWj5JGCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC9EF9C1DF693D395238ED21ED4D7C9335E96D8908CFB4A06F274C7E1642388F)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { contact } from '@kit.ContactsKit';

#### contact.addContact10+

addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void

Adds a contact. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the ID of the added contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/yQJHjD00SAqW6kHbkLEUxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FD2311607EE008ABC2954BDFB77E67DE1C42B8400717592C725BD904F5A4A99)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.addContact(context, {
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(\`Failed to add Contact. Code:${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in adding Contact. data: ${JSON.stringify(data)}\`);
  });

#### contact.addContact(deprecated)

addContact(contact: Contact, callback: AsyncCallback<number>): void

Adds a contact. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/qm9EOpmZR9OKERo5eYy3dQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85C8B62AA3055C0B680BA7F3A787F67D768B47ECABC3F7DE7A7CB565C0BFC873)

This API is supported since API version 7 and deprecated since API version 10. Use [addContact](#contactaddcontact10) instead.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contact | [Contact](#contact) | Yes | Contact information. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the ID of the added contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.addContact(context, {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: \[{
    phoneNumber: '138xxxxxxxx'
  }\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to add Contact. Code:${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in adding Contact. data: ${JSON.stringify(data)}\`);
});

#### contact.addContact10+

addContact(context: Context, contact: Contact): Promise<number>

Adds a contact. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result, which is the ID of the added contact. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/5X0tEEkVQByz6p9Kngmi-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B464300F448A86E3A95B4C7DF286475612B46716D6D030AC28961514ABB6DC7D)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.addContact(context, {
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  });
  promise.then((data) => {
    console.info(\`Succeeded in adding Contact. data: ${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to add Contact. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.addContact(deprecated)

addContact(contact: Contact): Promise<number>

Adds a contact. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/0h_fqQ20RoiVl3IoD5X1GA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87F2A825A00B4B2D9DF27EB40B1ABB528025DF0B685F0ACACBDD909DDFA97629)

This API is supported since API version 7 and deprecated since API version 10. Use [addContact](#contactaddcontact10-1) instead.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contact | [Contact](#contact) | Yes | Contact information. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result, which is the ID of the added contact. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.addContact({
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: \[{
    phoneNumber: '138xxxxxxxx'
  }\]
});
promise.then((data) => {
  console.info(\`Succeeded in adding Contact. data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to add Contact. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.deleteContact10+

deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void

Deletes a contact. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [selectContacts](#contactselectcontacts10-1). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the ID of the deleted contact is returned. If the operation fails, an error code is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/mi0RVyXsQTeObsja7OvPXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29479B900713A804E9D1D841917B2F6F81D5FDEFD1979F56A0626571057DC760)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

 // Select a contact via selectContacts.
  contact.selectContacts().then((data) => {
    // Obtain the context within the component.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // Pass the key of the selected contact as the second parameter.
    contact.deleteContact(context, data\[0\].key, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to delete Contact. Code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in deleting Contact.');
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.deleteContact(deprecated)

deleteContact(key: string, callback: AsyncCallback<void>): void

Deletes a contact. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/AdJ83kuwTbejADI13-6C3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F1ACE415C07425D71440DEA40A7B4A4638462C89C7237B2DC089EF3E1B1F255)

This API is supported since API version 7 and deprecated since API version 10. Use [deleteContact](#contactdeletecontact10) instead.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [selectContacts](#contactselectcontacts10-1). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the ID of the deleted contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Pass the key of the selected contact as the first parameter.
  contact.deleteContact(data\[0\].key, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to delete Contact. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in deleting Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.deleteContact10+

deleteContact(context: Context, key: string): Promise<void>

Deletes a contact. This API uses a promise to return the result.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [selectContacts](#contactselectcontacts10-1). |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/iXRqC1zRTB-J4l4A-c1lLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4661F298084B05A064AD214ED6E1A329582E403ADD8BFC1A800AC57803FF2BD)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Pass the key of the selected contact as the second parameter.
  let promise = contact.deleteContact(context, data\[0\].key);
  promise.then(() => {
    console.info(\`Succeeded in deleting Contact.\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to delete Contact. Code: ${err.code}, message: ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.deleteContact(deprecated)

deleteContact(key: string): Promise<void>

Deletes a contact. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/fijAYhvbTzSa6wniZYmH7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78EFEA214CC5604D3F36411C8E79C841F780960926FD45D838C8B0E919647CDC)

This API is supported since API version 7 and deprecated since API version 10. Use [deleteContact](#contactdeletecontact10-1) instead.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [selectContacts](#contactselectcontacts10-1). |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Pass the key of the selected contact as the first parameter.
  let promise = contact.deleteContact(data\[0\].key);
  promise.then(() => {
    console.info(\`Succeeded in deleting Contact.\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to delete Contact. Code: ${err.code}, message: ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.updateContact10+

updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void

Updates a contact. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. The ID is mandatory and can be obtained through [selectContacts](#contactselectcontacts10-1). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Gf6jqgN6STmj2R0Z_PyqNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50FA2E387CEDD1416A9ACE168384F8CE257B8CE74356F15EF36A2E0DDA1C393E)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data\[0\].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  }, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to update Contact. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.updateContact(deprecated)

updateContact(contact: Contact, callback: AsyncCallback<void>): void

Updates a contact. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Qy-KiTI_Q3SKMySRVhr62g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1FC7E04502370F0A3C1EF26D4CE524D58356DD15E3289E67C4C233D14E8DAFA)

This API is supported since API version 7 and deprecated since API version 10. Use [updateContact](#contactupdatecontact10) instead.

**Required permissions**: ohos.permission.WRITE\_CONTACTS and ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contact | [Contact](#contact) | Yes | Contact information. The ID is mandatory and can be obtained through [selectContacts](#contactselectcontacts10-1). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data\[0\].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  }, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to update Contact. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.updateContact10+

updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void

Updates a contact. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. The ID is mandatory and can be obtained through [selectContacts](#contactselectcontacts10-1). |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/50Yi5xXrTTao9jyn7XT0Rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22DDDCCA58ABC20A997FF48AAC375FFC1F95D373B3020B4D575777F69AF5D03B)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data\[0\].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  }, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  }, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to update Contact. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.updateContact(deprecated)

updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void

Updates a contact. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/7ZlFg3yoSMOPb83HJOnMiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D09E8DBB701978878DC46C183D92B3762327BCD1D8BF909E24704BF2A4453BAB)

This API is supported since API version 7 and deprecated since API version 10. Use [updateContact](#contactupdatecontact10-1) instead.

**Required permissions**: ohos.permission.WRITE\_CONTACTS and ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contact | [Contact](#contact) | Yes | Contact information. The ID is mandatory and can be obtained through [selectContacts](#contactselectcontacts10-1). |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  contact.updateContact({
    id: data\[0\].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  }, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  }, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to update Contact. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.updateContact10+

updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>

Updates a contact. (The contact attribute list can be imported.) This API uses a promise to return the result.

**Permission required**: ohos.permission.WRITE\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. The ID is mandatory and can be obtained through [selectContacts](#contactselectcontacts10-1). |
| attrs | [ContactAttributes](#contactattributes) | No | List of contact attributes. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/PfUPditBT4GpY6N22rDN1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9064A88314D72353AB2C7AA68C30DE836A29FB0C45C0EF25A83647F9B104CB6)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Select a contact via selectContacts.
  contact.selectContacts().then((data) => {
    // Obtain the context within the component.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let promise = contact.updateContact(context, {
      id: data\[0\].id, // Select the contact ID.
      name: {
        fullName: 'xxx'
      },
      phoneNumbers: \[{
        phoneNumber: '138xxxxxxxx'
      }\]
    }, {
      attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
    });
    promise.then(() => {
      console.info('Succeeded in updating Contact.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to update Contact. Code: ${err.code}, message: ${err.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.updateContact(deprecated)

updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>

Updates a contact. (The contact attribute list can be imported.) This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Gdc-xMAiRiSK3yRyVqUPxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52FACDE8E7EAC3D48D1F6DDFB3FE5DC36580A036F6DA837DBAF5719EBE0435C8)

This API is supported since API version 7 and deprecated since API version 10. Use [updateContact](#contactupdatecontact10-2) instead.

**Required permissions**: ohos.permission.WRITE\_CONTACTS and ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contact | [Contact](#contact) | Yes | Contact information. The ID is mandatory and can be obtained through [selectContacts](#contactselectcontacts10-1). |
| attrs | [ContactAttributes](#contactattributes) | No | List of contact attributes. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  let promise = contact.updateContact({
    id: data\[0\].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: \[{
      phoneNumber: '138xxxxxxxx'
    }\]
  }, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  });
  promise.then(() => {
    console.info('Succeeded in updating Contact.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to update Contact. Code: ${err.code}, message: ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.isLocalContact10+

isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void

Checks whether the ID of this contact is in the local address book. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. Each contact corresponds to one ID. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, a Boolean value is returned. The value **true** indicates that the contact ID is in the local phonebook, and the value **false** indicates the opposite. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/QqTWt-4mRqKYgJjIG0kLSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8220F03E26DA0779303FE517301052217CB2A2E29E204D1584DB9BDE27577572)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.isLocalContact(context, 1, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in isLocalContact. data->${JSON.stringify(data)}\`);
});

#### contact.isLocalContact(deprecated)

isLocalContact(id: number, callback: AsyncCallback<boolean>): void

Checks whether the ID of this contact is in the local address book. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/hgped2EkQQ2PZ4t2qSGeVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A27127AAA81EEA2F9E6B4A6F0287CCB3504B2BCEE0534B100F62C5EE365A200E)

This API is supported since API version 7 and deprecated since API version 10. Use [isLocalContact](#contactislocalcontact10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. Each contact corresponds to one ID. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, a Boolean value is returned. The value **true** indicates that the contact ID is in the local phonebook, and the value **false** indicates the opposite. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.isLocalContact(1, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in isLocalContact. data->${JSON.stringify(data)}\`);
});

#### contact.isLocalContact10+

isLocalContact(context: Context, id: number): Promise<boolean>

Checks whether the ID of this contact is in the local address book. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. Each contact corresponds to one ID. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the contact ID is in the local phonebook, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/dYS6YmJ4STqHv2-QzeGibA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB85110B0DF0F1E0A01160CFCE7276E31C6DABDBF93D928376AFB48413FED084)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.isLocalContact(context, 1);
  promise.then((data) => {
    console.info(\`Succeeded in isLocalContact. data->${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.isLocalContact(deprecated)

isLocalContact(id: number): Promise<boolean>

Checks whether the ID of this contact is in the local address book. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/mCx1gRhuRbq_zNOi30bqUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78FC116877A58162E25D4DD8E0FDEC81F65F1434F67E7CBA7E59AF087A9DEEFF)

This API is supported since API version 7 and deprecated since API version 10. Use [isLocalContact](#contactislocalcontact10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. Each contact corresponds to one ID. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the contact ID is in the local phonebook, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.isLocalContact(1);
promise.then((data) => {
  console.info(\`Succeeded in isLocalContact. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.isMyCard10+

isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void

Checks whether a contact is included in my card. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, a Boolean value is returned. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/kjP1NcSyReeJNmnKLeg3Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1132DAB0BCADAE80F072F127C40CE3900A50822DCA56498416CDEF13586493B3)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.isMyCard(context, 1, (err: BusinessError, data) => {
    if (err) {
      console.error(\`Failed to isMyCard. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in isMyCard. data->${JSON.stringify(data)}\`);
  });

#### contact.isMyCard(deprecated)

isMyCard(id: number, callback: AsyncCallback<boolean>): void

Checks whether a contact is included in my card. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Szw_IExIRZSNdpy1usQynA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=922768A2DC88B249F1399DAF8498C3272599E85354AB4B2D0D7C9DAD1DFD1880)

This API is supported since API version 7 and deprecated since API version 10. Use [isMyCard](#contactismycard10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, a Boolean value is returned. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.isMyCard(1, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to isMyCard. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in isMyCard. data->${JSON.stringify(data)}\`);
});

#### contact.isMyCard10+

isMyCard(context: Context, id: number): Promise<boolean>

Checks whether a contact is included in my card. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ls_rixJpR66Y4jCcIp0fDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2386822D679519BC8ED0CD1BE735BBEC17214050653D82031040AA54126A215B)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.isMyCard(context, 1);
  promise.then((data) => {
    console.info(\`Succeeded in isMyCard. data->${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to isMyCard. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.isMyCard(deprecated)

isMyCard(id: number): Promise<boolean>

Checks whether a contact is included in my card. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/VyC9WtTpRgqkKdVlUSV23g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1428670A689660A12743BCCF1E65FA779BC9E65897E5552453DE009BFBC38C5)

This API is supported since API version 7 and deprecated since API version 10. Use [isMyCard](#contactismycard10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.isMyCard(1);
promise.then((data) => {
  console.info(\`Succeeded in isMyCard. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to isMyCard. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryMyCard10+

queryMyCard(context: Context, callback: AsyncCallback<Contact>): void

Queries my card. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/PbDIj0_gRzSlk--9qrUNCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD572D4AB4503AB6A3396E6D77D72D645023ABD018BA6C328123D3999457D407)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, (err: BusinessError, data) => {
    if (err) {
      console.error(\`Failed to query My Card. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in querying My Card. data->${JSON.stringify(data)}\`);
  });

#### contact.queryMyCard(deprecated)

queryMyCard(callback: AsyncCallback<Contact>): void

Queries my card. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/oHg_LW3nSCahwJaIJdcX1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C106D958FCB7E10646AC16A32DC50EC39DBC700BE5F14AE70D8AE53490D41CEF)

This API is supported since API version 7 and deprecated since API version 10. Use [queryMyCard](#contactquerymycard10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryMyCard((err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query My Card. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying My Card. data->${JSON.stringify(data)}\`);
});

#### contact.queryMyCard10+

queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

Queries my card. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/_EeXhZZhTGaavwKhqHTVwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F9F122AD8C9DB270BF749F586C1800C8393C61AF1FB5CA2BBE20D5CFB253FFE)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(\`Failed to query My Card. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in querying My Card. data->${JSON.stringify(data)}\`);
  });

#### contact.queryMyCard(deprecated)

queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

Queries my card. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/r6h9QRv1Rj6P1pJNvfS5xQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAF0B057982CF53F6DB373C0E215E6060E0F7BCACAD6451B21A0939593E1102E)

This API is supported since API version 7 and deprecated since API version 10. Use [queryMyCard](#contactquerymycard10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryMyCard({
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query My Card. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying My Card. data->${JSON.stringify(data)}\`);
});

#### contact.queryMyCard10+

queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>

Queries my card. (The contact attribute list can be imported.) This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| attrs | [ContactAttributes](#contactattributes) | No | List of contact attributes. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<[Contact](#contact)\> | Promise used to return the result, which is a contact in my card. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/t8TECsHkTv6dga7aVwMdDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D33E5B223BCFCC61BB6DC41E1F89EE7B1E72410622644D698AFF51A56A8B198)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.queryMyCard(context, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  });
  promise.then((data) => {
    console.info(\`Succeeded in querying My Card. data->${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query My Card. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.queryMyCard(deprecated)

queryMyCard(attrs?: ContactAttributes): Promise<Contact>

Queries my card. (The contact attribute list can be imported.) This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/gTNRIscLTniZDZtYNvyVYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92F1DFE9000DD7909BBB1902D1120071FA1B272A7AFA912A02C81E2CCAE81FF7)

This API is supported since API version 7 and deprecated since API version 10. Use [queryMyCard](#contactquerymycard10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attrs | [ContactAttributes](#contactattributes) | No | List of contact attributes. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<[Contact](#contact)\> | Promise used to return the result, which is a contact in my card. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryMyCard({
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying My Card. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query My Card. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.selectContact(deprecated)

selectContact(callback: AsyncCallback<Array<Contact>>): void

Selects a contact. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/D46kIESMQJaJKocUlrHKcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC3676CF60D852B62E74AD0CC61E34EF172C5074B15558568139B0435702E52E)

This API is supported since API version 7 and deprecated since API version 10. Use [selectContacts](#contactselectcontacts10) instead.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of selected contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.selectContact((err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to select Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in selecting Contact. data->${JSON.stringify(data)}\`);
});

#### contact.selectContact(deprecated)

selectContact(): Promise<Array<Contact>>

Selects a contact. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rdDogBnZTNa9R5TwI6DWXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9399667B611AC47A9B5E306082C28888C639BC03E72BAA4F0E680BCACE874CC)

This API is supported since API version 7 and deprecated since API version 10. Use [selectContacts](#contactselectcontacts10-1) instead.

**System capability**: SystemCapability.Applications.Contacts

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of selected contacts. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.selectContact();
promise.then((data) => {
  console.info(\`Succeeded in selecting Contact. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contact. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.selectContacts10+

selectContacts(callback: AsyncCallback<Array<Contact>>): void

Selects a contact. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of selected contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.selectContacts((err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in selecting Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.selectContacts10+

selectContacts(): Promise<Array<Contact>>

Selects a contact. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.Contacts

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of selected contacts. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.selectContacts();
promise.then((data) => {
  console.info(\`Succeeded in selecting Contacts. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.selectContacts10+

selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void

Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ContactSelectionOptions](#contactselectionoptions10) | Yes | Contact selection options. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of selected contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.selectContacts({
  isMultiSelect:false
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in selecting Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.selectContacts10+

selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>

Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ContactSelectionOptions](#contactselectionoptions10) | Yes | Contact selection options. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of selected contacts. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.selectContacts({isMultiSelect:false});
promise.then((data) => {
  console.info(\`Succeeded in selecting Contacts. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to select Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContact10+

queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/JyV9xA9hSjywvKlieuqgVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=070353C4A27EDF308BBD7548A1630DD2626BD3A65AB7A5CF1698F7ECFE68F3BE)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact(deprecated)

queryContact(key: string, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/9tVMmlJuTlOMY122NaYFfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33FEF8E4D55E87BE8C8EB661F5CA84018F1E487FD11896DD3E7811BB5D83FBAB)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContact](#contactquerycontact10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact10+

queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key and holder. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/kj1mGlQsT66xF4-6PFt0eQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87B838E429AB0E97F05C8934C0860D001FABAF62C4134B0BE3FCBE1431319D7D)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact(deprecated)

queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key and holder. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/p6fhXM1_TTamwA8Q1skJuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4449B97CC1946F8E51B097C21B14F06A89A96AE205DB5E60C758281D486F2C4D)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContact](#contactquerycontact10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact10+

queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key and attributes. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/1yHJlU-YR5SxRvT7wfzceQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6C6424382E4F798D572904A496196A23654D16037281E1C87F864DACCF7D7D3)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact(deprecated)

queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key and attributes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/b-WE1PBDRo2RQ8lbWHn-FA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5813D71C3BC0F7B07382DDE0FDCDFEEC8A8ABDF67BD6AE26108B0451EEA9C4C)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContact](#contactquerycontact10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact10+

queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key, holder, and attributes. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/C71KyRk4TNehDGZJR-uBfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15E6E20F5B5DC2C787F80322F891966A519DEAFDB514E6921DCF0BC36B244115)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryContact(context, 'xxx', {
    holderId: 1,
    bundleName: "",
    displayName: ""
  }, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
  });

#### contact.queryContact(deprecated)

queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

Queries a contact based on the specified key, holder, and attributes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/KmiJVZIUTG6Vr_tcPYuMlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24F51C4AC5141BC82ADB3C515BB6ADE496B450F7B511A381F22787A27C47B91C)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContact](#contactquerycontact10-3) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<[Contact](#contact)\> | Yes | Callback used to return the result. If the operation is successful, the queried contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
});

#### contact.queryContact10+

queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>

Queries a contact based on the specified key, holder, and attributes. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<[Contact](#contact)\> | Promise used to return the result, which is the queried contact. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/6YlPD9gLRcSV_N6WJO6DKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E4084F5550A02CF2F914D96B86B570ABD672E94CD84C93A0635DE993A283FD8)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContact(context, 'xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContact(deprecated)

queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>

Queries a contact based on the specified key, holder, and attributes. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/44LMTCkmQvyLw3x38KtEnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C46865B71E810FA01E53D2E40065FDB7E0890C486071C164E2AD350D785AEB85)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContact](#contactquerycontact10-4) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Contact key. Each contact corresponds to one key. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<[Contact](#contact)\> | Promise used to return the result, which is the queried contact. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryContact('xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contact. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contact. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContacts10+

queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/quobR70CTP2HH--iLs0jCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A701D4B60CA6B7AB18223669CF0C435EBD4688479AE1F7C7B3774623884FE59)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts(deprecated)

queryContacts(callback: AsyncCallback<Array<Contact>>): void

Queries all contacts. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/CK7z5oK-S8iqJqkTOB35sA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAE32F6F86C2A0747B18E69AD2A97B22CCFE6D621C4FF426F954808317E746AC)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContacts](#contactquerycontacts10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts((err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts10+

queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts based on the specified holder. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Y8SCQMI0TUG7r1_01igBOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDD402A2C3E257550EAC70DB487515BDD4DADABF0D6D1A9A2DF50043CF37F9B0)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts(deprecated)

queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts based on the specified holder. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/URkufFGhRyCmDsF-kQRdBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=859AE3C5067F04B9ACDE4B6042FEA84A22AE4FD6964822F855CBE06E4EAB8041)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContacts](#contactquerycontacts10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts({
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts10+

queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts based on the specified attributes. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/oep_yQa0RiC5ElH-MSZ1bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F71B9A19DAEB020E78D257EBA779F5C8245679AF85D3F9150F5BF116864344)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts(deprecated)

queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts based on the specified attributes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/VVVxVf4QS1CrCQS2xUSGiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC9BBDB1EE111498A90842C781F410DE3DDBA3AC67697F04288684F6F4E56F71)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContacts](#contactquerycontacts10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts({
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts10+

queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts based on the specified holder and attributes. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/hKeU63kZScekTYDglUOEMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D14FC1430E357D2012390DF2F4E5CA908B008FC7C6A7616B1281769FAC318DA5)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts(deprecated)

queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries all contacts based on the specified holder and attributes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/LbTU0s52Sla9WrqgsUKtYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D564E7C2D9815D198FE1264BDE9D94EC5BD6E753FB3028C23A46561D828FBE9F)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContacts](#contactquerycontacts10-3) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts({
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
});

#### contact.queryContacts10+

queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

Queries all contacts based on the specified holder and attributes. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of queried contacts. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/fXJAP0quRYChotKcoqhs8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8AC6A7D4209DA267A17662387B7168F6CA09E84626138FFE5C85299870F341C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContacts(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contacts. data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContacts(deprecated)

queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

Queries all contacts based on the specified holder and attributes. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/tzQpTuTgQR6tgE1R2LDeBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1B882ECFDBEBC9BF1344A4BBCB5EE1F1BBB0806FFF4EE18852C88B62302919E)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContacts](#contactquerycontacts10-4) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of queried contacts. |

**Example**

  import { BusinessError } from '@kit.BasicServicesKit';

  let promise = contact.queryContacts({
    holderId: 1,
    bundleName: "",
    displayName: ""
  }, {
    attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
  });
  promise.then((data) => {
    console.info(\`Succeeded in querying Contacts. data->${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query Contacts. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| phoneNumber | string | Yes | Phone number of the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/YGo6LvfMQ56KIyQkGc7rTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=222502FBF778624191FF055332CD435B5D199E294DE61440DB6839C81B51C57C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ufo5qiihRqKfYCSjUeW2yA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D6C8D98D5CFF42BEF8CCB9A541303926FDCE307ED8882E81C6E908ECA816EC2)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByPhoneNumber](#contactquerycontactsbyphonenumber10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number of the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number and holder. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| phoneNumber | string | Yes | Phone number of the contacts. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/aH19i46ARb-1rwApSw9aIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C4DBE33B332AC62F6A8386F3361CD0BB6B8AD0F508A007459CFAED900B0536F)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number and holder. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/t0DVuFt3SSG0oVJfHGbCXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53D67833739ECE95CB2F516803586F0660251A198C9E9402E94DED0006EDEEA0)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByPhoneNumber](#contactquerycontactsbyphonenumber10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number of the contacts. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| phoneNumber | string | Yes | Phone number of the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/g8-csLWaT0aLFhIoSmI3IQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30552EF0C6738A39FE5B297DE8629E382C44355F273E5DA54849A98D0590FDB2)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/8i3kL_DAS_GT8bDkOuRTqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67F2FA5FF808B18948F0F1B9130CC0A5AEB950329880F528BCDBD1CAE77F4E27)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByPhoneNumber](#contactquerycontactsbyphonenumber10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number of the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number, holder, and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| phoneNumber | string | Yes | Phone number of the contacts. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7rBHJHooScCthiigW9w7bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2ADFE5B839CA5AC3C3F59B196A977E87EF6C79784B57F1EE056A66BA288C470)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified phone number, holder, and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/KyQmswTwQJCuGNqQJI9GyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA61A538DAC1979056F6CC088A538BDB2796EDDD476F711CB2AE9744B66C51F4)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByPhoneNumber](#contactquerycontactsbyphonenumber10-3) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number of the contacts. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

Queries a contact based on the specified phone number, holder, and attributes. This API uses a promise to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| phoneNumber | string | Yes | Phone number of the contacts. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of queried contacts. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/TsUadq-_T2isfcWeiAYdig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C266430A7F052BA037A95F65F212F51E7B7F9F58FD8D34DD9DBA3FE9BD1BAC9F)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

Queries a contact based on the specified phone number, holder, and attributes. This API uses a promise to return the result. The return result of this API includes only the **id**, **key**, and **phoneNumbers** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/aqWwvA8-RJeTH4zcaIRkvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DED25DE48267C57C3BE5BFB41B380B00B8301D681FB25C94DA7318FD6028D41A)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByPhoneNumber](#contactquerycontactsbyphonenumber10-4) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number of the contacts. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of queried contacts. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| email | string | Yes | Email address of the contact. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/p7_l60phSmGFABht1vH0nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5112BFD01487DF68B75813AB2435F398587A75E8B2D1FF038BD66552A42B70EB)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/2iGE3qE0TpivRj5l-Pr1_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=797D2363C6F270474E0A931E64FE8053DC5E09AE43A27D1100B9F43A61CD6DE3)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByEmail](#contactquerycontactsbyemail10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| email | string | Yes | Email address of the contact. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email and holder. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| email | string | Yes | Email address of the contact. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/c_9rjgx2SsWZo7adaqaGHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=115B683908F632DD6C7D35C6B5856550481F9E429523ECFE3C2F0A3B92270BCC)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email and holder. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/yQHZ0MJOTs6HxqLDLIlPyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE1FA4ECFE0B0492C73E4D44B1C3FB505D9564BAFC9C48AA155756A7161919C6)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByEmail](#contactquerycontactsbyemail10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| email | string | Yes | Email address of the contact. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| email | string | Yes | Email address of the contact. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/wr-NLSKdR4epQ_hSAofazw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EE79C5A5EAA2D13FB917B10D8F604CD18951D86536659FCD4AD7FC7993F92FE)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', {
  attributes: \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/EOIO9ndaT1mxZtsQvtTmBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1292F2AAD119F129C0B59DC19F16484FB645293F5F4C647A1A5CB3F07C45935)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByEmail](#contactquerycontactsbyemail10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| email | string | Yes | Email address of the contact. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', {
  attributes: \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email, holder, and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| email | string | Yes | Email address of the contact. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/2erBj2AMSYujJijTchMcPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B441A4D2810564367C7E0104701E0254A6CE1C8F6414CE0CCF4C78391FD986A2)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

Queries a contact based on the specified email, holder, and attributes. This API uses an asynchronous callback to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/8MQkv6N1T8uprzQeQgiMlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1AFE0A745523AE44FB289839BA7C2AE78C74260432A55288AB308BB0B6DD77B)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByEmail](#contactquerycontactsbyemail10-3) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| email | string | Yes | Email address of the contact. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| attrs | [ContactAttributes](#contactattributes) | Yes | List of contact attributes. |
| callback | AsyncCallback<Array<[Contact](#contact)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried contacts is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME\]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
});

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

Queries a contact based on the specified email, holder, and attributes. This API uses a promise to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| email | string | Yes | Email address of the contact. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of queried contacts. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/pM048VkhQKOuiLBEJvbnfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CB6000515E7791865585EC8C3B55B53A763A18F6F487EB0919AB81B2E770E97)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsByEmail(context, 'xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

Queries a contact based on the specified email, holder, and attributes. This API uses a promise to return the result. The return result of this API includes only the **id**, **key**, and **Emails** attributes. If you want to query all information about a contact, you are advised to call [queryContact](#contactquerycontact10-3) to query the contact based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/SZaJ7ZauS7eGKhXLJuD3vg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58C620FFEFD75C41C40E0E7F923486CD597F5ED9F4766BF4D207B9292595A261)

This API is supported since API version 7 and deprecated since API version 10. Use [queryContactsByEmail](#contactquerycontactsbyemail10-4) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| email | string | Yes | Email address of the contact. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |
| attrs | [ContactAttributes](#contactattributes) | No | Contact attribute list. If this parameter is not specified, all contact attributes are queried by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Contact](#contact)\>> | Promise used to return the result, which is an array of queried contacts. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryContactsByEmail('xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME\]
});
promise.then((data) => {
  console.info(\`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryGroups10+

queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void

Queries all groups of a contact. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| callback | AsyncCallback<Array<[Group](#group)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried groups is returned. If the operation fails, an error code is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/S0lKiyogQXGCssZn7KG2Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A0CFBE8A369177D3A003E724AA8A77C3A622341C8CC7D2A95CD5A4E9BC67EAC)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryGroups(context, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Groups. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Groups. data->${JSON.stringify(data)}\`);
});

#### contact.queryGroups(deprecated)

queryGroups(callback: AsyncCallback<Array<Group>>): void

Queries all groups of a contact. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/TaX95XFOS_asWpjYYFNpOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7350C81DA030557875EEF49E763CDFBFA16E73D22FD4E685A27F097277842599)

This API is supported since API version 7 and deprecated since API version 10. Use [queryGroups](#contactquerygroups10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Group](#group)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried groups is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryGroups((err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Groups. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Groups.. data->${JSON.stringify(data)}\`);
});

#### contact.queryGroups10+

queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void

Queries all groups of a contact based on the specified holder. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Group](#group)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried groups is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/pi3MUDAFR_e1hF92NMQMKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6E35987DAB2EFF41D6AB61FB4D04F7F2A3A979A32CBA452CCD1CB3C40D99DB0)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryGroups(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Groups. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Groups. data->${JSON.stringify(data)}\`);
});

#### contact.queryGroups(deprecated)

queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void

Queries all groups of a contact based on the specified holder. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/XWIXqrr7Qi67NWKN47mD3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3503A8EF81EA101D8C21FA6AAC8D8E14031BEB1B304FCA38112F5D88361FD1A5)

This API is supported since API version 7 and deprecated since API version 10. Use [queryGroups](#contactquerygroups10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<Array<[Group](#group)\>> | Yes | Callback used to return the result. If the operation is successful, an array of queried groups is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryGroups({
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Groups. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Groups. data->${JSON.stringify(data)}\`);
});

#### contact.queryGroups10+

queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>

Queries all groups of a contact based on the specified holder. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for group filtering by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Group](#group)\>> | Promise used to return the result, which is an array of groups. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/_UMQi6UiRnq75BA1UCMxjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA0B1E871F613602E24807D39309D6855AA33ACECC6B049F4FE508FD59925F3E)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryGroups(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(\`Succeeded in querying Groups. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Groups. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryGroups(deprecated)

queryGroups(holder?: Holder): Promise<Array<Group>>

Queries all groups of a contact based on the specified holder. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/r_rtd6BwTFOaRh-AfxcI1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19923E5125171E686AD8785F2A116970AC199CED59FFEBF60D74005A9EA96162)

This API is supported since API version 7 and deprecated since API version 10. Use [queryGroups](#contactquerygroups10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for group filtering by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Group](#group)\>> | Promise used to return the result, which is an array of groups. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryGroups({
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(\`Succeeded in querying Groups. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Groups. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryHolders10+

queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void

Queries all applications that have created contacts. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| callback | AsyncCallback<Array<[Holder](#holder)\>> | Yes | Callback used to return the result. If the operation is successful, an array of the queried applications is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/4ENxovFcRs-kDNQ-BmbmXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64CB9ECBFA4DCE3D55CE66371C7754623274E14F598FAE8D96C0D08393E06EA0)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryHolders(context, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Holders. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Holders. data->${JSON.stringify(data)}\`);
});

#### contact.queryHolders(deprecated)

queryHolders(callback: AsyncCallback<Array<Holder>>): void

Queries all applications that have created contacts. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/n0mTJNLrTx-PvlAEyatoRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CBDAF6901D9E23E4014E29A68B32D2484C2347CDFFBA371CFF7B25927980012)

This API is supported since API version 7 and deprecated since API version 10. Use [queryHolders](#contactqueryholders10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Holder](#holder)\>> | Yes | Callback used to return the result. If the operation is successful, an array of the queried applications is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryHolders((err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Holders. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Holders. data->${JSON.stringify(data)}\`);
});

#### contact.queryHolders10+

queryHolders(context: Context): Promise<Array<Holder>>

Queries all applications that have created contacts. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Holder](#holder)\>> | Promise used to return the result, which is an array of queried applications. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/k02b68FhTNSPNEqJZ5YTTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=697B74986EB259178E334A3452786A7CCA3B7BA7F5653094A4B7FC60677E2D92)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryHolders(context);
promise.then((data) => {
  console.info(\`Succeeded in querying Holders. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Holders. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryHolders(deprecated)

queryHolders(): Promise<Array<Holder>>

Queries all applications that have created contacts. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/ev4IvzwqQra1JOWGPX3OgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DF565C88204612700FABC8E5F5469C1A4C3E0CE71E0F71426FAE331FD9DD3A9)

This API is supported since API version 7 and deprecated since API version 10. Use [queryHolders](#contactqueryholders10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Holder](#holder)\>> | Promise used to return the result, which is an array of queried applications. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryHolders();
promise.then((data) => {
  console.info(\`Succeeded in querying Holders. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Holders. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryKey10+

queryKey(context: Context, id: number, callback: AsyncCallback<string>): void

Queries the key of a contact based on the specified contact ID. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/43tdW1uBR4-8Iqng-S9z7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDAB0D1568D5A85BE9B015A7E2F7C9966BE69EEF7A6126D3B5C9264D5EEC34CE)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryKey(context, 1, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Key. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Key. data->${JSON.stringify(data)}\`);
});

#### contact.queryKey(deprecated)

queryKey(id: number, callback: AsyncCallback<string>): void

Queries the key of a contact based on the specified contact ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/fLskUChGQeGCnqr7g_soxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26AD744C553077277E970408E4D11D4AF76932B33495D7A6DDF45A5DA2551356)

This API is supported since API version 7 and deprecated since API version 10. Use [queryKey](#contactquerykey10) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryKey(1, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Key. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Key. data->${JSON.stringify(data)}\`);
});

#### contact.queryKey10+

queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void

Queries the key of a contact based on the specified contact ID and holder. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/x4H8lEATRNCd1ku4mRGEvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91CA0CF0414114869C48A8398C2AB93AF8216A2B75EBBD2F693D43503AE4A80C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryKey(context, 1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Key. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Key. data->${JSON.stringify(data)}\`);
});

#### contact.queryKey(deprecated)

queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void

Queries the key of a contact based on the specified contact ID and holder. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Vaktf57tRrWYct8opVSrvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81CD98CE350960C2D4BC5194DEB3F0F2A29003DF9780C9C2189C32B35329FE3D)

This API is supported since API version 7 and deprecated since API version 10. Use [queryKey](#contactquerykey10-1) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. |
| holder | [Holder](#holder) | Yes | Application that creates the contacts. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

contact.queryKey(1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(\`Failed to query Key. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in querying Key. data->${JSON.stringify(data)}\`);
});

#### contact.queryKey10+

queryKey(context: Context, id: number, holder?: Holder): Promise<string>

Queries the key of a contact based on the specified contact ID and holder. This API uses a promise to return the result.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| id | number | Yes | Contact ID. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result, which is the key of the queried contact. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/JG0So7YUR6GUTkIXLCRk2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DBFB5E203E354606C026C8C86C69A8C421AA7965C7EF1BB32AC346E3E95F3F1)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryKey(context, 1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(\`Succeeded in querying Key. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Key. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryKey(deprecated)

queryKey(id: number, holder?: Holder): Promise<string>

Queries the key of a contact based on the specified contact ID and holder. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/WbX0mfakQfC1uHE6XtjlRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB906B3D08FA34BF1B8A439E933B81AB344493F9D8BFFD518E6468F879165094)

This API is supported since API version 7 and deprecated since API version 10. Use [queryKey](#contactquerykey10-2) instead.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Contact ID. |
| holder | [Holder](#holder) | No | Application information for a contact. If this parameter is not specified, it is not used for contact filtering by default. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result, which is the key of the queried contact. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryKey(1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(\`Succeeded in querying Key. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query Key. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.queryContactsCount22+

queryContactsCount(context: Context): Promise<number>

Queries the number of all contacts. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**Permission required**: ohos.permission.READ\_CONTACTS

**System capability**: SystemCapability.Applications.ContactsData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result, which is the number of queried contacts. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Contacts Error Codes](../../error-codes/contact-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 16700001 | General error. |

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsCount(context);
promise.then((data) => {
  console.info(\`Succeeded in querying ContactsCount. data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to query ContactsCount. Code: ${err.code}, message: ${err.message}\`);
});

#### contact.addContactViaUI15+

addContactViaUI(context: Context, contact: Contact): Promise<number>

Opens the **Add contact** page to add a contact. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result, which is the contact ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Contacts Error Codes](../../error-codes/contact-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 801 | The specified SystemCapability name was not found. |
| 16700001 | General error. |
| 16700102 | Failed to set value to contacts data. |
| 16700103 | User cancel. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/U2dX-gMPRTqoWGo6es9bnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5304054B0A6932B5C8373478118B8C4AA5C6FB0C5A0E609CABFE72EE9387AFE)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the context within the component.
let contactInfo: contact.Contact = {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: \[{
    phoneNumber: '138xxxxxx'
  }\]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.addContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(\`Succeeded in add Contact via UI.data->${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to add Contact via UI. Code: ${err.code}, message: ${err.message}\`);
  });

#### contact.saveToExistingContactViaUI15+

saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>

Opens the **Save to existing** page to save a contact to an existing one. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. For the application context of the stage model, see [Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| contact | [Contact](#contact) | Yes | Contact information. |

**Return Value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result, which is the contact ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Contacts Error Codes](../../error-codes/contact-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 801 | The specified SystemCapability name was not found. |
| 16700001 | General error. |
| 16700101 | Failed to get value to contacts data. |
| 16700102 | Failed to set value to contacts data. |
| 16700103 | User cancel. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/W6n61BLlQFGnuWLd5wbVgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=573A1B40FBF1C109189752A4D187B2B45EFB067D97FDBBE1DF755B9C5ABACFF5)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the context within the component.
let contactInfo: contact.Contact = {
  id: 1,
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: \[{
    phoneNumber: '138xxxxxx'
  }\]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.saveToExistingContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(\`Succeeded in save to existing Contact via UI.data->${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to save to existing Contact via UI. Code: ${err.code}, message: ${err.message}\`);
  });

#### ContactSelectionOptions10+

Defines the contact selection options.

**System capability**: SystemCapability.Applications.Contacts

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isMultiSelect10+ | boolean | No | Yes | Whether multiple contacts can be selected. The value **true** indicates that multiple contacts can be selected, and the value **false** indicates that only one contact can be selected. The default value is **false**. **Atomic service API**: This API can be used in atomic services since API version 11. |
| maxSelectable15+ | number | No | Yes | Maximum number of contacts that can be selected. The default value is **10000**. **Atomic service API**: This API can be used in atomic services since API version 15. |
| isDisplayedByName15+ | boolean | No | Yes | Whether to display contacts by name. The value **true** indicates that contacts are displayed by name, and the value **false** indicates that contacts are displayed by number. The default value is **false**. **Atomic service API**: This API can be used in atomic services since API version 15. |
| filter15+ | [ContactSelectionFilter](#contactselectionfilter15) | No | Yes | Contact selection filter. **Atomic service API**: This API can be used in atomic services since API version 15. |

#### ContactSelectionFilter15+

Defines the contact selection filter.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.Contacts

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| filterClause | [FilterClause](#filterclause15) | No | No | Filter criteria. |
| filterType | [FilterType](#filtertype15) | No | No | Filter type. |

#### FilterType15+

Enumerates contact filter types.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Value | Description |
| :-- | :-- | :-- |
| SHOW\_FILTER | 0 | 
Shows only contacts that meet the filter criteria.

**System capability**: SystemCapability.Applications.Contacts

 |
| DEFAULT\_SELECT | 1 | 

Selects contacts that meet the filter criteria by default.

**System capability**: SystemCapability.Applications.Contacts

 |
| SHOW\_FILTER\_AND\_DEFAULT\_SELECT | 2 | 

Shows only contacts that meet the filter criteria and selects these contacts by default.

**System capability**: SystemCapability.Applications.Contacts

 |

#### FilterClause15+

Defines the contact filter criteria.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.Contacts

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | Array<[FilterOptions](#filteroptions15)\> | No | Yes | Contact ID. |
| name | Array<[FilterOptions](#filteroptions15)\> | No | Yes | Contact name. |
| dataItem | [DataFilter](#datafilter15) | No | Yes | Contact data filter item. |
| focusModeList | Array<[FilterOptions](#filteroptions15)\> | No | Yes | Focus mode list. |

#### FilterOptions15+

Defines contact filter options.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.Contacts

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| filterCondition | [FilterCondition](#filtercondition15) | No | No | Filter criteria. |
| value | string | ValueType\[\] | No | Yes | Filter value. The default value is **undefined**. |

#### FilterCondition15+

Enumerates filter criteria.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Value | Description |
| :-- | :-- | :-- |
| IS\_NOT\_NULL | 0 | 
The corresponding field is not empty.

**System capability**: SystemCapability.Applications.Contacts

 |
| EQUAL\_TO | 1 | 

The corresponding field is equal to a value.

**System capability**: SystemCapability.Applications.Contacts

 |
| NOT\_EQUAL\_TO | 2 | 

The corresponding field is not equal to a value.

**System capability**: SystemCapability.Applications.Contacts

 |
| IN | 3 | 

The value of the corresponding field is in an array.

**System capability**: SystemCapability.Applications.Contacts

 |
| NOT\_IN | 4 | 

The value of the corresponding field is not in an array.

**System capability**: SystemCapability.Applications.Contacts

 |
| CONTAINS | 5 | 

The value of the corresponding field contains a certain value.

**System capability**: SystemCapability.Applications.Contacts

 |

#### DataFilter15+

Defines the contact data filter item.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.Contacts

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| field | [DataField](#datafield15) | No | No | Contact data field. |
| options | Array<[FilterOptions](#filteroptions15)\> | No | No | Filter options. |

#### DataField15+

Enumerates contact data fields.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Value | Description |
| :-- | :-- | :-- |
| EMAIL | 0 | 
Email of the contact.

**System capability**: SystemCapability.Applications.Contacts

 |
| PHONE | 1 | 

Phone number of the contact.

**System capability**: SystemCapability.Applications.Contacts

 |
| ORGANIZATION | 2 | 

Organization of the contact.

**System capability**: SystemCapability.Applications.Contacts

 |

#### Contact

Defines a contact.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| INVALID\_CONTACT\_ID | number | \-1 | Default contact ID. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | Yes | Yes | Contact ID, which is automatically generated by the system. |
| key | string | Yes | Yes | Contact key, which is automatically generated by the system. |
| contactAttributes | [ContactAttributes](#contactattributes) | No | Yes | List of contact attributes. |
| emails | [Email](#email)\[\] | No | Yes | List of email addresses of the contact. |
| events | [Event](#event)\[\] | No | Yes | List of important dates such as birthdays and anniversaries of the contact. |
| groups | [Group](#group)\[\] | No | Yes | List of groups of the contact. |
| imAddresses | [ImAddress](#imaddress)\[\] | No | Yes | List of instant message addresses of the contact. |
| phoneNumbers | [PhoneNumber](#phonenumber)\[\] | No | Yes | List of phone numbers of the contact. |
| portrait | [Portrait](#portrait) | No | Yes | Contact portrait. |
| postalAddresses | [PostalAddress](#postaladdress)\[\] | No | Yes | List of postal addresses of the contact. |
| relations | [Relation](#relation)\[\] | No | Yes | List of relationships with the contact. |
| sipAddresses | [SipAddress](#sipaddress)\[\] | No | Yes | List of Session Initiation Protocol (SIP) addresses of the contact. |
| websites | [Website](#website)\[\] | No | Yes | List of websites of the contact. |
| name | [Name](#name) | No | Yes | Contact name. |
| nickName | [NickName](#nickname) | No | Yes | Contact nickname. |
| note | [Note](#note) | No | Yes | Contact notes. |
| organization | [Organization](#organization) | No | Yes | Organization of the contact. |

**Example**

Create contact data in JSON format:

let myContact: contact.Contact = {
    phoneNumbers: \[{
        phoneNumber: "138xxxxxxxx"
    }\],
    name: {
        fullName: "fullName",
        namePrefix: "namePrefix"
    },
    nickName: {
        nickName: "nickName"
    }
};

#### ContactAttributes

Provides a list of contact attributes, which are generally used as arguments.

If **null** is passed, all attributes are queried by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| attributes | [Attribute](#attribute)\[\] | No | No | List of contact attributes. |

**Example**

Create contact data in JSON format:

let contactAttributes: contact.ContactAttributes = {
    attributes: \[
        contact.Attribute.ATTR\_EMAIL,
        contact.Attribute.ATTR\_NAME,
        contact.Attribute.ATTR\_PHONE
    \]
};

#### Attribute

Enumerates contact attributes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Value | Description |
| :-- | :-- | :-- |
| ATTR\_CONTACT\_EVENT | 0 | Important dates such as birthday and anniversaries of the contact. |
| ATTR\_EMAIL | 1 | Email address of the contact. |
| ATTR\_GROUP\_MEMBERSHIP | 2 | Groups of the contact. |
| ATTR\_IM | 3 | IM addresses of the contact. |
| ATTR\_NAME | 4 | Contact name. |
| ATTR\_NICKNAME | 5 | Contact nickname. |
| ATTR\_NOTE | 6 | Contact notes. |
| ATTR\_ORGANIZATION | 7 | Organization of the contact. |
| ATTR\_PHONE | 8 | Phone number of the contacts. |
| ATTR\_PORTRAIT | 9 | Contact portrait. |
| ATTR\_POSTAL\_ADDRESS | 10 | Postal address of the contact. |
| ATTR\_RELATION | 11 | Relationship with the contact. |
| ATTR\_SIP\_ADDRESS | 12 | SIP addresses of the contact. |
| ATTR\_WEBSITE | 13 | Website that stores the contact information. |

**Example**

Create contact data in JSON format:

let attributes = \[contact.Attribute.ATTR\_EMAIL, contact.Attribute.ATTR\_NAME, contact.Attribute.ATTR\_PHONE\];

#### Email

Defines a contact's email.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | 0 | Custom mailbox type. |
| EMAIL\_HOME | number | 1 | Home mailbox. |
| EMAIL\_WORK | number | 2 | Work mailbox. |
| EMAIL\_OTHER | number | 3 | Other mailbox. |
| INVALID\_LABEL\_ID | number | \-1 | Invalid mailbox. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| email | string | No | No | Email addresses |
| labelName | string | No | Yes | Name of the mailbox type. |
| displayName | string | No | Yes | Displayed name of the mailbox. |
| labelId | number | No | Yes | Mailbox type. |

**Example**

Create contact data in JSON format:

let email: contact.Email = {
    email: "xxx@email.com",
    displayName: "displayName"
}

Or, create data by configuring an **Email** object.

let email = new contact.Email();
email.email = "xxx@email.com";

#### Holder

Defines an application that creates the contact.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | Bundle name. The value is **com.ohos.contacts**. |
| displayName | string | Yes | Yes | Application name. |
| holderId | number | No | Yes | Application ID. |

**Example**

Create contact data in JSON format:

let holder: contact.Holder = {
  bundleName: "com.ohos.contacts",
  displayName: "displayName",
  holderId: 1
};

#### Event

Defines a contact's event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | 0 | Custom event. |
| EVENT\_ANNIVERSARY | number | 1 | Anniversary event. |
| EVENT\_OTHER | number | 2 | Other event. |
| EVENT\_BIRTHDAY | number | 3 | Birthday event. |
| INVALID\_LABEL\_ID | number | \-1 | Invalid event. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eventDate | string | No | No | Event date. |
| labelName | string | No | Yes | Event type. |
| labelId | number | No | Yes | Event type ID. |

**Example**

Create contact data in JSON format:

let event: contact.Event = {
    eventDate: "2000-01-01"
};

Or, create data by configuring an **Event** object.

let event = new contact.Event();
event.eventDate = "2000-01-01";

#### Group

Defines a contact group.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| groupId | number | No | Yes | ID of a contact group. |
| title | string | No | No | Name of a contact group. |

**Example**

Create contact data in JSON format:

let group: contact.Group = {
    groupId: 1,
    title: "title"
};

#### ImAddress

Enumerates IM addresses.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | \-1 | Custom IM |
| IM\_AIM | number | 0 | AIM |
| IM\_MSN | number | 1 | MSN |
| IM\_YAHOO | number | 2 | Yahoo |
| IM\_SKYPE | number | 3 | Skype |
| IM\_QQ | number | 4 | QQ |
| IM\_ICQ | number | 6 | ICQ |
| IM\_JABBER | number | 7 | JABBER |
| INVALID\_LABEL\_ID | number | \-2 | Invalid IM |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| imAddress | string | No | No | IM address. |
| labelName | string | No | Yes | IM name. |
| labelId | number | No | Yes | IM ID. |

**Example**

Create contact data in JSON format:

let imAddress: contact.ImAddress = {
    imAddress: "imAddress",
    labelName: "labelName"
};

Or, create data by configuring an **ImAddress** object.

let imAddress = new contact.ImAddress();
imAddress.imAddress = "imAddress";

#### Name

Defines a contact's name.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| familyName | string | No | Yes | Family name. **Atomic service API**: This API can be used in atomic services since API version 11. |
| familyNamePhonetic | string | No | Yes | Family name in pinyin. **Atomic service API**: This API can be used in atomic services since API version 11. |
| fullName | string | No | No | Full name of the contact. **Atomic service API**: This API can be used in atomic services since API version 11. |
| givenName | string | No | Yes | Given name of the contact. **Atomic service API**: This API can be used in atomic services since API version 11. |
| givenNamePhonetic | string | No | Yes | Given name of the contact in pinyin. **Atomic service API**: This API can be used in atomic services since API version 11. |
| middleName | string | No | Yes | Middle name of the contact. **Atomic service API**: This API can be used in atomic services since API version 11. |
| middleNamePhonetic | string | No | Yes | Middle name of the contact in pinyin. **Atomic service API**: This API can be used in atomic services since API version 11. |
| namePrefix | string | No | Yes | Prefix of the contact name. **Atomic service API**: This API can be used in atomic services since API version 11. |
| nameSuffix | string | No | Yes | Suffix of the contact name. **Atomic service API**: This API can be used in atomic services since API version 11. |
| hasName22+ | boolean | No | Yes | Whether the contact information contains the name. The value **true** indicates that the contact information contains the name, and the value **false** indicates the opposite. **Atomic service API**: This API can be used in atomic services since API version 22. |

**Example**

Create contact data in JSON format:

let name: contact.Name = {
    familyName: "familyName",
    fullName: "fullName"
};

#### NickName

Defines a contact's nickname.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| nickName | string | No | No | Contact nickname. |

**Example**

Create contact data in JSON format:

let nickName: contact.NickName = {
    nickName: "nickName"
};

#### Note

Defines a contact's note.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| noteContent | string | No | No | Notes of the contact. |

**Example**

Create contact data in JSON format:

let note: contact.Note = {
    noteContent: "noteContent"
};

#### Organization

Defines a contact's organization.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Organization name. |
| title | string | No | Yes | Job title. |

**Example**

Create contact data in JSON format:

let organization: contact.Organization = {
    name: "name",
    title: "title"
};

#### PhoneNumber

Defines a contact's phone number.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | 0 | Custom phone type. |
| NUM\_HOME | number | 1 | Home phone. |
| NUM\_MOBILE | number | 2 | Mobile phone. |
| NUM\_WORK | number | 3 | Work phone. |
| NUM\_FAX\_WORK | number | 4 | Work fax. |
| NUM\_FAX\_HOME | number | 5 | Family fax. |
| NUM\_PAGER | number | 6 | Pager. |
| NUM\_OTHER | number | 7 | Other phone type. |
| NUM\_CALLBACK | number | 8 | Callback phone. |
| NUM\_CAR | number | 9 | Car phone. |
| NUM\_COMPANY\_MAIN | number | 10 | Company phone. |
| NUM\_ISDN | number | 11 | Integrated Services Digital Network (ISDN) phone. |
| NUM\_MAIN | number | 12 | Main phone. |
| NUM\_OTHER\_FAX | number | 13 | Other fax phone. |
| NUM\_RADIO | number | 14 | Wireless phone. |
| NUM\_TELEX | number | 15 | Telex phone. |
| NUM\_TTY\_TDD | number | 16 | Teletypewriter (TTY) or Test Driven Development (TDD) phone. |
| NUM\_WORK\_MOBILE | number | 17 | Work mobile phone. |
| NUM\_WORK\_PAGER | number | 18 | Work pager. |
| NUM\_ASSISTANT | number | 19 | Assistant phone. |
| NUM\_MMS | number | 20 | MMS phone. |
| INVALID\_LABEL\_ID | number | \-1 | Invalid phone type. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| labelName | string | No | Yes | Phone number type. |
| phoneNumber | string | No | No | Phone number. |
| labelId | number | No | Yes | Phone number ID. |

**Example**

Create contact data in JSON format:

let phoneNumber: contact.PhoneNumber = {
    phoneNumber: "138xxxxxxxx",
    labelId: contact.PhoneNumber.NUM\_HOME
};

Or, create data by configuring a new **PhoneNumber** object.

let phoneNumber = new contact.PhoneNumber();
phoneNumber.phoneNumber = "138xxxxxxxx";

#### Portrait

Defines a contact's portrait.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/gUlElDTnSr6LBxJtNyYwog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062505Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C130476F8C2187BA83BE4244214E58E175CD98E96422038E6E6A64E8100FE613)

Since API version 22, contact portraits can be set in URI or [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) format. (Currently, contact avatars cannot be set through the [addContactViaUI](#contactaddcontactviaui15) or [saveToExistingContactViaUI](#contactsavetoexistingcontactviaui15) API.)

URI indicates the address of the contact portrait file that can be accessed, and [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) indicates the [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) object generated based on the contact portrait resource.

Since API version 22, the profile picture resource can be read through URI. The resource can be opened only in [fs.open](../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen) mode and cannot be directly displayed in the **Image** component using a URI. You need to read the resource and display it in [PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) format.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | Contact portrait in URI format. **Atomic service API**: This API can be used in atomic services since API version 11. |
| photo22+ | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Contact portrait in PixelMap format. **Atomic service API**: This API can be used in atomic services since API version 22. |

**Example**

Create contact data in JSON format:

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function SetPortraitUri(uri: string) {
  let portrait: contact.Portrait = {
    uri: uri
  };
}

async function SetPortraitPixelMap(photo: image.PixelMap) {
  let portrait: contact.Portrait = {
    uri: "",
    photo: photo
  };
}

#### PostalAddress

Defines a contact's postal address.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | 0 | Custom postal address type. |
| ADDR\_HOME | number | 1 | Home address. |
| ADDR\_WORK | number | 2 | Work address. |
| ADDR\_OTHER | number | 3 | Other addresses. |
| INVALID\_LABEL\_ID | number | \-1 | Invalid address type. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| city | string | No | Yes | City where the contact is located. |
| country | string | No | Yes | Country/Region where the contact is located. |
| labelName | string | No | Yes | Postal address type. |
| neighborhood | string | No | Yes | Neighbor of the contact. |
| pobox | string | No | Yes | Email of the contact. |
| postalAddress | string | No | No | Postal address of the contact. |
| postcode | string | No | Yes | Postal code of the region where the contact is located. |
| region | string | No | Yes | Area where the contact is located. |
| street | string | No | Yes | Street where the contact resides. |
| labelId | number | No | Yes | Postal address type. |

**Example**

Create contact data in JSON format:

let postalAddress: contact.PostalAddress = {
    city: "city",
    postalAddress: "postalAddress"
};

Or, create data by configuring a new **PostalAddress** object.

let postalAddress = new contact.PostalAddress();
postalAddress.city = "city";
postalAddress.postalAddress = "postalAddress";

#### Relation

Defines a contact's relationship.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | 0 | Custom relationship. |
| RELATION\_ASSISTANT | number | 1 | Assistant. |
| RELATION\_BROTHER | number | 2 | Sibling. |
| RELATION\_CHILD | number | 3 | Child. |
| RELATION\_DOMESTIC\_PARTNER | number | 4 | Domestic partner. |
| RELATION\_FATHER | number | 5 | Father. |
| RELATION\_FRIEND | number | 6 | Friend. |
| RELATION\_MANAGER | number | 7 | Manager. |
| RELATION\_MOTHER | number | 8 | Mother. |
| RELATION\_PARENT | number | 9 | Parent. |
| RELATION\_PARTNER | number | 10 | Partner. |
| RELATION\_REFERRED\_BY | number | 11 | Referrer. |
| RELATION\_RELATIVE | number | 12 | Relative. |
| RELATION\_SISTER | number | 13 | Sister. |
| RELATION\_SPOUSE | number | 14 | Spouse. |
| INVALID\_LABEL\_ID | number | \-1 | Invalid relationship. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| labelName | string | No | Yes | Relationship type. |
| relationName | string | No | No | Relationship name. |
| labelId | number | No | Yes | Relationship ID. |

**Example**

Create contact data in JSON format:

let relation: contact.Relation = {
    relationName: "relationName",
    labelId: contact.Relation.RELATION\_ASSISTANT
};

Or, create data by configuring a new **Relation** object.

let relation = new contact.Relation();
relation.relationName = "relationName";
relation.labelId = contact.Relation.RELATION\_ASSISTANT;

#### SipAddress

Defines a contact's SIP address.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

#### \[h2\]Constant

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| CUSTOM\_LABEL | number | 0 | Custom SIP address. |
| SIP\_HOME | number | 1 | Home SIP address. |
| SIP\_WORK | number | 2 | Work SIP address. |
| SIP\_OTHER | number | 3 | Other SIP address. |
| INVALID\_LABEL\_ID | number | \-1 | Invalid SIP address. |

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| labelName | string | No | Yes | SIP address type. |
| sipAddress | string | No | No | SIP address. |
| labelId | number | No | Yes | SIP address ID. |

**Example**

Create contact data in JSON format:

let sipAddress: contact.SipAddress = {
    sipAddress: "sipAddress"
};

Or, create data by configuring a new **SipAddress** object.

let sipAddress = new contact.SipAddress();
sipAddress.sipAddress = "sipAddress";

#### Website

Defines a contact's website.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.ContactsData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| website | string | No | No | Website of the contact. |

**Example**

Create contact data in JSON format:

let website: contact.Website = {
    website: "website"
};
