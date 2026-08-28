# Opening a File

#### Use Case

Common apps cannot directly access files in a common directory. To address this problem, Enterprise Data Guard Kit provides APIs for apps to obtain the file descriptor (FD) of a file for opening it.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[openFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section132239575117)(path: string, callback: AsyncCallback<number>): void

 | 

Obtains the FD of a file at a specified path using a callback.

 |
| 

[openFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1292915920212)(path: string): Promise<number>

 | 

Obtains the FD of a file at a specified path using a promise.

 |
| 

[openFileWrite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section779510429368)(path: string, callback: AsyncCallback<number>): void

 | 

Obtains the write-only FD of a file at a specified path using a callback.

 |
| 

[openFileWrite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section198141025172920)(path: string): Promise<number>

 | 

Obtains the write-only FD of a file at a specified path using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the **openFile** or **openFileWrite** API to obtain the FD of a file at a specified path in either of the following ways:
    
    -   Obtain the FD of a file using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function openFileCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test/test.txt';
      guard.openFile(path, (err: BusinessError, fd: number) => {
        if (err) {
          console.error(\`Failed to open file. Code: ${err.code}, message: ${err.message}.\`);
          return;
        }
        console.info(\`Succeeded in opening file. path: ${path}, fd: ${fd}.\`);
      });
    }
    
    -   Obtain the FD of a file using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function openFilePromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test/test.txt';
      guard.openFile(path).then((fd: number) => {
        console.info(\`Succeeded in opening file. path: ${path} , fd: ${fd}.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to open file. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
