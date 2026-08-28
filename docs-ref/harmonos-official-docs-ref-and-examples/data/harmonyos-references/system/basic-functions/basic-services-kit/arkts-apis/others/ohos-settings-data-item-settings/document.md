# @ohos.settings (Data Item Settings)

The **settings** module provides APIs for setting data items.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/TWQXuzPfShK2gDk-F2DV1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC38653B75821E39669EB129BAA61CBC376056BCAEF6581EF24D7FEF2DDD394B)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   If no value is obtained for the accessed data item, it indicates that the current system app does not add the value of the data item to the database.
    

#### Modules to Import

import { settings } from '@kit.BasicServicesKit';

#### domainName

Provides the domain name.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| DEVICE\_SHARED11+ | string | Yes | Shared device domain. All configurations in this domain are not distinguished between multiple users. |
| USER\_PROPERTY11+ | string | Yes | User attribute domain. All configurations in this domain are distinguished between multiple users. |

#### date

Provides data items for setting the time and date formats.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| DATE\_FORMAT(deprecated21) | string | Yes | 
Date format.

The value can be **mm/dd/yyyy**, **dd/mm/yyyy**, or **yyyy/mm/dd**, where **mm** indicates the month, **dd** indicates the day, and **yyyy** indicates the year. (This constant is deprecated.)

 |
| TIME\_FORMAT | string | Yes | 

Time format. The options are as follows:

\- **12**: 12-hour format.

\- **24**: 24-hour format.

 |
| AUTO\_GAIN\_TIME(deprecated21) | string | Yes | 

Whether the date, time, and time zone are automatically obtained from the Network Identity and Time Zone (NITZ).

\- **true**: Information is automatically obtained.

\- **false**: Information is not automatically obtained. (This constant is deprecated.)

 |
| AUTO\_GAIN\_TIME\_ZONE(deprecated21) | string | Yes | 

Whether the time zone is automatically obtained from NITZ.

\- **true**: Time zone is automatically obtained.

\- **false**: Time zone is not automatically obtained. (This constant is deprecated.)

 |

#### display

Provides data items for setting the display effects.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| FONT\_SCALE | string | Yes | Scale factor of the font (**domainName**: **USER\_PROPERTY**). The value is a floating point number. The standard scale factor is **1**, and allowed scale factors include **0.85**, **1.15**, **1.3**, and **1.45**. In care mode, **1.75**, **2**, and **3.2** are available. |
| SCREEN\_BRIGHTNESS\_STATUS | string | Yes | Screen brightness, with the value ranging from 0 to 255. |
| AUTO\_SCREEN\_BRIGHTNESS | string | Yes | 
Whether automatic screen brightness adjustment is enabled.

\- **AUTO\_SCREEN\_BRIGHTNESS\_MODE**: Automatic screen brightness adjustment is enabled.

\- **MANUAL\_SCREEN\_BRIGHTNESS\_MODE**: Automatic screen brightness adjustment is disabled.

 |
| AUTO\_SCREEN\_BRIGHTNESS\_MODE | number | Yes | Value of **AUTO\_SCREEN\_BRIGHTNESS** when automatic screen brightness adjustment is enabled. |
| MANUAL\_SCREEN\_BRIGHTNESS\_MODE | number | Yes | Value of **AUTO\_SCREEN\_BRIGHTNESS** when automatic screen brightness adjustment is disabled. |
| SCREEN\_OFF\_TIMEOUT | string | Yes | Waiting time for the device to enter the sleep state when not in use (unit: ms). |
| DEFAULT\_SCREEN\_ROTATION(deprecated21) | string | Yes | 

This attribute is invalid when screen auto-rotation is enabled; otherwise, the following options are available:

\- **0**: The screen rotates by 0 degrees.

\- **1**: The screen rotates by 90 degrees.

\- **2**: The screen rotates by 180 degrees.

\- **3**: The screen rotates by 270 degrees. (This constant is deprecated.)

 |
| ANIMATOR\_DURATION\_SCALE(deprecated21) | string | Yes | 

Scale factor for the animation duration, which affects the start delay and duration of all such animations.

\- **0**: The animation ends immediately.

\- **1**: default value. (This constant is deprecated.)

 |
| TRANSITION\_ANIMATION\_SCALE(deprecated21) | string | Yes | 

Scale factor for transition animations.

\- **0**: Transition animations are disabled. (This constant is deprecated.)

 |
