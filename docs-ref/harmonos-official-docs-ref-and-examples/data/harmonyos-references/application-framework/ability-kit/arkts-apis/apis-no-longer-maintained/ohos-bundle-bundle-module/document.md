# @ohos.bundle (Bundle Module)

The module provides APIs for obtaining information about an application, including [bundle information](../bundle/bundleinfo/document.md), [application information](../bundle/applicationinfo/document.md), and [ability information](../bundle/abilityinfo/document.md). It also provides APIs to obtain and set the application disabling state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/b6u1U6PmR_SX-woJBLX1kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21F397C1C97D9E86473179D4D93C96774BF74DBD16CE711931147FC10157756E)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [@ohos.bundle.bundleManager](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md) instead.

#### Modules to Import

import bundle from '@ohos.bundle';

#### Required Permissions

| Permission | APL | Description |
| :-- | :-- | :-- |
| ohos.permission.GET\_BUNDLE\_INFO | normal | Permission to query information about a specified bundle. |
| ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED | system\_basic | Permission to query information about all bundles. |

For details about the APL, see [Basic Concepts in the Permission Mechanism](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permission-mgmt-overview#basic-concepts-in-the-permission-mechanism).

#### bundle.getApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/o-3CR2llSQOsRJoHWzVH_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9313E77B61CA8B0E9E4CAB12B9E8DEC192633E7A7CE1868F3DFF3623458FE66)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>

Obtains the application information based on a given bundle name. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the application information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | No | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ApplicationInfo](../bundle/applicationinfo/document.md)\> | Promise used to return the application information. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;
let userId: number = 100;

bundle.getApplicationInfo(bundleName, bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/28tvGusnSoCp44dvuNJbWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCAEFB78D621B30B324768E5D8A9D7F06DBB7BF7A0F42C170EF96EA1C967E1EF)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getApplicationInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void

Obtains the application information of the specified user based on a given bundle name. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the application information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | Yes | User ID. The value must be greater than or equal to 0. |
| callback | AsyncCallback<[ApplicationInfo](../bundle/applicationinfo/document.md)\> | Yes | Callback used to return the application information. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;
let userId: number = 100;

bundle.getApplicationInfo(bundleName, bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/YBWTE-MzQxiey6dODUOkXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBF9EBE8294FC9B79031199C2E06CA7401DD45B5D674C04F4DCB9653CA4F1011)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void

