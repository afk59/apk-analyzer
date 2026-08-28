# @system.brightness (Screen Brightness)

The **brightness** module provides APIs for querying and adjusting the screen brightness and mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/hgKr6HmhST-Xw0JLsBEH5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51C240A62992EDD44D4A42A0D573A017B70CBC370180C71D347700AF2A72517A)

-   The APIs of this module are no longer maintained since API version 7.The substitute APIs are available only for system applications.
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import brightness, { BrightnessModeResponse, BrightnessResponse } from '@system.brightness';

#### brightness.getValue(deprecated)

getValue(options?: GetBrightnessOptions): void

Obtains the current screen brightness.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetBrightnessOptions](#getbrightnessoptionsdeprecated) | No | Options for obtaining the screen brightness. This parameter is optional and is left blank by default. |

**Example**

brightness.getValue({
    success: (data: BrightnessResponse) => {
      console.log('success get brightness value:' + data.value);
    },
    fail: (data: string, code: number) => {
      console.error('get brightness fail, code: ' + code + ', data: ' + data);
    }
});

#### brightness.setValue(deprecated)

setValue(options?: SetBrightnessOptions): void

Sets the screen brightness.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SetBrightnessOptions](#setbrightnessoptionsdeprecated) | No | Options for setting the screen brightness. This parameter is optional and is left blank by default. |

**Example**

brightness.setValue({
    value: 100,
    success: () => {
      console.log('handling set brightness success.');
    },
    fail: (data: string, code: number) => {
      console.error('handling set brightness value fail, code:' + code + ', data: ' + data);
    }
});

#### brightness.getMode(deprecated)

getMode(options?: GetBrightnessModeOptions): void

Obtains the screen brightness adjustment mode.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetBrightnessModeOptions](#getbrightnessmodeoptionsdeprecated) | No | Options for obtaining the screen brightness mode. This parameter is optional and is left blank by default. |

**Example**

brightness.getMode({
    success: (data: BrightnessModeResponse) => {
      console.log('success get mode:' + data.mode);
    },
    fail: (data: string, code: number) => {
      console.error('handling get mode fail, code:' + code + ', data: ' + data);
    }
});

#### brightness.setMode(deprecated)

setMode(options?: SetBrightnessModeOptions): void

Sets the screen brightness mode.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SetBrightnessModeOptions](#setbrightnessmodeoptionsdeprecated) | No | Options for setting the screen brightness mode. This parameter is optional and is left blank by default. |

**Example**

brightness.setMode({
    mode: 1,
    success: () => {
      console.log('handling set mode success.');
    },
    fail: (data: string, code: number) => {
      console.error('handling set mode fail, code:' + code + ', data: ' + data);
    }
});

#### brightness.setKeepScreenOn(deprecated)

setKeepScreenOn(options?: SetKeepScreenOnOptions): void

This API is no longer maintained since API version 7. You are advised to use [window.setWindowKeepScreenOn()](../../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#setwindowkeepscreenon9).

Sets whether to always keep the screen on. Call this API in **onShow()**.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SetKeepScreenOnOptions](#setkeepscreenonoptionsdeprecated) | No | Options for setting the screen to be steady on. This parameter is optional and is left blank by default. |

**Example**

brightness.setKeepScreenOn({
    keepScreenOn: true,
    success: () => {
      console.log('handling set keep screen on success.');
    },
    fail: (data: string, code: number) => {
      console.error('handling set keep screen on fail, code:' + code + ', data: ' + data);
    }
});

#### GetBrightnessOptions(deprecated)

Options for obtaining the screen brightness.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | (data: [BrightnessResponse](#brightnessresponsedeprecated)) => void | No | Called when an API call is successful. **data** is a return value of the [BrightnessResponse](#brightnessresponsedeprecated) type. |
| fail | (data: string, code: number) => void | No | Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when an API call is complete. |

#### SetBrightnessOptions(deprecated)

Options for setting the screen brightness.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Screen brightness. The value is an integer ranging from **1** to **255**.

\- If the value is less than or equal to **0**, value **1** will be used.

\- If the value is greater than **255**, value **255** will be used.

\- If the value contains decimals, the integral part of the value will be used. For example, if value **8.1** is set, value **8** will be used.

 |
| success | () => void | No | Called when API call is successful. |
| fail | (data: string, code: number) => void | No | Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when an API call is complete. |

#### BrightnessResponse(deprecated)

Defines a response that returns the screen brightness.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | Yes | No | Screen brightness. The value ranges from **1** to **255**. |

#### GetBrightnessModeOptions(deprecated)

Options for obtaining the screen brightness mode.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | (data: [BrightnessModeResponse](#brightnessmoderesponsedeprecated)) => void | No | Called when an API call is successful. **data** is a return value of the [BrightnessModeResponse](#brightnessmoderesponsedeprecated) type. |
| fail | (data: string, code: number) => void | No | Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when an API call is complete. |

#### SetBrightnessModeOptions(deprecated)

Options for setting the screen brightness mode.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | number | Yes | The value **0** indicates the manual adjustment mode, and the value **1** indicates the automatic adjustment mode. |
| success | () => void | No | Called when API call is successful. |
| fail | (data: string, code: number) => void | No | Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when an API call is complete. |

#### BrightnessModeResponse(deprecated)

Defines a response that returns the screen brightness mode.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Readable | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| mode | number | Yes | No | The value **0** indicates the manual adjustment mode, and the value **1** indicates the automatic adjustment mode. |

#### SetKeepScreenOnOptions(deprecated)

Options for setting the screen to be steady on.

**System capability**: SystemCapability.PowerManager.DisplayPowerManager.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keepScreenOn | boolean | Yes | The value **true** means to keep the screen steady on, and the value **false** indicates the opposite. |
| success | () => void | No | Called when API call is successful. |
| fail | (data: string, code: number) => void | No | Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when an API call is complete. |
