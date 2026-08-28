# System Common Events

This topic provides a list of common events defined by the system.

Common event types are defined in [Support](../ohos-commoneventmanager-common-event/document.md#support) of the **ohos.commonEventManager** module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Mz8Xmi0ySAi5b1MbM3OZ_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0059A3848DC9ADFE07E6E91170B6A4A6730E41716BF498720FC66836AF00F92B)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Ability Kit

#### \[h2\]COMMON\_EVENT\_PACKAGE\_RESTARTED

Indicates that the user has restarted the application package and killed all its processes.

When the specified user restarts the application and kills all its processes, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/FD_TCwCJSR61MufoO850sQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5997CDB96B38A8BF3E13B8CCC96F4787C1B90CF7A3F2885C987406578D018EE0)

Third-party applications can only listen for the restart event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_RESTARTED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED

Indicates that the user has cleared the application package data.

When the specified user clears the application package data on the device, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/bZ606BGWS7-tdRJW4xFvDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27BC9B9DC82194158A09B670D5BD935ED653209ECCCD82BD3103C60EF3E38AD4)

Third-party applications can only listen for the data clearance event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_DATA\_CLEARED"

#### \[h2\]COMMON\_EVENT\_QUICK\_FIX\_APPLY\_RESULT

Indicates the result of applying a quick fix to the application.

When the specified user applies a quick fix to the application on the device, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/n9n08ZZwTcKVM7kHElNqnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C1C216C117B9829B508864748BB2F05134C69FEB8F1ECB32C6F681777450A77)

Third-party applications can only listen for the quick fix event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.QUICK\_FIX\_APPLY\_RESULT"

#### \[h2\]COMMON\_EVENT\_QUICK\_FIX\_REVOKE\_RESULT10+

Indicates the result of revoking a quick fix to the application.

When a quick fix to the application is revoked on the device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.QUICK\_FIX\_REVOKE\_RESULT"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_ADDED

Indicates that a new application package has been installed on the device.

When a new application is installed by a specified user on the device, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/vfnGjvzgRp-zA7CLDImBpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71250F67F73EFE9367A8BBD17869EB2A1C24848D637212E3007A17FB737D1069)

Third-party applications can only listen for the installation event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_ADDED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_REMOVED

Indicates that an installed application has been uninstalled from the device with the application data retained.

When a specified application package is removed by a specified user on the device, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/2zaZXMFQR36qEcRhx06sGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DA2F8C1E86F91F3E3CB85FBE76C39D35F7AB9F1BA3F5A4CD119D9DCF72F77A1)

Third-party applications can only listen for the uninstallation event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_REMOVED"

#### \[h2\]COMMON\_EVENT\_BUNDLE\_REMOVED

Indicates that an installed bundle has been uninstalled from the device.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.BUNDLE\_REMOVED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED

Indicates that an installed application has been completely uninstalled from the device.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_FULLY\_REMOVED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_CHANGED

Indicates that an application package has been changed (for example, an ability in the package has been enabled or disabled).

When an application package installed on the device is updated or an ability in the package is enabled or disabled, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/oxk-EfX1R2SnCYF5R_hdCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCEAF4DA278164F0B1C80E17E68FA4D7DF41BE71865FF0B5CD2B2CA3F928C79F)

Third-party applications can only listen for the change event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_CHANGED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED

Indicates that the user cleared the application package cache.

When the cache of an application package installed on the device is cleared, the event notification service is triggered to publish this event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/p5X28Lf-RaOFhf-K-2dvSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=221B4E80E5F3F35D3C83149DFA4B938C134CEDBB28ED0B4D12D6D5ED77E47559)

Third-party applications can only listen for the cache clearance event of themselves.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_CACHE\_CLEARED"

#### \[h2\]COMMON\_EVENT\_PACKAGES\_SUSPENDED

Indicates that application packages have been suspended.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGES\_SUSPENDED"

#### \[h2\]COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED

Indicates that application packages have been suspended by the system.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.MY\_PACKAGE\_SUSPENDED"

#### \[h2\]COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED

Indicates that application packages have been unsuspended by the system.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.MY\_PACKAGE\_UNSUSPENDED"

#### \[h2\]COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE

Notifies the low memory state and package management should be started.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.MANAGE\_PACKAGE\_STORAGE"

#### Account Kit

#### \[h2\]COMMON\_EVENT\_MINORSMODE\_ON12+

Indicates that the minor mode is enabled.

When the minor mode is enabled on the device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 12.

**Value**: "usual.event.MINORSMODE\_ON"

#### \[h2\]COMMON\_EVENT\_MINORSMODE\_OFF12+

Indicates that the minor mode is disabled.

When the minor mode is disabled on the device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 12.

**Value**: "usual.event.MINORSMODE\_OFF"

#### ArkData

#### \[h2\]COMMON\_EVENT\_DATA\_SHARE\_READY12+

Indicates that the DataShare service is available.

After the DataShare service is started, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.DATA\_SHARE\_READY"

#### ArkUI

#### \[h2\]COMMON\_EVENT\_SPLIT\_SCREEN

Indicates a screen splitting action.

When any of the following actions is performed, the event notification service is triggered to publish this event: accessing the recent tasks screen, creating a split-screen bar, and destroying a split-screen bar.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 11.

**Value**: "common.event.SPLIT\_SCREEN"

#### Notification Kit

#### \[h2\]COMMON\_EVENT\_SLOT\_CHANGE

Indicates that the notification slot or notification switch settings have changed.

When the notification slot settings (including the switch) change or the notification feature is enabled or disabled, the notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.NOTIFICATION\_CONTROLLER

**Value**: "usual.event.SLOT\_CHANGE"

#### Background Tasks Kit

#### \[h2\]COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED

Indicates that the system idle mode has changed.

When the user does not use the device for the specified period of time and the screen is turned off, the system delays the CPU and network access by background applications, and the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.DEVICE\_IDLE\_MODE\_CHANGED"