Obtains the application information based on a given bundle name. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the application information flags in [BundleFlag](#bundleflagdeprecated). |
| callback | AsyncCallback<[ApplicationInfo](../bundle/applicationinfo/document.md)\> | Yes | Callback used to return the application information. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;

bundle.getApplicationInfo(bundleName, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAllBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/lmLZMbE0SN-i1oPO8Vn_3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BDC369263BCDA036E3B0976497359AFDC15A8BC4B1B6A51DC6B562A81744141)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>

Obtains the information of all bundles of the specified user. This API uses a promise to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleFlag | BundleFlag | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | No | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[BundleInfo](../bundle/bundleinfo/document.md)\>> | Promise used to return the information of all bundles. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlag: number = 0;
let userId: number = 100;

bundle.getAllBundleInfo(bundleFlag, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getAllBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/0qm2GmY3QK2Vook75MDfBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C19412F00F4AA7B5F1B1C0ABCC8DA993C7BD9541242BE2F39E91A00669F145EC)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void

Obtains the information of all bundles of the current user. This API uses an asynchronous callback to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleFlag | BundleFlag | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| callback | AsyncCallback<Array<[BundleInfo](../bundle/bundleinfo/document.md)\>> | Yes | Callback used to return the information of all bundles. |

**Example**

import bundle from '@ohos.bundle';

let bundleFlag: number = 0;

bundle.getAllBundleInfo(bundleFlag, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAllBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/IFxqKEqhRQ6mg44WJo0ZFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5603F5CDCB3111DFDF2B5DD91C792DD50EE2E1715A5D62ABBC41227161958A69)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void

Obtains the information of all bundles of the specified user. This API uses an asynchronous callback to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleFlag | BundleFlag | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | Yes | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |
| callback | AsyncCallback<Array<[BundleInfo](../bundle/bundleinfo/document.md)\>> | Yes | Callback used to return the information of all bundles. |

**Example**

import bundle from '@ohos.bundle';

let bundleFlag: number = 0;
let userId: number = 100;

bundle.getAllBundleInfo(bundleFlag, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/TwE_NB_JQmGLLtR4my_2zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=556FBDF42582E43DDD059DEA9177CD5D038DFC10EF14E947A5825383D931968E)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [getBundleInfo](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14-2) instead.

getBundleInfo(bundleName: string, bundleFlags: number, options?: BundleOptions): Promise<BundleInfo>

Obtains the bundle information based on a given bundle name. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| options | [BundleOptions](#bundleoptionsdeprecated) | No | Options that contain the user ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BundleInfo](../bundle/bundleinfo/document.md)\> | Promise used to return the bundle information. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;
let options: bundle.BundleOptions = {
  "userId": 100
};

bundle.getBundleInfo(bundleName, bundleFlags, options)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/MnfkbszxROaGsmY4DHOfDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1555A63240DCC3C6BFA69A1BE6AE8B56B10D5D644852A11C0488A3DB53DE84B8)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [getBundleInfo](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14-1) instead.

getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

Obtains the bundle information based on a given bundle name. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| callback | AsyncCallback<[BundleInfo](../bundle/bundleinfo/document.md)\> | Yes | Callback used to return the bundle information. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;

bundle.getBundleInfo(bundleName, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ibMBK503Q-e86Pgy5Se0kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0E3E9DB46E1345AD50A89F20A86511DAE4AAACB841147751B320CCBCF34885B)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [getBundleInfo](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14) instead.

getBundleInfo(bundleName: string, bundleFlags: number, options: BundleOptions, callback: AsyncCallback<BundleInfo>): void

Obtains the bundle information based on a given bundle name and bundle options. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| options | [BundleOptions](#bundleoptionsdeprecated) | Yes | Includes **userId**. |
| callback | AsyncCallback<[BundleInfo](../bundle/bundleinfo/document.md)\> | Yes | Callback used to return the bundle information. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;
let options: bundle.BundleOptions = {
  "userId": 100
};

bundle.getBundleInfo(bundleName, bundleFlags, options, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAllApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/KKUEikGsTsGrmNIxGioN0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52F24A0D09CBC517EF3C95246471F3070611695FF5378347D8A985E0B590AC8F)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAllApplicationInfo(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>

Obtains the information about all applications of the specified user. This API uses a promise to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the application information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | No | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ApplicationInfo](../bundle/applicationinfo/document.md)\>> | Promise used to return the application information. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlags: number = 8;
let userId: number = 100;

bundle.getAllApplicationInfo(bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getAllApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/sXGi19UNRgCAUxXI-3uCJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9059EF872FE7EAD8BD463612A0190FEE5E5FB14BC7C6951AA96B7AA809E3C15C)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAllApplicationInfo(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

Obtains the information about all applications. This API uses an asynchronous callback to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the application information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | Yes | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |
| callback | AsyncCallback<Array<[ApplicationInfo](../bundle/applicationinfo/document.md)\>> | Yes | Callback used to return the application information. |

**Example**

import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET\_APPLICATION\_INFO\_WITH\_PERMISSION;
let userId: number = 100;

bundle.getAllApplicationInfo(bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAllApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/t35b-1-sSpahlxasaUZVCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E3EAC611C1490CF20E118F6751817BFE728C0C8D6E37C672D9F28275FBED83F)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAllApplicationInfo(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

Obtains the information about all applications of the current user. This API uses an asynchronous callback to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleFlags | number | Yes | Type of information that will be returned. For details about the available enumerated values, see the application information flags in [BundleFlag](#bundleflagdeprecated). |
| callback | AsyncCallback<Array<[ApplicationInfo](../bundle/applicationinfo/document.md)\>> | Yes | Callback used to return the application information. |

**Example**

import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET\_APPLICATION\_INFO\_WITH\_PERMISSION;

bundle.getAllApplicationInfo(bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getBundleArchiveInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/MddA8wDBQZ2T5dTQCsJZ7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80451949F2624B1068582BE6A96CF646982960B2EC13F96BBD98F475322186E3)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number) : Promise<BundleInfo>

Obtains information about the bundles contained in a HAP file. This API uses a promise to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hapFilePath | string | Yes | Path where the HAP file is stored. The absolute path of the application and the data directory sandbox path are supported. |
| bundleFlags | number | Yes | Flags used to specify information contained in the BundleInfo object that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[BundleInfo](../bundle/bundleinfo/document.md)\> | Promise used to return the information about the bundles. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let hapFilePath: string = "/data/storage/el2/base/test.hap";
let bundleFlags: number = 0;

bundle.getBundleArchiveInfo(hapFilePath, bundleFlags)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getBundleArchiveInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/_FR9F4-RThWlZDcdsU5pyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DEBE5B655EBCE727599D0ED7B7DF458CB72A7B9FCD8BA032519DF999E12F3BB)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>) : void

Obtains information about the bundles contained in a HAP file. This API uses an asynchronous callback to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hapFilePath | string | Yes | Path where the HAP file is stored. The absolute path of the application and the data directory sandbox path are supported. |
| bundleFlags | number | Yes | Flags used to specify information contained in the BundleInfo object that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](#bundleflagdeprecated). |
| callback | AsyncCallback<[BundleInfo](../bundle/bundleinfo/document.md)\> | Yes | Callback used to return the information about the bundles. |

**Example**

import bundle from '@ohos.bundle';

let hapFilePath: string = "/data/storage/el2/base/test.hap";
let bundleFlags: number = 0;

bundle.getBundleArchiveInfo(hapFilePath, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAbilityInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/iYsmwmfYQVKRqzPUhS79rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F4D5DD5E67F0ECC52DFA4D6DCCE6886F82E22997231D09D9E8D8194DBC650FF)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>

Obtains the ability information based on a given bundle name and ability name. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityInfo](../bundle/abilityinfo/document.md)\> | Promise used to return the ability information. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getAbilityInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/gKEagiKYSbS_WUJ3VD7grg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DA19DBCC5C4EE8C6DE547BE8A7F5194DF25857C9CFF7A76576647AF844B976B)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void

