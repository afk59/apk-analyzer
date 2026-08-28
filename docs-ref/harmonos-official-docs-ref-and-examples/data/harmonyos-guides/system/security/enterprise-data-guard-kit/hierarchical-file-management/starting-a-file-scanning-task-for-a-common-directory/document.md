# Starting a File Scanning Task for a Common Directory

#### Use Case

Enterprise Data Guard Kit allows apps to scan files in a common directory to obtain the file list.

#### API Description

For details about these APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[startFileScanTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section5572254110)(type: [CommonDirScanType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1753862116813), callback: [ScanFileCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1747318273273), batchNum?: number): void

 | 

Scans a common directory and returns the result using a callback.

 |
| 

[startFileScanTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section17212835417)(path: string, callback: [ScanFileCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section1747318273273), batchNum?: number): void

 | 

Scans a specified directory and returns the result using a callback.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and declare the callback function for returning the scanning result.
    
    -   Scan files in the common directory and check the scanning result.
    
    function startFileScanTaskUnderCommonDir() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let onReceiveFileList: (files: string\[\]) => void = (files: Array<string>) => {
        files.forEach((value: string, index: number) => {
          console.info(\`Succeeded in getting file: ${value}.\`);
        })
      };
      let onCompleteScanTask: (count: number) => void = (count: number) => {
        console.info(\`Succeeded in getting count: ${count}.\`);
      };
      let scanFileCallback: fileGuard.ScanFileCallback = {
        onReceiveFileList: onReceiveFileList,
        onTaskCompleted: onCompleteScanTask
      };
      guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA\_ONLY, scanFileCallback);
    }
    
    -   Scan the files in a specified directory under the common directory and check the scanning result.
    
    function startFileScanTaskUnderSpecifiedDir() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let path: string = '/data/service/el2/test';
      let onReceiveFileList: (files: string\[\]) => void = (files: Array<string>) => {
        files.forEach((value: string, index: number) => {
          console.info(\`Succeeded in getting file: ${value}.\`);
        })
      };
      let onCompleteScanTask: (count: number) => void = (count: number) => {
        console.info(\`Succeeded in getting count: ${count}.\`);
      };
      let scanFileCallback: fileGuard.ScanFileCallback = {
        onReceiveFileList: onReceiveFileList,
        onTaskCompleted: onCompleteScanTask
      };
      guard.startFileScanTask(path, scanFileCallback);
    }
