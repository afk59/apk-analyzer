# @ohos.wifiManagerExt (WLAN Extension)

The **wifiManagerExt** module provides WLAN extension APIs for non-universal products.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/m1wBvqZ5Tja3YVPmRMpO_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=800D1D1BDF78745819ED5A33B344A3F862AD1982CA54A25C21681F1A7B058439)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs described in this document are used only for non-universal products, such as routers.

#### Modules to Import

import { wifiManagerExt } from '@kit.ConnectivityKit';

#### wifiManagerExt.enableHotspot(deprecated)

enableHotspot(): void

Enables the WLAN hotspot.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/e664cIdhQpCUzQbJv1T-hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F10933E6CDEB1425FD80E6E066D9F89C20AF883B4BB7801A26DCB78082BAEB69)

This API is supported since API version 9 and deprecated since API version 10.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**Example**

  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      wifiManagerExt.enableHotspot();
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }

#### wifiManagerExt.disableHotspot(deprecated)

disableHotspot(): void

Disables the WLAN hotspot.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/cS7gtADgS-2_sqXnKLKghQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B0272C0911500901ED6505169A6509AE2197B686B440023D357142DF1A2CCBB)

This API is supported since API version 9 and deprecated since API version 10.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**Example**

  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      wifiManagerExt.disableHotspot();
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }

#### wifiManagerExt.getSupportedPowerMode

getSupportedPowerMode(): Promise<Array<PowerMode>>

Obtains the supported power models. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[PowerMode](#powermode)\>> | Promise used to return the power modes obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

#### PowerMode

Enumerates the power modes.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SLEEPING | 0 | Sleeping |
| GENERAL | 1 | General |
| THROUGH\_WALL | 2 | Through\_wall |

#### wifiManagerExt.getSupportedPowerMode

getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void

Obtains the supported power models. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[PowerMode](#powermode)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the power modes obtained. If the operation fails, **err** is not **0**. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**Example**

import { wifiManagerExt } from '@kit.ConnectivityKit';

wifiManagerExt.getSupportedPowerMode((err, data: wifiManagerExt.PowerMode\[\]) => {
    if (err) {
        console.error("get supported power mode info error: ", err);
        return;
    }
    console.info("get supported power mode info: " + JSON.stringify(data));
});

#### wifiManagerExt.getPowerMode

getPowerMode(): Promise<PowerMode>

Obtains the power mode. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PowerMode](#powermode)\> | Promise used to return the power modes obtained. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**Example**

  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      let model = wifiManagerExt.getPowerMode();
      console.info("model info:" + model);
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }

#### wifiManagerExt.getPowerMode

getPowerMode(callback: AsyncCallback<PowerMode>): void

Obtains the power mode. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PowerMode](#powermode)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the power mode obtained. If the operation fails, **err** is not **0**. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**Example**

  import { wifiManagerExt } from '@kit.ConnectivityKit';

  wifiManagerExt.getPowerMode((err, data:wifiManagerExt.PowerMode) => {
      if (err) {
          console.error("Failed to get linked information");
          return;
      }
      console.info("get power mode info: " + JSON.stringify(data));
  });

  wifiManagerExt.getPowerMode().then(data => {
      console.info("get power mode info: " + JSON.stringify(data));
  }).catch((error:number) => {
      console.error("get power mode error");
  });

#### wifiManagerExt.setPowerMode(deprecated)

setPowerMode(mode: PowerMode) : void

Sets the power mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/GgcXb59vTRm-89zBNfC8sQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E487E1098920438BF8A9DE2DAEF0F985FAB8AB481CBAA18B23FAAA02D0FBF43)

This API is supported since API version 9 and deprecated since API version 10.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [PowerMode](#powermode) | Yes | Power mode to set. |

**Error codes**

For details about the error codes, see [Wi-Fi Error Codes](../../error-codes/wi-fi-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**Example**

  import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      let model = 0;
      wifiManagerExt.setPowerMode(model);
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