Obtains the ability information based on a given bundle name and ability name. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |
| callback | AsyncCallback<[AbilityInfo](../bundle/abilityinfo/document.md)\> | Yes | Callback used to return the ability information. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAbilityLabel8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/4ci-LhbhSLaHFEIlXyz9pA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DD608FCA07AA4919C196BC1E2C46D5D4B6FC7EBD8308B224E33F5468DC9CE2C)

This API has been supported since API version 8 and deprecated since API version 9. Its substitute is available only to system applications.

getAbilityLabel(bundleName: string, abilityName: string): Promise<string>

Obtains the application name based on a given bundle name and ability name. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the application name. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityLabel(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getAbilityLabel8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/h9kCm2yuTWOZSc6HHCMdsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05E60B0A5C1AC5C0A00CFB9882E04381BD41FC5437B179ABC74D3177574B8DE7)

This API has been supported since API version 8 and deprecated since API version 9. Its substitute is available only to system applications.

getAbilityLabel(bundleName: string, abilityName: string, callback : AsyncCallback<string>): void

Obtains the application name based on a given bundle name and ability name. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |
| callback | AsyncCallback<string> | Yes | Callback used to return the application name. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityLabel(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.isAbilityEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/m5eYkuIVQSeKwyFUGbdfjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8890C0C9CB7EF8EECC51F00DF6322D845CCDA5BFEED5AEA637B51DD5C3E7C078)

This API has been supported since API version 8 and deprecated since API version 9. Its substitute is available only to system applications.