| WINDOW\_ANIMATION\_SCALE(deprecated21) | string | Yes | 

Scale factor for normal window animations.

\- **0**: Window animations are disabled (This constant is deprecated.)

 |
| DISPLAY\_INVERSION\_STATUS(deprecated21) | string | Yes | 

Whether display color inversion is enabled.

\- **1**: Display color inversion is enabled.

\- **0**: Display color inversion is disabled. (This constant is deprecated.)

 |

#### general

Provides data items for setting the general information about the device.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| SETUP\_WIZARD\_FINISHED(deprecated21) | string | Yes | 
Whether the startup wizard has been run.

\- **0**: The startup wizard is not run.

\- non-zero value: The startup wizard has been run. (This constant is deprecated.)

 |
| END\_BUTTON\_ACTION(deprecated21) | string | Yes | 

Action after the call end button is pressed if the user is not in a call.

\- **0**: Nothing happens.

\- **1**: The home screen is displayed.

\- **2**: The device enters the sleep state and the screen is locked.

\- **3**: The home screen is displayed. If the user is on the home screen, the device will enter sleep mode automatically. (This constant is deprecated.)

 |
| ACCELEROMETER\_ROTATION\_STATUS | string | Yes | 

Whether the accelerometer is used to change screen orientation, that is, whether to enable auto-rotation.

\- **1**: The accelerometer is used.

\- **0**: The accelerometer is not used.

 |
| DEVICE\_PROVISION\_STATUS(deprecated21) | string | Yes | 

Whether the device is preconfigured.

On a multi-user device with a single system user, the screen may be locked when the value is **true**. In addition, other features cannot be started on the system user unless they are marked to display on the lock screen. (This constant is deprecated.)

 |
| HDC\_STATUS(deprecated21) | string | Yes | 

Whether the hard disk controller (HDC) on the USB device is enabled.

\- **true**: HDC is enabled.

\- **false**: HDC is disabled. (This constant is deprecated.)

 |
| BOOT\_COUNTING(deprecated21) | string | Yes | Number of boot operations after the device is powered on. (This constant is deprecated.) |
| CONTACT\_METADATA\_SYNC\_STATUS(deprecated21) | string | Yes | 

Whether contacts metadata synchronization is enabled.

\- **true**: Contacts metadata synchronization is enabled.

\- **false**: Contacts metadata synchronization is disabled. (This constant is deprecated.)

 |
| DEVICE\_NAME | string | Yes | Device name. |
| USB\_STORAGE\_STATUS(deprecated21) | string | Yes | 

Whether USB mass storage is enabled.

\- **true**: USB mass storage is enabled.

\- **false**: USB mass storage is disabled. (This constant is deprecated.)

 |
| DEBUGGER\_WAITING(deprecated21) | string | Yes | 

Whether the device waits for the debugger when starting an application to debug.

\- **1**: The device waits for the debugger.

\- **0**: The device does not wait for the debugger and the application runs normally. (This constant is deprecated.)

 |
| DEBUG\_APP\_PACKAGE(deprecated21) | string | Yes | Bundle name of the application to be debugged. (This constant is deprecated.) |
| ACCESSIBILITY\_STATUS(deprecated21) | string | Yes | 

Whether accessibility is enabled.

\- **1**: Accessibility is enabled.

\- **0**: Accessibility is disabled. (This constant is deprecated.)

 |
| ACTIVATED\_ACCESSIBILITY\_SERVICES(deprecated21) | string | Yes | List of activated accessibility features. (This constant is deprecated.) |
| GEOLOCATION\_ORIGINS\_ALLOWED(deprecated21) | string | Yes | Default geographic location that can be used by the browser. Multiple geographical locations are separated by spaces. (This constant is deprecated.) |
| SKIP\_USE\_HINTS(deprecated21) | string | Yes | 

Whether the application should attempt to skip all introductory hints at the first startup. This feature is intended for temporary or experienced users.

\- **1**: The application will skip all introductory hints at the first startup.

\- **0**: The application will not skip introductory hints at the first startup. (This constant is deprecated.)

 |
| TOUCH\_EXPLORATION\_STATUS(deprecated21) | string | Yes | 

Whether touch exploration is enabled.

\- **1**: Touch exploration is enabled.

\- **0**: Touch exploration is disabled. (This constant is deprecated.)

 |

#### input