#### Basic Services Kit

#### \[h2\]COMMON\_EVENT\_USB\_STATE

Indicates that the USB device state has changed.

When a USB device is connected to or disconnected from the device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.hardware.usb.action.USB\_STATE"

#### \[h2\]COMMON\_EVENT\_USB\_PORT\_CHANGED

Indicates that the USB port state of the device has changed.

When the USB port state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.hardware.usb.action.USB\_PORT\_CHANGED"

#### \[h2\]COMMON\_EVENT\_USB\_DEVICE\_ATTACHED

Indicates that a USB device has been attached to the device functioning as a USB host.

When a USB device is attached, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED"

#### \[h2\]COMMON\_EVENT\_USB\_DEVICE\_DETACHED

Indicates that a USB device has been detached from the device functioning as a USB host.

When a USB device is detached, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED"

#### \[h2\]COMMON\_EVENT\_TIME\_CHANGED

Indicates that the system time is set.

When the system time is set, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.TIME\_CHANGED"

#### \[h2\]COMMON\_EVENT\_TIME\_TICK

Indicates that the system time has changed.

When the system time in the unit of minute changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.TIME\_TICK"

#### \[h2\]COMMON\_EVENT\_TIMEZONE\_CHANGED

Indicates that the system time zone has changed.

When the system time zone changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.TIMEZONE\_CHANGED"

#### \[h2\]COMMON\_EVENT\_USER\_INFO\_UPDATED

Indicates that the user information has been updated.

When the distributed account information, system account profile picture, or system account name is changed, the event notification service is triggered to publish this event carrying the system account ID.

APIs related to this event: **setOsAccountName**, **setOsAccountProfilePhoto**, and **setOsAccountDistributedInfo**. The first two are system APIs, and the last is a public API. For details, see [@ohos.account.osAccount (System Account Management)](../../account-management/ohos-account-osaccount-system-account-management/document.md) and [@ohos.account.distributedAccount (Distributed Account Management)](../../account-management/ohos-account-distributedaccount-distributed-account-management/document.md).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.USER\_INFO\_UPDATED"

#### \[h2\]COMMON\_EVENT\_USER\_UNLOCKED

Indicates that the credential-encrypted storage has been unlocked for the current user after the device is restarted.

When the device is unlocked with the lock screen password the first time after user switching, the event notification service is triggered to publish this event carrying the system account ID that identifies the user.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.USER\_UNLOCKED"

#### \[h2\]COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN

Indicates a successful login from a distributed account.

When a distributed account is successfully logged in, the event notification service is triggered to publish this event carrying the system account ID.

APIs related to this event: **setOsAccountDistributedInfo** and **updateOsAccountDistributedInfo** (discarded), and **setOsAccountDistributedInfoByLocalId**. The first two are public APIs, and the last one is a system API. For details, see [@ohos.account.distributedAccount (Distributed Account Management)](../../account-management/ohos-account-distributedaccount-distributed-account-management/document.md).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 12.

**Value**: "common.event.DISTRIBUTED\_ACCOUNT\_LOGIN"

#### \[h2\]COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT

Indicates a successful logout from a distributed account.

When a distributed account is successfully logged out, the event notification service is triggered to publish this event carrying the system account ID.

APIs related to this event: **setOsAccountDistributedInfo** and **updateOsAccountDistributedInfo** (discarded), and **setOsAccountDistributedInfoByLocalId**. The first two are public APIs, and the last one is a system API. For details, see [@ohos.account.distributedAccount (Distributed Account Management)](../../account-management/ohos-account-distributedaccount-distributed-account-management/document.md).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 12.

**Value**: "common.event.DISTRIBUTED\_ACCOUNT\_LOGOUT"

#### \[h2\]COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID

Indicates that the token of a distributed account is invalid.

When the token of a distributed account is invalid, the event notification service is triggered to publish this event carrying the system account ID.

APIs related to this event: **setOsAccountDistributedInfo** and **updateOsAccountDistributedInfo** (discarded), and **setOsAccountDistributedInfoByLocalId**. The first two are public APIs, and the last one is a system API. For details, see [@ohos.account.distributedAccount (Distributed Account Management)](../../account-management/ohos-account-distributedaccount-distributed-account-management/document.md).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 12.

**Value**: "common.event.DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID"

#### \[h2\]COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOFF

Indicates that a distributed account is deregistered.

When a distributed account is deregistered, the event notification service is triggered to publish this event carrying the system account ID.

APIs related to this event: **setOsAccountDistributedInfo** and **updateOsAccountDistributedInfo** (discarded), and **setOsAccountDistributedInfoByLocalId**. The first two are public APIs, and the last one is a system API. For details, see [@ohos.account.distributedAccount (Distributed Account Management)](../../account-management/ohos-account-distributedaccount-distributed-account-management/document.md).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 12.

**Value**: "common.event.DISTRIBUTED\_ACCOUNT\_LOGOFF"

#### \[h2\]COMMON\_EVENT\_SCREEN\_LOCKED

Indicates that the screen has been locked.

When the screen is locked, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 11.

**Value**: usual.event.SCREEN\_LOCKED

#### \[h2\]COMMON\_EVENT\_SCREEN\_UNLOCKED

Indicates that the screen has been unlocked.

When the screen is unlocked, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 11.

**Value**: usual.event.SCREEN\_UNLOCKED

#### \[h2\]COMMON\_EVENT\_USER\_PRESENT(deprecated)

Indicates the action of a common event that the user unlocks the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/O3AimWZlS4-NZO8jJlRQyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53C2A12B7258964261E1739BF3238A30CB37B9B0D94FA04EF9655CACDC8E6E71)