isAbilityEnabled(info: AbilityInfo): Promise<boolean>

Checks whether the ability that matches a given AbilityInfo object is enabled. This API uses a promise to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [AbilityInfo](../bundle/abilityinfo/document.md) | Yes | Ability information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if enabled, **false** otherwise. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
  bundle.isAbilityEnabled(abilityInfo).then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
})

#### bundle.isAbilityEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/sIPwFnL_R8uGM69PRmpZ7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DAE89C25B8C9F85BACEEFC187DF3A049A2556F07492B9798165AE362AC4938D)

This API has been supported since API version 8 and deprecated since API version 9. Its substitute is available only to system applications.

isAbilityEnabled(info : AbilityInfo, callback : AsyncCallback<boolean>): void

Checks whether the ability that matches a given AbilityInfo object is enabled. This API uses an asynchronous callback to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [AbilityInfo](../bundle/abilityinfo/document.md) | Yes | Ability information. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if enabled, **false** otherwise. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
  bundle.isAbilityEnabled(abilityInfo, (err, data) => {
    if (err) {
      console.error('Operation failed. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Operation successful. Data:' + JSON.stringify(data));
  })
})

#### bundle.isApplicationEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/2x2HBYiFR4qQvY4WwjTinA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0553AE62DD7A5CEE9DF69707F44A7EDFBD821F753241D5D4F51ACAB39DC61C9C)

This API has been supported since API version 8 and deprecated since API version 9. Its substitute is available only to system applications.

isApplicationEnabled(bundleName: string): Promise<boolean>

Checks whether an application is enabled based on a given bundle name. This API uses a promise to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if enabled, **false** otherwise. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.isApplicationEnabled(bundleName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.isApplicationEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/ZbTxYwoVQ6eNXJEqO5hDxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79FB43A245E4DC795E0D020554E8B28F68D7694CC4AB93680187E7EAEBCF8544)

This API has been supported since API version 8 and deprecated since API version 9. Its substitute is available only to system applications.

isApplicationEnabled(bundleName: string, callback : AsyncCallback<boolean>): void

Checks whether an application is enabled based on a given bundle name. This API uses an asynchronous callback to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if enabled, **false** otherwise. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.isApplicationEnabled(bundleName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.queryAbilityByWantdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/8QNHz5qMSTCfz0Q3TU4oVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=317E0C7E8AD59AEC636BCE496601838F7DE2D2EA701CE8E50F7EEE0FD8A4B393)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

queryAbilityByWant(want: Want, bundleFlags: number, userId?: number): Promise<Array<AbilityInfo>>

Obtains the ability information based on given Want. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../ohos-application-want-want/document.md) | Yes | Want containing the bundle name. |
| bundleFlags | number | Yes | Ability information to be returned. For details about the available enumerated values, see the ability information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | No | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AbilityInfo](../bundle/abilityinfo/document.md)\>> | Promise used to return the ability information. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let userId: number = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.queryAbilityByWantdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/9DptO6kFSCyDIOzSgqvPFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8A6FC9C6177FE5AAA70B164101C29125229F93FD2C868DC539B9FE276BCE36D)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

queryAbilityByWant(want: Want, bundleFlags: number, userId: number, callback: AsyncCallback<Array<AbilityInfo>>): void

Obtains the ability information of the specified user based on given Want. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../ohos-application-want-want/document.md) | Yes | Want containing the bundle name. |
| bundleFlags | number | Yes | Ability information to be returned. For details about the available enumerated values, see the ability information flags in [BundleFlag](#bundleflagdeprecated). |
| userId | number | Yes | User ID. The value must be greater than or equal to 0. |
| callback | AsyncCallback<Array<[AbilityInfo](../bundle/abilityinfo/document.md)\>> | Yes | Callback used to return the ability information. |

**Example**

import bundle from '@ohos.bundle';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let userId: number = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.queryAbilityByWantdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/1BzKVqaHTdyQSc86zIDGaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D41C746CFB94970289BBB88B4F448F94D38A1165599E17DEFA3F5C99D5C888A)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

