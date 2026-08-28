# @ohos.multimodalInput.inputDevice (Input Device)

The inputDevice module implements input device management functions such as listening for the connection and disconnection of input devices and querying input device information such as the device name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Mox2b5_aRQCnLuUXJqw_Bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10A22A910E9C699A74A501D96E0AC5FE96CF3C0EC924CDFE33E3E520056533CF)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { inputDevice } from '@kit.InputKit';

#### inputDevice.getDeviceList9+

getDeviceList(callback: AsyncCallback<Array<number>>): void

Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the IDs of all input devices. **id** is the unique ID of an input device. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.getDeviceList((error: BusinessError, ids: Array<Number>) => {
              if (error) {
                console.error(\`Failed to get device id list, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                return;
              }
              console.info(\`Device id list: ${JSON.stringify(ids)}\`);
            });
          } catch (error) {
            console.error(\`Failed to get device id list, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getDeviceList9+

getDeviceList(): Promise<Array<number>>

Obtains the IDs of all input devices. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the IDs of all input devices. **id** is the unique ID of an input device. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.getDeviceList().then((ids: Array<Number>) => {
              console.info(\`Device id list: ${JSON.stringify(ids)}\`);
            }).catch((error: BusinessError) => {
              console.error(\`Failed to get device id list, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            });
          } catch (error) {
            console.error(\`Failed to get device id list, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getDeviceInfo9+

getDeviceInfo(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

Obtains information about the specified input device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| callback | AsyncCallback<[InputDeviceData](#inputdevicedata)\> | Yes | Callback used to return information about the input device, including the device ID, name, supported source, physical address, version information, and product information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          try {
            inputDevice.getDeviceInfo(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
              if (error) {
                console.error(\`Failed to get device info, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                return;
              }
              console.info(\`Device info: ${JSON.stringify(deviceData)}\`);
            });
          } catch (error) {
            console.error(\`Failed to get device info, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getDeviceInfo9+

getDeviceInfo(deviceId: number): Promise<InputDeviceData>

Obtains the information about the input device with the specified ID. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[InputDeviceData](#inputdevicedata)\> | Promise used to return information about the input device, including device ID, name, supported source, physical address, version information, and product information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          try {
            inputDevice.getDeviceInfo(1).then((deviceData: inputDevice.InputDeviceData) => {
              console.info(\`Device info: ${JSON.stringify(deviceData)}\`);
            }).catch((error: BusinessError) => {
              console.error(\`Get device info failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            });
          } catch (error) {
            console.error(\`Failed to get device info, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getDeviceInfoSync10+

getDeviceInfoSync(deviceId: number): InputDeviceData

Obtains information about the specified input device.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value**

| Type | Description |
| :-- | :-- |
| [InputDeviceData](#inputdevicedata) | Information about the input device, including the device ID, name, supported source, physical address, version information, and product information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          try {
            let deviceData: inputDevice.InputDeviceData = inputDevice.getDeviceInfoSync(1);
            console.info(\`Device info: ${JSON.stringify(deviceData)}\`);
          } catch (error) {
            console.error(\`Failed to get device info, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.on('change')9+

on(type: "change", listener: Callback<DeviceListener>): void

Enables listening for device hot swap events. When performing this operation, you need to connect to external devices such as a mouse, keyboard, and touchscreen. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This field has a fixed value of **change**. |
| listener | Callback<[DeviceListener](#devicelistener9)\> | Yes | Listener for events of the input device. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State isPhysicalKeyboardExist: boolean = false;
  @State message: string = "Click to obtain the device list and monitor device hot-plug events";
  keyBoards: Map<number, inputDevice.KeyboardType> = new Map();

  build() {
    RelativeContainer() {
      Column() {
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
      }
    }
  }
}

#### inputDevice.off('change')9+

off(type: "change", listener?: Callback<DeviceListener>): void

Disables listening for device hot swap events. This API is called before the application exits. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This field has a fixed value of **change**. |
| listener | Callback<[DeviceListener](#devicelistener9)\> | No | Callback to unregister. If this parameter is left unspecified, listening for hot swap events of all input devices will be canceled. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let callback = (data: inputDevice.DeviceListener) => {
            console.info(\`Report device event info: ${JSON.stringify(data, \[\`type\`, \`deviceId\`\])}\`);
          };

          try {
            inputDevice.on("change", callback);
          } catch (error) {
            console.error(\`Listen device event failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }

          // Disable this listener.
          try {
            inputDevice.off("change", callback);
          } catch (error) {
            console.error(\`Cancel listening device event failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }

          // Disable all listeners.
          try {
            inputDevice.off("change");
          } catch (error) {
            console.error(\`Cancel all listening device event failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getDeviceIds(deprecated)

getDeviceIds(callback: AsyncCallback<Array<number>>): void

Obtains the IDs of all input devices. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/9T1Y2ouFR56av_NJYIm-3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA8DDAC417995BF0C63A550C04CBB4BDC13CD84A14241DEB055553D6F7420335)

This API is supported since API version 8 and deprecated since API version 9. Use [inputDevice.getDeviceList](#inputdevicegetdevicelist9) instead.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the IDs of all input devices. **id** is the unique ID of an input device. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getDeviceIds((error: BusinessError, ids: Array<Number>) => {
            if (error) {
              console.error(\`Failed to get device id list, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
              return;
            }
            console.info(\`Device id list: ${JSON.stringify(ids)}\`);
          });
        })
    }
  }
}

#### inputDevice.getDeviceIds(deprecated)

getDeviceIds(): Promise<Array<number>>

Obtains the IDs of all input devices. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/BFukx36VT_eDf9-Y--DMLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C2784AD31A4F54A2FE5DEFE79C21ADA13C9FED6E3D8EAB969385B87555824DE)

This API is supported since API version 8 and deprecated since API version 9. Use [inputDevice.getDeviceList](#inputdevicegetdevicelist9) instead.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the IDs of all input devices. **id** is the unique ID of an input device. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getDeviceIds().then((ids: Array<Number>) => {
            console.info(\`Device id list: ${JSON.stringify(ids)}\`);
          }).catch((error: BusinessError) => {
            console.error(\`Failed to get device id list, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          })
        })
    }
  }
}

#### inputDevice.getDevice(deprecated)

getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

Obtains the information about the input device with the specified ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/8dcwnIkWQL6572qbgBzRKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0319C1588184F78E15ACAF22B65F155AA7CA59B3E582600107B188A5FE8C9CF7)

This API is supported since API version 8 and deprecated since API version 9. Use [inputDevice.getDeviceInfo](#inputdevicegetdeviceinfo9) instead.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| callback | AsyncCallback<[InputDeviceData](#inputdevicedata)\> | Yes | Callback used to return information about the input device, including device ID, name, supported source, physical address, version information, and product information. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          inputDevice.getDevice(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
            if (error) {
              console.error(\`Failed to get device info, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
              return;
            }
            console.info(\`Device info: ${JSON.stringify(deviceData)}\`);
          });
        })
    }
  }
}

#### inputDevice.getDevice(deprecated)

getDevice(deviceId: number): Promise<InputDeviceData>

Obtains the information about the input device with the specified ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/UVmDK2TUTPCOk2GLbngBVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E72ED1027C6749D1507F659C924841A766BCAE5B97587BA95929B0DCF65A307B)

This API is supported since API version 8 and deprecated since API version 9. Use [inputDevice.getDeviceInfo](#inputdevicegetdeviceinfo9) instead.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[InputDeviceData](#inputdevicedata)\> | Promise used to return information about the input device, including device ID, name, supported source, physical address, version information, and product information. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Obtain the name of the device whose ID is 1.
          inputDevice.getDevice(1).then((deviceData: inputDevice.InputDeviceData) => {
            console.info(\`Device info: ${JSON.stringify(deviceData)}\`);
          }).catch((error: BusinessError) => {
            console.error(\`Failed to get device info, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          })
        })
    }
  }
}

#### inputDevice.supportKeys9+

supportKeys(deviceId: number, keys: Array<KeyCode>, callback: AsyncCallback <Array<boolean>>): void

Checks whether the input device supports the specified keys. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| keys | Array[<KeyCode>](../ohos-multimodalinput-keycode-keycode/document.md#keycode) | Yes | Keys to be queried. A maximum of five keys can be specified. |
| callback | AsyncCallback<Array<boolean>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            inputDevice.supportKeys(1, \[17, 22, 2055\], (error: BusinessError, supportResult: Array<Boolean>) => {
              console.info(\`Query result: ${JSON.stringify(supportResult)}\`);
            });
          } catch (error) {
            console.error(\`Query failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.supportKeys9+

supportKeys(deviceId: number, keys: Array<KeyCode>): Promise<Array<boolean>>

Checks whether the input device supports the specified keys. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| keys | Array[<KeyCode>](../ohos-multimodalinput-keycode-keycode/document.md#keycode) | Yes | Keys to be queried. A maximum of five keys can be specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<boolean>> | Promise used to return the result. The value **true** indicates that the keycodes are supported, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            inputDevice.supportKeys(1, \[17, 22, 2055\]).then((supportResult: Array<Boolean>) => {
              console.info(\`Query result: ${JSON.stringify(supportResult)}\`);
            }).catch((error: BusinessError) => {
              console.error(\`Query support Keys failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            });
          } catch (error) {
            console.error(\`Query failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.supportKeysSync10+

supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>

Checks whether the input device supports the specified keys.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| keys | Array[<KeyCode>](../ohos-multimodalinput-keycode-keycode/document.md#keycode) | Yes | Keys to be queried. A maximum of five keys can be specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<boolean> | Result indicating whether the input device supports the keycode value. The value **true** indicates yes, and the value **false** indicates no. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, \[17, 22, 2055\])
            console.info(\`Query result: ${JSON.stringify(supportResult)}\`)
          } catch (error) {
            console.error(\`Query failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`)
          }
        })
    }
  }
}

