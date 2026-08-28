# Input Device Development

#### When to Use

Input device management provides functions such as listening for device hot-swap events and querying the keyboard type of a specified device. For example, as a user enters text, the input method determines whether to launch the virtual keyboard based on whether a physical keyboard is currently inserted. Your application can determine whether a physical keyboard is inserted by listening to device hot-swap events.

#### Modules to Import

import { inputDevice } from '@kit.InputKit';

#### Available APIs

The following table lists common APIs for input device management. For details, see [@ohos.multimodalInput.inputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputdevice).

| API | Description |
| :-- | :-- |
| getDeviceList(): Promise<Array<number>> | Obtains the list of input devices. |
| getKeyboardType(deviceId: number): Promise<KeyboardType> | Obtains the keyboard type of the input device. |
| on(type: "change", listener: Callback<DeviceListener>): void | Enables listening for device hot-swap events. |
| off(type: "change", listener?: Callback<DeviceListener>): void | Disables listening for device hot-swap events. |

#### Virtual Keyboard Detection

When a user enters text, the input method determines whether to launch the virtual keyboard based on whether a physical keyboard is currently inserted. Your application can determine whether a physical keyboard is inserted by listening to device hot-swap events.

## How to Develop

1.  Call the [getDeviceList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputdevice#inputdevicegetdevicelist9) API to obtain the list of connected input devices. Call the [getKeyboardType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputdevice#inputdevicegetkeyboardtype9) API to traverse all connected devices to check whether a physical keyboard exists. If a physical keyboard exists, mark the physical keyboard as connected. This step ensures that your application detects all inserted input devices before listening for device hot-swap events.
2.  Call the [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputdevice#inputdeviceonchange9) API to listen for device hot-swap events. If a physical keyboard is inserted, mark the physical keyboard as connected. If a physical keyboard is removed, mark the physical keyboard as disconnected.

import { inputDevice } from '@kit.InputKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State isPhysicalKeyboardExist: boolean = false;
  @State message: string = "Click to obtain the device list and monitor device hot-plug events";
  keyBoards: Map<number, inputDevice.KeyboardType> = new Map();

  // ...

  build() {
    RelativeContainer() {
      Column() {
        // ...

        Text(this.message)
          .onClick(() => {
            try {
              // 1. Obtain the list of input devices and check whether a physical keyboard is connected.
              inputDevice.getDeviceList().then(data => {
                for (let i = 0; i < data.length; ++i) {
                  inputDevice.getKeyboardType(data\[i\]).then(type => {
                    if (type === inputDevice.KeyboardType.ALPHABETIC\_KEYBOARD) {
                      // The physical keyboard is connected.
                      this.isPhysicalKeyboardExist = true;
                      this.keyBoards.set(data\[i\], type);
                    }
                  });
                }
              });
              // 2. Listen for device hot-swap events.
              inputDevice.on("change", (data) => {
                hilog.info(DOMAIN, 'InputDevice', \`Device event info: %{public}s\`, JSON.stringify(data));
                inputDevice.getKeyboardType(data.deviceId).then((type) => {
                  hilog.info(DOMAIN, 'InputDevice', 'The keyboard type is: %{public}d', type);
                  if (type === inputDevice.KeyboardType.ALPHABETIC\_KEYBOARD && data.type === 'add') {
                    // The physical keyboard is inserted.
                    this.isPhysicalKeyboardExist = true;
                    this.keyBoards.set(data.deviceId, type);
                  }
                });
                if (this.keyBoards.get(data.deviceId) === inputDevice.KeyboardType.ALPHABETIC\_KEYBOARD &&
                  data.type === 'remove') {
                  // The physical keyboard is removed.
                  this.isPhysicalKeyboardExist = false;
                  this.keyBoards.delete(data.deviceId);
                }
              });
              this.message = "Device monitoring enabled successfully"
            } catch (error) {
              hilog.error(DOMAIN, 'InputDevice', \`Execute failed, error: %{public}s\`,
                JSON.stringify(error, \["code", "message"\]));
              this.message = \`Failed to enable device monitoring. Click to retry. Error message:${JSON.stringify(error,
                \["code", "message"\])}\`
            }
          })
          // ...
      }
      // ...
    }
  }
}