Provides data items for setting input methods.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| DEFAULT\_INPUT\_METHOD(deprecated21) | string | Yes | Default input method and its ID. (This constant is deprecated.) |
| ACTIVATED\_INPUT\_METHOD\_SUB\_MODE | string | Yes | Type and ID of the default input method keyboard. |
| ACTIVATED\_INPUT\_METHODS(deprecated21) | string | Yes | 
List of activated input methods.

The list is a string that contains the IDs and keyboard types of activated input methods.

The IDs are separated by colons (:), and keyboard types are separated by semicolons (;).

An example format is **ima0:keyboardType0;keyboardType1;ima1:ima2:keyboardTypes0**, where **ima** indicates the ID of an input method, and **keyboardType** indicates the keyboard type. (This constant is deprecated.)

 |
| SELECTOR\_VISIBILITY\_FOR\_INPUT\_METHOD(deprecated21) | string | Yes | 

Whether the input method selector is visible.

\- **1**: The input method selector is visible.

\- **0**: The input method selector is invisible. (This constant is deprecated.)

 |
| AUTO\_CAPS\_TEXT\_INPUT(deprecated21) | string | Yes | 

Whether automatic capitalization is enabled for the text editor.

\- **0**: Automatic capitalization is disabled.

\- **1**: Automatic capitalization is enabled. (This constant is deprecated.)

 |
| AUTO\_PUNCTUATE\_TEXT\_INPUT(deprecated21) | string | Yes | 

Whether automatic punctuation is enabled for the text editor. Automatic punctuation enables the text editor to convert two spaces into a period (.) and a space.

\- **0**: Automatic punctuation is disabled.

\- **1**: Automatic punctuation is enabled. (This constant is deprecated.)

 |
| AUTO\_REPLACE\_TEXT\_INPUT(deprecated21) | string | Yes | 

Whether autocorrect is enabled for the text editor. Autocorrect enables the text editor to correct typos.

\- **0**: Autocorrect is disabled.

\- **1**: Autocorrect is enabled. (This constant is deprecated.)

 |
| SHOW\_PASSWORD\_TEXT\_INPUT(deprecated21) | string | Yes | 

Whether password presentation is enabled in the text editor. Password presentation enables the text editor to show password characters when the user types them.

\- **0**: Password presentation is disabled.

\- **1**: Password presentation is enabled. (This constant is deprecated.)

 |

#### network

Provides data items for setting network information.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| DATA\_ROAMING\_STATUS(deprecated21) | string | Yes | 
Whether data roaming is enabled.

\- **true**: Data roaming is enabled.

\- **false**: Data roaming is disabled. (This constant is deprecated.)

 |
| HTTP\_PROXY\_CFG(deprecated21) | string | Yes | Host name and port number of the global HTTP proxy. The host name and port number are separated by a colon (:). (This constant is deprecated.) |
| NETWORK\_PREFERENCE\_USAGE(deprecated21) | string | Yes | User preferences for the network to use. (This constant is deprecated.) |

#### phone

Provides data items for setting the modes of answering incoming and outgoing calls.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| RTT\_CALLING\_STATUS(deprecated21) | string | Yes | 
Whether the real-time text (RTT) call feature is enabled. If this feature is enabled, incoming and outgoing calls are answered as RTT calls when supported by the device and carrier.

\- **1**: RTT is enabled.

\- **0**: RTT is disabled. (This constant is deprecated.)

 |

#### sound

Provides data items for setting the sound effects.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| VIBRATE\_WHILE\_RINGING(deprecated21) | string | Yes | 
Whether the device vibrates when it is ringing for an incoming call. This property is applicable to the phone and settings applications

and affects only the scenario where the device rings for an incoming call. It does not affect any other application or scenario. (This constant is deprecated.)

 |
| DEFAULT\_ALARM\_ALERT(deprecated21) | string | Yes | Storage area of the system default alarms and alerts. (This constant is deprecated.) |
| DTMF\_TONE\_TYPE\_WHILE\_DIALING(deprecated21) | string | Yes | 

Type of the dual tone multi-frequency (DTMF) tone played while dialing.

\- **0**: normal short tone.

\- **1**: long tone. (This constant is deprecated.)

 |
| DTMF\_TONE\_WHILE\_DIALING(deprecated21) | string | Yes | 

Whether the DTMF tone is played when dialing.

\- **1**: DTMF tone is played when dialing.

\- **0**: DTMF tone is not played when dialing. (This constant is deprecated.)

 |
