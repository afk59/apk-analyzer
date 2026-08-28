# Revoking User Authorization

#### Use Cases

If you want to cancel the access to Screen Time Guard Kit, your app can call the API for revoking user authorization. Once user authorization is revoked, your app will be unable to access or use time management and other related functions on user devices. If your app still attempts to call screen time guard-related APIs, the system will return an error code indicating user authorization not granted, ensuring the security and privacy protection.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/CFb8lNGzRsy2ELP4BRCpRw/en-us_image_0000002504425155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FFDD4B43DAAE8C59DA5A705424BBFA3AC5F8A0CBA4CB729A1E78D64BA6F4BB5)

The process is as follows:

1\. To cancel the access to Screen Time Guard Kit, your app needs to call the API for revoking user authorization. Then, Digital Balance is started to query the app's authorization status in the local database.

2\. If the status is unauthorized, the result is directly returned. If the status is authorized, it is changed to unauthorized and then the result is returned.

#### API Description

The table below lists the key APIs for revoking user authorization. For details about the APIs, please refer to the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-arkts).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[revokeUserAuth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section10875605199)(): Promise<void>

 | 

Revokes user authorization to access related APIs of Screen Time Guard Kit.

 |
| 

[getUserAuthStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section12377142072717)(): Promise<[AuthStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/screentimeguard-guardservice#section92636497495)\>

 | 

Obtains the user authorization status.

 |

#### Development Procedure

1\. Import required modules.

import { guardService } from '@kit.ScreenTimeGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2\. Call **revokeUserAuth** to revoke user authorization.

async function testRevokeUserAuth() {
  try {
    await guardService.revokeUserAuth();
  } catch (err) {
    const message = (err as BusinessError).message;
    const code = (err as BusinessError).code;
    hilog.error(0x0000, \`ScreenTimeGuard:revokeUserAuth\`, \`revokeUserAuth failed with error code: ${code}, message: ${message}\`);
  }
}

3\. Obtain the user authorization status.

async function testGetUserAuthStatus() {
  try {
    const status = await guardService.getUserAuthStatus();
    hilog.info(0x0000, \`ScreenTimeGuard:getUserAuthStatus\`, \`user auth status: ${status}\`);
  } catch (err) {
    const message = (err as BusinessError).message;
    const code = (err as BusinessError).code;
    hilog.error(0x0000, \`ScreenTimeGuard:getUserAuthStatus\`, \`getUserAuthStatus failed with error code: ${code}, message: ${message}\`);
  }
}
