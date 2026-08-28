# @ohos.display (Display)

The **Display** module provides APIs for managing displays, such as obtaining information about the default display, obtaining information about all displays, and listening for the addition and removal of displays.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ZxKJnSlBRzq8BHyqictb2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40955709B0C1B31148B668143F9383429E8663837020E640C8CB5A7178EEE447)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { display } from '@kit.ArkUI';

#### DisplayState

Enumerates the states of a display.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_UNKNOWN | 0 | Unknown. |
| STATE\_OFF | 1 | The display is shut down. |
| STATE\_ON | 2 | The display is powered on. |
| STATE\_DOZE | 3 | The display is in sleep mode. |
| STATE\_DOZE\_SUSPEND | 4 | The display is in sleep mode, and the CPU is suspended. |
| STATE\_VR | 5 | The display is in VR mode. |
| STATE\_ON\_SUSPEND | 6 | The display is powered on, and the CPU is suspended. |

#### Orientation10+

Enumerates the orientations of a display.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PORTRAIT | 0 | The display is in portrait mode. |
| LANDSCAPE | 1 | The display is in landscape mode. |
| PORTRAIT\_INVERTED | 2 | The display is in reverse portrait mode. |
| LANDSCAPE\_INVERTED | 3 | The display is in reverse landscape mode. |

#### DisplaySourceMode19+

Enumerates the display modes for screen content.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The device is currently not in use. |
| MAIN | 1 | The primary screen of the device is currently in use. |
| MIRROR | 2 | The device is currently in mirror display mode. |
| EXTEND | 3 | The device is currently in extended display mode. |
| ALONE | 4 | The device is currently in independent display mode. |

#### FoldStatus10+

Enumerates the fold statuses of a foldable device. For dual-fold axis devices, when oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| FOLD\_STATUS\_UNKNOWN | 0 | 
The fold status of the device is unknown or the device cannot be folded.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FOLD\_STATUS\_EXPANDED | 1 | 

The device is fully open. For dual-fold axis devices, the first fold axis is fully open, and the second fold axis is folded.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FOLD\_STATUS\_FOLDED | 2 | 

The device is folded (completely closed). For dual-fold axis devices, both the first and second fold axes are folded.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FOLD\_STATUS\_HALF\_FOLDED | 3 | 

The device is half-folded, somehow between fully open and completely closed. For dual-fold axis devices, the first fold axis is half-folded, and the second fold axis is folded.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_EXPANDED15+ | 11 | 

For dual-fold axis devices, both the first and second fold axes are fully open.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_HALF\_FOLDED15+ | 21 | 

For dual-fold axis devices, the first fold axis is fully open, and the second fold axis is half-folded.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| FOLD\_STATUS\_FOLDED\_WITH\_SECOND\_EXPANDED15+ | 12 | 

For dual-fold axis devices, the first fold axis is folded, and the second fold axis is fully open.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| FOLD\_STATUS\_FOLDED\_WITH\_SECOND\_HALF\_FOLDED15+ | 22 | 

For dual-fold axis devices, the first fold axis is folded, and the second fold axis is fully folded.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| FOLD\_STATUS\_HALF\_FOLDED\_WITH\_SECOND\_EXPANDED15+ | 13 | 

For dual-fold axis devices, the first fold axis is half-folded, and the second fold axis is fully open.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| FOLD\_STATUS\_HALF\_FOLDED\_WITH\_SECOND\_HALF\_FOLDED15+ | 23 | 

For dual-fold axis devices, both the first and second fold axes are half-folded.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fXgOqRpqS6uzMsQioyrFQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=353C0C1C6C40C191F97CA3FC3E5FEA89F2D5A1D158CF276DA41A6525591AE628)

Devices with only one fold axis can be in the **FOLD\_STATUS\_EXPANDED**, **FOLD\_STATUS\_FOLDED**, or **FOLD\_STATUS\_HALF\_FOLDED** state.

Devices with two fold axes can be in any of the states provided in the table above, except for **FOLD\_STATUS\_UNKNOWN**, which indicates an unusable fold status.

#### FoldDisplayMode10+

Enumerates the display modes of a foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

| Name | Value | Description |
| :-- | :-- | :-- |
| FOLD\_DISPLAY\_MODE\_UNKNOWN | 0 | The display mode of the device is unknown. |
| FOLD\_DISPLAY\_MODE\_FULL | 1 | The device is displayed in full screen. |
| FOLD\_DISPLAY\_MODE\_MAIN | 2 | The primary screen of the device is displayed. |
| FOLD\_DISPLAY\_MODE\_SUB | 3 | The secondary screen of the device is displayed. |
| FOLD\_DISPLAY\_MODE\_COORDINATION | 4 | Both screens of the device are displayed in collaborative mode. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/pMwX1aDWT0y-3wMLr-3DaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0B4DF5BC22658BB5AD02D915EBED23F731552AC3C737574DC35699925EC5537)

For foldable devices where both the inner and outer screens can serve as the primary screen — like large or wide-folding models — the inner screen's display mode is **FOLD\_DISPLAY\_MODE\_FULL**, and the outer screen's display mode is **FOLD\_DISPLAY\_MODE\_MAIN**.

For foldable devices where the outer screen serves only as an auxiliary display — like small-folding models — the inner screen's display mode is **FOLD\_DISPLAY\_MODE\_MAIN**, and the outer screen's display mode is **FOLD\_DISPLAY\_MODE\_SUB**.