| AFFECTED\_MODE\_RINGER\_STREAMS(deprecated21) | string | Yes | Effect on audio streams determined by changes in the ringing mode and Do Not Disturb (DND) mode. If you want a specific audio stream to be affected by changes of the ringing mode and DND mode, set the corresponding bit to **1**. (This constant is deprecated.) |
| AFFECTED\_MUTE\_STREAMS(deprecated21) | string | Yes | Audio streams affected by the mute mode. If you want a specific audio stream to remain muted in mute mode, set the corresponding bit to **1**. (This constant is deprecated.) |
| DEFAULT\_NOTIFICATION\_SOUND(deprecated21) | string | Yes | Storage area of the system default notification tone. (This constant is deprecated.) |
| DEFAULT\_RINGTONE(deprecated21) | string | Yes | Storage area of the system default ringtone. (This constant is deprecated.) |
| SOUND\_EFFECTS\_STATUS(deprecated21) | string | Yes | 

Whether the sound feature is available.

\- **0**: The sound feature is not available.

\- **1**: The sound feature is available. (This constant is deprecated.)

 |
| VIBRATE\_STATUS(deprecated21) | string | Yes | 

Whether the device vibrates for an event. This attribute is used inside the system.

\- **1**: The device vibrates for an event.

\- **0**: The device does not vibrate for an event. (This constant is deprecated.)

 |
| HAPTIC\_FEEDBACK\_STATUS(deprecated21) | string | Yes | 

Whether haptic feedback is enabled.

\- **true**: Haptic feedback is enabled.

\- **false**: Haptic feedback is disabled. (This constant is deprecated.)

 |

#### TTS

Provides data items for setting text-to-speech (TTS) information.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| DEFAULT\_TTS\_PITCH(deprecated21) | string | Yes | 
Default pitch of the TTS engine.

100 = 1x. If the value is set to **200**, the frequency is twice the normal sound frequency. (This constant is deprecated.)

 |
| DEFAULT\_TTS\_RATE(deprecated21) | string | Yes | 

Default voice rate of the TTS engine.

100 = 1x. (This constant is deprecated.)

 |
| DEFAULT\_TTS\_SYNTH(deprecated21) | string | Yes | Default TTS engine. (This constant is deprecated.) |
| ENABLED\_TTS\_PLUGINS(deprecated21) | string | Yes | List of activated plug-in packages used for TTS. Multiple plug-in packages are separated by spaces. (This constant is deprecated.) |

#### wireless

Provides data items for setting wireless network information.

#### \[h2\]Constants

**System capability**: SystemCapability.Applications.Settings.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| BLUETOOTH\_DISCOVER\_ABILITY\_STATUS(deprecated21) | string | Yes | 
Whether the device can be discovered or connected by other devices through Bluetooth.

\- **0**: The device cannot be discovered or connected.

\- **1**: The device can be connected but cannot be discovered.

\- **2**: The device can be connected and discovered. (This constant is deprecated.)

 |
| BLUETOOTH\_DISCOVER\_TIMEOUT(deprecated21) | string | Yes | 

Duration for discovering a device through Bluetooth, in seconds.

After the duration expires, the device cannot be discovered through Bluetooth. (This constant is deprecated.)

 |
| AIRPLANE\_MODE\_RADIOS(deprecated21) | string | Yes | 

List of radio signals to be disabled when airplane mode is enabled.

Multiple radio signals are separated by commas (,).

The list can include the following: **BLUETOOTH\_RADIO**, **CELL\_RADIO**, **NFC\_RADIO**, and **WIFI\_RADIO**. (This constant is deprecated.)

 |
| BLUETOOTH\_RADIO(deprecated21) | string | Yes | A value of **AIRPLANE\_MODE\_RADIOS**, indicating that Bluetooth is disabled in airplane mode. (This constant is deprecated.) |
| CELL\_RADIO(deprecated21) | string | Yes | A value of **AIRPLANE\_MODE\_RADIOS**, indicating that cellular radio is disabled in airplane mode. (This constant is deprecated.) |
| NFC\_RADIO(deprecated21) | string | Yes | A value of **AIRPLANE\_MODE\_RADIOS**, indicating that NFC is disabled in airplane mode (This constant is deprecated.) |
| WIFI\_RADIO(deprecated21) | string | Yes | A value of **AIRPLANE\_MODE\_RADIOS**, indicating that Wi-Fi is disabled in airplane mode (This constant is deprecated.) |
| BLUETOOTH\_STATUS(deprecated21) | string | Yes | 

