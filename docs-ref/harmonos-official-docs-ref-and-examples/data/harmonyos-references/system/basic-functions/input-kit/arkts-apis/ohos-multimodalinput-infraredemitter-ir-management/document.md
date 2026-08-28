# @ohos.multimodalInput.infraredEmitter (IR Management)

The **infraredEmitter** module generates IR signals of the specified frequency and size, and queries the frequency range supported by the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/fk21ZB3bSg64IC_ikVKR9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062404Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D811C78DFC5BA7CF7FC1A05F25227530509FACFC9C9E79C775AA3AD10661EEBA)

-   The initial APIs of this module are supported since API version 15. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { infraredEmitter } from '@kit.InputKit';

#### infraredEmitter.transmitInfrared

transmitInfrared(infraredFrequency: number, pattern: Array<number>): void

Generates IR signals at the specified frequency and level.

**Required permissions**: ohos.permission.MANAGE\_INPUT\_INFRARED\_EMITTER

**System capability**: SystemCapability.MultimodalInput.Input.InfraredEmitter

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| infraredFrequency | number | Yes | IR frequency, in Hz. |
| pattern | Array<number> | Yes | 
IR level signal, in μs. The value range of the number of level signals is \[0, 1024\]. The value of the level signal must be greater than 0.

For example, in the IR level signal array \[100,200,300,400\], 100 μs is a high-level signal, 200 μs is a low-level signal, 300 μs is a high-level signal, and 400 μs is a low-level signal.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |

**Example**

import { infraredEmitter } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            infraredEmitter.transmitInfrared(38000, \[100, 200, 300, 400\]);
          } catch (error) {
            console.error(\`transmitInfrared failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### infraredEmitter.getInfraredFrequencies

getInfraredFrequencies(): Array<InfraredFrequency>

Queries the frequency range of IR signals supported by the device.

**Required permissions**: ohos.permission.MANAGE\_INPUT\_INFRARED\_EMITTER

**System capability**: SystemCapability.MultimodalInput.Input.InfraredEmitter

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[InfraredFrequency](#infraredfrequency)\> | 
Frequency range of IR signals, including multiple groups of maximum and minimum frequencies.

When the device does not have an infrared transmitter, it returns a set of maximum and minimum frequencies, both of which are **0** Hz.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { infraredEmitter } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let frequencies = infraredEmitter.getInfraredFrequencies();
            console.info(\`frequencies: ${JSON.stringify(frequencies)}\`);
          } catch (error) {
            console.error(\`Get infrared frequencies failed, error: ${JSON.stringify(error, \[\`code\`, \`message\`\])}\`);
          }
        })
    }
  }
}

#### InfraredFrequency

Defines the frequency range of IR signals.

**System capability**: SystemCapability.MultimodalInput.Input.InfraredEmitter

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| max | number | No | No | Maximum frequency, in Hz. |
| min | number | No | No | Minimum frequency, in Hz. |
