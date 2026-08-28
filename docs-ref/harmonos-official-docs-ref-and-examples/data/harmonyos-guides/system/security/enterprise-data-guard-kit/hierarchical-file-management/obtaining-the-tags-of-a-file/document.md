# Obtaining the Tags of a File

#### Use Case

Enterprise Data Guard Kit allows apps to obtain the tags of a file so HarmonyOS can effectively manage files based on control policies and file tags.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[queryFileTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section195124201031)(path: string, callback: AsyncCallback<[FileTagInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section118461622113311)\>): void

 | 

Obtains file tags using a callback.

 |
| 

[queryFileTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section62600419317)(path: string): Promise<[FileTagInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section118461622113311)\>

 | 

Obtains file tags using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the **queryFileTag** API to obtain file tags in either of the following ways:
    
    -   Obtain file tags using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function queryFileTagCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test/test.txt';
      guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
        if (err) {
          console.error(\`Failed to query file tag. Code: ${err.code}, message: ${err.message}.\`);
          return;
        }
        console.info(\`Succeeded in querying file tag.\`);
      });
    }
    
    -   Obtain file tags using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function queryFileTagPromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test/test.txt';
      guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
        console.info(\`Succeeded in querying file tag.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to query file tag. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
