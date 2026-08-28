# Setting a Watermark Image for KIA Files

#### Use Case

Enterprise Data Guard Kit provides the capability of setting a watermark image for KIA files.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setKiaWatermarkImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section7932161212533)(image: Uint8Array, info: string): Promise<void>

 | 

Sets the KIA file watermark image using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the [setKiaWatermarkImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section7932161212533) API to set the KIA file watermark image.
    
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    async function testSetKiaWaterMarkImage() {
      try {
        let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
        let imagePath: string = '/data/service/el2/100/hmdfs/account/files/Docs/Documents/1.png';
        let fd: number = await guard.openFile(imagePath);
        let stat: fs.Stat = fs.statSync(fd);
        let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
        fs.readSync(fd, buffer);
    
        let image: Uint8Array = new Uint8Array(buffer);
        let info: string = new Date().toLocaleString();
        guard.setKiaWatermarkImage(image, info).then(() => {
          console.info(\`Succeeded in setting the watermark image for Kia file.\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.\`);
        })
      } catch (e) {
        console.error(\`\[scanFileGuard\] testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}\`);
      }
    }
