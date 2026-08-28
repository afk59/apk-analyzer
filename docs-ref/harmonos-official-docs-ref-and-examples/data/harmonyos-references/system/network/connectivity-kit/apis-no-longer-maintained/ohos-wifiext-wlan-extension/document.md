# @ohos.wifiext (WLAN Extension)

This **wifiext** module provides WLAN extension interfaces for non-universal products.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/v6g0b3n_Rf6FXTbYjiOu-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBF2AB46F32BA6FB3D19BE74B94A93EFC9BA7CFF25D087FAD7E68223EC810629)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs described in this document are used only for non-universal products, such as routers.

The APIs provided by this module are no longer maintained since API version 9. You are advised to use [@ohos.wifiManagerExt (WLAN Extension)](../../arkts-apis/ohos-wifimanagerext-wlan-extension/document.md).

#### Modules to Import

import wifiext from '@ohos.wifiext';

#### wifiext.enableHotspot(deprecated)

enableHotspot(): boolean;

Enables the WLAN hotspot.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/_hQXwaUnQhm6WjUHXD7mZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=938014A904F312EB38778192E796F7AD28A7A3F4C7D24EB58AB3E58110165088)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManagerExt.enableHotspot](../../arkts-apis/ohos-wifimanagerext-wlan-extension/document.md#wifimanagerextenablehotspotdeprecated) instead.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

#### wifiext.disableHotspot(deprecated)

disableHotspot(): boolean;

Disables the WLAN hotspot.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/nyj3NRvwSuWhUrDmA7rb6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A77BC0CEADCCCB7871BA91E69596099B26CFF5CFAD3EB89DFC40634FC803FFE8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManagerExt.disableHotspot](../../arkts-apis/ohos-wifimanagerext-wlan-extension/document.md#wifimanagerextdisablehotspotdeprecated) instead.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

#### wifiext.getSupportedPowerModel(deprecated)

getSupportedPowerModel(): Promise<Array<PowerModel>>

Obtains the supported power models. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/G_FcW67nRWOGTSG13wokZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDA9747E5E39F795A2E1FFFE480CC94ED9876B2BA6FCCCF5A3585102BAC26D87)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManagerExt.getSupportedPowerModel](../../arkts-apis/ohos-wifimanagerext-wlan-extension/document.md#wifimanagerextgetsupportedpowermode) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[PowerModel](#powermodel)\>> | Promise used to return the power models obtained. |

#### PowerModel

Enumerates the power models.

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

| Name | Value | Description |
| :-- | :-- | :-- |
| SLEEPING | 0 | Sleeping |
| GENERAL | 1 | General |
| THROUGH\_WALL | 2 | Through\_wall |

#### wifiext.getSupportedPowerModel

getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void

Obtains the supported power models. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[PowerModel](#powermodel)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the power models obtained. If the operation fails, **err** is not **0**. |

#### wifiext.getPowerModel(deprecated)

getPowerModel(): Promise<PowerModel>

Obtains the power model. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/OWyyTELTS7eR3qtfVNaIgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0475392A25BC54083E0B8C8AEC4EEBD3570EE6A0C07857F877EFBF5FB25124A3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManagerExt.getSupportedPowerModel](../../arkts-apis/ohos-wifimanagerext-wlan-extension/document.md#wifimanagerextgetpowermode) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PowerModel](#powermodel)\> | Promise used to return the power models obtained. |

#### wifiext.getPowerModel(deprecated)

getPowerModel(callback: AsyncCallback<PowerModel>): void

Obtains the power model. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/SWoWA4FqTZmGASIhFDbhHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65A2DA3EA1F364F7AA15904D4BC3A3E75C95ED67EBFA59ECA451DF0E7AFB5E2B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [wifiManagerExt.getSupportedPowerModel](../../arkts-apis/ohos-wifimanagerext-wlan-extension/document.md#wifimanagerextgetpowermode-1) instead.

**Required permissions**: ohos.permission.GET\_WIFI\_INFO

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PowerModel](#powermodel)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **0** and **data** is the power model obtained. If the operation fails, **err** is not **0**. |

#### wifiext.setPowerModel

setPowerModel(model: PowerModel) : boolean;

Sets the power model.

**Required permissions**: ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**System capability**: SystemCapability.Communication.WiFi.AP.Extension

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | [PowerModel](#powermodel) | Yes | Power model to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |
