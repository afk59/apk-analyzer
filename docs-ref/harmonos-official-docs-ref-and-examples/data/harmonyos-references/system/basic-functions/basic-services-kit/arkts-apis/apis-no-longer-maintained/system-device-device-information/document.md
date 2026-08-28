# @system.device (Device Information)

The **device** module provides APIs for checking information about the current device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/T8SdZtEFTAKEigjZQPBzQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27916C27A4F4241EEE8284795AC039D8F913DF0EE698AA1DA63FDE20F7ED3FD1)

-   The APIs of this module are no longer maintained since API version 6. You are advised to use [@ohos.deviceInfo](../../device-management/ohos-deviceinfo-device-information/document.md) to query device information.
    
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import device from '@system.device';

#### device.getInfo(deprecated)

getInfo(options?: GetDeviceOptions): void

Obtains the device information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/mYOMUngHQ1qAPMQbZiQPMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26127E3D71337A7454494377785E44AC3DE75527726B2B4A4E2FF25C68573D8D)

Do not call **device.getInfo** before the **onShow** event of the home page.

**System capability**: SystemCapability.Startup.SystemInfo.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetDeviceOptions](#getdeviceoptionsdeprecated) | No | Parameters for obtaining the device information. |

#### GetDeviceOptions(deprecated)

Defines the parameters for obtaining the device information.

**System capability**: SystemCapability.Startup.SystemInfo.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | (data: DeviceResponse) => void | No | Called when an API call is successful. **data** indicates the returned device information. For details, see [DeviceResponse](#deviceresponsedeprecated). |
| fail | (data: any,code:number)=> void | No | 
Called when an API call has failed. **code** indicates the error code returned upon a failure.

**code:200**: Certain information could not be obtained.

 |
| complete | () => void | No | Called when an API call is complete. |

#### DeviceResponse(deprecated)

Defines the device information.

**System capability**: SystemCapability.Startup.SystemInfo.Lite

| Name | Type | Description |
| :-- | :-- | :-- |
| brand | string | Brand. |
| manufacturer | string | Manufacturer. |
| model | string | Model. |
| product | string | Product number. |
| language4+ | string | System language. |
| region4+ | string | System region. |
| windowWidth | number | Window width. |
| windowHeight | number | Window height. |
| screenDensity4+ | number | Screen density. |
| screenShape4+ | string | 
Screen shape. The options are as follows:

\- **rect**: rectangular screen

\- **circle**: round screen

 |
| apiVersion4+ | number | API version. |
| deviceType4+ | string | Device type. |

**Example**

export default class Page {
  getInfo() {
    interface DeviceData {
      brand: string;
    }

    try {
      device.getInfo({
        success: (data: DeviceData) => {
          console.info('Device information obtained successfully. Device brand:' + data.brand);
        },
        fail: (data: string, code: number) => {
          console.info('Failed to obtain device information. Error code:' + code + '; Error information: ' + data);
        },
      });
    } catch (error) {
      console.error('Device information API is not supported');
    }
  }
}