#### inputDevice.getKeyboardType9+

getKeyboardType(deviceId: number, callback: AsyncCallback<KeyboardType>): void

Obtains the keyboard type of the input device, such as full keyboard and numeric keypad. This API uses an asynchronous callback to return the result. The keyboard type of the input device is subject to the result returned by the API.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| callback | AsyncCallback<[KeyboardType](#keyboardtype9)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Query the keyboard type of the input device whose ID is 1.
          try {
            inputDevice.getKeyboardType(1, (error: BusinessError, type: Number) => {
              if (error) {
                console.error(\`Failed to get keyboard type, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
                return;
              }
              console.info(\`Keyboard type: ${JSON.stringify(type)}\`);
            });
          } catch (error) {
            console.error(\`Failed to get keyboard type, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getKeyboardType9+

getKeyboardType(deviceId: number): Promise<KeyboardType>

Obtains the keyboard type of an input device. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[KeyboardType](#keyboardtype9)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Query the keyboard type of the input device whose ID is 1.
          try {
            inputDevice.getKeyboardType(1).then((type: number) => {
              console.info(\`Keyboard type: ${JSON.stringify(type)}\`);
            }).catch((error: BusinessError) => {
              console.error(\`Get keyboard type failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            })
          } catch (error) {
            console.error(\`Failed to get keyboard type, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.getKeyboardTypeSync10+

getKeyboardTypeSync(deviceId: number): KeyboardType

Obtains the keyboard type of the input device.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyboardType](#keyboardtype9) | Keyboard type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Query the keyboard type of the input device whose ID is 1.
          try {
            let type: number = inputDevice.getKeyboardTypeSync(1)
            console.info(\`Keyboard type: ${JSON.stringify(type)}\`)
          } catch (error) {
            console.error(\`Failed to get keyboard type, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`)
          }
        })
    }
  }
}

