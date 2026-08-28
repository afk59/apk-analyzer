# @ohos.arkui.uiExtension (uiExtension)

The **uiExtension** module provides APIs for the [EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/embeddeduiextensionability) (or [UIExtensionAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md#uiextensionability)) to obtain the host application window information or the information about the corresponding [EmbeddedComponent](../../../arkts-components/rendering-drawing/embeddedcomponent/document.md) component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/TfsRnyKCTkGbsgdd3fVg9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74D7F9B1DD99B3BDEB0D070A13375A66171CCAB6D3D6AA9F3E296381C314307D)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { uiExtension } from '@kit.ArkUI';

#### WindowProxy

Implements the proxy for the UIExtension host application window.

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 14.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| properties14+ | [WindowProxyProperties](#windowproxyproperties14) | No | No | 
Information about the component (**EmbeddedComponent** or **UIExtensionComponent**).

Note: Due to architecture restrictions, avoid obtaining the value in [onSessionCreate](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md#onsessioncreate). Instead, when possible, obtain the value after receiving the [on('windowSizeChange')](#onwindowsizechange) callback.

 |

#### \[h2\]getWindowAvoidArea

getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea

Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area, and soft keyboard area.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [window.AvoidAreaType](../../window-manager/ohos-window-window/enums/document.md#avoidareatype7) | Yes | Type of the avoidance area. |

**Return value**

| Type | Description |
| :-- | :-- |
| [window.AvoidArea](../../window-manager/ohos-window-window/interfaces-others/document.md#avoidarea7) | Avoidance area for the content of the host window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Obtain the information about the area where the window cannot be displayed.
    let avoidArea: window.AvoidArea | undefined = extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE\_SYSTEM);
    console.info(\`avoidArea: ${JSON.stringify(avoidArea)}\`);
  }
}

#### \[h2\]on('avoidAreaChange')

on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void

Subscribes to events of system avoidance area changes.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'avoidAreaChange'**, indicating the event of changes to the area where the window cannot be displayed. |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[AvoidAreaInfo](#avoidareainfo)\> | Yes | Callback function that receives the information about the current avoidance area. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Subscribe to the event indicating changes to the area where the window cannot be displayed.
    extensionWindow.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
      console.info(\`The avoid area of the host window is: ${JSON.stringify(info.area)}.\`);
    });
  }
}

#### \[h2\]off('avoidAreaChange')

off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void

Unsubscribes from events of system avoidance area changes.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'avoidAreaChange'**, indicating the event of changes to the area where the window cannot be displayed. |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[AvoidAreaInfo](#avoidareainfo)\> | No | Callback used for unsubscription. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Cancel all subscriptions to the event indicating changes to the area where the window cannot be displayed.
    extensionWindow.off('avoidAreaChange');
  }
}

#### \[h2\]on('windowSizeChange')

on(type: 'windowSizeChange', callback: Callback<window.Size>): void

Subscribes to size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowSizeChange'**, indicating the component (**EmbeddedComponent** or **UIExtensionComponent**) size change events. |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[window.Size](../../window-manager/ohos-window-window/interfaces-others/document.md#size7)\> | Yes | Callback function that receives the current component size as the input parameter. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Subscribe to size change events of the component (EmbeddedComponent or UIExtensionComponent).
    extensionWindow.on('windowSizeChange', (size: window.Size) => {
      console.info(\`The avoid area of the host window is: ${JSON.stringify(size)}.\`);
    });
  }
}

#### \[h2\]off('windowSizeChange')

off(type: 'windowSizeChange', callback?: Callback<window.Size>): void

Unsubscribes from size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'windowSizeChange'**, indicating the component (**EmbeddedComponent** or **UIExtensionComponent**) size change events. |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[window.Size](../../window-manager/ohos-window-window/interfaces-others/document.md#size7)\> | No | Callback used to return the size of the current component (**EmbeddedComponent** or **UIExtensionComponent**). If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Unsubscribe from size change events of the component (EmbeddedComponent or UIExtensionComponent).
    extensionWindow.off('windowSizeChange');
  }
}

#### \[h2\]on('rectChange')14+

on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void

Subscribes to position and size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 14.

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'rectChange'**, indicating the rectangle change event for the component (**EmbeddedComponent** or **UIExtensionComponent**). |
| reasons | number | Yes | Reason why the position and size of the component (**EmbeddedComponent** or **UIExtensionComponent**) change. For details about the values, see [RectChangeReason](#rectchangereason14). |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[RectChangeOptions](#rectchangeoptions14)\> | Yes | Callback used to return the current rectangle change values and the reason for the change of the component (**EmbeddedComponent** or **UIExtensionComponent**). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Subscribe to position and size change events of the component (EmbeddedComponent or UIExtensionComponent).
    extensionWindow.on('rectChange', uiExtension.RectChangeReason.HOST\_WINDOW\_RECT\_CHANGE, (data: uiExtension.RectChangeOptions) => {
        console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
    });
  }
}

#### \[h2\]off('rectChange')14+

off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void

Unsubscribes from position and size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 14.

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'rectChange'**, indicating the rectangle change event for the component (**EmbeddedComponent** or **UIExtensionComponent**). |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[RectChangeOptions](#rectchangeoptions14)\> | No | Callback used to return the current rectangle change values and the reason for the change of the component (**EmbeddedComponent** or **UIExtensionComponent**). If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Unsubscribe from position and size change events of the component (EmbeddedComponent or UIExtensionComponent).
    extensionWindow.off('rectChange');
  }
}

#### \[h2\]createSubWindowWithOptions

createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>

Creates a subwindow for this window proxy. This API uses a promise to return the result.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Model restriction**: This API can be used only in the stage model.

**Device behavior differences**: This API can be called properly on a device that supports [freeform windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) and is in the freeform window state. If the device does not support freeform windows, or if the device supports freeform windows but is not in the freeform window state, this API returns error code 801 when called.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the subwindow. |
| subWindowOptions | [window.SubWindowOptions](../../window-manager/ohos-window-window/interfaces-others/document.md#subwindowoptions11) | Yes | Parameters used for creating the subwindow. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[window.Window](../../window-manager/ohos-window-window/interface-window/document.md)\> | Promise used to return the subwindow created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    const subWindowOpts: window.SubWindowOptions = {
      title: 'This is a subwindow',
      decorEnabled: true
    };
    // Create a subwindow.
    extensionWindow.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
      .then((subWindow: window.Window) => {
        subWindow.setUIContent('pages/Index', (err, data) => {
          if (err && err.code != 0) {
            return;
          }
          subWindow?.resize(300, 300, (err, data) => {
            if (err && err.code != 0) {
              return;
            }
            subWindow?.moveWindowTo(100, 100, (err, data) => {
              if (err && err.code != 0) {
                return;
              }
              subWindow?.showWindow((err, data) => {
                if (err && err.code == 0) {
                  console.info(\`The subwindow has been shown!\`);
                } else {
                  console.error(\`Failed to show the subwindow!\`);
                }
              });
            });
          });
        });
      }).catch((error: BusinessError) => {
      console.error(\`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}\`);
    })
  }
}

#### \[h2\]occupyEvents18+

occupyEvents(eventFlags: number): Promise<void>

Sets the events that the component (**EmbeddedComponent** or **UIExtensionComponent**) will occupy, preventing the host from responding to these events within the component's area.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| eventFlags | number | Yes | Type of events to occupy. For details about the available values, see [EventFlag](#eventflag18). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Window Error Codes](../../../error-codes/graphics/window-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300003 | This window manager service works abnormally. |

**Example**

// ExtensionProvider.ts
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddedUIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionWindow = session.getUIExtensionWindowProxy();
    // Occupy events.
    setTimeout(() => {
      try {
        let promise = extensionWindow.occupyEvents(uiExtension.EventFlag.EVENT\_CLICK | uiExtension.EventFlag.EVENT\_LONG\_PRESS);
        promise.then(() => {
          console.info(\`Succeeded in occupying events\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to occupy events. Cause code: ${err.code}, message: ${err.message}\`);
        });
      } catch (e) {
        console.error(\`Occupy events got exception code: ${e.code}, message: ${e.message}\`);
      }
    }, 500);
  }
}

#### EventFlag18+

Enumerates event types.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 18.

| Name | Value | Description |
| :-- | :-- | :-- |
| EVENT\_NONE | 0x00000000 | No event. |
| EVENT\_PAN\_GESTURE\_LEFT | 0x00000001 | Pan-left event. |
| EVENT\_PAN\_GESTURE\_RIGHT | 0x00000002 | Pan-right event. |
| EVENT\_PAN\_GESTURE\_UP | 0x00000004 | Pan-up event. |
| EVENT\_PAN\_GESTURE\_DOWN | 0x00000008 | Pan-down event. |
| EVENT\_CLICK | 0x00000100 | Click event. |
| EVENT\_LONG\_PRESS | 0x00000200 | Long press event. |

#### AvoidAreaInfo

Represents the information about the avoidance area of the window.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [window.AvoidAreaType](../../window-manager/ohos-window-window/enums/document.md#avoidareatype7) | No | No | Type of the avoidance area of the window. |
| area | [window.AvoidArea](../../window-manager/ohos-window-window/interfaces-others/document.md#avoidarea7) | No | No | Avoidance area for the content of the window. |

#### WindowProxyProperties14+

Provides information about a component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 14.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uiExtensionHostWindowProxyRect | [window.Rect](../../window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | No | Position and size of the component (**EmbeddedComponent** or **UIExtensionComponent**). |

#### RectChangeReason14+

Enumerates the reasons for changes in the rectangle (position and size) of the component (**EmbeddedComponent** or **UIExtensionComponent**).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 14.

| Name | Value | Description |
| :-- | :-- | :-- |
| HOST\_WINDOW\_RECT\_CHANGE | 0x0001 | The rectangle of the host window containing the component changes. |

#### RectChangeOptions14+

Provides the values and reasons returned when the rectangle (position and size) of the component (**EmbeddedComponent** or **UIExtensionComponent**) changes.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 14.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rect | [window.Rect](../../window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | No | New values of the rectangle of the component after the change. |
| reason | [RectChangeReason](#rectchangereason14) | No | No | Reason for the rectangle change. |

#### Example

This example shows how to use all the available APIs in the [EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/embeddeduiextensionability). The bundle name of the sample application is **com.example.embeddeddemo**, and the **EmbeddedUIExtensionAbility** to start is **ExampleEmbeddedAbility**.

-   The **EntryAbility** (**UIAbility**) of the sample application loads the **pages/Index.ets** file, whose content is as follows:

// The UIAbility loads pages/Index.ets when started.
import { Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Message: ';
  private want: Want = {
    bundleName: "com.example.embeddeddemo",
    abilityName: "ExampleEmbeddedAbility",
  }

  build() {
    Row() {
      Column() {
        Text(this.message).fontSize(30)
        EmbeddedComponent(this.want, EmbeddedType.EMBEDDED\_UI\_EXTENSION)
          .width('100%')
          .height('90%')
          .onTerminated((info) => {
            this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
          })
          .onError((error) => {
            this.message = 'Error: code = ' + error.code;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

-   The **EmbeddedUIExtensionAbility** to start by the **EmbeddedComponent** is implemented in the **ets/extensionAbility/ExampleEmbeddedAbility** file. The file content is as follows:

import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

const TAG: string = '\[ExampleEmbeddedAbility\]';

export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
  onCreate() {
    console.info(TAG, \`onCreate\`);
  }

  onForeground() {
    console.info(TAG, \`onForeground\`);
  }

  onBackground() {
    console.info(TAG, \`onBackground\`);
  }

  onDestroy() {
    console.info(TAG, \`onDestroy\`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, \`onSessionCreate, want: ${JSON.stringify(want)}\`);
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);
    session.loadContent('pages/extension', storage);
  }
}

-   The entry page file of the **EmbeddedUIExtensionAbility** is **pages/extension.ets**, whose content is as follows:

import { UIExtensionContentSession } from '@kit.AbilityKit';
import { uiExtension, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry()
@Component
struct Extension {
  @State message: string = 'EmbeddedUIExtensionAbility Index';
  private storage: LocalStorage | undefined = this.getUIContext()?.getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');
  private extensionWindow: uiExtension.WindowProxy | undefined = this.session?.getUIExtensionWindowProxy();
  private subWindow: window.Window | undefined = undefined;

  aboutToAppear(): void {
    this.extensionWindow?.on('windowSizeChange', (size: window.Size) => {
      console.info(\`size = ${JSON.stringify(size)}\`);
    });
    this.extensionWindow?.on('rectChange', uiExtension.RectChangeReason.HOST\_WINDOW\_RECT\_CHANGE,
      (data: uiExtension.RectChangeOptions) => {
        console.info('Succeeded window rect changes. Data: ' + JSON.stringify(data));
      });
    this.extensionWindow?.on('avoidAreaChange', (info: uiExtension.AvoidAreaInfo) => {
      console.info(\`type = ${JSON.stringify(info.type)}, area = ${JSON.stringify(info.area)}\`);
    });
  }

  aboutToDisappear(): void {
    this.extensionWindow?.off('windowSizeChange');
    this.extensionWindow?.off('rectChange');
    this.extensionWindow?.off('avoidAreaChange');
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
      Button("Obtain Component Size").width('90%').margin({ top: 5, bottom: 5 }).fontSize(16).onClick(() => {
        let rect = this.extensionWindow?.properties.uiExtensionHostWindowProxyRect;
        console.info(\`EmbeddedComponent position and size: ${JSON.stringify(rect)}\`);
      })
      Button("Obtain Avoid Area Info").width('90%').margin({ top: 5, bottom: 5 }).fontSize(16).onClick(() => {
        let avoidArea: window.AvoidArea | undefined =
          this.extensionWindow?.getWindowAvoidArea(window.AvoidAreaType.TYPE\_SYSTEM);
        console.info(\`Avoidance area: ${JSON.stringify(avoidArea)}\`);
      })
      Button("Create Subwindow").width('90%').margin({ top: 5, bottom: 5 }).fontSize(16).onClick(() => {
        let subWindowOpts: window.SubWindowOptions = {
          'title': 'This is a subwindow',
          decorEnabled: true
        };
        this.extensionWindow?.createSubWindowWithOptions('subWindowForHost', subWindowOpts)
          .then((subWindow: window.Window) => {
            this.subWindow = subWindow;
            this.subWindow.loadContent('pages/Index', this.storage, (err, data) => {
              if (err && err.code != 0) {
                return;
              }
              this.subWindow?.resize(300, 300, (err, data) => {
                if (err && err.code != 0) {
                  return;
                }
                this.subWindow?.moveWindowTo(100, 100, (err, data) => {
                  if (err && err.code != 0) {
                    return;
                  }
                  this.subWindow?.showWindow((err, data) => {
                    if (err && err.code == 0) {
                      console.info(\`The subwindow has been shown!\`);
                    } else {
                      console.error(\`Failed to show the subwindow!\`);
                    }
                  });
                });
              });
            });
          }).catch((error: BusinessError) => {
          console.error(\`Create subwindow failed. Cause code: ${error.code}, message: ${error.message}\`);
        })
      })
    }.width('100%').height('100%')
  }
}

-   Add an item to **extensionAbilities** in the **module.json5** file of the sample application. The details are as follows:
    
    {
      "name": "ExampleEmbeddedAbility",
      "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
      "type": "embeddedUI"
    }
