# How do I obtain the system version?

You can use the [@ohos.deviceInfo (Device Information)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-device-info) module to query device information.

The code snippet is as follows:

import { deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let displayVersionInfo: string = deviceInfo.displayVersion; // product version
let osFullNameInfo: string = deviceInfo.osFullName; // system version
let versionIdInfo: string = deviceInfo.versionId; // version ID

@Entry
@Component
struct GetSysVersion {
  build() {
    Row() {
      Column() {
        Button('get device info')
          .onClick(() => {
            hilog.info(0x000, 'displayVersion TAG', \`displayVersion:${displayVersionInfo}\`);
            hilog.info(0x000, 'osFullName TAG', \`osFullName:${osFullNameInfo}\`);
            hilog.info(0x000, 'versionId TAG', \`versionId:${versionIdInfo}\`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