queryAbilityByWant(want: Want, bundleFlags: number, callback: AsyncCallback<Array<AbilityInfo>>): void

Obtains the ability information based on given Want. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../ohos-application-want-want/document.md) | Yes | Want containing the bundle name. |
| bundleFlags | number | Yes | Ability information to be returned. For details about the available enumerated values, see the ability information flags in [BundleFlag](#bundleflagdeprecated). |
| callback | AsyncCallback<Array<[AbilityInfo](../bundle/abilityinfo/document.md)\>> | Yes | Callback used to return the ability information. |

**Example**

import bundle from '@ohos.bundle';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getLaunchWantForBundledeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/rZ3eMocdTM-NXwA82SBiRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3D73A36970DA43BF5320D0ABF568DDFA87D5B080BB1455881E5678BBA51405A)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getLaunchWantForBundle(bundleName: string): Promise<Want>

Obtains the Want object that launches the specified application. This API uses a promise to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Want](../ohos-application-want-want/document.md)\> | Promise used to return the Want object. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.getLaunchWantForBundle(bundleName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getLaunchWantForBundledeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/rp1qcETdSxiVX4K53Q2oiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE61DF3712515E73F257ECFB0B4F2E7B2575C00B1D7DF9FA7B18EFD334E42DB0)

This API has been supported since API version 7 and deprecated since API version 9. Its substitute is available only to system applications.

getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void

Obtains the Want object that launches the specified application. This API uses an asynchronous callback to return the result.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| callback | AsyncCallback<[Want](../ohos-application-want-want/document.md)\> | Yes | Callback used to return the Want object. |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.getLaunchWantForBundle(bundleName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getNameForUid8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/lyXsRMJIRKGLGFymqoDT-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F87D7B44ED6C8A5FB02A4AAFB669FF744B28ECBD60941391C397FFA83F25E85)

This API has been supported since API version 8 and deprecated since API version 9. You are advised to use [getBundleNameByUid](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundlenamebyuid14-1) instead.

getNameForUid(uid: number): Promise<string>

Obtains the bundle name based on a UID. This API uses a promise to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID based on which the bundle name is to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the bundle name. |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let uid: number = 20010005;

bundle.getNameForUid(uid)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/RfktP8C4R3y4LvUPY-VlrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10876E7BD3141B87F8F395337D7E810DF5B632B86E0B81817A88A104C6D2AC51)

This API has been supported since API version 8 and deprecated since API version 9. You are advised to use [getBundleNameByUid](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundlenamebyuid14) instead.

getNameForUid(uid: number, callback: AsyncCallback<string>) : void

Obtains the bundle name based on a UID. This API uses an asynchronous callback to return the result.

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | UID based on which the bundle name is to obtain. |
| callback | AsyncCallback<string> | Yes | Callback used to return the bundle name. |

**Example**

import bundle from '@ohos.bundle';

let uid: number = 20010005;

bundle.getNameForUid(uid, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### bundle.getAbilityIcon8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/I0F0YfsoSOuY8x_YWlaJag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34E0028A03B46C3324F866B67CB62CBE276E311BFA4DE57C6E14A9E97DD491F1)

This API has been supported since API version 8 and deprecated since API version 9. You are advised to use [resourceManager.getMediaContent](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getmediacontent9) instead.

getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>

Obtains the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) of the icon corresponding to a given bundle name and ability name. This API uses a promise to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<image.PixelMap> | Promise used to return the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md). |

**Example**

import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityIcon(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })

#### bundle.getAbilityIcon8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/uGQTRSxsRXKZxstXkmx1qA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F48513E69672B0FF207EB9145C40E94A1F84264E13D18577C24BB58D9205C9E)

This API has been supported since API version 8 and deprecated since API version 9. You are advised to use [resourceManager.getMediaContent](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#getmediacontent9) instead.

getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void

Obtains the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) of the icon corresponding to a given bundle name and ability name. This API uses an asynchronous callback to return the result.

No permission is required for obtaining the caller's own information.

