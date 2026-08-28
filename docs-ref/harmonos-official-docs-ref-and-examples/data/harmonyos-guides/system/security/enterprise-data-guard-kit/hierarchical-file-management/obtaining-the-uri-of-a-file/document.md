# Obtaining the URI of a File

#### Use Case

Enterprise Data Guard Kit allows apps to obtain file path information. A file path can be directly opened by an app to determine whether it is a KIA file.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getFileUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section10575755137)(path: string, callback: AsyncCallback<[FilePathInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1026911633210)\>): void

 | 

Obtains file path information using a callback.

 |
| 

[getFileUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1297191246)(path: string): Promise<[FilePathInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1026911633210)\>

 | 

Obtains file path information using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the **getFileUri** API to obtain the URI of a file in either of the following ways:
    
    -   Obtain a file URI using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function getFileUriCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/100/hmdfs/account/files/test/test.txt';
      guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
        if (err) {
          console.error(\`Failed to get file uri. Code: ${err.code}, message: ${err.message}.\`);
        } else {
          console.info(\`Succeeded in getting file uri.\`);
        }
      });
    }
    
    -   Obtain a file URI using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function getFileUriPromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/100/hmdfs/account/files/test/test.txt';
      guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
        console.info(\`Succeeded in getting the uri of file.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get the uri of file. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
