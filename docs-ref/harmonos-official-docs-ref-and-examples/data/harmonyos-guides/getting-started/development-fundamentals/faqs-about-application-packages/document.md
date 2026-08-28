# FAQs About Application Packages

#### How do I obtain the fingerprint in the signature information?

-   Call an API.

You can call [bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself) to obtain the bundle information, which contains the signature information, and signature information in turn contains fingerprint information.

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION |
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
    console.info('testTag', 'getBundleInfoForSelf successfully. fingerprint: ', bundleInfo.signatureInfo.fingerprint);
  }).catch((err: BusinessError) => {
    console.error('testTag', 'getBundleInfoForSelf failed. Cause: ', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('testTag', 'getBundleInfoForSelf failed: %{public}s', message);
}

-   Use [Bundle Manager](../../../system/debugging-tools/debugging-commands/bundle-manager/document.md) (bm).

hdc shell
# Replace \*\*com.example.myapplication\*\* with the actual bundle name.
bm dump -n com.example.myapplication | grep fingerprint

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/jwunPHbDRimawvDWG3smIw/en-us_image_0000002568764063.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2BFE6E424B7EF872CF0F06833037A45891B8A5732B370B9D9EEBCBCFC3B9D24)

-   Use the **keytool**. For details, see [Generating a Signing Certificate Fingerprint](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/appgallerykit-preparation-game-0000001055356911#section147011294331).
    

#### What is appIdentifier?

**appIdentifier**, generated during application signing, is a field in the [profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090) and is the unique identifier of an application. There are two ways to generate an application identifier:

1.  Randomly generate the **appIdentifier** field through [automatic signing](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section18815157237) on DevEco Studio. Signing on different devices or re-signing will result in different values of **appIdentifier**.
2.  Manually configure the signature and apply for a certificate from AppGallery Connect (AGC). The value of the **appIdentifier** field in the [debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278) or [release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090) is fixed and comes from the [app ID](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506#section16423184171915) allocated by AGC during the creation of the application. In this case, the **appIdentifier** field does not change along the application lifecycle, including version updates, certificate changes, public and private key changes, and application transfers.

Therefore, manual signing is recommended in scenarios where **appIdentifier** must remain unchanged, such as cross-device debugging, cross-application interaction debugging, or multi-user development with a shared key. For details, see [Use Cases for Automatic and Manual Signing](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section54361623194519).

#### How do I obtain appIdentifier from application information?

-   You can call [bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself) to obtain the bundle information, which contains the signature information, and signature information in turn contains the **appIdentifier**.

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION |
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
    console.info('testTag', 'getBundleInfoForSelf successfully. appIdentifier:', bundleInfo.signatureInfo.appIdentifier);
  }).catch((err: BusinessError) => {
    console.error('testTag', 'getBundleInfoForSelf failed. Cause:', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('testTag', 'getBundleInfoForSelf failed:', message);
}

-   Use the [bm](../../../system/debugging-tools/debugging-commands/bundle-manager/document.md) tool.

hdc shell
# Replace \*\*com.example.myapplication\*\* with the actual bundle name.
bm dump -n com.example.myapplication | grep appIdentifier

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/CbrUWT0pRLCBG6bNYJq-fw/en-us_image_0000002537764338.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01B6D8A2F2C421FE3EDEDC40A80455935281FA56063D138B2A1947AC6B548B4A)

#### What Is appId?

**appId**, the unique identifier of an application, consists of a bundle name, underscore (\_), and Base64-encoded public key of the certificate. Since it changes with the public key of the signing certificate, you are advised to use [appIdentifier](#what-is-appidentifier) as the unique identifier of an application.

#### How do I obtain appId from application information?

-   You can call [bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself) to obtain the bundle information, which contains the signature information, and signature information in turn contains the **appId**.

import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION |
  bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_SIGNATURE\_INFO;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo:bundleManager.BundleInfo) => {
    console.info('testTag', 'getBundleInfoForSelf successfully. appId:', bundleInfo.signatureInfo.appId);
  }).catch((err: BusinessError) => {
    console.error('testTag', 'getBundleInfoForSelf failed. Cause:', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('testTag', 'getBundleInfoForSelf failed:', message);
}

-   Use the [bm](../../../system/debugging-tools/debugging-commands/bundle-manager/document.md) tool.

hdc shell
# Replace \*\*ohos.app.hap.myapplication\*\* with the actual bundle name.
bm dump -n ohos.app.hap.myapplication |grep '"appId":'

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/GdpgmfbnRleseEoe8uVZ_A/en-us_image_0000002537924278.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E1B24F7B6E1CEEC50C65BD0E32F277453A944E620BE375837ADDBB703906E0E)
