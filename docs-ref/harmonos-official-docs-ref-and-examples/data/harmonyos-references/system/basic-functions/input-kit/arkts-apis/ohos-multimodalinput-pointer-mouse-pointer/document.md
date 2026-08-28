# @ohos.multimodalInput.pointer (Mouse Pointer)

The **pointer** module provides APIs related to pointer attribute management, such as querying and setting pointer attributes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Fj8ZOnmmTIq7r5Gd-_uL9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26CFF46DD1B0CA2A06CE09F717461E50096FA8B7E95E600FBC5FD62AAF4D0608)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { pointer } from '@kit.InputKit';

#### pointer.setPointerVisible

setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void

Sets whether the mouse pointer is visible in the current window. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| visible | boolean | Yes | Whether the mouse pointer is visible in the current window. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisible(true, (error: BusinessError) => {
              if (error) {
                console.error(\`Set pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                return;
              }
              console.info(\`Set pointer visible success\`);
            });
          } catch (error) {
            console.error(\`Set pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.setPointerVisible

setPointerVisible(visible: boolean): Promise<void>

Sets whether the mouse pointer is visible in the current window. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| visible | boolean | Yes | Whether the mouse pointer is visible in the current window. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisible(false).then(() => {
              console.info(\`Set pointer visible success\`);
            }).catch((error: BusinessError) => {
              console.error(\`Set pointer failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            })
          } catch (error) {
            console.error(\`Set pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.setPointerVisibleSync10+

setPointerVisibleSync(visible: boolean): void

Sets whether the mouse pointer is visible in the current window. This API returns the result synchronously.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| visible | boolean | Yes | Whether the mouse pointer is visible in the current window. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerVisibleSync(false);
            console.info(\`Set pointer visible success\`);
          } catch (error) {
            console.error(\`Set pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.isPointerVisible

isPointerVisible(callback: AsyncCallback<boolean>): void

Obtains the visible status of the mouse pointer. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.isPointerVisible((error: BusinessError, visible: boolean) => {
              if (error) {
                console.error(\`Get pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                return;
              }
              console.info(\`Get pointer visible success, visible: ${JSON.stringify(visible)}\`);
            });
          } catch (error) {
            console.error(\`Get pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.isPointerVisible

isPointerVisible(): Promise<boolean>

Obtains the visible status of the mouse pointer. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the visible status of the mouse pointer. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.isPointerVisible().then((visible: boolean) => {
              console.info(\`Get pointer visible success, visible: ${JSON.stringify(visible)}\`);
            }).catch((error: BusinessError) => {
              console.error(\`Get pointer failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            })
          } catch (error) {
            console.error(\`Get pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.isPointerVisibleSync10+

isPointerVisibleSync(): boolean

Checks whether the mouse pointer is visible in the current window. This API returns the result synchronously.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Visible status of the mouse pointer. The value **true** indicates that the mouse pointer is visible, and the value **false** indicates the opposite. |

**Example**

import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let visible: boolean = pointer.isPointerVisibleSync();
            console.info(\`Get pointer visible success, visible: ${JSON.stringify(visible)}\`);
          } catch (error) {
            console.error(\`Get pointer visible failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.getPointerStyle

getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void

Obtains the mouse pointer style of the specified window. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | 
Window ID. The value is an integer greater than or equal to **\-1**. The value **\-1** indicates the global window.

If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned.

If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default.

If the mouse pointer style is set for a non-existent window through [setPointerStyle](#pointersetpointerstyle), this API can obtain the mouse pointer style properly.

 |
| callback | AsyncCallback<[PointerStyle](#pointerstyle)\> | Yes | Callback used to return the mouse pointer style. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(\`Invalid windowId\`);
              return;
            }
            try {
              pointer.getPointerStyle(windowId, (error: Error, style: pointer.PointerStyle) => {
                console.info(\`Get pointer style success, style: ${JSON.stringify(style)}\`);
              });
            } catch (error) {
              console.error(\`Get pointer style failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          });
        })
    }
  }
}

#### pointer.getPointerStyle

getPointerStyle(windowId: number): Promise<PointerStyle>

Obtains the mouse pointer style. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | 
Window ID. The value is an integer greater than or equal to **\-1**. The value **\-1** indicates the global window.

If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned.

If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default.

If the mouse pointer style is set for a non-existent window through [setPointerStyle](#pointersetpointerstyle-1), this API can obtain the mouse pointer style properly.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PointerStyle](#pointerstyle)\> | Promise object, which is used to return the mouse pointer style. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(\`Invalid windowId\`);
              return;
            }
            try {
              pointer.getPointerStyle(windowId).then((style: pointer.PointerStyle) => {
                console.info(\`Get pointer style success, style: ${JSON.stringify(style)}\`);
              });
            } catch (error) {
              console.error(\`Get pointer style failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          });
        })
    }
  }
}

#### pointer.getPointerStyleSync10+

getPointerStyleSync(windowId: number): PointerStyle

Obtains the mouse pointer style, such as the east arrow, west arrow, south arrow, and north arrow, of the specified window. This API returns the result synchronously.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | 
Window ID. The value is an integer greater than or equal to **\-1**. The value **\-1** indicates the global window.

If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned.

If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default.

If the mouse pointer style is set for a non-existent window through [setPointerStyleSync](#pointersetpointerstylesync10), this API can obtain the mouse pointer style properly.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PointerStyle](#pointerstyle) | Mouse pointer style. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let windowId = -1;
          try {
            let style: pointer.PointerStyle = pointer.getPointerStyleSync(windowId);
            console.info(\`Get pointer style success, style: ${JSON.stringify(style)}\`);
          } catch (error) {
            console.error(\`Get pointer style failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### pointer.setPointerStyle

setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void

Sets the mouse pointer style of the specified window. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | 
Window ID. The value is an integer greater than or equal to 0.

If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be set properly.

If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly.

The result can be obtained through [getPointerStyle](#pointergetpointerstyle).

 |
| pointerStyle | [PointerStyle](#pointerstyle) | Yes | Pointer style. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(\`Invalid windowId\`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS, error => {
                console.info(\`Set pointer style success\`);
              });
            } catch (error) {
              console.error(\`Set pointer style failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          });
        })
    }
  }
}

#### pointer.setPointerStyle

setPointerStyle(windowId: number, pointerStyle: PointerStyle): Promise<void>

Sets the mouse pointer style of the specified window. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | 
Window ID. The value is an integer greater than or equal to 0.

If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be set properly.

If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly.

The result can be obtained through [getPointerStyle](#pointergetpointerstyle-1).

 |
| pointerStyle | [PointerStyle](#pointerstyle) | Yes | Pointer style. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(\`Invalid windowId\`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS).then(() => {
                console.info(\`Set pointer style success\`);
              });
            } catch (error) {
              console.error(\`Set pointer style failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          });
        })
    }
  }
}

#### pointer.setPointerStyleSync10+

setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void

Sets the mouse pointer style of the specified window. This API returns the result synchronously.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | 
Window ID. The value is an integer greater than or equal to 0.

If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be set properly.

If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly.

The result can be obtained through [getPointerStyleSync](#pointergetpointerstylesync10).

 |
| pointerStyle | [PointerStyle](#pointerstyle) | Yes | Pointer style. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(\`Invalid windowId\`);
              return;
            }
            try {
              pointer.setPointerStyleSync(windowId, pointer.PointerStyle.CROSS);
              console.info(\`Set pointer style success\`);
            } catch (error) {
              console.error(\`getPointerSize failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            }
          });
        })
    }
  }
}

#### PrimaryButton10+

Type of the primary mouse button.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

| Name | Value | Description |
| :-- | :-- | :-- |
| LEFT | 0 | Left button. |
| RIGHT | 1 | Right button. |

#### RightClickType10+

Enumerates shortcut menu triggering modes.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

| Name | Value | Description |
| :-- | :-- | :-- |
| TOUCHPAD\_RIGHT\_BUTTON | 1 | Tapping the right-button area of the touchpad. |
| TOUCHPAD\_LEFT\_BUTTON | 2 | Tapping the left-button area of the touchpad. |
| TOUCHPAD\_TWO\_FINGER\_TAP | 3 | Tapping or pressing the touchpad with two fingers. |
| TOUCHPAD\_TWO\_FINGER\_TAP\_OR\_RIGHT\_BUTTON20+ | 4 | Tapping or pressing the touchpad with two fingers, or tapping the right-button area of the touchpad. |
| TOUCHPAD\_TWO\_FINGER\_TAP\_OR\_LEFT\_BUTTON20+ | 5 | Tapping or pressing the touchpad with two fingers, or tapping the left-button area of the touchpad. |

#### PointerStyle

Mouse pointer style.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

| Name | Value | Description | Legend |
| :-- | :-- | :-- | :-- |
| DEFAULT | 0 | Default | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/20v9YJ3UT1CVjJilivjdbw/en-us_image_0000002568766103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BD858B454E82D95C0005E5DC918820A0785DF515CC7D5EC32D75FB79528D318) |
| EAST | 1 | East arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wUFW7yNuSoKIb5jP6uUbTA/en-us_image_0000002537766378.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83B8EEA3EA9951A25CEDB5F12B63A56118F3FD87E35C8A9C24C85A38B0B3E16D) |
| WEST | 2 | West arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/arpKq7VyRnWMX8zOP4cScg/en-us_image_0000002537926318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ED15091B5DAF37E0BDA53CDD51747EB9B200F24F46771D94E1DFE871AC479E2) |
| SOUTH | 3 | South arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/C76rFfwfRXOfZsO9vbOSqw/en-us_image_0000002568686095.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B743215E136DF065A9B28F10A9A6AB45677E5865528CFD58FF2A4271F37D7C04) |
| NORTH | 4 | North arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/sZiCWCqITf-cC53JDHct1A/en-us_image_0000002568766105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B85EAF4466FD446A2BAEE43D75FE1C8FE0C5EAC02F752D10E06DB343C6FD3F33) |
| WEST\_EAST | 5 | West-east arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/WgKYA6_CRSeh019o5YmjPw/en-us_image_0000002537766380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FBCDFDE320D51C3B99AA7AD2656C6142DF46D14CA821C3C54BB8BDFF6C0AB31) |
| NORTH\_SOUTH | 6 | North-south arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/05k59XP4TF2kbG_lVulXhA/en-us_image_0000002537926320.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFA007A4F14A1299C9FF4DB4014B1F993FF6B2687D8E29702940B3397A67E025) |
| NORTH\_EAST | 7 | North-east arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/YPdVClv3QQKjTrlTU-WjLw/en-us_image_0000002568686097.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45B9F4C25601476A72FE6E5020DC3F0F4E34A039E162FC034E3BB4F3D693F1CE) |
| NORTH\_WEST | 8 | North-west arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wFEfykXiRZOoihW0u95ynw/en-us_image_0000002568766107.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDF8126007056FF474AA93FFF2AF995F9C83E8EB52DD46DDE97902EF978A3A39) |
| SOUTH\_EAST | 9 | South-east arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/tYVXtbMATweKJIdJPRXC_A/en-us_image_0000002537766382.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=468E6DFFEE7220AA993125386163DBD8708E3B25AA6DA757556104411D392BC7) |
| SOUTH\_WEST | 10 | South-west arrow | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/8pJFw1jPRoGZzzR_b9kwNw/en-us_image_0000002537926322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=155B096E0B054F6BE797C75E4B55F0814DFC529A6E0B4A793D9BD379B202F94F) |
| NORTH\_EAST\_SOUTH\_WEST | 11 | North-east and south-west adjustment | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/hjzcjqugQ96NHKHzqVGqaQ/en-us_image_0000002568686099.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=961DC47E8509D31E82CB204F5C277CEE0CAF1D7E6B1636C617DB28691AFB8002) |
| NORTH\_WEST\_SOUTH\_EAST | 12 | North-west and south-east adjustment | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/tbhVubrZTSekkMDbTpRAXw/en-us_image_0000002568766109.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E668123316762F24EE04C91634B2647E132DA9D3B15CEF1389F53578A51DE76B) |
| CROSS | 13 | Cross (accurate selection) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/y-R8KAFNRGWkqwE2hm21lA/en-us_image_0000002537766384.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D5F0F7A854EF2454E074CD4E1363B829590B0765243D1983EFD4A2D57597F87) |
| CURSOR\_COPY | 14 | Copy | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/5ZWWNOXuRj6uufA_wgdN5w/en-us_image_0000002537926324.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A634C6F6C23D9BCB87F3E3A0612ED8C89CFBD50F7421D2252610DB5C17C0039) |
| CURSOR\_FORBID | 15 | Forbid | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/DH7y1YhjRQS3arC_NCLXAA/en-us_image_0000002568686101.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCCAA8E8CACF2DACDF094347A7DB47108A685489E646F3EFF9BB1C3A7894F114) |
| COLOR\_SUCKER | 16 | Sucker | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/GouP4kNsSDSa9DLSxIsCEA/en-us_image_0000002568766111.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B91E3B330A9CAAEACD959339E34CA3C6DAD5759B2821ED889F63B0E07E477FE) |
| HAND\_GRABBING | 17 | Grabbing hand | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/5hU6h6z8TSGQUZn0FrTxfw/en-us_image_0000002537766386.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BCDDA54176F049A9A55FB22DD41257A39267232FB90D5843EA3921A1269CB54) |
| HAND\_OPEN | 18 | Opening hand | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Gbd34E6BSWeMuJjIDrc45w/en-us_image_0000002537926326.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0645BBF385C42AD954BCA3B42964B6A871191689AE4281D86BBB64FBF4B54BF5) |
| HAND\_POINTING | 19 | Hand-shaped pointer | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/SEi7CapoSQC5oaUHz8SuGg/en-us_image_0000002568686103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D02DDB34B77A4536435CBA7DE2C23EB164E987DB4D27A55610B557C035BE8DA) |
| HELP | 20 | Help | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/2OXHUfyRQZ-NxXMEbMbFeQ/en-us_image_0000002568766113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75548A7AE7E1A4B1BEBC810803319ED5D5008C8FC2BAC8414F8714FAC99D6B07) |
| MOVE | 21 | Move | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/KZWCcehsTdOs6Z9mMXPHvw/en-us_image_0000002537766388.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEA0612D8DBDC078A2E479FD88F1E49C38334B19A9A52B93D420F33844888F5C) |
| RESIZE\_LEFT\_RIGHT | 22 | Left and right resizing | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/rUZHq1hsQhefsay3dgqqBw/en-us_image_0000002537926328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B7453A8B3603D0602AF9C51A835601C8135F08A037145B9E3B74F8962CEDBB3) |
| RESIZE\_UP\_DOWN | 23 | Up and down resizing | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/KW_HwnyqQRSVQuLjosxTJQ/en-us_image_0000002568686105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3306E9DA9D07C9A1570613B60865FDD7A60CC08ACE695131AF5C5257DBAF5423) |
| SCREENSHOT\_CHOOSE | 24 | Screenshot crosshair | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/ctdnMQYsTl--rHJXs6m88g/en-us_image_0000002568766115.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19F29F00A259FB8C55B6FC906A5B6455F764E1C52C829FEEE44499083F0AF2C0) |
| SCREENSHOT\_CURSOR | 25 | Screenshot | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/d4G6z3LDTs6JQBfFRCiUQg/en-us_image_0000002537766390.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7D9012E0141863A84CC19CBF551DDEA488E22DB0AF7D23EC0925B3FF23EA9EA) |
| TEXT\_CURSOR | 26 | Text selection | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/ZV684YinSwGTMA_mXtxRdA/en-us_image_0000002537926330.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=971190D9D4B23B48801B026628B3D9726ADE0A2B6F2DF44A5DE06FA6A3CCA9BD) |
| ZOOM\_IN | 27 | Zoom in | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/tYc18jgOSMqJM_B2UgiDnA/en-us_image_0000002568686107.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EB39ED59DFC196ACC3EC34E9485029A806337FE6E019D9A10C8FC8DF145FC75) |
| ZOOM\_OUT | 28 | Zoom out | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/okpcc1RfRXWD6nXVe511Wg/en-us_image_0000002568766117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAA95BA5526715AE0DC6CAF1F35CDA237C4323CB4002670320001902EF5C06E3) |
| MIDDLE\_BTN\_EAST | 29 | Scrolling east | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Rw_MQGBRQPWTNCsaylsm2A/en-us_image_0000002537766392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D87FBAC721FE91E0F95387D0C73F68C486FC1028AE881D7DD483796D06F3F5C) |
| MIDDLE\_BTN\_WEST | 30 | Scrolling west | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/oHsSjtPsRrKL1LG4G0teyA/en-us_image_0000002537926332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC7744F4BA6E1D3651B8D62A5C53E448A18FCC597A93FA2C8F8BDE5655AA6F7E) |
| MIDDLE\_BTN\_SOUTH | 31 | Scrolling south | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/RyOYG4fwT2SSOESgXbcc5Q/en-us_image_0000002568686109.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEE6839F1A7957B77502EF9E67F088108E910AAA93A285264714DD2101DBEC29) |
| MIDDLE\_BTN\_NORTH | 32 | Scrolling north | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/vR0GCx-hTvunKyRFV6Z76A/en-us_image_0000002568766119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF3E332713F459CE727E7508EB9C578E8F63BDC1CE15892BFB5209343F0EB667) |
| MIDDLE\_BTN\_NORTH\_SOUTH | 33 | Scrolling north-south | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/1jKSTgqJSfWWq_bUmpMxiw/en-us_image_0000002537766394.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C17537AD6C4F282D038D5E27BE7B233A4603D183B0D991C153D8CFF87145659) |
| MIDDLE\_BTN\_NORTH\_EAST | 34 | Scrolling north-east | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/tbannXzlTyOuIAIxZNyDcA/en-us_image_0000002537926334.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE7497D8DDECC4EFC872F8FE0D1CAB1744A198EA50DC61683D28A2DFFDA0C0CB) |
| MIDDLE\_BTN\_NORTH\_WEST | 35 | Scrolling north-west | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/7RySygkqQPC-5npDa3woaw/en-us_image_0000002568686111.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4A92467778A90E31C892ED0B07C6BB2C375E296F5A149E3BF1D615BF945FFE5) |
| MIDDLE\_BTN\_SOUTH\_EAST | 36 | Scrolling south-east | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/7_LfV5YJRSeVwSNOz7dIpA/en-us_image_0000002568766121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A06B9B8B976BAF9DB694EFF5F8054325FA15F5D3F5F8F05BCE19BD92390F08C9) |
| MIDDLE\_BTN\_SOUTH\_WEST | 37 | Scrolling south-west | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/vMNPcI4nRCe7GRyCKJzIcQ/en-us_image_0000002537766396.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=429E5D540D7D4D1D869451DF8C7B797E540F9A911470D6869D21460C1CE83731) |
| MIDDLE\_BTN\_NORTH\_SOUTH\_WEST\_EAST | 38 | Moving as a cone in four directions | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/nmiBKjXwR1WgMJzlAlb2qQ/en-us_image_0000002537926336.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9ACB530C5A5323C42B9B009C827BBEE365BC699C6CEEE15919C4F23D5F40DC87) |
| HORIZONTAL\_TEXT\_CURSOR10+ | 39 | Horizontal text selection | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/HIWVEJAPS-ake_ukz1XKTw/en-us_image_0000002568686113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32F22F232EAA69324C291E08C60C1377ACBA3C2C5C3761F35592486C242BE285) |
| CURSOR\_CROSS10+ | 40 | Cross | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/iLRW1sCFT_ClcY3MK2AhsA/en-us_image_0000002568766123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3080BA0F570E7BE79B430E4CB6CF2B89C6197D88EBC596E666DAAB54ADC17C80) |
| CURSOR\_CIRCLE10+ | 41 | Circle | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/oZfBEOSaQQyE23LkZLQDZQ/en-us_image_0000002537766398.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4039B63BDEF44FBD977812EC297DA526797984E63E4B792C8FB876CCAF784F92) |
| LOADING10+ | 42 | 
Animation loading

**Atomic service API**: This API can be used in atomic services since API version 12.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/Z7zpdZU5TBmXPOrman2sUQ/en-us_image_0000002537926338.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E122375643B76AA8B9E2EC64AFB537BF90FFC57F022B39538B86CD68CAFCF8BA) |
| RUNNING10+ | 43 | 

Animation running in the background

**Atomic service API**: This API can be used in atomic services since API version 12.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/q-CzofkzTq6UBszetZCQyg/en-us_image_0000002568686115.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F31289707EDBA4E85CB85B0951C1C2B965F16EFE37D57CF075DA5B165566B732) |
| MIDDLE\_BTN\_EAST\_WEST18+ | 44 | Scrolling east-west | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/noLgxvB4SSKdwQ9_1VVYsg/en-us_image_0000002568766125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A271FE018AD651221AC4EE9F26E964466EC75905FC401483937DEBAA0D6CA2FD) |
| RUNNING\_LEFT22+ | 45 | Running in the background (extension 1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/ehUkMZ0TQUib1xyZKmeoiQ/en-us_image_0000002537766400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30F604F602F543A6C30C06F9B32C5A086F7D689F96C02CFF094B9D8EEC76884E) |
| RUNNING\_RIGHT22+ | 46 | Running in the background (extension 2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/uNU9VCcBSOqerYGZUrajMQ/en-us_image_0000002537926340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B3473A713C0B331AF95571CF14BD4AE20E9E126617D172F876C6C9CAC3136C7) |
| AECH\_DEVELOPER\_DEFINED\_ICON22+ | 47 | Custom circular pointer | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Cuc9RC9fQ1aAoHgLEbDlpA/en-us_image_0000002568686117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2596B43E4638E56F72F99863CE9D143D2EE1382713DEB7E1C8CCB9D5F48D0385) |
| SCREENRECORDER\_CURSOR20+ | 48 | Screen recording | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/oNjvtjoMSy6Bk9pjpVy5Rw/en-us_image_0000002568766127.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F18E5CB20D193BF1ADB7BB8CFD16F0F0342447BC86055FBCF97595267D82103) |
| LASER\_CURSOR22+ | 49 | 

Floating This pointer can be used only when the stylus enters the air mouse mode.

In air mouse mode, you can rotate the stylus in the air to control the movement of the virtual pointer on the screen and press the button on the stylus to turn pages up or down. This mode is used PPT presentation and air gesture control.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/sj2tc0EmS5iM0_9JMUFkTQ/en-us_image_0000002537766402.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA1AC90113730E21F617E1659903D4F9A489A2C65C66128AD397FC90DC742B25) |
| LASER\_CURSOR\_DOT22+ | 50 | 

Click This pointer can be used only when the stylus enters the air mouse mode.

In air mouse mode, you can rotate the stylus in the air to control the movement of the virtual pointer on the screen and press the button on the stylus to turn pages up or down. This mode is used PPT presentation and air gesture control.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/8BRdTDeGRI-2bURq__vaJQ/en-us_image_0000002537926342.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A76C9F8728260057F6A33E6959F41C9782E25D22555A7EF8910812E74C6914D6) |
| LASER\_CURSOR\_DOT\_RED22+ | 51 | 

Laser pointer This pointer can be used only when the stylus enters the air mouse mode.

In air mouse mode, you can rotate the stylus in the air to control the movement of the virtual pointer on the screen and press the button on the stylus to turn pages up or down. This mode is used PPT presentation and air gesture control.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/U_rtjmTmRAiixosuc8HE8A/en-us_image_0000002568686119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=584FE7BAD0CDFBBECB2B43FAE393980274185FD1727DB424E6FA8614294FC980) |
| DEVELOPER\_DEFINED\_ICON22+ | \-100 | Custom pointer. You can use the [setCustomCursor](#pointersetcustomcursor15) to set a custom pointer, but not the [setPointerStyle](#pointersetpointerstyle-1) directly. | You can customize pointers as needed via API. |

#### pointer.setCustomCursor11+

setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>

Sets the custom cursor style of the specified window. This API uses a promise to return the result asynchronously.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | Window ID. |
| pixelMap | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Custom cursor resource. |
| focusX | number | No | Focus x of the custom cursor. The value is greater than or equal to **0**. The default value is **0**. |
| focusY | number | No | Focus y of the custom cursor. The value is greater than or equal to **0**. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app\_icon is an example resource. Configure the resource file based on the actual requirements.
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app\_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, pixelMap).then(() => {
                    console.info(\`setCustomCursor success\`);
                  });
                } catch (error) {
                  console.error(\`setCustomCursor failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                }
              });
            });
          });
        })
    }
  }
}

#### CustomCursor15+

Defines custom cursor resources.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pixelMap | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | No | Pixel map. The minimum size is subject to the minimum limit of the image. The maximum size is 256 x 256 px. |
| focusX | number | No | Yes | Horizontal coordinate of the cursor focus. The coordinates are restricted by the size of the custom cursor. The minimum value is **0**, and the maximum value is the maximum width of the image. The default value is **0** if the parameter is left empty. |
| focusY | number | No | Yes | Vertical coordinate of the cursor focus. The coordinates are restricted by the size of the custom cursor. The minimum value is **0**, and the maximum value is the maximum height of the image. The default value is **0** if the parameter is left empty. |

#### CursorConfig15+

Defines custom cursor configuration.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| followSystem | boolean | No | No | Whether to adjust the cursor size based on system settings. The value **true** means to adjust the cursor size based on system settings, and the value **false** means to use the custom cursor size. The adjustment range is \[size of the cursor image, 256 x 256\]. |

#### pointer.setCustomCursor15+

setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>

Sets the custom cursor style of the specified window. This API uses a promise to return the result asynchronously.

The cursor may be switched back to the system style in the following cases: application window layout change, hot zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of the cursor in different areas of the window. In this case, you need to reset the cursor style.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | Window ID. |
| cursor | [CustomCursor](#customcursor15) | Yes | Custom cursor resource. |
| config | [CursorConfig](#cursorconfig15) | Yes | Custom cursor configuration, which specifies whether to adjust the cursor size based on system settings. If **followSystem** in **CursorConfig** is set to **true**, the supported adjustment range is \[size of the cursor image, 256 x 256\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Mouse Pointer Error Codes](../../error-codes/mouse-pointer-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Abnormal windowId parameter passed in. 2. Abnormal pixelMap parameter passed in; 3. Abnormal focusX parameter passed in.4. Abnormal focusY parameter passed in. |
| 26500001 | Invalid windowId. Possible causes: The window id does not belong to the current process. |

**Example**

import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app\_icon is an example resource. Configure the resource file based on the actual requirements.
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app\_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, { pixelMap: pixelMap, focusX: 25, focusY: 25 },
                    { followSystem: false }).then(() => {
                    console.info(\`setCustomCursor success\`);
                  });
                } catch (error) {
                  console.error(\`setCustomCursor failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                }
              });
            });
          });
        })
    }
  }
}

#### pointer.setCustomCursorSync11+

setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void

Sets the custom cursor style of the specified window. This API returns the result synchronously.

**System capability**: SystemCapability.MultimodalInput.Input.Pointer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | Window ID. The value must be an integer greater than 0. |
| pixelMap | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Custom cursor resource. |
| focusX | number | No | Focus x of the custom cursor. The value is greater than or equal to **0**. The default value is **0**. |
| focusY | number | No | Focus y of the custom cursor. The value is greater than or equal to **0**. The default value is **0**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app\_icon is an example resource. Configure the resource file based on the actual requirements.
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app\_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursorSync(windowId, pixelMap, 25, 25);
                  console.info(\`setCustomCursorSync success\`);
                } catch (error) {
                  console.error(\`setCustomCursorSync failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                }
              });
            });
          });
        })
    }
  }
}