**Required permissions**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED or ohos.permission.GET\_BUNDLE\_INFO

**System capability**

SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |
| callback | AsyncCallback<image.PixelMap> | Yes | Callback used to return the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md). |

**Example**

import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityIcon(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})

#### InstallErrorCodedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/hWsXiBRFTDmuefY9yjDerg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8164B1E713D9C4402E9789BC3A6D07F5505EF2410E4124BD25A1579FE9B68195)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [errorcode-bundle](../../../error-codes/bundle-error-codes/document.md) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 0 | Installation succeeded. |
| STATUS\_INSTALL\_FAILURE | 1 | Installation failed. (The application to be installed is not found.) |
| STATUS\_INSTALL\_FAILURE\_ABORTED | 2 | Installation aborted. |
| STATUS\_INSTALL\_FAILURE\_INVALID | 3 | Invalid installation parameter. |
| STATUS\_INSTALL\_FAILURE\_CONFLICT | 4 | Installation conflict. (The basic information of the application to update is inconsistent with that of the existing application.) |
| STATUS\_INSTALL\_FAILURE\_STORAGE | 5 | Failed to store the bundle information. |
| STATUS\_INSTALL\_FAILURE\_INCOMPATIBLE | 6 | Installation incompatibility. (A downgrade occurs or the signature information is incorrect.) |
| STATUS\_UNINSTALL\_FAILURE | 7 | Uninstallation failed. (The application to be uninstalled is not found.) |
| STATUS\_UNINSTALL\_FAILURE\_BLOCKED | 8 | Uninstallation aborted. (This error code is not in use.) |
| STATUS\_UNINSTALL\_FAILURE\_ABORTED | 9 | Uninstallation aborted. (Invalid parameters.) |
| STATUS\_UNINSTALL\_FAILURE\_CONFLICT | 10 | Uninstallation conflict. (Failed to uninstall a system application or end the application process.) |
| STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_TIMEOUT | 0x0B | Installation failed. (Download timed out.) |
| STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_FAILED | 0x0C | Installation failed. (Download failed.) |
| STATUS\_RECOVER\_FAILURE\_INVALID8+ | 0x0D | Failed to restore the pre-installed application. |
| STATUS\_ABILITY\_NOT\_FOUND | 0x40 | Ability not found. |
| STATUS\_BMS\_SERVICE\_ERROR | 0x41 | BMS service error. |
| STATUS\_FAILED\_NO\_SPACE\_LEFT8+ | 0x42 | Insufficient device space. |
| STATUS\_GRANT\_REQUEST\_PERMISSIONS\_FAILED8+ | 0x43 | Application authorization failed. |
| STATUS\_INSTALL\_PERMISSION\_DENIED8+ | 0x44 | No installation permission. |
| STATUS\_UNINSTALL\_PERMISSION\_DENIED8+ | 0x45 | No uninstallation permission. |

#### BundleFlagdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/cYYfUpILRa2nypXQOOVRpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=464C3D722CE35FDC6FDBF00C43111DE25187FEB91C4AFB12C878E58B4927BA74)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager.BundleFlag](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundleflag) instead.

Enumerates the bundle flags, which indicate the type of bundle information to obtain.

If an API does not match the flag, the flag is ignored. For example, using **GET\_ABILITY\_INFO\_WITH\_PERMISSION** to obtain the application information does not affect the result.

