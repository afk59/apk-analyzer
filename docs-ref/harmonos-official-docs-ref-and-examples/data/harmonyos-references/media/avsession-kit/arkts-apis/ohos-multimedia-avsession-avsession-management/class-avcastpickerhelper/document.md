# Class (AVCastPickerHelper)

AVCastPickerHelper implements a semi-modal object used for casting. It displays a semi-modal window for users to select a target cast device. Before using the APIs of this class, you need to create an AVCastPickerHelper instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/pZMqbxMBSaW5qTufnwezUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062423Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C7B0FD17D12695E48C779E23CA0479382D4A1424FBCAA15F2C62BCB9D282FA5)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this class are supported since API version 14.

#### Modules to Import

import { avSession } from '@kit.AVSessionKit';

#### constructor14+

constructor(context: Context)

Creates an AVCastPickerHelper instance. For details about how to obtain the context, see [getHostContext](../../../../../application-framework/arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#gethostcontext12).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. (Only [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) is supported.) |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**Example**

import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as Context;
            let avCastPicker = new avSession.AVCastPickerHelper(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### select14+

select(options?: AVCastPickerOptions): Promise<void>

Starts the AVCastPicker dialog box, where users can select the target cast device. This API uses a promise to return the result. You can pass in **AVCastPickerOptions** to specify the properties for selection.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AVCastPickerOptions](../interfaces-others/document.md#avcastpickeroptions14) | No | AVCastPicker selection options. If this parameter is not specified, the default value of **AVCastPickerOptions** is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. If the command is sent, no value is returned; otherwise, an error object is returned. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

class MyPage {
  private avCastPicker: avSession.AVCastPickerHelper;

  constructor(context: common.Context) {
    this.avCastPicker = new avSession.AVCastPickerHelper(context);
  }

  async selectCastDevice() {
    const avCastPickerOptions: avSession.AVCastPickerOptions = {
      sessionType: 'video',
    };

    this.avCastPicker.select(avCastPickerOptions).then(() => {
      console.info('select successfully');
    }).catch((err: BusinerssError) => {
      console.error('AVCastPicker.select failed with err: ${err.code}, ${err.message}');
    });
  }
}

#### resetCommunicationDevice21+

resetCommunicationDevice(): Promise<void>

Restores the communication device of an application to the default device. For example, during a voice call, the communication device of the mobile phone is restored to the earpiece. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { common } from '@kit.AbilityKit';
import { avSession } from '@kit.AVSessionKit';

async function avCastPicker(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.resetCommunicationDevice().then(() => {
    console.info('resetCommunicationDevice successfully');
  });
}

#### on('pickerStateChange')14+

on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void

Subscribes to semi-modal window change events.

Multiple callbacks can be registered for this event. To ensure only the latest callback executes, unregister previous listeners first. Otherwise, all registered callbacks will fire on state changes.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'pickerStateChange'** is triggered when the semi-modal window changes. |
| callback | Callback<[AVCastPickerState](../../ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md#avcastpickerstate)\> | Yes | Callback function, where the **state** parameter indicates the new state of the semi-modal window. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**Example**

import { common } from '@kit.AbilityKit';
import { AVCastPickerState } from '@kit.AVSessionKit';
import { avSession } from '@kit.AVSessionKit';

async function onPickerStateChange(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.on('pickerStateChange', (state: AVCastPickerState) => {
    console.info(\`picker state change : ${state}\`);
  });
}

#### off('pickerStateChange')14+

off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void

Unsubscribes from semi-modal window change events. If a callback is specified, the corresponding listener is unregistered. If no callback is specified, all listeners for the specified event are unregistered.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.AVSession.AVCast

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'pickerStateChange'** in this case. |
| callback | Callback<[AVCastPickerState](../../ohos-multimedia-avcastpickerparam-avcastpicker-parameters/document.md#avcastpickerstate)\> | No | 
Callback function, where the **state** parameter indicates the new state of the semi-modal window.

If the unsubscription is successful, **err** is **undefined**; otherwise, **err** is an error object.

The **callback** parameter is optional. If it is not specified, all the subscriptions to the specified event are canceled for this session.

 |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |

**Example**

import { common } from '@kit.AbilityKit';
import { avSession } from '@kit.AVSessionKit';

async function onPickerStateChange(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.off('pickerStateChange');
}
