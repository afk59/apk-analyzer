# atomicService (Convergent Scenario-specific APIs)

This module provides capabilities for obtaining system information and settings and providing the follow component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Start version**: 5.0.0(12)

#### Modules to Import

import { atomicService } from '@kit.ScenarioFusionKit';

#### SystemSettingInfo

Provides an object for obtaining system setting attributes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bluetoothEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the Bluetooth function is enabled. **true**: yes; **false**: no.

 |
| 

locationEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the location function is enabled. **true**: yes; **false**: no.

 |
| 

wifiEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the Wi-Fi function is enabled. **true**: yes; **false**: no.

 |
| 

deviceOrientation

 | 

string

 | 

No

 | 

Yes

 | 

Current orientation of the device. The options are **portrait** and **landscape**.

 |

#### SystemInfo

Provides an object for obtaining system information attributes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

brand

 | 

string

 | 

No

 | 

Yes

 | 

Device brand.

 |
| 

deviceModel

 | 

string

 | 

No

 | 

Yes

 | 

Device type.

NOTE:

Special characters contained in the return value need to be escaped.

 |
| 

screenWidth

 | 

number

 | 

No

 | 

Yes

 | 

Screen width, in px.

 |
| 

screenHeight

 | 

number

 | 

No

 | 

Yes

 | 

Screen height, in px.

 |
| 

statusBarHeight

 | 

number

 | 

No

 | 

Yes

 | 

Height of the status bar, in px.

 |
| 

screenSafeArea

 | 

[window.AvoidArea](../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#avoidarea7)

 | 

No

 | 

Yes

 | 

Safe area on the portrait screen.

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

System language.

 |
| 

osFullName

 | 

string

 | 

No

 | 

Yes

 | 

System version.

 |
| 

fontSizeSetting

 | 

number

 | 

No

 | 

Yes

 | 

Logical pixel density of the display, which is the scaling coefficient between physical pixels and logical pixels. The calculation method is as follows: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/2kHMdR2cS_CeYW4-_tQxQQ/en-us_image_0000002503412105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CDE853FD5C466F81FCC9BB180129120440D4C9508C6DFDEA1655EBD1751868A)