Whether Bluetooth is available.

\- **true**: Bluetooth is available.

\- **false**: Bluetooth is unavailable. (This constant is deprecated.)

 |
| OWNER\_LOCKDOWN\_WIFI\_CFG(deprecated21) | string | Yes | 

Whether the Wi-Fi configuration created by the application of the device owner should be locked down.

\- **true**: The Wi-Fi configuration should be locked down.

\- **false**: The Wi-Fi configuration should not be locked down. (This constant is deprecated.)

 |
| WIFI\_DHCP\_MAX\_RETRY\_COUNT(deprecated21) | string | Yes | Maximum number of attempts to obtain an IP address from the DHCP server. (This constant is deprecated.) |
| WIFI\_TO\_MOBILE\_DATA\_AWAKE\_TIMEOUT(deprecated21) | string | Yes | Maximum duration to hold a wake lock when waiting for the mobile data connection after the Wi-Fi connection is disconnected. (This constant is deprecated.) |
| WIFI\_STATUS(deprecated21) | string | Yes | 

Whether Wi-Fi is available.

\- **true**: Wi-Fi is available.

\- **false**: Wi-Fi is unavailable. (This constant is deprecated.)

 |
| WIFI\_WATCHDOG\_STATUS(deprecated21) | string | Yes | 

Whether Wi-Fi watchdog is available.

\- **true**: Wi-Fi watchdog is available.

\- **false**: Wi-Fi watchdog is unavailable. (This constant is deprecated.)

 |

#### settings.setValue10+

setValue(context: Context, name: string, value: string, callback: AsyncCallback<boolean>): void

Sets the value for a data item in the **DEVICE\_SHARED** domain of the database. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**: ohos.permission.MANAGE\_SETTINGS (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| value | string | Yes | Value of the data item. The value range varies by service. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the setValue API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.setValue(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100', (status) => {
  console.info('Callback return whether value is set.');
});

#### settings.setValue10+

setValue(context: Context, name: string, value: string): Promise<boolean>

Sets the value for a data item in the **DEVICE\_SHARED** domain of the database. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**: ohos.permission.MANAGE\_SETTINGS (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| value | string | Yes | Value of the data item. The value range varies by service. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the setValue API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.setValue(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100').then((status) => {
  console.info('Callback return whether value is set.');
});

#### settings.setValue11+

setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>

Sets the value for a data item. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**:

