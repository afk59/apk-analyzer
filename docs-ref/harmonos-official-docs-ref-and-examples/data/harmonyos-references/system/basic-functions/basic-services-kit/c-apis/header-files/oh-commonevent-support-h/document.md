# oh\_commonevent\_support.h

#### Overview

Provides common event constants defined by the system.

**Library**: libohcommonevent.so

**File to include**: <BasicServicesKit/oh\_commonevent\_support.h>

**System capability**: SystemCapability.Notification.CommonEvent

**Since**: 12

**Related modules:** [OH\_CommonEvent](../../modules/oh-commonevent/document.md)

#### Summary

#### \[h2\]Constants

| Name | Description |
| :-- | :-- |
| static const char \* const COMMON\_EVENT\_SHUTDOWN = "usual.event.SHUTDOWN" | 
Indicates the common event that the device is being shut down and the final shutdown will proceed.

**Since**: 12

**System capability**: SystemCapability.Notification.CommonEvent

 |
| static const char \* const COMMON\_EVENT\_BATTERY\_CHANGED = "usual.event.BATTERY\_CHANGED" | 

Indicates the common event that the charging state, level, and other information about the battery have changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_BATTERY\_LOW = "usual.event.BATTERY\_LOW" | 

Indicates the common event that the battery level is low.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_BATTERY\_OKAY = "usual.event.BATTERY\_OKAY" | 

Indicates the common event that the battery exits the low state.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_POWER\_CONNECTED = "usual.event.POWER\_CONNECTED" | 

Indicates the common event that the device is connected to an external power supply.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_POWER\_DISCONNECTED = "usual.event.POWER\_DISCONNECTED" | 

Indicates the common event that the device is disconnected from the external power supply.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SCREEN\_OFF = "usual.event.SCREEN\_OFF" | 

Indicates the common event that the device screen is off and the device is sleeping.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SCREEN\_ON = "usual.event.SCREEN\_ON" | 

Indicates the common event that the device screen is on and the device is in interactive state.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_ENTER\_HIBERNATE = "usual.event.ENTER\_HIBERNATE" | 

Indicates the common event that the device is about to enter the hibernation mode.

**Since**: 15

 |
| static const char \* const COMMON\_EVENT\_EXIT\_HIBERNATE = "usual.event.EXIT\_HIBERNATE" | 

Indicates the common event that the device exits the hibernation mode.

**Since**: 15

 |
| static const char \* const COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED = "usual.event.THERMAL\_LEVEL\_CHANGED" | 

Indicates the common event that the device's thermal level has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_TIME\_TICK = "usual.event.TIME\_TICK" | 

Indicates the common event that the system time has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_TIME\_CHANGED = "usual.event.TIME\_CHANGED" | 

Indicates the common event that the system time has been set.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_TIMEZONE\_CHANGED = "usual.event.TIMEZONE\_CHANGED" | 

Indicates the common event that the system time zone has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_ADDED = "usual.event.PACKAGE\_ADDED" | 

Indicates the common event that a new application package has been installed on the device.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_REMOVED = "usual.event.PACKAGE\_REMOVED" | 

Indicates the common event that an installed application has been uninstalled from the device with the application data retained.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_BUNDLE\_REMOVED = "usual.event.BUNDLE\_REMOVED" | 

Indicates the common event that an installed bundle has been uninstalled from the device with the application data retained.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED = "usual.event.PACKAGE\_FULLY\_REMOVED" | 

Indicates the common event that an installed application, including both the application data and code, has been completely uninstalled from the device.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_CHANGED = "usual.event.PACKAGE\_CHANGED" | 

Indicates the common event that an application package has been changed (for example, a component in the package has been enabled or disabled).

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_RESTARTED = "usual.event.PACKAGE\_RESTARTED" | 

Indicates the common event that the user has restarted the application package and killed all its processes.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED = "usual.event.PACKAGE\_DATA\_CLEARED" | 