This API is deprecated since API Version 10 and replaced by [COMMON\_EVENT\_SCREEN\_UNLOCKED](#common_event_screen_unlocked).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.USER\_PRESENT

#### \[h2\]COMMON\_EVENT\_BATTERY\_CHANGED

Indicates that the charging state, level, and other information about the battery have changed.

When any of the following information changes, the event notification service is triggered to publish this event: battery level, battery temperature, battery health status, type of the charger connected to the device, maximum current of the charger, maximum voltage of the charger, battery charging status, number of charging times, total battery capacity, remaining battery capacity, battery model, and battery charging type.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.BATTERY\_CHANGED"

#### \[h2\]COMMON\_EVENT\_BATTERY\_LOW

Indicates that the battery level is low.

When the battery level drops to lower than the low battery level set for the device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.BATTERY\_LOW"

#### \[h2\]COMMON\_EVENT\_BATTERY\_OKAY

Indicates that the battery level is normal.

When the battery level changes from the low level to normal level, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.BATTERY\_OKAY"

#### \[h2\]COMMON\_EVENT\_POWER\_CONNECTED

Indicates that the device is connected to an external power supply.

When the device connects to an external charger, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.POWER\_CONNECTED"

#### \[h2\]COMMON\_EVENT\_POWER\_DISCONNECTED

Indicates that the device is disconnected from the external power supply.

When the device is disconnected from the external power supply, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.POWER\_DISCONNECTED"

#### \[h2\]COMMON\_EVENT\_DISCHARGING

Indicates that the system stops charging the battery.

When the system stops charging the battery, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.DISCHARGING"

#### \[h2\]COMMON\_EVENT\_CHARGING

Indicates that the system starts charging the battery.

When the system starts charging the battery, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.CHARGING"

#### \[h2\]COMMON\_EVENT\_CHARGE\_IDLE\_MODE\_CHANGED10+

Indicates that the device enters the charging idle mode.

When the device starts charging in idle mode, and the temperature rise is acceptable, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.CHARGE\_IDLE\_MODE\_CHANGED"

#### \[h2\]COMMON\_EVENT\_SHUTDOWN

Indicates that the device is being shut down and the final shutdown will proceed.

When the device is being shut down until it is powered off, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.SHUTDOWN"

#### \[h2\]COMMON\_EVENT\_SCREEN\_OFF

Indicates that a device screen-off initiated by the power service is complete.

When the device screen-off initiated by the power service is complete, the event notification service is triggered to release this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.SCREEN\_OFF"

#### \[h2\]COMMON\_EVENT\_SCREEN\_ON

Indicates that a device screen-on initiated by the power service is complete.

When the device screen-on initiated by the power service is complete, the event notification service is triggered to release this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.SCREEN\_ON"

#### \[h2\]COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED

Indicates that the system power-saving mode has changed.

When the system power saving mode changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.POWER\_SAVE\_MODE\_CHANGED"

#### \[h2\]COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED

Indicates that the device's thermal level has changed.

When the device's thermal level changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.THERMAL\_LEVEL\_CHANGED"

#### \[h2\]COMMON\_EVENT\_ENTER\_FORCE\_SLEEP12+

Indicates that the device is about to enter the forced sleep mode.

When the device is about to enter the forced sleep mode, the event notification service is triggered to publish this event. This event should be processed within one second.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.ENTER\_FORCE\_SLEEP"

#### \[h2\]COMMON\_EVENT\_EXIT\_FORCE\_SLEEP12+

Indicates that the device exits the forced sleep mode.

When the device exits the forced sleep mode, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.EXIT\_FORCE\_SLEEP"

#### \[h2\]COMMON\_EVENT\_ENTER\_HIBERNATE15+

Indicates that the device is about to enter the hibernation mode.

When the device is about to enter the hibernation mode, the event notification service is triggered to publish this event. This event should be processed within one second.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.ENTER\_HIBERNATE"

#### \[h2\]COMMON\_EVENT\_EXIT\_HIBERNATE15+

Indicates that the device exits the hibernation mode.

When the device exits the hibernation mode, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.EXIT\_HIBERNATE"

#### Connectivity Kit

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_CHANGE20+

Indicates that the Bluetooth HFP AG connection state changes.

When the Bluetooth HFP AG connection state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.handsfree.ag.CONNECT\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_CHANGE20+

Indicates that the Bluetooth A2DP source connection state changes.

When the Bluetooth A2DP source connection state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.CONNECT\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_CHANGE20+

Indicates that the Bluetooth AVRCP connection state changes.

When the Bluetooth AVRCP connection state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.AVRCP\_CONNECT\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_CHANGE20+

Indicates that the Bluetooth media codec changes.

When the Bluetooth media codec changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.CODEC\_VALUE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE20+

Indicates that the Bluetooth ACL connection state changes.

When the Bluetooth ACL connection state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.ACL\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE\_CHANGE20+

Indicates that the Bluetooth pairing state changes.

When the Bluetooth pairing state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.PAIR\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED

Indicates that the state of the device NFC adapter has changed.

When the state of the device NFC adapter changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.nfc.action.ADAPTER\_STATE\_CHANGED"

#### \[h2\]COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED

Indicates that the NFC RF field is on.

When the NFC RF field becomes available, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.nfc.action.RF\_FIELD\_ON\_DETECTED"

#### \[h2\]COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED

Indicates that the NFC RF field is off.

When the NFC RF field becomes unavailable, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.nfc.action.RF\_FIELD\_OFF\_DETECTED"

#### \[h2\]COMMON\_EVENT\_WIFI\_POWER\_STATE

Indicates that the Wi-Fi state changes.

When the Wi-Fi state changes (such as enabled or disabled), the event notification service is triggered to release the system public event.

State values: **0** indicates that the Wi-Fi is being disabled; **1** indicates that the Wi-Fi has been disabled; **2** indicates that the Wi-Fi is being enabled; **3** indicates that the Wi-Fi has been enabled.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.wifi.POWER\_STATE"

#### \[h2\]COMMON\_EVENT\_WIFI\_SCAN\_FINISHED

Indicates that a Wi-Fi access point is detected and proven to be available.

When a Wi-Fi access point is detected and proven to be available, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.LOCATION

**Value**: "usual.event.wifi.SCAN\_FINISHED"

#### \[h2\]COMMON\_EVENT\_WIFI\_SCAN\_STATE

Indicates that the Wi-Fi access point state has changed.

When the Wi-Fi access point state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.LOCATION

**Value**: "usual.event.wifi.SCAN\_STATE"

#### \[h2\]COMMON\_EVENT\_WIFI\_RSSI\_VALUE

Indicates that the Wi-Fi signal strength (RSSI) has changed.

When the Wi-Fi signal strength (RSSI) changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.RSSI\_VALUE"

#### \[h2\]COMMON\_EVENT\_WIFI\_CONN\_STATE

Indicates that the Wi-Fi connection state has changed.

When the Wi-Fi connection state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.wifi.CONN\_STATE"

#### \[h2\]COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE

Indicates that the Wi-Fi hotspot state has changed.

When the Wi-Fi hotspot state changes, the event notification service is triggered to publish this event.

State values: **2** indicates that the AP is being enabled, **3** indicates that the AP has been enabled; **4** indicates that the AP is being disabled; **5** indicates that the AP has been disabled.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.wifi.HOTSPOT\_STATE"

#### \[h2\]COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN

Indicates that a client has joined the Wi-Fi hotspot of the current device.

When a client joins the Wi-Fi hotspot of the current device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.WIFI\_HS\_STA\_JOIN"

#### \[h2\]COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE

Indicates that the client is disconnected from the Wi-Fi hotspot of the current device.

When a client is disconnected from the Wi-Fi hotspot of the current device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.WIFI\_HS\_STA\_LEAVE"

#### \[h2\]COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE

Indicates that the state of MPLINK (an enhanced Wi-Fi feature) has changed.

When the state of MPLINK changes, the event notification service is triggered to publish this event (not supported yet).

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.wifi.mplink.STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE

Indicates that the Wi-Fi P2P connection state has changed.

When the Wi-Fi P2P connection state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION

**Value**: "usual.event.wifi.p2p.CONN\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED

Indicates that the Wi-Fi P2P state has changed.

When the Wi-Fi P2P state changes, the event notification service is triggered to publish this event.

State values: **2** indicates that the P2P is being enabled, **3** indicates that the P2P has been enabled; **4** indicates that the P2P is being disabled; **5** indicates that the P2P has been disabled.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.p2p.STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED

Indicates that the state of the Wi-Fi P2P peer device has changed.

When the state of the Wi-Fi P2P peer device changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value:** "usual.event.wifi.p2p.DEVICES\_CHANGE"

#### \[h2\]COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED

Indicates that the Wi-Fi P2P discovery state has changed.

When the Wi-Fi P2P discovery state changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.p2p.PEER\_DISCOVERY\_STATE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED

Indicates that the state of the Wi-Fi P2P local device has changed.

When the state of the Wi-Fi P2P local device changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.p2p.CURRENT\_DEVICE\_CHANGE"

#### \[h2\]COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED

Indicates that the Wi-Fi P2P group information has changed.

When the Wi-Fi P2P group information changes, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**Value**: "usual.event.wifi.p2p.GROUP\_STATE\_CHANGED"

#### MDM Kit

#### \[h2\]COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED

Indicates that the browser hosting policy has been changed.

When the browser hosting policy changes, the event notification service is triggered to publish this system common event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.MANAGED\_BROWSER\_POLICY\_CHANGED"

#### Localization Kit

#### \[h2\]COMMON\_EVENT\_LOCALE\_CHANGED

Indicates that the system language is set.

When the system language is set, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.LOCALE\_CHANGED

#### Network Kit

#### \[h2\]COMMON\_EVENT\_CONNECTIVITY\_CHANGE10+

Indicates that the network connection state has changed.

When the (Ethernet, Wi-Fi, or cellular) network connection state changes (disconnected, connecting, or connected), the event notification service is triggered to publish this event.

The following table lists the enum values and their corresponding connection status.

| Value | Connection State |
| :-- | :-- |
| 2 | Connecting. |
| 3 | Connected. |
| 4 | Disconnecting. |
| 5 | Disconnected. |

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Atomic service API**: This API can be used in atomic services since API version 11.

**Value**: usual.event.CONNECTIVITY\_CHANGE

#### \[h2\]COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED10+

Indicates that the airplane mode state has changed.

When the airplane mode is enabled or disabled, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.AIRPLANE\_MODE

#### \[h2\]COMMON\_EVENT\_HTTP\_PROXY\_CHANGE10+

Indicates that the HTTP proxy configuration has changed.

When the configuration information of the system global proxy or HTTP proxy on various networks (such as Ethernet, Wi-Fi, and cellular networks) changes, the event notification service is triggered to release the system common event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.HTTP\_PROXY\_CHANGE

#### Telephony Kit

This topic lists the common system events provided by the telephony subsystem to applications.

#### \[h2\]COMMON\_EVENT\_SIM\_STATE\_CHANGED10+

Indicates that the SIM card status has changed.

When there is a change in the SIM card status of the device, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.SIM\_STATE\_CHANGED

#### \[h2\]COMMON\_EVENT\_CALL\_STATE\_CHANGED10+

Indicates that the call state has been updated.

When the call state of the device is updated, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_TELEPHONY\_STATE (for system apps only)

**Value**: usual.event.CALL\_STATE\_CHANGED

#### \[h2\]COMMON\_EVENT\_NETWORK\_STATE\_CHANGED10+

Indicates that the network state has been updated.

When the network state of the device is updated, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.NETWORK\_STATE\_CHANGED

#### \[h2\]COMMON\_EVENT\_SIGNAL\_INFO\_CHANGED10+

Indicates that the signal information has been updated.

When the signal information of the device is updated, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.SIGNAL\_INFO\_CHANGED

#### AppGallery Kit

This topic lists the common system events provided by the AppGallery Kit to applications.

#### \[h2\]COMMON\_EVENT\_PRIVACY\_STATE\_CHANGED11+

Indicates the privacy state has been changed.

When a user clicks **Agree** in a privacy dialog box, the event notification service is triggered to publish this event.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PRIVACY\_STATE\_CHANGED"

#### Reserved Common Event

Below are reserved common events that are not supported yet.

#### \[h2\]COMMON\_EVENT\_LOCKED\_BOOT\_COMPLETED

(Reserved, not supported yet) Indicates that the guidance is complete and the system is loaded, but the screen is still locked.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.LOCKED\_BOOT\_COMPLETED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_FIRST\_LAUNCH

(Reserved, not supported yet) Indicates an initial start of an application after installation.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_FIRST\_LAUNCH"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_NEEDS\_VERIFICATION

(Reserved, not supported yet) Indicates that a package is sent by the system verifier when the package needs verification.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_NEEDS\_VERIFICATION"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_VERIFIED

(Reserved, not supported yet) Indicates that a package is sent by the system verifier when the package is verified.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_VERIFIED"

#### \[h2\]COMMON\_EVENT\_PACKAGE\_REPLACED

(Reserved, not supported yet) Indicates the action of a common event that a new version of an installed application package has replaced the previous one on the device. Data contains the name of the package.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGE\_REPLACED"

#### \[h2\]COMMON\_EVENT\_MY\_PACKAGE\_REPLACED

(Reserved, not supported yet) Indicates the action of a common event that a new version of an installed application package has replaced the previous one on the device. This event does not contain additional data and is sent only to the replaced application.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.MY\_PACKAGE\_REPLACED"

#### \[h2\]COMMON\_EVENT\_PACKAGES\_UNSUSPENDED

(Reserved, not supported yet) Indicates that the package has been unsuspended.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.PACKAGES\_UNSUSPENDED"

#### \[h2\]COMMON\_EVENT\_CLOSE\_SYSTEM\_DIALOGS

(Reserved, not supported yet) Indicates that a user closes a temporary system dialog box.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.CLOSE\_SYSTEM\_DIALOGS"

#### \[h2\]COMMON\_EVENT\_UID\_REMOVED

(Reserved, not supported yet) Indicates that a user ID has been removed from the system.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.UID\_REMOVED"

#### \[h2\]COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_AVAILABLE

(Reserved, not supported yet) Indicates that applications installed on the external storage become available for the system.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.EXTERNAL\_APPLICATIONS\_AVAILABLE"

#### \[h2\]COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_UNAVAILABLE

(Reserved, not supported yet) Indicates that applications installed on the external storage become unavailable for the system.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.EXTERNAL\_APPLICATIONS\_UNAVAILABLE"

#### \[h2\]COMMON\_EVENT\_CONFIGURATION\_CHANGED

(Reserved, not supported yet) Indicates that the device state (for example, orientation and locale) has changed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.CONFIGURATION\_CHANGED"

#### \[h2\]COMMON\_EVENT\_DRIVE\_MODE

(Reserved, not supported yet) Indicates that the system is in driving mode.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.DRIVE\_MODE"

#### \[h2\]COMMON\_EVENT\_HOME\_MODE

(Reserved, not supported yet) Indicates that the system is in home mode.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.HOME\_MODE"

#### \[h2\]COMMON\_EVENT\_OFFICE\_MODE

(Reserved, not supported yet) Indicates that the system is in office mode.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.OFFICE\_MODE"

#### \[h2\]COMMON\_EVENT\_USER\_STARTED

(Reserved, not supported yet) Indicates that the user has been started.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.USER\_STARTED"

#### \[h2\]COMMON\_EVENT\_USER\_BACKGROUND

(Reserved, not supported yet) Indicates that the user has been brought to the background.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.USER\_BACKGROUND"

#### \[h2\]COMMON\_EVENT\_USER\_STARTING

(Reserved, not supported yet) Indicates that the user is going to be started.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (for system applications only)

**Value**: "usual.event.USER\_STARTING"

#### \[h2\]COMMON\_EVENT\_USER\_STOPPING

(Reserved, not supported yet) Indicates that the user is going to be stopped.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (for system applications only)

**Value**: "usual.event.USER\_STOPPING"

#### \[h2\]COMMON\_EVENT\_USER\_STOPPED

(Reserved, not supported yet) Indicates that the user has been stopped.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.USER\_STOPPED"

#### \[h2\]COMMON\_EVENT\_DISK\_REMOVED

(Reserved, not supported yet) Indicates that an external storage device was removed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.STORAGE\_MANAGER (for system applications only)

**Value**: "usual.event.data.DISK\_REMOVED"

#### \[h2\]COMMON\_EVENT\_DISK\_UNMOUNTED

(Reserved, not supported yet) Indicates that an external storage device was unmounted.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.STORAGE\_MANAGER (for system applications only)

**Value**: "usual.event.data.DISK\_UNMOUNTED"

#### \[h2\]COMMON\_EVENT\_DISK\_MOUNTED

(Reserved, not supported yet) Indicates that an external storage device was mounted.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.STORAGE\_MANAGER (for system applications only)

**Value**: "usual.event.data.DISK\_MOUNTED"

#### \[h2\]COMMON\_EVENT\_DISK\_BAD\_REMOVAL

(Reserved, not supported yet) Indicates that an external storage device was removed without being unmounted.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.STORAGE\_MANAGER (for system applications only)

**Value**: "usual.event.data.DISK\_BAD\_REMOVAL"

#### \[h2\]COMMON\_EVENT\_DISK\_UNMOUNTABLE

(Reserved, not supported yet) Indicates that an external storage device becomes unmountable.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.STORAGE\_MANAGER (for system applications only)

**Value**: "usual.event.data.DISK\_UNMOUNTABLE"

#### \[h2\]COMMON\_EVENT\_DISK\_EJECT

(Reserved, not supported yet) Indicates that an external storage device was ejected.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.STORAGE\_MANAGER (for system applications only)

**Value**: "usual.event.data.DISK\_EJECT"

#### \[h2\]COMMON\_EVENT\_DATE\_CHANGED

(Reserved, not supported yet) Indicates that the system time has changed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: usual.event.DATE\_CHANGED

#### \[h2\]COMMON\_EVENT\_USB\_ACCESSORY\_ATTACHED

Indicates that a USB accessory has been attached.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.hardware.usb.action.USB\_ACCESSORY\_ATTACHED"

#### \[h2\]COMMON\_EVENT\_USB\_ACCESSORY\_DETACHED

Indicates that a USB accessory has been detached.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.hardware.usb.action.USB\_ACCESSORY\_DETACHED"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates the common event about the connection state of Bluetooth handsfree communication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XRfrLw2YSj-d4bpmWxMAPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18A5BE57D3DE52E40F6833DABDFF433D30243FA30865A8C7F20CFDD4F028946A)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_CHANGE](#common_event_bluetooth_handsfree_ag_connect_state_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.handsfree.ag.CONNECT\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CURRENT\_DEVICE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the device connected to the Bluetooth handsfree is active.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/EeV7qQPrSDGySSuEIre8eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D17C2E9ACE0814A4BB2583F3DD2604BF01F89A339460CE1C8C4E48FCAD30B8D5)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.handsfree.ag.CURRENT\_DEVICE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_AUDIO\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the connection state of Bluetooth A2DP has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/HWfVV3mpR4W1BazsY9D2eA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F1B1770F6795186F572344E750B0F444EC3C7EB6FD8A446E4A3B15120C19E77)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.handsfree.ag.AUDIO\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates the common event about the connection state of Bluetooth A2DP.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Kha5ytb3Ru-T8UtjNP4OMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=512CE8508D0203AB3DE05ED6F62BFF875AAC1E0AFDCEE42761C761FF7FAA2897)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_CHANGE](#common_event_bluetooth_a2dpsource_connect_state_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.CONNECT\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CURRENT\_DEVICE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the device connected using Bluetooth A2DP is active.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/SBtabxEUSXGji4cHmFz-5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21369D277D38161013CAF1E7D8D6553F7A4BE78C7D524336C74A0B301EACEDD1)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.CURRENT\_DEVICE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the AVRCP connection state of Bluetooth A2DP has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/42dtvXu5S_q6EQuqKnr_dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16157B4678E46579EB18C4C7F09C837ADB6975E7B426F9AC98ECA3AD1C89D844)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_CHANGE](#common_event_bluetooth_a2dpsource_avrcp_connect_state_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.AVRCP\_CONNECT\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAYING\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the playing state of Bluetooth A2DP has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/tAqj2DpRQBSQ4piG4gMGaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB57EA6432CF6B5B5208E5EC69A198E1E16D8161973BE27F4622B70B764C8BC5)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.PLAYING\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the audio codec state of Bluetooth A2DP has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/VzlZ10VXQ5S4QPjtVHcCnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60381E533B8E1D64B7D40324FAC9B8F8155681851FEABD38D3FF3C67F4376362)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_CHANGE](#common_event_bluetooth_a2dpsource_codec_value_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsource.CODEC\_VALUE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_USER\_FOREGROUND

(Reserved, not supported yet) Indicates that the user has been brought to the foreground.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.USER\_FOREGROUND"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_DISCOVERED(deprecated)

(Reserved, not supported yet) Indicates that a remote Bluetooth device is discovered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/bBWbuAnxQay4A3ZwJlbFqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACE962D49B7D20D5D9123700411282A54C853DF13098FC2FF7CB7D2D758E7E61)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.LOCATION and ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.DISCOVERED"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CLASS\_VALUE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the Bluetooth class of a remote Bluetooth device has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Y9wOd1OZTjaIXtfxtGBG7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A49FE1ABE463525D176ABC530FC943EFD38691BCC9A33541D7695FF61316B6FE)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.CLASS\_VALUE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_CONNECTED(deprecated)

