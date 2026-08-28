# ErrorObserver

The ErrorObserver module defines an observer to listen for application errors. It can be used as an input parameter in [ErrorManager.on](../../../both-models-recommended/ohos-app-ability-errormanager-error-management-module/document.md#errormanageronerror) to listen for errors that occur in the current application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/n5Npxc1eT3idOcQMtMU4xA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB0396397E959DF9E523F9761B70C237AF2AA154FF6D94D846EA94D2A14C2850)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { errorManager } from '@kit.AbilityKit';

#### ErrorObserver.onUnhandledException

onUnhandledException(errMsg: string): void

Called when an uncaught exception occurs in the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| errMsg | string | Yes | Message and error stack trace about the exception. |

**Example**

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
  }
};

try {
  errorManager.on('error', observer);
} catch (error) {
  console.error(\`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}\`);
}

#### ErrorObserver.onException10+

onException?(errObject: Error): void

Called when the application encounters an exception and reports it to the JavaScript layer.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| errObject | Error | Yes | Event name, message, and error stack of the exception. |

**Example**

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
  },
  onException(errorObj) {
    console.error('onException, name: ', errorObj.name);
    console.error('onException, message: ', errorObj.message);
    if (typeof (errorObj.stack) === 'string') {
      console.error('onException, stack: ', errorObj.stack);
    }
  }
};

try {
  errorManager.on('error', observer);
} catch (error) {
  console.error(\`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}\`);
}
