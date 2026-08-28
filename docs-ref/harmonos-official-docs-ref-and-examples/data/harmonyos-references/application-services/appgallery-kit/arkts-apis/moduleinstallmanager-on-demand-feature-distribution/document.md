# moduleInstallManager (On-Demand Feature Distribution)

This module allows you to separate specific functions and resources from the basic module of an app and include them in extended modules. Users can dynamically download the extended modules when using the app. On-demand feature distribution provides functions such as checking whether a module has been installed, requesting on-demand loading, monitoring the download progress, displaying mobile data reminders, and canceling on-demand loading.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/zuuzzk7WRmCpmYZFfSld5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDD78EE87818BFEB1E82A1F486CCA687F2E364AEADFA30510DC0AA708F92AB5C)

Exceptions need to be captured when an API is called.

**Start version**: 4.1.0(11)

#### Modules to Import

import { moduleInstallManager } from '@kit.AppGalleryKit';

#### InstalledModule

Module installation information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

| 
Name

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

moduleName

 | 

string

 | 

Yes

 | 

No

 | 

Module name.

 |
| 

moduleType

 | 

[bundleManager.ModuleType](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#moduletype)

 | 

Yes

 | 

Yes

 | 

Module type.

NOTE:

When the value of **installStatus** is **1**, **moduleType** will return **0** by default, indicating an unknown type.

 |
| 

installStatus

 | 

[InstallStatus](#section45163241117)

 | 

Yes

 | 

No

 | 

Module installation result.

 |

#### ModuleInstallSessionState

Results of calling APIs for initiating requests, registering listeners, and unregistering listeners.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

| 
Name

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

code

 | 

[RequestErrorCode](#section320243191414)

 | 

Yes

 | 

No

 | 

API call result code.

 |
| 

taskStatus

 | 

[TaskStatus](#section1138541061512)

 | 

Yes

 | 

No

 | 

Status code of an on-demand download task.

 |
| 

taskId

 | 

string

 | 

Yes

 | 

Yes

 | 

ID of an on-demand download task. The default value is **0**.

 |
| 

desc

 | 

string

 | 

Yes

 | 

No

 | 

API call result description. The default value is **""**.

 |
| 

modules

 | 

string\[\]

 | 

Yes

 | 

Yes

 | 

List of module names in a download task. The default value is **\[\]**.

 |
| 

totalSize

 | 

number

 | 

Yes

 | 

Yes

 | 

Total size of modules to be downloaded, in bytes. The default value is **0**.

 |
| 

downloadedSize

 | 

number

 | 

Yes

 | 

Yes

 | 

Downloaded size, in bytes. The default value is **0**.

 |

#### InstallStatus

Enumerated status codes contained in the installation result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

INSTALLED

 | 

0

 | 

The specified module has been installed.

 |
| 

NOT\_INSTALLED

 | 

1

 | 

The specified module has not been installed.

 |

#### ReturnCode

Enumerated result codes of calling APIs for adding modules, canceling download, and displaying mobile data reminders.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SUCCESS

 | 

0

 | 

Successful.

 |
| 

FAILURE

 | 

1

 | 

Failed.

 |

#### RequestErrorCode

Enumerated result codes of calling APIs for initiating requests, registering listeners, and unregistering listeners.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

MODULE\_DEBUG\_FILES\_SIZE\_OVER\_LIMIT

 | 

\-10

 | 

The total size of debugging files of all modules in a single request exceeds 8 GB.

NOTE:

**Start version**: 5.0.2(14)

 |
| 

MODULE\_DEBUG\_FILES\_NOT\_EXIST

 | 

\-9

 | 

The module debugging file does not exist.

NOTE:

**Start version**: 5.0.2(14)

 |
| 

MODULE\_ALREADY\_EXISTS

 | 

\-8

 | 

The specified module already exists.

 |
| 

MODULE\_UNAVAILABLE

 | 

\-7

 | 

The module to be downloaded does not exist or does not adapt to the device.

 |
| 

INVALID\_REQUEST

 | 

\-6

 | 

The request is invalid because the information contained in the request is incorrect.

 |
| 

NETWORK\_ERROR

 | 

\-5

 | 

Request failed due to a network exception.

 |
| 

INVOKER\_VERIFICATION\_FAILED

 | 

\-4

 | 

The caller information is abnormal.

 |
| 

FOREGROUND\_REQUIRED

 | 

\-3

 | 

On-demand loading is allowed only when the app is running in the foreground.

 |
| 

ACTIVE\_SESSION\_LIMIT\_EXCEEDED

 | 

\-2

 | 

The request is denied because at least one download task is in progress.

 |
| 

FAILURE

 | 

\-1

 | 

Failed.

 |
| 

SUCCESS

 | 

0

 | 

Successful.

 |
| 

DOWNLOAD\_WAIT\_WIFI

 | 

1

 | 

Mobile data is used. Call [showCellularDataConfirmation](#section104451223191616) to prompt users to confirm whether to use mobile data for download.

 |

#### TaskStatus

Enumerated status codes of download tasks, returned by APIs for initiating requests, registering listeners, and unregistering listeners.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CREATE\_TASK\_FAILED

 | 

\-4

 | 

Failed to create a download task.

 |
| 

HIGHER\_VERSION\_INSTALLED

 | 

\-3

 | 

The same or a later version already exists on the user's device.

 |
| 

TASK\_ALREADY\_EXISTS

 | 

\-2

 | 

The download task already exists.

 |
| 

TASK\_UNFOUND

 | 

\-1

 | 

No download task exists.

 |
| 

TASK\_CREATED

 | 

0

 | 

A download task is created successfully.

 |
| 

DOWNLOADING

 | 

1

 | 

Downloading.

 |
| 

DOWNLOAD\_PAUSING

 | 

2

 | 

Paused.

 |
| 

DOWNLOAD\_WAITING

 | 

3

 | 

Pending download.

 |
| 

DOWNLOAD\_SUCCESSFUL

 | 

4

 | 

Download completed.

 |
| 

DOWNLOAD\_FAILED

 | 

5

 | 

Download failed.

 |
| 

DOWNLOAD\_WAIT\_WIFI

 | 

6

 | 

Scheduled to download with Wi-Fi.

 |
| 

INSTALL\_WAITING

 | 

20

 | 

Waiting to install.

 |
| 

INSTALLING

 | 

21

 | 

Installing.

 |
| 

INSTALL\_SUCCESSFUL

 | 

22

 | 

Installation completed.

 |
| 

INSTALL\_FAILED

 | 

23

 | 

Installation failed.

 |

#### moduleInstallManager.getInstalledModule

getInstalledModule(moduleName: string): InstalledModule

Queries module installation information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

moduleName

 | 

string

 | 

Yes

 | 

Name of the module to be obtained.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[InstalledModule](#section1518175355911)

 | 

Module installation information.

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

Parameter error.

 |
| 

1006500001

 | 

Failed to invoke the BMS.

 |

**Example**:

import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const moduleInfo: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule('AModule');
  hilog.info(0, 'TAG', 'Succeeded in getting installedModule moduleInfo' );
} catch (error) {
  hilog.error(0, 'TAG', \`getting installedModule onError.code is ${error.code}, message is ${error.message}\`);
}

#### InstallProvider

Parent class object of the controller in on-demand loading.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

#### InstallRequest

Parent class object of an on-demand loading request.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

#### ModuleInstallProvider

Implements on-demand loading and provides the capability of creating on-demand loading request objects. This method extends [InstallProvider](#section65611296515).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

#### \[h2\]ModuleInstallProvider.createModuleInstallRequest

createModuleInstallRequest(context: common.UIAbilityContext | common.ExtensionContext): ModuleInstallRequest

Creates an on-demand loading request object. You can set request parameters through the return value.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

context

 | 

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [common.ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md)

 | 

Yes

 | 

Context of the app that calls the API.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ModuleInstallRequest](#section5451648162618)

 | 

On-demand download request object.

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

401

 | 

Parameter error.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'createModuleInstallRequest';

@Entry
@Component
struct CreateModuleInstallRequest {

  build() {
    Column() {
      Button("createModuleInstallRequest")
        .onClick(() => {
          try {
            const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
              new moduleInstallManager.ModuleInstallProvider();
            const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext()  as common.UIAbilityContext;
            const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
              myModuleInstallProvider.createModuleInstallRequest(context);
          } catch (error) {
            hilog.error(0, TAG, \`createModuleInstallRequest onError.code is ${error.code}, message is ${error.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### ModuleInstallRequest

On-demand download request object, which extends [InstallRequest](#section7993755494).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

#### \[h2\]ModuleInstallRequest.addModule

addModule(moduleName: string): ReturnCode

Adds the name of the module to be loaded.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

moduleName

 | 

string

 | 

Yes

 | 

Module name.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ReturnCode](#section44479181311)

 | 

API call result code.

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

401

 | 

Parameter error.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'addModule';

@Entry
@Component
struct AddModule {

  build() {
    Column() {
      Button("addModule")
        .onClick(() => {
          try {
            const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
              new moduleInstallManager.ModuleInstallProvider();
            const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
              myModuleInstallProvider.createModuleInstallRequest(context);
            const aResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule('AModule');
            const bResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule('BModule');
            hilog.info(0, TAG, 'Succeeded in getting aResult:' + aResult + ' bResult:' + bResult);
          } catch (error) {
            hilog.error(0, TAG, \`addModule onError.code is ${error.code}, message is ${error.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### moduleInstallManager.fetchModules

fetchModules(moduleInstallRequest: ModuleInstallRequest): Promise<ModuleInstallSessionState>

Requests on-demand loading and returns the result asynchronously through a promise. This API supports the debug mode.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

moduleInstallRequest

 | 

[ModuleInstallRequest](#section5451648162618)

 | 

Yes

 | 

On-demand loading request object.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ModuleInstallSessionState](#section1535385414136)\>

 | 

Result of calling the API for initiating requests, registering listeners, or unregistering listeners, returned through a promise.

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

Parameter error.

 |
| 

1006500004

 | 

SA connection failed.

 |
| 

1006500008

 | 

Write param into container failed.

 |
| 

1006500009

 | 

Request to service error.

 |
| 

1006500010

 | 

Response from service cannot be recognized.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'fetchModules';

@Entry
@Component
struct FetchModules {

  build() {
    Column() {
      Button("fetchModules")
        .onClick(() => {
          try {
            const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
              new moduleInstallManager.ModuleInstallProvider();
            const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
              myModuleInstallProvider.createModuleInstallRequest(context);
            myModuleInstallRequest.addModule('AModule');
            myModuleInstallRequest.addModule('BModule');
            moduleInstallManager.fetchModules(myModuleInstallRequest)
              .then(() => {
                hilog.info(0, TAG, 'Succeeded in fetching modules success data.' );
              })
          } catch (error) {
            hilog.error(0, TAG, \`fetching modules onError.code is ${error.code}, message is ${error.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### moduleInstallManager.cancelTask

cancelTask(taskId: string): ReturnCode

Cancels a download task.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

taskId

 | 

string

 | 

Yes

 | 

ID of the download task.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ReturnCode](#section44479181311)

 | 

API call result code.

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

Parameter error.

 |
| 

1006500007

 | 

The specified service extension connect failed.

 |
| 

1006500008

 | 

Write param into container failed.

 |
| 

1006500009

 | 

Request to service error.

 |
| 

1006500010

 | 

Response from service cannot be recognized.

 |

**Example**:

import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // **taskId** is a field in **ModuleInstallSessionState** returned by **fetchModules**.
  const taskId: string = '\*\*\*\*\*\*\*\*';
  const rtnCode: moduleInstallManager.ReturnCode = moduleInstallManager.cancelTask(taskId);
  hilog.info(0, 'TAG', "Succeeded in getting result:" + rtnCode);
} catch (error) {
  hilog.error(0, 'TAG', \`cancelTask onError.code is ${error.code}, message is ${error.message}\`);
}

#### moduleInstallManager.showCellularDataConfirmation

showCellularDataConfirmation(context: common.UIAbilityContext | common.ExtensionContext,taskId: string): ReturnCode

Displays a mobile data reminder pop-up.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

context

 | 

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [common.ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md)

 | 

Yes

 | 

Context. Currently, only **UIAbilityContext** and **ExtensionContext** are supported. **UIAbilityContext** is used to check whether the current app is running in the foreground.

 |
| 

taskId

 | 

string

 | 

Yes

 | 

ID of the download task.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ReturnCode](#section44479181311)

 | 

API call result code.

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

Parameter error.

 |
| 

1006500007

 | 

The specified service extension connect failed.

 |
| 

1006500008

 | 

Write param into container failed.

 |
| 

1006500009

 | 

Request to service error.

 |
| 

1006500010

 | 

Response from service cannot be recognized.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'showCellularDataConfirmation';

@Entry
@Component
struct ShowCellularDataConfirmation {

  build() {
    Column() {
      Button("showCellularDataConfirmation")
        .onClick(() => {
          try {
            // **taskId** is a field in **ModuleInstallSessionState** returned by **fetchModules**.
            const taskId: string = '\*\*\*\*\*\*\*\*';
            const context = this.getUIContext().getHostContext()  as common.UIAbilityContext;
            const rtnCode: moduleInstallManager.ReturnCode =
              moduleInstallManager.showCellularDataConfirmation(context, taskId);
            hilog.info(0, TAG, "Succeeded in getting result:" + rtnCode);
          } catch (error) {
            hilog.error(0, TAG, \`showCellularDataConfirmation onError.code is ${error.code}, message is ${error.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### moduleInstallManager.on('moduleInstallStatus')

on(type: 'moduleInstallStatus', callback: Callback<ModuleInstallSessionState>, timeout: number): void

Monitors the progress of the current app download task. Multi-threaded calls are not supported. When a module is loaded, the callback function is used to notify the caller. If the installation is successful and the app is in debug mode, the debug files in the path of the successfully installed module will be deleted.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

type

 | 

string

 | 

Yes

 | 

The value is always **moduleInstallStatus**.

 |
| 

callback

 | 

Callback<[ModuleInstallSessionState](#section1535385414136)\>

 | 

Yes

 | 

Callback function used to return the result.

 |
| 

timeout

 | 

number

 | 

Yes

 | 

Maximum listening duration supported by the registered listener. The default duration is 30 minutes (30 x 60s). If the value exceeds 30 minutes, it is considered as 30 minutes.

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

Parameter error.

 |
| 

1006500002

 | 

The interface is called repeatedly with the same input.

 |
| 

1006500004

 | 

SA connection failed.

 |

**Example**:

import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const timeout = 30 \* 60;
  moduleInstallManager.on('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
    // Register a listener.
    hilog.info(0, 'TAG', 'Succeeded in getting moduleInstallManager.on.' );
  }, timeout)
} catch (error) {
  hilog.error(0, 'TAG', \`moduleInstallManager.on onError.code is ${error.code}, message is ${error.message}\`);
}

#### moduleInstallManager.off('moduleInstallStatus')

off(type: 'moduleInstallStatus', callback?: Callback<ModuleInstallSessionState>): void

Cancels the monitoring of the current app download task's progress. Multi-threaded calls are not supported.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 4.1.0(11)

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

type

 | 

string

 | 

Yes

 | 

The value is always **moduleInstallStatus**.

 |
| 

callback

 | 

Callback<[ModuleInstallSessionState](#section1535385414136)\>

 | 

No

 | 

Callback function used to return the result. If this parameter is left empty, all listeners of the current app will be canceled.

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

Parameter error.

 |
| 

1006500004

 | 

SA connection failed.

 |
| 

1006500006

 | 

The interface is not used together with "on".

 |

**Example**:

import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  moduleInstallManager.off('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
    // Cancel the listener.
    hilog.info(0, 'TAG', 'Succeeded in getting moduleInstallManager.off.' );
  })
} catch (error) {
  hilog.error(0, 'TAG', \`moduleInstallManager.off onError.code is ${error.code}, message is ${error.message}\`);
}
