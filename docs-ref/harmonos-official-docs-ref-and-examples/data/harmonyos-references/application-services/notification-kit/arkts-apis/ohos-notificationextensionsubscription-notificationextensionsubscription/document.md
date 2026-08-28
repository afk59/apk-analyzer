# @ohos.notificationExtensionSubscription (notificationExtensionSubscription)

The **notificationExtensionSubscription** module provides capabilities for managing notification extension, including opening the extension settings screen, subscribing to/unsubscribing from notification extension, and obtaining/setting the notification authorization status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/VHih72SFSYqQFiYjwLvmEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6A87F54AE4DD8B514C9109152397C1F9C410F92CC1C635E3C7D6BBCDF2BB7D8)

The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { notificationExtensionSubscription } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';

#### notificationExtensionSubscription.openSubscriptionSettings

openSubscriptionSettings(context: UIAbilityContext): Promise<void>

Opens the settings screen of notification extension subscription in a semi-modal dialog box. On this screen, the user can toggle on the **Allow access to notifications on this device** switch and grant access to notifications for specified applications. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Required permissions**: ohos.permission.SUBSCRIBE\_NOTIFICATION

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | Ability context bound to the notification settings page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600018 | The notification settings window is already displayed. |
| 1600023 | The application does not implement the NotificationSubscriberExtensionAbility. |

**Example**

import { common } from '@kit.AbilityKit';

try {
  // Obtain the context from the component and ensure that the return value of this.getuIContext().getHostContext() is UIAbilityContext.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  notificationExtensionSubscription.openSubscriptionSettings(context).then(() => {
    console.info(\`openSubscriberSettings success\`);
  }).catch((e:Error) => {
    let error = e as BusinessError
    console.error(\`failed to call openSubscriptionSettings ${JSON.stringify(error)}\`)
  });
} catch (error) {
  console.error(\`failed to call openSubscriptionSettings ${JSON.stringify(error)}\`)
}

#### notificationExtensionSubscription.subscribe

subscribe(info: NotificationExtensionSubscriptionInfo\[\]): Promise<void>

Subscribes to the notification extension. You can subscribe to the notification extension only after obtaining the unique address of the Bluetooth device by calling the APIs related to the [Bluetooth modules](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/connectivity-kit-intro#bluetooth). This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Required permissions**: ohos.permission.SUBSCRIBE\_NOTIFICATION

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [NotificationExtensionSubscriptionInfo\[\]](../notification/notificationextensionsubscriptioninfo/document.md) | Yes | List of subscribed notifications (in array). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |
| 1600023 | The application does not implement the NotificationSubscriberExtensionAbility. |

**Example**

let infos: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo\[\] = \[
  {
    addr: '01:23:45:67:89:AB', // Use the dynamically obtained Bluetooth address.
    type: notificationExtensionSubscription.SubscribeType.BLUETOOTH
  }
\];
notificationExtensionSubscription.subscribe(infos).then(() => {
  console.info("subscribe success");
}).catch((err: BusinessError) => {
  console.error(\`subscribe fail: ${JSON.stringify(err)}\`);
});

#### notificationExtensionSubscription.unsubscribe

unsubscribe(): Promise<void>

Unsubscribes from the notification extension. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Required permissions**: ohos.permission.SUBSCRIBE\_NOTIFICATION

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**Example**

notificationExtensionSubscription.unsubscribe().then(() => {
  console.info("unsubscribe success");
}).catch((err: BusinessError) => {
  console.error(\`unsubscribe fail: ${JSON.stringify(err)}\`);
});

#### notificationExtensionSubscription.getSubscribeInfo

getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo\[\]>

Obtains the subscription information about the notification extension of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Required permissions**: ohos.permission.SUBSCRIBE\_NOTIFICATION

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NotificationExtensionSubscriptionInfo\[\]](../notification/notificationextensionsubscriptioninfo/document.md)\> | Promise used to return the [NotificationExtensionSubscriptionInfo\[\]](../notification/notificationextensionsubscriptioninfo/document.md) array. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**Example**

notificationExtensionSubscription.getSubscribeInfo().then((data: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo\[\]) => {
  console.info(\`getSubscribeInfo successfully. Data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`getSubscribeInfo fail: ${JSON.stringify(err)}\`);
});

#### notificationExtensionSubscription.isUserGranted

isUserGranted(): Promise<boolean>

Checks whether the **Allow access to notifications on this device** switch is toggled on. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Required permissions**: ohos.permission.SUBSCRIBE\_NOTIFICATION

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that this feature is enabled, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**Example**

notificationExtensionSubscription.isUserGranted().then((isOpen: boolean) => {
  if (isOpen) {
    console.info('isUserGranted true');
  } else {
    console.info('isUserGranted false');
  }
}).catch((err: BusinessError) => {
  console.error(\`isUserGranted fail: ${JSON.stringify(err)}\`);
});

#### notificationExtensionSubscription.getUserGrantedEnabledBundles

getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo\[\]>

Obtains the applications that are allowed to access device notifications. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.Notification

**Required permissions**: ohos.permission.SUBSCRIBE\_NOTIFICATION

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GrantedBundleInfo\[\]](../notification/notificationcommondef/document.md#grantedbundleinfo22)\> | Promise used to return the applications obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Notification Error Codes](../../error-codes/notification-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**Example**

notificationExtensionSubscription.getUserGrantedEnabledBundles().then((data: notificationExtensionSubscription.GrantedBundleInfo\[\]) => {
  console.info(\`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`getUserGrantedEnabledBundles fail: ${JSON.stringify(err)}\`);
});

#### NotificationExtensionSubscriptionInfo

type NotificationExtensionSubscriptionInfo = \_NotificationExtensionSubscriptionInfo

Describes the information about the notification extension subscription.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationExtensionSubscriptionInfo](../notification/notificationextensionsubscriptioninfo/document.md) | Describes the information about the notification extension subscription. |

#### NotificationInfo

type NotificationInfo = \_NotificationInfo

Describes the notification information delivered to the [onReceiveMessage](../ohos-application-notificationsubscriberextensionability-extensionability-for-not/document.md#onreceivemessage) callback of ExtensionAbility for notification subscriptions.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_NotificationInfo](../notification/notificationinfo/document.md) | Describes the notification information delivered to the [onReceiveMessage](../ohos-application-notificationsubscriberextensionability-extensionability-for-not/document.md#onreceivemessage) callback of ExtensionAbility for notification subscriptions. |

#### SubscribeType

Describes the type that enables notification extension subscription.

**System capability**: SystemCapability.Notification.Notification

| Name | Value | Description |
| :-- | :-- | :-- |
| BLUETOOTH | 0 | Bluetooth. |

#### BundleOption

type BundleOption = \_BundleOption

Describes the bundle information of an application.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_BundleOption](../notification/notificationcommondef/document.md#bundleoption) | Bundle information. |

#### GrantedBundleInfo

type GrantedBundleInfo = \_GrantedBundleInfo

Describes the bundle information of the authorized application.

**System capability**: SystemCapability.Notification.Notification

| Type | Description |
| :-- | :-- |
| [\_GrantedBundleInfo](../notification/notificationcommondef/document.md#grantedbundleinfo22) | Bundle information of the authorized application. |