(Reserved, not supported yet) Indicates that a low-ACL connection has been established with a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/4hLjYESsTY64a3iXN49H_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=513FB4A649F0C3B97C482A5D501D33577B19C2378F5A0E7B66BBF970003F59F3)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE](#common_event_bluetooth_remotedevice_acl_state_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.remotedevice.ACL\_CONNECTED"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_DISCONNECTED(deprecated)

(Reserved, not supported yet) Indicates that a low-ACL connection has been disconnected from a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/QdJMc2BMQNO8fCPyz7qa8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3284A169AA951F5CEB57EB11488C2D48F2254BD41B49E94588EC974A21AF48A)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE](#common_event_bluetooth_remotedevice_acl_state_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.ACL\_DISCONNECTED"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_NAME\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the friendly name of a remote Bluetooth device is retrieved for the first time or has changed since the last retrieval.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/iQedV_DiSY6NQXCj8hbgvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CCBA64876BF6DD9F225BB388FA7D9277220F06838ECDAB360FFB8D327B80DEC)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.NAME\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE(deprecated)

(Reserved, not supported yet) Indicates that the connection state of a remote Bluetooth device has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/erByi_yuTpO3m4Kpw0BWtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75E8D69E2AAAC569612921A21D6D42D40570FE73C3D1015D6C9EB60FF215B3ED)

