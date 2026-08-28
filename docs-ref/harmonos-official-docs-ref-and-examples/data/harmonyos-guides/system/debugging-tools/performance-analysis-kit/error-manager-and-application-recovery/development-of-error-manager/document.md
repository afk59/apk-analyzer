# Development of Error Manager

#### Overview

If coding specification issues or errors exist in the code of an application, the application may encounter unexpected errors, for example, uncaught exceptions, while it is running. In such a case, the application may exit unexpectedly. Error logs, however, are usually stored on users' local storage devices, making it inconvenient to locate faults. With the APIs provided by the errorManager module, the related errors and logs will be reported to your service platform for fault locating before application exits.

After the errorManager APIs are used to listen for exceptions and errors, the application does not exit. You are advised to add the synchronous exit operation after the callback is executed. If you only want to obtain error logs, you are advised to use [HiAppEvent](../../event-subscription/introduction-to-hiappevent/document.md) to subscribe to events.

#### Available APIs

The errorManager APIs are provided by [@ohos.app.ability.errorManager(Error Management Module)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-errormanager). Before using the APIs, you need to register an error observer and import it through **import**. For details, see [How to Develop](#how-to-develop).

**errorManager APIs**

| API | Description |
| :-- | :-- |
| on(type: "error", observer: ErrorObserver): number | Registers an observer for application errors. A callback will be invoked when an application error is detected. This API works in a synchronous manner. The return value is the serial number (SN) of the registered observer. |
| off(type: "error", observerId: number, callback: AsyncCallback<void>): void | Unregisters an observer in callback mode. The number is the SN of the registered observer. |
| off(type: "error", observerId: number): Promise<void> | Unregisters an observer in promise mode. The number is the SN of the registered observer. |
| on(type: 'globalErrorOccurred', observer: GlobalObserver): void | 
Registers a global observer for process errors. This is a synchronous API. When the system detects an application exception, the observer is called. (**Recommended**)

Note: This API is supported since API version 18.

 |
| off(type: 'globalErrorOccurred', observer?: GlobalObserver): void | 

Unregisters an observer in callback mode. (**Recommended**)

Note: This API is supported since API version 18.

 |
| on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void | 

Registers a global observer for process errors. This is a synchronous API. When the system detects an application promise exception, the observer is called. (**Recommended**)

Note: This API is supported since API version 18.

 |
| off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void | 

Unregisters an observer in callback mode. (**Recommended**)

Note: This API is supported since API version 18.

 |
| on(type: 'loopObserver', timeout: number, observer: LoopObserver): void | 

Registers an observer for the message processing timeouts of the main thread.

This API can be called only in the main thread. A new observer will overwrite the previous one.

 |
| off(type: 'loopObserver', observer?: LoopObserver): void | Unregisters an observer for the message processing timeouts of the main thread in LoopObserver mode. |
| on(type: 'freeze', observer: FreezeObserver): void | Registers an observer for the main thread freeze event of the application. This API can be called only in the main thread. A new observer will overwrite the previous one. |
| off(type: 'freeze', observer?: FreezeObserver): void | 

Unregisters an observer for the message processing timeouts of the main thread in FreezeObserver mode.

Note: This API is supported since API version 18.

 |
| setDefaultErrorHandler(defaultHandler?: ErrorHandler): ErrorHandler | 

Sets a default error handler. This API can be called only in the main thread. When the **JS\_CRASH** exception occurs, chain callback is supported and the return value is the last registered handler.

Note: This API is supported since API version 21.

 |

When an asynchronous callback is used, the return value can be processed directly in the callback.

When a promise is used, the return value can also be processed in the promise. For details about the result codes, see [Result Codes for Unregistering an Observer](#result-codes-for-unregistering-an-observer).

**ErrorObserver APIs**

| API | Description |
| :-- | :-- |
| onUnhandledException(errMsg: string): void | Called when an uncaught exception is reported after the application is registered. |
| onException?(errObject: Error): void | Called when an application exception is reported to the JavaScript layer after the application is registered. |

**LoopObserver APIs**

| API | Description |
| :-- | :-- |
| onLoopTimeOut?(timeout: number): void | Called when the message processing of the main thread times out. |

## Result Codes for Unregistering an Observer

| Result Code | Description |
| :-- | :-- |
| 0 | Normal. |
| \-1 | Input **number** not exist. |
| \-2 | Invalid parameter. |

#### How to Develop

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/JuVbogCRRCq3DoDYBmFSlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68C8D26F759C4B018BBFAC88A6D1EFE5E421AADDB0E5BFEE25C01A83C7F6F485)

You are advised to add a synchronous exit operation at the end of the exception callback to prevent multiple exception callbacks.

## Single Thread Listening

Import the header files.

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

Add an observer.

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('testErrorManage','onUnhandledException, errorMsg: ', errorMsg);
  },
  onException(errorObj) {
    console.error('testErrorManage','onException, name: ', errorObj.name);
    console.error('testErrorManage','onException, message: ', errorObj.message);
    if (typeof(errorObj.stack) === 'string') {
      console.error('testErrorManage','onException, stack: ', errorObj.stack);
    }
  }
};

Add a trigger button.