Indicates the common event that the user cleared the application package data.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED = "usual.event.PACKAGE\_CACHE\_CLEARED" | 

Indicates the common event that the user has cleared the application package data cache.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_PACKAGES\_SUSPENDED = "usual.event.PACKAGES\_SUSPENDED" | 

Indicates the common event that application packages have been suspended.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED = "usual.event.MY\_PACKAGE\_SUSPENDED" | 

Indicates the common event that application packages are suspended.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED = "usual.event.MY\_PACKAGE\_UNSUSPENDED" | 

Indicates the common event that application packages have not been suspended.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_LOCALE\_CHANGED = "usual.event.LOCALE\_CHANGED" | 

Indicates the common event that the device locale has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE = "usual.event.MANAGE\_PACKAGE\_STORAGE" | 

Indicates the common event that the device storage is insufficient.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_USER\_UNLOCKED = "usual.event.USER\_UNLOCKED" | 

Indicates the common event that the credential-encrypted storage has been unlocked for the current user when the device is unlocked upon restart.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT = "common.event.DISTRIBUTED\_ACCOUNT\_LOGOUT" | 

Indicates the common event that a distributed account is successfully logged out.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID = "common.event.DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID" | 

Indicates the common event that the token of a distributed account is invalid.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOFF = "common.event.DISTRIBUTED\_ACCOUNT\_LOGOFF" | 

Indicates the common event that a distributed account is deregistered.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_POWER\_STATE = "usual.event.wifi.POWER\_STATE" | 

Indicates the common event that the Wi-Fi state has changed to a new state, such as enabled or disabled.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_SCAN\_FINISHED = "usual.event.wifi.SCAN\_FINISHED" | 

Indicates the common event that the Wi-Fi access point has been scanned and proven to be available.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_RSSI\_VALUE = "usual.event.wifi.RSSI\_VALUE" | 

Indicates the common event that the Wi-Fi signal strength (RSSI) has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_CONN\_STATE = "usual.event.wifi.CONN\_STATE" | 

Indicates the common event that the Wi-Fi connection state has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE = "usual.event.wifi.HOTSPOT\_STATE" | 

Indicates the common event that the Wi-Fi hotspot state has changed to a new state, such as enabled or disabled.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN = "usual.event.wifi.WIFI\_HS\_STA\_JOIN" | 

Indicates the common event that a client has joined the Wi-Fi hotspot of the current device.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE = "usual.event.wifi.WIFI\_HS\_STA\_LEAVE" | 

Indicates the common event that a client has disconnected from the Wi-Fi hotspot of the current device.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE = "usual.event.wifi.mplink.STATE\_CHANGE" | 

Indicates the common event that the state of MPLINK (an enhanced Wi-Fi feature) has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE = "usual.event.wifi.p2p.CONN\_STATE\_CHANGE" | 

Indicates the common event that the Wi-Fi P2P connection state has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED = "usual.event.wifi.p2p.STATE\_CHANGE" | 

Indicates the common event that the Wi-Fi P2P state has changed to enabled or disabled.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED = "usual.event.wifi.p2p.DEVICES\_CHANGE" | 

Indicates the common event that the state of the Wi-Fi P2P peer device has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED = "usual.event.wifi.p2p.PEER\_DISCOVERY\_STATE\_CHANGE" | 

Indicates the common event that the Wi-Fi P2P discovery state has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED = "usual.event.wifi.p2p.CURRENT\_DEVICE\_CHANGE" | 

Indicates the common event that the state of the Wi-Fi P2P local device has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED = "usual.event.wifi.p2p.GROUP\_STATE\_CHANGED" | 

Indicates the common event that the Wi-Fi P2P group information has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED = "usual.event.nfc.action.ADAPTER\_STATE\_CHANGED" | 

Indicates the common event that the state of the device NFC adapter has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED = "usual.event.nfc.action.RF\_FIELD\_ON\_DETECTED" | 

