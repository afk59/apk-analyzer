# Interface (Window)

Represents a window instance, which is the basic unit managed by the window manager.

In the following API examples, you must use [getLastWindow()](../functions/document.md#windowgetlastwindow9), [createWindow()](../functions/document.md#windowcreatewindow9), or [findWindow()](../functions/document.md#windowfindwindow9) to obtain a Window instance (named windowClass in this example) and then call a method in this instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/-MHDFEv-TVGG7Tj--lxv7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C32D0A0490AE9F6CC531027C3AEF866F065040DC26029CF718963FCA0615B896)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Use [canIUse()](../../../../../../common-capabilities/arkts-api/syscap/document.md#caniuse) to check whether the device supports the system capability SystemCapability.Window.SessionManager and the corresponding APIs.
    

#### Modules to Import

import { window } from '@kit.ArkUI';

#### showWindow9+

showWindow(callback: AsyncCallback<void>): void

Shows this window. This API uses an asynchronous callback to return the result. This API takes effect only for a system window, application child window, modal window, or global floating window. For the main window of an application, this API moves it at the top when the main window is already displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/vw_DuG3CS_6HdfqekBlEYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BED46DA0709695FDFBD787D96AD131E9BDCD8A5DCCD4529F0D3BFC25B08CBFE7)

