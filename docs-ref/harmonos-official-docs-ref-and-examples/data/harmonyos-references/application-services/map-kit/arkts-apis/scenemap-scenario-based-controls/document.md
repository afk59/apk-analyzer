# sceneMap (Scenario-based Controls)

This module provides scenario-based map controls, including the place details display control, location selection control, and division selection control.

**Start version**: 4.1.0(11)

#### Module Import

import { sceneMap } from '@kit.MapKit';

#### queryLocation

queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>

Starts up the place details display control based on the provided parameters. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/msIkcHMrQ-GHnpO_rAlm2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B37B9BBCE5427D72676CC8DD3EA829A8C101DBA4643822861D9E603A80184AA)

-   This API can be called only in the ArkUI page context.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context corresponding to [UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) or [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md).

 |
| 

options

 | 

[LocationQueryOptions](#section971194972117)

 | 

Yes

 | 

Parameters for querying place details.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002600001

 | 

System internal error.

 |
| 

1002600002

 | 

Failed to connect to the Map Kit server.

 |
| 

1002600003

 | 

App authentication failed.

 |
| 

1002600004

 | 

The Map permission is not enabled.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let queryLocationOptions: sceneMap.LocationQueryOptions = { siteId: "922207154068557824" };
sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
  .then(() => {
    console.info("QueryLocation", "Succeeded in querying location.");
  })
  .catch((err: BusinessError) => {
    console.error("QueryLocation", \`Failed to query Location, code: ${err.code}, message: ${err.message}\`);
  });

#### chooseLocation

chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise<LocationChoosingResult>

Starts up the location selection control based on the provided parameters. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/_r3jeJoOQdm4uSuvxqIKdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB8E9F550805A9806BF67D8F2715BDEB777CE3CBF6B0A8E120B8DB0D5B4D32E0)

-   This API can be called only in the ArkUI page context.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context corresponding to [UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) or [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md).

 |
| 

options

 | 

[LocationChoosingOptions](#section1313113517227)

 | 

Yes

 | 

Parameters for selecting a location on the map.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[LocationChoosingResult](#section0471517192216)\>

 | 

[LocationChoosingResult](#section0471517192216) object returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002600001

 | 

System internal error.

 |
| 

1002600002

 | 

Failed to connect to the Map Kit server.

 |
| 

1002600003

 | 

App authentication failed.

 |
| 

1002600004

 | 

The Map permission is not enabled.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
  location: { latitude: 39.92194051376904, longitude: 116.3971836796932 },
  searchEnabled: true,
  showNearbyPoi: true
};
sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, locationChoosingOptions)
  .then((data) => {
    console.info("ChooseLocation", "Succeeded in choosing location.");
  })
  .catch((err: BusinessError) => {
    console.error("ChooseLocation", \`Failed to choose Location, code: ${err.code}, message: ${err.message}\`);
  });

#### selectDistrict

selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>

Displays the division selection page based on the provided parameters. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/c6aOZvLMQfuPZ9nTyS8owA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D65BFEB5A09C7701216BC2C67347C245E288E8593D38C90CBAD6F0E9EE2F5DC)

-   This API can be called only in the ArkUI page context.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context corresponding to [UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) or [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md).

 |
| 

options

 | 

[DistrictSelectOptions](#section17211958161110)

 | 

Yes

 | 

Initial options on the division selection page.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[DistrictSelectResult](#section3745121172118)\>

 | 

[DistrictSelectResult](#section3745121172118) object returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |
| 

1002600001

 | 

System internal error.

 |
| 

1002600002

 | 

Failed to connect to the Map Kit server.

 |
| 

1002600003

 | 

App authentication failed.

 |
| 

1002600004

 | 

The Map permission is not enabled.

 |
| 

1002600012

 | 

The country code is not supported.

 |
| 

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let districtSelectOptions: sceneMap.DistrictSelectOptions = {
  countryCode: "CN"
};
sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
  console.info("SelectDistrict", "Succeeded in selecting district.");
}).catch((err: BusinessError) => {
  console.error("SelectDistrict", \`Failed to select district, code: ${err.code}, message: ${err.message}\`);
});

#### LocationQueryOptions

Defines parameters for querying place details.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

Place ID on the place details page.

The value of **siteId** can be obtained using the [on](../map-map-display/mapeventmanager/document.md#section0279247143911)(type: 'poiClick', callback: Callback<[mapCommon.Poi](../mapcommon-map-attribute-model/document.md#section1155919456273)\>) method of [MapEventManager](../map-map-display/mapeventmanager/document.md).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

language

 | 

string

 | 

No

 | 

Yes

 | 

Language. Refer to [Languages Supported by Map Picker](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section167751124121111) for supported languages. If this parameter is not set, the system language is used by default. If an invalid value is passed, the default value will be used.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Coordinates of the map center point. If **siteId** is not available, use this parameter to query place details.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Name of a place. If **siteId** is not available, use this parameter as the name of **location**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

address

 | 

string

 | 

No

 | 

Yes

 | 

Address of a place. If **siteId** is not available, use this parameter as the address of **location**.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

showBusiness

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display business information (such as taxi hailing). The default value is **true**.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

NOTE:

This parameter was reserved in API versions 4.1.0(11) through 5.1.1(19) and has been in use since API version 6.0.0(20).

 |
| 

themeColor

 | 

[CustomColors](../../../../application-framework/arkui/arkts-api/ui/ohos-arkui-theme-theme/document.md#customcolors)

 | 

No

 | 

Yes

 | 

Custom theme color object. The default value is **brand** (brand color).

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

cancelCallback

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function that returns no value. This callback is triggered when the place details control is closed.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

transitionDuration

 | 

number

 | 

No

 | 

Yes

 | 

Transition animation duration. The default value is **\-1**. The value range is \[0, Number.MAX\_VALUE). If an invalid value is passed, the default value **\-1** will be used, thereby preserving [interpolatingSpring](../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10)(0.5, 1, 328, 36). This parameter does not take effect on 2-in-1 devices as they do not support transition animation currently.

**Start version**: 6.0.2(22)

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/EqIjzeziSOyNAbf-y5BHOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062514Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=334FBB11F38165DC2DE7A6019472454076AF4C98F172EC528A26734AC58A553C)

At least one of the following groups of parameters must be passed. If all parameters are passed, use **siteId**.

-   siteId
-   location, name

**Example**:

let queryLocationOptions: sceneMap.LocationQueryOptions = { siteId: "922207154068557824" };

#### LocationChoosingOptions

Defines parameters for selecting a location on the map.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Coordinates of the map center point.

If this parameter is not set, the current location of the device is used as the center point. If the current location of the device fails to be obtained, the Palace Museum is used as the center point by default.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

language

 | 

string

 | 

No

 | 

Yes

 | 

Language. Refer to [Languages Supported by Map Picker](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section167751124121111) for supported languages. If this parameter is not set, the system language is used by default. If an invalid value is passed, the default value will be used.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

poiTypes

 | 

Array<string>

 | 

No

 | 

Yes

 | 

POI type to be displayed. The value range is the same as that of [HwLocationType](../appendixes/poi-types/document.md#section1662744719618).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

searchEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the search control. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

showNearbyPoi

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display nearby POIs. The default value is **false**. An invalid value is handled as the default value.

-   **true**: yes
-   **false**: no

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

snapshotEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to return mapped snapshots. The default value is **false**.

-   **true**: yes
-   **false**: no

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

themeColor

 | 

[CustomColors](../../../../application-framework/arkui/arkts-api/ui/ohos-arkui-theme-theme/document.md#customcolors)

 | 

No

 | 

Yes

 | 

Custom theme color object. The default value is **brand** (brand color).

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

cancelCallback

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function that returns no value. This callback is triggered when the location selection control is closed.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

transitionDuration

 | 

number

 | 

No

 | 

Yes

 | 

Transition animation duration. The default value is **\-1**. The value range is \[0, Number.MAX\_VALUE). If an invalid value is passed, the default value **\-1** will be used, thereby preserving [interpolatingSpring](../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10)(0.5, 1, 328, 36). This parameter does not take effect on 2-in-1 devices as they do not support transition animation currently.

**Start version**: 6.0.2(22)

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

 |

**Example**:

let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
  location: {latitude: 39.9, longitude: 116.4}
};

#### LocationChoosingResult

Defines the location selection result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

ID of a selected location. If the selected location is not a POI, no value is returned.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

No

 | 

Coordinates of a selected location.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

POI name of a selected location. If the selected location is not a POI, the corresponding marker is returned.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

address

 | 

string

 | 

No

 | 

No

 | 

Address of a selected location.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

addressComponent

 | 

[site.AddressComponent](../site-place-search/document.md#section1652881563212)

 | 

No

 | 

Yes

 | 

Detailed address of a selected location.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

zoom

 | 

number

 | 

No

 | 

No

 | 

Zoom level of a selected location. The value ranges from 2 to 20. If a value is out of this range, the nearest boundary value is used.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

snapshot

 |  | 

No

 | 

Yes

 | 

Map snapshot.

**Start version**: 5.0.0(12)

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |

#### DistrictSelectOptions

Defines the initial options on the division selection page.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

countryCode

 | 

string

 | 

No

 | 

Yes

 | 

Country/Region code of an administrative division, which must comply with ISO 3166-1 alpha-2.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

language

 | 

string

 | 

No

 | 

Yes

 | 

Page language. Refer to [Languages Supported by Map Picker](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-language#section167751124121111) for supported languages. If this parameter is not set, the system language is used by default. If an invalid value is passed, the default value will be used.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

address

 | 

string

 | 

No

 | 

Yes

 | 

Address specified for searching.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

 |
| 

themeColor

 | 

[CustomColors](../../../../application-framework/arkui/arkts-api/ui/ohos-arkui-theme-theme/document.md#customcolors)

 | 

No

 | 

Yes

 | 

Custom theme color object. The default value is **brand** (brand color).

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

subWindowEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the administrative division selection control in a subwindow. The default value is **false**.

-   **true**: yes
-   **false**: no

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

cancelCallback

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function that returns no value. This callback is triggered when the division selection control is closed.

**Start version**: 5.0.3(15)

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

transitionDuration

 | 

number

 | 

No

 | 

Yes

 | 

Transition animation duration. The default value is **\-1**. The value range is \[0, Number.MAX\_VALUE). If an invalid value is passed, the default value **\-1** will be used, thereby preserving [interpolatingSpring](../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10)(0.5, 1, 328, 36). This parameter does not take effect if **subWindowEnabled** is set to **true**.

**Start version**: 6.0.2(22)

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

 |

**Example**:

let districtSelectOptions: sceneMap.DistrictSelectOptions = {
  countryCode: "CN",
  language:"zh",
  address: "Henan"
};

#### DistrictSelectResult

Defines the division selection result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

districts

 | 

Array<[District](#section1818842852518)\>

 | 

No

 | 

No

 | 

Information about a selected administrative division.

 |
| 

addressDescription

 | 

string

 | 

No

 | 

Yes

 | 

Address of a selected administrative division.

 |

#### District

Defines administrative division information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: This API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

siteId

 | 

string

 | 

No

 | 

Yes

 | 

ID of an administrative division.

 |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Name of an administrative division.

 |
| 

location

 | 

[mapCommon.LatLng](../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

No

 | 

Yes

 | 

Coordinates of an administrative division.

 |
| 

adminLevel

 | 

string

 | 

No

 | 

Yes

 | 

Division level, including country, province/state, city, district/county, and street.

NOTE:

Country: COUNTRY

Province: ADMINISTRATIVE\_AREA\_LEVEL\_1

City: ADMINISTRATIVE\_AREA\_LEVEL\_2

District/County: ADMINISTRATIVE\_AREA\_LEVEL\_3

Street: ADMINISTRATIVE\_AREA\_LEVEL\_4

 |
| 

adminCode

 | 

string

 | 

No

 | 

Yes

 | 

[Administrative division code](../appendixes/city-codes-and-administrative-division-codes/document.md).

NOTE:

The administrative division codes returned by the API cover all provinces, cities, districts/counties, and towns/streets in the Chinese mainland, Hong Kong (China), and Macao (China). The appendix provides only a sample of city administrative division codes.

 |
| 

cityCode

 | 

string

 | 

No

 | 

Yes

 | 

[City code](../appendixes/city-codes-and-administrative-division-codes/document.md).

 |
| 

countryCode

 | 

string

 | 

No

 | 

Yes

 | 

Country/Region code.

 |
