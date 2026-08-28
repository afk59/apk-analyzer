# File Path Conversion API

#### Use Case

Scenario Fusion Kit provides an API for converting file paths in upgrade or clone scenarios from HarmonyOS 4 or earlier to HarmonyOS 5 or later.

#### API Description

The following table describes the API for obtaining URI information of the files to be converted. For other APIs, please refer to the [fileUriService (File Path Conversion APIs)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-fileuriresult).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[convertFileUris](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-fileuriresult#section1272664195920)(sourceFileUris: Array<string>): Promise<Array<[FileUriResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-fileuriresult#section443872764410)\>>

 | 

Obtains the request object that contains the URI information of the files to be converted.

 |

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { fileUriService } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Pass the list of file path parameters to be converted and call the relevant API to obtain the converted file path list. The code is as follows:
    
    try {
      // **'/storage/emulated/0/Pictures/test.gif'** indicates the file path of **test.gif**.
      let sourceFileUris: Array<string> =
        \['100','content://media/external/files/10', '/storage/emulated/0/Pictures/test.gif',
          '/storage/emulated/0/media/com.test/test.mp4'\];
      fileUriService.convertFileUris(sourceFileUris).then(result => {
        hilog.info(0x0000, 'testTag', 'succeeded in converting file uris');
        result.forEach(data => {
          switch (data.targetType) {
            case fileUriService.TargetType.UNKNOWN:
              hilog.info(0x0000, 'testTag', 'input uri or path is not exist');
              break;
            case fileUriService.TargetType.MEDIA:
              hilog.info(0x0000, 'testTag', 'converted media uri: %{public}s', data.targetUri);
              break;
            case fileUriService.TargetType.FILE:
              // If the input path actually exists, **targetUri** in the result will be the converted URI.
              // Otherwise, **targetUri** is the same as the input path value without conversion, and **targetType** is **UNKNOWN**.
              hilog.info(0x0000, 'testTag', 'converted file path: %{public}s', data.targetUri);
              break;
          }
        })
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
    }