Before calling this API, you are advised to load the page by using [loadContent](../interface-windowstage/document.md#loadcontent9) or [setUIContent](#setuicontent9-1). If the main window has not finished loading and you call this API directly, the starting window keeps showing. Similarly, if the system window, application child window, modal window, or global floating window has finished loading and you call this API directly, the window is in the foreground but is not visible.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      try {
        // Create a child window.
        windowStage.createSubWindow("testSubWindow").then((subWindow) => {
          if (subWindow == null) {
            console.error('Failed to create the subWindow. Cause: The data is empty');
            return;
          }
          subWindow.setUIContent('pages/Index', (err) => {
            if (err.code) {
              console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the subWindow content.');
            try {
              subWindow.showWindow((err: BusinessError) => {
                const errCode: number = err.code;
                if (errCode) {
                  console.error(\`Failed to show the window. Error code: ${err.code}, message: ${err.message}\`);
                  return;
                }
                console.info('Succeeded in showing the window.');
              });
            } catch (exception) {
              console.error(\`Failed to show the window. Cause code: ${exception.code}, message: ${exception.message}\`);
            }
          })
        });
      } catch (exception) {
        console.error(\`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
  });
  }
}

#### showWindow9+

showWindow(): Promise<void>

Shows this window. This API uses a promise to return the result. This API takes effect only for a system window, application child window, modal window, or global floating window. For the main window of an application, this API moves it at the top when the main window is already displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/jEcGguk6SqqdrXBAkXsquQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8316EC9345BA095D0F5B30681CBD98B0E877E0CD0ADB6E177B19EBA3F02C217)

Before calling this API, you are advised to load the page by using [loadContent](../interface-windowstage/document.md#loadcontent9) or [setUIContent](#setuicontent9-1). If the main window has not finished loading and you call this API directly, the starting window keeps showing. Similarly, if the system window, application child window, modal window, or global floating window has finished loading and you call this API directly, the window is in the foreground but is not visible.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      try {
        // Create a child window.
        windowStage.createSubWindow("testSubWindow").then((subWindow) => {
          if (subWindow == null) {
            console.error('Failed to create the subWindow. Cause: The data is empty');
            return;
          }
          subWindow.setUIContent('pages/Index', (err) => {
            if (err.code) {
              console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the subWindow content.');
            try {
              let promise = subWindow.showWindow();
              promise.then(() => {
                console.info('Succeeded in showing the window.');
              }).catch((err: BusinessError) => {
                console.error(\`Failed to show the window. Error code: ${err.code}, message: ${err.message}\`);
              });
            } catch (exception) {
              console.error(\`Failed to show window. Cause code: ${exception.code}, message: ${exception.message}\`);
            }
          });
        });
      } catch (exception) {
        console.error(\`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### showWindow20+

showWindow(options: ShowWindowOptions): Promise<void>

Shows this window. This API uses a promise to return the result asynchronously. This API takes effect only for a system window or an application child window. For the main window of an application, this API moves it to the top when the main window is already displayed. You can pass parameters to control the window display behavior.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/0rv4Hes9TRi7g2DK9dMRQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12E09265A560106D58C7201AB6C6A29188FA22B33E06536B96660B9801543BE2)

Before calling this API, you are advised to load the page by using [loadContent](../interface-windowstage/document.md#loadcontent9) or [setUIContent](#setuicontent9-1). If the main window has not finished loading and you call this API directly, the starting window keeps showing. Similarly, if the system window, application child window, or global floating window has finished loading and you call this API directly, the window is in the foreground but is not visible.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowWindowOptions](../interfaces-others/document.md#showwindowoptions20) | Yes | Parameters for displaying a child window or system window. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function showWindow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter validation error. Possible cause: 1. The value of the parameter is out of the allowed range; 2. The length of the parameter exceeds the allowed length; 3. The parameter format is incorrect. |

**Example**

// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      // Create a child window.
      try {
        windowStage.createSubWindow('subWindow').then((data) => {
          if (data == null) {
            console.error('Failed to create the subWindow. Cause: The data is empty');
            return;
          }
          data.setUIContent('pages/Index', (err) => {
            if (err.code) {
              console.error('Failed to load the subWindow content. Cause: %{public}s', JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the subWindow content.');
            let options: window.ShowWindowOptions = {
              focusOnShow: false
            };
            try {
              data.showWindow(options).then(() => {
                console.info('Succeeded in showing window');
              }).catch((err: BusinessError) => {
                console.error(\`Failed to show window. Error code: ${err.code}, message: ${err.message}\`);
              });
            } catch (exception) {
              console.error(\`Failed to show window. Cause code: ${exception.code}, message: ${exception.message}\`);
            }
          });
        });
      } catch (exception) {
        console.error(\`Failed to create the sub window. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### destroyWindow9+

destroyWindow(callback: AsyncCallback<void>): void

Destroys this window. This API uses an asynchronous callback to return the result. It takes effect for a system window, an application child window, a global floating window, or a modal window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.destroyWindow((err) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in destroying the window.');
});

#### destroyWindow9+

destroyWindow(): Promise<void>

Destroys this window. This API uses a promise to return the result. It takes effect for a system window, an application child window, a global floating window, or a modal window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.destroyWindow();
promise.then(() => {
  console.info('Succeeded in destroying the window.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### moveWindowTo9+

moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void

Moves this window. This API uses an asynchronous callback to return the result. A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [moveWindowToAsync()](#movewindowtoasync12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/aNR7PWc7QFiSkfJYNk5iug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CD613A9B7C0C76C7ABD4715D39DA0151690453E24C3F1DF964E7857B7A62D7D)

-   This API is best suited for the floating window mode (when the window mode is **window.WindowStatusType.FLOATING**, which can obtained using [getWindowStatus()](#getwindowstatus12)). You are advised not to use it in other window modes.
    
-   In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the window moves relative to the upper-left corner of the screen. In non-freeform window mode, the window moves relative to the upper-left corner of its parent window.
    
-   To move the window relative to the top-left corner of the screen while in non-freeform window mode, call [moveWindowToGlobal()](#movewindowtoglobal15).
    
-   This API does not work for the main window in non-freeform window mode.
    

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X-coordinate to which the window moves, in px. A positive value indicates a position to the right of the origin, and a negative value indicates a position to the left of the origin. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Y-coordinate to which the window moves, in pixels. A positive value indicates a position above the origin, and a negative value indicates a position below the origin. The value must be an integer. Non-integer values are rounded down. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in moving the window.');
  });
} catch (exception) {
  console.error(\`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### moveWindowTo9+

moveWindowTo(x: number, y: number): Promise<void>

Moves this window. This API uses a promise to return the result. A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [moveWindowToAsync()](#movewindowtoasync12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/wJMPK7knSDevatBVXjY2Yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41B9AEC332B802E9359343F79DB61C9B0F0B681B0D526BAFA6B658B744293A4D)

-   This API is best suited for the floating window mode (when the window mode is **window.WindowStatusType.FLOATING**, which can obtained using [getWindowStatus()](#getwindowstatus12)). You are advised not to use it in other window modes.
    
-   In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the window moves relative to the upper-left corner of the screen. In non-freeform window mode, the window moves relative to the upper-left corner of its parent window.
    
-   To move the window relative to the top-left corner of the screen while in non-freeform window mode, call [moveWindowToGlobal()](#movewindowtoglobal15).
    
-   This API does not work for the main window in non-freeform window mode.
    

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X-coordinate to which the window moves, in px. A positive value indicates a position to the right of the origin, and a negative value indicates a position to the left of the origin. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Y-coordinate to which the window moves, in pixels. A positive value indicates a position above the origin, and a negative value indicates a position below the origin. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowTo(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### moveWindowToAsync12+

moveWindowToAsync(x: number, y: number): Promise<void>

Moves this window. This API uses a promise to return the result. A value is returned once the call takes effect. You can use [getWindowProperties()](#getwindowproperties9) in the callback (see the code snippet below) to obtain the final effect immediately.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/xE5qv3mMTNyKJ-DsDtglzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6BF6F84D8C918BD3A669DC8631121167B477699642F3A7CD4972ADA230ACF1D)

-   In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the window moves relative to the screen. In non-freeform window mode, the window moves relative to the main window.
    
-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.
    

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Coordinate position along the x-axis to which the window is moved, measured in px. A positive value means the position is to the right of the x-axis origin; a negative value means it is to the left; the value **0** means it is at the x-axis origin. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Coordinate position along the y-axis to which the window is moved, measured in px. A positive value means the position is below the y-axis origin; a negative value means it is above; the value **0** means it is at the y-axis origin. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowToAsync(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(\`Get window rect: \` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### moveWindowToAsync15+

moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>

Moves this window to the specified position. This API uses a promise to return the result. You can use the **moveConfiguration** parameter to specify the target display ID for the window movement. A value is returned once the call takes effect. You can use [getWindowProperties()](#getwindowproperties9) in the callback (see the code snippet below) to obtain the final effect immediately.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/xQK_G4iSTI6uNdoA6YLTig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C91F5910378A73162C8527C5E24F4ECC092E9BBD95D077EA6348A59D42DADDF)

-   In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the window moves relative to the screen. In non-freeform window mode, the window moves relative to the main window.
    
-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.
    

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 15.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Distance that the window moves along the x-axis, in px. A positive value indicates that the window moves to the right. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Distance that the window moves along the y-axis, in px. A positive value indicates that the window moves downwards. The value must be an integer. Non-integer values are rounded down. |
| moveConfiguration | [MoveConfiguration](../interfaces-others/document.md#moveconfiguration15) | No | Window movement configuration. If this parameter is not set, the window will stay on the current display. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. |

**Example**

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let moveConfiguration: window.MoveConfiguration = {
    displayId: 0
  };
  let promise = windowClass.moveWindowToAsync(300, 300, moveConfiguration);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(\`Get window rect: \` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### moveWindowToGlobal13+

moveWindowToGlobal(x: number, y: number): Promise<void>

Moves this window based on the coordinates. This API uses a promise to return the result. A value is returned once the call takes effect. You can use [getWindowProperties()](#getwindowproperties9) in the callback (see the code snippet below) to obtain the final effect immediately.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/9m0nfbtPRL2dHmSaTw6_xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=413D3AA18FBB1496231C4812E8A17A8DA62CC71657D8164369237C758DEA3467)

-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 13.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Distance that the window moves along the x-axis, in px, with the top-left corner of the display used as the origin. A positive value indicates that the window moves to the right, and a negative value indicates that the window moves to the left. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Distance that the window moves along the y-axis, in px, with the top-left corner of the display used as the origin. A positive value indicates that the window moves downwards, and a negative value indicates that the window moves upwards. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowToGlobal(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(\`Get window rect: \` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### moveWindowToGlobal15+

moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>

Moves this window to the specified position based on the coordinates. This API uses a promise to return the result. You can use the **moveConfiguration** parameter to specify the target display ID for the window movement. A value is returned once the call takes effect. You can use [getWindowProperties()](#getwindowproperties9) in the callback (see the code snippet below) to obtain the final effect immediately.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/6GzuZNR0TM-8BPitTrUypw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=664399126F73C9CB994229E601C0C8B316134515612D57BC31376C0ABAC4CC90)

-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 15.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Distance that the window moves along the x-axis, in px, with the top-left corner of the target display used as the origin. A positive value indicates that the window moves to the right, and a negative value indicates that the window moves to the left. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Distance that the window moves along the y-axis, in px, with the top-left corner of the target display used as the origin. A positive value indicates that the window moves downwards, and a negative value indicates that the window moves upwards. The value must be an integer. Non-integer values are rounded down. |
| moveConfiguration | [MoveConfiguration](../interfaces-others/document.md#moveconfiguration15) | No | Window movement configuration. If this parameter is not set, the window will stay on the current display. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. |

**Example**

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let moveConfiguration: window.MoveConfiguration = {
    displayId: 0
  };
  let promise = windowClass.moveWindowToGlobal(300, 300, moveConfiguration);
  promise.then(() => {
    console.info('Succeeded in moving the window.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(\`Get window rect: \` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to move the window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### moveWindowToGlobalDisplay20+

moveWindowToGlobalDisplay(x: number, y: number): Promise<void>

Moves the window based on the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system). This API uses a promise to return the result asynchronously.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/QHjQhFXBQF-SENkFxywYLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77DE7C565E920B53D90AE094474221E0FCAC4061B27E572E5F3CB7B1776766A2)

-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Distance that the window moves along the x-axis, in px, with the top-left corner of the primary display used as the origin. A positive value indicates that the window moves to the right, and a negative value indicates that the window moves to the left. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Distance that the window moves along the y-axis, in px, with the top-left corner of the primary display used as the origin. A positive value indicates that the window moves downwards, and a negative value indicates that the window moves upwards. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.moveWindowToGlobalDisplay(300, 300);
  promise.then(() => {
    console.info('Succeeded in moving the window in global display.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to move the window in global display. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to move the window in global display. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### clientToGlobalDisplay20+

clientToGlobalDisplay(winX: number, winY: number): Position

Converts relative coordinates (based on the top-left corner of the current window) into global coordinates (based on the top-left corner of the primary screen).

This API is not supported in windows that are subject to display scaling, such as floating windows on phones or tablets not in free windows mode.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| winX | number | Yes | Offset along the X-axis, in pixels, with the top-left corner of the current window as the origin. A positive value moves the window to the right; a negative value moves it to the left. The value must be an integer. Non-integer values are rounded down. |
| winY | number | Yes | Offset along the Y-axis, in pixels, with the top-left corner of the current window as the origin. A positive value moves the window downward; a negative value moves it upward. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Position](../interfaces-others/document.md#position20) | Coordinates after conversion. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

try {
  let position = windowClass.clientToGlobalDisplay(100, 100);
  console.info(\`Succeeded in converting the position in the current window to the position in global display. Position: \` + JSON.stringify(position));
} catch (exception) {
  console.error(\`Failed to convert the position. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### globalDisplayToClient20+

globalDisplayToClient(globalDisplayX: number, globalDisplayY: number): Position

Converts global coordinates (based on the top-left corner of the primary screen) into relative coordinates (based on the top-left corner of the current window).

This API is not supported in windows that are subject to display scaling, such as floating windows on phones or tablets not in free windows mode.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| globalDisplayX | number | Yes | Offset along the X-axis, in pixels, with the top-left corner of the current window as the origin. A positive value moves the window to the right; a negative value moves it to the left. The value must be an integer. Non-integer values are rounded down. |
| globalDisplayY | number | Yes | Offset along the Y-axis, in pixels, with the top-left corner of the current window as the origin. A positive value moves the window downward; a negative value moves it upward. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Position](../interfaces-others/document.md#position20) | Coordinates after conversion. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300010 | The operation in the current window status is invalid. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

try {
  let position = windowClass.globalDisplayToClient(100, 100);
  console.info(\`Succeeded in converting in the position in global display to the position in the current window. Position: \` + JSON.stringify(position));
} catch (exception) {
  console.error(\`Failed to convert the position. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### resize9+

resize(width: number, height: number, callback: AsyncCallback<void>): void

Changes the size of this window based on the top-left vertex of the window. This API uses an asynchronous callback to return the result.

A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [resizeAsync()](#resizeasync12).

The window size is restricted by [WindowLimits](../interfaces-others/document.md#windowlimits11). You can call [getWindowLimits](#getwindowlimits11) to find out the exact limits.

The new window width and height you set must meet the following limits:

If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. However, the system window and global floating window settings are not subject to these minimum width or height restrictions.

If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/VQAkWAPCQmWbDA4BIXE4rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5668718363A608DD9FD2A86AF6808014342301B02B664EC6AC8CB58FD1E768EF)

-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | New width of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. A negative value is invalid, and error code 401 is thrown. |
| height | number | Yes | New height of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. A negative value is invalid, and error code 401 is thrown. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.resize(500, 1000, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in changing the window size.');
  });
} catch (exception) {
  console.error(\`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### resize9+

resize(width: number, height: number): Promise<void>

Changes the size of this window based on the top-left vertex of the window. This API uses a promise to return the result.

A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [resizeAsync()](#resizeasync12).

The window size is restricted by [WindowLimits](../interfaces-others/document.md#windowlimits11). You can call [getWindowLimits](#getwindowlimits11) to find out the exact limits.

The new window width and height you set must meet the following limits:

If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. However, the system window and global floating window settings are not subject to these minimum width or height restrictions.

If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Y4szxPTCRmCnnpUYz-lMGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08C76DD57ACE61CE1F49D7C77E9A9C4292581243E3EACB4907FDAAD6CFC92CE5)

-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | New width of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. A negative value is invalid, and error code 401 is thrown. |
| height | number | Yes | New height of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. A negative value is invalid, and error code 401 is thrown. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.resize(500, 1000);
  promise.then(() => {
    console.info('Succeeded in changing the window size.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### resizeAsync12+

resizeAsync(width: number, height: number): Promise<void>

Changes the size of this window based on the top-left vertex of the window. This API uses a promise to return the result.

A value is returned once the call takes effect. You can use [getWindowProperties()](#getwindowproperties9) in the callback (see the code snippet below) to obtain the final effect immediately.

The window size is restricted by [WindowLimits](../interfaces-others/document.md#windowlimits11). You can call [getWindowLimits](#getwindowlimits11) to find out the exact limits.

The new window width and height you set must meet the following limits:

If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. However, the system window and global floating window settings are not subject to these minimum width or height restrictions.

If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect.

This API takes effect only when the window is in freeform window mode (that is, the window mode is window.WindowStatusType.FLOATING, which can be obtained by calling [getWindowStatus()](#getwindowstatus12)). Otherwise, the error code 1300010 is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/imuzzZ2XTuGPyUQRayQGJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=482F7C4B86F0481CF23D10D9FA72AAC90B30B45201822874BDA2CB2D643D8CBE)

-   In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API does not work for the main window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | New width of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. A negative value is invalid, and error code 401 is thrown. |
| height | number | Yes | New height of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. A negative value is invalid, and error code 401 is thrown. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300010 | The operation in the current window status is invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.resizeAsync(500, 1000);
  promise.then(() => {
    console.info('Succeeded in changing the window size.');
    let rect = windowClass?.getWindowProperties().windowRect;
    console.info(\`Get window rect: \` + JSON.stringify(rect));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to change the window size. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowProperties9+

getWindowProperties(): WindowProperties

Obtains the properties of this window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowProperties](../interfaces-others/document.md#windowproperties) | Window properties obtained. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let properties = windowClass.getWindowProperties();
} catch (exception) {
  console.error(\`Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowDensityInfo15+

getWindowDensityInfo(): WindowDensityInfo

Obtains the display density information of this window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 15.

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowDensityInfo](../interfaces-others/document.md#windowdensityinfo15) | Display density information of the window. If the return value is **\[-1, -1, -1\]**, the current device does not support this API. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let densityInfo = windowClass.getWindowDensityInfo();
} catch (exception) {
  console.error(\`Failed to obtain the window densityInfo. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowContainerColor20+

setWindowContainerColor(activeColor: string, inactiveColor: string): void

Sets the background color of the main window container for both when it has focus and when it does not. In the stage model, you need to call this API after [loadContent()](#loadcontent9) or [setUIContent()](#setuicontent9).

The background color you set here covers the entire window, including both the title bar and the content area. If you also use [setWindowBackgroundColor()](#setwindowbackgroundcolor9), the content area shows the window background color, whereas the title bar shows the container background color.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

**Required permissions**: ohos.permission.SET\_WINDOW\_TRANSPARENT

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| activeColor | string | Yes | Background color of the window container when it is focused. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**. |
| inactiveColor | string | Yes | Background color of the window container when it is not focused. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**. The opacity is fixed at **'FF'**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in loading the content.');
      // Obtain the main window.
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        let activeColor: string = '#00000000';
        let inactiveColor: string = '#FF000000';
        try {
          windowClass.setWindowContainerColor(activeColor, inactiveColor);
          console.info('Succeeded in setting window container color.');
        } catch (exception) {
          console.error(\`Failed to set the window container color. Cause code: ${exception.code}, message: ${exception.message}\`);
        };
      });
    });
  }
}

#### getGlobalRect13+

getGlobalRect(): Rect

Obtains the actual display area of this window on the physical screen. This API returns the result synchronously.

This API can determine the actual on-screen location and size of a window that has been resized on certain devices.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 13.

**Return value**

| Type | Description |
| :-- | :-- |
| [Rect](../interfaces-others/document.md#rect7) | A set of four values, which indicates the horizontal distance from the screen's top-left corner to the window's left edge, the vertical distance from the screen's top-left corner to the window's top edge, the width of the window after scaling, and the height of the window after scaling. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  let rect = windowClass.getGlobalRect();
  console.info(\`Succeeded in getting window rect: \` + JSON.stringify(rect));
} catch (exception) {
  console.error(\`Failed to get window rect. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowAvoidArea9+

getWindowAvoidArea(type: AvoidAreaType): AvoidArea

Obtains the avoid area of this window.

Main window/Subwindow:

-   In the free-floating window mode (the window mode is [window.WindowStatusType.FLOATING](../enums/document.md#windowstatustype11)) under the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state, only the avoid area of the fixed soft keyboard type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_KEYBOARD**) is available.
-   In the free-floating window mode of the main window in the non-freeform window state, only the avoid area of the system bar type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_SYSTEM**) is available.
-   In other scenarios, the main window can obtain the avoid area calculated by this API only when it is not in the floating window mode or the device type is phone or tablet. Otherwise, the obtained avoid area is empty.
-   In non-freeform window state or non-floating window mode, the child window can obtain the avoid area calculated by this API only when its position and size are the same as those of the main window. Otherwise, the obtained avoid area is empty.

Global floating window, modal window, or system window:

-   This API can be called to obtain the avoid area only after [setSystemAvoidAreaEnabled](#setsystemavoidareaenabled18) is called. Otherwise, the obtained avoid area is empty.

This API is generally applicable to the following scenarios:

-   In the [onWindowStageCreate()](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onwindowstagecreate) callback, this API is used to obtain the initial layout avoid area when the application starts.
-   This API is used when a child window needs to temporarily display content and requires layout adjustments to avoid certain areas.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AvoidAreaType](../enums/document.md#avoidareatype7) | Yes | Type of the avoid area. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AvoidArea](../interfaces-others/document.md#avoidarea7) | Area where the window cannot be displayed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |

**Example**

let type = window.AvoidAreaType.TYPE\_SYSTEM;
try {
  let avoidArea = windowClass.getWindowAvoidArea(type);
} catch (exception) {
  console.error(\`Failed to obtain the area. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowAvoidAreaIgnoringVisibility22+

getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea

Obtains the avoid area of this application window, even if the avoid area is invisible.

Main window/Subwindow:

-   When the main window is in the free-floating window mode (the window mode is window.WindowStatusType.FLOATING\](arkts-apis-window-e.md#windowstatustype11)) under a non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state, only the avoid area of the system bar type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_SYSTEM**) is available.
-   In other scenarios, the main window can obtain the avoid area calculated by this API only when it is not in the floating window mode or the device type is phone or tablet. Otherwise, the obtained avoid area is empty.
-   In non-freeform window state or non-floating window mode, the child window can obtain the avoid area calculated by this API only when its position and size are the same as those of the main window. Otherwise, the obtained avoid area is empty.

Global floating window, modal window, or system window:

-   This API can be called to obtain the avoid area only after [setSystemAvoidAreaEnabled](#setsystemavoidareaenabled18) is called. Otherwise, the obtained avoid area is empty.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AvoidAreaType](../enums/document.md#avoidareatype7) | Yes | Type of the avoid area. Note that obtaining the avoid area for the soft keyboard type is not supported. If **TYPE\_KEYBOARD** is passed in, error code 1300016 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AvoidArea](../interfaces-others/document.md#avoidarea7) | Area where the window cannot be displayed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. Possible cause: 1. Parameter verification failed. |

**Example**

let type = window.AvoidAreaType.TYPE\_SYSTEM;
try {
  let avoidArea = windowClass.getWindowAvoidAreaIgnoringVisibility(type);
} catch (exception) {
  console.error(\`Failed to obtain the area. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setSystemAvoidAreaEnabled18+

setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>

Enables the capability to obtain the window avoid area information using [getWindowAvoidArea()](#getwindowavoidarea9) or listen for window avoid area changes using [on('avoidAreaChange')](#onavoidareachange9) after a global floating window, modal window, or system window is created.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to enable the window to access the avoid area.

**true** to enable, **false** otherwise. The default value is **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      let windowClass: window.Window | undefined = undefined;
      let config: window.Configuration = {
        name: "test",
        windowType: window.WindowType.TYPE\_DIALOG,
        decorEnabled: true,
        ctx: this.context
      };
      try {
        window.createWindow(config, (err: BusinessError, data) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(\`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}\`);
            return;
          }
          windowClass = data;
          windowClass.setUIContent("pages/Test");
          let enabled = true;
          let promise = windowClass.setSystemAvoidAreaEnabled(enabled);
          promise.then(() => {
            let type = window.AvoidAreaType.TYPE\_SYSTEM;
            let avoidArea = windowClass?.getWindowAvoidArea(type);
          }).catch((err: BusinessError) => {
            console.error(\`Failed to obtain the system window avoid area. Cause code: ${err.code}, message: ${err.message}\`);
          });
        });
      } catch (exception) {
        console.error(\`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### isSystemAvoidAreaEnabled18+

isSystemAvoidAreaEnabled(): boolean

Checks whether a floating window, modal window, or system window (**WindowType** is a system window) is enabled to access the [avoid area](../interfaces-others/document.md#avoidarea7).

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Check result for whether the window is enabled to access the avoid area.

**true** if enabled, **false** otherwise.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      let windowClass: window.Window | undefined = undefined;
      let config: window.Configuration = {
        name: "test",
        windowType: window.WindowType.TYPE\_DIALOG,
        decorEnabled: true,
        ctx: this.context
      };
      try {
        window.createWindow(config, (err: BusinessError, data) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(\`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}\`);
            return;
          }
          windowClass = data;
          windowClass.setUIContent("pages/Test");
          let promise = windowClass.setSystemAvoidAreaEnabled(true);
          promise.then(() => {
            let enabled = windowClass?.isSystemAvoidAreaEnabled();
          }).catch((err: BusinessError) => {
            console.error(\`Failed to obtain the system window avoid area enable. Cause code: ${err.code}, message: ${err.message}\`);
          });
        });
      } catch (exception) {
        console.error(\`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setTitleAndDockHoverShown14+

setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>

Sets whether to show the window title bar and dock bar when the cursor hovers over the hot zone while the main window is in full-screen mode. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Atomic service API**: This API can be used in atomic services since API version 14.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTitleHoverShown | boolean | No | 
Whether to show the window title bar.

**true** to show, **false** otherwise. The default value is **true**.

 |
| isDockHoverShown | boolean | No | 

Whether to show the dock bar.

**true** to show, **false** otherwise. The default value is **true**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Load the page corresponding to the main window.
    windowStage.loadContent('pages/Index', (err) => {
      let mainWindow: window.Window | undefined = undefined;
      // Obtain the main window.
      windowStage.getMainWindow().then(
        data => {
          if (!data) {
            console.error('Failed to get main window. Cause: The data is undefined.');
            return;
          }
          mainWindow = data;
          console.info(\`Succeeded in obtaining the main window. Data: ${JSON.stringify(data)}\`);
          // Call maximize to enable the full-screen mode for the window.
          mainWindow.maximize(window.MaximizePresentation.ENTER\_IMMERSIVE);
          // Call setTitleAndDockHoverShown to hide the window title bar and dock bar.
          mainWindow.setTitleAndDockHoverShown(false, false);
        }
      ).catch((err: BusinessError) => {
          if(err.code){
            console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          }
      });
    });
  }
}

#### setWindowLayoutFullScreen9+

setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>

Sets whether the application main window layout or the application child window layout is immersive. This API uses a promise to return the result. It does not work when called by other windows, and no error is reported.

An immersive layout means that the layout does not avoid the status bar or Bottom navigation area, and components may overlap with them.

A non-immersive layout means that the layout avoids the status bar and Bottom navigation area, and components do not overlap with them.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**

In versions earlier than HarmonyOS 5.0.2, this API can be called properly on all devices.

Starting from HarmonyOS 5.0.2, this API has no effect and does not report errors for a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state, but takes effect when the device exits that state. It can be properly called on a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLayoutFullScreen | boolean | Yes | Whether the layout of the window is immersive. (In immersive layout mode, the status bar and Bottom navigation area remain visible.) **true** if immersive, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen = true;
      try {
        let promise = windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
        promise.then(() => {
          console.info('Succeeded in setting the window layout to full-screen mode.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setImmersiveModeEnabledState12+

setImmersiveModeEnabledState(enabled: boolean): void

Sets whether to enable the immersive layout for the main window. This API does not change the window mode or size. It can be called only by the main window and child windows.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**

In versions earlier than HarmonyOS 5.0.2, this API can be called properly on all devices.

Since HarmonyOS 5.0.2, calls to this API do not take effect or return an error on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. On a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows, this API can be properly called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to enable the immersive layout.

**true** to enable, **false** otherwise.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

try {
  let enabled = false;
  windowClass.setImmersiveModeEnabledState(enabled);
} catch (exception) {
  console.error(\`Failed to set the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getImmersiveModeEnabledState12+

getImmersiveModeEnabledState(): boolean

Checks whether the immersive layout is enabled for this window.

The return value is consistent with the settings applied via [setImmersiveModeEnabledState()](#setimmersivemodeenabledstate12) and [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen9). If neither of these APIs has been called, the default return value is **false**.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Check result for whether the immersive layout is enabled.

**true** if enabled, **false** otherwise.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

try {
  let isEnabled = windowClass.getImmersiveModeEnabledState();
} catch (exception) {
  console.error(\`Failed to get the window immersive mode enabled status. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### isImmersiveLayout20+

isImmersiveLayout(): boolean

Checks whether this window is in immersive mode.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the window is in immersive mode. **true** if in immersive mode, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let isEnabled = windowClass.isImmersiveLayout();
} catch (exception) {
  console.error(\`Failed to check if the window layout is in immersive mode. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowDelayRaiseOnDrag19+

setWindowDelayRaiseOnDrag(isEnabled: boolean): void

Sets whether to enable delayed raising for the window. This API takes effect only for the main window and child windows.

If this API is not called or **false** is passed, the main window and child windows are raised immediately upon a left mouse button press by default.

When this API is called to enable delayed raising, in cross-window drag-and-drop situations, the window that contains the draggable component does not raise until the left mouse button is released, rather than raising immediately when the button is pressed.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 19.

**Device behavior differences**: This API can be called on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | boolean | Yes | 
Whether to enable delayed raising.

**true** to enable, **false** otherwise.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.function setWindowDelayRaiseOnDrag can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  windowClass.setWindowDelayRaiseOnDrag(true);
} catch (exception) {
  console.error(\`Failed to set window delay raise. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setDragKeyFramePolicy20+

setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>

Sets the keyframe policy for dragging the main window. This API uses a promise to return the result.

If this API is called by a non-main window, error code 1300004 is returned.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on 2-in-1 devices but returns error code 801 on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyFramePolicy | [KeyFramePolicy](../interfaces-others/document.md#keyframepolicy20) | Yes | Keyframe policy for dragging. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyFramePolicy](../interfaces-others/document.md#keyframepolicy20)\> | Promise used to return the keyframe policy that takes effect. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. The parameter format is incorrect. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let keyFramePolicy: window.KeyFramePolicy = {
        enable: true
      }
      try {
        let promise = windowClass.setDragKeyFramePolicy(keyFramePolicy);
        promise.then((ret: window.KeyFramePolicy) => {
          console.info(\`Succeeded in setting key frame: ${JSON.stringify(ret)}\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set key frame. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set key frame. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setWindowSystemBarEnable9+

setWindowSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>

Sets whether to show the main window's status bar and bottom navigation (which may appear as a navigation bar or a three-button navigation bar depending on user settings). The display of the status bar and bottom navigation is controlled by status, and the navigation parameter does not have any impact. This API uses a promise to return the result.

The return value does not indicate that the status bar and Bottom navigation area are shown or hidden. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Device behavior differences**

For versions earlier than HarmonyOS 5.0.0, this API can be properly called on all devices.

Since HarmonyOS 5.0.0, calls to this API do not take effect or return an error on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. On a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows, this API can be properly called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| names | Array<'status'|'navigation'> | Yes | 
Whether to show the status bar and Bottom navigation area in full-screen or maximized mode.

For example, to show all of them, set this parameter to **\['status', 'navigation'\]**; to hide them, set this parameter to **\[\]**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// The following assumes that all of them are hidden.
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = \[\];
      try {
        let promise = windowClass.setWindowSystemBarEnable(names);
        promise.then(() => {
          console.info('Succeeded in setting the system bar to be invisible.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setSpecificSystemBarEnabled11+

setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>

Sets whether to show or hide the status bar and Bottom navigation area of the main window. This API uses a promise to return the result.

The return value does not indicate that the status bar and Bottom navigation area are shown or hidden. This API does not take effect when it is called by a child window. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 11.

**Device behavior differences**

For versions earlier than HarmonyOS 5.0.0, this API can be properly called on all devices.

Since HarmonyOS 5.0.0, calls to this API do not take effect or return an error on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. On a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows, this API can be properly called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | [SpecificSystemBar](../types/document.md#specificsystembar11) | Yes | Type of the system bar to be shown or hidden. |
| enable | boolean | Yes | Whether to show the status bar and Bottom navigation area in full-screen mode. **true** to show, **false** otherwise. |
| enableAnimation12+ | boolean | No | Whether to enable animation when the status bar and Bottom navigation area status changes. **true** to enable, **false** otherwise. The default value is **false**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// Here, the status bar is hidden.
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let promise = windowClass.setSpecificSystemBarEnabled('status', false);
        promise.then(() => {
          console.info('Succeeded in setting the system bar to be invisible.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setWindowSystemBarProperties9+

setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>

Sets the properties of the status bar of the main window. This API uses a promise to return the result.

This API does not take effect when it is called by a child window. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**: This API has no effect and does not report errors for a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. It can be properly called on a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| systemBarProperties | [SystemBarProperties](../interfaces-others/document.md#systembarproperties) | Yes | three-button navigation bar and |
| status bar. |  |  |  |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        // The following properties are supported since API version 8.
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      try {
        let promise = windowClass.setWindowSystemBarProperties(SystemBarProperties);
        promise.then(() => {
          console.info('Succeeded in setting the system bar properties.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### getWindowSystemBarProperties12+

getWindowSystemBarProperties(): SystemBarProperties

Obtains the properties of the status bar in the main window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| [SystemBarProperties](../interfaces-others/document.md#systembarproperties) | Properties of the status bar. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let systemBarProperty = windowClass.getWindowSystemBarProperties();
        console.info('Success in obtaining system bar properties. Property: ' + JSON.stringify(systemBarProperty));
      } catch (err) {
        console.error(\`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}\`);
      }
    });
  }
};

#### setStatusBarColor18+

setStatusBarColor(color: ColorMetrics): Promise<void>

Sets the text color of the status bar in the main window. This API uses a promise to return the result.

Setting the status bar text color is not supported for child windows. Calling this API on a child window will have no effect. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Device behavior differences**: This API has no effect and does not report errors for a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. It can be properly called on a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ColorMetrics](../../../ui/arkui/graphics/document.md#colormetrics12) | Yes | Text color of the status bar. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported on this device. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let promise = windowClass.setStatusBarColor(ColorMetrics.numeric(0x112233));
        promise.then(() => {
          console.info('Succeeded in setting the status bar color.');
        }).catch((err: BusinessError) => {
          console.error(\`Set the status bar color failed. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set the status bar color. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### getStatusBarProperty18+

getStatusBarProperty(): StatusBarProperty

Obtains the properties (for example, text color) of the status bar in the main window.

Calls to this API from child windows are not supported and return error code 1300002.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Return value**

| Type | Description |
| :-- | :-- |
| [StatusBarProperty](../interfaces-others/document.md#statusbarproperty18) | Status bar properties, such as its color. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported on this device. |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let statusBarProperty = windowClass.getStatusBarProperty();
        console.info('Succeeded in obtaining system bar properties. Property: ' + JSON.stringify(statusBarProperty));
      } catch (err) {
        console.error(\`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}\`);
      }
    });
  }
};

#### setPreferredOrientation9+

setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void

Sets the orientation for the main window. This API uses a callback to return the result asynchronously. For details about the development practices of orientation, see [Display Orientation Switching](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-landscape-and-portrait-development). This API does not take effect when it is called by a child window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Device behavior differences**: This API can be called and takes effect immediately on devices that support sensor rotation and is not in [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state regardless of whether they support freeform windows. This API can be called on devices that support sensor rotation and are in the free window state, but the call does not take effect or report an error. It takes effect only when the device is switched to a state other than the free window state. In other cases, the call does not take effect or report an error.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| orientation | [Orientation](../enums/document.md#orientation9) | Yes | Orientation to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. The callback indicates the API call result. It does not mean that the application rotation animation ends. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let orientation = window.Orientation.AUTO\_ROTATION;
      try {
        windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(\`Failed to set window orientation. Cause code: ${err.code}, message: ${err.message}\`);
            return;
          }
          console.info('Succeeded in setting window orientation.');
        });
      } catch (exception) {
        console.error(\`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setPreferredOrientation9+

setPreferredOrientation(orientation: Orientation): Promise<void>

Sets the preferred orientation for the main window. This API uses a promise to return the result. This API does not take effect when it is called by a child window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Device behavior differences**: This API can be called and takes effect immediately on devices that support sensor rotation and is not in [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state regardless of whether they support freeform windows. This API can be called on devices that support sensor rotation and are in the free window state, but the call does not take effect or report an error. It takes effect only when the device is switched to a state other than the free window state. In other cases, the call does not take effect or report an error.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| orientation | [Orientation](../enums/document.md#orientation9) | Yes | Orientation to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let orientation = window.Orientation.AUTO\_ROTATION;
      try {
        let promise = windowClass.setPreferredOrientation(orientation);
        promise.then(() => {
          console.info('Succeeded in setting the window orientation.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the window orientation. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### getPreferredOrientation12+

getPreferredOrientation(): Orientation

Obtains the orientation of the window. If no orientation is specified, **window.Orientation.UNSPECIFIED** is returned.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| [Orientation](../enums/document.md#orientation9) | Orientation. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let orientation = windowClass.getPreferredOrientation();
      } catch (exception) {
        console.error(\`Failed to get window orientation. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
};

#### getUIContext10+

getUIContext(): UIContext

Obtains a UIContext instance.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Return value**

| Type | Description |
| :-- | :-- |
| [UIContext](../../../ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | UIContext instance obtained. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window, UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Load content for the main window.
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in loading the content.');
      // Obtain the main window.
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
        // Obtain a UIContext instance.
        let uiContext: UIContext | null = null;
        uiContext = windowClass.getUIContext();
      });
    });
  }
};

#### setUIContent9+

setUIContent(path: string, callback: AsyncCallback<void>): void

Loads the content of a page, with its path in the current project specified, to this window. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page from which the content will be loaded. In the stage model, the path is configured in the **main\_pages.json** file of the project. In the FA model, the path is configured in the **config.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main\_pages.json** or **config.json** file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.setUIContent('pages/page2/page3', (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in loading the content.');
  });
} catch (exception) {
  console.error(\`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setUIContent9+

setUIContent(path: string): Promise<void>

Loads the content of a page, with its path in the current project specified, to this window. This API uses a promise to return the result.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page content which needs to be loaded to the window. In the stage model, the path needs to be configured in the **main\_pages.json** file of the project. In the FA model, the path needs to be configured in the **config.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main\_pages.json** or **config.json** file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.setUIContent('pages/page2/page3');
  promise.then(() => {
    console.info('Succeeded in loading the content.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### loadContent9+

loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

Loads the content of a page, with its path in the current project specified, to this window, and transfers the state attribute to the page through a local storage. This API uses an asynchronous callback to return the result.

You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page content which needs to be loaded to the window. The path needs to be configured in the **main\_pages.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main\_pages.json** file. |
| storage | [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) | Yes | Page-level UI state storage unit, which is used to transfer the state attribute for the page. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
windowClass.loadContent('pages/page2', storage, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in loading the content.');
});

#### loadContent9+

loadContent(path: string, storage: LocalStorage): Promise<void>

Loads the content of a page, with its path in the current project specified, to this window, and transfers the state attribute to the page through a local storage. This API uses a promise to return the result.

You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page content which needs to be loaded to the window. The path needs to be configured in the **main\_pages.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main\_pages.json** file. |
| storage | [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) | Yes | Page-level UI state storage unit, which is used to transfer the state attribute for the page. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
let promise = windowClass.loadContent('pages/page2', storage);
promise.then(() => {
  console.info('Succeeded in loading the content.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
});

#### loadContentByName11+

loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void

Loads the content of a [named route](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#named-route) page to this window, and transfers the state attribute to the page through a local storage. This API uses an asynchronous callback to return the result.

You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the named route page. |
| storage | [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) | Yes | Page-level UI state storage unit, which is used to transfer the state attribute for the page. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import \* as Index from '../pages/Index'; // Import the named route page.

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let storage: LocalStorage = new LocalStorage();
    let newValue: Number = 121;
    storage.setOrCreate('storageSimpleProp', newValue);
    try {
      let windowClass: window.Window = windowStage.getMainWindowSync();
      if (!windowClass) {
        console.error('Failed to get main window.');
        return;
      }
      windowClass.loadContentByName(Index.entryName, storage, (err: BusinessError) => {
        const errCode: number = err?.code;
        if (errCode) {
          console.error(\`Failed to load the content. Cause code: ${err?.code}, message: ${err?.message}\`);
          return;
        }
        console.info('Succeeded in loading the content.');
      });
    } catch (exception) {
      console.error(\`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName, useSharedStorage: true})
@Component
export struct Index {
  @State message: string = 'Hello World'
  @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### loadContentByName11+

loadContentByName(name: string, callback: AsyncCallback<void>): void

Loads the content of a [named route](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#named-route) page to this window. This API uses an asynchronous callback to return the result.

You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the named route page. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import \* as Index from '../pages/Index'; // Import the named route page.

try {
  (windowClass as window.Window).loadContentByName(Index.entryName, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in loading the content.');
  });
} catch (exception) {
  console.error(\`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}\`);
}

// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName})
@Component
export struct Index {
  @State message: string = 'Hello World'
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### loadContentByName11+

loadContentByName(name: string, storage?: LocalStorage): Promise<void>

Loads the content of a [named route](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#named-route) page to this window, and transfers the state attribute to the page through a local storage. This API uses a promise to return the result.

You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the named route page. |
| storage | [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) | No | Page-level UI state storage unit, which is used to transfer the state attribute for the page content loaded to the window. This parameter is left empty by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import \* as Index from '../pages/Index'; // Import the named route page.

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
try {
  let promise = (windowClass as window.Window).loadContentByName(Index.entryName, storage);
  promise.then(() => {
    console.info('Succeeded in loading the content.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}\`);
}

// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName, useSharedStorage: true})
@Component
export struct Index {
  @State message: string = 'Hello World'
  @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### isWindowShowing9+

isWindowShowing(): boolean

Checks whether this window is displayed.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the window is displayed. **true** if displayed, **false** otherwise. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let data = windowClass.isWindowShowing();
  console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
} catch (exception) {
  console.error(\`Failed to check whether the window is showing. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('windowSizeChange')7+

on(type: 'windowSizeChange', callback: Callback<Size>): void

Subscribes to the window size change event. This API can be called only by the main thread.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowSizeChange'**, indicating the window size change event. |
| callback | Callback<[Size](../interfaces-others/document.md#size7)\> | Yes | Callback used to return the window size. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

try {
  windowClass.on('windowSizeChange', (data) => {
    console.info('Succeeded in enabling the listener for window size changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(\`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowSizeChange')7+

off(type: 'windowSizeChange', callback?: Callback<Size>): void

Unsubscribes from the window size change event. This API can be called only by the main thread.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowSizeChange'**, indicating the window size change event. |
| callback | Callback<[Size](../interfaces-others/document.md#size7)\> | No | Callback used to return the window size. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

const callback = (size: window.Size) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('windowSizeChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('windowSizeChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('windowSizeChange');
} catch (exception) {
  console.error(\`Failed to disable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('avoidAreaChange')9+

on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void

Subscribes to events indicating changes to the system avoid area of the current application window.

Main window/Subwindow:

-   When the callback is triggered in the free-floating window mode (the window mode is [window.WindowStatusType.FLOATING](../enums/document.md#windowstatustype11)) under the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state, only the avoid area of the fixed soft keyboard type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_KEYBOARD**) is available.
-   When the callback is triggered in the free-floating window mode of the main window in the non-freeform window state, only the avoid area of the system bar type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_SYSTEM**) is available.
-   When the callback is triggered in the main window in other scenarios, the calculated avoid area is returned only when the window is not in the free-floating window mode or the device type is phone or tablet. Otherwise, an empty avoid area is returned.
-   When the callback is triggered in the child window in the non-freeform window state or non-free-floating window mode, the calculated avoid area of the child window is returned only when the position and size of the child window are the same as those of the main window. Otherwise, an empty avoid area is returned.

Global floating window, modal window, or system window:

-   The calculated avoid area is returned only when the callback is triggered after [setSystemAvoidAreaEnabled](#setsystemavoidareaenabled18) is called. Otherwise, an empty avoid area is returned.

Common scenarios for triggering this event are as follows: transitions between full-screen mode, floating mode, and split-screen mode of the application window; rotation of the application window; transitions between folded and unfolded states of a foldable device; transfer of the application window between multiple devices. For details about how to implement the immersive layout, see [Immersive Effect Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-develop-apply-immersive-effects).

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'avoidAreaChange'**, indicating the system avoid area change event. |
| callback | Callback<[AvoidAreaOptions](../interfaces-others/document.md#avoidareaoptions12)\> | Yes | Callback used to return the avoid area and avoid area type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

try {
  windowClass.on('avoidAreaChange', (data) => {
    console.info('Succeeded in enabling the listener for system avoid area changes. type:' +
    JSON.stringify(data.type) + ', area: ' + JSON.stringify(data.area));
  });
} catch (exception) {
  console.error(\`Failed to enable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('avoidAreaChange')9+

off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void

Unsubscribes from the events indicating changes to the system avoid area of the current app window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'avoidAreaChange'**, indicating the system avoid area change event. |
| callback | Callback<[AvoidAreaOptions](../interfaces-others/document.md#avoidareaoptions12)\> | No | Callback used to return the avoid area and avoid area type. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

interface Param {
  type: window.AvoidAreaType,
  area: window.AvoidArea
}
const callback = (data: Param) => {
  // ...
}
try {
  windowClass.on('avoidAreaChange', callback);

  windowClass.off('avoidAreaChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('avoidAreaChange');
} catch (exception) {
  console.error(\`Failed to enable or disable the listener for system avoid area changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('keyboardHeightChange')7+

on(type: 'keyboardHeightChange', callback: Callback<number>): void

Subscribes to the event indicating soft keyboard height changes in the fixed state. The system notifies the keyboard height change when the soft keyboard is invoked by the window and overlaps with the window. Starting from API version 10, the soft keyboard can be set to the fixed or floating state. For details, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardHeightChange'**, indicating the keyboard height change event. |
| callback | Callback<number> | Yes | Callback used to return the current keyboard height, which is an integer, in px. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.on('keyboardHeightChange', (data) => {
    console.info('Succeeded in enabling the listener for keyboard height changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(\`Failed to enable the listener for keyboard height changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('keyboardHeightChange')7+

off(type: 'keyboardHeightChange', callback?: Callback<number>): void

Unsubscribes from the event indicating soft keyboard height changes in the fixed state so that the application does not receive notifications of soft keyboard height changes. Starting from API version 10, the soft keyboard can be set to the fixed or floating state. For details, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardHeightChange'**, indicating the keyboard height change event. |
| callback | Callback<number> | No | Callback used to return the current keyboard height, which is an integer, in px. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (height: number) => {
  // ...
}
try {
  windowClass.on('keyboardHeightChange', callback);

  windowClass.off('keyboardHeightChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('keyboardHeightChange');
} catch (exception) {
  console.error(\`Failed to disable the listener for keyboard height changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('keyboardWillShow')20+

on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void

Subscribes to the event indicating that the soft keyboard in the fixed state is about to show, or the soft keyboard is transitioning from the floating state to the fixed state.

For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardWillShow'**, indicating the soft keyboard in the fixed state is about to show. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | Yes | Callback used to return the information about the soft keyboard. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardWillShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(\`Keyboard will show animation. keyboardInfo: \` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillShow', callback);
  console.info(\`Register keyboard will show animation success\`);
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('keyboardWillShow')20+

off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void

Unsubscribes from the event indicating that the soft keyboard in the fixed state is about to show. For details about the APIs used to set the input method panel to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardWillShow'**, indicating the soft keyboard in the fixed state is about to show. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | No | Callback used to return the information about the soft keyboard. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardWillShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(\`Keyboard will show animation. keyboardInfo: \` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillShow', callback);
  windowClass.off('keyboardWillShow', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('keyboardWillShow');
  console.info(\`Unregister keyboard will show animation success\`);
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('keyboardWillHide')20+

on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void

Subscribes to the event indicating that the soft keyboard in the fixed state is about to hide, or the soft keyboard is transitioning from the fixed state to the floating state.

For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardWillHide'**, indicating the soft keyboard in the fixed state is about to hide. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | Yes | Callback used to return the information about the soft keyboard. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardWillHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(\`Keyboard will hide animation. keyboardInfo: \` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillHide', callback);
  console.info(\`Register keyboard will hide animation success\`);
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('keyboardWillHide')20+

off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void

Unsubscribes from the event indicating that the soft keyboard in the fixed state is about to hide. For details about the APIs used to set the input method panel to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardWillHide'**, indicating the soft keyboard in the fixed state is about to hide. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | No | Callback used to return the information about the soft keyboard. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardWillHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  console.info(\`Keyboard will hide animation. keyboardInfo: \` + JSON.stringify(keyboardInfo));
}
try {
  windowClass.on('keyboardWillHide', callback);
  windowClass.off('keyboardWillHide', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('keyboardWillHide');
  console.info(\`Unregister keyboard will hide animation success\`);
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('keyboardDidShow')18+

on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void

Subscribes to the event indicating that the show animation of the soft keyboard in the fixed state is completed, or when the soft keyboard finishes transitioning from the floating state to the fixed state.

For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardDidShow'**, indicating the show animation of the soft keyboard in the fixed state is completed. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | Yes | Callback used to return the information about the soft keyboard. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardDidShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.on('keyboardDidShow', (keyboardInfo) => {
    console.info('keyboard show animation completion. keyboardInfo: ' + JSON.stringify(keyboardInfo));
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('keyboardDidShow')18+

off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void

Unsubscribes from the event indicating that the show animation of the soft keyboard in the fixed state is completed, For details about the APIs used to set the input method panel to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardDidShow'**, indicating the show animation of the soft keyboard in the fixed state is completed. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | No | Callback used to return the information about the soft keyboard. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardDidShow can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  // ...
}
try {
  windowClass.on('keyboardDidShow', callback);
  windowClass.off('keyboardDidShow', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('keyboardDidShow');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('keyboardDidHide')18+

on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void

Subscribes to the event indicating that the hide animation of the soft keyboard in the fixed state is completed, or when the soft keyboard finishes transitioning from the fixed state to the floating state.

For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardDidHide'**, indicating the hide animation of the soft keyboard in the fixed state is completed. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | Yes | Callback used to return the information about the soft keyboard. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardDidHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.on('keyboardDidHide', (keyboardInfo) => {
    console.info('keyboard hide animation completion. keyboardInfo: ' + JSON.stringify(keyboardInfo));
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('keyboardDidHide')18+

off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void

Unsubscribes from the event indicating that the hide animation of the soft keyboard in the fixed state is completed, For details about the APIs used to set the input method panel to the fixed or floating state, see [Input Method Service](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#changeflag10).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'keyboardDidHide'**, indicating the hide animation of the soft keyboard in the fixed state is completed. |
| callback | Callback<[KeyboardInfo](../interfaces-others/document.md#keyboardinfo18)\> | No | Callback used to return the information about the soft keyboard. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function keyboardDidHide can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const callback = (keyboardInfo: window.KeyboardInfo) => {
  // ...
}
try {
  windowClass.on('keyboardDidHide', callback);
  windowClass.off('keyboardDidHide', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('keyboardDidHide');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('touchOutside')11+

on(type: 'touchOutside', callback: Callback<void>): void

Subscribes to the touch event outside this window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'touchOutside'**, indicating the touch event outside this window. |
| callback | Callback<void> | Yes | Callback used to return the touch event outside this window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

try {
  windowClass.on('touchOutside', () => {
    console.info('touch outside');
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('touchOutside')11+

off(type: 'touchOutside', callback?: Callback<void>): void

Unsubscribes from the touch event outside this window.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'touchOutside'**, indicating the touch event outside this window. |
| callback | Callback<void> | No | Callback used to return the touch event outside this window. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

const callback = () => {
  // ...
}
try {
  windowClass.on('touchOutside', callback);
  windowClass.off('touchOutside', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('touchOutside');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('screenshot')9+

on(type: 'screenshot', callback: Callback<void>): void

Subscribes to the screenshot event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'screenshot'**, covering screenshot events initiated from the Control Panel, by running hdc commands, or by calling the screenshot interfaces. |
| callback | Callback<void> | Yes | Callback invoked when a screenshot event occurs. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

try {
  windowClass.on('screenshot', () => {
    console.info('screenshot happened');
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('screenshot')9+

off(type: 'screenshot', callback?: Callback<void>): void

Unsubscribes from the screenshot event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'screenshot'**, indicating the screenshot event. |
| callback | Callback<void> | No | Callback invoked when a screenshot event occurs. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

let callback = () => {
  console.info('screenshot happened');
};
try {
  windowClass.on('screenshot', callback);
  windowClass.off('screenshot', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('screenshot');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('screenshotAppEvent')20+

on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void

Subscribes to the screenshot event.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'screenshotAppEvent'**, covering screenshot events from the Control Panel, shortcut keys, and scroll capture. |
| callback | Callback<[ScreenshotEventType](../enums/document.md#screenshoteventtype20)\> | Yes | Callback invoked when a screenshot event occurs. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (eventType: window.ScreenshotEventType) => {
  console.info(\`screenshotAppEvent happened. Event: ${eventType}\`);
}
try {
  windowClass.on('screenshotAppEvent', callback);
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('screenshotAppEvent')20+

off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void

Unsubscribes from the screenshot event.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'screenshotAppEvent'**, indicating the screenshot event. |
| callback | Callback<[ScreenshotEventType](../enums/document.md#screenshoteventtype20)\> | No | Callback invoked when a screenshot event occurs. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (eventType: window.ScreenshotEventType) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('screenshotAppEvent', callback);
  // Disable the listening of a specified callback.
  windowClass.off('screenshotAppEvent', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('screenshotAppEvent');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('dialogTargetTouch')10+

on(type: 'dialogTargetTouch', callback: Callback<void>): void

Subscribes to click or touch events in a window covered by a modal window. This API takes effect only when it is called by a modal window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'dialogTargetTouch'**, indicating the click or touch event in a window covered by a modal window. |
| callback | Callback<void> | Yes | Callback invoked when a click or touch event occurs in the window covered by the modal window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

try {
  windowClass.on('dialogTargetTouch', () => {
    console.info('touch dialog target');
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('dialogTargetTouch')10+

off(type: 'dialogTargetTouch', callback?: Callback<void>): void

Unsubscribes from the touch event of the target window in the modal window mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'dialogTargetTouch'**, indicating the touch event of the target window in the modal window mode. |
| callback | Callback<void> | No | Callback invoked when the touch event occurs in the target window of the modal window mode. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

const callback = () => {
  // ...
}
try {
  windowClass.on('dialogTargetTouch', callback);
  windowClass.off('dialogTargetTouch', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('dialogTargetTouch');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('windowEvent')10+

on(type: 'windowEvent', callback: Callback<WindowEventType>): void

Subscribes to the window lifecycle change event.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowEvent'**, indicating the window lifecycle change event. |
| callback | Callback<[WindowEventType](../enums/document.md#windoweventtype10)\> | Yes | Callback used to return the window lifecycle state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

try {
  windowClass.on('windowEvent', (data) => {
    console.info('Window event happened. Event:' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowEvent')10+

off(type: 'windowEvent', callback?: Callback<WindowEventType>): void

Unsubscribes from the window lifecycle change event.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowEvent'**, indicating the window lifecycle change event. |
| callback | Callback<[WindowEventType](../enums/document.md#windoweventtype10)\> | No | Callback used to return the window lifecycle state. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

const callback = (windowEventType: window.WindowEventType) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('windowEvent', callback);
  // Disable the listening of a specified callback.
  windowClass.off('windowEvent', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('windowEvent');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('displayIdChange')14+

on(type: 'displayIdChange', callback: Callback<number>): void

Subscribes to the display change event of this window. For example, this event is triggered when the window is moved to a different display.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'displayIdChange'**, indicating the display change event. |
| callback | Callback<number> | Yes | Callback invoked when the display where the window is located changes. The callback contains a parameter of the number type, indicating the new display ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  windowClass.on('displayIdChange', (data) => {
    console.info('Window displayId changed, displayId=' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('displayIdChange')14+

off(type: 'displayIdChange', callback?: Callback<number>): void

Unsubscribes from the display change event of this window.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'displayIdChange'**, indicating the display change event. |
| callback | Callback<number> | No | Callback invoked when the display where the window is located changes. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

const callback = (displayId: number) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('displayIdChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('displayIdChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('displayIdChange');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('windowVisibilityChange')11+

on(type: 'windowVisibilityChange', callback: Callback<boolean>): void

Subscribes to the visibility status change event of this window. The visibility returned by this API may be different from that perceived by human eyes in the following scenarios:

-   If the shadow area of a non-main window is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. ([setWindowShadowEnabled](#setwindowshadowenabled20) and [setWindowShadowRadius](#setwindowshadowradius17) can be used to set whether to display the shadow area and the shadow radius,respectively.)
-   If the upper-layer window has a transparency effect (any degree of transparency other than fully opaque), the lower-layer window will not be blocked and is visible.
-   Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowVisibilityChange'**, indicating the visibility status change event. |
| callback | Callback<boolean> | Yes | Callback used to return the visibility status of the window, which is a Boolean value. **true** if visible, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  windowClass.on('windowVisibilityChange', (boolean) => {
    console.info('Window visibility changed, isVisible=' + boolean);
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowVisibilityChange')11+

off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void

Unsubscribes from the visibility status change event of this window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowVisibilityChange'**, indicating the visibility status change event. |
| callback | Callback<boolean> | No | Callback used to return the visibility status of the window. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (bool: boolean) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('windowVisibilityChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('windowVisibilityChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('windowVisibilityChange');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('occlusionStateChanged')22+

on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void

Subscribes to the visibility status change event of the window. The visibility returned by this API may be different from that perceived by human eyes in the following scenarios:

-   If the shadow area of a non-main window is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. ([setWindowShadowEnabled](#setwindowshadowenabled20) and [setWindowShadowRadius](#setwindowshadowradius17) can be used to set whether to display the shadow area and the shadow radius,respectively.)
-   If the upper-layer window has a transparency effect (any degree of transparency other than fully opaque), the lower-layer window will not be blocked and is visible.
-   Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'occlusionStateChanged'**, indicating the window visibility status change event. |
| callback | Callback<[OcclusionState](../enums/document.md#occlusionstate22)\> | Yes | Callback invoked when the window visibility status changes. For details, see [Window Visibility Status](../enums/document.md#occlusionstate22). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  let callback: Callback<window.OcclusionState> = (data: window.OcclusionState) => {
    console.info(\`Window occlusion state changed: ${data}\`);
  };
  windowClass.on('occlusionStateChanged', callback);
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('occlusionStateChanged')22+

off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void

Unsubscribes from the visibility status change event of the window.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'occlusionStateChanged'**, indicating the window visibility status change event. |
| callback | Callback<[OcclusionState](../enums/document.md#occlusionstate22)\> | No | If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  let callback: Callback<window.OcclusionState> = (data: window.OcclusionState) => {
    console.info(\`Window occlusion state changed: ${data}\`);
  };
  // Enable listening through the on API.
  windowClass.on('occlusionStateChanged', callback);
  // Disable the listening of a specified callback.
  windowClass.off('occlusionStateChanged', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('occlusionStateChanged');
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('frameMetricsMeasured')22+

on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void

Subscribes to events indicating changes in window frame metrics. This API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

The callback is triggered only when the client UI content is redrawn (for example, during page transitions, interactions with responsive components, setting background colors, or adjusting opacity).

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameMetricsMeasured'**, indicating the window frame metrics change event. |
| callback | Callback<[FrameMetrics](../interfaces-others/document.md#framemetrics22)\> | Yes | Callback invoked when the window frame metrics change. For details, see [Frame Rate Metrics](../interfaces-others/document.md#framemetrics22). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let callback: Callback<window.FrameMetrics> = (data: window.FrameMetrics) => {
    console.info(\`Window frame metrics changed: ${JSON.stringify(data)}\`);
  };
  windowClass.on('frameMetricsMeasured', callback);
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('frameMetricsMeasured')22+

off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void

Unsubscribes from events indicating changes in window frame metrics. This API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'frameMetricsMeasured'**, indicating the window frame metrics change event. |
| callback | Callback<[FrameMetrics](../interfaces-others/document.md#framemetrics22)\> | No | If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let callback: Callback<window.FrameMetrics> = (data: window.FrameMetrics) => {
    console.info(\`Window frame metrics changed: ${JSON.stringify(data)}\`);
  };
  // Enable listening through the on API.
  windowClass.on('frameMetricsMeasured', callback);
  // Disable the listening of a specified callback.
  windowClass.off('frameMetricsMeasured', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('frameMetricsMeasured');
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('systemDensityChange')15+

on(type: 'systemDensityChange', callback: Callback<number>): void

Subscribes to the system density change event, which is triggered when the system's display size scale factor changes for the screen where the window is located.

In the callback function, you are advised to directly use the return value to convert from virtual pixels (vp) to physical pixels (px). For example, if the return value is **density**, the calculation formula is vp × density = px.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'systemDensityChange'**, indicating the system density change event. |
| callback | Callback<number> | Yes | Callback invoked when the system's display size scale factor changes. The callback contains a parameter of the number type, indicating the new scale factor. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

const callback = (density: number) => {
  console.info('System density changed, density=' + JSON.stringify(density));
  // Calculate px using the return value.
  let vp = 100;
  let px = vp \* density;
}
try {
  windowClass.on('systemDensityChange', callback);
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('systemDensityChange')15+

off(type: 'systemDensityChange', callback?: Callback<number>): void

Unsubscribes from the system density change event.

In the callback function, you are advised to directly use the return value to convert from virtual pixels (vp) to physical pixels (px). For example, if the return value is **density**, the calculation formula is vp × density = px.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'systemDensityChange'**, indicating the system density change event. |
| callback | Callback<number> | No | Callback invoked when the system's display size scale factor changes. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

const callback = (density: number) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('systemDensityChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('systemDensityChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('systemDensityChange');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('noInteractionDetected')12+

on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void

Subscribes to non-interaction events in a window within the specified period. Interaction events include physical keyboard input events and screen touch/click events, but not soft keyboard input events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'noInteractionDetected'**, indicating that there is no interaction event in the window within the specified period. |
| timeout | number | Yes | Period during which no interaction is performed, in seconds. The value must be an integer. Negative numbers and decimals are invalid. |
| callback | Callback<void> | Yes | Callback invoked when there is no interaction event in the current window within the specified period. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  windowClass.on('noInteractionDetected', 60, () => {
    console.info('no interaction in 60s');
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('noInteractionDetected')12+

off(type: 'noInteractionDetected', callback?: Callback<void>): void

Unsubscribes from non-interaction events in a window within the specified period. Interaction events include physical keyboard input events and screen touch/click events, but not soft keyboard input events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'noInteractionDetected'**, indicating that there is no interaction event in the window within the specified period. |
| callback | Callback<void> | No | Callback invoked when there is no interaction event in the current window within the specified period. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = () => {
  // ...
}
try {
  windowClass.on('noInteractionDetected', 60, callback);
  windowClass.off('noInteractionDetected', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('noInteractionDetected');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('windowStatusChange')11+

on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void

Enables the listening for window status changes. When the window status changes, a notification is sent. (In this case, the window attributes may not be updated yet. If you need to obtain the changed window size and position immediately after receiving the window status change notification, you are advised to use [on('windowStatusDidChange')](#onwindowstatusdidchange20).)

After the listening is enabled using this API, multiple callbacks will be received when the **maximize** or **recover** method is called. To obtain the deduplicated callback, you can use [on('windowStatusDidChange')](#onwindowstatusdidchange20).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/mXbXJox0Tb2-XQymrDdRPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77C2119C8B096976AFF0CD599F84AE911EA209C8ABECCB2EEC5037E2FD70EA31)

In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, when the window is maximized (covering the entire screen, with a dock bar and status bar on 2-in-1 devices, and a status bar on tablets), the return value differs based on the [targetAPIVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) setting. For versions below 14, the return value is **WindowStatusType::FULL\_SCREEN**. For versions 14 and above, the return value is **WindowStatusType::MAXIMIZE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowStatusChange'**, indicating the window status change event. |
| callback | Callback<[WindowStatusType](../enums/document.md#windowstatustype11)\> | Yes | Callback used to return the window status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

try {
    windowClass.on('windowStatusChange', (WindowStatusType) => {
        console.info('Succeeded in enabling the listener for window status changes. Data: ' + JSON.stringify(WindowStatusType));
    });
} catch (exception) {
    console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowStatusChange')11+

off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void

Unsubscribes from the window status change event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowStatusChange'**, indicating the window status change event. |
| callback | Callback<[WindowStatusType](../enums/document.md#windowstatustype11)\> | No | Callback used to return the window status. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

const callback = (windowStatusType: window.WindowStatusType) => {
    // ...
}
try {
    windowClass.on('windowStatusChange', callback);
    windowClass.off('windowStatusChange', callback);
    // Unregister all the callbacks that have been registered through on().
    windowClass.off('windowStatusChange');
} catch (exception) {
    console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('windowStatusDidChange')20+

on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void

Subscribes to the event indicating that the window status has changed (the [Rect](../interfaces-others/document.md#rect7) property of the window has been updated).

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowStatusDidChange'**, indicating that the window status has changed. |
| callback | Callback<[WindowStatusType](../enums/document.md#windowstatustype11)\> | Yes | Callback used to return the window status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
    windowClass.on('windowStatusDidChange', (WindowStatusType) => {
        console.info(\`Succeeded in enabling the listener for window status changes. Data: ${JSON.stringify(WindowStatusType)}\`);
    });
} catch (exception) {
    console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowStatusDidChange')20+

off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void

Unsubscribes from the window status change event.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowStatusDidChange'**, indicating that the window status has changed. |
| callback | Callback<[WindowStatusType](../enums/document.md#windowstatustype11)\> | No | Callback used to return the window status. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

const callback = (windowStatusType: window.WindowStatusType) => {
    // ...
}
try {
    windowClass.on('windowStatusDidChange', callback);
    windowClass.off('windowStatusDidChange', callback);
    // Unregister all the callbacks that have been registered through on().
    windowClass.off('windowStatusDidChange');
} catch (exception) {
    console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowGrayScale12+

setWindowGrayScale(grayScale: number): Promise<void>

Sets the grayscale effect for this window. This API uses a promise to return the result. This API can be called only after [loadContent()](#loadcontent9) or [setUIContent()](#setuicontent9) is called.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| grayScale | number | Yes | Grayscale of the window. The value is a floating-point number in the range \[0.0, 1.0\]. The value **0.0** means that the window image does not change, and **1.0** means that the window image is completely turned into grayscale. The effect changes linearly between 0.0 and 1.0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass?.setUIContent('pages/Index', (error: BusinessError) => {
  if (error.code) {
    console.error(\`Failed to set the content. Cause code: ${error.code}\`);
    return;
  }
  console.info('Succeeded in setting the content.');
  let grayScale: number = 0.5;
  try {
    if (canIUse("SystemCapability.Window.SessionManager")) {
      let promise = windowClass?.setWindowGrayScale(grayScale);
      promise?.then(() => {
        console.info('Succeeded in setting the grayScale.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the grayScale. Cause code: ${err.code}, message: ${err.message}\`);
      });
    }
  } catch (exception) {
    console.error(\`Failed to set the grayScale. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
});

#### on('windowTitleButtonRectChange')11+

on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void

Subscribes to the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window. This API takes effect for the window that has a title bar or a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowTitleButtonRectChange'**, indicating that the change event of the rectangle that holds the minimize, maximize, and close buttons. |
| callback | Callback<[TitleButtonRect](../interfaces-others/document.md#titlebuttonrect11)\> | Yes | Callback used to return the new rectangle. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

windowClass.setUIContent('pages/WindowPage').then(() => {
  try {
    windowClass?.on('windowTitleButtonRectChange', (titleButtonRect) => {
      console.info('Succeeded in enabling the listener for window title buttons area changes. Data: ' + JSON.stringify(titleButtonRect));
    });
  } catch (exception) {
    console.error(\`Failed to enable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
})

#### off('windowTitleButtonRectChange')11+

off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void

Unsubscribes from the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window. This API takes effect for the window that has a title bar or a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowTitleButtonRectChange'**, indicating that the change event of the rectangle that holds the minimize, maximize, and close buttons. |
| callback | Callback<[TitleButtonRect](../interfaces-others/document.md#titlebuttonrect11)\> | No | Callback used to return the new rectangle. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

windowClass.setUIContent('pages/WindowPage').then(() => {
    const callback = (titleButtonRect: window.TitleButtonRect) => {
        // ...
    }
  try {
    // Enable listening through the on API.
    windowClass?.on('windowTitleButtonRectChange', callback);
    // Disable the listening of a specified callback.
    windowClass?.off('windowTitleButtonRectChange', callback);
    // Unregister all the callbacks that have been registered through on().
    windowClass?.off('windowTitleButtonRectChange');
  } catch (exception) {
    console.error(\`Failed to disable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
})

#### on('windowRectChange')12+

on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void

Subscribes to window rectangle (position and size) change events.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowRectChange'**, indicating the window rectangle change event. |
| callback | Callback<[RectChangeOptions](../interfaces-others/document.md#rectchangeoptions12)\> | Yes | Callback used to return the value and reason of the window rectangle change. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  windowClass.on('windowRectChange', (data: window.RectChangeOptions) => {
      console.info(\`Succeeded in enabling the listener for window rect changes. Data: ${JSON.stringify(data)}\`);
  });
} catch (exception) {
  console.error(\`Failed to disable the listener for window rect changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowRectChange')12+

off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void

Unsubscribes from window rectangle (position and size) change events.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowRectChange'**, indicating the window rectangle change event. |
| callback | Callback<[RectChangeOptions](../interfaces-others/document.md#rectchangeoptions12)\> | No | Callback used to return the value and reason of the window rectangle change. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (rectChangeOptions: window.RectChangeOptions) => {
  // ...
}

try {
  windowClass.on('windowRectChange', callback);
  windowClass.off('windowRectChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('windowRectChange');
} catch (exception) {
  console.error(\`Failed to disable the listener for window rect changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('rectChangeInGlobalDisplay')20+

on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void

Enables the listening event for changes in the window rectangle (window position and size) in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'rectChangeInGlobalDisplay'**, indicating the window rectangle change event in the global coordinate system. |
| callback | Callback<[RectChangeOptions](../interfaces-others/document.md#rectchangeoptions12)\> | Yes | Callback used to return the value and reason of the window rectangle change. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (rectChangeOptions: window.RectChangeOptions) => {
  console.info(\`Succeeded in enabling the listener for window rect changes in global display. Data: \` + JSON.stringify(rectChangeOptions));
}

try {
  windowClass.on('rectChangeInGlobalDisplay', callback);
} catch (exception) {
  console.error(\`Failed to enable the listener for window rect changes in global display. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('rectChangeInGlobalDisplay')20+

off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void

Disables the listening event for changes in the window rectangle (window position and size) in the [global coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#global-coordinate-system).

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'rectChangeInGlobalDisplay'**, indicating the window rectangle change event in the global coordinate system. |
| callback | Callback<[RectChangeOptions](../interfaces-others/document.md#rectchangeoptions12)\> | No | Callback used to return the value and reason of the window rectangle change. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (rectChangeOptions: window.RectChangeOptions) => {
  // ...
}

try {
  windowClass.on('rectChangeInGlobalDisplay', callback);
  windowClass.off('rectChangeInGlobalDisplay', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('rectChangeInGlobalDisplay');
} catch (exception) {
  console.error(\`Failed to disable the listener for window rect changes in global display. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('subWindowClose')12+

on(type: 'subWindowClose', callback: Callback<void>): void

Subscribes to the event indicating that the child window is closed. This event is triggered only when the user clicks the system-provided close button in the top-right corner to close the child window. It is not triggered when the child window is closed in other ways.

If the event is subscribed to multiple times, only the most recently subscribed-to event takes effect.

The callback function in this API is executed synchronously. For asynchronous close events of child windows, refer to [on('windowWillClose')](#onwindowwillclose15).

If there is an existing event subscribed to by calling [on('windowWillClose')](#onwindowwillclose15), only the [on('windowWillClose')](#onwindowwillclose15) API will be responded to.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'subWindowClose'**, indicating the child window close event. |
| callback | Callback<void> | Yes | Callback invoked when the close button in the top-right corner of the child window is clicked. It does not return any parameter. The return value of the internal logic of the callback function determines whether to continue to close the child window. If **true** of the Boolean type is returned, the child window is not closed. If **false** or other non-Boolean types are returned, the child window is closed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

const callback = () => {
  // ...
  return true;
}
try {
  windowClass.on('subWindowClose', callback);
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('subWindowClose')12+

off(type: 'subWindowClose', callback?: Callback<void>): void

Unsubscribes from the event indicating that the child window is closed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'subWindowClose'**, indicating the child window close event. |
| callback | Callback<void> | No | Callback invoked when the close button in the top-right corner of the child window is clicked. It does not return any parameter. The return value of the internal logic of the callback function determines whether to continue to close the child window. If **true** of the Boolean type is returned, the child window is not closed. If **false** or other non-Boolean types are returned, the child window is closed. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

const callback = () => {
  // ...
  return true;
}
try {
  windowClass.on('subWindowClose', callback);
  windowClass.off('subWindowClose', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('subWindowClose');
} catch (exception) {
  console.error(\`Failed to register or unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('windowWillClose')15+

on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void

Subscribes to the event indicating that the main window or child window will be closed. This event is triggered only when the user clicks the close button in the system-provided title bar to close the window. It is not triggered when the window is closed in other ways.

The callback function in this API is executed asynchronously. For synchronous close events of child windows, refer to [on('subWindowClose')](#onsubwindowclose12). For synchronous close events of the main window, refer to [on('windowStageClose')](../interface-windowstage/document.md#onwindowstageclose14).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowWillClose'**, indicating the window close event. |
| callback | Callback<void, Promise<boolean>> | Yes | Callback invoked when the close button in the top-right corner of the window is clicked. It does not return any parameter. The internal logic of the callback function requires a return value of the Promise<boolean> type. In the returned Promise function, **resolve(true)** means not to close the window, and **resolve(false)** or **reject** means to continue to close the window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    const callback = () => {
      // ...
      return new Promise<boolean>((resolve, reject) => {
        // Whether to close the window.
        let result: boolean = true;
        resolve(result);
      });
    }
    try {
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowWillClose', callback);
    } catch (exception) {
      console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### off('windowWillClose')15+

off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void

Unsubscribes from the event indicating that the main window or child window will be closed.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowWillClose'**, indicating the window close event. |
| callback | Callback<void, Promise<boolean>> | No | Callback invoked when the close button in the top-right corner of the window is clicked. It does not return any parameter. The internal logic of the callback function requires a return value of the Promise<boolean> type. In the returned Promise function, **resolve(true)** means not to close the window, and **resolve(false)** or **reject** means to continue to close the window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      const callback = () => {
        // ...
        return new Promise<boolean>((resolve, reject) => {
          // Whether to close the window.
          let result: boolean = true;
          resolve(result);
        });
      }
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowWillClose', callback);
      windowClass.off('windowWillClose', callback);
      // Unregister all the callbacks that have been registered through on().
      windowClass.off('windowWillClose');
    } catch (exception) {
      console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### on('windowHighlightChange')15+

on(type: 'windowHighlightChange', callback: Callback<boolean>): void

Subscribes to the highlighted state change event of the window.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowHighlightChange'**, indicating the window highlighted state change event. |
| callback | Callback<boolean> | Yes | Callback used to return the highlighted state of the window. which is a Boolean value. **true** if highlighted, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  windowClass.on('windowHighlightChange', (data: boolean) => {
    console.info(\`Window highlight Change: ${data}\`);
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('windowHighlightChange')15+

off(type: 'windowHighlightChange', callback?: Callback<boolean>): void

Unsubscribes from the highlighted state change event of the window.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowHighlightChange'**, indicating the window highlighted state change event. |
| callback | Callback<boolean> | No | Callback used to return the highlighted state of the window. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (data: boolean) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('windowHighlightChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('windowHighlightChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('windowHighlightChange');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('rotationChange')19+

on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void

Subscribes to the window rotation change event. If the window rotation event type in [RotationChangeInfo](../interfaces-others/document.md#rotationchangeinfo19) is **WINDOW\_WILL\_ROTATE**, [RotationChangeResult](../interfaces-others/document.md#rotationchangeresult19) must be returned. If the window rotation event type is **WINDOW\_DID\_ROTATE**, [RotationChangeResult](../interfaces-others/document.md#rotationchangeresult19) does not take effect.

This API can be registered only on the main thread. If a window registers multiple callbacks of the same type, only the return value of the most recently registered callback will be effective. The system provides a timeout protection mechanism. If the window does not return [RotationChangeResult](../interfaces-others/document.md#rotationchangeresult19) within 20 ms, the system does not process the return value.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: Calling this API on 2-in-1 devices will return error code 801. For other devices: (1) This API can be called and takes effect immediately on devices that support sensor rotation and is not in [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state regardless of whether they support freeform windows. (2) This API can be called on devices that support sensor rotation and are in the free window state, but the call does not take effect or report an error. It takes effect only when the device is switched to a state other than the free window state. In other cases, the call does not take effect or report an error.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'rotationChange'**, indicating the window rotation change event. |
| callback | RotationChangeCallback<[RotationChangeInfo](../interfaces-others/document.md#rotationchangeinfo19), [RotationChangeResult](../interfaces-others/document.md#rotationchangeresult19) | void> | Yes | Callback used to return [RotationChangeInfo](../interfaces-others/document.md#rotationchangeinfo19) and [RotationChangeResult](../interfaces-others/document.md#rotationchangeresult19). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

function calculateRect(info: window.RotationChangeInfo): window.Rect {
  // calculate result with info
  let rect: window.Rect = {
    left: 0,
    top: 0,
    width: 500,
    height: 600,
  };
  return rect;
}

function callback(info: window.RotationChangeInfo): window.RotationChangeResult | void {
  let result: window.RotationChangeResult = {
    rectType: window.RectType.RELATIVE\_TO\_SCREEN,
    windowRect: {
      left: 0,
      top: 0,
      width: 0,
      height: 0,
    }
  };

  if (info.type === window.RotationChangeType.WINDOW\_WILL\_ROTATE) {
    result.rectType = window.RectType.RELATIVE\_TO\_SCREEN;
    result.windowRect = calculateRect(info);
    return result;
  } else {
    // do something after rotate
    return;
  }
}

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: 'test',
      windowType: window.WindowType.TYPE\_DIALOG,
      ctx: this.context
    };

    try {
      window.createWindow(config, (err: BusinessError, data: window.Window) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to create the window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        try {
          windowClass.on('rotationChange', callback);
        } catch (exception) {
          console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
        }
        windowClass.resize(500, 1000);
      });
    } catch (exception) {
      console.error(\`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### off('rotationChange')19+

off(type: 'rotationChange', callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void

Unsubscribes from the window rotation change event.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: Calling this API on 2-in-1 devices will return error code 801. For other devices: (1) This API can be called and takes effect immediately on devices that support sensor rotation and is not in [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state regardless of whether they support freeform windows. (2) This API can be called on devices that support sensor rotation and are in the free window state, but the call does not take effect or report an error. It takes effect only when the device is switched to a state other than the free window state. In other cases, the call does not take effect or report an error.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'rotationChange'**, indicating the window rotation change event. |
| callback | RotationChangeCallback<[RotationChangeInfo](../interfaces-others/document.md#rotationchangeinfo19), [RotationChangeResult](../interfaces-others/document.md#rotationchangeresult19) | void> | No | Callback used to return the result. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (info: window.RotationChangeInfo): window.RotationChangeResult | void => {
  // ...
  return;
}
try {
  windowClass.off('rotationChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('rotationChange');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### on('uiExtensionSecureLimitChange')20+

on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void

Subscribes to the event indicating changes in the security restrictions of the UIExtensionAbility within the window. You are advised to initiate the subscription right after the window is created.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventType | string | Yes | Event type. The value is fixed at **'uiExtensionSecureLimitChange'**, indicating that the UIExtensionAbility security restrictions in the window changes. |
| callback | Callback<boolean> | Yes | Callback used to return the result. The value **true** means that at least one UIExtensionAbility within the window has enabled the hiding of unsafe windows, and **false** means that all UIExtensionAbility components within the window have disabled the hiding of unsafe windows. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.Function on('uiExtensionSecureLimitChange') can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  windowClass.on('uiExtensionSecureLimitChange', (data: boolean) => {
    console.info(\`Window secure limit Change: ${data}\`);
  });
} catch (exception) {
  console.error(\`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('uiExtensionSecureLimitChange')20+

off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void

Unsubscribes from the event indicating changes in the security restrictions of the UIExtensionAbility within the window.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventType | string | Yes | Event type. The value is fixed at **'uiExtensionSecureLimitChange'**, indicating that the UIExtensionAbility security restrictions in the window changes. |
| callback | Callback<boolean> | No | Callback used to return the result. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.Function off('uiExtensionSecureLimitChange') can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (data: boolean) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('uiExtensionSecureLimitChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('uiExtensionSecureLimitChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('uiExtensionSecureLimitChange');
} catch (exception) {
  console.error(\`Failed to unregister callback. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### isWindowSupportWideGamut9+

isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void

Checks whether this window supports the wide-gamut color space. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if the wide-gamut color space is supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.isWindowSupportWideGamut((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in checking whether the window support WideGamut Data: ${data}\`);
});

#### isWindowSupportWideGamut9+

isWindowSupportWideGamut(): Promise<boolean>

Checks whether this window supports the wide-gamut color space. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if the wide-gamut color space is supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.isWindowSupportWideGamut();
promise.then((data) => {
  console.info(\`Succeeded in checking whether the window support WideGamut. Data: ${data}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setWindowColorSpace9+

setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void

Sets a color space for this window. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [ColorSpace](../enums/document.md#colorspace8) | Yes | Color space to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.setWindowColorSpace(window.ColorSpace.WIDE\_GAMUT, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting window colorspace.');
  });
} catch (exception) {
  console.error(\`Failed to set window colorspace. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowColorSpace9+

setWindowColorSpace(colorSpace:ColorSpace): Promise<void>

Sets a color space for this window. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [ColorSpace](../enums/document.md#colorspace8) | Yes | Color space to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.setWindowColorSpace(window.ColorSpace.WIDE\_GAMUT);
  promise.then(() => {
    console.info('Succeeded in setting window colorspace.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set window colorspace. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowColorSpace9+

getWindowColorSpace(): ColorSpace

Obtains the color space of this window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorSpace](../enums/document.md#colorspace8) | Color space obtained. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let colorSpace = windowClass.getWindowColorSpace();
  console.info(\`Succeeded in getting the window color space. ColorSpace: ${colorSpace}\`);
} catch (exception) {
  console.error(\`Failed to get the window color space. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowBackgroundColor9+

setWindowBackgroundColor(color: string | ColorMetrics): void

Sets the background color for this window.

If this API is not called, the default background color of the window is **'#FFF0F0F0'** in light mode and **'#FF1A1A1A'** in dark mode.

In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | string | [ColorMetrics](../../../ui/arkui/graphics/document.md#colormetrics12)18+ | Yes | 
Background color to set. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**.

Starting from API version 18, this parameter supports the ColorMetrics type.

 |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics } from '@kit.ArkUI';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in loading the content.');
  let color1: string = '#00FF33';
  let color2: ColorMetrics = ColorMetrics.numeric(0xff112233);
  try {
    windowClass?.setWindowBackgroundColor(color1);
    windowClass?.setWindowBackgroundColor(color2);
  } catch (exception) {
    console.error(\`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}\`);
  };
});

#### setWindowShadowEnabled20+

setWindowShadowEnabled(enable: boolean): Promise<void>

Sets whether the main window displays a shadow. This API uses a promise to return the result. By default, the main window displays a shadow unless you explicitly change it with this API.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

**Required permissions**: ohos.permission.SET\_WINDOW\_TRANSPARENT

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether the main window displays a shadow. **true** if the main window displays a shadow, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info('Succeeded in loading the content.');
      // Obtain the main window.
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        let enable = true;
        let promise = windowClass.setWindowShadowEnabled(enable);
        promise.then(() => {
          console.info('Succeeded in setting window shadow.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the window shadow. Cause code: ${err.code}, message: ${err.message}\`);
        });
      });
    });
  }
}

#### setWindowBrightness9+

setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void

Sets the window brightness for the main window. The window brightness takes effect only when the window is in the foreground and has focus. This API uses an asynchronous callback to return the result.

When the setting is valid, it affects only the physical screen where the window is displayed. It does not apply to virtual displays (for example, casting/mirroring screens).

If the input parameter is **\-1**, the window brightness reverts to the system brightness (which can be adjusted through Control Panel or shortcut keys).

When the window moves to the background, the setting becomes invalid, and brightness can be adjusted through Control Panel or shortcut keys. You are advised not to call this API consecutively or when the window is moved to the background. Otherwise, timing issues may occur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/brwaKKVJSIuzJcN6kvE8YQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CCDB9D31D1DCE96098D20C98E0BB837976DD473C0C0EC05B025F0962FD07300)

-   For non-2-in-1 devices: When the window's brightness setting is active, adjusting the system screen brightness from the control center does not take effect.
-   For 2-in-1 devices:
    -   Before HarmonyOS 5.0.2, if a window has custom brightness, system brightness controls (Control Panel or shortcut keys) are disabled.
    -   Starting from HarmonyOS 5.0.2, window brightness is always synchronized with system brightness. Brightness can be adjusted through this API, Control Panel, or shortcut keys.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | number | Yes | Brightness to set. The value is a floating-point number in the range \[0.0, 1.0\] or is set to **\-1.0**. The value **1.0** means the brightest, and **\-1.0** means that the window brightness resets to the original brightness set through Control Panel. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
      if (loadError.code) {
        console.error(\`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}\`);
        return;
      }
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        let brightness: number = 1.0;
        try {
          windowClass.setWindowBrightness(brightness, (err: BusinessError) => {
            const errCode: number = err.code;
            if (errCode) {
              console.error(\`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}\`);
              return;
            }
            console.info('Succeeded in setting the brightness.');
          });
        } catch (exception) {
          console.error(\`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}\`);
        }
      });
    });
  }
}

#### setWindowBrightness9+

setWindowBrightness(brightness: number): Promise<void>

Sets the window brightness for the main window. The window brightness takes effect only when the window is in the foreground and has focus. This API uses a promise to return the result.

When the setting is valid, it affects only the physical screen where the window is displayed. It does not apply to virtual displays (for example, casting/mirroring screens).

If the input parameter is **\-1**, the window brightness reverts to the system brightness (which can be adjusted through Control Panel or shortcut keys).

When the window moves to the background, the setting becomes invalid, and brightness can be adjusted through Control Panel or shortcut keys. You are advised not to call this API consecutively or when the window is moved to the background. Otherwise, timing issues may occur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/4Mr8CbA5TxCY6TRDPJpCUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C710E417B50E4B9CC260E18A8BF7DC986E5B581AF6C1D18C4B02796178E333D)

-   For non-2-in-1 devices: When the window's brightness setting is active, adjusting the system screen brightness from the control center does not take effect.
-   For 2-in-1 devices:
    -   Before HarmonyOS 5.0.2, if a window has custom brightness, system brightness controls (Control Panel or shortcut keys) are disabled.
    -   Starting from HarmonyOS 5.0.2, window brightness is always synchronized with system brightness. Brightness can be adjusted through this API, Control Panel, or shortcut keys.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | number | Yes | Brightness to set. The value is a floating-point number in the range \[0.0, 1.0\] or is set to **\-1.0**. The value **1.0** means the brightest, and **\-1.0** means that the window brightness resets to the original brightness set through Control Panel. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
      if (loadError.code) {
        console.error(\`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}\`);
        return;
      }
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        let brightness: number = 1.0;
        try {
          let promise = windowClass.setWindowBrightness(brightness);
          promise.then(() => {
            console.info('Succeeded in setting the brightness.');
          }).catch((err: BusinessError) => {
            console.error(\`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}\`);
          });
        } catch (exception) {
          console.error(\`Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}\`);
        }
      });
    });
  }
}

#### setWindowFocusable9+

setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void

Sets whether this window is focusable. This API uses an asynchronous callback to return the result.

Starting from API version 22, if a virtual screen is created by calling [createVirtualScreen](../../../display-management/ohos-display-display/document.md#displaycreatevirtualscreen16) with **supportsFocus** set to **false**, windows on this virtual screen cannot call the current API to change their focusability. Attempting to do so will result in error code 1300002.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFocusable | boolean | Yes | Whether the window is focusable. **true** if focusable, **false** otherwise. If this parameter is set to **false**, the window cannot bind to an input method or receive keyboard events. If input logic needs to be processed, follow the instructions provided in [Input Box and Input Method Interaction in Non-Focus Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
try {
  windowClass.setWindowFocusable(isFocusable, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting the window to be focusable.');
  });
} catch (exception) {
  console.error(\`Failed to set the window to be focusable. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowFocusable9+

setWindowFocusable(isFocusable: boolean): Promise<void>

Sets whether this window is focusable. This API uses a promise to return the result.

Starting from API version 22, if a virtual screen is created by calling [createVirtualScreen](../../../display-management/ohos-display-display/document.md#displaycreatevirtualscreen16) with **supportsFocus** set to **false**, windows on this virtual screen cannot call the current API to change their focusability. Attempting to do so will result in error code 1300002.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFocusable | boolean | Yes | Whether the window is focusable. **true** if focusable, **false** otherwise. If this parameter is set to **false**, the window cannot bind to an input method or receive keyboard events. If input logic needs to be processed, follow the instructions provided in [Input Box and Input Method Interaction in Non-Focus Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
try {
  let promise = windowClass.setWindowFocusable(isFocusable);
  promise.then(() => {
    console.info('Succeeded in setting the window to be focusable.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the window to be focusable. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowKeepScreenOn9+

setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void

Sets whether the screen of the current device remains on when the current window is in the foreground. This API does not take effect on heterogeneous virtual screens. This API uses an asynchronous callback to return the result.

Set **isKeepScreenOn** to **true** only in necessary scenarios (such as navigation, video playback, drawing, and gaming scenarios). After exiting these scenarios, set the parameter to **false**. Do not use this API in other scenarios (such as no screen interaction or audio playback). When the system detects that the API is used in a non-standard manner, automatic screen-off may be triggered.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isKeepScreenOn | boolean | Yes | Whether to keep the screen always on. **true** to keep the screen always on, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
try {
  windowClass.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting the screen to be always on.');
  });
} catch (exception) {
  console.error(\`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowKeepScreenOn9+

setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

Sets whether the screen of the current device remains on when the current window is in the foreground. This API does not take effect on heterogeneous virtual screens. This API uses a promise to return the result.

Set **isKeepScreenOn** to **true** only in necessary scenarios (such as navigation, video playback, drawing, and gaming scenarios). After exiting these scenarios, set the parameter to **false**. Do not use this API in other scenarios (such as no screen interaction or audio playback). When the system detects that the API is used in a non-standard manner, automatic screen-off may be triggered.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isKeepScreenOn | boolean | Yes | Whether to keep the screen always on. **true** to keep the screen always on, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
try {
  let promise = windowClass.setWindowKeepScreenOn(isKeepScreenOn);
  promise.then(() => {
    console.info('Succeeded in setting the screen to be always on.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowPrivacyMode9+

setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

Sets whether this window is in privacy mode. This API uses an asynchronous callback to return the result.

A window in privacy mode cannot be captured or recorded. This API can be used in scenarios where screen capture or recording is disabled.

If this API is not called, the privacy mode is disabled by default, and the window can be captured or recorded.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Required permissions**: ohos.permission.PRIVACY\_WINDOW

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacyMode | boolean | Yes | Whether the window is in privacy mode. **true** if the window is in privacy mode, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
try {
  windowClass.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting the window to privacy mode.');
  });
} catch (exception) {
  console.error(\`Failed to set the window to privacy mode. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowPrivacyMode9+

setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>

Sets whether this window is in privacy mode. This API uses a promise to return the result.

A window in privacy mode cannot be captured or recorded. This API can be used in scenarios where screen capture or recording is disabled.

If this API is not called, the privacy mode is disabled by default, and the window can be captured or recorded.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Required permissions**: ohos.permission.PRIVACY\_WINDOW

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacyMode | boolean | Yes | Whether the window is in privacy mode. **true** if the window is in privacy mode, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
try {
  let promise = windowClass.setWindowPrivacyMode(isPrivacyMode);
  promise.then(() => {
    console.info('Succeeded in setting the window to privacy mode.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the window to privacy mode. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowTouchable9+

setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void

Sets whether a window is touchable. This API uses an asynchronous callback to return the result.

When a window is touchable and a user taps it, a touch event is sent to the window. When a window is not touchable, the touch event is passed through to the lower-layer window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTouchable | boolean | Yes | Whether a window is touchable. **true** if touchable, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable = true;
try {
  windowClass.setWindowTouchable(isTouchable, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error(\`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in setting the window to be touchable.');
  });
} catch (exception) {
  console.error(\`Failed to set the window to be touchable. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowTouchable9+

setWindowTouchable(isTouchable: boolean): Promise<void>

Sets whether a window is touchable. This API uses an asynchronous promise to return the result.

When a window is touchable and a user taps it, a touch event is sent to the window. When a window is not touchable, the touch event is passed through to the lower-layer window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTouchable | boolean | Yes | Whether a window is touchable. **true** if touchable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable: boolean = true;
try {
  let promise = windowClass.setWindowTouchable(isTouchable);
  promise.then(() => {
    console.info('Succeeded in setting the window to be touchable.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the window to be touchable. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### snapshot9+

snapshot(callback: AsyncCallback<image.PixelMap>): void

Captures this window. This API uses an asynchronous callback to return the result. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setwindowprivacymode9)), taking a screenshot will result in a blank screen.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

windowClass.snapshot((err: BusinessError, pixelMap: image.PixelMap) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
  pixelMap.release(); // Release the memory in time after the PixelMap is used.
});

#### snapshot9+

snapshot(): Promise<image.PixelMap>

Captures this window. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setwindowprivacymode9)), taking a screenshot will result in a blank screen.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return the window screenshot. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let promise = windowClass.snapshot();
promise.then((pixelMap: image.PixelMap) => {
  console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
  pixelMap.release(); // Release the memory in time after the PixelMap is used.
}).catch((err: BusinessError) => {
  console.error(\`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### snapshotSync20+

snapshotSync(): image.PixelMap

Captures this window. This API returns the result synchronously. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setwindowprivacymode9)), taking a screenshot will result in a blank screen.

In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | return the window screenshot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300018 | Timeout. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

try {
  let pixelMap = windowClass.snapshotSync();
  console.info(\`Succeeded in snapshotting window\`);
  pixelMap.release(); // Release the memory in time after the PixelMap is used.
} catch (exception) {
  console.error(\`Failed to snapshot window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### snapshotIgnorePrivacy18+

snapshotIgnorePrivacy(): Promise<image.PixelMap>

Captures this window. This API can be called to obtain the screenshot of the current window even if the window's privacy mode is enabled (using [setWindowPrivacyMode](#setwindowprivacymode9)).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return the window screenshot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function snapshotIgnorePrivacy can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let promise = windowClass.snapshotIgnorePrivacy();
promise.then((pixelMap: image.PixelMap) => {
  console.info('Succeeded in snapshotting window. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
  pixelMap.release(); // Release the memory in time after the PixelMap is used.
}).catch((err: BusinessError) => {
  console.error(\`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setAspectRatio10+

setAspectRatio(ratio: number): Promise<void>

Sets the aspect ratio of the window content layout (excluding decorations like borders and title bars). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/3fTb4w7UQIm9URKPyj7k9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F4FC0D29DE68C548C1DBFE65834AA155D1A5CD141D98A8EB57D61B6E740C4AE)

-   When the window size is set by using other APIs such as [resize](#resize9) and [resizeAsync](#resizeasync12), the window size is not restricted by **ratio**.
    
-   This setting is available only for the main window and takes effect only in floating window mode (**window.WindowStatusType.FLOATING** mode). The aspect ratio is saved persistently, which means that the setting is valid in floating window mode even after the application is closed or the device is restarted.
    
-   After the aspect ratio is set for a main window of an application, the aspect ratio is used for subsequent main windows. If you need to set the aspect ratio for just one main window, use [setContentAspectRatio](#setcontentaspectratio21) instead.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ratio | number | Yes | Aspect ratio of the window content layout (excluding decorations like borders and title bars). The value is a floating-point number and is restricted by the maximum and minimum sizes of the window. The minimum ratio is the value of minimum width divided by the maximum height, and the maximum ratio is the maximum width divided by the minimum height. The maximum and minimum sizes of the window are determined by the intersection of [WindowLimits](../interfaces-others/document.md#windowlimits11) and the system limit. The system limit takes precedence over [WindowLimits](../interfaces-others/document.md#windowlimits11). The valid range of **ratio** varies with [WindowLimits](../interfaces-others/document.md#windowlimits11). If [WindowLimits](../interfaces-others/document.md#windowlimits11) is set first and the subsequently set **ratio** conflicts with it, an error code will be returned. If **ratio** is set first and **\[WindowLimits\]** is subsequently set in conflict with it, the window aspect ratio may not follow the set **ratio**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: Invalid parameter range. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
    if (!windowClass) {
      console.info('windowClass is null');
    }
    try {
      let ratio = 1.0;
      let promise = windowClass.setAspectRatio(ratio);
      promise.then(() => {
        console.info('Succeeded in setting aspect ratio of window.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}\`);
      });
    } catch (exception) {
      console.error(\`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### setAspectRatio10+

setAspectRatio(ratio: number, callback: AsyncCallback<void>): void

Sets the aspect ratio of the window content layout (excluding decorations like borders and title bars). This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/W_3wF5TATHW1n4_T9GsHDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B943BE9F105E55F8132F25CA48268CD3AD02D29A50B289E51EEAB57C727FC024)

-   When the window size is set by using other APIs such as [resize](#resize9) and [resizeAsync](#resizeasync12), the window size is not restricted by **ratio**.
    
-   This setting is available only for the main window and takes effect only in floating window mode (**window.WindowStatusType.FLOATING** mode). The aspect ratio is saved persistently, which means that the setting is valid in floating window mode even after the application is closed or the device is restarted.
    
-   After the aspect ratio is set for a main window of an application, the aspect ratio is used for subsequent main windows. If you need to set the aspect ratio for just one main window, use [setContentAspectRatio](#setcontentaspectratio21) instead.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ratio | number | Yes | Aspect ratio of the window content layout (excluding decorations like borders and title bars). The value is a floating-point number and is restricted by the maximum and minimum sizes of the window. The minimum ratio is the value of minimum width divided by the maximum height, and the maximum ratio is the maximum width divided by the minimum height. The maximum and minimum sizes of the window are determined by the intersection of [WindowLimits](../interfaces-others/document.md#windowlimits11) and the system limit. The system limit takes precedence over [WindowLimits](../interfaces-others/document.md#windowlimits11). The valid range of **ratio** varies with [WindowLimits](../interfaces-others/document.md#windowlimits11). If [WindowLimits](../interfaces-others/document.md#windowlimits11) is set first and the subsequently set **ratio** conflicts with it, an error code will be returned. If **ratio** is set first and **\[WindowLimits\]** is subsequently set in conflict with it, the window aspect ratio may not follow the set **ratio**. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: Invalid parameter range. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
    if (!windowClass) {
      console.info('Failed to load the content. Cause: windowClass is null');
    }
    try {
      let ratio = 1.0;
      windowClass.setAspectRatio(ratio, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeeded in setting the aspect ratio of window.');
      });
    } catch (exception) {
      console.error(\`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### setContentAspectRatio21+

setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>

Sets the aspect ratio of the window content layout (excluding decorations like borders and title bars). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/uUQzj2-5T8eIFjk6L0zqTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=605D9CA893BD8AA9157614FA4FA764C7A792110D04E55F0D9B8C4585C2EE6DB0)

-   When you adjust the window width and height using the same **ratio** parameter, the window size adapts to changes in the border decoration size or visibility.
    
-   When the window title bar is set to invisible by using [setWindowDecorVisible](#setwindowdecorvisible11), the window content area takes over the space that was previously used by the title bar.
    
-   When the window size is set by using other APIs such as [resize](#resize9) and [resizeAsync](#resizeasync12), the window size is not restricted by **ratio**.
    
-   This setting is available only for the main window and takes effect only in floating window mode (**window.WindowStatusType.FLOATING** mode).
    

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ratio | number | Yes | Aspect ratio of the window content layout (excluding decorations like borders and title bars). The value is a floating-point number and is restricted by the maximum and minimum sizes of the window. The minimum ratio is the value of minimum width divided by the maximum height, and the maximum ratio is the maximum width divided by the minimum height. The maximum and minimum sizes of the window are determined by the intersection of [WindowLimits](../interfaces-others/document.md#windowlimits11) and the system limit. The system limit takes precedence over [WindowLimits](../interfaces-others/document.md#windowlimits11). The valid range of **ratio** varies with [WindowLimits](../interfaces-others/document.md#windowlimits11). If [WindowLimits](../interfaces-others/document.md#windowlimits11) is set first and the subsequently set **ratio** conflicts with it, an error code will be returned. If **ratio** is set first and **\[WindowLimits\]** is subsequently set in conflict with it, the window aspect ratio may not follow the set **ratio**. |
| isPersistent | boolean | No | 
Whether the aspect ratio should be saved persistently.

If this parameter is set to **true**, the aspect ratio is saved persistently. This means that the setting is valid in floating window mode even after the window is destroyed, the application is closed, or the device is restarted. You can call [resetAspectRatio](#resetaspectratio10) to clear the persistently saved aspect ratio.

If this parameter is set to **false**, the aspect ratio applies only to the current window and is cleared once the window is destroyed.

The default value is **true**.

 |
| needUpdateRect | boolean | No | 

Whether the window size should be immediately updated based on the current aspect ratio.

If this parameter is set to **true**, the window size is updated immediately based on the current aspect ratio.

If this parameter is set to **false**, the window size is updated based on the current aspect ratio when dragged and resized. You can manually trigger an update by calling [resize](#resize9) or [resizeAsync](#resizeasync12).

The default value is **true**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows are supported. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. 2. Invalid parameter length. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      let windowClass = windowStage.getMainWindowSync();
      let ratio = 1.0;
      let promise = windowClass.setContentAspectRatio(ratio, true, true);
      promise.then(() => {
        console.info('Succeeded in setting aspect ratio of window.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}\`);
      });
    } catch (exception) {
      console.error(\`Failed to set the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### resetAspectRatio10+

resetAspectRatio(): Promise<void>

Resets the aspect ratio of the window content layout. This API uses a promise to return the result.

This API is valid only for the main window. After it is called, the persistently saved aspect ratio is cleared.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
    if (!windowClass) {
      console.info('Failed to load the content. Cause: windowClass is null');
    }
    try {
      let promise = windowClass.resetAspectRatio();
      promise.then(() => {
        console.info('Succeeded in resetting aspect ratio of window.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to reset the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}\`);
      });
    } catch (exception) {
      console.error(\`Failed to reset the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### resetAspectRatio10+

resetAspectRatio(callback: AsyncCallback<void>): void

Resets the aspect ratio of the window content layout. This API uses an asynchronous callback to return the result.

This API is valid only for the main window. After it is called, the persistently saved aspect ratio is cleared.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {

  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
    if (!windowClass) {
      console.info('Failed to load the content. Cause: windowClass is null');
    }
    try {
      windowClass.resetAspectRatio((err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to reset the aspect ratio of window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeeded in resetting aspect ratio of window.');
      });
    } catch (exception) {
      console.error(\`Failed to reset the aspect ratio of window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### minimize11+

minimize(callback: AsyncCallback<void>): void

The behavior of this API varies based on the caller:

-   Minimizes the caller window if it is a main window.. The main window can be restored in the dock bar. For 2-in-1 devices, you can call [restore()](#restore14) to restore the main window.
    
-   Hides the caller window if it is a child window or a global floating window. The child window or floating window cannot be restored in the dock bar. You can call [showWindow()](#showwindow9) to restore it.
    

This API can be called only by the main window, child window, or global floating window. If it is called by other windows, error code 1300002 is thrown. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.minimize((err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in minimizing the window.');
});

#### minimize11+

minimize(): Promise<void>

The behavior of this API varies based on the caller:

-   Minimizes the caller window if it is a main window.. The main window can be restored in the dock bar. For 2-in-1 devices, you can call [restore()](#restore14) to restore the main window.
    
-   Hides the caller window if it is a child window or a global floating window. The child window or floating window cannot be restored in the dock bar. You can call [showWindow()](#showwindow9) to restore it.
    

This API can be called only by the main window, child window, or global floating window. If it is called by other windows, error code 1300002 is thrown. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.minimize();
promise.then(() => {
  console.info('Succeeded in minimizing the window.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### maximize12+

maximize(presentation?: MaximizePresentation): Promise<void>

Maximizes the window. You can call this API to maximize the main window. For child windows, you need to set **maximizeSupported** to **true** during creation, and then call this API to maximize them. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, calls to this API do not take effect or return an error

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| presentation | [MaximizePresentation](../enums/document.md#maximizepresentation12) | No | Layout of the main window or child window when maximized. The default value is **window.MaximizePresentation.ENTER\_IMMERSIVE**, indicating that the window enters the full-screen mode when maximized. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function maximize can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and maximizable subwindows are supported. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let promise = windowClass.maximize();
      // let promise = windowClass.maximize(window.MaximizePresentation.ENTER\_IMMERSIVE);
      promise.then(() => {
        console.info('Succeeded in maximizing the window.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
};

#### maximize22+

maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>

Maximizes the window. You can call this API to maximize the main window. For child windows, you need to set **maximizeSupported** to **true** during creation, and then call this API to maximize them. On 2-in-1 devices with folding capabilities, you can use the **acrossDisplay** parameter to control the main window's behavior in waterfall mode when it is maximized in the hover state. For details about the hover state, see [Semi-Folded State of Foldable Screens](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-folded-hover). This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, calls to this API do not take effect or return an error

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| presentation | [MaximizePresentation](../enums/document.md#maximizepresentation12) | No | Layout of the main window or child window when maximized. The default value is **window.MaximizePresentation.ENTER\_IMMERSIVE**, indicating that the window enters the full-screen mode when maximized. |
| acrossDisplay | boolean | No | 
Behavior of the main window in waterfall mode when maximized in the hover state. The default value is **undefined**.

This parameter can be set only for the main window. Calling it on non-main windows results in error code 1300004.

When this parameter is set to **true**:

\- In the hover state, the window enters waterfall mode directly.

\- In the unfolded state, the window maximizes and retains waterfall mode when in the hover state.

When this parameter is set to **false**:

\- In the hover state, the window exits waterfall mode and maximizes on one half of the screen (single-sided maximization).

\- In the unfolded state, the window maximizes and exits waterfall mode when in the hover state.

When this parameter is set to **undefined** or not provided, the main window's behavior in waterfall mode remains unchanged.

\- In the hover state, the window maximizes on one half of the screen.

\- In the unfolded state, the window maximizes and defaults to maintaining waterfall mode when in the hover state.

**Device behavior differences**: This API can be called properly only on 2-in-1 devices with folding capabilities. Calls to this API do not take effect on other devices.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function maximize can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only main windows and maximizable subwindows are supported. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      let mainWindow = windowStage.getMainWindowSync();
      mainWindow.maximize(window.MaximizePresentation.ENTER\_IMMERSIVE, true)
        .then(() => {
          console.info('Window maximized successfully.');
        })
        .catch((err: BusinessError) => {
          console.error(\`Failed to maximize the window. Cause code: ${err.code}, message: ${err.message}\`);
        });
    });
  }
};

#### setResizeByDragEnabled14+

setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void

Sets whether to enable the main window or child window with decorations to resize itself by dragging. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to enable the window to resize itself by dragging. **true** to enable, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  let enabled = false;
  windowClass.setResizeByDragEnabled(enabled, (err) => {
    if (err.code) {
      console.error(\`Failed to set the function of disabling the resize by drag window. Cause code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in setting the function of disabling the resize by drag window.\`);
  });
} catch (exception) {
  console.error(\`Failed to set the function of disabling the resize by drag window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setResizeByDragEnabled14+

setResizeByDragEnabled(enable: boolean): Promise<void>

Sets whether to enable the main window or child window with decorations to resize itself by dragging. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to enable the window to resize itself by dragging. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let enabled = false;
  let promise = windowClass.setResizeByDragEnabled(enabled);
  promise.then(() => {
    console.info(\`Succeeded in setting the function of disabling the resize by drag window.\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the function of disabling the resize by drag window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the function of disabling the resize by drag window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### recover11+

recover(): Promise<void>

Restores the main window from the full-screen, maximized, or split-screen mode to a floating window (**window.WindowStatusType.FLOATING** mode), and restores the window size and position to those before the full-screen, maximized, or split-screen mode is entered. If the main window is already in the floating window mode, nothing will happen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let windowClass = windowStage.getMainWindowSync();
      if (!windowClass) {
        console.error('Failed to get main window.');
        return;
      }
      let promise = windowClass.recover();
      promise.then(() => {
        console.info('Succeeded in recovering the window.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to recover the window. Cause code: ${err.code}, message: ${err.message}\`);
      });
    } catch (exception) {
      console.error(\`Failed to recover the window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### restore14+

restore(): Promise<void>

Restores the main window from minimization to the foreground, returning it to its size and position before it is minimized. This API takes effect only when the main window is minimized and the UIAbility is in the onForeground state. If the main window is already in the foreground, this API simply raises the window's layer. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      let windowClass = windowStage.getMainWindowSync();
      // Call minimize() to minimize the main window.
      windowClass.minimize();
      // Set the delay function to restore the main window after 5 seconds.
      setTimeout(()=>{
        // Call restore() to restore the main window.
        let promise = windowClass.restore();
        promise.then(() => {
          console.info('Succeeded in restoring the window.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to restore the window. Cause code: ${err.code}, message: ${err.message}\`);
        });
      }, 5000);
    } catch (exception) {
      console.error(\`Failed to restore the window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### getWindowLimits11+

getWindowLimits(): WindowLimits

Obtains the size limits of this application window, in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowLimits](../interfaces-others/document.md#windowlimits11) | Window size limits. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let windowLimits = windowClass.getWindowLimits();
} catch (exception) {
  console.error(\`Failed to obtain the window limits of window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowLimitsVP22+

getWindowLimitsVP(): WindowLimits

Obtains the size limits of this application window, in vp.

For system windows and global floating windows, the default minimum width and height are set to 1 px. The 1 vp value obtained via this API represents the result after rounding calculations.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowLimits](../interfaces-others/document.md#windowlimits11) | Window size limits. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let windowLimits: window.WindowLimits = windowClass.getWindowLimitsVP();
} catch (exception) {
  console.error(\`Failed to obtain the window limits. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowLimits11+

setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>

Sets the size limits for this window. This API returns the result using a promise asynchronously.

By default, system size limits are provided. They are determined by the product configuration and cannot be modified.

If **setWindowLimits** has not been called, you can call [getWindowLimits](#getwindowlimits11) or [getWindowLimitsVP](#getwindowlimitsvp22) to obtain the system limits.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowLimits | [WindowLimits](../interfaces-others/document.md#windowlimits11) | Yes | Target size limits, in px or vp. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WindowLimits](../interfaces-others/document.md#windowlimits11)\> | Promise used to return the final size limits, which are the intersection between the passed-in size limits and the system size limits. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let windowLimits: window.WindowLimits = {
    maxWidth: 1500,
    maxHeight: 1000,
    minWidth: 500,
    minHeight: 400
  };
  let promise = windowClass.setWindowLimits(windowLimits);
    promise.then((data) => {
    console.info('Succeeded in changing the window limits. Cause:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to change the window limits. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to change the window limits. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowLimits15+

setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>

Sets the size limits for this window. This API returns the result using a promise asynchronously.

By default, system size limits are provided. They are determined by the product configuration and cannot be modified.

If **setWindowLimits** has not been called, you can call [getWindowLimits](#getwindowlimits11) or [getWindowLimitsVP](#getwindowlimitsvp22) to obtain the system limits.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**

In versions earlier than HarmonyOS 5.1.1, this API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

Since HarmonyOS 5.1.1, this API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device supports freeform windows but is not in the freeform window state, or if the device does not support freeform windows, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowLimits | [WindowLimits](../interfaces-others/document.md#windowlimits11) | Yes | Target size limits, in px or vp. |
| isForcible | boolean | Yes | 
Whether to forcibly set the window size limits.

When the unit of the input parameter [windowLimits](../interfaces-others/document.md#windowlimits11) is vp, the operation is performed based on value **false** regardless of whether this parameters is set to **true** or **false**. The minimum and maximum window widths and heights depend on the system limit.

When the unit of the input parameter [windowLimits](../interfaces-others/document.md#windowlimits11) is px: If this parameter is set to **true**, the minimum width and height of the window are subject to the smaller value between the system limit and 40 vp, and the maximum width and height of the window are subject to the system limit. If this parameter is set to **false**, the minimum and maximum widths and heights of the window are subject to the system limit.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WindowLimits](../interfaces-others/document.md#windowlimits11)\> | 
Promise used to return the new window size limits.

If the unit of the input parameter [windowLimits](../interfaces-others/document.md#windowlimits11) is vp, the intersection of the input parameter and the default window size limit of the system is returned.

If the unit of the input parameter [windowLimits](../interfaces-others/document.md#windowlimits11) is px: The intersection of the input parameter and the default window size limit of the system is returned when **isForcible** is set to **false**. The intersection of the input parameter and \[the smaller value between the system limit and 40 vp, the maximum value of the system limit\] is returned when **isForcible** is set to **true**.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let windowLimits: window.WindowLimits = {
    maxWidth: 1500,
    maxHeight: 1000,
    minWidth: 100,
    minHeight: 100
  };
  let promise = windowClass.setWindowLimits(windowLimits, true);
  promise.then((data) => {
    console.info(\`Succeeded in changing the window limits. Cause: ${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to change the window limits. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to change the window limits. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowMask12+

setWindowMask(windowMask: Array<Array<number>>): Promise<void>;

Sets a mask for this window to get an irregularly shaped window. This API uses a promise to return the result. The mask is used to describe the shape of the irregularly shaped window. This API is available only for child windows and global floating windows.

When the size of an irregularly shaped window changes, the actual display content is the intersection of the mask size and the window size.

Error code 1300002 may be returned only when multiple threads operate the same window. Error code 401 is returned when the window is destroyed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowMask | Array<Array<number>> | Yes | Mask. The value can only be a two-dimensional array containing the window size in pixels, with each element in the array set to either **0** or **1**. The value **0** indicates that the pixel is transparent, and **1** indicates that the pixel is opaque. If the passed-in pixel array does not match the window size or the value of any element in the array is not **0** or **1**, the value is invalid. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
try {
  let maskWidth = windowClass.getWindowProperties().windowRect.width;
  let maskHeight = windowClass.getWindowProperties().windowRect.height;
  let windowMask = Array<Array<number>>(maskHeight).fill(\[\]).map((\_, row) => {
    let array = Array<number>(maskWidth);
    for (let i = 0 ; i < maskWidth; i++) {
      array\[i\] = (i + row) > (maskWidth + maskHeight) / 2 ? 1 : 0;
    }
    return array;
  });
  let promise = windowClass.setWindowMask(windowMask);
  promise.then(() => {
    console.info('Succeeded in setting the window mask.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the window mask. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the window mask. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### keepKeyboardOnFocus11+

keepKeyboardOnFocus(keepKeyboardFlag: boolean): void

Determines whether to retain the soft keyboard created by another window when the current window gains focus. This API is only supported by system windows and application sub-windows.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keepKeyboardFlag | boolean | Yes | Whether to keep the soft keyboard created by others. **true** to keep, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

try {
  windowClass.keepKeyboardOnFocus(true);
} catch (exception) {
  console.error(\`Failed to keep keyboard onFocus. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowDecorVisible11+

setWindowDecorVisible(isVisible: boolean): void

Sets whether the title bar is visible in the window. This API takes effect for the window that has a title bar or a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

When the window title bar is hidden and the main window transitions into full-screen mode, hovering the cursor over the hot zone of the top window's title bar will cause a floating title bar to appear. To prevent the floating title bar from appearing, call [setTitleAndDockHoverShown()](#settitleanddockhovershown14).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isVisible | boolean | Yes | Whether the title bar is visible. **true** if visible, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
windowClass.loadContent("pages/page2", storage, (err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in loading the content.');
  let isVisible = false;
  // Call setWindowDecorVisible.
  try {
      windowClass?.setWindowDecorVisible(isVisible);
  } catch (exception) {
      console.error(\`Failed to set the visibility of window decor. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
});

#### getWindowDecorVisible18+

getWindowDecorVisible(): boolean

Checks whether the title bar of this window is visible. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the title bar is visible. **true** if visible, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

let isVisible: boolean | undefined = undefined;
windowClass.setUIContent('pages/WindowPage').then(() => {
  try {
    isVisible = windowClass?.getWindowDecorVisible();
  } catch (exception) {
    console.error(\`Failed to get the window decor visibility. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
})

#### setWindowTitle15+

setWindowTitle(titleName: string): Promise<void>

Sets the window title. The setting takes effect for a window with a title bar. If the window does not have a title bar, error code 1300002 is returned. This API returns the result using a promise asynchronously. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window). If the device does not support freeform windows, this API returns error code 1300002 or 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| titleName | string | Yes | Window title. The title display area should not go past the left side of the three-button area of the system. Any part that goes beyond will show as an ellipsis. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let title = "title";
  windowClass.setWindowTitle(title).then(() => {
    console.info('Succeeded in setting the window title.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the window title. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the window title. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowTitleMoveEnabled14+

setWindowTitleMoveEnabled(enabled: boolean): void

Enables or disables the capability to move the window (either main window or child window) by dragging its title bar and to maximize the window with a double-click. When this capability is disabled, you can use [startMoving()](#startmoving14) to move the window by dragging in the application's hot zone and use [maximize()](#maximize12) to maximize the window. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable the capability to move the window by dragging the title bar and to maximize the window with a double-click. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      windowStage.loadContent("pages/Index").then(() =>{
        let windowClass = windowStage.getMainWindowSync();
        let enabled = false;
        windowClass.setWindowTitleMoveEnabled(enabled);
        console.info(\`Succeeded in setting the the window title move enabled: ${enabled}\`);
      });
    } catch (exception) {
      console.error(\`Failed to set the window title move enabled. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### setSubWindowModal12+

setSubWindowModal(isModal: boolean): Promise<void>

Enables the modal property of the child window. This API uses a promise to return the result.

This API must be called by a child window and the setting takes effect for the child window. After the modal property is enabled, the parent window does not respond to user interactions until the child window is closed or the child window's modal property is disabled.

If this API is called by a main window, an error is reported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isModal | boolean | Yes | Whether to enable the modal property of the child window. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    // Create a child window.
    try {
      let subWindow = windowStage.createSubWindow("testSubWindow");
      subWindow.then((data) => {
        if (data == null) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        windowClass = data;
        let promise = windowClass.setSubWindowModal(true);
        promise.then(() => {
          console.info('Succeeded in setting subwindow modal');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set subwindow modal. Cause code: ${err.code}, message: ${err.message}\`);
        });
      });
    } catch (exception) {
      console.error(\`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### setSubWindowModal14+

setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>

Sets the modality type of the child window. This API uses a promise to return the result.

When the child window is of the window-modal type, its parent window does not respond to user interactions until the child window is closed or the child window's modal property is disabled.

When the child window is of the application-modal type, its parent window and the windows from other instances of the application do not respond to user interactions until the child window is closed or the child window's modal property is disabled.

This API is used to set the modality type only. To disable the modal property, you are advised to use [setSubWindowModal12+](#setsubwindowmodal12).

If this API is called by a main window, an error is reported.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isModal | boolean | Yes | Whether to enable the modal property of the child window. **true** to enable, **false** otherwise. Currently, this parameter can only be set to **true**. |
| modalityType | [ModalityType](../enums/document.md#modalitytype14) | Yes | Modality type of the child window. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    // Create a child window.
    try {
      let subWindow = windowStage.createSubWindow("testSubWindow");
      subWindow.then((data) => {
        if (!data) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        windowClass = data;
        let promise = windowClass.setSubWindowModal(true, window.ModalityType.WINDOW\_MODALITY);
        promise.then(() => {
          console.info('Succeeded in setting subwindow modal');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set subwindow modal. Cause code: ${err.code}, message: ${err.message}\`);
        });
      });
    } catch (exception) {
      console.error(\`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### setWindowDecorHeight11+

setWindowDecorHeight(height: number): void

Sets the height of the title bar of this window. This API takes effect for the window that has a title bar and a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

For tablets, if this API is called when the device is not in [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the change applies once the device switches to freeform window mode. If this API is called when the device is in freeform window mode, the change takes effect immediately.

When the main window transitions into full-screen mode, hovering the mouse over the hot zone of the window's title bar region will cause a floating title bar to appear, with a fixed height of 37 vp.

Due to the precision error in pixel conversion, the value obtained by calling [getWindowDecorHeight()](#getwindowdecorheight11) may differ from the set value by 1 vp.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window). If the device does not support freeform windows, calls to this API do not take effect or return an error.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| height | number | Yes | Height of the title bar. It takes effect only for the window with the title bar. The value is an integer in the range \[37,112\]. The unit is vp. If a floating-point number is passed in, the value is rounded down. A value outside the range is invalid. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

windowClass.setUIContent('pages/WindowPage').then(() => {
  let height: number = 50;
  try {
    windowClass?.setWindowDecorHeight(height);
    console.info(\`Succeeded in setting the height of window decor: ${height}\`);
  } catch (exception) {
    console.error(\`Failed to set the height of window decor. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
})

#### setDecorButtonStyle14+

setDecorButtonStyle(dectorStyle: DecorButtonStyle): void

Sets the button style of the decoration bar. The setting takes effect only for the main window and child windows. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**

In versions earlier than HarmonyOS 5.1.0, this API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

Since HarmonyOS 5.1.0, this API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device supports freeform windows but is not in the freeform window state, or if the device does not support freeform windows, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dectorStyle | [DecorButtonStyle](../interfaces-others/document.md#decorbuttonstyle14) | Yes | Button style of the decoration bar. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { ConfigurationConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      windowStage.loadContent("pages/Index").then(() =>{
        let windowClass = windowStage.getMainWindowSync();
        let colorMode : ConfigurationConstant.ColorMode = ConfigurationConstant.ColorMode.COLOR\_MODE\_LIGHT;
        let style: window.DecorButtonStyle = {
          colorMode: colorMode,
          buttonBackgroundSize: 28,
          spacingBetweenButtons: 12,
          closeButtonRightMargin: 20,
          buttonIconSize: 20,
          buttonBackgroundCornerRadius: 4
        };
        windowClass.setDecorButtonStyle(style);
        console.info(\`Succeeded in setting the style of button. Data: ${JSON.stringify(style)}\`);
      });
    } catch (exception) {
      console.error(\`Failed to set the style of button. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### getDecorButtonStyle14+

getDecorButtonStyle(): DecorButtonStyle

Obtains the button style of the decoration bar. The setting takes effect only for the main window and child windows.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**

In versions earlier than HarmonyOS 5.1.0, this API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

Since HarmonyOS 5.1.0, this API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device supports freeform windows but is not in the freeform window state, or if the device does not support freeform windows, this API returns error code 801 when called.

**Return value**

| Type | Description |
| :-- | :-- |
| [DecorButtonStyle](../interfaces-others/document.md#decorbuttonstyle14) | Button style on the decoration bar of the current window. The decoration button area is located in the top-right corner of the window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

try {
  let decorButtonStyle = windowClass.getDecorButtonStyle();
  console.info(\`Succeeded in getting the style of button. Data: ${JSON.stringify(decorButtonStyle)}\`);
} catch (exception) {
  console.error(\`Failed to get the style of button. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowDecorHeight11+

getWindowDecorHeight(): number

Obtains the height of the title bar of this window. This API takes effect for the window that has a title bar and a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

Due to the precision error in pixel conversion, the value obtained by calling [setWindowDecorHeight()](#setwindowdecorheight11) may differ from the set value by 1 vp.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window). If the device does not support freeform windows, calls to this API do not take effect or return an error.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Height of the title bar. The value is an integer in the range \[37,112\]. The unit is vp. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

windowClass.setUIContent('pages/WindowPage').then(() => {
  try {
    let height = windowClass?.getWindowDecorHeight();
    console.info(\`Succeeded in getting the height of window decor: ${height}\`);
  } catch (exception) {
    console.error(\`Failed to get the height of window decor. Cause code: ${exception.code}, message: ${exception.message}\`);
  }
})

#### getTitleButtonRect11+

getTitleButtonRect(): TitleButtonRect

Obtains the rectangle that holds the minimize, maximize, and close buttons on the title bar of the main window or the decorated child window.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [TitleButtonRect](../interfaces-others/document.md#titlebuttonrect11) | Rectangle obtained, which is located in the top-right corner of the window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let titleButtonArea = windowClass.getTitleButtonRect();
        console.info('Succeeded in obtaining the area of title buttons. Data: ' + JSON.stringify(titleButtonArea));
      } catch (exception) {
        console.error(\`Failed to get the area of title buttons. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### getWindowStatus12+

getWindowStatus(): WindowStatusType

Obtains the mode of this window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/CVIkdOPZTT6w3EltB_9Nsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92DA5AC9F92A8B40719EC00E1D423C5EF52CE94DD1D8BA2E97B5D7E1DBC3AD5A)

In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, when the window is maximized (covering the entire screen, with a dock bar and status bar on 2-in-1 devices, and a status bar on tablets), the return value differs based on the [targetAPIVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) setting. For versions below 14, the return value is **WindowStatusType::FULL\_SCREEN**. For versions 14 and above, the return value is **WindowStatusType::MAXIMIZE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| [WindowStatusType](../enums/document.md#windowstatustype11) | Window mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let windowStatusType = windowClass.getWindowStatus();
} catch (exception) {
  console.error(\`Failed to obtain the window status of window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### isFocused12+

isFocused(): boolean

Checks whether this window is focused.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the window is focused. **true** if focused, **false** otherwise. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |

**Example**

try {
  let focus = windowClass.isFocused();
  console.info(\`Succeeded in checking whether the window is focused. Data: ${focus}\`);
} catch (exception) {
  console.error(\`Failed to check whether the window is focused. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### createSubWindowWithOptions12+

createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>

Creates a child window under the main window, another child window, or floating window. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns **undefined** when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the child window. |
| options | [SubWindowOptions](../interfaces-others/document.md#subwindowoptions11) | Yes | Parameters used for creating the child window. If **decorEnabled** is set to **true**, the child window does not use an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout). If **decorEnabled** is set to **false**, the child window uses an immersive layout. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](#)\> | Promise used to used to return the child window created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let options : window.SubWindowOptions = {
    title: 'title',
    decorEnabled: true,
    isModal: true
  };
  let promise = windowClass.createSubWindowWithOptions('mySubWindow', options);
  promise.then((data) => {
    console.info(\`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setParentWindow19+

setParentWindow(windowId: number): Promise<void>

Sets a new parent window for this child window. The new parent window can be a main window, another child window, or a floating window in the same process. This API uses a promise to return the result.

If the child window is focused and the new parent window is in the foreground, the new parent window will be raised.

If the child window is focused and the new parent window has a modal child window with a higher level, the focus will be transferred to that modal child window.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

**Atomic service API**: This API can be used in atomic services since API version 19.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | Parent window ID, which must be an integer. You are advised to call [getWindowProperties()](#getwindowproperties9) to obtain the parent window ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let windowClass: window.Window = window.findWindow("subWindow");
  let newParentWindow: window.Window = window.findWindow("newParentWindow");
  let newParentWindowId: number = newParentWindow.getWindowProperties().id;
  let promise = windowClass.setParentWindow(newParentWindowId);
  promise.then(() => {
    console.info('Succeeded in setting the new parent window.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the new parent window. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the new parent window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getParentWindow19+

getParentWindow(): Window

Obtains the parent window of this child window.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on 2-in-1 devices but returns error code 801 on other devices.

**Atomic service API**: This API can be used in atomic services since API version 19.

**Return value**

| Type | Description |
| :-- | :-- |
| [Window](#) | Parent window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**Example**

try {
  let windowClass: window.Window = window.findWindow("subWindow");
  let parentWindow: window.Window = windowClass.getParentWindow();
  let properties = parentWindow.getWindowProperties();
  console.info(\`Succeeded in obtaining parent window properties. Property: ${JSON.stringify(properties)}\`);
} catch (exception) {
  console.error(\`Failed to get the parent window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowTitleButtonVisible14+

setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void

Shows or hides the maximize, minimize, and close buttons on the title bar of the main window.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isMaximizeButtonVisible | boolean | Yes | Whether to show the maximize button. **true** to show, **false** otherwise. If the maximize button is hidden, the corresponding restore button is also hidden in the maximize scenario. |
| isMinimizeButtonVisible | boolean | Yes | Whether to show the minimize button. **true** to show, **false** otherwise. |
| isCloseButtonVisible | boolean | No | Whether to show the close button. **true** to show, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Load the page corresponding to the main window.
    windowStage.loadContent('pages/Index', (err) => {
      let mainWindow: window.Window | undefined = undefined;
      // Obtain the main window.
      windowStage.getMainWindow().then(
        data => {
          if (!data) {
            console.error('Failed to get main window. Cause: The data is undefined.');
            return;
          }
          mainWindow = data;
          console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
          // Call setWindowTitleButtonVisible to hide the maximize, minimize, and close buttons on the title bar of the main window.
          mainWindow.setWindowTitleButtonVisible(false, false, false);
        }
      ).catch((err: BusinessError) => {
          if(err.code){
            console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
          }
      });
    });
  }
}

#### setWindowTopmost14+

setWindowTopmost(isWindowTopmost: boolean): Promise<void>

Places the main window above all the other windows of the application. This API uses a promise to return the result.

Applications use custom shortcut keys to pin or unpin the main window.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Required permissions**: ohos.permission.WINDOW\_TOPMOST

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isWindowTopmost | boolean | Yes | Whether to pin the main window on top. **true** to pin, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined;
let keyUpEventAry: string\[\] = \[\];

@Entry
@Component
struct Index {
  private context = (this.getUIContext()?.getHostContext() as common.UIAbilityContext);
  private windowStage = this.context.windowStage;

  build() {
    RelativeContainer() {
      Button("Pin")
        .onClick(() => {
          try {
            windowClass = this.windowStage.getMainWindowSync();
            // The value true indicates to pin the window on top, and value false indicates to unpin the window.
            let isWindowTopmost: boolean = true;
            let promiseTopmost = windowClass.setWindowTopmost(isWindowTopmost);
            promiseTopmost.then(() => {
              console.info('Succeeded in setting the main window to be topmost.');
            }).catch((err: BusinessError) => {
              console.error(\`Failed to set the main window to be topmost. Cause code: ${err.code}, message: ${err.message}\`);
            });
          } catch (exception) {
            console.error(\`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}\`)
          }
        })
    }
    .height('100%')
    .width('100%')
    .onKeyEvent((event) => {
      if(event) {
        if(event.type === KeyType.Down) {
          keyUpEventAry = \[\];
        }
        if(event.type === KeyType.Up) {
          keyUpEventAry.push(event.keyText);
          // Press Ctrl+T to pin or unpin the main window.
          if(windowClass && keyUpEventAry.includes('KEYCODE\_CTRL\_LEFT') && keyUpEventAry.includes('KEYCODE\_T')) {
            let isWindowTopmost: boolean = false;
            windowClass.setWindowTopmost(isWindowTopmost);
          }
        }
      }
    })
  }
}

#### raiseToAppTop14+

raiseToAppTop(): Promise<void>

Brings a child window to the top. This action is limited to child windows of the same type under the same parent window within the current application. For child windows with a custom zLevel property, it only applies to child windows with the same zLevel value under the same parent window within the current application. This API uses a promise to return the result.

Before calling this API, ensure that the child window has been created and the call to [showWindow()](#showwindow9) from the child window has been completed.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**Example**

// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    // Create a child window.
    windowStage.createSubWindow('testSubWindow').then((subWindow) => {
      if (subWindow == null) {
        console.error('Failed to create the subWindow. Cause: The data is empty');
        return;
      }
      subWindow.showWindow().then(() => {
        subWindow.raiseToAppTop().then(() => {
          console.info('Succeeded in raising window to app top');
        }).catch((err: BusinessError)=>{
          console.error(\`Failed to raise window to app top. Cause code: ${err.code}, message: ${err.message}\`);
        });
      });
    });
  }
}

#### setRaiseByClickEnabled14+

setRaiseByClickEnabled(enable: boolean): Promise<void>

Sets whether to enable a child window to raise itself by click. This API uses a promise to return the result.

Generally, when a child window is clicked, it is brought to the forefront among sibling child windows of the same type that share the same parent window within the application. If the **enable** parameter is set to **false**, when the child window is clicked, it still stays in its existing position.

Before calling this API, ensure that the child window has been created and the call to [showWindow()](#showwindow9) from the child window has been completed.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether a child window can be raised by clicking. **true** if the child window can be raised by clicking, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300009 | The parent window is invalid. |

**Example**

// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    // Create a child window.
    windowStage.createSubWindow("testSubWindow").then((subWindow) => {
      if (subWindow == null) {
        console.error('Failed to create the subWindow. Cause: The data is empty');
        return;
      }
      subWindow.showWindow().then(() => {
        try {
          let enabled = false;
          subWindow.setRaiseByClickEnabled(enabled).then(() => {
            console.info('Succeeded in disabling the raise-by-click function.');
          }).catch((err: BusinessError) => {
            console.error(\`Failed to disable the raise-by-click function. Cause code: ${err.code}, message: ${err.message}\`);
          });
        } catch (err) {
          console.error(\`Failed to disable the raise-by-click function. Cause code: ${err.code}, message: ${err.message}\`);
        }
      });
    });
  }
}

#### enableLandscapeMultiWindow12+

enableLandscapeMultiWindow(): Promise<void>

Enables the landscape multi-window mode for the UI page that supports the horizontal layout. You are not advised to call this API for the UI page that adopts the vertical layout.

This API takes effect only for the main window of the application. In addition, **preferMultiWindowOrientation** must be set to **landscape\_auto** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) tag in the **module.json5** file.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let promise = windowClass.enableLandscapeMultiWindow();
      promise.then(() => {
        console.info('Succeeded in making multi-window become landscape.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to make multi-window become landscape. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
}

#### disableLandscapeMultiWindow12+

disableLandscapeMultiWindow(): Promise<void>

Disables the landscape multi-window mode for the UI page that supports the horizontal layout.

This API takes effect only for the main window of the application. In addition, **preferMultiWindowOrientation** must be set to **landscape\_auto** in the [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) tag in the **module.json5** file.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let promise = windowClass.disableLandscapeMultiWindow();
      promise.then(() => {
        console.info('Succeeded in making multi-window become not landscape.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to make multi-window become not landscape. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
}

#### setDialogBackGestureEnabled12+

setDialogBackGestureEnabled(enabled: boolean): Promise<void>

Sets whether the modal window responds to the back gesture event. An error code is returned if this API is called for a non-modal window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to respond to the back gesture event.

**true** means to respond to the back gesture event and trigger the **onBackPress** callback, **false** otherwise.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: "test",
      windowType: window.WindowType.TYPE\_DIALOG,
      ctx: this.context
    };
    try {
      window.createWindow(config, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to create the window. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        windowClass = data;
        windowClass.setUIContent("pages/Index");
        let enabled = true;
        let promise = windowClass.setDialogBackGestureEnabled(enabled);
        promise.then(() => {
          console.info('Succeeded in setting dialog window to respond back gesture.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set dialog window to respond back gesture. Cause code: ${err.code}, message: ${err.message}\`);
        });
      });
    } catch (exception) {
      console.error(\`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

// ets/pages/Index.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'
  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .height('100%')
    .width('100%')
  }

  onBackPress(): boolean | void {
    console.info('Succeeded in setting dialog window to respond back gesture.');
    return true;
  }
}

#### enableDrag20+

enableDrag(enable: boolean): Promise<void>

Enables or disables window dragging. This API takes effect only for system windows, application child windows, global floating windows, and modal windows. This API uses a promise to return the result.

After window dragging is enabled, the window can be resized using the mouse or touch operations.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on phones, tablets, and 2-in-1 devices, but returns error code 801 on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable dragging.

**true** to enable, **false** otherwise.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  windowClass.enableDrag(true).then(() => {
    console.info('succeeded in setting window draggable');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set window draggable. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set window draggable. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### startMoving14+

startMoving(): Promise<void>

In [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, this API takes effect for system windows, application main windows, application child windows, global floating windows, and modal windows. In non-freeform window mode, this API takes effect only for system windows, application child windows, global floating windows, and modal windows. Starts moving this window. This API uses a promise to return the result.

The window moves along with the cursor or touch point only when this API is called in the callback function of [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent), where the event type is **TouchType.Down**.

In click-and-drag scenarios, if you do not want the drag to start as soon as you press down, you can call this API to start the moving effect when a [TouchType.Move](../../../../arkts-components/common-definitions/enums/document.md#touchtype) event occurs (as long as **TouchType.Down** has already been triggered) .

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 14.

**Device behavior differences**: This API can be called properly on phones, 2-in-1 devices, and tablets, but returns error code 801 on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private isTouchDown: boolean = false;
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Red)
          .onTouch((event: TouchEvent) => {
            if(event.type == TouchType.Down){
              this.isTouchDown = true;
            } else if (event.type === TouchType.Move && this.isTouchDown) {
              try {
                let context = this.getUIContext()?.getHostContext();
                if (!context) {
                  console.error('Failed to get host context.');
                  return;
                }
                window.getLastWindow(context).then((data)=>{
                  if (!data) {
                    console.error('Failed to get last window.');
                    return;
                  }
                  let windowClass: window.Window = data;
                  windowClass.startMoving().then(() => {
                    console.info('Succeeded in starting moving window.')
                  }).catch((err: BusinessError) => {
                    console.error(\`Failed to start moving. Cause code: ${err.code}, message: ${err.message}\`);
                  });
                });
              } catch (exception) {
                console.error(\`Failed to start moving window. Cause code: ${exception.code}, message: ${exception.message}\`);
              }
            } else {
              this.isTouchDown = false;
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}

#### startMoving15+

startMoving(offsetX: number, offsetY: number): Promise<void>

Specifies the cursor position within the window and moves the window. This API uses a promise to return the result.

When windows within the same application are split or merged, and the mouse is pressed down to move the new window directly, the cursor may move outside the window if it moves too quickly. This API allows you to set the cursor position within the window during movement. It first adjusts the window to the cursor position before starting to move the window.

The window moves along with the cursor only when this API is called in the callback function of [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent), where the event type is **TouchType.Down**.

In click-and-drag scenarios, if you do not want the drag to start as soon as you press down, you can call this API to start the moving effect when a [TouchType.Move](../../../../arkts-components/common-definitions/enums/document.md#touchtype) event occurs (as long as **TouchType.Down** has already been triggered) .

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Atomic service API**: This API can be used in atomic services since API version 15.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offsetX | number | Yes | X-axis offset of the cursor position relative to the top-left corner of the window during movement, measured in px. This parameter only accepts integer values; any floating-point input will be rounded down. Negative values or values greater than the window width are invalid. The window width can be obtained from [WindowProperties](../interfaces-others/document.md#windowproperties). |
| offsetY | number | Yes | Y-axis offset of the cursor position relative to the top-left corner of the window during movement, measured in px. This parameter only accepts integer values; any floating-point input will be rounded down. Negative values or values greater than the window height are invalid. The window height can be obtained from [WindowProperties](../interfaces-others/document.md#windowproperties). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private isTouchDown: boolean = false;
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Red)
          .onTouch((event: TouchEvent) => {
            if(event.type == TouchType.Down){
              this.isTouchDown = true;
            } else if (event.type === TouchType.Move && this.isTouchDown) {
              try {
                let context = this.getUIContext()?.getHostContext();
                if (!context) {
                  console.error('Failed to get host context.');
                  return;
                }
                window.getLastWindow(context).then((data)=>{
                  let windowClass: window.Window = data;
                  windowClass.startMoving(100, 50).then(() => {
                    console.info('Succeeded in starting moving window.')
                  }).catch((err: BusinessError) => {
                    console.error(\`Failed to start moving. Cause code: ${err.code}, message: ${err.message}\`);
                  });
                });
              } catch (exception) {
                console.error(\`Failed to start moving window. Cause code: ${exception.code}, message: ${exception.message}\`);
              }
            } else {
              this.isTouchDown = false;
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}

#### stopMoving15+

stopMoving(): Promise<void>

Stops window movement when a window is being dragged. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Atomic service API**: This API can be used in atomic services since API version 15.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage) {
    try {
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowRectChange', (data: window.RectChangeOptions) => {
        if (data.reason === window.RectChangeReason.MOVE) {
          windowClass.stopMoving().then(() => {
            console.info('Succeeded in stopping moving window.')
          }).catch((err: BusinessError) => {
            console.error(\`Failed to stop moving. Cause code: ${err.code}, message: ${err.message}\`);
          });
        }
      });
    } catch (exception) {
      console.error(\`Failed to stop moving window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### setGestureBackEnabled13+

setGestureBackEnabled(enabled: boolean): Promise<void>

Sets whether to enable the gesture-based swipe-to-return function for the current window. This API can be successfully called only for the main window. If it is called for other types of windows, error code 1300004 will be returned.

After this function is enabled, it takes effect only when the window is in full-screen mode and in the foreground with the focus.

After this function is disabled, the gesture hot zone of the current application is disabled, and the swipe-to-return function becomes invalid. After the user switches to another application or returns to the home screen, the gesture hot zone is restored, and the swipe-to-return function becomes normal.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: When this API is called on 2-in-1 devices, error code 801 is returned. However, it can be called properly on other devices.

**Atomic service API**: This API can be used in atomic services since API version 13.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable the back gesture feature. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;

      // Disable the back gesture feature in the current window.
      try {
        let gestureBackEnabled: boolean = false;
        let promise = windowClass.setGestureBackEnabled(gestureBackEnabled);
        promise.then(() => {
          console.info(\`Succeeded in setting gesture back disabled\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set gesture back disabled, Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch(exception) {
        console.error(\`Failed to set gesture back disabled, Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### isGestureBackEnabled13+

isGestureBackEnabled(): boolean

Obtains whether the back gesture function is enabled for the current window. This API can be successfully called only for the main window. If it is called for other types of windows, error code 1300004 is returned.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: When this API is called on 2-in-1 devices, error code 801 is returned. However, it can be called properly on other devices.

**Atomic service API**: This API can be used in atomic services since API version 13.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the back gesture feature is enabled. **true** if enabled, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;

      // Check whether the back gesture feature is enabled in the current window.
      try {
        let gestureBackEnabled: boolean = windowClass.isGestureBackEnabled();
        console.info(\`Succeeded in obtaining gesture back enabled status: ${gestureBackEnabled}\`);
      } catch (exception) {
        console.error(\`Failed to get gesture back enabled status. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setWindowShadowRadius17+

setWindowShadowRadius(radius: number): void

Sets the blur radius of the shadow on the edges of a child window or floating window.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**

In versions earlier than HarmonyOS 5.1.0, this API can be called properly on 2-in-1 devices and tablets but returns error code 801 on other devices.

In HarmonyOS 5.1.0 and later versions, this API can be called properly on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Atomic service API**: This API can be used in atomic services since API version 17.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | number | Yes | Radius of the shadow, measured in px. The value is a floating-point number greater than or equal to 0.0, and the value **0.0** means that the shadow is disabled for the window borders. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

try {
  windowClass.setWindowShadowRadius(4.0);
} catch (exception) {
  console.error(\`Failed to set shadow. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowCornerRadius17+

setWindowCornerRadius(cornerRadius: number): Promise<void>

Sets the radius of the rounded corners for a child window or floating window. This API uses a promise to return the result.

If the radius of the rounded corner is too large, it may cause the three buttons (maximize, minimize, and close) to be clipped and make their hotspots less recognizable. Set an appropriate radius based on the window size.

Before calling this API, you can call [getWindowCornerRadius()](#getwindowcornerradius17) to obtain the default corner radius of the window.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**

Before HarmonyOS 6.0.0, this API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

In HarmonyOS 6.0.0 and later versions, this API can be called properly on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Atomic service API**: This API can be used in atomic services since API version 17.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cornerRadius | number | Yes | Radius of the rounded corners, measured in vp. The value is a floating-point number greater than or equal to 0.0. The value **0.0** means that the window does not use rounded corners. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = windowClass.setWindowCornerRadius(1.0);
  promise.then(() => {
    console.info('Succeeded in setting window corner radius.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set window corner radius. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set corner radius. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### getWindowCornerRadius17+

getWindowCornerRadius(): number

Obtains the corner radius of a child window or floating window. If [setWindowCornerRadius()](#setwindowcornerradius17) is not yet called to set a corner radius, this API returns the default corner radius.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Atomic service API**: This API can be used in atomic services since API version 17.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Radius of the rounded corner of the child window or floating window, measured in vp. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

try {
  let cornerRadius = windowClass.getWindowCornerRadius();
} catch (exception) {
  console.error(\`Failed to get corner radius. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setExclusivelyHighlighted15+

setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>

Sets the exclusive highlight property for the window. When a window set to exclusive highlight gains focus, other windows in the current parent-child window chain that are in the highlighted state will lose their highlighted state. This API uses a promise to return the result.

This API does not take effect for the main window or modal window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 15.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exclusivelyHighlighted | boolean | Yes | Whether to set exclusive highlight for the window. **true** to set exclusive highlight, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let exclusivelyHighlighted: boolean = true;
try {
  let promise = windowClass.setExclusivelyHighlighted(exclusivelyHighlighted);
  promise.then(() => {
    console.info('Succeeded in setting the window to be exclusively highlight.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the window to be exclusively highlight. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the window to be exclusively highlight. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### isWindowHighlighted18+

isWindowHighlighted(): boolean

Checks whether the window is active. To obtain the active status correctly, call this API when [WindowEventType](../enums/document.md#windoweventtype10) is **WINDOW\_ACTIVE**.

You can use [on('windowHighlightChange')](#onwindowhighlightchange15) to listen for status changes and then execute the corresponding service.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the window is active. **true** if active, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isHighlighted = windowClass.isWindowHighlighted();
  console.info(\`Succeeded in getting the window highlight status: ${isHighlighted}\`);
} catch (exception) {
  console.error(\`Failed to get the window highlight status.. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setFollowParentMultiScreenPolicy17+

setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>

Sets whether a child window can span multiple screens and be simultaneously displayed while its parent window is being dragged or resized. This API uses a promise to return the result.

By default, when a child window follows its parent window's layout changes (through [moveWindowTo()](#movewindowto9)), it does not support multi-screen spanning and simultaneous display.

However, calling this API on the child window enables it to span multiple screens and be simultaneously displayed during the layout adjustment process.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Atomic service API**: This API can be used in atomic services since API version 17.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether the child window can span multiple screens and be simultaneously displayed while its parent window is being dragged or resized. **true** if supported, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported.Function setFollowParentMultiScreenPolicy can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let windowClass: window.Window = window.findWindow("subWindow");
  let enabled: boolean = true;
  let promise = windowClass?.setFollowParentMultiScreenPolicy(enabled);
  promise.then(() => {
    console.info('Succeeded in setting the sub window supports multi-screen simultaneous display')
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the sub window supports multi-screen simultaneous display. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the sub window supports multi-screen simultaneous display. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setFollowParentWindowLayoutEnabled17+

setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>

Sets whether the layout information (position and size) of a child window or modal window (a window with **WindowType** set to **TYPE\_DIALOG**) follows the main window. This API uses a promise to return the result.

1.  This API applies only to first-level child windows or modal windows of the main window.
    
2.  Once this API is called on a child window or modal window, its layout information will immediately match the main window and remain synchronized. This effect will persist until this API is called again with **false**.
    
3.  If this API is called on a child window or modal window, subsequent calls to APIs like **moveTo** or **resize** to modify the layout information will not take effect.
    
4.  When a child window or modal window stops using this functionality, its layout information (position and size) may not be a specific value. The application needs to reset it.
    

Once this API is successfully called, the [setRelativePositionToParentWindowEnabled()](#setrelativepositiontoparentwindowenabled20) API will no longer take effect.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to follow the layout of the main window. **true** to follow, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (loadError) => {
      if (loadError.code) {
        console.error(\`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}\`);
        return;
      }
      console.info("Succeeded in loading the content.");
      windowStage.createSubWindow("subWindow").then((subWindow: window.Window) => {
        if (subWindow == null) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        subWindow.setFollowParentWindowLayoutEnabled(true).then(() => {
          console.info("after set follow parent window layout")
        }).catch((error: BusinessError) => {
          console.error(\`setFollowParentWindowLayoutEnabled failed. ${error.code} ${error.message}\`);
        })
      }).catch((error: BusinessError) => {
        console.error(\`createSubWindow failed. ${error.code} ${error.message}\`);
      })
    });
  }
}

#### setRelativePositionToParentWindowEnabled20+

setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor, offsetX?: number, offsetY?: number): Promise<void>

Sets whether a first-level child window can maintain a fixed relative position to the main window. This API works only in [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode. This API uses a promise to return the result.

The relative position is defined by the offset between the anchor points of the child window and the main window. Both the child window and the main window use the same type of anchor point.

1.  This API applies only to level-1 child windows that are not maximized.
    
2.  Once this API is called on a child window, its display position will immediately follow the main window and maintain a fixed relative position. This effect will persist until this API is called again with **false**.
    
3.  If this API is called on a child window, subsequent calls to [moveWindowTo()](#movewindowto9) or [maximize()](#maximize12) to change the window's position or size will not take effect.
    

Once this API is successfully called, the [setFollowParentWindowLayoutEnabled()](#setfollowparentwindowlayoutenabled17) API will no longer take effect.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on 2-in-1 devices and tablets, but returns error code 801 on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to maintain a fixed relative position to the main window. **true** to maintain, **false** otherwise. |
| anchor | [WindowAnchor](../enums/document.md#windowanchor20) | No | Type of anchor point used to maintain the relative position. This parameter takes effect only when **enabled** is set to **true**. The default value is **window.WindowAnchor.TopStart**, indicating that the default anchor point is the top-left corner of the window. |
| offsetX | number | No | X-axis offset between the anchor points of the child window and the main window, in px. This parameter takes effect only when **enabled** is set to **true**. Only integer values are supported, and Non-integer values are rounded down. The default value is **0**. |
| offsetY | number | No | Y-axis offset between the anchor points of the child window and the main window, in px. This parameter takes effect only when **enabled** is set to **true**. Only integer values are supported, and Non-integer values are rounded down. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.Function setRelativePositionToParentWindowEnabled can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |

**Example**

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (loadError: BusinessError) => {
      if (loadError.code) {
        console.error(\`Failed to load the content. Cause code: ${loadError.code}, message: ${loadError.message}\`);
        return;
      }
      console.info("Succeeded in loading the content.");
      windowStage.createSubWindow("subWindow").then((subWindow: window.Window) => {
        if (subWindow == null) {
          console.error("Failed to create the subWindow. Cause: The data is empty");
          return;
        }
        subWindow.setRelativePositionToParentWindowEnabled(true).then(() => {
          console.info("after set relative position to parent window enabled");
        }).catch((error: BusinessError) => {
          console.error(\`setRelativePositionToParentWindowEnabled failed. ${error.code} ${error.message}\`);
        })
      }).catch((error: BusinessError) => {
        console.error(\`createSubWindow failed. ${error.code} ${error.message}\`);
      })
    });
  }
}

#### setWindowTransitionAnimation20+

setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>

Adds a transition animation to windows in specific scenarios.

Currently, this API can be used only on the main window of an application.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device supports freeform windows but is not in the freeform window state, or if the device does not support freeform windows, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transitionType | [WindowTransitionType](../enums/document.md#windowtransitiontype20) | Yes | Scene of the transition animation. Currently, only the destruction scene is supported. |
| animation | [TransitionAnimation](../interfaces-others/document.md#transitionanimation20) | Yes | Configuration of the transition animation. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range; 2. Invalid parameter length. |

**Example**

// EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        const animationConfig: window.WindowAnimationConfig = {
          duration: 1000,
          curve: window.WindowAnimationCurve.LINEAR,
        };
        const transitionAnimation: window.TransitionAnimation = {
          opacity: 0.5,
          config: animationConfig
        };
        let promise = windowClass.setWindowTransitionAnimation(window.WindowTransitionType.DESTROY, transitionAnimation);
        promise.then((data) => {
          console.info('Succeeded in setting window transition animation. Cause:' + JSON.stringify(data));
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set window transition animation. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (exception) {
        console.error(\`Failed to obtain the window status of window. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    })
  }
}

#### getWindowTransitionAnimation20+

getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined

Obtains the window transition animation configuration in a specific scenario.

Currently, this API can be used only on the main window of an application.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device supports freeform windows but is not in the freeform window state, or if the device does not support freeform windows, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transitionType | [WindowTransitionType](../enums/document.md#windowtransitiontype20) | Yes | Scene of the transition animation. Currently, only the destruction scene is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TransitionAnimation](../interfaces-others/document.md#transitionanimation20) | undefined | Transition animation configuration in the corresponding scene. If the [setWindowTransitionAnimation](#setwindowtransitionanimation20) API is not used yet, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

// EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      try {
        let transitionAnimationResult = windowClass.getWindowTransitionAnimation(window.WindowTransitionType.DESTROY);
        console.info('Succeeded in getting window transition animation: ' + JSON.stringify(transitionAnimationResult));
      } catch (exception) {
        console.error(\`Failed to obtain the window transition animation. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    })
  }
}

#### setSubWindowZLevel18+

setSubWindowZLevel(zLevel: number): Promise<void>

Sets the z-level of the current child window. Child windows with modal properties are not supported. This API uses a promise to return the result.

Changing the z-level of a child window using this API will not cause a focus switch. You are advised to use [shiftAppWindowFocus()](../functions/document.md#windowshiftappwindowfocus11) for focus switching.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Device behavior differences**: This API can be called properly on phones, tablets, and PCs/2-in-1 devices, but returns error code 801 on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| zLevel | number | Yes | Z-level of the child window. The default value is **0**, and the value range is \[-10000, 10000\]. Only integers are supported, and floating-point numbers will be rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Function setSubWindowZLevel can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. Possible cause: Invalid window type. Only non-modal subwindows are supported. |
| 1300009 | The parent window is invalid. |

**Example**

// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let zLevel: number = 1;
    // Create a child window.
    try {
      windowStage.createSubWindow('testSubWindow').then((subWindow) => {
        if (subWindow == null) {
          console.error('Failed to create the sub window. Cause: The sub window is null');
          return;
        }
        subWindow.setSubWindowZLevel(zLevel).then(() => {
          console.info('Succeeded in setting sub window zLevel.');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set sub window zLevel. Cause code: ${err.code}, message: ${err.message}\`);
        });
      });
    } catch (err) {
      console.error(\`Failed to create the sub window or set zLevel. Cause code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### getSubWindowZLevel18+

getSubWindowZLevel(): number

Obtains the z-level of the current child window. This API cannot be called by the main window or system window.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 18.

**Device behavior differences**: This API can be called properly on phones, tablets, and PCs/2-in-1 devices, but returns error code 801 on other devices.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Z-level of the child window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function getSubWindowZLevel can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |

**Example**

// EntryAbility.ets
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let subWindowZLevel = -1;
    // Create a child window.
    windowStage.createSubWindow('testSubWindow').then((subWindow) => {
      if (subWindow == null) {
        console.error('Failed to create the sub window. Cause: The sub window is null');
        return;
      }
      try {
        subWindowZLevel = subWindow.getSubWindowZLevel();
        console.info(\`Succeeded in obtaining sub window zLevel: ${subWindowZLevel}\`);
      } catch (err) {
        console.error(\`Failed to obtain the sub window zLevel. Cause code: ${err.code}, message: ${err.message}\`);
      }
    });
  }
}

#### isInFreeWindowMode22+

isInFreeWindowMode(): boolean

Checks whether the current window is in [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the window is in freeform window mode. **true** if the window is in freeform window mode, **false** otherwise. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

let isInFreeWindowMode: boolean = windowClass.isInFreeWindowMode();
console.info(\`isInFreeWindowMode: ${isInFreeWindowMode}\`);

#### on('freeWindowModeChange')22+

on(type: 'freeWindowModeChange', callback: Callback<boolean>): void

Subscribes to the freeform window mode change event.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'freeWindowModeChange'**, indicating the freeform window mode change event. |
| callback | Callback<boolean> | Yes | Callback used to return the result, indicating whether the window is in freeform window mode. **true** if the window is in freeform window mode, **false** otherwise. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

try {
  windowClass.on('freeWindowModeChange', (data) => {
    console.info('Succeeded in enabling the listener for free window mode changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(\`Failed to enable the listener for free window mode changes. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### off('freeWindowModeChange')22+

off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void

Unsubscribes from the freeform window mode change event.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'freeWindowModeChange'**, indicating the freeform window mode change event. |
| callback | Callback<boolean> | No | Callback used to return the result, indicating whether the window is in freeform window mode. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

const callback = (isInFreeWindowMode: boolean) => {
  // ...
}
try {
  // Enable listening through the on API.
  windowClass.on('freeWindowModeChange', callback);
  // Disable the listening of a specified callback.
  windowClass.off('freeWindowModeChange', callback);
  // Unregister all the callbacks that have been registered through on().
  windowClass.off('freeWindowModeChange');
} catch (exception) {
  console.error(\`Failed to disable the listener for free window mode change. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### setWindowSystemBarProperties(deprecated)

setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void

Sets the properties of the status bar of the main window. This API uses an asynchronous callback to return the result. This API cannot be called for 2-in-1 devices. For other devices, the calling does not take effect immediately in split-screen mode (window.WindowStatusType.SPLIT\_SCREEN mode), floating window mode (window.WindowStatusType.FLOATING mode), or freeform window mode (you can open the mode by touching the Free windows button in Control Panel), but takes effect only on the main window displayed in full-screen mode.

This API does not take effect when it is called by a child window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/A7GNVU_SQvWVfRpp-1yiVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81B70E1C4847A5614E234C0E9065FB0C7898F0D87B039D4CE55DE3FEAED211EF)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [setWindowSystemBarProperties()](#setwindowsystembarproperties9) in promise mode instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| systemBarProperties | [SystemBarProperties](../interfaces-others/document.md#systembarproperties) | Yes | three-button navigation bar and |
| status bar. |  |  |  |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        // The following properties are supported since API version 8.
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      try {
        windowClass.setWindowSystemBarProperties(SystemBarProperties, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(\`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}\`);
            return;
          }
          console.info('Succeeded in setting the system bar properties.');
        });
      } catch (exception) {
        console.error(\`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setWindowSystemBarEnable(deprecated)

setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void

Sets whether to show the main window's status bar and bottom navigation (which may appear as a navigation bar or a three-button navigation bar depending on user settings). The display of the status bar and bottom navigation is controlled by status, and the navigation parameter does not have any impact. This API uses an asynchronous callback to return the result.

From API version 12, This API cannot be called for 2-in-1 devices. For other devices, the calling does not take effect immediately in split-screen mode (window.WindowStatusType.SPLIT\_SCREEN mode), floating window mode (window.WindowStatusType.FLOATING mode), or freeform window mode (you can open the mode by touching the Free windows button in Control Panel), but takes effect only on the main window displayed in full-screen mode.

The return value does not indicate that the status bar and Bottom navigation area are shown or hidden. This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/YRywKXyAQnyeBBRAwnZgug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6EA8C1389C1787DEFD2D9136CC04F46483DF7CE4457AB6D4E264F8C14BB5AD3)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [setWindowSystemBarEnable()](#setwindowsystembarenable9) in promise mode instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| names | Array<'status'|'navigation'> | Yes | 
Whether to show the status bar and Bottom navigation area in full-screen mode.

For example, to show all of them, set this parameter to **\['status', 'navigation'\]**; to hide them, set this parameter to **\[\]**.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// The following assumes that all of them are hidden.
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = \[\];
      try {
        windowClass.setWindowSystemBarEnable(names, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(\`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}\`);
            return;
          }
          console.info('Succeeded in setting the system bar to be invisible.');
        });
      } catch (exception) {
        console.error(\`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### setWindowLayoutFullScreen(deprecated)

setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void

Sets whether the main window layout or the child window layout is immersive. This API uses an asynchronous callback to return the result. It does not work when called by a system window.

An immersive layout means that the layout does not avoid the status bar or Bottom navigation area, and components may overlap with them.

A non-immersive layout means that the layout avoids the status bar and Bottom navigation area, and components do not overlap with them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/FiwHIH67TUekvlVoolCaFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D40FC8953802CDDEA6E93B6AEC8C64D8978EC994BDE27251E5C6FC834D94B059)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen9) in promise mode instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Device behavior differences**

In versions earlier than HarmonyOS 5.0.2, this API can be called properly on all devices.

Since HarmonyOS 5.0.2, calls to this API do not take effect or return an error on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. On a device that supports freeform windows but is not in the freeform window state, or on a device that does not support freeform windows, this API can be properly called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLayoutFullScreen | boolean | Yes | Whether the layout of the window is immersive. (In immersive layout mode, the status bar and Bottom navigation area remain visible.) **true** if immersive, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen = true;
      try {
        windowClass.setWindowLayoutFullScreen(isLayoutFullScreen, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(\`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}\`);
            return;
          }
          console.info('Succeeded in setting the window layout to full-screen mode.');
        });
      } catch (exception) {
        console.error(\`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}\`);
      }
    });
  }
}

#### show(deprecated)

show(callback: AsyncCallback<void>): void

Shows this window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/t8coh_pbQ1uAy6mDwcDa5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90B6F61A2827018568324AE895C92E63840BDC4BCE48A5D990068DC5846D7379)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [showWindow()](#showwindow9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.show((err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to show the window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in showing the window.');
});

#### show(deprecated)

show(): Promise<void>

Shows this window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/p5_EjreBRYqBGe_lGyMMiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF26839951F8F9CAC67021EB9F44F8188ED7610B65E08FB9C0357D2A4D335B2B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [showWindow()](#showwindow9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.show();
promise.then(() => {
  console.info('Succeeded in showing the window.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to show the window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### destroy(deprecated)

destroy(callback: AsyncCallback<void>): void

Destroys this window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/rE_mouAGReiB9V-o5zrcMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC9C6B29395D9A3EC51CBAEE15E8E3B5D2F4978113E0E7A6432B90FDDFE0D301)

This API is supported since API version 7 and is deprecated since API version 9. You are advised to use [destroyWindow()](#destroywindow9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.destroy((err: BusinessError) => {
  const errCode: number = err.code;
  if (err.code) {
    console.error(\`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in destroying the window.');
});

#### destroy(deprecated)

destroy(): Promise<void>

Destroys this window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Lfsqvp_AQl6YUI440Srcuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A03624300A204DC68883991BDC131EFAE6E0C528CABD99863409EA013400CDD)

This method is supported since API version 7 and deprecated since API version 9. You are advised to use [destroyWindow()](#destroywindow9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.destroy();
promise.then(() => {
  console.info('Succeeded in destroying the window.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### moveTo(deprecated)

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

Moves this window. This API uses an asynchronous callback to return the result.

This operation is not supported in a window in full-screen mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/dEPlX15hRNy6RujujXIUFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05C536DA2E8EF523030B5B229212F63DAC31354201F7992120A3BB3E21F49A32)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [moveWindowTo()](#movewindowto9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Coordinate position along the x-axis to which the window is moved, measured in px. A positive value means the position is to the right of the x-axis origin; a negative value means it is to the left; the value **0** means it is at the x-axis origin. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Position of the window moved on the Y axis, in px. A positive value indicates that the window is moved to the lower side of the Y axis. A negative value indicates that the window is moved to the upper side of the Y axis. A value of 0 indicates that the window is moved to the origin of the X axis. The value must be an integer. Non-integer values are rounded down. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.moveTo(300, 300, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in moving the window.');
});

#### moveTo(deprecated)

moveTo(x: number, y: number): Promise<void>

Moves this window. This API uses a promise to return the result.

This operation is not supported in a window in full-screen mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/5A9mAs8vQ3mtZIoXRfsIcA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43435D9FAAAC4B8D9523E14D8DF03EF0DCC9F7C85A44E5838279C79C203A1A65)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [moveWindowTo()](#movewindowto9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Coordinate position along the x-axis to which the window is moved, measured in px. A positive value means the position is to the right of the x-axis origin; a negative value means it is to the left; the value **0** means it is at the x-axis origin. The value must be an integer. Non-integer values are rounded down. |
| y | number | Yes | Coordinate position along the y-axis to which the window is moved, measured in px. A positive value means the position is below the y-axis origin; a negative value means it is above; the value **0** means it is at the y-axis origin. The value must be an integer. Non-integer values are rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.moveTo(300, 300);
promise.then(() => {
  console.info('Succeeded in moving the window.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to move the window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### resetSize(deprecated)

resetSize(width: number, height: number, callback: AsyncCallback<void>): void

Changes the size of this window based on the top-left vertex of the window. This API uses an asynchronous callback to return the result.

The main window and child window have the following default size limits: \[320, 1920\] in width and \[240, 1920\] in height, both in units of vp.

The minimum width and height of the main window and child window of the application depends on the configuration on the product side. You can call [getWindowLimits](#getwindowlimits11) to obtain size limits.

The system window has the following size limits: (0, 1920\] in width and (0, 1920\] in height, both in units of vp.

The new window width and height you set must meet the following limits:

If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect.

If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect.

This operation is not supported in a window in full-screen mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/kuq3nqo4RwWzon4rtV-u4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BBCFA74DD6BDD25DE1F6E6BA46AB9780EEE3FF7B05820667AC73BE1721FC732)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [resize()](#resize9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | New width of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. Negative values are invalid, resulting in error code [401](../../../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed). |
| height | number | Yes | New height of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. Negative values are invalid, resulting in error code [401](../../../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.resetSize(500, 1000, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in changing the window size.');
});

#### resetSize(deprecated)

resetSize(width: number, height: number): Promise<void>

Changes the size of this window based on the top-left vertex of the window. This API uses a promise to return the result.

The main window and child window have the following default size limits: \[320, 1920\] in width and \[240, 1920\] in height, both in units of vp.

The minimum width and height of the main window and child window of the application depends on the configuration on the product side. You can call [getWindowLimits](#getwindowlimits11) to obtain size limits.

The system window has the following size limits: (0, 1920\] in width and (0, 1920\] in height, both in units of vp.

The new window width and height you set must meet the following limits:

If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect.

If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect.

This operation is not supported in a window in full-screen mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fCXYMAuOQVShcd2VWJdCQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=943D20B057DA58EC3D53AF8A7CB9D391B5D74839D8E62815CD4C196483A26865)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [resize()](#resize9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | New width of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. Negative values are invalid, resulting in error code [401](../../../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed). |
| height | number | Yes | New height of the window, in px. The value must be an integer. If a floating-point number is passed in, the value is rounded down. Negative values are invalid, resulting in error code [401](../../../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.resetSize(500, 1000);
promise.then(() => {
  console.info('Succeeded in changing the window size.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to change the window size. Cause code: ${err.code}, message: ${err.message}\`);
});

#### getProperties(deprecated)

getProperties(callback: AsyncCallback<WindowProperties>): void

Obtains the properties of this window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/HDT7-g5yR-aW7UbUMyYlGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A12766A29CA619B31175270D071445147CF6FDEFBE6281C9A5AC6580D3D2B421)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getWindowProperties()](#getwindowproperties9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WindowProperties](../interfaces-others/document.md#windowproperties)\> | Yes | Callback used to return the window properties. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.getProperties((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to obtain the window properties. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in obtaining the window properties. Data: ' + JSON.stringify(data));
});

#### getProperties(deprecated)

getProperties(): Promise<WindowProperties>

Obtains the properties of this window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PucKHZggRBGwsoe763JklA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A20E81FC173FB7DBA646CADA0681AA451AB9CE1ED61FCDFF481D08CB4BF3251)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getWindowProperties()](#getwindowproperties9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WindowProperties](../interfaces-others/document.md#windowproperties)\> | Promise used to return the window properties. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.getProperties();
promise.then((data) => {
  console.info('Succeeded in obtaining the window properties. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the window properties. Cause code: ${err.code}, message: ${err.message}\`);
});

#### getAvoidArea(deprecated)

getAvoidArea(type: [AvoidAreaType](../enums/document.md#avoidareatype7), callback: AsyncCallback<[AvoidArea](../interfaces-others/document.md#avoidarea7)\>): void

Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area, and soft keyboard area. This API uses an asynchronous callback to return the result.

Main window/Subwindow:

-   In the free-floating window mode under the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state (the window mode is **window.WindowStatusType.FLOATING**), only the avoid area of the fixed soft keyboard type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_KEYBOARD**) is available.
-   In the free-floating window mode of the main window in the non-freeform window state, only the avoid area of the system bar type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_SYSTEM**) is available.
-   In other scenarios, the main window can obtain the avoid area calculated by this API only when it is not in the floating window mode or the device type is phone or tablet. Otherwise, the obtained avoid area is empty.
-   In non-freeform window state or non-floating window mode, the child window can obtain the avoid area calculated by this API only when its position and size are the same as those of the main window. Otherwise, the obtained avoid area is empty.

Global floating window, modal window, or system window:

-   This API can be called to obtain the avoid area only after [setSystemAvoidAreaEnabled](#setsystemavoidareaenabled18) is called. Otherwise, the obtained avoid area is empty.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/xmsiss9MR5Co-RJUFRBC9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EEA666F1F78E073C06242FD96B8698B2EED92DAC397DF4F94C130751190B75F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getWindowAvoidArea()](#getwindowavoidarea9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AvoidAreaType](../enums/document.md#avoidareatype7) | Yes | Type of the avoid area. |
| callback | AsyncCallback<[AvoidArea](../interfaces-others/document.md#avoidarea7)\> | Yes | Callback used to return the result. The avoid area for window content is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let type = window.AvoidAreaType.TYPE\_SYSTEM;
windowClass.getAvoidArea(type, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to obtain the area. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in obtaining the area. Data:' + JSON.stringify(data));
});

#### getAvoidArea(deprecated)

getAvoidArea(type: [AvoidAreaType](../enums/document.md#avoidareatype7)): Promise<[AvoidArea](../interfaces-others/document.md#avoidarea7)\>

Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area, and soft keyboard area. This API uses an asynchronous callback to return the result.

Main window/Subwindow:

-   In the free-floating window mode under the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state (the window mode is **window.WindowStatusType.FLOATING**), only the avoid area of the fixed soft keyboard type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_KEYBOARD**) is available.
-   In the free-floating window mode of the main window in the non-freeform window state, only the avoid area of the system bar type ([AvoidAreaType](../enums/document.md#avoidareatype7) is **TYPE\_SYSTEM**) is available.
-   In other scenarios, the main window can obtain the avoid area calculated by this API only when it is not in the floating window mode or the device type is phone or tablet. Otherwise, the obtained avoid area is empty.
-   In non-freeform window state or non-floating window mode, the child window can obtain the avoid area calculated by this API only when its position and size are the same as those of the main window. Otherwise, the obtained avoid area is empty.

Global floating window, modal window, or system window:

-   This API can be called to obtain the avoid area only after [setSystemAvoidAreaEnabled](#setsystemavoidareaenabled18) is called. Otherwise, the obtained avoid area is empty.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/oH5kBoIBQxK6Zv0n2EzDEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F09007695E1738C5D3207DCA06C863CC40BFBDD9E1DAB55AA185ED850F7ACBC0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getWindowAvoidArea()](#getwindowavoidarea9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AvoidAreaType](../enums/document.md#avoidareatype7) | Yes | Type of the avoid area. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AvoidArea](../interfaces-others/document.md#avoidarea7)\> | Promise used to return the result. The avoid area for window content is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let type = window.AvoidAreaType.TYPE\_SYSTEM;
let promise = windowClass.getAvoidArea(type);
promise.then((data) => {
  console.info('Succeeded in obtaining the area. Data:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the area. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setFullScreen(deprecated)

setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void

Sets whether the main window or the child window is in full-screen mode. This API uses an asynchronous callback to return the result.

Full-screen mode means that the layout does not avoid the status bar or Bottom navigation area, and components may overlap with them.

Non-full-screen mode means that the layout avoids the status bar and Bottom navigation area, and components do not overlap with them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/JREvGS__QHmvXkH17r5YwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA079AC9528D9E86724E197E3371B6060A8AFACF1F4F8C898F2FB863D3398529)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowSystemBarEnable()](#setwindowsystembarenable9) and [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen9) to implement the full-screen mode.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFullScreen | boolean | Yes | Whether to set full-screen mode (full-screen mode affects the display of the status bar and Bottom navigation area). **true** to set full-screen mode, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let isFullScreen: boolean = true;
      windowClass.setFullScreen(isFullScreen, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to enable the full-screen mode. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeeded in enabling the full-screen mode.');
      });
    });
  }
}

#### setFullScreen(deprecated)

setFullScreen(isFullScreen: boolean): Promise<void>

Sets whether the main window or the child window is in full-screen mode. This API uses a promise to return the result.

Full-screen mode means that the layout does not avoid the status bar or Bottom navigation area, and components may overlap with them.

Non-full-screen mode means that the layout avoids the status bar and Bottom navigation area, and components do not overlap with them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/zfRpgnIcSl6PZyVvC2lYeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9787E0F16E62F56C0898C4B43FB8E372F4B8B1E8B7EF889E7E76E3AFC94E5AF)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowSystemBarEnable()](#setwindowsystembarenable9) and [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen9) to implement the full-screen mode.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFullScreen | boolean | Yes | Whether to set full-screen mode (full-screen mode affects the display of the status bar and Bottom navigation area). **true** to set full-screen mode, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let isFullScreen: boolean = true;
      let promise = windowClass.setFullScreen(isFullScreen);
      promise.then(() => {
        console.info('Succeeded in enabling the full-screen mode.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to enable the full-screen mode. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
}

#### setLayoutFullScreen(deprecated)

setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void

Sets whether the main window layout or the child window layout is immersive. This API uses an asynchronous callback to return the result.

An immersive layout means that the layout does not avoid the status bar or Bottom navigation area, and components may overlap with them.

A non-immersive layout means that the layout avoids the status bar and Bottom navigation area, and components do not overlap with them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Or9x8LtxSRCI17tvZT-MeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E809FCDA40153BD922FC7A28CA38F26C4D516AEC7F93CC67E7E2286CC4DBF5D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLayoutFullScreen | boolean | Yes | Whether the layout of the window is immersive. (Immersive layout mode does not affect the display of the status bar and Bottom navigation area.) **true** if immersive, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen: boolean = true;
      windowClass.setLayoutFullScreen(isLayoutFullScreen, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeeded in setting the window layout to full-screen mode.');
      });
    });
  }
}

#### setLayoutFullScreen(deprecated)

setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>

Sets whether the main window layout or the child window layout is immersive. This API uses a promise to return the result.

An immersive layout means that the layout does not avoid the status bar or Bottom navigation area, and components may overlap with them.

A non-immersive layout means that the layout avoids the status bar and Bottom navigation area, and components do not overlap with them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/b00HI1SPTt2xTeYFjSPf9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FF11983A7D1F229ADB449D73FA21E6F7820F1101B5B4EFAA29F984A683E00FE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLayoutFullScreen | boolean | Yes | Whether the layout of the window is immersive. (Immersive layout mode does not affect the display of the status bar and Bottom navigation area.) **true** if immersive, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen: boolean = true;
      let promise = windowClass.setLayoutFullScreen(isLayoutFullScreen);
      promise.then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
}

#### setSystemBarEnable(deprecated)

setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void

Sets whether to show the main window's status bar and bottom navigation (which may appear as a navigation bar or a three-button navigation bar depending on user settings). The display of the status bar and bottom navigation is controlled by status, and the navigation parameter does not have any impact. This API uses an asynchronous callback to return the result.

From API version 12, This API cannot be called for 2-in-1 devices. For other devices, the calling does not take effect immediately in split-screen mode (window.WindowStatusType.SPLIT\_SCREEN mode), floating window mode (window.WindowStatusType.FLOATING mode), or freeform window mode (you can open the mode by touching the Free windows button in Control Panel), but takes effect only on the main window displayed in full-screen mode.

The return value does not indicate that the status bar and Bottom navigation area are shown or hidden. This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/k5fnAcB3TtSzWwGI4_21hQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D37C577830ABA1B55D0D86CEE5C73F261000300E25144AB42B297E34AA91F97B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowSystemBarEnable()](#setwindowsystembarenable9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| names | Array<'status'|'navigation'> | Yes | 
Whether to show the status bar and Bottom navigation area in full-screen mode.

For example, to show all of them, set this parameter to **\['status', 'navigation'\]**; to hide them, set this parameter to **\[\]**.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

// The following assumes that all of them are hidden.
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = \[\];
      windowClass.setSystemBarEnable(names, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeeded in setting the system bar to be invisible.');
      });
    });
  }
}

#### setSystemBarEnable(deprecated)

setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>

Sets whether to show the main window's status bar and bottom navigation (which may appear as a navigation bar or a three-button navigation bar depending on user settings). The display of the status bar and bottom navigation is controlled by status, and the navigation parameter does not have any impact. This API uses a promise to return the result.

From API version 12, This API cannot be called for 2-in-1 devices. For other devices, the calling does not take effect immediately in split-screen mode (window.WindowStatusType.SPLIT\_SCREEN mode), floating window mode (window.WindowStatusType.FLOATING mode), or freeform window mode (you can open the mode by touching the Free windows button in Control Panel), but takes effect only on the main window displayed in full-screen mode.

The return value does not indicate that the status bar and Bottom navigation area are shown or hidden. This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/xBP-iIbnQSSkBtCSrAU72A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6F437AD26F17A71BD2A5A33EC415D13860105ABA4898D87091BEEF46C41B666)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowSystemBarEnable()](#setwindowsystembarenable9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| names | Array<'status'|'navigation'> | Yes | 
Whether to show the status bar and Bottom navigation area in full-screen mode.

For example, to show all of them, set this parameter to **\['status', 'navigation'\]**; to hide them, set this parameter to **\[\]**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// The following assumes that all of them are hidden.
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let names: Array<'status' | 'navigation'> = \[\];
      let promise = windowClass.setSystemBarEnable(names);
      promise.then(() => {
        console.info('Succeeded in setting the system bar to be invisible.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
}

#### setSystemBarProperties(deprecated)

setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void

Sets the properties of the status bar of the main window. This API uses an asynchronous callback to return the result. This API cannot be called for 2-in-1 devices. For other devices, the calling does not take effect immediately in split-screen mode (window.WindowStatusType.SPLIT\_SCREEN mode), floating window mode (window.WindowStatusType.FLOATING mode), or freeform window mode (you can open the mode by touching the Free windows button in Control Panel), but takes effect only on the main window displayed in full-screen mode.

This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/f9qXSvB5RHCdvRapg5Nlnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92863CE484D84DE66E375DA656430AED020B45BA35BC62E4CC6801F9C698A423)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowSystemBarProperties()](#setwindowsystembarproperties9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| systemBarProperties | [SystemBarProperties](../interfaces-others/document.md#systembarproperties) | Yes | three-button navigation bar and |
| status bar. |  |  |  |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        // The following properties are supported since API version 8.
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      windowClass.setSystemBarProperties(SystemBarProperties, (err) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(\`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeeded in setting the system bar properties.');
      });
    });
  }
}

#### setSystemBarProperties(deprecated)

setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>

Sets the properties of the status bar of the main window. This API uses a promise to return the result. This API cannot be called for 2-in-1 devices. For other devices, the calling does not take effect immediately in split-screen mode (window.WindowStatusType.SPLIT\_SCREEN mode), floating window mode (window.WindowStatusType.FLOATING mode), or freeform window mode (you can open the mode by touching the Free windows button in Control Panel), but takes effect only on the main window displayed in full-screen mode.

This API does not take effect when it is called by a child window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/jxOa50fRRJSWGr8E4ExrVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B5D885955BDC639D4F66747D6E680D6B4412A435282E7A934F44C2BDAFCB0E8)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowSystemBarProperties()](#setwindowsystembarproperties9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| systemBarProperties | [SystemBarProperties](../interfaces-others/document.md#systembarproperties) | Yes | three-button navigation bar and |
| status bar. |  |  |  |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        return;
      }
      windowClass = data;
      let SystemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        // The following properties are supported since API version 8.
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#00ffff'
      };
      let promise = windowClass.setSystemBarProperties(SystemBarProperties);
      promise.then(() => {
        console.info('Succeeded in setting the system bar properties.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}\`);
      });
    });
  }
}

#### loadContent(deprecated)

loadContent(path: string, callback: AsyncCallback<void>): void

Loads content from a page to this window. This API uses an asynchronous callback to return the result.

You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/-3j2UAJQTn210fk6O2h95Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81A133475C027567B31836CDEA6466FB38C3BB4B151394AE25F174356899DE11)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setUIContent()](#setuicontent9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page content which needs to be loaded to the window. In the stage model, the path needs to be configured in the **main\_pages.json** file of the project. In the FA model, the path needs to be configured in the **config.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main\_pages.json** or **config.json** file. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.loadContent('pages/page2/page3', (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in loading the content.');
});

#### loadContent(deprecated)

loadContent(path: string): Promise<void>

Loads content from a page to this window. This API uses a promise to return the result.

You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/P19Nlj41TFe5AUOdlXlE9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=911F37CEF337DBABEA659E2CE3BB559DDBB17BF179C241B224554805214DFCDB)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setUIContent()](#setuicontent9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page from which the content will be loaded. In the stage model, the path is configured in the **main\_pages.json** file of the project. In the FA model, the path is configured in the **config.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main\_pages.json** or **config.json** file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.loadContent('pages/page2/page3');
promise.then(() => {
  console.info('Succeeded in loading the content.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to load the content. Cause code: ${err.code}, message: ${err.message}\`);
});

#### isShowing(deprecated)

isShowing(callback: AsyncCallback<boolean>): void

Checks whether this window is displayed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/99d7IwpwQ3uYEiqghXJEsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25346779E8275BDD1AE8782AE6A3044808B96399171C4F6AB2A9051391C47350)

This method is supported since API version 7 and deprecated since API version 9. You are advised to use [isWindowShowing()](#iswindowshowing9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if the window is displayed, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.isShowing((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to check whether the window is showing. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
});

#### isShowing(deprecated)

isShowing(): Promise<boolean>

Checks whether this window is displayed. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/dJ30mnvRTe26JoZBlfFr1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=692E6B9DE5F0BE9BE45FA9AED9DA40F4C17280F4791731D31CA4E7A77BF9D872)

This method is supported since API version 7 and deprecated since API version 9. You are advised to use [isWindowShowing()](#iswindowshowing9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if the window is displayed, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.isShowing();
promise.then((data) => {
  console.info('Succeeded in checking whether the window is showing. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to check whether the window is showing. Cause code: ${err.code}, message: ${err.message}\`);
});

#### on('systemAvoidAreaChange')(deprecated)

on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void

Subscribes to events indicating changes to the system avoid area of the current window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/HvFwXy1vQDu0hh5JtI-EuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BC799EDD037DB52A50A860BC857B9B608109B5CAC207DFE1A92DD0CE2AA618D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [on('avoidAreaChange')](#onavoidareachange9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'systemAvoidAreaChange'**, indicating the system avoid area change event. |
| callback | Callback<[AvoidArea](../interfaces-others/document.md#avoidarea7)\> | Yes | Callback used to return the result. The current avoid area is returned. |

**Example**

windowClass.on('systemAvoidAreaChange', (data) => {
  console.info('Succeeded in enabling the listener for system avoid area changes. Data: ' + JSON.stringify(data));
});

#### off('systemAvoidAreaChange')(deprecated)

off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void

Unsubscribes from the events indicating changes to the system avoid area of the current window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WZ-lBLy0T9OtjZsM6hYtZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B1B6AC2DE323175C257549B6AB816285588F4A337A830F84C0F685240F650A1)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [off('avoidAreaChange')](#offavoidareachange9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'systemAvoidAreaChange'**, indicating the system avoid area change event. |
| callback | Callback<[AvoidArea](../interfaces-others/document.md#avoidarea7)\> | No | Callback used to return the result. The current avoid area is returned. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to system avoid area change events are canceled. |

**Example**

const callback = (avoidArea: window.AvoidArea) => {
  // ...
}
windowClass.on('systemAvoidAreaChange', callback);
windowClass.off('systemAvoidAreaChange', callback);
// Unregister all the callbacks that have been registered through on().
windowClass.off('systemAvoidAreaChange');

#### isSupportWideGamut(deprecated)

isSupportWideGamut(callback: AsyncCallback<boolean>): void

Checks whether this window supports the wide-gamut color space. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/vcKczC5eQ2afUm3u8PywEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=960B7F82C4819F9E214E7F406DAD67FF22CD3B3774FAE14851311ECF92B7C26E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isWindowSupportWideGamut()](#iswindowsupportwidegamut9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if the wide-gamut color space is supported, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.isSupportWideGamut((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in checking whether the window support WideGamut Data: ' + JSON.stringify(data));
});

#### isSupportWideGamut(deprecated)

isSupportWideGamut(): Promise<boolean>

Checks whether this window supports the wide-gamut color space. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/jdUYjZrIT7mFq845h0dWlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEA16E7A9F7C627D98CE91C401CE90A47B6498C88131FE43FCA686652BF48A43)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isWindowSupportWideGamut()](#iswindowsupportwidegamut9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if the wide-gamut color space is supported, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.isSupportWideGamut();
promise.then((data) => {
  console.info('Succeeded in checking whether the window support WideGamut. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to check whether the window support WideGamut. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setColorSpace(deprecated)

setColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void

Sets a color space for this window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/XbrZeAtDQf6yGFpkvF9K5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62812DB987BA05F9F2EFBB18F1992071BA78E9261B6E634141F0CBE0E6B3C072)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [setWindowColorSpace()](#setwindowcolorspace9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [ColorSpace](../enums/document.md#colorspace8) | Yes | Color space to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.setColorSpace(window.ColorSpace.WIDE\_GAMUT, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting window colorspace.');
});

#### setColorSpace(deprecated)

setColorSpace(colorSpace:ColorSpace): Promise<void>

Sets a color space for this window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/4km79vdHSpeHmXLqSHYyyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=495A08633F3822B40AE8F790FD1371DA5951969A9F0B8AEE4B960A26C6CDC627)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [setWindowColorSpace()](#setwindowcolorspace9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [ColorSpace](../enums/document.md#colorspace8) | Yes | Color space to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.setColorSpace(window.ColorSpace.WIDE\_GAMUT);
promise.then(() => {
  console.info('Succeeded in setting window colorspace.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set window colorspace. Cause code: ${err.code}, message: ${err.message}\`);
});

#### getColorSpace(deprecated)

getColorSpace(callback: AsyncCallback<ColorSpace>): void

Obtains the color space of this window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/zb-MsLovT7yQyNsAAE7Kmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7C5944A304A9CFF78D05788BAA8D6B2947B5A6B832295791F01BA7C48A0FCAA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getWindowColorSpace()](#getwindowcolorspace9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ColorSpace](../enums/document.md#colorspace8)\> | Yes | Callback used to return the result. When the color space is obtained successfully, **err** is **undefined**, and **data** is the current color space. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.getColorSpace((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to get window colorspace. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting window colorspace. Cause:' + JSON.stringify(data));
});

#### getColorSpace(deprecated)

getColorSpace(): Promise<ColorSpace>

Obtains the color space of this window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/QlORdIT7TreheC09rtLzWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42BE597DDBC7F49FA4AF2494E8DBEE38490378997266290380E14BCBE9D0349E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getWindowColorSpace()](#getwindowcolorspace9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ColorSpace](../enums/document.md#colorspace8)\> | Promise used to return the current color space. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.getColorSpace();
promise.then((data) => {
  console.info('Succeeded in getting window color space. Cause:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to get window colorspace. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setBackgroundColor(deprecated)

setBackgroundColor(color: string, callback: AsyncCallback<void>): void

Sets the background color for this window. This API uses an asynchronous callback to return the result. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/DqD-T9METZuUOcbi4krknw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFEB703DC6887BFEA7A76C73E413363131A148CD131A1249A85F02CE41F76055)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowBackgroundColor()](#setwindowbackgroundcolor9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | string | Yes | Background color to set. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let color: string = '#00ff33';
windowClass.setBackgroundColor(color, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the background color. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the background color.');
});

#### setBackgroundColor(deprecated)

setBackgroundColor(color: string): Promise<void>

Sets the background color for this window. This API uses a promise to return the result. In the stage model, this API must be used after the call of [loadContent](#loadcontent9) or [setUIContent()](#setuicontent9) takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/G8HQqtE2RIer-SpkkVtyWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7549992433EA647FDE049016BC11ADA3ED5F952C2AD515081060C09A2657BFC1)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowBackgroundColor()](#setwindowbackgroundcolor9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | string | Yes | Background color to set. The value is a hexadecimal RGB or ARGB color code and is case insensitive, for example, **'#00FF00'** or **'#FF00FF00'**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let color: string = '#00ff33';
let promise = windowClass.setBackgroundColor(color);
promise.then(() => {
  console.info('Succeeded in setting the background color.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the background color. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setBrightness(deprecated)

setBrightness(brightness: number, callback: AsyncCallback<void>): void

Sets the screen brightness for this window. This API uses an asynchronous callback to return the result.

When the screen brightness setting for the window takes effect, Control Panel cannot adjust the system screen brightness. It can do so only after the window screen brightness is restored to the default value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/wli6FovLR_2uFdeLTQEuaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=683B997B05FAC4385D4D579F8EA6D904A5658A60643F970BAC203707F6121729)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowBrightness()](#setwindowbrightness9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | number | Yes | Brightness to set. The value is a floating-point number in the range \[0.0, 1.0\] or is set to **\-1.0**. The value **1.0** means the brightest, and **\-1.0** means that the window brightness resets to the original brightness set through Control Panel. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let brightness: number = 1;
windowClass.setBrightness(brightness, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the brightness.');
});

#### setBrightness(deprecated)

setBrightness(brightness: number): Promise<void>

Sets the screen brightness for this window. This API uses a promise to return the result.

When the screen brightness setting for the window takes effect, Control Panel cannot adjust the system screen brightness. It can do so only after the window screen brightness is restored to the default value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/pdNEp4lRTZGUR_2Gmb_37w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61B32FF08250DB15FFFB6149DACFFAE2CDD1F839283D9F21C338D7C342A85588)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowBrightness()](#setwindowbrightness9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | number | Yes | Brightness to set. The value is a floating-point number in the range \[0.0, 1.0\] or is set to **\-1.0**. The value **1.0** means the brightest, and **\-1.0** means that the window brightness resets to the original brightness set through Control Panel. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let brightness: number = 1;
let promise = windowClass.setBrightness(brightness);
promise.then(() => {
  console.info('Succeeded in setting the brightness.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setDimBehind(deprecated)

setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void

Sets the dimness of the window that is not on top. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/mE_EHpNYSBemVq5zCv-C4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBD66FEB7CCC69CADEE1DD1D433212D874047F8389512CFD96B7CE9CE8BB0431)

This API cannot be used. This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dimBehindValue | number | Yes | Dimness of the window to set. The value range is \[0.0, 1.0\], and the value **1.0** means the dimmest. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.setDimBehind(0.5, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the dimness. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the dimness.');
});

#### setDimBehind(deprecated)

setDimBehind(dimBehindValue: number): Promise<void>

Sets the dimness of the window that is not on top. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/2HpqcPHeR2Kr93-SiP9Rlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFD0249851BC2DC0DF4D8BBE9C022DA293E9782F03DEFF59F4D13F73F5703915)

This API cannot be used. This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dimBehindValue | number | Yes | Dimness of the window to set. The value ranges from 0 to 1. The value **1** indicates the dimmest. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.setDimBehind(0.5);
promise.then(() => {
  console.info('Succeeded in setting the dimness.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the dimness. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setFocusable(deprecated)

setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void

Sets whether this window is focusable, that is, whether the window can gain focus after it is being operated or using other methods. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/igVXbTfqT8aNg_00iEWRGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=755DBD1DF9C6FF12DB102F1208257462EAFD7E6EAC951411DAC7EFE437F47F79)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowFocusable()](#setwindowfocusable9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFocusable | boolean | Yes | Whether the window is focusable. **true** if focusable, **false** otherwise. If this parameter is set to **false**, the window cannot bind to an input method or receive keyboard events. If input logic needs to be processed, follow the instructions provided in [Input Box and Input Method Interaction in Non-Focus Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
windowClass.setFocusable(isFocusable, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the window to be focusable.');
});

#### setFocusable(deprecated)

setFocusable(isFocusable: boolean): Promise<void>

Sets whether this window is focusable, that is, whether the window can gain focus after it is being clicked or using other methods. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/gVzDd9j2QN6rTZQUcXlPOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2C601AF71D6DCDA373485056330520300C020274171C228B85EC526127AED66)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowFocusable()](#setwindowfocusable9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isFocusable | boolean | Yes | Whether the window is focusable. **true** if focusable, **false** otherwise. If this parameter is set to **false**, the window cannot bind to an input method or receive keyboard events. If input logic needs to be processed, follow the instructions provided in [Input Box and Input Method Interaction in Non-Focus Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isFocusable: boolean = true;
let promise = windowClass.setFocusable(isFocusable);
promise.then(() => {
  console.info('Succeeded in setting the window to be focusable.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the window to be focusable. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setKeepScreenOn(deprecated)

setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void

Sets whether to keep the screen always on. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CXh1973VRIe5-B537eG6NQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67546711460FCFA955FE08AF5B086613E31845882508DC20EFE16FC42C2B754F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowKeepScreenOn()](#setwindowkeepscreenon9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isKeepScreenOn | boolean | Yes | Whether to keep the screen always on. **true** to keep the screen always on, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
windowClass.setKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the screen to be always on.');
});

#### setKeepScreenOn(deprecated)

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

Sets whether to keep the screen always on. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/usmMGlTMSau4w1N2F4Crxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5736CC11CC0893CB1D02AABEF921FDF0A389A512A95563325A64F1594FA312BA)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setWindowKeepScreenOn()](#setwindowkeepscreenon9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isKeepScreenOn | boolean | Yes | Whether to keep the screen always on. **true** to keep the screen always on, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isKeepScreenOn: boolean = true;
let promise = windowClass.setKeepScreenOn(isKeepScreenOn);
promise.then(() => {
  console.info('Succeeded in setting the screen to be always on.');
}).catch((err: BusinessError) => {
  console.info(\`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setOutsideTouchable(deprecated)

setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void

Sets whether the area outside the child window is touchable. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ZClM5fESQ3SKfCOkfyHU2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92F4E5D1B4F4439083975C55C139C667C841481B13A1049294592597997BBC0E)

This API is supported since API version 7 and deprecated since API version 9.

Starting from API version 9, the area outside the child window is touchable by default. This API is no longer supported and no substitute API is provided.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| touchable | boolean | Yes | Whether the area outside the child window is touchable. **true** if touchable, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

windowClass.setOutsideTouchable(true, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the area to be touchable. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the area to be touchable.');
});

#### setOutsideTouchable(deprecated)

setOutsideTouchable(touchable: boolean): Promise<void>

Sets whether the area outside the child window is touchable. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/6JD8m5IwQPC24npgOmJBaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1A6887B93A4ADA52EF887C342FD83064E007E8BFE57070F38383958C4C712DC)

This API is supported since API version 7 and deprecated since API version 9.

Starting from API version 9, the area outside the child window is touchable by default. This API is no longer supported and no substitute API is provided.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| touchable | boolean | Yes | Whether the area outside the child window is touchable. **true** if touchable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = windowClass.setOutsideTouchable(true);
promise.then(() => {
  console.info('Succeeded in setting the area to be touchable.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the area to be touchable. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setPrivacyMode(deprecated)

setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

Sets whether this window is in privacy mode. This API uses an asynchronous callback to return the result. A window in privacy mode cannot be captured or recorded. This API can be used in scenarios where screen capture or recording is disabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/X0o8eBJZSF-71ES2FpaBLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72320CDDEF46D07C30C2C799A60ABE5B134552ED227238429A8C9E82BB146924)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowPrivacyMode()](#setwindowprivacymode9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacyMode | boolean | Yes | Whether the window is in privacy mode. **true** if in privacy mode, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
windowClass.setPrivacyMode(isPrivacyMode, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the window to privacy mode.');
});

#### setPrivacyMode(deprecated)

setPrivacyMode(isPrivacyMode: boolean): Promise<void>

Sets whether this window is in privacy mode. This API uses a promise to return the result. A window in privacy mode cannot be captured or recorded. This API can be used in scenarios where screen capture or recording is disabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/f_GauV72QLK5srCy-XbpvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17C05F6DDF30A39B8584453A77659837D3C4AA356A0A6F759C86C0572F980DDC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowPrivacyMode()](#setwindowprivacymode9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacyMode | boolean | Yes | Whether the window is in privacy mode. **true** if in privacy mode, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isPrivacyMode: boolean = true;
let promise = windowClass.setPrivacyMode(isPrivacyMode);
promise.then(() => {
  console.info('Succeeded in setting the window to privacy mode.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the window to privacy mode. Cause code: ${err.code}, message: ${err.message}\`);
});

#### setTouchable(deprecated)

setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void

Sets whether this window is touchable. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/bqigF4I3TK-HjZ1DEedEVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2816D2F8EBA19F47E514BC67B660FA92EC2A43791121527B1341EABF73A05204)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowTouchable()](#setwindowtouchable9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTouchable | boolean | Yes | Whether the window is touchable. **true** if touchable, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable = true;
windowClass.setTouchable(isTouchable, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the window to be touchable.');
});

#### setTouchable(deprecated)

setTouchable(isTouchable: boolean): Promise<void>

Sets whether this window is touchable. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/5cGVtLPuTQ6II0GNFO4rZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7499BA3A20A4384192C1A088DD484C5800F07FCC84E94BA6952D9FBC93034156)

This method is supported since API version 7 and deprecated since API version 9. You are advised to use [setWindowTouchable()](#setwindowtouchable9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTouchable | boolean | Yes | Whether the window is touchable. **true** if touchable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let isTouchable = true;
let promise = windowClass.setTouchable(isTouchable);
promise.then(() => {
  console.info('Succeeded in setting the window to be touchable.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set the window to be touchable. Cause code: ${err.code}, message: ${err.message}\`);
});
