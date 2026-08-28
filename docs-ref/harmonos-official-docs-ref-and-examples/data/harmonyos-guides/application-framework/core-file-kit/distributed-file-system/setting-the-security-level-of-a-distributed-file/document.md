# Setting the Security Level of a Distributed File

The security capabilities vary with devices. For example, small embedded devices provide fewer security capabilities than tablets. The security requirements also vary with data. For example, personal health information and bank card information are not expected to be accessed by devices of lower security levels. HarmonyOS provides a complete set of data and device classification standards and supports customization of data transfer policies for different devices. For details, see [Access Control by Device and Data Level](../../../arkdata/data-reliability-and-security/access-control-by-device-and-data-level-arkts/document.md).

#### Available APIs

For details about APIs, see [ohos.file.securityLabel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-securitylabel).

Table 1 Security level APIs

| API | Description | Category | Synchronous Programming | Asynchronous Programming |
| :-- | :-- | :-- | :-- | :-- |
| setSecurityLabel | Sets a security level for a file. | Method | Supported | Supported |
| getSecurityLabel | Obtains the security level of a file. | Method | Supported | Supported |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/JQkCpHtfTVOsncoXxXPVIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00F54A439AE24493134D02ADF5788D33FF99EC58A5A25F49AC508EFEAF53F852)

-   In distributed networking, a device can view the files that have a higher security level but cannot access them.
    
-   The default security level of the distributed file system data is S3. Applications can set the security level of files.
    

#### Development Example

Obtain the sandbox path of a file and set the data security level. For details about how to obtain the context, see [Obtaining the Context of UIAbility](../../../ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).

import { securityLabel } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';

// Obtain the sandbox path of the file where the device data level is to be obtained. Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + '/test.txt';

// Open a file.
let file = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
// Set the data level of the file to S0.
securityLabel.setSecurityLabel(filePath, 's0').then(() => {
  console.info('Succeeded in setSecurityLabeling.');
  fs.closeSync(file);
}).catch((err: BusinessError) => {
  console.error(\`Failed to setSecurityLabel. Code: ${err.code}, message: ${err.message}\`);
});
