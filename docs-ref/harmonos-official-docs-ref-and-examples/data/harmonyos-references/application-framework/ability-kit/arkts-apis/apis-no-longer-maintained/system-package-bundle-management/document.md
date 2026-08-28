# @system.package (Bundle Management)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/A6gjgk5wRkm0MpbQn52DpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD0E5A29D38DBD15829F32B95767D612D06F930E130B294B19BEED8E22AFCB45)

-   The APIs of this module have been deprecated since API version 9. You are advised to use [@ohos.bundle.bundleManager](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md) instead.
    
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    

#### Modules to Import

import Package from '@system.package';

#### package.hasInstalled(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/bGNZQWLwQry73CBh2wlUTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7D731A506B5E852107C361F6EE3190AF74058CBD37F5FEF31CA48DD94CB44A6)

This API has been supported since API version 3 and deprecated since API version 9. You are advised to use [getBundleInfo](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfo14) instead.

hasInstalled(options: CheckPackageHasInstalledOptions): void

Checks whether an application exists, or whether a native application has been installed.

**System capability**: SystemCapability.BundleManager.BundleFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CheckPackageHasInstalledOptions](#checkpackagehasinstalledoptions) | Yes | Options. |

**Example**

import Package from '@system.package';

@Entry
@Component
struct MainPage {
  hasInstalled() {
    Package.hasInstalled({
      bundleName: 'com.example.bundlename',
      success: (data) => {
        console.log('package has installed: ' + data);
      },
      fail: (msg:string, code) => {
        console.log('query package fail, code: ' + code + ', data: ' + msg);
      },
    });
  }
  build() {
  }
}

#### CheckPackageHasInstalledResponse

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/iDjMPJ7mRWCm5UAok2QwQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A971324C73BC596E91A138DFAA416045BFF6193ECACFA857295F4E6E1ADB36C)

This API has been supported since API version 3 and deprecated since API version 9.

Checks whether a bundle has been installed.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | boolean | Yes | Check result for whether the bundle has been installed. **true** if installed, **false** otherwise. |

#### CheckPackageHasInstalledOptions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/9STHDzzUQFSxqoxNC5dhag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A778138C25541022BD404A3D85BC32A7BE5ACF749ACE102BB6470C752270835)

This API has been supported since API version 3 and deprecated since API version 9.

Defines the options used for checking whether a bundle has been installed.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name. |
| success | Function | No | Called when API call is successful. |
| fail | Function | No | Called when API call has failed. |
| complete | Function | No | Called when API call is complete. |
