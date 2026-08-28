# fileUriService (File Path Conversion APIs)

This module provides capabilities for converting file paths in upgrade or clone scenarios from HarmonyOS 4 or earlier to HarmonyOS 5 or later.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScenarioFusionComponent.FileUriService

**Start version**: 5.0.2(14)

#### Module Import

import { fileUriService } from '@kit.ScenarioFusionKit';

#### FileUriResult

Provides an object for file path conversion in convergent scenarios.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScenarioFusionComponent.FileUriService

**Start version**: 5.0.2(14)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sourceUri

 | 

string

 | 

No

 | 

No

 | 

Source file path.

 |
| 

targetUri

 | 

string

 | 

No

 | 

No

 | 

Target file path.

 |
| 

targetType

 | 

[TargetType](#section722791916597)

 | 

No

 | 

No

 | 

File type enumeration.

 |

#### TargetType

Defines the supported file types for the object URI.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScenarioFusionComponent.FileUriService

**Start version**: 5.0.2(14)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNKNOWN

 | 

0

 | 

Unknown file type.

 |
| 

MEDIA

 | 

1

 | 

Media file.

 |
| 

FILE

 | 

2

 | 

File management file.

 |

#### convertFileUris

convertFileUris(sourceFileUris: Array<string>): Promise<Array<FileUriResult>>

Obtains the URI information of the files for which the paths need to be converted. This method returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScenarioFusionComponent.FileUriService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.2(14)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

sourceFileUris

 | 

Array<string>

 | 

Yes

 | 

URI information list of the file paths to be converted. The list can contain 1 to 100 records. If the number of records is out of range, the following error code is displayed: "401 parameter error".

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[FileUriResult](#section443872764410)\>>

 | 

Promise used to return a [FileUriResult](#section443872764410) object.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |

**Example:**

import { fileUriService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

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