This API is supported since API version 9 and deprecated since API version 20. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE\_CHANGE](#common_event_bluetooth_remotedevice_pair_state_change20) instead.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.PAIR\_STATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_BATTERY\_VALUE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the battery level of a remote Bluetooth device is retrieved for the first time or has changed since the last retrieval.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/nemHl7MMR4ylXLOw5grRMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A77D4C6A85DC772349EB75C67AB65B116B52D791E31F65519B89967CD8C216B5)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.BATTERY\_VALUE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_SDP\_RESULT(deprecated)

(Reserved, not supported yet) Indicates the common event about the SDP state of a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/maq3to2MQsaeYCxSNnQ7FQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C04FD5EDD8D86EB705F7F66AF8E3DF7912AD5572F7CB74A23DDACB1B040F0E91)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.remotedevice.SDP\_RESULT"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_UUID\_VALUE(deprecated)

Indicates the action of a common event about the UUID connection state of a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Bf44CxAMRciMfo7n8zYsSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDC13A4560634BB398062E937718A34EFC61C75C7CE64DB9075DBD0E864A8BF8)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.UUID\_VALUE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_REQ(deprecated)

(Reserved, not supported yet) Indicates the common event about the pairing request from a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5lnEcY0XSe23-LGJ71G9oQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C994326BC5D899A3CFA6E723D1E820BEFCACC86430A418B20E62DDDEA8404037)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.DISCOVER\_BLUETOOTH