#### FoldCreaseRegion10+

Describes the crease region of a foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| displayId | number | Yes | No | ID of the display where the crease is located. |
| creaseRects | Array<[Rect](#rect9)\> | Yes | No | Crease region. |

#### Rect9+

Describes a rectangle on the display.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | Left boundary of the rectangle, in px. The value is an integer. |
| top | number | No | No | Top boundary of the rectangle, in px. The value is an integer. |
| width | number | No | No | Width of the rectangle, in px. The value is an integer. |
| height | number | No | No | Height of the rectangle, in px. The value is an integer. |

#### WaterfallDisplayAreaRects9+

Describes the curved area on a waterfall display.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | [Rect](#rect9) | Yes | No | Rectangle of the curved area on the left of the waterfall display. |
| top | [Rect](#rect9) | Yes | No | Rectangle of the curved area on the top of the waterfall display. |
| right | [Rect](#rect9) | Yes | No | Rectangle of the curved area on the right of the waterfall display. |
| bottom | [Rect](#rect9) | Yes | No | Rectangle of the curved area at the bottom of the waterfall display. |

#### CutoutInfo9+

Describes the unusable area of a display, including punch hole, notch, and curved area of a waterfall display.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| boundingRects | Array<[Rect](#rect9)\> | Yes | No | Unusable areas (bounding rectangles) designed for punch holes and notches. If there are no punch holes or notches, an empty array is returned. |
| waterfallDisplayAreaRects | [WaterfallDisplayAreaRects](#waterfalldisplayarearects9) | Yes | No | Curved area on a waterfall display. |

#### DisplayPhysicalResolution12+

Describes the display mode of a device and the corresponding physical screen resolution information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| foldDisplayMode | [FoldDisplayMode](#folddisplaymode10) | Yes | No | Display mode of the device. The value is **0** for non-foldable devices. |
| physicalWidth | number | Yes | No | Width of the device, in px. The value is an integer greater than 0. |
| physicalHeight | number | Yes | No | Height of the device, in px. The value is an integer greater than 0. |

#### BrightnessInfo22+

Describes the screen brightness information. The information comes from the underlying screen data.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentHeadroom | number | Yes | No | Dynamic brightness headroom. The value is a floating-point number greater than 0. The default value is **1.0**. |
| maxHeadroom | number | Yes | No | Maximum brightness headroom. The value is a floating-point number greater than 0. The default value is **1.0**. |
| sdrNits | number | Yes | No | Screen brightness. The value is a floating-point number greater than 0. The default value is **500.0**. |

#### BrightnessCallback22+

type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void

Defines the callback function used to listen for screen brightness information.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data1 | T1 | Yes | Display ID. The value is of the number type. |
| data2 | T2 | Yes | Brightness information. The value is of the [BrightnessInfo](#brightnessinfo22) type. |

#### ScreenShape18+

Enumerates the screen shapes of a display.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| RECTANGLE | 0 | The screen is in the shape of a rectangle. |
| ROUND | 1 | The screen is in the shape of a circle. |

#### VirtualScreenConfig16+

Describes the virtual screen parameters.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the virtual screen, which can be customized. |
| width | number | No | No | Width of the virtual screen, in px. The value must be a positive integer. |
| height | number | No | No | Height of the virtual screen, in px. The value must be a positive integer. |
| density | number | No | No | Density of the virtual screen, in px. The value is a floating-point number. |
| surfaceId | string | No | No | Surface ID of the virtual screen, which can be customized. The maximum length for this parameter is 4096 bytes. If it goes beyond that, only the first 4096 bytes are used. |
| supportsFocus22+ | boolean | No | Yes | Whether the virtual screen is focusable. **true** if focusable, **false** otherwise. The default value is **true**. |

#### Position20+

Describes a coordinate position. In the global coordinate system, the origin is the top-left corner of the primary screen. In the relative coordinate system, the origin is the top-left corner of the specified screen.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X coordinate relative to the origin, measured in px. The value must be a 32-bit signed integer, and floating-point numbers are rounded down. |
| y | number | No | No | Y coordinate relative to the origin, measured in px. The value must be a 32-bit signed integer, and floating-point numbers are rounded down. |

#### RelativePosition20+

Describes a coordinate position in the relative coordinate system, with the origin in the top-left corner of the screen specified by **displayId**.

**System capability**: SystemCapability.Window.SessionManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| displayId | number | No | No | Display ID for the relative coordinates. Only integers are supported, and the value must be greater than or equal to 0. |
| position | [Position](#position20) | No | No | Coordinates with the top-left corner of the screen specified by **displayId** as the origin. |

#### display.getDisplayByIdSync12+

getDisplayByIdSync(displayId: number): Display

Obtains a Display object based on the display ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | Display ID. The value must be an integer greater than or equal to 0. An object can be obtained only when the passed-in display ID is correct. You can use the value of the **displayId** property in [WindowProperties](../../window-manager/ohos-window-window/interfaces-others/document.md#windowproperties) as the input parameter. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Display](#display) | Display object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types. 3. Parameter verification failed. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;

try {
  // Use the value of the displayId property in WindowProperties as the input parameter.
  let displayId = 0;
  displayClass = display.getDisplayByIdSync(displayId);
} catch (exception) {
  console.error(\`Failed to get display. Code: ${exception.code}, message: ${exception.message}\`);
}

#### display.getBrightnessInfo22+

getBrightnessInfo(displayId: number): [BrightnessInfo](#brightnessinfo22)

Obtains the screen brightness information of a display. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the returned [BrightnessInfo](#brightnessinfo22) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | Display ID. The value must be an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| [BrightnessInfo](#brightnessinfo22) | Screen brightness information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**Example**

import { display } from '@kit.ArkUI';

try {
  let brightNessInfo = display.getBrightnessInfo(0);
  console.info(\`brightness info: ${JSON.stringify(brightNessInfo)}\`);
} catch (error) {
  console.error(\`Failed to getDisplayBrightness. Code: ${error.code}, message: ${error.message}\`);
}

#### display.getAllDisplayPhysicalResolution12+

getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>

Obtains all the display modes supported by the current device, along with the physical screen resolutions for each mode. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[DisplayPhysicalResolution](#displayphysicalresolution12)\>> | Promise used to return all the DisplayPhysicalResolution objects. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400003 | This display manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let promise = display.getAllDisplayPhysicalResolution();
promise.then((resolutionObjects) => {
  console.info('Obtaining physical resolution length: ' + resolutionObjects.length);
  for (let i = 0; i < resolutionObjects.length; i++) {
     console.info(\`resolutionObjects\[${i}\].foldDisplayMode: ${resolutionObjects\[i\].foldDisplayMode}\`);
     console.info(\`resolutionObjects\[${i}\].physicalWidth: ${resolutionObjects\[i\].physicalWidth}\`);
     console.info(\`resolutionObjects\[${i}\].physicalHeight: ${resolutionObjects\[i\].physicalHeight}\`);
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain physical resolution. Code: ${err.code}, message: ${err.message}\`);
});

#### display.getDefaultDisplaySync9+

getDefaultDisplaySync(): Display

Obtains the **Display** object of the screen where the application is located. If multiple abilities of an application are on different screens, the **Display** object of the main screen is returned. If multiple abilities of an application are on the same screen, the **Display** object of the screen is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Display](#display) | Default Display object. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400001 | Invalid display or screen. |

**Example**

import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
} catch (exception) {
  console.error(\`Failed to get default display. Code: ${exception.code}, message: ${exception.message}\`);
}

#### display.getPrimaryDisplaySync14+

getPrimaryDisplaySync(): Display

Obtains the information about the primary display. For devices other than 2-in-1 devices, the Display object obtained is the built-in screen. For 2-in-1 devices with an external screen, the Display object obtained is the primary screen. For 2-in-1 devices without an external screen, the Display object obtained is the built-in screen.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Display](#display) | Display object of the primary screen. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400001 | Invalid display or screen. |

**Example**

import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;

displayClass = display.getPrimaryDisplaySync();

#### display.getAllDisplays9+

getAllDisplays(callback: AsyncCallback<Array<Display>>): void

Obtains all Display objects. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Display](#display)\>> | Yes | Callback used to return all the Display objects. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400001 | Invalid display or screen. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: Array<display.Display> = \[\];
display.getAllDisplays((err: BusinessError, data: Array<display.Display>) => {
  displayClass = data;
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining all the display objects. Data: ${JSON.stringify(data)}\`);
});

#### display.getAllDisplays9+

getAllDisplays(): Promise<Array<Display>>

Obtains all Display objects. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Display](#display)\>> | Promise used to return all the Display objects. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400001 | Invalid display or screen. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: Array<display.Display> =\[\];
let promise: Promise<Array<display.Display>> = display.getAllDisplays();
promise.then((data: Array<display.Display>) => {
  displayClass = data;
  console.info(\`Succeeded in obtaining all the display objects. Data:  ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}\`);
});

#### display.on('add'|'remove'|'change')

on(type: 'add'|'remove'|'change', callback: Callback<number>): void

Subscribes to display changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **add**, indicating the display addition event. Example: event that a display is connected.

\- **remove**, indicating the display removal event. Example: event that a display is disconnected.

\- **change**, indicating the display change event. Example: event that the display orientation is changed.

 |
| callback | Callback<number> | Yes | Callback used to return the ID of the display, which is an integer. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<number> = (data: number) => {
  console.info(\`Listening enabled. Data: ${data}\`);
};

display.on("add", callback);

#### display.off('add'|'remove'|'change')

off(type: 'add'|'remove'|'change', callback?: Callback<number>): void

Unsubscribes from display changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- **add**, indicating the display addition event. Example: event that a display is connected.

\- **remove**, indicating the display removal event. Example: event that a display is disconnected.

\- **change**, indicating the display change event. Example: event that the display orientation is changed.

 |
| callback | Callback<number> | No | Callback used to return the ID of the display, which is an integer. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

// Unregister all the callbacks that have been registered through on().
display.off("remove");

let callback: Callback<number> = (data: number) => {
  console.info(\`Succeeded in unregistering the callback for display remove. Data: ${data}\`)
};
// Unregister the specified callback.
display.off('remove', callback);

#### display.isFoldable10+

isFoldable(): boolean

Checks whether this device is foldable.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the device is foldable. **true** if foldable, **false** otherwise. For small-screen foldable devices where the outer screen serves only as an auxiliary display (and cannot be customized by applications), the return value is always **false**. For other foldable devices, the return value is always **true**. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let ret: boolean = false;
ret = display.isFoldable();

#### display.getFoldStatus10+

getFoldStatus(): FoldStatus

Obtains the fold status of this foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [FoldStatus](#foldstatus10) | Fold status of the device. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let data: display.FoldStatus = display.getFoldStatus();
console.info(\`Succeeded in obtaining fold status. Data: ${data}\`);

#### display.getFoldDisplayMode10+

getFoldDisplayMode(): FoldDisplayMode

Obtains the display mode of this foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API returns **0** for 2-in-1 devices and non-foldable devices. For other devices, this API can be called properly.

**Return value**

| Type | Description |
| :-- | :-- |
| [FoldDisplayMode](#folddisplaymode10) | Display mode of the foldable device. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let data: display.FoldDisplayMode = display.getFoldDisplayMode();
console.info(\`Succeeded in obtaining fold display mode. Data: ${data}\`);

#### display.getCurrentFoldCreaseRegion10+

getCurrentFoldCreaseRegion(): FoldCreaseRegion

Obtains the crease region of the foldable device in the current display mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on foldable devices. If it is called on other device types, **undefined** is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| [FoldCreaseRegion](#foldcreaseregion10) | Crease region of the device. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let data: display.FoldCreaseRegion = display.getCurrentFoldCreaseRegion();
console.info(\`Succeeded in obtaining current fold crease region. Data: ${JSON.stringify(data)}\`);

#### display.on('foldStatusChange')10+

on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void

Subscribes to fold status change events of the foldable device.

To subscribe to display mode change events of foldable devices, use [display.on('foldDisplayModeChange')](#displayonfolddisplaymodechange10).

The two are different. In terms of timing, the fold status changes first, and the bottom layer matches the display mode status based on the fold status.

To check whether the content is displayed on the inner or outer screen of the foldable device, use [display.on('foldDisplayModeChange')](#displayonfolddisplaymodechange10).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'foldStatusChange'** is triggered when the fold status of the device changes. |
| callback | Callback<[FoldStatus](#foldstatus10)\> | Yes | Callback used to return the fold status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

/\*\*
 \* The callback parameter used for subscription must be passed as an object.
 \* If an anonymous function is used for registration, a new underlying object is created each time the function is called, causing memory leakage.
 \*/
let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  console.info(\`Listening enabled. Data: ${data}\`);
};
display.on('foldStatusChange', callback);

#### display.off('foldStatusChange')10+

off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void

Unsubscribes from fold status change events of the foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'foldStatusChange'** is triggered when the fold status of the device changes. |
| callback | Callback<[FoldStatus](#foldstatus10)\> | No | Callback used to return the fold status. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

// Unregister all the callbacks that have been registered through on().
display.off('foldStatusChange');

let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  console.info(\`unregistering FoldStatus changes callback. Data: ${data}\`);
};
// Unregister the specified callback.
display.off('foldStatusChange', callback);

#### display.on('brightnessInfoChange')22+

on(type: 'brightnessInfoChange', callback: BrightnessCallback<number, BrightnessInfo>): void

Subscribes to events related to screen brightness information changes. If the screen does not support HDR, the **currentHeadroom** and **maxHeadroom** fields in the [BrightnessInfo](#brightnessinfo22) object use the default values. For virtual screens, the **sdrNits** field in the BrightnessInfo object uses the default value.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'brightnessInfoChange'**, indicating that the screen brightness information is changed. |
| callback | [BrightnessCallback](#brightnesscallback22)<number, [BrightnessInfo](#brightnessinfo22)\> | Yes | Callback used to return the display ID (parameter 1) and the corresponding screen brightness information (parameter 2). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**Example**

let callback: display.BrightnessCallback<number, display.BrightnessInfo> = (id: number, data: display.BrightnessInfo) => {
  console.info(\`Listening enabled ${id}. Data: ${JSON.stringify(data)}\`);
};
try {
  display.on("brightnessInfoChange", callback);
} catch (error) {
  console.error(\`brightnessInfoChange error. Code ${error.code}, message: ${error.message}\`);
}

#### display.off('brightnessInfoChange')22+

off(type: 'brightnessInfoChange', callback?: BrightnessCallback<number, BrightnessInfo>): void

Unsubscribes from events related to screen brightness information changes.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'brightnessInfoChange'**, indicating that the screen brightness information is changed. |
| callback | [BrightnessCallback](#brightnesscallback22)<number, [BrightnessInfo](#brightnessinfo22)\> | No | Callback used to return the brightnessInfo status change. If this parameter is not specified, all subscriptions to the specified event are canceled. The first parameter indicates the display ID, and the second parameter indicates the screen brightness information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**Example**

let callback: display.BrightnessCallback<number, display.BrightnessInfo> = (id: number, data: display.BrightnessInfo) => {
  console.info(\`Listening enabled ${id}. Data: ${JSON.stringify(data)}\`);
};
try {
  display.off("brightnessInfoChange", callback);
} catch (error) {
  console.error(\`brightnessInfoChange error. Code ${error.code}, message: ${error.message}\`);
}

#### display.on('foldAngleChange')12+

on(type: 'foldAngleChange', callback: Callback<Array<number>>): void

Subscribes to folding angle change events of the foldable device. Note that there are two folding angles for dual-fold axis devices. When oriented with the charging port at the bottom, the hinges are identified from right to left as the first and second fold axes, respectively.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'foldAngleChange'** is triggered when the folding angle of the device changes. |
| callback | Callback<Array<number>> | Yes | Callback used to return the folding angle (0–180 degrees). For dual-fold axis devices, the array contains two angles. The first value represents the folding angle of the first fold axis, while the second value represents the folding angle of the second fold axis. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<Array<number>> = (angles: Array<number>) => {
  console.info('Listening fold angles length: ' + angles.length);
};
display.on('foldAngleChange', callback);

#### display.off('foldAngleChange')12+

off(type: 'foldAngleChange', callback?: Callback<Array<number>>): void

Unsubscribes from folding angle change events of the foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'foldAngleChange'** is triggered when the folding angle of the device changes. |
| callback | Callback<Array<number>> | No | Callback used to return the folding angle (0–180 degrees). If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

// Unregister all the callbacks that have been registered through on().
display.off('foldAngleChange');

let callback: Callback<Array<number>> = (angles: Array<number>) => {
  console.info('Listening fold angles length: ' + angles.length);
};
// Unregister the specified callback.
display.off('foldAngleChange', callback);

#### display.on('captureStatusChange')12+

on(type: 'captureStatusChange', callback: Callback<boolean>): void

Subscribes to events indicating whether the device's screen content is being captured.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'captureStatusChange'** is triggered when the screen capture status changes. |
| callback | Callback<boolean> | Yes | Callback used to return the result indicating whether the device's screen content is being captured. **true** is returned when screen content is being captured (including active screen capture, casting, recording, or the creation of a virtual screen that could be captured). **false** is returned when screen content is no longer being captured. In the case of screen capture, **true** is returned only once. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<boolean> = (captureStatus: boolean) => {
  console.info('Listening capture status: ' + captureStatus);
};
display.on('captureStatusChange', callback);

#### display.off('captureStatusChange')12+

off(type: 'captureStatusChange', callback?: Callback<boolean>): void

Unsubscribes from events indicating whether the device's screen content is being captured.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'captureStatusChange'** is triggered when the screen capture status changes. |
| callback | Callback<boolean> | No | Callback used to return the result indicating whether the device's screen content is being captured. **true** is returned when screen content is being captured (including active screen capture, casting, recording, or the creation of a virtual screen that could be captured). **false** is returned when screen content is no longer being captured. In the case of screen capture, **true** is returned only once. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

// Unregister all the callbacks that have been registered through on().
display.off('captureStatusChange');

let callback: Callback<boolean> = (captureStatus: boolean) => {
  console.info('Listening capture status: ' + captureStatus);
};
// Unregister the specified callback.
display.off('captureStatusChange', callback);

#### display.isCaptured12+

isCaptured(): boolean

Checks whether the device's screen content is being captured.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the device's screen content is being captured. **true** is returned when screen content is being captured (including active screen capture, casting, recording, or the creation of a virtual screen that could be captured). **false** is returned when screen content is no longer being captured. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let ret: boolean = false;
ret = display.isCaptured();

#### display.on('foldDisplayModeChange')10+

on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void

Subscribes to display mode change events of the foldable device.

To subscribe to fold status change events of foldable devices, use [display.on('foldStatusChange')](#displayonfoldstatuschange10).

The two are different. In terms of timing, the fold status changes first, and the bottom layer matches the display mode status based on the fold status.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API has no effect and does not report errors for 2-in-1 devices and non-foldable devices. For other devices, this API can be called properly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'foldDisplayModeChange'** is triggered when the display mode of the device changes. |
| callback | Callback<[FoldDisplayMode](#folddisplaymode10)\> | Yes | Callback used to return the display mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

/\*\*
 \* The callback parameter used for subscription must be passed as an object.
 \* If an anonymous function is used for registration, a new underlying object is created each time the function is called, causing memory leakage.
 \*/
let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(\`Listening enabled. Data: ${data}\`);
};
display.on('foldDisplayModeChange', callback);

#### display.off('foldDisplayModeChange')10+

off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void

Unsubscribes from display mode change events of the foldable device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API has no effect and does not report errors for 2-in-1 devices and non-foldable devices. For other devices, this API can be called properly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'foldDisplayModeChange'** is triggered when the display mode of the device changes. |
| callback | Callback<[FoldDisplayMode](#folddisplaymode10)\> | No | Callback used to return the display mode. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 1400003 | This display manager service works abnormally. |

**Example**

// Unregister all the callbacks that have been registered through on().
display.off('foldDisplayModeChange');

let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(\`unregistering FoldDisplayMode changes callback. Data: ${data}\`);
};
// Unregister the specified callback.
display.off('foldDisplayModeChange', callback);

#### display.createVirtualScreen16+

createVirtualScreen(config:VirtualScreenConfig): Promise<number>

Creates a virtual screen. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Required permissions**: ohos.permission.ACCESS\_VIRTUAL\_SCREEN

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [VirtualScreenConfig](#virtualscreenconfig16) | Yes | Virtual screen parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the screen ID of the created virtual screen. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported.function createVirtualScreen can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

class VirtualScreenConfig {
  name : string = '';
  width : number = 0;
  height : number = 0;
  density : number = 0;
  surfaceId : string = '';
  supportsFocus ?: boolean = true;
}

let config : VirtualScreenConfig = {
  name: 'screen01',
  width: 1080,
  height: 2340,
  density: 2,
  surfaceId: '',
  supportsFocus: false
};

display.createVirtualScreen(config).then((screenId: number) => {
  console.info(\`Succeeded in creating the virtual screen.ScreenId : ${screenId}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create the virtual screen. Code:${err.code},message is ${err.message}\`);
});

#### display.destroyVirtualScreen16+

destroyVirtualScreen(screenId:number): Promise<void>

Destroys a virtual screen. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Required permissions**: ohos.permission.ACCESS\_VIRTUAL\_SCREEN

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| screenId | number | Yes | Screen ID, which must match the ID of the virtual screen created by calling the [createVirtualScreen()](#displaycreatevirtualscreen16) API. This parameter only accepts integer values. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported.function destroyVirtualScreen can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 1;
display.destroyVirtualScreen(screenId).then(() => {
  console.info('Succeeded in destroying the virtual screen.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to destroy the virtual screen.Code:${err.code},message is ${err.message}\`);
});

#### display.setVirtualScreenSurface16+

setVirtualScreenSurface(screenId:number, surfaceId: string): Promise<void>

Sets a surface for a virtual screen. **surfaceId** identifies a surface, the content of which will be shown on this virtual screen. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Required permissions**: ohos.permission.ACCESS\_VIRTUAL\_SCREEN

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| screenId | number | Yes | Screen ID, which must match the ID of the virtual screen created by calling the [createVirtualScreen()](#displaycreatevirtualscreen16) API. This parameter only accepts integer values. |
| surfaceId | string | Yes | ID of the surface bound to the virtual screen. You can specify the ID of an existing surface. The maximum length for this parameter is 4096 bytes. If it goes beyond that, only the first 4096 bytes are used. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported.function setVirtualScreenSurface can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

**Example**

// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  xComponentController: XComponentController = new XComponentController();

  setVirtualScreenSurface = () => {
    let screenId: number = 1;
    let surfaceId = this.xComponentController.getXComponentSurfaceId();
    display.setVirtualScreenSurface(screenId, surfaceId).then(() => {
      console.info('Succeeded in setting the surface for the virtual screen.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set the surface for the virtual screen. Code:${err.code},message is ${err.message}\`);
    });
  }
  build() {
    RelativeContainer() {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController
      })
      Button('setSurface')
        .onClick((event: ClickEvent) => {
          this.setVirtualScreenSurface();
      }).width('100%')
      .height(20)
    }
    .width('100%')
    .height('100%')
  }
}

#### display.makeUnique16+

makeUnique(screenId:number): Promise<void>

Sets the screen to independent display mode. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Required permissions**: ohos.permission.ACCESS\_VIRTUAL\_SCREEN

**Device behavior differences**: This API can be properly called on phones, PCs/2-in-1 devices, and tablets, but does not take effect or report errors when being called on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| screenId | number | Yes | ID of the screen. Each ID must be an integer greater than 0; otherwise, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported.function makeUnique can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 0;
display.makeUnique(screenId).then(() => {
  console.info('Succeeded in making unique screens.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to make unique screens. Code:${err.code},message is ${err.message}\`);
});

#### display.convertRelativeToGlobalCoordinate20+

convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position

Converts relative coordinates (based on the top-left corner of the screen) into global coordinates (based on the top-left corner of the primary screen). This API supports only coordinate conversion between the primary screen and extended screen.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| relativePosition | [RelativePosition](#relativeposition20) | Yes | Relative coordinates to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Position](#position20) | Global coordinates based on the top-left corner of the primary screen. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**Example**

import { display } from '@kit.ArkUI';

let relativePosition: display.RelativePosition = {
  displayId: 0,
  position: {
    x: 100,
    y: 200
  }
};

try {
  let position: display.Position = display.convertRelativeToGlobalCoordinate(relativePosition);
  console.info(\`The global coordinate is ${position.x}, ${position.y}\`)
} catch (exception) {
  console.error(\`Failed to convert the relative coordinate to the global coordinate. Code: ${exception.code}, message: ${exception.message}\`);
}

#### display.convertGlobalToRelativeCoordinate20+

convertGlobalToRelativeCoordinate(position: Position, displayId?: number): RelativePosition

Converts global coordinates (based on the top-left corner of the primary screen) into relative coordinates (based on the top-left corner of the screen specified by **displayId**). If **displayId** is not passed, the coordinates are converted relative to the screen where the global coordinates are located. If the global coordinates are not on any screen, the coordinates are converted relative to the primary screen by default.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | [Position](#position20) | Yes | Global coordinates to convert. |
| displayId | number | No | Display ID for the relative coordinates. If this parameter is passed, the coordinates are converted relative to this screen. If it is not provided, the coordinates are converted to the screen where the global coordinates are located, or the primary screen if they are not on any screen. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RelativePosition](#relativeposition20) | Relative coordinates for the specified screen. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |
| 1400004 | Parameter error. Possible cause: 1.Invalid parameter range. |

**Example**

import { display } from '@kit.ArkUI';

let position: display.Position = {
    x: 100,
    y: 200
};

try {
  let relPos: display.RelativePosition = display.convertGlobalToRelativeCoordinate(position, 0);
  console.info(\`The relative coordinate is ${relPos.displayId}, ${relPos.position.x}, ${relPos.position.y}\`)
} catch (exception) {
  console.error(\`Failed to convert the global coordinate to the relative coordinate. Code: ${exception.code}, message: ${exception.message}\`);
}

#### display.getDefaultDisplay(deprecated)

getDefaultDisplay(callback: AsyncCallback<Display>): void

Obtains the default Display object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/HhnEyuPdSZWotoowJJ6K6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA5EE165157DF7CF6D99AC2B6B69BB69D3C025F16C4354046AE4C802367DA14F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getDefaultDisplaySync()](#displaygetdefaultdisplaysync9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Display](#display)\> | Yes | Callback used to return the default Display object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
display.getDefaultDisplay((err: BusinessError, data: display.Display) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to obtain the default display object. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining the default display object. Data: ${JSON.stringify(data)}\`);
  displayClass = data;
});

#### display.getDefaultDisplay(deprecated)

getDefaultDisplay(): Promise<Display>

Obtains the default Display object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/cd3UpLGsSwGdxyV4kTmTYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=421B8CC4EFF88704DF21B95CF6FC01FA3A9DDC0F3101081D863378BDE0D3E83A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getDefaultDisplaySync()](#displaygetdefaultdisplaysync9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Display](#display)\> | Promise used to return the default Display object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
let promise: Promise<display.Display> = display.getDefaultDisplay();
promise.then((data: display.Display) => {
  displayClass = data;
  console.info(\`Succeeded in obtaining the default display object. Data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the default display object. Code: ${err.code}, message: ${err.message}\`);
});

#### display.getAllDisplay(deprecated)

getAllDisplay(callback: AsyncCallback<Array<Display>>): void

Obtains all Display objects. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/JjXrrzYdRnuGUIOcbE64OA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD848DC86A1A6F5250D56F727CE14205D1F71BE378D38BFA186AB68830818237)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getAllDisplays()](#displaygetalldisplays9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Display](#display)\>> | Yes | Callback used to return all the Display objects. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

display.getAllDisplay((err: BusinessError, data: Array<display.Display>) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining the default display objects. Data: ${JSON.stringify(data)}\`);
});

#### display.getAllDisplay(deprecated)

getAllDisplay(): Promise<Array<Display>>

Obtains all Display objects. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/PtAruryiSGCF7xsTKJl49Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CB01AF5A877F8C0A52C8F0BEFC8D53D1B30FDDC1EBD0E3C485C9F3A2B5D8555)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getAllDisplays()](#displaygetalldisplays9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Display](#display)\>> | Promise used to return all the Display objects. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise: Promise<Array<display.Display>> = display.getAllDisplay();
promise.then((data: Array<display.Display>) => {
  console.info(\`Succeeded in obtaining the default display objects. Data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}\`);
});

#### Display

Implements a Display instance, with attributes and APIs defined.

Before calling any API in Display, you must use [getAllDisplays()](#displaygetalldisplays9) or [getDefaultDisplaySync()](#displaygetdefaultdisplaysync9) to obtain a Display instance.

#### \[h2\]Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | Yes | No | 
Display ID, which is an integer greater than or equal to 0.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| name | string | Yes | No | 

Name of the display.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| alive | boolean | Yes | No | 

Whether the display is alive. The value **true** indicates that the display is alive and running properly, and **false** indicates the opposite.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| state | [DisplayState](#displaystate) | Yes | No | 

State of the display.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| refreshRate | number | Yes | No | 

Refresh rate of the display, in Hz. The value is an integer.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| rotation | number | Yes | No | 

Clockwise rotation angle of the display.

The value **0** indicates that the display rotates clockwise by 0°, which is the standard display direction.

The value **1** indicates that the display rotates clockwise by 90°.

The value **2** indicates that the display rotates clockwise by 180°.

The value **3** indicates that the display rotates clockwise by 270°.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| width | number | Yes | No | 

Width of the display, in px. The value is an integer.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| height | number | Yes | No | 

Height of the display, in px. The value is an integer.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| densityDPI | number | Yes | No | 

Physical pixel density of the display, that is, the number of pixels per inch. The value is a floating-point number, in px. Generally, the value is **160.0** or **480.0**. The actual value depends on the optional values provided by the device in use.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| orientation10+ | [Orientation](#orientation10) | Yes | No | 

Orientation of the display.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| densityPixels | number | Yes | No | 

Logical pixel density of the display, which is the scaling coefficient between physical pixels and logical pixels. The calculation method is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nzX6HlikT5OcswIYBme-JA/en-us_image_0000002568685089.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D5DC93F597780644F7BCEFB84003B0508769FEA4CADD30ADC44236CFF69E89D)

The value is a floating-point number and is restricted by the range of **densityDPI**. The value range is \[0.5, 4.0\]. Generally, the value is **1.0** or **3.0**. The actual value depends on the density DPI provided by the device in use.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| scaledDensity | number | Yes | No | 

Scaling factor for fonts displayed on the display. The value must be a floating-point number. Generally, the value is the same as that of **densityPixels**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| xDPI | number | Yes | No | 

Exact physical pixels per inch of the display in the X axis. The value must be a floating-point number.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| yDPI | number | Yes | No | 

Exact physical pixels per inch of the display in the Y axis. The value must be a floating-point number.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| colorSpaces11+ | Array<[colorSpaceManager.ColorSpace](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md)\> | Yes | No | 

All color spaces supported by the display.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| hdrFormats11+ | Array<[hdrCapability.HDRFormat](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-hdrcapability-hdr-capability/document.md#hdrformat)\> | Yes | No | 

All HDR formats supported by the display.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| availableWidth12+ | number | Yes | No | 

Width of the available area, in px. The value is an integer greater than 0.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**: This API can be properly called on 2-in-1 devices and tablets. It does not work for other device types. To obtain the width of the available area on the current device, you can use the **width** property.

 |
| availableHeight12+ | number | Yes | No | 

Height of the available area, in px. The value is an integer greater than 0.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**: This API can be properly called on 2-in-1 devices and tablets. It does not work for other device types. To obtain the height of the available area on the current device, you can use the **height** property.

 |
| screenShape18+ | [ScreenShape](#screenshape18) | Yes | Yes | 

Screen shape of the display. The default value is **RECTANGLE**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| sourceMode19+ | [DisplaySourceMode](#displaysourcemode19) | Yes | Yes | 

Display mode for screen content. The default value is **DisplaySourceMode.NONE**.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| x19+ | number | Yes | Yes | 

X coordinate of the top-left corner of the display relative to the origin, which is the top-left corner of the primary screen, measured in px. The value is an integer. The default value is **0**. The actual value is returned only when **DisplaySourceMode** is set to **MAIN** or **EXTEND**; otherwise, the default value **0** is returned.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| y19+ | number | Yes | Yes | 

Y coordinate of the top-left corner of the display relative to the origin, which is the top-left corner of the primary screen, measured in px. The value is an integer. The default value is **0**. The actual value is returned only when **DisplaySourceMode** is set to **MAIN** or **EXTEND**; otherwise, the default value **0** is returned.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| supportedRefreshRates20+ | Array<number> | Yes | Yes | 

All refresh rates supported by the display, sorted in ascending order. The refresh rate is a positive integer, in Hz. The default value is empty.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### \[h2\]getCutoutInfo9+

getCutoutInfo(callback: AsyncCallback<CutoutInfo>): void

Obtains the cutout information of the display. This API uses an asynchronous callback to return the result. You are advised not to use the cutout area during application layout.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[CutoutInfo](#cutoutinfo9)\> | Yes | Callback used to return the **CutoutInfo** object. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400001 | Invalid display or screen. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();

displayClass.getCutoutInfo((err: BusinessError, data: display.CutoutInfo) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to get cutoutInfo. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}\`);
});

#### \[h2\]getCutoutInfo9+

getCutoutInfo(): Promise<CutoutInfo>

Obtains the cutout information of the display. This API uses a promise to return the result. You are advised not to use the cutout area during application layout.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CutoutInfo](#cutoutinfo9)\> | Promise used to return the CutoutInfo object. |

**Error codes**

For details about the error codes, see [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1400001 | Invalid display or screen. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let displayClass: display.Display | null = null;
displayClass = display.getDefaultDisplaySync();
let promise: Promise<display.CutoutInfo> = displayClass.getCutoutInfo();
promise.then((data: display.CutoutInfo) => {
  console.info(\`Succeeded in getting cutoutInfo. Data: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]getAvailableArea12+

getAvailableArea(): Promise<Rect>

Obtains the available area of the display of the current device. This API uses a promise to return the result.

The available area is the space left for applications after the system UI (such as the status bar and dock bar) is accounted for.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on 2-in-1 devices and tablets. It does not work for other device types. To obtain the available screen area on the current device, you can use the **width** and **height** attributes in [Display](#attributes).

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Rect](#rect9)\> | Promise used to return the available area, which is a rectangle. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400001 | Invalid display or screen. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let promise = displayClass.getAvailableArea();
  promise.then((data) => {
    console.info(\`Succeeded get the available area in this display. data: ${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get the available area in this display. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (exception) {
  console.error(\`Failed to obtain the default display object. Code: ${exception.code}, message: ${exception.message}\`);
}

#### \[h2\]on('availableAreaChange')12+

on(type: 'availableAreaChange', callback: Callback<Rect>): void

Subscribes to changes of the available area on the display of the current device. This callback function is triggered when the screen rotates, the freeform mode is enabled or disabled, or the visibility of system components such as the dock bar and status bar changes, and returns the available area information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on 2-in-1 devices and tablets. If it is called on other device types, it has no effect and does not report errors.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'availableAreaChange'** is triggered when the available area of the display changes. |
| callback | Callback<[Rect](#rect9)\> | Yes | Callback used to return the new available area. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(\`Listening enabled. Data: ${JSON.stringify(data)}\`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.on("availableAreaChange", callback);
} catch (exception) {
  console.error(\`Failed to register callback. Code: ${exception.code}, message: ${exception.message}\`);
}

#### \[h2\]off('availableAreaChange')12+

off(type: 'availableAreaChange', callback?: Callback<Rect>): void

Unsubscribes from changes of the available area on the display of the current device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on 2-in-1 devices and tablets. If it is called on other device types, it has no effect and does not report errors.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'availableAreaChange'** is triggered when the available area of the display changes. |
| callback | Callback<[Rect](#rect9)\> | No | Callback used to return the new available area. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { Callback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

let callback: Callback<display.Rect> = (data: display.Rect) => {
  console.info(\`Listening enabled. Data: ${JSON.stringify(data)}\`);
};
let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  displayClass.off("availableAreaChange", callback);
} catch (exception) {
  console.error(\`Failed to unregister callback. Code: ${exception.code}, message: ${exception.message}\`);
}

#### \[h2\]getLiveCreaseRegion20+

getLiveCreaseRegion(): FoldCreaseRegion

Obtains the live crease region of the foldable device in the current display mode.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [FoldCreaseRegion](#foldcreaseregion10) | Live crease region of the device. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();
  let data: display.FoldCreaseRegion = displayClass.getLiveCreaseRegion();
  console.info(\`Succeeded in getting the live crease region. Data: ${JSON.stringify(data)}\`);
} catch (exception) {
  console.error(\`Failed to get the live crease region. Code: ${exception.code}, message: ${exception.message}\`);
}
