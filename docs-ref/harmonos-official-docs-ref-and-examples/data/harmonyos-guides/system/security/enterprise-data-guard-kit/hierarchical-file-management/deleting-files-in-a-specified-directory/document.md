# Deleting Files in a Specified Directory

#### Use Case

Enterprise Data Guard Kit allows apps to delete files in a common directory.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[deleteFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section102212058545)(path: string, callback: AsyncCallback<void>): void

 | 

Deletes files in a specified path using a callback.

 |
| 

[deleteFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section869414101554)(path: string): Promise<void>

 | 

Deletes files in a specified path using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the **deleteFile** API to delete files in a specified directory that is scanned using either of the following ways:
    
    -   Delete files in a specified path using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function deleteFileCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
      guard.deleteFile(path, (err: BusinessError) => {
        if (err) {
          console.error(\`Failed to delete file. Code: ${err.code}, message: ${err.message}.\`);
        } else {
          console.info(\`Succeeded in deleting file.\`);
        }
      });
    }
    
    -   Delete files in a specified path using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function deleteFilePromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt';
      guard.deleteFile(path).then(() => {
        console.info(\`Succeeded in deleting file.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to delete file. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