Flags can be used together. For example, you can use the combination of **GET\_APPLICATION\_INFO\_WITH\_PERMISSION** and **GET\_APPLICATION\_INFO\_WITH\_DISABLE** to obtain the result that contains both application permission information and disabled application information.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| GET\_BUNDLE\_DEFAULT | 0x00000000 | Obtains the default application information. |
| GET\_BUNDLE\_WITH\_ABILITIES | 0x00000001 | Obtains the bundle information with the ability information. |
| GET\_ABILITY\_INFO\_WITH\_PERMISSION | 0x00000002 | Obtains the ability information with the permission information. |
| GET\_ABILITY\_INFO\_WITH\_APPLICATION | 0x00000004 | Obtains the ability information with the application information. |
| GET\_APPLICATION\_INFO\_WITH\_PERMISSION | 0x00000008 | Obtains the application information with the permission information. |
| GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION | 0x00000010 | Obtains the bundle information with the information about the required permissions. |
| GET\_ABILITY\_INFO\_WITH\_METADATA8+ | 0x00000020 | Obtains the ability metadata information. |
| GET\_APPLICATION\_INFO\_WITH\_METADATA8+ | 0x00000040 | Obtains the application metadata information. |
| GET\_ABILITY\_INFO\_SYSTEMAPP\_ONLY8+ | 0x00000080 | Obtains the ability information of system applications. |
| GET\_ABILITY\_INFO\_WITH\_DISABLE8+ | 0x00000100 | Obtains information about disabled abilities. |
| GET\_APPLICATION\_INFO\_WITH\_DISABLE8+ | 0x00000200 | Obtains information about disabled applications. |
| GET\_ALL\_APPLICATION\_INFO | 0xFFFF0000 | Obtains all application information. |

#### BundleOptionsdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/sCePtgpRR4KUGa_dtxyang/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02516DD3F5F273F3C03714B053C7CB17670A1B8BCB7F93C6803A498F6D5B2CAB)

This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.

Options that contain the user ID.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| userId | number | No | Yes | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |

#### AbilityTypedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/w2H4hlUDT5uSUKbZJ4rWQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37C560206ED61838528F195D57B21B3DA4BCCF054A8FECE076A197305CC45593)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager.AbilityType](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#abilitytype) instead.

Enumerates the ability types.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | None | Unknown ability type. |
| PAGE | None | FA developed using the Page template to provide the capability of interacting with users. |
| SERVICE | None | PA developed using the Service template to provide the capability of running tasks in the background. |
| DATA | None | PA developed using the Data template to provide unified data access for external systems. |

#### DisplayOrientationdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/JhgK2-v9SB-7_ZEsFTn7Jw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=664B87A3C13036273E100FE5966CD97454434F5F9AC12D41CBD2093D4F66AAEC)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager.DisplayOrientation](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#displayorientation) instead.

Enumerates display orientations.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | None | Unspecified display orientation. |
| LANDSCAPE | None | Landscape orientation. |
| PORTRAIT | None | Portrait orientation. |
| FOLLOW\_RECENT | None | Orientation same as that of the nearest ability in the stack. |

#### LaunchModedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/swu0UXXYTJuzIrJlfe0Zuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=658794336939FDC1F79FAF98874A0E577D4BD3841534CC86D551DBD95B8129D5)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager.LaunchType](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#launchtype) instead.

Enumerates the ability launch modes.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| SINGLETON | 0 | The ability has only one instance. |
| STANDARD | 1 | The ability can have multiple instances. |

#### AbilitySubTypedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/suU-lYIZSAWxgknzbNwmaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E76F0BF927895614DF9934651BD0A26BB1CED05CE0298176CD62C38B44784A5)

This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.

Enumerates the ability subtypes.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | Undefined ability subtype. |
| CA | 1 | Ability that has a UI. |

#### ColorModedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/d5h0rySTSWiLZ8ykiP-dxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8377E05037C72BA55381790D1CDB511FF7A8A075F42A97994270B614EA777E01)

This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.

Enumerates the color modes of applications and widgets.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO\_MODE | \-1 | Auto mode. |
| DARK\_MODE | 0 | Dark mode. |
| LIGHT\_MODE | 1 | Light mode. |

#### GrantStatusdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/OgGnGHJOSTe6x9jOvLxbMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0169642574BA793575752905C1BA99E7A0ACCB34EC48CAF3CE7A842A330C7DD7)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager.PermissionGrantState](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#permissiongrantstate) instead.

Enumerates the permission grant states.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| PERMISSION\_DENIED | \-1 | Permission denied. |
| PERMISSION\_GRANTED | 0 | Permission granted. |