**Value**: "usual.event.bluetooth.remotedevice.PAIRING\_REQ"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_CANCEL(deprecated)

(Reserved, not supported yet) Indicates that Bluetooth pairing is canceled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/3spVUxiPT8aSxKFqd9sB-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D20267E261469B02D172ED043B0DCEDBC7E38F6F2258A41398C7E7E7D039753)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.remotedevice.PAIRING\_CANCEL"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REQ(deprecated)

(Reserved, not supported yet) Indicates the common event about the connection request from a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/I9_ObLwpSlidkzh5G-aFIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4321B076F8A5AE5D5FDE624F892407A2F33F06341255628852A2C2B83D9A17C)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.remotedevice.CONNECT\_REQ"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REPLY(deprecated)

(Reserved, not supported yet) Indicates the common event about the response to the connection request from a remote Bluetooth device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/EZP985EaRTm8B2cSRvzZCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=441B603CC6BE22BE3855922EF3AD7D1BEF305E107840BE9DC8C13401AD880250)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.remotedevice.CONNECT\_REPLY"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_CANCEL(deprecated)

(Reserved, not supported yet) Indicates that the connection to a remote Bluetooth device has been canceled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/uMKsJ7PwQkOVAidqUWzsjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE2B25E8CB632042E3731BF7D4A5A01080E12F544AB11AA930B75EAC0AB2B6FB)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.remotedevice.CONNECT\_CANCEL"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_CONNECT\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the connection state of a Bluetooth handsfree has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/NXtao26OQkiHLJ0grdJZbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E7BE2DF9790B3E29B2ED236D7C81705231C99A300719B453007905BBE6DF5E2)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.handsfreeunit.CONNECT\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AUDIO\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the audio state of a Bluetooth handsfree has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/HHyyPIAVRqqdLX-VSYW8_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1646572425295366BA8B5CBF86FB550295C722C4735AD439B918B09E27336427)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.handsfreeunit.AUDIO\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_COMMON\_EVENT(deprecated)

