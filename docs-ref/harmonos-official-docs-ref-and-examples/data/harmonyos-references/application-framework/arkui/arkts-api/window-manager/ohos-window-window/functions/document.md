# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/wDsUcUuNRxytIVFKQfQEBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8E6C91DB41769E2048AE79952E982986DC764D72FB04A128C9614E5EAABA586)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For the system capability SystemCapability.Window.SessionManager, use [canIUse()](../../../../../../common-capabilities/arkts-api/syscap/document.md#caniuse) to check whether the device supports this system capability and the corresponding APIs.
    

#### Modules to Import

import { window } from '@kit.ArkUI';

#### window.createWindow9+

createWindow(config: Configuration, callback: AsyncCallback<Window>): void

Creates a child window or system window. This API uses an asynchronous callback to return the result.

In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the child window created uses an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout) by default.

In freeform window mode, the child window created uses an immersive layout when [decorEnabled](../interfaces-others/document.md#configuration9) is set to **false**, and it uses a non-immersive layout when this parameter is set to **true**.

**Required permissions**: ohos.permission.SYSTEM\_FLOAT\_WINDOW (required only when the window type is **window.WindowType.TYPE\_FLOAT**.)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [Configuration](../interfaces-others/document.md#configuration9) | Yes | Parameters used for creating the window. |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the window created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. createWindow can not work correctly due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |
| 1300006 | This window context is abnormal. |
| 1300009 | The parent window is invalid. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
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
        console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
        windowClass.resize(500, 1000);
      });
    } catch (exception) {
      console.error(\`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### window.createWindow9+

createWindow(config: Configuration): Promise<Window>

Creates a child window or system window. This API uses a promise to return the result.

In non-[freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) mode, the child window created uses an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout) by default.

In freeform window mode, the child window created uses an immersive layout when [decorEnabled](../interfaces-others/document.md#configuration9) is set to **false**, and it uses a non-immersive layout when this parameter is set to **true**.

**Required permissions**: ohos.permission.SYSTEM\_FLOAT\_WINDOW (required only when the window type is **window.WindowType.TYPE\_FLOAT**.)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [Configuration](../interfaces-others/document.md#configuration9) | Yes | Parameters used for creating the window. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the window created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. createWindow can not work correctly due to limited device capabilities. |
| 1300001 | Repeated operation. |
| 1300002 | This window state is abnormal. |
| 1300004 | Unauthorized operation. |
| 1300006 | This window context is abnormal. |
| 1300009 | The parent window is invalid. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    let config: window.Configuration = {
      name: "test",
      windowType: window.WindowType.TYPE\_DIALOG,
      ctx: this.context
    };
    try {
      window.createWindow(config).then((value:window.Window) => {
        console.info('Succeeded in creating the window. Data: ' + JSON.stringify(value));
        windowClass = value;
        windowClass.resize(500, 1000);
      }).catch((err:BusinessError)=> {
        console.error(\`Failed to create the window. Cause code: ${err.code}, message: ${err.message}\`);
      });
    } catch (exception) {
      console.error(\`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### window.findWindow9+

findWindow(name: string): Window

Finds a window based on the name.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Window name. When searching for a child window or system window, use the window name in [Configuration](../interfaces-others/document.md#configuration9). When searching for the main window, use [getWindowName](../../../ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getwindowname12) to obtain the window name of the current instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Window](../interface-window/document.md) | Window found. If the window with the specified name does not exist, an empty object is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. |

**Example**

let windowClass: window.Window | undefined = undefined;
try {
  windowClass = window.findWindow('test');
} catch (exception) {
  console.error(\`Failed to find the Window. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### window.getLastWindow9+

getLastWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void

Obtains the topmost layer child window of the current application. This API uses an asynchronous callback to return the result.

If no child window exists or the child window is not displayed by calling [showWindow()](../interface-window/document.md#showwindow9), the main window of the application is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current application context. |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the topmost layer window obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Top window or main window is null or destroyed. |
| 1300006 | This window context is abnormal. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      if (err.code) {
        console.error(\`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}\`);
      }
      windowStage.createSubWindow('TestSubWindow').then((subWindow) => {
        let storage: LocalStorage = new LocalStorage();
        subWindow.loadContent('pages/Index', storage, (err: BusinessError) => {
          if (err.code) {
            console.error(\`Failed to load content for sub window. Cause code: ${err.code}, message: ${err.message}\`);
          }
          subWindow.showWindow().then(() => {
            try {
              window.getLastWindow(this.context, (err: BusinessError, data) => {
                const errCode: number = err.code;
                if (errCode) {
                  console.error(\`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}\`);
                  return;
                }
                windowClass = data;
                console.info(\`Succeeded in obtaining the top window. Window id: ${windowClass.getWindowProperties().id}\`);
              });
            } catch (exception) {
              console.error(\`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}\`);
            }
          });
        });
      });
    });
  }
  // ...
}

#### window.getLastWindow9+

getLastWindow(ctx: BaseContext): Promise<Window>

Obtains the topmost layer child window of the current application. This API uses a promise to return the result.

If no child window exists or the child window is not displayed by calling [showWindow()](../interface-window/document.md#showwindow9), the main window of the application is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current application context. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the topmost layer window obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Top window or main window is null or destroyed. |
| 1300006 | This window context is abnormal. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      if (err.code) {
        console.error(\`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}\`);
      }
      windowStage.createSubWindow('TestSubWindow').then((subWindow) => {
        let storage: LocalStorage = new LocalStorage();
        subWindow.loadContent('pages/Index', storage, (err: BusinessError) => {
          if (err.code) {
            console.error(\`Failed to load content for sub window. Cause code: ${err.code}, message: ${err.message}\`);
          }
          subWindow.showWindow().then(() => {
            try {
              window.getLastWindow(this.context).then((topWindow) => {
                windowClass = topWindow;
                console.info(\`Succeeded in obtaining the top window. Window id: ${topWindow.getWindowProperties().id}\`);
              }).catch((err: BusinessError) => {
                console.error(\`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}\`);
              });
            } catch (exception) {
              console.error(\`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}\`);
            }
          });
        });
      });
    });
  }
  // ...
}

#### window.shiftAppWindowFocus11+

shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>

Shifts the window focus from the source window to the target window in the same application. The window focus can be shifted within the main window and child windows. This API uses a promise to return the result.

Ensure that the target window can gain focus (configurable by calling [setWindowFocusable()](../interface-window/document.md#setwindowfocusable9)) and that [showWindow()](../interface-window/document.md#showwindow9) has been successfully executed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/Osvc-zrlSbacfwqN5RUFUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=033E23F5AA3D2D74E56439518D56B370285C0E9CD8E6C6D792EAC5184D5EA872)

Before calling **shiftAppWindowFocus()**, ensure that the target window has called [loadContent()](../interface-window/document.md#loadcontent9) or [setUIContent()](../interface-window/document.md#setuicontent9) and these operations have been effective. Otherwise, an invisible window may gain focus, causing function exceptions or affecting user experience.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sourceWindowId | number | Yes | ID of the source window, which is having the focus. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the window ID. |
| targetWindowId | number | Yes | ID of the target window. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the window ID. |

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
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // ...
    console.info('onWindowStageCreate');
    let mainWindow: window.Window | undefined = undefined;
    let subWindow: window.Window | undefined = undefined;
    let mainWindowId: number = -1;
    let subWindowId: number = -1;

    try {
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          console.error(\`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}\`);
        }
        // Obtain the main window and ID of the application.
        windowStage.getMainWindow().then((data) => {
          if (data == null) {
            console.error('Failed to obtain the main window. Cause: The data is empty');
            return;
          }
          mainWindow = data;
          mainWindowId = mainWindow.getWindowProperties().id;
          console.info('Succeeded in obtaining the main window');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}\`);
        });

        // Create or obtain a child window and its ID. In this case, the child window has focus.
        windowStage.createSubWindow('testSubWindow').then((data) => {
          if (data == null) {
            console.error('Failed to obtain the sub window. Cause: The data is empty');
            return;
          }
          subWindow = data;
          subWindowId = subWindow.getWindowProperties().id;
          subWindow.resize(500, 500);
          subWindow.setUIContent('pages/Index');
          subWindow.showWindow();

          // Listen for the window status and ensure that the window is ready.
          subWindow.on("windowEvent", (windowEvent) => {
            if (windowEvent == window.WindowEventType.WINDOW\_ACTIVE) {
              // Switch the focus.
              window.shiftAppWindowFocus(subWindowId, mainWindowId).then(() => {
                console.info('Succeeded in shifting app window focus');
              }).catch((err: BusinessError) => {
                console.error(\`Failed to shift app window focus. Cause code: ${err.code}, message: ${err.message}\`);
              });
            }
          });
        });
      });
    } catch (exception) {
      console.error(\`Failed to shift app focus. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### window.shiftAppWindowPointerEvent15+

shiftAppWindowPointerEvent(sourceWindowId: number, targetWindowId: number): Promise<void>

Transfers a mouse input event from one window to another within the same application. This API takes effect only for the main window and its child windows. This API uses a promise to return the result.

To transfer mouse input events, the source window must call this API within the callback of the [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch) event (the event type must be **TouchType.Down**). After a successful call, the system sends a **TouchType.Up** event to the source window and a **TouchType.Down** event to the target window.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sourceWindowId | number | Yes | ID of the source window. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the window ID. |
| targetWindowId | number | Yes | ID of the target window. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the window ID. |

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

// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Blue)
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              try {
                let sourceWindowId = 1;
                let targetWindowId = 2;
                let promise = window.shiftAppWindowPointerEvent(sourceWindowId, targetWindowId);
                promise.then(() => {
                  console.info('Succeeded in shifting app window pointer event');
                }).catch((err: BusinessError) => {
                  console.error(\`Failed to shift app window pointer event. Cause code: ${err.code}, message: ${err.message}\`);
                });
              } catch (exception) {
                console.error(\`Failed to shift app pointer event. Cause code: ${exception.code}, message: ${exception.message}\`);
              }
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}

#### window.shiftAppWindowTouchEvent20+

shiftAppWindowTouchEvent(sourceWindowId: number, targetWindowId: number, fingerId: number): Promise<void>

Transfers a touchscreen input event from one window to another within the same application. This API takes effect only for the main window and its child windows. This API uses a promise to return the result.

To transfer touchscreen input events, the source window must call this API within the callback of the [onTouch](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#ontouch) event (the event type must be **TouchType.Down**). After a successful call, the system sends a **TouchType.Up** event to the source window and a **TouchType.Down** event to the target window.

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be called on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sourceWindowId | number | Yes | ID of the source window. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the window ID. The value must be an integer greater than 0. If it is less than or equal to 0, error code 1300016 is returned. |
| targetWindowId | number | Yes | ID of the target window. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the window ID. The value must be an integer greater than 0. If it is less than or equal to 0, error code 1300016 is returned. |
| fingerId | number | Yes | Unique ID of the finger in the touchscreen input event. You are advised to use the **touches** attribute in the [TouchEvent](../../../../arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent) object to obtain the ID. This parameter must be an integer greater than or equal to 0. If the value is less than 0, error code 1300016 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function shiftAppWindowTouchEvent can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |
| 1300004 | Unauthorized operation. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Blue)
          .onTouch((event: TouchEvent) => {
            // The source window touch event type must be TouchType.Down.
            if (event.type === TouchType.Down) {
              try {
                let sourceWindowId = 1;
                let targetWindowId = 2;
                let promise = window.shiftAppWindowTouchEvent(sourceWindowId, targetWindowId, event.touches\[0\].id);
                promise.then(() => {
                  console.info(\`Succeeded in shifting app window touch event\`);
                }).catch((err: BusinessError) => {
                  console.error(\`Failed to shift app window touch event. Cause code: ${err.code}, message: ${err.message}\`);
                });
              } catch (exception) {
                console.error(\`Failed to shift app touch event. Cause code: ${exception.code}, message: ${exception.message}\`);
              }
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}

#### window.getWindowsByCoordinate14+

getWindowsByCoordinate(displayId: number, windowNumber?: number, x?: number, y?: number): Promise<Array<Window>>

Obtains visible windows at the specified coordinates within the current application, sorted by their current layer order. The window at the topmost layer corresponds to index 0 of the array. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | ID of the display where the windows are located. The value must be an integer. If a non-integer is passed, the decimal part is ignored. The value can be obtained from [WindowProperties](../interfaces-others/document.md#windowproperties). |
| windowNumber | number | No | Number of windows to obtain. The value must be an integer greater than 0. If a non-integer is passed, the decimal part is ignored. If this parameter is not set or is less than or equal to 0, all windows that meet the conditions are returned. |
| x | number | No | X coordinate, with the top-left corner of the screen used as the origin. The value must be a non-negative integer. If a non-integer is passed, the decimal part is ignored. If this parameter is not set or is less than 0, all visible windows are returned. |
| y | number | No | Y coordinate, with the top-left corner of the screen used as the origin. The value must be a non-negative integer. If a non-integer is passed, the decimal part is ignored. If this parameter is not set or is less than 0, all visible windows are returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Window](../interface-window/document.md)\>> | Promise used to return an array of window objects. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    try {
      let displayId = 0;
      window.getWindowsByCoordinate(displayId, 2, 500, 500).then((data) => {
        console.info(\`Succeeded in getting windows. Data: ${data}\`);
        for (let windowObject of data) {
          // do something with window
          windowClass = windowObject;
        }
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}\`);
      });
    } catch (exception) {
      console.error(\`Failed to get window from point. Cause code: ${exception.code}, message: ${exception.message}\`);
    }
  }
}

#### window.getAllWindowLayoutInfo15+

getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>

Obtains an array of visible window layout information on the specified screen. The width and height of each returned Rect are the scaled values after calculation, arranged according to the current window hierarchy. The highest level corresponds to index 0 in the array. This operation uses **Promise** for asynchronous callbacks.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | ID of the display where the windows are located. The value must be an integer and can be obtained from [WindowProperties](../interfaces-others/document.md#windowproperties). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[WindowLayoutInfo](../interfaces-others/document.md#windowlayoutinfo15)\>> | Promise used to return an array of window layout information objects. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. function getAllWindowLayoutInfo can not work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  let promise = window.getAllWindowLayoutInfo(displayId);
  promise.then((data) => {
    console.info('Succeeded in obtaining all window layout info. Data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(\`Failed to obtain all window layout info. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to obtain all window layout info. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### window.getVisibleWindowInfo18+

getVisibleWindowInfo(): Promise<Array<WindowInfo>>

Obtains information about visible main windows on the current screen. Visible main windows are main windows that are not returned to the background. This API uses a promise to return the result.

**System capability**: SystemCapability.Window.SessionManager

**Required permissions**: ohos.permission.VISIBLE\_WINDOW\_INFO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[WindowInfo](../interfaces-others/document.md#windowinfo18)\>> | Promise used to return the information about visible windows. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Function getVisibleWindowInfo can not work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = window.getVisibleWindowInfo();
  promise.then((data) => {
    data.forEach(windowInfo=>{
      console.info(\`left:${windowInfo.rect.left}\`);
      console.info(\`top:${windowInfo.rect.top}\`);
      console.info(\`width:${windowInfo.rect.width}\`);
      console.info(\`height:${windowInfo.rect.height}\`);
      console.info(\`windowId:${windowInfo.windowId}\`);
      console.info(\`windowStatusType:${windowInfo.windowStatusType}\`);
      console.info(\`abilityName:${windowInfo.abilityName}\`);
      console.info(\`bundleName:${windowInfo.bundleName}\`);
      console.info(\`isFocused:${windowInfo.isFocused}\`);
    })
  }).catch((err: BusinessError) => {
    console.error('Failed to getWindowInfo. Cause: ' + JSON.stringify(err));
  });
} catch (exception) {
  console.error(\`Failed to get visible window info. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### window.getGlobalWindowMode20+

getGlobalWindowMode(displayId?: number): Promise<number>

Obtains the window mode of the window that is in the foreground lifecycle on the specified screen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | No | Optional display ID, which is used to obtain the window mode information on the corresponding screen. This parameter must be an integer greater than or equal to 0. If it is less than 0, error code 1300016 is returned. If this parameter is not passed or is set to null or undefined, all screens are queried. If a non-integer is passed, the decimal part is ignored. If the specified screen does not exist, the return value is 0. You are advised to call [getWindowProperties()](../interface-window/document.md#getwindowproperties9) to obtain the display ID of the window. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the window mode. Each binary bit represents a window mode. For details about the supported window modes, see [GlobalWindowMode](../enums/document.md#globalwindowmode20). The return value is the result of a bitwise OR operation on the corresponding window mode values. For example, if there are full-screen, floating, and PiP windows on the current screen, the return value is **0b1|0b100|0b1000 = 13**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. function getGlobalWindowMode can not work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  let promise = window.getGlobalWindowMode(displayId);
  promise.then((data) => {
    console.info(\`Succeeded in obtaining global window mode. Data: ${data}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to obtain global window mode. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to obtain global window mode. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### window.setWatermarkImageForAppWindows21+

setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>

Sets a watermark image for windows in the current application process. This API uses a promise to return the result. This API must be called after [loadContent()](../interface-window/document.md#loadcontent9) or [setUIContent()](../interface-window/document.md#setuicontent9) takes effect.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pixelMap | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | undefined | Yes | 
If this parameter is set to **image.PixelMap**, a watermark image is set. If this parameter is set to **undefined**, the watermark is removed.

If the width and height of the image both surpass the window and screen sizes, error code 1300016 is returned.

If the width or height of the image goes beyond the window dimensions, the excess part is trimmed.

If the width or height of the image falls short of the window dimensions, the shortfall is automatically repeated to complete the image.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function setWatermarkImageForAppWindows can not to work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

import { image } from "@kit.ImageKit";
import { BusinessError } from "@kit.BasicServicesKit";

let color: ArrayBuffer = new ArrayBuffer(96);
let initializationOptions: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.RGBA\_8888,
  size: {
    height: 4,
    width: 6,
  },
};
image.createPixelMap(color, initializationOptions).then((pixelMap: image.PixelMap) => {
  console.info("Succeeded in creating pixelmap.");
  try {
    let promise = window.setWatermarkImageForAppWindows(pixelMap);
    promise.then(() => {
        console.info("Succeeded in setting watermark image.");
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set watermark image. Cause code: ${err.code}, message: ${err.message}\`);
    });
  } catch (exception) {
    console.error(\`Failed to set watermark image. Exception code: ${exception.code}, message: ${exception.message}\`);
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to create PixelMap. Cause code: ${err.code}, message: ${err.message}\`);
});

#### window.setStartWindowBackgroundColor20+

setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>

Sets the background color of the splash screen of the UIAbility based on the specified module name and ability name within the same bundle name. This API uses a promise to return the result.

This API takes effect for all processes of the same bundle name, for example, in multi-instance or clone scenarios.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| moduleName | string | Yes | Module name of the UIAbility. The value is a string of 0 to 200 bytes. Only the module names within the same application can be set. The module name is specified in the **name** field of the [module.json5 file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#tags-in-the-configuration-file). |
| abilityName | string | Yes | Name of the UIAbility. The value is a string of 0 to 200 bytes. Only the ability names within the same application can be set. The UIAbility name is specified in the **name** field under [abilities in the module.json5 file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities). |
| color | [ColorMetrics](../../../ui/arkui/graphics/document.md#colormetrics12) | Yes | Background color of the splash screen. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.function setStartWindowBackgroundColor can not to work correctly due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics, window } from '@kit.ArkUI';

try {
  let promise = window.setStartWindowBackgroundColor("entry", "EntryAbility", ColorMetrics.numeric(0xff000000));
  promise.then(() => {
    console.info('Succeeded in setting the starting window color.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set the starting window color. Cause code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to set the starting window color. Cause code: ${exception.code}, message: ${exception.message}\`);
}

#### window.getAllMainWindowInfo21+

getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>

Obtains the information about all main windows. This API uses a promise to return the result.

**Required permissions**: ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[MainWindowInfo](../interfaces-others/document.md#mainwindowinfo21)\>> | Promise used to return an array of main window information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, UIAbility, common, Permissions } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error(\`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
      }
      reqPermissionsFromUser(permissions, this.context);
      console.info('Succeeded in loading the content');
    });
    try {
      let windowInfoPromise = window.getAllMainWindowInfo();
      windowInfoPromise.then((list: Array<window.MainWindowInfo>) => {
        console.info('Get all main window info success.');
      }).catch((err: BusinessError) => {
        console.error(\`Get all main window info failed. Error info: ${JSON.stringify(err)}\`);
      });
    } catch (err) {
      console.error(\`Get all main window info failed. Cause info: ${JSON.stringify(err)}\`);
    }
  }
}

const permissions: Array<Permissions> = \['ohos.permission.CUSTOM\_SCREEN\_CAPTURE'\];
function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    console.info('requestPermissionsFromUser');
    let grantStatus: Array<number> = data.authResults;
    let length: number = grantStatus.length;
    for (let i = 0; i < length; i++) {
      if (grantStatus\[i\] === 0) {
        // User granted permission.
      } else {
        // User denied permission.
        return;
      }
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request permission from user. Code is ${err.code}, message is ${err.message}\`);
  })
}

#### window.getMainWindowSnapshot21+

getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration): Promise<Array<image.PixelMap | undefined>>

Obtains the screenshots of one or more main windows specified by **windowId**. This API uses a promise to return the result.

**Required permissions**: ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**System capability**: SystemCapability.Window.SessionManager

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | Array<number> | Yes | Array of main window IDs. These IDs can be obtained using [window.getAllMainWindowInfo()](#windowgetallmainwindowinfo21). If the array is null or undefined, contains any negative number, includes duplicates, or has more than 512 entries, error code 401 is returned. If the array contains any positive ID that does not match an existing window, undefined is returned. |
| config | [WindowSnapshotConfiguration](../interfaces-others/document.md#windowsnapshotconfiguration21) | Yes | Configuration for obtaining the window screenshot. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | undefined>> | Promise used to return an array of PixelMap objects of the screenshots, representing the screenshots, in the order of the provided window ID array. If a window ID is valid but the corresponding main window cannot be found, undefined is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300003 | This window manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, UIAbility, common, Permissions } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error(\`Failed to load the content. Cause: JSON.stringify(err)\`);
      }
      reqPermissionsFromUser(permissions, this.context);
      console.info('Success in loading the content');
    });
    try {
      let windowIds: number\[\] = \[\];
      let configs: window.WindowSnapshotConfiguration = {
        useCache: false
      }
      let windowInfoPromise = window.getAllMainWindowInfo();
      windowInfoPromise.then((mainWindowInfoList: Array<window.MainWindowInfo>) => {
        for (let i = 0; i < mainWindowInfoList.length; i++) {
          windowIds\[i\] = mainWindowInfoList\[i\].windowId;
        }
        let promise = window.getMainWindowSnapshot(windowIds, configs);
        promise.then((list: Array<image.PixelMap | undefined>) => {
          for (let i = 0; i < list.length; i++) {
            console.info(\`Get main window snapshot, getBytesNumberPerRow: ${list\[i\]?.getBytesNumberPerRow()}\`);
          }
        }).catch((err: BusinessError) => {
          console.error(\`Get main window snapshot failed. Error info: ${JSON.stringify(err)}\`);
        });
      }).catch((err: BusinessError) => {
        console.error(\`Get all main window info failed. Error info: ${JSON.stringify(err)}\`);
      });
    } catch (err) {
      console.error(\`Get all main window info failed. Cause info: ${JSON.stringify(err)}\`);
    }
  }
}

const permissions: Array<Permissions> = \['ohos.permission.CUSTOM\_SCREEN\_CAPTURE'\];
function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    console.info('requestPermissionsFromUser');
    let grantStatus: Array<number> = data.authResults;
    let length: number = grantStatus.length;
    for (let i = 0; i < length; i++) {
      if (grantStatus\[i\] === 0) {
        // User granted permission.
      } else {
        // User denied permission.
        return;
      }
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request permission from user. Code is ${err.code}, message is ${err.message}\`);
  })
}

#### window.create(deprecated)

create(id: string, type: WindowType, callback: AsyncCallback<Window>): void

Creates a child window. This API uses an asynchronous callback to return the result.

The child window created uses an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout) by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/B2zcrdTNROebKuowC8Govw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C64FC56EB92568D7FC9F07F8E0EB7896144223E7362AD72C05D2445B2C58BB4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [createWindow()](#windowcreatewindow9) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Window name, that is, the value of name in [Configuration](../interfaces-others/document.md#configuration9). |
| type | [WindowType](../enums/document.md#windowtype7) | Yes | Window type. |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the child window created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.create('test', window.WindowType.TYPE\_APP, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
});

#### window.create(deprecated)

create(id: string, type: WindowType): Promise<Window>

Creates a child window. This API uses a promise to return the result.

The child window created uses an [immersive layout](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#immersive-layout) by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/zGDFBiZ5QkG66pOdj4J4kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57E386D04EFE363D5A916B2D181AFD3C899A9D8D13477A7D8AFA9836F0503DEF)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [createWindow()](#windowcreatewindow9-1) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Window name, that is, the value of name in [Configuration](../interfaces-others/document.md#configuration9). |
| type | [WindowType](../enums/document.md#windowtype7) | Yes | Window type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the child window created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.create('test', window.WindowType.TYPE\_APP);
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}\`);
});

#### window.create(deprecated)

create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void

Creates a system window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Yhm8xrMZQsKQdLwoZjTVFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D26C1669318F2BD4281E164B283EF285BF226C92110563B00669B4FE21CFA59)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [createWindow()](#windowcreatewindow9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current application context. |
| id | string | Yes | Window name, that is, the value of name in [Configuration](../interfaces-others/document.md#configuration9). |
| type | [WindowType](../enums/document.md#windowtype7) | Yes | Window type. |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the child window created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.create(globalThis.getContext(), 'test', window.WindowType.TYPE\_SYSTEM\_ALERT, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to create the window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
  windowClass.resetSize(500, 1000);
});

#### window.create(deprecated)

create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>

Creates a system window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/DiWcNWWWSKC1G1M9F3_sgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D272A592612DDFEC301F04C350600C5526FFD2DEC48B5032FCB12B3293A04B6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [createWindow()](#windowcreatewindow9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current application context. |
| id | string | Yes | Window name, that is, the value of name in [Configuration](../interfaces-others/document.md#configuration9). |
| type | [WindowType](../enums/document.md#windowtype7) | Yes | Window type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the child window created. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.create(globalThis.getContext(), 'test', window.WindowType.TYPE\_SYSTEM\_ALERT);
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to create the Window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### window.find(deprecated)

find(id: string, callback: AsyncCallback<Window>): void

Finds a window based on the ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ys9cf6P6R0CDz2FWRxCv2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D53F03061F7937D9EE8975C40B66464B676C24B5DFC796E7CEF5FC647614F768)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [findWindow()](#windowfindwindow9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Window name, that is, the value of name in [Configuration](../interfaces-others/document.md#configuration9). |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the window found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.find('test', (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
});

#### window.find(deprecated)

find(id: string): Promise<Window>

Finds a window based on the ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/bPx3RotYSXmiI6TkDKA_KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79883ECFE6F75CCAAB7DDC9364E590D3F607DC3CAD2210489CB374A69931BC80)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [findWindow()](#windowfindwindow9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Window name, that is, the value of name in [Configuration](../interfaces-others/document.md#configuration9). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the window found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.find('test');
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### window.getTopWindow(deprecated)

getTopWindow(callback: AsyncCallback<Window>): void

Obtains the top window of the current application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/2X7ninfhTG-OMZxPsVVreA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF21781EFA01C704A0C223264F866615496558B7CF60E980EAB6D0145F911571)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getLastWindow()](#windowgetlastwindow9) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the top window obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.getTopWindow((err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(\`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}\`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
});

#### window.getTopWindow(deprecated)

getTopWindow(): Promise<Window>

Obtains the top window of the current application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/KglrXGWXS4amNZvvroP2MQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2CCBB8DCF2009A0C834D42DF35A1C98A851289DD9E3533C1E768EA800D850F0)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getLastWindow()](#windowgetlastwindow9-1) instead.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the top window obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.getTopWindow();
promise.then((data)=> {
    windowClass = data;
    console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError)=>{
    console.error(\`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}\`);
});

#### window.getTopWindow(deprecated)

getTopWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void

Obtains the top window of the current application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/IELbXqB4RFyzM0NUU5hZjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6723138A031DCFB24E1CFF4160D2C6C1841C16F9F55DE676952F0F8E966A421F)

This API has been supported since API version 8 and deprecated since API version 9. If **null** or **undefined** is passed to the **ctx** parameter, the callback may fail to be executed. You are advised to use [getLastWindow()](#windowgetlastwindow9) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current application context. |
| callback | AsyncCallback<[Window](../interface-window/document.md)\> | Yes | Callback used to return the top window obtained. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage:window.WindowStage){
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    try {
      window.getTopWindow(this.context, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if(errCode){
          console.error(\`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}\`);
          return ;
        }
        windowClass = data;
        console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
      });
    } catch(error){
      console.error(\`Failed to obtain the top window. Cause code: ${error.code}, message: ${error.message}\`);
    }
  }
}

#### window.getTopWindow(deprecated)

getTopWindow(ctx: BaseContext): Promise<Window>

Obtains the top window of the current application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/dJd9Hn4tQumiFpbyK16Vtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ABE76E4AE45808AF076B93E389B37DFA247C8D9A97CA6922458ABFDF291FBB4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getLastWindow()](#windowgetlastwindow9-1) instead.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current application context. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Window](../interface-window/document.md)\> | Promise used to return the top window obtained. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage:window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let promise = window.getTopWindow(this.context);
    promise.then((data) => {
      windowClass = data;
      console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(\`Failed to obtain the top window. Cause code: ${error.code}, message: ${error.message}\`);
    });
  }
}
