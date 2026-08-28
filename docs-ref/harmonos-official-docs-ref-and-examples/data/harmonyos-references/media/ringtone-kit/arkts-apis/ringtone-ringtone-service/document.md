# ringtone (Ringtone Service)

The **ringtone** module provides the function of setting ringtones.

**Start version**: 5.0.0(12)

#### Module Import

import { ringtone } from '@kit.RingtoneKit'

#### RingtoneType

Enumeration of ringtone types.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CALL

 | 

0

 | 

Ringtone for incoming calls.

 |
| 

MESSAGE

 | 

1

 | 

Ringtone for SMS messages.

 |
| 

NOTIFICATION

 | 

2

 | 

Ringtone for notifications.

 |
| 

ALARM

 | 

3

 | 

Ringtone for alarms.

 |

#### RingtoneErrors

Enumeration of error codes of the APIs for setting ringtones and obtaining supported ringtone types and ringtone file types.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ERROR\_INVALID\_PARAM

 | 

401

 | 

Invalid parameter.

 |
| 

ERROR\_USER\_CANCELED

 | 

1011600001

 | 

The operation is canceled by the user.

 |
| 

ERROR\_FILE\_NOT\_FOUND

 | 

1011600002

 | 

The file does not exist.

 |
| 

ERROR\_SHOW\_FAILED

 | 

1011600003

 | 

The ringtone dialog box fails to be displayed.

 |
| 

ERROR\_CALL\_SYSTEM\_API\_FAILED

 | 

1011600004

 | 

Failed to call the system API.

 |
| 

ERROR\_SYSTEM

 | 

1011699999

 | 

Internal system error.

 |

#### ringtone.getSupportedRingtoneTypes

getSupportedRingtoneTypes(): Array<RingtoneType>

Queries custom ringtone types supported by the system.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Array<[RingtoneType](#section18108304244)\>

 | 

Custom ringtone types supported by the system.

 |

**Example**:

import { ringtone } from '@kit.RingtoneKit'
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP\_TAG = "Msc\_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button("Query Supported Custom Ringtone Types")
          .width(200)
          .height(50)
          .onClick(() => {
            let typeList: Array<ringtone.RingtoneType> = ringtone.getSupportedRingtoneTypes()
            hilog.info(DOMAIN, APP\_TAG, 'getSupportedRingtoneTypes : ' + JSON.stringify(typeList));
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}

#### ringtone.getSupportedDataTypes

getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>

Queries the file types supported by a ringtone type.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ringtoneType

 | 

[RingtoneType](#section18108304244)

 | 

Yes

 | 

Ringtone type to be queried.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Array<[uniformTypeDescriptor.UniformDataType](../../../../application-framework/arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md#uniformdatatype)\>

 | 

File types supported by a ringtone type.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid parameter.

 |

**Example**:

import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP\_TAG = "Msc\_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button("Query Supported File Types")
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let typeList: Array<uniformTypeDescriptor.UniformDataType> =
                ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION)
              hilog.info(DOMAIN, APP\_TAG, 'getSupportedDataTypes3----- : ' + JSON.stringify(typeList));
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP\_TAG,
                'getSupportedDataType error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}

#### ringtone.getSupportedMaxDuration

getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number

Queries the maximum duration supported by a ringtone type and file type.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

ringtoneType

 | 

[RingtoneType](#section18108304244)

 | 

Yes

 | 

Ringtone type to be queried.

 |
| 

dataType

 | 

[uniformTypeDescriptor.UniformDataType](../../../../application-framework/arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md#uniformdatatype)

 | 

Yes

 | 

File type to be queried.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Maximum duration (unit: second) supported by the ringtone and file types. The maximum duration for an alarm ringtone is 300s, for an SMS message ringtone and notification ring tone is 7s, and for an incoming call ringtone is 60s.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid parameter.

 |

**Example**:

import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP\_TAG = "Msc\_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button("Query Maximum Duration")
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let maxDuration: number =
                ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE,
                  uniformTypeDescriptor.UniformDataType.MP3)
              hilog.info(DOMAIN, APP\_TAG, 'getSupportedMaxDuration: ' + maxDuration);
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP\_TAG,
                'getSupportedMaxDuration error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}

#### ringtone.startRingtoneSetting

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback<RingtoneType>): void

Opens the ringtone setting pop-up window and returns the type of the tapped ringtone. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |
| 

path

 | 

string

 | 

Yes

 | 

Path of the file you have the permission to access.

 |
| 

name

 | 

string

 | 

Yes

 | 

File name. The value contains a maximum of 1000 characters.

 |
| 

callback

 | 

AsyncCallback<[RingtoneType](#section18108304244)\>

 | 

Yes

 | 

Ringtone types set by users, which are returned through a callback.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid parameter.

 |
| 

1011600001

 | 

User canceled.

 |
| 

1011600002

 | 

The media file is not found.

 |
| 

1011600003

 | 

Failed to show the dialog box.

 |
| 

1011600004

 | 

Failed to call the system API.

 |
| 

1011699999

 | 

System exception.

 |

import { common } from '@kit.AbilityKit';
import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP\_TAG = "Msc\_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Stack() {
      Column() {
        Button ("Set Ringtone OGG Format")
          .width(200)
          .height(50)
          .onClick(async () => {
            let audioPath: string = this.context.filesDir + '/test.ogg'
            let splitList = audioPath.split('/')
            let fileName = splitList\[splitList.length - 1\]
            hilog.info(DOMAIN, APP\_TAG, 'audioPath:' + audioPath)
            hilog.info(DOMAIN, APP\_TAG, 'fileName:' + fileName)

            try {
              ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, res) => {
                hilog.info(DOMAIN, APP\_TAG, 'Return value:' + JSON.stringify(res))
              })
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP\_TAG,
                'accessSync failed with error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}

#### ringtone.startRingtoneSetting

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise<RingtoneType>

Opens the ringtone setting pop-up window and returns the type of the tapped ringtone. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Ringtone.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |
| 

path

 | 

string

 | 

Yes

 | 

Path of the file you have the permission to access.

 |
| 

name

 | 

string

 | 

Yes

 | 

File name. The value contains a maximum of 1000 characters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RingtoneType](#section18108304244)\>

 | 

Ringtone types set by users, which are returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid parameter.

 |
| 

1011600001

 | 

User canceled.

 |
| 

1011600002

 | 

The media file is not found.

 |
| 

1011600003

 | 

Failed to show the dialog box.

 |
| 

1011600004

 | 

Failed to call the system API.

 |
| 

1011699999

 | 

System exception.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { ringtone } from '@kit.RingtoneKit'
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP\_TAG = "Msc\_Demo"
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Stack() {
      Column() {
        Button ("Set Ringtone OGG Format")
          .width(200)
          .height(50)
          .onClick(async () => {
            let audioPath: string = this.context.filesDir + '/test.ogg'
            let splitList = audioPath.split('/')
            let fileName = splitList\[splitList.length - 1\]
            hilog.info(DOMAIN, APP\_TAG, 'audioPath:' + audioPath)
            hilog.info(DOMAIN, APP\_TAG, 'fileName:' + fileName)
            try {
              await ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
                hilog.info(DOMAIN, APP\_TAG, 'Return value:' + JSON.stringify(res))
              })
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP\_TAG,
                'accessSync failed with error message: ' + err.message + ', error code: ' + err.code);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