(Reserved, not supported yet) Indicates that the audio gateway state of a Bluetooth handsfree has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/hwLZHUBhRiCZgou0DrSgTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A2BEF4C42CEAABA3C3527FD346372D3809AC44C552B79839F555D10678C6FE4)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.handsfreeunit.AG\_COMMON\_EVENT"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_CALL\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the calling state of a Bluetooth handsfree has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/aiFmAfMMSnenfvbpF-NP6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0540185D89B36560B29BC4547F5BD0CD2AEAA8114D2F9C6DE250DF46B24CB050)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.handsfreeunit.AG\_CALL\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_STATE\_UPDATE(deprecated)

Indicates that the state of a Bluetooth adapter has been changed, for example, Bluetooth has been enabled or disabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/hhtOajSBTKa_cUt2MjCC-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=881809C5DE0A736B5BFEAA0A74598CFDACBA2793F01E16F802B652237636F11A)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.host.STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISCOVERABLE(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/IFVxSj74SKGTwx7ZgSwEbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=658E555C6A2E2E7D13359669B640B7F28A23C1B4A68C3EA41E5549BB5F79995C)

This API is supported since API version 9 and deprecated since API version 20.

(Reserved, not supported yet) Indicates the common event about the request for the user to allow Bluetooth device scanning.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.bluetooth.host.REQ\_DISCOVERABLE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_ENABLE(deprecated)

(Reserved, not supported yet) Indicates the common event about the request for the user to enable Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Z98HoUVoSzel0rKt7kXRNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73FEAC260323670CA6EB20CC7629E9182FB813775A1D74C87CB9666E15E9D50A)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.host.REQ\_ENABLE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISABLE(deprecated)

(Reserved, not supported yet) Indicates the common event about the request for the user to disable Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9EK1T5WkRySIxYUzYZeTjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C0D71A7D1562F37CB2B66891068E91856133952A1213884B459C81837CD4B15)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.host.REQ\_DISABLE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the Bluetooth scanning mode of a device has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/nghuuF5vRxaJMgqwB03OUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7359E961351C3D6FC2AB6C56B80613EA543CB04A19B56D1C34434090B84E0A1B)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.host.SCAN\_MODE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_STARTED(deprecated)

Indicates that the Bluetooth scanning has been started on the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/JFEjP9xNTu24cJw5ZS6tCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59859E67B2B842BFEEEE2C20DCB085E011113085141C2C370AE1835A45B70FD5)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.host.DISCOVERY\_STARTED"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_FINISHED(deprecated)

Indicates that the Bluetooth scanning is finished on the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/ghQBk0ESSOu8w_CNtIPrIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97D4F5E6C7231EBBFF99DF5C50CE592105C0EAD7BA6F6B25F5C68495F391FB9A)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.host.DISCOVERY\_FINISHED"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_HOST\_NAME\_UPDATE(deprecated)

