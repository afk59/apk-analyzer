# How do I implement HTTP concurrent download?

You can use the APIs provided by the **request** module to implement upload and download. Currently, a maximum of four concurrent download tasks are supported.

The code snippet is as follows:

import { request } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Using AppStore to store UIContext in ExitAbility
const context = AppStorage.get("context") as UIContext;
let downloadTask: request.DownloadTask;
try {
  request.downloadFile(context.getHostContext(), { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    downloadTask = data;
  }).catch((err: BusinessError) => {
    console.error(\`Failed to request the download. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (err) {
  console.error(\`Failed to request the download. err: ${JSON.stringify(err)}\`);
}

**Reference**

[@ohos.request (Upload and Download)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-request)