-   ohos.permission.MANAGE\_SETTINGS for writing the DEVICE\_SHARED and USER\_PROPERTY fields (available only to system applications);
-   ohos.permission.MANAGE\_SECURE\_SETTINGS for writing the USER\_SECURITY field (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| value | string | Yes | Value of the data item. The value range varies by service. |
| domainName | string | Yes | 

Domain name to set.

\- **domainName.DEVICE\_SHARED**:

shared device domain

\- **domainName.USER\_PROPERTY**:

user property domain

\- **domainName.USER\_SECURITY**:

user security domain (for system applications only)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the setValue API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.setValue(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100', settings.domainName.DEVICE\_SHARED).then((status) => {
  console.info(\`callback:return whether value is set.\`)
});

#### settings.getValue10+

getValue(context: Context, name: string, callback: AsyncCallback<string>): void

Obtains the value of a data item in the **DEVICE\_SHARD** domain of the database. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the value of the data item. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, (err, value) => {
  if (err) {
    console.error(\`Failed to get the setting. ${err.message} \`);
    return;
  }
  console.info(\`callback:value -> ${value}\`)
});

#### settings.getValue10+

getValue(context: Context, name: string): Promise<string>

Obtains the value of a data item in the **DEVICE\_SHARD** domain of the database. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS).then((value) => {
  console.info(\`promise:value -> ${value}\`)
});

#### settings.getValue11+

getValue(context: Context, name: string, domainName: string): Promise<string>

Obtains the value of a data item in the database. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**:

-   ohos.permission.MANAGE\_SECURE\_SETTINGS for reading the USER\_SECURITY field (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| domainName | string | Yes | 

Domain name to set.

\- **domainName.DEVICE\_SHARED**:

shared device domain

\- **domainName.USER\_PROPERTY**:

user property domain

\- **domainName.USER\_SECURITY**:

user security domain (for system applications only)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the getValue API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.getValue(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, settings.domainName.DEVICE\_SHARED).then((value) => {
  console.info(\`Promise:value -> ${value}\`);
});

#### settings.getValueSync10+

getValueSync(context: Context, name: string, defValue: string): string

Obtains the value of a data item in the **DEVICE\_SHARED** domain of the database. Unlike **getValue**, this API returns the result synchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| defValue | string | Yes | Default value, which is returned when the value of a data item is not found in the database. Set this parameter as needed. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the data item. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the value of SCREEN\_BRIGHTNESS\_STATUS (this data item already exists in the database).
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let value = settings.getValueSync(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '10');

#### settings.getValueSync11+

getValueSync(context: Context, name: string, defValue: string, domainName: string): string

Obtains the value of a data item. Unlike **getValue**, this API returns the result synchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**:

-   ohos.permission.MANAGE\_SECURE\_SETTINGS for reading the USER\_SECURITY field (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| defValue | string | Yes | Default value, which is returned when the value of a data item is not found in the database. Set this parameter as needed. |
| domainName | string | Yes | 

Domain name to set.

\- **domainName.DEVICE\_SHARED**:

shared device domain

\- **domainName.USER\_PROPERTY**:

user property domain

\- **domainName.USER\_SECURITY**:

user security domain (for system applications only)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the data item. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS (this data item already exists in the database).
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let value = settings.getValueSync(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100',  settings.domainName.DEVICE\_SHARED);

#### settings.setValueSync10+

setValueSync(context: Context, name: string, value: string): boolean

Sets the value for a data item in the **DEVICE\_SHARED** domain of the database. Unlike **setValue**, this API returns the result synchronously.

-   If the specified data item exists in the database, the **setValueSync** method updates the value of the data item.
-   If the data item does not exist in the database, the **setValueSync** method inserts the data item into the database.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**: ohos.permission.MANAGE\_SETTINGS (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| value | string | Yes | Value of the data item. The value range varies by service. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the value is set successfully. Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the setValueSync API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.setValueSync(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100');

#### settings.setValueSync11+

setValueSync(context: Context, name: string, value: string, domainName: string): boolean

Sets the value for a data item. Unlike **setValue**, this API returns the result synchronously.

-   If the specified data item exists in the database, the **setValueSync** method updates the value of the data item.
-   If the data item does not exist in the database, the **setValueSync** method inserts the data item into the database.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Required permissions**:

-   ohos.permission.MANAGE\_SETTINGS for writing the DEVICE\_SHARED and USER\_PROPERTY fields (available only to system applications);
-   ohos.permission.MANAGE\_SECURE\_SETTINGS for writing the USER\_SECURITY field (available only to system applications)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| value | string | Yes | Value of the data item. The value range varies by service. |
| domainName | string | Yes | 

Domain name to set.

\- **domainName.DEVICE\_SHARED**:

shared device domain

\- **domainName.USER\_PROPERTY**:

user property domain

\- **domainName.USER\_SECURITY**:

user security domain (for system applications only)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the value is set successfully. Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the setValueSync API will update its value.)
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.setValueSync(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100', settings.domainName.DEVICE\_SHARED);

#### settings.registerKeyObserver11+

registerKeyObserver(context: Context, name: string, domainName: string, observer:AsyncCallback<void>): boolean

Registers an observer in the specified context so that the specified data item can be observed in the specified domain name. When the data item value changes, the registered callback is called. Returns **true** if the operation is successful; returns **false** otherwise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| domainName | string | Yes | 

Domain name to set.

\- **domainName.DEVICE\_SHARED**:

shared device domain

\- **domainName.USER\_PROPERTY**:

user property domain

\- **domainName.USER\_SECURITY**:

user security domain (for system applications only)

 |
| observer | AsyncCallback<void> | Yes | Callback used to return the value of the data item. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether an observer is successfully registered. Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.registerKeyObserver(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, settings.domainName.DEVICE\_SHARED, () => {
  let value:string = settings.getValueSync(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '10');
  console.info(\`Promise:value -> ${value}\`);
});

#### settings.unregisterKeyObserver11+

unregisterKeyObserver(context: Context, name: string, domainName: string): boolean

Unregisters the observer under the specified domain name. This API returns the result synchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| name | string | Yes | 

Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| domainName | string | Yes | 

Domain name to set.

\- **domainName.DEVICE\_SHARED**:

shared device domain

\- **domainName.USER\_PROPERTY**:

user property domain

\- **domainName.USER\_SECURITY**:

user security domain (for system applications only)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the observer under the specified domain name is successfully unregistered. Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let ret = settings.unregisterKeyObserver(context, settings.display.SCREEN\_BRIGHTNESS\_STATUS,  settings.domainName.DEVICE\_SHARED);

#### settings.openNetworkManagerSettings18+

openNetworkManagerSettings(context: Context): Promise<boolean>

Opens the WLAN settings window. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Applications.Settings.Core

**Devices supported**: This API can be called on phones, PCs/2-in-1 devices, and tablets.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context. Only UIAbilityContext and ExtensionContext are supported.

For details about the application context of the stage model, see [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Settings Error Codes](../../../error-codes/settings-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 14800000 | Parameter error. |
| 14800010 | Original service error. |

**Example**

import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Redirect to the network manager settings page.
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.openNetworkManagerSettings(context).then((status) => {
  console.info(\`callback:return whether settings is open.\`);
});

#### settings.enableAirplaneMode

enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void

Enables or disables airplane mode. This API uses an asynchronous callback to return the result. (Not supported yet.)

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether airplane mode is enabled. The value **true** means that airplane mode is enabled, and **false** means the opposite. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled, (err:Error) => {
    if (err) {
        console.error('Failed to enable AirplaneMode.');
        return;
    }
    console.info('Return true if enable.');
})

#### settings.enableAirplaneMode

enableAirplaneMode(enable: boolean): Promise<void>

Enables or disables airplane mode. This API uses a promise to return the result. (Not supported yet.)

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether airplane mode is enabled. The value **true** means that airplane mode is enabled, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled).then(() => {
  console.info('Succeeded in enabling AirplaneMode.');
}).catch((err:Error) => {
  console.error(\`Failed to enable AirplaneMode. Cause: ${err}\`);
})

#### settings.canShowFloating

canShowFloating(callback: AsyncCallback<boolean>): void

Checks whether the application can be displayed in a floating window. This API uses an asynchronous callback to return the result. (Not supported yet.)

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | 
Callback used to return the result.

The value **true** means that the application can be displayed in a floating window, and **false** means the opposite.

 |

**Example**

settings.canShowFloating((err:Error, status: boolean) => {
  if (err) {
    console.error(\`Failed to Checks whether a specified application can show as float window ${err.message} \`);
    return;
  }
  console.info('Checks whether a specified application can show as float window.');
});

#### settings.canShowFloating

canShowFloating(): Promise<boolean>

Checks whether the application can be displayed in a floating window. This API uses a promise to return the result. (Not supported yet.)

**System capability**: SystemCapability.Applications.Settings.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

The value **true** means that the application can be displayed in a floating window, and **false** means the opposite.

 |

**Example**

settings.canShowFloating().then((status:boolean) => {
    console.info('Checks whether a specified application can show as float window.');
});

#### settings.getUriSync8+

getUriSync(name: string): string

Obtains the URI of a data item. (Not supported yet.)

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | URI of the data item. |

**Example**

// Obtain the URI of a data item.
let uriVar:string = settings.getUriSync(settings.display.SCREEN\_BRIGHTNESS\_STATUS);

#### settings.getURI(deprecated)

getURI(name: string, callback: AsyncCallback<object>): void

Obtains the URI of a data item. This API uses an asynchronous callback to return the result. (Not supported yet.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/3aGQ_-CmQ6aGK3lsI9InVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24F0EC771B7522D2E16875D97C333DE7555DB5005A63FE64D75CE235D9C837D7)

This API is supported since API version 7 and deprecated since API version 9. No substitute API is provided.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| callback | AsyncCallback<object> | Yes | Callback used to return the result. Obtains the URI of a data item. |

**Example**

settings.getURI(settings.display.SCREEN\_BRIGHTNESS\_STATUS, (uri:string) => {
    console.info(\`callback:uri -> ${JSON.stringify(uri)}\`)
})

#### settings.getURI(deprecated)

getURI(name: string): Promise<object>

Obtains the URI of a data item. This API uses a promise to return the result. (Not supported yet.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/frZ10VoaStG31I3LuCYR_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E4A6756A30E1781A530E260F2934F36C186AA30337C26E2E709A7A3DC2A0B9D)

This API is supported since API version 7 and deprecated since API version 9. No substitute API is provided.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<object> | Promise used to return the result. |

**Example**

settings.getURI(settings.display.SCREEN\_BRIGHTNESS\_STATUS).then((uri:string) => {
    console.info(\`promise:uri -> ${JSON.stringify(uri)}\`)
})

#### settings.getValue(deprecated)

getValue(dataAbilityHelper: DataAbilityHelper, name: string, callback: AsyncCallback<object>): void

Obtains the value of a data item in the **DEVICE\_SHARD** domain of the database. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/toSe9CcuQJqHTDSpTpXo3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=274B46884CB9C02DA5309F1D3D771BF3027010B5FEACCE464DB002EBD49C76A0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getValue()](#settingsgetvalue10) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataAbilityHelper | [DataAbilityHelper](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | Yes | **DataAbilityHelper** class. |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| callback | AsyncCallback<object> | Yes | Callback used to return the value of the data item. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let uri:string = settings.getUriSync(settings.display.SCREEN\_BRIGHTNESS\_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
settings.getValue(helper, settings.display.SCREEN\_BRIGHTNESS\_STATUS, (err:Error, value:string) => {
    if (err) {
        console.error(\`Failed to get the setting. ${err.message} \`);
        return;
    }
    console.info(\`callback:value -> ${JSON.stringify(value)}\`)
});

#### settings.getValue(deprecated)

getValue(dataAbilityHelper: DataAbilityHelper, name: string): Promise<object>

Obtains the value of a data item in the **DEVICE\_SHARD** domain of the database. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/v3zBXF-hSUWHKliZr67LJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1542454F85D52AB87345655E4195913B77DCE0E32A420E8A5B370589B530A4D0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getValue()](#settingsgetvalue10-1) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataAbilityHelper | [DataAbilityHelper](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | Yes | **DataAbilityHelper** class. |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<object> | Promise used to return the result. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

let uri:string = settings.getUriSync(settings.display.SCREEN\_BRIGHTNESS\_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
settings.getValue(helper, settings.display.SCREEN\_BRIGHTNESS\_STATUS).then((value:string) => {
    console.info(\`promise:value -> ${JSON.stringify(value)}\`)
});

#### settings.getValueSync(deprecated)

getValueSync(dataAbilityHelper: DataAbilityHelper, name: string, defValue: string): string

Obtains the value of a data item. Unlike **getValue**, this API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/hlENnb3gQSi_Xv0BuwQa8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7498A19C0FE92E51FE1AB1F36404DC4E92B67DCC9FD6ABD67B3488D2A02D6ED4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getValueSync()](#settingsgetvaluesync10) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataAbilityHelper | [DataAbilityHelper](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | Yes | **DataAbilityHelper** class. |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| defValue | string | Yes | Default value, which is returned when the value of a data item is not found in the database. Set this parameter as needed. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the data item. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

// Obtain the value of SCREEN\_BRIGHTNESS\_STATUS (this data item already exists in the database).
let uri:string = settings.getUriSync(settings.display.SCREEN\_BRIGHTNESS\_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
let value:string = settings.getValueSync(helper, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '10');

#### settings.setValueSync(deprecated)

setValueSync(dataAbilityHelper: DataAbilityHelper, name: string, value: string): boolean

Sets the value for a data item. Unlike **setValue**, this API returns the result synchronously.

-   If the specified data item exists in the database, the **setValueSync** method updates the value of the data item.
-   If the data item does not exist in the database, the **setValueSync** method inserts the data item into the database.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/dpfhtvg5Rtm-_OyLJR9EGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56B5E6150BF246CD5A9C26448144427248328780F3AF54AEFF4E1BAE09D16CEF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [setValueSync()](#settingssetvaluesync10) instead.

**Model restriction**: This API can be used only in the FA model.

**Required permissions**: ohos.permission.MANAGE\_SETTINGS (available only to system applications)

**System capability**: SystemCapability.Applications.Settings.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataAbilityHelper | [DataAbilityHelper](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | Yes | **DataAbilityHelper** class. |
| name | string | Yes | 
Name of the target data item. Data items can be classified as follows:

\- Existing data items in the database

\- Custom data items

 |
| value | string | Yes | Value of the data item. The value range varies by service. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the value is set successfully. Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import featureAbility from '@ohos.ability.featureAbility';

// Update the value of SCREEN\_BRIGHTNESS\_STATUS. (As this data item exists in the database, the setValueSync API will update its value.)
let uri:string = settings.getUriSync(settings.display.SCREEN\_BRIGHTNESS\_STATUS);
let helper = featureAbility.acquireDataAbilityHelper(uri);
let ret:string = settings.setValueSync(helper, settings.display.SCREEN\_BRIGHTNESS\_STATUS, '100');