Indicates that the Bluetooth adapter name of the device has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Vj7u-fVQSS6ObXEDd5MPww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA590697D3CE28CC506A8F9F89515578E7270CAE31108D284D46D496D9EFE66E)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.ACCESS\_BLUETOOTH

**Value**: "usual.event.bluetooth.host.NAME\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_CONNECT\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the connection state of Bluetooth A2DP has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/zjO9rcP-QzCWJmD87YPZxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0888D83B14F6D2F8AE493F2CF0C1D62DE801D3CDFD1946696ADA48DA45DC9CC1)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsink.CONNECT\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_PLAYING\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the playing state of Bluetooth A2DP has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/wfe_O_yUSByweQf8MEZo-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4808528E5E800F06F099C9F4FB9FCD9E80ACD97DD041561131CBFB62E6D0F883)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsink.PLAYING\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_AUDIO\_STATE\_UPDATE(deprecated)

(Reserved, not supported yet) Indicates that the audio state of Bluetooth A2DP Sink has changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/tcI1nqKkRo6TLrJiWCG4Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D205BE72BD8E1D6096E7E821C714722F76B3CCDE5AE7510D0D29C48546E9DC65)

This API is supported since API version 9 and deprecated since API version 20.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.USE\_BLUETOOTH

**Value**: "usual.event.bluetooth.a2dpsink.AUDIO\_STATE\_UPDATE"

#### \[h2\]COMMON\_EVENT\_ABILITY\_ADDED

(Reserved, not supported yet) Indicates that an ability has been added.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.LISTEN\_BUNDLE\_CHANGE

**Value**: "usual.event.ABILITY\_ADDED"

#### \[h2\]COMMON\_EVENT\_ABILITY\_REMOVED

(Reserved, not supported yet) Indicates that an ability has been removed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.LISTEN\_BUNDLE\_CHANGE

**Value**: "usual.event.ABILITY\_REMOVED"

#### \[h2\]COMMON\_EVENT\_ABILITY\_UPDATED

(Reserved, not supported yet) Indicates that an ability has been updated.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.LISTEN\_BUNDLE\_CHANGE

**Value**: "usual.event.ABILITY\_UPDATED"

#### \[h2\]COMMON\_EVENT\_LOCATION\_MODE\_STATE\_CHANGED

(Reserved, not supported yet) Indicates that the location mode of the system has changed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.location.MODE\_STATE\_CHANGED"

#### \[h2\]COMMON\_EVENT\_IVI\_SLEEP

(Reserved, not supported yet) Indicates that the in-vehicle infotainment (IVI) system of a vehicle is sleeping.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_SLEEP"

#### \[h2\]COMMON\_EVENT\_IVI\_PAUSE

(Reserved, not supported yet) Indicates that the IVI system of a vehicle has entered sleep mode and the playing application is instructed to stop playback.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_PAUSE"

#### \[h2\]COMMON\_EVENT\_IVI\_STANDBY

(Reserved, not supported yet) Indicates that a third-party application is instructed to pause the current work.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_STANDBY"

#### \[h2\]COMMON\_EVENT\_IVI\_LASTMODE\_SAVE

(Reserved, not supported yet) Indicates that a third-party application is instructed to save its last mode.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_LASTMODE\_SAVE"

#### \[h2\]COMMON\_EVENT\_IVI\_VOLTAGE\_ABNORMAL

(Reserved, not supported yet) Indicates that the voltage of the vehicle's power system is abnormal.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_VOLTAGE\_ABNORMAL"

#### \[h2\]COMMON\_EVENT\_IVI\_HIGH\_TEMPERATURE

(Reserved, not supported yet) Indicates that the temperature of the IVI system is high.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_HIGH\_TEMPERATURE"

#### \[h2\]COMMON\_EVENT\_IVI\_EXTREME\_TEMPERATURE

(Reserved, not supported yet) Indicates that the temperature of the IVI system is extremely high.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_EXTREME\_TEMPERATURE"

#### \[h2\]COMMON\_EVENT\_IVI\_TEMPERATURE\_ABNORMAL

(Reserved, not supported yet) Indicates that the IVI system has an extreme temperature.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_TEMPERATURE\_ABNORMAL"

#### \[h2\]COMMON\_EVENT\_IVI\_VOLTAGE\_RECOVERY

(Reserved, not supported yet) Indicates that the voltage of the vehicle's power system is restored to normal.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_VOLTAGE\_RECOVERY"

#### \[h2\]COMMON\_EVENT\_IVI\_TEMPERATURE\_RECOVERY

(Reserved, not supported yet) Indicates that the temperature of the IVI system is restored to normal.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_TEMPERATURE\_RECOVERY"

#### \[h2\]COMMON\_EVENT\_IVI\_ACTIVE

(Reserved, not supported yet) Indicates that the battery service is active.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "common.event.IVI\_ACTIVE"

#### \[h2\]COMMON\_EVENT\_VISIBLE\_ACCOUNTS\_UPDATED

(Reserved, not supported yet) Indicates that the account visibility changed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.GET\_APP\_ACCOUNTS (for system applications only)

**Value**: "usual.event.data.VISIBLE\_ACCOUNTS\_UPDATED"

#### \[h2\]COMMON\_EVENT\_ACCOUNT\_DELETED

(Reserved, not supported yet) Indicates that the account was deleted.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (for system applications only)

**Value**: "usual.event.data.ACCOUNT\_DELETED"

#### \[h2\]COMMON\_EVENT\_FOUNDATION\_READY

(Reserved, not supported yet) Indicates that the foundation is ready.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: ohos.permission.RECEIVER\_STARTUP\_COMPLETED (for system applications only)

**Value**: "usual.event.data.FOUNDATION\_READY"

#### \[h2\]COMMON\_EVENT\_SPN\_INFO\_CHANGED

Indicates that the SPN information had changed.

**System capability**: SystemCapability.Notification.CommonEvent

**Required permissions**: none

**Value**: "usual.event.SPN\_INFO\_CHANGED"
