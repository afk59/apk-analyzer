# context\_constant.h

#### Overview

The file declares the context constants of the AbilityRuntime module.

**File to include**: <AbilityKit/ability\_runtime/context\_constant.h>

**Library**: libability\_runtime.so

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since**: 13

**Related module**: [AbilityRuntime](../../modules/abilityruntime/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AbilityRuntime\_AreaMode](#abilityruntime_areamode) | AbilityRuntime\_AreaMode | Enumerates the data encryption levels. |
| [AbilityRuntime\_StartVisibility](#abilityruntime_startvisibility) | AbilityRuntime\_StartVisibility | Enumerates the visibility modes of the window and dock bar icons when the ability is started. |
| [AbilityRuntime\_WindowMode](#abilityruntime_windowmode) | AbilityRuntime\_WindowMode | Enumerates the window modes. |
| [AbilityRuntime\_SupportedWindowMode](#abilityruntime_supportedwindowmode) | AbilityRuntime\_SupportedWindowMode | Enumerates the window modes supported by an ability when it is started. The supported window mode specifies whether to display the maximize, minimize, or split-screen button when the UIAbility is launched in an application. |

#### Enum Description

#### \[h2\]AbilityRuntime\_AreaMode

enum AbilityRuntime\_AreaMode

**Description**

Enumerates the data encryption levels.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL1 = 0 | 
Device-level encryption. Directories with this encryption level are accessible after the device is powered on.

For private files, such as alarms and wallpapers, the application can place them in a directory with the device-level encryption (EL1) to ensure that they can be accessed before the user enters the password.

 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL2 = 1 | 

User-level encryption. Directories with this encryption level are accessible only after the device is powered on and the password is entered (for the first time).

For private files, such as alarms and wallpapers, the application can place them in a directory with the device-level encryption (EL1) to ensure that they can be accessed before the user enters the password.

 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL3 = 2 | 

User-level encryption. The file permissions vary according to their scenarios.

\- Open files: You can read and write to files that are already open, whether the screen is locked or unlocked.

\- Closed files: When the screen is locked, you cannot open, read, or write to closed files. Once the screen is unlocked, you can open, read, and write to closed files.

\- New files: When the screen is locked, you can create, open, and write to new files, but reading them is not permitted. Once the screen is unlocked, you can create, open, read, and write to new files.

For step recording, file download, or music playback that needs to read, write, and create files when the screen is locked, the application can place these files in EL3.

 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL4 = 3 | 

User-level encryption. The file permissions vary according to their scenarios.

\- Open files: When the screen is locked, you can read and write to open files in FEB2.0, but not in FEB3.0. When the screen is unlocked, you can read and write to open files.

\- Closed files: When the screen is locked, you cannot open, read, or write to closed files. Once the screen is unlocked, you can open, read, and write to closed files.

\- New files: When the screen is locked, you cannot create files. Once the screen is unlocked, you can create, open, read, and write to new files.

For files that are related to user security information and do not need to be read, written, or created when the screen is locked, the application can place them in EL4.

 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL5 = 4 | 

Application-level encryption. The file permissions vary according to their scenarios.

\- Open files: You can read and write to files that are already open, whether the screen is locked or unlocked.

\* Closed files: When the screen is locked, you can open, read, and write to closed files only if a DataAccessLock (JS API) is obtained. When the screen is unlocked, you can always open, read, and write to closed files.

\- New files: You can create, open, read, and write to new files, whether the screen is locked or unlocked.

By default, sensitive user privacy files cannot be read or written on the lock screen. If such files need to be read or written on the lock screen, you can call [Access](../../../arkts-apis/both-models-recommended/ohos-ability-screenlockfilemanager-sensitive-data-access-management-under-lock-s/document.md#screenlockfilemanageracquireaccess) to apply for reading or writing files before the screen is locked or create new files that can be read and written after the screen is locked. It is more appropriate to place these files in EL5.

 |

#### \[h2\]AbilityRuntime\_StartVisibility

enum AbilityRuntime\_StartVisibility

**Description**

Enumerates the visibility modes of the window and dock bar icons when the ability is started.

**Since**: 17

| Value | Description |
| :-- | :-- |
| ABILITY\_RUNTIME\_HIDE\_UPON\_START = 0 | Hides the window and dock bar icons. This mode takes effect only on 2-in-1 devices. |
| ABILITY\_RUNTIME\_SHOW\_UPON\_START = 1 | Displays the window and dock bar icons. This mode takes effect only on 2-in-1 devices. |

#### \[h2\]AbilityRuntime\_WindowMode

enum AbilityRuntime\_WindowMode

**Description**

Enumerates the window modes.

**Since**: 17

| Value | Description |
| :-- | :-- |
| ABILITY\_RUNTIME\_WINDOW\_MODE\_UNDEFINED = 0 | Window mode not defined. |
| ABILITY\_RUNTIME\_WINDOW\_MODE\_FULL\_SCREEN = 1 | Full-screen mode. This mode takes effect only on 2-in-1 devices. |

#### \[h2\]AbilityRuntime\_SupportedWindowMode

enum AbilityRuntime\_SupportedWindowMode

**Description**

Enumerates the window modes supported by an ability when it is started. The supported window mode specifies whether to display the maximize, minimize, or split-screen button when the UIAbility is launched in an application. If this property is not set, the value of **supportWindowMode** configured under [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file corresponding to the UIAbility is used by default.

**Since**: 17

| Value | Description |
| :-- | :-- |
| ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FULL\_SCREEN = 0 | A window in full-screen mode is supported. |
| ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT = 1 | A window in split-screen mode is supported. Generally, **ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FULL\_SCREEN** or **ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FLOATING** must be used together. You are not advised to configure only **ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT**. If only **ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT** is configured, the window on 2-in-1 devices is in floating window mode by default and can transition to the split-screen mode. |
| ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FLOATING = 2 | A floating window is supported. |