Button('Single thread listening').onClick(()=>{
  let observerId = -1;
  try {
    observerId = errorManager.on('error', observer);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error('testErrorManage',\`error: ${code}, ${message}\`);
  }
  // Construct a fault scenario.
  throw new Error('test errorObserver msg');
}).position({x:50, y:50});

## Process Listening Exception

Import the header files.

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

Add an observer.

function errorFunc(observer: errorManager.GlobalError) {
  console.error('testErrorManage','result name :' + observer.name);
  console.error('testErrorManage','result message :' + observer.message);
  console.error('testErrorManage','result stack :' + observer.stack);
  console.error('testErrorManage','result instanceName :' + observer.instanceName);
  console.error('testErrorManage','result instanceType :' + observer.instanceType);
};

Add a trigger button.

Button('Process listening exception').onClick(()=>{
  try {
    errorManager.on('globalErrorOccurred', errorFunc);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error('testErrorManage',\`error: ${code}, ${message}\`);
  }
  // Construct a fault scenario.
  throw new Error('test errorFunc msg');
}).position({x:50, y:100});

## Process Promise Exception

Import the header files.

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

Add an observer.

function promiseFunc(observer: errorManager.GlobalError) {
  console.error('testErrorManage','result name :' + observer.name);
  console.error('testErrorManage','result message :' + observer.message);
  console.error('testErrorManage','result stack :' + observer.stack);
  console.error('testErrorManage','result instanceName :' + observer.instanceName);
  console.error('testErrorManage','result instanceType :' + observer.instanceType);
};

async function promiseFuncOne() {
  throw new Error('process promise exception');
};

Add a trigger button.

Button('Process promise exception').onClick(()=>{
  try {
    errorManager.on('globalUnhandledRejectionDetected', promiseFunc);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error('testErrorManage',\`error: ${code}, ${message}\`);
  }
  // Construct a fault scenario.
  new Promise<string>(() => {
    promiseFuncOne();
  }).then(() => {
    throw new Error('test promiseFuncOne msg');
  });
}).position({x:50, y:200});

## Main Thread Freeze Exception

Import the header files.

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

Add an observer.

function freezeCallback() {
  console.error('testErrorManage','freezecallback');
};

Add a trigger button.

Button('Main thread freeze exception').onClick(()=>{
  try {
    errorManager.on('freeze', freezeCallback);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error('testErrorManage',\`error: ${code}, ${message}\`);
  }
  // Construct a fault scenario.
  let date = Date.now();
  while (Date.now() - date < 15000) {
  };
}).position({x:50, y:300});

## Main Thread Message Processing Timeout

Import the header files.

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

Add an observer.

let loopObserver: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.error('testErrorManage','Duration timeout: ' + timeout);
  }
};

Add a trigger button.

Button('Main thread message processing timeout').onClick(()=>{
  try {
    errorManager.on('loopObserver', 1, loopObserver);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error('testErrorManage',\`error: ${code}, ${message}\`);
  }
  // Construct a fault scenario.
  let date = Date.now();
  while (Date.now() - date < 4000) {
  };
}).position({x:50, y:150});

## Process Promise Observer Registration Rejected

Import the header files.

import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

Add an observer.

let promise1 = new Promise<void>(() => {}).then(() => {
  throw new Error('uncaught error');
});

let unhandledrejectionObserver: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
  if (promise === promise1) {
    console.error('testErrorManage','promise1 is rejected');
  }
  console.error('testErrorManage','reason.name: ', reason.name);
  console.error('testErrorManage','reason.message: ', reason.message);
  if (reason.stack) {
    console.error('testErrorManage','reason.stack: ', reason.stack);
  }
};

async function promiseFuncTwo() {
  throw new Error('process promise unhandled rejection exception');
};

Add a trigger button.

Button('Process promise observer registration rejected').onClick(()=>{
  try {
    errorManager.on('unhandledRejection', unhandledrejectionObserver);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error('testErrorManage',\`error: ${code}, ${message}\`);
  }
  // Construct a fault scenario.
  new Promise<string>(() => {
    promiseFuncTwo();
  }).then(() => {
    throw new Error('test promiseFuncTwo msg');
  });
}).position({x:50, y:250});

## Chaining Error Handlers

Define the first error handler and register the method. If no pre-handler is available, the process exits.

import { errorManager } from '@kit.AbilityKit';
import { process } from '@kit.ArkTS';

let firstHandler: errorManager.ErrorHandler;
const firstErrorHandler: errorManager.ErrorHandler = (reason: Error) => {
    // Implement the logic of the first custom error handler.
    console.info('\[FirstHandler\] First uncaught exception handler invoked.');
    if (firstHandler) {
        firstHandler(reason);
    } else {
        // You are advised to add a null check. If the value is null, use a synchronous exit approach.
        const processManager = new process.ProcessManager();
        processManager.exit(0);
    }
};

export function setFirstErrorHandler() {
    firstHandler = errorManager.setDefaultErrorHandler(firstErrorHandler);
    console.info('Registered First Error Handler');
}

Define the second error handler and register the method to implement a chain call.

import { errorManager } from '@kit.AbilityKit';
import { process } from '@kit.ArkTS';

let secondHandler: errorManager.ErrorHandler;
const secondErrorHandler: errorManager.ErrorHandler = (reason: Error) => {
    // Implement the logic of the second custom error handler.
    console.info('\[SecondHandler\] Second uncaught exception handler invoked.');
    if (secondHandler) {
        secondHandler(reason);
    } else {
        const processManager = new process.ProcessManager();
        processManager.exit(0);
    }
};

export function setSecondErrorHandler() {
    secondHandler = errorManager.setDefaultErrorHandler(secondErrorHandler);
    console.info('Registered Second Error Handler');
}

Import the header files.

import { setFirstErrorHandler } from './FirstErrorHandler';
import { setSecondErrorHandler } from './SecondErrorHandler';

Add the constructor for chaining error handlers.

function testErrorHandlers() {
  setFirstErrorHandler();
  setSecondErrorHandler();
  throw new Error('Test uncaught exception!');
}

Trigger the test through the button for the main component, register two handlers, and throw an error to verify the handler chain.

Button ('Chaining error handlers').onClick(()=>{
  testErrorHandlers();
}).position({x:50, y:350});
