# @ohos.vibrator (Vibrator)

The **vibrator** module allows precise control over the vibration of device vibrators. With the APIs provided by this module, you can start vibration in various modes such as specified duration, preset effect, and custom effect and stop any or all of them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/tNvlIWN7S6iAV7rdh2CAKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062411Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91B342CF651E0F50AB71F0C47554439EBB14108F57E55A37FEFF7C12AF5DA90A)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { vibrator } from '@kit.SensorServiceKit';

#### vibrator.startVibration9+

startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>): void

Starts vibration based on a specified effect and attribute. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.VIBRATE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [VibrateEffect](#vibrateeffect9) | Yes | 
Vibration effect. The following options are supported:

1\. [VibratePreset](#vibratepreset9): triggers vibration according to preset vibration effects. This mode is suitable for short vibration scenarios in interactive feedback (such as tapping, long-pressing, sliding, dragging, etc.). This API is recommended to maintain consistency with the system's overall vibration feedback experience.

2\. [VibrateFromFile](#vibratefromfile10): triggers vibration according to custom vibration configuration file. This mode is suitable for interactive feedback in complex scenarios requiring precise vibration patterns (such as realistic effects triggered by emoji packs, or feedback for in-game actions/mechanics).

3\. [VibrateTime](#vibratetime9): triggers vibration of the specified duration, providing basic control over the start and stop of vibration. This mode does not support customization of vibration intensity, frequency, or other parameters. As a result, the vibration adjustment is relatively coarse and not suitable for delivering a refined experience.

4\. [VibrateFromPattern18+](#vibratefrompattern18): starts vibration according to a custom vibration pattern. The usage scenario is the same as **VibrateFromFile**. **VibrateFromFile** utilizes predefined effects in a custom configuration file, passing specific vibration events to the API via file descriptors. By contrast, **VibrateFromPattern** enables more flexible vibration event combinations, delivering them to the API as a vibration event array.

 |
| attribute | [VibrateAttribute](#vibrateattribute9) | Yes | Vibration attribute. |
| callback | AsyncCallback<void> | Yes | Callback used to return the operation result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object, which contains the error code and error information. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14600101 | Device operation failed. |

**Example**

1.  Trigger vibration based on a preset effect.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Use try catch to capture possible exceptions.
    try {
      // Check whether 'haptic.notice.success' is supported.
      vibrator.isSupportEffect('haptic.notice.success', (err: BusinessError, state: boolean) => {
        if (err) {
          console.error(\`Failed to query effect. Code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeed in querying effect');
        if (state) {
          try {
            vibrator.startVibration({
              type: 'preset',
              effectId: 'haptic.notice.success',
              count: 1,
            }, {
              usage: 'notification' // The switch control is subject to the selected type.
            }, (error: BusinessError) => {
              if (error) {
                console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
          return;
              }
              console.info('Succeed in starting vibration');
           
            });
          } catch (err) {
            let e: BusinessError = err as BusinessError;
        console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
          }
        }
      })
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
2.  Trigger vibration based on a custom vibration configuration file.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { resourceManager } from '@kit.LocalizationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    const fileName: string = 'xxx.json';
    
    @Entry
    @Component
    struct Index {
      uiContext = this.getUIContext();
    
      build() {
        Row() {
          Column() {
            Button('alarm-file')
              .onClick(() => {
                let rawFd: resourceManager.RawFileDescriptor | undefined = this.uiContext.getHostContext()?.resourceManager.getRawFdSync(fileName);
                if (rawFd != undefined) {
                  try {
                    vibrator.startVibration({
                      type: "file",
                      hapticFd: { fd: rawFd.fd, offset: rawFd.offset, length: rawFd.length }
                    }, {
                      id: 0,
                      usage: 'alarm' // The switch control is subject to the selected type.
                    }, (error: BusinessError) => {
                      if (error) {
                        console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
                        return;
                      }
                      console.info('Succeed in starting vibration');
                    });
                  } catch (err) {
                    let e: BusinessError = err as BusinessError;
                    console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
                  } finally {
                    vibrator.stopVibration();
                    this.uiContext.getHostContext()?.resourceManager.closeRawFdSync(fileName);
                  }
                }
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
3.  Trigger vibration based on a specified duration.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    try {
      vibrator.startVibration({
        type: 'time',
        duration: 1000,
      }, {
        id: 0,
        usage: 'alarm' // The switch control is subject to the selected type.
      }, (error: BusinessError) => {
        if (error) {
          console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
          return;
        }
        console.info('Succeed in starting vibration');
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    

#### vibrator.startVibration9+

startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Promise<void>

Starts vibration based on a specified effect and attribute. This API uses a promise to return the result.

**Required permissions**: ohos.permission.VIBRATE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [VibrateEffect](#vibrateeffect9) | Yes | 
Vibration effect. The following options are supported:

1\. [VibrateTime](#vibratetime9): triggers vibration according to preset vibration effects. This mode is suitable for short vibration scenarios in interactive feedback (such as tapping, long-pressing, sliding, dragging, etc.). This API is recommended to maintain consistency with the system's overall vibration feedback experience.

2\. [VibratePreset](#vibratepreset9): triggers vibration according to custom vibration configuration file. This mode is suitable for interactive feedback in complex scenarios requiring precise vibration patterns (such as realistic effects triggered by emoji packs, or feedback for in-game actions/mechanics).

3\. [VibrateFromFile](#vibratefromfile10): triggers vibration of the specified duration, providing basic control over the start and stop of vibration. This mode does not support customization of vibration intensity, frequency, or other parameters. As a result, the vibration adjustment is relatively coarse and not suitable for delivering a refined experience.

4\. [VibrateFromPattern18+](#vibratefrompattern18): starts vibration according to a custom vibration pattern. The usage scenario is the same as **VibrateFromFile**. **VibrateFromFile** utilizes predefined effects in a custom configuration file, passing specific vibration events to the API via file descriptors. By contrast, **VibrateFromPattern** enables more flexible vibration event combinations, delivering them to the API as a vibration event array.

 |
| attribute | [VibrateAttribute](#vibrateattribute9) | Yes | Vibration attribute. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14600101 | Device operation failed. |

**Example**

1.  Trigger vibration based on a preset effect.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Use try catch to capture possible exceptions.
    try {
      // Check whether 'haptic.notice.success' is supported.
      vibrator.isSupportEffect('haptic.notice.success', (err: BusinessError, state: boolean) => {
        if (err) {
          console.error(\`Failed to query effect. Code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info('Succeed in querying effect');
        if (state) {
          try {
            vibrator.startVibration({
              type: 'preset',
              effectId: 'haptic.notice.success',
              count: 1,
            }, {
              usage: 'notification' // The switch control is subject to the selected type.
            }, (error: BusinessError) => {
              if (error) {
                console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
                return;
              }
              console.info('Succeed in starting vibration');
           
            });
          } catch (err) {
            let e: BusinessError = err as BusinessError;
            console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
          }
        }
      })
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
2.  Trigger vibration based on a custom vibration configuration file.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { resourceManager } from '@kit.LocalizationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    const fileName: string = 'xxx.json';
    
    @Entry
    @Component
    struct Index {
      uiContext = this.getUIContext();
    
      build() {
        Row() {
          Column() {
            Button('alarm-file')
              .onClick(() => {
                let rawFd: resourceManager.RawFileDescriptor | undefined = this.uiContext.getHostContext()?.resourceManager.getRawFdSync(fileName);
                if (rawFd != undefined) {
                  try {
                    vibrator.startVibration({
                      type: "file",
                      hapticFd: { fd: rawFd.fd, offset: rawFd.offset, length: rawFd.length }
                    }, {
                      id: 0,
                      usage: 'alarm' // The switch control is subject to the selected type.
                    }, (error: BusinessError) => {
                      if (error) {
                        console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
                        return;
                      }
                      console.info('Succeed in starting vibration');
                    });
                  } catch (err) {
                    let e: BusinessError = err as BusinessError;
                    console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
                  } finally {
                    vibrator.stopVibration();
                    this.uiContext.getHostContext()?.resourceManager.closeRawFdSync(fileName);
                  }
                }
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
3.  Trigger vibration based on a specified duration.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    try {
      vibrator.startVibration({
        type: 'time',
        duration: 1000
      }, {
        id: 0,
        usage: 'alarm' // The switch control is subject to the selected type.
      }).then(() => {
        console.info('Succeed in starting vibration');
      }, (error: BusinessError) => {
        console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    

#### vibrator.stopVibration9+

stopVibration(stopMode: VibratorStopMode, callback: AsyncCallback<void>): void

Stops vibration in the specified mode. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stopMode | [VibratorStopMode](#vibratorstopmode) | Yes | 
Mode to stop the vibration. The options are as follows:

\- **VIBRATOR\_STOP\_MODE\_TIME**: used to stop vibration of the specified duration.

\- **VIBRATOR\_STOP\_MODE\_PRESET**: used to stop vibration of the preset effect.

To stop custom vibration, use [vibrator.stopVibration10+](#vibratorstopvibration10).

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the vibration stops, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

1.  Stop vibration of the specified duration.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Use try catch to capture possible exceptions.
    try {
      // Start vibration of the specified duration.
      vibrator.startVibration({
        type: 'time',
        duration: 1000,
      }, {
        id: 0,
        usage: 'alarm' // The switch control is subject to the selected type.
      }, (error: BusinessError) => {
        if (error) {
          console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
          return;
        }
        console.info('Succeed in starting vibration');
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
    try {
      // Stop vibration in VIBRATOR\_STOP\_MODE\_TIME mode.
      vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR\_STOP\_MODE\_TIME, (error: BusinessError) => {
        if (error) {
          console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
          return;
        }
        console.info('Succeed in stopping vibration');
      })
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
2.  Stop preset vibration.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    try {
      // Start vibration based on a preset effect.
      vibrator.startVibration({
        type: 'preset',
        effectId: 'haptic.notice.success',
        count: 1,
      }, {
        id: 0,
        usage: 'notification' // The switch control is subject to the selected type.
      }, (error: BusinessError) => {
        if (error) {
          console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
          return;
        }
        console.info('Succeed in starting vibration');
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
    try {
      // Stop vibration in VIBRATOR\_STOP\_MODE\_PRESET mode.
      vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR\_STOP\_MODE\_PRESET, (error: BusinessError) => {
        if (error) {
          console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
          return;
        }
        console.info('Succeed in stopping vibration');
      })
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    

#### vibrator.stopVibration9+

stopVibration(stopMode: VibratorStopMode): Promise<void>

Stops vibration in the specified mode. This API uses a promise to return the result.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stopMode | [VibratorStopMode](#vibratorstopmode) | Yes | 
Vibration stop mode:

\- **VIBRATOR\_STOP\_MODE\_TIME**: used to stop vibration of the specified duration.

\- **VIBRATOR\_STOP\_MODE\_PRESET**: used to stop vibration of the preset effect.

To stop custom vibration, use [vibrator.stopVibration10+](#vibratorstopvibration10-1).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

1.  Stop vibration of the specified duration.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Use try catch to capture possible exceptions.
    try {
      // Start vibration of the specified duration.
      vibrator.startVibration({
        type: 'time',
        duration: 1000,
      }, {
        id: 0,
        usage: 'alarm' // The switch control is subject to the selected type.
      }).then(() => {
        console.info('Succeed in starting vibration');
      }, (error: BusinessError) => {
        console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
    try {
      // Stop vibration in VIBRATOR\_STOP\_MODE\_TIME mode.
      vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR\_STOP\_MODE\_TIME).then(() => {
        console.info('Succeed in stopping vibration');
      }, (error: BusinessError) => {
        console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
2.  Stop preset vibration.
    
    import { vibrator } from '@kit.SensorServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    try {
      // Start vibration based on a preset effect.
      vibrator.startVibration({
        type: 'preset',
        effectId: 'haptic.notice.success',
        count: 1,
      }, {
        id: 0,
        usage: 'notification' // The switch control is subject to the selected type.
      }).then(() => {
        console.info('Succeed in starting vibration');
      }, (error: BusinessError) => {
        console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    
    try {
      // Stop vibration in VIBRATOR\_STOP\_MODE\_PRESET mode.
      vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR\_STOP\_MODE\_PRESET).then(() => {
        console.info('Succeed in stopping vibration');
      }, (error: BusinessError) => {
        console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
    }
    

#### vibrator.stopVibration10+

stopVibration(callback: AsyncCallback<void>): void

Stops vibration in all modes. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.VIBRATE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the vibration stops, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Stop vibration in all modes.
  vibrator.stopVibration((error: BusinessError) => {
    if (error) {
      console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
      return;
    }
    console.info('Succeed in stopping vibration');
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.stopVibration10+

stopVibration(): Promise<void>

Stops vibration in all modes. This API uses a promise to return the result.

**Required permissions**: ohos.permission.VIBRATE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Stop vibration in all modes.
  vibrator.stopVibration().then(() => {
    console.info('Succeed in stopping vibration');
  }, (error: BusinessError) => {
    console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.stopVibration19+

stopVibration(param?: VibratorInfoParam): Promise<void>

Stops vibration based on the specified vibrator parameters. If no parameters are passed, this API stops all vibrators of the local device by default. This API uses a promise to return the result.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | [VibratorInfoParam](#vibratorinfoparam19) | No | Vibrator parameters, such as the specified device and vibrator. If this parameter is left unspecified, this API applies to all vibrators of the local device by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14600101 | Device operation failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function vibratorDemo() {
  // Query information about all vibrators.
  const vibratorInfoList: vibrator.VibratorInfo\[\] = vibrator.getVibratorInfoSync();
  // Obtain the target vibrator based on the actual service logic. The following example shows how to obtain the local vibrator. You need to adjust the filtering logic as required.
  const targetVibrator = vibratorInfoList.find((vibrator: vibrator.VibratorInfo) => {
    return vibrator.isLocalVibrator;
  });
  if (!targetVibrator) {
    return;
  }
  // Call vibrator.startVibration to start vibration.
  // ...

  // Use try catch to capture possible exceptions.
  try {
    // Stop the vibration based on the actual service scenario.
    vibrator.stopVibration({ deviceId: targetVibrator.deviceId, vibratorId: targetVibrator.vibratorId }).then(() => {
      console.info('Succeed in stopping vibration');
    }, (error: BusinessError) => {
      console.error(\`Failed to stop vibration. Code: ${error.code}, message: ${error.message}\`);
    });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
  }
}

#### vibrator.stopVibrationSync12+

stopVibrationSync(): void

Stops any form of motor vibration.

**Required permissions**: ohos.permission.VIBRATE

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Sensors.MiscDevice

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14600101 | Device operation failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Stop any form of motor vibration.
  vibrator.stopVibrationSync()
  console.info('Succeed in stopping vibration');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.isSupportEffect10+

isSupportEffect(effectId: string, callback: AsyncCallback<boolean>): void

Checks whether an effect ID is supported. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effectId | string | Yes | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means that the effect ID is supported, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether 'haptic.notice.success' is supported.
  vibrator.isSupportEffect('haptic.notice.success', (err: BusinessError, state: boolean) => {
    if (err) {
      console.error(\`Failed to query effect. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeed in querying effect');
    if (state) {
      try {
        // To use startVibration, you must configure the ohos.permission.VIBRATE permission.
        vibrator.startVibration({
          type: 'preset',
          effectId: 'haptic.notice.success',
          count: 1,
        }, {
          usage: 'unknown' // The switch control is subject to the selected type.
        }, (error: BusinessError) => {
          if (error) {
            console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
          } else {
            console.info('Succeed in starting vibration');
          }
        });
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
      }
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.isSupportEffect10+

isSupportEffect(effectId: string): Promise<boolean>

Checks whether an effect ID is supported. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effectId | string | Yes | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise that returns the result. The value **true** means that the effect ID is supported, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether 'haptic.notice.success' is supported.
  vibrator.isSupportEffect('haptic.notice.success').then((state: boolean) => {
    console.info(\`The query result is ${state}\`);
    if (state) {
      try {
        vibrator.startVibration({
          type: 'preset',
          effectId: 'haptic.notice.success',
          count: 1,
        }, {
          usage: 'unknown' // The switch control is subject to the selected type.
        }).then(() => {
          console.info('Succeed in starting vibration');
        }).catch((error: BusinessError) => {
          console.error(\`Failed to start vibration. Code: ${error.code}, message: ${error.message}\`);
        });
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
      }
    }
  }, (error: BusinessError) => {
    console.error(\`Failed to query effect. Code: ${error.code}, message: ${error.message}\`);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.isSupportEffectSync12+

isSupportEffectSync(effectId: string): boolean

Checks whether the preset vibration effect is supported.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effectId | string | Yes | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returned object. The value **true** means that the effect ID is supported, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14600101 | Device operation failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether the preset 'haptic.notice.success' is supported.
  let ret = vibrator.isSupportEffectSync('haptic.notice.success');
  console.info(\`The query result is ${ret}\`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.getEffectInfoSync19+

getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo

Obtains the preset vibration effect based on the device ID and vibrator ID to determine whether the preset vibration effect is supported.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effectId | string | Yes | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. |
| param | [VibratorInfoParam](#vibratorinfoparam19) | No | Device ID and vibrator ID. If this parameter is left unspecified, this API applies to the local device by default. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14600101 | Device operation failed. |

**Return value**

| Type | Description |
| :-- | :-- |
| [EffectInfo](#effectinfo19) | Whether the preset vibration effect is supported. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  const effectInfo: vibrator.EffectInfo = vibrator.getEffectInfoSync('haptic.clock.timer', { deviceId: 1, vibratorId: 3});
  console.info(\`isEffectSupported: ${effectInfo.isEffectSupported}\`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.getVibratorInfoSync19+

getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>;

Queries the vibrator list of one or all devices.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | [VibratorInfoParam](#vibratorinfoparam19) | No | Vibrator parameters, such as the specified device and vibrator. If this parameter is left unspecified, this API applies to all vibrators of the local device by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[VibratorInfo](#vibratorinfo19)\> | Vibrator information. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const vibratorInfoList: vibrator.VibratorInfo\[\] = vibrator.getVibratorInfoSync({ deviceId: 1, vibratorId: 3 });
  console.info(\`vibratorInfoList: ${JSON.stringify(vibratorInfoList)}\`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.on19+

on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void

Enables listening for vibrator status changes.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'vibratorStateChange' | Yes | Event type. The value **vibratorStateChange** indicates a vibrator online/offline event. |
| callback | Callback<[VibratorStatusEvent](#vibratorstatusevent19)\> | Yes | Callback used to return the vibrator status change event. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14600101 | Device operation failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Callback
const vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
  console.info('vibrator state callback info:', JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  // Subscribe to vibratorStateChange events.
  vibrator.on('vibratorStateChange', vibratorStateChangeCallback);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### vibrator.off19+

off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void

Disables listening for vibrator status changes.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'vibratorStateChange' | Yes | Event type. The value **vibratorStateChange** indicates a vibrator online/offline event. |
| callback | Callback<[VibratorStatusEvent](#vibratorstatusevent19)\> | No | Callback used to return the vibrator status change event. If this parameter is not specified, all callbacks of vibrator status change events will be unregistered. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14600101 | Device operation failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Callback
const vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
  console.info('vibrator state callback info:', JSON.stringify(data));
}
// Use try catch to capture possible exceptions.
try {
  // Unsubscribe from specified vibratorStateChange events.
  vibrator.off('vibratorStateChange', vibratorStateChangeCallback);
  // Unsubscribe from all vibratorStateChange events.
  // vibrator.off('vibratorStateChange');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### VibratorStatusEvent19+

Defines the vibrator status change event.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timestamp | number | No | No | Event timestamp. |
| deviceId | number | No | No | Device ID. |
| vibratorCount | number | No | No | Number of vibrators on the device. |
| isVibratorOnline | boolean | No | No | Vibrator status. The value **true** indicates that the device is online, and the value **false** indicates the opposite. |

#### VibratorInfoParam19+

Defines the vibrator parameters. If **VibratorInfoParam** is left unspecified, an API applies to all vibrators of the local device by default.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | number | No | Yes | Device ID. The default value is **\-1**, indicating the local device. Since API version 19, you can use [getVibratorInfoSync](#vibratorgetvibratorinfosync19) or [on](#vibratoron19) to query the device ID. |
| vibratorId | number | No | Yes | Vibrator ID. The default value is **0**, which indicates all vibrators of the local device. Since API version 19, you can use [getVibratorInfoSync](#vibratorgetvibratorinfosync19) or [on](#vibratoron19) to query the vibrator ID. |

#### EffectInfo19+

Defines the preset effect.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isEffectSupported | boolean | No | No | Whether the preset effect is supported. The value **true** indicates that the preset effect is supported, and the value **false** indicates the opposite. |

#### VibratorInfo19+

Defines the vibrator information.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | number | No | No | Device ID. |
| vibratorId | number | No | No | Vibrator ID. |
| deviceName | string | No | No | Device name. |
| isHdHapticSupported | boolean | No | No | Whether HD vibration is supported. The value **true** indicates that HD vibration is supported, and the value **false** indicates the opposite. |
| isLocalVibrator | boolean | No | No | Whether the device is a local device. The value **true** indicates that the device is a local device, and the value **false** indicates the opposite. |

#### vibrator.isHdHapticSupported12+

isHdHapticSupported(): boolean

Checks whether HD vibration is supported.

**System capability**: SystemCapability.Sensors.MiscDevice

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value indicating whether HD vibration is supported. The value **true** indicates that HD vibration is supported, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Vibrator Error Codes](../../error-codes/vibrator-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14600101 | Device operation failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether HD vibration is supported.
  let ret = vibrator.isHdHapticSupported();
  console.info(\`The query result is ${ret}\`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### VibratorPatternBuilder18+

#### \[h2\]vibrator('addContinuousEvent')18+

addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder;

Adds a long vibration event as a **VibratorPattern** object.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| time | number | Yes | Start time of the long vibration event, in ms. The value range is \[0, 1800000\]. |
| duration | number | Yes | Duration of the long vibration event, in ms. The value range is (0,5000\]. |
| options | [ContinuousParam](#continuousparam18) | No | Optional parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| VibratorPatternBuilder | **VibratorPatternBuilder** object representing a long vibration event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let builder = new vibrator.VibratorPatternBuilder();
// Use try catch to capture possible exceptions.
try {
  let pointsMe: vibrator.VibratorCurvePoint\[\] = \[
    { time: 0, intensity: 0, frequency: -7 },
    { time: 42, intensity: 1, frequency: -6 },
    { time: 128, intensity: 0.94, frequency: -4 },
    { time: 217, intensity: 0.63, frequency: -14 },
    { time: 763, intensity: 0.48, frequency: -14 },
    { time: 1125, intensity: 0.53, frequency: -10 },
    { time: 1503, intensity: 0.42, frequency: -14 },
    { time: 1858, intensity: 0.39, frequency: -14 },
    { time: 2295, intensity: 0.34, frequency: -17 },
    { time: 2448, intensity: 0.21, frequency: -14 },
    { time: 2468, intensity: 0, frequency: -21 }
  \] // No less than four VibratorCurvePoint objects must be set. The maximum value is 16.
  let param: vibrator.ContinuousParam = {
    intensity: 97,
    frequency: 34,
    points:pointsMe,
    index: 0
  }
  builder.addContinuousEvent(0, 2468, param);
  console.info(\`addContinuousEvent builder is ${builder.build()}\`);
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Exception. Code ${e.code}\`);
}

#### \[h2\]vibrator('addTransientEvent')18+

addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder;

Adds a short vibration event as a **VibratorPattern** object.

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| time | number | Yes | Start time of the short vibration event, in ms. The value range is \[0, 1800000\]. |
| options | [TransientParam](#transientparam18) | No | Optional parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| VibratorPatternBuilder | **VibratorPatternBuilder** object representing a short vibration event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let builder = new vibrator.VibratorPatternBuilder();
// Use try catch to capture possible exceptions.
try {
  let param: vibrator.TransientParam = {
    intensity: 80,
    frequency: 70,
    index: 0
  }
  builder.addTransientEvent(0, param);
  console.info(\`addTransientEvent builder is ${builder.build()}\`);
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]vibrator('build')18+

build(): VibratorPattern;

Constructor used to create a **VibratorPattern** object, which determines the vibration sequence of short or long events.

**System capability**: SystemCapability.Sensors.MiscDevice

**Return value**

| Type | Description |
| :-- | :-- |
| [VibratorPattern](#vibratorpattern18) | **VibratorPattern** object. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let builder = new vibrator.VibratorPatternBuilder();
try {
  let param: vibrator.TransientParam = {
    intensity: 80,
    frequency: 70,
    index: 0
  }
  builder.addTransientEvent(0, param);
  console.info(\`addTransientEvent builder is ${builder.build()}\`);
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}
try {
  vibrator.startVibration({
    type: "pattern",
    pattern: builder.build()
  }, {
  usage: "alarm", // The switch control is subject to the selected type.
  }, (error) => {
  if (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Vibrate fail. Code: ${e.code}, message: ${e.message}\`);
  } else {
    console.info(\`vibrate success\`);
  }
  });
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`An unexpected error occurred. Code: ${e.code}, message: ${e.message}\`);
}

#### EffectId

Enumerates the preset vibration effect IDs. This parameter is needed when you call [vibrator.startVibration9+](#vibratorstartvibration9) or [vibrator.stopVibration9+](#vibratorstopvibration9-1) to deliver the vibration effect specified by [VibratePreset](#vibratepreset9). This parameter supports a variety of values, such as **haptic.clock.timer**. [HapticFeedback12+](#hapticfeedback12) provides several frequently used **EffectId** values.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qbnBbrgGTyeE-mpV-7F72Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062411Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A1190574C856FF8B2D1EAD6F79276C349EEA8C1BD90DBA310CBCCD33C30659C)

Preset effects vary according to devices. You are advised to call [vibrator.isSupportEffect](#vibratorissupporteffect10-1)10+ to check whether the device supports the preset effect before use.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| EFFECT\_CLOCK\_TIMER | 'haptic.clock.timer' | Vibration effect when a user adjusts the timer. |

#### HapticFeedback12+

Defines the vibration effect. The frequency of the same vibration effect may vary depending on the vibrator, but the frequency trend remains consistent. These vibration effects correspond to the specific **EffectId** values. For details, see the sample code that demonstrates how to use [vibrator.startVibration9+](#vibratorstartvibration9) or [vibrator.stopVibration9+](#vibratorstopvibration9-1) to deliver the vibration effect defined by [VibratePreset](#vibratepreset9).

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| EFFECT\_SOFT | 'haptic.effect.soft' | Soft vibration, low frequency. |
| EFFECT\_HARD | 'haptic.effect.hard' | Hard vibration, medium frequency. |
| EFFECT\_SHARP | 'haptic.effect.sharp' | Sharp vibration, high frequency. |
| EFFECT\_NOTICE\_SUCCESS18+ | 'haptic.notice.success' | Vibration for a success notification. |
| EFFECT\_NOTICE\_FAILURE18+ | 'haptic.notice.fail' | Vibration for a failure notification. |
| EFFECT\_NOTICE\_WARNING18+ | 'haptic.notice.warning' | Vibration for an alert. |

#### VibratorStopMode

Enumerates vibration stop modes. This parameter is required for [vibrator.stopVibration9+](#vibratorstopvibration9) or [vibrator.stopVibration9+](#vibratorstopvibration9-1). The stop mode must match that delivered in [VibrateEffect9+](#vibrateeffect9).

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| VIBRATOR\_STOP\_MODE\_TIME | 'time' | The vibration to stop is in **duration** mode. |
| VIBRATOR\_STOP\_MODE\_PRESET | 'preset' | The vibration to stop is in **EffectId** mode. |

#### VibrateEffect9+

type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern

Enumerates vibration effects of the vibrator. You can specify the vibration effect when calling [vibrator.startVibration9+](#vibratorstartvibration9) or [vibrator.startVibration9+](#vibratorstartvibration9-1).

**System capability**: SystemCapability.Sensors.MiscDevice

| Type | Description |
| :-- | :-- |
| [VibrateTime](#vibratetime9) | 
Triggers vibration based on a specified duration.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| [VibratePreset](#vibratepreset9) | Triggers vibration based on a preset effect. |
| [VibrateFromFile](#vibratefromfile10) | Triggers vibration based on a custom vibration configuration file. |
| [VibrateFromPattern18+](#vibratefrompattern18) | Triggers vibration based on a custom effect. |

#### VibrateTime9+

Represents vibration of the specified duration.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | 'time' | No | No | The value is **time**, indicating vibration of the specified duration. |
| duration | number | No | No | Vibration duration, in ms. The value range is (0,1800000\]. The maximum vibration duration varies with devices due to different component protection design specifications of drivers provided by different vendors. It is recommended that a single vibration duration be less than or equal to 10s to maximize user experience. |

#### VibratePreset9+

Represents the preset vibration effect. You can pass **VibratePreset** to [VibrateEffect9+](#vibrateeffect9) to specify a preset vibration effect when calling [vibrator.startVibration9+](#vibratorstartvibration9) or [vibrator.startVibration9+](#vibratorstartvibration9-1).

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | 'preset' | No | No | The value **preset** means that vibration is triggered based on the specified effect. |
| effectId | string | No | No | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. |
| count | number | No | Yes | Number of repeated vibrations. This parameter is optional. The default value is **1**. |
| intensity12+ | number | No | Yes | Vibration intensity. This parameter is optional. The value range is \[0, 100\]. The default value is **100**. If vibration intensity adjustment is not supported, the default vibration intensity will be used. |

#### VibrateFromFile10+

Represents a custom vibration pattern. It is supported only by certain devices. An error code will be returned if a device does not support this vibration mode. You can pass **VibrateFromFile** to [VibrateEffect9+](#vibrateeffect9) to specify a custom vibration pattern when calling [vibrator.startVibration9+](#vibratorstartvibration9) or [vibrator.startVibration9+](#vibratorstartvibration9-1).

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | 'file' | No | No | The value **file** means vibration according to a vibration configuration file. |
| hapticFd | [HapticFileDescriptor](#hapticfiledescriptor10)10+ | No | No | File descriptor (FD) of the vibration configuration file. |

#### HapticFileDescriptor10+

Describes the FD of a custom vibration configuration file. Ensure that the file is available, and the parameters in it can be obtained from the sandbox path through the [fileIo.open](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen) API or from the HAP resource through the [getRawFd](../../../../../application-framework/localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getrawfd9) API. The application scenario is as follows: The vibration sequence is stored in a file and vibration needs to be triggered based on the offset and length. For details about the storage format of the vibration sequence, see [Vibration Effect Description](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/vibrator-guidelines#vibration-effect-description).

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | No | No | FD of the custom vibration configuration file. |
| offset | number | No | Yes | Offset from the start position of the file, in bytes. The default value is the start position of the file, and the value cannot exceed the valid range of the file. |
| length | number | No | Yes | Resource length, in bytes. The default value is the length from the offset position to the end of the file, and the value cannot exceed the valid range of the file. |

#### VibratorEventType18+

Vibration event type.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTINUOUS | 0 | Long vibration. |
| TRANSIENT | 1 | Short vibration. |

#### VibratorCurvePoint18+

Defines the gain relative to the vibration intensity.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| time | number | No | No | Start time offset. |
| intensity | number | No | Yes | Gain relative to the vibration intensity. This parameter is optional. The value range is \[0,100%\]. If this parameter is left empty, the default value is **1**. |
| frequency | number | No | Yes | Change relative to the vibration frequency. This parameter is optional. The value range is \[-100,100\]. If this parameter is left empty, the default value is **0**. |

#### VibratorEvent18+

Vibration event.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eventType | VibratorEventType | No | No | Vibration event type. |
| time | number | No | No | Vibration start time, in ms. The value range is \[0,1800000\]. |
| duration | number | No | Yes | Vibration duration. This parameter is optional. The value range is (0,5000\]. The default value is **48** for short vibration and **1000** for long vibration. |
| intensity | number | No | Yes | Vibration intensity. This parameter is optional. The value range is \[0,100\]. If this parameter is left empty, the default value is **100**. |
| frequency | number | No | Yes | Vibration frequency. This parameter is optional. The value range is \[0,100\]. If this parameter is left empty, the default value is **50**. |
| index | number | No | Yes | Channel number. This parameter is optional. The value range is \[0,2\]. If this parameter is left empty, the default value is **0**. |
| points | Array<[VibratorCurvePoint](#vibratorcurvepoint18)\> | No | Yes | Adjustment points of the vibration curve. |

#### VibratorPattern18+

Defines the vibration sequence.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| time | number | No | No | Absolute vibration start time. |
| events | Array<[VibratorEvent](#vibratorevent18)\> | No | No | Vibration event array, which is the **VibratorPattern** object returned by \*\*build() \*\*. |

#### ContinuousParam18+

Defines the parameters for continuous vibration.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| intensity | number | No | Yes | Vibration intensity. This parameter is optional. The value range is \[0,100\]. If this parameter is left empty, the default value is **100**. |
| frequency | number | No | Yes | Vibration frequency. This parameter is optional. The value range is \[0,100\]. If this parameter is left empty, the default value is **50**. |
| points | [VibratorCurvePoint](#vibratorcurvepoint18)\[\] | No | Yes | Adjustment points of the vibration curve. |
| index | number | No | Yes | Channel number. This parameter is optional. The value range is \[0,2\]. If this parameter is left empty, the default value is **0**. |

#### TransientParam18+

Defines the parameters for transient vibration.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| intensity | number | No | Yes | Vibration intensity. This parameter is optional. The value range is \[0,100\]. If this parameter is left empty, the default value is **100**. |
| frequency | number | No | Yes | Vibration frequency. This parameter is optional. The value range is \[0,100\]. If this parameter is left empty, the default value is **50**. |
| index | number | No | Yes | Channel number. This parameter is optional. The value range is \[0,2\]. If this parameter is left empty, the default value is **0**. |

#### VibrateFromPattern18+

Defines the custom vibration effect.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | 'pattern' | No | No | If the value is **pattern**, the vibrator vibrates based on the specified pattern. |
| pattern | VibratorPattern | No | No | Vibration event array, which is the **VibratorPattern** object returned by \*\*build() \*\*. |

#### VibrateAttribute9+

Describes the vibration attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | No | Yes | Vibrator ID. The default value is **0**. |
| deviceId19+ | number | No | Yes | 
Device ID. The default value is **\-1**, indicating the local device. Since API version 19, you can use [getVibratorInfoSync](#vibratorgetvibratorinfosync19) or [on](#vibratoron19) to query the device ID.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| usage | [Usage](#usage9) | No | No | Vibration scenario. The default value is **unknown**. The value must be an enum defined in [Usage](#usage9). |

#### Usage9+

type Usage = 'unknown' | 'alarm' | 'ring' | 'notification' | 'communication' | 'touch' | 'media' | 'physicalFeedback' | 'simulateReality'

Enumerates the vibration scenarios.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.MiscDevice

| Type | Description |
| :-- | :-- |
| 'unknown' | Unknown vibration scenario, lowest priority. This parameter has a fixed value of unknown. Vibration is controlled by the haptic switch and will not occur when the switch is disabled. |
| 'alarm' | Alarm vibration scenario. This parameter has a fixed value of alarm. Vibration is controlled by the three-way switch and will not occur when the switch is in mute mode. |
| 'ring' | Ringing vibration scenario. This parameter has a fixed value of ring. Vibration is controlled by the three-way switch and will not occur when the switch is in mute mode. |
| 'notification' | Notification vibration scenario. This parameter has a fixed value of notification. Vibration is controlled by the three-way switch and will not occur when the switch is in mute mode. |
| 'communication' | Communication vibration scenario. This parameter has a fixed value of communication. Vibration is controlled by the three-way switch and will not occur when the switch is in mute mode. |
| 'touch' | Touch vibration scenario. This parameter has a fixed value of touch. Vibration is controlled by the haptic switch and will not occur when the switch is disabled. |
| 'media' | Multimedia vibration scenario. This parameter has a fixed value of media. Vibration is controlled by the haptic switch and will not occur when the switch is disabled. |
| 'physicalFeedback' | Physical feedback vibration scenario. This parameter has a fixed value of physicalFeedback. Vibration is controlled by the haptic switch and will not occur when the switch is disabled. |
| 'simulateReality' | Simulated reality vibration scenario. This parameter has a fixed value of simulateReality. Vibration is controlled by the haptic switch and will not occur when the switch is disabled. |

#### vibrator.vibrate(deprecated)

vibrate(duration: number): Promise<void>

Triggers vibration based on a specified duration. This API uses a promise to return the result.

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [vibrator.startVibration](#vibratorstartvibration9-1)9+ instead.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| duration | number | Yes | Vibration duration, in ms. The value range is (0,1800000\]. The maximum vibration duration varies with devices due to different component protection design specifications of drivers provided by different vendors. It is recommended that a single vibration duration be less than or equal to 10s to maximize user experience. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the result. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(1000).then(() => {
  console.info('Succeed in vibrating');
}, (error: BusinessError) => {
  console.error(\`Failed to vibrate. Code: ${error.code}, message: ${error.message}\`);
});

#### vibrator.vibrate(deprecated)

vibrate(duration: number, callback?: AsyncCallback<void>): void

Triggers vibration based on a specified duration. This API uses an asynchronous callback to return the result.

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [vibrator.startVibration](#vibratorstartvibration9)9+ instead.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| duration | number | Yes | Vibration duration, in ms. The value range is (0,1800000\]. The maximum vibration duration varies with devices due to different component protection design specifications of drivers provided by different vendors. It is recommended that a single vibration duration be less than or equal to 10s to maximize user experience. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If the vibration starts, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(1000, (error: BusinessError) => {
  if (error) {
    console.error(\`Failed to vibrate. Code: ${error.code}, message: ${error.message}\`);
  } else {
    console.info('Succeed in vibrating');
  }
})

#### vibrator.vibrate(deprecated)

vibrate(effectId: EffectId): Promise<void>

Triggers vibration based on a specified effect. This API uses a promise to return the result.

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [vibrator.startVibration](#vibratorstartvibration9-1)9+ instead.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effectId | [EffectId](#effectid) | Yes | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. You are advised to check whether the effect ID is supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the result. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(vibrator.EffectId.EFFECT\_CLOCK\_TIMER).then(() => {
  console.info('Succeed in vibrating');
}, (error: BusinessError) => {
  console.error(\`Failed to vibrate. Code: ${error.code}, message: ${error.message}\`);
});

#### vibrator.vibrate(deprecated)

vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void

Triggers vibration based on a specified effect. This API uses an asynchronous callback to return the result.

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [vibrator.startVibration](#vibratorstartvibration9)9+ instead.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effectId | [EffectId](#effectid) | Yes | Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64 characters are used. You are advised to check whether the effect ID is supported. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If the vibration starts, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(vibrator.EffectId.EFFECT\_CLOCK\_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(\`Failed to vibrate. Code: ${error.code}, message: ${error.message}\`);
  } else {
    console.info('Succeed in vibrating');
  }
})

#### vibrator.stop(deprecated)

stop(stopMode: VibratorStopMode): Promise<void>

Stops vibration in the specified mode. This API uses a promise to return the result.

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [vibrator.stopVibration](#vibratorstopvibration9-1)9+ instead.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stopMode | [VibratorStopMode](#vibratorstopmode) | Yes | Mode to stop the vibration. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the result. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Start vibration based on the specified effect ID.
vibrator.vibrate(vibrator.EffectId.EFFECT\_CLOCK\_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(\`Failed to vibrate. Code: ${error.code}, message: ${error.message}\`);
  } else {
    console.info('Succeed in vibrating');
  }
})
// Stop vibration in VIBRATOR\_STOP\_MODE\_PRESET mode.
vibrator.stop(vibrator.VibratorStopMode.VIBRATOR\_STOP\_MODE\_PRESET).then(() => {
  console.info('Succeed in stopping');
}, (error: BusinessError) => {
  console.error(\`Failed to stop. Code: ${error.code}, message: ${error.message}\`);
});

#### vibrator.stop(deprecated)

stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void

Stops vibration in the specified mode. This API uses an asynchronous callback to return the result.

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [vibrator.stopVibration](#vibratorstopvibration9)9+ instead.

**Required permissions**: ohos.permission.VIBRATE

**System capability**: SystemCapability.Sensors.MiscDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stopMode | [VibratorStopMode](#vibratorstopmode) | Yes | Mode to stop the vibration. |
| callback | AsyncCallback<void> | No | Callback used to return the result. If the vibration stops, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Start vibration based on the specified effect ID.
vibrator.vibrate(vibrator.EffectId.EFFECT\_CLOCK\_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(\`Failed to vibrate. Code: ${error.code}, message: ${error.message}\`);
  } else {
    console.info('Succeed in vibrating');
  }
})
// Stop vibration in VIBRATOR\_STOP\_MODE\_PRESET mode.
vibrator.stop(vibrator.VibratorStopMode.VIBRATOR\_STOP\_MODE\_PRESET, (error: BusinessError) => {
  if (error) {
    console.error(\`Failed to stop. Code: ${error.code}, message: ${error.message}\`);
  } else {
    console.info('Succeed in stopping');
  }
})