#### inputDevice.isFunctionKeyEnabled15+

isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>

Checks whether the specified function key (for example, **CapsLock**) is enabled. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| functionKey | [FunctionKey](#functionkey15) | Yes | Type of the function key. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the function key is enabled, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Input Device Error Codes](../../error-codes/input-device-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900002 | There is currently no keyboard device connected. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.isFunctionKeyEnabled(inputDevice.FunctionKey.CAPS\_LOCK).then((state: boolean) => {
              console.info(\`capslock state: ${JSON.stringify(state)}\`);
            }).catch((error: BusinessError) => {
              console.error(\`Get capslock state failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
            })
          } catch (error) {
            console.error(\`Failed to get capslock state, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### inputDevice.setFunctionKeyEnabled15+

setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>

Specifies whether to enable a function key (for example, **CapsLock**). This API uses a promise to return the result.

**Required permissions**: ohos.permission.INPUT\_KEYBOARD\_CONTROLLER

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| functionKey | [FunctionKey](#functionkey15) | Yes | Type of the function key. |
| enabled | boolean | Yes | Status of the function key. The value **true** indicates that the function key is enabled, and the value **false** indicates the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Input Device Error Codes](../../error-codes/input-device-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900002 | There is currently no keyboard device connected. |
| 3900003 | It is prohibited for non-input applications. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS\_LOCK, true).then(() => {
              console.info(\`Set capslock state success\`);
            }).catch((error: BusinessError) => {
              console.error(\`Set capslock state failed, error=${JSON.stringify(error)}\`);
            });
          } catch (error) {
            console.error(\`Set capslock enable error\`);
          }
        })
    }
  }
}

#### inputDevice.getIntervalSinceLastInput14+

getIntervalSinceLastInput(): Promise<number>

Obtains the interval (including the device sleep time) elapsed since the last system input event. This API uses a promise to return the result.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the interval since the last system input event, in μs. |

**Example**

import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getIntervalSinceLastInput().then((timeInterval: number) => {
            console.info(\`Interval since last input: ${JSON.stringify(timeInterval)}\`);
          }).catch((error: BusinessError) => {
            console.error(\`Get interval since last input failed, error: ${JSON.stringify(error)}\`);
          })
        })
    }
  }
}

#### DeviceListener9+

Provides hot swap information about an input device.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ChangedType](#changedtype9) | No | No | Device change type, which indicates whether an input device is inserted or removed. |
| deviceId | number | No | No | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

#### InputDeviceData

Provides information about an input device.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | No | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| name | string | No | No | Name of the input device. |
| sources | Array<[SourceType](#sourcetype9)\> | No | No | Input sources supported by the input device, including the keyboard, mouse, touchscreen, trackball, touchpad, and joystick. |
| axisRanges | Array<[AxisRange](#axisrange)\> | No | No | Axis information of the input device. |
| bus9+ | number | No | No | Bus type of the input device. By default, the bus type reported by the input device prevails. |
| product9+ | number | No | No | Product information of the input device. |
| vendor9+ | number | No | No | Vendor information of the input device. |
| version9+ | number | No | No | Version information of the input device. |
| phys9+ | string | No | No | Physical address of the input device. |
| uniq9+ | string | No | No | Unique ID of the input device. |

#### AxisType9+

type AxisType = 'touchmajor' | 'touchminor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolminor' | 'toolmajor' | 'null'

Defines the axis type of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Type | Description |
| :-- | :-- |
| 'touchmajor' | Major axis of the elliptical touching area. |
| 'touchminor' | Minor axis of the elliptical touching area. |
| 'toolminor' | Minor axis of the tool area. |
| 'toolmajor' | Major axis of the tool area. |
| 'orientation' | Orientation axis. |
| 'pressure' | Pressure axis. |
| 'x' | Horizontal axis. |
| 'y' | Vertical axis. |
| 'null' | None. |

#### AxisRange

Defines the axis range of an input device.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| source | [SourceType](#sourcetype9) | No | No | Input sources supported by the input device, including the keyboard, mouse, touchscreen, trackball, touchpad, and joystick. |
| axis | [AxisType](#axistype9) | No | No | Axis type of an input device. |
| max | number | No | No | Maximum value of the axis. |
| min | number | No | No | Minimum value of the axis. |
| fuzz9+ | number | No | No | Fuzzy value of the axis. |
| flat9+ | number | No | No | Benchmark value of the axis. |
| resolution9+ | number | No | No | Resolution of the axis. |

#### SourceType9+

type SourceType = 'keyboard' | 'mouse' | 'touchpad' | 'touchscreen' | 'joystick' | 'trackball'

Input sources supported by the input device, including the keyboard, mouse, touchscreen, trackball, touchpad, and joystick.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Type | Description |
| :-- | :-- |
| 'keyboard' | The input device is a keyboard. |
| 'touchscreen' | The input device is a touchscreen. |
| 'mouse' | The input device is a mouse. |
| 'trackball' | The input device is a trackball. |
| 'touchpad' | The input device is a touchpad. |
| 'joystick' | The input device is a joystick. |

#### ChangedType9+

type ChangedType = 'add' | 'remove'

Enumerates hot swap events.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Type | Description |
| :-- | :-- |
| 'add' | Device insertion. |
| 'remove' | Device removal. |

#### KeyboardType9+

Enumerates keyboard types.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Keyboard without keys. |
| UNKNOWN | 1 | Keyboard with unknown keys. |
| ALPHABETIC\_KEYBOARD | 2 | Full keyboard. |
| DIGITAL\_KEYBOARD | 3 | Keypad. |
| HANDWRITING\_PEN | 4 | Stylus. |
| REMOTE\_CONTROL | 5 | Remote control. |

#### FunctionKey15+

Enumerates function key types.

**System capability**: SystemCapability.MultimodalInput.Input.InputDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| CAPS\_LOCK | 1 | CapsLock key. This key can be enabled or disabled only for the input keyboard extension. |