The value is a floating point number and is restricted by the range of [densityDPI](../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#display). The value range is \[0.5, 4.0\]. Generally, the value is **1.0** or **3.0**. The actual value depends on the [densityDPI](../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#display) provided by the device in use.

 |
| 

sdkApiVersion

 | 

number

 | 

No

 | 

Yes

 | 

SDK API version.

 |
| 

bluetoothEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the Bluetooth function is enabled. **true**: yes; **false**: no.

 |
| 

locationEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the location function is enabled. **true**: yes; **false**: no.

 |
| 

wifiEnabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the Wi-Fi function is enabled. **true**: yes; **false**: no.

 |
| 

deviceOrientation

 | 

string

 | 

No

 | 

Yes

 | 

Current orientation of the device. The options are **portrait** and **landscape**.

 |
| 

theme

 | 

[ColorMode](../../../../application-framework/arkui/arkts-components/state-management-and-rendering-control/built-in-environment-variables/document.md#colormode)

 | 

No

 | 

Yes

 | 

Color mode. The options are as follows:

\- **ColorMode.LIGHT**: light mode

\- **ColorMode.DARK**: dark mode

 |
| 

windowWidth

 | 

number

 | 

No

 | 

Yes

 | 

Available window width, in px. The value must be an integer.

 |
| 

windowHeight

 | 

number

 | 

No

 | 

Yes

 | 

Available window height, in px. The value must be an integer.

 |

#### FollowResult

Defines the following result types.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.1(21)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SUCCESS

 | 

0

 | 

Followed successfully.

 |
| 

FAILED

 | 

1

 | 

Following failed.

 |

#### FollowComponentParams

Obtains the parameters of the follow component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.1(21)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

pubId

 | 

string

 | 

No

 | 

No

 | 

Business account ID. Obtain the value from the business account management console on HUAWEI Developers. The value contains 1 to 64 characters.

 |
| 

channelId

 | 

string

 | 

No

 | 

Yes

 | 

Channel ID. The value contains 0 to 32 characters, which can only be digits or letters. This parameter is used to identify the source channel from which the follow operation is triggered.

 |
| 

offset

 | 

[Position](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#position) | [Edges](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#edges12) | [LocalizedEdges](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#localizededges12)

 | 

No

 | 

Yes

 | 

Component position, which is based on its offset from the screen center point.

Default value: **{ x: 0, y: 300 }**

 |

#### FollowComponentCallback

Callback API for the follow component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.1(21)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

onFollowComplete

 | 

AsyncCallback<[FollowCompleteResult](#section163417717564)\>

 | 

No

 | 

No

 | 

Callback function. If the follow operation is successful, **err** is **undefined** and **data** is the **FollowCompleteResult** obtained; otherwise, **err** is an error object.

 |

#### FollowCompleteResult

Defines the response body of the following result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Start version**: 6.0.1(21)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

code

 | 

[FollowResult](#section16831162003419)

 | 

No

 | 

No

 | 

Following result. The result is **FollowResult.SUCCESS** if the following is successful and is **FollowResult.FAILED** if the following fails.

 |

#### SystemInfoType

type SystemInfoType = 'brand' | 'deviceModel' | 'screenWidth' | 'screenHeight' | 'statusBarHeight'

| 'screenSafeArea' | 'language' | 'osFullName' | 'fontSizeSetting' | 'sdkApiVersion' | 'bluetoothEnabled'

| 'locationEnabled' | 'wifiEnabled' | 'deviceOrientation' | 'theme' | 'windowWidth' | 'windowHeight'

Defines an information setting type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: For version 5.0.0(12), this API is supported on phones, tablets, and 2-in-1 devices. On other devices, it returns error code 801. For version 5.1.0(18) and later, this API is supported on phones, tablets, 2-in-1 devices, wearables, and TVs. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'brand'

 | 

Device brand.

 |
| 

'deviceModel'

 | 

Device type.

 |
| 

'screenWidth'

 | 

Screen width.

 |
| 

'screenHeight'

 | 

Screen height.

 |
| 

'statusBarHeight'

 | 

Height of the status bar.

 |
| 

'screenSafeArea'

 | 

Safe area on the portrait screen.

 |
| 

'language'

 | 

System language.

 |
| 

'osFullName'

 | 

System version.

 |
| 

'fontSizeSetting'

 | 

Logical pixel density of the display, which is the scaling coefficient between physical pixels and logical pixels. The calculation method is as follows: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/RV2yk62ISSG7mIKrqkxl4g/en-us_image_0000002503572017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDABCE21790D1C8A507F5F5CBB019266C851AE70A5B685C29C4CA31E5955B33D)

The value is a floating point number and is restricted by the range of [densityDPI](../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#display). The value range is \[0.5, 4.0\]. Generally, the value is **1.0** or **3.0**. The actual value depends on the [densityDPI](../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#display) provided by the device in use.

 |
| 

'sdkApiVersion'

 | 

SDK API version.

 |
| 

'bluetoothEnabled'

 | 

Indicates whether the Bluetooth function is enabled.

 |
| 

'locationEnabled'

 | 

Indicates whether the location function is enabled.

 |
| 

'wifiEnabled'

 | 

Indicates whether the Wi-Fi function is enabled.

 |
| 

'deviceOrientation'

 | 

Current orientation of the device.

 |
| 

'theme'

 | 

System color mode.

 |
| 

'windowWidth'

 | 

Available window width.

 |
| 

'windowHeight'

 | 

Available window height.

 |

#### SystemSettingType

type SystemSettingType = 'bluetoothEnabled' | 'locationEnabled' | 'wifiEnabled' | 'deviceOrientation'

Defines a system setting type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: For version 5.0.0(12), this API is supported on phones, tablets, and 2-in-1 devices. On other devices, it returns error code 801. For version 5.1.0(18) and later, this API is supported on phones, tablets, 2-in-1 devices, wearables, and TVs. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'bluetoothEnabled'

 | 

Indicates whether the Bluetooth function is enabled.

 |
| 

'locationEnabled'

 | 

Indicates whether the location function is enabled.

 |
| 

'wifiEnabled'

 | 

Indicates whether the Wi-Fi function is enabled.

 |
| 

'deviceOrientation'

 | 

Current orientation of the device.

 |

#### getSystemInfoSync

getSystemInfoSync(properties?: Array<SystemInfoType>): SystemInfo

Obtains system information including the device, network, screen, language, and color mode information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: For version 5.0.0(12), this API is supported on phones, tablets, and 2-in-1 devices. On other devices, it returns error code 801. For version 5.1.0(18) and later, this API is supported on phones, tablets, 2-in-1 devices, wearables, and TVs. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

properties

 | 

Array<[SystemInfoType](#section994220537517)\>

 | 

No

 | 

Request object for obtaining system information including the device, network, screen, language, and color mode information.

NOTE:

-   The Wi-Fi permission and Bluetooth permission are not required for version 5.0.1(13) and later versions.
-   To obtain Wi-Fi information, the permission **ohos.permission.GET\_WIFI\_INFO** is required.
-   To obtain the Bluetooth function status, the permission **ohos.permission.ACCESS\_BLUETOOTH** is required.
-   To obtain the user program access control permission, you need to configure [program access control management](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#requestpermissionsfromuser9) first.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/QRxDIk_3RAyljSMm0O_MzA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24CAFFC164BD80B0A487EA1EF6FEDEC52E32742C271624E7767D44E75B3D4A54)

When the **getSystemInfoSync** API is called in multi-thread mode, do not obtain **theme**, **windowWidth**, **windowHeight**, **statusBarHeight**, and **screenSafeArea**. Otherwise, the program may break down.

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SystemInfo](#section6926144111527)

 | 

Returned [SystemInfo](#section6926144111527) object.

NOTE:

Currently, the **getSystemInfoSync** API cannot be called to obtain the **windowWidth**, **windowHeight**, **statusBarHeight**, and **screenSafeArea** attributes. To obtain them, call the [getSystemInfo](#section17779133174510) API instead.

 |

**Example:**

import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let stateArray: Array<atomicService.SystemInfoType> =
  \['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'language', 'osFullName', 'fontSizeSetting',
    'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation', 'theme'\];
try {
  let data = atomicService.getSystemInfoSync(stateArray);
  hilog.info(0x0000, 'testTag', 'succeeded in getting system info');
  let brand: string | undefined = data.brand;
  let deviceModel: string | undefined = data.deviceModel;
  let screenWidth: number | undefined = data.screenWidth;
  let screenHeight: number | undefined = data.screenHeight;
  let language: string | undefined = data.language;
  let osFullName: string | undefined = data.osFullName;
  let fontSizeSetting: number | undefined = data.fontSizeSetting;
  let sdkApiVersion: number | undefined = data.sdkApiVersion;
  let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
  let wifiEnabled: boolean | undefined = data.wifiEnabled;
  let locationEnabled: boolean | undefined = data.locationEnabled;
  let deviceOrientation: string | undefined = data.deviceOrientation;
  let theme: ColorMode | undefined = data.theme;
} catch (error) {
  hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}

#### getSystemInfo

getSystemInfo(properties?: Array<SystemInfoType>): Promise<SystemInfo>

Returns system information including the device, network, screen, language, and color mode information asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: For version 5.0.0(12), this API is supported on phones, tablets, and 2-in-1 devices. On other devices, it returns error code 801. For version 5.1.0(18) and later, this API is supported on phones, tablets, 2-in-1 devices, wearables, and TVs. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

properties

 | 

Array<[SystemInfoType](#section994220537517)\>

 | 

No

 | 

Request object for obtaining system information including the device, network, screen, language, and color mode information.

NOTE:

-   The Wi-Fi permission and Bluetooth permission are not required for version 5.0.1(13) and later versions.
-   To obtain Wi-Fi information, the permission **ohos.permission.GET\_WIFI\_INFO** is required.
-   To obtain the Bluetooth function status, the permission **ohos.permission.ACCESS\_BLUETOOTH** is required.
-   To obtain the user program access control permission, you need to configure [program access control management](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#requestpermissionsfromuser9) first.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/j_HT4HEmRHSI-OBmFwsK0g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D7F09FB45AF260CA7ACCB6F155BDD37C6104A50625E63FDEA1308112CE4268B)

When the **getSystemInfo** API is called in multi-thread mode, do not obtain **theme**, **windowWidth**, **windowHeight**, **statusBarHeight**, and **screenSafeArea**. Otherwise, the program may break down.

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SystemInfo](#section6926144111527)\>

 | 

Promise used to return the [SystemInfo](#section6926144111527) object obtained.

 |

**Example:**

import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let stateArray: Array<atomicService.SystemInfoType> =
  \['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'statusBarHeight', 'screenSafeArea', 'language', 'osFullName',
    'fontSizeSetting', 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation',
    'theme', 'windowWidth', 'windowHeight'\];
try {
  atomicService.getSystemInfo(stateArray).then((data: atomicService.SystemInfo) => {
    hilog.info(0x0000, 'testTag', 'succeeded in getting system info asynchronously');
    let brand: string | undefined = data.brand;
    let deviceModel: string | undefined = data.deviceModel;
    let screenWidth: number | undefined = data.screenWidth;
    let screenHeight: number | undefined = data.screenHeight;
    let statusBarHeight: number | undefined = data.statusBarHeight;
    let screenSafeArea: window.AvoidArea | undefined = data.screenSafeArea;
    let language: string | undefined = data.language;
    let osFullName: string | undefined = data.osFullName;
    let fontSizeSetting: number | undefined = data.fontSizeSetting;
    let sdkApiVersion: number | undefined = data.sdkApiVersion;
    let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
    let wifiEnabled: boolean | undefined = data.wifiEnabled;
    let locationEnabled: boolean | undefined = data.locationEnabled;
    let deviceOrientation: string | undefined = data.deviceOrientation;
    let theme: ColorMode | undefined = data.theme;
    let windowWidth: number | undefined = data.windowWidth;
    let windowHeight: number | undefined = data.windowHeight;
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
  })
} catch (error) {
  hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}

#### getSystemSetting

getSystemSetting(properties?: Array<SystemSettingType>): SystemSettingInfo

Obtains system information, including Bluetooth, location, Wi-Fi, and device orientation information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: For version 5.0.0(12), this API is supported on phones, tablets, and 2-in-1 devices. On other devices, it returns error code 801. For version 5.1.0(18) and later, this API is supported on phones, tablets, 2-in-1 devices, wearables, and TVs. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

properties

 | 

Array<[SystemSettingType](#section11423195912475)\>

 | 

No

 | 

Request object for obtaining system information including the Bluetooth, location, Wi-Fi, and device orientation information.

NOTE:

-   The Wi-Fi permission and Bluetooth permission are not required for version 5.0.1(13) and later versions.
-   To obtain Wi-Fi information, the permission **ohos.permission.GET\_WIFI\_INFO** is required.
-   To obtain the Bluetooth function status, the permission **ohos.permission.ACCESS\_BLUETOOTH** is required.
-   To obtain the user program access control permission, you need to configure [program access control management](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-abilityaccessctrl-application-access-control/document.md#requestpermissionsfromuser9) first.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SystemSettingInfo](#section53111326141919)

 | 

Returned [SystemSettingInfo](#section53111326141919) object.

 |

**Example:**

import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let stateArray: Array<atomicService.SystemSettingType> =
  \['bluetoothEnabled', 'locationEnabled', 'deviceOrientation', 'wifiEnabled'\];
try {
  let data = atomicService.getSystemSetting(stateArray);
  hilog.info(0x0000, 'testTag', 'succeeded in getting system setting info');
  let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
  let locationEnabled: boolean | undefined = data.locationEnabled;
  let deviceOrientation: string | undefined = data.deviceOrientation;
  let wifiEnabled: boolean | undefined = data.wifiEnabled;
} catch (error) {
  hilog.error(0x0001, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}

#### showFollowComponent

showFollowComponent(ctx: UIContext, params: FollowComponentParams, callback: FollowComponentCallback): Promise<void>

Displays the follow component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AtomicserviceComponent.atomicservice

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.1(21)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ctx

 | 

[UIContext](../../../../application-framework/arkui/arkts-components/custom-components/custom-component-built-in-apis/document.md#uicontext)

 | 

Yes

 | 

**UIContext** instance.

 |
| 

params

 | 

[FollowComponentParams](#section1881114501476)

 | 

Yes

 | 

Parameters of the follow component.

 |
| 

callback

 | 

[FollowComponentCallback](#section137361343174413)

 | 

Yes

 | 

Callback function, which returns the following result.

 |

**Returns:**

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

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[801](../../../../api-reference-overview/universal-error-codes/document.md#section801-api-not-supported)

 | 

Capability not supported.

 |
| 

[1009601001](../arkts-api-error-codes/document.md#section310313457116)

 | 

Invalid service account id.

 |
| 

[1009601002](../arkts-api-error-codes/document.md#section182327351133)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1009601003](../arkts-api-error-codes/document.md#section1710114369396)

 | 

Request server failed.

 |
| 

[1009601004](../arkts-api-error-codes/document.md#section12303893910)

 | 

Network connection error.

 |
| 

[1009601005](../arkts-api-error-codes/document.md#section17511740104712)

 | 

Other error.

 |

**Example:**

import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // One-tap follow component.
    // **pubId**: business account ID. The following uses the business account ID of Huawei's official assistant as an example.
    const pubId: string = '0cca1c645526449fb89d4a83e3bc25df';
    // **channelId**: channel ID. The value contains a maximum of 32 characters and can contain only digits and letters. **offset**: coordinates of the follow component.
    const params: atomicService.FollowComponentParams =
      { pubId: pubId, channelId: '', offset: { x: 0, y: 300 } };
    // Callback triggered when the follow button is tapped.
    const callbacks: atomicService.FollowComponentCallback = {
      onFollowComplete: (err, result) => {
        if (err) {
          // Error processing.
          hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
          return;
        }
        hilog.info(0x0000, "testTag", "follow result: %{public}d", result.code);
        if (result.code === atomicService.FollowResult.SUCCESS) {
          hilog.info(0x0000, "testTag", "follow succeeded handle");
        } else {
          hilog.info(0x0000, "testTag", "follow failed handle");
        }
      }
    }
    // Display the follow component.
    atomicService.showFollowComponent(this.getUIContext(), params, callbacks).catch((error: BusinessError<void>) => {
      hilog.error(0x0000, 'testTag', 'showFollowComponent failReason: %{public}d %{public}s:', error.code,
        error.message);
    })
  }

  build() {
  }
}