Indicates the common event that the NFC RF field is on.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED = "usual.event.nfc.action.RF\_FIELD\_OFF\_DETECTED" | 

Indicates the common event that the NFC RF field is off.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_DISCHARGING = "usual.event.DISCHARGING" | 

Indicates the common event that the system stops charging the battery.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_CHARGING = "usual.event.CHARGING" | 

Indicates the common event that the system starts charging the battery.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED = "usual.event.DEVICE\_IDLE\_MODE\_CHANGED" | 

Indicates the common event that the system standby mode has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_CHARGE\_IDLE\_MODE\_CHANGED = "usual.event.CHARGE\_IDLE\_MODE\_CHANGED" | 

Indicates the common event that the device enters the charging idle mode.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED = "usual.event.POWER\_SAVE\_MODE\_CHANGED" | 

Indicates the common event that the system power saving mode is changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_USB\_STATE = "usual.event.hardware.usb.action.USB\_STATE" | 

Indicates the common event that the USB device state has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_USB\_PORT\_CHANGED = "usual.event.hardware.usb.action.USB\_PORT\_CHANGED" | 

Indicates the common event that the USB port state of the user device has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_USB\_DEVICE\_ATTACHED = "usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED" | 

Indicates the common event that a USB device has been attached when the user device functions as a USB host.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_USB\_DEVICE\_DETACHED = "usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED" | 

Indicates the common event that a USB device has been detached when the user device functions as a USB host.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED = "usual.event.AIRPLANE\_MODE" | 

Indicates the common event that the airplane mode of a device has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SPLIT\_SCREEN = "common.event.SPLIT\_SCREEN" | 

Indicates the common event of screen splitting.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_QUICK\_FIX\_APPLY\_RESULT = "usual.event.QUICK\_FIX\_APPLY\_RESULT" | 

Indicates the common event that a quick fix is applied to an application.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_QUICK\_FIX\_REVOKE\_RESULT = "usual.event.QUICK\_FIX\_REVOKE\_RESULT" | 

Indicates the common event that a quick fix is revoked.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_USER\_INFO\_UPDATED = "usual.event.USER\_INFO\_UPDATED" | 

Indicates the common event that the user information has been updated.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SIM\_STATE\_CHANGED = "usual.event.SIM\_STATE\_CHANGED" | 

Indicates the common event that the SIM card state has been updated.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_CALL\_STATE\_CHANGED = "usual.event.CALL\_STATE\_CHANGED" | 

Indicates the common event that the call state has been updated.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_NETWORK\_STATE\_CHANGED = "usual.event.NETWORK\_STATE\_CHANGED" | 

Indicates the common event that the network state has been updated.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SIGNAL\_INFO\_CHANGED = "usual.event.SIGNAL\_INFO\_CHANGED" | 

Indicates the common event that the signal information has been updated.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SCREEN\_UNLOCKED = "usual.event.SCREEN\_UNLOCKED" | 

Indicates the common event that the screen has been unlocked.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_SCREEN\_LOCKED = "usual.event.SCREEN\_LOCKED" | 

Indicates the common event that the screen has been locked.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_HTTP\_PROXY\_CHANGE = "usual.event.HTTP\_PROXY\_CHANGE" | 

Indicates the common event that the HTTP proxy configuration has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_CONNECTIVITY\_CHANGE = "usual.event.CONNECTIVITY\_CHANGE" | 

Indicates the common event that the network connection state has changed.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_MINORSMODE\_ON = "usual.event.MINORSMODE\_ON" | 

Indicates the common event that the minor mode is enabled.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_MINORSMODE\_OFF = "usual.event.MINORSMODE\_OFF" | 

Indicates the common event that the minor mode is disabled.

**Since**: 12

 |
| static const char \* const COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED = "usual.event.MANAGED\_BROWSER\_POLICY\_CHANGED" | 

Indicates the common event that the browser hosting policy has been changed.

**Since**: 15

 |
