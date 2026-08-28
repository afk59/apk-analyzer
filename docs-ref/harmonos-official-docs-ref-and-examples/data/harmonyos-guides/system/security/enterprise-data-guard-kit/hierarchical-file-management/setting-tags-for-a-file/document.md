# Setting Tags for a File

#### Use Case

Enterprise Data Guard Kit allows apps to set tags for a file to facilitate identification and classification of files.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setFileTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section41871252322)(path: string, level: [SecurityLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section36136612415), tag: string, callback: AsyncCallback<void>): void

 | 

Sets file tags using a callback.

 |
| 

[setFileTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section8961041532)(path: string, level: [SecurityLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section36136612415), tag: string): Promise<void>

 | 

Sets file tags using a promise.

 |
| 

[setFileCustomTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section379716351208)(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;

 | 

Sets custom tags for a file using a callback.

 |
| 

[setFileCustomTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section123482527015)(path: string, tagList: Array<string>): Promise<void>;

 | 

Sets custom tags for a file using a promise.

 |
| 

[unsetFileCustomTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1510152719118)(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;

 | 

Cancels custom tags for a file using a callback.

 |
| 

[unsetFileCustomTag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section45481034915)(path: string, tagList: Array<string>): Promise<void>;

 | 

Cancels custom tags for a file using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the guard object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215), and call the **setFileTag** or **setFileCustomTag** API to set file tags. You can call the **unsetFileCustomTag** API to cancel custom tags.
    
    -   Set file tags using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function setFileTagCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test/test.txt';
      let tag: string = 'test';
      guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
        if (err) {
          console.error(\`Failed to set file tag. Code: ${err.code}, message: ${err.message}.\`);
          return;
        }
        console.info(\`Succeeded in setting file tag.\`);
      });
    }
    
    -   Set file tags using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function setFileTagPromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test/test.txt';
      let tag: string = 'test';
      guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
        console.info(\`Succeeded in setting file tag.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to set file tag. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
