# SysCap

SystemCapability (SysCap) refers to a standalone feature in the operating system. Different devices support different SysCap sets. Each SysCap corresponds to one or more APIs. You can determine whether an API can be used by checking SysCap support.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/6XM8hEdbQjGze4R_LSOySA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062526Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2234E507F7A3364D4ECDEE50573F0ECFFF7FA8CA6D2302E01C954E9C4EC228DB)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### canIUse

canIUse(syscap: string): boolean

Checks whether a SysCap is supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| syscap | string | Yes | Name of the SysCap to check. **null** and **undefined** are not supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** means that the SysCap is supported, and **false** means the opposite. |

**Example**

import { geoLocationManager } from '@kit.LocationKit'
import { BusinessError } from '@kit.BasicServicesKit';

const isLocationAvailable = canIUse('SystemCapability.Location.Location.Core');
if (isLocationAvailable) {
    geoLocationManager.getCurrentLocation((err: BusinessError, location: geoLocationManager.Location) => {
        if (err) {
            console.error('err=' + JSON.stringify(err));
        }
        if (location) {
            console.info('location=' + JSON.stringify(location));
        }
    });
} else {
    console.info('Location not by this device.');
}
