# Setting the KIA File List

#### Use Case

Enterprise Data Guard Kit allows apps to set a KIA file list so HarmonyOS can effectively manage files in the list based on control policies.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setKiaFilelist](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section276855317514)(filelist: string, callback: AsyncCallback<void>): void

 | 

Sets the KIA file list using a callback.

 |
| 

[setKiaFilelist](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section920033180)(filelist: string): Promise<void>

 | 

Sets the KIA file list using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the **setKiaFilelist** API to convert the KIA file list into the string type and set the KIA file list in either of the following ways:
    
    -   Set the KIA file list using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function setKiaFilelistCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let fileListStr: string = '{' +
        '"kia\_filelist":' +
        '\["' +
        '/data/service/el2/100/hmdfs/account/files/Documents/Desktop/aaa.docx",' +
        '"/data/service/el2/100/hmdfs/account/files/Documents/Desktop/bbb.docx"' +
        '\]' +
        '}';
      guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
        if (err) {
          console.error(\`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.\`);
        } else {
          console.info(\`Succeeded in setting the list of KIA file.\`);
        }
      });
    }
    
    -   Set the KIA file list using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function setKiaFilelistPromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let fileListStr: string = '{' +
        '"kia\_filelist":' +
        '\["' +
        '/data/service/el2/100/hmdfs/account/files/Documents/Desktop/aaa.docx",' +
        '"/data/service/el2/100/hmdfs/account/files/Documents/Desktop/bbb.docx"' +
        '\]' +
        '}';
      guard.setKiaFilelist(fileListStr).then(() => {
        console.info(\`Succeeded in setting the list of KIA file.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
